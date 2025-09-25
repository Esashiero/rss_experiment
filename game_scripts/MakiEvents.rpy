label callmakimorning:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump callmorning
    if chap4active == True and cafeclosed == False:
        jump makispringmorninggen
    if chapthreeactive == True and chap4active == False:
        jump makisummer2morninggen
    else:
        play sound "phonebeep.wav"

        "I tap on Maki's name and wait for her to answer."
        "........."
        "......"
        "..."
        "Nothing. I guess she's still sleeping."

        jump callmorning

label callmakiafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump callafternoon
    if makidate1 == False:
        play sound "phonebeep.wav"

        "I tap on Maki's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        maki "Hello?"
        s "Hey, Maki. It's your daughter's teacher. I was wondering if you were up to anything right now."
        maki "Ahh, shoot! As a matter of fact, I am."
        maki "Would you mind giving me a call later? I'll be able to talk tonight."
        s "Yeah, sure. No problem at all."
        s "Talk to you later."

        play sound "phonebeep.wav"

        "Damn. Looks like I'll have to find something else to do..."
        "Maybe there's some late-night place nearby the two of us could hang out at that isn't filled with porn?"
        "I should make sure I know a place like that before calling her again..."

        jump callafternoon
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Maki's name and wait for her to answer."
        "........."
        "......"
        "..."
        "Nothing. I guess she's busy right now."

        jump callafternoon
    if christmas7 == True:
        jump makinoongen2
    else:
        jump makigenafternoon

label callmakinight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump callnight
    if maki_love >= 0 and mollycafe1 == True and makidate1 == False:
        jump makidate1
    else:
        "Maki should be at work right now. I can probably see her if I head over to the porn shop."
        jump callnight

label pornshopmaki:
    if makiblock == True:
        "I don't really think I should visit Maki right now..."
        jump satnightmenu
    if maki_love >= 5 and makotodorm25 == True and makidate1 == True and bar30 == True and makidate5 == False:
        jump makidate5
    if maki_love >= 10 and christmas7 == True and makidate10 == False:
        jump makidate10
    if maki_love >= 15 and makiday351 == True and harukalust10 == True and makibj == True and makidate15 == False:
        jump makidate15
    if osako_love >= 20 and osakodate15 == True and osakodate20 == False:
        jump osakodate20
    if maki_love >= 25 and nodokaspecial30p4 == True and amispecial50 == True and makihornyquestintro == False:
        jump makihornyquestintro
    if maki_lust >= 5 and yasuspring3 == True and makilust5 == False:
        jump makilust5
    if maki_love >= 30 and christmasfive8 == True and osakospring6 == True and makispring1 == False:
        jump makispring1
    if miku_lust >= 5 and dormwarsfive14 == True and mikulust5 == False:
        jump mikulust5        
    if chap4active == True:
        jump makispringporngen
    if chapthreeactive == True:
        jump makisummer2porngen
    if christmas7 == True:
        jump makinightgen2
    else:
        jump makigennight

label makinoongen2:
    scene makinoongen2
    with dissolve
    play music "cafe.mp3"

    "Maki and I make plans to meet for lunch at the cafe and she manages to go a full ten minutes before making her first sex joke of the day."
    "I'm really proud of her. I don't think she's ever lasted that long before."
    "If I were Maki, I would have added a {i}that's what she said{/i} to the end of that last sentence, but I am a civilized adult with a thing they call restraint."
    "Just kidding, I make the joke anyway and her eyes light up, prompting the two of us to spiral into an endless tirade of crude humor that culminates in Haruka coming over to scold the two of us."
    "Having just gotten in trouble, we go back to being well-behaved [[boring] people and finish our respective lunches, making plans to do this again soon."

    scene black
    with dissolve

    "I find it surprising how easy it is to get along with Maki despite the uptight and diligent nature of her daughter."
    "That's not me saying I don't like Makoto or anything, I just can't stop thinking of how different the two of them are."
    "Maki feels like someone I've known for a long time, which is obviously odd given just how briefly we've known one another."
    "Either way, the two of us wind up going our separate ways."
    "Maki to her shop- and me to..."
    "Well, me to anywhere."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki's affection has increased to [maki_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label makinightgen2:
    scene makinightgen2
    with dissolve
    play music "citylife.mp3"

    "I arrive at the porn shop to find Maki groping a poster."
    "I would question this sort of behavior for anyone else but it makes complete sense for her."

    if bonus == True:
        "I'm just kind of upset that Makoto couldn't be around to see it."
        "Maki summons me over to grope the poster along with her and, within a matter of minutes, I find myself getting turned on by a large sheet of paper."
        "What sort of person am I becoming?"
    else:
        "Maki summons me over to grope the poster along with her, but I refuse because I am a good boy and my parents would not approve of such behavior."

    scene black
    with dissolve

    if bonus == True:
        "We repeat this for the next ten minutes before Maki gets bored and decides to give me a tour of the bukkake section."
        "She does not hesitate in informing me that it is one of her favorite genres and, just when I was beginning to think I couldn't see her as any more of a degenerate, she proves me wrong."
        "I've gotta admit, she really {i}is{/i} amazing in one of the most...unusual ways that you can think of someone as amazing."
        "Whatever that means."
    else:
        "Instead of participating in this immature debauchery, I say goodbye to Maki and go home to play with my toys."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki's affection has increased to [maki_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makigenafternoon:
    play sound "phonebeep.wav"

    "I tap on Maki's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    maki "Afternoon, Sensei! To what do I owe this pleasure?"

    scene black
    with dissolve

    "Maki and I make plans to meet up for coffee at Koi Cafe."
    "She still has some time before she has to open the porn shop, so this is a good opportunity for the two of us to get closer..."

    scene makiafternoongen
    with dissolve
    play music "cafe.mp3"

    "We meet up roughly half an hour later and get to chatting over lunch and coffee."
    "I expected Maki to be a little different outside of work, but I'm quickly realizing that isn't the case."
    "If anything, she might actually be even more vulgar in public."
    "Apparently, Maki wasn't always the twisted pervert she is now and was actually closer to having Makoto's demeanor back in the day."
    "She tells me a few stories of how she acted back in [high_school] and the difference is like night and day."
    "But seeing what she's become now will never cease to amaze me when compared to how closed-off and high-strung her daughter is."
    "I wonder if there's any reason for that..."

    scene black
    with dissolve

    "An hour or two passes by before the two of us decide to head out."
    "It isn't until I'm walking through the city that I realize how strange it is to feel closer to someone even when fifty-percent of your conversations end in sex jokes."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki's affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label makigennight:
    scene makinightgen
    with dissolve
    play music "citylife.mp3"

    "I decide to head over to the porn shop to see if Maki is around."
    "As it turns out, Makoto is taking the night off to relax or unwind or something along those lines, so I get a rare opportunity to be alone with her mother."

    if bonus == True:
        "The conversation quickly devolves from relatively normal to outright abrasive as she grabs a dildo off of the counter and begins to wave it around in front of me."
        "I'm not sure what her gameplan is here since I have absolutely no intention of ever purchasing an object like this, but it's mildly funny so I decide to let her do her thing."
        "I'm still shocked by how openly perverted the mother of someone like Makoto is, but I guess it takes a special kind of person to manage a porn shop..."
    else:
        "She seizes the opportunity to show me a new sculpture she purchased from a recent auction of fine art."
        "I respect the piece for its artisinal craftsmanship and applaud her for her sophisticated taste."

    scene black
    with dissolve

    "Maki goes on to recommend me a few of her favorite DVDs and, having some extra cash, I decide to buy all of them."

    if bonus == True:
        "It's great finally having someone who will actually sell me porn, let alone recommend it, so wasting an opportunity like this would be outright foolish."
    else:
        "I am glad that Napoleon Dynamite is not included in her list of recommendations."

    "I'll have to let her know how I feel about these once I finally get around to watching them..."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki's affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makiinvite:
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump inviteover
    if makiinvite1 == False:
        jump makiinvite1
    if makiinvite1 == True and makiinvite2 == False:
        jump makiinvite2
    if sadgirls8 == True and day == 7 and makiinv3 == False:
        jump makiinv3
    if sadgirls8 == True and makiblock == False and makiinv3 == False and day != 7:
        play sound "phonebeep.wav"
        "I tap on Maki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        jump inviteover
    else:
        jump makiinvitegen

label makiinvitegen:
    play sound "phonebeep.wav"

    "I tap on Maki's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    maki "Hey, Porn Guy!"
    s "I don't want to be Porn Guy. I don't like that name."
    maki "But I am Porn Woman. There needs to be a Porn {i}Guy.{/i} That's the rule."
    s "I have never heard of this rule before, but I guess it doesn't matter."
    s "Are you doing anything right now?"
    maki "Nope! Want me to come over and terrorize your [niece]?"
    s "Or just, you know, hang out with me and not get Ami involved."
    maki "Works for me! I'll head over now."
    s "Cool. Just take your time and don't get there before me again."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene makiinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    if bonus == True:
        maki "In case you're wondering, no. I did not bring the lube this time."
    else:
        maki "In case you're wondering, no. I did not bring any lotion this time."

    maki "Looks like you're going to have to choose what we do, [makimaster]."

    "How should I spend my time with Maki?"
    menu makiinvmenu:
        "Hang Out (Raise Affection)":
            jump makiinviteaff
        "Doggystyle Sex (Raise Lust)" if makisex == True and bonus == True:
            jump makidoggyanim
        "Huggystyle (Raise Lust)" if makisex == True and bonus == False:
            jump makidoggyanim
        "Headpat" if makisex == True and bonus == True:
            jump makiheadpat

label makiinviteaff:
    scene makiinvitegen
    with fade

    if bonus == True:
        "Maki and I decide to spend the night together like any two sexually confident, mature adults would- by watching porn bloopers and ranking the actors involved on a scale of one to ten."
        "As it turns out, we have surprisingly similar tastes and wind up within one or two points of each other with virtually every choice we make."
        "Of course, you can only watch porn bloopers for so long before they get exhausting- so we eventually move to watching real porn and...yeah."
        "I guess that's just the kind of relationship I have with Maki now."
        "And while it's entirely different from the one I have with Makoto (Like, literally {i}entirely{/i} different) it's definitely one that I enjoy."
        "I know plenty of openly sexual people now, but none able to remain so casual about it without blushing or nervously offering me a handjob."
        "Now, don't get me wrong- nervous handjobs are possibly the best type of handjob you can get. But there's just something about a woman being so unintimidated by sex that it's...weirdly refreshing."
        "But, then again, if you start to view Maki's outlook on all things sexual as more of a desensitization thing rather than a quirky personality trait, it's kind of sad."
        "I do hope that whatever it was that managed to get her to the point she's at today (Likely the overconsumption of pornography) didn't damage her beyond repair."
        "Thankfully, the smile on her face as we watch a tiny blonde girl get split in half by a penis nearly half of her total size forces me to realize that this is...just what makes her happy."
        "As strange as that may be..."
    else:
        "Maki and I decide to spend the night together like any two adult humans beings would- by eating Fig Newtons and watching the news."

    scene black
    with dissolve

    if bonus == True:
        "Watching so many people have sex works up an appetite for the two of us and we ultimately wind up going out to dinner at some restaurant around the corner from my house."
        "After that, we split apart and decide to call it a night."
        "And even though we did nothing but watch some of the lewdest videos I have ever seen and wash them down with pasta, I feel like I got a lot closer to Maki."
        "I've known it for a while, but she's a lot more than just...Makoto's mom."
        "Sure, her interests aren't exactly commonplace or...widely accepted or...even {i}appropriate{/i} by any stretch of the imagination-"
        "But at least she's passionate about something."
        "That's more than a lot of people can say."
        "..."
        "That's more than {i}I{/i} can say."
    else:
        "Boy, do I love Fig Newtons."

    $ maki_love += 3
    stop music fadeout 5.0

    "{i}Maki's affection has increased to [maki_love]!{/i}"

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

label makidoggyanim:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump makidoggyanimx
    else:
        $ maki_lust += 3
        stop music fadeout 5.0

        "{i}Maki's lust has increased to [maki_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makidate1:
    "Maybe I’ll give Makoto’s mother a call?"
    "Under most pretenses, I probably wouldn’t make my first call to someone I barely know just before nightfall, but she tends to work late anyway so maybe she’s used to it?"
    "Besides, Makoto is pretty much always at the shop anyway and this might give me a good opportunity to be alone with her."

    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and listen to it ring a few times, hoping she picks up."
    "........."
    "......"

    play sound "phonebeep.wav"

    maki "Hello? "
    s "Hey, Maki? This is your daughter’s teacher."
    maki "Oh, hey!"
    maki "Normally, people introduce themselves by their name and not their job over the phone."

    "Normally, people {i}know{/i} their name to begin with."

    s "Sorry about that."
    maki "No need to apologize. I just don't know what to call you."
    s "Just Sensei is fine."
    maki "Hmm...Okay, okay. But if you get to go by your job, I want to as well."
    s "You want me to call you...porn salesman?"
    maki "Beautiful porn salesman preferably, but sure."
    s "I’ll see if I can remember that."
    maki "So what’s up? Why are you calling so late?"
    maki "Did something happen with Makoto?"
    s "Nothing in particular. I just wanted to see if you’d like to meet up for coffee or something."
    maki "...Coffee?"
    s "Yeah. It’s that brown stuff tired people drink."
    maki "Sensei, are you asking a married woman out on a date right now?"
    s "..."
    maki "..."
    s "Yes."
    s "Yes, I suppose I am."
    maki "Hah! Well at least you’re up front about it."
    maki "I can probably slip away for a little while if you want to meet up at Koi Cafe."
    s "Yeah, that works for me. I’ll start heading over now."
    maki "Same here. I’ll see you soon."

    play sound "phonebeep.wav"

    "Well...She just seems full of energy."
    "I have to admit, I saw that call ending a little differently once she brought out the “married woman” line."
    "But I guess it’s not really my place to question her relationship."
    "I’ll just head over to the cafe and wait for her to get there."

    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene mollycafe1
    with dissolve
    play music "justbehappy.mp3" fadein 6.0

    mo "Welcome to Good Burger, home of the Good Burger. Can I take your order?"
    s "...What?"
    mo "It’s a thing. Don’t ask questions."
    s "Sure, Molly."
    s "Can I just get a black coffee? I’m meeting someone here in a few minutes."

    scene mollycafe18
    with dissolve

    mo "Meeting someone? Like...on a date thingy?"
    s "Uhh, I guess so."
    s "It’s just Makoto’s mom."
    mo "Makoto? Like, glasses Makoto? The Witch of the West Wind?"
    s "You gave her a nickname too?..."

    scene mollycafe1
    with dissolve

    mo "Of course! And I’ll do my best to not disrupt your date thingy!"
    mo "As a fellow degenerate, I know just how hard it can be finding love in this day and age. I’m cheering for you, Sir!"
    s "Really? I kind of saw this going a little differently."
    mo "No, no! Not at all! Go sit down in the corner! I’ll even bring over something special once she gets here."
    s "That’s really considerate of you, Molly. Thanks."

    scene makifirstdate1
    with fade

    "I take a seat near the back wall and wait for Maki to arrive. "
    "I wonder what sort of “special” thing Molly is going to bring over once the time comes?"
    "I hope it’s not anything explosive."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene makifirstdate2
    with dissolve

    if bonus == True:
        maki "Hey. Sorry it took me so long. Makoto had a question about blowjobs that I needed to answer."
    else:
        maki "Hey. Sorry it took me so long. I was continuously running into the wall in hopes that all of its atoms aligned at the perfect time, allowing me to pass through it."

    s "That’s probably the strangest intro to a date I’ve ever had the pleasure of hearing. "

    scene makifirstdate3
    with dissolve

    maki "Such is the life of the newly proclaimed “Beautiful Porn Salesman.”"
    s "Oh, right. I forgot that was your nickname now."
    maki "Don’t worry. So did I until five seconds ago."

    scene makifirstdate4
    with dissolve

    maki "Which is also right around the time that I became acutely aware that I’m still wearing my tracksuit."

    scene makifirstdate3
    with dissolve

    maki "You don’t mind, do you? "
    s "Not at all. If anything, I think it even accentuates your beauty."

    scene makifirstdate5
    with dissolve

    maki "Yeah, they {i}do{/i} look pretty nice in this, don’t they?"
    maki "Most people beat around the bush when they say that, though."

    scene makifirstdate6
    with dissolve

    maki "Heh. Bush."

    "Is Makoto really related to this woman?"

    scene makifirstdate2
    with dissolve

    maki "But anyway, thanks for calling me and blah blah blah. It’s not often I get out anymore, which I’m sure you’re able to tell by the get-up."

    scene makifirstdate7
    with dissolve

    maki "Oh how I have longed for the days to go out and enjoy my youth once again."
    maki "The life of a parent is truly a rough one."
    s "I can imagine. Makoto’s a good girl, though. At least she makes it easy on you."

    scene makifirstdate3
    with dissolve

    maki "She does now. But she was miserable as a kid. It was always “I want this. I want that. Buy me an encyclopedia.”"

    scene makifirstdate7
    with dissolve

    maki "I mean, really? What kind of five year old wants an encyclopedia for their birthday? Ask for a pony or something. Jeez."
    s "Wow. She was like that back then, too?"

    scene makifirstdate2
    with dissolve

    maki "Oh yeah. Big time. But hey, at least she’s consistent. Right?"
    maki "And she’s smarter than both her father and me now, so I can’t help but be proud of her."

    scene makifirstdate3
    with dissolve

    maki "High maintenance or not, she’ll always be my little girl."

    scene makifirstdate8
    with dissolve

    mo "..."
    maki "..."

    "Molly shows up at the table and places a normal cup of coffee in front of Maki."
    "How is this, in any way, special?"

    scene makifirstdate9
    with dissolve

    maki "That’s strange. I just felt the atmosphere in here change a little."
    maki "It feels...darker in some way."
    s "Well, that’s..."
    maki "..."
    mo "..."
    maki "Someone is giving me the death-stare, aren’t they?"
    s "Yeah. I think that might be my fault."
    mo "Clíodhna, beseech unto me a fraction of your beauty so that I may leave this harlot in the grimy waters of Glandore to {i}drown{/i}."

    scene makifirstdate10
    with dissolve

    maki "Uhh, hello there."
    s "Molly, please tell me that the coffee you brought to the table isn't poisoned."
    mo "What do you think you're doing here?"
    maki "Umm...Have I done something to offend you?"
    mo "State your name and occupation, harlot."
    maki "Maki Miyamura. Beautiful porn salesman."
    mo "And what exactly is it you intend to do with my master, {i}Maki Miyamura{/i}?"
    maki "Master?..."

    scene makifirstdate11
    with dissolve

    if bonus == True:
        maki "Isn’t she a little young?..."
        s "Not that kind of master, Maki..."

        "Though, I wouldn’t exactly complain if that were the case..."
    else:
        s "I am a ninja and I am teaching Molly how to be a ninja as well."
        maki "Wow, you're so cool."
        s "I know."

    scene makifirstdate12
    with dissolve

    maki "The two of us were just having some coffee. It’s an entirely wholesome meeting and you’re welcome to join us if you’d like."
    mo "I’m afraid I can not. Your aura is suffocating me. "

    scene makifirstdate11
    with dissolve

    maki "{i}I think this girl might like you.{/i}"
    s "I don’t think she’s into actual humans, to tell you the truth."

    scene makifirstdate13
    with dissolve

    if bonus == True:
        maki "Ahh...A hentai fan then?"

        scene makifirstdate14
        with dissolve

        mo "L-Leave my fetishes out of this, devil-woman!"
        maki "Tell me, child, what kind of hentai are you into? Vanilla? Tentacles? {i}NTR?{/i}"

        scene makifirstdate15
        with dissolve

        mo "I hate NTR! Don’t even get me started!"
        maki "Hmmm...I see, I see. So you approached this table because you’re afraid that I’m going to get to your {i}master{/i} before you. Is that it?"
    else:
        maki "Never fear. My husband also prefers other types of life forms. There is nothing wrong with it."

    scene makifirstdate16
    with dissolve

    mo "You have horrible taste in women, Sir."
    mo "This is clearly a succubus and you’ve just been lured into her trap. "
    mo "It is the only possible explanation."
    mo "But do not fear. I shall protect you."

    scene makifirstdate17
    with dissolve

    if bonus == True:
        maki "Though...I suppose I wouldn’t mind sharing him with you as long as he’s okay with it."
        s "Definitely okay with it."
        mo "Sh...Sharing...him?"

        scene makifirstdate18
        with dissolve

        maki "Of course, my dear. Real succubi like myself can thrive off the energy of both males and females alike."
        maki "Would you like me to show you how?..."

        scene makifirstdate19
        with dissolve

        mo "A threesome with Master and a succubus?..."
        mo "Perhaps...something like this would strengthen our bond?..."
        s "..."
        maki "..."

        scene makifirstdate18
        with dissolve

        mo "Will you leave us enough life essence to live our lives normally afterward? Or do you plan on taking everything?"
        maki "{i}Everything.{/i}"
        maki "But I’ll make it worth your while. I promise."
        s "Maki, it’s probably not healthy to go along with this. Molly tends to believe pretty much anything she-"
    else:
        maki "Hey, do you ever stare into the mirror for so long that it starts to look like all of your skin is detaching and floating somewhere else?"
        s "Maki, are you on drugs?"
        maki "What? Who is Maki? Where am I?"

    scene makifirstdate20
    with dissolve

    if bonus == True:
        mo "I’ll do it!"
        mo "I-I don’t know much about pleasing women...But I have played several yuri games and I’m sure I could figure it out!"
        maki "Leave the ‘pleasing’ to me, dear. You just sit back and relax..."
    else:
        maki "Are you my daughter?"
        mo "Ah!"
        s "Maki, stop. You are scaring the employees."
        maki "There is money for you in my purse."
        mo "Where...is your purse?"
        maki "Over there. Go get it."

    scene makifirstdate21
    with dissolve

    mo "AAAAHHH!"
    mo "I’LL BE RIGHT BACK!"

    scene makifirstdate22
    with dissolve

    if bonus == True:
        "Molly quickly sprints into the back room and I can hear a few things being knocked over in the process."
        "The poor girl is probably having a heart attack as we speak."
    else:
        "Molly nervously runs away and Maki refocuses her attention on me."

    scene makifirstdate23
    with fade

    s "You’re kind of terrifying."
    maki "Yeah. I kind of am."
    maki "Years and years of experience. I’m pretty good at figuring out what will set people off."

    scene makifirstdate25
    with dissolve

    if bonus == True:
        maki "I’m sure you know I don’t really plan on having a threesome with you two, though. Right?"
        s "..."

        "Damnit."

        maki "Heheh~ Sorry, Sensei. I don’t think my daughter would be very happy with me if I did that kind of stuff with one of her classmates."
        maki "Her {i}teacher{/i} on the other hand..."

        "Woah. Am I already in the clear?"
        "Was that husband thing from earlier just a bluff?"
    else:
        s "I feel like skirting the line betweeen dementia and drug addiction is enough to set most people off."
        maki "Yeah, well, I'm a free woman and I can do whatever I want."

    s "Not like it matters to me but...aren’t you married?"

    scene makifirstdate23
    with dissolve

    maki "I am. But it’s one of those “open relationship” deals. "

    if bonus == True:
        maki "I’m sure my husband is out there in space impregnating an alien-girl as we speak."
        s "Is that even possible?"
    else:
        maki "I’m sure my husband is out there in space hugging an alien-girl as we speak."
        s "Is that even possible? Have we confirmed that they have arms?"

    maki "I don’t know. But he’s a smart man. I’m sure he’ll find a way."
    maki "I hear the economy is pretty horrible in space, too. Child support will probably only be a few dollars a month."
    s "What is this conversation turning into?"

    scene makifirstdate25
    with dissolve

    maki "Hey, {i}you’re{/i} the one who brought up my marriage. I’m just trying to explain the situation to you."
    s "Does Makoto know about the situation?"

    scene makifirstdate24
    with dissolve

    maki "She...prefers not talking about things like that. "
    maki "And besides, even though it’s an open relationship, it’s not like I’m passing myself around. "

    scene makifirstdate25
    with dissolve

    maki "Believe it or not, I don’t really have many friends and-"
    s "Yeah, I believe that."

    scene makifirstdate26
    with dissolve

    maki "Wait, what? Why did you believe that so easily?"
    s "Just the vibe you give off. "
    s "It’s like a mix between shut-in, mega-deviant, and doting mother. It’s a strange combination and I can’t imagine it makes it easy to meet people or retain friendships."

    scene makifirstdate27
    with dissolve

    maki "Yup. Pretty much hit the nail on the head with that one."

    scene makifirstdate28
    with dissolve

    maki "It’s fine, though. If sexual feelings happen, they happen. I’m just not the type to go out and actively search for them with anyone."
    maki "Despite working in a porn shop, I could pretty much live without sex if I wanted to."

    scene makifirstdate25
    with dissolve

    maki "Obviously doesn’t mean I don’t enjoy it, though. "
    s "Well that’s...good news?"

    "I’m not really sure how to respond to Maki right now. "
    "This conversation is walking a fine line between serious and flirty, and it’s sort of putting me on the back foot."
    "But it’s not like I have a time limit or anything."
    "I’m sure if the two of us just keep hanging out like this, things are bound to happen eventually."
    "I just need to make sure Makoto doesn’t find out about it."

    scene makifirstdate28
    with dissolve

    maki "So, do you think the red-haired girl is doing okay?"
    maki "She’s been in the back for a while now."
    s "Molly? I’m sure she’s fine. Just a little worked up."

    scene makifirstdate25
    with dissolve

    maki "Sure you don’t want to go check on her?"
    s "There are several reasons that I don’t think that would be a good idea right now."
    s "Let’s just finish drinking our coffee and head out."
    maki "Hahah~ If that’s what you want, sure."

    scene black
    with dissolve2

    "And then, the two of us do just that."
    "We sit there like civilized adults, sipping coffee and talking about our respective outlooks and interests."
    "Maki talks much more than I do. "
    "I just relax and take in as much information as she’s willing to give me."
    "I’m sure it will come in handy eventually..."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makidate1 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate5:
    scene makiseconddate1
    with dissolve
    play music "citylife.mp3"

    "I show up at the porn shop to find Maki leaning up against the counter, admiring a large DVD display of several fully-nude women being gangbanged by a minimum of three men each."
    "It’s the first and only time I imagine I will ever see something like this, so I take a deep breath and focus on her in all of her immensely perverted beauty."

    maki "..."
    s "..."
    maki "I know you’re there, Sensei."
    s "Sorry. I was just thinking about how nice it is to see someone fully absorbed in their element."
    maki "That’s right. This is exactly where I belong."

    if bonus == True:
        maki "Surrounded by sex toys and all thirty-seven volumes of “Totally Anal.”"
        s "How do you even make that many volumes of something that sounds so simple?"
    else:
        maki "A totally legitimate DVD store."

    scene makiseconddate2
    with dissolve

    if bonus == True:
        maki "I can give you a discount if you want to find out."
        s "No, I think I’m okay. Not much of an anal person."
        maki "Neither am I but that doesn’t mean it’s not a nice surprise every once in a while."

    s "Right. Anyway, what are you up to?"
    s "No Makoto tonight?"

    scene makiseconddate3
    with dissolve

    maki "No Makoto for a little while, I’m afraid."
    s "What? Why?"
    maki "I’m not really sure, to be honest."
    maki "She’s seemed really...out of it lately."

    scene makiseconddate4
    with dissolve

    maki "You wouldn’t happen to have any idea why, would you?"
    s "Not a clue. She seemed fine the last time I saw her."
    maki "Huh...That’s really weird."
    maki "Normally I’d at least be able to tell what’s troubling her, but things are a little different this time."
    maki "Worst part is I can’t even ask her father. He was always much better at hearing her out than me."
    maki "I try my best but I normally just wind up making jokes and...she’s not the biggest fan of things like that."
    s "..."

    scene makiseconddate5
    with dissolve

    maki "Oh, am I talking too much? "
    maki "I didn’t mean to start ranting but there’s not really anyone I can go to when I need to vent, so you’re kind of just caught in the crossfire right now."
    s "What about Sara or Haruka? "
    s "I don’t mind listening but the two of them would probably be much better to vent to than me."

    scene makiseconddate6
    with dissolve

    maki "Sara...kind of sucks when it comes to talking about real-life stuff."
    maki "You guys are close so I’m sure you’ve heard about her son, right?"
    s "Yeah. Her daughter’s told me in the past that she doesn’t really like talking about it. "
    s "Still have no idea what happened, though."
    maki "Specifics don’t really matter. What {i}does{/i} matter is that she’s the same way about everything."
    maki "Just starts running away once things get real. "
    maki "And Haruka is kind of the opposite. "
    maki "She dives headfirst into problems, which is fine. But she normally spins things to be more about her and starts...relating a little too much..."

    scene makiseconddate7
    with dissolve

    maki "So, here we are. Maki Miyamura’s porn-shop-turned-counseling-corner."
    maki "Thank you for seeing me today. Am I able to sit wherever I’d like?"
    s "Yes. Please take a seat next to the lube. "

    if bonus == True:
        maki "Actually, I think I’d rather stand. The best lubricant is the kind you generate with your body."
        s "That’s fine as well. I’m on the same page as you in the lube department."
    else:
        s "I have years of experience as a guidance counselor, so I am sure I will be able to help you in some way."

    scene makiseconddate8
    with dissolve

    if bonus == True:
        maki "Thanks, by the way. "
        maki "I know I’m kind of just springing this on you out of nowhere when you want to go home and jerk off, so I really do appreciate it."
        s "It’s cool. I’m actually a guidance counselor for the[school] as well."
        maki "Oh, good. So I can blame you for my daughter not feeling well, then?"

    s "Did I say guidance counselor? I meant janitor."

    scene makiseconddate9
    with dissolve

    maki "Oh, come on. I’m kidding."
    maki "I wouldn’t actually blame you for something like that."

    scene makiseconddate8
    with dissolve

    maki "Makoto is brilliant, but she’s more stubborn than anyone else I’ve ever met."
    maki "I’m not sure where she got this weird drive to be the best from, but her father was kind of similar in [high_school]."
    s "You two started dating in [high_school]?"
    maki "Oh God, no. He was super popular and I was just some nerdy girl who sat with other nerdy girls at the nerdy girl lunch table."

    if bonus == True:
        maki "We met again in college and by that time I’d gotten pretty hot. So one thing lead to another and we actually kind of fell in love."
    else:
        maki "We met again a few years later and by that time I’d gotten pretty hot. So one thing lead to another and we actually kind of fell in love."

    scene makiseconddate10
    with dissolve

    maki "Or something like that, at least."
    maki "A lot of people seem to have a problem with us seeing other people, but neither of us really felt the same way."
    maki "My husband’s always been a bit of a player. And I was just happy that people started to think I was pretty somewhere along in life."

    scene makiseconddate11
    with dissolve

    maki "Also, I’m sure you’ve realized this by now, but I’m kind of a pervert."
    s "You? A pervert? {i}No...{/i}"
    s "Didn’t you say you could live without sex when we hung out at the cafe, though?"
    maki "Yup. And I still stand by that. "

    if bonus == True:
        maki "But it’s fun and it feels good, so why abstain when I’ve got a choice not to?"
        s "Agreed. Though, I doubt I’d be able to live as long as you without sex."
        s "I think I’ve become pretty dependent on it, to be honest."
        maki "Well as long as you’re not screwing my daughter, you’re free to do whatever you want."

        "About that..."

        s "Not even with your supervision?"

        scene makiseconddate12
        with dissolve

        maki "Hmm...interesting proposition."
        s "Is that really all it took for you to cave?"
        maki "Well I’d feel much more comfortable as long as I knew she was being treated well."
        maki "And I have to admit that it would be rather cute to see that diligent facade of hers crumble under intense pleasure."
        maki "And of course I’m sure you know I’m also joking right now and that I will happily be the outlet to absorb your sexual frustrations if the need arises."

        scene makiseconddate13
        with dissolve

        maki "Besides, I’m just the mature version of her anyway. "
        maki "You see petite girls for eight hours a day pretty much every day. I’m sure you’d welcome the thought of someone closer to your age and size."
        s "You seem extremely cocky all of a sudden, Maki."
        maki "Heh. Cock."
    else:
        s "As do I. I think sex becomes a sort of crutch for a lot of people when, in all actuality, it's nothing but a grossly personal act that does nothing but consume short bursts of time that could be better spent on furthering one's education."
        maki "You sound just like my daughter."

    scene makiseconddate14
    with dissolve

    maki "On a serious note, though..."
    maki "Please do let me know if you hear anything from Makoto."
    maki "I try to hide it around her, but I really do care about her."
    maki "And if there’s anything in this world that’s troubling her, I will do absolutely anything to make it stop."

    "My mind travels back to a conversation I’ve had with Makoto in her dorm recently."
    "I remember her saying something about how her mom has never really been the...{i}mom{/i} type, exactly."
    "Couldn’t all of that be remedied by Maki just...not intentionally hiding the way she feels about her daughter?"
    "Why is it so hard for some people to realize that all they need to do is be themselves?"

    s "Have you tried talking to her?"

    scene makiseconddate15
    with dissolve

    maki "You mean like...with words?"
    s "..."
    maki "..."
    s "Yes?"

    scene makiseconddate16
    with dissolve

    maki "Didn’t I already tell you she has a hard time talking to me?"
    maki "She’s a daddy’s girl. All she’s ever known her whole life is crumbling in the arms of a strong male figure. "
    maki "She can’t crumble in my arms because my boobs are too big and they’ll hurt her neck when she tries to squeeze me."
    s "Maybe just try a little harder then?"
    s "There are only a handful of reasons I can imagine Makoto keeping her troubles away from you."

    scene makiseconddate17
    with dissolve

    maki "Really? What are they?"

    "I guess I’ll lead in with the one Makoto has openly admitted to me in the past."
    "It’s not my place to fix her problems, so at least getting her mom to understand how to force them out into the open might benefit her in some way."
    "If something is really wrong with Makoto, Maki is surely able to do more for her than I can as some guy she’s only known for a few months."

    s "Well, the first reason is that she might want you to act a little more like a mom than a...Maki."
    maki "But I’m more experienced at being a Maki than I am at being a mom."
    maki "I’ve been a Maki for my entire life."
    s "Maybe try to be a Makoto instead?"
    maki "Be a Makoto..."
    maki "Hmm..."

    scene makiseconddate18
    with dissolve

    maki "The square root of 16 is 4."
    maki "I pretend to hate porn and I’m secretly self-conscious about my breasts."
    maki "I slept in the same bed as my parents up until I was nine years old."
    s "If you’re going to just keep revealing her secrets to me, I feel a little strange about listening."
    s "Please text them all to me instead so I can memorize them and use them as weapons against her."
    s "The part about the square root was pretty spot on, though."

    scene makiseconddate8
    with dissolve

    maki "Thanks. I have years of practice."
    maki "So, what’s the next reason? You said you had a few."
    s "The next would be something like..."
    s "Maybe she feels a little self-conscious around you?"

    scene makiseconddate5
    with dissolve

    maki "Around me? Why would she feel that way?"
    s "Well, you said it yourself, didn’t you?"
    s "You’re a more mature version of her with more experience and...chest-size."
    s "And by mature I mean only in age. If we’re going by personality, Makoto is much more mature than you are."

    scene makiseconddate19
    with dissolve

    maki "Hey! I take offense to that!"
    maki "I’m an adult! I do adult things like pay the water bill and check the mail!"
    s "You don’t need to be an adult to check the mail."
    maki "You do in my house!"
    maki "It would be really bad if Makoto checked the mail one day and found a sex toy I ordered or something!"
    s "She literally sells sex toys every single day."

    scene makiseconddate4
    with dissolve

    maki "Do you really think that could be an actual issue?"
    maki "If my own daughter was...intimidated by me, I’d feel like a complete failure."
    maki "All I want is for her to be happy and if she can’t even feel happy about {i}herself{/i} around me then I must have royally screwed up somewhere..."
    s "I’m not saying that’s what’s happening. It’s just a possibility."
    maki "I hope that’s not it..."
    maki "Is there anything else you think it could be?"
    s "There is one more thing- and it’s something most girls her age need to just toughen up and deal with."
    maki "And what’s that?"
    s "Well, basically what I just said."
    s "She needs to toughen up and deal with whatever is going on personally."
    s "Everyone goes through rough patches in life and Makoto is probably just going through something like that."
    s "She misses her dad. Maybe it’s just...father-withdrawal or something."

    scene makiseconddate17
    with dissolve

    maki "So..."
    maki "You’re saying to just wait it out and let her get over it?"
    s "Yeah. Pretty much."
    maki "..."
    s "..."
    maki "Aren’t you supposed to be a guidance counselor?"
    maki "That’s horrible advice."
    s "What?"
    maki "I know I haven’t been the most...motherly figure I could be, but no one in their right mind would ever just abandon their daughter and let them deal with hardships on her own."
    maki "If something is wrong, it’s a mom’s job to help her fix it."

    scene makiseconddate2
    with dissolve

    maki "Which is why I’ll probably sit down with her soon and figure out if there’s something the two of us can do as mother and daughter."
    maki "In a roundabout way, the horrible portion of your advice actually helped me figure something out!"
    maki "Was that your goal all along?"

    "..."
    "I actually thought that advice was pretty good."

    s "Yup. You got me."
    s "Talk to Makoto and let me know how it goes."
    maki "Will do!"
    maki "It’s time for Maki Miyamura’s Mom-Mode Mission!"
    maki "Like that alliteration, Sensei?"
    maki "I learned what that word means from my daughter. She’s so smart, isn’t she?"
    s "..."
    s "Yes, Maki. "
    s "She’s brilliant."

    scene black
    with dissolve2

    if bonus == True:
        "The conversation gradually drifts back into normal territory and, before long, Maki and I are conversing about sex positions and famous porn-stars."
    else:
        "The conversation gradually drifts back into normal territory and, before long, Maki and I are conversing about how exactly soda manufacturers get the soda into cans."

    "It’s slightly odd counting those two things as “Normal territory” but, with a girl like her, there isn’t much {i}abnormal{/i} territory."
    "I do hope she’s able to coax Makoto out of her shell soon, though."
    "I haven’t exactly noticed her acting any differently other than the walk back to her dorm after we went up to the roof, but..."
    "That just seemed entirely random."
    "Maybe it would be worth asking her about it myself?"

    $ renpy.end_replay()
    $ makidate5 = True
    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate10:
    scene makifirstbj1
    with fade
    play music "citylife.mp3"

    "I stop by the porn shop to see if Maki is working and, luckily enough, it seems that Makoto has the night off."

    if bonus == True:
        "Either that or she’s in the back room unloading vibrators or something."
    else:
        "Either that or Makoto doesn't actually exist and is just someone I made up in my head."

    "Regardless, it looks like I’m going to get to spend some time with the older Miyamura tonight as long as the younger one doesn’t show up and ruin everything out of nowhere."

    if bonus == False:
        maki "Yo! Mind if I shoot a bunch of euphemisms at you really quick?"
        s "Yes, actually. I do mind."
        maki "Damn."
    else:
        maki "Yo! Long penis, no see."
        s "I think you mean “Long time, no see.”"
        maki "I said what I said."
        maki "How’s it hanging?"
        s "Is that another penis joke?"
        maki "Is that a {i}hard{/i} concept to grasp?"
        s "Okay, Maki. That one was bad. “Hard” is extremely vague and doesn’t always refer to a penis."
        maki "I know that, but it’s not like you have to be a dick about it."
        s "..."
        maki "..."
        maki "Come on. That one was good."
        s "Better than the others, at least."

        scene makifirstbj2
        with dissolve

        maki "So, what brings you in tonight, Sensei?"
        maki "Gangbang stuff? Teen stuff? Maybe this gigantic dildo behind me that I have to sell at a discount because the box was damaged?"
        s "What in the world would I do with that thing?"
        maki "Hey, I don’t know what you’re into. Even my husband got curious about-"
        s "I don’t want to hear wherever this is headed."
        maki "Suit yourself. It’s actually a really funny story."
        s "I’m sure it’s funny for you but I’m pretty sure I’d leave the conversation traumatized."

    scene makifirstbj3
    with dissolve

    maki "Really, though. Why are you here? What do you want?"
    s "...Are you trying to get rid of me or something?"
    maki "No, of course not. You just came straight up to me instead of browsing, so you’re probably not here to buy anything."
    maki "Makoto’s not working tonight. If you’re looking for her, I’m pretty sure she’s back in her dorm."
    s "Am I not allowed to come here to see you instead?"
    maki "I mean, you are."

    if bonus == True:
        maki "In fact, that would make me a little more comfortable than you continuously coming to a porn shop to hang out with my daughter."
    else:
        maki "I enjoy your company and think you're a really nice guy with only the best intentions for both myself and my daughter, a person who actually exists."

    s "Exactly. So why don’t the two of us do something tonight?"

    scene makifirstbj4
    with dissolve

    maki "Sure. We’re a little dead once Christmas season is over anyway. Everyone’s still playing with their new toys."

    if bonus == True:
        maki "Except Makoto, of course. Darn girl had the audacity to return the present I got her while I wasn’t paying attention."
        s "You...actually bought her a sex toy? I thought you were just joking when you said you were going to do that."
        maki "I don’t see an issue with that sort of gift."

        "Of course {i}you{/i} don't."

        maki "I didn’t get my first toy until I was out of [high_school]. Do you have any idea how much pent up stress I had by then?"
        maki "Do you know {i}anyone{/i} more stressed than Makoto? If there’s anyone that has a use for a vibrator, it’s her."
        s "I can’t tell if you’re a horrible mother or a great one."
        maki "That’s fine. Neither can my daughter."
    else:
        s "I got a train set."
        maki "Aww, that's cute. I'd buy one of those for Makoto, but she was on the naughty list this year."
        s "That just means you're a bad mom."
        maki "Maybe."

    maki "I like to think I’m pretty good, though."
    maki "Like, that whole thing with Makoto getting all weird recently just sort of boiled over after a little while and all I did was talk to her."
    maki "I’m sure you had something to do with it as well, but I’m going to go ahead and take most of the blame since it will make me feel better about myself."
    s "Sure, Maki. Go ahead and-"
    s "Wait, you remember Makoto acting weird?"

    scene makifirstbj5
    with dissolve

    maki "Why wouldn’t I remember that? It’s one of the last big conversations we had."
    maki "I opened up to you about not knowing what to do and you provided some bad advice that made me realize what I {i}actually{/i} had to do."
    s "Yeah, I remember. It’s just Makoto had no idea what I was talking about when I brought it up to her."
    maki "Huh..."
    maki "Now that you mention it, she seemed confused when I said something about it the other day as well."
    maki "Maybe she’s just shrugging it off because she knows we were worried about her?"
    maki "That seems like a pretty Makoto thing to do, right?"
    s "..."

    "There’s definitely something fishy going on, but I can’t tell how much of that is due to the weird reset rules and how much of it is coming from Makoto directly."
    "But if Maki can remember something that Makoto can’t..."

    s "I’m so confused..."

    scene makifirstbj6
    with dissolve

    maki "Yeah, me too."
    maki "But as long as she isn’t acting out or anything like that, all we can really do is keep checking in on her, right?"

    if bonus == True:
        maki "I swear, this whole thing could be solved so easily if her stupid father would stop banging space girls and just come home already."
    else:
        maki "I swear, this whole thing could be solved so easily if her stupid father would stop hugging space girls and just come home already."

    scene makifirstbj7
    with dissolve

    maki "Good thing she’s got you to step in and provide that much-needed dominant male authority she’s always been into."
    s "I think your overexposure to porn has caused that sentence to sound a little different to me than it should have."

    if bonus == True:
        maki "I’m sure adding “dominant” helped with that."
        maki "You thinking about dominating my daughter now, Sensei?"
        s "That’s a loaded question and I am not answering it."
        maki "Good call. I almost caught you."
        s "You won’t trick me that easily."

    scene makifirstbj8
    with dissolve

    maki "Really, though. Thanks for your help with the Makoto situation."
    maki "Without her father being around, it’s a little overwhelming having to step in and just handle everything alone- even if she’s way more independent than she has any right to be."
    s "Don’t worry about it. I’m just doing my job."
    s "I care about Makoto, too. It’s not like I {i}want{/i} her to be sad or anything like that."
    maki "I know. But you still went out of your way to help her. And for that, I owe you one."

    scene makifirstbj9
    with dissolve

    maki "So!"
    s "So what? What’s happening?"
    maki "As special repayment for your assistance in recent matters regarding my Makoto, I will add an additional 20%% to your existing store discount."
    s "Oh."

    scene makifirstbj10
    with dissolve

    maki "Oh what? That seems like a pretty good deal, doesn’t it? That’s almost 50%% off total."
    s "Yeah, it sounds good. I just figured your daughter’s well-being was worth a little more than a 20%% store discount."

    scene makifirstbj11
    with dissolve

    maki "What happened to “don’t worry about it?!” You were so fine with doing this for free a minute ago!"
    s "That was until you insulted me with that 20%% thing."
    maki "Well then what do you want instead? What’s your price?!"

    "Hmm..."
    "Something with equal value to Makoto's well being..."
    "What should I ask for?"

    menu makiblowmenu:
        "A blowjob" if bonus == True:
            jump makibjx
        "A hug" if bonus == False:
            s "One hug, please."
            maki "Like a normal hug or a bro hug?"
            s "Do you consider yourself my bro?"
            maki "Sure. I think it's safe to say we've got a bit of a bromance going on."
            s "I have always wanted a bro. The one I got was kind of a dick."
            maki "Well I am here for you now. Come on, bro. Bring it in."

            scene black
            with dissolve

            "Maki and I have a quick bro hug in which our minds connect and are filled with cool, manly stuff like football and guns. People who like those things are masculine and we are just like them."

            s "Anyway, it's past my bedtime and I have to go home now."
            maki "Aw, shucks. Okay."
            maki "Thanks for dropping by, though."
            s "Thank {i}you{/i} for the hug."

            $ renpy.end_replay()
            $ maki_love += 1
            $ makidate10 = True
            $ makibj = True
            stop music fadeout 5.0

            "{i}Maki’s affection has increased to [maki_love]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        "Your daughter’s hand in marriage":
            s "I’ve thought long and hard about this, but-"
            s "There’s only one thing that would truly be worth Makoto’s well being to me."

            scene makifirstbj13
            with dissolve

            if bonus == True:
                maki "Wait a minute...you’re not about to ask me if you can fuck my daughter, are you?"
            else:
                maki "Wait a minute...you’re not about to ask me if you can hug my daughter, are you?"

            s "What? No."

            "Probably because I already have."
            "Sorry, Maki."

            s "I’m asking for her hand in marriage."

            scene makifirstbj14
            with dissolve

            maki "That’s even worse!"
            s "Okay, I’ve decided that you really are a horrible mother."

            if bonus == True:
                maki "Well, yeah! It’s one thing to just pull her aside for a quickie, but you’re asking if it’s okay to...pull her into your heart for a bunch of quickies in the future!"
                s "Okay, well it definitely sounds worse when you put it that way."

            scene makifirstbj15
            with dissolve

            maki "I’m not going to let you marry my daughter...especially while her father is still away."
            maki "Just take your discount and call it a day."
            s "Ugh...fine. Whatever."
            s "I’m not inviting you to the wedding once it happens, though."
            maki "Yeah, yeah. Fine."
            maki "Are we even now, then?"
            s "...Yeah. I guess so."

        "An “upgrade” for the store":
            s "Actually, Maki. There’s something I’ve been thinking this store is lacking as of late."

            scene makifirstbj12
            with dissolve

            maki "Lacking?"
            maki "What are you thinking of exactly?"
            s "Well, you see, this is a porn shop."
            maki "That’s right."
            s "And you know what all good porn shops should have?"
            maki "..."
            maki "Porn?"

            if bonus == True:
                s "I think you should install a glory hole."
                maki "A glory hole? Is that even legal?"
                s "I have no idea."
                maki "I’m pretty sure it’s not."
                s "Well, look at it this way. People have had sex in the store before, right?"
                maki "Obviously. What else do you think the back room is for?"
                s "Just build a box or something then. All you need to do after that is cut a hole in it and call it a day."
                maki "..."
                s "..."
                maki "So, my daughter’s well being {i}isn’t{/i} worth a 20%% discount, but...it’s worth a...glory hole?"
                s "I said what I said."
                maki "I mean...I guess I can...look into it?"
                maki "That’s not something I can just build on my own and it might be hard finding a contractor who has made that sort of thing before."
                maki "But your suggestion has been duly noted."
                maki "Are we even now?"
                s "Yes. We’re even now."
            else:
                s "One of those cool arcade machines with like a million games programmed into it."
                maki "Oooooooh, that would be cool."
                maki "Can you chip in, though? I might be a business owner, but I'm not exactly well off or anything."
                s "No. You have to buy it with your own money or I won't be shopping here anymore."
                maki "Okay, fine. I'll see what I can do."

    scene makifirstbj16
    with dissolve

    maki "Well, then..."
    maki "With that out of the way, I guess it’s about time that I start actually doing some work."

    if bonus == True:
        maki "I need to take inventory tonight and find out what to do with the {i}rest{/i} of the boxless dildos that came in."
        s "There are {i}more{/i} of them?"
    else:
        maki "I need to take inventory tonight and find out what to do with all of the extra copies of Napoleon Dynamite that came in."
        s "Dear god no."

    maki "It’s like a war zone, man. A god...damn war zone."

    scene black
    with dissolve2

    "Maki and I only talk for a short while longer before I take the hint and start heading home."
    "On the way back, I begin to think about what would have happened if I’d asked her for something else."
    "I mean, I liked what I chose a lot-"
    "But I can’t help but feel like I missed an opportunity."

    s "..."

    "Oh well, I guess."
    "It is what it is."
    "I’ll just figure out what to do with the rest of my spare time once I get home."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makidate10 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makibjanim:
        scene black
        with dissolve
        play music "citylife.mp3" fadein 3.0

        if bonus == True:
            "I show up at the porn shop to hang out with Maki and, within a matter of minutes, we get to talking about- you guessed it...porn."
            "She goes on to tell me stories about how awkward it was for her when she started watching things like that."
            "I, of course, struggle to believe this since she is the single most perverted person I have ever encountered."
            "But it's still interesting to think of her long before she turned into the monster she is today."
            "Eventually, we get bored of just talking and she grabs a random DVD for us to go watch in the back room."
            "We get bored of that shortly after as well..."
        else:
            "I show up at Maki's store, immediately hug her, and then leave."
            "She is very impressed by how bold I am"

        if bonus == True:
            jump makibjanimx
        else:

            $ maki_lust += 1
            stop music fadeout 4.0

            "{i}Maki's lust has increased to [maki_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label makiday351:
    scene makimalldate1
    with dissolve
    play music "mall.mp3"

    s "So...what exactly was it you wanted to talk to me about?"

    "Maki and I walk silently through the halls of the mall for a short while and I can’t help but notice her looking a little distracted."
    "I don’t know if that’s just her tell for wanting me to buy her something but, if it is, she is in for a very rude awakening."

    if bonus == True:
        maki "Nothing in particular. I just figured you’d rather be spending time with someone who’s actually your age than following around a bunch of [teens]."
        s "..."

        scene makimalldate2
        with dissolve

        maki "It’s one thing to fill up on[teen]porn but, as a former [teenager] myself, I can confirm that almost all of them are confusing and irritating and-"
        s "Exhausting."
        maki "Yes. That as well."

        scene makimalldate3
        with dissolve

        s "Are you sure it’s okay to be saying that when you have a [teenage]daughter, though?"
        maki "Are you afraid she’ll jump out from behind a mannequin and call me a bad mother or something?"
        s "Well it’s not like you two really have the best relationship to begin with, right?"
    else:
        maki "Nothing in particular. I just confused you for someone else and, by the time I realized who you were, it was too late to back down."
        s "Oh."
        s "Anyway, how are you and Makoto?"

    scene makimalldate4
    with dissolve

    maki "Makoto and me? I think our relationship is great."
    maki "It’s true that I have a hard time deciding how to tackle certain things, but as long as I have you as my stand-in husband until mine stops fucking aliens, I think everything will turn out just fine."
    s "Woah there. I never agreed to this whole “stand-in husband” thing."

    scene makimalldate5
    with dissolve

    maki "Not five minutes into our marriage and you’re already asking for a divorce? "
    maki "Is it because you have to go to space? Because I’m already used to that and don’t mind at all."

    if bonus == True:
        maki "Enjoy your alien sex."
        s "Every day, your existence somehow manages to make me even more impressed by the head your daughter has on her shoulders."
        maki "Well as long as it’s up there and not pressed between someone’s knees, I’m totally happy."
        s "I would like to take this opportunity to reiterate my previous statement."
    else:
        s "I thoroughly enjoy it when you make jokes about your husband disappearing and abandoning your family to hug aliens."

    scene makimalldate6
    with dissolve

    maki "Jokes aside, I’m glad that Makoto seems to be going back to her old self as of late."
    maki "Actually, strike that. She seems truly happy for the first time since her father left as of late."
    s "Really? Because she kind of suffered a crushing defeat during her dorm wars contest thing and I thought it might get to her."

    scene makimalldate7
    with dissolve

    maki "Did you talk to her about it?"
    s "I didn’t see any reason to. That’s not something I should really get involved in."
    maki "Well {i}I{/i} did, so ha."
    s "Wow. Look at you being a real mom."
    maki "I’ll have you know there’s not any minute of any day that I’m not a mom before anything else."
    maki "It’s just a little difficult when your child imprints on your significant other instead of you."

    scene makimalldate8
    with dissolve

    maki "But I digress."
    maki "Makoto’s knowledge test thing crashing and burning may have even been good for her in a way."
    maki "I don’t want to call it a wake up call or a...rude awakening or...any other phrase that involves waking up-"
    maki "But it’s kind of good to get the shit kicked out of you every once in a while."
    s "Are you asking me to mug your daughter?"
    maki "You’ll have to go through me first, Sensei."

    if bonus == True:
        s "That doesn’t sound very hard."
        maki "We’d probably get turned on while wrestling and wind up taking each other’s clothes off."
        s "You know, maybe I {i}will{/i} mug your daughter after all."
    else:
        s "I will destroy you, Maki Miyamura. I know at least three cool karate moves."
        s "Hi-ya."

        "I show her one of my cool karate moves. She is very impressed."

    scene makimalldate9
    with dissolve

    maki "Ahh, the things we do for love."
    s "Please don’t love me. There is not a single person we know who would approve of this relationship."
    maki "Miku might."
    s "Miku is on Team Makoto now."
    maki "As in she’s rooting for you to fall in love with my daughter?"
    s "It appears that way."

    if bonus == True:
        maki "It appears that a spanking may be in order then."
        s "For me or for Miku?"
        s "I don’t really want to be spanked."
        maki "That’s what my actual husband thought at first."
        s "Be careful. Anything you say right now may one day be used against Makoto to embarrass her in front of class."
    else:
        maki "I am not too worried about that. Makoto was born with a tragic disease that causes her to immediately explode if she ever falls in love."
        s "As her teacher, this is something I should have been informed about. "
        maki "I didn't want to embarrass her."
        s "It may be too late for that. I am going to tell everyone so they can properly prepare themselves in the event of her demise."

    scene makimalldate10
    with dissolve

    if bonus == True:
        maki "Oh please. She’s such a daddy’s girl that she could have walked in on me spanking him and still pinned the whole thing on me just...being too dominant."
        maki "But to everyone's surprise, I'm actually an innocent and pure sub at heart."
        s "Yeah, I don’t believe that for one second."
        maki "..."
        s "..."
    else:
        maki "Have you ever touched a deer? They are very soft."
        s "Are they? I had no idea."
        maki "My mom gave birth to one shortly after me. It was on the news and everything."
        s "I do not believe this."

    scene makimalldate11
    with dissolve

    maki "Okay, fine. I was lying. "

    if bonus == True:
        maki "But in my defense, being dominant is basically where all of my experience is. "
        maki "I haven’t really gotten many chances to play out any of my submissive fantasies because of my husband’s love for spanking and petplay."
        s "Having someone like you as a pet does sound like it would have its perks."
    else:
        maki "Or was I?"
        s "So...was he like, just a regular member of the family after that? I don't understand the lineage her."

    maki "Oh, no. He was the pet."
    maki "We had a leash and everything."
    s "..."
    maki "..."

    scene makimalldate12
    with dissolve

    s "Anyway."

    if bonus == True:
        maki "I’m sorry, Makoto. It looks like your classmates may soon find out that your father had a very different side than the one you grew up with."
    else:
        s "I don't think I want to talk to you anymore."

    scene black
    with dissolve2

    "Maki and I do a lap or two around the mall and manage to avoid contact with the group of girls I split up with earlier."
    "I’m not sure if the three of them have already gone home, but it’s starting to get dark and Maki is showing no signs of ending our gathering just yet."
    "I pull out my phone to text Ami about missing dinner but realize that she’s likely still with Ayane anyway-"

    if bonus == True:
        "So it looks like I’ll be able to dodge all suspicion entirely tonight and get to continue hanging out with a MILF."
        "Nice."
    else:
        "Darn it. This means I have to keep hanging out with Maki."

    scene makimalldate13
    with dissolve

    maki "Hey...can I ask you something?"
    s "You’re just going to ask anyway, aren’t you?"
    maki "Yeah. You said something that kind of made me upset earlier and I wanted to bring it up again before I hate myself for letting it go."
    maki "You don’t actually think I’m a bad mother, do you?"
    maki "Because I’ve exhausted pretty much every resource available for Makoto. She’s just too annoyingly smart to really {i}need{/i} someone like me."
    s "I didn’t really mean that. I was just using your words against you, really."
    maki "I don’t remember ever calling myself a bad mother. That hurt."
    s "No. But you said that you might try to approach things more like a friend at times. "
    s "And there’s also the issue of your...complicated relationship dynamic with your husband."

    if bonus == True:
        maki "Spanking your husband makes you a bad mom?"
        s "What? No. The whole open relationship thing."

    maki "What does that have to do with Makoto?"
    s "Well...can you really say her environment was “normal” growing up?"

    scene makimalldate14
    with dissolve

    maki "I can, actually."
    maki "Do you think we let her run around the store and use vibrators as rattles? Let her watch gangbang videos in the backroom while we kept an eye on the front?"
    maki "Do you think she was present for all of the times her father insisted on bringing a new girl home?"
    maki "Or do you think I, as a competent but slightly confused mother, would have kept my little girl away from that as best as I could?"
    s "I think that Makoto is perceptive enough to figure things out even when they’re not right in front of her."
    s "And I think that she’s the type of person to measure her circumstances against those of others to try and figure out what “normalcy” is."
    maki "So I’m a bad mother because my daughter is a genius?"
    s "I already told you I didn’t mean that."
    maki "Well then apologize. "
    s "..."
    maki "..."

    scene makimalldate15
    with dissolve

    maki "Hey. If you’re going to be my stand-in husband, you’re going to have to realize when you’re in the wrong."
    s "I never agreed to-"
    maki "You don’t have to. Makoto’s already chosen you as her stand-in daddy, so now it’s all on you to live up to it."
    s "..."
    maki "..."

    if bonus == True:
        s "Can you call me daddy again please?"
        maki "Daddy."
        s "A little softer this time."

        scene makimalldate16
        with dissolve

        maki "{i}Daddy...{/i}"
        s "Now do it like you’re about to cum."

        scene makimalldate17
        with dissolve

        maki "Ahh! Daddy! Yes! Yes!"
        s "Wow."

        scene makimalldate18
        with dissolve

    maki "Teehee~"

    if bonus == True:
        s "There are a bunch of people looking this way now."
        maki "Of course there are. I just came on a bench in a mall."
        s "Did you actually-"

        scene makimalldate19
        with dissolve

        maki "God, no. If it were that easy, I’d literally never leave home. "
        s "Well it was very convincing and I hope for your husband’s sake that he never fell victim to your deceit."
        maki "If he knew the amount of times he’d been deceived, I really {i}would{/i} need a new husband."
        s "I’ll be sure to keep it a secret if he ever returns from the alien orgy."

        scene makimalldate20
        with dissolve

        maki "{i}If{/i}, huh?..."
        s "Oh. I didn’t mean it like-"
        maki "No, no. I get it. I just don’t like hearing it out loud."
        maki "The truth is that...and don’t tell Makoto I said this-"
        maki "But...I don’t really want to wind up waiting forever."
        maki "I miss my husband. I really do."
        maki "But there’s a point where you have to sort of just accept that things might not turn out how you wanted them to turn out."
        maki "It’s painful not hearing from someone for years. Especially someone you spent so many years {i}with{/i}."
        maki "But I can’t do everything on my own."

        scene makimalldate21
        with dissolve

        maki "I’m not like Sara or Haruka. I’m willing to accept my shortcomings and don’t want them to weigh me down."
        maki "I’ve got a genius daughter to take care of. And, like you said earlier, she’s perceptive enough to realize things I don’t want her to."
        maki "The second I start killing myself by working even harder is the second she starts killing herself as well."
        s "Well-"
        s "And this isn’t me agreeing to be Makoto’s new father-"
        s "But I’ll wind up supporting you in whatever you decide to do."
    else:
        s "Makoto is my student and I have no intention of making any adjustments to our relationship at any point."

    scene makimalldate22
    with dissolve

    maki "Oh my God. Did you just agree to become Makoto’s new father?"
    s "Maki, I specifically stated-"

    scene makimalldate23
    with dissolve

    if bonus == True:
        maki "Makoto’s going to be so happy that she won’t even mind hearing me yell “Daddy” over and over from the back room all night!"
        s "No, I very much think she would mind that."
    else:
        maki "Makoto is going to be so happy."
        s "Maki no."

    scene makimalldate24
    with dissolve

    maki "Thank you, Sensei."
    maki "Not for the father thing, but for the support. "
    maki "You’ve done so much for Makoto and me in such a short time that I can’t help but feel like we owe a lot of ourselves to you."

    if bonus == True:
        s "Is that-"

        maki "For once, I don’t mean that sexually."

        "Damn it."

    maki "I mean that, in some way or another, you just being you is enough to keep Makoto afloat."
    maki "And Makoto being afloat means that I get to be afloat."
    maki "And before we know it, we’re all on the same raft together."

    if bonus == True:
        maki "Floating past nudist colonies and shielding that pure girl’s eyes from the things you and I as perverts see in our dreams."

        "I’m glad that Makoto is also smart enough to not reveal to her mother that she’s in an ongoing illicit relationship with her teacher."
        "I figure that must be difficult to do, but so many of my students are missing parents that it’s honestly hard to say."

    scene makimalldate25
    with dissolve

    maki "I’m not suggesting anything here, but..."
    maki "Even if my husband does wind up coming back, I hope you’ll stick around."
    maki "If not for me, then for Makoto."
    maki "She really needs you."
    s "..."
    s "I’ll see what I can do."

    scene black
    with dissolve2

    "Of course I have no intention of just skipping town and abandoning the Miyamuras...but it’s not like I could even if I wanted to."
    "The truth is that even though Maki and Makoto couldn’t be further apart in terms of personality, they’re still two of three cerberian heads. "
    "The third, however, has been severed and is now floating somewhere out in space."

    if bonus == True:
        "Maybe fucking aliens, maybe not."
        "There’s no way of knowing."
        "But at least I know that the other two heads are [[probably] safe for the indeterminate future."

    $ renpy.end_replay()
    $ makiday351 = True
    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate15:
    scene makihhg1
    with dissolve
    play music "citylife.mp3"

    "I make my way into the porn shop only to be immediately assaulted by a hefty dose of deja vu."

    maki "Why am I doing this to myself? I don’t even like fishing."

    if bonus == True:
        maki "Besides, everyone knows that putting mini games into a porn game is the quickest way to get people to drop it."
        maki "Just let me fuck bitches. I wanna fuck bitches."
    else:
        maki "Besides, everyone knows that putting mini games into a porn game makes people quit even faster than blatantly censoring 100%% of its adult content."
        maki "Just let me HUG WOMEN. I wanna HUG WOMEN."

    s "Ahem."

    scene makihhg2
    with dissolve

    maki "..."
    s "..."
    maki "What?"
    s "Seems to me that you’re having a little trouble."

    if bonus == True:
        maki "I’m sorry, sir. We’re closed for the night because I apparently have to catch fish if I ever want to get laid."
    else:
        maki "I’m sorry, sir. We’re closed for the night because I apparently have to catch fish if I ever want to get hugged."

    s "You know, it wasn’t too long ago that I remember having a similar conversation with your daughter."

    if bonus == True:
        maki "Is Makoto making you fish in order to get into her pants? Because I’m pretty sure I taught her better than that."
    else:
        maki "Is Makoto making you fish?"

    s "What? No."

    if bonus == True:
        "Though, she did have to beg for a good amount of time."
        "But it’s not like I can say that to Maki."

    s "I just mean that she was playing this game the first time you and I met."

    scene makihhg3
    with dissolve

    maki "Aww. That makes this some sort of romantic reunion then, doesn’t it?"
    s "I don’t think there’s anything romantic about watching you catch fish in a porn shop."
    maki "And yet here we are."
    s "Why are you even playing it if you’re not having a good time?"

    scene makihhg4
    with dissolve

    if bonus == True:
        maki "Well, technically I’m {i}re{/i}playing it. I played a bit when it first came out, but Makoto had more sex than me so now I need to catch up."
        maki "Besides, she said they added more content and I want to see if I can bang the girl with the cat ears yet."
        s "Well I wish you the best of luck, Maki. "
        maki "Why are you making it sound like you’re about to leave? Come bang the cat girl with me."
    else:
        maki "Because that's what the script says I'm supposed to do."
        s "I see."

    mak "Ahem."

    scene makihhg2
    with dissolve

    maki "Oh, come on. What now?"
    s "It wasn’t me that time. "
    maki "If it wasn’t you then-"

    scene makihhg5
    with dissolve

    mak "..."
    maki "Oh. "
    maki "I thought you went out with Miku."

    scene makihhg6
    with dissolve

    mak "I thought {i}you{/i} were going to be working tonight."
    maki "I {i}am{/i} working. This is my job, sweetie."

    if bonus == True:
        jump makihhgx
    else:
        s "I was? Why?"
        maki "Because that's what the script says you have to do?"
        s "Ugh. Really? I wish they'd tell me these changes ahead of time."
        mak "Just shut up and leave, Sensei."
        s "You're so rude in the censored version."

        scene black
        with dissolve2

        "I go home and write an angry letter to the developer of Lessons in Love."

        $ renpy.end_replay()
        $ makidate15 = True
        $ maki_love += 1
        $ maki_lust += 3
        stop music fadeout 5.0

        "{i}Maki’s affection has increased to [maki_love]!{/i}"
        "{i}Maki’s lust has increased to [maki_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makiinvite1:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "I’m not exactly sure how Ami will handle me inviting over the mother of her arch nemesis, but I’ll be damned if I let an obnoxious girl with A-cups rule my life."
    "I am an adult looking for another adult to do adult things with- and Maki is the only adult I know who is very rarely busy with anything since her daughter can just take over."
    "I mean, I guess Sara would also work, but I feel like it’s a lot easier to sell porn than it is to revitalize a failing bar. No offense, Sana."

    play sound "phonebeep.wav"

    if bonus == True:
        maki "Gangbang hotline, this is Maki speaking."
        s "Before I place an order, are you able to clarify if {i}I{/i} would be the one getting gangbanged? Or am I calling to participate in a gangbang? "
        maki "I would not be willing to clarify that, no. Would you still like to place an order?"
        s "Sure. One Maki, please."
        maki "Can it be any Maki or are you looking for a particular model?"
        s "Do you want to hang out or are you just going to keep being weird?"
        maki "Mmm...I choose both!"
    else:
        maki "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHH!"
        s "Why are you screaming?"
        maki "I don't know. Can I come over?"
        s "I guess."

    s "Just don’t be {i}too{/i} weird in front of my [niece]. She already kind of hates your daughter, so you’re kind of starting off on thin ice."
    maki "What? Why would anyone ever hate Makoto? Makoto is great. "
    maki "I hope your [niece] is ready to throw hands."
    s "Okay. Sending you the address now. "

    if bonus == True:
        maki "How much lube should I-"
    else:
        maki "Sure! But I recently started selling lotion and-"

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and quickly text Maki my address."

    if bonus == True:
        "I feel mostly safe in assuming that she won’t actually be bringing any lube, but I ask her to leave everything behind in the event that she just...doesn't care about anything I say."
        "It’s one thing bringing an older, lazier looking Makoto over to the house, but having her come equipped with what I imagine is an entire collection of lubricant would be too hard for even {i}me{/i} to get out of."
        "Either way, I wait for Maki to confirm that she’s on her way over and slide my phone back into my pocket before setting course home."

    "........."
    "......"
    "..."

    scene makifirstinv1
    with dissolve
    play sound "dooropen.mp3"
    play music "normalday.mp3"

    "I make my way inside and prepare myself for what I hope will be a rather easy and dramaless night in."

    a "Get out of here!"

    "It appears that will not be the case."

    s "I don’t know what I did, but-"
    a "You mean to tell me that for only 1,000 yen a month, I can get all of the lotion I want?! "
    s "..."
    maki "That’s right, Ami! And this isn’t just {i}any{/i} lotion...it’s lotion {i}guaranteed{/i} to keep you looking [young]and energetic for the rest of eternity."
    a "Ahh, that’s even better! My [uncle]’s not home right now so he won’t get mad at me for saying this, but he {i}really{/i} seems to like [younger_girls]."
    s "..."
    maki "Does he now? Well, then I...totally understand why you’d want him to look at you that way! "

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "Maybe I should just come back later."

    a "Wait, Sensei?! Is that you or did somebody break in?!"
    s "..."

    play sound "dooropen.mp3"
    scene makifirstinv2
    with dissolve

    s "Hah...Hi, Ami. And hi-"

    if bonus == True:
        maki "Felicity Fellatio, at your service!"
        s "..."
        a "Sensei! Miss Fellatio says that for only 1,000 yen a month, I can have all the lotion I want!"
        a "Can I borrow 1,000 yen a month so I can be pretty {i}forever?{/i}"
        s "You have a job now. Use your own money."
        s "Also, don’t you think her last name is kind of suspicious?"
        a "Hm? Isn’t fellatio some type of...Italian dessert or something? Stop being so culturally insensitive, Sensei."
    else:
        maki "Just call me Ami 2!"
        s "No."

    scene makifirstinv3
    with dissolve

    maki "Now, I know what you’re thinking."
    s "Do you really, though?"
    maki "Of course! {i}You’re{/i} thinking...“Wow! Only 1,000 yen a month?! What a steal!” "
    maki "Well, let me tell you this, buddy. It really all starts to make sense when you take a look at our business model."
    s "You don’t even have any products with you."
    a "She showed up with a whole suitcase of all different kinds of exotic lotions. "
    a "I thought it was a little strange when she knocked since we don’t really get a lot of door to door salespeople around here, but as soon as I smelled what was inside, I immediately knew what was going on."
    s "I’m sure you did, Ami. "

    scene makifirstinv4
    with dissolve

    maki "Oh my. It appears we may have a bit of a skeptic on our hands!"
    maki "Tell me, fine sir who I have never met before, how would {i}you{/i} like to sample some of my one of a kind, {i}exotic{/i} hand lotions?"
    s "You mean the “hand lotions” I specifically asked you not to bring?"

    scene makifirstinv5
    with dissolve

    a "Wait, you were expecting her, Sensei? Did you set up an appointment thingy with this lady?"
    a "My birthday isn’t for a long time, so-"

    scene makifirstinv6
    with dissolve

    a "Wait, is this an early Christmas present?! You’re getting me a lifetime supply of youthful lotion so I can stay adorable forever?!"

    if bonus == True:
        s "No. This is actually Makoto’s mom and her suitcase is full of a bunch of stuff that is most definitely not lotion."
        a "...What?"
    else:
        s "No. This is actually Makoto’s mom and all of that lotion is for me. I have very dry skin."
        a "...What?"

    maki "Why didn’t you just go along with it? "
    s "Better question, how did you manage to get here before me?"

    scene makifirstinv7
    with dissolve

    maki "I just happened to be making my rounds in the area as a totally legitimate lotion sales rep! And since you {i}scheduled an appointment with me{/i}, I was {i}always{/i} going to show up."
    a "Sensei, would you mind explaining to me what is going on here?"
    s "I kind of did already."
    a "So this actually {i}is{/i} Makoto’s mom?"

    scene makifirstinv8
    with dissolve

    maki "Uhh...yes! But just because I lied about my name doesn’t mean I lied about the product!"
    a "I {i}thought{/i} you looked familiar..."

    if bonus == True:
        s "Maki, why are you still so focused on selling a product that doesn’t even exist?"
    else:
        s "Anything for a sale, right? You're a true business woman, Ami 2."

    scene makifirstinv9
    with dissolve

    maki "It’s in my blood, obviously! My job is to sell things! And sometimes, in order to sell things, you need to lie about them!"

    if bonus == True:
        maki "“{i}Excuse me, miss, but does this vibrator have multiple speeds?{/i}” “Why, of course it does! Just don’t read the part of the box that says it only has one!”"
        maki "“{i}Excuse me, miss, but my wrists are very sensitive. Do you have any velcro handcuffs?{/i}” “Why, of course I do! Because that product totally exists!”"

    s "How are you still in business?"

    if bonus == True:
        maki "Because I sell fucking porn, not security devices. No one’s going to ask for their money back so long as they still have an orgasm at the end of the day."
    else:
        maki "Because I sell fucking porn, not security devices."

    a "You sell {i}what{/i}?"

    scene makifirstinv10
    with dissolve

    maki "Corn! Canned! Cobbed! Creamed! Any type of-"

    scene makifirstinv11
    with dissolve

    maki "Pfft~"

    if bonus == True:
        maki "Creamed..."
    else:
        maki "Corn..."

    a "..."
    s "..."

    scene black
    with dissolve

    "Perhaps I should have played along."
    "And you know, maybe in another life, I would have."

    if bonus == True:
        "But as Ami’s legal guardian and a man who, on several occasions, has let her borrow my credit card, I refuse to allow her to get sucked into a fictional pyramid scheme."
    else:
        "But as Ami's little pogchamp, I owe it to her to be honest."

    "Even if it means sentencing her to a life of hating Makoto’s mother- something I’m already sure was going to happen anyway."
    "........."
    "......"
    "..."

    scene makifirstinv12
    with dissolve

    a "You betrayed me! I invite you into my house because your suitcase smells good and {i}this{/i} is how you repay me?!"
    a "Get out and never come back!"

    if bonus == True:
        maki "Fine! I admit it! I took advantage of your trust and made you believe my suitcase full of lubricant was a suitcase full of lotion! "
        a "Why are you selling something that weird door to door?! Are you some kind of...nymphomaniac or something?!"
        s "Ami, come on. You can’t just elect to believe the door to door part of her story. It’s clearly all part of a coordinated effort to-"
    else:
        maki "You're not my mom! I don't have to listen to you!"

    scene makifirstinv13
    with dissolve

    a "How many more Miyamuras are you going to invite into this household, Sensei?"
    maki "If you wind up inviting a third, can you ask him to {i}at least{/i} come say hello to his daughter? She misses him."

    if bonus == True:
        s "I’m not inviting any other Miyamuras over to the house. One was more than enough and that still didn’t deter me from bringing in Maki and her lube collection."
        maki "Heh. You said lube."
    else:
        s "I’m not inviting any other Miyamuras over to the house. One was more than enough and that still didn’t deter me from bringing in Maki and all of her fancy lotions."
        maki "I'm not Maki. I am Ami 2."

    scene makifirstinv14
    with dissolve

    a "Get out of my house, you harlot!"
    maki "Harlot? Is this the renaissance? Have some dignity and call me a whore like a normal girl."
    a "I can’t tell which of you is worse! You or Makoto!"

    if bonus == True:
        maki "Me, obviously. Makoto is just the prettier, smarter, less sexually confident version. And if there is anything worth admiring in today’s political climate, it is a lack of sexual confidence."
        maki "And also a surplus of sexual confidence. As long as it’s one or the other, things’ll be good. "
        maki "Anyway, were you going to buy any {i}lotion{/i} or should I start packing my things?"
    else:
        maki "Obviously me! Makoto is great!"
        maki "But seeing as I am no longer welcome here, I will start packing my things."

    s "You’re not planning on leaving already, are you?"

    scene makifirstinv15
    with dissolve

    a "Why do you want her here when you have me?!"
    maki "You’re actually okay with me staying? "

    if bonus == True:
        maki "I could have sworn the whole pretending to be a saleswoman and roping your [niece] into a make believe pyramid scheme by calling lube lotion would have been your sign to be like, “Bye, Maki.”"
        s "Well, you have sworn incorrectly."
        s "Besides, this gives me the opportunity to try something I’ve been wanting to try for a long time now."
        maki "I hope it involves lube, because I brought plenty."
    else:
        s "Yeah. I still need to go through all of the lotions and figure out which one is best for my skin."

    a "You can’t be serious!"
    s "I am serious. In fact...I am so serious, that I am, going to do {i}this.{/i}"
    a "Lay one finger on her and she’ll be leaving this house in a variety of different bags!"
    s "Ami-"

    stop music

    s "Go to your room."

    scene makifirstinv16
    with dissolve

    a "Ah..."
    a "You {i}didn’t...{/i}"
    maki "Hah. Get parented, loser."
    s "Right now, [young]lady."

    "I do my best to put on an adult voice, but I’m pretty sure it’s just my normal voice."
    "Probably because I’m an adult."

    play music "normalday.mp3"

    a "You..."
    a "Why do I...actually feel compelled to go to my room?..."
    s "Because starting right now, you are grounded."

    scene makifirstinv17
    with dissolve

    a "For...for how long?!"
    s "Until Maki leaves. After that, you can do whatever. "
    a "Why am I in trouble when all I wanted to do was protect your honor?!"
    maki "Be careful or he might {i}actually{/i} ground you."
    s "Ami. Room."

    scene makifirstinv18
    with dissolve

    a "GRAAAAAAH! I STILL HATE YOU AND YOUR STUPID DAUGHTER!"

    scene makifirstinv19
    with dissolve
    play sound "doorslam.mp3"

    "Ami [[miraculously] goes into her room and slams the door behind her."
    "And, in other news, I gained a new power today."

    if bonus == True:
        maki "You know, if I knew this was going to turn into a whole thing, I would have just left the lube behind."
    else:
        maki "You know, if I knew this was going to turn into a whole thing, I would have just left the lotion behind."

    scene makifirstinv20
    with fade

    s "You mean like I {i}asked{/i} you to?"

    if bonus == True:
        maki "I thought that was a joke. I wasn’t about to miss out on an opportunity to break out the travel lube. Do you have any idea how long it’s been since I got to show that to anyone?"
        maki "Cause it’s been a long time, Sensei. A {i}long{/i} time."
    else:
        maki "Did you ask me something like that?"
        s "Maybe not in this game, but I swore I could have asked in the last one."
        maki "Huh. Either way-"
        maki "You hung up on me and I wanted to spite you."

    s "That aside, I think it’s safe to assume Ami hates you now."

    scene makifirstinv21
    with dissolve

    maki "Excellent."
    s "Why is that excellent? Normally, when you get invited over to a person’s house, you’re supposed to try to {i}not{/i} make them hate you."
    maki "Normally, yes. But I came here with the knowledge that, for some reason, your fake daughter has a problem with my real daughter."
    s "She is my [niece], not my daughter."

    if bonus == True:
        maki "I bet she calls you Daddy in her fantasies."
    else:
        maki "I bet she still thinks of you as her daddy."

    if amimaster.lower() in ["daddy"]:
        "I mean...she calls me that in a lot more than just her fantasies."
        "But even if that’s the case, I can’t let Maki actually believe it."

    s "Her real dad is actually dead, so...probably not."

    scene makifirstinv22
    with dissolve

    maki "Oh...crap."
    maki "I’m sorry. I didn’t mean to bring up bad memories."
    s "It’s fine. I don’t have many memories of it in the first place."

    play sound "static.mp3"
    scene amiani4 with flash
    scene makifirstinv22 with flash
    stop sound

    maki "Either way, I crossed a line and I’m sorry."
    s "..."

    scene makifirstinv23
    with dissolve

    maki "But, uhh...what I meant by the whole “excellent” comment is that now, by comparison, Ami will probably hate {i}me{/i} a little more than Makoto."
    s "That wasn’t your plan from the start, was it?"

    scene makifirstinv24
    with dissolve

    if bonus == True:
        maki "No. I just wanted to hang out and talk and maybe show off all of my cool lubes."
        maki "But halfway through my sales pitch, I started thinking, “You know what? This is probably going to go south eventually.”"
        maki "In my defense, though, if you hadn’t taken your sweet ass time getting over here, this never would have happened."
        s "What are you talking about? I came right over after I called you."
        maki "Well then I guess I’m just super fast and you’re the human equivalent of a turtle."
        maki "Anyway, want to go get dinner or something? It’s nice being invited over, but it feels a little strange when your [niece] likely has her ear to the door to make sure we’re not having sex."
    else:
        maki "No. I just really need the money and have to sell as many lotions as possible or I'm going to have to take out a second mortgage on my home."
        maki "Anyway, want to go out to a fancy restaurant or something? I will pay."
        s "Sure. That sounds great."

    play sound "knock.mp3"

    a "{i}THAT’S RIGHT! RUN AWAY, MAKOTO’S MOM! THIS HOUSE BELONGS TO THE ARAKAWAS!"

    if bonus == True:
        maki "See what I mean?"
        s "You’ll grow to accept her in due time. Ami just has a very strong sense of family values."

        if amilust15 == True:
            "In fact, it’s so strong that sometimes she even starts masturbating in my bed while I’m asleep."
            "Just normal family stuff, I suppose."

        scene makifirstinv25
        with dissolve

        maki "I wish Makoto was like that."
        maki "Sometimes, I feel like she doesn’t really care {i}what{/i} I do."

        scene makifirstinv26
        with dissolve

        maki "Buuuut I’m not about to start complaining right before we leave."
        maki "I have wreaked enough havoc on your relationship with {i}one{/i} [teenager] today, and I’ll be damned if I make you think less of Makoto by complaining or venting to you."
        s "I mean...if you really want to talk-"
        maki "You’ll hear me out and help me with my problems?"
        s "The first part, sure. But if you ever have to come to me for help, you’re likely so far off the deep end that literally {i}no one{/i} can help you anymore."
        maki "Blah blah blah self-deprecation and sad stuff. I want meat. Let’s go get...barbecue or something."
        s "Deal."

    scene black
    with dissolve
    play sound "knock.mp3"

    if bonus == False:
        s "Come, Maki. Fine dining awaits."

    a "WAIT! NO! SENSEI! YOU HAVEN’T TOLD ME I CAN LEAVE MY ROOM YET!"
    maki "Should you maybe let your [niece] out first? She might have to go to the bathroom at some point."
    s "She’ll be fine. She’s well behaved when she wants to be."

    play sound "dooropen.mp3"

    a "NO! DON’T LEAVE ME!"
    a "ESPECIALLY NOT WITH A MIYAMURA!!!!!!!!!!!"

    "Maki and I make our way over to some restaurant close to her shop so that, once we’re done, she can head back home to sub in for Makoto."
    "As it turns out, Maki was supposed to work tonight and Makoto was supposed to be helping Miku with something."
    "But, of course, whenever I ask anyone to do anything, they almost always drop their previous plans for me."
    "Just one of the perks of living in Kumon-mi, I guess."
    "Anyway, dinner is great and Maki winds up fronting the bill to pay for causing a disturbance at my house."
    "Was it a disturbance I both expected and created by inviting her there? Yes. But it’s not like I’m going to give away a free dinner in exchange for admitting that."
    "Instead, I’ll just shelve that idea alongside the thousands of others that I have pushed away from me in a never ending journey toward complacency."
    "The two of us split apart-"
    "And I go home to let my [niece] out of her cage."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makiinvite1 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makiinvite2:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "Seeing as last time she came over we didn’t exactly get to spend too much time together, I’m thinking that today might be a good chance to turn that around."

    if bonus == True:
        "Unless she brings another suitcase full of sexual accessories again. "
        "Actually, if she {i}is{/i} going to bring a suitcase full of sexual accessories again, today is probably the best day to do that on account of Ami being out with some of the other girls."
    else:
        "Unless she brings another suitcase full of lotion again. "

    "I’ll just let Maki field this however she wants to and we’ll see where things go from there."

    play sound "phonebeep.wav"

    if bonus == True:
        maki "Gangbang hotline! Maki-"
        s "Is this just how you answer the phone now?"
        maki "Well, with so many gangs and so little banging, I’m just trying to contribute in the only way I know how."
        s "Cool. Are you free right now?"
        maki "Would you like to set up another lotion sales meeting? I’m still waiting on your [niece]’s initial down payment to get the ball rolling."
        s "I would like to set up a normal get together without any briefcases or short girls with vendettas against taller, attractive women."
        maki "Aww~ You really think I’m tall?"
        s "Are you coming or not?"
        maki "Makotoooooooo?"
        mak "{i}What? What do you want?{/i}"
        maki "I forgot I had an important SALES MEETING tonight. Are you able to watch the store for me?"
        mak "{i}Sure, but...why did you say SALES MEETING like that?{/i}"
        maki "No reason! Love you!"
        maki "Sensei?"
        s "Still here."
        maki "I shall be over shortly. Just have to pack the briefcase."
        s "...Sounds good. "
    else:
        maki "Phone stuff!"
        s "Wanna come over?"
        maki "K!"

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and begin to walk a little faster than normal on the way home so Maki doesn’t wind up there before me again."
    "Even if Ami isn’t home right now, I’d feel weird about some woman in a vest just hanging out outside of my house when my neighbors...exist."
    "Come to think of it, I’ve never even talked to my neighbors."
    "Or...seen them."
    "But I’d like to keep that up for as long as possible, so...here’s to walking a little faster than normal, I guess."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene makisecondinv1
    with dissolve
    play music "acoustic.mp3"

    maki "Yo!"
    s "Woah. Look at you."
    maki "Tall, right?"
    s "I was thinking something more along the lines of...handsome?"
    s "Is calling a girl handsome offensive in some way?"

    if bonus == True:
        maki "Not when that girl has pegged her husband more times than he’s pegged her. "
        s "Thank you for reminding me of that. "
        maki "Don’t mention it."
    else:
        maki "To some! But I kind of like it!"

    scene makisecondinv2
    with dissolve

    maki "So, what’s the plan? I was actually feeling energetic enough to put on nice clothes today, so I kinda want to do something out in public so people can see how hot I am."
    s "Just dress like this more often and everyone can see that all the time."

    scene makisecondinv3
    with dissolve

    maki "But getting dressed is haaaaaaard. That’s why I only do it on special occasions."
    s "Special occasions?"

    "Does she think today is...special for some reason?"

    scene makisecondinv4
    with dissolve

    maki "Oh! Uhh...huh."
    maki "I mean...I don’t think it’s...{i}not{/i} special spending time with you?"
    maki "Even though both of my closest friends {i}and{/i} my daughter seem to be closer to you than I am and...woah. Weird."
    s "What’s weird, exactly?"

    scene makisecondinv5
    with dissolve

    maki "Was I...trying to impress you?"
    s "...You don’t know?"
    maki "Not a clue. But I’ve got the suspenders on and I barely ever even broke these out when I was married."
    s "Well...thank you, I guess?"

    scene makisecondinv6
    with dissolve

    maki "{i}Ahem{/i}. Yes, don’t mention it. All in a day’s jerk."
    maki "Err, work."
    s "..."

    scene makisecondinv7
    with dissolve

    if bonus == True:
        maki "I said work. You know, like a blowjob."
    else:
        maki "I said work. You know, like an accountant."
        s "..."

    scene makisecondinv8
    with dissolve

    if bonus == True:
        maki "No, Maki. Bad. {i}Not{/i} blowjob. {i}Normal{/i} job. The less fun kind that end with paychecks instead of cumshots."
    else:
        maki "No, Maki. Stop talking about accountants. He'll think you're schizophrenic."

    s "You doing okay over there?"

    scene makisecondinv9
    with dissolve

    if bonus == True:
        maki "Is it hot in here or do I just want to fuck you?"
    else:
        maki "Is it hot in here or is it just the opposite of cold?"

    s "Well, based on how it’s the same temperature as always in here and...your sudden inner struggle to speak normally, I’m going to guess it’s the latter."

    if bonus == True:
        maki "The nice clothes are beginning to make sense."
    else:
        maki "Fuck, dude."

    if makibj == True or harukalust10 == True:
        if bonus == True:
            s "So...what now? Do we have sex?"
            s "I mean, it would make sense for that to finally happen since we are both adults with a great appreciation for it who just...haven’t done it with each other for whatever reason."
            maki "I will not lie in saying that I am immensely intrigued by the idea of something as large as your penis inside of me. "
            maki "I mean, it also helps that you’re hot, too. But this is really all about the dick."
            maki "It is a very good dick. A real pornstar sized schlong. A big ole baseball bat boner. Just a straight up colossal cock."
            s "..."
            s "Thanks."

            scene makisecondinv10
            with dissolve

            maki "It’s just..."
            maki "I don’t know. It feels weird. You’re my daughter’s teacher."
            s "So...the other stuff wasn’t weird, but actually having sex is?"
            maki "Maybe? I just feel like if Makoto found out, it wouldn’t end well for either one of us."
            maki "I’m sure it’s just a[school]girl crush and that it’ll all fade away on its own...I had one of those too. But like...it would break her heart if she found out about it."
            s "We can just...not let her find out?"

            scene makisecondinv11
            with dissolve

            maki "I think you’re misunderstanding how perceptive Makoto is. I don’t really know if I’ll be able to hide it."
            maki "I’m not that...bright, you know? Like I’m not stupid, I’m just...too open. Or something."
            maki "But {i}my god{/i}, that dick."
        else:
            s "So...do you want me to turn the temperature down or something?"
            maki "Yes. Please do that."

    elif makibj == False and harukalust10 == False:
        if bonus == True:
            s "So...what now? Do we have sex?"

            scene makisecondinv10
            with dissolve

            maki "I...don’t know?"
            maki "This is...weird."
            maki "I mean...I’m sure I knew in the back of my mind that something like this was a possibility when you started inviting me over."
            maki "Not to mention your porn addiction completely revealing that you’re not the more “wholesome” kind of guy."
            s "It’s not an {i}addiction{/i}, Maki. I just go there to hang out with you and your daughter."

            scene makisecondinv12
            with dissolve

            maki "Do you mind if I ignore the daughter part so I can keep living in blissful ignorance that you’re not coming to a porn shop to hang out with my [high_school]er?"
            s "Yes. In fact, I’d prefer that you do just that as mentioning Makoto there was an accident and definitely not why I go there."

            "It looks like our secret lives to fight another day, Makoto. "
            "You’re welcome."

            scene makisecondinv13
            with dissolve

            maki "R-Right! Yeah. Of course you go there to see me. But like...being addicted to porn isn’t bad, you know?"
            maki "I mean, I am! And I’m just fine! It’s not like I’m getting dressed up to go tell my daughter’s teacher I want to have sex with him or anything. "
            maki "Like, who in their right mind would do that?"
            s "Are you going to trick yourself into thinking you don’t want it now?"

            scene makisecondinv14
            with dissolve

            maki "Hah...I don’t know."
            maki "It just feels kind of...wrong. You’re my daughter’s teacher."
            s "And that makes it wrong?"
            maki "It’s wrong because of how she feels about you."
            maki "I’m sure it’s just a[school]girl crush and that it’ll all fade away on its own...I had one of those too. But like...it would break her heart if she found out about it."
            s "..."

            scene makisecondinv11
            with dissolve

            maki "I’m sorry. I’ll stop. I’m taking things too far this time and I apologize."
        else:
            s "So...do you want me to turn the temperature down or something?"
            maki "Yes. Please do that."

    "Well...it looks like the time has come for me to make yet another decision that can make or break a relationship."

    if bonus == False:
        "I had no idea Maki took the temperatures inside of houses so seriously."
        "But if she wants it turned down, then..."
    else:
        "Well, maybe."
        "I think Maki’s interest in sex is great enough that more opportunities may arise, but..."
        "Is that really the relationship I want to have with her?"
        "Makoto’s fragile enough as-is. If she finds out that I’m fucking her {i}mother{/i}, the last person she has left in this city, what will that do to her?"
        "She may act mature, but I know for a fact now that there’s a darker side to her. And converting a playful relationship with her parent into something more is just..."

    scene makisecondinv15
    with dissolve

    maki "I’m, uhh...not liking the sudden silence, Sensei."
    s "Because you’re worried about how it will impact our future?"
    maki "I don’t think much will change with us no matter {i}what{/i} we decide to do here. We’re adults and adults just...do things like this sometimes."

    if bonus == True:
        maki "It’s more that just long stretches of silence make me feel weird, especially when they happen shortly after admitting that I kiiiiiinda wanna fuck my daughter’s teacher."
        s "And I kind of want to fuck my student’s mother."
    else:
        maki "That's right. Sometimes, adults adjust the thermostat."
        s "And other times..."
        maki "They adjust it together..."
        s "..."
        maki "..."

    scene makisecondinv16
    with dissolve

    maki "So...is that it, then? We’re doing it?"
    s "I mean..."

    "I sigh to myself and try to figure out what I want to do here."

    menu:
        "I can’t do that to Makoto":
            if bonus == True:
                s "..."
                maki "..."
                s "We shouldn’t."

                scene makisecondinv17
                with dissolve

                maki "Yeah..."
                maki "Yeah, you’re right."
                maki "No matter how much we want to, we have to think about Makoto."
                maki "We can’t risk breaking her heart just because we can’t keep our pants on."

                scene makisecondinv18
                with dissolve

                maki "But, uhh...that’s just how we are! You know?!"
                maki "Always thinking about dicks and...pussies...and...spontaneous blowjobs under your office desk after I drop Makoto’s lunch off at[school]."
                s "..."
                s "Is it too late to change my choice?"

                scene makisecondinv19
                with dissolve
            else:
                s "..."
                maki "..."
                s "We shouldn’t."
                s "What would Makoto think?"
                maki "Probably nothing. She'd have no idea."
                s "But what if she {i}did?{/i}"
                maki "Good point."

            "Maki goes silent for a moment and makes eye contact with me for longer than she ever has before."

            if bonus == True:
                "And even though the topic at hand is sexual in nature, I feel as if she’s actually trying to connect with me on a level that isn’t just physical this time."

            "I can’t tell what her gaze is saying, but I can feel that there’s a lot more to it than just one more fleeting moment in a life of many for her."
            "How many others has she given this look to in the past? "
            "Am I among the few?"
            "Am I perhaps the only one who’s ever gotten this look?"
            "I don’t know."
            "And, unfortunately, I don’t think I ever will now."

            maki "Yeah."
            maki "It’s too late."
            maki "But we..."
            maki "We can stay friends."
            s "..."
            maki "..."

            scene makisecondinv20
            with dissolve

            if bonus == True:
                maki "But...don’t get mad when I go home and fuck myself to the {i}fantasy{/i} of having sex with you!"
                maki "I can do that as many times as I want and both you {i}and{/i} Makoto can’t do anything to stop it."
                s "I...did not plan on stopping you."
                maki "Rub one out in my honor tonight, would you?"
                maki "Or don’t. I don’t care."

                scene makisecondinv21
                with dissolve

                maki "I’m...uhh...gonna head out, though?"
                s "Already?"
                maki "Yeah...I feel like I might try and make a move on you if I don’t, so..."
                maki "This is for both ours and Makoto’s safety."
                s "..."

                scene black
                with dissolve

                s "I understand."
                s "Have a good night, Maki."
                maki "You too!"
                maki "And...remember to lock the door while you...yeah."
                maki "See ya."

                play sound "dooropen.mp3"

                "Maki exits the house quicker than I’ve probably ever seen her move before, but I don’t really blame her."
                "Things kind of got a little awkward once the two of us decided to cast aside our sex drives in favor of someone who wasn’t even around."
                "It’s...kind of weird, now that I think about it."
                "Since when do I care about what other people think?"
                "And, even weirder, since when do I let that dictate who I do and don’t have sex with?"
                "I don’t know."
                "But..."
                "One thing I do know-"
                "Is that I know who I’m thinking about when I rub one out tonight."

                $ renpy.end_replay()
                $ makiskip = True
                $ makibj = False
                $ maki_love += 1
                $ makiinvite2 = True
                stop music fadeout 10.0

                "{i}A string snaps- but Maki’s affection still increases to [maki_love]!{/i}"
                "{i}Who do you think you’re helping?{/i}"
                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat
            else:
                maki "But you can't get mad at me when I go home and change the temperature of my {i}own{/i} thermostat!"
                s "Why would I get mad about that?"
                maki "Because!"
                maki "Anyway...bye!"

                scene black
                with dissolve

                "Maki exits the house quicker than I’ve probably ever seen her move before, but I don’t really blame her."
                "The temperature really {i}is{/i} uncomfortable now that I think about it."
                "Hopefully she doesn't refuse to come over from now on."

                s "..."

                "I wonder if Ami knows how to fix the air conditioner?"

                $ renpy.end_replay()
                $ makiskip = True
                $ maki_love += 1
                $ makiinvite2 = True
                stop music fadeout 10.0

                "{i}A string snaps- but Maki’s affection still increases to [maki_love]!{/i}"
                "{i}Who do you think you’re helping?{/i}"
                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

        "Fuck the mother of a girl who’s always there for you" if bonus == True:
            jump makisecondinvx
        "Adjust the temperature and then hug Maki" if bonus == False:
            s "If I turn the thermostat down, will you agree to hug me?"
            maki "I thought you would never ask."
            s "Asking would be weird. I prefer hugs to happen naturally."
            maki "But you literally just asked me if I would agree to a hug."
            s "Do you want the temperature turned down or not?"
            maki "I'm sorry. Please turn the air on. I am melting."

            scene black
            with dissolve

            s "That'll teach you to never mess with me again."

            "I turn the air on."
            "Maki gets cold five minutes later and asks me to turn it back off."
            "Girls are so exhausting."

            $ renpy.end_replay()
            $ makiinvite2 = True
            $ makisex = True
            $ maki_lust += 3
            stop music fadeout 8.0

            "{i}Maki’s lust has increased to [maki_lust]!{/i}"
            "{i}You can now invite her over after[school] and on weekends!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sadgirls3:
    $ totaldays += 1
    $ day = 6
    hide friday onlayer date
    show saturday onlayer date

    scene makidayafter1
    with dissolve2
    play music "comfort.mp3"

    maki "Hey, sorry I’m late. I didn’t wind up falling asleep until a few hours ago and may or may not have slept through my alarm."
    s "There’s no need to apologize. I’ve only been here for a little while myself."
    maki "Oh yeah? Did {i}your{/i} husband die too?"
    s "..."

    scene makidayafter2
    with dissolve

    maki "Uhh...sorry. "
    maki "Fair warning, though- I’m one of those “mask the pain with jokes” types. So chances are that it’s going to happen again."
    s "If it happens, it happens. I don’t really have any right to talk about how uncomfortable {i}I{/i} am when you’re the one who has to deal with this."

    scene makidayafter3
    with dissolve

    maki "Well, I appreciate that as you’re the first person I’ve been able to actually talk {i}to{/i} about this. The fact that you respect my newfound status as a widow really means a lot."
    s "Was that another joke?"
    maki "It was supposed to be. It sounded funnier in my head."
    s "What about Sara and Haruka? You haven’t talked to them?"
    maki "I texted Sara yesterday. I’m going over to her place after this so I can tell her the full story."
    maki "Haruka, I didn’t talk to until this morning...but she called me yesterday while I was handling Makoto."
    maki "When I looked at my recent calls, my heart dropped as I figured she’d just gone through the same thing I did...and that she was reaching out for someone to lean on."

    scene makidayafter4
    with dissolve

    maki "Of course, that was before the text about how {i}her{/i} husband is still alive and how hearing the news was the best thing that ever happened to her."

    if harukasex == True:
        "Well, it’s good to see that Haruka has an easier time lying through text than in person."

    maki "Sooo...yeah. I kinda gave up on the idea of calling her yesterday out of a mix of envy and misdirected frustration. "
    maki "Especially considering the fact that she didn’t even {i}ask{/i} if I heard anything about my husband. But hey, she rarely ever finds the time to think about anyone other than herself anyway, so it is what it is."
    maki "Actually, come to think of it, maybe my frustration {i}wasn’t{/i} misdirected...and that it was totally okay for me to be angry about that?"

    scene makidayafter1
    with dissolve

    maki "Either way, it’s fine now. I told her on my way over this morning since I figured it would be easier than letting her see me as a zombie and figuring things out through context."
    s "If it’s any consolation, I think you look pretty good as a zombie."
    maki "It’s the hair. It keeps growing even after death."

    scene makidayafter5
    with dissolve

    maki "But, that aside, I guess you’re probably curious about what exactly {i}happened,{/i} right?"
    s "I’d be lying if I said I wasn’t. But it’s not like I expect you to give me all of the specifics since going over them likely won’t do your mental health any good."
    maki "You know, that’s the weirdest part."
    maki "Like, yeah. Yesterday was one of the most miserable days of my life."
    maki "But when I woke up this morning, I brushed my teeth...I got dressed...fixed my hair in the mirror...and for a moment, I forgot my husband was even dead."
    maki "When you rip away the constant realization of something you love being gone, it’s easy to just trick yourself back into feeling normal."
    maki "I don’t know. Maybe it just hasn’t fully set in yet."
    maki "But being able to sit at this table without needing to use your sleeve to dry my tears is pretty nice."
    s "..."
    r "Uhh...good morning."

    scene makidayafter6
    with dissolve

    maki "Good morning, Rin. I like your hair like that. "
    r "Oh. Uhh...thanks. But that’s...not really why I..."
    s "..."

    scene makidayafter7
    with dissolve

    r "Um..."
    r "Is everything okay? Like...with Makoto?"
    r "I heard that she got called to the office yesterday and never came back. And then Miku left too and..."
    r "And now you guys are here and the vibe is all weird and neither of you have even ordered anything and-"
    maki "You don’t have to worry. Everything’s fine."
    maki "Makoto’s just probably not going to be back in school for a while. "
    r "Is she, like...in trouble? Because we don’t really talk much, but she’s seriously one of the most well-behaved people I’ve ever met. And like, there’s no way she actually did something bad."
    maki "She’s not in trouble, don’t worry. It’s just not something you need to be concerned about right now."
    maki "If Makoto wants you to know, she’ll tell you. But knowing that girl, she probably just wants to keep things to herself for now."

    scene makidayafter8
    with dissolve

    r "Okay..."
    r "Can I at least get you something to drink? Coffee? Tea?"
    maki "Coffee sounds nice, actually. Thank you."
    s "And I’ll just have whatever you decide to make me today."

    scene makidayafter9
    with dissolve

    r "Got it..."
    r "I’ll...uhhh..."
    r "..."
    r "Yeah."

    scene makidayafter10
    with dissolve

    "Rin wanders back behind the bar and begins to get our drinks ready, prompting Maki to focus on her as a means of temporarily escaping the reality of the conversation we’re here to have."
    "I don’t attempt to pull her away as even I don’t like having to do this."
    "The whole way here this morning, I was dreading it."
    "Not because I don’t want to see Maki sad...or not because I don’t want to be {i}aware{/i} that Makoto is sad either..."
    "Those things are horrible, don’t get me wrong-"
    "But the reason I was dreading this is because I have no idea what {i}I{/i} am meant to do here."
    "I can’t {i}console{/i} anyone. And Maki is far too old and not nearly naive enough to treat my words as gospel."
    "She’s an adult dealing with an adult issue in an adult way and I’m..."
    "I’m admittedly not good with things like that."
    "If only her daughter were here."
    "If only there was someone still too inexperienced with the world to see through the lack of meaning in all that I say."
    "And how despite acknowledging that, I still wholeheartedly believe it all."

    maki "I like her."
    s "As...a barista? Or as a human being?"
    maki "Mostly as a barista. She seems pretty high maintenance. But she seems like a good person too."
    s "You deal with Miku on a regular basis and you’re worried about how high maintenance {i}Rin{/i} is?"

    scene makidayafter11
    with dissolve

    maki "Okay, listen. Miku may be hyper, but she’s pretty one dimensional when you strip away the baggage she carries."
    maki "I always know what I’m going to get with her. Just...unreserved, innocent sweetness and childlike fascination with pretty much everything and everyone she sees on a regular basis."
    maki "There’s a reason I call her my second daughter, you know."
    s "Is it because your first one doesn’t like you enough?"

    scene makidayafter12
    with dissolve

    maki "Woah, there! Only I’m allowed to make jokes like that today! When you do it, it just makes everything feel more real."
    s "Sorry. I’m a lot better at dragging down the mood than lightening it."

    scene makidayafter13
    with dissolve

    maki "Then I guess I’ll have to switch roles and be the one to make things sad again."
    s "Or we can just...you know, avoid that."
    maki "If it were a small problem, sure. I’d be all for just ignoring it and waiting for it to get bigger."
    maki "But what we’re dealing with is something that has dramatically altered both my life and my daughter’s life. And seeing as you play a part in both of those lives, you should be in the know."
    s "Maki-"
    maki "Yesterday morning, I got a call from my husband’s branch in the JSDF or...KMDF? Whatever the name of the defense force is called. I really wasn’t paying much attention to that part."
    maki "In fact, I was barely paying attention {i}at all{/i} when the call started since it sounded like it was going to be one of those robots who try to sell you stuff. You know?"
    maki "But just as I was about to hang up, I heard my husband’s name and started to put the pieces together."
    maki "Which is probably why I remember the rest of the call word-for-word when I’ve already forgotten the beginning."

    scene makidayafter14
    with dissolve

    maki "Masahiro Miyamura."
    maki "Status: deceased."
    maki "Cause of death: asphyxiation."
    maki "Date and time of death: June 19th, 21:13."
    maki "Remember to smile."
    maki "Transmission over."
    s "June 19th? But that’s-"
    maki "They waited two months to tell me."
    maki "For two fucking months, my husband has been dead."
    maki "And we’ve been talking about him and telling stories about what we’ll do when he gets back without a single fucking clue."
    maki "Isn’t that ridiculous?"

    scene makidayafter15
    with dissolve

    maki "They didn’t even have the dignity to make a {i}person{/i} call me. "
    maki "To have a {i}real, live fucking person{/i} call and tell me my daughter will never see her father again."
    maki "This is a man who lived for over 30 years...who had a daughter...who went into fucking {i}space{/i} to fight in a war despite being a wimpy ass pacifist...and all he gets in memoriam is an {i}automated phone call?{/i}"
    maki "Are you fucking kidding me?"
    maki "That’s seriously it?"
    s "..."

    scene makidayafter16
    with dissolve

    maki "No...No, it’s fine. That’s not even the big issue right now. After all, he’s been dead for {i}two fucking months.{/i} The big issue {i}now{/i} is getting Makoto over this hurdle. "
    maki "It’s spending the next fucking...I don’t know, two years. Three years. Any amount of fucking years watching her excitedly spout out plans for his return and then {i}remembering{/i} that he’s fucking gone."
    maki "Do you think {i}she{/i} got up this morning, brushed her teeth, and fixed her hair in the mirror? Fuck no."

    scene makidayafter17
    with dissolve

    maki "That’s my little girl, Sensei. That’s my little girl and she’s suffering. She’s suffering and I can’t even do anything about it because, let’s face it, {i}who the fuck could in my shoes?{/i}"
    s "How about you, though?"
    maki "What do you mean? What about me? "
    s "I mean how are {i}you{/i} going to get over this hurdle?"

    scene makidayafter18
    with dissolve

    s "Makoto’s not the only person who lost something. You did too. And you need to grieve just as badly as she does."
    maki "..."
    s "What? Am I wrong?"

    scene makidayafter19
    with dissolve

    maki "Hah..."
    maki "It’s going to be hard explaining this to someone without a kid."
    s "I have Ami. She’s close enough."
    maki "If she was “close enough” you’d understand that what you just said might {i}sound{/i} good...but that’s really it. Just sound. "
    maki "I want to grieve. I want to struggle. It feels wrong {i}not{/i} doing that right now."

    scene makidayafter20
    with dissolve

    maki "But, as of yesterday, I'm the only parent Makoto has left. "
    maki "And if {i}I{/i} start breaking down and forgetting to eat and shower and brush my teeth, there’s no way that she’ll get over this in a healthy way."
    maki "So {i}that{/i} is what I’m worried about right now. Getting {i}her{/i} over this."
    maki "I can cry when that’s done."
    s "..."
    maki "..."

    scene makidayafter21
    with dissolve

    "As if on cue, Haruka walks into the cafe and immediately takes note of the friend she absentmindedly forgot to check on yesterday."

    if harukasex == True:
        "And while Haruka and I certainly have our own share of “issues” that we’ll need to address, that doesn’t matter right now."

    scene makidayafter22
    with dissolve

    "She stops at the counter and grabs a small tray of drinks and assorted pastries that Rin prepared for us but likely refrained from delivering on account of the conversation heating up."
    "With Maki’s eyes still closed in either reflection or avoidance at the sound of the door opening, I find no other space to rest {i}my{/i} eyes than in Haruka’s."
    "In that moment, hers rest in mine as well."
    "And they become congruent not in the fact that they share the same level of concern for someone that we enjoy the company of-"
    "But in the fact that they share in mutual pity."
    "For we may {i}think{/i} that we can connect with Maki in this moment."
    "But truly no one can without having experienced what she has."

    scene makidayafter23
    with dissolve

    "Haruka puts the tray down and fills her arms with something else before saying what any reasonable person in this situation would."

    h "I’m so sorry for your loss..."

    "But what does saying something like that even do?"
    "What good is the apology of an uninvolved party in the face of having your life ripped away from you?"
    "Are we not meant to mask our pity in situations like these?"
    "Are we not meant to scrounge up more genuine responses than we’d be able to find at the bottom of a barrel?"
    "Are we truly supposed to say we’re {i}sorry?{/i}"
    "Why?"
    "It doesn’t make sense."
    "But I suppose most things in this life don’t."
    "And I suppose that sometimes a genuinely sorrowful canned response can work as serviceable acknowledgment of that."

    maki "Thanks, Haruka. "
    maki "I’m really happy for you."
    h "Maki...if I knew that your husband-"
    maki "Don’t worry about it. You were excited and...wanted to share the news with someone."
    maki "You had no way of knowing."
    h "But if I did, I-"
    maki "It doesn’t matter."
    maki "So...thanks for your apology. I really appreciate it. But if you don’t mind, I’d like to finish up my conversation with Sensei. "
    maki "You and I can talk later."

    scene black
    with dissolve2

    "Maki tells me more about what she expects from Makoto going forward."
    "She has no idea when she’ll be able to return to school, but assured me that it wouldn’t be a problem as Miku would be taking all of her work directly to her."
    "As if that would even matter right now."
    "I’m not just saying this because I am a horrible teacher, but the last thing I expect out of a girl whose father just died is {i}schoolwork.{/i}"
    "Regardless, I nod and tell Maki not to worry about it- going so far as even offering to deliver Makoto’s “schoolwork” myself."
    "But of course, she in her unwavering devotion to not burdening anyone, refuses such a gesture before getting up from the table and straightening out her clothes."

    scene makidayafter24
    with dissolve2

    maki "Thanks again for meeting with me. I didn’t want the Maki from yesterday ruining your thoughts about the Maki from the future."
    s "I like all Makis equally. Though, I could do with this one being a little more selfish when it comes to her personal feelings."
    maki "Psht. Who needs feelings anyway? All they ever do is get in the way."
    maki "I’ve got a genius to take care of, Sensei. If she stays upset, she’ll never develop the cure for whatever the next big pandemic is."
    maki "I am doing this to save the world. My tears mean nothing in the face of the greater good."
    s "Well, whatever the case, good luck. And if you need any help with Makoto, don’t hesitate to ask."

    scene makidayafter25
    with dissolve

    maki "Leave it to me, Sensei!"
    maki "There’s no problem that Maki Miyamura can’t handle!"

    scene black
    with dissolve2

    "Maki says goodbye and wanders off to meet up with Sara and give her what I imagine will be a very similar speech."
    "I watch from the opposite side of the window, expecting to see her break down now that she’s no longer faced with a situation where she feels obligated to keep her tears in."
    "But she’s an adult."
    "So she probably holds it in until she’s at least a few blocks away."

    $ renpy.end_replay()
    $ sadgirls3 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls4

label sadgirls6:
    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    scene makidrive1
    play music "goodmorning.mp3"

    a "Sensei?..."
    a "I’m sorry to wake you up so early, but..."
    a "There’s a stranger in our house."
    s "..."
    a "..."

    scene black
    with dissolve

    s "I’m going back to sleep."
    a "You’re going to leave me to die just like that?!"

    scene makidrive2
    with dissolve

    s "Ami, if there was an actual stranger in our house, I know for a fact you wouldn’t be calmly discussing it with me after gently waking me up."
    a "Okay...So maybe it isn’t a {i}stranger{/i} per se, but it’s still someone who shouldn’t be here!"
    s "Then tell them to go home. I’m tired."
    a "I tried! But she walked right past me and poured herself a cup of coffee that I made for {i}you{/i} and then sat down on the couch like she owned the place!"
    s "Ugh...who is it then? Noriko? Ayane?"
    a "It’s that frickin’ lube dealer again! And she didn’t even bring any samples this time!"

    "Maki? "
    "She’s {i}here?{/i}"

    s "If it’s her...I’ll be up in a second. I just need to get dressed."

    scene makidrive3
    with dissolve

    a "What do you mean, “{i}If it’s her?”{/i} How the heck am I supposed to interpret that?"
    s "You can interpret it by making more coffee since Maki has apparently taken mine."

    scene makidrive4
    with dissolve

    a "Fine! But only because I love you and would do whatever you tell me, no matter what it is."
    s "I’m aware. Thanks, Ami."

    scene black
    with dissolve2

    "Ami leaves the room and I bring myself to my feet, throwing on the shirt Molly made for me- a shirt that was neatly folded by my “beloved” niece and placed on my desk sometime this morning."
    "If Maki’s here, it can really only mean one of two things."
    "Either the conversation she had with Sara yesterday dramatically failed and she has nowhere else to turn to-"
    "Or it {i}didn’t{/i} fail. And she just needs my help with Makoto again because she can’t figure out how to believe in herself as a parent."
    "I’m not sure why that would cause her to believe in {i}me,{/i} a significantly worse “parent,” but if she’s already here, I shouldn’t keep her waiting."
    "Especially since every second I spend not supervising Ami when she’s near her increases Maki’s chance of being poisoned."

    scene makidrive5
    with dissolve2

    maki "Morning. Do you always sleep this late?"
    s "It’s like 8:00 AM."
    maki "I know. I just figured I’d try making a joke that isn’t depressing, dark, or sexual. Which is probably why it didn’t come out very funny."
    s "While I admire the effort, I {i}would{/i} like to know what you’re doing here."
    maki "Not even going to {i}try{/i} waking up first? Just gonna jump straight to business?"
    maki "Sit down. Have a cup of coffee. Take your time. I’m in no rush."

    scene makidrive6
    with dissolve

    a "You {i}drank{/i} his coffee. Now I have to brew more since {i}somebody{/i} doesn’t have any manners."
    maki "While you’re at it, would you mind making some more for me as well? I’ve been up since 4:00 AM, so I can kind of use it."
    a "Would you like me to add a little something to it that will help you sleep better tonight? {i}Much{/i} better?"

    "Okay. So, apparently supervising Ami won’t stop her from trying to poison Maki either. That’s...good to know."

    s "Ami, don’t poison our house guests please."

    scene makidrive7
    with dissolve

    a "You never let me do anything fun anymore!"
    maki "Thanks for looking out for me. I roofied myself once just to see what it was like and, honestly? It’s not really all it's cracked up to be."
    s "I...don’t think that’s a thing people really “crack up” to be all that exciting."

    scene makidrive8
    with dissolve

    "Ami returns to the kitchen, giving me an opportunity to press a little further about Maki’s reason for coming. "

    maki "Want to go for a drive?"

    "But before I can even ask, she opens her mouth and says that."

    s "Depends. Are you so deeply distressed that you’re going to drive us off a cliff?"
    maki "No. But I {i}will{/i} drive at least 20 mph over the speed limit and make plenty of rolling stops."
    s "You’re lucky Kumon-mi uses American measurement systems or I wouldn’t even know how fast that is."
    maki "And you’re lucky that the roads aren’t busy this early in the morning. Rolling stops are dangerous."

    scene makidrive9
    with dissolve

    maki "Especially when-"
    s "Talk about something else."

    scene makidrive10
    with dissolve

    a "Hm? Did I miss something?"
    s "No."
    maki "..."
    s "..."
    a "...?"

    scene makidrive11
    with dissolve

    maki "Got it."
    maki "Anyway, as I was saying, you’re coming with me. I’ve got a {i}little{/i} bit of a problem I could use your help with."
    s "Does that problem wear glasses and get straight A’s?"
    maki "Usually. Right now? Not really."
    a "Does this have something to do with Makoto getting called to the office the other day?"
    a "Because if she’s been starting trouble, I don’t know if I’ll feel safe in class anymore. "
    a "As the class president, she should be-"
    s "Knock it off, Ami."

    scene makidrive12
    with dissolve

    a "I was only kidding this time!"
    maki "Makoto’s fine. We’re just having some family problems right now."

    scene makidrive13
    with dissolve

    a "Family problems?..."
    maki "It’s nothing you need to worry about."
    a "..."
    maki "...?"
    s "Ami?"

    scene makidrive14
    with dissolve

    a "Oh! Umm..."
    a "Coffee!"
    a "I’ll...be right back."

    scene black
    with dissolve2

    "Strangely enough, Ami retreats to her room without being told after bringing the two of us a fresh pot of coffee."
    "I guess saying “strangely enough” is a little...dismissive, though. Especially when it’s likely that she’s in the early stages of putting two and two together."
    "But while I wish I could stick around and see firsthand just what that dramatic realization does to her, I have been given a job."
    "I am not sure if it is a job that I can handle...nor a job I even {i}want,{/i} but Maki’s assertion (Combined with her exceedingly flattering soccer mom getup) forces me to come along regardless of what I want."
    "And before I know it, I find myself in the passenger seat of a car- checking three times to make sure my seatbelt is buckled."
    "........."
    "......"
    "..."

    scene makidrive15
    with dissolve2

    maki "Are you nervous?"
    s "About what? Seeing Makoto?"
    maki "About anything. You’ve been biting your nails and staring out of the window ever since I started the car."
    maki "My driving isn’t {i}that{/i} bad, is it?"
    s "Your driving’s fine. I didn’t even realize I was acting strangely."
    s "I don’t know. Maybe I {i}am{/i} nervous about seeing Makoto. But it would be a more...subconscious thing than me actively going over it in my head."
    s "Cheering people up isn’t really one of my specialties."
    maki "Yeah, that’s one of many things we have in common. And probably the most boring and depressing out of all of them as well."
    s "So, how is she doing exactly? And...better question, what do you want {i}me{/i} to do about it?"
    maki "I’m pretty sure she hasn’t left her room since I took her home on Friday. But I was out for a good portion of the day yesterday, so I guess it’s possible she got up to use the bathroom or something."
    s "I really hope so."
    s "I’m surprised you felt comfortable leaving her, though. I figured you’d be attached at the hip right now."
    maki "To be completely honest, I’m pretty sure that would just make things worse for her."
    maki "Miku’s been staying over, though. And at least Makoto doesn’t try to keep {i}her{/i} away."
    maki "I dropped her off back at the dorm this morning. Poor girl’s gotten less sleep than both of us."

    if kirinkill == False:
        s "Yeah, well..."
        s "I think we both probably know why."

        scene makidrive16
        with dissolve

        maki "I mean...{i}I{/i} know why. Do {i}you{/i} know why?"
        s "I know enough about her past to piece it together. I just don’t really know the specifics."

        scene makidrive15
        with dissolve

        maki "Huh."
        maki "You two are closer than I thought. "
        maki "Miku doesn’t normally share that with people she doesn’t completely trust."
        s "To be fair, I didn’t exactly learn it from {i}her.{/i}"
        maki "At the risk of harboring a vendetta against whoever told you, I’m going to suggest that we cut this conversation short and just...leave it at our mutual understanding of Miku’s sadness."
        maki "That girl’s been through enough. Talking about this without her knowing just doesn’t sit right with me."
        s "Fair enough. I wasn’t trying to get the details out of {i}you{/i} or anything."
        maki "If Miku trusts you, she’ll tell you. That’s really all you need to know."

    else:
        s "She really cares about Makoto, doesn’t she?"
        maki "Yeah..."
        maki "Yeah, she does."

    "Maki goes back to focusing on the road as a long and uncomfortable silence emerges from the backseat of her car and crawls its way onto the center console."
    "In this abrupt, unwelcome separation comes the realization that I am biting off much more than I can chew right now."
    "That realization grows and festers with every passing stoplight, infecting my body and liquefying my teeth to the point where I can no longer bite anything."
    "It doesn’t make a difference whether or not Maki intends to drive us off a cliff when I started falling to my death the moment I checked my seatbelt for the third time."
    "I want this car to turn around."
    "I want the suffering to end without my intervention- because if there is anything I have learned over my time here, it is that the past repeats itself."
    "And that if my ways of handling Makoto were even the slightest bit successful, I wouldn’t have to keep fixing her."

    maki "You’re doing it again."
    s "Doing what?"
    maki "Biting your nails. "
    s "..."
    maki "You should stop. It’s gross."

    scene black
    with dissolve2

    "Maki continues driving, twenty miles per hour over the speed limit on almost every street we take."
    "But she stops at every stop sign."
    "........."
    "......"
    "..."

    scene makidrive17
    with dissolve2

    maki "So, uhh...do you mind if I get mildly sappy for a minute or two before I take you up to see Makoto?"
    s "Take as long as you like because I still have no idea what I’m going to say to her."
    maki "I mean...I don’t think you really need to say {i}anything.{/i} It’s not like I expect you to go up there and be like, “Hey, Makoto. Sorry your dad’s dead. Feel better now.”"
    maki "She just..."
    maki "I don’t know. I keep wanting to say this is something I should be able to handle on my own, but...the more I think about it, the more I realize that might be the exact problem."
    maki "Makoto can’t see {i}me{/i} without also seeing her father. And it’s that constant reminder that I think is making this so hard for her."
    s "So...serious question. Do you think she can see {i}me{/i} without seeing her father?"

    scene makidrive18
    with dissolve

    maki "I think..."
    maki "Okay. So, you’re obviously the only male authority figure left in her life now. And one that she admires greatly."
    maki "But even with that, I don’t think she’ll ever see you as anything more than her teacher or...maybe a schoolgirl crush."

    "I think it’s a lot more than just a {i}crush{/i} at this point..."

    maki "That girl just...does better with people like you than people like me. It’s a respect thing."
    maki "Like, how is she going to be consoled by someone she automatically associates sex jokes and dildos with? "
    maki "Each time I try to hold her hand, she’s probably thinking “Wow, this hand has touched so many sex toys.”"
    s "I haven’t seen Makoto since Friday, but I’m pretty sure that is not what she’d be thinking."

    scene makidrive19
    with dissolve

    maki "I don’t {i}know{/i} what she’d be thinking, though. I {i}never{/i} know what she’s thinking because her brain is on another level than mine."
    maki "She’s stubborn. She needs someone on the {i}same{/i} level as her to talk to or she’s just going to keep circling the drain."
    s "With all due respect, I think Makoto is several levels above me as well."
    maki "She might be. But I don’t think she sees it that way."
    maki "To her, you’re a role model. Someone she aspires to be. Someone she’ll actually {i}listen{/i} to because you’re not just a joke to her."
    maki "You’re not {i}me.{/i}"
    s "..."

    scene makidrive20
    with dissolve

    maki "Oh, and if you’re having second thoughts about this, I’m not giving you a ride home. I am out of other options and turning to you is pretty much my last ditch effort."
    s "Have you considered {i}time?{/i}"

    scene makidrive21
    with dissolve

    maki "Well, obviously! But time alone doesn’t cure anything when it feels like the walls are closing in around you."
    maki "I need her to feel safe. I need someone to stop those walls from closing in and I’m not strong enough to hold them back on my own."
    s "For what it’s worth, I think you are. But fuck it. I’ll give it a shot. "
    s "If this doesn’t work though and your daughter just winds up becoming even {i}worse{/i} due to something I said, you owe me free porn forever."
    maki "That’s so much porn!"
    s "Yes. I have a problem."
    maki "Okay, fine. But don’t go screwing this up on purpose just to fuel your addiction. "

    "So either Makoto cheers up or I get free porn forever. At least I can’t lose anymore."

    s "Deal. Pleasure doing business with you."
    s "Maybe I’ll even throw in an added bonus of trying to cheer {i}you{/i} up if whatever methods I use on Makoto actually work."

    scene makidrive22
    with dissolve

    maki "Oh, come on...You don’t have to worry about me. "
    maki "I’ve got two close friends who can cheer me up when I need it. You’re here for my daughter."
    s "I am. But I’m here because {i}you{/i} brought me. Which means that you deserve something too."

    scene makidrive23
    with dissolve

    maki "Then I’d like to sacrifice my reward for an additional serving of Makoto’s happiness."
    s "You know...you’re a pretty great mom for someone who thinks they’re a pretty {i}shitty{/i} mom."
    maki "Tell me that again when I don’t feel pressured to rely on a third party to console my daughter because I suck at it."
    maki "And then again when I stop being creeped out by how {i}off{/i} she looks when she’s grieving."

    "..."
    "Wait..."

    scene makotoflashback with fade

    mak "Until everything melts down and reforms into one disturbing mass of flesh, complete with twelve smiles. "
    mak "One for each girl in class that you [masturbate] to while all alone in bed at night."

    scene makidrive23
    with fade

    "Oh no."

    s "Uhh..."
    maki "Welp! Time to go. Makoto’s not going to cheer {i}herself{/i} up."
    s "On second thought, maybe I’ll-"

    play sound "dooropen.mp3"
    scene black
    with dissolve
    stop music fadeout 20.0

    maki "Nope! No more procrastinating. We’ve talked for long enough."
    s "But what if I’m also creeped out by her?"
    maki "You’re like three times her size. What do you possibly have to be afraid of?"
    s "You sell whips. What do {i}you{/i} have to be afraid of?"
    maki "Are you suggesting that I {i}whip{/i} my daughter? I’m into some weird shit, Sensei, but that’s just crossing a line."
    s "Hah..."

    "Maki leads me up a dark staircase, but it’s not dark enough to conceal the array of framed photos hanging on her wall."
    "They’ve all been turned backwards."

    $ renpy.end_replay()
    $ maki_love += 3
    $ sadgirls6 = True

    "........."
    "......"
    "..."

    jump sadgirls7

label makiinv3:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "She hasn’t been back at my house ever since the impromptu semi-kidnapping that resulted in me failing (At least by my definition) to cheer up Makoto, so I figure I should invite her back now that things are..."
    "Well, less horrible."
    "Of course there will be some lingering pain for lifetimes to come, but who says you can’t counteract some of that with a little quality time?"

    play sound "phonebeep.wav"

    maki "Hello?"
    s "Hey. On a scale of one to ten, how miserable are you today?"
    maki "On the inside or on the outside?"
    s "Uhh...both?"
    maki "Eight and four. Why? Do you need a dildo? We offer delivery now."
    s "I can’t imagine there is very much demand for that."
    maki "The market for dildo delivery is actually surprisingly large."
    s "That aside, would you want to come hang out at my place? I can’t guarantee that I can do anything for you on the inside, but I might be able to bring that external misery down to a three."
    maki "Is that so? I think I might have to take you up on your offer then."
    maki "This actually works out really well. I had something to do in that area already. "
    s "It’s not dildo delivery, is it?"
    maki "Nah, it’s nothing that fun. I’m dropping Makoto off for a therapy session."
    s "Oh. "
    s "Yeah, that’s not fun at all."
    s "But good for her."
    maki "Yup! I’ll be over in about...half an hour?"
    s "Sounds good. See you soon."
    maki "Yup! See you!"

    scene black
    with dissolve

    play sound "phonebeep.wav"

    "I hang up the phone and decide to crash on the couch until Maki gets here."
    "........."
    "......"
    "..."

    scene makivisits1
    with dissolve2
    play sound "knock.mp3"
    play music "acoustic.mp3"

    "I spring up from the couch as soon as I hear a knock on the door, hoping I’m able to let Maki in and hide from Ami before that’s a thing I have to deal with today."
    "Should I have waited until Ami was {i}gone{/i} to invite Maki over? Yes. "
    "But part of me doubts she’ll put up much of a fight considering that she now understands everything that happened. "
    "Only part of me, though."
    "This could very well still end extremely poorly."

    play sound "dooropen.mp3"
    scene makivisits2
    with dissolve

    maki "Hey. Thanks for the invite. "
    maki "I was starting to worry that I’d never be invited back after the whole kidnapping thing."
    s "To be fair, that was a situation in which you weren’t invited at all. So I would think that it wouldn’t even matter if I were to invite you or not."
    maki "I guess it doesn’t. I like to keep my home intrusion to a minimum, though."
    s "Probably a good call. Do you have a time limit today?"

    scene makivisits3
    with dissolve

    maki "Time limit?"
    s "You know...since you dropped Makoto off?"
    s "I kind of figured you’d have to go pick her up as well."
    mak "Oh, don’t worry about that. She’s a lot closer than you think."
    s "What?"

    play sound "dooropen.mp3"
    scene makivisits4
    with dissolve

    s "..."
    mak "..."
    s "Please don’t tell me I’m the therapist."
    maki "Hey, I just said it was a therapy {i}session.{/i} I never said there was a therapist involved."

    scene makivisits5
    with dissolve

    maki "But, no. Makoto is here to see someone else. So you and me can hang out until she’s ready to leave. Such a convenient coincidence, right?"
    s "Maybe a little too convenient..."

    play sound "dooropen.mp3"
    scene makivisits6
    with dissolve

    a "Why, hello there. Are you ready for today’s session, Makoto?"
    mak "Can you not call it that? I just want to talk without feeling like I’m totally and irreversibly broken."

    scene makivisits7
    with dissolve

    a "Sure! Come on, I’ll show you my room."
    maki "Maybe keep the door cracked open a little. That look you just gave my daughter a second ago has me questioning just what type of therapist you are."

    scene makivisits8
    with dissolve

    mak "Can you maybe, like...{i}not{/i} ruin this before it even starts? I’m uncomfortable enough as is."
    s "You two can close the door, it’s fine. Just don’t lock it because we’ll be listening closely."

    scene makivisits9
    with dissolve

    mak "Uhh...please don’t."

    play sound "dooropen.mp3"
    scene makivisits10
    with dissolve

    "Makoto and Ami disappear into Ami’s bedroom- which is a thing I never thought I would say, but here we are."
    "I guess the fruits of tragedy can be a little surprising after repeatedly kicking its tree and hoping for something else to fall."

    maki "Makoto told me all about how Ami was able to help her when she ran away to school the other day."
    maki "Of all the people, who would’ve thought she’d be the one to throw her one of those...life saving, floaty tube things."
    s "They’ve found one more thing they have in common, I guess...albeit not a very good thing."

    if kirinkill == False:
        s "Though, I find it a little strange how Ami was able to do something for her Miku {i}wasn’t{/i} when both of them have dealt with the deaths of their parents."
        maki "True. Miku’s case is a little different from most, though."
        maki "In a lot of ways, she hasn’t really processed things either."
        maki "And while I have no idea what your niece’s situation is like, it seems that she was able to tell it to Makoto straight without having to hide everything behind a bunch of walls she put up."
        s "I wouldn’t say Ami has really processed things either. She still breaks down every now and then."
        maki "I think it’s kind of impossible for anyone that young to truly process something like this. It’ll be years before any of those girls can talk about it without bursting into tears."
        maki "For now, though...I say we let them be. They’ll help each other...they’ll connect with each other...and we’ll be here to plug them back in if they ever get disconnected."
    else:
        maki "Yeah...I guess so."

    maki "It pains me to say this as even {i}I’m{/i} starting to see her as a bit of rival, but Ami’s a good girl."
    s "Why would you ever see Ami as a rival?"
    maki "I have no idea. But every time I’m around her, I keep wanting to put her in her place."
    s "It’s starting to make a little sense why you wanted to keep the door cracked..."

    scene black
    with dissolve2

    "Maki takes a seat at the kitchen table."
    "I offer her something to drink but she respectfully declines as scattered but pained laughs play quietly in the background."
    "I turn on the TV to mask them as invading their respective privacies now would do me no good. And curiosity is only beneficial when there is something to be gained from its existence."
    "I will gain nothing from the acute awareness of the suffering of girls that I care for."
    "But they have everything to gain from one another."
    "Which is why I wouldn’t mind if they locked the door."
    "........."
    "......"
    "..."

    scene makivisits11
    with dissolve2

    maki "I’ve gotta say...your family’s been really good at bailing me out lately. This single mother thing isn’t easy. Especially when your relationship with your daughter is already all over the place."
    maki "I’ve got no idea how Sara does it. Especially after losing one of her kids."
    s "I think you’ll be fine. Things already seem to be getting a little better with you two."
    maki "Things {i}are{/i} a little better. We had dinner together for the first time in what feels like years last night."
    maki "Granted, it was a just a pizza we had delivered. But hey, baby steps are fine for now. We’ll be able to walk on our own two feet again in no time at all."
    maki "And all that lashing out in the beginning...while it hurt at the time...I get it now."
    maki "I probably would have done the same if either of my parents died when I was Makoto’s age. But, then again, I was never really as close to either of them as she was with her dad."
    maki "And, you know...while this is still one of the worst things that’s ever happened to me...part of me feels a little relieved."
    maki "I’ve got nothing left to dread anymore."
    maki "I don’t have to worry about the slow creep of tragedy in watching everyone I care about get older since everyone but Makoto is already gone- and I’m going to die {i}way{/i} before her."
    s "I'm pretty sure there should have been some knocking on wood there."

    scene makivisits12
    with dissolve

    maki "Heh. Wood."
    maki "But what about you? Anyone you’re dreading the eventual loss of?"
    s "Wow, what a fun conversation topic you’ve chosen."
    maki "Hey, we’ve got a few hours to kill. We might as well get all of the dark stuff out of the way now so we can get back to talking about the {i}real{/i} main topic today — dildo delivery."
    s "Main topic aside..."
    s "I guess there {i}is{/i} someone."
    maki "Mother? Father? Sister? Brother?"
    s "None of the above."
    s "It’s kind of complicated, really."
    maki "Are you going to tell me? Or am I going to have to keep naming potential relationships you may have in hopes of getting it right?"
    s "You can name as many “potential relationships” as you want, but the unfortunate truth is that I have no idea what I'd even {i}call{/i} a relationship like this."

    scene makivisits13
    with dissolve

    maki "Wow. That {i}does{/i} sound complicated."
    s "Even that doesn’t really begin to describe it. I guess I see your point, though. Not having to worry about that anymore does sound like it would be a load off of my back."
    s "I’m just...okay with carrying that load for now, I guess."

    scene makivisits14
    with dissolve

    maki "Yeah...if that were an option for me, I would have done the same without even giving it a second thought."
    maki "It’s kind of crazy how much my life has changed recently despite it having been me and- uhh, {i}Makoto and me{/i} on our own for over three years now."
    maki "Knowing that Masahiro is dead completely changes everything even when we’ve been “alone” all this time."
    maki "So now I’ve...just got a {i}new{/i} load to carry, I guess."
    s "..."
    maki "Heh. Load."
    s "Comparing single parenthood to semen seems low for even you, Maki."
    maki "Come on, man. Laughs are going to be few and far between for me from now on. You’ve gotta let me have moments like that."
    s "I’m sure you’ll laugh just as much as you always do. There just might be some...melancholy mixed in with everything now."
    maki "Maybe you’re right..."
    maki "Maybe I’m just worried right now that things are going to permanently change because of how different and horrible everything feels all of a sudden."
    maki "But before that, there were {i}other{/i} worries. And if this one fades as well, I’m sure even more will take its place."
    maki "Isn’t it weird, Sensei?"
    maki "How your worries become amplified the moment you’re all someone has left?"
    s "Yeah...the girl giving your daughter “therapy” right now intentionally reinforces that idea nearly every single day for me."
    maki "You should be glad she does. For it’s that exact sort of thing that will keep us alive longer since we’re no longer living for just ourselves."

    "A moment of silence passes."
    "Then, a set of unexpected words bent into the shape of an anecdote — pouring from the mouth of a woman who laughs at dick jokes — makes me realize just who she is beneath her skin."
    "It’s someone far more beautiful than I could have ever imagined."

    maki "You want to know the weirdest change that’s come from all of this?..."
    maki "There’s a one way road not far from the shop that I have to cross to get to the local corner store."
    maki "Before my husband died, I’d only look to the left when crossing since that’s where all of the cars come from."

    scene makivisits15
    with dissolve

    maki "But now...I look to the right as well."
    maki "Just to be sure."

    scene black
    with dissolve2

    "Maki and I remain at the table for another couple hours until Makoto and Ami emerge from the bedroom."
    "Both of their eyes are red from crying."
    "But for a brief moment, a slight smile spreads across Makoto’s face."
    "When I look toward Maki to see if she notices, I catch a glimpse of a thin layer of fluid beginning to form over her eyes."
    "I get lost somewhere between aquamarine and turquoise."
    "But I find myself just in time to watch her ruffle her daughter’s hair as the two of them leave my home."

    s "..."
    a "They’ll be okay, Sensei..."
    a "Just like us..."

    stop music fadeout 10.0

    "I follow suit and ruffle Ami’s hair as well."
    "And then I manage to get to sleep without my mind wandering off the deep end once more."

    $ renpy.end_replay()
    $ makiinv3 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"

    jump advancetomon

label makihornyquestintro:
    scene nightsky
    with dissolve2
    play music "citylife.mp3"

    "It’s a hot summer night — the stars are shining, the moon is bright, and I have a raging erection that only copious amounts of pornography will be able to quell."
    "That said, you can probably guess where I am headed."
    "Dorm 10."
    "I kid, I kid. Though, who I kid, I’m not quite sure."
    "Regardless, I begin to make my way over to the porn shop in hopes that Maki is working tonight- seeing as Makoto, despite having sex with me almost constantly, still won’t sell me anything."
    "I’m not sure if she’s just the type who doesn’t want her {i}in{/i}significant other consuming such content or if she’s just secretly worried I’ll start liking grown women if I watch too much of it, but..."
    "Either way, jokes on her because I like {i}all{/i} women and I will prove that tonight by buying all of the porn I can fit into one basket."

    scene girlspornshop1
    with dissolve2

    "Or multiple baskets as there are several sets of arms here who will be able to increase my carrying capacity without much trouble at all."

    s "Alright, everyone grab a basket. It’s boner time."
    maki "It’s always boner time at Bukkake Maki’s. "
    maki "That’s not our official slogan. Or even the name of the store. But it’s the truth and I’ll be damned if I let a penis walk out of here all flaccid and stuff."
    h "Ooookay, ignoring everything Maki just said, hey."
    sar "I was just about to leave, so I can’t tell if your timing is great or totally horrible."
    s "Sorry, Sara. I have no interest in whatever you’re proposing. I am here for porn and porn only."

    if sarasex == True:
        sar "Not even if I’m proposing a crazy foursome with me and my two best friends?"
        s "I may have some interest in whatever you’re proposing. But I’m hard-pressed to believe there’s any truth to that statement."
        sar "Hey, you never know!"

    else:
        sar "You’ve had no interest in anything I’ve proposed ever, so I’m somehow not surprised."
        sar "And if it sounds like I’m offended by that, it’s because I am."

    scene girlspornshop2
    with dissolve

    sar "But what I really meant by that is you showed up at the perfect time to get invited to a thing I’m not able to tag along for anymore."
    h "You really can’t come? Can’t Sana or Yuki hold down the bar for a night?"
    sar "If this were last year, I don’t think that’d be a problem. But with the way things have been lately, I’m not sure if it would be a great idea to push all of {i}my{/i} responsibilities onto them."
    maki "Look at you being a reliable business owner. After a long wait, it seems like the Kumon-mi Women’s Business Association is finally made up of successful entrepreneurs!"

    scene girlspornshop3
    with dissolve

    h "We have an association?"
    maki "No, but we should because it would make us sound more important and Makoto would be more inclined to take over the business when I die and ascend to that big orgy in the sky."
    s "You know, that might be the best take on the afterlife I’ve heard yet."
    s "But again, disregarding Maki's dialogue, what are you talking about? What’s this thing Sara can’t attend and why am I suddenly invited?"

    scene girlspornshop4
    with dissolve

    sar "I’ll let them field this one. I just swang by to grab some batteries for my Official DildoSaber and have to get back to the bar before my break ends."
    s "I’m both happy to hear that item is selling and gravely disappointed to hear that you have purchased one."
    sar "Don’t knock it ‘til you try it, Sensei. "

    scene black
    with dissolve

    sar "I’ll see you guys later! And sorry for not being able to come! I’ll make it next time, I promise!"

    "Sara exits the store and, still confused about whatever is going on, I turn to Maki and Haruka for guidance."

    scene girlspornshop5
    with dissolve

    maki "You know, I should really start telling people those batteries are rechargeable. I feel kind of bad selling so many replacement parts all the time."

    "Guidance is not received and my trust in Maki lessens."

    h "Are you cool with Sensei tagging along? Or should we just try and postpone this for some other time?"

    scene girlspornshop6
    with dissolve

    maki "Why does what I want matter? You’re the one paying for all of this. I’m just coming along for the ride."
    s "Can someone please tell me what I’m suddenly being included in? Because I’m all about being included in stuff, I just normally like to know {i}what.{/i}"

    scene girlspornshop7
    with dissolve

    h "I bought three tickets to some tropical resort thing as a...token of my appreciation for Maki’s friendship. "
    maki "What she really means is she feels bad for me because my husband is dead as fuck and she wants to help me take my mind off of that. Amongst other things."
    h "And also that, but I’d probably...word it a lot more sensitively."
    s "And...now I get to come along and help Maki not care as much about her dead husband?"
    maki "Pretty much, yeah."

    scene girlspornshop8
    with dissolve

    h "What? No."
    maki "Sorry, no. I don’t really know what’s going on anymore."
    h "Maki, you totally know what’s going on. You haven’t been yourself lately. Just let me do this one thing to try and pick you up, okay? "
    s "You haven’t been yourself? But you’ve seemed mostly fine ever since Makoto started coming back to school."
    maki "I have been. "
    maki "Well, except for one little thing."
    s "And that thing is?"

    scene girlspornshop9
    with dissolve

    h "She’s not horny anymore."
    s "What?"
    maki "It's dryer than a desert down there. "
    s "That’s not “one little thing.” That’s like 90%% of your personality."

    scene girlspornshop10
    with dissolve

    maki "That just means I need a new thing now! Like, what if I get really into golf? Or NASCAR? Or those little rubber bands you put around your wrist that turn into shapes when you take them off?"
    h "Those stopped being trendy ages ago. Just humor me and come on this trip. I’m like, 99%% sure this whole no-horny thing is from stress and you need to relax."
    s "Question, was Sara aware this was a journey to recover Maki’s libido? Because, if so, you guys are an even stranger group of friends than I initially thought."

    scene girlspornshop11
    with dissolve

    h "I mean...it’s more than just a “quest for the horny.” I’m not even sure Sara fully knows what’s going on with Maki’s {i}libido.{/i} Like I said, the main thing is just getting her to relax a bit."
    h "Combine that with how I’ve been a shitty friend and...voila. Free tropical resort trip where a bunch of cougars can go silently ogle at younger fit guys and girls."
    maki "Mostly girls because all of the men are dying in space. Like-"

    scene girlspornshop12
    with dissolve

    h "Yes, Maki! We know your fucking husband is dead!"
    maki "He is?! Oh my God!"

    scene girlspornshop13
    with dissolve

    h "On second thought, I hope you stay unhorny forever."
    maki "Thank you for the free vacation, Haruka. "
    s "Yes. Thank you for the free vacation, Haruka."

    if makisex == True and harukasex == True:
        s "But you could have avoided all of this if you had just called me. Making women horny is kind of my thing. I’m way better at that than Sara is."
        s "Well...maybe. I feel like half of the people I know are also attracted to girls, so..."

        scene girlspornshop14
        with dissolve

        h "Is no one listening to me when I say this is a stress thing?! "
        maki "{i}Someone’s{/i} confident today."
        s "Am I wrong? I’ve made you horny plenty of times in the past."
        maki "But the past isn’t the present. It’s the future’s yesterday."

        scene girlspornshop15
        with dissolve

        h "Thanks, Jaden. Tell your dad I loved him in {i}I Am Legend.{/i}"
        s "I...might just be misremembering...but I could have sworn that after your husband died, we still-"
        maki "I can’t really remember either. But I was probably faking it if we did. This might hurt to hear, but women do that."
        s "...All of them?"

        scene girlspornshop16
        with dissolve

        maki "All of them except Haruka. All it takes to make her cum is a seat on the bus and a large pothole."
        maki "Heh. Hole."
        s "Well, I’m glad to see your sense of humor is still intact."
        h "{i}Yeah. Same.{/i}"
        s "Regardless, I’m still pretty confident I can turn Maki on. A vacation really isn’t necessary."

        scene girlspornshop17
        with dissolve

        maki "But I want shaved ice! And a massage from a small woman with strong hands who doesn’t speak my language!"
        h "If you’re so confident, why don’t you give it a shot?"
        s "What, like...right here?"
        h "Or the back room. Doesn’t make a difference. I’m telling you right now it won’t work. I’ve already tried."
        s "How?"
        h "That is between Maki and me."

        scene girlspornshop18
        with dissolve

        maki "And also the Official DildoSaber."
        h "..."
        s "..."
        maki "..."

        scene black
        with dissolve2

        s "You know what? I’ll prove once and for all that no sci-fi themed sex toy can compete with my real, human penis."
        h "Wow, inspiring. "
        maki "Do we have to do this right now? I’m tired and I have leftovers upstairs."
        s "My pride is on the line here, so yes."
        h "Sensei, I’m telling you now, it’s not going to work."
        s "Yeah, well...we’ll see about that."

        jump makihornyquestintrop2

    else:
        s "Question, though- what happens if this trip isn’t enough to get Maki back to her normal self? What if she’s just never horny again?"

        scene girlspornshop19
        with dissolve

        maki "I’d probably just go out of business after a while."
        maki "I can bullshit people for now since I’m a good salesperson, but I can only do something I’m not passionate about for so long before I just...give up."
        h "You can’t give up. You run the only sex shop in town. The women of Kumon-mi need you."

        scene girlspornshop20
        with dissolve

        maki "Alas...it seems we’ll just have to find someone else to take care of them."

        scene girlspornshop21
        with dissolve

        maki "..."
        h "..."
        s "..."
        s "So, when is this vacation thing?"

        scene black
        with dissolve2

        h "Ugh...not soon enough."
        maki "Haru, you said those tickets are only good for Saturdays, right?"
        h "Hm? Oh, yeah. That’s why Sara can’t get off. We just need to make sure we’re there by noon or they won’t let us in."
        maki "I guess just call Haruka whenever you’re ready, then. The sooner the better, though. I know I can’t stay like this forever."

        "After the conversation about Maki’s libido (Or lack thereof) wears off, I make good on an earlier promise to myself and fill up a basket of assorted pornography, carefully selecting things I think Maki might like."
        "But I’m surprised to see she barely even looks at what I lay out on the counter."
        "There are no comments on how much she loves gangbangs or how much certain AV stars can fit in their mouths..."
        "It’s just-"
        "It’s like she doesn’t even care."
        "And it’s, strangely, one of the most depressing things I have encountered in this very depressing life."

        $ renpy.end_replay()
        $ maki_love += 1
        $ haruka_love += 1
        $ makihornyquestintro = True
        $ harukaresortticket = True
        stop music fadeout 7.0

        "{i}Maki’s affection has increased to [maki_love]!{/i}"
        "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label makihornyquestintrop2:
    "After quickly throwing all of the porn I can get my hands on into a basket and spending way too much money on it, I swallow what little pride I still have and push my way into the back room."
    "I begin to remove my clothes, but the spontaneity of this combined with how pressured I suddenly feel does not do me any favors in the penis department."
    "It’s very sad to say this, but the erection I entered the building with has now dwindled to...yeah."
    "Basically, it’s not looking good for me."
    "Which means, by extension, it’s not looking good for Maki either."
    "At this rate, the only person who is going to win is Haruka, and that’s counterproductive to all of us as she basically always wins at everything when you really think about it."
    "She even managed to win by having her husband sent to space because now she gets habitually fucked by a guy with a much bigger and better dick (AKA: Me)."

    scene girlspornshop22
    with dissolve2

    "But that’s not important right now."
    "What’s important right now is helping Maki remember who she is-"
    "And there is no better tool for that than my penis."

    maki "..."
    h "..."
    s "..."
    maki "Hmm..."
    s "..."
    h "Well, it works on me."
    s "Thanks."
    h "Why is it soft, though?"
    s "Because this is extremely weird and uncomfortable and I’m kind of already regretting it."
    maki "Excellent length. Nice girth. Clean. Circumcised. Even soft, you’ve gotta admit, that’s an excellent cock."
    h "Oh, okay. There it goes."
    s "It’ll get there, don’t worry. Just give it a few minutes."

    scene girlspornshop23
    with fade

    h "Are you really not feeling anything? Because the old Maki would be creaming her pants over this spontaneous CFNM scenario."
    maki "Hmm...I can’t quite tell."
    maki "It’s true that I respect and appreciate the situation unfolding before us...but all I can see is the foundation of an excellent film and not something that I want to personally immerse myself in."
    maki "That being said, I must regretfully acknowledge that I am still, depressingly, not aroused."

    scene girlspornshop24
    with dissolve

    h "Great job, Maki. Now it’s starting to get soft again."
    maki "You know...this is quite peculiar. Not being turned on by porn is one thing, but to see such a perfect cock in the flesh and {i}still{/i} feel nothing?..."
    h "Aaaand up we go."
    maki "This is quite the predicament, Agent Hamasaki. What's unfolding before us is something unlike anything I've ever experienced before..."
    maki "It's imperative we get to the bottom of this immediately."
    h "Why are you starting to sound like you’re in some kind of film noir?"

    scene girlspornshop25
    with dissolve

    maki "{i}It had been a long time since a cock like this crossed my desk. But I could tell from the moment he walked into my office that this man wasn’t like the rest.{/i}"
    maki "{i}No...This man had been through Hell and back — chewed up by the streets of Kumon-mi and spat back out onto the curb like he wasn’t even good enough to swallow.{/i}"
    maki "{i}Heh. Swallow.{/i}"
    h "Maki, snap out of it and be horny again."

    scene girlspornshop26
    with dissolve

    maki "It ain’t that easy, you see. I can’t just “get horny,” you see. There’s more to it than that, you see."
    h "Oh I’m seeing something alright."
    maki "When life hands you lemons, there’s not much you can do but squeeze ‘em and hope the juice doesn’t wind up in your eyes- or the sores on your hands from workin’ em to the bone."
    maki "Means there’s only one thing you can do. You gotta go with the flow. You gotta take that first step, look ‘em in the eye and say “You’re messin’ with the wrong gal, punk.”"
    h "Maki, what are you even saying right now?"
    maki "What I’m sayin’ is I think you’ve gotta suck it, kid."
    h "Uh-huh. Right."

    scene girlspornshop27
    with dissolve

    h "Wait, like...literally?"
    maki "Cases like this ain’t solved by just sittin’ around. You’ve gotta act if you wanna make a change. You’ve gotta look that cock in the eye and say, “You’re messin’ with the wrong gal, cock.”"
    h "Uhhhh..."
    s "You heard her, Haruka. Come over here and make your friend horny or whatever is going on right now."

    scene black
    with dissolve

    h "Yeah, easy for you to say! You’re getting something out of this and you don’t even have to give anything back in return."

    scene girlspornshop28
    with dissolve

    s "Oh, come on. We both know you love this."
    h "I’d love it more if it wasn’t part of some cheap 1950’s movie Maki was playing out in her head."
    maki "{i}I couldn’t believe what I was hearing. Even Haruka Hamasaki, my best friend for over ten years, didn’t believe in me. And if she didn’t believe in me, who would?{/i}"

    scene girlspornshop29
    with dissolve

    h "You realize you’re saying all of that out loud, r-"

    scene girlspornshop30
    with hpunch

    h "Mmgrglrlgpphmmhmlh!"

    scene girlspornshop31
    with dissolve

    maki "{i}As I looked down at the woman I used to call my friend, I could tell she’s played this game before. But for how long? And with who? And why here of all places?{/i}"
    maki "{i}Could it be that she only came in the first place to throw me off her trail? Is this what they talk about when they mention “hiding in plain sight?”{/i}"
    maki "{i}I didn’t know. And the only way for me to find out was to get a little closer.{/i}"

    scene girlspornshop32
    with dissolve

    maki "{i}As I knelt down beside her, those cherry red cheeks infected me with a feeling I couldn’t quite describe. I knew that this was the stuff dreams were made of. I knew that-{/i}"

    scene girlspornshop33
    with dissolve

    maki "Ahh, fuck it. I’m still not feeling anything. Just stop."
    s "Stop? Why stop? I didn’t say stop."
    h "Drrrlllyhvtstp?...Hdnnntcmmmyttt."
    maki "You can keep going if you want, but I’m not going to be the one to clean the cum off of the floor. I’m just gonna go eat my leftovers."

    scene black
    with dissolve

    h "{i}...pah.{/i} Wait, Maki."
    s "What? Seriously? We’re done? Just like that? That was the shortest sex scene ever."

    scene girlspornshop34
    with dissolve

    maki "Sorry to disappoint you, I think I’m just broken or something."

    scene girlspornshop35
    with dissolve

    h "You’re not {i}broken,{/i} Maki. You’re just, and I’m probably going to sound like a broken record here, {i}stressed.{/i} You need to do something to relieve the tension."
    s "Like having sex with me. Let’s go."

    scene girlspornshop36
    with dissolve

    maki "I just don’t feel like it."
    h "Stop making this about you."
    s "Wow, treat Maki to {i}one{/i} vacation and suddenly you’re not self-centered anymore. Real cool, Haruka."
    h "Shut up or I won’t let you finish."
    s "Too late. I’m already soft again."

    scene girlspornshop37
    with dissolve

    h "Wait, already? What is going on with you today?"
    maki "Guys, it’s been fun and all, but I’m going to close up the store and head upstairs."

    scene girlspornshop38
    with dissolve

    h "Oh, come on! Maki!"

    scene black
    with dissolve

    h "Wait up! At least let me help you count the register!"
    s "Uhh, hello? I’m here too. You guys can’t just leave me like this."
    h "Just watch one of the eight million DVDs you bought. That’s why you came here in the first place isn’t it?"

    "As I glance over to the bag of porn I dragged into the room with me, I remember who my real friends are."
    "And I remind myself that {i}they{/i} will never betray me as I unceremoniously jerk myself off into Maki’s sink."

    play sound "phonebeep.wav"

    "The moment I exit the store, my phone goes off. And I make the mistake of tricking myself into believing it will be Haruka asking me to return and fuck the horny back into Maki or something."
    "Unfortunately, it’s just this:"

    h "{i}Heeeeeey. Sorry for abandoning you :x I wanted to keep going.{/i}"
    h "{i}Those tickets I got are good for any Saturday, so just call me whenever you want to go.{/i}"
    h "{i}Also, did you cum in the sink? Because it looks like somebody came in the sink.{/i}"

    "In the end, I won."
    "But it was not an admirable victory."

    $ renpy.end_replay()
    $ maki_love += 1
    $ haruka_love += 1
    $ makihornyquestintro = True
    $ harukaresortticket = True
    $ makiblock = True
    stop music fadeout 7.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label makihornytrip2:
    if _in_replay:
        play music "summerwind.mp3"

    scene sky
    with dissolve2

    "And so our mostly unremarkable stay at a relatively remarkable resort begins."
    "Maki and Haruka keep their eyes closed for the meantime as electing to do the opposite would alert them to my awesome existence and probably excite them too much to properly relax."

    scene noonsky
    with dissolve2

    "But when the sun begins to set, they realize they can’t live without me and I’m included once more."
    "But only for a short while as they then hurry off the women’s only section while I am left on my own in the rightfully uncrowded one belonging to the men."
    "Overall, the trip is extremely relaxing — but not in the way I expected it to be as I’ve been just...by myself for the vast majority of it."
    "There are both good and bad sides to that."
    "The good side is that I’m all alone and I can think about whatever I want without anyone bothering me."
    "The bad side is that I’m all alone and I can think about whatever I want without anyone bothering me."
    "As such, this relaxation is surrounded by the putrid, rotting aura of never knowing what I am supposed to do or say without something or someone to guide me."
    "I wish Ami were here to help. She’d know what to do."

    scene nightsky
    with dissolve2

    "But she is not. And she doesn’t."
    "And as I wander back to the common area in search of the two women I came here with, I’m surprised to see that they’re looking for me as well."
    "Unfortunately, I missed our dinner reservation. And even more unfortunately, I’m not sure what happened to all of the time between the morning and now as it all seems to have just slipped away."
    "Just like being alone, there are good and bad sides to that."
    "The good side is that I wasn’t able to hurt anyone in my absentminded daze."
    "The bad side is that one more day has slipped away without anything happening at all."
    "That kind of thing happens far too often...and the only thing preventing me from dwelling on it is the fact that my days are endless. "
    "And the only thing I have to worry about is coming one step closer to losing something else I care about in a far more torturous way."

    if harukasex == True and makisex == True:
        jump harumakihornytrip
    else:
        stop music fadeout 10.0
        $ renpy.end_replay()
        $ harumakihornyskip = True
        jump makihornytrip3

label harumakihornytrip:
    scene makipegsherhomie1
    with dissolve2

    "When we make it back to the room, it’s already pretty late."
    "Most of the other resort-goers (or whatever the better name for them is) filter into their rooms alongside us, likely fulfilled and rejuvenated from a day of rest and relaxation, but things seem different for Maki."
    "It seems that, despite her and Haruka taking their time and {i}not{/i} focusing on my penis, she’s still a little on-edge. Or at least more than I’m accustomed to seeing from her."
    "It’s not like she’s {i}worried{/i} or {i}upset{/i} or anything, but...something seems wrong."
    "And my thoughts on that don’t change after hearing what she has to say next."

    maki "Guys, what if I just never want to have sex again? How crazy would that be? "
    s "You can always {i}fake it{/i} apparently. "
    maki "Yeah, but where’s the fun in that? "
    maki "You know what? Screw my earlier approach. Taking it easy isn’t doing anything. Let’s get this motherfucking ball rolling. Hit me with your best shot."
    h "Yeah, the further we got into the day, the less confident I was in the whole “stress” thing being the cause. I think you might just genuinely be broken."
    s "If something is broken, tools are normally required to fix it. And thankfully for you, I brought my {i}toolbox.{/i}"
    maki "Is the toolbox your penis?"

    scene makipegsherhomie2
    with dissolve

    s "{i}No.{/i}"
    h "Put that thing away. "

    if harukalust10 == False:
        s "Sorry. But after last time, I wasn’t taking any chances."
    else:
        s "Sorry. I just thought it might help."

    scene makipegsherhomie3
    with dissolve

    maki "Well, that might not have made me horny, but I’d be lying if I said I’m not very impressed by your...preparedness."
    s "You know me, always ready for anything. "
    h "Is this your idea of “hitting her with our best shot?” Because I’m pretty sure that was Maki openly challenging us to turn her on."
    s "There’s nothing that turns women on more than free labor. I learned that from all of the porn I bought the other night."
    h "I’m suddenly very upset with myself for knowing exactly which section you must have raided during your horny, porn-shop rampage."
    s "You mean the one where you sucked my dick on command? If anything, I think that should be the part you’re upset about. "
    h "Nuh-uh. That was Maki’s fault. I was just being a good friend and trying to help her out."
    s "Maki, do you actually want us to hit you with our best shot? Because I’m not sure if I have it in myself to try after you just watched me the other night. That was degrading."

    scene makipegsherhomie4
    with fade

    maki "It was, wasn’t it?!"
    s "Why do you seem so proud of that?"
    maki "Because degradation and humiliation are major fetishes for a lot of people! And tons of fun to watch! Just ask Haruka. She loves that sort of thing."
    h "Oh, okay. I guess we’re airing out our {i}interests{/i} now. Thanks for the heads up, Bukkake Maki."
    maki "Hey, if I’m ever going to go back to my old self, we might need to broach some serious subjects. And there’s nothing more serious than diving head first into one another’s fetishes!"

    scene makipegsherhomie5
    with dissolve

    s "Lupus is more serious than that."
    h "Yeah, I’m sure that will rile her up. Nice job, Sensei. We might as well just pack it up now."
    s "Hey, with Maki, you never know. She’s probably seen so much of every single fetish by now that she might {i}need{/i} something like that to get her excited."
    h "Oh, that’s it! Maki, maybe you just need to try something new?"
    s "Is...there something she {i}hasn’t{/i} tried yet?"
    maki "There are a few things. I’m not sure if trying something new is the key here, though. The whole problem is that I just don’t {i}want{/i} to have sex. It’s not like I’m bored of it or something."
    h "Are you suuuuuure? Because there’s plenty of stuff the three of us could figure out."
    s "Yeah, I’m down for anything. Just name it."
    maki "Anything? So you’ll let me peg you?"

    scene makipegsherhomie6
    with fade

    s "Uh-"
    h "Pfft!"
    h "This, I have to see...That sounds hilarious."

    scene makipegsherhomie7
    with dissolve

    s "Haruka...I’m not {i}normally{/i} a violent person."
    s "But that can always change."
    h "Hahaha! You did this to yourself! Never say {i}anything{/i} to Maki! She’ll jump on any chance she gets to pitch, horny or not!"
    maki "She’s right, you know. It’s not often that opportunity presents itself. "
    maki "It’s like when somebody offers you a really fancy chocolate even if you’re not hungry. You’re taking that damn chocolate anyway and you know it."

    scene makipegsherhomie8
    with dissolve

    s "Yeah, sure. Just one of those scenarios involves delicious food and the other involves excruciating pain and extreme discomfort."
    maki "Hey, I know my way around a strap-on, pal. I’ll make it comfortable for you."

    scene makipegsherhomie9
    with fade

    s "Absolutely not."
    maki "Not even a {i}little{/i} bit? Not even the tip?"
    h "The tip doesn’t count, Sensei. We went over this earlier."
    s "The tip absolutely counts and you are not putting anything inside of me at any point."
    maki "Not even if this will cure my dry spell?"
    s "To be totally honest, I’d rather you stay abstinent forever. This is the one thing I will not budge on."
    maki "Pleeeeeeease?"
    h "Yeah, pleeeeeeease? "
    s "Why are you taking her side? You're my friend too and you should be protecting my body."
    h "Uhh, obviously because I want to see this! You never know, man! You might like it!"
    h "At this rate, this might be the only chance we get for the rest of her lives to turn Maki on! If she wants to strap on a dick and fuck somebody, we need to let her!"
    h "Sacrifice your ass for the greater good! It’s the only way!"

    scene makipegsherhomie5
    with dissolve

    s "If Maki wants to be the “pitcher,” you’re catching. I’ll be the referee. "
    h "Baseball doesn’t have referees. They have umpires, idiot."
    s "Thanks, Haruka. I’ll make sure to etch that into my mind when I am going to sleep later on with my anal virginity still intact. "
    h "Ughhhhh guys are such losers sometimes. Explore a little! Let Maki fuck you!"
    s "She can have sex with me the normal way if she wants. If not, I say we sacrifice {i}your{/i} body for the greater good. "
    h "But Maki wants to fuck {i}you!{/i} It’s no fun if it’s-"
    maki "No, it’s still fun. Plus, it’s a great workout and doable even if I’m not in the mood!"
    maki "I’m down to take a trip to pound-town with Haruka. It’ll be a nice way to thank her for treating us to this vacation."
    h "Wait, what? "
    s "I am also down to take a trip to pound town with Haruka."
    maki "No. You watch. "
    s "Wait, what?"
    maki "You didn’t let me peg you, so you’re not allowed to participate. I pitch, Haruka catches, and you’re the referee."
    h "Baseball doesn’t have referees! They have-"

    play sound "static.mp3"
    scene makipegsherhomie10 with flash
    stop sound

    h "AaAAaaAaaaAAaahHHHhhhh! How did we even get to this point?!?!?"
    maki "You know exactly how we got here, you little slut! Now shut up and take that dick! You know you love it!"
    h "These sex scenes...keep coming out of nowhere!! I have feelings too, you guys!!"
    s "Am I seriously just going to watch? I can’t participate at all?"
    maki "You’re lucky I let you jerk off and didn’t make you sit in the corner. Just enjoy the show. And don’t be afraid to compliment me on my {i}technique.{/i}"
    s "Honestly, you do look pretty good at this and it’s making me feel weird about myself."
    maki "Should we ask her who’s better?"
    s "I’m...afraid of what the answer will be, so no."
    h "Hahh! Hah! Oh...fuck! Oh, fuck that’s good!"
    maki "Yeah? Tell me how fucking good it is, you unfaithful whore. Tell me how much better I am than your man."
    h "So much! So much better! I’m going...fucking insane!"
    maki "You’re not gonna cum already, are you? Were you really that desperate to get fucked? You couldn’t wait one day?"
    h "N...N...Noooo! I’m a filthy whore! I’m a...cheating piece of shit! I just...love cock so much! I can’t help it!"
    s "Maki, can I at least get behind you and-"
    maki "Lay a finger on me and I’ll rip it off, you impotent, limp-dicked motherfucker."
    s "Friendly reminder that I don’t like being degraded the way Haruka does."

    scene makipegsherhomie11
    with dissolve

    maki "Really? Not even a little?"
    maki "Come to think of it, what {i}are{/i} your fetishes anyway? Because sometimes it feels like the most intense thing you’re into is consensual sex in the missionary position."
    h "Is this...really the...time to...have a conversation?!?!"
    s "I think Haruka wants you to pay a little more attention to her."
    maki "And I think {i}you{/i} just don’t want to tell me what you’re into. You can’t avoid it forever, though. Sooner or later, I’m going to pick up on what you like."
    s "Yeah...I really hope it doesn’t come to that."
    h "M...Maki!...You’re...slowing down!"

    scene makipegsherhomie12
    with dissolve

    maki "God, you’re such an attention-craving bitch. Isn’t this supposed to be about {i}me?{/i}"
    h "Hah...hah...hah...you...later...me...now..."
    s "And...me {i}when?{/i}"
    maki "Oh for the love of fucking Christ, just take the other end if you can’t follow directions."

    scene makipegsherhomie13
    with dissolve

    h "Mmph??!?!!!?!"
    s "Thank you. I won’t forget this."
    maki "Thank me when we’re not double-teaming the local barista. That takes precedence right now."
    s "Are you really not into this at all?"
    maki "Hm? I thought it was pretty apparent how “into this” I am. I’m having a blast. And seeing how hot Haruka is getting over it is really fun too."
    s "Yeah, but...are you like, {i}turned on{/i} yet? Or are you just going along with it like it’s some sort of game?"
    maki "My nipples are a little hard, I guess. But that’s probably just because the AC is cranked up. I’m definitely not wet, if that’s what you’re asking. Which it can be. You don’t need to be obtuse about it."
    s "So if I were to try and fuck you right now, would you really “rip it off?”"
    maki "No, but good luck trying to get Haruka off your dick when she’s so in the zone."
    maki "Honestly, fucking me right now probably wouldn’t feel as good as her mouth anyway. I can’t get into it and Haruka would just wind up being the one to suffer since it would impede my thrusting ability."
    h "Mmm! Mm! Mmfhhrllrlrl!"

    scene makipegsherhomie14
    with dissolve

    maki "Ahh, yes. Spoken like a true whore."
    s "Maybe you should see a doctor or something? It’s probably some kind of mental-"
    maki "I know exactly what it is, but now is definitely not the time to bring it up since it’ll only make things worse."
    s "That’s fine, but-"
    maki "I’ll tell you later, okay? Let’s just take care of Haruka for now. She both deserves it and is doing an {i}excellent{/i} job of not passing out from the immense pleasure brought on by Kumon-mi’s best tag-team."
    s "You know, it’s only been a couple minutes, but I’m fine with that title and am happy to be a part of this team with you."

    scene makipegsherhomie15
    with dissolve

    maki "Same. But show {i}her{/i} that, not me."
    maki "Drown this wannabe hotwife in your cum since that’s basically the {i}one{/i} thing you can do that {i}I{/i} can’t right now."
    s "There are...other things too."
    maki "Like?"
    s "..."
    maki "..."
    h "Mm! Mm! Mm!"
    s "There’s no way you’re better at that than me."

    scene makipegsherhomie16
    with dissolve

    maki "Just shut up and cum."

    with sexfade
    with sexfade
    scene makipegsherhomie17
    with cumflash
    with hpunch

    h "MMMGLLGMLGMLLGMMGLLGLL!!!!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene makipegsherhomie18
    with dissolve2

    h "Haaaaaaaaaaaaaaaahhhh.............."
    maki "All in a day’s work."
    s "Today shall be known as the first ever victory for Kumon-mi’s greatest tag-team."

    scene makipegsherhomie19
    with fade

    maki "You sure you don’t want to give it a go? It’s all lubed up for you already."
    s "I’ve never been more certain of anything in my life."
    maki "Haruka was right earlier, you know. You might actually like it if you give it a try."
    s "What part of “more certain of anything in my life” do you not understand?"
    maki "The part where I know I’m out of time if you refuse..."
    maki "And that we’ll have to have another awkward conversation about me not knowing how to be a mom."
    s "Wait, so this is-"

    scene black
    with dissolve2

    maki "Put your clothes back on. I’ll tell you outside."

    "........."
    "......"
    "..."

    scene makipegsherhomie20
    with dissolve2

    h "Hah....."
    h "Ahh........."
    h "........."
    h "Guys?..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    $ renpy.end_replay()
    $ makihornytrip2 = True
    $ maki_love += 1
    $ haruka_love += 1
    $ haruka_lust += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
    "........."
    "......"
    "..."

    jump makihornytrip3

label makihornytrip3:
    if harukasex == False or makisex == False:
        scene black
        with dissolve2

        "The next few hours go by so quickly it’s like they never happened in the first place."
        "And, you know...maybe they didn’t."
        "But as I step back outside to get on with the rest of the night, I imagine a world in which they did."
        "And then I think about how many people I’d need to hurt in order to get there."
        "........."
        "......"

    scene clearnightsky
    with dissolve2

    "As I mentioned in the very beginning, there was no way this trip was going to end without some semblance of seriousness. And with the sun merely hours away from rising, it appears I can no longer avoid that."
    "The two of us move through a maze of white beach chairs and brightly colored umbrellas to an opening halfway between pools number four and five."
    "I didn’t understand how they were numbered earlier, but it didn’t take very long to figure out once I had a little more time to focus on them."
    "It’s like that for most things, I find."
    "Everything is confusing at first — from the way the body works to the manner in which moonlight can reflect off of nearly everything it touches. "
    "Granted, both of those things would likely still confuse me if you were to sit down and carefully explain them, but what I’m trying to say is there will {i}always{/i} be aspects of life that just don’t click for us."
    "For me, the most glaring issue of all is figuring out a way to circumvent how I really feel and properly disguise myself as a good person."
    "For Maki, the problem is much simpler."
    "She just doesn’t give herself enough credit."
    "And if I had to take a guess, it would be that this has something to do with that as well."

    scene makiclearnight1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Or...maybe I’m wrong."
    "That’s not the look of someone who’s battling depressing inner-turmoil or...questioning the methods they’ve used to navigate through mazes far more complex than ones full of chairs and parasols."
    "To be honest, I don’t really {i}know{/i} what that look is."
    "And for someone who spends so much time deciding how people feel before they’re able to tell me, that’s a little surprising."
    "Again, it’s only a matter of hours until the sun begins to rise — and that’s not enough time to learn everything there is to know about Maki."
    "But it’s enough to figure out whatever it is that infiltrated her mind and planted itself within her most identifiable quality. "
    "I just don’t like watching her rot from the inside out, and if there is something I can do to stop it-  "

    maki "Have you noticed anything different about Makoto lately?"
    s "..."

    "I might have to just look the other way."

    s "Something tells me we've been here before."
    maki "Something tells me you're right."
    s "Maki, I’m not really sure I should be getting any further involved in anything that goes on between you and Makoto. It never really goes the way we want it to."
    maki "Not even if it’s good this time? "
    s "What do you mean?"
    maki "I’m talking about how she’s been pretty great lately. She’s not sulking or sleeping in or anything like that. She seems to be genuinely enjoying herself."

    "Or at least doing an exceptional job of pretending to."

    s "If...that’s what you’re talking about, then yes. I have noticed. I can’t imagine that’s what you called me out here to talk about, though."

    scene makiclearnight2
    with dissolve

    maki "It is and it isn’t."
    maki "It’s no secret that I may have sidelined my own feelings when my husband died so Makoto wouldn’t be {i}completely{/i} without a parental figure, but..."
    maki "Now that she’s fine...I don’t know. Maybe all those feelings I didn’t have time to {i}feel{/i} are catching up to me or something. There’s a lot going on, but none of it is really {i}bad.{/i}"
    maki "I’m just confused, I guess. About where to go from here and who I’m supposed to be and what I’m supposed to feel or...do."
    s "So...are you saying stress or...grief or something really {i}is{/i} what’s making you all...non-Maki?"
    maki "It’s definitely not helping, I’ll tell you that much."

    scene clearnightsky
    with dissolve2

    maki "Despite how it might seem basically all the time, I {i}am{/i} an adult at the end of the day. And I can figure out ways to deal with stress and all that other lame adult stuff. "
    maki "I’ve been stressed {i}plenty{/i} of times in my life, and it’s never had this effect on me before. But..."
    maki "There’s been something bothering me lately. Something that I’ve {i}never{/i} had to deal with. And, despite all of the experience in the world, I have no idea what to do about it."
    s "And that is...somehow centered around Makoto’s happiness?"

    scene makiclearnight3
    with dissolve2

    maki "I know it probably sounds weird, but...{i}yeah.{/i}"
    maki "She’s never been {i}this{/i} happy before. And the timing of it all is just really confusing to me since her dad hasn’t even been gone all that long."
    maki "Like, I’m not hoping she goes back to being miserable. I’m over the moon that she can get out of bed on her own now. I just think there’s...something else to this."
    maki "I know her well enough to understand that there’s no way this level of glee would ever come naturally. And so...I think there’s something {i}else{/i} that’s making her happy."
    s "Why not just accept whatever that is, then? There’s no need to bash your head against the wall trying to figure it out when you should just be happy {i}for{/i} her."
    maki "What I’m saying is I think she’s having sex. "
    s "..."
    maki "At the very least, she probably has a boyfriend or something. But the weirdest part of all of it is that I, Maki Miyamura, the sex queen of the city-"
    maki "Have absolutely no idea how to talk to her about it..."
    maki "It’s crazy, isn’t it? You’d think that if {i}anyone{/i} could talk to their daughter about this, it would be me. I even had a dry run during that Dorm Wars thingy."
    maki "I’ve been preparing for it for...basically {i}forever{/i} since I knew this day would come."
    maki "But now that it’s here...I’m lost. I have no idea what to say to her. I feel totally useless in my very own area of expertise. "
    maki "Now, any time I think about sex at all, I just start thinking about her. And I’m sure I don’t have to tell you why that hasn’t really been working out for me."
    s "..."
    maki "..."
    maki "You want to weigh in on this at all or should I just keep ranting? Because you should at least be {i}slightly{/i} invested in this as her teacher."
    s "Why...do you think she’s having sex?"
    maki "Well, between the constant excitement, her better attitude toward me, {i}and the huge box of condoms I found in her room,{/i} I’ve just got a pretty good idea. Call it mother’s intuition. "
    s "I see..."
    maki "I had no idea she even knew any boys. Like, where would she even find one? "
    s "I have no idea, Maki..."

    scene makiclearnight4
    with fade

    maki "Do you get why I’ve been weird lately, now? Or does this still sound all sorts of ridiculous to you? Because it sounds kind of ridiculous to {i}me{/i} and I’m smack-dab in the middle of it."
    s "I...don’t really know how it sounds. And I probably shouldn’t be weighing in on this."

    scene makiclearnight5
    with dissolve

    maki "That’s it, then? You’re just going to blue ball me in the advice department {i}again{/i} because it makes you uncomfortable? How the hell do you think {i}I{/i} feel? This is my teenage daughter we’re talking about."
    s "Makoto’s smart. You probably don’t need to talk to her about anything if you don’t want to."
    maki "Makoto is smart, yes. But she’s also a {i}child.{/i} And for all we know, there could be some older dude who swooped in to take advantage of her in a time of weakness or something."
    maki "That stuff doesn’t just happen in porn, you know. It happens in real life every single day and, most of the time, we have no idea until it’s already too late."

    "What I want to say is that continuing to not do anything is the exact way things become “too late” in the first place..."
    "But I obviously can’t — because {i}I’m{/i} the man she’s talking about. "
    "{i}I’m{/i} the man preying upon her daughter in a time of weakness. "
    "{i}I’m{/i} the man leveraging his position and {i}her{/i} affinity for male authority figures for my own personal gain- and the fact that Makoto is magically {i}happy{/i} now doesn’t absolve me of that."
    "This couldn’t stay hidden forever. Maki was destined to find out the moment she was forced into a more active role in Makoto’s life."
    "But what does that mean for me?"
    "Do I have to {i}stop{/i} now? "
    "Do I have to give up on something and {i}someone{/i} I’ve grown so attached to just because her mother is worried?"
    "Can the two of us remain the way we are with Maki indefinitely stuck trying to peer through the brush? Is such a thing possible?"
    "Should I just come clean?"
    "No. Fuck no. Of course not. I’m lucky she doesn’t seem to suspect me in the first place."
    "What should I do? "
    "What am I supposed to do?"
    "How can I get out of this?"
    "How can I bring myself to care about Maki’s issues when I’m so consumed by my own?"
    "Now, {i}I{/i} am the one rotting from the inside out. How am I supposed to circumvent {i}this?{/i}"

    maki "Sensei?..."
    s "Call me Akira."

    scene makiclearnight6
    with dissolve

    maki "Akira?..."

    "The answer to my last rhetorical question is the same one I provided just a few short moments ago."
    "I can get around this by disguising myself as someone better."
    "I’ll remain disgusting inside of my head- and apply a fresh coat of paint so that those who don’t spend too much time with me mistake me for someone special."
    "Right now, what I need to do is connect. If I can connect, I can both bring Maki over to my side {i}and{/i} start easing her out of these ridiculous worries of hers."
    "Makoto is smart. "
    "It’s just like I said. "
    "She’s smart and she can make her own decisions. "
    "If she wants a thick, adult cock inside of her, she should be allowed to have one. It’s no different from the ones they sell in the store, right?"
    "It’s not wrong just because it’s attached to {i}me,{/i} right? I’m better. I’m getting better. I’m not the same person I was when I started doing this. It’s different now. "
    "It’s different now."

    scene makiclearnight7
    with dissolve

    maki "How about “Aki-kun” instead? I like that better."

    "It’s no different now."
    "I’m the same piece of shit I’ve always been."
    "And no amount of paint could ever hide that."

    s "That..."
    maki "What’s wrong? Too childish? You embarrassed?"
    s "Just...stick with Akira for now."

    scene makiclearnight8
    with dissolve

    maki "...Okay."
    maki "Don’t think I’ll let you off the hook just because you finally gave me your name, though. I still want to know what you think I should do. Like, what you {i}really{/i} think. Not what you think I want to hear."
    maki "What if this were Ami we were talking about? What would you say to {i}her{/i} if it started to be clear that she was involved with someone?"
    s "I...don’t think I have to worry about that."
    maki "I didn’t think I had to worry about it with Makoto for at least a couple more years, but here we are. Life just moves quicker than we want it to sometimes."
    maki "In fact, it’s so quick that whatever preparations we make along the way can wind up totally worthless once the ball really gets rolling."
    maki "I just want her to be safe. Like, safer than condoms — which I am very proud of her for, by the way. But I want her to be so safe that she just doesn’t have sex ever. That would be cool. No sex means no talk."
    s "Just have the fucking talk, Maki. It’s better than walking on eggshells every time the subject comes up — which I imagine it does pretty frequently since the two of you work at a porn shop."

    scene makiclearnight9
    with dissolve

    maki "But what if she takes it the wrong way? I’m finally on her good side and I don’t want it to seem like I’m overbearing or...anything like that."
    s "Well, what’s more important to you? Making sure your daughter is safe or making sure she likes you?"

    scene makiclearnight10
    with dissolve

    maki "Obviously the first one. I know that. But that doesn’t make it any easier."
    s "It’s not supposed to be easy. This is what you signed up for when you carried her around inside of you for nine months."

    scene makiclearnight11
    with dissolve

    maki "It was actually ten. That girl did {i}not{/i} want to come out."
    s "That is information I did not need or want. "
    maki "You’re welcome."
    s "Listen, can we head back in now? I’ve exhausted all I have to say about this and if Makoto finds out I was talking to her mom about her sex life, she’s going to stop helping me out after school."
    maki "“Helping you out after school?” You think I haven’t heard that before? Don’t tell me {i}you’re{/i} the one Makoto’s sleeping with, are you?"
    s "Maki-"

    scene makiclearnight12
    with dissolve

    maki "Relax, Aki...ra. I’m obviously joking. "

    if makisex == True:
        maki "You’re already boning me. Well, when I’m not in desert-mode at least. And you’d be a real idiot to think you can get away with boning my daughter as well."
        maki "Especially since she’s only-"
        s "Yeah, I know. You don’t need to remind me."

        scene makiclearnight13
        with dissolve

        maki "No...but it doesn’t hurt."
        s "..."
        maki "..."
        maki "Can, uhh..."
        maki "Can I ask you a personal question? One that {i}doesn’t{/i} really have to do with Makoto?"
        s "Please, yes. I’ve been trying to move on from that topic since it came up."
        maki "Then..."
        maki "You don’t have to answer this if you don’t want to, but...do you think you’ll ever look for something a little more {i}serious?{/i} Romantically, I mean."
        s "Are you...interested in me like that?"
        maki "My husband literally just died. "
        s "That’s exactly why I asked. Because if you’re trying to get me to commit to a relationship right now-"
        maki "I just...want to know. That’s all. "
        maki "I like what we have now. But I’d also like knowing if this is all it will ever be or..."
        maki "If there will ever be room to grow."
        s "..."
        maki "I think we...work kind of well together. And stuff. Whether it be as friends or fuck-buddies or...whatever. "
        maki "It’d just be a little comforting knowing you’re not going anywhere. That’s all."
        maki "I don’t really have anyone else anymore."
        s "..."
        maki "..."

        scene black
        with dissolve2

        s "Ask me again when Makoto’s out of high school."
        maki "But if we wait that long, you might start liking her instead! I only have so many years of youthful beauty left!"
        s "I’m going back to the room now, Maki."
        maki "Ah! Wait, no! You can’t leave without me! You have the key! "

    else:
        scene black
        with dissolve2

        s "Well, it wasn’t a very good joke...and I’d appreciate it if you didn’t suggest things like that anymore."
        maki "No wonder you didn’t want to sleep with me. You already have the younger model."
        s "I’m just going to walk away now."
        maki "Ah, wait up! I need you to let me back into the room. I didn’t bring my key."
        s "You should have thought of that before messing with me."
        maki "Akiraaaaaa!"

    "The two of us make our way back to the room, but I’m slowed down along the way by the weight of a gigantic pit in my stomach."
    "As Maki climbs into bed with Haruka and I spread out a futon, that pit expands in size- planting itself into the lining of my organs and sprouting what I can only imagine as the ugliest flowers to ever bloom."
    "As I sleep tonight, I will think of all of the wrong I’ve done. "
    "My sins will go on to create the longest highlight reel one could imagine and I will watch with bated breath as every single unfortunate segment sinks its nails into my irises."
    "And I will do this because there will always be certain aspects of life that just don’t click for us."
    "For me, the most glaring issue is letting go and accepting just how weak I really am."
    "And for Maki, it’s trusting the wrong people."
    "She should have never let me into her home."
    "And I know that she’ll regret it one day..."
    "Because, if she doesn’t-"
    "This was all for nothing."
    "..."
    "I go to sleep."
    "And I pause the highlight reel in a room with a deep pink glow."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makihornytrip3 = True
    $ harukaresortticket = False
    stop music fadeout 10.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    jump makihornytrip4

label makicamp1:
    scene nightsky
    with dissolve2
    play music "ame.mp3"

    "There’s a phrase I heard recently that made me stop and think for a little while."
    "It isn’t a new one, and this isn’t me saying it’s the first time I’ve heard it, but it {i}is{/i} the first time that I’ve ever tried to seriously make sense of it, for it’s something I can’t seem to wrap my head around."
    "{i}Love is in the air.{/i}"
    "First and foremost, I applaud the creator of this phrase for framing love in a way that makes it sound like an airborne virus as that’s something I can actually relate to and agree with."
    "But what I don’t get is why everyone looks at this like a {i}good{/i} thing."
    "No one is ever excited to catch a cold. And public opinion when it comes to the flu is even worse. "
    "So why is {i}this{/i} virus one that we all seem so determined to host? The air we breathe should remain clean at all times, should it not?"
    "The existence of {i}anything{/i} swimming or flying or living in the air is a terrifying concept, and it calls into question why more people don’t wear masks outside of the more popular pandemics."
    "Maybe I should start doing that."
    "Maybe covering my face would prevent me from falling for anyone who accidentally contaminates the air in the midst of some lukewarm debate on wires or the concept of breathing."
    "Because even if I don’t believe it’s love, my broken mind can’t help but display the symptoms of it."
    "It’s the same for everyone else who breathes on me and winds up getting tricked by the failure of their immune system into some state that makes their legs shake."
    "We’re all just sick."
    "So when I hear someone say that “love is in the air,” I can’t help but feel a little worried."
    "I can’t help but be a little scared — because there’s no way I can live without breathing, and I’m too cowardly to die at such a slow pace."
    "I can hold my breath as much as I want."
    "I can hide inside my home and hope the cracks beneath my doors suffice at keeping fresh air out."
    "But the rotting carcasses of those I’ve left behind are simply far too pungent now, and even masks and doors won’t keep their stench away from this cursed respiratory system. "

    scene black
    with dissolve2

    "I try to calm my nerves."
    "It never works."
    "There is only one thing that will."

    scene makiwantstocamp1
    with dissolve2

    s "Okay, give me the hardest shit you’ve got."

    scene makiwantstocamp2
    with dissolve

    maki "Go to the back room and take your pants off. I’ll be there with the lube in five. And I promise it’ll only hurt for the first ten minutes."
    h "Tough day?"
    s "Every day is tough when you’ve lost the will to live."
    maki "That’s where the pegging comes in. Why are you still here when you should be preparing your anus?"
    s "That’s not- forget it. I’ll just fill a basket with anything I can find and hope that something works."

    scene makiwantstocamp3
    with dissolve

    maki "Is {i}your{/i} libido broken this time? Because Haruka is a self-proclaimed master when it comes to helping others re-find the horny. And maybe it’s your turn to be fixed instead of mine?"
    h "I’m not looking to {i}fix{/i} anybody right now. I’m just glad to see you’re still alive and well."
    s "I am not well at all, Haruka."
    h "Well hey, alive and {i}unwell{/i} beats dead, doesn’t it?"
    s "I don’t know. I’d say you could ask Maki’s husband, but I’m not sure you’d get a response."

    scene makiwantstocamp4
    with dissolve

    maki "Nice."
    h "Ignoring the fact that I’m apparently the only one here without a morbid sense of humor, are you sure porn is the remedy to your missing will to live?"
    s "There can be no remedy at this point, only distractions. So I will drown my sorrows in my own cum while my niece eats microwaved TV dinners and cries her eyes out a few walls over."

    scene makiwantstocamp5
    with dissolve

    maki "That one was too real for me to laugh at. Sorry, Sensei."
    h "Go home and get some sleep, man. Because, as much as I want Maki’s shop to succeed, I feel like {i}someone{/i} has to put their foot down right now and she’s way too much of a salesman to ever do that."
    s "I can only sleep so many hours, you know. What am I supposed to do with the rest of the day?"

    scene makiwantstocamp6
    with dissolve

    maki "I mean...you {i}could{/i} just hang out with us as we’re both adults who have also endured hardship and wouldn’t judge you at any point for what you’re going through."
    h "She’s got a point, Sensei. And it’s kind of surprising that you haven’t really tried leaning on either of us {i}at all{/i} during this extremely prolonged and sudden bout of sadness that no one understands but you."
    maki "And hey, now that I’m a widow, you can even marry me if you want to take advantage of my health benefits and go seek out actual therapy instead or something."
    s "At the very least, that’d be the funniest way to cancel out the un-submitted marriage license your daughter has been holding over my head for months."
    h "The what?"
    maki "Did...Makoto trick you into signing a marriage license? Because she did something like that with me when she was little as well and I wouldn’t put it past her."

    scene makiwantstocamp7
    with dissolve

    h "Your...daughter made you fill out a marriage license?"
    maki "No, it was a recommendation letter for Harvard. She just asked to see my signature and then printed a whole ass form on top of it."
    maki "Joke's on her, though. Harvard doesn’t give a shit what some mid-thirties porn dealer has to say. I don’t even know where Harvard {i}is.{/i}"
    s "Nowhere you have to worry about her actually going to so long as we’re all trapped in here. But, that’s enough about Makoto. Give me everything you’ve got."

    scene makiwantstocamp8
    with dissolve

    maki "Are you robbing me now? Do I need to go get my rifle?"
    s "You mean the horse dildo?"
    maki "Rifle. Horse cock. Same difference."
    s "I’m not robbing you. I’m just starting to feel normal by standing here and talking to you two and would like to crawl back into my hole and stop existing now."

    scene makiwantstocamp9
    with dissolve

    maki "Heh. Hole."
    h "Is that why you never came to either of us? You {i}want{/i} to feel miserable?"
    s "Don’t you do the same thing when you’re upset?"
    maki "No, Haruka just calls upon everyone else for validation and attention until whatever’s causing her sadness goes away."
    h "Yeah. I never {i}want{/i} to be sad. I just want people to feel bad for me. So, if that’s what you’re doing now-"
    s "That’s not what I’m doing. I just don’t really know how to exist right now and it feels like everything I {i}try{/i} to do makes things worse. So stasis seems like the only option."
    h "What about Ami, though?"

    scene makiwantstocamp10
    with dissolve

    maki "Yeah, what’s going on with her? Makoto said something about...organ harvesting recently?"

    if harukasex == True:
        h "That sounds about right."

    s "Ami...isn’t doing so great."
    maki "“Not great” as in refusing to eat and keeping herself locked in her room for days on end like Makoto did when Masahiro died? Or “not great” as in Haruka complaining about being lonely?"
    s "Neither, really. She’s awake and conscious and replies to me when I speak to her, but she’s not leaving the house and seems just...completely dead inside. "
    s "She’s been under a lot of mental stress lately and I’m pretty sure she’s blaming herself for the way {i}I{/i} am. Which, on its own, would be one thing-"
    s "But when combined with the fact that she’s {i}already{/i} all sorts of fucked up from being raised by {i}me,{/i} it makes things kind of snowball into some big clusterfuck that I don’t know what to do about."
    maki "That just sounds like parenting, to be honest."
    s "Yeah, that’s the problem. I don’t know how to be a {i}parent.{/i}"

    scene makiwantstocamp11
    with dissolve

    maki "You and me both, buddy."
    h "Have you tried asking Sara? She’s all about parenting stuff. Even if she occasionally medicates her teenage daughter with exorbitant amounts of alcohol."
    s "I haven’t. The only person I’ve really asked for help isn’t a parent either."
    h "Well, it’s no wonder why you’re still struggling then. Just talk to Sara. I’m sure she’ll have some idea of what to do to get Ami back to normal. And if she doesn’t-"

    scene makiwantstocamp12
    with dissolve

    maki "Go camping with us tomorrow."
    s "That is...a strange alternative to what Haruka just said."

    scene makiwantstocamp13
    with dissolve

    h "Come to think of it, that’s actually a great idea."
    maki "Right? It’ll be just like the “Make Maki Horny Again” trip, but fractionally more depressing."
    s "And...how is camping going to make me a better parent, exactly? It’s not going to turn into some type of boot camp, is it?"

    scene makiwantstocamp14
    with dissolve

    maki "Not at all. A few of us girls were just looking to unwind and, since the weather’s been great lately, we figured we’d head out into the woods and try not to be eaten by bears."
    h "So what Maki’s suggesting is that you and Ami come along and try not to be eaten by bears too."
    maki "Yeah! We can all avoid being eaten by bears together! Plus, Sara will be there and she might be able to help with the Ami situation."
    s "Sure. Except for the part where “the Ami situation” involves her not wanting to leave her room. There’s no way I can talk her into going {i}camping.{/i} She’ll look at me like I’m insane."
    maki "How can you be so sure? For all you know, Ami might have been {i}waiting{/i} for you to do something like this for years. "
    h "No harm in trying, right?"
    maki "Unless you don’t want to come, that is."
    h "Or you’re just afraid of bears."

    "Camping?..."
    "I can’t say that’s...something {i}I{/i} have much interest in, to tell you the truth. And I can’t imagine Ami would either given that she’s a girly-girl in practically every sense."
    "But..."
    "Maybe this {i}would{/i} be an opportunity to turn things around? For {i}her.{/i}"
    "My happiness comes second- and I’m not just saying that because I’ve all but abandoned it."
    "If Ami can find some semblance of normalcy in her life again...even if that normalcy comes in the form of something that wouldn’t be normal {i}at all{/i} for us..."
    "Maybe it would make pretending to be okay a little easier on my end?"

    maki "Well?"

    "And maybe it would make her less afraid to open the door."

    s "I’ll...talk to her tonight."

    scene makiwantstocamp15
    with dissolve

    maki "My parental genius knows no bounds! So long as it involves other people’s children and not my own."
    h "You think she’ll be okay with a bunch of women your age also being there?"
    s "Not even slightly."
    h "Yeah, I didn’t think so."
    s "Like you said, though, there’s no harm in trying. And it’s a somewhat passive way for me to start ascending the steps to parenthood."

    scene black
    with dissolve2

    maki "That settles it, then! Sensei and Ami will come camping with us tomorrow!"
    s "She hasn’t agreed yet, Maki..."
    maki "But she will! "
    h "Maybe."
    maki "Good enough for me! We’ll pick you up at 9:00. "
    s "But-"
    h "Just talk to her when you get home and give Maki a call when you find out."
    h "Worse comes to worst and she still drops by in the morning despite Ami not wanting to go, I can just restrain her and prevent her from honking."
    maki "But I love honking the horn and I never get to do it! Don’t take this from me, Haruka!"

    "I take it upon myself to sneak away as the two of them argue."
    "But, just when I think I’m safe, I wind up bumping into something else..."

    scene makiwantstocamp16
    with dissolve2

    mak "..."
    s "..."
    mak "Hi..."
    s "Hey..."
    mak "How...are things?"
    s "Oh, you know..."
    s "Terrible."

    scene makiwantstocamp17
    with dissolve

    mak "I see..."
    mak "Do you think they’ll maybe...{i}stop{/i} being terrible soon?"
    s "Probably not, to be honest..."
    mak "I see..."
    s "..."

    scene makiwantstocamp18
    with dissolve

    mak "Sensei, I-"
    s "Are you going camping tomorrow?"

    scene makiwantstocamp19
    with dissolve

    mak "What?"
    s "Camping...with your mom. Are you going?"
    mak "Are...are {i}you{/i} going?"
    s "I don’t know yet. Probably not."
    mak "Uh..."
    s "I’m trying to be a parent."

    scene makiwantstocamp20
    with dissolve

    mak "A parent?"
    s "Yeah."
    mak "That’s...different."
    s "Yeah. Everything’s different now. And none of it’s really good."
    mak "I figured as much on account of you not even showing up to the dorms anymore. And to think that all it took was something worse than the apocalypse in your eyes."
    s "I guess this means you’re a true member of the club now, huh?"

    scene makiwantstocamp21
    with dissolve

    mak "Yeah, I guess so. I’m not really sure what to do, though. Nothing I say about it sticks with anyone other than Ayane."
    s "Help her out, okay?"

    scene makiwantstocamp20
    with dissolve

    mak "Help her?"
    s "Yeah. With how fucked I am right now, you’re kind of the only person she has to talk to about any of this since I just...don’t want to be bothered for the time being."
    mak "And you think I do?"
    s "No. But I know you’re enough of a teacher’s pet to do what I tell you."

    scene makiwantstocamp22
    with dissolve

    mak "You’re not even my teacher anymore."
    s "I’ll always be your teacher and you know that."
    mak "..."
    s "Makoto, I’m really sorry. I’ve got a lot of shit I have to figure out right now."
    mak "You’ve had a lot of shit to figure out since the first time you walked into the classroom. The difference is that now you finally {i}have{/i} to figure it out or we’ll all leave you behind."
    s "Maybe that’s for the best."
    mak "It’s not."

    scene makiwantstocamp23
    with dissolve

    mak "At least not for me. But new Makoto doesn’t have time to care about what anyone else wants as she’s too busy playing the game for the first time in her life."
    s "Still have that marriage license?"

    scene makiwantstocamp24
    with dissolve

    mak "Mhm. And no, you can’t have it."
    s "That’s fine. "
    mak "Is it?"
    s "Yeah, hang on to it. It might come in handy one day."

    scene makiwantstocamp25
    with dissolve

    mak "It might-"
    s "If I need health benefits or something."
    mak "Health...benefits?"

    scene black
    with dissolve2

    s "Are you coming camping tomorrow or not?"
    mak "Camping...right! I..."
    mak "I can’t..."
    mak "But maybe some other time-"
    s "Yeah. Maybe some other time."
    mak "Are you leaving? Already?..."
    s "I’ll call you. "
    mak "Will you actually?..."
    s "We’ll see."
    s "Only one way to find out."

    stop music fadeout 10.0

    $ renpy.end_replay()
    $ makicamp1 = True
    $ maki_love += 1
    $ haruka_love += 1
    $ makoto_love += 1

    jump amicamp1

label makicamp2:
    scene makiactualfish1
    with dissolve2
    play music "fallishere.mp3"

    "After making my way back to the campground, I find Maki sitting beside a lake that looks more like a large puddle in a rare moment of somewhat quiet contemplation for her."
    "And the only reason it’s {i}somewhat{/i} and not {i}genuinely{/i} quiet contemplation is the fact that I can hear Haruka chatting up Sara and Ami inside of their tent not that far from here. "
    "But, not wanting to intrude (And also being given the rare opportunity to hang out with Maki in an area where she can not immediately reach for a plastic horse penis), I can’t help but indulge and make my way over."
    "She notices me immediately and gazes back with eyes that scream both “I have no idea what I’m doing” and “I’m glad you came over because I was bored as hell.”"

    maki "Hey! I’m glad you came over because I was bored as hell. And also, I have no idea what I’m doing."

    "Cool. I guess I know her better than I thought."

    s "Why bother fishing if you have no idea what you’re doing?"

    scene makiactualfish2
    with dissolve

    maki "Thought I’d try learning. But apparently, this isn’t something you can just sit down and do. But hey, not much else is going on right now. So maybe this will bring me {i}closer to nature{/i} or something like that."
    s "I didn’t take you as the type of woman who’d want to be closer to nature in any capacity."
    maki "And I didn’t take you as the type of man who’d go out of his way to bring his niece camping just because he thought it might make her happy."

    scene makiactualfish1
    with dissolve

    maki "But I’m glad that you are. "
    maki "It’ll make packing up all of our gear a lot easier tomorrow morning."
    s "Is there an extra chair I could set up next to you?"
    maki "Ooooh, is it bondage time?"
    s "You know damn well that the word is “bonding.” "

    scene makiactualfish2
    with dissolve

    maki "I have no idea what you’re talking about. But yes, there are a few extra chairs in my trunk. You just might have to move a few things out of the way first. Only a handful of them bite, though."
    s "There are toys for all sorts of people nowadays, aren’t there?"
    maki "They’re the backbone keeping society propped up and I refuse to believe otherwise."

    scene black
    with dissolve2

    s "You know, I can’t say I disagree. But I feel like your thoughts on this matter are a lot more passionate than mine, so I’m just going to dig through your trunk now."
    maki "Jeez, Akira. At least lube yourself up first. That’s a sensitive spot and I’m a fragile young woman."

    "I ignore Maki’s somewhat flirtatious prodding for what I imagine is the millionth time in my life as I make my way over to her car."
    "........."
    "......"
    "..."

    scene makiactualfish3
    with dissolve2

    "I prop the chair up beside her and sink down into it, digging my heels into the grass to prevent it from slipping away and sending me face first into the water and then subsequently her hook."
    "She looks at me again and pauses for a moment, but I can’t discern what her gaze is saying this time. So I just look back at her. And I wonder if she’s trying to figure out what {i}my{/i} eyes are saying."
    "I get compliments on them a lot, but I’ve never understood why. And, more often than not, it leads me to believe that the words themselves are empty and only exist to curry favor with a potential mate."
    "There’s none of that here, though. We’re just two confused adults who happen to exist at the same time, fighting our own battles and pretending to be stronger than we actually are."
    "It’s the illusion that matters, after all. Because things are only real once you can see them. And if you can never see {i}pain,{/i} you can trick yourself into believing it doesn’t exist."
    "I know why Maki’s fishing."
    "And I can promise you that nature has nothing to do with it."

    maki "You know...you’re a good guy, Akira."

    "You’re only saying that because you still don’t know I’m screwing your daughter."
    "{b}i’m glad you said it because i was going to if you didn’t.{/b}"
    "Why not make me say it out loud then? That’s a thing you can do, isn’t it?"
    "{b}beep boop bop. too far out of service area. waiting for more bars. try back later.{/b}"
    "So I can get away from you if I just stay out here?"
    "{b}maybe. but then you’d run out of cumsluts and drown yourself in the river and i don’t know how to swim.{/b}"

    maki "Are you always this quiet after getting a compliment? Or are you still just trying to figure out how to respond?"
    s "Sorry. Just...thinking."

    scene makiactualfish4
    with dissolve

    maki "I get it. That’s kind of why I’m out here trying new things in the first place."
    maki "Masahiro liked fishing. He’d take Makoto out with him from time to time. "
    maki "Said it was his way of {i}calming down.{/i} But he was always pretty mild-mannered to begin with."
    maki "Guess you never really know what’s going through someone’s head, though. Like, for all I know, maybe he was miserable? Maybe he only needed to “calm down” because I was stressing him out?"
    s "I doubt that was it. You might be weird, but you don’t seem like a {i}stressful{/i} partner."

    scene makiactualfish5
    with dissolve

    maki "You’re probably right. Or at least that’s what I’ll keep telling myself since it’s not like I can really {i}ask{/i} anymore."

    scene makiactualfish4
    with dissolve

    maki "But even if he’s gone now, I still feel like I can {i}connect{/i} with him if I do things like this. So I guess it’s less about being “one with nature” and more about being “one with dead husband.”"
    s "That was actually really sweet up until the end."
    maki "Yeah, that made me sound kind of like a necrophiliac, didn’t it? "
    s "That’s most assuredly not where my mind went, but it’s a very {i}Maki{/i} way of interpreting it, so I guess I’m not surprised."
    maki "Do you think you’d ever bone a zombie if you were given the chance?"

    scene makiactualfish6
    with dissolve

    s "Is that really what we’re going to talk about? I was expecting more of a serious conversation after the way this talk started."
    maki "Can we not have a serious conversation about the ethics of having sex with a dead body?"
    s "I take it that means you would?"

    scene makiactualfish7
    with dissolve

    maki "I’m not sure, actually. Like, can zombies even get boners? Is it just {i}always{/i} hard because of the rigor mortis?"
    s "Maki, are you doing okay? Because I can leave you alone if you’re only doing this right now to connect with your husband. I wasn’t trying to interrupt that."

    scene makiactualfish8
    with dissolve

    maki "Thank you for that...but I’m fine. I’ll probably just stick to fishing in porn games and connect with Masahiro in other ways. Like eating his favorite foods or...recommending elderly porn to my customers."
    s "This is not a thing I ever needed to know or learn, so thanks for that."

    scene makiactualfish9
    with dissolve

    maki "Dead men tell no tales, so their widows must sing their glories instead. Even if their glories involve fishing and watching grandma take a massive dong up her cooter like she’s back in her twenties again."
    s "You miss him, don’t you?"

    scene makiactualfish10
    with dissolve

    maki "..."
    maki "Yeah."
    maki "But that’s not something I expect to ever go away. I mean...how {i}can{/i} it?"
    maki "Falling in love is, like...it’s something that changes a person. It’s not a thing you can just fall {i}out{/i} of once one side isn’t there anymore. "

    scene makiactualfish11
    with dissolve

    maki "That’s okay, though. I {i}want{/i} to keep those feelings because I really {i}did{/i} love that mild-mannered elder fucker. And- you know what, Akira? If he was a zombie, I’d still let him hit it."
    maki "I’m putting a lot of faith in rigor mortis right now though and I hope you know that."
    s "..."

    scene makiactualfish12
    with dissolve

    maki "Akira?..."
    s "Do you have, like...advice?"
    maki "For...for parenting, you mean? I thought that’s why Sara-"
    s "For moving on after losing someone you love."

    scene makiactualfish13
    with dissolve

    maki "..."
    s "I know we haven’t really, like...{i}talked{/i} ever since I started coming back to the shop. But that’s kind of what caused this whole shitty situation in the first place."
    s "And seeing you out here doing things like fishing just because your husband used to do it makes me want to try and kind of...take matters into my own hands as well."
    s "Like, Ami’s not the only person who I hope this trip helps out. But I’m so torn between wanting to feel better and thinking I don’t {i}deserve{/i} to that I have no way of knowing what to actually {i}do.{/i}"
    s "All I know is that everything I see reminds me of someone I can’t let go of. And I was wondering if you had any, like...advice on what I should be latching onto or not."
    maki "Do the others know?"
    s "Not yet. And I didn’t even plan on telling {i}you{/i} until a minute ago. I just can’t help but admire how...{i}resilient{/i} you are."

    scene makiactualfish14
    with dissolve

    maki "..."
    s "..."
    maki "There’s nothing I can say that will make you feel any better."
    s "Yeah...I figured as much."
    maki "It sucks, I know. And, just like with Makoto, I wish there was {i}something{/i} I can do. But if there’s anything I’ve unfortunately learned lately, it’s that moving past something like this entirely comes down to you."
    maki "No matter what you tell me, I’ll never understand the way you saw the person you’re referring to. Just like how you’ll never understand what I had with Masahiro."
    maki "All we can do is relate to one another and share in each other’s experience and...maybe that helps a little. But it pales in comparison to the pain that returns when all those precious memories start flooding in."

    scene makiactualfish15
    with dissolve

    maki "It’s going to hurt for the rest of your life. "
    maki "But there are {i}other{/i} things that can keep you grounded. "
    s "That’s probably why I’m putting so much of myself into Ami right now."

    scene makiactualfish16
    with dissolve

    maki "That is illegal in several ways, good sir."
    s "Maki, come on."
    maki "On or in? Because pulling out of Ami makes things a little more socially acceptable, but {i}still.{/i} Not a smart move, man."
    s "Just...forget I even said anything."

    scene makiactualfish17
    with dissolve

    maki "I’m just trying to lighten the mood, Akira. I know you and Ami don’t have {i}that{/i} kind of relationship."

    if amifingered == True:
        "Yeah. It’s much worse than you could probably imagine."

    maki "I understand exactly what you mean when you say you’re putting all of yourself into Ami because that’s exactly what I’m doing with Makoto. Just...in a way that’s very hands-off and doesn’t annoy her."
    maki "You think {i}your{/i} happiness will come from her, right? So you want {i}her{/i} to feel better because that will make {i}you{/i} feel like you’re doing something right."
    s "I guess you grasp the situation a lot better than you let on."
    maki "Because it’s the {i}same{/i} situation, Akira. We’re parents. {i}Both{/i} of us. Not just me."
    s "I don’t deserve to be called a parent."

    scene makiactualfish18
    with dissolve

    maki "And I {i}do?!{/i} I didn’t take up the mantle of “Mom” until my husband passed away. That’s why Makoto has such a hard time even {i}seeing{/i} me as a proper mother."
    maki "And...I have no clue who the person you’re talking about is, but maybe that’ll serve as yours and Ami’s prompt for sneaking a bit of normalcy back into your lives."
    s "I’m just...not sure if I can do it, Maki."
    maki "Doubting yourself is just part of the process, Akira. No one’s good at this right away. It’s scary having someone else’s life in your hands. {i}Especially{/i} when that person is smart."
    maki "And yeah, Ami might not be {i}Makoto{/i}-smart. But I’ve heard about what happened to her parents and I can almost assure you that sort of event would make her at least {i}emotionally{/i} mature."
    s "Yeah...I’m not so sure about that. "
    s "That’s not really a thing we ever talk about in our house."

    scene makiactualfish19
    with dissolve

    maki "Mm...so {i}that’s{/i} the way it is."
    maki "Sorry. I didn’t know."
    s "There’s nothing to apologize for. I just have to figure out a way to make this work on my own. Learning coping techniques from someone else who experienced something similar would have been way too easy."

    scene makiactualfish20
    with dissolve

    maki "Like I said, though...there are things out there that can keep you grounded. And Ami is the biggest one of all."

    if makisex == False:
        s "Yeah...you’re right."

        scene black
        with dissolve2
        stop music fadeout 25.0

        s "I need to get my shit together for her sake."
        s "I can’t be hurting right now as all that will do is make things even harder for her."
        maki "Exactly..."
        maki "But that doesn’t mean it’s okay to just give up on yourself either, okay?"
        s "..."
        maki "Do you understand what I’m saying here? It’s fine to prioritize her. You {i}should{/i} be prioritizing her. But you’re a human as well, Akira. And being upset is, like...the most human thing I can even think of."
        s "Yeah, I hear you."
        maki "So you agree that you’ll try and take care of yourself when you really need to?"
        s "I’ll see what I can do."
        maki "Akira-"
        s "I’ll talk to you later, Maki."
        maki "Hah..."
        maki "Okay."
        maki "I’ll be here if you need me."

        scene sky
        with dissolve2

        "I make my way back into a space between the trees..."
        "And I think of other ways to kill the time."

        $ renpy.end_replay()
        $ makiblock = False
        $ makicamp2 = True
        $ maki_love += 1

        "{i}Maki’s affection has increased to [maki_love]!{/i}"

        "Now what?"

        jump campmenu1

    else:
        scene makiactualfish21
        with fade

        maki "But..."
        maki "You know...I wouldn’t really mind being another one..."
        maki "If Ami’s not enough, I mean."
        maki "Which isn’t me saying that I think I should be even close to as important in your life as she is, just that I...well...you know..."
        maki "Like...you and me are...I kind of...well, like...uhh...how should I put this?"
        s "I don’t know, Maki. How {i}should{/i} you put it?"
        maki "Well, it’s...it’s kind of, like...like, it’s no secret that I see you a little differently than the rest of my friends."
        maki "And...while it’s not the same way I see Masahiro or...{i}saw{/i} Masahiro...it doesn’t mean you aren’t, like...it doesn’t mean that, uhh..."

        scene makiactualfish22
        with dissolve

        maki "It doesn’t mean that you...aren’t something I...don’t want to protect."
        s "That...was too many negatives in one sentence. I need a second to parse-"
        maki "It means you can lean on me because I like you. Okay? There. I said it."
        s "You didn’t have to say it, Maki. I already knew that."

        scene makiactualfish23
        with dissolve

        maki "Then you should have cut me off before I started stammering like that! I’m not good at sounding cute and this is what happens when I try!"
        s "I mean, ignoring how your inability to be cute is what {i}makes{/i} you cute, you shouldn’t feel pressured to say or do things like that."
        s "I know you’ll be there if I need you. And just talking to you today has already helped a lot. "

        scene makiactualfish24
        with dissolve

        s "Hell, this whole trip has helped a lot and we’ve still got almost a full day ahead of us. So thanks for that. And thanks for giving me the opportunity to...try and make things better."

        scene black
        with dissolve2

        s "I can’t promise to lean more on you in the future as...I’m not really in a position now to promise anyone {i}anything.{/i}"
        s "But you’re important to me as well. And I’m flattered you’d even consider accepting me after falling so hard for someone who fit you so much better."
        maki "And I’m flattered you’d consider accepting {i}me{/i} when I’ve had so many penises and penis-shaped objects inside of me that most would consider it a major turn off."
        s "And now the moment is ruined. "
        maki "Ruined? Or {i}better?{/i}"
        s "Ruined, Maki. Now there’s no way I can have a nice, emotional send off."
        maki "You can’t have a send off at all if I leave first! "
        s "Maki-"

        play sound "tackle.mp3"
        scene sky
        with hpunch
        stop music fadeout 15.0

        maki "Bye!"

        "Maki leaps out of her chair and sprints into the woods, but I’m able to catch a glimpse of how red her face is just before she vanishes into the trees."
        "And I think for a moment about why she’d look that way for me."
        "I think about how {i}my{/i} existence has subtly conned her into believing she could ever squeeze anything out of me that isn’t just semen — and I feel both shameful and regretful as a result of this."
        "I’m ashamed because I doubt I could ever love her."
        "But I’m regretful to have ever loved at all."
        "For life would be so much easier if she were the one I wanted the most."

        s "..."

        "Doubting that Maki will be returning any time soon, I head back to a place between the trees and think of what else to do before the sun sets."

        $ renpy.end_replay()
        $ makiblock = False
        $ makicamp2 = True
        $ maki_love += 1

        "{i}Maki’s affection has increased to [maki_love]!{/i}"
        "What now?"

        jump campmenu1

label makilust5:
    scene nightsky
    with dissolve2
    play music "citylife.mp3"

    "{i}Porn.{/i} "
    "It’s such a beautiful word."
    "Just not really. In fact, it’s kind of a horrible word. It’s harsh, ugly-sounding, and doesn’t properly convey how pivotal it is at keeping society functioning the way it should."
    "To be fair, though, there isn’t really {i}anything{/i} that keeps society functioning the way it should because the curiosity of humans is both their greatest strength and biggest curse."
    "But this isn’t the time to be talking about humans. This is the time to be talking about what humans do when they take their clothes off."
    "How, through some weird ritual or something like that, we found out that it feels good for us to combine our genitals and...wiggle them around until stuff comes out."
    "So good, in fact, that when video cameras were invented and we gained the capability to capture moments in time, those wiggly sex moments were some of the first we captured."

    scene makianal1
    with dissolve2

    "Which brings me to where I am today."

    s "Hey, Maki."
    maki "Hey there, old sport."

    scene black
    with dissolve

    s "Bye, Maki."
    maki "See you later, old sport."

    "And that’s the story of how porn was invented."

    scene makianal1
    with dissolve

    "Except for the fact that it’s not. And that Maki can basically call me whatever she wants and I’ll continue to come back because I’m one of like seven people who still actually {i}buys{/i} porn."

    maki "Welcome back to my humble abutt. "
    s "I believe the word is “abode.”"
    maki "Humble aboner."
    s "..."
    maki "Humble aboobies."
    s "It’s crazy to think that you’re a grown woman."

    scene makianal2
    with dissolve

    maki "That’s the same thing my mother used to say to me when I tried to teach her about spitroasting."
    s "..."

    scene makianal3
    with dissolve

    maki "Through video, of course. I may be an insatiable pervert, but I know better than to disparage my mother’s good name by hiring two men to spitroast her."
    s "I never really know with you. I figured you might think that would be a fun birthday present or something."

    scene makianal4
    with dissolve

    maki "Maybe. Though, some light grave robbery would need to be done first. And it might be tough finding two men willing to spitroast a skeleton."
    s "..."
    maki "There’s a joke to be made about boners here, but I can’t come up with a good one."
    s "You rarely do."

    scene makianal5
    with dissolve

    maki "Hmph! I guess it would be best if you just take your business elsewhere then."
    s "Okay. See you, Maki."

    scene makianal6
    with dissolve

    maki "Wait, no! I like money."
    s "Then please read my mind and direct me to whichever section carries the genre you have landed on."

    scene makianal3
    with dissolve

    maki "Remind me — how do you feel about watersports?"
    s "Bad."

    scene makianal7
    with dissolve

    maki "Ugh, great. Guess I’m going to Makoto’s swim meet alone then."
    s "Is that actually a thing that’s happening? Or is this just more mindless riffing?"

    scene makianal3
    with dissolve

    maki "What about mindless rimming?"
    s "..."
    maki "Go on. I’m listening."
    s "Maki, just tell me what to buy so I don’t have to use my brain."
    maki "Can you at least give me an {i}idea{/i} of what direction your boner is pointing in today? I’m a saleswoman, not a miracle worker."
    s "Uh...north?"

    scene makianal8
    with dissolve

    maki "Normal boners call for normal recommendations! To which I will suggest our newest release, Totally Anal Volume 19!"
    s "That doesn’t sound very normal to me."

    scene makianal3
    with dissolve

    maki "What doesn’t sound normal about it? Totally Anal’s a great series. There wouldn’t be nineteen of them if it wasn’t the case."
    s "The anal part."
    maki "Anal is normal as hell, you vanilla cupcake. Girls {i}and{/i} boys have been taking it up the ass since the dawn of time. It’s way more normal than like...I don’t know. Cell phones?"
    s "What?"

    scene makianal9
    with dissolve

    maki "Cell phones! Anesthesiology! Microwaves! All common parts of every day life despite being brand new in the face of Father Time! But {i}all{/i} of these are younger than anal sex, sir!"
    s "What kind of life do you lead where anesthesiology is such a common thing?"

    scene makianal3
    with dissolve

    maki "You know, selling porn is basically the same thing as anesthesiology when you think about how many people go right to bed after rubbing one out."
    s "..."
    maki "I’m right and you know it."
    s "Just recommend something normal, please."
    maki "Are you really that against anal?"
    s "It’s not that I’m {i}against{/i} it. I just...don’t know much about it?"
    maki "Do you..."
    maki "Do you want me to {i}teach{/i} you?"
    s "Not if your go-to method is hiring two dudes to come and show me firsthand."
    maki "That was for my {i}mom,{/i} old sport. {i}And{/i} it was rhetorical."

    scene makianal10
    with dissolve

    maki "I’ll teach you in the best way possible! With my body!"
    s "The store is {i}open{/i} right now, Maki."

    scene makianal3
    with dissolve

    maki "So, there are these things called “locks” and “closed signs...”"
    s "Okay, okay. I get it. "
    maki "No, {i}I{/i} get it. In the ass. From you and your man-penis. Unless you’re saying you {i}want{/i} to do it the other way around and-"
    s "Absolutely not. {i}You{/i} get it. I provide."

    scene makianal11
    with dissolve

    maki "Hell yes for consensual sex. Gimme some skin. "
    s "Like...a high five? Or penis skin?"
    maki "Gimme a penis five."
    s "..."
    maki "Let me slap your penis with my hand."
    s "Maki, I don’t know if I’m going to be able to get an erection at this rate."

    scene makianal12
    with dissolve

    maki "Then how about we make things a little more exciting by spicing stuff up?!"
    s "We already kind of {i}are,{/i} aren’t we?"
    maki "No, like with pet names! There’s gotta be something that’ll cause your Johnson to salute if you hear me cry it out, right?"
    s "I mean..."
    s "Now that you mention it..."

label makinaming:
    $ makimaster = renpy.input("Enter a name for Maki to call you...")
    $ makimaster = makimaster.strip()

    if makimaster.lower() in ["miku"]:
        s "Would you mind calling me Miku while I am having anal sex with you?"

        scene makianal13
        with dissolve

        maki "Hold on a second. Did she put you up to this? Is this all just one cleverly coordinated ruse? Because she’s been really fascinated by this lately and-"
        s "She didn’t put me up to it. I just really want to experience having anal sex with you while being called Miku."
        maki "I feel weird rejecting you when you’re being so formal and direct about it."
        s "Then agree."
        maki "Uhhhhh..."
        maki "{i}Okay?{/i}"
        s "I guess that settles it, then."

        jump endofmakinaming

    if makimaster.lower() in ["makoto"]:
        s "I kind of want you to call me Makoto."

        scene makianal14
        with dissolve

        maki "Akira — you might not know this about me, but I actually have a daughter named Makoto."
        s "Really?"
        maki "Yes. Which would make calling you her name during sex very uncomfortable for me."
        s "Oh. So it’s because you already call Makoto “Makoto” while you are having sex."
        maki "{i}Noooo.{/i} It’s because that is her {i}non-{/i}sex name. Do you understand?"
        s "No."
        maki "I call her Makoto while we are shopping. Or selling porn. Or watching television."
        s "Then what do you call her during sex?"

        scene makianal15
        with dissolve

        maki "Nothing!"
        s "So you’re just quiet? That sounds unlike you."
        maki "I don’t have sex with my daughter!"
        s "{i}Yet.{/i}"

        scene makianal13
        with dissolve

        maki "Can you just pick a new name please?"
        s "Ugh...fine."

        jump makinaming

    if makimaster.lower() in ["sara"]:
        s "Would you mind calling me Sara from now on?"

        scene makianal3
        with dissolve

        maki "Not really. But Sara might."
        s "Who is that again?"
        maki "Our friend. The petite one whose daughter likes her more than my daughter likes me and I’m only kind of jealous about."
        s "Maybe calling me her name during sex will help you cope with those jealous feelings you’re having."
        maki "Maybe. Or maybe I’ll just be thinking of her the whole time. Which, you know, probably won’t have much of an overall impact on my enjoyment or performance."
        s "So you’ll call me Sara from now on?"
        maki "I mean...I {i}guess?{/i}"
        s "That settles it, then."

        jump endofmakinaming

    if makimaster.lower() in ["haruka"]:
        s "I kind of want you to call me Haruka from now on."

        scene makianal3
        with dissolve

        maki "What am I supposed to call Haruka then?"
        s "Akira."
        maki "This could potentially make future threesomes very confusing. Especially since she hasn’t gotten the memo that you’ve taken her name."
        s "She can find out the hard way. "
        maki "I think that’s the way she likes it. Are you really sure that’s what you want to be called, though?"
        s "I’ve never been more sure of anything in my life."
        maki "That’s a little...concerning."
        s "It sure is, Melinda."
        maki "Wait, I don’t get to choose my own name? Why am I Melinda?"
        s "I don’t know, Melinda. "
        maki "Can I just be Maki again? I like Maki more."
        s "That sounds like something Melinda would say."
        maki "What would Maki say?"
        s "She’d call me Haruka and let me put it in her ass."
        maki "Oh. Okay, so we’re back on the right page then, Haruka."
        s "I guess that settles it, Mel- Maki."

        jump endofmakinaming

    if makimaster.lower() in ["maki"]:
        s "I would like you to call me Maki from now on."

        scene makianal4
        with dissolve

        maki "I feel like that name might already be taken by someone."
        s "I wouldn’t doubt it. It’s a great name."

        scene makianal3
        with dissolve

        maki "I can’t tell if you’re flirting right now or if you hit your head earlier today."
        s "It actually took a lot of courage to tell you that. I’ve been wanting you to call me Maki pretty much since I met you."
        maki "Well, why the hell did you wait so long to tell me? You missed your shot, not-Maki."
        s "Don’t call me that. Anything but that."
        maki "Old sport."
        s "Almost anything but that."
        maki "Come on, Akira. Pick something else."
        s "Ugh...fine."

        jump makinaming

    if makimaster.lower() in ["masahiro"]:
        s "Would you mind calling me Masahiro from now on?"

        scene makianal16
        with dissolve

        maki "I {i}knew{/i} you were into the zombie thing! You tried to deny it but I {i}knew!{/i}"
        s "I know that it’s the name of your dead husband who may or may not be a zombie now, but I really just like the name."

        scene makianal17
        with dissolve

        maki "Well, luckily for you, I have a lot of experience yelling it out during sex."
        s "Then you should adjust right away."
        maki "The problem isn’t so much {i}adjusting.{/i} It’s that I’d kind of like to keep that name tied to my husband for a few reasons."
        s "They better be good, woman."
        maki "The first is that I don’t want my memories of my husband to fade. "
        maki "And while I’m not saying that getting boned into oblivion by someone with the same name would {i}do{/i} that, it still feels weird taking away that special element of our past."
        s "That’s the first reason. What’s the next?"
        maki "The next is that I don’t want Makoto to have to deal with the most confusing several seconds of her life if she ever hears us getting down and dirty."
        s "{i}I do.{/i}"
        maki "Pick a different name, Akira."
        s "Ugh. I hate girls."

        jump makinaming

    if makimaster.lower() in ["selebus"]:
        s "I’d really appreciate it if you’d call me Selebus from now on."

        scene makianal18
        with dissolve

        maki "Hey, I know him! That’s the Lessons in Love guy!"
        s "The what?"
        maki "Lessons in Love! The hit dating sim with way too many words and way too few lizards!"
        s "But why would lizards-"
        maki "Did you know that Selebus posts an update almost every single month? And that Lessons in Love is the actual longest visual novel {i}ever{/i} by word count? Because I did! I’m a good egg!"
        s "Are there eggs in Lessons in Love too?"

        scene makianal7
        with dissolve

        maki "Don’t even get me started."
        s "I’m confused."

        scene makianal8
        with dissolve

        maki "{i}Everyone{/i} is confused when it comes to Lessons in Love, but that’s kind of the point! Maybe. I think? Probably."
        s "This sounds way too complicated for a soft boy like me who isn’t very good at reading. "
        maki "The charm lies {i}in{/i} its complication, Akira! The whole point is trying to uncover mysteries in a world actively trying to keep you from doing just that!"
        s "But what if I just want to yank my wiener and make the white stuff come out?"
        maki "Then you’re completely missing the point and probably never going to touch a real girl."
        s "But I’m like two minutes away from touching you."
        maki "Yes, but {i}I’m{/i} not real. I’m made of polygons and pixels. Just like you and just like everyone else you know."
        s "Uhhhhh..."

        play sound "broken.mp3"
        scene makianal19

        maki "{b}PICK A NEW NAMEEEEEEEEEEEEEEE{/b}"

        stop sound
        scene makianal1

        jump makinaming

    if makimaster.lower() in ["daddy", "dad", "father", "papa"]:
        s "Would you mind calling me [makimaster] from now on?"

        scene makianal7
        with dissolve

        maki "{i}Hah...{/i}"
        s "Is...something wrong?"
        maki "{i}Yes,{/i} something’s wrong! That’s like, the go-to name for everyone out there completely lacking in creativity! It’s so {i}boring!{/i}"
        s "I mean...is it really wrong to enjoy something just because everyone else does?"

        scene makianal14
        with dissolve

        maki "Yes."
        s "Oh."
        maki "Sex is like {i}music,{/i} Akira. {i}Everybody{/i} listens to Taylor Swift. And yeah. She’s fine. She’s talented. But you’re not unique or cool for listening to her."
        s "Who is Taylor Swift and why do you have such a problem with her?"

        scene makianal15
        with dissolve

        maki "I {i}don’t!{/i} Just like I don’t have a problem with white bread or brown sugar cinnamon Pop-tarts! But that’s exactly the thing!"
        maki "If you just keep doing what everyone else is doing, all you’re {i}really{/i} doing is following the beat of someone else’s drum! And that’s not what sex {i}or{/i} life is about!"
        maki "Get out there and experiment! Find what you {i}really{/i} love, not what you’re {i}programmed{/i} to love. Do you know what I mean?"
        s "I don’t think so. Are you going to call me [makimaster] or not?"

        scene makianal7
        with dissolve

        maki "Ugh..."
        maki "Yeah, I’ll do it."
        s "Nice. I guess that settles it, then."

        jump endofmakinaming

    if makimaster.lower() in ["old sport"]:
        s "Actually, can you just keep calling me “Old Sport” but, like...more seductively?"

        scene makianal3
        with dissolve

        maki "Oh, wow. You were actually into that? I could have sworn you thought it was annoying."
        s "What would have given you that idea?"
        maki "How you’ve vocally asked me to stop calling you that. And how you almost left today when I called you it after you walked in."
        s "I just couldn’t contain my erection and didn’t want to embarrass myself in front of you."
        maki "Don’t ever worry about embarrassing yourself in {i}front{/i} of me, [makimaster]. Embarrass yourself {i}inside{/i} of me. Accidental orgasms are hot in their own way."
        s "Ah..."

        with sexfade
        with sexfade
        scene makianal14 with cumflash
        with hpunch

        maki "..."
        s "..."
        maki "Did you just-"
        s "No."
        maki "[makimaster], it’s okay if you-"
        s "I didn’t."
        maki "..."
        s "It was a sneeze."
        maki "Do you need a minute to recover?"
        s "..."
        maki "..."
        s "No, I’m good now."
        maki "Atta boy, [makimaster]."
        s "Well...since you’re still calling me that...I guess that settles it?"

        jump endofmakinaming

    else:
        s "Would you mind calling me [makimaster] from now on?"

        scene makianal1
        with dissolve

        maki "That works for me, but I won’t bother asking why you chose that."
        s "That actually makes it sound like you find it boring and now I’m kind of questioning my decision."
        maki "I don’t find it boring at all. I’m just excited to get fucked in the ass and don’t have any problem with calling you that."
        s "Oh."
        maki "Oh indeed."
        s "Well...I guess that settles it, then."

        jump endofmakinaming

label endofmakinaming:

    scene makianal2
    with dissolve

    maki "I guess it does..."

    scene makianal8
    with dissolve

    maki "Well then, [makimaster]! Are you ready to boldly go where several men have gone before?"
    s "Ew. Not when you put it like that."
    maki "Are you ready to definitely take my anal virginity?"
    s "..."
    maki "Are you ready?!"

    scene black
    with dissolve2

    s "I...guess I am."

    "........."
    "......"
    "..."

    scene makianal20
    with dissolve2

    "Maki takes a moment to lock the door and flip the sign to closed after assuring me that Makoto won’t be stopping by tonight. But all I do is just...stand around awkwardly and wait."
    "Once the site is secured, she comes over to me and kisses me, sliding her hand into my pants and attempting to resurrect my temporarily deceased member."
    "At which she succeeds. And quite dramatically at that as I can’t help but want to pounce on her the moment she slides her shorts off."
    "And while I don’t know much about anal sex, I {i}do{/i} know that I could cause some serious damage if I just...dig in right away. {i}Especially{/i} with my size."

    maki "Go ahead and pick your poison, [makimaster]. I’ve got over one hundred different types of lubes in stock. And just for tonight, I’ll give you 50%% off."
    s "You’re still making me pay?"
    maki "A girl’s gotta do what a girl’s gotta do. I know a sale when I see one."
    s "Oh, you’re {i}actually{/i} evil."
    maki "Mhmm...And what are you gonna do about it, [makimaster]?"
    maki "It’s probably really {i}hard{/i} seeing me standing here like this...defenseless and waiting...isn’t it?"
    s "You know exactly how hard it is, you fucking super villain. It was in your hand like thirty seconds ago."
    maki "Mmm...I think I forgot already. Want to come over here and remind me?"

    "Maki begins to wave her hips and the glow of the porn shop’s fluorescent lights on her pale skin turns her lewd gesture into a siren song."
    "I know I have to have her. And {i}she{/i} knows I’ll do anything to make it happen. How sick it is that she’s making me work for it {i}and{/i} holding the hole I’m used to hostage."
    "Though, I guess I {i}could{/i} just use that one anyway and-"

    maki "Oh, by the way, if your cock just happens to {i}slip out{/i} and find my pussy instead, we’re stopping and restarting. This is an {i}educational{/i} session, [makimaster]."
    s "I don’t like how you can read my mind."
    maki "I don’t like how your cock is still over there and not inside of me."

    scene makianal21
    with dissolve

    s "Ugh...hold on."
    maki "Don’t keep me waiting too long. I haven’t done it like this in a while. And {i}never{/i} with one as big as {i}yours.{/i} I’m excited."
    s "{i}Stop trying to sell me. I’m already in too deep.{/i}"
    maki "You’re not in at all, [makimaster]. I would know. "
    s "{i}You know what I mean, Maki.{/i}"
    maki "All I know is that anyone else would be over here fucking me right now and you’re still busy picking out a lube."
    s "{i}Yeah, well there are too fucking many of them.{/i}"

    scene makianal22
    with dissolve

    maki "{i}Just pick one.{/i} It really doesn’t matter. "

    scene black
    with dissolve2

    s "Fine..."
    s "I’m on my way."

    "........."
    "......"
    "..."

    scene makianal23
    with dissolve2

    maki "Ngh!!! [makimaster]! Not so...hard in the beginning!!!"

    "After taking a moment to {i}prepare,{/i} I mount Maki from behind and slide myself inside of her."
    "It’s a little...different to say the least. But not exactly in a bad way."
    "It’s harder to move and definitely a little tighter, but the most difficult part (at least so far) is figuring out how to pace myself."

    maki "Mngh....mngh!!"

    "Despite not being entirely comfortable with the size of my cock in an area that I’m {i}still{/i} not sure it’s meant to go...Maki thrusts backward into me, taking it deeper in the process."
    "I can tell she’s in a little bit of pain, but I land on the fact that it’s probably within the “acceptable” level of pain for her and not just entirely unexpected."

    maki "God, [makimaster]...you’re so fucking big...GOD you’re so fucking big...fuck!"
    s "Are you starting to regret your suggestion?"

    scene makianal24
    with dissolve

    maki "Fuck...no, I’m not!"
    maki "I’ve always wondered...what having a {i}big{/i} one in here would feel like..."
    maki "Tiny dicks are...fine and all, but...ahh...they’ve got nothing on you, [makimaster]!..."
    maki "Harder...I’m starting to warm up..."
    s "Any “pointers” for me? This is supposed to be “educational,” isn’t it?"
    maki "Yeah...your pointer is “fuck me harder when I tell you to.” You got that, [makimaster]?"

    scene makianal23
    with dissolve
    play sound "dosex.mp3"

    s "You mean like this, Maki?"
    maki "Ngh! Yes, [makimaster]! Fuck me...fuck my...fucking ass! Agh!"

    "The excessive force from both of us causes several objects to fall off of the porn shop counter — including a vibrator that turns on once it hits the ground and immediately becomes very distracting. "

    maki "Ngh!....Ngh!........Fuck!!!!"
    s "Can you actually cum from this? Is that a thing?"
    maki "If you...do it right...yes!"
    s "Am I doing it right? I’m still not getting the sort of tips I thought I’d be getting."
    maki "That’s cause...the tip is inside of me! Along with...the rest of you! Fuck, [makimaster]! Slap my ass!"

    play sound "slap.mp3"
    scene makianal25 with hpunch

    maki "HAAAAH! YES, BABY! Just like...that!"

    scene makianal26
    with dissolve

    s "You like that, huh? You like being hit?"
    maki "I like it when {i}you{/i} hit me, [makimaster]...I like it when you...use me like a fucking toy!"
    s "Is that not what you are? You looked so natural bent over the counter that I figured you were on sale."
    maki "Hah! Hah! That’s...good! Both the joke and...the way you’re {i}fucking me,{/i} baby...ohhhh FUCK!"
    s "You were right, Maki...this isn’t half bad..."
    maki "Aaah...half...bad?...Is that...what you really think?"
    maki "You don’t...fucking love my...tight ass, [makimaster]?...You don’t love...treating me like a...fucking doll?!"

    scene makianal27
    with fade

    maki "Because {i}I{/i} love it, [makimaster]..."
    maki "I love how deep your fucking...massive cock gets inside of me...I love how it...stretches me out..."
    maki "And I’ll...love it even more when you...cum for me, baby!..."
    s "At this rate, I think you’re going to cum first..."
    maki "Hah...hah...that’s just...how good you are, [makimaster]!"
    s "I think you being a fucking slut might have something to do with it."

    scene makianal28
    with dissolve

    maki "Hah...hah...we don’t...use that word...in this house!"
    s "Really? Do you have a better word for a girl who cums from just a few minutes of anal sex?"
    maki "Y...Yes...The word...is Maki! I love...getting fucked like this! Oh GOD it’s so good!"
    s "How much better am I than the others, Maki? "
    maki "So much, baby...you’re so good...you’re so big...go faster...put them all...to shame! For me!...I want...you to cum for me!"
    s "And I want to hear you call yourself a slut. "
    maki "I’m...a slut! "
    s "I bet you’d let any customer fuck you in the ass if they paid enough, wouldn’t you?"
    maki "Haah! That’s not...true!"
    s "It’s not?"

    scene makianal27
    with dissolve

    maki "No! Only you can...fuck me now, [makimaster]! I want to be {i}your{/i} toy! I want to be {i}your{/i} slut!"
    maki "I never want you to leave this store...without fucking me again...do you understand?!"
    s "You’re seriously that needy?"
    maki "Yes! I want it every day! Every night! I want you to...fuck my little ass until I can’t walk anymore!"
    s "It’s actually not little at all. It’s kind of huge. But in a good way."
    maki "Hah...aaah...yeah?...You like it, baby?....Does that feel good?..."

    "Maki leans back until I’m almost fully submerged inside of her, creating a suction-like sensation that’s almost kind of painful. But again, in a good way."

    play sound "static.mp3"
    scene makianal26 with flash
    stop sound

    maki "Does that make you want to cum for me, baby?...Do you like it when I squeeze your...big fucking cock like that?"

    "She clenches down and nearly snaps me in half. And I’d be lying if I said I didn’t feel my life flash before my eyes just now, but I don’t have the heart to tell her that when she’s having so much fun."

    s "You want me to cum that bad, huh?"
    maki "Ngggh yes! I want it to fill me up! I want your hot cum deep inside of my ass, baby! Give it to me!"

    "She clenches down again, but achieves a bit more success this time as it almost forces an orgasm out of me."

    maki "I can feel it, baby...it’s throbbing...you’re so close...just keep fucking me!"

    "She returns to thrusting and I need to angle myself so my dick doesn’t snap off. This is actually kind of terrifying."

    maki "AAAAaah! God, I can’t take it anymore! I’m gonna fucking cum!"

    with hpunch

    "She clenches down again."

    s "Maki-"
    maki "Cum with me! [makimaster]! Cum inside of me! Let’s cum together!"
    s "I-"

    with hpunch

    s "Ngh!"
    maki "Aaaaah you’re so fucking close! What are you waiting for?!"
    s "Right now, I’m just trying to stay alive."
    maki "Well, stop!"

    with hpunch

    s "Maki-"
    maki "[makimaster]! Fuck me! Fuck my ass! Deeper! I want it, baby! I want your fucking cum! I want it!"
    s "Maki..."
    maki "I want it, I want it...I want it!"

    "Goodbye, world."

    with sexfade
    with sexfade
    scene makianal29 with cumflash
    with hpunch

    maki "AAAAAAAAAaaaaaaaaaAAAAAAAAAaaaAAAAAAAAAAHHHHHHHHHH!!!!!!!!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene makianal30
    with dissolve2

    maki "...and that’s why anal sex rules."
    s "It just felt like normal sex but tighter, dryer, and significantly more dangerous."

    scene makianal31
    with dissolve

    maki "But for {i}me,{/i} it was eye opening..."
    s "Well...I won’t deny that I had a good time as well."
    maki "I know. I can feel the evidence of that oozing out of me as we speak."
    s "Gross. So, what do I owe you for the lube?"

    scene makianal32
    with dissolve

    maki "Akira, I’m not {i}actually{/i} going to make you pay. Come in. I mean on. Come on."
    s "Oh. Well hey, that’s great news."

    scene makianal33
    with dissolve

    maki "You know I’m like...{i}actually{/i} into you, right? That this isn’t just a sexual thing?"
    s "I mean...yeah. I know that."

    scene makianal34
    with dissolve

    maki "Okay..."
    maki "Well, as long as you know."

    scene makianal30
    with dissolve

    maki "But aaaaaaanyway...I need to go take a shower and then...clean up the counter..."
    maki "And then eat dinner. And then post a review of Totally Anal Volume 19 to my porn review blog."
    s "And I need to go wallow in shame for the next hour and then pass out."

    scene makianal3
    with dissolve

    maki "Shame? Because of the anal?"
    s "No, I do that after every orgasm. I think it’s a guy thing."
    maki "That sounds so sad. "
    s "It is. But anyway, thanks for “teaching” me about anal sex tonight. I “learned” a lot."

    scene makianal1
    with dissolve

    maki "Yes. I also “learned.” We did a good job “learning” together."
    s "We normally do."
    maki "..."
    s "..."

    scene black
    with dissolve

    s "Okay, goodnight."
    maki "Heheh...goodnight, Akira."
    maki "I’ll see you soon..."

    $ renpy.end_replay()
    $ makilust5 = True
    $ maki_lust += 1
    stop music fadeout 10.0

    "{i}Maki’s lust has increased to [maki_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label makispring1:
    scene makimikudicks1
    with dissolve2
    play music "citylife.mp3"

    "There’s nothing quite like a trip to the porn shop at the end of the night. Everyone knows why you’re there."
    "Well, I suppose everyone knows why you’re there when you come during the afternoon too. But there’s a special type of person who shows up specifically when the sun goes down."
    "We’re the type who can’t sleep until we get our fill. The type who have hollowed out a special place in our hearts for sex and sexual paraphernalia. "
    "And there is {i}nothing{/i} too depraved for us."

    stop music fadeout 5.0
    play sound "footsteps.mp3"

    "........."
    "......"
    "..."

    s "Miku? What are {i}you{/i} doing-"

    play sound "static.mp3"
    scene makimikudicks2 with flash
    stop sound
    play music "anothernewsong.mp3"

    mi "Hey, you! With the big, floppy wiener!"

    "I look over my shoulder to make sure there’s no one else around with a big floppy wiener. It appears I am alone in that department."

    s "Uhh...hello?"
    mi "Do you like DICKS?!"
    s "Uhhhhhhhh..."

    play sound "airhorn.mp3"
    scene makimikudicks3
    with dissolve

    mi "What am I askin’?! Of course you like dicks! {i}Everybody{/i} likes dicks! Well guess what, buddy?! You’re in luck! Because {i}we’ve{/i} got ‘em!"

    scene makimikudicks4
    with dissolve

    mi "We’ve got big dicks! We’ve got little dicks! We’ve even got average and slightly above or {i}below{/i} average dicks! Any kinda dick you could ever want!"
    s "Please stop."
    mi "You want a horse dick?! We got it! You want a tentacle dick thing?! We got that too! And as if that ain’t awesome enough, we’ve also got these cool rings you can put on ‘em!"

    scene makimikudicks5
    with dissolve

    mi "I ain’t learned what those do yet, though. "

    scene makimikudicks4
    with dissolve

    mi "But still! We’ve got ‘em! And there ain’t ever been a better time to buy a cock than during our annual blowjob sale! "
    s "Don’t you mean “blowout” sale?"

    play sound "airhorn.mp3"

    mi "No, you fucking idiot! Blowouts are for hair! Now get that friggin’ wiener out and let me measure ya for your ring size!"

    scene makimikudicks6
    with dissolve

    maki "Okay. That’s enough. I am not going to let you measure Sensei’s penis."
    mi "How’d I do?! He ain’t bought anything yet, but I’ve got ‘im right in the crosshairs! And I ain’t even brought up  the lube yet!"
    s "Oh no. Is Miku working here too now?"
    mak "This is a {i}trial{/i} period. And one that I hope ends quickly because I can only take so much more of this."

    scene makimikudicks7
    with dissolve

    mi "She’s just joshin’, Sensei! Here at Miku’s Cock Emporium, there ain’t a hard limit about how much we can take! We can take it all! Just bend us over and shove it in! "
    maki "Metaphorically, of course. Japanese law forbids the sale of penetrative sex of the non-anal variety. "
    mi "And we all know how you feel about butt stuff!"
    s "We do?"

    scene makimikudicks8
    with dissolve

    mak "Please just ignore them. This overt and blatant promiscuity is little more than a means to get on my nerves."
    mi "Sounds to me like {i}somebody{/i} needs a new dick! And maybe a ring or two to dress it up with!"
    maki "We’ll get her to tone it down, Makoto. Learning is a process."

    scene makimikudicks9
    with dissolve

    mak "Don’t you think she might be learning a little too {i}quickly{/i} though?"
    mi "Sensei! Maki told me she’ll promote me to supervisor if I can sell a hundred dicks this week! You’ll help, right! I really need the cash."
    s "For {i}what?{/i}"

    play sound "airhorn.mp3"
    scene makimikudicks10

    mi "For all these friggin’ dicks, of course!"
    maki "Ooh, floating text!"
    mi "Dicks, dicks, dicks! Chant it with me, Sensei! Dicks, dicks, di-"

    play sound "static.mp3"
    scene makimikudicks11 with flash
    stop sound

    mak "Nope. You’re coming upstairs with me. We’re not even supposed to be working tonight."
    mi "Nooo! I’ve got a duty to fulfill to the world! Miku’s Cock Emporium waits for no one!"
    maki "Have fun, you two! And don’t forget to do your homework!"
    s "I really hope this isn’t going to happen every time I come here from now on."

    scene makimikudicks12
    with dissolve

    maki "Makoto and I will still be here, don’t worry. I’m just letting Miku help out around the place so she can feel better about taking money from me. "

    scene makimikudicks13
    with dissolve

    maki "And I promise it has absolutely nothing to do with labor laws!"
    s "I...didn’t assume it did until you said that."
    maki "Nothing at all!"
    s "..."
    maki "..."

    play sound "airhorn.mp3"
    scene makimikudicks14

    maki "Hey, guy! Do you like dicks?!"
    s "Okay. See you later, Maki."

    scene makimikudicks15
    with dissolve

    maki "Oh, stop. I might be an aggressive salesperson, but I know better than to market dildos to depressingly hetero males like you. Gotta know your market."

    scene makimikudicks16
    with dissolve

    maki "Oh! Speaking of! I bought a new thing! "
    s "Please tell me it’s not a dick."
    maki "It’s not a dick! Dicks are involved, though. Come! I’ll show you! It’s super cool."
    s "I don’t know if I-"

    scene black
    with dissolve
    play sound "tackle.mp3"
    stop music fadeout 8.0

    maki "No, you definitely do! You’ll appreciate it way more than the girls do, that’s for sure. "
    s "Ugh, fine. But let the record show that I am very hesitant about this based on how heavily involved dicks appear to be."
    maki "For {i}now{/i} you are. But within moments, Sensei, you’ll be praising Maki Miyamura for her unbeatable eye and predatorial business acumen!"
    maki "You like that word? Acumen? Makoto taught it to me. She made it sound more negative though. Which you will soon realize it’s not! Come!"

    play sound "lock.mp3"

    "Maki drags me by the wrist to the backroom, locking the door behind us once we’re inside. "
    "I notice immediately upon entry that some things have been shifted around. Which means that either she’s converting this room into something else or-"

    play sound "static.mp3"
    scene makimikudicks17 with flash
    stop sound
    play music "citylife.mp3"

    "Or she...bought something she needed to make room for."

    maki "Feast your eyes upon my latest investment and praise me for my vulture-like instincts to buy things before they become trash! "
    s "Wouldn’t it make more sense to just...wait until they become trash?"
    maki "And risk losing out on something as cool as this?! What if someone else swooped it up first?!"
    s "What even {i}is{/i} it?"

    play sound "static.mp3"
    scene makimikudicks18 with flash
    stop sound

    maki "A portable glory hole, obviously! It has these little wheels you can attach to the bottom to move it around to different events and locations and stuff."
    s "I have so many questions and I don’t know which ones to start with."
    maki "Well, if it’s concerning the legality of this, which we may or may not have already discussed at some point based on dialogue choices you may have made, I have confirmed that it {i}is{/i} legal."

    scene makimikudicks19
    with dissolve

    s "Okay, well that’s one question out of the way then."
    maki "Hit me with the rest. I’ve thought tirelessly about what I’m going to do with this thing."
    s "Okay. What are you going to do with it then?"

    scene makimikudicks20
    with dissolve

    maki "I don’t know!"
    s "..."
    maki "I only said I’ve {i}been{/i} thinking! Not that I’m good at it!"

    scene makimikudicks21
    with dissolve

    maki "Like, obviously I can’t actually charge people to use it until I get a bunch of permits and stuff. "
    maki "And while I’m sure there are a bunch of legal loopholes that would allow the {i}free{/i} use of it, it’s still just me and the girls here. And my days of swinging are long gone, pal. "
    s "Can’t imagine there are many guys coming here other than me too."
    maki "We get ‘em every now and then. But yeah, you’re definitely our top male customer."

    scene makimikudicks22
    with dissolve

    s "Where did you even get it? {i}Why{/i} did you get it? You barely have room for it in here."
    maki "I got it because it’s cool as hell! And even if it doesn’t get any actual use in here, it’s still a sweet memento packed with tons of history!"
    s "So it’s...been used already?"
    maki "Dude, look at it. Of course it’s been used. This thing’s been operational for over thirty years now."

    scene makimikudicks23
    with dissolve

    maki "There’s a sex club in the urban district I used to go to with Masahiro that decided to finally replace it with a new one. I imagine {i}thousands{/i} of dudes have stuck their dicks in those holes by now."
    s "And that doesn’t...disturb you at all?"
    maki "If it disturbed me, I wouldn’t have watched my former husband use it a bunch of times."
    s "Have {i}you{/i} used it?"

    scene makimikudicks24
    with dissolve

    maki "Me? No. I just watched most of the time. Haruka and I have made jokes about doing it together in the past, though. "
    s "This interests me. But I implore you to thoroughly clean it at least fifty times before I get any closer."
    maki "Come on, let’s get closer."

    scene black
    with dissolve

    s "Do you just {i}never{/i} listen to me or something? "
    maki "Not to the things I think are lame or boring! Come on. It’s not gonna {i}bite{/i} you. That- oh my god. Imagine it {i}could?{/i} Then I’d {i}really{/i} have to get those permits. What a cool feature."

    scene makimikudicks25
    with dissolve2

    "Maki slides the sofa over to the front of her new over-sized toy and I have no choice but to sit on it as well — which gives me a rather interesting glimpse into its insides."

    s "What’s with all the posters?"
    maki "They used to be blank back in the day. There was a little compartment thing with a marker hanging off the side that people could use to draw or write stuff. Not sure why it was always in English, though."
    s "So there were dudes in there just getting their dick sucked while doodling on a wall?"
    maki "Hell yeah. Isn’t history so cool?"
    s "If you count this as history, sure."

    scene makimikudicks26
    with dissolve

    maki "Of course it’s history! Just think of how many amazing people must have ejaculated into the built-in drain by now."
    s "Drain? Where does it even drain {i}to?{/i} "
    maki "No one knows."
    s "It’s portable. Wouldn’t it just leak out of the bottom?"
    maki "{i}No one knows.{/i}"
    maki "For real, though! How often do you get to straight up purchase an important piece of your past? "
    maki "I knew this little sex box before I even knew {i}you.{/i} Hell, I knew it before I knew {i}Makoto.{/i}"

    scene makimikudicks27
    with dissolve

    maki "And one day, I’m excited for her to learn that the memory of her father clings to {i}this{/i} as well. It’s not just his old fishing pole she has to remember him by."
    s "You want your daughter to remember her father by a portable box he used to put his dick in?"
    maki "You laugh...but I’m sure that one day, she’ll have her {i}own{/i} sex box memories to share with {i}her{/i} children."
    s "Miku too if things keep escalating like they have been over the course of this visit."

    scene makimikudicks28
    with dissolve

    maki "Yeah..."
    maki "Maybe even sooner for her."
    s "..."
    maki "She’s got me kind of worried lately, if we’re being honest."
    maki "Actually had to take her to the hospital recently because-"
    s "I know."

    scene makimikudicks29
    with dissolve

    maki "You {i}know?{/i} How do you know? Did Makoto tell you?"
    s "No. The...school. The hospital had to notify them and they called me. Either way, I know. So there’s no need to get into the details."

    scene makimikudicks30
    with dissolve

    maki "Hm...yeah. I imagine you {i}would{/i} be uncomfortable talking about this if you know the gist of what happened."

    "Yes, that is exactly why I am uncomfortable right now."

    maki "You get why I’m worried though, right?"
    maki "It was one thing when I thought Makoto was becoming {i}active...{/i}and she’s light years more mature than Miku is. Like, that girl still thinks “missionary” is a traveling nun. "
    maki "Combine that with this newfound interest in the shop and...I don’t know. Maybe I’m overreacting. I just feel responsible for her. That’s all."
    s "Yeah. You seem even more motherly with her than you do with Makoto sometimes."
    maki "Makoto doesn’t need me. She was born smart and had her dad to look up to for most of her life. Miku had me."
    s "Yeah, I...guess you {i}have{/i} been her guardian this whole time, technically. "
    maki "There was a little back and forth at first...but she’s been under our wing for a while, yeah. It never felt like she really considered herself a part of the family though, which..."
    maki "I don’t know. I do see her as my daughter too. And I’ve talked to her about sex, but...it’s hard to make Miku...{i}understand{/i} things at times. "
    maki "She’s one of those girls who learns better by {i}doing.{/i} And with something like {i}this,{/i} you’d obviously  see why that would be a problem."
    s "Yeah...sounds rough."

    scene makimikudicks31
    with dissolve

    maki "It is. You’ll help me keep an eye on her though, right? "
    s "Not sure I can help much without going back to school, Maki."
    maki "Maybe...go back to school then? If Makoto got over her hump, I’m sure you can too."
    s "Makoto’s more mature than {i}me{/i} as well. It’s not just Miku she has the jump on."
    maki "Guess she’s got all of us beat then, huh? "

    scene makimikudicks32
    with dissolve

    maki "It’s kind of crazy when I, like...really think about it."
    maki "I don’t know if times have just changed or something but, when {i}I{/i} was their age, boys were one of the last things on my mind."
    maki "And I get that there comes a time in every mother’s life when she needs to just sort of...let her children take the reins and figure things out on their own...but {i}already?{/i}"
    maki "Do you think it’s {i}my{/i} fault? For...putting them in a situation where sex is so...normalized? Because, when I was growing up, my mom was way more traditional. Having someone like me-"
    s "Don’t...blame yourself, Maki. You’re doing everything you can."

    scene makimikudicks33
    with dissolve

    maki "Yeah...I guess so. I think I’ll always feel somewhat responsible, though. "

    play sound "static.mp3"
    scene makimikudicks34 with flash
    stop sound

    maki "The world a child is brought up in...does a lot to determine who they are and...how they wind up."
    maki "I’ve been talking to Sara about it lately...trying to get better and...you know. Stuff like that. And I’m sure you get it since things have been changing in your relationship with Ami lately. It’s just tough."
    se "What do you think, Aki-kun? Imagine you’d have wound up any different without me around?"
    s "..."
    se "Do you {i}blame{/i} me for the way you are? Or do you think there’s a little more to it than that?"
    s "..."
    se "Because I’ve watched what you’ve done to {i}both{/i} of her little girls. Maybe even {i}felt{/i} it. But the point remains — wouldn’t it be easier to just blame {i}her{/i} for that?"

    "I have to stay quiet..."
    "{i}I have to stay quiet.{/i}"

    scene makimikudicks35
    with dissolve

    maki "It’s actually kind of funny how late I lost my virginity when you look at how I ended up. Haruka too. We’re both extreme degenerates now. "
    maki "Just kind of assumed it would be the same for Makoto and Miku. "
    se "Aki-kuuuuuun~"
    se "Your friend is going to think she’s boring you if just let her ramble on without adding anything to the conversatiooooon~"

    "Stay..."
    "Quiet..."

    scene makimikudicks36
    with dissolve

    maki "How old were you when you had your first time, Akira? If you don’t mind me asking."
    se "{i}Booooom{/i} goes the dynamite. You {i}love{/i} opening up about this, don’t you? Let her have it. Let’s see the look on her face when your deepest, {i}darkest{/i} secret is unveiled."
    maki "Like, maybe you’d be better than me at dealing with this if you know what it’s like to be in high school when-"

    scene makimikudicks37
    with dissolve2
    stop music fadeout 6.0

    s "..."
    maki "..."
    se "{i}Come onnnnnn~{/i}"
    se "So what if she gets mad at a ghost? Finding out you were such an early bloomer might lessen the blow when she finds out you’re porking her little girl."

    scene makimikudicks38
    with dissolve2

    s "..."
    maki "..."
    maki "Akira?..."
    se "Aki-kuuuuun?"
    s "I..."

    scene makimikudicks39
    with dissolve

    maki "Why don’t we go for a drive?"
    se "Nooooo, I hate cars! I have such bad luck with them!"
    s "But-"
    maki "Save your excuses. Let’s go."

    scene black
    with dissolve2

    s "We could also just...talk about something else or-"
    maki "Or not at all! I just want to go for a drive and think you’d make a good passenger princess."
    s "A...what?"
    se "Ughhhh! I’ll just meet you guys there. Bye bye, Aki-kun!"

    $ renpy.end_replay()
    $ makispring1 = True
    $ maki_love += 1

    jump makispring2

label makispring2:
    play sound "static.mp3"
    scene makikyoto1 with flash
    stop sound

    "{i}Hello alone.{/i}"

    scene makikyoto2
    with pixellate
    play music "sensei.mp3"

    "So I’m here again, hello — on the way to wherever Maki wants to take me to try and fix me."
    "And while I’m ever-depressed by the notion that my misery is so apparent to everyone at this point, I take solace in the fact that this flaw has once again rescued me from harm’s way."
    "How lucky I am to have so many attentive friends. How lucky I am to be pulled away from my inner struggles constantly whenever they’re around. "
    "It’s almost as if the world is telling me I’m not {i}meant{/i} to be alone. Or that I should lean on others for help more. Or whatever else I know to be true but neglect to believe regardless."
    "She won’t force me to talk. She’ll merely give me the opportunity to. And should I neglect {i}that{/i} as well, I imagine she’ll be perfectly content with just being in the same place as me."
    "Maybe she {i}does{/i} just want to drive? That’s what I’ll tell myself until we get to wherever we’re going."
    "But when these shaking hands reach for the handle once this car comes to a stop, I pray that I won’t recall the days when they were smaller and steadier."
    "Someone else sat beside me back then. "
    "Someone who I never thought I’d be able to live without. "
    "How apt that I’ve spent nearly a decade since then coming to terms with (or avoiding) just how true that is."

    maki "Have you ever driven a car, Akira?"
    s "What?"

    scene makikyoto3
    with dissolve

    maki "Have you or have you {i}not{/i} ever driven a motor vehicle? It’s a simple question."
    s "Oh, you’re not taking me somewhere I can “practice,” are you? You know I have a thing with cars."
    maki "I’m not taking you anywhere in particular. I’m just driving."

    scene makikyoto4
    with dissolve

    maki "We’re lucky to live somewhere we don’t really {i}need{/i} to know how to drive. So it’s not every day you get to spend time without someone who has."
    maki "It’s pretty liberating, actually. Terrifying, at first...but really freeing once the jitters wear off."
    s "Yeah..."
    s "There are a lot of things in life like that, aren’t there?"

    scene makikyoto5
    with dissolve2

    maki "Yeah..."
    maki "There sure are."
    s "..."
    maki "You know..."
    maki "I’d never think less of someone for learning early. I’d think less of the person who taught them."
    maki "Like Makoto, for example. I don’t think she’s ready yet, but I’ve told her about it and think she could figure it out pretty easily if she wanted to. Miku, though? I wouldn’t trust her behind the wheel of a car at all."
    maki "The unfortunate truth, though, is that I wouldn’t be able to stop them if they really wanted to."
    maki "That said, I’m not going to just hop in the passenger seat and watch as they figure it out on their own. Doing that would be directly putting them in harm’s way. Don’t you think?"
    s "Maki-"
    maki "It’s just driving, Akira. "
    maki "We’re talking about driving."
    s "..."
    maki "..."
    maki "I’m sorry."
    maki "I thought that would make it easier."
    s "There’s nothing to be sorry for."
    s "I just..."
    s "Have a thing with cars."

    scene makikyoto6
    with dissolve

    maki "Yeah..."
    maki "Why don’t we pull over then? This looks like a nice spot to get out and relax for a little while. "

    scene black
    with dissolve2

    s "Yeah...whatever you want."

    "Maki pulls off to the side of the road and parks her car in a spot with faded lines and cracked paint — causing memories to roll in before my shaking hands have the chance to evoke them."

    scene clearnightsky
    with dissolve2

    "There was a spot that {i}she{/i} used to park her car in after picking me up from Niki’s place."
    "Halfway between my childhood home and the one {i}she{/i} made with {i}him,{/i} there was an old shopping plaza she told me she worked at when she was younger. "
    "I never believed her, though. The thought of her having any sort of regular job just seemed flat out bizarre to me. She was larger than life. She was {i}Sekai.{/i}"
    "Something didn’t {i}always{/i} happen when she pulled into that spot in the back of the shopping plaza...But many days, something did."
    "Something that, like driving, felt liberating. Terrifying at first...but freeing once the jitters wore off."
    "She taught me everything I know."
    "Now, every single vehicle I lay my eyes on reminds me of her."

    scene makikyoto7
    with dissolve2

    "Some days, when I stare up at that wall, I imagine what {i}she{/i} would have done about it. Because if anyone could figure out how to scale it, it would have been her."
    "She didn’t even like sitting in that car for more than an hour at a time. She always needed to be moving. There’s no {i}way{/i} she’d just sit back and let some colossal barrier keep her from getting out of here."
    "Guess she figured it out in the end, though. Now, even death can’t keep her in one place."

    maki "It’s always crazy when I remember how we used to be able to just...leave. The thought of that today is just...surreal."
    s "Have you ever been outside of Kumon-mi?"
    maki "Kyoto for a field trip once."
    s "Ahh..."
    s "Never been."
    maki "It’s beautiful. Romantic. You’d love it there."
    s "Yeah...I probably would."
    maki "Have you ever been {i}anywhere{/i} outside of Kumon-mi? Tokyo, maybe?"
    s "If I have, I can’t remember it. "
    s "At the very least, I know Ami’s never left. No real desire to either."
    maki "Yeah. Plenty of people seem perfectly content with just...never getting out and exploring. "
    maki "That was weird to me when I was younger, but I’m starting to understand it now."
    maki "The longer we stay behind this thing, the more comfortable we become with everything that’s inside of it. But of course that makes everything on the {i}outside{/i} scarier."
    maki "Like, for all {i}we{/i} know, everything else could be gone already."
    s "We still get TV and stuff from the outside, though."
    maki "Sure, but is anything actually {i}real{/i} before we see it with our own eyes?"
    s "Yes. Otherwise those things would not exist for us to see. But I get what you’re saying."
    maki "Yeah. Exactly. You’re the smart one here. I make a living selling rubber penises."
    s "You’re smart too, Maki. Your knowledge is just a little less...conventional than it is for most people."
    maki "Thanks, Akira. That means a lot coming from someone who’s never bought any of my rubber penises."
    s "I will eventually. I still owe several people secret Santa presents, I think. Maybe I’ll just wait a few more years and place a bulk order?"
    maki "Well, you best hurry up or Miku’s Cock Emporium is going to put my place out of business."
    s "Only a matter of time."
    maki "Only a matter of time..."
    s "..."
    maki "..."

    scene makikyoto8
    with dissolve2

    maki "I wonder if anybody’s ever had sex up against the barrier?"
    s "Maki."

    scene makikyoto9
    with dissolve

    maki "What?! That’s a totally normal thing to wonder! Somebody’s had to have done it by now, right?"
    s "It...does seem statistically improbable that everyone in this city would have avoided it, yes."

    scene makikyoto10
    with dissolve

    maki "I wonder what the first couple thought? Assuming it was a regular couple and not an orgy, of course. But hey, that sex club downtown organizes some crazy events sometimes. Maybe {i}they{/i} did it?"
    s "I’m sure learning a lot about a sex club I didn’t know existed until today...today."

    if makisex == True:
        maki "Maybe we can go together? You’ll get in for free if I bring you along."
        s "Only if you promise to stay mine while we’re in there and not run off with some other guy."

        scene makikyoto11
        with dissolve

        maki "Deal. "
        maki "How about you, though? You’ll be immensely outnumbered. Think I’ll be enough for you in there?"
        s "I think...I’m not sure if you {i}want{/i} to be enough for me in there."
        maki "Monogamy can be fun too, Akira."

        scene makikyoto12
        with dissolve

        maki "Though...I guess it {i}might{/i} be a little weird if we just go there and only screw each other. Nobody else there really rolls like that."

    else:
        maki "Great news for me. Less competition when it comes to buying their old stuff."
        maki "You should check it out, though. You’d like it there. {i}Plus,{/i} you’d be greatly outnumbered. Just one more benefit of not getting called to war and killed by aliens."
        s "Maybe the alien sex was worth it?"
        maki "Asking myself that question is exactly what I do to calm down when I think about Masahiro. He always {i}said{/i} he wanted to fuck an alien."

    scene makikyoto13
    with dissolve

    maki "Regardless, it’s cool knowing that, in this world of infinite possibilities, there are new “firsts” every single day."
    maki "First people to bone up against the barrier...first people to {i}talk{/i} about the first people to bone up against the barrier...and the first people to mention people talking about the first people to-"
    s "I get it, Maki."
    maki "Good, because I was starting to lose track of what I was saying."

    scene makikyoto14
    with dissolve

    maki "But I guess if we’re all out of topics, we-"

    scene makikyoto15
    with dissolve

    maki "...Akira?"

    scene black
    with dissolve2
    scene makikyoto16
    with dissolve2

    s "..."
    maki "Was...it something I said? Do you...need something? What do I-"
    s "I should have gone..."
    maki "Gone...where?"
    s "It doesn’t matter anymore..."
    s "None of us are ever leaving this place again."
    maki "Um..."
    maki "D...Do I...hug you? Do I give you space? What do I do? I’m bad at this. You need to tell me or I’ll get it wrong."

    play sound "static.mp3"
    scene makikyoto17 with flash
    stop sound

    se "Gah! My poor ghost legs! I’m never running that far again...{i}especially{/i} in that white dress. It was so tight that I had no choice but to stop for a change of clothes on the way here."

    scene makikyoto18
    with dissolve

    se "So! What’d I miss? Anything fun? Anything {i}sexy?{/i} What are you guys talking about?"
    s "Nothing..."
    maki "Do...nothing? Okay. Got it. Carry on."
    s "No...not you, Maki."
    maki "But...we’re the only ones here?"
    s "Not to me, we’re not."

    scene makikyoto19
    with dissolve2

    maki "I...don’t think I...understand..."
    s "Driving..."
    s "I’m talking about driving."

    scene makikyoto20
    with dissolve2

    maki "Okay...sure."
    s "I..."
    s "Was young."
    maki "..."
    s "Very young..."

    scene makikyoto21
    with dissolve2

    maki "..."
    s "But I loved that person...with every fiber of my being. And when she..."
    s "When she died, it changed everything. "
    s "I still see her, Maki. "
    s "She follows me. She speaks to me. She-"
    maki "And she’s here right now?"
    se "Present!"
    s "Yeah..."
    maki "Can she hear me?"
    se "Loud and clear!"
    s "Yes..."
    maki "Great. Then can I have a minute to think of something really horrible to say to whoever did this to you? "

    scene makikyoto22
    with dissolve2

    se "One more girl who just doesn’t {i}get{/i} it. We really are a rare breed nowadays."
    s "It wasn’t her fault. She really {i}did{/i} love me. She just didn’t...see the world the way other people do."
    maki "Akira-"

    scene makikyoto23
    with dissolve

    s "I get it. I blame her too sometimes. But then I..."
    s "I remember all the {i}good{/i} things. How she saved me. How she gave me {i}something{/i} I could finally look forward to in a world where I...never had anything like that."

    scene makikyoto24
    with dissolve

    s "So yeah...I gave her all of me. Or whatever I had left, I guess. And I don’t regret it at all, but...I’m a monster now. "
    s "And I spend a lot of time just wishing I was someone else...or {i}somewhere{/i} else. "
    s "Anywhere but here would be fine."
    s "Anyone but {i}me{/i} would be fine..."

    scene makikyoto25
    with dissolve2

    maki "Your past doesn’t make you a monster, Akira."
    s "No, it doesn’t. But she painted everything black and it’s hard to just...paint over that because it feels like I’d be erasing her. "
    s "And if I let go of the parts of myself that {i}she{/i} put there...what if I never {i}saw{/i} her again? Because I want to let go! I do..."
    s "But I also don’t want her to stay gone forever. {i}Because{/i} of those good parts. {i}Because{/i} I loved her."
    maki "That wasn’t {i}love,{/i} Akira...That was-"

    play sound "static.mp3"
    scene makikyoto26 with flash
    stop sound

    s "No! You don’t get it! It {i}was!{/i} And I know how it sounds, but it wasn’t like that! She was amazing! She wasn’t like {i}me!{/i} {i}I’m{/i} the one who’s terrible! She was just misunderstood!"
    se "Aki-kun, don’t yell. She’s not going to get it. She’s not like us. Just let her say whatever she wants to say about me and call it a day. I can assure you I’ve heard worse."
    maki "You’re not like that deplorable woman, Akira! I know you! You’re better than-"
    s "You know what I {i}want{/i} you to know! But what if there’s more to me than that?! What if I’ve been hiding something?! Then what?!"
    se "Aki-kun, don’t do it. Don’t tell her you’ve-"

    play sound "static.mp3"
    scene makikyoto27 with flash
    stop sound

    se "Fucked your daughter like a gazillion times! {i}Both{/i} daughters, actually! And guess what, lady?! All that time teaching them about safe sex was for nothing! My Aki-kun likes it {i}raw!{/i}"

    scene makikyoto28
    with dissolve

    se "Wha- get out of here, me! Aki-kun doesn’t want you here right now!"
    se "Aki-kun doesn’t {i}know{/i} what he wants! That’s why I’m here in the first place!"

    scene makikyoto29
    with dissolve

    se "Aki-kun, look at me. You’re better than this. Don’t throw this away just because you’re getting emotional. It’s not worth it."

    scene makikyoto30
    with dissolve

    se "No, Aki-kun! Look at me! You’re {i}not{/i} better than this. But that’s {i}okay!{/i} We know who we are and hiding it won’t do anything but confuse us! Accept it and just {i}live!{/i} "
    maki "Akira-"

    scene makikyoto31
    with dissolve

    s "I don’t know what to do. I don’t know what to do. I don’t know what to-"
    maki "{b}AKIRA!!!!{/b}"

    play sound "static.mp3"
    scene makikyoto32 with flash
    stop sound

    s "Huh?......."

    play sound "static.mp3"
    scene makikyoto33 with flash
    stop sound

    maki "Whatever you are...whatever you’ve {i}done...{/i}it’s okay..."
    maki "We all make mistakes. But that doesn’t mean we can’t be forgiven."
    s "Can {i}everything{/i} be forgiven, Maki?...You don’t know what I’ve done."
    maki "That doesn’t matter. What matters is that you {i}understand{/i} that what you’ve done is wrong and that you’re making an effort to get better. "
    maki "Hating you for being a shitty driver when you were taught by a shitty teacher isn’t going to do any good for anyone. "
    s "What if I’m not trying to get better, though?...What if I’m barreling down some suburban street at twice the recommended speed with my eyes closed and my hands off the wheel?"
    maki "Then yeah, you’re a shitty person. But a shitty person wouldn’t be this-"
    s "Broken?..."
    s "Is that what you want to say?..."

    scene makikyoto34
    with dissolve2

    s "That changes nothing, Maki."
    s "I make my own decisions."
    maki "Are you sure about that? Because I’m not sure I believe it if you’re hallucinating a dead woman, Akira. "
    s "I..."
    s "It gets...complicated when you...start bringing that kind of stuff into the picture. There’s all sorts of weird supernatural shit happening here every single day."
    maki "That sounds exactly like what someone who’s losing it would say."
    s "Maki-"

    scene makikyoto35
    with dissolve

    maki "Makoto was the same way when Masahiro died. And I know you lost someone else not too long ago, so maybe you just need a reset?"
    s "Heh...yeah. Because those fix everything."
    maki "A little break won’t hurt you, will it?"
    s "Maki, why do you think I haven’t gone back to school yet? Why do you think I spend my days just wandering around Kumon-mi looking for shit to do or people to kill time with?"
    maki "Because..."

    scene makikyoto36
    with dissolve2
    stop music fadeout 15.0

    maki "Because you’re lost..."
    s "Bingo."
    maki "..."
    s "..."
    maki "How are we supposed to find where you’re meant to be then?"
    s "{i}You’re{/i} not supposed to do anything. I’m an adult. I’m supposed to figure that out alone. Like you did with Makoto."
    maki "You {i}helped{/i} me with Makoto. I owe it to you to at least try and do the same."
    s "Well...good luck. You’ve got your work cut out for you. Prepare to be let down more than you could ever believe."
    maki "At the very least..."

    scene makikyoto37
    with dissolve

    maki "Thank you for telling me, Akira. "
    maki "Anything to lessen a burden placed entirely on you."
    s "This lessens nothing...just makes me more self-conscious around you."
    maki "I’m sorry you feel that way, but I don’t. And if you ever need anything-"
    s "Can I get a ride home? I want to see Ami."

    scene black
    with dissolve2

    maki "...Yeah."
    maki "And I want to see Makoto. "

    "My hands are surprisingly still when I get back into Maki’s car, but I don’t understand why."
    "I feel no better than I did before. My chest is no lighter now that one more secret has been shed from it into the palms of someone else who cares for no good reason at all."
    "Despite this, though...and despite the many hints of my deranged depravity that I forced upon Maki just minutes ago...she never stops checking on me the whole way home."
    "I don’t understand why."
    "Is this willful ignorance?"
    "Is it pity? "
    "Or have I effortlessly warped {i}her{/i} definition of “love” now too?"
    "Whatever the case, there’s one thing I know for sure."
    "It’s that I fucking hate driving."

    $ renpy.end_replay()
    $ makispring2 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "{i}You can’t hide the truth from her much longer.{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
