label mollycafe:
    if molly_love >= 0 and mollycafe1 == False:
        jump mollycafe1
    if molly_love >= 5 and mollycafe1 == True and mollycafe5 == False:
        jump mollycafe5
    if molly_love >= 10 and mollycafe5 == True and mollydorm5 == True and mollycafe10 == False:
        jump mollycafe10
    if molly_love >= 15 and christmas7 == True and mollycafe15 == False:
        jump mollycafe15
    if molly_love >= 20 and mollycafe15 == True and mollydorm15 == True and mollycafe20 == False:
        jump mollycafe20
    if molly_love >= 25 and tsuneyodorm25 == True and rindorm50 == True and day > 5 and mollycafe25 == False:
        jump mollycafe25
    if molly_love >= 30 and nikilovesyou3 == True and otohaspecial15p2 == True and day == 5 and mollycafe30p1 == False:
        jump mollycafe30p1
    if mollyspring2 == True and day == 2 and harukasex == True and harukaspring1miss == False and harukaspring1 == False:
        jump harukaspring1
    if chap4active == True:
        jump mollyspringcafegen
    if chapthreeactive == True:
        jump mollysummer2cafegen
    if christmas7 == True:
        jump mollynightgen2
    else:
        jump mollycafegen

label mollyinvite:
    if mollyinvite1 == False:
        jump mollyinvite1
    if mollyinvite1 == True and mollyinvite2 == False:
        jump mollyinvite2
    else:
        jump mollyinvitegen

label mollyinvitegen:
    play sound "phonebeep.wav"

    "I tap on Molly's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    mo "Greetings, Sir! To what or whom do I owe the pleasure?"
    s "To me. But you owe it in person and this phone call is me asking you to come do that."
    mo "You want me to come do you?"
    s "Or just come over. Whichever is easier."
    mo "It's difficult to do anyone if you can not physically touch them, Sir. Technology has advanced quite a bit, but-"
    s "Are you coming or not?"
    mo "Aye aye! I'm on my way!"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene mollyinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    mo "Tell me, Supreme Overlord...what does fate have in store for us today?"

    "How should I spend my time with Molly?"
    menu mollyinvmenu:
        "Hang Out (Raise Affection)":
            jump mollyinviteaff
        "Cunnilingus (Raise Lust)":
            jump mollyinvitecun
        "Headpat":
            jump mollyheadpat

label mollyinviteaff:
    scene mollyinvitegen
    with fade

    "I decide to give Molly free {b}reign{/b} of what we're going to do today and I don't think I've ever regretted anything so immediately before."
    "She quickly summons me over to the computer and, after convincing her to avoid my porn folder (which is becoming customary any time someone else uses it), she opens up Youtube."
    "And while she states that the purpose of such a thing is to educate me about upcoming games in an attempt to pique my interest, it turns out to be anything but."
    "What it {i}does{/i} wind up being, however, is a great opportunity for her to argue with people who do not share her opinion in the comment section. Under my usernames, of course."
    "I somehow am both proud and disappointed at the same time. Especially since I feel like she is using my account to agree with her own comments."

    scene black
    with dissolve2

    "Eventually, I manage to convince her to do something else and, after informing her that she can not download any games, we wind up moving the laptop over to the bed and watching some movie instead."
    "She does not masturbate this time. And I don't either."
    "Which means that today is both successful {i}and{/i} unsuccessful at once."

    $ molly_love += 3
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]!{/i}"

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

label mollynightgen2:
    scene mollynightgen2
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe to find Molly slacking off the same way she always does."
    "Why Haruka continues to allow her to run this place at night is beyond me, but I guess as long as she remains upbeat and energetic, no one is going to complain."
    "The only people who show up to coffee shops around this time of night have problems anyway, so it's not like they're coming in here expecting a life-changing experience."
    "They just want caffeine."
    "Kind of like how Molly only wants guild members."
    "I know this because she mentions it probably seven different times over the course of the night."
    "But, miraculously, I manage to avoid becoming annoyed by it. I think I might even be developing some sort of resistance to her."
    "Soon enough, I might even be able to translate her sentences the same way Rin does."
    "One can only hope, I guess."

    scene black
    with dissolve

    "Once it comes time for the store to close, Molly begins to say goodbye."
    "But, defying all expectations of me, I offer to help her clean up the store for a little while."
    "She lets out a shockingly loud cry of victory when she realizes this will cut roughly ten minutes off of her closing time and quickly fetches me a broom."
    "I sweep for five minutes before realizing I hate this and leave without saying anything."
    "Sorry, Molly."
    "This is your fault for trusting me."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafegen:
    scene mollyphonegame6
    with dissolve
    play music "cafe.mp3"

    "I arrive at the cafe to find Molly at her usual table, playing some game on her phone."
    "I initially think that she's just on break or something judging by the food and coffee in front of her, but quickly find out that this is not the case."
    "Apparently, this is just what a normal work day is for Molly."
    "The two of us get to talking more about how much she enjoys the cafe and her hobbies outside of this place and I quickly begin to question whether I am in the right line of work or not."
    "I wonder if I would still be able to support myself and Ami if I quit teaching and started working nights here instead?"

    scene black
    with dissolve

    "That dream fades as soon as Molly brings up her minimum-wage pay and I, once again, resign myself to a life of being surrounded by cute girls and notebooks rather than cute girls and coffee."
    "But hey, either way, there are cute girls involved and that's more than most people can say about their jobs."
    "Time passes and Molly finally realizes that she actually has things to do before heading home."
    "I let her get back to her responsibilities and decide to head back home and get some sleep..."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "... "

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label callmollymorning:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if mollysad == True:
        s "..."
        s "No."
        jump callmorning
    if chap4active == True:
        jump mollyspringmorninggen

    play sound "phonebeep.wav"

    "I tap on Molly's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    "I guess she's still asleep."
    "Who should I call instead?"

    jump callmorning

label callmollyafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if mollysad == True:
        s "..."
        s "No."
        jump callafternoon

    play sound "phonebeep.wav"

    "I tap on Molly's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    mo "Top o' the mornin' to ya, Sir!"
    mo "Well, afternoon I suppose."
    mo "Top o' whatever time it is right now! The lack of sunlight has propelled my world into a never ending spiral of darkness and-"
    s "Yeah, yeah. Are you free right now?"
    mo "Right now? I'm afraid not, Sir. These are gaming hours."
    s "Aren't all hours for you gaming hours?"
    mo "Exactly! I knew you'd understand, Sir!"
    s "..."
    mo "If you don't mind waiting for me to finish these next twenty mount-runs or so, I can try to-"

    play sound "phonebeep.wav"

    "Knowing that Molly is busy and won't be able to hang out this afternoon, I decide to call someone else instead."

    jump callafternoon

label callmollynight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if mollysad == True:
        s "..."
        s "No."
        jump callnight

    if cafeclosed == False:
        "Molly is working right now."
        "If I want to see her, I should head over to Koi Cafe."
    else:
        play sound "phonebeep.wav"

        "I tap on Molly's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "...but she doesn't."

    jump callnight

label mollycafe1:
    scene cafe_night
    with dissolve
    play music "cafe.mp3"

    "I decide to check out the cafe at night for once."
    "I’ve known that they’re open later than just mornings for quite a while, but I guess I really haven’t had any reason to go knowing that Rin wouldn't be working."
    "But hey, this is a cafe."
    "I’m sure there’s bound to be another overly-perky, slightly-weird girl behind the counter no matter what."

    scene mollycafe1
    with dissolve

    mo "Greeting and salutations, Supreme Overlord!"
    s "Oh, right. You work here."
    mo "I do! Though, some of my co-workers may disagree with that statement!"
    mo "What can I get for you today, Sir? A cappuccino? Double espresso? Or perhaps..."

    scene mollycafe2
    with dissolve

    mo "DESTRUCTION?!"
    s "Yes, Molly. One order of destruction."
    mo "Small, medium, or THE GATES OF HELL?"
    s "How much coffee have you had to drink tonight?"

    scene mollycafe3
    with dissolve

    mo "I CAN’T EVEN FEEL MY HANDS ANYMORE!"

    "I guess it’s not surprising that Molly works here..."
    "Her and Rin seem like pretty good friends, so I’m sure that them being together all the time has something to do with that."
    "Still, though...why did Haruka hire {i}Molly{/i} of all people? Isn’t she a little too...{i}everything{/i} for this place?"

    s "Molly, just out of curiosity, how do you still have a job?"

    scene mollycafe4
    with dissolve

    mo "That question would be better answered by the Magistrate of Mammaries, Sir. Though, I'm sure Rin has something to do with it."
    mo "I'm sure it helps that I only work nights now and no one has to deal with me directly anymore."
    mo "I'm surprised to see you here so late, though. I was under the impression you only showed up in the mornings- and quite often at that!"
    s "How exactly do you know about how often I come here if you don't directly work with Haruka or Rin anymore?"

    scene mollycafe5
    with dissolve

    mo "I may have mentioned something along the lines of a...contract with a new master in our group chat. Which then evolved into a conversation about you. "

    "Oh, good. A private group chat where three girls I see on a near daily basis are free to gossip about me. That is exactly what I needed."

    s "I'm guessing that means Haruka knows you're in my class now?"
    mo "Well, I didn’t exactly word it like that, but yes. I believe that is the impression she got."

    scene mollycafe4
    with dissolve

    mo "Can I take this visit as an omen that you will be visiting me at night more often, Sir? "
    mo "Not that...you can visit me in the mornings on account of the whole {i}how hard I am to handle{/i} thing."
    s "To be completely honest, you don’t seem any easier to handle at night."
    mo "You’re just not a high enough level yet, Sir."
    mo "I can't be equipped until much later into the game."

    if bonus == True:
        s "I really hope that’s not foreshadowing."
        mo "I don’t...think it is?"
        mo "It's probably just gamer-brain, Sir. You know- like items, skill levels, party members...etcetera, etcetera."
        mo "Just assume that it's stuff you don’t care about that I am going to {i}make{/i} you care about."
    else:
        s "Stop hinting at a future for us. I am your teacher and that is disgusting."
        mo "I will make you mine through methods unknown to mere mortals."

    s "And how do you plan on doing that, exactly?"

    scene mollycafe5
    with dissolve

    mo "Mind control, perhaps? "
    mo "Or maybe I’ll just win you over with my feminine wiles?"
    s "What wiles? You haven’t done a single {i}feminine{/i} thing since I’ve met you."

    scene mollycafe1
    with dissolve

    mo "I don’t know! Foreigners are appealing to men, aren’t they?"
    mo "And now that we’re alone, I bet you’re thinking something like, “WOW, WHAT A CUTE GIRL” or whatever it is h-game protagonists think."
    s "Not really. I'm still stuck on trying to figure out why you haven't been fired yet."

    scene mollycafe6
    with dissolve

    mo "I’m plenty good at my job!"
    s "We've been talking for five minutes and you haven't even finished taking my order yet."
    mo "I just like talking and I’m excited to see my teacher after school!"
    mo "Ms. Watabe never came to the cafe! She always talked about how tea was better and that coffee was just hot bean water!"
    mo "And any time I tried to tell her we had tea as well, she told me to leave her alone and that she just wanted to die!"
    s "Huh. Coffee really is just hot bean water, isn't it?"

    scene mollycafe7
    with dissolve

    mo "Well...yes. I believe it is. But it’s good for other stuff too. Like when you need to stay up late....{i}studying{/i} and stuff."
    s "Molly, please don’t feel the need to pretend you study around me. I might be your teacher, but it’s not like I have any intention of-"
    s "Well, teaching."

    scene mollycafe2
    with dissolve

    mo "Fuck yeah!"
    mo "Ami was right when she said you were the best [uncle] in the world!"
    mo "Will you be my [uncle] too, Sir?"
    s "I don’t think that’s possible."
    mo "Then will you adopt me and become my new father?!"
    mo "I’m not good at cooking or cleaning, but I’m certain I would make decent company on a rainy day!"
    s "I'm not really looking to adopt right now. Nor do I think Ami would be okay with it."
    s "I know you guys are in the manga club together, but she hasn’t ever really talked about you before and I doubt she views you as a sister."

    scene mollycafe8
    with dissolve

    mo "Ami hasn't talked about me before?!"
    s "Is that really something to yell about?"
    mo "Of course! Ami is a loyal member of the Cult of Molly! "
    mo "We have plans to conquer the demon king and restore order to the forest one day!"
    s "You’re really going to need to learn to talk about things I actually understand if this relationship is ever going to work out."

    scene mollycafe9
    with dissolve

    mo "Oh ho ho ho~ So you accept my contract after all?"
    s "Contract? What contract?"
    mo "You just said we’re in a relationship. "
    mo "And even if it were a slip of the tongue, these are words that will greatly shape the rest of our time together, Supreme Overlord."
    mo "If Molly MacCormack is to become the lead heroine of this visual novel, hearing things like “relationship” only allude to its truth!"
    s "Just out of curiosity, you haven't heard anything about how much time I’ve spent with the other students, right?"
    s "Because you seem pretty dead-set on this whole heroine thing and I’m not quite sure if you fully understand what you're getting yourself into."
    mo "Oh ho ho~ You underestimate me, Sir."
    mo "I just so happen to be an expert in the world of dating sims. "
    s "But not...actual dating? Why choose to live a life like that when real humans exist?"

    scene mollycafe10
    with dissolve

    mo "You don’t choose 2D, Sir. 2D chooses you."

    scene mollycafe2
    with dissolve

    mo "But even if it didn’t, I would have wound up here eventually!"
    mo "There’s nothing quite like watching romance flourish from textbox to textbox. H-Scene to H-Scene!"
    s "Would you mind explaining to me what some of those things mean? Because I feel like I need to understand what an “H-Scene” is if I'm ever going to catch up with this conversation."

    scene mollycafe11
    with dissolve

    mo "The “H-Scene” is the holy grail of dating sims, Sir!"
    mo "The moment where two characters consummate their love for another in the form of...{i}you know what{/i}."
    s "..."
    mo "..."

    if bonus == True:
        s "You mean sex?"
    else:
        s "You mean by throwing peanuts at each other and pretending it was an accident?"

    scene mollycafe12
    with dissolve

    mo "..."
    mo "Yup!"
    s "So, let me get this straight-"
    s "You would willingly choose a life where the only physical contact you have with anyone is done through a computer screen with a fictional character?"

    scene mollycafe13
    with dissolve

    mo "..."
    s "..."
    mo "You don’t get it at all."
    mo "It’s not just about the physical part, Sir. "
    mo "It’s about the emotions leading up to it! The build-up! The will-they, won’t-they!"
    s "That exists in real life too, though."

    scene mollycafe14
    with dissolve

    mo "REAL LIFE IS STUPID! THERE’S NO BACKGROUND MUSIC OR TSUNDERE CHARACTERS! JUST NTR AND PREGNANCY!"
    s "And what is NTR exactly?..."
    mo "HORRIBLE! THAT’S WHAT!"

    "I can feel passion and anger beginning to exude from Molly’s being, turning the cafe roughly three degrees hotter."
    "And in other news, we are now roughly ten minutes into this and I still do not have a drink in my hands."

    s "Uhh, Molly."
    mo "What do you want?! I’m having a crisis and remembering a thing that happened in a game I played!"
    mo "NTR warnings should be mandatory! Not everyone is into that! It genuinely hurts some people!"
    s "Molly, I would like to order a drink now."

    scene mollycafe15
    with dissolve

    mo "Oh, right. I’m at work. "
    mo "What would you like? It’s on me today."
    s "Woah, really? Rin never offers to give me anything for free and I’ve been ordering from her for months."
    mo "Rin is much better at her job than I am."
    mo "It is not often I form connections with live males, so I must do everything in my power to keep this one going strong."

    if bonus == True:
        mo "Even if you are three times my age."
        s "Okay, come on. I’m definitely not three times your age."

        scene mollycafe16
        with dissolve

        mo "Okay! {i}Four{/i} times my age!"
        s "How old do you think I am?..."
        mo "Old enough that my father would disown me for becoming romantically involved with you!"
        s "Okay, fair point. Let’s avoid that for the indefinite future as I have no intention of literally ever meeting your father."
    else:
        s "The best course of action would be for me to meet your father and inform him that my intentions are nothing but pure."

    mo "That is fine with me, Sir!"
    mo "I believe it is customary for me to meet {i}your{/i} parents, though."
    mo "It would make for a heartwarming scene where I bond with your mother and cook dinner with her."
    s "That sounds...great. But I honestly don’t even know if my parents are still alive."

    scene mollycafe17
    with dissolve

    mo "Oh! Shoot. I’m sorry, Sir. I didn’t mean anything by it. I just got swept up in my-"
    s "It’s fine, Molly. Don’t beat yourself up over it. I really couldn’t care less, to be honest."

    scene mollycafe18
    with dissolve

    mo "But that’s so sad..."
    s "Yeah, that's life for you."
    s "We’re all going to die someday, so we might as well live it up while we can, right?"

    scene mollycafe19
    with dissolve

    mo "Master!"
    s "...What?"
    mo "Thank you!"
    s "What’s going on? Why are you thanking me?"
    mo "That was just the inspiration I needed to convince myself to level-cap my druid tonight!"
    s "Your...what?"
    mo "That doesn’t matter!"
    mo "Just know that I greatly appreciate it!"
    s "Okay, but can I-"
    mo "Coffee! Yes! I will infuse it with a special buff just for you as well!"
    s "I’m not really a fan of sugar-"

    scene mollycafe3
    with dissolve

    mo "ONE MOLLY-SPECIAL, COMING RIGHT UP!"

    scene black
    with dissolve2

    "As it turns out, it isn’t just Rin who vehemently refuses to make anything that is actually on the menu here."
    "The only difference is that Rin’s custom drinks are actually fit for human consumption."
    "And I’m pretty sure that whatever Molly winds up making for me contains cocaine, because I wind up walking home with my hands shaking uncontrollably after just one sip..."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe1 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "... "

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe5:
    scene cafe_night
    with dissolve
    play music "cafe.mp3"

    "I decide to spend another night at the cafe and see what Molly is up to."
    "I wound up getting sidetracked along the way, so I’m a little later than normal, but they’re still open by the time I get there, so...at least that's good."
    "After stepping closer to the counter and realizing there isn’t anyone behind it, however, I begin to wonder if I'm a little too late after all and that...Molly just forgot to lock the doors or something."
    "That seems like a thing she would do."
    "But just as I'm about to leave, I hear some strange sound effects coming from the corner of the room..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mollyphonegame1
    with dissolve2

    "I take a step closer to the sounds to find none other than my favorite Irish student (Out of one total) tapping away at what I imagine is a game on her phone."
    "She’s humming happily along with the song that's playing and is so wrapped up in it that she doesn’t even notice I’m here."
    "Would this be cause for concern if I were an actual customer? Of course. "
    "But I’m not, so I suppose I'll continue letting her do her thing until she notices me."

    mo "Hmm hm hmmm. Hm hmmm hmm hmmm~"
    s "..."
    mo "Hmmmm hm HMMMM. HMMM hmm HMMM~"
    s "..."
    mo "HMMMMMM HMM HMM HMM HMMMHMMMM~"

    "The song picks up the pace and Molly’s fingers begin to dance quicker across the screen."
    "This must be one of those rhythm game things I’ve heard Ami talking about in the past."
    "And even though Molly seems to be having a good time, I’m not sure if I want to just stand here and watch her for the next...however long I’m going to be here for."

    s "Molly."

    scene mollyphonegame2
    with hpunch

    mo "AH! I DIDN’T DO IT, I SWEAR!"
    s "...Didn’t do what?"

    scene mollyphonegame3
    with dissolve

    mo "Oh. It’s you."
    mo "Top o’ the mornin’, Sir."
    s "It’s the middle of the night. And stop saying “Top o' the mornin'” just because you’re Irish. It’s cliche."

    scene mollyphonegame4
    with dissolve

    mo "I had to say it at least once, Sir. I think it's some sort of...unwritten rule for Irish characters."
    s "Anyway, what are you up to? Playing a game?"

    scene mollyphonegame5
    with dissolve

    mo "I {i}was{/i} in the middle of a full combo until you decided to show up and scare the pants off of me."
    s "Your pants are very much on right now."
    mo "My metaphorical pants. The ones I wear over my normal pants. They only come off when I get scared."
    s "Molly, you’re a really weird girl. You know that, right?"

    scene mollyphonegame6
    with dissolve

    mo "Yes! I've been being reminded for as long as I can remember. But that’s what makes me so lovable!"
    mo "Besides, you’re pretty weird yourself. Aren’t you, Sir?"
    s "In what way?"
    mo "I used 'Detect Thoughts' on you when you weren’t paying attention in class the other day."

    if bonus == True:
        mo "You think about some pretty unsavory things, Sir."

    "As much as I want to say that the sort of magic Molly is referring to is impossible, I literally watched a girl her age reset the world a little while ago."
    "So I guess nothing is off limits, really."
    "But either way, I doubt Molly has actual mind-reading powers and that this was probably just a lucky guess."
    "If she {i}actually{/i} had mind-reading powers, she would know that I've been picturing her without her clothes on this entire time."

    s "Okay, Molly. If you’re so smart, what am I thinking right-"

    scene mollyphonegame7
    with dissolve

    mo "You really want me to say it, Sir?"
    mo "What if the security cameras in here record audio? You could get in a loooooooot of trouble~"
    s "..."
    mo "..."

    "I'm just going to assume that she's only able to successfully guess these things because I am a generally creepy person."

    s "As a growing boy, I believe I should be forgiven for all of the impure thoughts plaguing my mind."

    if bonus == True:
        scene mollyphonegame8
        with dissolve

        mo "That can't be true, Sir. You should have stopped growing a long time ago. "
        mo "Even I am barely growing at this point and you’re much older than I am."
        s "It was a joke, Molly. Now, I only grow when I get excited."

        scene mollyphonegame9
        with dissolve

        mo "Ahh! Penis joke!"
        mo "I’ve read enough eroge to know what you mean by that!"
        s "Oh, right. I forgot that you were an expert in all things depressing."
        mo "What’s so depressing about spending hundreds, if not thousands of hours seducing fictional characters?!"
        mo "It's all of the fun with none of the cleanup!"
        s "Cleanup?..."

        scene mollyphonegame10
        with dissolve

        mo "Bodily fluids! Scrunched up tissues! Messy hair! The whole kitten caboodle!"
        s "Wow. Your mind is even further gone than I thought."
        mo "You’re the one who asked, Sir! Don’t pretend you don’t know what I’m talking about!"

        scene mollyphonegame11
        with dissolve

        mo "Besides, who even cares if somebody is into that kinda stuff? It’s not like 2D romance hurts anybody."
        s "I know that. You can be into whatever you want to be into. I’m just messing around with you."
        s "Do I think it's depressing? Yes. But I'm not about to stand between you and whatever weird fetishes you have."
    else:
        mo "Yes you are, and I am very proud of you."
        s "Thank you, Molly. You always know how to turn my frown upside down."

    scene mollyphonegame12
    with dissolve

    mo "Thank you, Sir! Appreciated! I was worried we were about to reach a bad end!"
    s "A bad end this early in your story would be really unfortunate."
    mo "Reviews would plummet. I can hear it now..."
    mo "“This game is too hard! How do I escape the time loop?! Where is the walkthrough?!”"
    s "I’m not sure what any of that means, but I doubt there’s anyone out there who’d be so detached from reality that they’d complain about something like that."

    scene mollyphonegame13
    with dissolve

    mo "You clearly haven’t spent enough time on the Internet."
    s "No, I really haven’t."
    mo "It’s a freakin’ battlefield out there, Sir. "
    mo "Bodies scattered across the plains...The remnants of forgotten memes, desperately clawing their way out of the depths of the Earth..."
    mo "It is literally Hell. And I haven't even told you about Twitch chat yet."
    s "Well then, why do you spend so much time on the Internet if it's that horrible? Wouldn’t it be better to go out and do, you know, real-life stuff?"

    scene mollyphonegame14
    with dissolve

    mo "Real life is hard..."
    mo "The progression system is hidden...and you can’t even check your affection scores with everyone."
    mo "You’ve actually gotta think about stuff...and I've never been good at that."

    scene mollyphonegame8
    with dissolve

    mo "You know, Sir- I read in one game that life is like a staircase. You’ve just gotta keep on climbing."
    mo "Otherwise, if you start to overthink it, you’ll have trouble taking the next step."

    scene mollyphonegame15
    with dissolve

    mo "But to that, I pose a follow-up question!"

    "A fire ignites within Molly’s eyes as she so passionately adds to the quote she just mentioned."
    "Like, a literal fire. There’s actual fire in her eyes. It’s terrifying."

    mo "What that quote does not take into mind is the existence of the escalator!"
    mo "There is a way to live life without climbing up anything!"
    mo "It is possible to rise by just standing still and waiting for everything to pass by you!"
    mo "Is it fulfilling? No! But if you wind up at the same place, it’s much more economical!"

    scene mollyphonegame16
    with dissolve

    mo "And so I, Molly MacCormack, have vowed to live a life on the escalator."
    mo "Who needs stairs when ANYTHING can be stairs?! THE WORLD IS MY STAIRCASE!"
    s "Is it hot closing your eyes with fire still inside them?"
    mo "It burns with the white hot intensity of a thousand suns."
    s "Then open them back up."
    mo "The flames have sealed my skin shut. I shall never see again."
    mo "Please cast 'Cure Wounds' as a third level spell on me, Sir."
    s "I...don’t know how to do that."
    mo "Just touch my head. I’ll act out the rest."
    s "I can’t touch your head until we reach the $5k stretch goal."
    mo "We hit that goal a long time ago, Sir. That line should have been changed with the revamp."
    s "Okay, but I'm still not touching your head. I don't know where it's been."
    mo "Life truly can be cruel sometimes."
    s "It really can."

    scene mollyphonegame7
    with dissolve

    mo "Regardless, I shall persevere. Even in the face of adversity, I shall not falter! I shall not admit defeat at the hands of life itself!"

    scene mollyphonegame12
    with dissolve

    mo "And also because...I'd be letting you down, too..."
    s "..."
    mo "..."

    scene mollyphonegame6
    with dissolve

    mo "How was that? Did I sound like a real character in a dating sim, Sir? "
    mo "Have I advanced to the lead heroine role yet?"
    s "For someone who isn’t interested in live humans, you certainly seem pretty set on becoming an actual love interest. "
    mo "Just in the metaphorical sense. I would be a horrible girlfriend if it actually came down to it."
    s "Why do you say that? You’re weird, but I think you’d be fine if you found the right partner."

    scene mollyphonegame12
    with dissolve

    mo "Thank you, Sir! Please ignore my face if it suddenly changes colors! This always happens when I receive compliments from those I admire!"
    s "You admire me?"

    scene mollyphonegame15
    with dissolve

    mo "Of course I admire you!"
    mo "From the moment I first laid eyes on you, I knew our contract would be one strong enough to outweigh the prying eyes of any non-believer!"
    mo "Together, you and I can weed out the darkness...and bring light back to this dying world!"

    scene mollyphonegame9
    with dissolve

    mo "Oh! But I raid with my guild on Tuesdays and Wednesdays, so we’ll have to weed out the darkness on the other five days of the week instead."
    mo "If that's okay with you, I mean."
    s "Sure, Molly. We can weed out the darkness whenever your schedule allows for it."

    scene mollyphonegame15
    with dissolve

    mo "Excellent!"
    mo "Thank you for understanding and accommodating my hours of availability."
    mo "Now, if you would also be willing to postpone the start of[school] for several hours so I can sleep in-"
    s "Changing[school] hours isn’t really something I’m allowed to do. I would have done that a long time ago if it was."

    scene mollyphonegame5
    with dissolve

    mo "I figured...It was worth a shot, though..."

    scene mollyphonegame6
    with dissolve

    mo "I already like you more than Ms. Watabe anyway, so there’s not really any point in complaining."
    mo "Plus, I already had some friends in your class, so everything's coming up Molly!"
    mo "I just need to work on getting Tsuneyo to like stuff other than noodles and I’ll have pretty much everything I’ve ever wanted."
    s "Pretty much? What else are you missing?"
    mo "A life-sized, realistic statue of my waifu that I can hug before I go to bed at night."
    mo "And an RTX 3080."
    mo "That line didn't even need to be changed since they're still basically unavailable everywhere."
    s "A...what?"
    mo "It doesn’t matter!"
    mo "The point is, as long as the bond between us is not severed, I feel as if all of my dreams will come true!"
    mo "Please do not abandon me! I need you!"
    mo "Think of it like one of those recruitment systems in an MMO where we need to be next to each other to gain an EXP buff!"
    s "Molly, I have no idea what you’re talking about."

    scene mollyphonegame12
    with dissolve

    mo "That’s fine! No one ever does!"
    mo "I’m just happy to have met you! That’s all! Even if you don’t like anime and call me weird all the time!"

    "As always, I have a hard time comprehending what Molly means- but I’m glad that she seems happy at the very least."
    "The truth is, I’m starting to enjoy spending time with her as well. "
    "There are plenty of girls in my life now with a bit more energy than I’m used to..."
    "But I think something about how I {i}never{/i} have any idea what Molly is talking about really...sets her apart from the rest."
    "Now, seeing her in a romantic light is obviously a much different question."
    "Especially when factoring in that I...think she might only be attracted to 2D characters?"

    if bonus == True:
        "But either way, I'm excited to see where this relationship heads..."

    s "I'm happy to have met you too, Molly."
    mo "R...Really?"
    mo "You mean that, Sir?"
    s "Of course. Even if I don't like anime and call you weird all the time."

    scene mollyphonegame11
    with dissolve

    mo "That's totally fine!"
    mo "I won't let you down, Sir! I promise!"

    scene black
    with dissolve2

    "..."
    "You know, maybe this 'contract' thing won't be so bad after all."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe5 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe10:
    scene mollycafe19
    with dissolve
    play music "cafe.mp3"

    mo "And that’s when I was like, “Watch your mouth, lich! You’re messin’ with the wrong priest!”"
    mo "And right before my holy nova went off, a swarm of adds spawned and aggro’ed straight to me so fast that the tank rage-quit on just our third wipe."
    mo "Some people just aren’t meant for progression raiding, you know?"
    s "No."

    "As you can see, I’m caught up in yet another “conversation” with Molly and beginning to question whether or not I will ever be able to talk about things {i}I{/i} like with her."

    if bonus == True:
        "Mind you, the list of things I like is limited to...cute girls, sex, food, and sleep...And maybe those aren’t really the best conversation pieces after all."
    else:
        "Like vanilla ice cream or donating money to various charities."

    mo "Oh well. That’s fine. You don’t really need to get it. I can fill you in on all of the stuff you don’t understand so that when you finally start your free trial, you’ll know the basics."
    s "The basics of what? I don’t have time for video games."

    scene mollycafe6
    with dissolve

    mo "Why do you have so much time to hang out with [teenage]girls but no time to play games?! That doesn’t make any sense!"
    s "I don’t have time to play games because I {i}have{/i} to hang out with [teenage]girls. It is my calling. "
    s "Just like how your calling is guarding emeralds or whatever it is you do."

    scene mollycafe14
    with dissolve

    mo "I don’t guard emeralds! I’m the Emerald Guardian! It is very different!"
    s "So like, you’re...made of emeralds? I’m not really sure what you’re trying to get at here."
    r "Jeez. Give the girl a break, man. She’s just trying to get you interested in her hobbies."
    s "..."

    scene mollysecondcafe1
    with fade

    "I turn around to find both Rin and Futaba waiting behind me in line. "
    "I didn’t even hear the two of them come in."
    "Probably on account of Molly’s obnoxiously loud voice, but still. "
    "If I were her, I’d probably make some comment about their skill in stealth or something along those lines, but I’m-"
    "Wait...why did that thought even occur to me? Have I really been spending so much time with Molly that this is just...the way I think now?"
    "What is happening to me?"

    s "How long have you two been standing there?"
    f "Since the part with the lich. So not that long at all."
    r "Yeah, it’s only been a few-"

    scene mollysecondcafe2
    with dissolve

    r "Hey, wait a minute! What are you doing here so late?!"
    r "You’re supposed to be {i}my{/i} guinea pig! Not Molly's!"
    r "Am I not good enough for you anymore?! Explain yourself, damn it!"
    f "Uh...umm..."
    s "It’s really not what it looks like. I-"

    scene mollysecondcafe3
    with dissolve

    r "Futaba, I’m being cheated on. Hold me."
    f "I’m...a little confused. But I don’t have a problem-"

    scene mollysecondcafe4
    with dissolve

    mo "Oh, such sorrow. Having your favorite customer stolen by a girl with minimal talent who put all of her points into charisma. "
    r "Why are you touching me? I asked for Futaba."
    mo "Because even if we are arch nemeses...I still love you."

    scene mollysecondcafe5
    with dissolve

    f "They’re always like this. Don’t pay it any mind. "
    f "Half of our club meetings are just the two of them arguing about things. I’m sure they’ll be back to normal in no time at all."
    s "You’re in the manga club too, Futaba?"

    scene mollysecondcafe6
    with dissolve

    mo "She’s not just in the club, she’s the vice president of it!"
    s "Wait, really? Who’s the president then?"
    mo "Yours truly!"
    s "Weren’t you just telling me the other day that it was hard for you to even be accepted into the club?"

    scene mollysecondcafe7
    with dissolve

    r "Wait, did you really say something like that? Why?"
    r "We wouldn’t have made you the new president if we didn’t accept you."
    mo "Well...I...uhh..."

    scene mollysecondcafe8
    with dissolve

    mo "Anyway! That's not what we're talking about right now!"
    mo "Sir, do you now understand just how powerful I truly am?! You should be thankful to have such a strong force on your side! Willing to fight tooth and nail for your honor!"
    s "I can assure you that any honor I may have had was lost long, long ago."
    mo "Then we must begin the side quest to track it down at once!"

    scene mollysecondcafe9
    with dissolve

    r "Uhh, can I order a drink or do I need to get back there and make it myself?"
    mo "What would you like to order, miss?"
    r "Quad grande upside down caramel macchiato. Extra caramel. "
    mo "..."
    mo "Black coffee?"

    scene mollysecondcafe10
    with dissolve

    r "Ugh. I’ll just do it."

    scene mollysecondcafe11
    with dissolve

    "Rin breaks free from Molly’s grasp and gets behind the counter to make whatever the hell she just said she wanted."

    mo "As you can see, Sir, I’m pretty horrible at my job."
    s "At least you’re aware of it."
    s "I’m not great at mine either, but it still seems to be working out somehow."
    mo "Aye. Because the two of us are cut from the same cloth! Two peas in a pod! Mercenaries selling ourselves to the highest bidder!"
    f "I’m glad to see the two of you are getting along so well despite only having just met each other recently."
    s "Is that what this is called? Getting along? Because Molly more or less just yells stuff at me every time the two of us are together."
    mo "I yell things at everyone. It is an endearing character trait. "
    s "You should try to be more like Futaba and never yell anything at anyone."

    scene mollysecondcafe12
    with dissolve

    mo "Ah! Oh no! It’s my worst nightmare come to life! "
    mo "You’re into the dandere type, aren’t you, Sir?!"
    s "The what?..."
    mo "Weebnote: Dandere characters are the super quiet, awkward ones with surprisingly cute sides that they break out just to get into your head!"
    mo "It's all a ploy! None of it is real!"
    mo "Fight the moe, Sir! Fight it!"

    if bonus == True:
        mo "All that stuff about them being freaks in the sack is purely fiction! Don't give in!"

        play sound "glass.mp3"
        scene mollysecondcafe12
        with hpunch

    r "Ah! Shit! I dropped my freakin'-"
    r "Molly, what the Hell are you talking about over there?! You know my hands stop working correctly when that sort of stuff comes up!"
    mo "I am sorry, but this is a major crisis! Sensei is about to leave us for Futaba!"
    s "That archetype sounds more like Sana than Futaba, to tell the truth."
    s "Futaba can be a little quiet at times but she’s not ever really {i}awkward.{/i} "

    scene mollysecondcafe13
    with dissolve

    f "I’m...only quiet in school, really..."
    s "That’s true, I guess. You’re actually quite talkative whenever we're in the library."
    s "Which is kind of...the opposite of how you’re supposed to be in the library, now that I think about it."
    mo "Oh! I’m glad the Supreme Overlord brought the library up cause I’ve been meaning to ask you if they have any of the resources I need for our one-shot thingy."
    s "One-shot thingy? What does that mean?"

    scene mollysecondcafe14
    with dissolve

    mo "Oh ho ho~ You want in, Sir? Why didn’t you just say so?"
    s "Probably because I still have no idea what you’re talking about."
    f "She’s talking about...Dungeons and Dragons..."
    f "Molly wants to play when we go on vacation since she can’t spend much time in the sun without getting burnt..."
    mo "Correct-a-mundo, Sword-dancer of the Seven Suns."
    s "Is that your nickname, Futaba? That’s the coolest one yet."

    scene mollysecondcafe15
    with dissolve

    f "You really...think so, Sensei?..."
    f "Hahaha...hah..."
    mo "You see, Sir...I’m gathering up able-bodied men and women to compete in a short-term campaign for one night only in whatever building you decide to keep us in!"
    s "Please don’t make it sound like I’m holding you captive."
    mo "We are {i}all{/i} but prisoners to the protagonist of the game. And that’s you, Sir. You’re the only male character around."
    s "Okay, fine. Whatever. But don’t make it sound like that to anyone who isn’t in the class."

    scene mollysecondcafe16
    with dissolve

    mo "Hehehe~ One male and so many females...all housed in close proximity to one another."
    mo "It’s like something straight out of a nukige."
    s "..."
    s "Can I get another weebnote, please?"

    scene mollysecondcafe17
    with dissolve

    if bonus == True:
        r "It means a game with a lot of sex."
    else:
        r "It means a game with a lot of hugging."

    s "Ahh. That explains why Molly is blushing so much right now."
    r "Futaba is too, I’d wager?"
    s "Yup. Both of them are."
    s "You are too, I think."
    r "Nah, this is just how my cheeks look."
    r "Three blushing girls would be overkill for one scene, dude. Don’t flatter yourself."
    s "Worth a shot."
    mo "A-Anyway! What I’m trying to ask is if you’d maybe want to get in on some of the action, Sir."

    if bonus == True:
        s "..."

        "Is she asking what I think she's asking?"

        s "Hell yeah. Of course I’d-"
    else:
        s "Hell yeah. I've always wanted to try my hand at a tabletop RPG. That sounds really nifty."

    scene mollysecondcafe18
    with dissolve

    if bonus == True:
        r "She means the campaign, Sensei. She’s not inviting you to an orgy."
        s "Oh."
        s "Well that’s significantly less exciting."
    else:
        r "She means the- wait. What?"
        r "I feel like this conversation used to be different."
        s "Shut up, Rin. Get excited."
        r "I mean...I {i}guess{/i} it's kind of exciting?"

    scene mollysecondcafe19
    with dissolve

    if bonus == True:
        mo "It’s plenty exciting! Some would even say it’s {i}more{/i} exciting than an orgy!"
        s "What sort of sad human being would ever say something like that?..."
        mo "I would!"
    else:
        mo "It’s plenty exciting! Some might even say that it's a smashing good time!"
        mo "And by some I mean Nigel Thornberry from the Wild Thornberries! Another character we are now able to reference in this game!"

    scene mollysecondcafe20
    with dissolve

    if bonus == True:
        mo "What would you even do in an orgy with so many people?...There would be like...twelve of us..."
        mo "Who would go first? Who would go last?"
        mo "Where would we put all of our clothes?"
        mo "Would we even {i}bring{/i} clothes?"
        mo "Can the male body even produce that much-"
        s "Okay, Molly. You asked too many questions and Rin is also blushing now. "
        s "Unless that is...also the natural color of her cheeks?"
        r "................................"
        s "Nope, definitely blushing."
        s "Anyway, I can’t say I know what’s going to happen on this “educational field trip,” but I’m almost positive there won’t be an orgy that large. Or even at all, for that matter."
    else:
        mo "Whatever happened to that show?"
        s "I can't say I know what's going to happen on this field trip or whatever, but I'm almost positive that we'll all make it back alive."

    scene mollysecondcafe21
    with dissolve

    f "Ummm...doesn't saying it that way...imply that...it’s possible?"

    "Again, I’ve literally watched this world be reset. Nothing is impossible in my head anymore."

    if bonus == True:
        s "Sure. I mean, who knows when some crazy virus will break out and cause all of the women everywhere to be overcome by lust?"
        s "Look, it's already claimed Rin."

        scene mollysecondcafe22
        with dissolve

        mo "Oh! I’ve played a game like that before!"
        r "{i}All{/i} of the women?..."
        s "You have strange taste in games, Molly."
        s "In fact, you have strange taste in everything."
        mo "My tastes are normal! I swear! I’ll even show you my homework folder to confirm this!"

        scene mollysecondcafe23
        with dissolve

        mo "Ah, wait! No! I should...probably check it first to make sure that all of the...uhh...more questionable material has been erased!"
        s "If you need to check the folder beforehand, I think that says more than enough about whatever {i}questionable content{/i} you're referencing."

        scene mollysecondcafe24
        with dissolve

        r "I mean...I guess {i}I{/i} could always...you know, give it a look...Since I’m an unaffiliated, unbiased party and everything."

        scene mollysecondcafe26
        with dissolve

        mo "Umm...orgy stuff aside, I do need to know if you’re gonna be joining us, Sir. "
    else:
        s "I mean...I guess we {i}could{/i} die. There's no good way of knowing in advance."

        scene mollysecondcafe26
        with dissolve

        mo "Um, all that aside, I do need to know if you’re gonna be joining us, Sir. "

    mo "I’m kind of neurotic when it comes to organizing stuff, believe it or not. So the sooner I know, the better."
    s "Oh. Uhh, well I don’t think I’ll play. But I wouldn’t mind watching you guys, I guess. "
    s "That would probably be fun in a really...different sort of way. "
    mo "Are you sure, Sir? It’s a load of fun. Two loads even. So many loads that you won’t even know where to put everything."
    r "So...many loads..."
    f "You word things very strangely sometimes, Molly..."
    s "She words things very strangely all the time."

    scene mollysecondcafe27
    with dissolve

    mo "And yet you still visit me at night!"
    f "Well...are you really sure he's here to see you and that...he didn’t just come for...a pastry or something?..."
    mo "Molly MacCormack is sweeter than any pastry, Sword-dancer. She is the main course and everyone else is just an appetizer."
    s "It's really impressive how you can be so weird {i}and{/i} conceited at once."

    scene mollysecondcafe29
    with dissolve

    mo "Why wouldn’t I be? Peak Molly-moments always happen when I’m surrounded by my friends! "
    mo "I’ve gotta hype myself up so I don’t fall behind them and wind up as nothing more than a girl passing by in the end credits."
    mo "The lead heroine always has to leave a lasting impression, Sir. Which is exactly why I need to remind you all the time about how awesome and powerful I am!"
    mo "And you’ll get to see that power in full-display come time for vacation! Even {i}if{/i} I need to hide my sensitive Irish skin from the sun during daylight!"
    s "I’m sure I will, Molly...I’m sure I will."

    scene black
    with dissolve2

    "The four of us hang out at the cafe for another hour or two until it comes time to close up shop."
    "I’m honestly surprised that Haruka trusts Molly enough to close this place on her own."
    "But I guess just being overly-spontaneous and hyper doesn’t make her a bad employee."
    "After all, when it came time for her to clean things up, she started focusing harder than I've ever seen her focus before."
    "It was actually a little impressive, to be honest."
    "But I guess it doesn't stay impressive for very long as I elect to leave in the middle of her cleaning spree."
    "At the end of the day, who wants to watch a girl clean up a restaurant when there’s an equally cute one waiting at home?"
    "And so I say goodbye to everyone, turning my back to them as I finally begin to make my way back to the residential district-"
    "Thinking about various combinations of orgies the whole way home."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe10 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe15:
    scene mollyoutside1
    with dissolve
    play music "molly.mp3"

    "It’s a cold winter night, as is customary for...winter."
    "Let me start over."
    "That was a horrible introduction to my nightly activities."
    "I make my way to the cafe to see what Molly is up to because I guess I’m in the mood to be confused tonight or something."
    "I suppose I just subconsciously enjoy spending time with her despite being at a complete disadvantage in around 100%% of our conversations."
    "Hell, I can’t even say something like “At least she’s fun” because, frankly, I don’t really {i}know{/i} how I feel around her."
    "Unique is a better word than fun, in her case."
    "But, then again, unique is the catch-all word you use to describe people that don't fit in. "
    "People with unclear sets of circumstances and ideals that have equally unclear outlooks on what people should enjoy or despise."
    "Unique used to be a bad character trait."
    "People used to be made fun of for not conforming."
    "But now it’s a sort of goal."
    "A finicky goal, but a goal nonetheless. "
    "You want to be unique, but not {i}so{/i} unique that you scare people away."
    "I think this is what Molly struggles with."
    "She hasn’t managed to scare me away yet, but she also seems to enjoy my class a lot more than her last one."
    "I wonder if they thought she may have been a little too unique as well?"
    "Probably."
    "But, somehow or another, her existence was enough to compel me to come here, of all places, in the middle of the night."
    "The middle of this cold, winter night."
    "As is customary for winter."

    scene mollyoutside2
    with fade

    "I find her seated outside of the cafe under the glow of a streetlight, closing her eyes and waiting for her coffee to cool off."
    "It’s rare seeing her without a fiery glare of determination or fists clenched out of passion for some...anime character or...paladin or other things she’s brought up throughout our brief time together."
    "And, strangely enough, despite being stripped of all of those qualities you can easily melt into her industrial grade pot of uniqueness-"
    "She looks more natural than ever."

    mo "Have you blessed yourself tonight, Sir?"
    s "Oh. You knew I was here."
    mo "You have a distinct aura that only someone with my affinity for holy magic is able to sense."
    s "Does that holy aura or whatever have something to do with you asking if I’ve blessed myself?"
    mo "Nay."
    mo "I ask because the moon is but a child."
    mo "Have you looked up at all in the last several hours, Sir?"
    s "...Probably?"
    s "That’s not something I normally keep track of."

    scene mollyoutside3
    with dissolve

    mo "There’s an old Irish superstition that says if you don’t bless yourself whenever you see a new moon, bad luck is sure to befall you."
    mo "But of course, it’s just a superstition...and those aren’t always true."

    scene mollyoutside4
    with dissolve

    mo "For example, I didn’t even drop a fork today and you still showed up."
    s "Ireland is weird."
    mo "Of course, Sir. What other country could have possibly birthed a girl like me?"
    s "I take it this weather is fine for you as well, then?"
    mo "Are you struggling with the cold, Sir?"

    if bonus == True:
        mo "Come! Embrace me! Share in my warmth!"
    else:
        s "Yeah, but I'm a big crybaby, so you can just ignore me."

    scene mollyoutside5
    with dissolve

    if bonus == True:
        mo "But yes. I actually think it’s rather nice tonight."
    else:
        mo "I actually think it’s rather nice tonight."

    mo "The perfect temperature to go on an adventure, even."
    mo "Unfortunately, my legs are far too weak and my body far too frail to embark on such a thing."
    mo "I shall confine myself to this bench instead, waiting patiently for my true love to return to me."
    s "And your true love is?"

    scene mollyoutside6
    with dissolve

    mo "Kagome Higurashi..."
    mo "But she is a story for another day..."
    s "Anime character, I’m guessing?"

    scene mollyoutside7
    with dissolve

    mo "I refuse to believe that it’s possible to have a first love who {i}isn’t{/i} some type of cartoon character."
    mo "Weren’t you particularly fond of a certain sailor scout, Sir? That’s what Ami claims, at least."
    s "Hey, Molly. Here’s an idea-"
    s "How about we talk about normal human stuff tonight instead of...whatever {i}you're{/i} talking about."

    scene mollyoutside8
    with dissolve

    mo "But I already used up all of my human knowledge when I told you about new moons and forks."
    s "Why is your human knowledge limited to such strangely specific things?"
    mo "Because I wiped everything else clear to make room for more otaku stuff. "
    mo "Besides, every conversation I’ve ever tried to have about life with Japanese people has fallen even flatter than my chest."
    s "That sounds pretty bad."

    if bonus == True:
        mo "It is, Sir. I am very much banking on you being a lolicon."

    s "Without divulging any additional information about my feelings on that matter, what’s so different about Japanese people compared to the Irish?"

    scene mollyoutside9
    with dissolve

    mo "Are you truly asking that?"
    mo "That’s like asking about the difference between a warlock and mage."
    s "Are those not the same thing?"

    scene mollyoutside10
    with dissolve

    mo "No! Not even close! I’m offended that you’d even say something like that!"
    mo "Mages are masters of the arcane arts and stupid warlocks get all their stupid powers from a stupid god! It’s barely even magic!"
    s "Maybe you should drink your coffee, Molly. "
    s "Isn’t caffeine good at helping people with...ADHD or whatever?"

    scene mollyoutside11
    with dissolve

    mo "I have also heard that. But you can't just go around bringing up people's conditions like that, Sir."
    mo "You’re going to hurt someone’s feelings that way."

    scene mollyoutside12
    with dissolve

    mo "However!"
    mo "I have become excellent at shielding myself from what {i}actual{/i} humans say!"
    mo "I will be completely fine as long as I don’t read it through a textbox on the bottom third of my computer screen!"
    mo "And since the night is just as [young]as the moon above, I suppose I wouldn’t mind educating you on what makes people like me different from people like you."
    mo "And I’m not just talking about our celestial affinities! Hahahahaha!"
    s "Haha..."

    "Our celestial what?"

    scene mollyoutside13
    with dissolve

    mo "What is the first thing that comes to your mind when you think of Ireland, Sir?"
    mo "I’d be willing to wager that it’s either potatoes or alcohol, am I correct?"
    s "Hey, you said it. Not me."
    mo "The fact of the matter is, there are stereotypes."
    mo "And being a girl implanted from another country, and one who was dedicated enough to learn the language and culture for the sake of my hobbies-"
    s "I’m definitely impressed by that, by the way. I’m not sure if I’ve told you that before."

    scene mollyoutside14
    with dissolve

    mo "Ah-"
    mo "Well, umm...Thank you, Sir."
    mo "But...umm..."

    scene mollyoutside15
    with dissolve

    mo "Like I was saying, there are a bunch of other stereotypes or...stuff people expect that just isn’t always true."
    mo "Like how the Irish are all liars or that they’re violent and...don’t have access to Internet or television."
    mo "You never really understand what people think about you until you go somewhere you don’t fit in."
    mo "But, at the same time, stereotypes exist for reasons and they don’t just come out of nowhere."

    scene mollyoutside16
    with dissolve

    mo "Like...like goblins! Or dwarves!"
    mo "What do you think of when you hear those things, Sir?!"
    s "That they’re short."

    scene mollyoutside17
    with dissolve

    mo "Oh."
    mo "Well, yeah. That’s true."
    mo "But anyone with even mild exposure to fantasy would say things like goblins are greedy and dwarves are masculine and spend all their time blacksmithing."
    mo "Point is, people like me are just like dwarves or goblins in a place like this."
    mo "I was raised a certain way and grew up surrounded by cultures and traditions that wouldn’t make sense here."
    mo "I still have a hard time remembering to take my shoes off inside or how I'm supposed to call out to servers at restaurants."
    mo "And if you threw a Japanese person into the Emerald Isle, they’d feel just as out of place."
    mo "The fact that I speak in...constant reference to things that even most Japanese don’t understand just makes things even harder for me."
    mo "If life’s a game, I’m basically playing on the hardest difficulty right now."
    mo "Like Ornstein & Smough, except there are two Ornsteins and five Smoughs."
    s "Are those...anime characters as well?"

    scene mollyoutside18
    with dissolve

    mo "You have...so much to learn, Sir."
    mo "So much to learn."
    s "Apparently so."
    s "I can’t really attest to what it must be like being “implanted” here, like you put it-"
    s "But even though you’re weird and draw way too much attention to yourself and talk too loudly pretty much all the time-"
    mo "Are you just...going to keep listing the things you don’t like about me?"
    s "And you always cause a commotion in class and never make me any of the things I order inside of the cafe and-"

    scene mollyoutside19
    with dissolve

    mo "When does it end?!"
    s "And all of the other things I find annoying about you-"
    mo "AHHHHHHHHH!"
    s "I think you’re doing great."
    mo "AHHHHH FINE, I’LL TRY TO CUT DOWN ON-"

    scene mollyoutside20
    with dissolve

    mo "Wait, repeat that last part. I was so torn up inside that I drowned it out with my fury."
    s "I think you’re doing great."
    s "I mean, my life was a lot easier before you showed up, but it’s not like I’d get rid of you if I had the choice now."
    s "So yeah, we’re different. Complete opposites even, but-"
    mo "But opposites attract..."
    s "Yeah. That."

    scene mollyoutside21
    with dissolve

    mo "Am I..."
    mo "Am I on the Sensei route already?!"
    mo "Are you in love with me?!"
    s "..."
    mo "..."
    s "I’m not in love with you."

    scene mollyoutside22
    with dissolve

    mo "Oh."
    mo "F’s in chat for the Irish girl. Please and thank you."
    s "Just because I’m not in love with you doesn’t mean I don’t want to spend more time with you, though."
    s "It’s a cold winter night and, instead of going inside and getting a hot beverage, I’ve stayed out here talking about Irish stereotypes and...warlocks."

    scene mollyoutside23
    with dissolve

    mo "If you’re not in love with me, can you stop saying things that will cause my puny gamer brain to think you are?"
    mo "This isn’t the bad end, is it? "
    mo "Is this what the friend zone feels like?"
    mo "You never even turned in your Cult of Molly paperwork so I can’t even contractually bind you to me as a servant."
    mo "Also, don’t get me started on warlocks. I could go on for hours."
    mo "Oh, and if you actually {i}do{/i} want a drink, allow me to purchase it for you so I can use my super awesome employee discount that definitely wasn’t the main selling point to me applying here."
    s "Sure. We'll go in in a few minutes."
    s "Actually, why are you out here anyway? Aren’t you supposed to be working right now?"
    s "It looks kind of busy in there tonight."

    scene mollyoutside24
    with dissolve

    mo "Hohohoho~ I am out here precisely {i}because{/i} it is busy, Sir."
    mo "Do you truly think someone like me is fit to serve that many customers while the owner herself is working?"
    mo "I would just ruin everything."
    s "You seem awfully proud to be bad at your job."

    scene mollyoutside25
    with dissolve

    mo "I learned from the best."
    mo "There’s this one teacher I have who is utterly horrible at his job and still manages to make the lives of everyone he knows marginally better."

    "Easier, sure. Better? No."
    "That’s just not true."

    mo "So if I, too, can make everyone’s lives better by never improving, I am ready to lay down my sword and surrender as well."
    mo "Onward to Valhalla, Sensei."
    mo "You, me, and our unearthly desire to be lazy!"
    s "..."

    "Oh my god."
    "Am I also a Molly?"

    s "I feel kind of sick all of a sudden."
    mo "That’s not illness, Sir. It’s {i}revelation{/i}."

    scene mollyoutside26
    with dissolve

    mo "Lay down your weapon! Shelve your armor!"
    mo "Today, our battle ends! But our war begins!"
    mo "For freedom! For love!"
    mo "For Ireland!"
    s "..."

    scene black
    with dissolve2

    "Molly and I wind up going inside and taking advantage of her employee discount shortly after that."
    "I order a drink directly from Haruka, who places her hand on my shoulder in a show of solidarity for my valiant sacrifice (AKA: spending time with Molly)."
    "But, even if I joke-"
    "It isn’t much of a sacrifice."
    "I mentioned earlier that I wouldn't describe her as “fun.”"
    "And, in doing that, I was wrong."
    "She {i}is{/i} fun."
    "Just..."
    "Not the type of fun I’m used to."
    "And she’s unique as well."
    "Just..."
    "Not the type that’s entirely bad."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe15 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe20:
    scene seconddnd1
    with fade
    play music "breeze.mp3"

    "I swing open the door to the cafe and quickly stumble onto the fact that tonight will be exponentially louder than I expected."
    "And considering I came here to see Molly, the expectation for noise was already pretty high."
    "Is it really okay for them to be playing this in the cafe, though? I can’t imagine Haruka signed off on this."

    mo "Ohoho~ It appears we have ourselves a new player!"
    mo "Take a seat, Sir! I shall help you create a character!"
    s "Uhh, no. I’m good. "
    s "I didn’t realize you all had plans to play here tonight."
    a "But I literally texted you about this exact thing happening."
    s "Yes, but I stopped reading the second I saw words I didn’t understand."

    scene seconddnd2
    with dissolve

    a "What if what I had to say was important?!"
    a "What if I was being kidnapped and didn’t have time to think of words you like?!"
    s "Then you’d probably be in someone’s trunk right now."
    mo "Are you sure you don’t want to play, Sir? We could use someone with your alignment."
    s "My...what?"
    mo "Neutral evil, Sir. That’s how I see your character."
    ay "Evil? Absolutely not. "
    ay "Sensei is lawful good. He’d never do anything to hurt anyone and always stands up for what is right."

    scene seconddnd3
    with dissolve

    f "I don’t think he’s {i}lawful{/i} good but maybe...neutral good? "
    f "His intentions aren’t always clear but I don’t think he’s a bad guy."
    a "Ayane! Stop saying you’re in love with my [uncle]!"
    r "How do you see yourself, Sensei? "
    s "I don’t even know what you’re talking about."
    sa "That’s okay...neither did Tsuneyo and...we helped her figure it out."
    s "Tsuneyo? Is she here?"
    t "Behind you."

    scene seconddnd4
    with dissolve

    t "My alignment is noodle evil."
    mo "{i}Neutral evil{/i}, Kendo Princess."
    t "Noodle evil."
    s "Do you understand what they’re talking about?"
    t "Almost. I seem to have everything very slightly wrong."
    s "That adds up."
    mo "She’ll be able to play once she starts following the rules."
    t "She’s right. I am very bad at this game."
    s "Well, I guess the two of us can watch together as long as you don’t get drunk and pass out on me again."
    t "I will do my very best."

    scene seconddnd5
    with dissolve

    m "If anyone wants my input, I think Sensei is chaotic evil. The absolute worst kind of person."
    s "And I think you’re a nerd."

    scene seconddnd6
    with dissolve

    m "Why does everyone keep calling me a nerd?!"
    mo "Ooooh, a critical hit!"
    mo "I’m giving Sensei advantage on his next attack as a special bonus for getting Maya to yell."

    scene seconddnd7
    with dissolve

    m "Tch!"
    ay "It’s okay, Maya. I don’t think you’re a nerd."
    ay "But I do want you to know that a certain rogue might sneak into your room at night and assassinate you for calling her true love evil."
    f "So...you watched the game on the beach...right, Sensei?"
    f "The one I wasn’t around for."
    s "I tried to. All I remember is a mushroom."
    mo "Well, never fear, Sir! For I shall be giving a recap of our exploits thus far shortly!"
    sa "We’ve played...a few more times since then and...you’ve missed a lot."
    r "Sana had her arm chopped off."
    sa "And then I...beat a man to death with it..."
    s "..."
    a "Yeah, Sana doesn’t really mess around when it comes to D&D. "
    s "..."
    s "Okay, well I’m going to sit down now."

    scene seconddnd8
    with fade

    t "They never chose an alignment for you."
    t "Allow me to do it instead."
    t "I declare you..."
    t "True noodle."
    s "I declare you weird."
    t "I declare my feelings hurt."
    t "Please never talk to me again."
    s "Can I treat you to ramen to win you back?"
    t "..."
    s "..."

    scene seconddnd9
    with dissolve2

    t "I will not allow myself to be bought off like this."

    scene seconddnd10
    with fade

    mo "Okay! That’s enough idle chit chat! The time has come for our journey to continue!"
    mo "We only have two hours until the Magistrate of Mammaries returns to the cafe and scolds all of us for taking up an entire section of the store without buying anything!"
    r "I’m a big fan of the nickname you chose for Haruka. It's very fitting."
    ay "Don’t you think it would be a little better for Futaba, though? I think hers are bigger."
    a "Futaba, what size bra do you wear? Like X?"
    f "I...don’t think it goes that high..."
    mo "Enough!"

    scene seconddnd11
    with dissolve

    mo "When we last left off, we discovered that a powerful Illithid by the name of Thaum had emerged from the Underdark with a small army of thralls at their disposal."
    mo "The party, sensing it had to unite or face a rather untimely and premature level two demise, banded together to force back the thralls."

    scene seconddnd12
    with dissolve

    mo "But not before the loss of Zagull Throat Spear’s arm. "
    mo "Without anyone able to help Zagull regenerate said arm and Thaum retreating to do more evil psion stuff..."
    mo "The party headed to the nearby city of Frostford for some much needed rest and...hopefully an experienced healer."

    scene seconddnd13
    with dissolve

    mo "Despite its name, Frostford is a coastal, port city that is home to one of the biggest alchemical colleges in all of the land."
    mo "So it’s no surprise when you see the streets lined with [young]alchemists, their noses buried deep in books, studying their hearts out to prepare for upcoming exams."
    mo "It’s the end of a semester and the city is bustling with uncertainty and energy. "
    mo "The perfect time to talk to anyone you want or, better yet, ask them anything you’re still curious about."
    mo "Your party still has no clear goal as you took a wrong turn and ran into Thaum long before you were supposed to, so things could really go anywhere from here."

    scene seconddnd14
    with dissolve

    mo "So, what do you guys wanna do? "
    mo "Like I said, there’s no goal right now and you still don’t know why you all woke up next to one another, so it’s probably a good idea to go out and find a...reason to exist or something."

    scene seconddnd15
    with dissolve

    r "Sana, how important is it for you to get your arm back?"
    sa "I..."
    sa "I kind of like only having one arm..."
    sa "It makes me look strong and...I’m able to wield my greataxe with one hand."
    mo "You’ll still have disadvantage though, so...just saying."
    r "Okay, but what matters more to you? Looking cool or killing people?"
    sa "That’s...umm..."
    r "Actually, don’t let Sana think about that. What would {i}Zagull{/i} want?"

    scene seconddnd16
    with dissolve

    sa "Zagull will...bathe in the blood of his enemies no matter the circumstances!"
    sa "He only needs one arm to drain the life from his opponents!"

    scene seconddnd17
    with dissolve

    a "Well...while Nithhala and Zagull are trying to figure out the arm thing, do you think maybe the rest of us should head to a tavern or something?"
    m "Is your wizard also an alcoholic?"

    scene seconddnd18
    with dissolve

    a "What? No. Just...that’s where you normally go to pick up quests and stuff."
    f "That’s true. Innkeepers always seem to know the latest gossip in fantasy novels."

    scene seconddnd14
    with dissolve

    mo "So you three are going to head to the tavern?"
    m "Yes. Arborea needs to get her fix."
    a "I do not! I’m just looking for some sort of goal so we don’t wander around town until we grow old and die!"
    mo "Oooookay! Arborea, Urrheak and Xessaxia-"
    mo "You’re lucky enough to come across a signpost pointing you directly toward the tavern immediately after entering the city limits."
    mo "It appears to be only a short walk from here, so you should be able to get there in no time at all."

    scene seconddnd19
    with dissolve

    mo "Nithhala and Zagull, are you going to the tavern as well?"
    r "Huh? Oh, yeah. We’ll go."
    r "Zagull isn’t convinced that he wants his arm reattached yet."
    sa "But Zagull {i}could{/i} go for a tall glass of mead! Bahahaha!"
    mo "Okay! So the five of you begin to make your way to the tavern-"

    scene seconddnd20
    with dissolve

    ay "Wait a second, I haven’t said what I wanted to do yet."
    mo "Oh, sorry. Lots of people. Trying to keep track of everything."
    mo "What is Lidearel doing?"
    ay "..."
    ay "She’s gonna go with everyone because she gets lonely easily."
    ay "But she’s also going to try and pickpocket the first man she sees."
    mo "You see a lot of men. It’s a relatively busy city."
    ay "Are there any gnomes?"
    mo "There are not."
    ay "Tieflings?"
    mo "Apart from Nithhala? No."
    ay "I’m just going to try to pickpocket Nithhala then."
    r "Dude."
    ay "I won’t keep anything. I just want to assert dominance."
    r "Steal from Zagull. He’s only got one arm."
    ay "Yeah but that arm is bigger than my entire body. I’m going to pickpocket Nithhala."

    scene seconddnd21
    with dissolve

    r "..."
    sa "This is fun..."
    r "Easy for you to say. You killed someone with your arm."
    mo "I mean...it's kind of an unwritten rule to not do things like this...but roll sleight of hand, I guess."

    ay "Woo! Just gonna grab my dice and..."

    play sound "dice.wav"

    ay "That’s an...18."
    mo "Oof. Okay. Rin, roll perception to see if you catch her."
    r "Why? We all know what it’s going to be."
    mo "So you’re just going to ignore her pickpocket attempt?"
    r "Ugh, fine."

    scene seconddnd22
    with dissolve

    r "Sana. "
    sa "...Yes?"
    r "Can you blow on my dice for good luck?"
    sa "Is that...a thing people do?"
    r "I think so?"
    sa "...Um."

    scene seconddnd23
    with dissolve

    sa "{i}Hoooo...{/i}"
    r "..."
    r "So cute..."

    scene seconddnd24
    with dissolve

    r "OKAY! Thanks, Sana! With your blessing, there’s no way I can lose!"

    scene seconddnd25
    with dissolve
    play sound "dice.wav"

    r "..."
    sa "..."
    r "..."
    sa "..."

    scene seconddnd26
    with dissolve

    sa "There there..."

    scene seconddnd27
    with dissolve

    mo "Nithhala rolled a 5 for anyone who didn’t see. Which means Lidearel is able to successfully reach her hands into Nithhala’s pockets and find..."
    ay "Woo! What did I get?!"
    mo "Absolutely nothing."
    mo "You didn’t start with any items and Nithhala’s bag is completely empty."

    if bonus == True:
        mo "Since you rolled an 18, though, we can assume that you just successfully groped her without being noticed."
    else:
        mo "Since you rolled an 18, though, we can say that you managed to like...steal a button off of her outfit or something."
        r "Noooooooo my button!"

    ay "Oh. Well, that’s better than nothing, I guess."

    scene seconddnd28
    with dissolve

    t "Are you having a good time?"
    s "Are you?"
    t "I think so. "
    t "Everyone else is having a good time, so I think I’m supposed to be having one as well."
    t "I’m very confused, though."
    s "You and me both."
    s "What’s so fun about deciding success based on dice rolls?"
    t "Perhaps there is a certain ingrained desire in all of us to allow chance to rule our lives?...So that we do not have ourselves to blame when things don’t go our way."
    s "..."
    t "Or maybe they just like dice."
    t "I don’t know. I’m not allowed to play."

    scene seconddnd29
    with dissolve

    mo "So, after Lidearel feels up her tiefling companion, she and the rest of the group make their way to the local tavern."
    mo "It’s a large building situated in the center of the city with an ornate wooden archway towering over a beautiful pair of dwarven, hand carved doors."
    mo "But, before you’re able to enter, the doors swing open and out flies a young, half elf woman."
    mo "She falls flat on her face, but quickly regains her composure and scurries backward."
    mo "Her clothes are tattered and torn...and look as if they haven’t been washed even once in her life."

    scene seconddnd30
    with dissolve

    mo "{i}Back! Back, I say!{/i}"
    mo "{i}You’re...you're all here to laugh at me as well, aren’t you?!{/i}"
    mo "{i}That’s all they ever do in this town! Laugh, laugh, laugh!{/i}"

    scene seconddnd31
    with dissolve

    mo "The woman brandishes a golden dagger with a silver inlay on the handle, one that looks far too valuable for her to own, and points it directly at Arborea."
    a "Wait, me? What did I do?"
    mo "Is that {i}in{/i} character or out of character?"
    a "Oh. Uhh, both I guess?"
    mo "Cool. I’m just going to keep roleplaying then."

    scene seconddnd32
    with dissolve

    mo "{i}You...You think I don’t know who you are?{/i}"
    mo "{i}You’re the same woman who turned me away in the last tavern!{/i}"
    mo "{i}None of you ever listen! Thaum is...Thaum is coming!{/i}"

    scene seconddnd33
    with dissolve

    f "Surely, you jest. "
    f "If you speak of the mind flayer, we made quick work of him on our way into town."
    mo "{i}Then...Thaum is...dead{/i}?"
    f "Nay, just forced back. But his army reduced to mere nothing."
    a "The Satyr speaks the truth. "
    a "You must have me confused with someone else."
    a "I’ve never even come to this town before."
    m "Bacawk."

    scene seconddnd34
    with dissolve

    mo "You...you know the aarakocra can speak common as well, don’t you? "
    mo "You don’t always have to talk like a bird."
    m "Urrheak never learned common."
    mo "R...Right..."
    mo "But anyway..."

    scene seconddnd35
    with dissolve

    mo "{i}If...if what you say is true and the first line has already been pushed back...then...{/i}"
    mo "{i}Then it’s only a matter of time before...{/i}"

    scene seconddnd36
    with dissolve

    mo "The woman takes several steps back, tripping over a park bench and tumbling into the cart of a food vendor."
    mo "But just as the vendor is about to cry out in a fit of rage after having his product destroyed, the woman violently grips her head and begins ripping out large clumps of her hair."
    mo "She lets out a pained scream as if she’s being consumed from the inside out."

    scene seconddnd37
    with dissolve

    mo "{i}NGAHHHHH! I...I CAN FEEL HIM!{/i}"
    mo "{i}STAY...BACK! I CAN’T...FIGHT IT ANY LONGER!{/i}"
    mo "{i}I...I-{/i}"
    mo "{i}Blahhhhhgababababababa!{/i}"

    scene seconddnd38
    with dissolve

    mo "The woman suddenly turns into a mushroom. Go ahead and roll for initiative."

    scene seconddnd39
    with dissolve

    t "The fungus returns!"
    t "Run, friends! Escape while you still can!"
    s "Are there any enemies in this game other than different types of mushrooms?"
    t "One can only hope. "
    t "They won’t last much longer at this rate."
    s "And neither will I."
    s "I’m going to head out."

    scene seconddnd40
    with dissolve

    t "What?"
    t "But then who will I talk to?"
    mo "What’s this I hear about heading out?"

    scene seconddnd41
    with dissolve

    mo "Are you not having a good time, Sir?"
    mo "I’m sorry. If I’d have known you’d be appearing tonight, I wouldn’t have scheduled our next session when I did."
    s "Oh, I’m not asking you to call it off or anything."
    s "Don’t let me get in the way of your fun. This sort of thing just isn’t for me."
    mo "Do you...not even want to try? "
    mo "There are plenty of things I never expected to like that I absolutely love now...And I never would have known that if I didn’t give them a chance."

    if bonus == True:
        mo "Granted, they’re all different doujinshi tags and that doesn’t really apply to this conversation, but I’m sure you know what I mean."
        t "I don’t. Please explain."
        mo "When you’re older, Kendo Princess."
        t "Yes, Emerald Guardian. I understand."

    s "Maybe some other time. I’m just going to head out now, though."
    s "As for Tsuneyo-"
    mo "She’ll be fine. "

    scene seconddnd42
    with dissolve

    mo "Come sit at the table with us. We’re starting combat in a minute or two and I’ll try teaching you how that works again."

    scene seconddnd43
    with dissolve

    mo "Sorry you didn’t have fun, Sir. "
    mo "I was hoping it would be exciting enough for everyone, but it seems I may have failed you."
    s "Again, don’t be too hard on yourself. It’s just a personal interest thing."
    s "Maybe some other time."
    mo "Okay. Maybe some other time..."

    scene black
    with dissolve2

    "I get up off the stool and say goodbye to all of the girls, exiting the cafe and starting my journey back."
    "I hope Molly doesn't take my early departure too personally."
    "I understand why she’d be upset that I’m not interested in the same things as her but, at the same time, she should have probably realized that by now."
    "Liking different things is fine, though."
    "It gives me more time to..."
    "Aimlessly wander around town and think about all of the other things I could have done with my night."
    "Oh well, I guess."
    "At least all of the girls seem to be having a good time."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe20 = True
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe25:
    scene mollycleaning1
    with fade
    play music "cafe.mp3"

    mo "Guh..."

    "It’s dark by the time I make it to the cafe. "
    "Molly, still attempting to put the pieces of herself together after losing several of them recently, has spent the last ten minutes wiping down the same spot on the counter without realizing it."
    "I think about informing her but, at this point, I’m curious to see whether or not she can manage cleaning it so thoroughly that it burns a hole into the bar."
    "I imagine that we are at least another ten minutes away from anything like that happening, unfortunately. "

    s "Keep it up, Molly. Just a little while longer until your goal is accomplished."

    scene mollycleaning2
    with dissolve

    mo "Are you kidding, Sir? We’ve been closed for ten minutes already and there are still guests inside. I am never going home."
    mo "At this rate, my long rest is going to turn into a short rest and I’m not even going to recover all of my hit points."
    mo "Do you have any idea how low my health is right now? A leaf could fall on my foot and knock me unconscious."
    s "Sounds like a big leaf."

    scene mollycleaning3
    with dissolve

    mo "Hah. Getting eliminated by nature certainly would be an ironic way to go after spending most of my life indoors."
    mo "If only I had listened to my father and went outside to play with all of the “normal” kids more often. "
    s "I’m a little confused about what a “normal” Molly would even be like."

    scene mollycleaning4
    with dissolve

    mo "Probably a little like the abnormal one, but less loud and better at not destroying friendships."
    s "Yeah. I figured that might have had something to do with your unenthusiastic demeanor tonight."
    mo "Unenthusiastic demeanor?"
    s "You’ve been wiping the counter for ten minutes now."
    mo "It’s really dirty."
    s "In just one spot?"
    mo "..."
    mo "Yes."
    s "Molly, come on. You’re not fooling anyone."

    scene mollycleaning5
    with dissolve

    mo "Okay, yeah. So maybe I {i}am{/i} a little less...rambunctious than normal. But my inability to maintain long lasting relationships isn’t a part of that, Sir."
    mo "I’ve simply been losing sleep lately."
    s "Right. And {i}why{/i} are you losing sleep, Molly?"

    scene mollycleaning6
    with dissolve

    mo "Why, gaming of course!"

    if bonus == True:
        mo "I don’t have time to grieve over my missteps when I have alts to level and fictional characters to put my fictional penis inside of!"
    else:
        mo "I don’t have time to grieve over my missteps when I am too busy making my Saurfang costume for Blizzcon!"

    s "Yes, I can see now how valuable your time truly is."
    s "Are you sure that’s it, though?"

    scene mollycleaning7
    with dissolve

    mo "You’re showing an awful lot of concern tonight when you normally seem to completely overlook me, Sir."
    s "I never {i}overlook{/i} you. You’re just a little more exhausting to spend time with than most of the other girls."
    mo "That makes sense."
    s "Plus, I always manage to be around people when they’re at the worst of their worst, and I’d like to avoid that with you if at all possible."

    if bonus == True:
        mo "You already found me at the worst of my worst when I was...admiring Rin’s Instagram. "
    else:
        mo "You already found me at my worst that one time where you walked into the janitor's closet and founding me kissing a mop."

    s "Was that really the {i}worst{/i}?"
    mo "Not at the time, but I imagine the embarrassment will linger in my mind far longer than what I am experiencing now."
    s "That sounds...surprisingly mature for you."

    scene mollycleaning8
    with dissolve

    mo "Then I suppose it would be for the best if I were to compare it to yet another reference to a video game you have never played in hopes that you will somehow understand what I’m talking about."
    s "That’s the Molly I know."
    mo "This whole thing with Rin is like a bout of resurrection sickness."
    mo "For a little while, everything is going to hurt a lot more than normal. And I’m going to have to be more careful about the things I do and...who I party up with."
    mo "But that will fade over time. "
    mo "I just need to go AFK for a little while. Or put myself on autorun against the corner of a wall or something like that."
    s "Well, if anything, you have definitely succeeded in getting me lost."

    scene mollycleaning9
    with dissolve

    mo "You know...the worst part of all of it isn’t that she’s with someone else now. Or that things between us will take a long time to get back to normal."
    mo "It’s the embarrassment of what happened. And the moments at work where our eyes meet and we have to quickly look in opposite directions to avoid feeling awkward around one another."
    mo "It’s like a scene out of the end of a visual novel, where two characters who were once close have grown apart and don’t want to stop each other from going their separate ways."
    s "Who are you and what have you done with Molly?"

    scene mollycleaning10
    with dissolve

    mo "Gah! I’m sorry, okay?! The sleep deprivation is making me more mature than I want to be!"

    scene mollycleaning11
    with dissolve

    mo "Besides, just because the hardest part isn’t what I expected doesn’t mean the whole thing isn’t hard at all."
    mo "It sucks. I hate it times a million and I want these stupid human feelings to leave my body so I can go back to focusing on games and nothing {i}but{/i} games."
    s "Maybe preserve a little bit of that focus for work, though. "

    s "Haruka will be mad if you clean a hole into her bar."

    scene mollycleaning3
    with dissolve

    mo "{i}Hah.{/i} To tell ya the truth...I haven’t really been a great employee as of late."
    s "{i}What? You? No...{/i}"

    scene mollycleaning2
    with dissolve

    mo "Okay. I haven’t been a great employee as of...ever."
    mo "But I’ve been even worse lately."
    mo "Honestly, Sir? I think I would have been fired already if Haruka didn’t understand, to some extent, the feelings I am so unfortunately...feeling right now."
    s "Then the least you can do is not destroy her belongings."

    scene mollycleaning4
    with dissolve

    mo "Sir, may I ask you a question?"
    mo "Does being disliked and being bad at your job ever keep {i}you{/i} awake at night?"
    s "I thought it was gaming that was keeping you awake at night?"
    mo "Well...yes. It is."
    mo "Games certainly are the most prominent cause of my current lack of energy, but there {i}are{/i} times that I have to lay in bed where I can’t just...escape it all."
    mo "At least not until the NerveGear is actually developed and I can just full dive into a completely different world and start over from zero."

    scene mollycleaning12
    with dissolve

    mo "Ooh! If that ever happens, you should come with me!"
    s "If what happens? I think you forgot that not everyone understands your lingo again."
    mo "A virtual reality helmet that lets you live a completely new life inside of a virtual realm!"
    mo "Think of all the amazing things you could do there!"

    if bonus == True:
        s "I could finally have sex with an elf..."
    else:
        s "I could finally hug an elf..."

    scene mollycleaning13
    with dissolve

    mo "Oooh, an elf lover. "

    if bonus == True:
        s "Hey, no one mentioned love. I just want to bang one."
    else:
        s "Hey, no one mentioned love. I just want to hug one and tell him or her they are important."

    mo "Luckily for you, NPCs are incapable of love! And in a fictional setting, they’d probably be easier to woo as well!"
    mo "Not that you have any issue with wooing women or anything. I mean, you {i}are{/i} the Herald of the Adolescents, after all."

    if bonus == True:
        s "I’m just going to assume that this section of the conversation is over and that I have your full support when it comes to interspecies sexual intercourse."
    else:
        s "Thank you, Molly. You are always so helpful and full of knowledge."

    scene mollycleaning14
    with dissolve

    if bonus == True:
        mo "Of course, Sir! In fact, I have a lengthy list of h-games readily available to scratch that exact itch of yours!"
    else:
        mo "Of course, Sir! And if you are looking for a game where you can hug as many elves as you would like, might I suggest-"

    s "Thanks, but I’ll probably stick to real humans for the time being."

    scene mollycleaning3
    with dissolve

    mo "Gah. How boring."
    s "Weren’t you head over heels for an actual human being until just recently?"

    scene mollycleaning2
    with dissolve

    mo "Well...yes. But then I received a cruel reminder as to why I shouldn’t be getting involved in affairs like that in the first place."
    mo "I’m happy that Rin is happy. "
    mo "Well, partially happy."
    s "And the other parts?"

    scene mollycleaning7
    with dissolve

    mo "Well...they’d obviously have to be unhappy, wouldn’t they?"
    s "Unhappy {i}why{/i}?"
    mo "..."
    mo "Probably...the same reason I’m happy. Just spun around until it can’t stand up anymore and has to throw up all over the floor."
    s "It’s okay to just...not be happy, you know? I-"

    scene mollycleaning15
    with dissolve

    mo "Thank you, Sir. But I’d like to save a conversation as depressing as this for a time when it’s easier for me to escape into more allusions."
    s "Sure. That’s fine. I just don’t want you feeling down if there is an option to not do that."
    mo "That is the issue, though, Sir. "
    mo "I {i}deserve{/i} to feel down right now."
    mo "I did a horrible thing. Not just once, but twice. "
    mo "If I get hung up on the fact that it did not personally benefit me instead of being happy for a friend or...{i}whatever{/i} she is now, who finally got something she wanted..."
    mo "Well...I think I’d feel even worse about myself than I already do."
    s "So what, then? Are you just going to go back to ignoring those feelings?"
    mo "If you get good enough at ignoring something, it eventually feels like it’s not even there."
    mo "And while it might not sound like a storybook ending, that outcome would be better than anything else I can think of right now."
    s "..."
    s "It sounds good to me too."

    scene mollycleaning16
    with dissolve

    mo "Yeah?"
    s "Yeah. "
    s "To be honest, I was expecting you to be doing a lot worse than you actually are."
    s "I know that you’ve been through some pretty rough shit in the past, but I also know that this was important enough for you to break down in my arms about before."
    s "But if you feel like you’re capable of just ignoring it and letting time do its shitty thing of taking forever to make you feel slightly better, go for it."
    s "Not like I can really help anyway."
    s "Oh, also, your last customer just left."

    scene mollycleaning17
    with dissolve

    mo "A-ha! Then you {i}can{/i} help!"
    s "Please don’t make me clean the store. I don’t work here."

    scene mollycleaning18
    with dissolve

    mo "So you’ll do anything possible to cheer me up {i}except{/i} for helping me do my job?"
    s "I don’t think I ever said {i}anything{/i}."
    mo "I believe it was implied, Sir. "
    mo "Are you not aware of my incapability to perform at my full potential right now?"
    mo "There is a darkness growing within me that is sucking out my life essence as we speak. How would you feel in my shoes?!"

    if bonus == True:
        s "Eh. Getting life juice sucked out of me doesn’t sound too bad right now."
    else:
        s "Probably bad. I think my feet are bigger."

    scene mollycleaning19
    with dissolve

    if bonus == True:
        mo "W-Well...no! I guess...it would make sense for you to say that!"
    else:
        mo "Uh...probably!"

    mo "But I would still very much appreciate it if you could, at the very least, place the chairs on top of all of the tables."

    scene mollycleaning20
    with dissolve

    mo "As a...one time favor to me for...not making your life as difficult as you expected me to tonight."
    s "..."
    mo "And also if you’d walk me home after we’re done."
    s "So a two time favor."
    mo "One time consisting of two things."
    mo "Maybe a third when we get back to the dorm. Who knows?"

    if bonus == True:
        s "Can you do {i}me{/i} a favor when we get back to the dorm?"
        mo "Is this favor you have in mind a lewd one?"
        s "Is it {i}allowed{/i} to be a lewd one?"
        mo "Is my name Molly Medb MacCormack?"
        s "...Maybe?"
        mo "Wrong! It is Molly Moyra MacCormack!"
        mo "Why do you not know this?!"
        s "It wasn’t in your character profile."
    else:
        s "My father never taught me how to do any handyman-type things, so if you need a lock replaced or something, you should probably just ask Io."

    mo "Silence! Chairs! Go go go!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I sigh to myself and somehow let Molly bully me into helping out in some way."
    "I really don’t care as much as I made it seem, though."
    "It’s not like this place has {i}that{/i} many chairs...and the ones they do have are relatively light."
    "As such, I’m able to finish the task in several minutes and proceed to wait by the counter (That lives to see another day) for Molly to finish her portion of the work."
    "She does what I imagine is a half-assed job and finishes up in about twenty minutes before changing back into her winter clothes and beckoning me outside."
    "........."
    "......"
    "..."

    scene mollycleaning21
    with dissolve
    play music "molly.mp3"

    mo "Alas, the stars have retreated back into their caves in the depths of the night sky...preserving their light for the end of days as it steadily approaches."
    s "There are no caves in the sky, Molly."
    mo "Of course I know that, Sir."
    mo "I just mean that there’s a clear amount of light pollution here. It’s not like it was at the beach."

    scene mollycleaning22
    with dissolve

    s "Ah. I guess not."
    s "I wouldn’t really expect any less in a city, though."
    mo "You don’t have to expect something before being disappointed, Sir. Sometimes, you can just...be disappointed."
    mo "I like the stars. I wish the sky always looked the way it did when we were there."
    s "Don’t let Maya hear that. She’ll probably quiz you on them."
    mo "I’d fail a quiz miserably. I just like looking at them."
    s "... "
    s "They’re okay, I guess."
    mo "So, do you intend to venture forth on a side quest back to the dorm with me? Or is this where our party disbands and heads its separate ways?"
    s "My answer to this question hinges on how long you plan on talking about stars for."
    mo "I was already done, Sir. I was simply pointing out how I wish there were more."
    s "Then yeah. I can come back to the dorm with you."
    mo "Excellent. I’ll see to it that you obtain a rather desirable quest reward as a result."

    if bonus == True:
        s "Lewd or not lewd?"
        mo "Not lewd, of course."
        s "That doesn’t sound very desirable to me."
    else:
        s "Can you teach me how to tie my shoes? My father never taught me that either."
        mo "Of course, Sir. If that is what will make you happy."
        s "Yay!"

    scene mollycleaning23
    with dissolve

    mo "Sir, I realize this may be annoying, but would we be able to stop somewhere along the way?"
    s "Where did you have in mind?"
    mo "A nearby leyline I like to draw power from when my stocks begin to run low."
    s "Based on what I know about Mollyspeak...I’m going to assume that means a convenience store."

    scene mollycleaning24
    with dissolve

    mo "It appears you still have much to learn then, as that answer is rather far from the truth."
    mo "Come. Let us pick up yet another side quest and see if that one yields any worthy rewards as well!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump mollycafe25p2

label mollycafe25p2:
    if _in_replay:
        play music "molly.mp3"

    scene nightsky
    with dissolve2

    "Molly and I walk relatively close together for the duration of the trip or...side quest or...whatever you want to call it."
    "I’m not too worried about whatever rewards it will yield considering that, if this were some sort of role playing game, I would either be the final boss or an overpowered hero character."
    "Someone who everyone else either aspires to be or inherently fears."
    "Or somewhere in between, but carrying over the best sides from both ends of the spectrum and packing them neatly into one tiny box known as “me.”"
    "Of course, it would be no game at all if there weren’t other people I met along the way."
    "Tonight, my companion is a [young_girl] who was not even born in this section of the world."
    "And while I can’t imagine her being of much use in terms of defeating enemies, she brings with her an aura that, more often than not, manages to bleed into and inspire others."
    "Or annoy them."
    "The effects are random, of course. And sometimes the aura is so clearly disadvantageous that, before you know it, you’re attempting to compensate for what she lacks."
    "If that doesn’t sound like a party member you’d take on your journey, you can chalk it up to the fact that I am no game designer."
    "I don’t know what is good or what is bad."
    "I’m just naming the things I see before me and attempting to connect them to a bigger picture and kill the silence that has consumed the air where her aura so typically lies."
    "The wind picks up as we wander into the park Otoha plays in."
    "We walk past her bench and I resist the urge to draw comparisons between her and the girl she “lost” to."
    "If Molly even considers it a loss in the first place and not just some...obstacle on the way to her next game."
    "That’s right."
    "I’m sure this will all blow over just as quickly as it began."
    "Kind of like the wind."

    scene mollywind1
    with dissolve2

    mo "Arise, spirits of the night! And to arms, my fae companions! "
    mo "I draw on your power in this time of need, for the world has begun to spin once more and left me behind."

    scene mollywind2
    with dissolve

    mo "Ahh, yes! It spins even now..."
    mo "And as the ground beneath my feet trembles...and the oceans swell with the pulsating, overinflated abdomens of gods of yore...I can feel it."
    mo "Silence, friends. For you may feel it too."
    mo "And though that feeling may cause you quite the fright, ‘tis fine! For as my guide is the light that brings you vibrance, your presence is the light that guides me home!"

    scene mollywind3
    with dissolve

    mo "Help me, dearest friends...for I have seen thou when no one else did."
    mo "And I have felt thou in the same winds that blow through these lands tonight and chills my bones to their core."
    mo "Be here for me, as I have been there for you."

    scene mollywind4
    with dissolve

    mo "And please, if you truly do exist at all- grant me your strength."
    s "..."
    mo "..."
    s "If you don’t really know if whatever you’re talking to exists or not, why talk to them or...{i}it{/i} at all?"

    scene mollywind5
    with dissolve

    mo "I wish I had an answer for that, Sir."
    mo "You see, I’ve spent most of my life talking to things that aren’t really there in the hopes that...if they {i}are{/i}, they’ll know I believed in them."
    s "Why?"
    mo "Because magic, Sir. Duh."
    mo "Imagine how amazing life would be if you could manipulate the elements or...fate...or...pull power out of the ether and convert it into anything you wished for."
    mo "I think that would be spectacular. "
    mo "So if there is anything out there that {i}has{/i} that power, all I wish is to see it."
    mo "And maybe channel a fair bit of it into myself for personal use, but only if those gifting it would be willing."
    mo "Wouldn’t want to ask for too much, of course."
    s "Well, I hope that whatever you’re talking to exists as well, since that was kind of the reason we came out here in the first place."

    scene mollywind6
    with dissolve

    mo "Would you like to try as well, Sir? Communicating with the fae, I mean."
    s "Yelling at trees in the middle of the night? I’m okay."
    s "I don’t even know what a fae is."
    mo "‘Tis not just {i}one{/i} thing, Sir. The fae encompass all fairies."
    mo "Aos Sí...Clurichaun...Púca.  "
    s "Those are words, alright."
    mo "Not just words, Sir. Legends."
    mo "And not just legends either. They’re characters in tales from not just Ireland, but all over the world."
    mo "Every country you can think of has their own myths...their own creatures that people believe exist, but just can’t gather enough proof for."
    mo "If such a thing exists all across the globe, I don’t think it’s fair to dismiss them without giving them a little more time."
    mo "They could always just be shy."
    s "So...all of these {i}allegedly{/i} made-up creatures from all over the world can also be known as the fae?"

    scene mollywind7
    with dissolve

    mo "For the sake of helping you understand, sure. We can summarize it like that for now."
    s "Wow. Look at you actually {i}helping{/i} me understand this time instead of just saying a bunch of things and expecting me to learn them right off the bat."

    scene mollywind8
    with dissolve

    mo "I’ve tried to help you many times, Sir! You’re just always very quick to tell me you don’t care."
    s "Probably because I don’t."
    mo "See? You just did it again."
    s "I know what I did. "
    s "But I don’t really {i}have{/i} to care about all the same stuff as you, do I?"
    s "If I had any interests, I wouldn’t expect you to jump all over them and...be excited to talk about stuff you know nothing about."

    scene mollywind9
    with dissolve

    mo "No...I understand. I am not looking for sympathy. I’ve been getting enough of that from the Kendo Princess lately. "
    mo "I..."
    mo "I need to get better at not...forcing myself onto others."
    mo "I just get excited easily. ‘Tis all, Sir. "
    mo "I swear it."
    s "It doesn’t really matter to me. I’m still here, aren’t I?"

    scene mollywind10
    with dissolve

    mo "Surprisingly, yes. You even allowed me to come to my power spot and everything."
    s "Well...are you feeling any more powerful?"
    mo "Not particularly. It did help being able to talk to all of my friends, though. Mythical-slash-mystical or not. "
    s "Great. Are we done here then?"

    scene mollywind11
    with dissolve

    mo "Aaaaaaaactually..."
    s "..."
    mo "Can we sit down for a little while? "
    mo "It’s a nice night and...I know I’ll start thinking once I get home."
    s "You? Thinking? That sounds dangerous."
    mo "Haha...hah..."
    s "Sure, Molly. We can sit. "
    s "But, I’d prefer if it didn’t take up too much time since it’s only getting colder and windier as the night goes on."
    mo "Understood, Sir. I will do my best to annoy you for less time than normal. "

    scene black
    with dissolve2

    "Molly runs forward and chooses a different bench than the one right beside me, probably because she is difficult, and immediately begins looking up at the sky again."
    "I’m not sure if it’s some sort of reflex for her or if she’s just doing it for momentary comfort, but I see no sense in stopping it because at least it’s bringing a smile to her face."

    scene mollywind12
    with dissolve2

    "Instead of talking, I decide to stare at her for a little while- wondering how she’s managing to keep things together even though I know she’s being torn up inside."
    "In the midst of mentally listing those possibilities, a funny thought pops into my head."
    "What if these fae or whatever...do exist?"
    "And what if they’re just...inside of her?"

    s "..."

    "Then I kick myself in the mental balls for being so corny, even if it was only in the form of an inner monologue."
    "The more realistic answer would be that she’s already dealt with one of the worst things a person can go through in losing her mother."
    "Does that have some sort of correlation to experiencing heartbreak? Probably not."
    "But at least she’s been hurt before."
    "It’s always easier when you’re hurt multiple times."

    s "..."
    mo "My foresight is telling me that you’re planning on asking me something."
    s "Your foresight is pretty damn good then because I haven’t even planned on that yet."

    scene mollywind13
    with dissolve

    mo "What is it, Sir? Do you want to learn more about the fae?"
    mo "Which kind? Leprechauns? Changelings?"
    s "Actually..."
    s "Why not tell me more about your family?"

    scene mollywind14
    with dissolve

    mo "My family?"
    s "More specifically-"

    scene mollywind15
    with dissolve

    mo "Ah."
    mo "I think our brain waves may have connected just now, for I was thinking the same thing when I was staring up at the sky."
    s "But I haven’t even told you what I was thinking about yet."
    mo "Then I will tell {i}you{/i} what I was thinking and we can pretend it was the same if it actually was not."
    mo "Tír na nÓg."
    s "..."
    s "Nope. Can’t even pretend that’s what I was thinking since I have no idea what it means."
    mo "Tír na nÓg- or the Land of the Young, is a magical land not far off the Isle, where no one can die...and where everyone remains eternally young."
    mo "Many believe that the reason the fae will not grace us with their presence is because they reside there, Sir."
    mo "One of those people was my mother."

    "Oh."
    "So I guess Molly might actually have foresight after all."
    "Either that or I’m just...incredibly easy to read."

    mo "I don’t have many memories of her, to tell you the truth."
    mo "But I do remember a large collection of storybooks and fairytales that she would read to me before she died."
    mo "I wish I remembered more about {i}her{/i} specifically...but I think that leaving all of those books behind was just...her way of communicating."
    mo "I wasn’t left with nothing like many other children who lose their parents are. "
    mo "I still have my father...and mountains of magical myths my mother may have memorized..."
    mo "I have pictures of her too. And old clothes I hope to be able to wear one day."
    mo "She was beautiful."
    mo "Not like me."
    s "Hey, now. "
    s "I doubt she’d be happy to hear you saying that about yourself."

    scene mollywind16
    with dissolve

    mo "No...It’s true, Sir."
    mo "And I’ve known it to be true for quite some time. "
    mo "If I was...prettier or...cooler like someone like Chika or Otoha, you and I wouldn’t be on this bench right now."
    mo "I’d have won."
    mo "But I made the executive decision to put all of my stat points into categories that didn’t matter as much as aesthetics to some people."
    mo "Which is fine. We all have different things we look for in partners."
    mo "I just wish it wasn’t too late to change where I allotted those points, is all."
    s "It’s not, though."

    scene mollywind17
    with dissolve

    mo "But, Sir...you {i}have{/i} to say that."
    mo "You’re the protagonist."
    mo "It’s your job to make us feel loved or wanted. "
    mo "We can’t just change who we are now after spending so many years figuring it out."
    s "These are the exact years you’re supposed to be {i}using{/i} to figure it out, though."
    s "Even if Rin {i}doesn’t{/i} think you’re pretty, which I don’t think is the case, there are plenty of people who do."
    s "And it might sound kind of weird, but a lot of people are really attracted to foreigners in Japan."

    scene mollywind18
    with dissolve

    mo "Well, {i}that{/i} was mildly racist. "
    s "I didn’t mean it in a bad way."

    scene mollywind19
    with dissolve

    mo "{i}*Sniff*{/i} No, it’s fine. I know you meant no harm."
    mo "I’m sure I’m overreacting. It’s just hard not to think certain things when you share literally {i}every{/i} interest with the person you like and they still won’t give you a shot."
    s "Some people just want something different from them, I guess."
    mo "Otoha isn’t that far off from Rin, Sensei."
    s "Okay, sure. But we shouldn’t be using Rin as the basis for {i}anything{/i} when she is about as composed as..."
    s "I can’t even think of a comparison. She’s a wreck."

    scene mollywind20
    with dissolve

    mo "A wreck I’ll never get to have or hold."

    if bonus == True:
        mo "Or get all hot and bothered with while playing h-games."

    s "No. But you {i}have{/i} kissed her before, which is more than a lot of people can say."

    if rinbetrayed == False:
        "Not including me, of course. I’m in that same boat. But Molly doesn't need to know that."

    mo "I don’t think it’s fair to count what happened on Christmas as a real kiss, Sir."
    mo "I've done some more thinking on the matter and, as far as I’m concerned, I still haven’t had my first."
    s "Really? Not even going to pretend you had your first with the girl you like just to make yourself feel better?"

    scene mollywind21
    with dissolve

    mo "The only thing that makes me feel better is gaming, Sir! And anime! That is all I need!"
    s "That’s so depressing."
    mo "Maybe! But this is the person I am! "
    mo "This is Molly MacCormack!"
    mo "And...if you don’t like that...Go dtachtfadh an diabhal thú!"
    s "Yeah. Gothafababable and dhtafghdadadad."

    scene mollywind22
    with dissolve

    mo "Pfft!"
    mo "Thank you for trying, Sir. I felt quite similar when I was learning Japanese. "
    s "I did my best. "
    s "But, on another note, I am done sitting on this bench. It is fucking cold."

    scene mollywind23
    with dissolve

    mo "Then...off to the original side quest we go!"
    mo "There were no physical rewards for this one, but I do believe we have increased our social link!"
    s "Yeah. And we’ve grown a little closer as well."

    scene mollywind24
    with dissolve

    mo "Oh, Sir...You still have so much to learn..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25p2 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump mollydorm25

label mollycafe30p1:
    scene mollyharukacafenight1
    with fade
    play music "cafe.mp3"

    "I wind up making it to the cafe shortly after closing as I got caught up in doing some things I don’t want to tell you about."
    "You see, I typically show you the most important parts of my day — and those parts almost always revolve around all of the girls I’m trying to have sex with."
    "But sometimes, other things happen to me behind the scenes that I think it’s best to omit as they would only confuse you."
    "Am I telling you the truth right now? Perhaps. "
    "But who would be there to fact check me if I wasn’t?"
    "For all you know (And for all anyone else knows) this little monologue might only be a hook meant to reel you in."
    "You won’t pay attention to me throughout the mundane happenings of my life if I don’t do something to make your heart beat a little faster every now and then, right?"
    "Do you like it when I strip myself of special text? "
    "Do you like it when I make your screen flash?"
    "Do you like it when I lead you into dark rooms with exchange students and award you affection points under the pretense that you will use them to get your dick wet?"
    "Of course you do, because you’re still here."
    "Now, follow these two out into the night in hopes that it will happen once more."
    "If it doesn’t, you can always jerk off into a sock."
    "- One of the narrators, or Sensei, or Selebus, or a bug, or something else, or all of those things, or you."
    "How does the hook feel nestled in your jaw?"

    mo "And that’s the story of when I let fifteen dudes fuck me in one night!"

    scene mollyharukacafenight2
    play music "likepigstopigwater.wav"

    h "I wish I had a penis so could fuck you toooooooo"

    stop music
    play sound "static.mp3"
    scene mollyharukacafenight3 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    scene mollyharukacafenight4
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene mollyharukacafenight1 with flash
    stop sound
    play music "cafe.mp3"

    mo "And that’s the story of when I solo’ed fifteen group-bosses in one night!"
    h "That’s very nice, Molly. But I would like to go home now."
    s "Hey. I’m here."

    scene mollyharukacafenight5
    with dissolve

    mo "Supreme Overlord? When did you come in? Actually, better question- {i}why{/i} did you come in? We’re closed. And we’ve {i}been{/i} closed for about half an hour."
    h "Did Molly forget to flip the sign again? "
    mo "I probably forgot to flip the sign again. I tend to rush things on Fridays so I can go home and watch anime."
    s "I didn’t really pay any attention to the sign. I just figured I was allowed in here whenever I want since I basically own the place."
    h "But...{i}I{/i} own the place."
    s "Yeah, but we’re best friends. Which means I pretty much own the place too."

    scene mollyharukacafenight6
    with dissolve

    h "We’re best friends? Since when? I thought Sara was my best friend."
    mo "Oh, okay. I get it, Sir. It’s not like hearin’ firsthand that Haruka means more to you than I do is a slap in the face or anythin’."
    h "Look, you made Molly pout. Molly never pouts."
    s "You’re {i}both{/i} important to me. "
    s "It’s just that my friendship with Haruka is {i}more{/i} important because it brings me one step closer to a lifetime of free coffee. No offense, Molly."

    scene mollyharukacafenight7
    with dissolve

    h "See, this is one more reason why my business is succeeding and Sara’s isn’t. I bet you pulled that same trick on her, didn’t you?"
    s "Hey, I pay there sometimes. It’s mostly just because I feel bad, though."
    mo "Unfortunately, Sir, if you’ve come here seeking coffee, I regret to inform you that our stock has been depleted. "
    mo "However, I do have a plethora of uneventful side quests I keep stashed in my back pocket for when adventurers like you are looking for something to-"
    s "So, how are things, Haruka?"

    scene mollyharukacafenight8
    with dissolve

    mo "For the love of- why doesn’t anyone ever want my quests?! It’s like the lot of you live your lives without thinking you have a hidden XP meter at the bottom of your HUD! Come on!"
    h "I mean...things are fine. Busy. Which is why I stayed and helped Molly close when I’m normally out of here by now."
    s "Yeah, I stopped by the other night and this place was packed. And, I know this might be a little hard to believe, but Molly was actually {i}working{/i} that night."

    scene mollyharukacafenight9
    with dissolve

    mo "You were there for that and didn’t even bother saying hello?! Am I just an NPC to you?!"
    s "Weren’t you trying to give me a quest like, thirty seconds ago?"
    mo "That-"

    scene mollyharukacafenight10
    with dissolve

    mo "Wait...maybe I {i}am{/i} an NPC. That would certainly explain why things progress for everyone else while I’m stuck here with the same habits and search history I’ve had since I was ten."
    h "I {i}know{/i} Molly was working that night. I thought she made a typo when she sent me the numbers after closing. I’m surprised she was able to handle that on her own."

    scene mollyharukacafenight11
    with dissolve

    mo "Oh, Rin was there to help. I got lucky. There’s no way-"
    h "Put your hands down, Molly."

    scene mollyharukacafenight12
    with dissolve

    mo "Theres no way I would have been able to handle that crowd on my own. "
    h "Either way, you held down the fort and I’m very proud of you for that."
    mo "Does this mean I’m being promoted to supervisor?"
    h "Absolutely not. But, if you don’t mind waiting an extra few hours to go home and watch anime, I wouldn’t mind buying you dinner to celebrate."
    mo "Buying me dinner? Are you...asking me out on a date?"
    h "Would it count as a date if I invited your teacher as well?"

    scene mollyharukacafenight13
    with dissolve

    mo "No...but it would certainly seem like the beginning to some sort of bonus event where our dynamic as a triad changes forever."
    s "Molly works hard and {i}I{/i} benefit from it? Count me in."
    mo "But I haven’t even said yes. There are three harems and a mech drama waiting for me in my dorm room right now."
    s "You’re that willing to just walk away from a bonus event?"

    scene mollyharukacafenight14
    with dissolve

    mo "Damn it, Sir! Stop using my words against me! You know bloody well I won’t be able to say no if you put it like that!"
    h "Make the correct choices and you might even unlock a sex scene. That's how those games work, right?"

    scene mollyharukacafenight15
    with dissolve

    mo "Are you legally allowed to say that to me as my boss?"
    h "Say what? I didn’t say anything. That was Sensei."

    scene mollyharukacafenight16
    with dissolve

    s "Am I legally allowed to say that as-"
    mo "Sir, if there’s anything I’ve learned from my time in dating sims, it’s that teachers can get away with anything. Games would be no fun if they were caught right before any of the CGs were unlocked."
    h "I picked the wrong profession."
    s "I think you should agree to this dinner thing, Molly. "
    s "Not just because I want food, but because Haruka seems to be in a type of mood right now that would only boil over into something extremely destructive if you didn’t."

    scene mollyharukacafenight17
    with dissolve

    mo "I don’t know, Sir. Wouldn’t an NPC like me just be getting in the way of your friendship with the Magistrate of Mammaries? Because it sounds like I’d just be an image variant at the end of the day."
    h "Oh, stop. If you’re not coming, there’s no point to any of this. I have nothing to reward Sensei for and the best friend thing is only an excuse he came up with for free coffee."
    mo "I don’t know...the mech anime I was talking about left off on a pretty big cliffhanger last week and I don’t want the Kendo Princess accidentally spoiling something for me again..."
    s "{i}Bonus event...{/i}"

    scene mollyharukacafenight18
    with dissolve

    mo "Gaaaah, fine! Damn this completionist brain of mine!"
    mo "But I swear, if I wind up bein’ forced to hide under the bed while the two of you go at it, I’m never playin’ another visual novel again!"

    scene black
    with dissolve2

    "Reluctant as it may be, Molly agrees to take Haruka up on her dinner offer and the three of us exit the store before heading over to the bus stop."

    scene nightsky
    with dissolve

    "After a short drive, we’re dropped off in Haruka’s neighborhood so she won’t have to walk very far after she drinks too much and loses feeling in her legs."
    "This is never verbalized, but I know it to be true as she has gotten hammered on several occasions now and has {i}consistently{/i} been a bad drunk."
    "In fact, so has Molly. "
    "So either tonight is going to be extremely loud and embarrassing for me-"
    "Or I am going to get tossed into a “special bonus CG” regardless of whether I want to be or not."

    scene mollyharukacafenight19
    with dissolve2

    mo "Um...don’t you think you may have ordered a little too much wine?"
    h "One of the bottles is for later."
    s "Yeah, who am I kidding? Of course you and Sara are best friends. I’d only get in the way of your soon-to-be liver disease."

    scene mollyharukacafenight20
    with dissolve

    h "I’m glad you understand."
    mo "Are you not going to drink, Sir?"
    s "Are {i}you{/i} not going to drink, Molly? The waitress didn’t seem to mind that you were underage based on...well, the fact that she offered you a drink as well."
    mo "I’ve decided it’s best for everyone if I just don’t drink anymore."
    h "You’re stronger than I am, Molly."
    s "Yeah, that’s probably for the best. I’ll hold off for tonight as well."
    mo "If it’s for my sake, Sir-"
    s "I’ll hold off for tonight as well."

    scene mollyharukacafenight21
    with dissolve

    mo "Oh...okay."
    h "Hey now, why the long face? I thought the “emotional climax of Molly MacCormack’s teenage years” or whatever it was you called it earlier had already come to an end."

    scene mollyharukacafenight22
    with dissolve

    mo "It...It is! And my face is no longer than normal! I just...I remembered a particular scene in a show I’m watching that...evoked the...memory of a debuff I..."
    mo "Anyhow, thanks for dinner! Let’s not talk about the previous stages of an NPC’s life!"
    h "How about the {i}future{/i} stages then?"

    scene mollyharukacafenight23
    with dissolve

    mo "Why do we have to talk about the NPC at all when you two are clearly the playable characters here?"
    h "Because you’re {i}not{/i} an “NPC.” You’re a good girl who’s passionate about her interests and has just fallen on some hard times. That’s all."

    scene mollyharukacafenight24
    with dissolve

    mo "That...That is perhaps the nicest thing you’ve ever said to me."
    s "It’s probably the alcohol talking. Or the fact that this actually is a date and I’m just here as her wingman."
    h "It’s neither of those things. I can be nice sometimes too, you know. If Molly was {i}really{/i} a thorn in my side, I wouldn’t let her work for me anymore."

    scene mollyharukacafenight25
    with dissolve

    h "I’m genuinely interested in what the next stage of your life will hold. I mean it."
    s "Just look at that face. She’s hitting on you right now and if you don’t pick up on that, all of those dating games were for nothing."
    mo "The Supreme Overlord makes a valid point. You do look like you’re about ready to pounce on me. But I will give you fair warning, my stamina is far too low to be worth it right now."
    h "Molly, I’m being serious. I’m rooting for you. It’s about time you got some sort of win in life."

    scene mollyharukacafenight26
    with dissolve

    mo "This sudden eruption of sentimentality is super effective and I suggest you slow down if you don’t want me fainting at the dinner table."
    h "Go ahead and faint. Sensei will carry you home."
    s "Hey, don’t rope me into this. I’m just here to eat and watch you two flirt."
    h "Why would {i}I{/i} be the one to flirt with Molly when you’re obviously next in line for her heart now that Rin’s out of the picture?"
    mo "Next in line? There is no queue for my feelings. This isn’t the Sims and I didn’t just go around right clicking on “flirt” with everyone in my line of sight."
    h "I’m not saying you did. But if you {i}were{/i} to pursue romance with anyone right now, who would it be?"
    s "Haruka, you’re making her un-"

    scene mollyharukacafenight27
    with dissolve

    mo "Probably...the Herald of the Adolescents..."
    h "Bingoooo. I know my work-daughters better than anyone."
    s "Uh..."

    scene mollyharukacafenight28
    with dissolve

    mo "That...uhh...doesn’t mean I’m planning on moving out of the common route or anything, though! I’m just simply stating that there isn’t really anyone else {i}in{/i} the make-believe feeling queue!"
    mo "And that if this were a game, which it is because everything is a game and that is why life is worth living, you would just so happen to be the closest person I have to...you know...a romance route..."
    s "Molly-"

    scene mollyharukacafenight29
    with dissolve

    mo "You don’t...have to tell me you don’t look at me that way, Sir! I’m already aware! I couldn’t be further away from your type. Just like..."

    scene mollyharukacafenight30
    with dissolve

    mo "Just like...how it was for Rin..."
    h "Look what you did."
    s "Me? You’re the one who started this. I literally just said I was only here to eat and watch you two flirt."
    h "Yeah, but if a girl starts getting down on herself in front of you, you’re supposed to say something. Not just sit there and let her fall deeper into the hole she’s digging."
    s "And {i}you’re{/i} not supposed to put people on the spot like that. What did you think was going to happen? That I’d jump over the table and kiss her?"
    mo "Weird...the event’s turning sour and we didn’t even have any options to choose from..."

    scene mollyharukacafenight31
    with dissolve

    h "I’m just saying, that’s how it is for {i}everyone{/i} in your class. They {i}all{/i} feel that way about you — not just Molly. It’s obvious to anyone that you’d be next in line for her."
    h "I didn’t mean anything bad by it and I didn’t mean to put either of you on the spot. I just figured it might be a boost in confidence for her to know that the guy she’s {i}interested{/i} in is at least somewhat-"
    mo "He’s not, though."

    scene mollyharukacafenight32
    with dissolve

    mo "Why {i}would{/i} he be? "
    mo "What do you get for falling in love with an NPC? They never change. Their whole purpose in the game is to move the actual players forward. "
    mo "Sir is the protagonist and I’m just a stepping stone. All that stuff about me becoming the main heroine is all talk because I know I’m not cut out for it."
    mo "Best chance I have is to wait for a fandisc that makes all the background girls like me more appealing to the masses."
    h "This is not the direction I was trying to lead this conversation in and I’m really sorry I brought anything up. "

    scene mollyharukacafenight33
    with dissolve

    mo "Don’t worry about it, Magistrate. You’ll not be faulted for lacking clairvoyance. There are some things about me that even you do not understand."
    mo "Let’s just...get back to talking about non-Molly things because Molly-{i}centric{/i} things always seem to bring everybody down! But that’s a problem with {i}her,{/i} not everyone else."
    s "It’s not a problem with {i}you.{/i}"

    scene mollyharukacafenight34
    with dissolve

    s "You’re not doing anything wrong. You’ve never {i}been{/i} doing anything wrong."
    s "The game you’re playing is just really hard."
    mo "You’ve got that right, Sir. I haven’t even figured out the controls yet."
    s "Me neither, and you haven’t been playing even {i}half{/i} as long as I have."
    s "It’s a weird situation when {i}Haruka{/i} is the one at the table who has the most of her shit together."

    scene mollyharukacafenight35
    with dissolve

    h "Hey! Don’t compliment me and insult me at the same time! I don’t know how to process that!"
    mo "Perfection only exists in fan-fiction. And also Cyberpunk: Edgerunners. "
    mo "Your flaws make you beautiful, Haruka."

    scene mollyharukacafenight36
    with dissolve

    mo "And your breasts amplify it."
    h "Oh, come on..."
    mo "I hope to one day be as powerful as you."
    h "Yeah, we’ll see how you feel about that once the back problems start kicking in..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Somehow, we manage to avoid further tragedy and carry on with dinner without hurting one another again."
    "But along the way, I realize just how endangered Molly is. "
    "For while I wasn’t looking, she got my hook caught in her mandible."
    "And her only options at this point are to either wait for me to free her-"
    "Or to be captured and consumed."
    "Which would you rather see?"
    "I know the answer."
    "Because you’re the same as her."
    "And I love the way you taste."

    $ renpy.end_replay()
    $ mollycafe30p1 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump mollycafe30p2

label mollycafe30p2:
    scene nightsky
    with dissolve2
    play music "molly.mp3"

    "After that, the night refuses to end."
    "Though, I suppose it would be a bit more accurate to say that two of us would be extremely irresponsible if we let it."
    "For, just as expected of a woman who ordered two bottles of wine, Haruka leaves the restaurant in a state of disrepair- and it falls on Molly and me to make sure she gets home safely."
    "It would have been simple to leave her lying there in the gutter, but then two of my students would be without jobs in the morning and my chance of co-owning a coffee shop would be all but null."
    "So, instead of allowing her to follow in the footsteps of that one poet who paraphrased that one politician that I told you about years and years ago- we return her to her rightful place."
    "But that place is wrong for the rest of us."

    scene mollyharukahome1
    with dissolve2

    h "I’ll have...one more glass of...chardonnay, please!"
    mo "That item is on cooldown. You will have a cold shower and flask of sobriety. Which is also known as coffee — a thing I am assuming you have in your home based on your profession."

    scene mollyharukahome2
    with dissolve

    h "Molly...do you...{i}hic...{/i}think I’m pretty?..."
    mo "Right now, the only thing I can think of is how regretful I am to have ever stooped to your current level in the past."
    h "Because I think {i}you’re{/i} pretty! And I think everyone who {i}doesn’t{/i} want to have sex with you is {i}hic...{/i}a fucking loser!"
    mo "That’s somewhat reassuring as it would mean the amount of losers in our class greatly surpasses just me."
    h "Lessgo...to my room...and I’ll make a...{i}hic...{/i}real woman outta ya..."
    s "Have fun, Molly. I’ll wait out here."

    scene mollyharukahome3
    with dissolve

    mo "As if I’d take her up on that! I’m playing the light path on this run and taking advantage of women in a drunken stupor is something only Dark Molly would do!"
    mo "Also, why do I have to be the one carrying her?! Your level is much higher than mine and, need I remind you, I main a healer!"
    s "Reminding me of things I don’t really get isn’t going to do much. Also, it’s safer if you’re the one carrying Haruka based on...prior history I have with her in that state."
    mo "{i}Sir...{/i}you didn’t."

    scene mollyharukahome4
    with dissolve

    h "Your teacher’s a...really good kisser, you know! You should try it!"
    mo "But...your husband-"

    scene mollyharukahome5
    with dissolve

    h "Let’s all make out on my bed! I volunteer to teach Molly! And it won’t be illegal because I’m her boss!"
    mo "I can’t believe I skipped out on watching anime for this."

    scene mollyharukahome6
    with dissolve

    h "Stop pretending you’re not {i}hic...{/i} a little interested when our {i}hic...boobs{/i} have been touching this whole time!"
    mo "I...have noticed. "
    s "She’s not going to stop until she gets some sleep, just to let you know. No amount of coffee or cold showers can force the horny out of Haruka."

    scene mollyharukahome7
    with dissolve

    mo "Sir, you and the Magistrate may both have several years on me, but I can assure you my knowledge of “the horny” far surpasses my age. "
    mo "I have several addictions I am not very proud of."
    s "It’s a little more than {i}several{/i} years, but thank you for not making me feel as old as everyone else does."
    s "Now, go put your horny boss to bed before our bonus CG is one that we’ll look back on with regret."

    scene mollyharukahome8
    with dissolve

    mo "T’at’s what I’m feckin’ tryin’ ta’ do and all ye’ve done ta’ help’s sit around wit’ ‘yer cock in yer hands!"
    s "Don’t get Irish with me, young lady. You have a job to do."

    scene mollyharukahome9
    with dissolve

    mo "Fackin’...Haruka! Move ‘yer arse! Ye’ know it’s serious when even Molly MacCormack has had enough of the games!"
    h "Are you suuuuuure you don’t wanna mess around with me? I won’t tell anybody! It’ll be a {i}hic...{/i} lil’ secret!"
    mo "Yes! The quest ends at droppin’ you off in bed! There ain’t any more to it!"
    h "Not even if I got a free Sybian from Maki last moooooonth~"
    mo "I don’t care about ‘yer feckin’-"

    scene mollyharukahome10
    with dissolve

    mo "Wait...really? "
    h "Want me to...{i}hic...{/i} teach you how to ride it?..."
    mo "..."
    h "Weeeeeeell?..."

    scene mollyharukahome11
    with dissolve

    mo "Gah! Yes! But you’re still drunk as all Hell and I’m apparently the responsible one tonight, so I can’t! "
    mo "I wouldn’t mind a referral to this Maki person, though! I have more than enough open slots in my friends list for a connection like that!"

    scene black
    with dissolve2

    mo "Sir, wait out ‘ere. Lord knows what’ll happen next if ya follow the two of us into the Magistrate’s lair."
    s "See, this is exactly why I wasn’t helping you. I’m glad you finally understand."

    "Molly somehow manages to get Haruka moving again and I head into the living room to wait out...whatever it is that’s going to happen in her bedroom."
    "And while I absolutely {i}do{/i} want to follow them in there-"

    stop music
    play sound "static.mp3"
    scene lavendersgreen28 with flash
    stop sound

    "it is for the best that i don’t"

    play sound "static.mp3"
    scene mollyharukahome12 with flash
    stop sound
    play music "molly.mp3"

    mo "Christ almighty, it’s like heroic Spine all over again. "
    mo "I’ve led my share of cracked out parties in the day, but this may have just been my greatest challenge yet."
    h "S...Sybian..."

    scene mollyharukahome13
    with dissolve

    mo "Drink ‘yer water, damn it! That’s twice ‘ye made me look like a buffoon in front of the Herald tonight!"
    h "Why don’t you just...{i}hic...{/i}go for it if you want him so bad? There’s no harm in trying, is there?"

    scene mollyharukahome14
    with dissolve

    mo "Hah..."
    mo "‘Tis true that Sir probably wouldn’t hold it against me if I {i}did,{/i} but things are a bit more complicated than that."
    h "Complicated...shmomplicated...You wanna fuck him, don’t you? Be honest..."
    mo "I..."
    mo "Have toyed with the idea of experimenting with him. But it was {i}he{/i} who planted that idea in my head."
    h "What’s the problem then?...Just do it...You can even use my couch if you want..."

    scene mollyharukahome15
    with dissolve

    mo "I think that zeppelin may have already departed."

    scene mollyharukahome16
    with dissolve

    h "Yeah, well...there’s Greta Van Fleet now, so..."
    mo "I’m...still not fully over Rin. But I’m moving on now, and it’s true that I {i}am{/i} interested in the Supreme Overlord...it’s just..."
    mo "I don’t think {i}he’s{/i} interested in me. In fact, I {i}know{/i} he’s not interested in me as he still can’t hold eye contact the way he used to."
    mo "He’s never been good at that to begin with, but ever since that Halloween it’s just..."
    h "Hallo.......ween......"
    mo "Do you think we can ever go back, Haruka?"
    mo "Do you think it’s possible for a relationship that was so damaged to be repaired when you’ve still not even figured out the true {i}cause{/i} of that damage?"
    mo "All my gold goes to PNGs and I’m running out of resources to tackle this never-ending repair bill. "
    mo "Some nights, I think it might be better to just swap sets entirely. Maybe use cloth armor or something. "
    mo "Other nights, I think of trying a whole new game entirely."
    mo "But there’s one person I keep wantin’ to play with and that person just..."
    mo "Doesn’t like games."
    mo "Or {i}me.{/i}"
    h "..."
    mo "..."
    mo "You’re asleep, aren’t you?"
    h "{i}Just......like that.........Tsuneyo.....{/i}"

    scene mollyharukahome17
    with dissolve

    mo "Um...{i}what?{/i}"
    h "{i}It’s okay...you can bite it, baby...it won’t hurt me...{/i}"

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    mo "Okay! That’s enough of that. What happens in my boss’s room stays in my boss’s room and I never heard any of it."

    "........."
    "......"
    "..."

    scene mollyharukahome18
    with dissolve2

    mo "Hah..."
    mo "I’d seen her drunk before, but never like that. That was just a step or two away from “A Night to Remember” level tomfoolery."
    s "Well, based on what I assume Haruka said to you in there, I have a hard time believing this is a night you’ll soon {i}forget.{/i}"
    mo "It likely wasn’t what you think, Sir. Her sexual propositioning of me stopped once I laid her down. "

    scene mollyharukahome19
    with dissolve

    s "Yeah...I’m more or less talking about what I expect she said to you {i}after{/i} her propositioning ended."
    mo "Sir?"
    s "..."
    mo "Sir, you can talk to me. I hope you know that."
    s "Am I really the...next in line or whatever?"
    mo "Next in line?...Are you referring to what Haruka said at dinner?"
    s "And probably again behind closed doors just a few minutes ago. "
    s "I know her pretty well at this point. She’s more gung-ho about me banging teenagers than even {i}I{/i} am sometimes."

    scene mollyharukahome20
    with dissolve

    mo "You mean...{i}other{/i} teenagers."
    mo "Not me."
    s "I should be the last person in whatever that {i}line{/i} is, Molly. We both know that. "
    mo "Except we don’t. "
    mo "And every time we’ve tried talking about it, we’ve settled on how we {i}don’t.{/i} Which is precisely why I’m so confused, Sir."
    mo "Granted, I was confused before any of this even began. And you were close enough to catch onto that confusion and offer to help me learn things about myself I’d been nervous about learning."
    s "Is that why you like me so much? Because I’m {i}close?{/i}"

    scene mollyharukahome21
    with dissolve

    mo "Not at all, Sir. You’re not at the front of the line for showing up earlier than anyone else- you’re at the front of the line for caring about me and appreciating me in ways no one else has."
    s "Tsuneyo appreciates you. The rest of the manga club appreciates you. And even if things are weird with Rin, I’m sure she appreciates you on some level as well."
    s "But none of those people ever took advantage of you while you were unconscious in a dark room."
    mo "{i}Stop going back to that.{/i} "
    mo "It’s over."
    mo "Sir, if you’re not attracted to me, just say it. I’ve had trouble accepting that in the past, but the context this time is obvious enough that I won’t be able to blow it off again."
    s "That’s not the problem, Molly."

    scene mollyharukahome22
    with dissolve

    mo "Then what is it that makes me different from everyone else? "
    mo "I ask this not just as someone who wants to be closer to you, but as someone who has {i}always{/i} been different in the first place."
    mo "Is it my interests or hobbies that make me undesirable? Is it my hair? My skin? "
    mo "I need to know these things so if I ever {i}do{/i} decide to pursue romance with a real human being, I’ll understand what sticks out the most."
    s "It’s me. I’m the problem."
    mo "That’s a cop-out answer the protagonist gives to a side character who didn’t make it onto the box art. What is the {i}real{/i} one?"
    s "..."
    mo "Do you..."
    mo "Do you still want to help me experiment, Sir?"
    mo "Because Haruka won’t be waking up for a long time and- can you please look at me when I’m speaking seriously with you? "
    mo "My moments of true maturity are rare...but they exist, Sir. And this is one of them. "
    s "Just...pick someone else who's less capable of hurting you."

    scene mollyharukahome23
    with dissolve

    mo "It is {i}I{/i} who chooses what does and does not hurt me, Sir. Not you."
    mo "I may be a frail Irish lass who burns after five minutes of exposure to the sun, yes-"
    mo "But I’m the daughter of a single parent, who experienced loss in the worst way possible...Who’s lived her whole, albeit very short life as both an outcast and the center of attention {i}everywhere.{/i}"
    mo "I may hide away in fiction from time to time because it makes things easier, but I’m strong enough to survive on the outside when I need to."
    mo "Let what happened in the dark {i}stay{/i} there...It doesn’t matter if it was the worst thing possible or nothing at all."
    mo "Because, Sir...and this is embarrassing to admit...but if I were to walk into a room just like that today...there is no one I would rather have follow me in than you."
    mo "Or maybe Felicia Day."
    s "I don’t know who that is."
    mo "Sir, answer me honestly-"
    mo "If I were to make a move right now, how would you react?"
    s "..."
    mo "Because I’m going to."
    mo "And this is the part where you make a decision that changes the rest of our relationship. "
    s "Molly..."
    mo "How will you react?"

    stop music

    menu:
        "Rape her":
            play sound "static.mp3"
            scene mollyharukahome24 with flash
            stop sound

    s "I think you should sleep here tonight. I can’t walk you home."
    mo "Sir! Wait! You don’t have to leave! You can just say no!"
    s "You never got to say no."

    scene mollyharukahome25 with dissolve

    mo "It’s okay if you’re uncomfortable! I just wanted to know if-"

    play sound "dooropen.mp3"

    s "Goodnight, Molly."
    mo "Sir..."

    scene mollyharukahome26
    with dissolve

    mo "Tch..."
    mo "Damn it...Damn it, damn it, damn it..."
    mo "Can’t you see this is exactly what I meant when I put you before everyone else?..."
    mo "As if any of the others would ever look that way for me..."

    scene black
    with dissolve2

    mo "Why do humans have to be so hard?..."

    play sound "static.mp3"
    scene park_night with flash
    stop sound

    s "She didn’t mean that."
    s "She’s confused."
    s "She doesn’t know what she wants."
    s "She’s just a hormonal teenage girl."

    scene black
    with dissolve2

    s "But if that’s true..."
    s "What is it that makes the others different?"

    "I try to fall asleep on a park bench, but I keep thinking of Molly."
    "I think about how Molly wants me."
    "I think about what I want to do to her."
    "But for some strange reason-"
    "I still want to run away."

    play sound "static.mp3"
    scene bedroom_night
    with flash
    stop sound

    "The hook under my desk reels me back to safety and I don’t have to run at all."
    "I end the night by jerking off into an orange sock."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mollycafe30p2 = True
    $ molly_love += 1
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day += 1
    hide friday onlayer date
    show saturday onlayer date

    jump mollydate35p1

label mollydate35p1:
    scene bedroom_day
    with dissolve4

    "Morning comes. "

    play sound "phonering.mp3"

    "And I receive a phone call."

    s "..."

    play sound "phonebeep.wav"

    s "Hel-"

    with hpunch
    play music "justbehappy.mp3"

    mo "Bal'a dash, malanore! Doral ana'diel?"
    s "Sorry, wrong number."
    mo "How goes it, Sir? How fares thee?"
    s "I would have liked to have slept a little longer before being woken up by whatever your language is called again."
    mo "Irish. Or Gaelic. Technically Irish, but only because the damn Scots {i}stole{/i} Gaelic and we just keeled over and let ‘em. "
    mo "But what I was speaking just now was actually Thalassian- the language of the blood elves. Selama ashal'anore! Justice for our people!"
    s "Why are you calling me?"
    mo "Because I refuse to have our rank drop down {i}again{/i} just because you’re not attracted to me!"
    mo "Also, I require aid- for my quest today is significantly harder without someone there to support me and the Kendo Princess has other matters she must tend to."
    s "I don’t-"
    mo "Anar'alah, Sir! Act ‘yer feckin’ age! The Supreme Overlord I know isn’t perturbed by the presence of teenage girls! He steals their life force and converts it into mana!"
    mo "So we had an awkward night! Big deal! {i}Every{/i} night is awkward when you’re me and you’ll never survive in the outside world if you can’t come to terms with that!"
    s "You are probably the last person I want to lecture me on how to survive in the outside world. "
    mo "Well, stop making amateur mistakes and I won’t have to keep bringing up tooltips! You did this to yourself!"
    mo "How quickly can you make it to Silvermoon?"
    s "I...have no idea where that even is."
    mo "Eversong Woods, just north of the East Sanctum."
    s "Are we traveling to an alternate dimension?"
    mo "God, I wish. An isekai is exactly what I need right now. Preferably one where I’m extremely overpowered and have an entire harem at my disposal."
    s "Sounds exhausting."
    mo "You would know, Sir. So, can you make it to the Entertainment District within the hour? Or should I open a portal to your home and retrieve you along the way?"
    s "I can head over...but I’m still not sure if-"
    mo "Excellent! Shorel'aran, Sir! I’ll see you soon!"

    play sound "phonebeep.wav"

    s "...that’s a good idea."

    scene sky
    with dissolve2

    "Molly hangs up the phone and, despite the sudden return of my uneasiness when it comes to being around her (Thanks, Haruka), I get dressed and start heading over to “Silvermoon.”"
    "It’s annoying, though. Things were going completely fine until the invisible girl-magnet inside of me started pulling Molly over. And it’s annoying that I’m so aware of that as well. "
    "I want more than anything to return to the blissfully ignorant me who would have fucked her on Haruka’s couch prior to our dramatic fallout two Halloweens ago."
    "I want to see her the way she {i}wants{/i} me to see her...and carry through with those lust-driven ideas I proposed to her way back when."

    stop music
    play sound "static.mp3"
    scene lavendersgreen6 with flash
    stop sound

    "But all I can see when I’m alone with her is this."

    play sound "static.mp3"
    scene mollydressingroom1 with flash
    stop sound
    play music "justbehappy.mp3"

    mo "Greetings, Sir! Thank you for clearing out some room in your quest journal. Your assistance is invaluable and I appreciate you in an entirely platonic, not-at-all sexually driven way!"
    s "Okay, I guess we’re already going there."
    mo "Not at all, Sir! You made your stance loud and clear last night! And the new and improved Molly MacCormack has taken several precautions to ensure she doesn’t make you uncomfortable again!"
    s "Well, you’re off to a pretty rocky start. So, what are we doing? Why did you need me?"
    mo "I need your help trying on clothes."
    s "Mission failed."

    scene mollydressingroom2
    with dissolve

    mo "Geh! The worst words any gamer could ever hear!"

    scene mollydressingroom3
    with dissolve

    mo "...is what I {i}would{/i} be saying if I wasn’t a genius who had already taken that into consideration!"
    s "I’m listening..."
    mo "The fact that you are so wholly opposed to physical contact with me at this point makes you the {i}perfect{/i} dressing room partner, Sir!"
    mo "We’re here on {i}strictly{/i} business! We’ve eliminated the risk for lewd behavior and are free to focus purely on making me the best Molly I can be!"
    s "Is that “best Molly” just normal Molly dressed up as and pretending to be someone else?"

    scene mollydressingroom4
    with dissolve

    mo "Exactly! I knew calling upon you as my backup was the right choice, Sir."
    s "Even if any of that is true, you seem to be forgetting the part where I am an adult male and you are a young girl. No one is going to let me into a dressing room with you."

    scene mollydressingroom5
    with dissolve

    mo "They will if we’re dating."
    s "Molly-"
    mo "Hear me out-"
    s "I’m trying to. But it seems like every single step you’re taking to make things {i}less{/i} weird is somehow making them {i}more{/i} weird."
    mo "If tact and subtlety will not work, which they never seem to for me, I must change directions entirely! Now come, dalah'surfal!"
    s "And what does “dalah'surfal” mean, exactly?"
    mo "Lover."
    s "I’m going home."

    scene mollydressingroom6
    with dissolve

    mo "Fine. I’ll just have to ask some random person off the street if they want to follow me into a dressing room and take my clothes off. I’m sure {i}that{/i} will work out perfectly."
    s "The fact that you’re not worried about me is perhaps the most concerning element of all of this."

    scene mollydressingroom7
    with dissolve

    mo "Sir, you have seen me in ways more intimate than anyone. "
    mo "You have caught me with my pants down, you’ve rejected my advances, {i}and{/i} you’ve ejaculated on me. "
    mo "I do not care at this point if you see me in my underwear. {i}Especially{/i} when you have no desire to touch me. "
    s "This is so weird."
    mo "What’s weird is how weird you’re making it. How messed up do things have to get for {i}me{/i} to be the one trying to normalize them? "
    mo "We’re friends, aren’t we? Just help me zip some zippers and tie some bows. It’s not like I’m asking you to bend me over a stack of props and spank me ‘til my arse is red."
    s "But what if I-"
    mo "I trust you, Sir. And I highly, {i}highly{/i} doubt you will do anything to hurt me."

    scene mollydressingroom8
    with dissolve

    mo "But, on the off chance you do, I consent to everything. Now, no one has to feel guilty if anything does happen."
    s "What did Haruka say to you after I left last night?"

    scene mollydressingroom9
    with dissolve

    mo "Nothing. But, if she happens to ask about anything missing from her closet, I was never there."
    s "What did-"
    mo "That’s for me to know and you to be entirely disinterested in, Sir."
    s "..."

    scene mollydressingroom10
    with dissolve

    mo "Now, then! Shall we go, dalah'surfal? "
    s "Fine. But I’m staying ten feet away at all times when I don’t have to “zip zippers or tie bows.”"
    mo "Look at that! Substantial character development in one measly conversation! Turns out dumping points into speech {i}does{/i} help after all!"

    scene black
    with dissolve2

    "Molly subsequently drags me into several stores, each one specializing in different types of paraphernelia- whether it be wigs, makeup, or materials."

    scene mollydressingroom11
    with dissolve

    "But it isn’t until we make it to the fourth store that I’m put on the spot, as this one seems to specialize in premade costumes."
    "Which means of course, that in a matter of minutes, I’m going to be behind closed doors with a girl I have a history of preying upon in a...way I’ve decided is less acceptable than the way I prey upon others."
    "It’s a little confusing considering that Molly is essentially lying on her back with her legs up at this point in an act of pure submission-"
    "But it doesn’t change the way I feel."
    "I wish it would."
    "But it doesn’t. "
    "And I’m not sure what (if anything) will."

    mo "Anything in particular you’d like to see me in, Sir? Ami has informed me of an affinity you seem to have for Sailor Scouts and I must say I make an excellent Venus."
    s "I have no idea what Ami is talking about and you should never listen to anything she says because it is probably just an attempt to sabotage you in some way."
    mo "A true yandere in the making, it seems. But will it be {i}she{/i} who crosses the line first? Or will someone else put their foot down before her?"
    s "Probably Ami. I can’t see anyone else ever going that crazy."
    mo "Not even the likes of Noriko? Or maybe a hidden candidate like Sana or Miss Watabe?"
    s "Miss Watabe is in a committed relationship with a girl who could kick my ass. And despite recent occurrences, I still believe Sana is an angel."
    mo "I see you’ve yet to refuse Noriko."
    s "Noriko will probably just cry and masturbate."

    scene mollydressingroom12
    with dissolve

    mo "I knew I liked her."
    s "Just pick whatever you want. I don’t really care. "
    s "Maybe avoid things with too many zippers or ties, though. "

    scene mollydressingroom13
    with dissolve

    mo "Hmm...I guess that rules out anything Square Enix has ever touched..."

    scene black
    with dissolve2

    mo "Oh! I know! "
    mo "This way, Sir. I’ve been here before. I know where I’m going."
    s "I am somehow not surprised."

    "Molly proceeds to grab several costumes off of the racks, never checking the sizes of anything as I’m sure she probably wants to make adjustments to them anyway."
    "After her hands are full, she tosses everything she picked up to {i}me{/i} as this is apparently the job I signed up for before going out of her way to grab even {i}more.{/i}"
    "I have no idea how long she anticipates this ordeal taking but, based on the amount of clothes we’re both holding and how complicated they all appear to be-"
    "I think we’ll probably be ready to leave by sometime next month."

    scene mollydressingroom14
    with dissolve2

    mo "Hmm..."
    mo "Sir, based on visuals alone, do I strike you as the more innocent type? Or do I come across as a more...closet-pervert type of character? I’m branching out from the chuuni stuff, you see."
    s "I know too much about you to not take into account the type of person you actually are, which is 100%% a pervert. No closet involved."
    mo "I said {i}visuals{/i} only, Sir. Stop metagaming."
    s "I just told you I {i}can’t{/i} do visuals alone. I’ve seen too much."

    scene mollydressingroom15
    with dissolve

    mo "Oh well. I’ll just have to try everything. "
    s "Everything? You grabbed like fifty outfits."

    scene mollydressingroom16
    with dissolve

    mo "And I grabbed them for a reason. You don’t go shopping with-"

    scene mollydressingroom17
    with dissolve

    mo "Hey! I get that you’re not attracted to me, but isn’t it a little rude to shield your eyes when I’m taking my clothes off?"
    s "Wouldn’t it be more rude to {i}not{/i} do that? You made me turn around the last time you got dressed, didn’t you?"
    mo "Yeah, but that was well before you busted a load all over my most expensive cosplay to-date. {i}Now,{/i} I’m just offended."
    s "Just tell me when you need zipper assistance. I’ll stay like this in the meantime."

    scene mollydressingroom18
    with dissolve

    mo "{i}Hah...{/i}how are you supposed to judge my cosplays if you won’t even look at me?"
    s "Is “girl in underwear” one of your cosplays? "
    mo "Sir, that’s like 10%% of {i}all{/i} cosplays. Sex sells and you should know that better than anyone as the lead character in an H-game. "
    mo "Or at least the {i}former{/i} lead character in an H-game. Right now, you seem like every other dense harem protagonist out there."
    s "I’ll look at you when you’re finished getting dressed. Doing it now would be...trouble."
    mo "Ooooh? What {i}kind{/i} of trouble, Sir? Are you actually attracted to me after all?"
    s "I’ve been telling you this whole time that I am. Why is that so hard to believe?"
    mo "Maybe it has something to do with the fact that you are not seizing this extremely precious opportunity to see me in the truest of my elements."
    s "I’m good. But thanks."

    scene mollydressingroom19
    with dissolve

    mo "Fine! But don’t come cryin’ to me years down the line when you’re missing one CG and have to play the whole damn game all over! A true completionist would watch me get dressed!"
    mo "And then...probably do other things to me as well! But I will admit that I am less prepared for that now than I was half an hour ago!"
    s "Are you dressed yet?"

    scene mollydressingroom20
    with dissolve

    mo "Yes. I am."

    scene mollydressingroom21
    with dissolve

    s "Great. Then-"
    mo "..."
    s "..."
    mo "Was that so hard?"

    scene mollydressingroom22
    with dissolve

    s "Not really. But I’m going to keep doing this anyway."
    mo "Guh. The old you was much better at boostin’ my confidence, Sir. This one just makes me feel like a gremlin."

    scene black
    with dissolve2

    "Molly stops pestering me to stare at her in her underwear and I do a mostly-successful job at judging her cosplays as time goes on. "
    "The reason I say “mostly-successful” is that I give essentially the same feedback for all of them — cute. Or hot. "
    "Or both cute and hot. "
    "But despite how limited those descriptions are, she seems to go along with it and thanks me for my assistance each time. "
    "Most of the bows on her outfits come pre-tied, but there are several zippers I need to help with. Thankfully, she remains steady enough that I never really come into contact with her flesh. "
    "Which is good because I’d be lying right now if I said I wasn’t extremely tempted to take advantage of her “consent to everything” pass from earlier."
    "I’m just as unsafe in here as I thought I’d be."

    mo "Okay...last one, but..."
    mo "This is, uhh..."
    mo "This one’s a little embarrassing..."

    scene mollydressingroom23
    with dissolve2

    mo "..."

    "I am even more unsafe in here than I thought I’d be."

    mo "The skirt on this one is a little...shorter than I expected it to be..."
    mo "So much so that I should probably just skip the turning-around part of the modeling phase. "
    s "You’re nervous in a short skirt but...{i}not{/i} your underwear?"

    scene mollydressingroom24
    with dissolve

    mo "Well...yes! I’m sure it sounds strange to you, but being in an outfit like this where you’re {i}not{/i} supposed to see those parts of me is way more embarrassing than being in one where you {i}are!{/i}"
    s "I don’t get it."
    mo "Neither do I, but that’s just how it is! And it also doesn’t help that I have a great deal of inappropriate artwork of this character saved on my computer!"
    s "Well, it’s...cute."
    s "And hot."

    scene mollydressingroom25
    with dissolve

    mo "Where would it rank compared to the other outfits I wore today? "
    mo "I’m trying to coordinate what our next group cosplay should be, but I didn’t want to go through with making a whole costume from scratch for something that might not work for all of us."
    s "I’d put all of them in whatever the highest tier is. But I think I just have a thing for costumes, so..."

    scene mollydressingroom26
    with dissolve

    mo "That doesn’t really help me much, Sir."
    s "I didn’t think it would. But frankly, I can’t see how Tsuneyo would have been any better at this."
    mo "She’s more or less just as helpful as you are. But the added benefit of bringing Tsuneyo is that I get to dress her up as well. And I have a sneaking suspicion you wouldn’t let me take {i}your{/i} clothes off."
    s "I have a sneaking suspicion that doing that would be a horrible decision, Molly."

    scene mollydressingroom27
    with dissolve

    mo "R-Really?..."
    mo "But things went perfectly fine with you watching {i}me...{/i}"
    s "Except I didn’t really watch you. And it’s significantly harder to conceal certain parts of my body when I am not wearing pants."
    mo "I...don’t mind. "
    mo "I’ve seen enough of them in porn to...not be bothered by that kind of stuff. And I think dressing you up would be really fun..."
    s "That is the complete opposite of what your cheeks are saying. Also, I don’t “dress up.” If I’m taking my clothes off, it’s for one reason. Well, two counting bathing."

    scene mollydressingroom28
    with dissolve

    mo "That said, Sir..."
    mo "Would you mind maybe...helping me take this costume {i}off?{/i}"
    s "..."
    mo "..."
    s "What happened to entirely platonic and not-at-all sexually driven?"
    mo "I’m a pervert, Sir. I tried."
    s "Did you really, though?"
    mo "For a little while. This was more exciting than I thought it was going to be."
    mo "It wasn’t horrible, though...was it?"
    mo "You seem like you’re still doing fine...and I’m..."

    scene mollydressingroom29
    with dissolve

    mo "Also {i}fine...{/i}"
    s "You don’t look fine."
    mo "I’m not fine."
    s "..."
    mo "..."
    s "I should go."

    scene mollydressingroom30
    with dissolve

    mo "Sir-"
    s "It wasn’t horrible. You’re right. And under different circumstances, I’m sure we’d be doing something completely different right now."
    mo "So, then...what’s the-"
    s "I just need a little more time, Molly. "
    s "But if you keep being this annoying and pushy and forcing me into situations where you know I’m going to get turned on, it might not be {i}as much{/i} time as I currently expect."

    scene mollydressingroom31
    with dissolve

    mo "That wasn’t...{i}exactly{/i} my intention. Just a positive side effect that I thought might happen if I got lucky."
    s "Well, you did. But now I’m going to step out because I am still grappling with the basics of self-control and don’t want all of my excruciating efforts to have been for nothing."
    mo "Aye aye, Sir..."
    mo "I’m sorry I keep doing things that make you want to run away."
    s "Don’t be."

    scene black
    with dissolve2

    s "Because I can assure you that you’re doing even more to pull me forward..."

    $ renpy.end_replay()
    $ mollydate35p1 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump mollydate35p2

label mollydate35p2:
    scene mollytrain1
    with dissolve2

    "Today has been...eventful if nothing else."
    "And while I’d like to take this time to pat myself on the back for not violating Molly, the day is not yet over."
    "There is still plenty of time for me to make a horrible, impulsive decision that will, once again, lead me spiraling downward until the possibility of ever returning to the surface disappears once and for all."
    "She’s making it easier, though."
    "Which is strange considering that everything she’s done today has been making something {i}else{/i} harder, but...I guess that was kind of the point."
    "Of course talking wouldn’t have a substantial effect on me when my experience with it is almost entirely impure."
    "But convincing me that I can do no wrong at this point plays right into my ego. "
    "There was an experiment some twisted scientist did a long time ago where he or she would shock some sort of animal any time it went to take a bite of food. "
    "Whatever that animal was became so scared of that food that it was forced to either starve itself or endure the shock in order to eat."
    "It starved itself — which is precisely what I’m doing right now."
    "But the food has grown legs and keeps coming closer- and I am a natural predator who is not known for my ability to stave off temptation."
    "I can only starve myself for so long before the urge to survive kicks in and I push through the preconceived pain to take what I want."
    "All I ask is that you keep shocking me every now and then so I do not grow fat and complacent."
    "And that you stop giving me my favorite treats."

    mo "I never realized just how packed these subway cars can get until I moved here."
    mo "I’d seen rush hour depicted in anime and manga, but had always just assumed that things were being blown out of proportion as it wasn’t ever even {i}close{/i} to this where I’m from."
    s "Do they have subways in Ireland?"
    mo "There are commuter trains, but even the ones in busy places like Dublin are above ground."
    mo "Everyone just drove where I’m from. The population wasn’t dense enough to warrant anything like this."
    mo "Things may have been different the closer you got to the city but, being from a small town, things like packed subway cars stay kind of surprising no matter how many times I see or live through it."
    s "Well, you’re doing a good job of blending in. If it weren’t for your appearance, I probably wouldn’t even realize you’re not from around here."

    scene mollytrain2
    with dissolve

    mo "{i}Neither{/i} of us are doing a good job blending in since we’re the only ones talking right now, Sir."
    mo "We’re supposed to mind our own business and quietly hate ourselves on the subway. That is one of the first things I learned when I moved here."
    s "Why Kumon-mi anyway? Why not Tokyo or something? That seems to be the hub for most foreigners."
    mo "Yes, which is precisely {i}why{/i} I didn’t move there. It would have been too easy, Sir."
    mo "Coming somewhere like Kumon-mi, where outsiders are extremely limited, was a way for me to challenge myself to become better."

    scene mollytrain3
    with dissolve
    stop music fadeout 15.0

    mo "It would have been nice if they made it a {i}little{/i} easier for foreigners to find housing, though. Thank Mara for the dorms. Saves me from having to sleep in the sewers."
    s "And who is Mara exactly?"
    mo "The goddess of love in the Imperial Pantheon of the Nine Divines."
    s "Maybe choose one of the other eight since love hasn’t really seemed to be an area of success for you thus far."

    scene mollytrain4
    with dissolve

    mo "Thank you for reminding me, Sir. As if you hadn’t already done that an hour-"

    scene mollytrain5
    with hpunch
    play sound "tackle.mp3"

    mo "Ago?!"
    s "Hey, come on. There’s plenty of room-"
    train "Shh!"
    mo "Oh God...I’m in one of {i}those{/i} games."

    scene mollytrain6
    with dissolve

    s "Molly...sorry, but I-"
    mo "Shh!"
    s "What? You too?"
    mo "Don’t talk."

    play music "trainnoise.mp3" fadein 3.0

    mo "And also, don’t move."
    mo "In fact, don’t do anything."
    mo "This is the part where you stay still and discreet or the game ends. I have experience. Trust me."
    s "Uhh..."

    scene mollytrain7
    with dissolve

    mo "Just...have to make it to the end of the first level. That’s all. Should be easy."
    s "Are you-"
    mo "Shh. Focusing."
    s "..."

    "The cage opens and my meal is, once again, placed on an electric panel."

    play sound "static.mp3"
    scene mollytrain8 with flash
    stop sound

    "I come to understand her pleas for stillness as I gaze downward and find that our position is one of common concern when train passengers are packed in like sardines."
    "And while I know Molly to not be the type to cry about me being a groper or anything like that, it is now impossible for me to think of anything other than a forced connection I can not escape from."
    "Several others press against my back and move me forward- which moves {i}her{/i} forward as well. But she has nowhere else to go as she’s already firmly up against the door."
    "Molly attempts to resist regardless by nudging what little of her body she’s still able to control backward, but that creates an even more immediate problem as it just leads to her grinding against me."
    "That, paired with the vibration of the train as it moves along its tracks and an echo chamber built to amplify the breathing of those trapped within it-"
    "I am faced with my hardest challenge yet."
    "And am now just seconds away from allowing myself to be shocked."

    play sound "static.mp3"
    scene mollytrain9
    with flash
    stop sound

    mo "{i}Mm~!{/i}"
    s "I-"
    mo "{i}Shh!{/i}"
    s "..."
    mo "..."

    scene mollytrain10
    with dissolve2

    mo "{i}Mm......nn...{/i}"
    mo "{i}I’m sorry, Sir...{/i}"
    s "You? Why are {i}you-{/i}"
    mo "{i}That it...has to be me you...wound up like this with...{/i}"

    "The harder Molly resists being forced up against the glass, the stronger the connection between us grows."
    "The tightness of her shorts and the fact that I was circumstantially forced into having an erection make it nearly impossible for me to hold myself back from pressing harder into her."
    "I can feel my cock being swallowed by the denim-covered flesh of her ass — firmer and tighter than I’ve envisioned it being in the past."
    "And I can feel it even more when she adjusts and angles herself so I’m caught firmly between her cheeks."

    scene mollytrain11
    with dissolve

    mo "{i}Ngh!........Hngh.......{/i}"

    "She moves."
    "So do I."
    "How apt that the world itself would be the one to force us together when neither one of us has had the willpower or resolve to move forward on our own."
    "Molly has tried, which is why she’s moving more than I am now."
    "Which is why she’s pressing back against me with more fervor than before."
    "Which is why I can feel her body burning up."
    "Which is why I can see the glass in front of her beginning to turn white with fog."
    "Which is why I grow harder."
    "Which is why I feed into the cycle and push back."
    "Which is why she presses back again with more fervor than before."
    "Which is why she continues to burn."
    "Which is why-"

    play sound "trainbell.mp3"
    stop music fadeout 3.0
    scene mollytrain12 with hpunch

    ann "This stop is...Shiori-eki...Shiori-eki."

    scene black
    with dissolve2

    mo "Okay! Time for a break!"

    "........."
    "......"
    "..."

    scene mollytrain13
    with dissolve2
    play music "notabluearchivesong.mp3"

    s "Are we-"
    mo "Day one ends with your character deciding that you’ve had enough! And with mine questioning her sanity in a public restroom!"
    s "Our stop wasn’t for-"

    scene mollytrain14
    with dissolve

    mo "I know when our stop was! We just came way too close to fulfilling a lifelong fantasy of mine and I need several minutes to myself before we’re both arrested for public indecency!"
    s "Oh god, does {i}everyone{/i} masturbate in public restrooms? Am I the weird one for {i}not{/i} doing that?"

    scene mollytrain15
    with dissolve

    mo "Probably not! But it does comfort me knowing I’m not the only person you’re aware of who has stooped to this level of degeneracy!"
    mo "Also, now’s as good a chance as any if you want to join the club! Because either you were feeling it back there too or you have a {i}very{/i} oddly shaped wallet!"
    s "I...was obviously feeling it."
    mo "Would it be presumptuous for me to invite you into the restroom at this point in time, Sir?!"
    s "Presumptuous? No. Dangerous? Yes."
    mo "Danger is the whole point!"
    mo "But even then, no one ever comes to this station! If we’re going to have our first {i}actual{/i} sexual encounter in a bathroom, this would be the one!"
    s "Considering I’m still on the fence when it comes to doing that with you-"
    mo "The fence, my arse! What we did back there would already {i}be{/i} sex by Irish Catholic standards! Are you coming or not?!"
    s "..."
    mo "Damn it, Jim! I’m a pervert, not a princess! I don’t have all day to wait for you to select a damn option from the dropdown menu!"

    menu:
        "Don't do sex (Now fully implemented!)":
            s "You...go ahead. I think I need a little more time."

    mo "Understood, Sir! Please do not think less of me for anything that happened today and I will promise to not think any less of you!"
    s "Have...fun, I guess?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mollytrain16
    with dissolve2

    mo "Steady hands, Emerald Guardian...now is not the time to falter!"
    mo "You know exactly what you were doing when you packed this! The train was merely a setback!"

    scene mollytrain17
    with dissolve

    mo "Eureka! Viva la Molly!"
    mo "..."

    scene mollytrain18
    with dissolve

    mo "Heh?"

    scene mollytrain19
    with fade

    w "..."
    mo "..."
    os "Umm..."
    os "Wakana?..."
    w "Yes, my dear?"
    os "There’s...someone there...isn’t there?"
    w "..."
    mo "..."
    w "Yes, my dear."

    scene mollytrain20
    with dissolve

    os "I thought you said no one ever came to this station?! Why would you lie to me?!"
    mo "..."
    w "..."
    w "Neither of us were ever here and we never speak about this again. Understood?"
    mo "Understood."

    scene mollytrain21
    with dissolve

    w "Come now, Osako. We have overstayed our welcome."
    os "Wakana! I still have to get dressed!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mollytrain22
    with dissolve2

    w "Arakawa? What are {i}you{/i} doing here?"
    s "I could ask you two the same question. Last I heard, no one ever came to this station."
    os "It was a lie."
    os "It’s all a lie."
    os "Nothing is real."
    s "What’s her problem?"
    w "She had a bad lunch. Pay it no mind."
    w "I’m glad I bumped into you, though. I’ve been meaning to ask if your class had any final entries for the poetry contest."
    s "That hasn’t happened yet?"
    w "The deadline is just before the next batch of standardized tests, which will be here before you know it."
    s "{i}Those{/i} are a thing again too?"
    w "Do you do...{i}any{/i} of your job? Or do Imani and Miyamura just earn your paycheck for you at this point?"
    s "They more or less just earn my paycheck for me. But I’ll follow up with them and see if they know anything the next time I’m back in school."
    w "Understood."
    w "Have you decided if you’ll be submitting anything? I’ve been looking forward to-"
    s "I don’t know."

    scene mollytrain23
    with dissolve

    w "You disregard the sanctity of the {i}dare,{/i} Arakawa. Do you mean to say that honor and loyalty mean nothing to you?"
    s "I mean to say that I’m just not that great at putting my feelings into words anymore."
    w "You had no trouble putting them into a predatory kabedon in the local library, though."
    s "Please don’t say things like that in front of a woman who could kill me with one kick."
    w "Write something, Arakawa. We both know you can."
    s "I’ll...see what I can do."
    s "Also, did you bump into Molly by any chance?"

    play sound "static.mp3"
    scene mollytrain24 with flash
    stop sound

    mo "AaaaaAAAAaaaAAAAaaaaaAAAaaaaaaAAAaaaaAAAaaahhhhhhhhh........."

    play sound "static.mp3"
    scene mollytrain23 with flash
    stop sound

    w "I have never met anyone who goes by that name before."
    s "Wasn’t she in your-"
    w "I have never met anyone who goes by that name before."
    s "..."
    w "..."
    s "I think I understand everything now."

    scene mollytrain25
    with dissolve

    w "You understand nothing and I was never here. Goodbye, Arakawa."
    s "Yeah...see you."

    scene black
    with dissolve2

    "Wakana drags Osako away and, after another five minutes or so, Molly returns from the restroom beet-red and sweaty."
    "Which is, not-so-coincidentally, the same state she walked {i}into{/i} the restroom in. But I hope she was able to hold herself over for now."
    "Not just because it looked like she was going to burst if she had to go another five minutes without an orgasm-"
    "But because I am now just one more dark room and one more push away from giving her as many as her heart desires."
    "The shock won’t kill me."
    "And I will be okay."

    $ renpy.end_replay()
    $ mollydate35p2 = True
    $ molly_love += 1
    stop music fadeout 7.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mollycamp1:
    "You know...there’s really nothing about today that makes much sense when you look at how I’ve approached my relationship with Ami as a whole."
    "I mean, sure. We’ve gone on a number of trips together. And we’ve made more memories along the way than I ever would have assumed I’d make when I first opened my eyes and saw her standing there in the sunlight."
    "I had no idea who she was. And hearing that from me directly was probably startling despite how easily she played it off as some sort of memory lapse."
    "I wonder just how many times she’s had to do such a thing — or how many times she’s had to kick herself into a shape that believes all that really {i}was{/i} just some sort of post-nap daze."
    "The point is, though...if today is meant to be a day of new beginnings, it should be a day where the {i}me{/i} I left at home would be unable to predict the actions of the me that’s in the woods."
    "And since everything else has gone completely against my character so far, there’s only one person I can think of talking to right now if I want to keep that pattern up."

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "So I tap on her name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"
    scene mollyontheline1 with dissolve

    mo "Hello?"

    play music "notabluearchivesong.mp3"

    s "{i}Hey. What’s up?{/i}"

    scene mollyontheline2
    with dissolve

    mo "Sir?!"
    s "{i}That’s right. {/i}"
    mo "I know it’s right! I just don’t know {i}why{/i} it’s right. Mayhap you’ve called the wrong number? "
    mo "Or better yet! You’ve been stricken with a deadly ailment and are now saying goodbye to everyone you know in the order of least to most appreciated!"
    s "{i}Right again. And you just happen to be the last person on that list.{/i}"
    mo "Roll for deception."
    s "{i}One million.{/i}"
    mo "All I heard was “one.” Which means you’ve critically failed as I already know you’ve yet to speak with the Kendo Princess."
    s "{i}Tsuneyo’s with you?{/i}"

    scene mollyontheline3
    with dissolve

    mo "Aye. We’re at the arcade. Would you like me to pass on a greeting?"
    s "{i}No.{/i}"
    t "Who is that?"
    mo "It is the Supreme Overlord. He’s dialed my number on accident. Would {i}you{/i} like me to pass on a greeting?"
    t "No."
    mo "Do the two of you even like one another?"
    t "Not really."
    s "{i}She’s fine.{/i}"

    scene mollyontheline4
    with dissolve

    mo "Sir, apologies for repeating the transmission, but {i}why{/i} are you calling me exactly? I was under the impression you were still under the effects of corrupted blood."

    play sound "static.mp3"
    scene mollyontheline5 with flash
    stop sound

    s "Is that another video game reference?"
    mo "{i}Only to the deadliest plague in MMO history! No one was safe, Sir! The entire world needed to be reset and repaired before it went away!{/i}"
    s "Yeah well, that’s definitely a realistic way of fixing things. So hey, maybe I just need to wait for that to happen in order to feel normal again?"
    mo "{i}Tuesday is just around the corner, Sir. Bug fixes should be rolling out.{/i}"
    s "Then it seems I have something to look forward to."
    mo "{i}Sir-{/i}"
    s "I just wanted to hear your voice."

    play sound "static.mp3"
    scene mollyontheline6 with flash
    stop sound

    mo "You..."
    mo "You {i}what?{/i} Apologies again, Sir. I believe my delusions of grandeur may have finally begun rewriting reality in a way that causes me to overwrite actual dialogue with what you’d say as a character in a dating sim."
    s "{i}I said I wanted to hear your voice.{/i}"

    scene mollyontheline7
    with dissolve

    mo "Gods help me. What if this is permanent?"
    t "Your face has changed colors, Emerald Guardian. And I know you well enough to understand that you must either be aroused or embarrassed if this is the case. Which one is it?"
    mo "Both I think."

    play sound "static.mp3"
    scene mollyontheline5 with flash
    stop sound

    s "I just figured talking to you might be a nice change of pace since this admittedly isn’t a thing I do all that often."
    mo "{i}I’ll say, Sir. It’s been so long that I was taken quite aback when I saw Arthas Menethil’s name pop up on my screen just now.{/i}"
    s "I don’t know how to tell you this, but that is not my name and I’m not sure where you heard that."
    mo "{i}The name matters not, Sir. It’s just how you’re labeled in my phone. But what is all of this about a change of pace? Have things truly gotten so terrible that you’re looking to me of all people for help?{/i}"
    s "I guess so. But today isn’t really that bad, all things considered. In fact, it’s actually been pretty {i}good{/i} so far. Just...different."
    s "If you’re hanging out with Tsuneyo though, I can just call back some other time."

    play sound "static.mp3"
    scene mollyontheline8 with flash
    stop sound

    mo "She actually just left!"
    t "Who left?"
    s "{i}I can hear her.{/i}"

    scene mollyontheline9
    with dissolve

    mo "Geh!"
    t "Oh. It appears a telepathic communication is coming in."

    scene mollyontheline10
    with dissolve

    t "I must listen closely so the sounds are not muddled by various action games."
    mo "Ngh!!!!!!!!"
    s "{i}Is everything-{/i}"
    mo "One moment...Sir! Channelling...my energy!"
    s "{i}Uh...{/i}"
    t "Message received. Rail everyone."

    scene mollyontheline11
    with dissolve

    mo "Wow, {i}that{/i} worked too."
    s "{i}What worked? What’s going on?{/i}"
    mo "Not much, Sir. Just, between this and the recent Dorm Wars, I’m beginning to think that some of my quirks aren’t actually fake after all."

    play sound "static.mp3"
    scene mollyontheline5 with flash
    stop sound

    s "So we can keep talking?"
    mo "{i}We can talk for as long as you like! I’m still just confused as to why!{/i}"
    s "Like I said, I just wanted to try something different. And there’s no greater change of pace than going from talking to Ami then talking to the Emerald Molly of the MacCormack Jungle or whatever it was."
    mo "{i}That was so far off that I can’t help but feel somewhat offended, Sir. But still, is that alone enough to warrant seeking me out? I’ve proven on several occasions now that there’s nothing I can do to help you.{/i}"
    mo "{i}Which depresses me greatly as I would very much LIKE to help you. I’m just not sure if a phone call alone will be enough to do that. But, then again, nor would meeting in person...so...{/i}"
    s "I’m not asking you to specifically do something that will help, Molly. I’m just asking you to exist. And to continue existing for at least the duration of this call."

    play sound "static.mp3"
    scene mollyontheline12 with flash
    stop sound

    mo "I have no plans to stop existing, Sir. And I’m happy to hear your voice as well. "
    mo "I’ve actually been thinking about you a lot lately."
    s "{i}In what way?{/i}"
    mo "Mostly just wondering when I’ll be able to see you again. The dorms have gotten rather lonely in the wake of your departure, Sir. The halls still call your name just as they did in days past."
    s "{i}Again, hate to be the bearer of bad news, but that probably wasn’t the hall you heard calling my name.{/i}"

    scene mollyontheline13
    with dissolve

    mo "And I’m sure it’s not the hall I’ve been hearing call it recently either but rather someone else struggling with your absence, Sir."
    s "{i}Well, it’s good to see that not much has changed on that end I guess.{/i}"
    mo "Good for you, perhaps. But all of us can’t stop wondering when we’ll be able to see you again. Your company may as well require a lottery ticket at this point in time, Sir."
    s "{i}Then you can view this call as me trying to combat that to some extent.{/i}"

    scene mollyontheline14
    with dissolve

    s "{i}I know that things have to change. And I know that there are certain things I’m going to have to do if Ami is ever going to regain some normalcy in her life.{/i}"
    mo "But what about you, Sir?"
    s "{i}What do you mean?{/i}"
    mo "What about {i}you{/i} regaining some sort of normalcy in your life? Because your prior proposal made it sound more like you’re just doing this for Arborea’s sake."
    s "{i}Oh. Well, that’s because I am.{/i}"

    play sound "static.mp3"
    scene mollyontheline15 with flash
    stop sound

    mo "{i}Then that’s not good at all, Sir! And this is coming from someone who quite literally has devoted herself to a variety of fictional characters!{/i}"
    s "Then you should understand better than most what it means to live for someone else and not yourself. Just, in my case, it’s a living human. And in yours, it’s probably a werewolf or something."
    mo "{i}I believe you may have me confused with Noriko, Sir. Which would actually explain this call quite well if you had not already addressed me by name.{/i}"
    s "Is Noriko also into werewolves?"
    mo "{i}The word “also” implies that I am into them as well, Sir.{/i}"
    s "Are you not?"
    mo "{i}No comment.{/i}"
    s "Yeah, that’s what I thought."

    play sound "static.mp3"
    scene mollyontheline16 with flash
    stop sound

    mo "All yiff aside, Sir- there’s something I’m rather curious about."
    s "{i}Probably not the best time to ask about whether or not I’m still up for sexual experimentation with you.{/i}"

    if makotonodowin == True:
        mo "Oh, don’t worry. I’ve done enough of that in recent days and don’t mind another period of waiting before something else enters my body."
        s "{i}Wow. What the hell have you been getting up to while I’ve been away?{/i}"
        mo "Losing the last shred of my dignity, Sir."
    else:
        mo "That is not what I had in mind, but I will make a mental note of this so I do not accidentally disgust you again."

    mo "Regardless, the thing I’m curious about is exactly what you’re {i}up{/i} to at the moment as you’ve alluded to the day being rather different and I’m not quite sure what that means."
    mo "Have you and Arborea departed the inn on a fetch quest? Is your party larger than just the two of you? What’s going on precisely?"
    s "{i}I’m camping.{/i}"

    scene mollyontheline17
    with dissolve

    mo "{i}Camping?{/i} Like...outside?"
    s "{i}Weird, right?{/i}"
    mo "But...outside is where the sun is, Sir. You don’t mean to tell me you’re willingly spending time under such an evil entity, do you?"
    s "{i}There are a few trees blocking it out, but yeah. This is where the sun is.{/i}"
    mo "Should I send help? I can have a gryphon headed your way in no time at all, Sir. Just do not be alarmed if that gryphon is disguised as a taxi."
    s "{i}It’s fine, Molly. And yes, this is definitely something I’d never come up with on my own. But I needed to get Ami out of the house somehow and I figured she’d enjoy something like this.{/i}"

    scene mollyontheline18
    with dissolve

    mo "But then why are you talking to {i}me?{/i} You should be with her if you’re really doing this to try and make her happy, Sir."
    s "{i}I can’t. She’s been kidnapped.{/i}"
    mo "Just out of curiosity, what percentage of this conversation has been entirely fabricated so far?"
    mo "Because I’m starting to think it’s all of it and that you really did somehow roll a one million on that deception check earlier."
    s "{i}Everything has been real, Molly.{/i}"
    s "{i}Ami’s with a friend of mine right now. And I’m fine with it because she’s another girl that’s my age and Ami really needs a mother figure right now.{/i}"
    mo "I think a parent as a whole would be fine, Sir. It doesn’t have to be a mother."
    s "{i}I think for her it does. But you might be right. I don’t know.{/i} "
    s "{i}That’s sort of another reason I’m doing this.{/i}"
    mo "You mean...you’re looking to act like more of a father figure to her?"
    s "{i}That’s the idea.{/i}"

    scene mollyontheline19
    with dissolve

    mo "Mm..."
    mo "Well, I think it’s a great one, Sir."
    mo "Though, it does further complicate the fact that she wants to harbor your offspring."

    if amifingered == False:
        s "{i}Yeah. That’s a thing I’d really like her to stop wanting as soon as possible.{/i}"
    else:
        s "{i}Yeah. But that’s something I can deal with another day.{/i}"

    play sound "static.mp3"
    scene mollyontheline15 with flash
    stop sound

    s "There’s another reason I called, you know."
    mo "{i}Aye...And I think I know what it might be if it has anything to do with where this conversation’s currently headed.{/i}"
    s "You were essentially just raised by your dad, right?"
    mo "{i}Aye, Sir.{/i}"
    s "Then, do you have any tips for me? Things that maybe {i}he{/i} did that I can...try and probably fail at?"
    mo "{i}Tips, you say?{/i}"
    s "Yeah. Anything that may have stuck out to you or...anything you appreciate all these years later."
    mo "{i}It’s not “all these years later, Sir.” My father is still helping me to this day. How do you think I can afford so many expensive figures and games with my part time cafe salary?{/i}"
    s "So the key to parenting is to increase her allowance?"

    play sound "static.mp3"
    scene mollyontheline20 with flash
    stop sound

    mo "It’s to be mindful of her wants and needs...and to always keep her in your heart and mind."
    mo "But an increase in her allowance would work wonders as well, I’m sure."
    s "{i}Got it. Thanks for your help, Molly.{/i}"
    mo "There’s no need to thank me, Sir. I’m just glad you called. "

    scene mollyontheline21
    with dissolve

    mo "I miss you."
    s "{i}I know...{/i}"
    s "{i}And I’m sorry. For just...kind of vanishing the way I did. But things aren’t exactly easy right now and I just need some time to-{/i}"
    mo "You don’t owe me an apology, Sir."
    s "{i}I know I don’t owe you one, but I want to give you one. And I also want you to know that it’s not just you I’ve been avoiding. It’s everyone.{/i}"
    mo "I know, Sir. I can hear the halls, remember?"

    scene mollyontheline15
    with fade

    s "Right...yeah."
    mo "{i}...{/i}"

    scene mollyontheline22
    with dissolve

    s "..."
    s "Listen, I-"
    mo "{i}How long will you be camping for, Sir?{/i}"
    s "Just today I think."
    mo "{i}May I see you when you return?{/i}"
    s "Maybe not right away, but..."
    s "Soon."
    mo "{i}I’ll be looking forward to it.{/i}"
    s "Why?"
    mo "{i}Why do you think?{/i}"
    s "..."
    mo "{i}Anyway! I must rail the Kendo Princess now. But I thank you again for the transmission, Sir.{/i}"
    mo "{i}And feel free to reach out again should you need me for anything.{/i}"

    scene black
    with dissolve2

    s "Sounds good."
    s "Thanks, Molly."

    play sound "phonebeep.wav"

    "I hang up the phone and slip it back into my pocket, wandering off once more in a direction I don’t know."
    "But that’s really what all of this is when you think about it."
    "Today is just one man’s journey through uncharted territory."
    "But it’s nice knowing there will always be an entire class full of girls to lend me an ear when I really need one."
    "Or, in Molly’s case-"

    stop music
    scene apollotheclown

    "{b}{size=+15}someone who will lend me everything{/size}{/b}"

    scene black

    $ renpy.end_replay()
    $ mollycamp1 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    scene sky
    with dissolve2

    "Now what should I do?"

    jump campmenu1

label mollyspring1:
    scene bedroom_day
    with dissolve2

    play sound "phonebeep.wav"
    play music "fallishere.mp3"

    "I tap on Molly’s name in my phone and wait for her to answer, prepared this time to inform her that my call {i}is{/i} intentional and that I did not accidentally dial her number."
    "But I am also prepared to have to argue that point as she’s the type of girl who has a hard time accepting that she is someone who can be loved."
    "Have I played a pivotal role in that by dismissing nearly all of her interests and making her feel less desirable by putting her into a box several miles outside of the one I’ve shoved the others into? Sure."
    "But am I going to continue to do that knowing full well that all it will take to get her on top of me is some light flirting and nicer words than normal?"
    "Again, sure. Because I have a hard time getting over the somewhat traumatic sexual hill this endless subconscious fight against things that don’t exist has caused me in terms of sex with her."

    play sound "phonebeep.wav"

    mo "Mm...hello?"
    s "{b}Good morning and get ready for the penis.{/b}"

    play sound "phonebeep.wav"

    s "..."

    "{s}I hang up the phone after realizing that today will be another day in which my tongue betrays me.{/s} {i}i hang up the phone because I’m a baby-back bitch.{/i}"
    "{i}also, since when does giving you the ability to freely speak your mind instead of hiding behind your good-guy mask count as “betrayal?”{/i}"
    "There’s a difference between giving me the ability to do something and then quite literally commandeering my thoughts."
    "{i}not to me. besides, i wouldn’t be here at all if you hadn’t emptied out a room for me to live in, so this is your fault. just like everything else terrible that has ever happened to you.{/i}"
    "Can I call her back now or are you just going to make me come on{s}to{/s} her again?"
    "{i}lol. get it?{/i}"
    "{i}it was a joke about that time you raped her.{/i}"
    "{s}Maybe I should just not call her at all if it will risk{/s} {i}why do you keep thinking you can think things without me thinking about the things you think?{/i} "
    "Because you’re only there sometimes and I don’t understand it. Stop using my mind as a toy."
    "{i}hey, you’re the crazy dude talking to himself in his room and telling europeans to get ready for the penis. i’m not even real.{/i}"
    "{i}OR AM I? /////////////////spooOOOOOOoooky{/i}"

    play sound "phonebeep.wav"

    "I tap on Molly’s name in my phone again and hope that things go better this time."

    play sound "phonebeep.wav"

    mo "Mm...Sir...is that you?..."
    s "Yes. This is the first time I’m calling you today."
    mo "That’s...good to hear...because I just had what may just be the strangest ending to a dream I’ve ever-"
    s "Yeah, I’m sure it was weird. But anyway, do you want to hang out?"
    mo "Ahh...alas...The dream continues..."
    s "It’s not a dream anymore, Molly. It’s a follow-up to your camping event."
    mo "Camping event?..."
    mo "Oh. You mean when {i}you{/i} were camping and Tsuneyo was railing herself in the background. But that was- wait! It’s merely 8:00 AM! Why are you calling me this- wait times two!"
    mo "You dreamt of me as well, didn’t you Sir?!"
    s "{b}Yeah and it was a really spicy sex dream. Wanna hear about it?{/b}"

    "FUCK OFF."

    mo "I have not wanted to hear something this much since the last time Kaguya Luna posted an ASMR video. Rest in peace, my queen."
    s "Who is that and what is that and why? And also no, because that was a lie and that dream never happened."
    mo "There are too many sections of that sentence for me to process this early in the morning, so I’m just going to go back to sleep now."
    s "So that’s a no to hanging out?"
    mo "Supreme Overlord, we both know you don’t want to actually hang out with me. "
    s "But-"
    mo "You just need a healer for a group quest! To which I respond...aye!"
    s "You what?"
    mo "Not {i}I,{/i} sir. Aye! "
    s "Those are the same thing."
    mo "Damn these text boxes and the way they foil my humor once more! "
    mo "I’ll gladly meet up with you, Sir. Just...not right now. The hands moved far too much last night."
    s "Is that new masturbation slang?"
    mo "The hands on the clock, Sir. I was being a dunce again. But do note that I did not declare your suggestion as incorrect."
    s "Okay. Well, just...call me whenever you’re ready I-"

    play sound "static.mp3"
    scene mollyarcadedate1 with flash
    stop sound

    mo "Top o’ the mornin’ to ye, Sir!"
    s "...guess."

    scene mollyarcadedate2
    with dissolve

    mo "Guess what, Sir?"
    s "Nothing. Just having one of those mornings where large chunks of time disappear while a divine voice echoing in the back of my head tells me to have sex with girls."
    mo "That would make a good premise for an h-game."
    s "I disagree. Too convoluted. Anyway, how are you?"
    mo "How {i}am{/i} I?"
    s "Yeah. Have you been well lately?"

    scene mollyarcadedate3
    with dissolve

    mo "You’re being weird."
    s "So what? You’re literally {i}always{/i} being weird. That’s like, your whole thing."

    scene mollyarcadedate4
    with dissolve

    mo "That’s precisely the issue, Sir! It’s not abnormal for me to act in such a way as it would be a cornerstone of my archetype! But for you-"
    s "I do much weirder things much more frequently. I should be allowed to ask you how you’ve been without it raising any flags."

    scene mollyarcadedate5
    with dissolve

    mo "You can never be too careful when it comes to flags, Sir. And I’m not just talking about Wales here."
    s "What?"

    scene mollyarcadedate6
    with dissolve

    mo "I just mean that hidden flags show up in games all the time. And since they’re the ultimate factor in determining plot or character deviations, they can’t be taken too lightly."

    $ hiddenmollyflagwhatdoesitmean = True
    ##shhhhhdonttellakiralmao

    mo "You never know when one is going to show up and change the outcome of your story, Sir."
    s "Are you doing well or not, Molly? Because talking about how life has been for you is the easiest way for me to avoid talking about how it’s been for me and {i}that’s{/i} what I’m trying to do here."

    scene mollyarcadedate7
    with dissolve

    mo "You’re still struggling, Sir?"
    s "Okay well, this was fun. I’ll see you later. Teleport me home now, Pareidolia. "

    "your message can not be delivered at this time. please try again when you’re not such a pussy."

    mo "Pareidolia?..."
    s "That’s that voice I was talking about earlier."

    scene mollyarcadedate8
    with dissolve

    mo "I understand completely, Sir. The entity commanding my every thought is named Siobhan. It is {i}her{/i} fault I am the way I am, not mine."
    s "I’m going to latch onto the end of that sentence harder than you know, Molly. Also, nice dress."

    scene mollyarcadedate9
    with dissolve

    mo "Thank you, Sir! It comes off very easily."
    s "That’s nice."
    mo "I did not intend to say that out loud. It must have been Siobhan."
    s "Did Siobhan also make our plans for this afternoon? Because if you could ask her what we’re doing out here, it’d be really helpful since time skipped for me and I can’t remember at all."

    scene mollyarcadedate6
    with dissolve

    mo "Siobhan did not make our plans, Sir. Nor did I. It was you who ultimately chose how we’d be spending my bonus event."
    s "Well, do you remember what I chose?"
    mo "The arcade, Sir."
    s "Now you’re just taking advantage of me."

    play sound "broken.mp3"
    scene mollyarcadedate10
    mo "{b}AT LEAST YOU GOT TO KEEP YOUR CLOTHES ONNNNNNN{/b}"

    play sound "static.mp3"
    scene mollyarcadedate6 with flash
    stop sound

    mo "I’m not, Sir! Do you really not remember?"
    mo "You said you wanted to do something nice for me since you’ve yet to pay much attention to any of my hobbies. To which I responded that such a thing would not be necessary."
    mo "But you were very insistent and I ultimately folded. If you’re saying you’ve changed your mind now, though, I’d be happy to do something else."
    mo "Just being out and about with you is enough of a shock to me. "
    s "We can still go, it’s fine."

    "I’m just trying to internally figure out why {i}I’d{/i} suggest such a thing."
    "{i}we’re gonna get it wet today{/i}"

    mo "Are you absolutely positive, Sir?"

    play sound "static.mp3"
    scene mollyarcadedate11 with flash
    stop sound

    s "Y-"
    s "Well, fuck me I guess."
    mo "I believe there are rules against that in public, Sir. Not to mention how I can only imagine the effect it would have on this room full of virgins. "
    s "Well, how would {i}you{/i} react if you saw a couple having sex in the arcade while you were trying to enjoy being a nerd?"
    mo "I think I’d have a much harder time being a nerd in that moment, Sir. I don’t fare well when given such distractions."
    s "Is that another ADHD thing?"
    mo "Or just being a pervert, Sir. I’m not sure if I could successfully remove myself from such a situation as it’s far too close to fantasy."

    scene mollyarcadedate12
    with dissolve

    mo "But alas! Real gamers do not have sex, so this is not a random event I shall ever encounter!"
    s "Is it really okay to be yelling that in front of them?"
    mo "Of course, Sir. For when I am with you, there can be no side characters! Which means no one could possibly respond to such an emboldened proclamation!"
    gamergirl "Hey! Screw you, lady! Just because you’ve got a hot boyfriend doesn’t mean you can pick on those of us who don’t!"

    scene mollyarcadedate11
    with dissolve

    mo "Never mind, Sir. It appears that our scenario conflicts with hers and that simply being together does not prevent others from having dialogue as well."
    mo "There goes my theory that everyone else is just an NPC on dates."
    s "I’m going to go hang out with that other girl. I’ll see you later, Molly."

    scene mollyarcadedate13
    with dissolve

    mo "Molly-pout, activated!"
    s "Turn the Molly-pout off. I was kidding."

    scene black
    with dissolve2

    mo "Not until you give me everything you’ve got, Sir!"
    s "I thought you said there were rules against that in public?"
    mo "There are! But that does not change how I’d be open to breaking them under the right circumstances and how that is {i}not{/i} what I was referring to at all!"

    scene mollyarcadedate14
    with dissolve2

    s "Then why add that first part at all?"
    mo "To reaffirm that I am still level one when it comes to dating, Sir."
    mo "Because, as it turns out, years worth of dating sims don’t prepare you for the nerves you experience when communicating with actual humans!"
    s "There shouldn’t be any nerves at all. We’ve spent plenty of time together before."

    scene mollyarcadedate15
    with dissolve

    mo "That...may be true, Sir. But it does not change how something feels...{i}different{/i} about today. Like I’ve glitched the system and triggered your route early or...something."
    mo "But if Parold E Dolia was truly holding your CTRL key down and skipping the bulk of your day, I suppose I can understand how things may feel more “normal” to you."
    mo "And it’s also highly probable that my impressionable {size=-15}yet highly depraved{/size} maidenly heart is just ill-prepared for actual “dates.”"
    s "Did I actually say this would be a date?"
    mo "You did, Sir. Why else would I ever wear a dress?"
    s "Because you...look good in them?"

    scene mollyarcadedate16
    with dissolve

    mo "S-See?! This is romantic dialogue, is it not?! You do see this as a date after all!"
    gamergirl "Oh my God, can you two shut up?!"
    mo "Ignore her, Sir. ‘Tis just jealousy and I know it well."
    mo "Now, about this game-"
    s "Are you not worried about being out here with me, Molly?"

    scene mollyarcadedate17
    with dissolve

    mo "Worried? Why would I be worried? Compensated dating is extremely normal in places such as this and the likelihood of someone believing I’m just your {i}hired{/i} girlfriend is rather-"
    s "Not about the age thing. About going out on a date with me when you’re fully aware of how little time I’ve spent with everyone else in the class as of late."
    s "Aren’t you at least somewhat scared that we might bump into one of them and that you’ll have to figure out a way to explain this away while {i}I{/i} can just slink back into the shadows?"

    scene mollyarcadedate18
    with dissolve

    mo "Hm...That would be somewhat problematic now that I think about it."
    mo "But I guess I was just so excited to do something like this with you that I hadn’t bothered thinking about it."

    scene mollyarcadedate19
    with dissolve

    mo "I sincerely doubt anyone would assume that we’re {i}together{/i} if they saw us like this though, Sir. I don’t think many of them see me as a viable partner for you at all."
    s "Is that nerd Molly speaking or self-conscious Molly speaking? Because one of those is unpopular by design and the other one just over-thinks things."
    mo "Despite what my alts would indicate- I am but one character, Sir. And those are both aspects of my person."
    mo "There is not {i}one{/i} reason the others would not see me as a viable candidate, there are many. And granted, they are warranted."
    mo "But if there’s anything I know about romance, which there is not, it’s that {i}anyone{/i} has a chance with {i}anyone{/i} if they try hard enough."
    s "Yeah, that’s terrible advice and definitely not true."

    scene mollyarcadedate20
    with dissolve

    mo "Which is why I clarified that I know nothing of this form of magic."
    s "Did you know I went on a date just like this with Rin once?"

    scene mollyarcadedate21
    with dissolve

    mo "Is now really the best time to brag, Sir?"
    s "I’m not trying to brag, just drawing similarities. For example, do you think the others see {i}her{/i} as a viable partner for me?"

    scene mollyarcadedate22
    with dissolve

    mo "I’d say so, Sir. Your camaraderie is noted by everyone, and I’m not sure anyone would be surprised if the two of you were to become more {i}involved{/i} one day."
    s "That’s exactly what I mean."

    scene mollyarcadedate21
    with dissolve

    mo "So you {i}are{/i} bragging."
    s "No..."

    scene mollyarcadedate22
    with dissolve

    s "I just mean that you two are very similar. And if you think everyone can picture {i}her{/i} with me, why would it be any different for you?"
    s "You’re both perverted, nerdy weirdos at the end of the day. And even if people think those qualities are a little more exaggerated in you, which they are, who cares?"
    mo "So...the moral is to believe in myself and not care about what other people think of me?"
    s "No. If that were the moral, I wouldn’t have to say anything because I believe you already {i}do{/i} that."
    s "The moral is that you {i}should{/i} care. Because it will make proving them wrong feel infinitely better."

    scene mollyarcadedate23
    with dissolve

    mo "Wording it that way makes it sound as if {i}you{/i} believe in us, Sir."
    s "What I believe doesn’t matter. I’m a spineless husk of a man who will accept any affection thrown at him because that’s all I’ve ever done throughout my time on this planet."
    mo "Well...you are my favorite spineless husk of all, Sir."

    scene black
    with dissolve2

    mo "N-Now! About this game..."

    "Molly and I spend the next couple hours playing various arcade games before leaving to go get lunch."
    "Conveniently, that lunch is located directly upstairs at a cafe built into the gaming center."
    "So we return to the ground floor for more arcade stuff once we’re done there and that kills {i}another{/i} couple hours."
    "And honestly, I didn’t even know it was possible to spend so much time in an arcade."
    "But when you’ve got someone as passionate about this stuff as Molly, it’s normally fine if you get caught in the current."

    play sound "static.mp3"
    scene mollyarcadedate24 with flash
    stop sound

    "But the thing with currents is that they can be dangerous if you don’t approach them with caution."
    "In fact, in most cases, it’s probably best to leave the more violent ones alone. For if you’re not whisked away to somewhere you don’t want to go, you may very well drown."

    play sound "static.mp3"
    scene mollyarcadedate25 with flash
    scene mollyarcadedate24 with flash
    stop sound

    "I can feel my feet beginning to slip, and I can’t find anything to latch onto that will not break the moment I touch it. And that’s my fault."
    "Under most circumstances, it {i}is{/i} normally fine getting caught in the current. But no matter how many times I learn not to, I can’t help but fight back at the water."
    "All that does is tire me out and drag me under. But again, that {i}could{/i} be fine if you have someone like Molly acting as a lifeguard. You just have to be careful not to drag her down with you."

    mo "Sir-"

    play sound "static.mp3"
    scene mollyarcadedate25 with flash
    scene mollyarcadedate24 with flash
    stop sound

    "I flew too close to the sun again."

    mo "Thank you for today. Really."
    mo "Because even if you didn’t enjoy yourself, it meant a lot to me. And if there is anything {i}I{/i} can do to make you feel any better, all you have to do is say the word."

    "SAY THE WORD."

    s "Molly-"

    "COME ON."

    s "Things have been pretty terrible lately. You know that."

    "UGHHHHH HERE WE GO AGAIN."

    mo "I know, Sir."
    s "And, to be completely honest with you, there’s probably nothing you can do to help that doesn’t involve selling your soul."
    mo "I have collected thousands upon thousands of souls. Just ask the Lord of Cinder."
    s "What I mean to say is that this is the peak of what we can accomplish together. We’ve gotten everything we possibly can out of this date."
    mo "But you’ve gotten nothing, Sir. And I’ve gotten to experience something I may never get the chance to again once the rest of the class comes back into the picture."
    s "Molly-"

    stop music fadeout 25.0

    mo "Don’t fight me on this one, Sir. I may be level one in love, but that’s only because I’ve been grinding loneliness for so long."
    mo "You won’t ever actually be my {i}boyfriend.{/i} And I won’t ever actually be your {i}girlfriend.{/i} But that’s okay, because we can still {i}be{/i} together in our own way."
    mo "That doesn’t need to make sense to anyone else. But in my life, nothing has ever really {i}needed{/i} to make sense to anyone else."
    s "And that’s what I both love and hate about you."
    mo "Aye...but do you know what I both love and hate about you, Sir?"
    s "What’s that?"

    scene mollyarcadedate26
    with dissolve2

    mo "That even though I constantly annoy you...or confuse you...or make you feel terrible with my unwanted advances..."
    mo "You still cherish me."
    mo "You may jest...and say mean things about how much of a nerd I am, or...poke fun at the way I’ve lived my life. But that’s just it, Sir. It’s all in jest. So {i}of course{/i} I love that."
    s "But if any of that’s true, and I’m not claiming it is...why would you hate it? Because I don’t think many people would take exception to any of those things."

    scene mollyarcadedate27
    with dissolve2

    mo "..."
    s "..."
    mo "It’s because it conflicts with something else I want, Sir."
    s "..."
    mo "It is nice to be cherished, yes."

    scene mollyarcadedate28
    with dissolve2

    mo "But sometimes I wish that you’d just break me already."

    "oh shit."

    s "Molly-"

    scene mollyarcadedate24
    with dissolve

    mo "It’s because of Halloween, isn’t it?"

    play sound "static.mp3"
    scene mollyarcadedate25 with flash
    scene mollyarcadedate24 with flash
    stop sound

    mo "Put it behind you, Sir."

    play sound "static.mp3"
    scene mollyarcadedate25 with flash
    scene mollyarcadedate24 with flash
    stop sound

    mo "Come back to the dorms with me."

    scene black
    with dissolve2

    mo "We can do something for {i}you{/i} next."

    $ renpy.end_replay()
    $ mollyspring1 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump mollyspring2

label mollyspring2:
    scene clearnightsky
    with dissolve2
    play music "asobeatsex8.mp3"

    "I’ve spent so much time indoors today that I didn’t realize how dark it had already gotten."
    "You’d think that after going so long without sunlight just a short while ago that my biological clock may have somewhat recalibrated to compensate for that, but no."
    "As it turns out, even the most intangible parts of your body must be exercised in order to properly function. "
    "Which is perhaps why I might feel so numb right now as the organ that’s meant to be pounding was buried roughly six feet beneath the surface before I ever met this girl."
    "But it’s because of that absent muscle that I’m able to do things like this in the first place. "
    "And now that the mass inside of my skull no longer has the motivation to act in the place of a heart, I find turning her away to be nothing more than a waste of time."
    "I’m sure that satisfies a less fragile existence inside of my head. But you know that things are bad when the only reason I’d say no right now is to get revenge on it."
    "It’s quiet — as nights like this typically are. But there’s a certain level of excitement to it as well. "
    "We both know where we’re headed. We know what’s going to happen when we get there. So all there is to feel in the dark is...anticipation. Maybe even worry on {i}her{/i} end."
    "The nerves are plentiful, that much is for sure. But for her, their sole function is to try and dissuade her from wasting what little purity she’s maintained on a man twice her age."
    "And for me, all they’re doing is making my hands shake."
    "That’s what pockets are for, though. So my hands make their home inside of them as I open my mouth to cut the tension before stitching it back together and making it even stronger."

    s "I don’t really want anyone else to see me at the dorms, Molly. "
    mo "‘Tis fine, Sir. I’ll use Cloak of Shadows."
    s "I’m serious. Why don’t we just go somewhere else? Like a love hotel or something?"
    mo "That...might be a little much. Wouldn’t it? I’ll feel more comfortable surrounded by my figures, Sir."
    s "But will you feel more comfortable with the looming threat of others listening in? "
    mo "Ah, about that. Touka recently took it upon herself to fund the soundproofing of my room as my constant screaming was impacting her sleep, Sir."
    s "It’s good knowing that all it takes to get your way is continuously bothering people."
    mo "Aye. It is clearly an effective method if you’re still with me right now, Sir."
    s "Does it really have to be the dorms, though?"
    mo "A special quest reward awaits you there, Sir. And it’s one that’s mandatory for progression as well. We don’t want your development being halted, do we?"
    s "Molly-"

    scene black
    with dissolve2

    mo "I’ll check the halls ahead of time to make sure there’s no one there, Sir. It’ll be like you never came at all."
    mo "In the...sense of your actual location, I mean. I do hope that, in the other way-"
    s "Save it for when we’re in your room, Molly."

    "........."
    "......"
    "..."

    scene dorm2
    with dissolve2

    "It isn’t long before we’re there and I come face to face with a familiar sight...but I can’t help but feel like something’s changed."
    "I practically used to live here with how frequently I visited the girls. And more often than not, the purpose was far from pure. So at least {i}that{/i} much hasn’t changed."
    "The atmosphere, though..."
    "It’s like something’s missing."

    scene black
    with dissolve2

    mo "{i}Quietly, Sir. Our stealth mission is nearly complete.{/i}"
    s "..."

    play sound "dooropen.mp3"

    "Oh, right."
    "What’s missing is {i}her.{/i}"

    scene mollysuckubus1
    with dissolve2

    "Even on another floor, I can feel her absence. "
    "And I’m not saying that her existence as a whole is what gave me comfort when I used to enter this building-"
    "I’m just saying it would comfort me now."
    "But I suppose this is the part where I do what I’ve always done and replace that comfort with something that’ll feel mostly the same so long as I close my eyes."
    "Because even if she’s not here, her friends are. And if I lose myself in them, maybe she’ll shatter the fabric of reality just to show up and belittle me for being an unfaithful deviant."
    "I think I’d like that."
    "Then, the two of them could go down on me together."

    mo "So...here we are."
    s "I came back to the dorm with Rin after my “date” with her as well."

    scene mollysuckubus2
    with dissolve

    mo "Again with the bloody bragging. There’s no escape..."
    s "Just trying to draw more parallels. And besides, there’s nothing to even brag about since her intentions were never sexual and yours are."

    scene mollysuckubus3
    with dissolve

    mo "Should they not be, Sir? I wouldn’t want to force you into {i}another{/i} situation you’re uncomfortable with after the misunderstanding in the dressing room."
    s "Does it even matter? I’m the one who gave you these ideas in the first place, aren’t I?"
    mo "If you are referring to the idea of sexually experimenting with a handsome older man, surely not. I believe that is something we all imagine at least once."
    s "But-"
    mo "Weekly."

    scene mollysuckubus4
    with dissolve

    s "But we probably never would have gotten to this point if I hadn’t told you all that time ago that I’d be open to “experimenting” with you."
    mo "‘Tis easy to say that in hindsight, Sir. But we don’t know that for sure. The type of girl I am and the type of man {i}you{/i} are could have easily landed us in this very same event."
    mo "And if you’d like my opinion, Sir, the troubles and turmoils we’ve endured on the way here make it all the more exciting. So it is my belief that this meeting is somewhat fated. "
    s "You believe in fate?"
    mo "I believe in {i}fae{/i}, Sir. And the idea of {i}fate{/i} is far less fantastical than that."

    scene mollysuckubus5
    with dissolve

    mo "Which isn’t to say I’m not nervous at all...I certainly am. "
    mo "I’ve never done anything like this outside of games, but..."
    mo "But I have...ways in which I can attempt to counteract those nerves, Sir..."
    s "Like?"
    mo "I..."

    scene mollysuckubus6
    with dissolve

    mo "I believe the best way of informing you would be to have you close your eyes for a minute or two, Sir."
    mo "When they open again, {i}then{/i} you will know exactly what I’m referring to."

    scene black
    with dissolve2

    s "Okay. But if you’re planning on using this time to kill me, please make it as slow and painful as possible."
    mo "D...Don’t people typically ask for the opposite?"
    s "Not anyone who actually wants to die. Or I guess “deserves” is a better way of putting it."
    mo "You’ve done naught to deserve death, Sir. ‘Tis the law of the land that disallows the actions we’re about to take with one another. And even then, they’d not be punishable by-"
    s "As much as I appreciate you attempting to justify this on my behalf, I ask that you keep your mouth closed."
    mo "Entirely? But that would make what I’m about to attempt nigh impossible, Sir. "
    s "Very funny."
    mo "Sir, all I am saying is that if I had any belief that this was wrong, I wouldn’t be doing it. You may now open your eyes."

    scene mollysuckubus7
    with dissolve

    s "And I’m saying that-"
    mo "..."
    s "I forget what I was saying."
    mo "I cast Charm on you while your eyes were closed, Sir."
    s "What {i}is{/i} that?"
    mo "My aforementioned confidence booster, Sir. You see before you Yrelixis, Succubus of the Void — experienced satiator of ten thousand lusts."
    s "I see a redhead with wings and not nearly enough clothing."
    mo "Same difference, Sir."
    s "You put that on really quickly."

    scene mollysuckubus8
    with dissolve

    mo "Mortal — did I or did I not inform thee that mine prior cloth was easy to shed?"
    s "You’ve informed me of many things and the vast majority have gone over my head, but I can promise you that that one didn’t."
    mo "Then why dost thou remain upright when thou should be begging for...thou’s life?"
    s "So I {i}am{/i} going to be killed."

    scene mollysuckubus9
    with dissolve

    mo "Behave and I shall spare thee the smallest bit of energy while consuming {i}everything else.{/i}"
    s "This is certainly going to be an interesting {i}first{/i} sexual escapade."

    scene mollysuckubus10
    with dissolve

    mo "The cosplay isn’t too much, is it? Because this is more for me than it is for you, but I have others that may also accomplish the same feat if you find the wings too distracting or-"
    s "Oh, it’s fine. But I hope you know that this sets a precedent for future events and that I’m going to want to see what other {i}characters{/i} you have in store."

    scene mollysuckubus11
    with dissolve

    mo "That may just be the single most alluring sentence I have ever heard. "

    play sound "tackle.mp3"
    scene mollysuckubus12
    with hpunch

    mo "Now, down with thee!"

    "Molly catches me off guard and manages to push me to the ground after I lose my balance."

    mo "From this moment forth, thou ist under the command of Yrlexis and shall do as I bid! Is that understood, mortal?"
    s "Do I really have to roleplay as well?"
    mo "OOC: I suppose not, Sir. But please keep questions to a minimum so I may stay in character from this point onward. "
    mo "Also, please provide verbal consent so as to prevent any more misunderstandings."
    s "Consent given."

    scene mollysuckubus13
    with dissolve

    mo "As if your consent means anything to Yrlexis!"

    scene black
    with dissolve2

    mo "Now, mortal — do as I command and removest thine trousers or I will banish them to the void!"

    play sound "zipper.mp3"

    s "Yes, Yrlexis."

    "I do as Molly asks and play along, unzipping my pants and revealing myself to her."
    "And it doesn’t take long until she joins me on the ground."
    "........."
    "......"
    "..."

    scene mollysuckubus14
    with dissolve2

    "She crawls closer, forcing me back until I’m pressed against the door as she positions herself between my legs."

    mo "Such a long and powerful member...I expected nothing less from you, mortal."
    mo "I’m sure it’s positively brimming with power..."

    scene mollysuckubus15
    with dissolve

    mo "I can feel the heat radiating from your core as you fall deeper under my spell..."
    mo "You shall think of no one but I — the one who binds thine heart with chains of lust that can be broken by no one else."
    mo "You shall be my toy for the rest of eternity...do I make myself clear?"

    scene mollysuckubus16
    with dissolve

    mo "And what an excellent toy you shall be, mortal..."
    mo "I can already feel your energy coursing through my body...there is no greater feeling known to man..."
    mo "Tell me...do you feel it as well?"

    "Molly gently strokes the head of my cock, lubricating it with the precum that’s already seeped from it as I continue to “fall under her spell.”"
    "Her hand can barely fit around me, but that doesn’t dissuade her from carefully and gently exploring it, pumping softly and managing to make me even harder."
    "It’s like I’m being studied. She can’t take her eyes off of it. But I guess that’s what happens when you let a degenerate like her close to real dick for the {s}first{/i} second time ever."

    mo "Truly spectacular...I believe it’s even longer than the tentacle."
    s "Tentacle?"
    mo "Aye...but less thick around the base."
    s "I can’t tell if you’re insulting me or not."

    scene mollysuckubus17
    with dissolve

    mo "Of course not, mortal. Yours is truly the most magnificent of all..."
    mo "And I’d love nothing more than to suck every...last...drop of energy from you..."

    "She strokes me harder...and I can feel her breath on my skin as she begins to pant from the excitement."

    mo "Ahh...aah...it grows stronger...{i}harder...{/i}dost thou desire greater pleasure, mortal?"
    s "How tightly are those horns secured to your head?"
    mo "They’re fused to my skull, mortal. As a succubus of the void, my skeletal structure is significantly different from that of a-"

    scene mollysuckubus18
    with dissolve

    s "That’s good to hear."
    mo "You...you dare touch the horns of a void succubus without express permission? Such an act is punishable by-"

    play sound "tackle.mp3"
    scene mollysuckubus19
    with hpunch

    mo "M-Mortal?! Thou shall remain under my command lest the connection be severed entirely!"
    s "The effects of your spell have worn off."
    mo "What?! But...that simply can’t be! I am Yrlexis, the satiator of ten thousand lusts! "
    s "And I’m the guy who’s about to fuck Yrlexis’ mouth."

    scene mollysuckubus20
    with dissolve

    mo "N-Not if I attack first! And my speed is higher due to my wings, so I have action priority! "
    s "Then by all means, {i}Yrlexis.{/i}"

    scene mollysuckubus21
    with dissolve2

    mo "Mm..."

    "Molly closes her eyes and slides my cock into her mouth, shedding her “confident” persona as she spends the next several minutes letting cute gasps and moans slip out from between her lips."
    "Her head bobs up and down with passion and determination, and it’s clear to me that she’s either naturally talented at this or has “practiced” in some form or another."
    "Probably the latter considering this is Molly we’re talking about. But either way, I look on in undeniable enjoyment as her tongue traces the underside of my tip."

    scene mollysuckubus22
    with dissolve

    mo "Mmph.....mngh...."

    "She looks up at me and I can tell that her “switch” has been flipped again as she attempts to revert to her succubus-self."
    "She begins moving faster...her moans become more sexual in nature...and for a moment, it’s like someone else has taken her place."
    "But those eyes are unmistakable. That hair is unmistakable. Those freckles and even the way she blinks are unmistakable."
    "I know exactly who is devoting herself to getting me off right now...and I know it’s someone who’s been patiently waiting for this moment for even longer than I have."
    "I’m sorry I kept you waiting, Molly."
    "I regret every minute of it."

    scene mollysuckubus23
    with dissolve

    mo "Mm...mmnh....mm!"

    "She takes me in deeper, innocently gazing up at me as I finally let go of her horns. But I can’t tell if she wants me to grab them again or if she’s just reacting to an expression I’m making."
    "I try not to think about it, slumping harder against the door and thrusting gently into her mouth as she continues sucking me off."

    scene mollysuckubus24
    with dissolve

    mo "Ahm......ahnn......ahmf....."
    mo "You lied, mortal...you’re still under my spell..."
    mo "You’re far too hard right now to have broken free from my grasp..."
    s "You’re right...I just couldn’t help myself."

    scene mollysuckubus25
    with dissolve

    mo "I blame you not...the tongue of a void succubus has wreaked havoc on many men, mortal...it’s only natural you’d want to experience it as well..."
    mo "Ahn......does it live up your expectations?......."
    mo "Does it make you want......even more?......"
    s "Can I {i}have{/i} more?"

    scene mollysuckubus26
    with dissolve

    mo "You’d burst into flames if I gave you what you want right now, mortal."
    s "And you’d split in half."
    mo "You crave this body that badly?"
    s "You have no idea..."
    mo "It craves you as well, mortal..."

    scene mollysuckubus27
    with dissolve

    mo "Each and every night...yours is the one I crave the most..."
    mo "That’s why I’ve descended upon you now..."
    mo "I simply could not wait anymore..."

    scene mollysuckubus21
    with dissolve

    "I grab her horns once more and begin violently thrusting into her mouth, unable to contain myself any longer."

    mo "Mm! Mngh! Mnnghhh! Mm! Mm! Mm!"
    s "I’m...gonna cum, Molly..."
    mo "Mm! Mm! Mm!"

    scene mollysuckubus26
    with dissolve

    mo "You know, mortal...legend has it that ejaculating on the face of a succubus will increase her lifespan by 1,000 years."
    s "Then work for it..."
    mo "It would be my pleasure..."

    play sound "static.mp3"
    scene mollysuckubus28 with flash
    stop sound

    mo "Hah...hah...hahh!"

    "Molly leans back and ramps up her speed once again, rapidly pumping me as she aims my cock directly at her face."

    mo "Let...it out...Sir..."
    s "Don’t you mean “mortal?”"
    mo "Same...difference..."
    mo "Just...ahh..."
    mo "Let..."

    with sexfade

    mo "It..."

    with sexfade

    mo "Out!"

    with sexfade
    with sexfade
    scene mollysuckubus29 with cumflash
    with hpunch

    mo "Ah!"

    scene mollysuckubus30
    with dissolve

    mo "Geh..."
    s "Congratulations on the extra thousand years you get to stay on this shitty planet. Which isn’t to say you already wouldn’t have gotten those considering-"

    scene mollysuckubus31
    with dissolve

    mo "Sir."
    s "..."
    mo "How do I look?"
    s "..."
    mo "Like a degenerate?"

    scene black
    with dissolve2

    s "I don’t think you’ve ever been prettier, Molly."

    "I lie to her, but that’s only because it’s hard to tell her I’ve never been {i}less{/i} attracted to her."
    "In the act, everything was fine. In the act, she was beautiful."
    "But now, with proof of one more failure on my end painted across her face, all I see is the inability to ever {i}truly{/i} abstain from anything."

    stop music fadeout 15.0

    "Some might say that this is progress-"
    "{i}present{/i}"
    "But I think I’d have to disagree."
    "I think this is the mark of one more downfall."
    "I think this may be a defining moment in reaffirming the original way I looked at girls like Molly."
    "How they’re pretty when they’re touching me-"
    "But prettier when they’re locked inside of their rooms."

    $ renpy.end_replay()
    $ mollyspring2 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"

    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    "{i}You have also unlocked the dorms again!{/i}"

    s "Wonderful."

    "{i}Now, you can go back to hurting little girls whenever you want.{/i}"

    s "I’m aware."

    "{i}This is also the part where I’d like to tell you that the Invite Over option is unlocked again, but I can't because you’re still shutting me out!{/i}"

    s "And I don’t plan on changing that any time soon."

    "{i}Sure! But you didn’t plan on cumming all over the Irish girl’s face either and look what happened tonight.{/i}"

    s "I would like to go to sleep now."

    "{i}Then stop talking to yourself, nerd.{/i}"

    scene black
    play sound "tackle.mp3"

    s "Okay."
    s "Goodnight, audience."
    s "Goodnight, Wilford Blackhole Hands."

    play sound "slap.mp3"

    wil "Hi-yah."

    "It takes a while for me to fall asleep."
    "I keep getting slapped."

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

label mollylust10:
    play sound "static.mp3"
    scene mollyalsowantsxmasdick1 with flash
    stop sound
    play sound "knock.mp3"

    s "..."
    f "Ah..."

    "There is a knock at the door."
    "This happens sometimes."
    "Normally not with Futaba, though."
    "Apart from a few spare instances, she’s been one of the most careful of all."
    "That changes today."
    "The only question is {i}who{/i} is intruding this time?"

    play sound "knock.mp3"

    s "..."

    "Another knock."
    "Can we wait them out? "
    "Will the person on the other end simply go away if we wait for {i}long{/i} enough?"

    f "What...do we do?"

    play sound "knock.mp3"

    s "There are a few things we {i}can{/i} do."
    f "I’d appreciate it if you would start naming them because I’m both extremely lightheaded and also...in a minor state of shock, I think?"

    play sound "knock.mp3"

    s "You said you didn’t notice being followed, right?"
    f "Yeah?..."
    s "Then, do you think one of the others got tired of waiting around and wants a piece of me too?"
    f "I...uhh...maybe? "
    f "But I’m not really..."

    play sound "knock.mp3"

    s "You want me all to yourself?"
    f "I...um..."
    f "Uh-huh..."
    s "You think you’re good enough for that?"

    scene mollyalsowantsxmasdick3
    with dissolve

    f "I really hope you’re still in character and not being serious right now."

    play sound "knock.mp3"

    s "Of course I’m “still in character.” I’m just not really sure how to handle this apart from either waiting until they go away, which clearly isn’t going to work, or letting {i}them{/i} in as well."
    f "But we don’t even know {i}who{/i} it is. "
    s "Well, who do you {i}want{/i} it to be?"
    f "Henry Cavill."
    s "Who?"
    f "Some...hot guy. He’s an actor."
    s "I doubt it’s him, Futaba. It has to be one of the girls. Besides, I wouldn’t want to share you with some other guy anyway."
    f "Sure. But I don’t want to share you with some other {i}girl.{/i} So neither one of us is going to get what we want."

    play sound "knock.mp3"

    s "Do you want to try hiding then?"
    f "{i}Where?{/i} This is a bathroom. There’s nowhere {i}to{/i} hide."

    scene black
    with dissolve2

    "I carefully slide Futaba back to the ground so she can straighten her dress out and...at least {i}attempt{/i} to disguise the fact that I emptied myself into her several minutes ago."

    play sound "knock.mp3"

    "The knocking goes on for another five minutes before I give in and decide to open the door."

    play sound "static.mp3"
    scene mollyalsowantsxmasdick4 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    "But who I find on the other side is slightly unexpected. Especially since I didn’t see her with Futaba’s group when the two of us “snuck” away."

    mo "Something suspicious is afoot here..."
    s "What makes you say that, Molly?"

    scene mollyalsowantsxmasdick5
    with dissolve

    mo "The fact that you are not wearing pants."
    s "Oh. Shit."
    f "Seriously, Sensei?! You had like five whole minutes to put them back on!"
    s "Yeah, but you didn’t warn me. I’m much more used to having my pants off than on, so this is kind of {i}your{/i} fault too."

    play sound "static.mp3"
    scene mollyalsowantsxmasdick6 with flash
    stop sound

    mo "Then it’s true what the innkeeper says — that a knight’s been having his way with the farmer’s daughter."
    s "I thought your father was an architect, Futaba?"
    f "I think she’s just...roleplaying like normal, Sensei."
    mo "Is now {i}really{/i} the best time be running around and unlocking h-scenes, Sir? Because you never know when you might encounter another player embarking on various side quests."

    scene mollyalsowantsxmasdick7
    with dissolve

    mo "Like {i}me{/i} for example. I was merely minding my own business, scouring Tsukioka Manor for dungeons to crawl through when- what’s this? {i}Screams{/i} coming from a nearby cave? I simply {i}had{/i} to investigate."
    s "Sure. But you’re not delusional to the point where you’d hear those screams and not immediately interpret them as people having sex. You knew what you were walking into."

    scene mollyalsowantsxmasdick8
    with dissolve

    mo "Aye! And I am prepared for whatever it is that will happen to me next, Sir!"
    f "Oh, god..."
    f "Molly, did you really mean to...intrude? If you knew it was me in here with Sensei-"

    scene mollyalsowantsxmasdick9
    with dissolve

    mo "Oh, that much was unknown to me. I had assumed the Supreme Overlord was in here with someone more...{i}prone{/i} to engaging in illicit affairs at parties."
    f "L...Like who?"
    mo "Most others, honestly. This is rather unlike you, Xessaxia. But I appreciate the boldness and will allow you to carry your Christmas miracle over to our next session."
    f "Greaaaaat. What an...awesome reward in exchange for you now knowing that Sensei and I are...{i}hanging out.{/i}"
    mo "{i}Now?{/i}"
    f "Wonderful. So you knew too, then. And, since you’re here, I’m assuming Sensei is...{i}hanging out{/i} with you as well."
    s "Molly’s new to the harem. "

    scene mollyalsowantsxmasdick10
    with dissolve

    mo "Aye! Which means it’s time for me to catch up! And what better place to fall deeper into corruption than a mysterious {i}cave{/i} while being watched by a satyr?!"

    scene mollyalsowantsxmasdick11
    with dissolve

    mo "Unless said satyr would rather take part in the festivities as well. Which I assume is quite unlikely given that she rolled a natural one on sexuality."
    s "Futaba?"
    f "Wha- of course not. You said no to Henry Cavill, so it’s only fair that I-"

    play sound "static.mp3"
    scene mollyalsowantsxmasdick12 with flash
    stop sound

    s "Got it. I’ll just take care of Molly next then."
    mo "EYEAAHH?! S...SIR?!"
    f "While I’m still in the room?!"
    s "Yeah. You could use some time to recover, right? "
    f "Well...yes! But I don’t think this is particularly comfortable for either one of us!"

    "I lift Molly up and throw her onto some kind of dresser thing or...I don’t know. I’m sure there’s some fancier word for it that I don’t know about because I wasn’t privileged enough to grow up in a place like this."
    "However, I {i}have{/i} managed to somehow claw my way to the top. So I’ve reached the point where I have no trouble reaping and tending to the crops others have painstakingly grown. "

    mo "Are you...are we going to, like...actually {i}do it{/i} this time, Sir?"
    s "No. I just came inside your friend and it’ll take me a little while to {i}recharge.{/i} But that doesn’t mean I can’t figure out what to do with you."

    scene mollyalsowantsxmasdick13
    with dissolve

    mo "Tch. It’s always the farmer’s daughter. Just once, I’d like the knight to have his way with another traveler instead."
    f "Yes. Forgive me for having the {i}audacity{/i} to have sex with Sensei where I thought no one would find us."

    scene mollyalsowantsxmasdick14
    with dissolve

    mo "A...Always check the stables? "
    f "I thought this was a {i}cave.{/i}"
    mo "Check...there too! The fact of the matter is, the two of you decided to have your tryst in a place that someone experienced in CG-hunting would surely-"

    play sound "static.mp3"
    scene mollyalsowantsxmasdick15 with flash
    stop sound

    mo "FiiiiIIIiIIIIiIIIIiiiiIINd?!!?!?! AaAAAaah! Sir!?"
    f "I don’t really know why I thought you wouldn’t be the type to do something like this, Molly."
    mo "D...D-Do what?! I was merely...hunting slimes when...this man seized me and...aaaAaaah!"

    "I shift her panties to the side and slip two of my fingers inside of her."
    "I figure I won’t have to start slowly given that she’s surely “practiced” on herself before today."
    "Probably with me too if the voices that come and go are worth believing. "
    "The monks are gone for now. The sounds that bounce off of the marble must have scared them away. "
    "They’re plentiful now. Two felt so lonely, but three? This is how it {i}should{/i} be. Even if one of them is only here reluctantly."

    f "So...what am I supposed to do now? Just wait?"
    mo "K...Kiss me...Xessaxia!"
    f "No."
    mo "Hah...haaah...it was...worth a shot! I’m taking...away your...Christmas miracle!"
    s "Want to try talking dirty again, Futaba? You were getting really into it when it was just the two of us."

    scene mollyalsowantsxmasdick16
    with dissolve

    f "To...{i}who?{/i} You’re touching Molly, not me. Am I supposed to...narrate it? How does this work?"
    mo "I...think a little...narration would...be nice!"
    f "Then, uhh..."

    scene mollyalsowantsxmasdick17
    with dissolve

    f "He...um..."
    f "Used his hands to...bring pleasure to the...traveler...It was the only way to...satisfy his...curiosities and...uhh...lust?"
    s "It sounds like I’m listening to an audio-book all of a sudden."

    scene mollyalsowantsxmasdick18
    with dissolve

    f "Aaaah! Forget it! I’ll just go back to the party and cover for Molly or something!"

    scene black
    with dissolve

    f "Enjoy the {i}knight,{/i} you thief! I hope he...sees how evil you are and...can’t get hard because of it!"

    play sound "doorslam.mp3"

    "Futaba slams the door behind her and, presumably, runs down the hall to tear herself away from the now-screaming Molly MacCormack."

    play sound "lock.mp3"

    "I reach over and lock the door behind her. "

    scene mollyalsowantsxmasdick19
    with dissolve2

    "It never makes much of a difference, but at least it’ll prevent someone else from barging in while I’m stirring the insides of a small Irish girl with my fingers."

    mo "Mmnghg! S...Sir! I’m sorry for...interrupting! I had assumed that...probability favored...the bisexuals! "
    s "You knocked on the door expecting to find yourself in a threesome moments later?"
    mo "It was less of an...expectation and...more of a...wish!"
    s "You’re that much of a pervert, huh?"

    scene mollyalsowantsxmasdick20
    with dissolve

    mo "Hah...this should...come as no surprise to you...Sir!..."
    mo "We’ve...reached the point where...ngaaah...things like that are...bound to happen! The harem has...grown too large...for any one of us...to {i}ever{/i} expect to get to you alone! So forgive me for...wanting to party up!"

    scene mollyalsowantsxmasdick21
    with dissolve

    mo "But I suppose that...now I..{i}aaAaaaAahhh...{/i}finally get to experience a...holiday tryst!"

    "At least one that you’re conscious for."

    mo "That feels...amazing, Sir..."
    mo "So much better...than when I do it!..."
    s "And you do it a lot, don’t you?"
    mo "Yes...so often, Sir...I’m such a naughty girl...I’m so needy...I want it so bad...every day...every night...I can’t...be sated...Sir!"
    s "What do you think about when you do it?"

    scene mollyalsowantsxmasdick22
    with dissolve

    mo "That...ngah...depends...Sir!"
    s "On what? "
    mo "On...whatever mood I’m in that day..."
    mo "Sometimes...I like to imagine myself...being used by a horde of goblins..."
    mo "And other days...that I’m the...regent queen of an ancient elven society...holding the head of an aspiring suitor between my legs..."
    s "That is an extremely specific fantasy."
    mo "It’s not...always like that, Sir..."
    mo "A lot of the time, I...aah...I just think about...exactly what I’m thinking right now..."
    s "Which is?"

    scene mollyalsowantsxmasdick23
    with dissolve

    mo "How I want you to bend me over and fuck my little brains out, S-"

    scene mollyalsowantsxmasdick24
    with hpunch

    mo "HYAAAaAAaAAAH!!!~~~!!!~"

    "I hear what I want to hear, so I give her what she wants to feel. Or a taste of it, at least, since I’m still awaiting my second or...third or...whatever wind I’m owed after blacking out and cumming inside of Futaba."
    "I care not about goblins or queens, just the fact that this tiny creature somehow gets off to thoughts of {i}me.{/i}"
    "That she’d do as I say and spread her legs to welcome me. That she’d look me in the eyes and me make feel that, for once, {i}I{/i} am the fantasy she’s lost in. "
    "That she’d do it all looking like this. Adorable, yet trapped in ecstasy as she squirms under my touch."
    "It’s the type of temptation I would never be able to hold myself back from — even when I tell myself I can."
    "Or I did."
    "Or I didn’t. "
    "She is a gem of far more than just the Emerald Isle."

    mo "AAAAaaaAAAAh SSSSssssiiir!!!!! It’sssss...c...ccccummmmming!"
    s "Yeah...I bet that feels good, huh? Way better than watching porn in your room, isn’t it?"

    scene mollyalsowantsxmasdick25
    with dissolve

    mo "Nnnghghghhh!!! Get...hard alreadyyyyy!!!!"
    s "You want it that badly?"
    mo "Yes! Yes, yes, yes, yes! I want it, Sir! I want it! I want you to fuck me...I want you to fuck me...so fucking hard! Aaah! Sir! Haah! Fuck....me!"
    s "You can beg all you want. It doesn’t change the fact you got to me a little too late."
    mo "So if I...went up to you first-"
    s "I’d have bent you over...and fucked your little brains out...just like you want."

    play sound "static.mp3"
    scene mollyalsowantsxmasdick26
    with flash
    stop sound

    mo "AAAAAH! YES! SIR! SIR! I CAN’T! I’M...HAAAH! SIR! SIIIIIIIR!"

    with sexfade
    with sexfade
    scene mollyalsowantsxmasdick27
    with cumflash
    with hpunch

    mo "EYAAAHAAAHAHHH!!!!!!!~~~ AAAAaaaaaAAAHHEEHHH!!!!!! HAAAA!!!! AAAAHHH!"

    with sexfade
    with sexfade
    scene mollyalsowantsxmasdick26
    with cumflash
    with hpunch

    mo "MMMGNHHGHHHH! I’M STILL...AAAAHH...MMFHHHH!! MMMMMMMM!~~~~~~"

    with sexfade
    with sexfade
    scene mollyalsowantsxmasdick28
    with cumflash
    with hpunch

    mo "AAaaaaahhhAHHHHH...AAAaaaaaaahh!!! Haaaaaaahhhhh!!!!"

    scene mollyalsowantsxmasdick29
    with dissolve2

    mo "Haaah...haaah...haaaah! Oh...my lord..."
    mo "I’ve never......that hard......aaah!"
    s "Is now a good time to tell you how cute you look tonight?"

    scene mollyalsowantsxmasdick30
    with dissolve

    mo "Yes, but...hah...it would have been a better time if...we weren’t done yet."
    s "Who says we’re done?"

    scene mollyalsowantsxmasdick31
    with dissolve

    mo "Heh?"
    s "I was planning on keeping Futaba in here until the monks died."
    mo "Which...which ones?"
    s "Doesn’t matter. Point is, she’s gone. You’re not. Now get on your knees and make me hard again."
    mo "Lord Godfrey’s gonads, I’ve never been so turned on by a single sentence before."
    s "Yeah, Futaba liked being talked down to as well. Guess both of you are just filthy fucking whores now."

    scene mollyalsowantsxmasdick32
    with dissolve

    mo "I mean...I don’t know if I’d go {i}that{/i} far, Sir. I may be a degenerate, but I’m not sure how I feel about-"
    s "No, Malvin. I’m not going to say that. She clearly didn’t respond well to the first one."

    scene mollyalsowantsxmasdick33
    with dissolve

    mo "M...Malvin?"
    s "I don’t {i}care{/i} if you’ll be gone after tonight. You’re what I have {i}now,{/i} so I’m going to need you to be productive in some capacity. Pareidolia was an asshole, but at least he got things done. "

    scene mollyalsowantsxmasdick34
    with dissolve
    play sound "lock.mp3"

    mo "{i}Ahem.{/i} "
    s "Then why can’t I get hard? It’s not because she’s the fourth girl today, is it? Can my mind not keep up? Is it because {i}you guys{/i} are taking up too much space in it all of a sudden?"

    play sound "dooropen.mp3"

    mo "{i}Ahem, ahem, ahem.{/i}"
    s "Molly, just...hold on for one second, okay? I’m trying to get this fucking guy out of my- no. I already told you I’m not saying that to her."
    tb "Excuse me. But in the words of that {i}very young{/i} white girl, may I just say — {i}ahem.{/i}"

    $ renpy.end_replay()
    $ mollylust10 = True

    $ molly_lust += 1

    stop music

    jump christmastsubasa1

label mollyinvite1:
    play sound "phonebeep.wav"

    "I tap on Molly’s name in my phone and wait for her to answer."
    "And I do this knowing that at least Ami is going to be present today."
    "But hey, having her encounter the various girls I invite over to the house is practically tradition at this point."
    "And while it very well may be a tradition that will ultimately wind up with someone dying, it’s a tradition nonetheless."
    "Now please excuse me as I put Molly’s life in jeopardy for at least the second time since I have met her."

    play sound "phonebeep.wav"
    play music "breeze.mp3"

    mo "Well met, traveler! ‘Tis I — Molly MacCor-"
    s "I know who you are, Molly. I needed to tap on your name in order to call you. That is how phones work on planet Earth."
    mo "Aye. ‘Tis strange to think that once upon a time you’d have needed to pry my name from the clutches of ye olde rolodex. To what do I owe the pleasure though, Sir? Has fair Arborea’s phone departed this mortal coil?"
    s "No. I just wanted to hear your voice and remind you that I care for and appreciate you."
    mo "Okay, but what do you really want?"
    s "Nothing in particular."
    mo "You want to do ecchi stuff, don’t you?"
    s "Sure. So long as you’re fine with Ami joining in."
    mo "..."
    s "Mo-"
    mo "Hold on. I’m deliberating."
    s "Molly, I was kidding. I was just wondering if you wanted to come over and do...whatever it is you like to do."
    mo "But...Sir! The things {i}I{/i} like to do only make you want to punt me. It’s why I try to avoid you on Tuesdays as server resets compel me to speak about things you’d never-"
    s "I’m bored. Do you want to just watch a movie or something?"
    mo "FFFFFF- This is exactly what I mean! Why lead me on like this?!"
    s "The movie thing was a joke. I’m fully prepared to endure whatever sort of nerdy, geeky, and/or otaku stuff you want to force upon me today. I promise."
    mo "But...{i}why?{/i}"
    s "Do you think this is a trap?"
    mo "Yes."
    s "Cool. Then be at my place in an hour."
    mo "Sir! I-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and...I know what you’re thinking. “Sensei, you’re so manly and cool. What could have possibly compelled you to do such an uncharacteristically lame thing?”"
    "Well, the answer to that is simple."

    play sound "static.mp3"
    scene mollyfirstinv1 with flash
    stop sound

    "Molly’s cute and I want to put my penis inside of her."
    "And going along with the things she wants to do sometimes feels like the {i}least{/i} I can offer in exchange for the real estate that is her lower body."

    a "Molly? What are you doing here?"

    "Just kidding. I simply want her to be happy."
    "{i}I’m not kidding about wanting to put my penis inside of her, though.{/i}"

    mo "Top ‘o the...evening, Ami! As unexpected and unbelievable as it may sound, the Supreme Overlord has summoned me here to engage in gaming and/or anime and/or cosplay with him!"
    a "Ha-ha. Now tell me why you’re really here."
    s "She’s telling the truth."

    scene mollyfirstinv2
    with dissolve

    a "She’s {i}what?{/i}"
    mo "For some reason that I dare not question, the Herald of the Adolescents has seen the light and wishes to learn more about my way of life!"
    a "I was kind of hoping your midlife crisis would be more along the lines of wanting to cuddle with your daughter all day long...but I guess I can live with this too?"
    s "Oh, right. I forget you’re {i}also{/i} uncool sometimes."

    scene mollyfirstinv3
    with dissolve

    a "I don’t need to be cool! I’m cute! Teehee!"
    mo "Firstly, there is nothing {i}uncool{/i} about engaging in gaming and/or anime and/or cosplay! That is a dated outlook, Sir. "
    mo "Secondly, however, is there something specific you {i}wanted{/i} to do?"
    mo "Or are we but seconds away from the rug being pulled out from underneath mine legs, leaving me sobbing and wishing for death on the kitchen floor?"
    a "I mopped today, so at least you’ll die clean."
    s "No murder in the house, Ami. And Molly, why don’t we just play that game you girls are always playing together? You seem to enjoy that enough and I’ve shrugged it off in the past, so-"

    scene mollyfirstinv4
    with dissolve

    mo "Hooooold on! Surely you jest, Sir! One does not simply walk into Mordor. There are preparations that must be made. Stories that must be carefully crafted and...all sorts of other things!"
    a "Why that, Dad? If you really wanted to learn, you could have just asked me."
    s "I’m just struggling to think of anything else Molly likes as it all sort of blends into this weird soup of Japanese culture that I’m surprised Molly even knows about."

    scene mollyfirstinv5
    with dissolve

    mo "Dungeons and Dragons is from the states, Sir. It isn’t Japanese at all."
    s "Then maybe I’m just secretly American and want to feel a slice of home again."
    a "Come to think of it, we {i}are{/i} pretty culturally American in like a million different ways. I wonder why?"
    s "No clue. But anyway, let’s play. I may never feel this generous again."

    scene mollyfirstinv6
    with dissolve

    mo "Sir, we can’t! You don’t even have a character yet!"
    a "Don’t you have like a trillion premade ones, though? Can’t he just use one of those while you...run some campaign from a book or something?"
    s "I could always just {i}make{/i} a character. I can’t imagine it takes very long."

    scene mollyfirstinv7
    with dissolve

    mo "I can’t even begin to explain how many problems I have with that statement, Sir."

    scene mollyfirstinv8
    with dissolve

    mo "But it matters not! For character creation is arguably the best part of the experience and one that I’m not inherently inclined to believe you’ll utterly despise!"
    a "Yay! Everyone wins. Except for my daddy who will probably still kind of despise it."

    scene mollyfirstinv9
    with dissolve

    mo "I...I’d heard that the relationship between the two of you was leveling up, but...hearing you address the Supreme Overlord in such fashion is...a bit more jarring than I expected."
    a "Hahah! You should hear how I say it in my dreams."

    play sound "static.mp3"
    scene mollyfirstinv10 with flash
    stop sound

    "So anyway, we’re here now. And I’m only a little bit in over my head."
    "It’s a type of drowning I’m prepared for, though. And not just because I’m the one who threw myself off the bridge and into the water, but because it...well, it could be {i}fun.{/i}"
    "I think I need that — something to bond with people over that isn’t just...literally hovering over them."
    "Frankly, I’ve probably needed something like that for quite some time. I’ve just never been as acutely aware of how true that is until right now due to how quiet it’s become inside of my head."
    "But hey, if I’m good enough at this game, maybe Molly will let me borrow one of the voices inside of hers."

    mo "Now! There are several different ways in which we can tackle this, Sir."

    scene mollyfirstinv11
    with dissolve

    mo "When it comes to crafting a character, there are many questions to be asked. What race do you prefer? Is there a particular class you’re interested in? Where do you come from? What are your goals?"
    mo "And while I don’t expect you to have the answer to all of them right away-"
    s "I want to be a bird-man warrior from Tokyo who kills the demon lord."

    scene mollyfirstinv12
    with dissolve

    mo "Or you have {i}all{/i} of the answers already and they’re {i}all{/i} incorrect. I don’t know why I expected any less."
    a "Maya plays a bird-man. {i}That’s{/i} not why you’re suddenly interested in this game, is it?"
    s "Just one of many unfortunate coincidences that involve the two of us. Just tell yourself I’m learning so I can be closer to my daughter."

    scene mollyfirstinv13
    with dissolve

    a "Easy! That’s already how I rationalize practically everything."
    mo "Sir, if you’re serious about being an Aarakocra, which is the D&D equivalent of “bird people,” I’ll mark it down. "
    mo "I’d urge you to at least {i}look{/i} at the other options first though, so you can be sure that what you’re choosing is right for you."
    s "Well, what other options are there? I didn’t even realize being a bird-person was possible. I was just naming stuff."

    scene mollyfirstinv14
    with fade

    mo "Oof. Where do I even begin? In terms of traditional fantasy that normies like you would be familiar with...you’ve got elves, dwarves, orcs, gnomes, humans, half-orcs, half-elves, halflings-"
    s "Why are there so many halves? That last one just sounded derogatory."
    a "That’s what Ayane plays. They’re these weird mini-people. You’d like them because reasons."
    s "I don’t like the implications of that, Ami."

    scene mollyfirstinv15
    with dissolve

    mo "In terms of {i}less{/i} traditional fantasy if you’re feeling a bit more exotic, there are races like...aarakocra, tabaxi, kobolds, aasimar, tieflings, the warforged, and even this race of turtle people called tortles."
    s "That’s just “turtles” but slightly mispelled."

    scene mollyfirstinv16
    with dissolve
    play sound "dooropen.mp3"

    mo "Right you are, Sir! And this is nowhere close to even {i}half{/i} of the official playable races in 5e! "
    mo "And while each one comes with their own set of racial advantages, certain races are better at certain jobs or roles than others."
    mo "Many people, myself included, like to use a character’s race as the starting point for character building as the majority of them provide some sort of base-level fantasy to jump off of."
    mo "But if the race itself is not important to you, it’s perfectly fine to work backwards as well! And seeing as you don’t really know about any of them yet, why not first ask yourself {i}what{/i} you want to do with-"
    ni "Hey, sorry to interrupt, but does anyone want coffee?"

    scene mollyfirstinv17
    with fade

    mo "Ah! A new challenger approaches!"
    ni "Yeah, my bad. I was planning on waiting for you to finish your speech, but I had a feeling I was going to be standing here for the next year or two and the warmer only stays on for an hour."
    s "It’s not what it looks like, I swear."
    ni "You mean you’re {i}not{/i} making a D&D character with two teenage girls right now?"
    s "That’s right. I’m here to seduce them."

    scene mollyfirstinv18
    with dissolve

    ni "Is seducing teenagers really more acceptable in your eyes than engaging in stereotypically nerdy conduct?"
    s "Yes. I’m a cool guy. And I need to remain a cool guy to keep up my awesome cool guy image."
    mo "{i}Hah.{/i} Those who are born as normies ultimately {i}die{/i} as normies. This is presumably naught more than a temporary phase for the Supreme Overlord here. But one I must indulge regardless!"
    mo "Also, I like your shirt."

    scene mollyfirstinv19
    with dissolve

    ni "Thank you! I relate to her on a level that not many understand. I like your hair."
    mo "Thank you! It’s...red."
    ni "Yes."

    scene mollyfirstinv20
    with dissolve

    ni "In regard to the whole “normie” thing, though, let me just say...this guy wasn’t {i}always{/i} as lame and uninteresting as he is right now."

    scene mollyfirstinv21
    with fade

    ni "As a matter of fact, the two of us were {i}both{/i} pretty huge dweebs back in the day."
    a "Yay! Flashback story! I can’t wait to not be in it because Dad didn’t love me yet!"
    mo "What...do you mean exactly?"
    ni "I mean he and I used to hang out in my room watching mech shows and playing Dragon Quest all day."

    scene mollyfirstinv22
    with hpunch

    mo "YOU WHAT?!?!?!?!"

    play sound "static.mp3"
    scene mollyfirstinv23 with flash
    stop sound

    s "Oh, great. Here we go."
    mo "THE SUPREME OVERLORD HAD AN OTAKU PHASE AND I NEVER KNEW ABOUT IT?! "
    mo "THIS IS VITAL INFORMATION THAT HAS BEEN KEPT FROM ME FOR REASONS UNKNOWN! IT IS INCONCEIVABLE! IT IS UNFORGIVABLE!"
    ni "Why does she keep calling him the “Supreme Overlord?” Is this a chuuni thing?"
    a "Molly’s entire personality is a chuuni thing. Also, you should hear the second half of that title. That part’s even {i}more{/i} interesting."
    s "It certainly is not. And we certainly {i}will{/i} not be talking about anything Niki and I did in her bedroom when we were children. "

    scene mollyfirstinv24
    with dissolve

    ni "Yeaaaah...that’s probably for the best."
    a "I...am suddenly much more interested in this flashback."
    mo "ME TOO! BUT MY RAGE OVERRIDES MY CURIOSITY!"
    mo "Why didn’t you ever tell me, Sir? You don’t feel guilt over your childhood interests, do you? Because if it’s a matter of merely growing up-"
    s "It’s not that. I just don’t really {i}remember{/i} any of it. Everything from back then is...still kind of blurry to me."
    ni "I could probably bring those memories back if I try hard enough. I might still even have one of our old save files on a memory card back at my parents’ place."
    a "Yeah, so about what you and Aunt Niki did when you were kids-"
    s "Sorry. Can’t remember that either."

    scene mollyfirstinv25
    with dissolve2

    a "Heeeeeey..."
    ni "{i}Yes,{/i} Ami?"
    a "Story please?"
    ni "Mmmmmm..."
    ni "I’ll tell you when you’re older."

    play sound "static.mp3"
    scene mollyfirstinv26 with flash
    stop sound

    a "Aaaaaaah! Why is it okay for me to hear you guys going at it from across the house but {i}not{/i} okay for me to hear about the way you explored when you were little?! I need to know!"
    s "Ami, go to your room."
    a "WE’RE ALREADY HERE!"
    mo "Mech shows...Dragon Quest..."
    mo "I can’t believe I never knew..."

    scene mollyfirstinv27
    with dissolve

    mo "All this time, we had that thread in common...just obscured by the passage of time and the onset of shame. But...for what?"
    ni "Uh-oh. I think your friend might be on the verge of having an existential crisis, Ami."
    s "Hey, I’m {i}always{/i} on the verge of having one of those- so that’s one {i}more{/i} thread we have in common."
    a "Just let her ride it out. Sometimes, time is the best medicine for-"

    play sound "static.mp3"
    scene mollyfirstinv28 with flash
    stop sound

    mo "That settles it!"
    a "Or not."
    s "Settles what? Did you finish my character without me? Did I beat the game?"
    mo "No! Your character has been scrapped! Because, in the words of Illidan Stormrage, YOU ARE NOT PREPARED!"
    mo "But I’ll tell you what, Sir! I will not sit idly by as you gaze upon the days of your youth as if they were a dark place that you should feel ashamed of!"
    s "Boy, do I have bad news for you."

    scene mollyfirstinv29
    with dissolve

    mo "Save it! Speak not of your darkest days, for Molly MacCormack will show you the light!"
    mo "...Not to be confused with the light Yasu is always speaking of, though. A new light! One that shines favorably upon your childhood affinities and shows you there is naught to be ashamed of!"
    mo "You can still enjoy what you once loved! You’re not too old for games, Sir! Age is just a-"

    scene black
    with dissolve
    stop music fadeout 10.0
    play sound "tackle.mp3"

    ni "So! About that coffee-"

    "Niki breaks up the conversation before it can spiral any further out of control and...potentially invoke something or...{i}someone{/i} I don’t want to be here right now."
    "Molly goes back to Ami’s desk, removing a laptop from her bag and taking the next ten minutes to try and figure out which Dragon Quest I apparently played when I was younger."
    "And while she doesn’t press me any further on the contents of my past {i}outside{/i} of that, she makes it clear that she has a new mission now."
    "She wants to turn me back into a loser."

    $ renpy.end_replay()
    $ mollyinvite1 = True
    $ molly_love += 1

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label mollyinvite2:
    play sound "phonebeep.wav"

    "I tap on Molly’s name in my phone and wait for her to answer. But I don’t intend to partake in any sort of character building this time around."
    "Unless that character is her vagina and I am building it with my penis."
    "That probably didn’t make as much sense as I wanted it to, but you get the point."

    play sound "phonebeep.wav"
    play music "love.mp3"

    mo "Hello?"

    "And so will Molly soon if by “point” we mean “penis.”"
    "That one worked a little better."

    s "Hey, Molly. What’s-"
    mo "Ah! Excellent timing, Sir! I was just thinking about you."
    s "I bet it was sexual."
    mo "Not this time! Though, I will admit that {i}has{/i} become somewhat of a regular occurrence for me as of late."
    mo "Well...maybe not so much “late” as it is...from the moment we first met. But surely that’s not why you called today!"
    s "It kind of is, actually."
    mo "Oh."
    s "Yeah. I think you should come over. And then I think you should take your pants off. And then I think I should take my pants off too."
    mo "This sudden influx of lustful affection is turning the somewhat sentimental mental anecdote I had in mind into a puddle of relatively tangible desire between mine legs. Quest accepted, Sir!"
    mo "Though, I would appreciate it if I could at least {i}mention{/i} the non-sexual thing I had in mind."
    s "I’ll think about it and come up with an answer based on your performance today."
    mo "I’m going to be graded?!"

    play sound "phonebeep.wav"

    "I hang up the phone and figure it’ll be easier to iron out all of the important details over text."
    "That {i}and{/i} it makes it easier to avoid whatever brand of Molly-coded “sentimentality” she wants to bring to the table."

    play sound "static.mp3"
    scene mollycomesliterally1 with flash
    stop sound

    "For too long, I have let “feelings” cloud the space between the two of us. But as this life (If you could even call it that) becomes increasingly less coherent, I become increasingly impatient."
    "And I really {i}do{/i} think it would be best to just “break her” once and for all. Like she wants me to. Like she dreams of — {i}without{/i} the caveat of needing to fix me first."
    "Assuming she cares much about that at all, of course. She might not. I haven’t put forth that much effort when it comes to “fixing” her."
    "That said, though...I can’t find much about her that {i}requires{/i} fixing in the first place."
    "She’s weird, yeah. But she’s also..."
    "Molly."
    "..."
    "And I think that’s what I need right now."

    play sound "doorbell.mp3"

    "The doorbell rings."
    "Outside awaits one more mistake."

    s "It’s open..."

    play sound "dooropen.mp3"
    scene mollycomesliterally2
    with dissolve

    mo "Aye! It surely is, Sir. But I do hope it will remain locked from this point on if your cum meter is as full as you made it sound."
    s "My...what?"

    scene mollycomesliterally3
    with dissolve

    mo "Your cum meter, Sir! The white bar in the bottom right hand corner of your screen that slowly fills up over time and needs to be emptied by a sexual partner or masturbation. Don’t all men have one of those?"
    s "You play too many games, Molly."

    scene mollycomesliterally4
    with dissolve

    mo "And you {i}don’t,{/i} Sir! But that changes today!"
    mo "Because the one and only Molly MacCormack has devised a plot that will aid both your cum meter {i}and{/i} the crippling depression that has turned you into a boring normie!"
    s "Normally, this is the part where I’d talk about how draining my cum meter is the exact sort of thing that {i}would{/i} help with that second part. But sure, let’s hear what you came up with."

    scene mollycomesliterally5
    with dissolve

    mo "In this bag, I possess a laptop with so many porn games from so many genres that Jesus Christ would cast me to Hell the moment he stepped within one hundred miles of it. And today, Sir?"

    scene mollycomesliterally6
    with dissolve

    mo "We are going to play them {i}all.{/i}"
    s "{i}All{/i} of them?"
    mo "No, that was a lie. Deception check failed. Playing all of them would take years."

    scene mollycomesliterally7
    with dissolve

    mo "But we {i}will{/i} play some of them. At least one. We {i}have{/i} to."
    s "Sorry, we {i}have{/i} to? We can’t just skip all that and cut straight to the good part?"
    mo "Sir, the buildup {i}is{/i} the good part. It’s what makes it possible for people to sit through hundreds of hours of content in pursuit of sex with their favorite character. It’s why visual novels are so successful."
    s "That just sounds like needless padding to me."
    mo "And surely sometimes it is! But others? It’s what makes everything seem so {i}real!{/i}"
    s "So...you play games to escape from reality...but you want your fake reality to feel like...actual reality?"

    scene mollycomesliterally8
    with dissolve

    mo "Not all the time. Sometimes, you just want to get raped by an orc. Or have your cum meter drained by some sort of spider monster that latches onto your penis without consent."
    s "One of those felt weirdly relatable to me."
    mo "That’s quite disturbing, Sir. Would you like to talk about it before I’ve reached the height of my arousal?"
    s "Nope. Let’s go."

    scene black
    with dissolve

    mo "Aye, Sir! Let’s! Are we- oh! Shoes. Sorry. Mildly nervous. But also excited!"
    mo "Having an actual human to experiment with now is truly a game changer, Sir!"

    "Yeah..."
    "We’re just experimenting."

    play sound "static.mp3"
    scene mollycomesliterally9 with flash
    stop sound

    "All I’m doing is helping some weird, horny teen purge the pent-up lust from her system in an environment that doesn’t mask itself as a safe one."
    "She can’t be {i}put{/i} in harm’s way if she wanders into it on her own. And, in Molly’s terms, what she’s doing right now is probably akin to, like...venturing into the den of a dragon or something like that."
    "But she’s an adventurer. Or a traveler. Or whatever she calls herself."
    "She feels like it’s her duty to conquer me. But she doesn’t realize she’s not strong enough yet, so it’ll have to be a learning experience."
    "I’ll let her practice as much as she needs. I’ll let {i}anyone{/i} practice as much as they need."
    "I’ve grown used to newcomers flocking to my den in hopes of finding treasure, just to be burnt to a crisp before respawning at a nearby town...confused, tired and hurt."
    "She’s probably done this a million times before. Raided countless lairs...fought countless battles. And I imagine she's already learned a great deal about life from those experiences."
    "But there are some things in games that just don’t translate well, and we will always be one of them."
    "But it’s better me than someone who will pick her bones clean."
    "Dragons must eat too."

    mo "The goal here is simple, Sir. We ease you back into the world of gaming by introducing you to something that fits your {i}current{/i} interests more than your older ones."
    mo "No pink-haired pop stars are necessary to evoke such memories, surely. This is very obviously a task best suited to me of all people!"
    s "Why are you so desperate for me to like the same things as you, Molly?"

    scene mollycomesliterally10
    with dissolve

    mo "I’m not, Sir."

    scene mollycomesliterally11
    with dissolve

    s "What do you mean you’re not? You’ve been desperate to have something in common with me from the start. And you proved that again the last time you came over when-"
    mo "I {i}want{/i} you to like the same things as me, Sir. I want {i}everyone{/i} to like the same things as me because it provides more opportunities for me to form bonds with them. But it’s not {i}desperation.{/i}"
    mo "The reason I appear forceful {i}now{/i} is because I’m sad."
    s "Sad? Why?"
    mo "Because you stopped doing something that made you happy."

    scene mollycomesliterally12
    with dissolve

    mo "I don’t specifically know why, of course. Perhaps you had a good reason. Or perhaps you never really cared for such things {i}that much{/i} in the first place. I don’t know."
    mo "But when I compare that to myself...and envision a future in which {i}I{/i} am going around telling people I’m too old or “cool” to participate in certain things because they’re not traditionally accepted..."
    mo "I have a hard time describing the way that makes me feel."
    mo "It’s not good, though. And I think this world would be a lot better if we all just did what we wanted without fear of how others would look at us."
    s "You’re...surprisingly mature when you’re not pretending you can speak to trees."
    mo "Thanks, I hate it."
    s "Molly, I do appreciate this. And I’m glad you’re...putting some amount of actual care into this that doesn’t ultimately tie back to you just wanting someone else to play games with."
    mo "Of course, Sir. But I assume you’re leading up to some type of caveat now, so please- do your worst."
    s "I just don’t think playing a {i}porn{/i} game together is going to reignite whatever affinity I had for role playing games when I was a kid."

    scene mollycomesliterally13
    with dissolve

    mo "Why not, Sir?"
    s "Well, to put it simply-"
    mo "You think I’m going to get too horny and attack you? And that it will all be counterproductive because barely any {i}gaming{/i} will be done at all?"
    s "You took the words right out of my mouth."

    scene mollycomesliterally14
    with dissolve

    mo "Then perceptive you are, Sir. For that {i}would{/i} happen under normal circumstances. However!"

    scene mollycomesliterally15
    with dissolve

    mo "I may or may not be exceedingly close to fulfilling my lifelong fantasy of playing porn games with someone I like while we...both masturbate and fully immerse ourselves in our delusional perversions?"
    s "So it {i}is{/i} self-motivated."

    scene mollycomesliterally16
    with dissolve

    mo "N-No! I didn’t mean it like that! We don’t {i}have{/i} to if-"
    s "I’m kidding."

    scene black
    with dissolve2

    s "Put on whatever makes you the horniest. I want to see the {i}real{/i} Molly MacCormack in her natural element. When she isn’t just fingering herself to pictures of her friends, I mean."
    mo "Th...That’s far more rare than you think, Sir! You merely picked the worst time possible to-"
    s "Just shut up and pick a game, Molly."

    "........."
    "......"
    "..."

    scene mollycomesliterally17
    with dissolve2

    "I’m not sure how much time has gone by since we started. It’s been more than an hour, though. I know that for sure."
    "Which is long enough that even {i}I’ve{/i} been turned on by this game I still can’t be bothered to memorize the name of. So I can only imagine how Molly must be feeling."
    "Her breathing’s been getting heavier by the minute. Yet, despite how long we’ve been here, just inches from each other, we haven’t touched at all."
    "She squeezes her thighs together every now and then, trying to suppress or hide her arousal — something I don’t understand since indulging in it was meant to be the point of this awkward interaction."
    "But I guess it’s much easier to say things than to actually {i}do{/i} them. And if this really {i}is{/i} a fantasy of hers, I imagine she’s trying to stretch it out for as long as she can, but...that she’s {i}also{/i} a little scared."
    "I don’t blame her."
    "I’d be scared if I were her too."

    s "How hot are you right now, Molly?..."

    "Because I say things like that."

    scene mollycomesliterally18
    with dissolve

    mo "{i}Very,{/i} Sir..."
    mo "And...having you beside me is..."
    s "Not helping?..."
    mo "Not in the slightest..."

    "I say all sorts of things."
    "Typically, it’s just whatever will bring me closer to my target."

    s "Well..."

    "But right now...I care less about hunting and more about...{i}observing.{/i}"

    s "You can start whenever you want..."

    "Right now, I’ll let my curiosity guide my speech."
    "I’ve seen far too many times what happens to girls when they hand themselves over to me."
    "But Molly’s fantasy calls for something else. And it’s a wish she can easily grant herself by just doing what she’s done a million times before."
    "The only difference is I’ll be watching this time."

    scene mollycomesliterally19
    with dissolve

    mo "You don’t...mind...Sir?..."

    "And if I like what I see enough..."
    "Maybe I’ll join her?"

    s "Of course not...I {i}want{/i} to see..."
    mo "You won’t...make fun of me, will you?..."
    mo "Because...I know it may seem strange to you as...someone who doesn’t typically play these sorts of things, but-"
    s "It’s not weird at all, Molly..."
    s "Go on..."
    s "Show me what it’s like when you’re alone."
    mo "I..."
    mo "..."
    mo "Okay...{i}Sir...{/i}"

    scene mollycomesliterally20
    with dissolve

    mo "{i}Ah...{/i}"

    "She clumsily slides her hand into her shorts, not bothering to unhook the button. I can tell just how badly she’s been looking forward to this."
    "I watch carefully as her fingers dance beneath the fabric, imagining their tips inching closer to her clit..."
    "All while scattered protrusions of her knuckles through denim paint a picture of pleasure you can’t find in games."
    "I imagine her pale flesh, peppered lightly with freckles that feel like they only exist to make me want her more."
    "And while I know I could reach down and see them if I try to, I find the mystery itself more arousing this time."

    mo "{i}Hah.....aah.....{/i}"
    s "I bet that feels good, doesn’t it?..."
    mo "I’ve been holding it in...Sir..."
    mo "I didn’t want to...start without you..."
    mo "Will you...will you...join me?..."
    s "In a minute, probably..."
    s "I’m fine just watching you for now."

    scene mollycomesliterally21
    with fade

    mo "Do you......enjoy watching me......Sir?..."
    s "I do..."
    mo "Hah...mnn...that’s...excellent news...because...aahh! I think I..."
    mo "I think I...like it when you...watch me too..."
    s "Yeah...you love it when I look at you in general, don’t you?..."
    mo "Yes...{i}Sir...{/i}"
    mo "But you’re almost always...looking at someone else..."
    mo "I...aaah...I need to...stand out more...I need to...make you-"

    scene mollycomesliterally22
    with dissolve

    mo "Mnh!"
    s "You can get all sentimental later. I want to see you fuck yourself right now. Can you do that for me?"
    mo "Mmngh! Of course...Sir! But you...I want...I want..."
    s "What do you want? Say it clearly."
    mo "I want...to see you..."
    s "What do you want to see, Molly? Say it."
    mo "Show me...aah...how hard...you’ve gotten!..."
    mo "My fantasy...will only come true if...we’re {i}both{/i} doing this! It’s too...embarrassing...by myself!"
    s "Molly MacCormack is {i}embarrassed?{/i} I didn’t realize that could happen."
    mo "Hah...hahh! Of course it...can happen! Like...haaah...right now...I’m-"
    s "You’re gonna cum, aren’t you? I can tell by the way you’re squinting. Your fingers are moving faster too. You’re so close, Molly."
    mo "Mmngh! Sir...Sir!"
    s "Cum for me...Cum for me and I’ll give you what you want..."
    mo "Haah!...Aaah!....S....Sir!!!!! Aah! Aaah! Aaah! AaAaaaaAAAaaAAaahhhh-"

    play sound "static.mp3"
    scene mollycomesliterally23 with flash
    stop sound

    "And so she did. Which meant that {i}I{/i} had to hold up my end of the bargain."
    "While I unzipped and unbuttoned my jeans, Molly pulled her shorts off entirely, tossing her laptop to the side and allowing the glow of that unnamed porn game to become our only light for the time being."
    "She curled up next to me and pressed her head up against my chest, shifting her hips so her legs brushed against mine while she went right back to work."
    "Now, though, {i}she{/i} has something to look at. Something that isn’t encased behind glass and built out of pixels and polygons."
    "And she {i}sure{/i} does enjoy it."

    mo "Christ almighty, Sir...You’re an orc in your own regard, aren’t you?"
    s "What does that make you then? One of those halfling things?"
    mo "I certainly feel like one when I see {i}that{/i} next to my body..."
    s "You know I’ll fuck you if you want it, right?"

    scene mollycomesliterally24
    with dissolve

    mo "You really want to fuck me, Sir?..."
    s "More than anything right now."
    mo "But I gave you so many chances and you denied me for all of them."
    s "That was...in your best interest..."
    mo "My best interest?..."
    mo "You just wanted me to go home and masturbate to you, didn’t you?..."
    mo "You’re so mean, Sir...giving me the idea that I could experiment with you...only to string me along for eternities afterward..."
    mo "Do you have any idea how many times I’ve cum for you, Sir?"
    s "More than you have for Rin, I hope."
    mo "Aye...you’re certainly in first place now..."
    mo "And I want it, Sir...I want it {i}badly...{/i}"
    mo "I want to feel you inside of me...I want to ride you so hard that...it puts your cum meter on...cooldown for the next twenty four hours..."
    s "Then why are we still touching ourselves?"

    scene mollycomesliterally25
    with dissolve2

    mo "Because we can’t help it..."

    "Molly begins to finger herself harder and faster. And I can tell she’s looking at me, but the angle I’m stuck at prevents me from tying my gaze to hers."
    "Regardless, I can still feel her body. Her warmth. Her scraggly hair and her frail legs, twitching intermittently as she brings herself to the verge of one more climax."
    "All the while, I can feel one of my own approaching."

    mo "I’m glad...you’re such a terrible teacher...Sir..."
    mo "I can only imagine the things I’d do if you were {i}opposed{/i} to unlocking sex scenes with your students..."
    s "You think you’d come after me still?"
    mo "Let’s just say I’d be more inclined to take a page out of the Magistrate of Mammaries’ book and {i}force{/i} you to look at me."
    s "You’re not bold enough for that, Molly. We both know it."

    scene mollycomesliterally26
    with dissolve2

    mo "Do we, Sir?"
    s "Y...I...I thought we weren’t supposed to-"
    mo "We’re not. I just wanted to show you that I {i}can{/i} get a little bolder when I’m horny, Sir."
    s "Molly-"
    mo "Feel good?"
    mo "Still want to put it inside of me?"
    s "I...can’t imagine I’d last long at this point..."
    mo "Me neither, Sir...I’ll be cumming again any second now."

    scene mollycomesliterally27
    with dissolve

    mo "And I’d fear for your safety if you were to put it inside since I might accidentally snap it off."

    "She picks up the pace and wraps her hand tighter around my shaft, pumping the top half as I proceed to work on the bottom."
    "And while such a thing sounds like it could be a recipe for disaster if we’re not in sync, Molly manages to match my rhythm perfectly. Probably thanks to video games or something, so that’s cool."

    mo "You want to know how my fantasy ends, Sir?..."
    s "Hopefully...with my dick in your mouth..."
    mo "Close. Want to guess again?"
    s "Your...pussy?"
    mo "Coooolder. I’ll give you one more guess."
    s "Before what?"
    mo "I don’t know. I haven’t thought of that part."
    s "Molly-"
    mo "Cum on my face while I finger myself...{i}Sir.{/i}"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "That’s the hottest thing anyone has ever said to me."
    mo "Heheh! Seems like I’ve set a record I’m going to have to be-aahh!"

    play sound "static.mp3"
    scene mollycomesliterally28 with flash
    stop sound

    "I push Molly back as I position myself above her — so close that I can feel her breath on my cock as I go back to stroking myself."
    "She doesn’t let up either, spreading her legs and playing with herself as she gazes deeply into my eyes, finally able to meet hers."

    mo "Haah...Sir...give it to me...give it to me..."
    s "You’re gonna cum for me too, right?"
    mo "Sir...yes...sir..."
    mo "I’m...so close...so...so close..."
    s "Be louder..."

    scene mollycomesliterally29
    with dissolve

    mo "Aah.....Aaah!"
    s "{i}Louder.{/i}"

    scene mollycomesliterally30
    with dissolve

    mo "Aah! Ngaaah! Aaaah! S...Sir! I’m...haaaah!"
    s "Just like that, Molly...Lie there...and play with your little clit like the degenerate you are..."

    scene mollycomesliterally31
    with dissolve

    mo "Mnn! Mm! Sensei...Sensei! I’m cumming...I’m cumming!"
    s "Mmngh...Molly-"

    scene mollycomesliterally32
    with dissolve

    mo "Aaah...aaaaahn~"

    "Before I can even tell her what to do, she manages to figure it out. And I not only silently thank video games again, but pat myself on the back for making her fantasy play out presumably exactly how she wanted."

    mo "Aaah! Aaaah! Aaaaaaaah!"

    with sexfade
    with sexfade
    scene mollycomesliterally33 with cumflash
    with hpunch

    mo "AIAYAAAaaaaAHHhhhHHAAAAaaaAAAaaaAAAaaaHHHH!!!!!~!!!!~~~"

    scene mollycomesliterally34
    with dissolve2

    mo "Aaah...aaaaaah....aaaaaaaahhhh~"

    "She pulls her hand back and slumps down, falling helplessly into whatever sort of sensory overload is brought on by experiencing an orgasm while the guy you like jerks off onto your face."

    scene mollycomesliterally35
    with dissolve2

    mo "Ah...aaaaaaaaaah~"

    scene black
    with dissolve2

    s "This is a good look for you, Molly..."
    mo "{i}Gulp.{/i} Heheheh~"
    mo "Thank you, Sir..."
    mo "Maybe you can...dress me up again soon?"

    "Molly begins to clean herself off and-"
    play sound "winner.mp3"
    "{i}And you CAN “dress her up” again soon! Any night, in fact! Because she’s officially unlocked as an Invite-Character!{/i}"
    "Oh, okay. I guess my job is done here then."
    play sound "winner.mp3"
    "{i}That’s right, Akira! You’ve once more fulfilled your only purpose on this planet and ejaculated all over some helpless girl! Great job!{/i}"
    "I collapse onto the bed beside her while-"

    $ molly_lust += 1
    $ molly_love += 1

    play sound "winner.mp3"
    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "I go to reach for a towel and-"
    play sound "winner.mp3"
    "{i}Molly’s lust has increased to [molly_lust]!{/i}"
    "..."
    "..."
    "I-"
    play sound "winner.mp3"
    "{i}Upon reaching 500 headpats, Molly MacCormack will-{/i}"
    "Oh, fuck it. Goodnight."

    stop music fadeout 5.0

    play sound "winner.mp3"
    "{i}Molly leaves the room!{/i}"
    "{i}Just...not right away.{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ mollyinvite2 = True

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label beachsixmolly1:
    scene sky
    with dissolve2
    play music "asobeatsex3.mp3"

    "I journey into the woods because Molly has decided to be weird again and apparently just doesn’t want to have sex with me in a normal location. So that’s fun."
    "Why we needed to come all the way out {i}here{/i} instead of some storage shed or custodial closet, I don’t know. But it’s not as if I can really find out without first finding {i}her.{/i}"
    "So here’s hoping I’m able to do that without being mauled by some sort of wild animal or god or Chika or anything else that might track me down within this sea of trees first."
    "And also here’s hoping that when I ultimately {i}do{/i} find Molly, my mind doesn’t explode and cause me to lose all control of my body again."
    "Because I can’t imagine she’d want to have much more sex with me in the future if that’s going to be a recurring thing. And also because that’s what Nodoka’s for. "
    "I don’t need multiple girls to fill the same role. So I’ll just continue to internally label Molly as my horny roleplay sex-friend. Because everybody needs at least one of those, right?"

    scene mollylustnaming1
    with dissolve2

    "Granted, I’m not sure what type of character she’ll be playing in a place like {i}this.{/i} Nor do I imagine she’d lug an entire costume out here just to take it off."
    "But again, this is Molly we’re talking about. And seeing as she’s the type to take all of her passions to the next level, I should match that energy and take all of {i}mine{/i} out on her."
    "Especially since it will help quell the rage and sadness and fear bubbling up within me, rapidly congealing into an orb that shakes me to my very core as my life crumbles into dust."

    s "Hello? Molly?"

    scene mollylustnaming2
    with dissolve

    s "{i}Anyone?{/i}"
    mo "{i}Ahem...{/i}"
    s "And I mean {i}literally{/i} anyone because I refuse to leave this forest without sex. "
    mo "Sir-"
    s "And if I am going to engage in such a ridiculous “scavenger hunt,” I’ll be damned if I’m not handsomely rewarded for it in the form of a submissive, young girl."

    scene mollylustnaming3
    with dissolve

    mo "Sir, you have been staring directly at me for several seconds now. So I’m confused as to whether or not you don’t actually see me or if I forgot to unclick shadowmeld."
    s "Oh, there you are. Sorry, Molly. I was just voicing my feelings out loud in hopes of subconsciously informing whoever I cross paths with that I will not be taking it easy on them."

    scene mollylustnaming4
    with dissolve

    mo "Well, um...how...{i}hard{/i} do you plan on going exactly? Because most of my...{i}penetrative experience{/i} comes in the form of toys that...don’t quite measure up to your, um..."
    mo "{i}Skill level...{/i}"
    s "To be completely honest, I have had a very rough month. And I intend to make you feel every last bit of that before you exit these woods."

    scene mollylustnaming5
    with dissolve

    mo "You...you do?!"
    s "I do. And if that sounds like a problem to you, I’ll give you roughly ten seconds to run away as quickly as you can in an attempt to escape. "
    s "I {i}will{/i} catch you, though. I’ve already made my purpose here abundantly clear, I think."

    scene mollylustnaming6
    with dissolve

    mo "I...shan’t dash for safety, Sir. I am...quite happy to...fulfill such a crucial role at this point in your development. Just..."
    mo "I’m not quite sure what it’s like to be, um...sexually...power-leveled..."
    s "Power-leveled?"
    mo "It’s when an experienced player carries an {i}inexperienced{/i} player through content not designed for them in an effort to grant them an abundance of experience at once."
    s "Oh, then yeah. That’s exactly what I’m doing here. We’re going to max out your sex level or whatever. Sound good? Good. Take your swimsuit off."

    scene mollylustnaming7
    with dissolve

    mo "W...Wait! I had a whole speech planned before you showed up! "
    mo "{size=-2}It was my intention to come across as one of those NPCs you find in indie porn games that repeat the same phrase over and over as their bodies are used passionately and violently to sate the lust of a rampant hero!{/size}"
    s "Oh...Wait, what?"
    mo "It’s a real genre, Sir. A lazy one, yes. But very real! And surprisingly scintillating when done well. Which...it typically isn’t. But it {i}can{/i} be!"
    s "Right. Well, I have no problem letting you do your little speech thing, but can this be one of those games where I get to choose a name first or whatever?"

    scene mollylustnaming8
    with dissolve

    mo "Oh! Uh...yes! I apologize. I got a bit ahead of myself in the heat of my arousal."

    scene mollylustnaming9
    with dissolve

    mo "F...Fair hero! What is your name?"

    "What do I want Molly to call me during sex?..."

    jump mollysexnaming

label mollysexnaming:
    $ mollymaster = renpy.input("Enter a name for Molly to call you...")
    $ mollymaster = mollymaster.strip()

    if mollymaster.lower() in ["molly"]:
        s "Molly."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming11
        with hpunch

        mo "Wait, Sir! {i}I’m{/i} Molly! And disregarding the fact that you are attempting to commandeer my name, adopting such a title would be akin to cultural appropriation! Would it not?!"
        s "I can’t see {i}how.{/i} It’s just a name."
        mo "Aye! But if I had a child with another European and the two of us decided to name him “Akira,” would that not be weird?!"
        s "Not really. In fact, I actually think it’d be very flattering. And I’d like to congratulate you on the birth of your fictional son."

        scene mollylustnaming12
        with dissolve

        mo "But I don’t {i}want{/i} a fictional son yet! That’s epilogue material! Just choose another name!"
        s "Ugh...fine."

        jump mollysexnaming

    if mollymaster.lower() in ["rin"]:
        s "Rin."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming11
        with hpunch

        mo "R-Rin?!"
        s "But like, {i}boy{/i} Rin. Because Rin is a unisex name that I just also happen to want to be addressed by."

        scene mollylustnaming13
        with dissolve

        mo "I...{i}do{/i} suppose it is a relatively common Japanese name that...{i}would{/i} make sense to use as the name of a protagonist, but..."
        mo "Surely you understand that name bears...quite {i}significant{/i} relevance to my, um...{i}sexual proclivities,{/i} Sir."
        s "Are you trying to tell me that if you had to call me Rin during sex, you’d be thinking about {i}girl{/i} Rin and not {i}boy{/i} Rin? AKA — me?"

        scene mollylustnaming11
        with dissolve

        mo "I don’t {i}know{/i} what I’d be thinking of as this is not a branch of the narrative I have ever expected to encounter! "
        mo "What I {i}do{/i} know, however, is that I have also imagined what if would be like for {i}girl{/i} Rin to have a penis as well! Which obviously means I have envisioned that penis inside of me, Sir!"
        s "So what I’m hearing is you’re cool with it."
        mo "How is {i}that{/i} your takeaway from this?! "
        s "Well, am I wrong?"
        mo "Well...{i}no!{/i} But-"
        s "Great. Then we’re ready to begin."

        scene black
        with dissolve

        mo "Sir, wait! I’m- aah!"
        s "I’m not {i}Sir{/i} anymore..."
        s "I’m {i}Rin{/i} now..."

        jump endofmollysexnaming

    if mollymaster.lower() in ["tsuneyo"]:
        s "Tsuneyo"

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming14
        with hpunch

        mo "I’m sorry. Did you just say “Tsuneyo?”"
        s "Only because it wouldn’t be properly conveyed in narrative format if I had {i}just{/i} entered it into a text box. I don’t think you’re allowed to question my entry, though."
        mo "We’re sorry. The name you have entered is unavailable. Please choose a new one. One that does not already belong to a character in the game we are playing."
        s "Can there not be more than one Tsuneyo in this world?"
        mo "It complicates things on a programming end. Probably. "
        mo "I don’t know how to code, to be honest. But that won’t stop me from complaining about how other developers do it anyway because that is my God-given right as a gamer. "
        s "I’m confused. Are you going to call me Tsuneyo or not?"

        scene mollylustnaming15
        with dissolve

        mo "I mean...I’d {i}prefer{/i} not to. "
        mo "I just don’t want to get used to doing it in the event of all three of us having sex {i}together{/i} one day. Likely as the result of another special update or something along those lines."
        s "{i}Hah...{/i}fine. But only because I would also like for that to happen one day and I don’t want to have to fight Tsuneyo for her name. I would definitely lose."

        "Looks like I’ll have to choose something else this time..."

        jump mollysexnaming

    if mollymaster.lower() in ["haruka"]:
        s "Haruka."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming11
        with hpunch

        mo "Haruka?!"
        s "My answer was recorded in the Haruka?"
        mo "That’s not what I meant and you know it! "
        s "Either “Haruka” or...what’s that other thing you call her again? The Magistrate of Mammaries?"
        mo "That is far too many words to be spitting out in the throes of pleasure, Sir!"
        s "Great. Just “Haruka” is fine then. I don’t need the whole title. Just part of it."

        scene mollylustnaming16
        with dissolve

        mo "May I ask if the two of you coordinated this tomfoolery together? Or if this is a specific choice you are making for the sole purpose of rustling my jimmies."
        s "Okay. You be Jimmy and I’ll be Haruka. That works for me."

        scene mollylustnaming11
        with dissolve

        mo "Again! That is not what I meant and you know it!"
        s "Why are you freaking out, Jimmy? It’s just a name. It’s not like you’ll {i}actually{/i} be fucking Haruka. At least...not right {i}now.{/i} I don’t know what you guys do in your free time."
        mo "Not {i}that!{/i} Though, I’d be...lying if I said I hadn’t...{i}thought{/i} about it before."
        mo "Several...times."
        s "Awesome. I see no reason to change my choice then. "

        scene black
        with dissolve

        mo "Sir, wait! I’m- aah! Ngh! No! I’m not...ready yet!"
        s "I bet you would be for the {i}real{/i} Haruka..."

        jump endofmollysexnaming

    if mollymaster.lower() in ["sir"]:
        s "Sir."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming14
        with hpunch

        mo "Hold on a second, Sir. That is...{i}already{/i} what I call you."
        s "Yeah. And?"
        mo "And you’d...like to forego naming your own character in favor of the default option?"
        s "Yeah. I think it’s cute when you call me that. it sets you apart from the other girls and just...reminds me you’re you. "
        s "As if the distinct appearance and...the {i}rest of you{/i} didn’t already do that."

        scene mollylustnaming17
        with dissolve

        mo "Then I’d be glad to, Sir! And it makes me very happy knowing that you {i}also{/i} enjoy it when I call you that!"

        scene mollylustnaming18
        with dissolve

        mo "I always kind of worry that...you think I might be trying to be different {i}on purpose{/i} or something and that...you secretly wish I’d be more like the other girls."
        mo "So knowing that you...enjoy something {i}because{/i} I’m the only doing it is, um..."
        mo "I..."

        scene mollylustnaming19
        with dissolve

        mo "I would very much like to have sex with you now if...that’s okay."

        scene black
        with dissolve2

        s "Of course it’s okay, Molly..."
        s "You-"

        jump endofmollysexnaming

    if mollymaster.lower() in ["thunderfury, blessed blade of the windseeker"]:
        s "[mollymaster]."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming11
        with hpunch

        mo "[mollymaster]?!"
        s "That’s right. [mollymaster]."
        mo "You really want me to call you [mollymaster]? {i}The{/i} [mollymaster]?!"
        s "I’m sorry if it makes you uncomfortable calling [mollymaster]. I’ve just really always wanted to hear a cute girl call me [mollymaster]."
        mo "Thank you for calling me cute, [mollymaster]. I just don’t know [mollymaster] is...{i}appropriate{/i} for sex."

        scene mollylustnaming20
        with dissolve

        mo "You see, I’ve...I’ve always wanted to {i}hold{/i} [mollymaster]...So if {i}you’re{/i} [mollymaster]...that wish comes true. And I..."
        mo "I’m not sure if I’m ready yet...[mollymaster]. The responsibility is...too much to bear, [mollymaster]."
        s "Of course you’re ready, Molly. Just because I’m [mollymaster] doesn’t mean your feelings about [mollymaster] have to die. "
        s "In fact, I’d say this makes your feelings for [mollymaster] even stronger. "

        scene mollylustnaming21
        with dissolve

        mo "[mollymaster]..."
        s "Molly..."
        mo "Your name is so much longer than mine now, [mollymaster]...And I can feel the warrior spirit bleeding out of you as we speak."
        mo "I simply...can’t wait any longer! Take me, [mollymaster]! Right now!"

        scene black
        with dissolve2

        s "I’m sorry for making you wait so-"

        jump endofmollysexnaming

    if mollymaster.lower() in ["daddy", "papa", "father", "dad"]:
        s "[mollymaster]."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the- "

        scene mollylustnaming22
        with hpunch

        mo "Wait. You really want me to call you [mollymaster]?"
        s "Is that really surprising? That’s, like...the most common sex name possible."
        mo "Aye, Sir. But...I’m not sure if {i}I{/i} fit the bill of a girl one would normally {i}want{/i} to hear such a...{i}sexually{/i} charged name from."
        s "What do you mean?"

        scene mollylustnaming23
        with dissolve

        mo "Well...I’m {i}Molly.{/i} Weeb...otaku...whatever you want to call me. The {i}nerd.{/i} Geek. {i}Loser.{/i} You know how it is. "
        mo "[mollymaster] is, like...for girls like {i}Chika.{/i} Or Kirin. Or any of the less, um...Molly-{i}ish{/i} types. I’m just...not sure if it {i}fits.{/i} And I...wouldn’t want you to laugh...at me."
        s "I won’t laugh at you, Molly. You don’t need to be someone like Chika to say something like that. "
        s "In fact, I think that name might be even {i}more{/i} endearing from someone like you since it’s so uncharacteristic. "
        mo "Well...you’re not wrong about {i}that.{/i} I’m just not sure if this will be as...enjoyable as you desire it to be, Sir."
        s "Cut it out with the {i}Sir{/i} stuff already. Go ahead. Call me it now. See how it sounds."

        scene mollylustnaming24
        with dissolve

        mo "Mm..."
        s "Come on. Just try."
        mo "..."
        s "..."
        mo "[mollymaster]..."
        s "{i}See?{/i} Hot as fuck."

        scene mollylustnaming25
        with dissolve

        mo "R...Really?"
        s "Yeah. That was great. Now keep doing it for the rest of forever."
        mo "Forever?..."
        mo "So...you’ll be my [mollymaster] for...the rest of our lives?"
        s "..."
        mo "[mollymaster]? What are you-"

        scene black
        with dissolve

        s "I’m sorry, Molly. I can’t wait any longer."

        jump endofmollysexnaming

    else:
        s "[mollymaster]."

        play sound "computeryay.mp3"
        scene mollylustnaming10
        with dissolve2

        mo "Your entry has been recorded in the log. You will now be referred to as [mollymaster] during most sexual dialogue. "

        scene black
        with dissolve

        s "Perfect. I would like to put that to the test immediately."

        jump endofmollysexnaming

label endofmollysexnaming:
    mo "Wait! I still have to do my speech thing!"

    play sound "static.mp3"
    scene mollylustnaming26 with flash
    stop sound

    s "Oh...right. Okay. Fine. Go."
    mo "Well met, traveler. It appears that you have found yourself lost in the afterlife — where those who once traversed the plains of the living {i}now{/i} thrive, unbound by the chains of God."
    mo "{size=-3}This land is known as the Mystical Breeding Forest. And while its denizens are few in number after the events of the Red Plague, the ones who {i}still{/i} exist here are ruthless...and will not hesitate to suck you dry in every sense of the word.{/size}"
    mo "Should you manage to escape, you will find yourself in the Land of Plenty to the east...or the Dark Moors of Formalia to the West. "
    mo "But be careful — your species is rare in this world. And the wildlife here is rather {i}thirsty...{/i}"
    s "So, like...this “wildlife” you speak of-"

    scene mollylustnaming27
    with dissolve

    mo "The Land of Plenty is to the east...and the Dark Moors of Formalia are to the west."
    s "I know. You literally {i}just{/i} said-"
    mo "Be careful, Traveler. The wildlife here is rather {i}thirsty...{/i}"
    s "Ohhhh...so you’re just going to repeat those lines from here on out, aren’t you?"

    scene mollylustnaming26
    with dissolve

    mo "The Land of Plenty is to the east...and the Dark Moors of Formalia are to the west."
    mo "Be careful, Traveler. The wildlife here is rather-"

    play sound "static.mp3"
    scene mollylustnaming28 with flash
    stop sound

    mo "NGHGHGH?!?!?"
    s "Already breaking character, Molly? "
    mo "The...Landy of Plenty...is to the east! And...the Dark Moors of...Formalia...aah....to the...west!"

    "I pin her up against the tree, lifting one of her legs up and pulling her swimsuit to the side so I can penetrate her with little resistance."
    "Which isn’t to say she’d resist {i}at all{/i} since the girl she’s playing today exists only to help the hero get his bearings."
    "I’m interested in seeing how long she can keep it up, though. Molly’s much less {i}experienced{/i} than most of the other girls I’ve been with. At least with actual humans."
    "But the amount of work she’s done on {i}herself{/i} makes it rather easy to slide in and out of her, even as she struggles to accept my full length."

    mo "Be...aah...careful...traveler! The...wildlife here is...rather...thirsty!"
    s "So are the {i}helpful{/i} NPCs it seems. I didn’t expect you to get so wet so easily, Molly."
    mo "Land...of the...Plenty!~ Haaah!"

    scene mollylustnaming29
    with dissolve

    mo "Dark...Moors of...ngh...Formalia!"
    s "I wonder what it says about you that you’d stage a fantasy where you exist solely to be taken advantage of. That seems like more of a {i}Sana{/i} thing, doesn’t it?"
    mo "Ngh! Mngh! The...wildlife...aaah...mngh!"
    s "Do you want to know which one of you I chose first, Molly? "
    mo "MNGHH! MMMNGH!"
    s "Heh...no wonder you chose the woods. Easier to relinquish control when you know it’ll happen uninterrupted, isn’t it?"
    mo "Fo...Form...alia! To the...east!"
    s "I thought you said Formalia was to the {i}west?{/i} What kind of useless NPC are you?"

    scene mollylustnaming30
    with dissolve

    mo "NGAAAAAH! Forget...what I said...[mollymaster]! You...get the point! Aaah! So big!"
    s "Aww...I was having fun. Part of me wishes me {i}everyone{/i} was like that."
    mo "You have...spawned in the...wrong game, Sir! Surely there’s a...world out there where...everyone {i}is{/i} a...mindless sex toy!"
    s "Maybe...Looks like I’ll just have to settle for {i}one{/i} mindless sex toy for now, though."
    mo "But I’m...aah! Not...mindless anymore...[mollymaster]! I can...feel you...inside of me! So...deep inside of me! "
    s "And? How do you like it, Molly?"

    scene mollylustnaming31
    with dissolve

    mo "Mngh! I...{i}love{/i} it...[mollymaster]...Thank you...so much...for treating this...perverted body with...such care! "
    s "I have to be careful not to break you if I want to keep using you in the future, don’t I?"
    mo "Sometimes...I {i}wish{/i} you would just...break me, though!"
    s "Heh...you’ve said something similar before, haven’t you?"

    scene mollylustnaming32
    with dissolve

    mo "P...Probably...[mollymaster]! These...fantasies of mine...know no bounds! P...Please teach this...inexperienced body how to...properly love!"

    "I squeeze her ass with my right hand as I force more of my cock inside of her, hoping that her hair serves as some sort of barrier from scratching her back against the tree too much."
    "At the same time, though...I do feel like a slew of minor abrasions might make a nice little trophy for her to walk back to the beach with. "
    "In addition to {i}another{/i} trophy I plan on making her walk back with at least."

    s "Hey...you’re on birth control, right?"
    mo "Hah...hah! Yes...[mollymaster]! So please...feel free to...empty your stores inside of me! This body is...where you...rightfully belong!"
    s "Look me in the eyes and say it again. More {i}directly.{/i}"

    scene mollylustnaming33
    with dissolve2

    mo "Aah...aah!...Cum...inside of me...[mollymaster]..."
    s "Louder."
    mo "Cum inside of me...[mollymaster]!"
    s "Louder! {i}Lewder!{/i}"

    scene mollylustnaming32
    with dissolve

    mo "HYAAAHAHAHHH! PIERCE MY FRAGILE WOMB WITH YOUR PLEASURE-SPEAR! I’M GONNA CUM!"
    s "Can you...split the difference maybe? "
    mo "NO! AAAH! MNGH! F...FUCK! AAAAH! HAHHA! CUMMING! CUMMING! CUM WITH ME! CUM...WITH ME!"

    with sexfade
    with sexfade
    scene mollylustnaming34 with cumflash
    with hpunch

    mo "{i}Ah!.............Hah!{/i}"

    "I begin to cum inside of Molly and-"

    scene mollylustnaming35
    with hpunch

    mo "MGNNGHGHGH!! AAAH! HAAAH! SIR...MNGH! AAAH! HYAHAAAHAHAAA!!!!!!"

    "And a...particularly violent and somewhat delayed climax is pulled out of her along with the last drop of my seed."
    "She’s like a robot going haywire for a few seconds and I actually worry that she might be having a seizure."

    play sound "static.mp3"
    scene mollylustnaming36 with flash
    stop sound

    "But it ultimately subsides and she winds up spent on the ground — cum dripping out of her and mixing with the dirt below as her body becomes filthier than I have already made it."

    mo "Aaaah.......aaah......."
    mo "Was I...a good NPC...[mollymaster]?..."
    s "Spectacular, actually. Between that and watching you masturbate in my bed, I might actually be into video games now."
    mo "That’s...excellent news...[mollymaster]!"
    mo "Perhaps...now we...can find something we-"

    play sound "static.mp3"
    scene mollylustnaming37 with flash
    play sound "dosex.mp3"
    with hpunch

    mo "HNGHGHGG?!?!!?"
    s "Sorry...Molly! Not...done with you yet!"

    scene mollylustnaming38
    with dissolve

    mo "YAAAH!...HAAAH! WA...WAIT! IT’S...TOO MUCH! I CAN’T...BREATHE! HAAAH! OH MY GOD! OH MY GOD!"

    "Unwilling to give Molly {i}any{/i} recovery time at all and still sufficiently hard, I pounce on top of her and thrust myself back inside to meet the results of my prior wrongdoings."
    "The sounds are utterly {i}degenerate{/i} as her arousal combines with the product of mine, squelching in tune with the melody of me slamming against her ass."
    "She doesn’t thrust back against me, or really move much {i}at all{/i} to be honest. It’s just me treating her body like a blow-up doll as I viciously claim her pussy for a second time today."

    play sound "static.mp3"
    scene mollylustnaming39 with flash
    stop sound

    "Then a third."

    play sound "static.mp3"
    scene mollylustnaming40 with flash
    stop sound

    "Then a fourth and a fifth and a sixth until her body has been adequately {i}power-leveled{/i} and she’s cumming every five minutes. I’d like to say this a job well done."

    mo "Ah! Ah! Ah! Haaah! Aachhk! Aaah! S...aaaah! [mollymaster]! Aah! Ah! Ah! Ah! Yesh! Yeshh! Yeshh yeshhs yeshhs yeshhs yeshhhh! "
    s "Last...one...okay?!"
    mo "Aaah! HyaaaAAaAaahhh! N...nooOooOo!! Don’t...sh...shtoppppp!!! P...Pleasshhheheee.....don’t...shtththttopppp!!!!!"

    "She’s thrusting backwards with full force now — just “full force” for her at this point is basically weak, rabbit-like humps as I have drained every ounce of what little strength she has. "
    "And I’ve done the same for myself as well. I can barely even hold myself upright anymore. "
    "So the time has come to say goodbye, as I have learned that {i}all{/i} good games must eventually come to an end. "
    "But I take solace in knowing that I can replay {i}this{/i} one any time I like."
    "And with a little more practice, Molly might even be on the same level as me soon."

    s "Beg for it...again!"
    mo "C...CcCCcC...CUmmMMMmMM INSHIIDDEEEEE MEEEEEEE!!!!! F...FLLL...FILL...MEE....uUuuUuUuupppPppppPPPP!!!!!!!"
    mo "[mollymaster]!!!! AAAAHhAaAAHHH! [mollymaster]!!!!!!!!!!!!!!!"

    with sexfade
    with sexfade
    scene mollylustnaming41 with cumflash
    with hpunch

    mo "HYAHAHAAHAYAHAAYAHAHAHAAAAA!@!!~@@!!!!!@@!!!!!!~~~!!~~~"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I collapse on top of her, breathing rapidly as I inhale the residual scent of shampoo mixed with sweat and our surroundings."
    "I can barely move. So I hold her a moment, not caring that she’s still convulsing and I’m {i}still{/i} submerged inside of her. "
    "When her shaking stops, she passes out. But I stay with her until she wakes up again. And I help her back to her feet when she has trouble using her legs."
    "But that’s all I do...because my reign of terror is not over yet. Nor {i}will{/i} it be until every last drop of negativity has been expelled from my demonic phallus. "
    "That said..."
    "Who shall I conquer next?"

    $ renpy.end_replay()
    $ beachsixmolly1 = True
    $ molly_lust += 5

    jump beachsixsexmenu
