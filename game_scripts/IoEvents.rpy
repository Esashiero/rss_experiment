label bathhouse:
    if io_love >= 0 and day247 == True and bathhouse1 == False:
        jump bathhouse1
    if io_love >= 5 and bathhouse1 == True and bathhouse5 == False:
        jump bathhouse5
    if io_love >= 10 and dormwar17 == True and bathhouse10 == False:
        jump bathhouse10
    if io_love >= 20 and iodorm15 == True and bathhouse20 == False:
        jump bathhouse20
    if io_love >= 25 and ioarchery1 == True and bathhouse25 == False:
        jump bathhouse25
    if io_love >= 35 and amispecial50mainp2 == True and bathhouse35p1 == False:
        jump bathhouse35p1
    if chap4active == True:
        jump iospringbathhousegen
    if chapthreeactive == True:
        jump iosummer2bathgen
    else:
        jump bathhousegen

label calliomorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if ioblock == True:
        "I should leave Io alone for now..."
        jump callmorning
    if io_love >= 35 and iodorm35 == True and predormwars3 == True and ioarchery35 == False:
        jump ioarchery35
    if chap4active == True:
        jump iospringmorninggen
    if chapthreeactive == True:
        jump iosummer2morninggen
    else:
        play sound "phonebeep.wav"

        "I tap on Io's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        i "Hey! Good morning Sen-"
        i "Oh, shoot."
        i "I got too excited and might have woken Uta up."
        i "Hold on."

        "A few seconds go by as Io presumably makes sure that her roommate is still asleep."
        "It's kind of cute that she'd get so excited by just a phone call-"
        "But the cuteness of that excitement quickly fades when I remember that she is just one of thirty-ish options, and that I could have just as easily called anyone else."
        "She can't be happy every morning."

        i "Okay. Back."
        i "Sorry about that."
        i "I went out into the hall and now I have to try and avoid confrontation with anyone else who happens to walk by."
        s "How about I make that a little easier by meeting up with you?"
        i "Really? Right now?"
        s "Is that a problem?"
        i "Not at all! I'm already dressed, so we can meet wherever really."
        i "I just didn't think you'd be up to hanging out so early in the day."
        s "Well, I am."
        s "Let's meet up near the bathhouse and just figure out what to do from there."
        i "Cool! Sure!"
        i "See you soon!"

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene iomorninggen
        with dissolve
        play music "justbehappy.mp3"

        "Io and I make plans to get breakfast at a nearby convenience store, but..."

        s "Io."
        i "Yeah?"
        s "Are you eating a hot dog for breakfast?"
        i "I'm eating {i}three{/i} hot dogs for breakfast."
        i "This is just the first one."
        i "There are a few more stores on this road and I have timed my hot dog consumption to end just as we make it to the each of them."
        i "Is that weird?"
        s "Yes."
        i "Oh."
        i "Well, whatever. You should get one too."
        s "How exactly are you this skinny again?"
        i "Idunno. Intermittent fasting, maybe?"
        i "I normally only eat like once or twice a day."
        i "But that's not important right now! It's hot dog time!"

        scene black
        with dissolve

        "The rest of the morning goes by...strangely, I guess."
        "But at least Io is happy."

        $ io_love += 1
        stop music fadeout 5.0

        "{i}Io's affection has increased to [io_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label callioafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if ioblock == True:
        "I should leave Io alone for now..."
        jump callafternoon
    else:
        "Io should be working right now."
        "I can probably see her if I go to the bathhouse."
        jump callafternoon

label callionight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if ioblock == True:
        "I should leave Io alone for now..."
        jump callnight
    if chap4active == True:
        jump iospringnightgen
    if chapthreeactive == True:
        jump iosummer2nightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Io's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        i "Hey! What's up?"
        i "I was hoping you'd call."
        s "Were you?"
        i "Yup!"

        if day > 5:
            i "I'm actually about to leave work right now, and I was going to call you if you didn't call me first."
        else:
            i "I'm actually on my way back from the convenience store right now and was just about to call you."

        s "What a convenient coincidence."
        i "Heheh! Super convenient."
        i "Wanna go walk around the park or something?"
        i "Nobody really goes to the one near the dorm, and there are a few trails there where nobody will bother us."
        s "Sounds good to me. I'll start heading over now."
        i "Awesome!"
        i "See you soon, Sensei!"

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene ionightgen
        with dissolve
        play music "io.mp3"

        "Io and I spend the night roaming the park and talking about whatever crosses our minds."
        "As a result, the conversation rapidly switches back and forth from the meaning of life to food...then back around to what it means to exist and then, finally-"
        "Bugs."
        "As it turns out, Io isn't only a tomboy in her woodworking, handicraft, and baseball hobbies. She also likes to catch bugs and torment Uta with them."
        "Their friendship becomes significantly stranger once I realize this, and I can't help but contemplate if Uta's pet beetle is somehow involved."
        "Either way, Io decides against tormenting {i}me{/i} and instead just points out and names facts about almost every single creature we come across."

        if bonus == True:
            "I find it impressive how she is essentially a fountain of biological knowledge and manage to refrain from including any of {i}my{/i} biological knowledge into the conversation as well."
            "That was a sex joke."
            "Please laugh."
        else:
            "I find it impressive how she is essentially a fountain of biological knowledge and consider pushing her into further expanding that talent of hers once she gets out of college."

        scene black
        with dissolve

        "We end the night by sitting on a park bench for another half hour or so, not really talking about anything- but instead just staving off the cold and gazing up at streetlights."
        "Io rests her head on my shoulder and ultimately falls asleep."

        $ io_love += 1
        stop music fadeout 5.0

        "{i}Io's affection has increased to [io_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label bathhousegen:
    scene bathhousegen
    with fade
    play music "normalday.mp3"

    "I decide to go to the bathhouse to see what Io is up to."
    "Since it's the middle of the day, there aren't many people around."
    "Because of that, we're able to spend the afternoon uninterrupted, eating snacks from one of the vending machines and talking about life."
    "Apparently, Io's pretty much the only employee this place has."
    "She informs me that a few temporary hires show up in the summer when the place gets busier, but she's able to hold things down on her own the rest of the year."
    "It's strange that I've yet to see her aunt around, though, considering she owns the place and also apparently lives here."
    "I'm glad that Io is able to run the bathhouse on her own, but she's still just a [young_girl]."
    "Someone like her shouldn't be burdened by such a responsibility just yet."
    "But, then again, it's not like she's dying to get out and spend time with anyone other than Uta or me."
    "So...as long as she's fine with wasting away in a place like this, it's not really any of my business."

    scene black
    with dissolve

    "We wind up eating so many snacks that the two of us slip into food-induced comas and need to be carted off to the hospital and placed on life support."
    "Just kidding."
    "Io never makes it to the hospital. She dies in the ambulance."
    "Just kidding again."
    "The food-induced coma thing isn't a joke, though."
    "It's near impossible for me to tear myself away from the counter and walk out of the bathhouse."
    "As for Io..."
    "Not a day goes by where I don't blame myself for her passing."
    "Just kidding a third time."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label bathhouse1:
    scene firstbath1
    with dissolve
    play music "io.mp3"

    "It’s the middle of the day and yet I find myself in the bathhouse."
    "Normally (And I use the word “normally” lightly since coming here in general isn’t exactly something I’d typically do)-"
    "Normally, I’d wait for it to be dark out. "
    "I mean, taking a bath in the afternoon is kind of pointless."
    "Isn’t it?"
    "Sure, there’s always the possibility of coming somewhere like this to relax-"
    "But something about having to pay to get naked and sit in a giant, wet rectangle while cold winter air attacks my skin doesn’t scream “relaxing.”"
    "It does scream, though."
    "Just not a noise I’m able to discern."
    "But-"
    "Nonetheless, I’m here."

    i "Welcome in. You can pay up here before-"
    i "Oh."
    i "Sensei. It’s you."

    scene firstbath2
    with dissolve

    s "Hey. How’s work going?"
    i "Fine, I guess."
    i "You’re here early. "
    i "And alone."
    i "Trying to kill time or something?"
    s "Or something, yeah."

    if bonus == True:
        i "Well, the discount I talked about is still on the table if you want it."
        i "You’re a few hours early for the peep-show, though. No Uta until at least 8:00 tonight."
        s "So I can’t come here to hang out with you?"
    else:
        s "Am I not allowed to come here to hang out with you?"

    scene firstbath3
    with dissolve

    i "I mean, you {i}can{/i} if you want. It just doesn’t seem like it would be very exciting to spend your afternoon off in a place like this."

    if bonus == True:
        i "Unless you’re just trying to sneak a peek at anyone else weird enough to come at this time of day."
        i "If that’s the case, this is exactly where you’d want to be."
        i "Just try to be discreet about it, though. I’ve got a crowbar under the counter and I’ve been given the okay to break it out if anyone gets weird."
        s "A - That’s very intimidating."
        s "B - Why even have a co-ed changing room if you’re worried about things like that?"
    else:
        s "I see nothing unexciting about good personal hygiene."
        s "Personally, I don't understand why there isn't more privacy in a place like this."
        s "I would be willing to invest if the issue is a financial one."
        i "It is not."
        s "Then why? Why must you create such an unsafe business?"

    scene firstbath4
    with dissolve

    i "My aunt’s idea. "
    i "We were actually thinking of just getting rid of the male section entirely and making this an all-female bathhouse after the war started."
    i "But we’ve got a fair share of customers who cherish their privacy and rent out the men’s side for themselves."
    s "Guilty as charged."

    if bonus == True:
        s "That was all Ayane’s idea, though."
    else:
        s "I am very rich."

    scene firstbath5
    with dissolve

    i "I’m not just talking about you."
    i "We’ve got several pairs of regulars who do the same exact thing a few times a week."

    if bonus == True:
        i "Most of them don't have the same sort of age gap you two have, but still."

    i "You’d be surprised by how many people prefer their privacy here."
    i "Could be body image issues, couples looking for alone time, sports teams wanting a communal place to wind down after a game-"
    i "Or green-haired, blue-eyed [teens] who thrive in empty spaces."
    s "...I’m not disturbing you, am I?"
    i "Sorry, that clearly didn’t come out the way I wanted it to."
    i "You’re fine."
    i "I already told you that I’m starting to like the time we spend together, even if the vast majority of it is me cryptically hinting at my backstory."
    s "Why be cryptic at all? Why not just tell me?"

    scene firstbath6
    with dissolve

    i "Tell you what?"
    i "What part do you want to know, exactly?"
    s "Well, you hate secrets, don’t you? "
    i "They’re the worst. "
    s "Just...tell me one of those, then. "
    i "Mm...I don’t think I can."
    i "Secrets are exhausting but it’s not like they don’t exist for a reason."
    i "For example, even though I keep saying stuff about how I like being around you, don’t you think there are a few things you could say that would change that?"
    i "Something you’re not proud of?"
    i "Something I couldn’t possibly understand?"

    if amifingered == True:
        play sound "static.mp3"
        scene amisfirsttime34
        with flash
        scene firstbath6
        with flash
        stop sound
    else:
        play sound "static.mp3"
        scene amidormten12
        with flash
        scene firstbath6
        with flash
        stop sound

    i "I’m just a [young_girl] after all."
    i "There are plenty of things I don’t know, even if I like to pretend there aren’t."

    scene firstbath7
    with dissolve

    i "Wanna trade?"
    i "You try to make me hate you and I try to make you hate me?"
    s "..."
    s "I’m not looking to make any enemies today, so how about you just tell me how you wound up in a place like this?"

    scene firstbath8
    with dissolve

    i "Heh. Weirdly enough, that’s probably one of the hardest questions you could ask me."
    i "Want to accept my prepared, cop-out answer instead?"
    s "Sure. Hit me."

    scene firstbath9
    with dissolve

    i "I woke up and walked here. The end."
    s "I feel like you could have done a little better if that was an actual {i}prepared{/i} remark."
    i "Could have, yes. But I didn’t. So you’ve gotta take what you can get."

    "“I walked here” really is a cop-out answer. She wasn’t kidding."
    "But it’s not like I expect her to spill her guts out on the floor in front of me when our relationship is still just getting started."
    "I get the feeling that whatever is happening here is going to take a long time to unravel."
    "I’m sure you’ve heard by now that if you were to remove your intestines and stretch them out across the floor, you’d wind up with around fifteen feet worth of organs, right?"
    "So, even if she {i}were{/i} to spill her guts out, it would take an astounding amount of work on my end to fully uncover them."
    "And sure, “astounding” may sound like a stretch given that it’s only fifteen feet-"
    "But fifteen feet is a long way to go in a number of ways."
    "That’s three whole Io’s."
    "I guess what I’m really trying to say is that it’s possible to spill your guts out and still only give someone a fraction of what’s really there."
    "In order to fully understand anything, you need to get your hands dirty. "
    "Feel those intestines slipping between your fingers-"
    "Memorize each and every groove-"
    "And then put them back together...and shove them back inside so whoever gave them to you can eat or drink once more."
    "Praise be."

    scene firstbath10
    with dissolve

    i "It’s not a bad place, though, this bathhouse."
    i "The fridge upstairs is always stocked with food, the bed is warm, and no one bothers me other than Uta whenever she has some spare time to herself."
    i "I think I may have even called it home on several occasions."
    i "I never mean to when it happens. I {i}am{/i} just a visitor after all."
    s "Same here."

    scene firstbath7
    with dissolve

    i "You also don’t feel at-home where you live, Sensei?"
    s "I’m starting to, I think."
    s "But I definitely don’t think this place was made for me."
    i "This “place” probably wasn’t made for anyone."
    i "When I called myself a visitor, I was doing it in more of a “This is just my aunt’s home” sort of way. But yeah, I guess it parallels how I am...or how {i}we are{/i} as a whole."
    s "You remind me a lot of one of the other girls in class when you say things like that."
    i "I think I’m supposed to ask which one but, honestly, I really don’t care."
    i "If whoever you’re talking about sounds the same as me during a time like this, I can’t imagine she’d like discovering our apparent connection either."
    i "You don’t develop this kinda mindset by just watching TV and listening to music, you know?"
    i "You’ve gotta see stuff. {i}Feel{/i} stuff."
    i "And then you’ve gotta figure out how to lock it all away so no one can discern your vulnerabilities."
    i "Chances are, whoever that girl is, she's remarkably unhappy."

    scene firstbath10
    with dissolve

    i "Haha~ This is fun!"
    i "I don’t normally get to talk about stuff like this! Let alone while I’m working."
    i "And I’m pretty sure Uta isn’t mature enough to handle these kinds of discussions yet, so I’m glad I can keep up with you."
    s "To be fair, you’re the one doing most of the talking so, from my perspective, it feels more like I’m trying to keep up with you."

    scene firstbath11
    with dissolve

    i "Maybe we’re trying to keep up with each other?"
    i "Like...we’re both on treadmills facing one another and no matter how quickly we run to meet up, the belt-speed just gets faster."

    scene firstbath12
    with dissolve

    i "It’s fucking torturous. Isn’t it?"
    i "You just want to make it to the goal line and you can’t because life is a cruel bitch and keeps figuring out ways to push you back."
    i "I fucking hate it, Sensei. I hate all of it."

    scene firstbath13
    with dissolve

    i "But I guess that line of thinking is self-destructive."
    i "And I guess I actually really want you to like me after all."
    i "So I guess I’ll stop being immature for the next few minutes."
    s "You seem to be doing a lot of guessing right now."

    scene firstbath14
    with dissolve

    i "Always am. Just the way I’ve become, I suppose."
    i "Second guessing even the most obvious answers."
    s "Well, whatever the case, you’re free to be as self-destructive as you want."
    s "Just don’t hold it against me if I can’t help you when you need me most."
    s "I have an admittedly hard time resolving things."
    i "And I have an admittedly hard time accepting help, so that’s probably good for both of us."
    i "As long as we can keep talking like this, I’m pretty sure I can keep the treadmill running."
    i "It would hurt like hell falling off and getting thrown across the room, so I’ll definitely avoid that any way I can."

    scene firstbath6
    with dissolve

    i "As far as the bathhouse goes, though, I really {i}did{/i} just wake up and walk here."
    i "Just not in the way you might be expecting."
    s "Wait, what?"

    scene firstbath15
    with dissolve

    i "Hehehe~ Nothing! Just ignore that."
    i "Just a little metaphor I thought up on the spot so my cop-out answer would become less...cop-outy. "
    s "..."

    "I break out my hidden dictionary of metaphors and try to figure out what Io means by that."
    "I give up somewhere near page 23 and stop attempting to decode what a confusing girl like her could possibly be thinking."
    "I settle on something close to “turning over a new leaf” and don’t bother digging any deeper."
    "Sometimes, what’s buried beneath the surface isn’t worth uncovering."
    "This could very well be one of those cases."

    s "Well, as long as you keep coming here, I’ll keep coming here as well."

    scene firstbath14
    with dissolve

    i "Wanna apply for a part time job? I could show you how to scrub the floors."
    i "We could use a few more hands around here, anyway."
    s "As much as I’d love to...scrub floors...my current job already takes up most of my time."
    i "You sure? Cause you’d get an employee discount that would stack on top of the one I already gave you and you’d basically get to bathe for free at that point."
    s "I can already bathe for free at that place called “home.”"

    scene firstbath16
    with dissolve

    i "Sorry, Sensei, but we’re not all fortunate enough to have one of those."
    i "Luckily, I’ve got the dorm now. And that’s starting to feel like one, slowly but surely."
    i "Even if no one wants to talk to me and I don’t want to talk to any of them."
    i "It’s a place I can lay my head and fall asleep without the worry of burdening anyone."
    i "A worry that I probably shouldn’t have somewhere like this, but that I still can’t seem to shake."
    i "Nonetheless, I’m here."
    i "Surrounded by bathwater and body scrubs."
    i "Making the best of what I have-"
    i "Even if that is absolutely nothing."

    scene black
    with dissolve2

    "Io and I talk for a little while longer."
    "It’s hard to tell when it becomes dark due to the blacked out windows but, at some point, it does."
    "And that part arrives just before I realize I’ve spent far too much time here and decide to head back outside and find something else to do."
    "As I leave, Io smiles."
    "I don’t know whether or not the smile sticks around the second I make it outside."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse1 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label bathhouse5:
    scene ioyuki1
    with dissolve
    play music "normalday.mp3"

    "I show up at the bathhouse to find Io happily humming to herself and scrubbing away at the floor with a brush basically the same size as her."
    "There’s no one else around at the moment (That I can see, at least) and the volume from some sports broadcast is turned up loud enough that she doesn’t hear me enter."
    "It looks like she’s in a good mood, though."
    "I never really know what I’m going to be getting into when I go see her, but at least I’ve been given a sign of good things to come in that childish smile of hers."
    "Probably. "
    "To be fair, I’m half-expecting her to make everything awkward and uncomfortable the second our conversation starts."
    "She’s quite good at that, if I’ve learned anything about her by now."
    "Which I think I have."
    "Again, probably."

    i "So is staring at [high_school] girls a hobby of yours or something?"
    i "This is the second time I’ve caught you just looking at me and not saying anything."
    s "I should have known you saw me walk in. The volume of the TV deceived me into thinking you somehow didn’t."

    scene ioyuki6
    with dissolve

    i "Of course I saw you. You’re impossible to miss."
    i "Do you have any idea how many people of your size come in here? Like, none."
    i "Well, obviously at least one. But you get what I’m saying."
    s "Yes, I am tall. Thank you for noticing."
    i "So, here to hang out with me? Or are you actually going to use the bath this time?"
    i "If it’s the latter, you’re going to have to wait a little while. I’ve got someone in the men’s section right now."
    s "I mean, I’m not {i}opposed{/i} to sharing, but I kind of just came here for you anyway."
    i "Well good, because the girl in there doesn’t really like people intruding on her private time."

    if bonus == True:
        s "Now that I have confirmed it is a woman, I would like to reinforce that I {i}really{/i} do not mind sharing."
    else:
        s "What if I like...wore a blindfold and stayed really far away or something? I'd have no intention of peeking, but this woman sounds safer than the ones I normally associate with."

    scene ioyuki3
    with dissolve

    i "Sensei, I literally {i}just{/i} told you she likes being left alone."

    if bonus == True:
        i "Just because I like you and I’ve seen your penis doesn’t mean I’ll let you walk all over me."
        s "Then you’re already far too advanced for me to comprehend. That combination normally works wonders."
        i "You know, I’m glad that you’re starting to open up to me the way I open up to you...but lengthy conversations about your sexcapades are not really a thing I’m interested in."
        s "Then what {i}are{/i} you interested in? Besides scrubbing the floors of a bathhouse, I mean."
    else:
        s "I don't like how hurting my feelings is becoming your new hobby."

    scene ioyuki4
    with dissolve

    i "This isn’t a hobby. I do this to make money and help my aunt."
    i "My real hobbies are stuff like...baseball and...camping."
    i "Actually, I’ve got quite a few hobbies now that I think of it."
    i "I also like hiking...and building stuff...and those cool serial killer documentaries they have on Netflix."
    s "And not a single “girly” thing to be found."

    scene ioyuki5
    with dissolve

    i "Uhh...isn’t that a little sexist?"
    i "You’re not gonna make fun of me for not being into the same sort of stuff Uta is into, are you?"
    s "Oh, not at all. If anything, your interests are easier for me to understand than hers. "
    s "It’s actually kind of refreshing seeing someone who’s into such...normal things."
    i "Putting it that way just makes me sound boring..."
    i "Where are you trying to go with this?"
    s "No clue. "
    s "How’d you get into all of that, though?"

    scene ioyuki6
    with dissolve

    i "It’s just what I’m into, you know? There doesn’t have to be some long backstory about why I like baseball. I just...like baseball."
    i "It’s that simple."
    s "Fair enough. I was just opening up a window for you to talk more so I don’t feel pressured to think up a conversation topic."

    scene ioyuki5
    with dissolve

    i "It’s been five minutes and you’re already struggling with that? You’re even worse than me, Sensei."
    s "True, but at least I try."

    scene ioyuki7
    with dissolve

    i "Heheh~ True."
    i "At least you try."
    fv "Io! Can you spot me some of that conditioner I like?"

    scene ioyuki8
    with dissolve

    yu "You know, the one in the black bottle that smells like-"

    scene ioyuki9
    with dissolve

    yu "Oh."
    yu "What are you doing here?"
    s "I was about to ask you the same question."
    i "We’re out of the one you like but we should have more by Monday. "
    i "Want me to get my personal bottle from upstairs for you? It’s basically the same thing."

    scene ioyuki10
    with dissolve

    yu "Nah. I’ll survive without it. No need to go out of your way for me."
    i "You sure? I don’t mind if it’s for you."
    yu "Yeah, I’m good. No worries."
    s "I take it you two are familiar with one another?"

    scene ioyuki11
    with dissolve

    i "This is the girl I was talking about before- the one who likes being left alone."
    i "But I take it you two...know each other in some way?"

    if bonus == True:
        yu "Yeah. He’s boning my daughter."
    else:
        yu "Yeah. He hugged my daughter."

    scene ioyuki12
    with dissolve

    i "Uhh...come again?"

    if bonus == True:
        s "Okay, hold on a second. I am not {i}boning your daughter.{/i} She’s just a student in my class and I’m helping her find a job."

        "I would absolutely bone her if given the opportunity, though."
        "But I’d bone pretty much anyone if given the opportunity and-"
        "This is not a thing I should be thinking right now."
    else:
        s "And I'd do it again, too."

    i "Wait wait wait wait wait. Yuki’s daughter is in our class?"

    scene ioyuki13
    with dissolve

    yu "So I hear."
    yu "Smartass lookin’ girl. Probably wearin’ that same old long-ass skirt I used to wear when I was in[school]."
    i "Long skirt..."
    i "Wait, Yumi?"
    i "Holy shit, how did I not realize this?"
    yu "Probably better off not tellin’ her we’re close. She’ll just get pissed off and threaten to beat your ass or somethin’."
    s "Yup, definitely sounds like Yumi."

    scene ioyuki14
    with dissolve

    yu "Yeah. I’m sure you know all about her, don’t you?"
    s "As her teacher, not her lover."
    i "I’m gonna stop you two right there since I feel like this is skirting into uneasy territory."

    scene ioyuki15
    with dissolve

    yu "Hah...Yeah."
    yu "No use talkin’ about that shit right now. "
    yu "Still weird findin’ out you’re in the same class as my kid, though. "
    yu "Knew you switched[school]s but didn’t think a coincidence like that was gonna pop up."
    i "I’m more interested in whatever coincidence brought {i}you two{/i} together."
    i "It’s like a weird little family reunion we’ve got going on right now. Just none of us are related and one of us is naked."
    yu "Not naked...Got a towel on."
    s "We bumped into each other at a ramen shop one day."
    s "And then again at...that same ramen shop."
    yu "I don’t go many places, alright? Give me a fuckin' break."
    i "Oh, okay. Okay. So you’re not really {i}friends{/i}, just acquaintances."
    s "Something like that, sure."

    scene ioyuki16
    with dissolve

    i "Which means you probably haven’t seen {i}that{/i} yet."
    yu "That?"
    yu "You have any idea what she’s talkin’ about?"
    s "How would I know? You’re the one with {i}that{/i}."
    yu "I don’t even know what {i}that{/i} is. How am I supposed to know I actually have it?"

    scene ioyuki17
    with dissolve

    i "Yuki! Show him your tattoo!"
    yu "Ooooooh, {i}that{/i}."
    s "Again, Yuki and I are hardly acquainted and there’s no way she’d-"
    yu "Sure."
    yu "Long as I can do it in the men’s locker room and not out here in the co-ed one."
    yu "Not really a thing I want most people seeing."
    s "Wait, really?"

    scene ioyuki18
    with dissolve

    i "Yay!"
    yu "What’s wrong, man?"
    yu "You ain’t the type to get all nervous and shit when a girl takes her clothes off, are you?"

    if bonus == True:
        s "Quite the opposite, actually. "
        yu "That’s kind of just as bad."
        yu "Just don’t touch me and we’re good."
        yu "It’s on my back so it’s not like I’m showin’ you my tits or anything. Just totally normal shit."
        i "Woo! Let’s get you two into the locker room! It's game time!"
    else:
        s "I am. Girls intimidate me and often make me feel very small."

    scene black
    with dissolve2

    "Io locks the entrance to the bathhouse so no one can come in and then immediately shows us to the men’s locker room."
    "And when I say “shows us to” I mean she gets behind me and pushes me inside."

    if bonus == True:
        "I’m not sure why. I would have gladly walked in on my own."
        "Even if it’s just from behind, the chance to see Yumi’s mom without clothes on is an opportunity I would never miss out on."

    "........."
    "......"
    "..."

    scene ioyuki19
    with dissolve

    yu "Remember, touch me and I’ll cut your fucking hands off."
    s "Deal. "
    i "That’s right. Only {i}I’m{/i} allowed to touch Yuki."
    yu "Io ain’t allowed to touch me either."
    i "I’m going to anyway. Watch."
    yu "Let’s just get this shit over with. "
    yu "It ain’t even that impressive. "

    scene black
    with dissolve

    "Yuki turns around and begins to slowly lower her towel."
    "It isn’t until it gets halfway down her back that I {i}really{/i} notice how pale she is."
    "Paired with the fluorescent light, she’s almost like a ghost."
    "........."
    "......"
    "..."

    scene ioyuki20
    with dissolve

    "Her towel stops just as it reaches her ass (An anticlimactic finale, I know) and I’m suddenly faced with a Yakuza-esque tattoo taking up her entire back."
    "I’m sure this is part of the reason why she takes up this side to herself whenever she’s here."
    "There aren't a lot of Japanese people who'd be willing to...overlook something like this."
    "But I-"

    s "I think it’s-"
    i "SO COOL!"

    scene ioyuki21
    with dissolve

    "Io appears before I’m able to finish my train of thought and places her hand directly on Yuki’s back."
    "I’ve gotta say, for someone who doesn’t like girls, she seems to be handling her, of all people, rather well."
    "But I guess Yuki isn’t exactly the most feminine person around."

    yu "Hah..."
    yu "You’re lucky I like you, Io."

    scene ioyuki22
    with dissolve

    i "Sensei! Isn’t this like, the coolest thing you’ve ever seen?"
    i "The first time I saw it was actually on the camera and I was so impressed that I ran out to meet her in the bath."
    yu "Fuckin’ horrible first impression."
    i "Oh, I was the absolute worst. I know."
    i "But it was so awesome that I couldn’t stay away."
    yu "Well I’d be more than happy to give it to ya if that were possible."
    yu "Shit’s a fuckin curse, if ya ask me."
    i "Sensei, do you think I’d look good with a tattoo like that?"

    if bonus == True:
        s "I’d have to see you without a shirt on first to figure that out."
        yu "Hey. Don’t forget I’m still here."
        yu "If you two are gonna fuck, go do it on the girl’s side. I still need to take a bath and I don't wanna watch that shit."
        i "I think I want one but like, not as big as Yuki’s."
        i "It doesn’t have to be on my back, either. Anywhere would be fine."
        i "Oh! We should get them together!"
        i "Sensei, let’s go get tattoos!"
        s "Uhh...Yeah, I think I’m good."
        yu "Aight, time to beat it, you two. Still dry as fuck and not feelin' it."
        yu "Kinda ruinin’ my me-time right now."
        i "Fine, fine. We’re leaving."
    else:
        s "No, your body is a temple and you should not disgrace it with such atrocious art."
        yu "Dude wtf"

    scene ioyuki23
    with dissolve

    i "Thanks for showing Sensei your tattoo, Yuki!"

    if bonus == True:
        i "I know how long it’s been since you’ve taken your clothes off in front of a man and-"
        yu "Get...out..."
        i "Yes ma’am!"
    else:
        yu "Wtf"

    scene black
    with dissolve2

    "Io quickly scurries out of the room, picking up her floor brush as she does so."
    "I follow behind her and the two of us quickly return to our earlier conversation once we’re in the lobby again."
    "She goes back to talking about her hobbies and how much she apparently likes body art and-"
    "After another thirty minutes of that, Yuki rejoins us."

    scene ioyuki24
    with dissolve

    yu "You’re still here? Don’t you have like, shit to do or whatever?"
    yu "Yumi have a job yet?"
    s "No shit to do and I’m not sure what Yumi is up to right now."
    yu "Well that makes two of us then."

    scene ioyuki25
    with dissolve

    yu "Uhh..."
    yu "Listen."
    yu "I know this will probably sound fucking dumb or whatever but like..."
    yu "If you’d want to meet up at the ramen shop again sometime and talk about her...or other shit, that would be cool."
    yu "I kinda still owe you for payin’ for me the first time...so it would be on me."
    yu "Just don't buy anything fuckin' expensive. I'm not made of cash."

    "Yuki proceeds to tell me her phone number and I give her mine in return."
    "We don’t make any concrete plans or anything so I guess I’ll just...call her whenever I call her."
    "I have to say, this is definitely not how I envisioned myself acquiring her number."
    "Hell, I didn’t envision that at all, to be honest."
    "But it’s a thing I have now, so I might as well get to know her."

    $ yukinumber = True

    "{i}Congratulations! You now have Yuki’s number!{/i}"

    scene ioyuki26
    with dissolve

    "After entering my number into her phone, Yuki nods at Io and heads outside..."

    i "..."
    i "So...Yuki, huh?"
    i "You ever gonna call her?"
    s "Maybe."
    s "You don't have a problem with that, do you?"
    i "Why would I have a problem? She gave it to you so you can do whatever you want with it."
    i "Call her, don’t call her. Not up to me."
    i "She’s not...a bad person or anything. I like her a lot."
    i "So it would...only make sense if you liked her too."

    scene ioyuki27
    with dissolve

    i "Sorry. I’m probably being weird. Am I being weird?"
    i "Yeah, I’m definitely being weird."
    i "Let’s just go back to talking about normal stuff again."

    scene black
    with dissolve2

    "At her behest, Io and I return to standard banter and, before long, it’s time for her to go on break."
    "I offer to walk around the city with her for a little while to help kill time, but she adamantly refuses going out in the cold as she doesn’t want to get dressed."
    "I don’t blame her. Getting dressed is horrible."
    "Wearing pajamas out in public should be socially acceptable. It would solve so many problems."
    "But that has nothing to do with where I’m going now, which is-"
    "..."
    "Huh."
    "Where am I going again?"

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse5 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label bathhouse10:
    scene bathhouseten1
    with fade
    play music "normalday.mp3"

    "I head over to the bathhouse to find Io and Yuki hanging out at the counter."
    "And, judging by Yuki’s skin being significantly less pale and lifeless than usual, I think it’s safe to assume that she is on her way out."
    "I apologize to Yuki inside of my head for making fun of her skin. I wish her the best in her journey back to health."

    if bonus == True:
        yu "Yo. Five minutes earlier and you would have gotten to see me nude."
        s "Damn it. I knew I should have run here."
    else:
        yu "Yo."

    i "Hey, Sensei. Welcome back."
    i "Yuki was just leaving."

    scene bathhouseten2
    with dissolve

    yu "Was I? Cause I’m pretty sure I was planning on making fun of you for losing to my daughter a little more."
    i "Nope! You were just leaving. Bye, Yuki."
    s "I take it this means you told her about the dorm war results?"

    scene bathhouseten3
    with dissolve

    yu "See? Told you Yumi was going to win if all that had to be done was cooperate or whatever."
    yu "Io’s less of a brat, but she’ll never cooperate with anyone or anything. Just the kind of girl she is."
    i "Yes. I am a pitiful isolationist. Why are we still talking about this?"
    yu "Cause I’ve gotta brag to your fuckin’ teacher on my way out."
    i "What will that accomplish, though? It's already over and done with."

    scene bathhouseten4
    with dissolve

    yu "It won’t {i}accomplish{/i} shit. It’s just fun."
    i "This is the last time I let you use my shampoo."
    i "Your bill is six million yen. Please leave the money on the counter and be on your way."
    yu "Nah, hold on a sec. Just cause I want to brag about how I was right doesn’t mean there’s no lesson on the way for you."
    i "Can we maybe leave the lessons to my teacher?"
    s "No. Go ahead, Yuki. I don’t particularly enjoy teaching anyway."
    yu "Then change your fucking career, dude."
    i "Ugh...what’s the “lesson” I have to learn today, Yuki? Just get it over with."

    scene bathhouseten5
    with dissolve

    yu "The lesson is that you’re completely fucked if you’re not even going to try and win winnable battles."
    yu "The hell is wrong with cooperating? What happened to all that shit about you being fake as hell or whatever it is you’re always saying?"
    yu "Wouldn't being fake mean sticking your neck out for your team even though you don’t want to?"
    i "You’re forgetting the very important detail of me also being a hypocrite. "
    i "So yes, I am incredibly fake in many respects. But I am fake on my own terms. Which means not getting involved with a bunch of sentient handbags."
    yu "Yumi might be a brat, but she ain’t a fuckin’ handbag."
    i "Yumi was on the other team. And she like, won by default or something. So it’s not like it was even a deserved win."
    i "Also, why are we still talking about this?"
    yu "Just fuckin’ shape up, kid. Ya ain’t gonna be happy if you’re so dead set on never doing anything for the rest of your life."
    i "Then I guess I’m never going to be happy. Thanks, Yuki."

    scene bathhouseten6
    with dissolve

    yu "Man, do you really deal with this shit every day?"
    s "Not really. In true Io fashion, she doesn’t really talk while she’s in[school]."
    yu "Beat. Just means she’s missin’ out on forging new friendships and all that."
    s "Yes. At this rate, Io will never have any bond as strong as the one between you and me, Yuki."

    scene bathhouseten7
    with dissolve

    i "I have Uta!"
    i "And besides, you two aren’t even that close!"
    yu "Sure we are. Your teacher and I chill all the time now. He practically has me on speed dial."
    i "Speed dial isn’t even a thing anymore! Probably."
    i "If it is, I have no idea how to use it."

    scene bathhouseten8
    with dissolve

    i "But that doesn’t matter! "
    i "You two can get as close as you want. I don’t care."
    i "But rubbing it in my face isn’t going to make me think, “Oh. Time to turn things around and be a normal member of society.”"
    yu "We can get as close as we want?"

    if bonus == True:
        i "I mean, I’d prefer that you didn’t because it would make things extremely awkward for me and I really don’t want to clean up whatever mess you would leave behind in the men’s bath-"
    else:
        i "Yeah. You can even...{i}hug{/i} if you want."

    scene bathhouseten9
    with dissolve

    yu "Uhh...okay. No need to get graphic. I obviously wasn’t being serious."

    "Damn it."

    i "But still...I don’t care. Do whatever."
    i "Also, the whole thing with the speed dial wasn’t even fair since Sensei doesn’t have my phone number yet."
    s "You know there’s a very easy way to change that, right?"

    scene bathhouseten10
    with dissolve

    yu "You really askin’ a [teenage]girl for her number right in front of me? "
    s "Yes, because you and I have an unbreakable bond and you will not judge me for it."
    yu "That was just...yeah, aight. Whatever."
    i "I’d be more than happy to give you my contact information. I was just under the impression you didn’t want me to have {i}yours{/i} since I would annoy you all the time."
    s "You already annoy me all the time. A little more won’t hurt."

    scene bathhouseten11
    with dissolve

    i "Really?!"
    s "Oh, wow. You're really that excited about this?"
    i "I am! Because now I can shove it in Yuki’s stupid face and start my own inseparable bond with you!"
    yu "The fuck just happened? We were teasing her like two seconds ago and now you guys are legit flirting."
    s "It’s not flirting. Io just really likes me for some reason."

    scene bathhouseten12
    with dissolve

    yu "Yeah...weird."
    yu "You ain’t hiding a dragon tattoo anywhere on your body, are you? Only time I’ve seen her get that excited is when she got to touch mine."
    s "No, but...I’ve also never looked at my back, so..."

    scene bathhouseten13
    with dissolve

    i "Want me to check for you?"
    i "My hands are cold and callused and I can’t imagine they’ll feel very good if I touch you but, so long as you don’t turn around, it should be fine."

    if bonus == True:
        s "What’s wrong with turning around when you’ve seen my penis before?"

    scene bathhouseten14
    with dissolve

    yu "Okay, that’s enough for me."
    yu "Enjoy your new unbreakable bond or whatever. I’m gonna go load up on ramen and probably pass out on my bike."
    i "Night, Yuki. Thanks for inadvertently becoming the bridge Sensei and I needed to exchange contact information."
    yu "Kids are fuckin’ weird now."

    scene bathhouseten15
    with fade

    "Yuki leaves the store and I get a little closer to the counter."

    if bonus == True:
        s "So, about my penis."
        i "Weird segue."
        s "Does this bathhouse provide any sort of “extra services?” Because that's what you made it sound like just now."
        i "Nope. But I’m sure one of the imaginary old ladies playing mahjong in the back room that we don’t have would be happy to help you out for the right price."
        s "So that thing about your hands being cold and callused or whatever-"
        i "Grave misinterpretation. I was just talking about washing your back."
        s "Well, it would certainly make sense why I’m not supposed to turn around then."
        i "Right."
    else:
        s "Do you guys sell M&M's here?"
        i "What? No."
        s "I really want them, though."
        i "..."
        s "Please?"

    i "Anyway, can I give you my number now?"

    if bonus == True:
        s "Oh, cool. We got over that misunderstanding a lot quicker than I thought we would."
        i "It comes with the job. Gotta be ready for stuff like that."
        i "Number?"
        s "..."

    s "Sure."

    scene black
    with dissolve
    stop music fadeout 10.0

    "I slide my phone across the counter to Io, who programs her number into it and sends herself a quick text message to-"

    s "Wait, why did you send a heart?"
    i "First emoji I saw. Definitely not going to look at it all the time and tell myself that you like me or anything."
    s "That’s a strangely specific and unwarranted thing to clarify."
    i "Yes. Yes it is."
    i "Now! Right this way, sir! I will show you to your bath!"

    $ ionumber = True

    "{i}Congratulations! You now have Io’s cell phone number!{/i}"

    "Io quickly pushes me through the curtain and into the men’s locker room, completely disregarding her responsibilities as an employee of this establishment."
    "I’m going to have to file a complaint."

    if bonus == True:
        scene bathhouseten16
        with dissolve2
        play music "io.mp3"

        s "This is strange behavior for someone who refused {i}additional{/i} service to me just seconds ago."
        i "Feel free to undress whenever you’d like."
        s "Are you actually going to wash my back?"
        i "Nah. We don’t do that here either."
        s "But you {i}do{/i} escort customers to the locker room and watch them get undressed."
        i "Only one customer has received this “escort” you speak of, and I wasn’t planning on watching you."
        i "I was just gonna close my eyes and talk to you while you relaxed or something."
        i "I don’t know. It seemed less weird in the lobby where the TV was on and everything wasn’t completely silent."
        i "Should I leave? "
        i "I should leave."
        i "I’m gonna leave."
        s "You don’t have to leave."
        s "Just think of it as...payback for you getting undressed in my hotel room or something."
        i "Except I was in wholesome onesie pajamas afterward and you’re going to be...not wearing those."
        s "It would be an extremely funny surprise if I was, though."
        i "No, it would be gross and weird. Save the cute pajamas for me."
        s "Io, please explain to me what’s happening right now."
        i "The bad parts of me are waging war with good parts of me. Which are waging war with my hormones. Which are, in turn, waging war with my greatest fears."
        i "Basically, I’m being Io again. Yay."
        i "I don’t know. This is weird."
        s "Am I taking a bath or am I not taking a bath?"
        i "I...guess that depends on if you want to take a bath?"
        s "I mean, that wasn’t the intention when I came here..."
        i "Am I forcing you into doing something you aren’t comfortable with?"
        s "Are you forcing {i}yourself{/i} into doing something you aren’t comfortable with?"
        i "I’m just trying to spend time with you in a way that won’t tire you out."
        i "I’m exhausting, right?"
        i "And I figure that if you’re warm and cozy and wet and stuff, you’ll be a little less annoyed by all of the talking I’m going to do."
        s "And you’re not just saying that to compensate for something you’re realizing now is flat out odd?"

        scene bathhouseten17
        with dissolve

        i "So it’s odd because it’s me."
        s "It’s odd in general."
        i "But it wasn’t odd when you came here with that blonde girl."
        s "Okay, valid point."
        i "I mean...it’s not like I’m going to be {i}in there{/i} with you, you know? I’ll be turned around, talking about...stuff."
        s "Which, in theory, we could have just done in the lobby."
        i "But I already said all that stuff about you being relaxed and warm. So isn’t that like, a preexisting counterpoint?"
        s "It sounds like more of an unplanned rationalization to me."

        scene bathhouseten18
        with dissolve

        i "Then it fits me perfectly!"
        s "Io-"

        scene bathhouseten19
        with dissolve

        i "The fact that you’re still talking makes this a million times worse than it would be if you just...did what you wanted rather than wait for me to do something."
        s "..."

        "She’s right."
        "That’s what I’m {i}supposed{/i} to do after all."
        "Why bother trying to fix situations that I did not personally break?"
        "I’m here at a bathhouse. Which means I should take a bath."
        "And if anyone is there to awkwardly try and hold a conversation with me as it happens, that’s on them."

        s "You’re weird."

        scene bathhouseten20
        with dissolve

        i "Yeah..."
        i "Yeah, this was a bad idea."
        s "Nah. Just close your eyes."
        i "..."
        s "..."

        scene bathhouseten21
        with dissolve

        i "..."
        s "..."

        scene black
        with dissolve2

        "Io does as she’s told and closes her eyes."
        "I take a moment to awkwardly remove my clothes several feet away from a cute [teenager], something I’ve done hundreds (If not thousands) of times in the past."
        "But something feels different about this time in particular."
        "Like it’s something that neither of us particularly {i}wants{/i} to do, but something we’re doing nonetheless."
        "I don’t even have an erection."
        "It’s just a bath."
        "That’s all it is."

    play sound "water1.mp3"

    "I get into the water and let my body soak in both chemicals and uncertainty."
    "And I hear a stool dragged across the stone floor just moments later."

    scene bathhouseten22
    with dissolve

    i "Is it hot enough?"
    s "It’s fine."
    i "Okay..."
    s "..."
    i "..."
    i "So, uhh...Yuki."
    s "Is that going to be our conversation topic for the night?"
    i "It’s just the first thing that came to mind."
    i "Well, the first thing actually worth talking about that came to mind. "
    i "There were a lot of other things that popped into my head beforehand, but they were all either stupid or pointless."
    s "So...Yuki, then."

    scene bathhouseten23
    with dissolve

    i "Her and Yumi..."
    i "Could you...tell me a little about them?"
    s "Why not ask her?"
    i "I’ve tried. But she always gets this look on her face that’s like a mix of...regretful and defeated."
    i "And I don’t want to make her talk about things that will obviously upset her."
    i "And...given Yumi’s general demeanor, I’m starting to think that maybe Yuki wasn’t really as great back then as she is now."
    s "She’s had her fair share of problems. They all make sense given the situation she was brought up in, though."
    i "I see..."
    i "And...do you think that situation justifies anything that she may have done?"
    s "Of course not. The justification of tragedies like that is an inevitable result of a seemingly infinite desire to be forgiven shared by nearly all humans."
    i "Yeah...Yeah, it is."
    i "What is it you want to be forgiven for, Sensei?"
    s "..."
    s "Everything, I guess."
    s "I just don’t want to put in the work required to actually {i}be{/i} forgiven."
    s "And you?"
    i "Everything, I guess."
    i "I’d just rather hide from all of it because it’s exhausting even confronting things you don’t like looking back on."
    s "Does it make you feel any less alone knowing you’re not the only one going through that?"
    i "No."
    i "But I like being alone."
    s "So do I."

    scene bathhouseten24
    with dissolve

    i "But...you spend virtually all of your time with other people. I barely ever even get to see you."
    s "Being with other people is easier."
    s "When you’re alone, it’s a lot harder to ignore the parts of yourself you want forgiveness for."
    i "I think this is where our paths start to change directions."
    i "When I’m alone, I can focus on whatever I want."
    i "I can build things. Or read. Or watch baseball."
    i "Or I guess text you now that I finally have your phone number."
    i "But when I’m with anyone else, it’s like I’m constantly being reminded of everything I hate about this world."
    i "And I understand that it’s irrational to live this way and that it will greatly increase the amount of stress I have and lead me to an early grave..."
    i "But there are some things that you can’t change. Or things you wouldn’t want to change."
    i "Like...you, for example."
    i "You’re just as fucked up as I am on the inside, but I’d hate for you to be anyone other than who you are."
    s "Or who you think I am. You barely know me, all things considered."
    i "I don’t need to know your story to know who you are. "
    i "So long as you can understand where I’m coming from and I can understand where {i}you’re{/i} coming from, we can be completely different from one another but still exactly the same."

    scene bathhouseten25
    with dissolve

    i "Uhh....Wait. That sounded better in my head."
    i "It's a little too contradictory to put it that way."
    i "But...you understand...right?"
    i "That...we don’t need to know everything about each other."
    s "Of course."
    s "But that will never mean we won’t {i}want{/i} to know."
    i "Yeah..."
    i "Umm...Sensei?"
    i "Is it..."
    i "Is it wrong for me to hope that Yuki and Yumi never patch things up with one another?"
    s "I mean...it’s not really your place to get involved."
    s "Are you afraid of losing Yuki or something?"
    i "No. It’s nothing like that."
    i "I just think I’d have a little more faith in myself if I got to watch others fail as well."
    i "There’s something incredibly vindicating about watching others struggle while you’re struggling yourself."
    i "It’s like turning off all of the lights and letting your eyes adjust."
    i "If you fill your world with sadness, you’ll get used to it and get better at accepting it."
    i "If everything is depressing to begin with, you can manage to find joy in even minor tragedies because, by comparison, they really aren’t as bad as they could be."
    i "I guess I just want more people to turn the lights off."
    i "And for me-"
    s "It’s like everyone is walking into your room and turning them on."

    scene bathhouseten26
    with dissolve

    i "..."
    s "..."
    i "I..."
    i "..."
    s "..."

    scene bathhouseten27
    with dissolve

    i "I..."
    i "Shouldn’t say what I was about to say yet."
    i "It’s too soon."
    s "...?"

    scene bathhouseten28
    with dissolve

    i "When the[school] year ends...do you want to go somewhere with me?"
    s "Where did you have in mind?"
    i "Somewhere far away. Like...maybe America or something?"
    s "We’re not allowed to leave Kumon-mi."
    i "Then...an amusement park?"
    s "What is it with you and amusement parks all of a sudden?"
    i "It could be anywhere."
    i "But...I want to be with you."
    s "Hmm..."
    s "I don’t know."

    if bonus == True:
        i "Why...not?"
        s "I’m not sure how I feel about being with a girl who can look at me while I’m naked and not actually do anything about it."
        i "But my hands are all cold and callused."
        s "Still better than no hands at all."
    else:
        s "Sounds kind of inappropriate."

    i "..."
    s "..."

    scene bathhouseten29
    with dissolve

    i "Okay...that’s enough bathside talk for now."
    i "I’m gonna go back to watching the game. But you’re free to take as long as you want in here."

    if bonus == True:
        i "Also, if you hang around for a few more hours, you might get to see Uta’s boobs through the hole in the fence."
        s "There’s a hole in the fence? Where?"
        i "{i}It’s a mystery.{/i}"
        s "Io, you can’t just tell me something like that exists and then not help me."
        i "I’ll show you if you promise to run away with me one day."
        s "What kind of trade is that?"
        i "One where we both get something we want very badly."
        s "Ugh..."
        s "I’ll just find it myself."
        i "And I’ll keep slowly poisoning myself with unattainable desires."

    i "Enjoy your bath, Sensei."

    scene black
    with dissolve2

    "Io leaves and I suddenly feel a lot more alone than I thought I would."
    "Even the sound of the water is barely audible while I’m not moving around."
    "And since no one seems to be on the other side of the bath right now, I can’t even steal away the opposing share of ambiance."
    "I just soak."
    "In chemicals and uncertainty, I soak and wonder what it is that made Io the way she is."
    "If it was anything at all."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse10 = True
    stop music fadeout 7.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label bathhouse20:
    scene iopresent1
    with fade
    play music "io.mp3"

    i "Oh! Uhh, hi! How are you doing, Sensei?"
    s "I’m...good. "
    s "Why do you seem so surprised to see me?"
    i "Well, you never give me a warning when you’re coming, so I’m kind of always surprised to see you."
    s "Should I be informing you beforehand? Because that’s not really my style."
    i "No no no, it’s fine. I don’t mind at all."
    s "Right..."

    "I show up at the bathhouse (Which is apparently surprising) and immediately head over to the counter to talk to Io."
    "There are a good amount of people moving in and out of the lobby today, so I’m kind of wary about getting in the way."
    "But, at the same time, I’m a little {i}less{/i} wary because all of them are women who have, given the circumstances, probably pictured me naked for at least several seconds."
    "This somehow manages to calm me down."

    i "So...um..."

    scene iopresent2
    with dissolve

    i "So, we’ve got this new scented lotion that’s pretty cool, I guess."
    s "Amazing."
    s "Why are you being so weird?"
    i "Because I’m...always weird?"
    s "Medication again?"

    scene iopresent3
    with dissolve

    i "What? No. I haven’t taken anything today. I’m fine right now."
    s "So you’re just being weird out of habit and not because of an external force."
    i "Also not entirely true. You’re an external force and if I were to pretend you didn’t have at least a minor impact on how I’m acting, I’d be a liar."
    s "Are you..."
    s "Are you hiding something behind your back?"

    scene iopresent4
    with dissolve

    i "Nope!"
    s "What is it?"
    i "Nothing!"
    s "Hand it over, Io."
    i "What if it’s...something really gross? Like a bug?!"
    s "You didn’t take Uta’s pet beetle to work, did you?"
    i "That...depends on whether you’re interested in beetles or not!"
    s "Okay, so it’s not a beetle."
    i "It’s the...scented lotion! So boring, right?! "
    s "It better be something extremely embarrassing if you’re making this much of a big deal about it."

    scene iopresent5
    with dissolve

    i "Ugh...it is."
    i "The truth is, it’s...not really something I wanted to show you just yet. Which is why I was so taken aback when you came in."
    i "Like...another day or two and I would have been totally okay with showing you and-"
    i "Okay, maybe not {i}entirely{/i} okay. But I’d be at least kind of okay. Probably. Maybe."
    s "..."
    i "..."

    scene iopresent6
    with dissolve

    i "It’s just scented lotion. Forget everything else I’ve said up until this point."
    s "Correct me if I’m wrong, but I think a good reason this relationship has been as “successful” as it has been is because you don’t typically hide anything from me."
    i "That’s not true. I hid most of my medication stuff from you when I fell down the other day."
    s "But you also gave me the freedom to grab them and figure out what they were on my own."
    i "Yeah. But that’s just because it would have been light years easier to talk about it or explain things if I didn’t have to make the first step on my own."
    s "You really are a coward, aren’t you?"
    i "I'm absolutely worthless. "
    i "I’ll probably never do anything unless you force me to do it."
    i "Unless it’s like, asking you to go to an amusement park or something. That's something I can do on my own."
    i "Speaking of which, that sounds really good right about now."
    s "Why should I have to always make the first step to compensate for your issues?"
    i "Because if I make the first step, I’ll wind up accidentally tripping and destroying everything."
    s "And if I make the first step, I'll wind up pushing you over."

    scene iopresent7
    with dissolve

    i "Then it appears that neither of us will ever walk again."
    s "Io."

    scene iopresent8
    with dissolve

    i "Okay, fine! I’ll show you!"
    i "But...I should explain first!"

    scene iopresent9
    with dissolve

    i "A while ago..."
    i "In fact, I think it was the first time you ever came into my room...we talked about how...I like building stuff or making stuff and..."
    i "And that sometimes I make things like...toys or figures...or other things like that."
    s "Have you finally summoned the courage to actually start giving your creations away?"
    i "Uhh...not to random orphanages or...real kids or anything like that."
    i "But..."

    scene iopresent10
    with dissolve

    i "But I thought it might be nice if I could...give something to you, since..."
    i "You kind of took the first step back then in helping me realize I should just...go for it."
    i "And...you know, I thought it would be easier this way since it {i}is{/i} just you, but now I can’t help but feel like you’ll think it’s dumb and won’t want to talk to me anymore."
    s "If it's something you personally made, of course I wouldn't do something like that."
    s "A beetle, on the other hand..."

    scene iopresent11
    with dissolve

    i "Are you sure you want it? It’s like...not even done yet."
    i "Like, I was going to put the finishing touches on it while working tonight, so...it’s missing a few of the details and..."
    i "And you’re obviously too old for toys anyway."
    s "Who cares? Even if it’s something I have no use for, it’s something you made for me. "
    s "So, I obviously want to see it."
    i "Even if it sucks?"
    s "Even if it sucks."
    i "Even if {i}I{/i} suck?"
    s "Even {i}though{/i} you suck."
    i "And you’re not gonna just like...grab it and throw it on the ground or something, are you? Because I worked really hard on this one."
    s "That would be the actual meanest thing I could possibly do."
    i "It really would. And you’re not exactly a great person, so you can probably sense my hesitation."
    s "Your hesitation was apparent long before how “not great” I am started to weave its way into the conversation."
    s "Just show me. It’s no big deal."

    scene iopresent12
    with dissolve

    i "It is for me..."
    i "It’s like...giving you a little piece of me that you’ll take with you when you leave today."
    i "And so I’m worried not just about how much you’ll like it, but...what will happen to it."
    i "Is it just going to sit on a shelf and collect dust? "
    i "Will it be thrown into a box of a bunch of other things you feel bad about getting rid of because they’re not things you personally bought, but things that were given to you?"
    i "What if it breaks?"
    i "What if it breaks and you don’t want to tell me about it because it will look like you didn’t care for it as much as you should have, or..."
    i "I...I wouldn’t mind fixing it for you if it breaks. "
    i "I’m...really good at that kind of stuff after all."

    "In typical Io fashion, she’s trying to pull the plug at the last second."
    "The problem is that her paperthin arms, weakened by prescription drugs and apparent malnourishment, are too weak to get it all the way out of the socket."
    "She wants me to help her euthanize her worries because she, herself, is not strong enough to do so."
    "But pulling the plug should be a last ditch effort when all else fails, and she hasn’t failed yet."
    "At least not in my eyes."
    "I’m sure she’s failed in her own eyes time and time again. "
    "And I’m sure that every night when she pulls the blanket over her tiny frame, that is both the first and last thing she thinks of."

    s "I won’t break it, I won’t shove it into a box, and I won’t let it collect dust."
    s "I’m not displaying it on my desk at[school], though, because that would make me look immature and I’ve already cemented myself as the {i}cool{/i} guy."

    scene iopresent13
    with dissolve

    i "I wouldn’t expect you to do something like that anyway."
    i "In fact, I’d much rather you put it somewhere in your room so that I can kind of like...always be there, in a way."
    s "I really appreciate how you can still manage to be so cute despite being a tiny, green bundle of self-deprecation."
    i "And I really appreciate that you haven’t gotten tired of that yet."
    i "And..."
    i "Hopefully...giving this to you means that you never will..."

    scene iopresent14
    with dissolve

    "Io reveals the painted, wooden robot that she’d been concealing behind her back."
    "It’s quite similar to the one she showed me in her dorm room but, at least at first glance, it seems like there is a lot more work put into this version."
    "I’m not sure if she’s just getting better or if she only took extra care of this one because she intended to give it to me-"
    "But I want to believe it’s the latter."
    "In fact, it almost certainly is the latter."
    "Of course she’ll put extra care into something for me when she expects {i}me{/i} to be the person to ultimately save her from herself."
    "Or everything else."
    "To save her from a world she wants no part of, filled with people she wants no part of. "
    "But now I have a part of her."
    "Which is just one small step on the way to all of her."

    i "Are..."
    i "Are you going to...say something?..."
    s "I love it."

    scene iopresent15
    with dissolve

    i "You...you do?"
    s "I do."
    s "It’s obviously not something I can really {i}use{/i} because I am a grown man, but I’ll be happy to keep it in my room."
    i "And you’re not just saying that to make me happy, are you?"
    i "Actually, even if you {i}are{/i} just saying that to make me happy, it’s okay."
    i "I’m...I’m happy."
    i "It’s...the first thing I’ve ever really made {i}for{/i} someone and...I wish it would have been something a little more relevant to you as a person or...your interests, but..."

    scene iopresent16
    with dissolve

    i "I kind of just...think robots are really cute and stuff..."
    s "So, does it have a name?"

    scene iopresent17
    with dissolve

    i "Not yet."
    i "I was gonna give him one when I was like, {i}totally{/i} done. But, like I said...there are still a few more details to put in and..."
    i "And I think that {i}you{/i} should name him instead."
    i "It’s a boy robot, by the way."
    s "I didn’t realize robots had genders."
    i "This one does."
    s "Do you want to help me name him?"

    scene iopresent18
    with dissolve

    i "No...I want you to name him by yourself."
    i "I want you to give him a name that’s...important to you."
    i "It’s a lot easier to get attached to something if you get to give it a name, and...I think it would be really nice if you somehow got attached to this little guy."
    s "..."
    s "In that case..."

    $ robotname = renpy.input("What do you want to name your robot?")
    $ robotname = robotname.strip()

    s "I think I’ll call him-"

    scene iopresent19
    with dissolve

    i "I don’t have to know. "
    i "In fact, I don’t {i}want{/i} to know. Because then {i}I’ll{/i} get attached. And getting attached to a little part of myself sounds really exhausting."
    i "Honestly, I don’t understand how you can put up with {i}any{/i} part of me."
    s "The whole “being cute” thing really helps."

    scene iopresent20
    with dissolve

    i "Take care of Sensei for me...Okay, little guy?"
    i "When he’s sad...when he’s tired...when he’s angry..."
    i "Take all of the bad things that can happen to him and-"

    scene iopresent21
    with dissolve

    n "Sensei? What are you doing here?"
    i "Huh?"

    scene iopresent22
    with fade

    "Noriko and Kirin show up at the counter and the mood completely shifts."

    i "Umm...welcome to-"
    ki "Sensei, get this. Noriko and I were hanging out at my house when one of the pipes burst like {i}seconds{/i} before we were about to take a bath."
    ki "We were gonna just go back to the dorm and shower instead, but then we saw this place on the way back and..."

    if bonus == True:
        ki "Wait, are these baths co-ed? Do you want to get in with us?"
    else:
        ki "Wait, do you want to come back to the dorm with us afterward and watch the third season of Seinfeld?"
        s "Kirin stop."

    scene iopresent23
    with dissolve

    n "Hi, Io. I didn’t realize you worked here."
    i "Uhh...hey."
    s "It’s not co-ed. There’s a girls’ section. "
    s "I think it’s kind of busy right now, though."
    ki "Gotcha. Do you come here often or something?"
    s "More or less. "
    s "Io runs the place with her aunt, so it’s one of the only places I can really see her."
    n "Oooh, what’s that you’re holding? It’s cute."

    scene iopresent24
    with dissolve

    i "This is..."
    i "It’s...nothing..."
    ki "What even is that thing?"
    i "A...robot..."
    ki "Did you like, pick it out of a dumpster or something? It's kinda creepy looking."

    scene iopresent25
    with dissolve

    i "What?..."
    n "..."
    ki "Am I wrong?"
    s "Yes. It’s not creepy at all."
    ki "Do you actually like that kind of stuff, Sensei? "
    n "Wait..."
    n "Did you...{i}make{/i} that, Io?"
    i "I..."

    scene iopresent26
    with dissolve

    i "I found it in the trash."
    s "..."
    n "Really?...I kind of wanted one..."
    i "Bathhouse is...free tonight. Just go through the pink curtain."
    i "I’m...going to go on break..."

    scene black
    with dissolve

    "Io leaves [robotname] at the counter and quickly rushes to the front door without even grabbing her hoodie."
    "I follow closely behind her, trying to stop her from running away the same way she always does, but she immediately notices this and swings around."

    scene iopresent27
    with dissolve

    i "You don’t have to follow me."
    s "I know I don’t {i}have{/i} to. But I’m going to."
    i "Why? I’m probably just going to scream and cry and punch things."
    s "Because if I don’t come with you, you’ll wind up taking what Kirin said to heart despite it being obviously incorrect."

    scene iopresent28
    with dissolve

    i "It’s not {i}obviously{/i} incorrect. If that’s the impression she got, that’s the impression other people are going to get as well."
    i "I should have...practiced more and...gotten better before giving you anything."

    scene iopresent29
    with dissolve

    i "I should have been better..."
    s "Who cares what Kirin or “other people” think? You made it for me and I like it."
    s "I gave it a name and everything."
    i "I’ll make you a new one...with better materials and..."
    s "I don’t want a new one."
    i "..."
    s "So, where are we going?"
    i "You’re..."
    i "You’re still going to come with me?"
    s "Obviously."
    s "Just try and pick somewhere nearby. I wouldn’t recommend straying too far in the cold wearing just that."

    scene iopresent30
    with dissolve

    i "..."
    i "There’s a...bench I normally sit on during my lunch break..."
    i "It’s not far..."
    i "You really don’t have to come, though. It won’t be any fun."
    s "Then we’ll be bored and depressed together."
    i "Wouldn’t you rather be bored and depressed by yourself instead of bored and depressed with some random girl who’s just going to complain and make things sound worse than they actually are?"
    s "Not really, no."
    s "We’ve already uncovered that I mask my downsides by surrounding myself with other people."
    i "But there are two other girls who want your attention right behind you. They’re still looking this way."
    s "That's nice. But I'm looking forward right now."

    if bonus == True:
        i "You can probably see them naked if you stay here."
        s "I can see naked girls any time I want."
        i "Pervert."
        s "You’re wasting precious break time, Io."
        i "..."
        s "..."
    else:
        i "You can probably hug them if you stay here."
        s "I can hug girls any time I want, Io."

    scene black
    with dissolve2

    "Io turns around and leaves the bathhouse."
    "I follow behind her and-"

    s "Wait a second."
    i "...Huh?"
    i "What’s wrong?"
    s "I almost forgot something."

    $ renpy.end_replay()
    $ bathhouse20 = True
    $ io_love += 3

    "........."
    "......"
    "..."
    "{i}Io’s affection has increased to [io_love]!{/i}"

    jump bathhouse20part2

label bathhouse20part2:
    if _in_replay:
        play music "io.mp3"

    scene clearnightsky
    with dissolve2

    "It’s dark by the time we go outside."
    "I didn’t realize how much time had passed...but I guess it always gets dark a little earlier in the winter."
    "Kumon-mi, despite being incredibly different from everywhere else in more ways than you can count, is no exception to that."
    "I silently follow Io as she rounds the corner and heads for whatever bench she normally spends her breaks on, noticing with each hundred feet or so that her disappointment is slowly fading."
    "Like she’s hitting a different stage of life each time she passes under a streetlight, each one bringing with it a brand new, but instinctively reserved outlook on life as we know it."
    "The word “caterpillar” comes to mind."
    "But it’s not the first time I’ve thought of her as something like that."
    "Something absolutely worthless, but with so much room to grow and so much left to give, if she ever elects to give anything to anyone."
    "Anyone other than me, I mean."
    "I’ve already managed to win her over simply by being in the right place at the right time."
    "But who’s to say that our encounter was the last place or the last time."
    "For all I know, someone else could swoop in and take her away the second they seem more valuable or even make {i}her{/i} seem more valuable."
    "The two of us have a lot in common."
    "We’ve accepted our worthlessness and rely on others to make up for what we can’t cultivate within ourselves."
    "Our blood is poisoned and our minds are tainted."
    "And while Io has an entire pharmacy’s worth of pills at her bedside to counteract this-"
    "I have these thoughts."
    "But that’s all I need."
    "Because everything is going to work out."
    "Because life will repeat itself and mistakes will correct themselves."
    "Either that or I disappear."
    "I can’t lose."
    "I’d definitely prefer not disappearing, though."
    "And for Io’s sake, temporary or not, I’m going to continue hoping that doesn’t happen."

    i "Here."

    scene iobench1
    with dissolve2

    "Io props herself onto the edge of a park bench, dragging her knees to her chest and shivering as a gust of wind comes to greet us."
    "I sit next to her and place my {s}unnamed{/s} wooden robot down on the opposite end."
    "A minute or two goes by without any dialogue...but this is fine."
    "I expected this."
    "Any minute now, she’ll revert back to her instinctive self-deprecation."

    i "I really suck, don’t I?"

    "See?"

    s "Why? Because you had a sensible reaction to someone insulting something you worked really hard on?"

    scene iobench2
    with dissolve

    i "Because I dragged you down with me."
    i "Those girls are going to remember this. "
    i "You're probably going to have to explain yourself to them now."
    i "All I did was create more problems for you."
    i "Which means I suck."
    s "I don’t see it as much of a problem. "

    if bonus == True:
        s "Noriko will probably get jealous and Kirin will probably just accuse me of sleeping with you or something."
    else:
        s "Noriko will probably get jealous and Kirin will probably just try to get me to watch Seinfeld or something."

    scene iobench3
    with dissolve

    i "Yeah..."
    i "Not going to lie, that sounds like a pretty big problem."
    s "I think it would be more of a problem for you than it would be for me. No one really thinks highly of me to begin with."
    i "I think highly of you."
    i "It’s not a problem for me since I don’t talk to any of them. They can think whatever they want."
    s "Yeah, I guess it’s kind of hard to be ostracized when you’re already a wallflower."

    scene iobench4
    with dissolve

    i "I suck at being a wallflower too. I couldn’t even win the wallflower contest thing for the dorm war."
    s "I’m pretty sure not winning makes you a {i}better{/i} wallflower."
    i "Hmm...maybe."
    i "Yumi seems to be actively hated, though. While everyone probably looks at me and thinks, “Oh, right. She’s in this class.”"
    i "So I guess I’m in my own category when you look at things that way."
    s "You’re definitely one of a kind. I’ll give you that."
    i "You know..."
    i "You know, I'm sorry for saying this again out of what seems like nowhere..."
    i "But I really think you should break up with that gyaru girl."
    s "The one that you’re well aware I’m not actually dating?"
    i "I’m not well aware of that. I still think it’s technically possible that you’re lying."
    s "Well, I’m not really sure what else I can do to prove to you that I’m not."
    i "You coooooould...start dating me instead?"
    i "I think that might help prove it."
    s "Two minutes ago, you were talking about how just following you would create problems for me...and now you’re suggesting we start dating."
    i "Because I know you won't want to."
    s "And you would?"
    s "I’ve gotta say, you don’t really seem like the type to start any sort of “official” relationship with anyone."

    scene iobench5
    with dissolve

    i "It’s not really something I’ve ever wanted...that’s true."
    i "But I think it would be kind of nice if it were you."
    s "..."
    i "It’d be really hard, though."
    s "Why’s that?"
    i "Because I’d cry a lot. "
    i "And probably freak out on you over a bunch of different things that aren’t your fault or that you can’t control."
    i "Oh, and I have lots of medications that you would probably have to help me pay for. "
    i "And I’d be up all hours of the night banging on stuff when I’m making shelves and dressers and other furniture for Uta."
    s "So we’re moving in together, too?"
    i "I move quickly."
    i "Well, that’s not entirely true."
    i "In some areas I move quickly. In other areas, I’d rather not move at all."
    s "Yeah, this relationship is already exhausting me and it doesn’t even exist."

    scene iobench6
    with dissolve

    i "Um..."
    i "Can I hold your hand?"
    s "Sure. But the second you start calling yourself my girlfriend, I am walking away."
    s "I can not make that same mistake twice."
    i "That was all rhetorical. I know I’m not your girlfriend. And I know I’ll probably never {i}be{/i} your girlfriend because there are a million better choices and-"

    scene iobench7
    with dissolve

    s "Just give me your hand already."
    i "Oh, yeah. Sure. Sorry."
    s "Don’t apologize. Just accept that this is a momentary sign of affection and that it does not mean we are formally dating."
    i "I accept your affection and henceforth agree to not enter into a relationship with you."

    scene iobench8
    with dissolve

    i "But if you change your mind...you can have me."
    s "What kind of “have” are we talking about here? Because that word carries some rather heavy connotations in my dictionary."

    if bonus == False:
        s "And before you misunderstand what I mean by that, I'm referring to hugs."

    i "It means that you get to inherit Io Ichimonji and her six billion pounds of baggage."
    i "And that you need to figure out what to do about it because she’s been trying for years and has solved absolutely nothing."
    s "This isn’t even high maintenance in the lowest way possible anymore. It’s just high maintenance. "
    i "True. But how many other girlfriends could you get right now that could build you a fence?"
    s "I’m sure that line would kill in a dating profile."
    i "Online dating is stupid. Whatever happened to traditional relationships that formed from just...people meeting each other out in public and stuff?"
    s "Half of them ended in divorce."
    i "Oh. Right. That’s a thing. "

    scene iobench9
    with dissolve

    i "Do you think I’m crazy, Sensei?"
    s "I think neurotic is probably a better word."
    i "I think that’s fair."
    i "I know better than anyone how much of a handful I can be."
    i "Thankfully, your hands are really big. And surprisingly soft."
    i "Have you been using our new scented lotion?"
    s "I’m surprised you can feel anything with the amount of calluses on your hands."

    scene iobench10
    with dissolve

    i "Hey! You already know I’m kind of self-conscious about that!"
    s "Does this mean I should let go?"
    i "No! I’ve never held hands with a boy before. I like it."
    s "Have you held hands with a girl?"

    scene iobench11
    with dissolve

    i "I mean...not that I can remember. But I’m sure I’ve held hands with Uta at least once."
    s "Are you two actually closer than you look?"
    i "Are you about to make this weird?"
    s "Making things weird is basically the only way I know how to function in extended conversations."

    if bonus == True:
        s "Why else would I bring up sex so much?"
        i "Because you're trying to groom everybody."

    scene iobench12
    with hpunch

    i "Ow! Hey! Why are you squeezing me?!"

    if bonus == True:
        s "Sorry. Just a reflex."
    else:
        s "This is exactly what I was talking about. I am so weird."

    scene iobench13
    with dissolve

    i "Geez..."
    i "To think a hand this soft could crush mine with almost zero effort..."
    s "I bet you wish you had one of your four boxcutters on you now, huh?"

    scene iobench14
    with dissolve

    i "As if I’d ever go out of my way to hurt you."
    s "If I was truly attempting to crush your appendages, I really hope you {i}would{/i} hurt me."
    i "If you ever try to crush any part of me, I'll probably deserve it."
    s "I don’t think there’s much a person can do to deserve something like that."
    i "I do."
    s "What a quick response."

    i "Quick and easy. "

    if bonus == True:
        s "Like sex."
    else:
        s "Like a Hot Pocket."

    i "You’re making things weird again."
    s "The conversation’s been going on for a while."
    i "Do you want it to stop? Are you already tired of me?"
    s "Not really. But I can’t imagine you’re allowed to stay on break for this long."
    i "Did you actually think this was my break and that I wasn't just running away because I was about to have a panic attack?"
    s "I mean...it could have been both."
    i "I guess it could have."
    i "I’m feeling a lot better now, though."
    i "And I’m sure it goes without saying, but I’m glad you followed me out. Even if it seemed like I might have been trying to push you away."
    i "That’s gonna happen a lot from now on, you know? Times where I say the opposite of how I feel because I’m scared or nervous."
    i "Are you okay with that?"
    s "It doesn’t sound like I have much of a choice."
    i "You do, though. You can abandon me whenever you want and I can’t do anything about it."
    i "I’m definitely at the point where that would really mess me up, though. So...sorry to put all of that pressure on you again."
    s "I’m getting used to it."
    i "Would you like a reward for all of your hard work?"
    s "I already got a robot."
    i "Would you like {i}another{/i} robot?"

    if bonus == True:
        s "How about an Io?"

        scene iobench15
        with dissolve

        i "You already have an Io."
        s "An Io I wouldn’t mind being closer with. "
        i "But you already said you don’t want to date me."
        s "And that’s not what I’m saying now..."
        i "Then...you..."

        scene iobench16
        with dissolve

        i "..."
        i "Oh..."
        i "I think I know what you’re saying, but..."
        s "I’m just messing around."
        i "Yeah. Yeah, I know."
        i "Sorry, it’s just..."
        i "I know it’s not much, but...you can at least hold my hand like this whenever you want..."
        i "Like, even if it’s in class or something. I’m okay with it."
        i "But...anything more right now is..."
        s "Why are you giving me a whole explanation? Just tell me to shut up if I say something you don’t like."
        i "You just...sounded really serious when you...insinuated that."
        i "And I don’t want you to get your hopes up and then get fed up with me if I take too long to do what you want and-"
        s "Shut up."

        scene iobench17
        with dissolve

        i "..."
        i "Okay."
        i "You wouldn’t want me anyway. I’m too scrawny and my hands are all hard. And I have stupid hair."
        s "Your hair isn’t stupid."
        i "You directly told me my hair was stupid once and I still haven’t lived it down."
        s "Stop taking all of my jokes so seriously."
        i "Stop saying everything with the exact same inflection then. It’s hard to keep up."
        s "Welcome to my life. Everything about you is hard to keep up with."
        s "Everyone and everything else, too."
        s "The world moves too quickly."
        i "And in other areas, it doesn’t move at all."
    else:
        s "Can you buy me new wheels for my skateboard? I am trying to look young again."
        i "Sure."

    scene iobench18
    with dissolve

    i "I like you, by the way."
    i "I’m sure I’ve made that pretty obvious. But I feel like now is a really good time to come out and just say it."
    s "I had a feeling."
    i "Like, a lot. "
    i "My heart is beating like crazy right now."
    i "It’s keeping me warm even though it’s like negative a million degrees outside."
    s "Why are you telling me this when you know I’m not going to date you?"
    i "Because now you’ll have no choice but to think about it."
    i "If I didn’t tell you, you’d probably walk home whispering some weird monologue to yourself about how {i}I’m{/i} lost or {i}you’re{/i} lost-"
    i "But now you’ll just think about my stupid hair and my garbage robot and how dating me would be harder than adopting six babies all at once."
    s "You really need to work on selling yourself a little better."
    i "Sorry. I only sell products I’d be fine with using myself."
    i "Have I mentioned our new scented lotion?"

    scene iobench19
    with hpunch

    i "Ah! You’re squeezing again!"
    s "You’ve said “scented lotion” way too many times today."
    i "At least...take a free sample!"
    s "Io..."
    i "Sensei! Stop!"

    scene black
    with dissolve2

    "The two of us head back to the bathhouse and I drop Io off without going inside."
    "There’s a distinct lack of inner monologue on my way home after that."
    "But there are plenty of thoughts about a girl with stupid hair."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse20part2 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ioarchery1:
    scene ioarchery1
    with fade
    play music "summerwind.mp3"

    "The desire to see small girls wielding dangerous weapons beckons me toward the archery club’s morning meeting. "
    "But it is upon the realization of this desire that I transition into wanting to see small girls who are {i}not{/i} wielding dangerous weapons, as doing so detracts from the attention I should be receiving."
    "At least {i}one{/i} teacher is the recipient of such attention, though. But what I don’t like about that is that she probably has just as much of a chance at sleeping with Uta as I do."
    "If only I knew how to use a bow. Maybe then I could launch Cupid’s arrow straight through the heart of everyone here and take them all back to my house for one giant, ponytail-filled orgy."

    w "Your grip on the arrow is too loose. And if you don’t start straightening out your wrist, you’re going to cause serious damage to it."
    u "But I’ve hit the target every single time."
    w "That doesn’t mean you’re not making any mistakes. What good is hitting the target at all if your method in doing so could lead to injury?"
    w "Try it again but focus on your wrist instead of hitting the target. Missing right now is fine so long as you develop proper form."
    u "Are your hands always this cold, Miss Watabe?"
    w "Everything is cold when you’re dead inside. Now, do what I tell you as you’re the one girl here who’s shown any amount of promise so far."

    scene ioarchery2
    with dissolve

    i "Sensei! Good morning. I didn’t realize you were going to be here today."
    s "I didn’t realize {i}you{/i} were going to be here today either. Since when do you participate in literally anything?"
    i "Oh, I’m not participating. I’ve been sitting under a tree and waiting for Uta to finish since we got here."
    i "She’s weirdly adamant about this archery stuff and her desire to drag me down with her has become very annoying."
    i "I did find a really cool caterpillar, though. Hanging out with him was a good use of like, twenty minutes. But I just put him back on the tree since I like you a little more than bugs."
    s "Just a little?"
    i "Or a lot if saying “a lot” gets you to like me more. I also spent twenty minutes figuring out things to say that would make me sound less clingy, but in true Io fashion, I have already given up."
    s "I’m fine with your...adhesiveness. It would just probably be a little smarter to not say things like that in a place where Kirin could easily gain access to a weapon."
    i "Don’t worry, Sensei. I would take the arrow for you."
    s "I was more suggesting that you’d be the one she shoots."

    scene ioarchery3
    with dissolve

    i "Oh, well that’s no big deal. Uta’s a better shot than her and she’d protect me."
    s "Would Uta...not protect me? "
    i "Idunno. Maybe? She does like you. I just don’t know if she likes you enough to murder someone."
    s "Are you saying you {i}do{/i} like me enough to murder someone?"
    i "Sometimes, I think about murdering people for reasons that don’t even pertain to you. So probably."
    s "You’re just a walking red flag, aren’t you?"
    i "Kind of, yeah. I’m surprised you don’t just walk past me at this point."
    s "If you weren’t so cute, I probably would."
    i "My mind tells me that I should be saddened by that response, but my mind sucks so I am going to ignore that and just revel in the fact that I’m cute enough to stop you in your tracks."
    s "..."
    i "..."
    i "Uta’s so cool, isn’t she? I wonder if I’ll ever be able to draw a bow like that."
    s "If only there was some sort of place you could practice."
    i "Yeah...if only."

    scene ioarchery2
    with dissolve

    i "Oh well. Since there’s not, wanna go hang out in the shade where I can say more clingy things without either of us having to worry about some bitch with a side ponytail going rogue and killing us?"
    s "As long as you don’t try introducing me to your caterpillar friend. I’m not very fond of insects."
    i "Cody the Caterpillar would be very upset to hear that, but sure. I can probably keep our little retreat bug-free if that’s what you want."

    scene black
    with dissolve2

    "Io and I sneak away from Uta and Wakana, walking behind the rest of the girls as well in hopes of them not seeing where we’re about to run off to."
    "She takes me behind a small building where I’m assuming they store all of their equipment and slaps the wall of it as if to tell me this is where we’ll be hiding for now."

    scene ioarchery4
    with dissolve2

    "Given the type of person she is, I’m not surprised to find that she’s already uncovered a location concealed from the prying eyes of girls she tells herself she despises."
    "I think whether or not she actually {i}does{/i} is another story entirely."
    "It’s easier to block people out than to let them in, and if you convince yourself that everyone is someone to be hated before even meeting them, you can shield yourself from being let down."
    "But what you shouldn’t be doing along with that is constantly drawing attention to it, for when you doubt yourself to begin with, the last thing you’ll benefit from is the sound of your own voice."
    "Unfortunately, I think Io has gotten so used to the act of blocking things out that, more often than not, the sound of her own voice is the only thing she hears."
    "And if I were her, I’d be annoyed by that too."

    i "So...what do you want to talk about? The weather? The news? What our plans are for this weekend and how we don’t actually have any, so we’re going to spend the entire time with each other?"
    s "Smooth."

    scene ioarchery5
    with dissolve

    i "I can be good at stuff when I want to be. I just don’t normally want to be."
    s "I guess I might be able to free up some time this weekend. Or next weekend. Or some weekend. "
    s "Or whenever I really think about it, I guess."
    i "The fact that I cross your mind at all is already more than I deserve, so whenever works for you is what is best for me."
    s "Other than mornings, apparently. Since you are now defying all expectations and actually coming to club meetings."

    scene ioarchery6
    with dissolve

    i "That’s not something I {i}have{/i} to do, though. I’m just trying to make Uta happy since she’s always going above and beyond for me."
    i "The truth is that I kind of hate archery. I think it’s annoying and stupidly traditional and that the outfits are too hot."
    i "I guess the woodworking on some of the bows is really neat, though. I wonder if I’d be able to make one with a little practice?"
    s "You picked a weird club to join for someone who apparently hates archery."
    i "True. But I hate most things, so I was kind of screwed the moment they announced we {i}had{/i} to join a club."
    i "I tried to get out of it the best I could by just not submitting the paper, but then I realized that being disciplined might mean I wouldn’t get to see you anymore, so I backtracked and just did what Uta was doing."
    i "Seems to be a recurring thing for me, really. Just following her lead since she’s able to actually walk without her feet being chained to giant cinderblocks."
    s "You’re not always following her lead, though. If you were, you’d have more than one friend."

    scene ioarchery7
    with dissolve

    i "Excuse me, good sir. I have {i}two{/i} friends. I just have an unquenchable desire to cuddle and watch movies with one of them."
    s "Does Uta know you feel that way about her?"
    i "Hmm...she does seem like she’d be a good cuddler. I think I’d rather be with someone a little taller, though. Someone with a penis."

    scene ioarchery8
    with dissolve

    s "Well, I sure hope Uta doesn’t have one of those."
    i "It’s funny because I was sure she {i}did{/i} have one of those back in the day. Boy, was that a surprise."
    s "Weird friendship backstory aside, I think it might be good for you if you actually...you know...{i}did{/i} make another female friend."
    i "Pass. I’m content with the one that I have now. Any more would be a fucking nightmare."
    s "What if it was someone like Kirin?"

    scene ioarchery9
    with dissolve

    i "That would be even worse! You suggested literally the last person in class I would even {i}consider{/i} being friends with!"
    s "And why is that?"
    i "Have you {i}seen{/i} how toxic that girl is? There’s so much poison pouring out of everything she says that the whole room starts dying the moment she speaks."
    s "You’re pretty toxic yourself, though."
    i "Do you think I’d seize the opportunity to be friends with {i}myself?{/i} Because that’s the only thing I can think of that would be even worse than Kirin."
    i "One of the key reasons I like Uta so much is that she’s the complete opposite of that. She like, kills toxicity. It’s good for counteracting the things I do."

    scene ioarchery10
    with dissolve

    s "I’m just saying I think you two have a lot in common and that you’d be able to talk without inherently hating one another."
    s "At the very least, it seems like she wants to be friends with {i}you.{/i}"
    i "I don’t really care about what Kirin wants. "
    s "Do you care about what I want?"
    i "Of course."
    s "Just not when it’s something that conflicts with your own personal interests?"

    scene ioarchery11
    with dissolve

    i "Where’s this coming from? I just wanted to hang out with you and have fun. If I wanted to confront my demons first thing in the morning, I would have medicated before leaving the house."
    s "Just a thought. I could have kept it inside but I figured that was pointless since you don’t keep {i}anything{/i} inside ever."

    scene ioarchery12
    with dissolve

    i "I keep plenty inside."
    s "Like what?"
    i "Like how I hate that {i}you{/i} like Kirin when she’s just one out of millions of other fakes wandering around Japan, hoping to find something to make her feel whole."
    i "I also hate her lack of understanding when it comes to people’s boundaries as she would literally {i}not{/i} stop questioning me about you on the way back home from the Christmas party."
    i "But I realize that’s less of a thing I was keeping inside and more of a thing I just didn’t share with you due to lack of timely relevancy. "
    s "She questioned you on the way back home from the Christmas thing?"
    i "Relentlessly. And the vast majority of it was extremely personal. Things no one should just blatantly and unabashedly discuss despite barely knowing one another."

    scene ioarchery13
    with dissolve

    s "Yeah...that sounds like her."
    i "I’ve got...limits, you know? Like, not everything is easy for me to just talk about."
    i "And if I had somebody in my life who was always trying to force that out of me...well, things would suck even more than they do right now."
    s "I get that. But I also think you also have to understand that if things suck right now, they’re going to keep sucking for the rest of forever unless you actually do something about it."
    s "Would you rather get to know someone who’s interested in getting to know {i}you,{/i} despite all of the obstacles you throw their way...or someone who’s shown no interest in you whatsoever?"
    i "The latter. Anyone who shows any interest in me has extraordinarily bad taste."
    s "Try it again but with less self-loathing."

    scene ioarchery14
    with dissolve

    i "But that’s so hard! You’re taking away my most defining trait!"
    s "Yeah, well when your most defining trait is also your biggest weakness as a person, it’s good to peel it back every once in a while."
    s "Being depended on is cool and all and I’m glad that you...think you’re whatever that weird burrowing sperm fish is-"
    i "Anglerfish. "
    s "Yeah, that. I’m glad you’re able to think up weird metaphors about our relationship because it solidifies my sense of importance when it comes to your life and...that’s a thing I think I need."
    s "But I also want you to be able to exist on your own because you remind me of myself and I still don’t really know how to do that."

    scene ioarchery15
    with dissolve

    i "Did you just..."
    i "Did you just open up to me?"
    s "I guess. But I did it more for myself than I did for you."
    s "Watching you “succeed” would be for my own personal benefit at the end of the day. And if getting you to feel uncomfortable in pursuit of that is what it winds up taking, I {i}want{/i} you to be uncomfortable."
    i "Me...making more friends...will somehow make {i}you{/i} feel better about {i}yourself?{/i}"
    s "It’s weird how our minds work sometimes, isn’t it?"

    scene ioarchery16
    with dissolve

    i "That’s so strange. Because any time I think of you forming more relationships, I just get pissed off and jealous."
    s "Not all of my relationships are sexual, you know."
    i "I guess not. But according to Kirin, the ones you care most about are. "
    i "Why she’d somehow spin that into pressuring {i}me{/i} to crumble when she very obviously likes you as well, I don’t get. "
    i "But I guess that all of our minds are little messed up when you start applying actual logic to them."
    s "..."
    i "..."
    i "Is it too much to ask for a brain that doesn’t break down every time you try to use it?"
    s "It’s too much to ask for anything. Life is going to give us what it gives us and all we can do is scarf it down or starve ourselves. There’s no third option."
    i "Life kind of sucks, doesn’t it?"
    s "Why else would we constantly try to distract ourselves from it?"
    i "..."
    s "..."
    i "This was a good talk. I enjoyed this."
    i "I figured I was still like, a year away from learning anything about you. So the fact that I now think I understand something is..."
    i "I guess for lack of a better term-"
    i "A good distraction."

    scene black
    with dissolve2

    "Io and I leave our spot behind the storage building and wander back into the lives of everyone else, knowing full well that our prior distraction had overstayed its welcome. "
    "I’m glad she has another one now, though."
    "What I’m not glad about is that it now feels like a small piece of me is missing."
    "But when I’m the one who ripped it off and so carefully placed it into her hands, I don’t really have any right to complain."
    "When we round the corner, I step on something soft. "
    "It sticks to my shoe and I have to kick the dirt in order to get it off."
    "I won’t tell you what it was."

    $ renpy.end_replay()
    $ ioarchery1 = True
    $ io_love += 1

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump utaarchery1

label bathhouse25:
    scene iosidesbath1
    with fade
    play music "normalday.mp3"

    i "Hah...Okay. I’m done working for today. You can take over now, Sensei."
    s "But I don’t know the first thing about running a bathhouse."
    i "It’s easy. Just do what I do."
    s "You mean complain and talk down on myself while watching baseball and drinking soda?"

    scene iosidesbath2
    with dissolve

    i "Yeah. Just make sure you clean the floors every once in a while and take money whenever someone tries to give it to you."

    "I find myself at the bathhouse- which is apparently now my second workplace."
    "I came here in an attempt to spend some time alone with Io but, as fate would have it, things haven’t really worked out that way thus far."
    "The second school dorm building (You know, the one where every class {i}but{/i} mine lives) has a busted water heater at the moment, meaning that everyone interested in practicing personal hygiene must come {i}here.{/i}"
    "This is not something I knew until showing up. And I really wish it {i}was{/i} because all of those girls know who I am and I can’t imagine seeing me casually hanging out with Io is a good look for either one of us."
    "Which is why, for today only, I have become an unofficial employee of the bathhouse. Though, only in name so I can tell everyone that there’s an actual reason I’m here."
    "When it comes to work, I’ve yet to do anything."

    s "What if we just close early? That’s a thing we should be allowed to do, right?"
    i "You want to close early on what has quickly become the busiest day we’ve had in years?"
    s "Kind of, yeah."
    i "Sounds good to me. Maybe you should just become an actual employee if you’re going to keep coming up with stuff like that?"
    s "I’m just applying the same strategy I use at school to this- work less, not hard."

    scene iosidesbath3
    with dissolve

    i "And what an admirable strategy that is, Sensei. "
    i "When you look at the reality of this situation, the bathhouse has already taken in far more cash than normal."
    i "Which means it should be completely acceptable to cut off that cash flow now in favor of the employees."
    s "Exactly. But also, probably don’t consider starting your own business any time soon."

    scene iosidesbath4
    with dissolve

    i "So! Now that we’re officially {i}unofficially{/i} closed, what do you wanna do? Ready for a bath yourself? "
    s "Are you just saying that because you want to see my penis again?"
    i "Nah. The novelty of your penis has worn off. It’s your ability to appeal to my inner broodiness and the fact that you actually pay attention to me that’s keeping me hooked right now."
    s "First, the novelty of my penis will never wear off. Second, your broodiness is far from {i}internal.{/i} Third, it’s hard {i}not{/i} paying attention to you when everything about you screams “Pay attention to me.”"
    i "Correction: everything about me screams “Pay attention to me, Sensei.” I couldn’t care less as far as everyone else is concerned. "
    s "Yes, you’ve made that quite apparent as well."

    play sound "entrybell.mp3"
    scene iosidesbath5
    with dissolve

    i "Oh, welcome! We’re actually closed right-"

    scene iosidesbath6
    with dissolve

    i "Ah! Yuki!"

    scene iosidesbath7
    with fade

    i "And...some other girl."
    sar "Hey! What are you doing here?"
    yu "Rockin’ the cradle, that’s what."
    s "I actually work here now."

    scene iosidesbath8
    with dissolve

    yu "You what?"
    sar "Hey, what the big deal?! How come you can work {i}here{/i} but not at my bar? "
    s "I’m sorry, Sara. It’s the name of it."
    sar "I take offense to that! That’s {i}my{/i} name too!"
    yu "You actually workin’ here now? What happened to teaching?"
    s "It’s just for today. A bunch of girls from the school are here because of some water issue, so I’m pretending to work here so it doesn't seem weird that I'm hanging out with Io."
    i "Once again, I have inconvenienced Sensei in a way that benefits me! Rejoice!"

    scene iosidesbath9
    with dissolve

    sar "Io? The girl behind you?"
    sar "I knew that you spent some of your free time with Sana and Ayane, but I didn’t realize you were going around and doing that with {i}everyone{/i} in your class."
    yu "Like I said, rockin’ the cradle. Don’t tell me you’re surprised, Sara."

    scene iosidesbath10
    with dissolve

    sar "Well, just don’t go luring them into a false state of security before impregnating them and leaving them to fend for themselves while you run off with somebody else."
    yu "Damn. If I knew you were bringin’ this much baggage, I would’ve suggested stopping at one of those coin lockers on the way over here."

    scene iosidesbath11
    with dissolve

    sar "I’m over it. And hi, Io. I’m Sara. "
    sar "I know I might look 20, but I’m actually Sana’s mom. "
    i "Sana? Do we have somebody in class with that name?"
    yu "Ignore her. She ain’t the type to really make friends."
    sar "That’s fine. Neither is my daughter."

    scene black
    with dissolve2

    "Yuki pulls a wad of crumpled up bills out of her pocket before trying to hand them over to Io, only to have them shoved back in her face seconds later."
    "And seeing as none of the girls from the “main” dorm knew about the men’s side of the bath being open to the highest bidder, it’s currently unoccupied."
    "Which means that, just moments from now, Sara and Yuki will be naked together."
    "I like this and I want to participate."

    scene iosidesbath12
    with dissolve

    "However, a small green roadblock stands in my way."

    i "You guys can take the men’s side. But, just so you know, I’m closing the place up because Sensei thinks it would be best for business if the business part just...stopped."
    s "That is not what I said. But also, yes. "
    yu "Fine by me. Two’s already a crowd when it comes to shit like this."
    sar "Yuki is just embarrassed because it’s the first time she’ll be seeing my naked body."
    i "Yeah, I wasn’t talking to you."

    scene iosidesbath13
    with dissolve

    sar "Wow. Teenagers are really hard to approach now, huh?"
    yu "Ay, don’t be a bitch. Sara’s good people. She’s the one I’ve been working for. "

    scene iosidesbath14
    with dissolve

    sar "Ahh...so this is what it means to have protection from the Yakuza."
    yu "For the last time, I ain’t Yakuza anymore. I’m just Yuki now."
    i "Good. Stay “Just Yuki.” I like Yuki. This other one, I’m still not sure about. "

    scene iosidesbath15
    with dissolve

    sar "Ooh! Here’s an idea! What if we all took a bath together?!"
    i "Strike that. I’ve decided I don’t like her."
    yu "Were you not listenin’ when I just said two’s already a crowd? Three sounds even worse."
    sar "Except it wouldn’t be three. It would be four with Sensei."

    scene iosidesbath16
    with dissolve

    i "Uhh..."
    yu "Ain’t you supposed to like, {i}not{/i} encourage the whole cradle rockin’ thing? Io’s still in high school. "
    s "I’m just not going to say anything and let Sara field this one herself as I don’t want to get in trouble."
    sar "Hey, Yuki and I are just here to relax. I don’t see an issue with getting into the bath with swimsuits on. Especially since doing that would let Sensei join in on the fun as well."

    "I’m suddenly less interested, but this is still a thing I want to participate in."

    yu "Why not just leave him out of this? Ain't no reason he has to come in there with us."

    "I also don't like Yuki anymore."

    sar "Obviously because he's our friend and we don't want him to be lonely."
    yu "I mean...I guess wearin' swimsuits would solve the whole high school nudity problem, but it ain’t like either of us brought shit like that, right?"
    yu "I don’t even think I own a swimsuit."

    scene iosidesbath17
    with dissolve

    sar "Do you have any we could borrow, Io? There have to be some, like...community swimsuits, right?"
    i "Towels, yeah...swimsuits? That’s...not really a thing anyone has ever asked for before."
    i "I guess I could raid my aunt’s stuff and see if she has anything, but..."
    i "Sorry, why am I even being included in this again? "
    sar "Aren’t you closing up? I figured you’d want to unwind after a hard day of work."
    s "That does sound pretty relaxing. Working at a bathhouse is a lot more exhausting than I thought."

    scene iosidesbath18
    with dissolve

    i "You didn’t even do anything..."
    yu "You really okay with this idea? "
    s "I mean...I don’t see anything {i}technically{/i} wrong with it so long as both Io and I are covered up. But I do think it’s kind of weird no matter how you look at it since this is a bathhouse and not a pool."
    sar "What is a bathhouse if not a hot pool that people bathe in?"
    s "You should write a book. "

    scene iosidesbath19
    with dissolve

    i "I’ll, uhh...go check upstairs. But only because I do think that getting in the water sounds relaxing right now and I’m afraid that Sensei would still join you if I refused."

    "I would have."

    yu "You sure about this? I know you’re weird around girls who are like, actual girls and not {i}me.{/i}"
    i "You said she’s “good people,” so I’m trusting your word on this. But if she annoys me, which I feel like she is going to, I will not hesitate to let her know."
    sar "Thanks, Io. I’m sure you’ll have just as much fun as the rest of us."
    i "Yeah, it’s easy to say things like that when you don’t know me."
    i "Anyway...whatever. You two can just go wait in the dressing room while I flip the sign. Sensei can stay out here."
    i "I don’t want people seeing you guys standing around and assuming we’re still open. And everybody else has already paid, so..."
    i "Yeah. Bye."
    i "And don’t do anything weird while I’m gone. The cameras store footage for up to 24 hours, so I’ll know."

    scene iosidesbath20
    with dissolve

    sar "Cameras?"
    sar "Is that even legal?"
    yu "I ain’t worried. Chances are somebody out there’s already got footage of me. Doubt a little more would hurt at all."

    scene black
    with dissolve2

    "I decide to do as I'm told and wait in the lobby while Sara and Yuki retreat into the men’s dressing room."
    "This lasts about five minutes before Sara, wearing nothing but a towel, walks back out into the lobby and forcibly pulls me away from my monthly good deed."
    "And while it wouldn’t be right of me to complain about an attractive grown woman’s desire to be closer to me while she’s wearing next to nothing, I can’t imagine Io will be happy to see me in there with them."

    scene iosidesbath21
    with dissolve2

    i "If I didn’t already know this was going to happen and wasn’t so dependent on your affection, I’d be really frustrated with you right now, Sensei."
    s "I tried to listen. Sara just wasn’t having it."

    scene iosidesbath22
    with dissolve

    i "Why am I not surprised?"
    sar "So, did you find anything? "
    i "Unless you want to try wearing one of {i}my{/i} swimsuits, no. I did not."
    i "Well, I did find a pair of shorts for Sensei. But it looks like you are going to have to wear your towel if you still want to carry through with this “safe for work bath time extravaganza.”"
    i "That or Sensei and I can just come in after you two are done and-"

    scene iosidesbath23
    with dissolve

    sar "Oh no! My towel has fallen off! How could this have happened?!"
    yu "Yo."
    s "Yeah, saw that coming."

    scene iosidesbath24
    with dissolve

    if sarasex == False:
        sar "And you can’t even run away this time..."
    else:
        sar "{i}Oh no. Whatever will I do now that Sensei has seen me naked?{/i}"

    s "You realize you’re just going to make this harder for me, right?"
    sar "That’s exactly what I want."
    yu "Hah..."

    scene iosidesbath25
    with dissolve

    yu "If you can’t beat ‘em, join ‘em."
    sar "Woo! Go Yuki! Take it off!"
    i "Uhh...hold on. Sensei’s still here. Shouldn’t you, like...maybe {i}not{/i} strip in front of him?"
    sar "I mean, {i}technically,{/i} this is {i}his{/i} side of the bath, isn’t it? "
    i "Technically, yeah. But-"

    scene iosidesbath26
    with dissolve

    yu "Can all this talkin’ stop already? I’m fucking tired."
    i "Sensei! Look away! There are too many boobs in here all of a sudden!"
    sar "And, for the first time in my life, I’m the biggest out of everyone."

    scene iosidesbath27
    with dissolve

    yu "You tryin’ to fuckin’ start something?"
    sar "Of course not! After you, Yuki. We wouldn’t want to stand here and intrude on Sensei’s personal space while {i}he{/i} gets undressed, would we?"

    scene iosidesbath28
    with dissolve

    sar "If only there wasn’t a student here...Then maybe he wouldn’t need those shorts at all."
    i "I’ve seen him naked plenty of times! We have cameras, remember?! What I {i}haven’t{/i} seen is him naked with-"
    i "Well...actually there was one time. But nothing happened then and...and..."
    i "Everybody just get in the fucking water, already!"

    scene black
    with dissolve2

    "Io pushes Sara and Yuki out of the room and I get changed faster than I’ve ever gotten changed before."
    "And while it’s unfortunate that both Io and I have to keep our clothes on to preserve my image as an upstanding member of society, I {i}do{/i} understand it."
    "I’m sure that both Sara and Yuki have their...{i}suspicions,{/i} but so long as those remain nothing more than {i}suspicions,{/i} everything will be okay."
    "We can all take solace in the fact that it’s easy to ignore things you don’t want to be true. But it’s a lot harder to accept them when they are."

    scene iosidesbath29
    with dissolve2

    "For the time being, the only thing that {i}is{/i} true in all of our minds is that we’re here willingly. "
    "Some less willing than others, sure...but it’s all agreed upon even when certain aspects of that agreement have been bent and twisted out of shape."
    "This is fine because nothing is going to happen tonight."
    "And if anything does happen tonight, I’m sure {i}that{/i} would be agreed upon as well."
    "Part of me hopes something does, for my true colors would appear far less vibrant amidst the contents of several other boxes of crayons being poured into one big pile."
    "That’s just wishful thinking, though."
    "I know my colors will always stand out."
    "They’re just too dark to properly blend in with the others."

    sar "So, Io...{i}you’re{/i} the girl who’s always complimenting Yuki on her back tattoo, right? Did you know that {i}I{/i} have tattoos as well?"
    i "Yes. I found that out the moment you decided it was acceptable to strip down to nothing right in front of my teacher."

    scene iosidesbath30
    with dissolve

    sar "Want to take a closer look? Here. I got this one when I was only 17 and-"
    i "Sit down! Jesus! I don’t want a closer look!"
    sar "How about you, Sensei? Want to touch it? "
    s "Uhh..."
    yu "No one wants to see your basic ass butterfly tattoo, Sara. There are like a trillion other girls who have the same exact shit in the same exact spot."

    scene iosidesbath31
    with dissolve

    sar "Well excuse me for not having the cool Yakuza connections required to get a huge dragon tattooed across my back. "
    sar "I like my butterfly and I am proud of it. "
    yu "You don’t {i}need{/i} Yakuza connections to get shit like that. Just makes it cheaper. Got mine done for free. "
    yu "Wish I could get it finished, though. Wound up abandoning that lifestyle before I could get it colored in. Might’ve hung around a little while longer if I thought of it back then."
    yu "Ain’t no way I can afford that shit now. Not without crawlin’ back to Yumi’s prick of a dad."

    scene iosidesbath32
    with dissolve

    yu "Oh, speaking of which- you hear anything about her lately?"
    s "Yumi? I...haven’t seen her around. Why?"
    yu "Got a call the other day from some chick I used to ride with. Dude she’s seein’s the captain of one of the Yamaguchi branches."
    yu "Told me Yumi showed up back at home the other day. First time in like a year."
    yu "Probably just needs money or some shit. But I figured you might know something about it."
    i "I wonder if it has anything to do with the fight?"

    scene iosidesbath33
    with dissolve

    yu "Fight?"
    i "Yumi kicked some girl’s ass in school the other day and hasn’t shown up ever since. It was brutal. She was unconscious and everything."

    scene iosidesbath34
    with dissolve

    yu "Get the fuck out of here. Did she really? No shit?"
    sar "Why do you look so proud? If Sana got into a fight, I’d be worried sick."
    yu "Sana’s like 50lbs soaking wet. Course you’d be worried. Yumi’s got the blood of a fuckin’ warrior. ‘Bout time she’s gotten to actually show it off."
    yu "How’s the girl she fucked up? Can she walk?"
    i "She had two black eyes for a while, but she’s pretty much back to normal now."

    scene iosidesbath35
    with dissolve

    yu "Damn. Best news I’ve heard all week. And here I was thinking I wouldn’t be able to relax with all these extra bodies around."
    i "You really haven’t heard anything, Sensei? Not even from the principal?"
    s "Nothing that everyone else doesn’t already know."
    i "Crazy. That whole situation was weird. Like, Yumi’s a dick and all, but I don’t think she’s the type to just beat the shit out of somebody for no good reason. "
    i "Nodoka had to have done something, right? What do you think it could be?"
    s "I-"
    yu "Who the fuck cares? My girl won and that’s all that matters."
    yu "Haven’t been this proud since I found out she was runnin’ her own business."
    sar "Lucky. I feel bad just asking Sana to {i}show up{/i} at mine."
    yu "Yeah, well your daughter’s a puss. Just like her mom with that basic ass butterfly tattoo."

    scene iosidesbath36
    with dissolve

    sar "Say one more bad thing about my butterfly and I will come over there and shut you up myself!"

    scene black
    with dissolve2

    "Once more, I narrowly avoid having to figure out how to speak on the Nodoka issue as the conversation quickly devolves into both Yuki and Io mocking Sara for the next ten minutes."
    "Eventually, Sara {i}does{/i} get up to try and silence Yuki, but is promptly shoved underwater and forced to submit."
    "It’s around this time that Io moves closer to me and attempts to grab my hand."
    "And even though it all happens underwater, the idea of doing something like that beside two adults is enough to dissuade me from carrying through with it."
    "And yet she does not relent."
    "Each moment that the eyes are not on us is another opportunity for her to bash me over the head with her affection. "
    "But it’s affection I can only accept behind closed doors."
    "When we’re out in the open-"
    "It’s better off if I pretend that it just doesn’t exist."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse25 = True
    stop music fadeout 5.0

    play sound "phonebeep.wav"

    "{i}You have received a new picture message from Sara!{/i}"
    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label iodorm25:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Io’s door and wait for her to answer, but my patience is quickly met by the sounds of the half-hushed humming of an unfamiliar tune halfway between heartbreak and harmony."
    "I do not know what has broken from this side of the door. But if there is anything I know about Io, it is that she likely has the tools to fix it."

    play sound "knock.mp3"

    "I knock again so she knows it’s me."
    "The humming stops and her attention bounces from whatever undeserving plank of wood it previously settled on and back to me where it rightfully belongs."

    i "Sensei?..."
    s "Yup. Can I come in?"
    i "I don’t knooooooww~ You might be kind of boooooored..."

    "Her words are slurred, something I couldn’t pick up from the humming, but the vulnerable state of an already vulnerable girl is not something that would force me back the way it would force others."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "It just brings me closer."
    "........."
    "......"
    "..."

    scene iooutofit1
    with dissolve2
    play music "io.mp3"

    "What I’m closer {i}to{/i} is something I’m not sure of, though. "
    "It’s not heartbreak for the remnants of my cardiovascular system have been worn so thin that “breaking” wouldn’t even suffice in describing the severing of the bits that are left at this point."
    "It’s not harmony either as the two of us inside of this room are almost constantly acting in opposition to whatever the world would have us do to move in unison."
    "I’m just closer to {i}her.{/i}"
    "Whether that’s good for either of us is something that remains to be seen."
    "But, if you want my opinion-"
    "The only thing that would be good for us is if we were left alone and stopped forcing ourselves to find one another."

    i "Heeeeey. Io Ichimonji here, reporting live from the floor. Which is coincidentally exactly where she belongs."
    s "I’m not sure if I’d call this “boring,” Io."
    i "Well, hey! If me being hopped on a medicinal cocktail’s enough to keep you entertained, you might be in for the most exciting night of your life."
    i "Just kind of figured I wouldn’t be as much fun as normal when every word I speak brings me one step closer to passing out."
    i "But then again, I’m not really any fun to begin with. So your taste is already kind of weird."
    i "Anyway, how’re things? Your niece still number one in the harem ranking? Uta says she makes a mean omurice."
    s "If talking is bringing you closer to passing out, maybe it’s best if you just...you know, don’t do that?"
    i "But then you’d {i}really{/i} be bored. And it’s not like I’m actually {i}gonna{/i} pass out. I’m just getting {i}closer{/i} to passing out."
    i "As if I’d waste this precious time with my favorite person in the world on {i}sleeping{/i} when he’s already expressed that he’s cool with me over-medicating myself."
    s "I’m not “cool” with that. You’re kind of weirding me out right now, actually. But at least you don’t look like you’re on the verge of dying this time."
    i "Different pills, different side effects. The endless cycle of targeted drug usage to combat the many things wrong with this stupid brain of mine."
    s "And what exactly were you targeting this time?"
    i "Yes."
    s "Io-"
    i "Why’s it matter what I was targeting? Can’t we just pretend that I’m feeling completely normal so we can have a completely normal conversation?"
    s "Is any conversation with you completely normal?"
    i "No. I like you too much to be able to speak normally. I’ll just wind up messing up again."
    s "Can I help you up? Or do you want to stay down there on the floor?"
    i "Wait wait wait. I just had the best idea."
    s "I somehow doubt that."
    i "No no no. Hear me out."
    i "If things can’t be normal because of how fucked up I am right now..."

    scene iooutofit2
    with dissolve

    i "You just need to get fucked up too!"
    s "How is that “the best” idea? That’s a horrible idea."
    i "Why’s that?"
    s "Because you very clearly need someone to look after you."

    scene iooutofit3
    with dissolve

    i "Nuh-uh. I know my limits when it comes to treating myself. Do I intentionally push those limits sometimes? Hell yeah. But this isn’t one of those times."
    i "I promise this is like, normal loopiness. The kind of stuff you’d be dealing with at least three nights a week if you ever ran away with me."
    i "If it was {i}really{/i} bad, I’d be hunched over my stepladder again and you’d have to carry me over to the kotatsu. But look! I made it here all by myself this time! Woohoo!"
    s "Either way, I’m not taking any of your pills. "
    i "Why not? They might help you."
    s "I don’t need help."
    i "Wish I could think that way."
    i "Either way, I wasn’t talking about pills in the first place. They’re too expensive and I like them too much to share."
    s "What {i}were{/i} you talking about then?"

    scene iooutofit4
    with dissolve

    i "One of our regular customers gifted us a bottle of sake a while back that I was supposed to give to my aunt- but I never did because I’m an asshole."
    i "Also, I thought it would be a fun thing to have in case Uta and I ever got bored one night. But it’s been here ever since and neither one of us has ever touched it."

    scene iooutofit5
    with dissolve

    i "Sensei, I bestow unto you this humble gift. May you partake so that we may {i}both{/i} get fucked up and free ourselves from the endless torment that is life itself."
    s "Well...that’s definitely a better alternative to unidentified medication, but I still don’t think getting drunk around someone so clearly under the influence is a great idea."

    scene iooutofit6
    with dissolve

    i "Why not?"
    s "Because we wouldn’t be ourselves at that point."
    i "If we’re not ourselves, anything that happens isn’t our fault."
    i "It would be more like whatever happens never happened in the first place."
    s "That’s not-"
    i "Just accept the fucking gift, Sensei. "
    i "With how uncertain the future is, {i}not{/i} accepting the gift could lead to Uta or I getting alcohol poisoning one day. And if that ever happened, I bet you’d regret not drinking right now."
    s "My bad. I didn’t realize I was supposed to be thinking ten steps ahead."

    scene iooutofit7
    with dissolve

    i "Why {i}step{/i} at all when jumping is so much more fun?"

    scene black
    with dissolve2

    "Io scrambles to her feet and is able to set her chair back up without much of an issue."
    "I’m not sure if I just caught her at the height of her drug-induced stupor but, fortunately, it appears to be in the early stages of wearing off right now."
    "She grabs her stepladder or, to paraphrase what she said just moments ago, the symbol of whether or not she is “really bad.”"
    "In some ways, though, the Io today seems worse."
    "Sure, she isn’t feverish or struggling to walk, but she seems almost numb to the fact that she’s leaving herself open."
    "I guess some might call that a good thing- that she’s comfortable enough with me to let her guard down in knowing that I won’t do anything to hurt her."
    "It’s just worrying when she lets that guard down before {i}I{/i} do."
    "Because sometimes, I hurt people without even trying."
    "Without even thinking about it."
    "And I do not want a reality where that becomes okay because the two of us decided to be someone else for a night."
    "........."
    "......"
    "..."

    scene iooutofit8
    with dissolve2

    "I am a marsh warbler."
    "I abandon the me from minutes ago and slip into a new reality- one where I don’t feel the need to restrain myself in favor of protecting someone else because the center of this world is {i}me.{/i}"
    "I am the one who needs to be protected. And the subsequent results of my decisions, while serving as occasional preventative measures, very rarely make things worse."
    "Things become worse on their own regardless of the choices I make or the things I do."
    "There are consequences that we face without knowing or understanding what even invokes them at times."
    "If the world is going to break, I am not going to be the one to break it."
    "If Io is going to break, I am not going to be the one to break her."
    "Especially when she’s just like the wires and rods keeping my heart propped up- spread too thin to spread anymore."
    "And so immeasurably shattered from the get-go that her further destruction would be impossible."
    "I jumped not because I thought it would be more fun."
    "I jumped because I knew it wouldn’t hurt me."

    i "See! Aren’t you so much happier now that we’re {i}both{/i} not our normal selves?"
    s "You seem more or less the same to me. Just a shade redder and...more animated with your hand movements."
    i "Heheh. Yeah. The Clonazepam always makes my limbs feel a little numb, so that just kinda happens sometimes. Uta likes making fun of it."
    s "I take it she sees you like this pretty often?"
    i "Oh yeah. It’s like the only time I can kinda keep up with her, too. I think we both kind of enjoy it in a way."
    i "She gets an Io who doesn’t complain about herself as much, and I get an Uta who...well, you know. It’s Uta. She’s always fun."
    i "Hey, what were you guys doing in the tea ceremony room thing the other day? That was weird."
    s "I think it was something about me being sad."
    i "Were you actually sad? Do you wanna talk about it?"
    s "No thanks. I can’t even really remember what it was about."
    i "Do you have depression, Sensei? I wouldn’t normally ask about something that directly because I hate when people do that for me, but this isn’t the {i}real{/i} Io speaking right now, so it’s cool if I do that."
    s "No clue. It wouldn’t surprise me if I did, but it’s not something I think I really need to know."
    i "I mean, {i}I{/i} would wanna know if {i}I{/i} had depression. "
    s "Do you...not?"

    scene iooutofit9
    with dissolve

    i "No! I don’t! That’s like, one of the only things I {i}don’t{/i} have! And it really pisses me off when people just {i}assume{/i} I have it because I don’t act how they {i}want{/i} me to, you know?!"
    i "Kirin asked me the same shit the other day and then started rattling off all this stuff about psychology like she actually {i}knew{/i} what she was talking about and I almost turned her into an art project!"

    scene iooutofit10
    with dissolve

    i "Now, asking if I take drugs that {i}treat{/i} depression is another story entirely since the usage of antidepressants extends far beyond depressive disorder, but do I actually have {i}depression?{/i} Fuck no!"

    scene iooutofit11
    with dissolve

    i "You’d think that shit with that disorder was annoying enough in the fact that everybody and their mother claims to have it now-"
    i "But the fact that it’s extended to the point where undiagnosed people are diagnosing {i}other{/i} people with it despite having zero understanding of how it works is just straight up ridiculous!"

    scene iooutofit12
    with dissolve

    i "Anyway, rant over. I’ve been holding that in for a while and it felt good to let it out, so thanks. Even {i}if{/i} you just did the exact thing that I was complaining about."
    s "Yeah...now I know for next time, I guess."
    s "If you don’t mind me asking, though, exactly what {i}are{/i} all of these medications for then? Besides anxiety, which I think everybody already knows about."

    scene iooutofit13
    with dissolve

    i "Honestly? I don’t even know what they’re trying to treat with some of them. I’m at the point where I just take whatever’s given to me without questioning it and watch as it fucks me up later."
    s "That...is extremely worrying."
    i "Worried my aunt at first too. In fact, I wouldn’t be surprised if it still worries her now. She just doesn’t let it show anymore."
    i "It’s obviously not like that for all of them, though. Some of this stuff I’ve been taking for, like...I don’t know, seven or eight years?"
    i "I just got to a point where I accepted that everything about me is broken and that some of it can be patched up by the shit they shove into orange bottles."

    scene iooutofit14
    with dissolve

    s "Hey, it can’t be {i}everything{/i} if you don’t have depression, right?"
    i "That’s a good point. The TLDR is that there’s a lot of me that hasn’t worked the way it’s supposed to since I was little. "
    s "TLDR?"
    i "Too long, didn’t read. You’re old."
    s "Thanks, Io."
    i "No, like really old. The cap is still on that bottle. And your glass is full."
    s "..."
    i "..."
    s "You don’t have any pills in here that treat dementia, do you?"
    i "I don’t think so. But the clinic I get my Ketamine from is open 24 hours and I can probably cash in a few of my broken girl punch-cards in exchange for a couple free doses. "
    i "I don’t think it helps with dementia, but it feels cool."
    s "I think I’m just...more drunk than I thought."
    i "I bet. I’ve only had sake a couple times, but I remember it being super strong and messing me up like, right away."
    s "Considering that this bottle is probably heavier than you, I’m not surprised."
    i "Can I try?"

    scene iooutofit15
    with dissolve

    s "Aren’t you on like eight hundred medications? There’s no way mixing alcohol with them would be a good idea."
    i "Nothing about tonight has been a good idea by most accounts. Plus, I’ve been watching you drink from that glass all night and I want to ham up the indirect kiss cliche."
    s "Okay. But I’m only agreeing to this because I’m also intoxicated and, if you actually die, I’m going to run away with Uta just to spite you."

    scene iooutofit16
    with dissolve

    i "You say that like it would be a bad thing."
    s "Wouldn’t it?"
    i "You and Uta? Not really. If that made you guys happy, I probably wouldn’t even mind dying."
    s "Io-"
    i "Don’t worry. I’m having too much fun right now to actually die."
    i "I’m just saying that the two people who matter most to me finding joy in the arms of one another wouldn’t ever be {i}bad.{/i}"
    i "I just wish it could be me in your arms instead."

    scene iooutofit17
    with dissolve

    i "Mnh...mm......mnh..."

    scene iooutofit18
    with dissolve

    i "Geh..."
    s "This never happened."
    i "Heheh..."
    i "That stuff...really is strong, huh?"
    s "Did you enjoy it at least?"

    scene iooutofit19
    with dissolve

    i "Yeah..."
    i "I got to taste your lips."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene iooutofit20
    with dissolve2

    "I turn off the lights and rest Io on the bed after she finally passes out."
    "But before you blame me, I didn’t let her have any more alcohol after that."
    "Does that absolve me of the fact that I let her have some in the first place? No. "
    "But it’s something she would have done on her own the moment I left either way. Being able to watch over her as it happens is surely better than the alternative, isn’t it?"
    "Like I said before, things are going to happen whether I want them to or not."

    scene black
    with dissolve2

    "Which is why, despite knowing that I am the last thing she needs, I want to keep seeing her."
    "I want to taste her lips as well."

    $ renpy.end_replay()
    $ iodorm25 = True
    $ io_love += 1
    stop music fadeout 7.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iospecial30:
    play music "phonering.mp3"

    s "..."
    s "..."
    s "..."

    "I wake up to the sound of my phone ringing and the day quickly gets off to a rocky start."
    "Thankfully, phones can’t ring forever. So any second now, this is going to stop and things are going to return to the way they should be at..."

    s "7:00 AM..."

    stop music
    play sound "phonebeep.wav"

    "I press a button to ignore the call and-"

    play music "phonering.mp3"

    "Oh, come on."

    stop music
    play sound "phonebeep.wav"

    s "Hello?"

    play music "acoustic.mp3"

    i "Hi! Did I wake you?"
    s "Yes. Goodbye."
    i "Wait, don’t hang up yet! I have awesome news!"
    s "Can the news not wait until, like...two hours from now?"
    i "I mean, it probably {i}could.{/i} But do I really seem like the type with enough self control to be able to abstain for that long when there’s something I clearly want to tell you about?"
    s "Nope. Anyway, talk to you later."

    play sound "phonebeep.wav"

    "I hang up the phone and-"

    play sound "phonering.mp3"

    "You’ve gotta be fucking kidding me."

    scene bedroom_day
    with dissolve
    play sound "phonebeep.wav"

    i "Stop ignoring me and let me share my awesome news with you! If you still don’t think it’s awesome, you can ignore me forever and forget we ever even met."
    i "Except not really because my self-esteem is already pretty horrible and a blow like that would be the final nail in the coffin that is Io."
    s "Just tell me what the news is."
    i "I don’t have to work today!"
    s "..."
    i "Awesome, right?!"
    s "Is that seriously it?"
    i "Pretty much, yeah!"
    i "But it’s {i}because{/i} of that that I figured you and me could spend some time together! If that’s not too presumptuous and you don’t already have other plans, which I figured you might."
    i "But that’s just one of several reasons I’m calling you as early as this! I didn’t want someone else beating me to the punch and stealing you away before I even get a shot."
    s "I’m surprised you’re actually the one reaching out to {i}me{/i} this time when I’m pretty much always the one who finds you first. But I guess your reasoning makes sense."
    i "Hey, the only reason I don’t call you more often is that I’m still like 85%% sure you’re only pretending to like me. But Uta says I should be more assertive if I’m ever going to get what I want, so hi."
    i "Anyway, can we hang out? I have something for you."
    s "You do?"
    i "Yes. Well, kind of. I found it at a garage sale. But you’ll love it. Maybe. Or not. Probably not, now that I think about it. But I will, so I still want to give it to you."
    s "Just come over. I’m pretty sure Ami has work today."
    i "Come...come over? Like...to your house?"
    s "Yes. But I’m going back to sleep until you get here, so goodbye."
    i "Wait! I don’t know where you live!"
    s "Ask Uta."
    i "Why does Uta know where you live?!"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "I hang up the phone and collapse back onto the bed."
    "I’m not sure if I’m going to be able to get any sleep now that I’ve been torn from my slumber for more than five minutes, but it’s worth a shot."
    "And hey, if Io lacks the self confidence or assertiveness to come over here (Which I figure there is a 50%% chance she will), I’m sure that just staying in bed will be enough to at least partially rejuvenate me."
    "I close my eyes, unsure of how the day is going to proceed..."

    scene bedroom_day
    with dissolve2
    play sound "doorbell.mp3"

    "But when I open them roughly two hours later to the sound of my doorbell being repeatedly pressed, I figure it out."

    play sound "doorbell.mp3"

    s "..."

    play sound "doorbell.mp3"

    s "..."

    play sound "doorbell.mp3"

    s "Well, at least she gave me an extra two hours."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene iocomesover1
    with dissolve2

    i "Wow! It’s just as normal as I thought it would be!"
    s "Thank...you?"
    i "Ooooh, and your TV is huge! Do you get all of the sports channels? Or any of the American ones?"

    scene iocomesover2
    with dissolve

    i "Well, not like we’ll have any time to watch anything anyway. Not with what I’ve got planned for the two of us."
    s "Oh?..."
    i "You know it."
    i "Are you ready for the ride of your life, Sensei?"
    s "If I knew that’s what you were calling about, I wouldn’t have asked you to wait two-"

    scene iocomesover3
    with dissolve

    i "Because it’s time for the 1999 PC classic, Rollercoaster Tycoon!"
    s "..."
    i "Sweet, right?"
    s "..."

    scene iocomesover4
    with dissolve

    i "What’s wrong? Are you not interested in the 1999 PC classic, Rollercoaster Tycoon?"
    s "Are you going to refer to it by that lengthy title every time?"
    i "It’s a relic of the past. I thought repeatedly saying its release year might unlock some core memories for you that lead to the two of us playing it until it gets dark and I have to go home."
    s "I’m not that interested in video games, Io."
    i "Not even the 1999 PC classic-"
    s "Not even the 1999 PC classic, Rollercoaster Tycoon."

    scene iocomesover5
    with dissolve

    i "But I spent like 500 yen on this!"
    s "That’s not even that much."
    i "Also, you still haven’t taken me to an amusement park so it’s very considerate that I would bring the amusement park to {i}you{/i} instead! This is significantly cheaper and only like, three degrees less fun!"
    s "I mean...I {i}guess{/i} we can play if you’re that excited about it. But are you really content with just spending all of our time together playing video games? "

    scene iocomesover6
    with dissolve

    i "Yeah."
    s "There’s nothing else you’d rather do instead?"
    i "Not really."
    i "Everything else sounds exhausting. And every time Uta and I have played games like this together, it’s been a total blast."
    s "There’s {i}really{/i} nothing you’d rather do?"
    i "Nope."
    s "{i}Nothing?{/i}"

    scene iocomesover7
    with dissolve

    i "You’re being a real creep today, Sensei."

    "I sigh to myself and think back to what Uta said at the love hotel the other day."
    "And while I’m still not sure exactly how accurate that assessment of hers is (Ignoring the fact that she probably knows more about Io than I do), I’m not about to just come out and {i}ask{/i} Io about it."
    "If she wants to play the 1999 PC classic, Rollercoaster Tycoon, then..."
    "Well, I guess the two of us are going to play the 1999 PC classic, Rollercoaster Tycoon."

    scene black
    with dissolve2

    i "Oh! Which one is your room? I don’t want to accidentally walk into Ami’s and have my eyes singed by how pink and girly everything probably is."
    s "It’s the one on the left."

    play sound "dooropen.mp3"

    i "Cool! That means- ah! My eyes! They burn! You lied to me!"

    "I lead Io to my {i}actual{/i} room after destroying her eyesight, which she takes as an invitation to immediately run up to my table and start playing with my things."

    scene iocomesover8
    with dissolve2

    "Granted, she is the one who {i}created{/i} the thing she is currently playing with. But still, touching other peoples’ belongings is rude."

    i "You kept it! You kept it and didn’t throw it in the trash even though it was made by a trash person who previously put and is currently putting her trash hands all over it!"
    s "I wouldn’t just throw away something you made for me."
    s "Even that wardrobe thing is still around here somewhere. I just had to move it out of the bedroom since it was taking up way too much space."
    i "That’s fine! A 50%% success rate combined with a 0%% garbage rate is way better than I thought I’d get, so thank you!"
    i "How you doing, little guy? Is Sensei treating you well? "
    i "Have you seen him doing anything weird under the blanket? Or does he make you turn away for that?"
    s "Please don’t talk to my robot that way."

    "Not after the things he has seen..."

    scene iocomesover9
    with dissolve

    i "Can he play with us? He is technically one of my offspring, so there’s no way he doesn’t also enjoy the 1999 PC classic, Rollercoaster Tycoon."

    if robotname.lower() in ["1999 pc classic, rollercoaster tycoon"]:
        s "You know, despite him not being able to talk, I knew from the get-go that he loved that game."
        s "Which is exactly why I decided to name him after it."

        scene iocomesover8
        with dissolve

        i "You didn’t!"
        s "I certainly did."
        i "How are you doing, 1999 PC Classic, Rollercoaster Tycoon?!"
        i "Are you having fun?! Are you having a good time?!"
        s "I also taught him Spanish so he has no idea what you’re saying."
        i "That’s fine. He can just be confused along with the rest of the people who had to go into the code to find this additional dialogue since no one would ever actually name him 1999 PC Classic, Rollercoaster Tycoon."
        s "Anyway, back onto the topic of whether or not he can play-"

    s "I guess. But I have no idea if he’ll enjoy it or not."
    s "Or...if he’s even capable of enjoying anything because he is an inanimate hunk of wood."
    i "For now! But in about 99 years, he’ll be very mad that you said that."

    scene black
    with dissolve2

    "Io takes the robot over to my desk and places him down beside my laptop."
    "Thankfully, the laptop is old enough to still have a disc drive, so Io pops the 1999 PC classic, Rollercoaster Tycoon into the tray and, after an outdated installation screen, she loads up the game."

    scene iocomesover10
    with dissolve2

    "I think to myself as she goes over the basics that this is really similar to the way Niki acts whenever she comes into my room."
    "The only difference is that I don’t [[yet] have an extensive sexual history with Io and that she actually tries to include me rather than just seizing my things for her own personal gain."
    "We play for an hour or two. And when I say {i}we{/i}, I mean {i}me-{/i} as Io vehemently refuses to play at all in favor of trying to get me addicted."
    "And while her efforts are in vain for the majority of time I spend pressing buttons on this rectangular machine, I do begin to reevaluate that when she begins teaching me the {i}secrets{/i} of this game."

    i "So, yeah. If you just delete parts of the tracks on your rollercoasters, you can send all of your guests flying to their deaths."
    i "What I like to do is position them so that the carts go flying into the water, causing everyone to drown."
    i "It’s kind of like how in the 2000 PC classic, The Sims, you could delete the ladder on your swimming pool and laugh as all of the characters you created slowly drown to death."
    s "Why are you so experienced when it comes to games that existed before you?"
    i "Because I am a contrarian and refuse to live the same type of life as my peers, electing to instead participate in activities that others would call outdated or boring so no one tries to connect with me."
    i "Oh. And there’s also a Zoo Tycoon where you can make lions eat all of your guests."

    scene iocomesover11
    with dissolve

    s "I think you might have a problem."
    i "Sensei, if it weren’t for outlets like this where I can get all of my inner rage out in peace, I would probably be in jail for literal murder."
    s "I highly doubt you’d have the resolve to actually kill someone."

    scene iocomesover12
    with dissolve

    i "Well, thanks to extremely outdated PC hits, we’re probably not going to find out any time soon."
    i "Besides, going to jail would mean that I don’t get to spend time with you anymore. And days like this are quickly becoming my favorite reason to continue existing."
    s "I’ll admit this isn’t as bad as I thought it would be."
    s "Still probably not how I’d choose to spend my time, though."

    scene iocomesover13
    with dissolve

    i "Well, we’ve done what I’ve wanted to do for like, two hours already. So if there’s something you had in mind, we could try that instead."
    i "As long as it doesn’t involve going out, because there is no way I’m going to be into that today. Or...any day."
    i "Unless you’re absolutely insistent that we should. In that case, I’d probably make an exception. But even then, I’d only be pretending to be okay with it in order to make you happy."
    s "I wish you’d learn to be antisocial in fewer words."
    i "Me too. Incessant self deprecation can be really tiring."

    scene iocomesover14
    with dissolve

    s "Anyway, I didn’t have any concrete plans. I just figured that whatever was going to happen in here would involve a little less murder and a little more...intimacy."

    scene iocomesover15
    with dissolve

    i "Oh...Hahah...Yeah..."
    i "Yeah, I...I don’t know. It’s just...still my first time over and..."
    i "You know, just barging into your room to play games without really thinking about any of the consequences or how that would look is starting to sound like a pretty amateur move."
    s "You were excited. It happens. Besides, for someone who spends virtually their entire life {i}thinking,{/i} you kind of suck at it. So this is to be expected."
    i "Yeah. You’d think that after years and years of repeated failure and endless misery that maybe my brain would self-correct and cause me to act a little less shitty, but alas."
    i "Is, uhh..."
    i "Is...{i}intimacy{/i} really your go-to when people come over here, though? Cause, like...there’s no way I’m the first, right?"
    s "You’re the first girl to ever come into this room, Io."

    scene iocomesover16
    with dissolve

    i "Can you at least make your lies sound {i}a little{/i} convincing so I can trick myself into believing them?"
    s "You were going to beat yourself up no matter what I responded with right there. I know you. Avoiding that topic entirely is the best way to prevent that from happening."

    scene iocomesover17
    with dissolve

    i "I mean...we don’t have to {i}avoid{/i} it. Avoiding things makes stuff awkward. And if we keep avoiding stuff, we’ll wind up just sitting here in silence for the rest of the day and that sounds like it would bore you."
    s "I can turn the game volume up. At least it wouldn’t be silent then."

    scene iocomesover18
    with dissolve

    i "J...Just for clarity’s sake, what did you mean by “intimacy?”"
    s "..."
    i "Should I not have asked that? Did I just make a mistake?"
    i "Because different people have different definitions of that word and I think I might just be misinterpreting {i}your{/i} definition of it and turning this into a thing when it’s not a thing at all."
    s "Just assume that my definition of the word is whatever {i}your{/i} definition of the word is. That sounds like the easiest way to end this."
    i "If our definitions of that word are the same, then I {i}am{/i} turning this into a thing- because I’d be totally fine with intimacy if it’s like, Io intimacy....Iontimacy. Sorry. That wasn’t funny. Sorry."
    s "Even though we have the same definitions, I feel like I should ask you what your brand of intimacy is."
    i "Uhhhhhh..."

    scene iocomesover19
    with dissolve

    i "Like..."
    i "Cuddling?..."
    i "Or something?..."
    s "Why are you getting so flustered? We’ve “cuddled” in your room several times before, haven’t we?"
    i "Yes...but also no? Never like this, at least. Never in {i}your{/i} room. And never when we’re...so alone."
    s "Are you nervous?"

    scene iocomesover20
    with dissolve

    i "Yes, but only that you’ll realize you don’t want anything to do with me anymore."
    s "That’s not going to happen."
    i "Do you promise?"
    s "Sure. If promising that somehow reassures you, I’ll promise it as often as you want."
    s "I’m not going anywhere. And no, I’m not just saying that because I live here."
    i "You won’t leave even if I’m full of disappointments?"
    s "If I was going to abandon you, I would have done it already. I’m in this for the long haul at this point."

    scene iocomesover21
    with dissolve

    i "The...long haul..."
    s "..."
    i "..."
    s "..."
    i "..."

    scene iocomesover22
    with dissolve

    i "W...Wow! Your bed looks so...comfortable..."
    i "Is it okay if I...lay down on it for a little while to test it out?"
    s "What are you doing?"

    scene iocomesover23
    with dissolve

    i "Oooooh...so...good. Or...soft. Or something..."
    i "If only I...had someone to cuddle with me. Then I’d...{i}really{/i} be able to form a solid opinion on the...marketability of this...mattress..."
    s "Io-"
    i "Yes, I’m awkward! I’m sorry! That was your cue! We played enough of the 1999 PC classic, Rollercoaster Tycoon and now it’s time to do what you want so you won’t hate me!"
    s "I’m not going-"
    i "I also just want to cuddle now and am only saying things like that because it’s too hard to admit and accept the truth!"
    s "..."
    i "What?!"
    s "Nothing. Just thinking that I probably should have asked for three hours instead of two."

    scene black
    with dissolve2

    "I close the laptop and make my way over to the bed, climbing over Io so I can take my place behind her as the big spoon."
    "How things came to this when I already accepted that they {i}wouldn’t,{/i} I have no clue."

    scene iocomesover24
    with dissolve2

    "But I’m glad that they did- for the sensation of this paperthin bundle of contradictions that smells vaguely of blueberry shampoo pressing up against me fills me with my {i}own{/i} set of contradictions."
    "The acceptance I felt just moments ago begins a painful metamorphosis into doubt. But not just the doubt of myself- the doubt of everyone around me."
    "We can not predict the future. And even those who think they know each other most can be hazy on the details if they have not pried in the right places at the right times."
    "Would Uta have been able to predict that Io would not hesitate in calling me to bed?"
    "Would she have been able to predict that her fingers would crawl inside of my sleeve and pull me closer to her?"
    "That she’d trust me so much she’d close her eyes just minutes after hearing about my anticipation and expectation of intimacy?"
    "Of course not."
    "Because Uta doesn’t know Io as well as she thinks she does."
    "But I do."
    "I do, because Io is me."
    "I know what Io wants, because I am Io."
    "We are one and the same- two broken people who have given up on themselves and must now find solace through the embrace of the opposite sex."
    "Would she truly have come here without the expectation that we’d end up like this?"
    "Would she truly give in so easily?"
    "She likes me."
    "She likes me and she wants to be intimate with me."
    "I want to be intimate with her."
    "I want to take her {s}costume{/s} shorts off."
    "I want to be intimate with her."
    "I want-"

    i "This is..."
    i "The most peaceful I’ve felt in a really long time, Sensei..."
    i "I really wish you’d let me be your girlfriend."
    s "..."
    i "..."

    scene iocomesover25
    with dissolve2

    s "Maybe one day."
    i "Sensei?..."

    "She likes me."
    "She likes me and she wants to be with me."
    "I want to be with her."
    "She will tell me to stop if she wants me to stop."

    s "Does this room smell strange to you?"
    i "Does...huh? Strange how?"
    i "Do you not like blueberries? I can wear something else if you-"
    s "It’s like Spring."
    i "Spring?..."

    scene iocomesover26
    with dissolve2

    i "Um-"
    s "Why doesn’t it exist anymore?"
    i "Uhh..."
    s "Why do I remember a season we don’t have?"
    s "Why do I remember the scent of what can not exist anymore?"

    scene iocomesover27
    with dissolve

    i "..."
    s "Why do you think that is?"

    stop music
    play sound "static.mp3"
    scene imissyoumore with flash
    scene iocomesover28 with flash
    stop sound
    play music "allofthesounds.mp3"

    "SHE LIKES ME"
    "SHE LIKES ME AND WANTS TO BE WITH ME"
    "SHE WILL TELL ME TO STOP IF SHE DOES NOT WANT THIS"
    "SHE WILL TELL ME TO STOP"

    scene black
    stop music

    "I WILL NOT STOP"

    play sound "static.mp3"
    scene happy4 with flash
    scene happy2 with flash
    scene happy6 with flash
    scene iocomesover29 with flash
    stop sound

    i "Okay! Uhh...I just remembered that, umm..."
    i "My day off is, uhh...actually {i}tomorrow...{/i}hahah..."
    s "What just-"

    scene iocomesover30
    with dissolve

    i "It’s...It’s fine! Really! It’s not you! I’m just...kind of weird when it...yeah..."
    i "But, uhh...I had a lot of fun today! I’m sorry I had to go and ruin it at the end..."

    scene iocomesover31
    with dissolve

    i "And...uhh..."
    i "It was...a lot of fun and...wait- I already said that."
    i "Uhh..."

    scene iocomesover30
    with dissolve

    i "I love you! Or...umm...like you! Whichever one I said the...last time and..."
    i "And..."
    i "Please don’t hate me..."

    scene iocomesover32
    with hpunch
    play sound "doorslam.mp3"

    "Io runs out of the room."

    scene black

    "I catch up on sleep."

    $ renpy.end_replay()
    $ iospecial30 = True

    "{i}Io’s affection does not increase.{/i}"
    "{i}You scared her.{/i}"

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

label bathhouse35p1:
    scene iosenseifaint1
    with fade
    play music "lifeismostlygood.mp3"

    i "...and then Murakami hit a walk-off missile to the opposite field that smacked some old lady right in the face! It was totally crazy! You had to see it!"
    s "Io, I don’t like baseball."
    i "Yeah, I know. But I do, so you should at least try to be interested. Like I do when you talk about other girls around me."
    s "But you never try to be interested when I talk about other girls."
    i "Sure I do! I just fail immediately. "

    "As you can see, I’ve decided to spend the afternoon at the bathhouse...and by afternoon I mean “night” because the day has kind of just slipped away from me at this point."
    "But hey, I’ve apparently got decently high tolerance when it comes to hot water and don’t feel anywhere even close to passing out just yet despite being in here for-"

    s "Io, how long have I been in here for?"

    scene iosenseifaint2
    with dissolve

    i "Mmm......six hours. But you don’t have to rush to get out. The more time I get to spend with you, the better."

    "Strike that. I apparently have {i}very{/i} high tolerance when it comes to hot water. But I make up for that in being utterly horrible when it comes to time management."
    "Either way, we wind up in the same position we’ve found ourselves in time and time before — with me facing one direction while Io faces the other."
    "I’m not quite sure what makes her immune to the allure of my penis (Especially given just how much she’s seen of it), but I’m pretty confident it’s only a matter of time now until she winds up in the bath with me."
    "And I’m dead set on spending another six hours in here if that brings me any closer to whatever rhetorical tipping point is needed to make that happen."

    s "Is it really okay if you just spend all of your time with me instead of watching the front desk?"

    "Or at least I {i}tell{/i} myself I’m dead set on that while my mouth attempts to betray me in coaxing her away."
    "But on the bright side, at least one segment of my being isn’t morally inept tonight."

    i "It’s fine. I put a sign thingy up. And it’s not like I’ve been {i}completely{/i} neglecting my post. I’m still going out there to check on stuff every once in a while."

    scene iosenseifaint3
    with dissolve

    i "In fact, it’s probably better for business if I stay on the men’s side and make sure all of our male customers don’t go peeping on the women."
    s "I am the only male customer you ever have."
    i "And are you saying you {i}wouldn’t{/i} try and look through the fence if I wasn’t around?"
    s "Fair point."
    s "It would be nice to have {i}something{/i} to look at while I’m in here, though."

    scene iosenseifaint4
    with dissolve

    i "Want me to go get your phone? There’s a level of damage-risk involved since you’re in the bath and whatnot, but I do it all the time and I’ve only lost, like...one phone because of it."
    s "I was suggesting something a bit more impure if you catch my drift."

    scene iosenseifaint5
    with dissolve

    i "Hey, it’s not my business what you look at on your phone. I was just trying to be of some help since I {i}am{/i} technically on the clock right now."
    s "What about when you’re off the clock?"

    "Somehow or another, I manage to remind my mouth of who we really are as the last, flimsy barrier between my good side and bad side is ripped to shreds."

    i "When I’m off the clock, I have to clean everything. Then, I have to eat dinner. {i}Then,{/i} I have to pick up dinner for Uta. {i}Then,{/i} I have to walk all the way back to the dorms."
    i "As you can see, I’ve got a pretty busy night ahead of me."
    s "Sounds to me like you could use a little something to relax."
    i "Probably. But I should wait at least another two hours before popping a second Adderall. "
    s "If only there was some other way for you to wind down..."

    scene iosenseifaint6
    with dissolve

    i "Want me to give you a few minutes alone so you can relieve yourself and stop trying to get me into the bath with you?"
    i "Also, when I say “relieve yourself” I mean {i}outside{/i} of the bath, please. That stuff’s not good for the drain."
    s "That’s probably for the best at this point. It’s a little difficult for me to stop myself once my brain gets locked onto something."

    scene iosenseifaint7
    with dissolve

    i "Testosterone will do that to you. I think. I’m admittedly less knowledgeable about the male anatomy than the female one. But that’s not something I want to get into with you, even if you {i}are{/i} my teacher."
    i "Hold on. I’ll Google it."
    s "Io-"
    i "Yup. Google says, “Sexual desire is typically higher in men than in women, with testosterone (T) thought to account for this difference.” The more you know."
    s "Io, how much longer are you going to do this for?"

    scene iosenseifaint8
    with dissolve

    i "Do what? Google stuff? Because I’m already done. That was it. "
    s "You know what I mean."
    i "Of course I know what you mean, which is why I’m trying to delicately steer the conversation {i}away{/i} from that subject by both boring and annoying you with science and stats. Is it working?"
    s "A little bit, yeah..."

    scene iosenseifaint9
    with dissolve

    i "Great! Then you won’t mind if I just zoom right on past all this anatomy stuff and find something else to annoy you about!"
    i "Ooh, here’s an article about whales. That should kill a few more minutes while we wait for all the women to leave."

    "I’m going to have to get to the bottom of this sooner or later...I’m just not sure {i}how{/i} when every time I try winds up like this."
    "And even if Uta has trouble keeping her mouth shut, I know she won’t just go spilling whatever Io’s deal is to me if I ask nicely."
    "It’s obviously going to require a little more work...but how exactly can I work {i}toward{/i} it when the tool I’ve used for every other issue thus far is disabled?"
    "Sex has been my weapon for almost everything- but some creatures or targets require something a little different."
    "I don’t want to have to manipulate Io into revealing her secrets to me, especially when I know she’s perceptive enough to pick up on that immediately."
    "The saddest part of all of it is that this method probably {i}would{/i} work-"
    "And that she’d simply {i}allow{/i} herself to be manipulated because it would make it easier to blame her mental shortcomings on someone else later on."
    "I know that to be true because that’s what {i}I{/i} would do. And every day that passes by, she seems more and more similar to me."
    "But no one will ever be an exact replica...so there will always be something to misunderstand or misinterpret. "
    "I just hope it won’t last forever."
    "Because beneath the sentimentality and the desire for her to feel safe whenever she’s with me-"
    "There is an undying urge to shove my cock so deep inside of her that she splits into two pieces."
    "And an even greater urge to show her that what she wants isn’t what she wants at all."

    i "Ooooh, interesting. Sensei, did you know there’s a type of whale that-"

    scene iosenseifaint10
    with dissolve

    cust "Um...hello?...Is anyone there?..."
    i "That’s not another guy, is it?"
    s "I hope not. I don’t like sharing. "
    i "Oh. No. That's a girl."
    s "Is she attractive?"
    i "Not really."
    s "Screw it. Let her in anyway."
    i "Hey, you. You’re not allowed over here, you know. This is the men’s bath."
    cust "Y-Yes! I know, but...the towel rack is empty and...I left mine at home..."

    scene iosenseifaint11
    with dissolve

    i "Ugh, already? Just how busy are we on the other side tonight?"
    i "Sensei, I’ll be back in a few minutes. Just gotta refill some stuff. "

    scene iosenseifaint12
    with dissolve

    i "But remember, no jerking it in the bath. "
    s "It’s bad for the drains, I know."
    i "Atta boy."

    scene iosenseifaint13
    with fade

    s "Hah..."

    "I close my eyes and try to relax a bit as Io exits the men’s side of the bath."
    "I know I was getting ahead of myself a short while ago, but...I guess I’m just not used to getting the runaround when it comes to romance."
    "If you can even call this romance, that is."
    "If anything, it feels more like I’m {i}her{/i} uncle sometimes — what with the minimal sexual attraction and the overall desire to just “hang out” with me."
    "But, then again, she has mentioned on many occasions having actual feelings for me and wanting to be my girlfriend..."
    "All things considered, though...that’s pretty tame compared to my current perception of what unclehood entails."

    play sound "water1.mp3"

    "I just wish I could bring myself to understand how she can love in such a “hands-off” kind of way."

    play sound "water1.mp3"

    "For me, that’s not what love is like at all."

    play sound "water1.mp3"

    "For me, love is something much more primitive. "

    play sound "water1.mp3"

    "And while that may be just me poorly defining one more word that’s meant to be interpreted in a different way, I-"

    play sound "water1.mp3"

    s "..."

    "I- "

    play sound "water1.mp3"

    s "..."

    play sound "water1.mp3"
    scene iosenseifaint14 with dissolve

    s "..."

    scene iosenseifaint15
    with fade
    play sound "water1.mp3"

    se "Aaahh..."
    se "There’s nothing quite like a hot bath after a long day of being dead."
    s "..."
    se "..."

    scene iosenseifaint16
    with dissolve

    se "Oh, hey. "
    s "..."
    se "..."
    se "Come here often?"

    stop music
    scene black
    play sound "waterdrop.mp3"
    $ renpy.pause(5, hard=True)
    "........."
    "......"
    "..."

    scene iosenseifaint17
    with dissolve2
    play music "io.mp3"

    i "Ah...You’re finally awake."
    s "...Io?"
    s "Where am I?..."

    scene iosenseifaint18
    with dissolve

    i "My room. "
    i "You passed out in the bath...which, in hindsight, is probably my fault after letting you stay in there for over six hours. So yeah, I’ll take the hit for this one."
    i "Do you...need anything? Water? Tea? Maybe like, a...sandwich or something? "
    i "If there’s something specific you’re craving, it means your body’s probably low on some kind of nutrient or something. And there’s plenty of stuff downstairs I could grab for you."
    s "How long have I been out?"

    scene iosenseifaint19
    with dissolve

    i "Not long. Maybe only twenty minutes or so. But I was somehow able to drag you up here all by myself, which I should definitely be praised for. Just...when you’re a little more conscious. I can wait until then."

    "I stare up at an unfamiliar ceiling, but instead of wondering what transpired between when I passed out and now, I get stuck guessing how many more times I’ll wake up here."
    "One if I’m lucky. "
    "Two if Io is an idiot."
    "Three or more if there’s anything to this connection other than “obnoxious girl” and “the guy she latched onto.”"
    "The room smells like her — a mix of blueberries and wood polish. It’s just as cluttered as her dorm and it appears as though it hasn’t been dusted or cleaned in over a year."
    "She probably doesn’t spend much time in here. And if I didn’t know her as well as I do, I might even mistake it for some sort of storage room."
    "But, with that being said...it’s far more comfortable than it has any right to be."
    "And I’m not quite sure if I’m just saying that because I’m waking up in a daze."
    "I stare at the ceiling again. "
    "There’s a tennis ball grip on the pull-chain of a fan."
    "The word “Io” is written on it."
    "And this one small glimpse of one small speck of her childhood makes me sick to my stomach for the things I was thinking just a short while ago."
    "I’d give anything to not desire fruit before it’s at its ripest — and I curse this body’s need for the sourest of sweets."

    i "So...tea? Water? What’s it gonna be?"
    s "You really carried me all the way up here by yourself?"

    scene iosenseifaint20
    with dissolve

    i "I’m stronger than I look, Sensei. "
    i "Though, I will reiterate that it was more like {i}dragging{/i} you than carrying you. And if you feel sore tomorrow morning, blame the stairs, not me."
    s "Thank you, Io. I really appreciate that."

    scene iosenseifaint21
    with dissolve

    i "It’s nothing. Like I said, it’s probably my fault in the first place. "
    i "Oh, and I couldn’t get your pants back on without getting a little too {i}handsy,{/i} so I hope you don’t mind what I dressed you up in instead."

    scene iosenseifaint22
    with fade

    s "..."
    i "..."
    s "What have you done to me?"
    i "What? I think you look kinda cute in this. It’s a side of you I’m sure that only {i}I’ve{/i} gotten to see, and that makes me really happy."

    scene iosenseifaint23
    with dissolve

    s "Why do you even {i}own{/i} something like this?"
    i "It’s my aunt’s, obviously. She’s not really known for her sense of fashion. And {i}I’m{/i} not really known for wearing flashy colors or leopard print."
    s "Neither am I. Where are my normal clothes?"
    i "Folded near the door. But you don’t need to worry about getting changed right now. Let me take care of you a little bit longer. Just until you’re ready to go home."
    i "Heck, you don’t even have to go home today if you don’t want. My aunt’s away for the whole weekend and I’ve got the place to myself."
    s "And you’re sure this is okay?"
    i "Of course. If I’m gonna treat anybody to the ultimate Io special at no charge at all, it’s you. "

    scene iosenseifaint24
    with dissolve

    s "..."
    i "..."
    i "Wow, you must {i}really{/i} be out of it. I basically just handed you the perfect opportunity for another perverted joke and you completely squandered-"
    s "I’m sorry for saying all that stuff to you earlier, Io."

    scene iosenseifaint25
    with dissolve

    i "...huh?"
    s "I know it makes you uncomfortable, but I keep doing it anyway. "
    s "You don’t deserve that."
    i "..."
    s "..."

    scene iosenseifaint26
    with dissolve

    i "Even..."
    i "Even {i}if{/i} that’s true, it’s not something you need to apologize for. "
    i "There’s no reason you should have to change the way you are just because {i}I’ve{/i} got issues. That’s not fair to anybody."
    s "What’s not fair is that you have to go so far out of your way for me for things like this, but I never do {i}anything{/i} for you."

    scene iosenseifaint27
    with dissolve

    i "Now, that’s not true at all."
    i "You brought me into your class when I wasn’t happy in my last one. "
    i "You let me bother you all the time even though I know it annoys you and you’ve miraculously not asked me to stop talking to you yet."
    i "You even chased me out of the bathhouse when I got upset about my trashy toy and held my hand in the park."
    i "I’m not the only one who does stuff for you, Sensei. In fact, this is {i}nothing{/i} compared to everything you’ve done for me and-"
    s "..."
    i "..."
    s "And what?"

    scene iosenseifaint28
    with dissolve

    i "Pfft! "
    s "...And {i}what?{/i}"
    i "Hahaha! Hahahahaha!"
    i "I’m sorry! I can’t do it! I tried, but I just can’t! It’s not possible to have a serious conversation with you while you’re dressed like that! Hahah! Hahahahaha!"

    scene iosenseifaint29
    with dissolve

    i "Okay, okay. Let me try this-"

    scene iosenseifaint30
    with dissolve

    i "Hahahaha! Ahahaha! Hahah! Ahh! Oh god! I can’t do it! I can’t!"
    s "{i}Hah...{/i}"
    s "You said my clothes are near the door?"

    scene black
    with dissolve2

    i "Hahah! Hahah...{i}ahh...{/i}Yeah...Hahaha...If you want to keep talking, go ahead and put them on."
    i "Either that or I can keep them as a keepsake of yours and you can keep my aunt’s clothes as a keepsake of- oh. The pants are already off."
    s "This is not a memory I want to treasure and I’d prefer if we never talked about this-"

    play sound "doorslam.mp3"
    scene iosenseifaint31
    with hpunch

    u "Io! I came as quickly as I could! Is Sensei really-"

    scene iosenseifaint32
    with dissolve

    u "..."
    i "Hey, Uta. He’s awake now. You don’t have to worry anymore."
    u "..."

    scene iosenseifaint33
    with dissolve2

    i "Uta?"

    play sound "thump.mp3"
    scene iosenseifaint34
    with hpunch

    s "..."
    i "Welp. Uta's dead now."
    s "That was quick."
    i "Rest in peace...my dearest friend."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ bathhouse35p1 = True
    $ io_love += 1

    "........."
    "......"
    "..."

    jump bathhouse35p2

label bathhouse35p2:
    if _in_replay:
        play music "io.mp3"

    scene iocollapse1
    with dissolve2

    "It appears that tonight will be a night of collapses."
    "It started with me- overstaying my welcome in a welcoming place until {b}something else{/b} came and forced my head underwater."
    "If it weren’t for Io’s inherent need to remain burrowed into my scales in order to function, I’d probably be a lot worse off than I am right now. "
    "I repeatedly thank her inside of my head, doing my best to not curse her in the process as I’m often unsure of whether or not staying here is good for me after all."
    "We’re at a point now where I often contemplate disappearing again for the sole purpose of making everyone else’s lives easier."
    "Unfortunately, there are reasons for me to stay here. Which allows me to circle back to my incessant, half-hearted gratefulness and remind you that this is a night of collapses."
    "Uta was the next to collapse- and she’s currently tucked into the same bed I was asleep in just minutes ago. But the reason for her departure from the conscious world was a lot more cut and dry."
    "Unless my penis reminded her of something she’d rather not see, that is."
    "But based on the hue of her cheeks and the smile plastered to her face even now, I don’t think that’s the case."
    "Io will be the last to fall — though, it’s difficult for me to say that when she’d likely have you know she started tonight from the ground already."
    "She’s been trying to regain her footing since I’ve met her, and I’ve done nothing but kick her in the kneecaps as she tries to get up."
    "But...in a sense, she’s been kneecapping herself as well."
    "In looking at the pull switch with the tennis ball grip, I recount the things she's done, both right and wrong, and prop up imaginary fingers on imaginary hands in order to keep track of them."
    "The one with all her issues is packed before I know it- so I add even more fingers to the invisible hand. "
    "I add...and add...and add until it’s no longer a hand at all, but a hideous abomination that only someone like her, who sees ugliness in beauty and beauty in ugliness, could ever grow to love."
    "Maybe that’s why she’s fallen so hard for me."
    "Maybe that’s one more reason she’d have you know she started off this night collapsed already."

    s "..."
    i "..."

    "I feel young again."

    s "..."
    i "..."

    "But I also feel as if I’m not meant to be here."

    i "Uta will be fine in a few minutes, Sensei. Just need to wait for the cock shock to wear off."
    s "I’m a little offended you don’t react the same way. Seeing how calm you are around it is mildly off-putting."
    i "Need I remind you that I’ve been doing this since before all the men disappeared? I’ve seen my fair share of penises and have built up a bit of an immunity as the days have gone by, good sir."
    i "Yours is totally the biggest though. So I don’t blame Uta one bit for fainting."
    s "I’m just going to say thank you and leave it at that so I don’t perv out on you any more than I already have tonight."
    i "I don’t {i}hate{/i} the fact that you do that, you know. And I definitely don’t want it to seem like I’m trying to change you or anything."
    s "Sure. You just {i}want{/i} me to change, right?"
    i "Right. And that’s totally different from changing you myself."
    i "I’m sure that goes both ways though, right? Like, there’s no way you’d accept all of me the way I am now. If you did, you’d be an idiot."
    s "Well, you’re right about that. You have more flaws than I can fit onto one invisible, mutated hand."
    i "An invisible mutated what now?"
    s "Don’t worry about it. The point is that both of us suck and that we’ll probably continue sucking for the rest of our lives."
    i "True that. But we can suck together and that’ll make it okay."
    i "It’s better to wear your flaws like decorative patches than to keep them tucked in your pockets after all."
    i "Because at least {i}we{/i} know who each other really are."
    s "..."
    i "..."
    s "Do we?"
    i "..."
    s "..."
    i "We know enough."

    scene clearnightsky
    with dissolve2

    i "There’s only so much room on one jacket for...patches and stuff. And if you’ve got deep pockets, then...there’s no harm in-"
    s "Can we do away with the clothing metaphor while I’m still freshly wounded by the outfit I was wearing just a minute ago?"
    i "Yes, thank god. I was about to back myself into a corner and had no idea how I was going to get out of it."
    s "Seems par for the course nowadays. You look that way every single time you step into the classroom."
    i "I’m sure you have a handful of places you’d rather not be as well."
    s "Well...you’re definitely right about that."
    i "You wanna talk about it? Or you wanna ignore this part of the conversation and move onto something that makes it seem like we suck a little bit less?"
    s "I never really want to talk about anything, to be honest. Which is extremely annoying because I keep {i}doing just that{/i} lately."
    s "And the worst part is that I’m not even trying to. It’s just happening."
    i "Well...there’s only so much room on one jacket."
    s "I thought we were done with clothing metaphors?"
    i "Me too, but I couldn’t think of anything better other than a bottle and that’s just way too cliche."
    i "The usage was a little different this time, though. In fact, I like this new one way more than the flaws one. There really is only so much room on one jacket, Sensei."
    i "You can decorate it with a million things that make it look nicer and more colorful..."
    i "But after a while, it’ll be hard to tell what any of it means at all. All those patches will start overlapping and you’ll lose any chance you have of ever blending into the background."
    s "Is that still what you’re trying to do in school?"
    i "That’s what I’m trying to do everywhere."
    i "And it makes trying to stand out at the same time really hard. Those two things kind of contradict one another, you see."
    s "We can’t have everything. No one can."
    i "Too many patches, not enough jacket."

    scene iocollapse2
    with dissolve2

    s "..."
    i "..."
    i "Crap. I think I might be the next one to pass out."
    s "You can fall asleep if you want. I’ll stay here until...either one of you comes back to life."
    i "I think I can hold out for a little longer. If I fall asleep, I’ll miss out on {i}this.{/i} And I’ll be damned if I don’t savor this shoulder for every second I can."
    s "I’m just glad that’s all it takes to make you happy when everyone else always seems to want more."

    scene iocollapse3
    with dissolve

    i "Careful. You’re about to open up. And you were {i}just{/i} talking about how you hate that you keep doing that lately. "
    s "That’s not what I was trying to do, Io."
    i "Well, what were you trying exactly? Because the untrained observer might interpret that “everyone always wants more” as a bit of narcissism or braggadocio leaking through."
    s "Good word."
    i "I don’t just show up to class because I {i}have{/i} to, you know. "
    s "You don’t {i}have{/i} to show up to class at all."
    i "True. But I actually kind of like learning. Well, some things at least. "
    i "Or...at least the {i}idea{/i} of learning, I guess...You know, since you always seem more focused on flirting with all your fake girlfriends than {i}molding our minds.{/i}"
    s "If I were to try and {i}mold{/i} any of your minds, I’d most likely just turn them into gross, unrecognizable lumps of clay."
    i "He says, completely unaware that a gross lump of clay is currently resting its weird clay head upon his shoulder."
    s "All I meant was that it’s...nice you’re content with just {i}this{/i} sometimes. "
    s "It’s...a bit of a reprieve."

    scene iocollapse4
    with dissolve

    i "You..."
    i "..."
    i "Fuck. I’m about to ruin things."
    i "You don’t have to lie to me, Sensei."
    i "I know you abhor the person I am and the things I want...or, in some cases...{i}don’t{/i} want."

    scene iocollapse5
    with dissolve

    s "I know that’s how I made it sound earlier, but-"
    i "It wasn’t {i}just{/i} earlier. It’s all the time."
    i "You’ve been trying to take things further with me for like, {i}forever.{/i} And I’ve done nothing but shoot you down. So to hear you say you’re {i}glad{/i} that I’m like this now is...{i}kind of{/i} a slap in the face."
    i "It’s like...all that anguish I felt for not being who you want me to be was totally pointless. So just tell it to me straight instead of pretending like you’ve been okay with me this whole time."

    scene iocollapse6
    with dissolve

    s "..."
    i "Knew it. Everything is ruined. Fucking Io. You did it again."
    s "Nothing’s ruined, I..."
    s "I {i}have{/i} been pushy with you. I know that."
    s "But the reason for it has nothing to do with me not accepting who you are or...{i}disliking{/i} you or anything like that. I think those parts of you are fine, just...a little confusing."
    s "I’m...not really good when it comes to connecting {i}without{/i} relying on the...physical aspect of a relationship to bridge the gap between myself and...whoever else."
    i "I can help you build that bridge, you know. You don’t have to do it alone."
    s "I know. But, like I said...that’s not really an area of expertise for me. "
    s "So I probably just tried to take the easy route and lure you into having sex with me so I could...fall back on that instead."
    i "Gotcha."
    i "I get it now. "
    i "That’s a little different from what I thought was going on...but I’m really glad you told me since what you said is {i}way{/i} better than you only hanging around for the, uhh...{i}potential benefits.{/i}"
    i "The truth is, and there’s probably no need for me to actually {i}say{/i} this when I’ve already made it pretty obvious, but..."
    i "I don’t really look at that kind of stuff the way everyone else does."
    i "I don’t think it’s necessary for a functional relationship at all."
    i "I think that the only reason people make such a big deal of it is because it’s portrayed in movies and TV as this huge, important concept when, in all actuality...it’s kind of repulsive."
    i "We’re taught when we’re younger that we’re only supposed to do that kind of stuff with people we love. Then the second we get older, it’s no longer about loving anyone at all — just “feeling good” or something."
    i "But what if it doesn’t feel good? What if one person’s idea of pleasure is another’s nightmare brought to life?"
    i "The idea of letting someone inside of {i}my{/i} body makes me so fucking sick at this point that it’s borderline impossible to even speak about sometimes. "
    i "If you wanna get even more real, it’s taking all I have to not vomit right now."
    s "Then stop."
    i "Are you sure?..."
    i "We were just about to reach the climax. "
    i "Pun not intended."
    s "I don’t want you doing anything you’re not comfortable with...And if this is a topic that makes you feel sick, we can stay away from it."
    i "Thank you, Sensei..."
    i "I get that it’s probably disheartening to hear that I’m {i}this{/i} against sleeping with you...but that’s just something I can’t imagine myself budging on any time soon."
    i "I’m a special case. I should have held up a big warning sign when we first met or something. “Hi, I’m Io. Please don’t touch me.” Something like that."
    s "It’s just one kind of touching, though."
    i "That’s right. It’s just one kind of touching."
    i "You can hold my hand whenever you want. You can hug me whenever you want. You can even {i}kiss{/i} me if the thought of that doesn't repulse you for some strange reason. "
    i "Just...anything more than that is..."
    s "..."
    i "..."
    i "I can’t do it."
    i "I’m sorry."
    s "There’s nothing to apologize for."
    i "There is, though. "
    i "I get that I’m an outlier and that...given your apparent libido, I’m pretty much the worst possible match for you on a physical level."
    i "But I get that you have “needs” and stuff, so..."
    i "If you were to ever make me your girlfriend, I wouldn’t be opposed to you...you know..."
    i "Doing that kind of stuff with other people..."

    scene iocollapse7
    with dissolve

    s "What?..."
    i "O-Obviously not with just anyone! It would need to be someone I’m okay with! Like Uta or..."
    i "Actually, Uta is probably the only person right now I’d be cool with. Or...maybe Yuki too."
    i "Basically, it would have to be someone else I could be around every day. And instead of doing sexual stuff with {i}me,{/i} you could take care of all of that with the...other girl."
    i "And we’d all share our time equally and...I guess for you it would be like having two or...one and a {i}half{/i} girlfriends since I can’t...you know...uhh..."
    i "This sounded a lot less insane when I pitched it to Uta, I swear."

    scene iocollapse8
    with dissolve

    s "You pitched this to Uta already?"
    i "Yeaaaaah...but I don’t think it went very well."
    s "Io...would you seriously be okay with a relationship like that? You wouldn’t feel left out at all?"

    scene iocollapse9
    with dissolve

    i "Left out? Why would I feel left out? I already told you I don’t look at that kind of stuff the way other people do. And if it’s with someone else I love, I’d be totally okay with it."
    i "The big thing for me is just knowing I’m wanted and needed and...that I have someone to share all of my shitty thoughts with. "
    i "Whatever you and the other girl do to each other would be fine so long as it doesn’t come between all of us. I’d just stay out of that part."
    i "But I’m sure you and I could find something to do on our own as well. Same thing with me and the girl who, again, would probably be Uta because I can’t imagine this sort of future with anyone else."
    s "..."
    i "Again, I swear it sounded less crazy when I pitched it to her. I think I’m fucking things up right now."
    s "No, I just..."
    s "That’s not really...a proposal I was expecting from you given how...combative you’ve been in terms of me with literally any other girl."
    i "That’s because I don’t {i}like{/i} any of those girls. But if you were to hook up with Uta, I wouldn’t really mind at all. "
    i "In fact, I’d be happy for you guys since you’re my two favorite people and, to be honest, you both have {i}way{/i} too much sexual energy that needs to be let out."
    i "I’m just not sure if Uta sees you the same way I do. If she did, I’d be 100%% down to give this a shot."
    i "Like sure, it might have its issues at first, but what doesn’t? "
    i "It’s the only way the two of us could ever be together without me completely rebuilding everything I am. And I might be great at building stuff, Sensei, but that is a task so daunting that even I wouldn’t touch it."
    s "You really...can’t imagine a future where the two of us are together {i}without{/i} a second girl?"

    scene iocollapse10
    with dissolve

    i "Not one I can realistically see happening at least..."
    s "Io..."
    i "I can’t give you what you want, Sensei."
    i "All I can do is hold you over."

    scene black
    with dissolve2

    u "Nngh...what time is it?..."
    u "What happened to me?..."
    i "Morning, sleepyhead. You passed out after walking in on Sensei’s giant wang."
    u "Oh...crap."
    u "I was really hoping that was a dream."
    u "He’s...not still here is-"
    s "Morning, Uta."
    u "Ah! H-Heeeeey, Sensei! Crazy meeting you here! Hahah!"
    u "Hey, uhh...I ran here all the way from the dorms, so if it seemed like I was passing out after seeing your-"
    u "Actually, wait. Starting over. I didn’t see anything at all! I was just really tired!"
    u "So tired that...I’m going back to sleep! Goodnight!"
    i "Uta, no one is going to hold it against you for-"
    u "Don’t hold it anywhere near me! That thing was the size of my leg and it wasn’t even hard yet!"
    s "I thought you said you didn’t see it?"
    u "I thought I said goodnight!"

    "Uta wakes up and...promptly goes back to sleep before Io and I can put a definitive end to our conversation."
    "And while the final arc of our extremely uncomfortable and alarming discussion was the {i}one{/i} bit of salvation I had during tonight’s mandatory collapse-"
    "It didn’t pick me up at all."
    "It left me wanting nothing more than to remain stuck here-"
    "Glued to the floor-"
    "And gazing into the deep blue eyes of a girl that I should not want, but do."
    "Thus one more name is added to the list of things I can not have."
    "And it’s distressing in ways that nothing else has been."
    "I decide against wasting any more thoughts on it."
    "I feel like doing so would just make me sick."

    $ renpy.end_replay()
    $ bathhouse35p2 = True
    $ io_love += 5
    stop music fadeout 8.0

    "{i}Io’s affection has increased by 5!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm35:
    scene iovisityuki1
    with fade
    play sound "knock.mp3"

    "I decide to spend the night with Io in hopes that, this time, I’ll be able to make it at least an hour or two in without making her uncomfortable."
    "It should be a little easier now that she’s outright told me about her aversion to [[the good kind of] physical contact, but that doesn’t mean I won’t figure out a way to ruin things regardless."
    "Because, to be fair, she’s dropped plenty of hints about this exact thing so far and it has changed literally nothing about my actions- but that ends today."
    "Or rather, it ended last time we talked. But also today."
    "Anyway, here comes Io."

    play sound "dooropen.mp3"
    scene iovisityuki2
    with dissolve

    u "Greetings, Master! Party of one? Our specials today are smiles and love. And also the new deluxe strawberry parfait Osako-chan just came up with for the low, low cost of 2,000 yen."
    s "Has the cafe somehow gone bankrupt and been relocated to your dorm room?"

    scene iovisityuki3
    with dissolve

    u "As if we’d ever go bankrupt with how much time you spend there, Master. You’re basically subsidizing Uta-chan’s entire livelihood at this point."
    s "Well, if the cafe isn’t here, why are you in Uta-chan mode?"
    u "Beats me. I don’t always get to choose when I switch back and forth. What brings you over, though? Which one of us are you lookin’ for, you sly dog you?"
    s "Io."

    scene iovisityuki4
    with dissolve

    u "Man, you couldn’t even lie to me?"
    s "Sorry, there’s just something I wanted to talk to her about that I probably shouldn’t involve you in at this point in time."
    u "Well, what the heck is it? We don’t keep secrets in this household. Out with it, Master."
    s "Oh, you know. Just that quirky character trait of hers where she wants me to have sex with her best friend so we can all live happily ever after."

    scene iovisityuki5
    with dissolve

    u "She actually told you about that?!"

    if day <= 5:
        u "Also, what the heck do you think you’re sayin’ in the middle of the hallway on a weekday?! Someone could hear you!"

    s "I take it you were just as surprised to hear about this as I was?"

    scene iovisityuki6
    with dissolve

    u "Oh! Not at all, Sensei! I thought it was totally friggin’ normal that girl-hating Io was randomly cool with the idea of a throuple! I wasn’t surprised at all!"

    scene iovisityuki7
    with dissolve

    u "That set your sarcasm detector off? Cause it should’ve. "
    u "I have no idea what that girl’s been on lately. But whatever it is, her dosage needs to get halved cause this whole throuple thing is just crazy talk. The heck does she think she’s proposing?"
    s "I take it you’re not a fan of the idea, then?"

    scene iovisityuki8
    with dissolve

    u "Course I’m not a fan of the idea."
    u "I get where it’s coming from, but...I don’t know. What she wants just seems all sorts of wrong to me. There’s no way something like that could work out without one of us getting hurt."
    s "Gotcha. So it’s not the having sex with me part you’re not cool with, it’s the Io part."

    scene iovisityuki9
    with dissolve

    u "Huh? What? Huh? Me? You? Huh?"
    s "..."
    u "..."

    scene iovisityuki10
    with dissolve

    u "A-Anyway! Io was going over to Yuki’s place tonight and...I’ve got lots of homework to do, so...it’d probably be best if you just...you know...didn’t come inside."

    scene iovisityuki9
    with hpunch

    u "The room! Didn’t come inside {i}the room!{/i} Not...Not Uta-chan."
    s "I knew what you meant, Uta. "
    u "Uta-{i}chan.{/i} Regular Uta’s not home. Cause she’d {i}definitely{/i} never say any of this weird stuff that the customer service oriented version is saying."

    scene iovisityuki11
    with dissolve

    u "Anyway! Have a nice day! Or night! And don’t come anywhere you’re not supposed to! Bye!"

    play sound "doorslam.mp3"
    scene iovisityuki1
    with hpunch
    stop music fadeout 15.0

    u "{i}AAAAAAAAAAAAAAAAAAAAHHHHHH!{/i}"
    u "{i}WHY DID I SAY THAT?!?!?!{/i}"
    s "You know I can still hear you in there, right?"
    u "No you can’t! Go away!"

    scene black
    with dissolve2

    "With nothing else to do and Io nowhere to be found, I decide to head home for the night."
    "But only after embarrassing the one resident of Dorm 7 that I {i}don’t{/i} have to be careful with."
    "It’s definitely strange hearing that {i}Uta{/i} is the one who has issues with Io’s “arrangement,” though."
    "If you’d have asked me several months ago, I would have assumed it to be the other way around."
    "And while it’s true that both of them have rejected my advances, it seems like only one of them is forcing themselves to."
    "The other is just defective."
    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    scene iovisityuki12
    with dissolve2
    play music "hometown.mp3"

    i "I didn’t overdo it, did I?"
    i "No. No way. I mean, this is Yuki we’re talking about. I highly doubt she’s actually cooking herself balanced meals every night."

    scene iovisityuki13
    with dissolve

    i "But, then again, this is weird. I’m being weird. She didn’t even invite me over and now I have enough groceries to fill her fridge."
    i "Wait...does she even have a fridge? Should I just try and return all of this stuff? Does the grocery store even accept returns?"

    scene iovisityuki14
    with dissolve

    i "Damn it, Io. Can you do anything right at all? You’re just going to make Yuki think you’re awkward and- "
    i "But...wait. You {i}are{/i} awkward. So why is having someone {i}think{/i} you’re awkward bad when allowing them to think {i}otherwise{/i} would only screw up their expectations and-"
    i "You know what? Maybe I’ll just go home. I can always try again next week. And I’m kind of tired anyway, so-"
    y "Hm? "

    scene iovisityuki15
    with dissolve

    i "Hm?"

    scene nightsky
    with dissolve2

    y "You look kinda familiar..."
    i "I’m not. You probably have me confused with someone else. "
    i "I’ll be on my way n-"
    y "Nah, hold up a sec."

    scene iovisityuki16
    with dissolve

    y "Ain’t we in the same class or whatever?"
    i "Uh..."
    i "No. I’ll be leaving now."
    y "The fuck you lyin’ to me for? You’re, uhh...Ito, right? Or was it...Iro?"
    i "..."
    y "Iori?"

    scene iovisityuki17
    with dissolve

    i "You know what? Come to think of it, we {i}are{/i} in the same class. I just don’t normally see you in there. "
    i "And it’s {i}Io,{/i} by the way. We had an entire contest thing against each other...Ring any bells?"
    y "Not really. The fuck you doin’ over {i}here{/i} for, though? You live in this dump or some shit?"

    scene iovisityuki18
    with dissolve

    i "I was visiting someone. Or...{i}trying{/i} to at least."
    y "Friend of yours? Boyfriend? Family?"

    scene iovisityuki19
    with dissolve

    i "Do you forcefully interrogate {i}everyone{/i} you meet for the first time? Or...?"
    y "Oh, no. My bad. I just...ain’t really used to strikin’ up conversations and shit."
    i "Then why strike one up with {i}me?{/i} I probably hate people even more than you do."
    y "Just...seemed like you were havin’ a shitty night. That’s all. I’ll leave you alone if you want."

    scene iovisityuki20
    with dissolve

    i "Ugh...fuck my life."
    i "Aren’t you supposed to be harder to talk to or something? Why do you seem so...weirdly rational? "

    scene iovisityuki21
    with dissolve

    y "Beats the fuck outta me. I ain’t really known for my {i}rationality{/i} after all. But it ain’t like I’m just gonna go around startin’ problems with people for no reason whatsoever."
    y "The old me might’a done that shit, but I ain’t really like that anymore. I’ve like...{i}grown{/i} or something. Whatever the fuck they call it. "
    i "Do you...want me to {i}congratulate{/i} you? Because that's not going to happen."

    scene iovisityuki22
    with dissolve

    y "Not really. But if you wanna come inside and chill for a little while, you can."
    y "Ain’t my apartment, but I’ve got a key and shit. And it’ll give you a chance to rest or whatever before you finish chickening out on bringing all that shit to...wherever the fuck you were tryin’ to bring it."
    i "Uhh..."
    i "Yeah, I’m probably just gonna finish chickening out instead. I’ve seen what you can do to people and I’d prefer to not have my teeth punched in, thanks."

    scene iovisityuki23
    with dissolve

    y "I ain’t gonna lay a finger on you, don’t worry."
    y "Learned my lesson last time. Hit the wrong person at the wrong time {i}once{/i} and it’s like throwin’ away everything you’ve worked for."
    y "And it ain’t like I have shit to begin with now that I’m startin’ over again, but...still. I ain’t gonna touch you."
    y "Don’t fuck with me and I won’t fuck with you. That’s my new policy. Do with that whatever the fuck you will. Doesn’t make a difference to me."
    i "..."
    y "..."

    scene black
    with dissolve2

    i "Ugh...fine. Okay."
    i "But...just for a few minutes."

    "........."
    "......"
    "..."

    scene iovisityuki24
    with dissolve2

    y "Well...here we are. Welcome to Casa Del Shithole."
    i "Wow...Yuki’s place is actually a lot nicer than I thought it would be."
    y "Yeah. She ain’t-"

    scene iovisityuki25
    with dissolve

    y "Wait, what’d you just say?"
    i "Oh! Uhh...that...{i}your{/i} place is a lot nicer than I thought it would be."
    y "Really? Cause I could’a sworn you-"
    i "I think I know what {i}I{/i} said, thanks."

    scene iovisityuki26
    with dissolve

    y "R...Right. Well, as I was sayin’ before, this ain’t my place. I just come here to eat food and crash on the couch whenever I’m in the area."
    y "And I’ve been, like...lookin’ for jobs and shit around here, so I’ve been around a lot lately."
    y "Figured it’d be easy findin’ somethin’ over here since it’s, like...what do you call it...a low-income area or something? I don’t know. This is where the poor people chill, basically. So I’m right at home."
    i "It’s not that bad. I kind of like it."
    y "Yeah, you ain’t had to deal with the sirens and trains and shit in the middle of the night yet. Or the busted ass AC or how the windows get stuck when you try and open ‘em to get rid of all the smoke."
    i "I guess not..."

    scene iovisityuki27
    with dissolve

    i "Is there a fridge I can put all this stuff in? I don’t want it getting cold. "
    y "Then why the fuck would you put it in the fridge?"
    i "That’s-"
    i "Wait, hold on. No. I meant I...don’t want it getting cold...naturally?"
    y "What?"
    i "Can you just tell me where the fucking fridge is?"
    y "Behind me and to the left. Mind grabbin’ me a water while you’re in there?"

    scene black
    with dissolve2

    i "Are you incapable of getting one yourself? What about the nine thousand half-empty water bottles lying around the room? Will one of them work?"
    y "Ew, no. I can’t remember which ones are mine and I’ll be damned if I accidentally trade spit with some bitch who’s probably got every disease known to man."
    i "Boo-hoo. Woe is you."
    y "The fuck’s your deal? Just get me a damn water. You can take one too if you want."
    i "I just think you should be a little less generous when it comes to giving away {i}someone else’s{/i} stuff when none of this is yours to hand out in the first place."
    y "And I think you should dye your hair a normal fuckin’ color but you don’t see me preachin’ that with every single step you take."

    scene iovisityuki28
    with dissolve

    i "Touche. Also, whoops. Forgot your water."
    y "You didn’t forget shit, you little brat. You did that on purpose."
    i "If you want water, you can buy your own or use the faucet. Someone worked for what’s in that fridge and it’s not fair if someone else just takes it."
    y "Use the faucet? In a place like this? Would be safer to drink my own piss. ‘Sides, the bitch who lives here owes me. She can go without a bottle or two."
    i "Owes you for what exactly?"

    scene iovisityuki29
    with dissolve

    y "Oh, not much. Only scarring me for life and shit like that. You know how it is. "
    y "Or maybe you don’t. Ain’t got a clue what your fuckin’ background is- just that it probably ain’t hard to connect the dots in figurin’ out where you and me are on the {i}social ladder{/i} based on context clues."

    scene iovisityuki30
    with dissolve

    i "Yeah...I guess you're right about that."
    y "..."
    i "..."
    y "So what’s {i}your{/i} deal? Where’s that “fuck the world” attitude come from? Shit like that doesn’t just happen on its own. Know that from experience."
    i "I’d prefer not talking about myself with people I don’t know very well."
    y "Shit like that is what makes it impossible to get to know somebody in the first place, but..."
    y "Fair enough. Just trying to make shit less quiet. And it seems like the only things we’ve got in common are bein’ stuck in here and the fact that we’ve got the same douchebag teacher."
    i "Sensei’s not a douchebag. He’s a good person."
    y "Sure, if your idea of being a good person is hooking up with children and getting paid to neglect your responsibilities all day long."
    i "No one’s perfect. We’re probably just as fucked up as he is when it really comes down to it."
    y "But we’re also teenagers. We ain’t supposed to be {i}perfect.{/i}"
    y "This is the age where we’re supposed to be fuckin’ around and findin’ shit out as we go. That dude’s fuckin’ doubled our lives and he still hasn’t gotten that shit down yet."
    i "So what? Neither has your mom apparently and you’re still coming here to mooch off of her. Some people take longer to fully develop than others."
    y "And some people never fully develop at all."
    i "..."
    y "..."

    scene iovisityuki31
    with fade

    y "From one fuck-up to another, you ever worry that you’ll end up like that? That school will end before you’ve ever figured out a direction you’re supposed to head in and that it’ll all just...burn to the ground after that?"
    i "Think? No. I’ve already accepted that fate."
    y "Why? We’re young as shit. Feelin’ sorry for ourselves is only gonna wind up hurting the people we care about further down the line."
    i "You say that as if I have anyone I actually care about."
    y "Don’t you?"

    scene iovisityuki32
    with fade

    y "You’re close with that loudmouth girl, ain’t ya? The short one who sucks at arm wrestling."
    i "Uta? Yeah. She’s the only girl I actually like."
    y "Then wouldn’t you feel like shit letting her down and not doin’ anything with your life?"
    i "Not really. She knows better than to expect anything out of me. And I doubt I’ll wind up even making it to 30 in the first place."
    y "What? You ain’t, like...thinkin’ of killin’ yourself or some shit, are you? Cause if I just accidentally prevented a suicide, that’s pretty fuckin-"
    i "I’m not going to do something like that. I’m way too afraid of not knowing what comes next."
    i "It’s just a feeling I have, really. There’s no rhyme or reason to it."
    y "Huh..."

    scene iovisityuki33
    with fade

    y "Well, that’s fuckin’ dumb."
    i "I never said it wasn’t. All I said was that it’s a feeling I have. And with that in mind, it’s no different from wasting your time worrying whether or not you’ll wind up as someone’s definition of a failure."
    y "How so?"
    i "Well...life is just a whole bunch of {i}feelings{/i} at the end of the day. Right?"
    i "We get happy when good things happen...or sad when shitty things happen. All we’re really doing is reacting to the world around us doing its...shitty world stuff."
    i "And so, when you start to think about it like that, nothing we do matters in the first place. "
    i "Like, yeah, we can work hard and set goals and shit. We can make our {i}dreams come true.{/i} But there’s so much happening {i}around{/i} us that we have no influence over that it makes those goals seem kind of sucky."
    y "I ain’t gettin’ it. How’s that make thinkin’ you’re a failure the same thing as thinkin’ you’re gonna die at an early age?"
    i "Well, it’s like...not everybody has the same idea of what it means to...fail, I guess? And they’re both...things you can never really know for sure? Does that make sense?"
    y "Not really. Sounds to me like you’re just talkin’ outta your ass."

    scene iovisityuki34
    with fade

    i "Ha...maybe you’re right."
    i "Maybe I {i}am{/i} just talking out of my ass."
    i "But when you never learn how to properly express yourself, things like...explaining your {i}feelings{/i} or {i}opinions{/i} become a lot like mazes. "
    i "And even the people who {i}make{/i} mazes aren’t immune to getting stuck in them. We all need to fail or get lost and shit and...some people can work through that while others just give up."
    y "And you’re one of those “give-up” types, I guess?"

    scene iovisityuki35
    with fade

    i "I guess."
    i "Which means you’re the other one?"
    y "I guess."
    y "Ain’t nothin’ to write home about though when I still ain’t done shit."
    i "Not like I have anyone to write to in the first place."
    y "Same here."
    y "Truth is...I’ve only {i}just{/i} started talkin’ to my mom again after all the shit she put me through when I was little."
    i "...What?"
    y "It’s like...that whole “never learning how to express yourself” thing you brought up a second ago. "
    y "That was me too. Or...{i}is{/i} me. Which is probably why I also only have, like...one friend."
    i "..."
    y "My mom was a hardcore junkie. "
    y "She walked out on me when I was really little and I had to...pretty much grow up {i}without{/i} parents since my dad was always busy with...{i}work.{/i}"
    y "Wasn’t easy...but I made it this far without anyone’s help, so I guess that’s somethin’ to be proud of or whatever."
    y "And, you know...I think I was doin’ pretty okay until she walked back into my life. Like, yeah, I was an asshole and a bully and shit...but I’m still kind of those things {i}now,{/i} so..."
    y "I just don’t get how someone can disappear for so long and then just...try to patch things up. Makes my whole struggle growin’ up seem like it was all for nothing."
    y "Like she got to take the easy road while I bashed my head against the fuckin’ wall hopin’ that one day I’d-"
    i "Pfft..."

    stop music fadeout 5.0
    scene iovisityuki36
    with dissolve2

    y "Huh?..."
    i "Pfft!"
    i "Hahah...haha...hahahah!!!"

    scene iovisityuki37
    with dissolve

    y "Are you..."
    y "Are you...{i}laughing{/i} at me?..."

    play sound "static.mp3"
    scene iovisityuki38 with flash
    stop sound

    i "{i}That’s{/i} your tragic backstory?"
    i "Your mom {i}wasn’t there?{/i} And now she {i}is{/i} again?"
    i "That’s all it took to break you?"
    y "Wha-"
    i "Are you kidding? You are. You have to be. Am I really not supposed to laugh at that?"
    y "It..."
    y "It’s not funny!"
    i "Oh, I know."
    i "It’s fucking {i}hilarious.{/i}"
    y "Who..."
    y "Who the fuck do you think you are, talking to me like that?! You ain’t got the faintest idea of the shit that I’ve been through!"

    scene iovisityuki39
    with dissolve

    i "I would have {i}killed{/i} for what you’ve {i}been through.{/i}"
    y "You...what?..."
    i "Do you know what I got instead?"
    y "..."
    i "Tell me."
    i "{i}Do you know{/i} what I got instead?"
    y "..."
    i "..."
    y "No..."
    i "Good."

    scene black

    i "You don’t want to."

    "////////////////event complete"


    $ renpy.end_replay()
    $ iodorm35 = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ioarchery35:
    scene iotearoom1
    with dissolve2
    play music "io.mp3"

    i "Ahh...Finally, some peace and quiet."
    i "You know, you’d think kyudo of all things would be the quietest of all the clubs...but between Uta and Kirin, I just don’t know sometimes."
    s "That’s weird.  Uta’s usually so focused when it comes to archery."
    i "Yeah, but Kirin does this thing where she pollutes any environment she’s thrown into and, sometimes, that leads to Uta getting pulled back to her normal Uta-ish ways."
    i "I never have to worry about that with you, though. Because even when you’re talkative, which doesn’t happen much, you’re still kind of quiet."
    s "And you’re kind of hugging my leg so hard that it’s cutting off my circulation."
    i "That’s fine. I can probably make a sweet prosthetic after a few tries. Believe in me, Sensei. I’ll help you learn to walk again."

    "I find myself in...what I {i}believe{/i} is the tea ceremony room, but I might be incorrect about that as all I can remember from the last time I was in here is how red Uta’s face was."
    "But this time, I’ve taken up temporary residence with her best friend instead and Uta is none the wiser."
    "All the while, I cautiously and quietly bang invisible nails into an invisible wall I put up around myself to remind me not to do what isn’t welcome with today’s guest."
    "Not to make any sort of advances or allude to any sort of impurity- because that wall {i}is{/i} visible to one person and that person is, you guessed it...me."
    "I can do this. "
    "I did it with Molly and I can do it with Io."
    "I can accept that not everyone has an inherent desire to sleep with me and I can grow in ways dissimilar to the way I grow the most."
    "I can be a better person."
    "I can learn to protect things."
    "And if I can be better, that means Io can too."
    "The two of us are adaptable. We’re different in a million {i}other{/i} ways, but our resilience and the fact that our skin can camouflage to match its surroundings is what makes the two of us work as well as we do."
    "Or as well as I think we do."
    "Or as well as {i}she{/i} thinks we do, but I don’t understand because the way {i}I{/i} think isn’t the way {i}she{/i} thinks and the things {i}I{/i} do aren’t the things {i}she’d{/i} do when the two of us are thinking."
    "When the two of us are thinking is when we grow the closest."
    "But it’s also the scariest time of all — because every single word strips a plank from the bridge between us."
    "And one day, when we’re older and exhausted, our skin will lose its color."
    "One of us will lose the will to adapt."
    "And sometimes, it feels like it’s a race to get to that point and see who will break first."

    i "..."
    s "..."

    "But right now, the two of us are thinking."
    "And only one of us has thoughts that can be spoken out loud."

    i "Hey...Sensei?"
    s "Yeah?"
    i "I really like you."
    s "I know. You’ve already confessed on multiple occasions."
    i "I’m just gonna keep doing it, you know. "
    i "I feel safe when I’m with you. Which makes me {i}want{/i} to confess my feelings because it’s the one time I know I’m not going to be judged for them."
    s "I judge you all the time. The same way you judge me."
    i "Sure, but it seems to me like we keep ruling in one another’s favor if we can still sit here like {i}this.{/i}"
    s "Then it seems to me like your judgement is just as shot as everything else about you."

    scene iotearoom2
    with dissolve

    i "Yeah. I kinda suck, don’t I?"
    s "{i}And{/i} you have stupid hair."
    i "{i}And{/i} I’m really mean to all the girls you like."
    i "Remind me, why do you keep me around again? What are you getting out of this? Because we already know it’s not the thing you want."
    s "{i}What I’m getting{/i} is the opportunity to spend time with a cute girl that’s hopelessly devoted to me."
    i "But you’ve got tons of those. And most of them don’t have stupid hair or stupid mental health issues."
    s "Then I guess I’m just a masochist and like making things difficult for myself."

    scene iotearoom1
    with dissolve

    i "Ahh, yes. The “When life gives you lemons, squeeze them into your eyes” method. I know it quite well."
    s "Has your reason for wanting to be with me expanded beyond just “I was in the right place at the right time” yet?"
    i "Of course. Do you really think I could just endlessly hug {i}anyone?{/i} It should be obvious how precious you are to me by now."
    i "Just don’t ask me to describe why or how since I don’t have a reasonable explanation for it and will likely just make it sound like I don’t really care when, in all actuality, I do."
    i "I care {i}a lot.{/i}"
    i "I even had a dream about you last night. You wanna hear it?"
    s "Was I better or worse in the dream than I am in real life?"
    i "You were a cat."
    s "I...can’t figure out which one of the categories I listed that falls into."
    i "Do you ever dream about me?"
    s "..."
    i "Do you ever dream about {i}anything?{/i}"
    i "It’s not uncommon for some people to just never dream, you know. And I won’t be offended if REM-Sensei isn’t wasting any thoughts on Io when Io isn’t even worth any thoughts in real life."
    s "It’s not like I {i}don’t{/i} dream or anything...I just don’t do it very often and, when I do, what I see normally doesn’t make much sense."
    i "{i}But{/i} the question I posed was if you ever see {i}me.{/i} Even if it’s for something weird, like...helping you build a go-kart or something."
    s "I...can’t really remember. But I’ll try and keep track for your sake if it makes you happy."

    scene iotearoom3
    with dissolve

    i "You’re being really nice today. Do you feel weird around me now?"
    s "Io, come on."
    i "What? It’s a genuine question. I’m difficult enough as-is. The last thing I need is you having {i}another{/i} reason to show up at somebody else’s door instead of mine."
    s "Well, if I said yes, what would you even do about it?"
    i "Internally? Hate myself. Externally? Maybe a big hug or something."
    i "You still haven’t cashed in on that kiss I said you could have. That might pull you back to my side, right?"
    s "I don’t think it’s a good idea for us to do that right now."

    scene iotearoom4
    with dissolve

    i "Why not?"
    s "Trust me. It’s just better for both of us if we stick to...cuddling or whatever for now."
    i "Why do you always pause like that before you say cute words like “cuddle?” "
    i "Come to think of it, you never really say anything cute in the first place. It’s always straight-laced, semi-formal dialogue with you. Like you’re following the unofficial handbook on mid-thirties male speech."
    s "{i}Early-thirties.{/i} And I don’t know. That’s just kind of how I talk, I guess."
    i "There wasn’t like, somebody who taught you to speak that way? To never say anything fun? "
    s "I say fun stuff all the time. Or...at least I think it’s fun. But I’ve been calling this my hot boy summer for months and no one has laughed yet, so maybe my sense of humor just sucks."
    i "Say more fun things around me. Tell me a joke or something. Go."
    s "Uhh..."
    i "I’m waiting."
    s "Yeah, I’m aware. It’s been two seconds. It’s just kind of hard to think of any jokes on the spot like that."

    scene iotearoom5
    with dissolve

    i "I have one! You wanna hear it?"
    s "Yes, but I will judge you harshly if it’s not funny."
    i "Deal. What do corporate woodworkers do when they need to discuss their next project?"
    s "..."
    i "They have a {i}board{/i} meeting!"
    s "..."
    i "Get it? Like...{i}board.{/i} Like...wood. A wooden board."
    s "I get it. That silence was just me judging you harshly."

    scene iotearoom6
    with dissolve

    i "Hey, it could’ve been worse. It could’ve been, like...Tsuneyo’s stand-up set bad. "
    s "I am...very thankful it was not."
    i "What was that even about anyway? Like, raunchy humor is one thing...but to just blatantly start spreading ridiculous lies about people? That’s like...kind of fucked up, isn’t it?"
    i "Thank god nobody believed her. Cause all that stuff about the chuuni girl was actually nauseating. And another thing-"
    s "Hey, on the topic of the Dorm Wars, how are you feeling going into this year’s competition? Are you actually going to try?"

    scene iotearoom7
    with dissolve

    i "I’m glad you asked! Because I {i}am{/i} going to try this year!"
    i "Crazy things happen when you let Io do a thing Io actually wants to do. Which, to be fair, isn’t many things. But building a raft? That sounds super fun. I’ve never tried anything like that before."
    i "Plus, I get to compete against Miku! And I don’t despise her!"
    s "Yeah...you two seem to be seeing each other pretty often nowadays, huh?"

    scene iotearoom8
    with dissolve

    i "That’s right! I {i}am{/i} her pharmacist after all."
    s "Except...you’re not. You’re a random girl with a surplus of pills who doesn’t mind handing them out to other people."
    i "Isn’t that what pharmacists do?"
    s "Io, I’m trying to lecture you."

    scene iotearoom9
    with dissolve

    i "Why?! Today was going so well! Can’t we save all the serious conversation until next time or something?"

    scene black
    with dissolve2

    "I shift my lower body away from Io and inadvertently force her off of me."
    "There’s a moment of hesitance as she tries to figure out whether or not she should attempt to steal my leg again- and there’s a second moment when she reaches toward me with lightly-trembling hands."
    "My lack of morals prevents me from swatting her away as I don’t think it’s right to punish anyone for {i}anything{/i} when I’m sure I’ve done much worse."
    "But I do stare into her eyes in a way I’ve only done a few times before."
    "I haven’t had to look this way at any other girl — but Io feels less like a girl and more like a feral cat I need  to housebreak at times."
    "She does so many things that just go against all common sense, but..."
    "..."
    "I guess I do too."
    "And I guess that might be why she sees me the same way in her sleep."

    scene iotearoom10
    with dissolve2

    i "..."
    s "..."
    i "Am I in trouble?"
    s "Do I have the authority to ground you?"
    i "Not technically. But I like you enough to humor you by {i}acting{/i} grounded. Plus, it’s not like I ever go anywhere in the first place. If anything, being grounded sounds kind of like a vacation."
    s "Io, why are you medicating Miku when-"

    scene iotearoom11
    with dissolve2

    i "Because no one else is!"
    s "..."

    scene iotearoom12
    with dissolve

    i "I’m doing it because no one else is..."
    i "Miku’s got severe PTSD that was entirely untreated before I started sharing my medication with her."
    i "Do you have any idea what it’s like having to just fucking...raw dog that? It’s terrible. And it was holding her back from...living a normal life."
    i "And living a normal life when your trauma is {i}that{/i} fucking earth-shattering?...Well, that's...that's one of the hardest things {i}anyone{/i} could ever even {i}attempt{/i} to do."
    s "But that doesn’t make it okay to-"

    scene iotearoom13
    with dissolve

    i "Well, what would {i}you{/i} do instead?! Have her just deal with it on her own?! "
    i "You’ve seen her panic attacks, right?! She can barely breathe when they happen! And it’s not like you can just prevent her triggers from ever showing up, right?! So then what?! What would {i}you{/i} do?!"
    s "I’d...leave it to the professionals."
    i "Oh, so they could throw a bunch of shit at her and just see which one sticks?! It takes {i}forever{/i} to find the right medication for some people! Not to mention dosage and the cost and-"
    i "And you’re not even her guardian! In fact, she doesn’t even {i}have{/i} a guardian if I’m understanding her situation correctly! "
    i "There’s nothing anyone can do {i}but{/i} me and I can’t just sit back and watch her suffer when I know I can help!"
    s "I know you’re just trying to help. But what you’re doing is dangerous and you know that."

    scene iotearoom14
    with dissolve

    i "You know what’s even {i}more{/i} dangerous? {i}Not{/i} treating her."
    i "Miku is doing a million times better now. And that’s not just me saying it to save face. She’ll tell you herself. "
    i "Fuck, she probably doesn’t even {i}need{/i} to tell you. Just take one look at her and you’ll realize how much easier her life has gotten lately."
    s "I know Miku way better than you do, Io. "

    scene iotearoom15
    with dissolve

    i "Then you should know how much help she needs."
    i "Too many people just shrug mental health issues off because it makes them uncomfortable and it’s shit like that that winds up killing people."
    i "I’m not going to abandon her when I’m making a real difference in her life. You {i}know{/i} that’s what I want to do with mine. I’ve told you that."
    s "When you told me that, you were talking about toys...not pills."

    scene iotearoom16
    with dissolve

    i "Right, yeah. Let’s just pull her off the working medication and throw a fucking toy at her the next time she has a panic attack. That’ll work."
    s "Io, that’s not what I’m suggesting and you know that."
    i "Of course I know that. But I’m mad at you right now and I’m probably going to be a little more sarcastic than normal for a few minutes. If that’s going to be a problem, then just leave."
    s "..."
    i "..."
    s "You really care about Miku, don’t you?"
    i "Not really."
    s "So you’re doing all of this for...what? The principle of it?"
    i "I’m doing it for myself. But not in a “Playing pharmacist makes me feel like I have a purpose” sort of way."
    i "I’m doing it because if {i}I{/i} had to look my issues in the eye, I know how I’d feel. And I wouldn’t wish that on my worst fucking enemy."
    s "..."
    i "..."
    s "So...what then?"
    i "I don’t know. Sounds like you’re gonna tell on me or something. And then Miku will just be fucked until someone else comes along and decides she’s worth helping."
    s "I’m not the type to “tell” on anyone, Io. "
    i "..."
    s "You just have to realize how this looks from the {i}outside.{/i}"
    i "It just seems pretty fucked up that I got confronted for helping her before anyone confronted {i}her{/i} about getting help."
    i "That’s the kind of shit people like me have to go through, Sensei. No one ever helps themselves. It always starts with somebody talking us into doing something and then {i}us{/i} figuring shit out later."
    i "God forbid I ever try and be that for another person. God forbid I ever do anything that isn’t in {i}my{/i} best interest."
    s "But didn’t you say just a second ago that you were doing this for yourself?"
    i "Shut up."
    s "You really do care about her after all, huh?"
    i "..."
    i "No."
    s "..."
    i "..."
    s "Do you want to lay on my lap again?"

    scene iotearoom17
    with dissolve

    i "Huh? Aren’t we mad at each other?"
    s "I was a little mad in the beginning. But not anymore after hearing your rationale behind all this."
    i "So...wait. Where does that put us in regard to the medication situation? Can I keep sharing my stuff with Miku?"
    s "I...won’t stop you. But I want you to try and talk her into getting help from an actual professional rather than someone who just...has way too much experience."
    i "I’m not good at talking. You know this. If I talk to Miku, she’ll probably give up on taking medication altogether and just jump off a bridge."
    s "Then give her a phone number or...something. I don’t know. I have no idea how any of this works."

    scene iotearoom18
    with dissolve

    i "Sensei..."
    s "What now? I thought that was a pretty good ending to all of this. "
    i "It was, just..."
    i "Have you..."
    i "Have you really never tried taking anything to help with {i}your{/i}...problems?"
    i "You don’t have to go it alone, you know. "
    s "Are you going to start treating {i}me{/i} now too?"
    i "Don’t turn this into a joke. I think you could really stand to benefit from...something. "
    i "I’m just...not sure what."
    s "I’ll be fine. I’ve made it to 31 without anything like that and I’ll make it to 32 if the world ever goes back to-"
    i "I just really think you should reconsider. I want you to be happy and...it’s not like anything I can do will ever get you to that point."
    s "..."
    i "..."
    i "Sensei?"

    scene black
    with dissolve2

    s "Just lay back down, Io."

    $ renpy.end_replay()
    $ ioarchery35 = True
    $ io_love += 1
    stop music fadeout 7.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label iospring1:
    scene clearnightsky
    with dissolve2

    "I started reading again."
    "Not words that I should or words that I’m meant to, but words that make the pain more painful and remind me why I limp when a girl with red hair would rather be the splint I never asked for."
    "A blueish glow bleeds out from the screen of my phone, but the vision it carries with it is not one with inflated breasts nor hair in private places, no."
    "It carries with it, words. "
    "Words that make the pain more- "
    "You already know."
    "I already told you."
    "This one is particularly relevant. And it goes like this."
    "{i}It's late. I've come\nto find the flower which blossoms\nlike a saint dying upside down. {/i}"
    "{i}The rose won't do, nor the iris.\nI've come to find the moody one, the shy one,\ndowncast, grave, and isolated.{/i}"
    "{i}Now, blackness gathers in the grass,\nand I am on my hands and knees.\nWhat is its name?{/i}"
    "{i}Little sister, my indigo,\nmy secret, vaginal and sweet, you unfurl yourself shamelessly\ntoward the ground. {/i}"
    "{i}You burn. You live\na while in two worlds at once. {/i}"
    "This one is called “My Indigo” and it makes me feel a little less alone."
    "But the way I’m feeling doesn’t matter now when there’s so much left unfelt."
    "Like cholera I spread, siphoning the moisture that I’ve come to know as complacency from everything and everyone — leaving a trail of excrement in my wake toward another resting place."
    "To properly spread, I must find water."
    "I hope I can remember how to swim."

    i "Ah..."

    scene iobluedeath1
    with dissolve2
    play music "io.mp3"

    s "..."
    i "..."
    s "Hey."
    i "..."
    s "Long time, no see. How’s the bathhouse holding up?"

    scene iobluedeath2
    with dissolve

    i "We’re closed for the night."
    s "Isn’t it a little early for-"
    i "Sorry for the inconvenience."
    s "..."
    i "..."

    "I’ve spread a little faster than normal, I see. "
    "I didn’t even need to enter the water."

    s "Is something wrong, Io?"
    i "Something? No. Everything? Yes. But everything is {i}always{/i} wrong because I’m basically just the human equivalent of a magnet that’s forgone its attraction to metal in place of tragedy."
    s "That sounds pretty rough. But hey, if it’s any consolation, I’ve felt more or less the same about myself lately."
    i "Mhm."
    s "That’s it? Not in the mood to talk tonight?"
    i "Mhm."
    s "Are you mad at me or something?"

    scene iobluedeath3
    with dissolve

    i "I should be."
    s "..."
    i "I should be a lot of things right now. But of course I can’t get a hold of my brain and tell it how to feel because, if I could do that, this wouldn’t be a problem in the first place."

    scene iobluedeath4
    with dissolve

    i "Trash will be trash, right? Is that a phrase? Because if it’s not, it is now. I’m making it a phrase."
    s "Then I’ve got one of my own in saying that one man’s trash is another man’s treasure."

    scene iobluedeath5
    with dissolve

    i "Hoarding is a trauma response. I’m not taking that as a compliment. Both because I don’t want to be complimented and because I think I {i}am{/i} mad at you."
    s "For what?"
    i "Something I don’t want to bring up because I don’t want you to be mad at {i}me.{/i}"
    s "That’s a little hypocritical, don’t you think?"
    i "Have you been away for so long that you’ve already forgotten who you’re talking to right now?"
    s "Depends. Have {i}you{/i} forgotten how attached to me you’re supposed to be, even when we both know it’s wrong?"
    i "I don’t think I ever said it was wrong."
    s "Well, you’re acting like it’s wrong."
    i "Can you just tell me why you’re here so I can come up with some sort of shitty excuse for why it’s a bad time?"
    s "Can you look at me?"

    scene iobluedeath6
    with dissolve

    i "I don’t know if that’s a good idea...It’ll make me want to talk to you."
    i "And if I talk to you, we’ll have to talk about the last few months. Which means we’ll mention things that have changed and things that we’ve learned."
    i "Then, that will naturally progress to you learning that I know a thing I’m not supposed to know and that {i}you...{/i}"
    i "That you may have...{i}heard{/i} something about...someone who might...have stupid green hair or...is named Io..."
    s "No one really talks about you, Io."

    scene iobluedeath7
    with dissolve

    i "Huh?"
    s "It’s just hard to hear things about you when no one but Uta brings you up. And I’ve barely seen her lately either."
    i "So...you {i}haven’t{/i} heard anything then? No rumors...or...{i}anything{/i} at all?"
    s "None whatsoever. So, about this thing that you’re not supposed to know-"

    scene iobluedeath8
    with dissolve

    i "Sorry, I don’t have any idea what you’re talking about. And we’ve already spent too much of this reunion’s time on a thing I misunderstood. Quite thankfully at that."
    s "But-"
    i "Nope! Besides, the thing I know is probably just another misunderstanding anyway. Or at least that’s what I’m going to tell myself so I can slink back into blissful ignorance, as forced as that bliss may be."
    i "But hey, bliss is a thing I’m already used to forcing. Mostly in the form of stuff that comes in translucent orange bottles. But you already know that since it’s the same stuff I almost killed Miku with."
    s "I was well aware of it long before she was even involved."
    i "Which she’s not anymore, by the way. She doesn’t need me now that she has a thing. Just like you don’t need me now that you have a thing."
    s "The only {i}thing{/i} I have is an expired lease on life and the desire to lock myself in a padded room for the rest of eternity."

    scene iobluedeath9
    with dissolve

    i "Sounds like a better plan than wasting your breath on someone so worthless that her peers won’t even bring her up again after shining the spotlight on her for everyone to see."
    s "You should tell me what happened, Io."

    scene iobluedeath10
    with dissolve

    i "I’d rather fall asleep on an active tablesaw!"
    s "Io-"

    scene iobluedeath8
    with dissolve

    i "Just forget it, Sensei! Let’s seize this opportunity to go back to square one! Or...whatever square it was that we left off on before you went catatonic and I broke into your house."
    s "Yeah, about that. You might have noticed back when I met up with you and Miku at the park, but I’m not sure if I can just “go back.”"
    s "And by “not sure,” I quite literally mean that I can not. So there’s a high likelihood that {i}both{/i} of us are going to do nothing but shit all over ourselves in one another’s presence from now on."

    scene iobluedeath11
    with dissolve

    i "I think this might be the first time I’ve ever been excited to listen to someone whine before."
    s "For now, maybe. But there’s a good chance you’ll be the one who winds up getting sick of {i}me{/i} at this rate."
    i "Wanna make a bet, then?"
    s "Why not? If nothing else, it’ll give us one more paper-thin excuse to stay together."
    i "Then, I’ll bet you my life that you give up on me before I give up on you."
    s "And I’ll bet you mine that you’re wrong."

    scene iobluedeath12
    with dissolve

    i "So we both die either way."
    s "Poetic, isn’t it?"
    i "A little cringey too, but that’s par for the course when it comes to people like us."

    scene black
    with dissolve2

    i "But hey, this is a reunion! Which means that we should celebrate with greasy food and continued tales of why we hate the world that we were born in!"
    s "Or fell in love with."
    i "Hm? Love? This place? I don’t get it."
    s "And I hope you never do."

    "........."
    "......"
    "..."

    scene iobluedeath13
    with dissolve2

    "Io and I head over to a fast food restaurant to medicate ourselves with food that would be called poison by most other standards. But, in a sense, poison is just as good as medicine for those who deserve death."
    "I’m talking about myself in regard to that last part, of course. Shocking, I know. But I don’t think that Io deserves death. Just maybe something along the same lines that Nodoka got after fucking with Yumi."
    "She isn’t feeling well, but I’m not sure if she’s always been this way or if it’s just more apparent to me now that I see this same faux-contentment every time I look in the mirror."
    "I wonder if it might have something to do with the fact that “something may have happened.” But I concede that whatever that wasn’t doesn’t have anything to do with me since I’m not her teacher anymore."
    "I have my life and she has hers. The rest of the girls have {i}theirs{/i} too. And the best way for me to stay involved with them, since I can not tear myself away entirely, is to shed what matters least."
    "It’s okay to have things of your own. It’s okay to hide your problems from the people you don’t want to burden."
    "It’s okay to fake a smile while you’re doing that because maybe, just maybe, that smile will help someone."
    "So as the two of us, surrounded by smiles in a business that uses them as a marketing tactic, fake our happiness for the sake of one another, I take a bite out of a cheeseburger. But all I taste is flesh."
    "Flesh and the idea that I, too, have found myself in the mouth of a greater being. "
    "But instead of trying to preserve myself, I just wonder how I must taste."
    "It must be good if so many chunks of me have been ripped out."

    i "So...hear any funny jokes lately?"
    s "No. But I {i}did{/i} go camping recently."

    scene iobluedeath14
    with dissolve

    i "Camping?! I want to go camping! Why didn’t you go with me?!"
    s "Because I went with a bunch of older women and Ami instead."

    scene iobluedeath15
    with dissolve

    i "Ew. I didn’t like anything about that sentence."
    s "Yeah, that’s why I didn’t invite you."

    "I conveniently leave out the fact that she didn’t even cross my mind."

    scene iobluedeath16
    with dissolve

    i "You should go again, but with Uta and me next time. I’ve never gone before, but I’ve always wanted to try."
    s "Well, I’m glad at least {i}you’re{/i} enthusiastic about it since Uta and I would very likely be useless."
    i "Uta wouldn’t be useless. She went camping all the time when she was little. She has a crossbow and everything."
    s "A crossbow? Exactly how long do you think we’d be camping for to warrant bringing that along?"
    i "Hopefully for the rest of our lives. If the three of us start living off the grid, we can bypass taxes and grow our own food and stuff. It would be true freedom, Sensei."
    s "You’re in high school. You don’t pay taxes."

    scene iobluedeath17
    with dissolve

    i "I pay taxes when I buy things from the store, which is more than enough to make me know how much they suck and that we’d be better off without them."
    s "Fair enough. But even then, I can’t say I like the idea of living in the woods for the rest of my life."

    scene iobluedeath18
    with dissolve

    i "Yeah. It sounds nice in theory, but I wouldn’t be able to charge my power tools or watch baseball anymore, and those two things are basically half of the reasons I have to stay alive."
    s "Hey, that’s four more than I have."

    scene iobluedeath19
    with dissolve

    i "Think you’re broken enough to settle for someone like me yet, then? Maybe I could be your first reason if all this sudden trauma has lowered your standards by enough?"
    i "Which isn’t to say they were high at all since you had no problem consenting to a relationship with that blonde who isn’t blonde anymore. Slight improvement, sure. But still gross."
    s "I’ll take blonde over green any day."

    scene iobluedeath20
    with dissolve

    i "Smart move. I hear that girls with green hair can be kind of psycho sometimes."
    s "Yeah, they never shut up either."
    i "They’re probably just so excited whenever someone acknowledges their worthless existence that they-"

    malec "Over here. There’s a table open this way."

    scene iobluedeath21
    with dissolve

    i "Huh?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene iobluedeath22
    with dissolve2

    femalec "Can you believe that the ice cream machine is broken {i}again?{/i} Has it {i}ever{/i} worked?"
    littlegirl "Mommy, can we go next door for dessert after dinner? Please?"

    scene iobluedeath23
    with dissolve

    femalec "I don’t know, dear. I’m not sure if all of those calories are good for your health. It’s bad enough that we’re stopping at-"
    littlegirl "Daaaaaaad? Pleeeeeeeease?"
    malec "Listen to your mother, sweetheart. "
    littlegirl "But Mommy was going to get ice cream for herself! That’s not fair!"
    malec "That’s because Mommy is pregnant and if she doesn’t get what she wants, she’s going to kill all of us."
    femalec "Mommy will give you a bite of her ice cream when we get home, baby. Now, follow your father so we stop disturbing the other customers."

    scene iobluedeath24
    with dissolve

    littlegirl "{i}Would you really kill me, Mommy?{/i}"
    femalec "{i}Robert, can you please tell your daughter I’m not actually a murderer?{/i}"
    malec "{i}Not until I know for sure.{/i}"
    i "..."
    s "..."
    s "Are you alright, Io?"

    scene iobluedeath25
    with fade

    i "Yeah, I’m fine."
    s "Well, now I {i}know{/i} you’re not fine. The Io Ichimonji I know would never miss out on an opportunity to self-deprecate, and I basically just handed you one on a silver platter."
    i "I just get annoyed when other people interrupt my conversations, that’s all."
    s "They weren’t really-"
    i "I lost my train of thought. Now I can’t remember what I was talking about and I have to start all over. It’s annoying."
    s "..."
    i "And now they’re being loud...how am I supposed to focus?"
    s "Io, they’re just eating. They’re not-"

    scene iobluedeath26
    with dissolve

    i "Can we leave?"
    s "..."
    i "I’m not feeling well all of a sudden."

    "Io had been tapping her knuckles on the table since we first showed up here. "
    "She’s stopped now."
    "It’s like she’s focusing all she has on just maintaining composure and, as unfortunate as it is to say, I get it."
    "I don’t have to know {i}why.{/i} And sure, I can guess to sate my own curiosity...But guessing will do nothing other than risk hurting her, and I’m not sure how much more pain that fragile frame of hers can take."

    s "Do you want me to ask if we can take this to go instead? Or-"
    i "I’m not really hungry anymore. I just want to leave. Can we leave? Please?"
    s "..."
    i "Please?"

    scene black
    with dissolve2

    s "Yeah."
    s "We can leave."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ io_love += 1
    $ iospring1 = True

    jump iospring2

label iospring2:
    scene clearnightsky
    with dissolve2

    "There is no second half of “My Indigo.”"
    "It’s one of those poems that comes and goes — like sunlight in the afternoon when it finds the gaps between leaves and squeezes through them, spilling itself out onto the asphalt."
    "I often wonder how {i}I{/i} would look splayed out upon the asphalt, but the manner in which I envision that is a lot less aesthetically pleasing."
    "We’re heading back to the bathhouse, I think. Or some other place that Io wants to go, but she hasn’t said much ever since leaving the restaurant and I don’t think it’s safe to ask her."
    "It goes without saying, but she reminds me of myself sometimes. Especially when her voice fades out."
    "So as the moon attempts to mimic the sun and cast its light through the trees, this is what I’m thinking of."
    "But the differences between Io and me are just as noticeable as that of the sun and the moon."
    "One of us is stronger, one of us is weaker. But neither one of us can agree on which is which. Which is fine, because it creates just enough space between the two of us that she’ll feel safe."
    "And so I keep my distance-"
    "But I long to go for a swim."
    "I’m sure when I was younger, there were times I wanted something I couldn’t have. And given that I still possess the mental maturity of a child at times, I should be okay with this. I should be able to adapt."
    "I should be okay with keeping my swim trunks locked in the drawer until the setting is right and the sun has no tree to meld with."
    "But I {i}really{/i} want to go for a swim."

    s "..."
    i "..."

    "And I want to take her with me."

    i "Sorry for being stupid again. I left my safety net at home."
    s "The one with Uta or the one with naked people? Because I’m not really sure where we’re headed right now."
    i "The latter. I haven’t really been staying at the dorm as much as I used to lately."
    s "Any reason why?"
    i "I just don’t like girls very much."
    s "Wow, really? I had no idea. "
    i "How do you do it, Sensei? Or...how {i}did{/i} you do it before you too learned to appreciate just how great it is to live a life of mostly solitude?"
    s "I’m sure my sexual attraction to them played some sort of role in keeping me sane."
    i "Does it really make that much of a difference?"
    s "I’m not sure. I’ve never really thought about it."
    s "I’ve just never spent much time around other guys, I don’t think."
    i "Even when you were younger?"
    s "All I remember from when I was younger is my childhood friend who, and you might want to brace yourself for this, was also a girl."
    i "Why would I have to brace myself for such a predictable thing?"
    s "You just get so jealous any time another girl comes up that I figured hearing about such a fated connection might hurt your feelings."
    i "Is she important to you?"
    s "In a lot of ways, she’s the {i}most{/i} important person to me."
    i "And in others?"
    s "..."

    scene black
    with dissolve2

    s "In other ways, part of me wishes she didn’t exist."

    "........."
    "......"
    "..."

    scene komorebi1
    with dissolve2

    "We make our way into Io’s room because of course we do. We were {i}always{/i} going to come here whether I knew it deep down or not because {i}this{/i} is where she’s safest."
    "Not next to me. Not next to Uta. But in a room surrounded by wooden robots and tools and pills and wires and even more pills and everything else that serves as her {i}safety net.{/i}"
    "The air is different this time around — and it’s not just because I’m not waking up in some gaudy bathrobe and faux-fur pajama pants."
    "Maybe it’s the light — and that stale scent of turpentine— or the fact that I am dangerously conscious for the time being."
    "Whatever it is, it makes me want to fall asleep and never get up."
    "I want to collapse in her bed, fall asleep in her arms, then awake and brush her hair out of her face before going home and getting scolded by my {i}daughter.{/i}"
    "But this is someone else’s daughter. And yes, that’s true of every girl I crawl into bed with, but you know what I mean."
    "The idea of something so pure and innocent is antithetical to the evils at play here. So again, I keep my distance."
    "Again I recite “My Indigo.” But I keep stopping at the line “blackness gathers in the grass” and worry that the grass is {i}here{/i} and that {i}I{/i} am the blackness."
    "I’m sure that’s not what Lee had in mind when he wrote this poem. My existence matters not to him, nor anyone else with a brain even half as functional."
    "But Io’s brain is held together by glue and benzodiazepines, and it isn’t strong enough to protect its container from the blue death."
    "I really want to go swimming."

    i "You haven’t been here since you accidentally flashed Uta, have you?"
    s "Not unless the two of you dragged me here after breaking into my house. But that whole night is blurry to me and I don’t think either one of you is strong enough."

    scene komorebi2
    with dissolve

    i "We kind of just showed up, freaked out, then got forced out of the house by your psychopath of a niece."
    s "I’m sure she was just trying to protect me."

    scene komorebi3
    with dissolve

    i "So does that give {i}other{/i} people permission to capture you and hold you in captivity so long as they’re doing it out of what you’d call “the goodness of their heart?” Asking for a friend."
    s "My answer to that question hinges entirely on whether or not you have a pair of handcuffs in this room."
    i "And now I’m even more confused because I can’t tell if you {i}want{/i} me to have handcuffs or not and I don’t want to say the wrong thing."

    scene komorebi4
    with dissolve

    s "Do you want to keep me here forever?"
    i "I don’t know. It sounds nice and all, but it also might make it really hard to go to the amusement park when you finally decide to take me there."
    s "Let’s go soon."

    scene komorebi5
    with dissolve

    i "Really?!"
    s "Yeah. It’s not like I have anything else going on anymore. And I’ve already been there with Tsuneyo twice since first talking to you about it."
    i "I’m just going to ignore that last part so I can continue to be excited! Heck yeah! Amusement park!"
    s "Don’t get {i}too{/i} excited. The fact that it’s an amusement park won’t change the fact that I will continue to be completely unamusing while inside it."
    i "Doesn’t matter! I suck too, which just means that we can suck together while participating in slightly less sucky activities!"

    scene komorebi6
    with dissolve

    s "Works for me, Io."
    i "Sensei? Where are you going?"
    s "Bed. I’m tired."

    play sound "static.mp3"
    scene komorebi7 with flash
    stop sound

    i "But we just got here."
    s "We did. Which means you’re welcome to join me if you’d like."
    i "You’re giving me permission to enter my own bed?"
    s "That’s right. I’ve seized control of it. This is my bed now."

    scene komorebi8
    with dissolve

    i "You’re allowed to do that?!"
    s "We can do anything we want. That’s what it means to be free."
    i "Then I hereby seize control of your heart and command that you leave behind however many fake girlfriends you have in favor of either me or Uta! Or both."
    s "Can I bring Ami along?"

    scene komorebi9
    with dissolve

    i "Ew, no. I’ll never get to see you if she’s there. She’s too clingy."
    s "And you’re not?"
    i "Not like {i}that.{/i} She’s genuinely creepy. I’m just annoying. "
    s "She’s family, Io. I can’t just abandon her even if you {i}do{/i} seize control of my heart."

    scene komorebi10
    with dissolve

    i "Then what good does seizing it even do in the first place? Besides, isn’t it sort of arbitrary to keep her close-by just because she’s “family?” That word means literally nothing."
    s "This is your aunt’s house, isn’t it? If family meant nothing, you’d be back at the dorms right now."
    i "I’m not here for my aunt. I’m here because this is where all of my stuff is."
    s "But your stuff wouldn’t {i}be{/i} here without your aunt is what I’m saying. Which, by extension, means we never would have met without her."
    s "And, speaking of which, when {i}am{/i} I going to meet her? Because I’ve been coming here for a while now and she’s never even-"

    scene komorebi11
    with dissolve

    i "She travels a lot. "
    s "Where? She can’t leave the city."
    i "Around? I don’t know. It’s a big city. And you’d have nothing to gain from meeting her anyway."
    s "It’s not really about gaining anything, it’s about putting a face to a name."
    i "You don’t even know her name, though."
    s "Do you not {i}want{/i} me meeting her or something?"

    scene komorebi12
    with dissolve

    i "Was that not immediately obvious?"
    s "It...was. I just don’t really get why."
    i "Because I want to keep my life with you separate from my life outside of you."
    s "That’s not really how having a life with someone works, Io. You can’t just hide things from me forever."
    i "Sure I can. But that’s fine because it means you can also hide things from me, so we don’t accidentally start mixing traumas and make our relationship all messy and sad like everything else in our lives."
    s "But what if I want to share something with you?"
    i "Then you can. I just don’t want it to be mandatory."
    s "I’m not proposing we make it “mandatory.” I’m proposing that-"
    i "If you meet her, you’ll meet her. If you don’t, you won’t. It’s as simple as that. "
    i "It’s not like you’re missing out anything. She’s just some random woman with really bad fashion sense."

    play sound "static.mp3"
    scene komorebi13 with flash
    stop sound

    s "She’s more than just “some woman.” She’s the person effectively raising you. And if she isn’t doing anything wrong, it’s messed up to just {i}reduce{/i} her to that."
    i "How is it messed up? It’s not like I’m calling her an evil bitch. I’m just saying she is a human being who exists and that you don’t have a good reason to meet her. Which is true. "
    s "You’re right. That {i}is{/i} true. I don’t have to meet her. I’ve gotten along just fine without her and I am perfectly content never coming into contact with a woman whose clothes I wore."
    s "But, as someone currently reevaluating just what it means to be part of a “family,” I have a problem with you talking about her like that."
    i "Like what? Again, I said literally nothing bad about her. She’s just there. "

    play sound "static.mp3"
    scene komorebi14 with flash
    stop sound

    s "Do you have any idea how hard “just being there” is?"
    i "Uhh...{i}not{/i} hard? Because it is literally as simple as “just being there.” Which is like, the bare minimum amount of activity required to participate in something."
    i "Just look at how I’ve acted at essentially every single class gathering that we’ve ever-"
    s "Just being there as a person is way different than just being there as a parent."
    i "Cool. Except she {i}isn’t{/i} a parent. She’s my {i}aunt.{/i} "
    s "Is she there for you when you need her? Does she give you a place to live and food to eat? Who’s the one refilling all of your prescriptions? Who is giving you money?"
    i "She is, but-"
    s "Then she’s a parent. She’s your mother."

    play sound "static.mp3"
    scene komorebi15 with flash
    stop sound

    i "Excuse me?"
    s "Maybe I was wrong when I asked you if you knew how hard it was to “just be there.” What I should have asked is if you know how easy it is to fuck that up."
    s "You have a problem with Ami, right? Well, the reason she’s like that is because of me. It’s because {i}I{/i} wasn’t there that she’s all fucked up now. So if you’re going to blame anyone, blame me for that. Not her."
    i "What’s going on with you? Why are you getting so beaten up over this? Are you just {i}trying{/i} to start a fight with me or something? "
    s "What’s going on is that I think you’re taking your aunt for granted and that isn’t fair to her. She doesn’t {i}have{/i} to look after you, but she does. And she gives you everything you need, doesn’t she?"
    i "I could look after myself if I had to. That’s basically what I do anyway."
    s "Well, that’s good for you. But not everyone can do that. And if Ami had someone like her instead of someone like me, maybe fewer people would hate her for what she’s become."
    i "Oh, so it’s a {i}personal{/i} thing. You’re coming after me because you regret things {i}you{/i} have done. Got it. That’s fine. I’ll be a scapegoat if it makes you feel better, Sensei."
    s "I’m not trying to come after you, Io. I just-"

    scene komorebi16
    with dissolve

    i "You just want to tell me how I’m supposed to look at family because you’re pretending to be more than just Ami’s uncle now, right? And you want to feel better about the job you’re doing!"
    s "..."
    i "Right?!"
    s "You’re not entirely off-base, but you’re not entirely correct either."
    i "Well I think it’s {i}cute{/i} that you want to play dress-up, Sensei! But maybe you should pretend to be something {i}other{/i} than a parent because parents fucking suck and you don’t want to be one!"
    s "You’re right. I don’t {i}want{/i} to be one. I {i}have{/i} to be one or Ami is going to-"
    i "There’s no fixing that girl, Sensei. Just like there’s no fixing me! And I already {i}have{/i} an extended relative who inherited a role that, based on my experience, gets way more credit than it should for literally nothing!"

    play sound "static.mp3"
    scene komorebi14 with flash
    stop sound

    i "I’ll never get this fascination people have with {i}family.{/i} Like, oh! Congrats on having similar DNA structure to someone else! You guys must really love each other!"
    s "That’s not-"
    i "Shut up! I’m not finished! I need to tell you how fucking {i}stupid{/i} this topic is so we can go back to liking each other!"
    s "Io-"
    i "I said shut up!"

    play sound "static.mp3"
    scene komorebi17 with flash
    stop sound

    i "I don’t give a single FUCK about what you want to be or what you think you {i}are,{/i} just keep me out of it!"
    i "I don’t {b}NEED{/b} family and I don’t {b}NEED{/b} to be reminded of how {b}EASY IT IS{/b} to fuck up just {b}EXISTING,{/b} okay?!"
    i "Parents have {b}ONE FUCKING JOB{/b} and it’s to {b}BE THERE.{/b} It isn’t hard! It’s really not! And I don’t {b}CARE{/b} that I’ve never experienced what it’s like on their end because I don’t {b}HAVE{/b} to!"
    i "And here {b}YOU{/i} are, playing a game of charades where you get to act out the role of a {b}FATHER{/b} for the first time in your life, and you want {b}ME{/b} to be thankful for {b}SOMEONE ELSE{/b} playing too?!"
    i "Are you an {b}IDIOT?{/b} Are you {b}STUPID?!{/b} Or do you just {b}HATE{/i} kids and get joy out of inflicting pain on them?! Is {b}THAT{/b} why you’re doing this?! Is that your end goal here?! Are you one of {b}THEM{/b} now?!"
    s "Of course not..."
    i "Then {b}WHY?!{/b} Why would you press me about this?! Why would you call my {b}AUNT{/b} such a {b}TERRIBLE{/b} thing to my face?! "
    i "You {b}DID{/i} hear, didn’t you?! {b}YOU HEARD WHAT THEY SAID ABOUT ME!{/b} That I’m {b}ROTTEN! SPENT! TRASH!{/b} "

    scene komorebi18
    with dissolve2

    i "And you know it’s true..."
    i "But you have no idea what it’s like."
    i "You’ve never felt like a prisoner...even when you {i}were{/i} one."
    i "You’ve never seen your home as a jail cell. Never had your cries for help ignored by everyone around you."
    i "Never had to make up stories and excuses about why you’d have panic attacks in the middle of school! And why they weren’t anything for someone to be concerned about! But they were!"
    i "Someone should have done something! {b}SOMEONE SHOULD HAVE HELPED ME!{/b} But they didn’t! No one did! Not until the damage had already been done!"
    i "Are {b}THOSE{/b} the people you want me to feel sorry for?! The ones who let a little girl {b}ROT{/b} and {b}BREAK{/b} because {b}THEY{/b} had kids of their own?! Or the ones who {b}BROKE ME{/b} in the first place?!"
    i "I {i}have{/i} no parents. Not anymore. "
    i "I have an aunt and that’s it."
    i "And if you want me to start seeing her as anything else, you should grab me a bucket because I can’t even say the word “Mom” without wanting to throw up."

    scene komorebi19
    with dissolve2

    s "..."
    i "..."
    i "Do you want to know how old I was?"
    s "No..."
    i "Are you just lying to me now? "
    s "No..."
    i "Then what were you doing with that picture of Uta?"

    scene komorebi20
    with dissolve2

    s "What...picture of Uta?..."
    i "You know exactly what I’m talking about..."
    i "It wasn’t just a misunderstanding...that was all typical wishful thinking from typical Io..."
    i "I mean...what’s there to even misunderstand? You’re just another sick adult who can’t control himself around little girls. And I’m so fucked up by now that it barely even bothers me anymore when it comes to {i}me.{/i}"
    i "But Uta..."
    i "Those pictures ruined her life."
    i "And you’re keeping one as a...fucking trophy."
    s "How...did you even..."
    i "It doesn’t matter...Nothing matters...I’m done..."
    s "Done with {i}what,{/i} Io?..."
    i "Everything."
    i "Do whatever you want to me. I won’t fight back."
    s "..."

    play sound "static.mp3"
    scene komorebi21 with flash
    stop sound

    se "Did you hear that, Aki-kun? She says she won’t fight back. Sounds like consent to me."
    s "My Indigo..."

    scene komorebi22
    with dissolve

    se "Hm?"
    s "I've come to find the flower which blossoms...like a saint dying upside down..."

    scene komorebi23
    with dissolve

    se "The rose won't do, nor the iris. I've come to find the moody one, the shy one, downcast, grave, and isolated..."

    scene komorebi24
    with dissolve

    se "Right?"
    s "..."
    se "It could be good for her, you know. "
    se "It could be good for you too."
    se "Maybe she’ll become the next whatshername?"
    s "..."
    se "You’re like me when it comes to this stuff, Aki-kun. And we both know you’ve always looked up to me."
    se "I won’t tell you what to do — just that you should follow {i}your{/i} heart instead of someone else’s. "
    se "And if you think that making love to this girl will do her more good than it will harm, I say do it. "
    se "You’ve always been a special boy. You can fix anything you want so long as you put your mind to it."
    se "This little one is no exception."
    se "But {i}you{/i} have to make the decision, Aki-kun."
    se "It has to be {i}you{/i} this time."

    $ renpy.end_replay()
    $ iospring2 = True
    $ io_love -= 1

    jump iospring3

label iospring3:
    stop music
    play sound "static.mp3"
    scene londonbridge1 with flash
    stop sound

    i "Do you have any idea what it’s like to have an orgasm against your will?"
    i "How shameful...embarrassing...and nauseating that is?..."
    i "Because I do."
    s "..."
    i "Do you know what it’s like to come home from school every day not knowing whether or not someone is going to put something inside you?"
    s "Io-"

    play music "stopwind.mp3"

    i "Because I do."
    i "Do you know what it’s like to go to bed with a stomachache? Or the taste of a woman who hasn’t showered in over a week? Because I do, Sensei."
    i "I know way more than a girl my age should ever know. And it’s all because of that title you’re oh-so proud to claim now."
    s "..."
    i "Do you want to know how old I was?"
    s "I don’t, Io..."

    scene londonbridge2
    with dissolve2

    i "You’re a liar."
    s "I’m not lying. And if I’d known that this was-"
    i "You knew. You’re lying again right now."
    i "Even if you didn’t hear it from them, you could have put two and two together. You’re smart."
    i "But you just kept on pushing...because you wanted to hear it from me directly. Didn’t you?"
    s "I never wanted this."
    i "Is it hard, Sensei?"
    i "Do you want to put something inside me?"
    s "I {i}do{/i} know what it’s like, Io."
    i "..."
    s "You’re not the only one in this room who bloomed before they were meant to."
    i "Don’t use flowery words to describe what happened to me. "
    i "I was raped nearly every single day for years. That isn’t {i}blooming.{/i} It’s being trampled — and I’m as good as dead now."
    i "So if you want to dance around that, have at it. But I’m not a very good dancer, and I’d much prefer to abstain from such activities."
    s "What do you want me to do?"
    i "Can you go back in time and make it so this talk never happened?"
    s "I...don’t think so. But we can pretend-"
    i "The point of pretending has come and gone. You know who I am now."
    i "And I don’t know what happened to you, but if it really {i}is{/i} anything like what happened to me, the person you became makes a lot more sense now."
    s "..."
    i "I’ve heard it goes one way or the other, you know. But both ways involve sexual identity being torn to shreds and left out in the water to warp into shapes that won’t ever “fit” again. "
    i "But who knows? I’ll never stop being surprised by what can fit inside someone if you try hard enough."
    i "Maybe in another life, I could have been everything you wanted. I could have been a version of me that welcomes or wants your lust. But that’s not who I am."
    i "I’m a secondhand sex doll who’s sewn herself shut. "
    i "But I’ll let you tear open the stitches right now since we both know that’s what you want."
    s "What I want is for you to feel loved."
    i "Then you’ve picked a horrible way to show me that."
    s "I didn’t come here to hurt you...you just didn’t really interpret things the way I anticipated and...everything kind of spiraled out of control after that. But that’s fine. I’ll leave."
    i "You don’t want to do it with me?"
    s "Io, come on."
    i "I won’t blame you for not wanting to bathe in dirty water, Sensei. But it’s all I have to offer right now."
    i "Will you take it or not?"
    s "Why are you even giving me the option?..."
    s "What’s the point of keeping me around at all if I can turn you into this? And that’s not even mentioning what you know about my phone now. You gain nothing from keeping me here."
    i "This isn’t about gaining anything. It’s about survival."
    s "You don’t need me to survive. You said just earlier you’d be fine on your own."
    i "I say a lot of things and only half of them are true. That’s what it means to be a liar."

    "As probability slips through my hands, I clasp them back together and pray that everything she’s said tonight has been a lie."
    "But I know those eyes, so I know the truth."
    "She {i}is{/i} like me — in the worst way imaginable."
    "But what can I do about that? How can I help her?"
    "Do I even {i}care{/i} about helping her? Or do I want to go back to treating this all like some sort of game. I-"
    "No...of {i}course{/i} I want to help her. But the issue is {i}how{/i} I can help her since I only know of one way. "
    "Two counting this newfound reluctant affinity for parenthood, but she’s made it overwhelmingly clear that {i}that{/i} is the one thing that would help her the least of all."

    s "..."
    i "..."
    s "Can I ask you something?"
    i "Five."
    s "Five what? "
    i "Sorry, what’s the question?"
    s "I just want to know if you really {i}do{/i} want me to stay in your life or if that’s something you’re just saying to try and protect yourself in...some way I don’t understand."
    i "I wouldn’t open my legs for you if I didn’t want you to stay."
    s "Okay, then...{i}why{/i} do you want me to stay?"
    i "Another question? "
    s "And hopefully one you have an answer for."
    i "At first, I thought you might be able to save me."
    i "Now, I just don’t know what else to do with myself."
    s "..."
    i "Tragic, isn’t it? That all of my vitriol and angst isn’t just unwarranted and childish."
    s "..."
    i "..."
    se "How long are you going to stall for, Aki-kun? I’m bored."
    s "As long as I have to, Sekai."
    i "Sekai?"
    s "That was her name."
    i "The woman who trampled you?"
    se "Ah! Rude!"
    s "...Yeah."
    i "You talk to her in your head?"
    s "I see her everywhere I go."
    i "And you’re not afraid?"
    s "I am, but..."
    se "You are, but?..."
    s "I love her."
    se "Awwwww! I love you too! Now, hurry up and keep the cycle going before I disappear again."

    scene londonbridge3
    with dissolve

    i "Love?"
    s "Love..."
    i "Even though she raped you?"
    se "Ahem...{i}Statutorily.{/i}"
    s "Yeah..."
    i "Why?"
    s "I don’t know..."
    s "I have no idea."
    s "I just...do."
    i "Stockholm Syndrome?"
    s "Maybe. "
    se "Meanie! We were so cute together."
    i "Lucky. "
    i "If I ever saw the woman who did those things to me again, I’d slit her throat with my box-cutter."
    s "She’s still out there?"
    i "Last I heard, she was on the other side of the wall. But that doesn’t mean I don’t still live in fear that she’ll show up again one day."
    s "What about your father?"
    i "Probably right behind her, silent as ever. But if there really is a god out there, maybe he’s killed them both by now. I don’t know. A girl can dream."
    s "Io...I don’t want this to change anything between us. I’m not going to look at you any differently now than I did yesterday."
    i "You might be telling yourself that, but you’re wrong. This is going to haunt you. You’re going to think about it constantly whether you want to or not...but at least it will be me instead of Uta."
    s "Uta has nothing to do with this. You and I are-"
    i "Are we going to do it or what? I’m tired."
    s "..."

    scene londonbridge2
    with dissolve2

    i "..."
    se "Like I said, Aki-kun...it might help her. "
    se "Like, maybe she’ll realize that all sex doesn’t {i}have{/i} to be gross and that there are certain adults it {i}is{/i} okay to- hmm. Wait, let me reword that in a less predatory way."
    se "Maybe she just doesn’t like sex because she’s only done it with her mom? Or...hold on, was her dad touching her too?"
    se "She wasn’t specific enough. Could you ask her a quick question for me? It’s relevant, I promise."
    s "I don’t know..."
    se "Come on! Stop being so indecisive. I can see your hard-on through your pants."
    se "You know you want to. She’s consented and everything. Probably. I think. Sorry, what are the laws again? I’m dead. They might have changed by now."

    "{b}akira.{/b}"
    "You too?"
    "{b}destroy her.{/b}"
    "That’s a lot less convincing."
    "{b}destroy. then rebuild.{/b}"
    "{b}she will be stronger for it.{/b}"
    "{b}you both will.{/b}"

    i "It’s rude to keep a girl waiting."
    i "I’m on the edge of my seat."
    s "..."

    menu:
        "Go home":
            s "..."
            i "..."
            s "I can’t..."

            scene londonbridge4
            with dissolve2

            i "You can’t?"
            s "I can’t."
            i "Because you’re disgusted?"
            s "Because you don’t want it. And if you don’t want it, I won’t do it."
            i "But I said I’d let you."
            s "It’s not about you {i}letting me,{/i} Io. Sex isn’t some kind of favor. It’s a way for two people to strengthen a bond or...expel their mutual lust."
            i "I’m confused..."
            s "And it’s sad that you’re confused...but I understand why you are."
            s "And I’m so sorry that you had to go through what you did."

            scene black
            with dissolve2
            play sound "dooropen.mp3"
            stop music fadeout 10.0

            s "I’ll let you get some sleep now."
            s "I’m sorry for ruining your night."
            s "I won’t look at you any differently."
            s "I promise."

            "........."
            "......"
            "..."

            scene londonbridge5
            with dissolve2

            i "..."
            i "What?..."

            scene londonbridge6
            with dissolve2

            i "Is he..."
            i "Did he really just...leave?..."
            i "..."

            scene londonbridge7
            with dissolve2

            i "That can...happen?..."
            i "..."

            scene londonbridge8
            with dissolve2

            i "What?..."
            i "..."

            scene londonbridge9
            with dissolve2

            i "What?..."

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ iospring3miss = True
            $ iosex = False
            $ io_love += 10
            $ ioblock = True

            "........."
            "......"
            "..."

            play sound "dooropen.mp3"
            scene bedroom_night
            with dissolve2

            "I crawl into bed alone."
            "Tonight, I will dream of nothing."

            scene black
            with dissolve2

            "It would probably be best to leave Io alone for a little while."
            "I’ll wait for her to come to me."
            "I’ve inflicted enough damage upon that girl as it is."
            "She can be an exception."
            "She can be my indigo."
            "{i}Io’s affection has increased by 10!{/i}"
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

        "Destroy her":
            jump iodestroyed

label iodestroyed:
    if _in_replay:
        scene londonbridge2
        with dissolve
        play music "stopwind.mp3"

    s "I don’t want to hurt you, Io."
    i "You won’t hurt me. I’ll just tune it out."
    s "I don’t want you to tune it out either. I want you to enjoy it."
    i "Then I’ve got some very bad news for you."
    s "Io...the reason I don’t abhor the person who did this to me is...complicated. And maybe you won’t ever look at me the way I look or...{i}looked{/i} at her...but I want to try."
    s "I want to be someone to you. I want to be someone {i}for{/i} you. And I wish I could do that in the way you want me to, but...I don’t know {i}how.{/i}"
    s "There’s only one way I know how to show love...and I want you to be the recipient of that for once."
    i "Right."
    i "So, do I take my pants off myself or are you going to do it for me?"
    s "Are you going to ignore the fact that I basically just told you I love you?"
    i "Mhm. It’s easy when you use the same words {i}she{/i} used to."
    s "..."
    i "Come on. Let’s do it."

    scene black
    with dissolve2

    "I take a step forward, expecting her to flinch, but she doesn’t move a muscle."
    "Slowly, I push her closer to the wall, gently so as to not make her trip over some of the toys and tools scattered across the floor."

    play sound "static.mp3"
    scene londonbridge10 with flash
    stop sound

    "We make it there sooner than I expect to. Time is moving faster than normal. Either that or my heart is. But whatever is actually happening, I can’t tell if I like it or not."
    "Thankfully, my limbs move on instinct. They come into contact with her and I quickly learn just how pliable she is."
    "I can move her around without any resistance at all...touch her in any way I please without changing her expression...and I realize just how true her earlier comparison to a doll really was."
    "But I’m not perturbed by the fact that I’m not the first, for I’ll be the first to show her the pleasures of flesh in a way doused in affection rather than hatred."
    "For now, I will relinquish my role as a parent. For now, I’ll be a lover."
    "I’ll be the bridge that Io crosses from hell to heaven — and borrow a piece of her that I will wear as a medal. Not to brag of glory, but to commemorate our bond."
    "I am doing the right thing."
    "I am teaching her how to love."

    s "You’re sure this is okay?"
    i "I already told you, I won’t fight back."
    s "How far is too far?"
    i "Just do whatever you want and wake me up when it’s over."

    scene londonbridge11
    with dissolve2

    s "Are you sure you don’t want to be awake for it?"
    i "..."

    scene londonbridge12
    with dissolve2

    s "No one said you {i}can’t{/i} enjoy this, Io...That’s a limit you’re placing on yourself."
    i ".................."
    s "I’ll show you what it’s like have a {i}real{/i} orgasm...not an accidental one against your will..."
    i ".................."

    "I do my best to keep the dialogue flowing since I know my partner won’t be contributing this time, but it doesn’t seem to be working."
    "She takes two of my fingers deep into her mouth without so much as gagging, and I toy with the idea of testing her limits by tickling her tonsils."
    "But I decide against it since such actions are better reserved for Nodoka."

    scene londonbridge13
    with dissolve2

    "I remove myself from her mouth and trace my way down her body to the zipper of her cargo pants, undoing it before grazing the space just above her slit to see if I can elicit a reaction."
    "Again, there is nothing. Just the semi-lifeless body of a girl who’s done this song and dance and a man who was never fit for the stage."
    "But alas, I proceed — out of devotion and desire for this relic I plucked from a yard sale."

    s "You don’t touch yourself, do you?"

    scene londonbridge14
    with dissolve2

    s "That’s no good. You need to relieve yourself every once in a while or you’ll go crazy..."

    "My fingers, still wet from her saliva, slide into her panties and down to her pussy."
    "She isn’t wet, which I expected. But that’s what her spit is for. So I coat her nether regions with this alternate form of lubrication before grazing her clit on my way back up her body."

    scene londonbridge15
    with dissolve2

    s "You don’t mind, do you? Since I can {i}do whatever I want{/i} and all..."
    i "................"

    scene londonbridge16
    with dissolve2

    s "I’m surprised...you didn’t seem like the type who shaves to me. But I don’t feel any hair at all down here..."

    play sound "static.mp3"
    scene londonbridge17 with flash
    stop sound

    s "Does that feel good?..."

    "I press one hand to her throat while submerging the other in the depths of her panties once more."
    "The weight of her belt presses hard against my hand but does little to stop the motion of my middle finger as I sink it inside of her."
    "I can feel a bit of moisture now, but I’ve also double-dipped into her mouth and can’t discern just what percentage is imported versus exported."
    "Regardless, I press my weight against her, fingering her gently and softly in hopes of forcing {i}something-{/i} anything out of her."

    play sound "static.mp3"
    scene londonbridge18 with flash
    stop sound

    "But again, there is nothing."

    s "You’re still alive, right?"
    i "Yeah. Are we done?"
    s "Do you want to be done?"
    i "Did you finish?"
    s "Uh..."
    i "You’ve gotta finish, Sensei. You need to relieve yourself every once in a while or you’ll go crazy."
    s "Can you feel that, Io?"

    "I increase my speed, inserting a second finger inside of her."

    scene londonbridge19
    with dissolve2

    i "What do you think you’re doing, exactly?"
    s "Trying to get you excited."
    i "Why?"
    s "Because I...want you to enjoy this as much as I’m enjoying it."
    i "You’re enjoying this?"
    s "I would be if you were...you know...participating."
    i "Weird."
    s "Is it really?"
    i "Listen — can we just skip the foreplay and do it? This is awkward and uncomfortable for me and we both know that’s what you really want."

    scene londonbridge20
    with dissolve2

    i "Besides, I have to pee and I don’t want this to take all night."
    s "..."
    i "It’s fine, Sensei. You know what to do, right?"
    s "Of course I know what to do..."
    i "Then show me."
    i "Show me what your {i}love{/i} feels like."

    scene black
    stop music

    i "And maybe it won’t make me sick."

    $ renpy.pause(10, hard=True)
    play sound "bedcreak.mp3"
    $ renpy.pause(8, hard=True)
    scene londonbridge21
    with dissolve4

    i "{i}Ah...{/i}"
    i "{i}I guess seeing it up close doesn’t prepare you for how big it feels when it goes in...{/i}"
    i "{i}My stomach hurts.{/i}"
    i "{i}But at least he’s being gentle...{/i}"
    i "{i}Maybe he really does care about me? Saying all of that stuff about how he wants me to “enjoy it” and everything.{/i}"
    i "{i}I don’t get it. Just hurry up and cum so I can go to the bathroom.{/i}"
    s "Ngh......ngh!"
    i "{i}Is he enjoying it? Was it worth the wait? Probably not.{/i}"
    i "{i}He’s probably grossed out. That’s why he hasn’t finished yet.{/i}"
    i "{i}I wonder how it even feels for boys? Maybe it’s different? It probably is, right? That’s probably why he doesn’t hate it.{/i}"
    s "Hah....hah....."
    i "{i}Ugh...I really hope this doesn’t become a regular thing.{/i}"

    play sound "static.mp3"
    scene londonbridge22 with flash
    stop sound
    play sound "dosex.mp3"
    play music "mystomachhurts.mp3"

    s "Ngh!...Mngh!..."
    i "..."

    "Each thrust shakes the room as I repeatedly pump myself into Io’s pussy."
    "I hover over her, desperately attempting to ignore the blank stare plastered to her face as I’ve resigned myself to the fact that she hates this."
    "Or maybe “hates” isn’t the right word."
    "True to her promise, she’s not fighting it. But she’s not really {i}doing{/i} anything either. She’s just lying there and letting me have my way with her like she’s some kind of corpse."
    "But if I close my eyes, I can picture her smiling."
    "If I tune out the creaking of the bed, I can hear her calling my name."
    "I just wish that either of those things would bring me closer to cumming."

    s "Io......Io......."
    i "...................."

    play sound "static.mp3"
    scene londonbridge23 with flash
    stop sound

    s "Hah...hah...hah..."
    i "......................"
    s "I’m sorry...I’m close...I am..."
    i "Take your time. I’m not going anywhere."

    "Maybe it’s the scent of turpentine. Maybe it’s the shadow of the tennis ball grip on her ceiling fan’s lamp that appears on her body every nineteen seconds (approximated) from all of the shaking."
    "Maybe {i}those{/i} things are why I haven’t finished yet."
    "Because, whatever it is, it’s most assuredly {b}NOT{/b} the fact that she isn’t enjoying it. Or that I’m forcing her to relive events that effectively ruined her life and {b}NO.{/i} That is {b}NOT IT.{/b}"
    "Those things don’t matter to me. I’m a creature of habit. I’m a rabbit. I have sex because that’s what I do and if I’m not doing it {b}CORRECTLY{/b} then {b}SOMETHING ELSE{/b} is to blame."

    play sound "static.mp3"
    scene londonbridge24 with flash
    stop sound

    s "Mmf!....Hmmm!...Aaah!..."

    "She’s swallowed most of my cock."
    "I figured I didn’t need to hold back since she has {b}EXPERIENCE.{/b}"
    "But that doesn’t bother me. No, that definitely doesn’t bother me. I’m just happy to be making {b}LOVE{/b} to her because it happened so {b}QUICKLY{/b} and that means it must be {b}FATE.{/b}"
    "{i}She{/i} used to talk about fate. Maya. Maya is she. She is Maya."
    "I can pretend Io is Maya. That will work. That will-"

    play sound "static.mp3"
    scene londonbridge25 with flash
    stop sound

    "Fuck. She’s looking at me."
    "Does that mean she’s finally enjoying it?"
    "I can’t close my eyes if she’s looking at me. If I do that, she’ll know I’m not thinking of her. And if she knows I’m not thinking of her, she’ll think it’s because I’m disgusted. But I’m {b}NOT.{/b} I’m {b}NOT{/b} bothered."
    "What is she thinking? What could she possibly be thinking? What does she want me to {b}DO?{/b}"

    i "................"
    s "Io...say something..."
    i "Like what?"
    s "Anything...help me out here..."

    scene londonbridge23
    with dissolve

    i "You’re not a bad guy if that’s what you’re worried about."
    i "Think of us like animals or something. If we lived in the wilderness as like, dogs or wolves...you could just take me whenever and wherever you wanted and it would be totally normal."
    i "This is instinct for you. I just happened to be the only girl around. It is what it is. At least you’re not calling me names."
    s "Hah.....hah!"
    i "If you’re not done in five minutes, can we take a break? I really can’t hold it in for much longer."

    play sound "static.mp3"
    scene londonbridge24 with flash
    stop sound
    play sound "dosex.mp3"

    s "Haaah! Hah! Hah! Fuck!"
    i "Mm..."
    s "How’s that?! You like that?! What was that noise?!"
    i "You went too deep...it stung a little..."

    "Ahh...this isn’t going to work."

    i "You don’t have to slow down. I was just surprised. That’s all."
    s "I don’t know if I can do this, Io..."

    play sound "static.mp3"
    scene londonbridge26 with flash
    stop sound

    i "What are you talking about? We’re already doing it."
    s "I don’t know if...I can cum..."
    i "Why not? Am I too loose?"
    i "You’re not going to make me use my mouth, are you? Because I really don’t want to taste that thing."
    s "Just...pretend to like it or something...I don’t know..."

    scene londonbridge27
    with dissolve

    i "Right there...fuck me harder or...whatever..."
    s "Ngh..."
    i "Oh, yes...that’s the spot..."
    s "Io..."
    i "Sensei..."
    s "I’m sorry..."
    s "I’m really sorry..."

    scene londonbridge28
    with dissolve2

    i "Don’t be."
    i "This is what I was put here for."
    i "And I’d much rather be {i}your{/i} tool than anyone else’s..."
    i "Because at least {i}I like{/i} you..."

    play sound "static.mp3"
    scene londonbridge24 with flash
    stop sound

    s "Hah! Fuck! Io...I’m gonna cum..."
    i "For real this time?"
    s "Inside or outside?..."
    i "Whatever. I can get a pill if I have to."
    s "Hah...hah...haaah!"

    with sexfade
    with sexfade
    scene londonbridge29 with cumflash
    with hpunch

    s "AAAAaaaaAAAH!!!!!!!"

    play sound "static.mp3"
    scene londonbridge30 with flash
    stop sound

    s "Hah.....hah....hah...."
    i "..."
    s "Hah.......sorry......"
    s "It normally doesn’t.....take that long....."

    scene londonbridge31
    with dissolve

    i "No worries."
    i "I’m gonna go pee now."

    scene black
    with dissolve2
    stop sound
    stop music fadeout 12.0

    s "Oh...yeah. Yeah, okay."
    i "Would you mind seeing yourself out? I won’t be able to sleep if you’re here."
    s "Uhh...yeah. Yeah. But I’ll call you tomorrow and-"
    i "I’m busy tomorrow."
    s "Then-"
    i "I’m sort of just indefinitely busy for a while. Sorry."
    s "Oh..."
    s "Okay..."
    s "Yeah."
    i "Yeah."
    i "Goodnight."

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve2

    s "..."

    play sound "knock.mp3"

    a "Dad? Is everything okay?"
    a "I didn’t even realize you were home. I got up to get a glass of water and-"
    s "Ami, can you sleep in here tonight?"

    scene black
    with dissolve2

    s "I don’t want to be alone."

    $ renpy.end_replay()
    $ iosex = True
    $ ioblock = True
    $ iospring3 = True
    $ io_love -= 10
    $ ami_love += 1

    "{i}Ami’s affection has increased by 1!{/i}"
    "{i}Io’s affection has decreased by 10!{/i}"
    "I..."
    "I think I should leave Io alone for a little while..."
    "She’ll come to me if she ever wants to talk again."
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

label iospring4:
    scene lr2_noon
    with dissolve2
    play sound "doorbell.mp3"

    "I did some cleaning today."
    "Or tried to, at least. "
    "Ami has always been better at that sort of thing. And Niki’s good at anything if she puts her mind to it."

    play sound "doorbell.mp3"

    "It’s still new to me, though."
    "Pathetic, I know. But I’ve yet to figure out which chemical concoctions best erase water stains. Or which type of vinegar is the one I’m supposed to use to prevent mold."
    "I can’t be bothered to look it up either. I just can’t find the motivation. I just don’t care enough."

    play sound "doorbell.mp3"

    "It’s satisfying, though."
    "Not the act of cleaning itself, but taking a step back and looking at all you’ve managed to accomplish in just a brief window of time."
    "Or in my case — how you have accomplished nothing in a window so large that the house itself could fall through it."
    "It’s satisfying because it’s validating. Just it validates that I am not cut out for this. And I am satisfied because I’ve always loved the way it feels to be right."

    play sound "doorbell.mp3"

    s "..."

    "I’ve been using that word a lot lately."
    "{i}Love.{/i}"
    "I’ve been handing it out like candy."

    play sound "static.mp3"
    show sakinormal with flash
    hide sakinormal with flash
    stop sound

    "For some reason, when I close my eyes, I can almost taste it. "
    "{i}That{/i} was like vinegar too."
    "Just it didn’t work the way it was supposed to."
    "Mold still grows within me to this very day."

    play sound "doorbell.mp3"

    s "..."
    s "Come in."

    play sound "static.mp3"
    scene iothemehosp1 with flash
    stop sound
    play music "io.mp3"

    i "Hi! Hello. I’m here to annoy you again. This time, with the 1997 PC Classic, Theme Hospital."
    s "Jumping back even further in time, huh? Don’t girls your age typically like modern things more?"
    i "I’m going to give you a second to think about what you just said so you can find the flaws yourself without me having to point them out."
    s "I’m glad you’re here, Io."

    scene iothemehosp2
    with dissolve

    i "You are? Why? I suck."
    s "Yeah, but so do I. So being around someone equally shitty makes me somehow feel a little {i}less{/i} shitty."

    if iosex == True:
        i "Well, I don’t know if I’d say I’m {i}equally{/i} shitty. I think you took the crown that time you had sex with me. But still, I’m probably a close second."
    else:
        i "You’re not shitty at all, though. You’re like my cool, guardian angel — who watches over me and prevents me from feeling like I’m the worst thing in the world."
        s "I literally {i}just{/i} called you shitty."
        i "Yeah, in comparison to {i}you{/i}, who is decidedly {i}un-{/i}shitty."

    scene iothemehosp3
    with dissolve

    i "Either way! Let’s go play games in your room so I stop feeling like I was only put here to suffer!"
    s "Is everything okay?"
    i "No! Of course not! Nothing is ever okay! Which is a huge part of why a lot of people play games in the first place!"
    i "But before I go on a tirade about how that statement applies to the endless rollercoaster, no pun intended, that is my life, how about you just agree and show me to your room?!"
    s "Io-"

    if iosex == True:
        scene iothemehosp4
        with dissolve

        i "Don’t worry, Sensei. I won’t be the only one having fun. I have something in store for you too."
        s "Am I allowed to ask what it is?"
        i "I’d really prefer you didn’t."

        scene black
        with dissolve2

    else:
        scene iothemehosp5
        with dissolve

        i "If you’re still feeling bad about what happened the last time I came over and did something like this, don’t be. That was {i}my{/i} fault for putting myself in a situation where I knew it could happen."
        i "But I know you aren’t going to hurt me now. So there’s nothing you need to worry about. Just sit back and let me bother you. I need you today."
        s "You need me?"

        scene iothemehosp6
        with dissolve

        i "I mean, realistically, I kind of need you {i}every{/i} day since when I’m {i}not{/i} with you, I’m still thinking about you. But, yeah. Today I guess I {i}really{/i} need you."
        s "And you don’t want to talk about {i}why?{/i}"

        scene iothemehosp5
        with dissolve

        i "Nope. I just want to sit in the dark with my favorite person and forget all about it. Please help?"
        s "..."
        i "Pleeeeeeease?"
        s "Okay, fine. And I promise not to invite you into bed this time."

        scene iothemehosp7
        with dissolve

        i "Fuck yeah! Affection!"

        scene iothemehosp5
        with dissolve

        i "You can totally invite me into bed if you want, though. I’d let you hug the life out of me if you felt like it. It’s just all that {i}other{/i} stuff I can’t stomach. But you already know that, so-"
        s "I sure do. Let’s just go to my room, okay? "

        scene black
        with dissolve2

        s "You clearly want to talk more about your weird retro hospital game than your feelings right now and, as always, I am fully supportive of avoiding any and all trauma dumping."
        i "Fuck yeah! Emotional cowardice!"

    "I lead Io to the bedroom."
    "She doesn’t notice how unclean everything is."

    scene iothemehosp8
    with dissolve2

    "Or maybe she does and she just ignores it. Maybe she’s being polite?"
    "Maybe she’s {i}used{/i} to filth by now after all that’s happened to her? And how I’ve surely only added to that by rubbing off on her over time. "
    "We sit with our shoulders close together. They brush against each other every once in a while — each one accompanied by a small flinch before she remembers I don’t {i}want{/i} to hurt her. I just {i}will.{/i}"

    i "It needs to install first. It might take a second."
    s "That’s fine. I’ll just be thankful for this moment of awkward silence in the meantime."
    i "And {i}I’ll{/i} be thankful your laptop still has a disc drive that allows me to install this in the first place. Those aren’t exactly common anymore."
    s "Yeah, well, when it comes to being behind the times in terms of technology and...the Internet...and the concept of growing up as a whole, I’m your guy."

    scene iothemehosp9
    with dissolve

    i "What’s in the “Math Homework” folder on your desktop?"
    s "Math homework. I am a very organized, intellectual man."
    i "It’s porn, isn’t it?"

    scene iothemehosp10
    with dissolve

    s "I don’t even know what that means. As I said, I am very behind the times in terms of technology and-"
    i "So you don’t mind if I open it then."

    scene iothemehosp11
    with dissolve

    s "Please don’t. A man’s math homework folder should remain hidden from even those he trusts the most."
    i "There’s some weird stuff in there, isn’t there?"
    s "I’m surprised you even want to know given who you are as a person."

    scene iothemehosp10
    with dissolve

    i "I work in a bathhouse. I’m used to nudity, Sensei. Besides, I think it’s kind of funny. Like...porn as a whole. Would I watch it on my own? No. But I won’t think less of you for doing it."
    i "Unless you still have those pictures of Uta from when she was a kid in there."

    scene iothemehosp12
    with dissolve2

    s "..."
    i "Put you on the spot, huh?"
    s "Io-"
    i "Don’t worry. It’s not really my place to weigh in anymore now that she’s straight up told both of us that she’s okay with you having them."
    s "..."

    scene iothemehosp13
    with dissolve

    i "Oh, look! It finished installing."
    s "You...{i}can{/i} weigh in if you want."

    scene iothemehosp14
    with dissolve

    s "I think it’s...great that you want to protect your friend. And I know that holding onto something I never should have had in the first place was wrong. "
    i "..."
    s "So...you can weigh in. You can call me out. I know you haven’t gotten it all out of your system yet."

    if iosex == True:
        s "You already know how bad I {i}can{/i} be, so-"
    else:
        s "Just because I...left {i}you{/i} alone...doesn’t mean I-"

    i "There are a lot of really bad people in this world, Sensei."
    i "We both know that."

    scene iothemehosp15
    with dissolve

    i "But not all of them understand that what they’re doing is even wrong to begin with. Like that douchebag who posted Uta’s pictures online in the first place."

    play sound "static.mp3"
    scene iothemehosp16 with flash
    stop sound

    i "{i}Or the woman who used to torture me.{/i}"
    s "{i}You don’t have to-{/i}"
    i "{i}No, it’s...{/i}"
    i "{i}I mean, it’s not fine. But there’s no sense in hiding it from you anymore now that it’s out in the open. {/i}"
    i "{i}Like, shit, the whole fucking class probably knows after that stupid trivia show thing. And talking about it always just makes it worse, but...{/i}"
    i "{i}On the off chance that a place like Heaven exists, cursing her any chance I get can remind the gods or...angels or...whoever makes the guest list to keep her off of it. {/i}"
    i "{i}Even Hell would be too cold for a demon like her.{/i}"
    mot "You’re going to be good, right?"
    i "..."
    mot "Because you know what will happen if you {i}aren’t{/i} good, right?"
    i "You’ll send Sir Meowington back to the shelter."
    mot "And?"
    i "No dinner. No computer. No games. No anything."
    mot "And if the doctor asks you how you’re feeling? Do you remember that too?"
    i "I’m having a hard time getting adjusted to my new school."
    mot "Because?"
    i "Because everyone hates me."
    mot "That’s not what we discussed."
    i "It’s the truth, though."
    mot "Do you know {i}why{/i} they hate you, Io?"
    i "Because I’m not like them."
    mot "Because you’re an ungrateful, disobedient, obnoxious little brat who insists on ruining the lives of {i}everyone{/i} you speak to."
    i "I’m sorry."
    mot "Well, you won’t have to be sorry for long..."
    mot "You’ll be getting home-schooled as soon as that useless father of yours finishes the paperwork."
    mot "You know what that means, don’t you?"
    i "You’ll be my teacher."
    mot "And Mommy’s already taught you so much, hasn’t she? Are you excited to learn more?"
    i "Can we just move again instead?"
    mot "{i}What did you just say?{/i}"
    i "..."
    mot "{i}This{/i} is why the kids at school hate you. {i}This{/i} is what makes you ungrateful."
    mot "I {i}made{/i} you. I put a roof over your head. I buy you nice clothes...all the games you want...those fucking {i}animals{/i} that {i}I{/i} have to feed, and {i}this{/i} is how you say thanks for all of that?"
    i "I’m sorry."
    mot "No, you’re not. You’re never sorry. You’re a useless child who can’t follow even the simplest of directions. The kind that only a mother could love."
    mot "What will you do if {i}I{/i} start to hate you next, Io? Where will you go? Are you going to live out on the street? Become a fucking {i}whore?{/i} Is {i}that{/i} your plan?"
    i "I’ll be good."
    mot "{i}Good.{/i} Because if you’re not, I’ll-"

    scene iothemehosp17
    with dissolve

    mot "Um...{i}excuse me?{/i} Can I help you?"

    scene iothemehosp18
    with fade

    yamom "{i}Yasu! Move! What are you doing?!{/i}"
    mot "Would you mind controlling your child? My daughter has {i}anxiety.{/i} She’s not equipped to speak to random, weird little girls who want to stare at her for no fucking reason."
    yamom "I-I’m sorry. She’s not well. Yasu, move. {i}Now.{/i}"
    ya "Bad woman..."
    mot "{i}What?...{/i}"
    yamom "I’m so sorry! She thinks she sees things! And she’s always hearing these {i}voices{/i} and-"
    mot "And you think I {i}care?!{/i} Get your fucking freak away from my little girl or I’ll call the police. This is harassment. Who’s your doctor? Are you even supposed to be here?"

    scene iothemehosp19
    with dissolve

    yamom "S-Sorry! We were just leaving!"
    ya "But-"
    yamom "{i}Shh! Will you ever stop embarrassing me?! You can't just stare at other girls like that! I don’t care what you think you heard! Just...be normal!{/i}"
    mot "Tch. The nerve of some people."
    mot "Clearly, not everyone is cut out to be a mother."

    scene black
    with dissolve2

    mot "Go to the bathroom and fix your hair before your appointment. We can stop for ice cream on the way home if you do a good job."
    i "I’m tired. I don’t want ice cream."
    mot "Yes you do. You love ice cream. Now, go. You look like a fucking mess. Almost as bad as that other girl. People are going to think I abuse you. Do you {i}want{/i} that? Do you {i}want{/i} to make me look bad?"
    i "I’m sorry. I-"
    mot "That’s it. No computer. No games. You’ll sit in your room and read until Mommy has a job for you. Do you understand?"
    i "..."
    i "I’m sorry."

    if iosex == False:
        scene iothemehosp20
        with dissolve2

        i "..."
        s "..."
        s "You’ve been...sitting there in silence for like five minutes now, Io."
        i "I’m sorry."
        s "{i}Why?{/i}"

        scene iothemehosp21
        with dissolve

        i "No, like...sorry for...zoning out. Uhh...where..."
        i "Where were we exactly?"
        s "Something about Hell being too cold for-"

        scene iothemehosp22
        with dissolve

        i "Y-Yeah. Hell is too cold for people like her. Not you, though. And that’s pretty much all I have to say on the subject. Sorry if I made it sound like I had more. I-"
        s "So...this “Theme Hospital” game. What’s the point? What do you do?"

        scene iothemehosp23
        with dissolve

        i "Huh?"
        s "You said it finished installing? I want to hear you explain it to me. What are we supposed to do?"
        i "..."
        s "...Io?"
        i "Am I..."
        i "{i}Really{/i} safe now, Sensei?..."
        s "..."
        i "..."
        s "You’re in danger any time you’re near me, Io. I’m not going to pretend you’re not just because I decided against having sex with you {i}one time.{/i}"
        i "Do you want to have sex with me {i}now?{/i}"
        s "Not really, no."
        i "That’s two times then. {i}Now,{/i} will you say it?"
        s "Nope. We’re supposed to be playing the 1997 PC Classic, Theme Hospital. You wanted to {i}avoid{/i} feelings today, remember?"
        i "I remember. But now my heart is beating out of my chest and I kind of want to just hug you and cry. But I also {i}hate{/i} crying so it’s a major conundrum. I’m not sure what to do."
        s "Give me your hand."

        scene black
        with dissolve
        play sound "tackle.mp3"
        stop music fadeout 15.0

        i "Sensei?"
        s "Sorry. Do you need both hands to play this game? I figured holding onto one of mine might help us kill two birds with one stone."
        i "I..."
        i "I can...play with one..."
        i "A-Anyway! The whole point of the game is to create a hospital that specializes in curing a bunch of weird diseases that-"

        "Io and I spend the rest of the afternoon holding hands and playing video games in the dark."
        "I feel like a kid again. I imagine she does too."
        "But I’m confused about why we like it."
        "Eventually, she leaves. But she keeps the game here."
        "I keep playing until it’s dark everywhere, not just in my room."
        "And before I know it, I’m looking down at a chat window full of pictures of my progress, with her name plastered to the top of it."

        $ renpy.end_replay()
        $ iospring4 = True
        $ io_love += 5

        "{i}Io’s affection has increased by 5!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4

    else:
        scene iothemehosp24
        with dissolve2

        i "..."
        s "..."
        s "You’ve been...sitting there in silence for like five minutes now, Io."
        i "I’m sorry."
        s "{i}Why?{/i}"
        i "Because I’m sorry for everything. That’s just...how I am."
        i "I know it’s not my fault. But I still can’t help but say it. It’s like...a reflex, almost."
        i "Like, if I’m not constantly apologizing, everything I care about is going to be taken away. And I’ll be all alone in the dark...in the glow of some old laptop, waiting for my pills to kick in."
        s "..."
        i "Why can’t I be happy, Sensei?"
        s "I ask myself the same question all the time."
        i "But you know what will {i}make{/i} you happy...."

        scene iothemehosp25
        with dissolve2

        i "And it’s something {i}I{/i} can help with..."
        i "So I will."

        scene black with dissolve
        scene iothemehosp26 with dissolve2

        s "Io-"
        i "It’s hard."
        s "..."
        i "Do you mind if it’s under the table?..."
        s "Do I mind if {i}what{/i} is under the table, Io?"
        i "Are you asking because you genuinely don’t know? Or because you want to hear me say it?"
        s "The latter — but only because I want you to snap out of whatever it is that’s going on with you right now."
        i "Let me make you happy, Sensei. As payment for spending time with me today. It's the least I can do."
        s "You don’t need to {i}pay{/i} me, Io. You don’t need to do any of this."
        i "But it’s hard."
        s "..."
        i "That means you want it, right?"
        s "Of course I {i}want{/i} it, but-"
        i "It’s just my hand..."
        i "This much, I can stomach."
        s "..."
        i "It’s so big..."
        i "You’re so-"

        scene iothemehosp27
        with dissolve

        s "No."

        play sound "static.mp3"
        scene iothemehosp28 with flash
        stop sound

        i "..."
        s "..."
        i "{i}No?{/i}"
        s "No."
        i "But I..."
        i "I started it. {i}I{/i} chose to do this. So you don’t have to feel guilty about-"
        s "I said no."
        i "..."
        s "Do you know what that word means?"
        i "To me, it meant nothing for a very long time."
        s "And now?"
        i "Now, I’m just...confused."
        i "Do you like me or...do you not like me?"
        s "I like you. But I’m not going to force you to do anything."

        scene iothemehosp29
        with dissolve

        i "But...you’re not! Like I said, this is {i}my{/i} choice! {i}I{/i} intended to do this today!"
        s "Okay. Then I won’t let you force {i}yourself{/i} either."
        i "Why...not?"
        s "Because I never want to see you like that again."

        scene iothemehosp30
        with dissolve2

        i "..."
        s "..."
        i "I never want to see you like that again either..."
        s "Was it scary?"
        i "Yeah."
        s "But you still like me either way? You’re not just lying about it because you’re afraid of change?"
        i "I like you...a lot."
        s "Then take your hand off of me..."
        s "Okay?"
        i "..."
        s "..."

        scene black
        with dissolve2
        stop music fadeout 8.0

        i "Okay..."

        "Io and I spend the rest of the afternoon holding hands and playing video games in the dark."
        "I feel like a kid again. I imagine she does too."
        "But I’m confused about why we like it."
        "Eventually, she leaves. But she keeps the game here."
        "I keep playing until it’s dark everywhere, not just in my room."
        "And before I know it, I’m looking down at a chat window full of pictures of my progress, with her name plastered to the top of it."

        $ renpy.end_replay()
        $ iospring4 = True
        $ io_love += 5

        "{i}Io’s affection has increased by 5!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4

label iospring5:
    scene black
    stop music

    "The roseate spoonbill’s colors are the brightest early May."
    "The crowning jewel of avians in threskiornithidae."
    "Its favorite meal, carotenoids — they paint its wings in pink"
    "While astaxanthin lies in wait and hydrocarbons sink."

    scene krill
    "why do i still try so hard"

    play sound "static.mp3"
    scene iofinallywins1 with flash
    stop sound
    play music "justbehappy.mp3"

    i "Uta! Look! We’d totally die if we fell from here right now!"
    u "Yeah, but...is that really something you want to be excited about?"

    "Before the dialogue drifts further into unintended, unwanted, or uncertain directions, I want to take a minute to interrupt this Io event for the sake of shining a light on the rapidly declining mental state of me and my cat."
    "It all started one week when the sun was shining. Everything was good and I had just finished cloaking the outdoor plants and pipes in various quilts to shield them from the impending endless cold."
    "When I came back inside, I noticed a shine on the floor I couldn’t quite explain. Did someone wax it while I wasn’t looking? Unlikely. Was it dissolving? Also unlikely. It had to be a trick."
    "So I went upstairs, gripping the railing on the right as it fits my dominant hand better, hoping that today isn’t the day I accidentally pry it off of the wall and fall to my death. When, at the top of the stairs, I notice him."
    "His mouth is open in an attempt to meow, but no sound comes out. I mock him. He hates me. He tries again. No sound. I mock him again. Why can I meow, but he can not?"
    "Have I been the cat this whole time? Has he been the human? Are words just arbitrary things we use to signify and explain ideas that can be better explained and emphasized by the balls in our eyes alone?"
    "We sat on the couch. He curled up beside me. This is a lie."
    "I went to my room and locked him out behind a gate. He always disturbs me. He’s meowing right now. I can hear him. I know it came back. He was merely deceiving me."
    "That bastard. I will never forgive him. But more than that, I will never forgive myself for succumbing to the pressure of existing for the sole purpose of existing."
    "“When did this become so boring?” I ask myself, asking myself. “What was the meaning of that phone call?”"
    "Anyway, that’s it. Back to Io."

    i "Of course it’s something to be excited about! Any situation where you’re close to death is something to be excited about! It’s why amusement parks are so cool!"

    scene iofinallywins2
    with dissolve

    u "{i}That’s{/i} why they’re cool? Not because they’re little urban sanctuaries filled with fun rides and assorted street foods?"
    i "Those help too! But more than anything, they’re fun because they give us a chance to experience things we’d never be able to in real life!"
    u "But...this is real life right now."

    scene iofinallywins3
    with dissolve

    i "Technically speaking, yes. But amusement parks exist in a special area between {i}real{/i} real life and {i}fake{/i} real life. Which is also known as fiction. Which is also known as where I want to be because it hurts less."
    u "You’re weird. Are you experimenting with new drugs again?"
    i "No, I’m just happy I’m finally here."

    scene black
    with dissolve
    play sound "tackle.mp3"

    u "Me too! I don’t get to see you actually have fun very often."

    scene iofinallywins4
    with dissolve

    u "I’m sorry it’s with me and not Sensei, though. I know {i}he’s{/i} the one you really wanted to come with."
    i "Don’t be sorry at all! You’re just as high up in the Io ranking as he is. And it’s not like I was aiming for it to be a {i}date,{/i} so this is perfect as far as I’m concerned! I just don’t know why it took us so long to come here."
    u "Our schedules don’t always match up because of work and school. Like, when was the last time we {i}both{/i} had an entire weekend off?"

    scene iofinallywins5
    with dissolve

    i "Probably...never. I don’t think that’s happened once since you got sucked into the hellhole that is the maid cafe."
    u "It’s not a hellhole, Io. I love working there. I’m just sad that it cuts into our time together. I like going on dates with you."
    i "I literally just said that it wasn’t a date."
    u "Noooo, you said you weren’t {i}aiming{/i} for it to be a date."

    scene iofinallywins6
    with dissolve

    u "But seeing as {i}I{/i} paid and {i}I{/i} invited you out, {i}I{/i} get to decide what we call it. We are on a date."
    i "Over Sensei already then? Am I the next obsession?"

    scene iofinallywins7
    with dissolve

    u "A date with him here {i}does{/i} sound enticing, right? Holding hands as you go up the ferris wheel...kissing beneath the moon once you reach the top."
    i "Mhm."
    u "We’re almost there, Io. Perhaps...{i}we{/i} should-"

    scene iofinallywins8
    with dissolve

    i "No thanks! You’ll be the first to know if my sexuality magically changes, though. I’ll just keep waiting for the adult male I’ve decided to like to kiss me up here instead."
    u "How’s that going, by the way? You went over to his house the other day, didn’t you?"

    scene iofinallywins9
    with dissolve

    i "Yeah. We just sat in the dark and played games, though."
    u "So a perfect Io date?"
    i "Nah. Not enough wood."
    u "Curious. I imagined a perfect Io date wouldn’t involve any wood at all."

    scene iofinallywins10
    with dissolve

    i "Ha ha ha. Bad Uta. I’m sending you to horny jail. You’ll need to roll doubles to escape and you can not collect $200 when you pass Go."
    u "A boy and a girl...alone in the dark...huddled together in the glow of a computer...even {i}that{/i} doesn’t get your blood pumping, Io?"
    i "It...{i}does.{/i} Just not really in {i}that{/i} way, you know?"

    scene iofinallywins11
    with dissolve

    u "Ugh. I {i}wish{/i} I knew. I can’t even bump into the guy without wanting to get freaky anymore."
    i "That sounds horrible."
    u "It is."

    scene iofinallywins12
    with dissolve

    u "But you know what isn’t? The fact that we can talk about it now."
    i "Yeah, there seems to be a lot less “internal struggle” going on with you ever since telling me about your feelings. I’m happy for you, Uta."
    u "I’m happy for {i}us,{/i} Io. There aren’t many best friends who’d be able to like the same guy and just openly talk about it like it’s no big deal at all. The fact that {i}we{/i} can survive it just means we’re the best."
    i "Or that our thoughts on love and companionship have been mutilated beyond recognition due to our traumatic upbringings and resulted in an abnormally skewed perception of what it means to be with someone."
    u "Don’t ruin it."
    i "But ruining things is my specialty."
    u "Yeah! But for a second, I thought it was going to be {i}mine{/i} since I’ve never had to admit to somebody I’m crushing on the same person as them before!"
    i "I like how you didn’t refute the fact that ruining things is my specialty and just went along with it."
    u "There’s no use fighting with you when it comes to the way you think about yourself. I’ll only refute that if it’s someone {i}else{/i} who says it."
    i "Regardless, I’m happy too. That we can talk about this. Even though I’ve kind of {i}always{/i} been open to talking about it and was just unaware that you {i}wanted{/i} to."
    u "What do you think’s gonna happen if one of us actually gets him?"
    i "You mean if {i}you{/i} actually get him? Sensei would never choose me as a partner, even if he {i}does{/i} really care about me. I’m too lacking when it comes to aspects he actually requires in a person."
    u "Like...the whole sex thing?"
    i "Right. And the fact that there’s no way I could ever help him with any of {i}his{/i} issues when you’ve seen how I handle mine. You, though? You’re great at that."

    scene iofinallywins13
    with dissolve

    u "I’m not {i}great{/i} at anything, Io. We’re both screwed if getting help is going to be important to him. Especially since, on a baseline level, him getting help would effectively {i}destroy{/i} our chances."
    i "Not mine if sex is the implication there. But also, you’re way wrong. You’ve helped me a ton, Uta."
    u "And you’ve helped {i}me{/i} a ton too. But that doesn’t mean we’re any good compared to everyone else in the running. Neither one of us is in the top five of the love journal."

    scene iofinallywins14
    with dissolve

    i "Buuuuuuuuut...if we combine {i}forces?...{/i}"
    u "You’re really gunning for this throuple thing, aren’t you?"

    scene iofinallywins15
    with dissolve

    i "Just imagine it! All {i}three{/i} of us on the ferris wheel! Me holding his hand and talking about how close to death we are while the two of you do, like...sex stuff."
    u "On a ferris wheel? Right next to you?"
    i "You would. You know it."

    scene iofinallywins16
    with dissolve

    u "Yes, but I would {i}not{/i} be proud."
    i "Well, whatever happens Uta...I’m glad I get to go through it with you."

    scene iofinallywins17
    with dissolve

    i "You really are the best thing that’s ever happened to me. And it is {i}because{/i} we are so close to death that you can trust me when I say that."
    u "I’d trust you either way, Io. You’re the best thing that’s ever happened to me too."
    u "Also, we’ve finally reached the top of the ferris wheel. So if you {i}are{/i} looking to kiss someone up here-"

    scene black
    with dissolve2

    i "I’m good, Uta. Also, this ferris wheel is, like...crazy slow, isn’t it?"
    u "Right? We’ve barely moved this whole time."

    "The thing goes around and eventually completes a cycle or something and then the ride ends and then they get off of it because Uta needs to pee. Narration."

    stop music
    play sound "static.mp3"
    scene iofinallywins18 with flash
    stop sound
    play music "blueair.mp3"

    u "I need to pee!"

    "Also Blue Air comes on and changes the mood. Something is probably about to happen."

    i "Why do you seem so proud of that?"
    u "Because I held it in for what I can only imagine is the longest ferris wheel ride in all of Japan!"
    i "Okay. Well, the bathroom is right there. So."

    scene iofinallywins19
    with dissolve

    u "Aren’t you going to offer to come with me?"
    i "Why would I do that?"
    u "Because we’re girls and that’s what girls do."
    i "Why?"
    u "Well...because."
    i "..."
    u "..."

    scene iofinallywins20
    with dissolve

    u "{i}Okaaaay!{/i} Guess I’ll just go to the bathroom alone then! Sure hope nothing happens to me!"

    scene iofinallywins21
    with dissolve

    u "But...after that? Rollercoasters."
    i "Fuck yeah."
    u "We’re staying here until they kick us out tonight. I hope you’re ready, bitch."
    i "I was born ready, other bitch."

    scene iofinallywins22
    with dissolve

    u "Let’s not call each other “bitch” anymore. I love you too much."
    i "I love you too, Uta. That felt wrong and I’m sorry."

    play sound "static.mp3"
    scene iofinallywins23 with flash
    stop sound

    u "Kaybye! Be right back! Don’t go anywhere!"

    "“Where would I even go in the first place?” she thought to herself, removing a phone from her pocket that she’d neglected to look at since approximately 2:00 PM."
    "She hadn’t received even a single notification within that time, though. Sensei must have been done playing that game and sending her progress updates."
    "She didn’t expect him to ever go back to it without being pushed or reminded to, but she liked how he kept her in the loop for a whole night. Like he was actually thinking about her."
    "Which he probably wasn’t right now. And that made her want to text him. But she didn’t, because she thought that would be annoying. And this was essentially the only way Io ever used her phone in the first place."
    "Type something out. Erase it. Scroll through older messages. Scroll through her photo reel to find candid photos she’d taken of him from her desk when he used to come to school."
    "It wasn’t a {i}good{/i} use of her time. But it was enough to bridge the gap between different bouts of nothingness on the way to something that {i}might{/i} be good."
    "This was the best day she’d had in a long time, and he hadn’t even been involved. So why was there this urge to involve him {i}now?{/i}"

    scene iofinallywins24
    with dissolve2

    "She got caught up in this question for so long that she didn’t even notice she was being approached by two large men."
    "They’d seen her at several points throughout the day. Her stupid hair made her stick out."
    "They joked among each other about using her twintails as handlebars for impure purposes. What they said about her friend was even worse."
    "But right now, they said nothing. They just stood in front of the girl, waiting for her to notice them."

    i "Go away."

    "And then she did. But it was not in the way they wanted."

    man1 "{i}Go away?{/i} Can a guy not even walk up to a girl anymore without her trying to turn it into a thing?"
    i "..."
    man2 "Maybe she’s deaf? Try-"
    man1 "{i}Speaking louder and drawing attention to ourselves? Are you a fucking idiot? Just let me work my magic.{/i}"
    i "I hope it’s to make yourself disappear, because I want nothing to do with either of you."
    man1 "Aaaah, so you can hear us after all. What are you up to? Where’d your friend go?"
    i "Home. And my ride will be here any second now, so you should probably leave."
    man2 "The hell’s your problem? All we did was walk up to you."
    man1 "Yeah. We just wanted to see if you and you and your friend wanted to go somewhere together."
    i "Welp. She’s not here, so I guess that defeats the purpose. Bye."
    man1 "How about {i}just{/i} you?"
    man2 "Yeah. Think you can handle both of us, little girl?"

    scene iofinallywins25
    with dissolve2

    i "..."
    man1 "{i}Don’t creep her out, man. You’re coming on too strong.{/i}"
    man2 "{i}But that’s what-{/i}"
    man1 "{i}Yeah, I know what the goal is. But that’s not how this works. Just let me do the talking.{/i}"
    i "Why are you even here?...Shouldn’t you be in space or something?"
    man1 "Space? You kidding? Do we look like the type to get roped into that bullshit? You should see the car I pulled up in. It’d get you wetter than the log flume."
    man2 "{i}Yeah. And I’m the one who comes on too strong.{/i}"
    man1 "{i}Fuck off.{/i}"
    i "I’m asexual."
    man1 "Translation — I ain’t had a good dick yet."
    man2 "Probably hasn’t had one at all. She’s a sophomore, max."
    man1 "I bet her friend has. {i}She{/i} looked like she could handle both of us. This one’s just a prude."

    scene iofinallywins26
    with dissolve
    play sound "footsteps.mp3"

    i "Mm..."
    man2 "Whatcha looking at on your phone there? Mind showing us?"

    scene iofinallywins27
    with dissolve

    man1 "In fact, why not just {i}give{/i} us your phone? I won’t keep it, I promise. I just want to put my contact info in there."
    man2 "Daisuke, hold up. There’s someone-"
    man1 "It’s {i}fine.{/i} We’re not doing anything wrong. We’re just talking to our new friend here. What’s your name? I don’t bite."
    i "{size=-20}Leave me alone.{/i}"
    man1 "What was that? I couldn’t hear you."

    scene iofinallywins28
    with dissolve

    i "I said...{i}leave me a-{/i}"
    q "You ain’t...gotta say shit...to punks like them."

    scene iofinallywins29
    with dissolve2

    i "Huh? Who-"
    man2 "Oh, fuck! Isn’t that-"

    play sound "static.mp3"
    scene iofinallywins30 with flash
    stop sound
    play sound "window.mp3"
    with hpunch

    man2 "W-What are you doing, you crazy bitch?! His bones are made of glass!"
    yu "Well...he should’ve thought about that...before pickin’ on a fuckin’ high school girl!"
    man1 "My...fragile...everything! I can’t move!"
    i "Yuki?! What are you-"
    yu "Leave them...to me! I...can handle this!"

    play sound "static.mp3"
    scene iofinallywins31 with flash
    stop sound

    i "Is he bleeding out of his {i}eyes?{/i}"
    yu "If he ain’t already...he’s about to be!"
    man1 "N-No! Don’t! Stop! Please!"

    play sound "window.mp3"
    scene iofinallywins32 with hpunch

    man2 "Daisuke! No! His eyes were made of glass too!"
    man1 "Omar! I can’t see! I can’t fucking see!"
    man2 "I’ve got you, buddy! I’ve got you!"

    scene iofinallywins33
    with dissolve

    yu "Yeah...take him. And while you’re at it, do yourselves a fuckin’ favor and...never come around here again...you got that?"

    play sound "footsteps.mp3"

    man2 "Y-Yeah! You’ll never see us again! Just p...please! D...Don’t tell the boss we-"
    yu "Do you want some too?! Huh?!"
    man2 "{i}Aaaah! No! Don’t hurt me!{/i}"
    man1 "{i}Omar...I...I can see the light...{/i}"
    man2 "{i}Hang in there, Daisuke! Hang in there!{/i}"

    scene iofinallywins34
    with dissolve

    i "Yuki! That...was so fucking cool! Like, where did you even {i}come{/i} from?! If I wasn’t seconds away from having a panic attack, I’d-"

    scene iofinallywins35
    with dissolve2

    yu "Hah....hah....haah..."
    i "Yuki?..."
    i "Is everything...alright?"

    scene iofinallywins36
    with fade

    yu "Never...better..."
    i "You look terrible...Did something happen?"

    scene iofinallywins37
    with dissolve

    yu "Forget about me...what are you doing here...alone?..."
    i "I’m with Uta. She just went into the bathroom and....what...what are {i}you{/i} doing here?"
    yu "Meeting...someone..."
    yu "Those guys come up to you...outta nowhere?..."
    i "I...yeah. I was just waiting here and-"
    yu "That happens again...just tell ‘em...you know me..."
    yu "You got it?..."
    i "Yuki...you’re so pale...I really think you should-"
    yu "I’m fine...but....I’ve...gotta go..."

    scene black
    with dissolve2

    yu "Remember...say my name...if shit...mngh...gets...bad!"

    play sound "static.mp3"
    scene iofinallywins38 with flash
    stop sound

    u "Io! What happened?! I heard yelling! But I was already in the middle of stuff and-"

    scene iofinallywins39
    with dissolve

    u "Is that Yumi’s mom? What’s she doing here?"
    i "She...saved me from...these two fucking creepy guys..."

    scene iofinallywins40
    with dissolve

    u "What?!"
    i "One of them had glass bones. It was weird."
    u "You’re okay though? They didn’t hurt you? They didn’t touch you? I’m sorry I wasn’t here. If I knew, I-"

    scene iofinallywins41
    with dissolve

    i "Would have held it in forever?"
    u "If that’s what it takes to protect you."

    scene iofinallywins42
    with dissolve

    i "I’m fine, Uta. Thank you."

    scene clearnightsky
    with dissolve2

    i "But I..."
    i "I’m worried about Yuki..."
    i "I’ve never seen her so-"
    u "Tell me at home. The bus just pulled up. We should catch it before it leaves."
    i "What? But I thought you said they’d have to kick us out-"
    u "That was {i}before{/i} you were apparently almost abducted! We’ll come back for the rollercoasters soon. It’s not safe tonight."
    i "But-"
    u "Hot dogs. Konbini. As many as you want."
    i "Ugh. You’re lucky I’m hungry."
    u "I’m lucky you’re {i}safe.{/i} Now, come on. Hold my hand."
    i "Do I really have to-"
    u "Hold my fucking hand, bitch!"

    scene black
    with dissolve2

    i "Wow. That was the shortest pact we’ve ever made, other bitch."
    u "I’m sorry and I love you. Again."
    i "I love you too. Again. But love can wait! It’s wiener time!"

    stop music
    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    s "Did somebody say “wiener time?”"
    s "...Wait, what?"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Why did I just jump out of bed to say that? That’s not even the line."

    "{i}Somewhere else, two girls were safe.{/i}"
    "{i}One woman wasn’t.{/i}"

    $ renpy.end_replay()
    $ iospring5 = True

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

label dormwarsfiveio1:
    "........."
    "......"
    "..."
    play sound "static.mp3"
    scene iodatewar1
    with flash
    play music "goodmorning.mp3"
    stop sound

    hide saturday onlayer date
    show sunday onlayer date

    $ day = 7
    $ totaldays += 1

    "I didn’t sleep well last night. "
    "As it turns out, I’m haunted whether I dream or not. The only difference is the one behind the spectral wheel. "
    "So I guess I’ll just resign myself to a life where I never feel rested again and let my body get carried off by the wind to whatever dump the universe has in store for me next."
    "Something tells me there will be a girl there. That much is all but guaranteed when they’re somehow more accessible to me than air. "
    "That isn’t me bragging, I promise. I’m sure you’d be drowning in suitors too if all of the competition suddenly vanished. So maybe you can bank on that."
    "Just know that every monkey’s paw is cursed — and being wanted isn’t something I’d suggest you want yourself."
    "Of course, there’s always a chance I’m just projecting here. And that you’re off somewhere else, being happier and more loved than I am."
    "Actually, come to think of it, that sounds pretty plausible."
    "If that {i}is{/i} the case, though — maybe I can ask you a question this time instead of just providing you with unsolicited advice on how to fuck everything up."
    "Where would I even begin, though?"
    "Who are you, maybe?"
    "Who have I been talking to this whole time? Who is it that keeps me sane when all else seems to advocate for the opposite?"

    scene iodatewar2
    with dissolve

    "I don’t even know where to start. "
    "We’re so close, yet so far. You know everything about me and I know {i}nothing{/i} about you."
    "But maybe there’s something that can bring us together."

    scene iodatewar3
    with dissolve

    "Maybe there’s something that-"

    scene iodatewar4
    with dissolve2

    s "..."

    play sound "static.mp3"
    scene iodatewar5 with flash
    stop sound

    i "..."
    s "..."
    i "Why do you sleep like that?"
    s "Why are you in my room?"

    scene iodatewar6
    with dissolve

    i "Why is it already that hard? Are you just like this by default?"
    s "Unfortunately, yes."
    i "Gross."
    s "Thanks, Io. I always love being insulted as soon as I wake up. Now, to get back to my first question-"

    scene iodatewar7
    with dissolve

    i "Jeez, Sensei. You act like there’s no precedent for this."
    i "Every time you go to sleep, you should be thinking to yourself, “there is a possibility that Io will pick the lock and I will wake up beside her.” Would it kill you to act accordingly?"
    s "Kill me, no. But having {i}any{/i} amount of time to myself might be-"

    scene iodatewar8
    with dissolve

    s "Actually, nevermind. It’s probably good that you’re here."
    i "Right! Plus, this gives us more time for our date! It’s a {i}good{/i} thing my anxiety ate away at me and forced me to sneak into your hotel room again! Praise my broken mind!"

    scene iodatewar9
    with dissolve

    i "Maaaaybe put on pants first, though."

    if iosex == True:
        i "Unless this is the part where you put it inside of me again. Which, as always, ew. But if it earns me any date points and gets you to enjoy my company any more-"
        s "Io, stop that."
        i "I can’t! Conditioning is fun!"

    s "Just...go wait outside of the room and I’ll be out in a minute."

    scene iodatewar10
    with dissolve

    i "Fine. But if you escape outside of the window to try and get away from me, just know that it will make me really sad and that I won’t actually do anything about it because I’m weak and I suck."
    s "I will...keep that in mind."

    scene black
    with dissolve2

    "Io steps out and, hopefully, isn’t accosted by any of her classmates wondering why she’s outside of my room."
    "I figure it’s either that or {i}all{/i} of them are outside of my room, joined by a camera crew and providing commentary on how they expect this thing to go."
    "From what I understand, the girls have always really liked this “date war” stuff — even when they’re not the ones who get to take me out."
    "I think they just like the idea that it {i}could{/i} be them. And that it likely {i}will{/i} be them if we go through enough of these."
    "And I bet all of the ones who are thinking that are jumping for joy right now given that my dates this year are my perpetual best friend and...whatever they see Io as."
    "What {i}do{/i} they see Io as?"
    "I know how Uta does, but...do the rest even see her at all?"
    "Or is going out with her going to be one more situation akin to holding hands with a ghost?"

    scene iodatewar11
    with dissolve2

    "Find out now — because we’re already at her favorite place in the world."

    i "Green tea...energy drink. Which one is better for spelunking?"
    s "Which one is better for {i}what?{/i}"

    scene iodatewar12
    with dissolve

    i "Spelunking. It’s when you-"
    s "I know what it is, Io."
    i "Then why did you ask?"
    s "Because it’s the first hint of what this “date” has in store and is perhaps the most wildly different scenario I have encountered in all of these so far."
    i "Thanks. I take great pride in being an unlikable outcast with fringe interests that may or may not annoy you."
    s "You’re a very likable outcast. I’m just not sure if I’m built for cave exploration."
    i "Then it sounds to me like you could use a green tea. {i}Or{/i} an energy drink. Which one of those sounds like it would be more useful?"
    s "Io-"

    scene iodatewar13
    with dissolve

    i "Relax, okay? I’m not throwing you into an actual cave. That’s a third date activity. "
    i "I’m just taking you back to the secret tunnel that I know you already explored with Uta since {i}I{/i} always wanted to be the one to show you that place."
    s "Oh. Well, why didn’t you then?"
    i "Why do you think?"
    s "Because you’re a cowardly loser who gets off on self-inflicted pain?"

    scene iodatewar14
    with dissolve

    i "I mean, that’s not really how {i}I{/i} would word it. But yeah, that’s more or less the answer I was looking for. The only problem is I still don’t know what to buy you."
    s "Wait, it’s for me?"
    i "Yeah. Am I not supposed to buy you things? We’re on a date."
    s "Isn’t that usually-"
    i "If you’re about to perpetuate gender norms at me, let it be known that I am far more traditionally masculine than you are. "
    s "I hate that you’re right."

    scene iodatewar15
    with dissolve

    i "Don’t! Because that stuff doesn’t matter! "
    s "It clearly matters {i}a little{/i} if you’ve aimed all of your hate specifically at girls and not-"
    i "Okaaaay, so it matters in some specific circumstances! But again, I am a hypocrite! And I think the important thing right now is taking into account that I am bringing {i}you{/i} on a date!"
    i "Doesn’t it make the most sense for the date aggressor to be the one who has to provide material goods for the date prey?"
    s "Sorry, are you calling me your {i}prey{/i} right now?"
    i "Just because I’m nervous and couldn’t think of a better word! Beverage?"
    s "..."
    i "???"
    s "Give me the tea."

    scene iodatewar16
    with dissolve

    i "As expected of the prey."
    s "Fine. Give me the energy drink, then."

    scene black
    with dissolve2

    i "Nope! You’ve already made up your mind!"
    i "Come, Sensei! Or shall I say — {i}darling,{/i} ala romantic stereotypes that mean nothing to me but make me feel weirdly warm inside now that I say them out loud."

    scene sky
    with dissolve2

    "Hanging out with Io on a date is kind of like...well, the way it always is when I hang out with Io. Just slightly more...cute, I guess?"
    "Which isn’t to say she isn’t normally cute. She’s adorable when she’s not insulting everyone she knows (including herself). "
    "But she’s extra attentive today. And keeps offering me snacks out of a large plastic bag she’s been clutching ever since we left the convenience store."
    "Which — and hear me out here because this is going to sound weird due to the fact that I am attracted to her — makes her feel almost...grandmotherly?"
    "Like, Touka never offers me snacks. Or spends ten minutes on a walk to a secret tunnel talking about the effects of various sleeping pills. "
    "I swear, it’s like Io is one or two steps away from calling me “Sonny Boy” and selling me a membership badge so I can use the community pool."
    "..."
    "Wait, what?"
    "Why did I-"

    play sound "static.mp3"
    scene iodatewar17 with flash
    stop sound

    i "Sensei — you’ve been counting our steps, right?"
    s "Our steps? I thought all I had to do was count the amount of turns we made and stuff."
    i "Yeah, that. Status report, navigator. Your captain has issued a command."
    s "Thirteen lefts and nine rights. Obviously not in that order."
    i "I’ve also been keeping track of that part. But how many-"
    s "Fifteen grates or vents or...whatever it is you want to call them. With the most recent being literally right behind us."

    scene iodatewar18
    with dissolve

    i "Roger! We’re probably getting close then."
    s "To {i}what?{/i}"
    i "The end of the line! Where the new half of town meets the old half and causes a rift in the time and space continuum we can throw ourselves into to become finally happy!"

    scene iodatewar19
    with dissolve

    s "Oh. Well, why didn’t you just say so? A time rift is way better than how dates normally end. And significantly more your speed."
    i "That’d be cool, wouldn’t it? Unfortunately, I am a liar. And I am leading you to a secret location where I can murder you and conveniently dispose of the body."
    s "This day just keeps getting better."
    i "Okay, no more lies this time. There’s a secret room built into the wall with a high-tech keypad that we’re going to crack the code for together."
    s "I thought you said no more lies?"
    i "I did. I’m serious this time."

    scene iodatewar20
    with dissolve

    s "I’m sorry, what?"
    i "Did Uta not tell you about it? I know we promised to keep it a secret, but I figured she would have blabbed to {i}you{/i} since you guys are like, a {i}thing{/i} now and stuff."
    s "We’re not {i}a thing,{/i} Io."
    i "You {i}better{/i} be a thing, Sensei. Because if I find out you’re using my best friend, I will once again be very sad but ultimately not do anything about it."
    i "Like {i}really{/i} sad this time, though. And I’ll probably hate you for a few minutes before caving and convincing myself I don’t."

    scene iodatewar21
    with dissolve

    s "If you’re worried about me using her or something, I can promise that’s not what’s happening."
    s "Uta’s...important, obviously. But I think that she understands just as well as me that I am being pulled in a million different directions and...one of those just happens to be her."

    scene iodatewar22
    with dissolve2

    s "If that upsets you, I get it. But it’s not like-"
    i "Something’s different. "

    stop music fadeout 10.0
    scene iodatewar23
    with dissolve2

    s "I know. That’s what I’m trying to-"
    i "Not with you and Uta. With the tunnel. Be quiet."

    scene iodatewar24
    with dissolve2

    s "..."
    i "..."
    i "Can you hear that?"
    s "I can’t really hear anything. But you know this place better than me, so-"
    i "You’re sure we’ve passed fifteen sewer grates, right?"
    s "I...think so? But keep in mind that I never claimed to be an effective navigator. So if we’ve gotten lost, I think you should take some of the blame for bringing me here."
    i "No, I don’t think we’re lost. I kept the instructions on my phone. There’s just...something different. And I’m not sure what-"

    scene iodatewar25
    with dissolve2

    i "Is that...light? Do you see that?"
    s "A light at the end of a tunnel? Did it cave in on us while we were bickering or something? Are we dead now?"
    i "It’s not just one. It’s..."

    scene black
    with dissolve2
    play sound "escape.mp3"

    i "Come on! Let’s check it out!"
    s "Io, don’t run. It’s dark in here and I don’t want to have to carry you out if-"

    play sound "static.mp3"
    scene iodatewar26 with flash
    stop sound
    play music "ichiyarakka.mp3"

    s "If..."
    i "Holy shit..."

    "Right there in the middle of the tunnel is a ledge, haphazardly marked with several small street barriers as if it {i}doesn’t{/i} just suddenly descend into nothing but a sea of black."
    "From out its depths crawl thousands of dust particles, illuminated and brought to life by the light of the sun, falling endlessly from a separate abyss extending above."
    "I can hear water. I can hear air. I can hear everything. But at the same time, there’s an inescapable, terrifying silence that finds its way between Io and me."
    "The two of us feed that silence in our confusion, left to do nothing but stand there and gawk at one more inexplicable feat of this even more inexplicable city."
    "Just {i}I{/i} am used to this. And {i}she{/i} is-"

    i "This..."
    i "Is so..."

    scene iodatewar27
    with dissolve

    i "Fucking cool!"
    s "We encounter an endless pit of darkness in the middle of a tunnel, coming one or two steps from falling into it, and your response is to call it {i}cool?{/i}"

    scene iodatewar28
    with dissolve

    i "Fuck yeah it is! Who gives a shit about a secret door with a dumb keypad when we’ve found the edge of the friggin’ world?!"

    scene iodatewar29
    with dissolve

    i "Don’t jump in, though. And don’t push me either. I was only joking when I talked about hiding your body. I swear I didn’t know this was here."

    scene iodatewar30
    with dissolve

    i "This is so weird, though. I’ve been down here with Uta tons of times and we’ve never seen anything like this. It’s almost like the tunnel is-"
    s "Changing?"
    i "Yeah..."

    play sound "static.mp3"
    scene iodatewar31 with flash
    stop sound

    i "But if that’s the case, what are these barrier things doing here? Don’t they indicate that someone knows about this?"
    s "Construction maybe? "
    s "New businesses are popping up all over the place. Maybe one of them was connected to the tunnels and-"
    i "No, that wouldn’t explain how deep it is. The only thing that would-"

    scene iodatewar32
    with dissolve

    i "Ah! Sensei! Do you know what I think this is?!"
    s "A rift in the time and space continuum that we can throw ourselves into to become happy?"
    i "No! But you’re close!"

    scene iodatewar33
    with dissolve

    i "I think this might be the sinkhole that swallowed the school Uta and I transferred in from."
    s "I don’t really see how that’s close, but okay."
    i "It’s close because it’s a crack in reality! Something that {i}shouldn’t{/i} happen, but did. "
    i "No one expects an entire school to just disappear, just like no one expects a rift that grants happiness to open up somewhere in the sky or wherever it is rifts form."
    s "Well...if it is, what does that mean? "

    scene iodatewar34
    with dissolve

    i "That I can finally get my old pencil case back!"
    s "Io, please don’t tell me you’re actually planning on jumping into a giant hole that disappears into nothingness."
    i "Jumping? No. We just need a lot of rope."
    s "Please don’t venture into the sinkhole. This is a formal request from your former teacher."

    scene iodatewar35
    with dissolve

    i "Aww, Sensei. I’ve always wanted someone to be worried enough about me to ask me not to jump into a bottomless pit."
    s "Well, if it’s actually the sinkhole that claimed your school, it {i}would{/i} have a bottom. Right?"
    i "Oh, you know what I mean."

    play sound "static.mp3"
    scene iodatewar36 with flash
    stop sound

    i "What do we do now, though? Like, we’re obviously not the first ones to find it based on the barriers. But I can’t just {i}ignore{/i} something as cool as this. "
    s "So...what? You want to keep investigating?"
    i "I say we regroup. We’ll return to the surface and enlist the help of Uta to go scream into the sinkhole from the top and see if we can hear her from down here."
    s "Do they not have the hole blocked off up there?"
    i "They do. But we’ve snuck into plenty of stuff we’re not allowed into. It’s one of the ways we bond."
    s "You do realize I still have another date after this, right?"
    i "You do realize that no date you could ever go on after this one will possibly live up to the wonder of a giant hole, right?"
    s "The giant hole is only a wonder at all because I got to see it with you."
    i "I still think it’d be pretty cool even if I were by myself right now."
    s "Then I guess that just means I like you more."
    i "I respectfully disagree. "
    i "Actually, no. I disrespectfully disagree. I think you are wrong and dumb and that I like you more. And I will not apologize for this assessment of our relationship."
    s "Oh. Okay."
    i "Also, you should kiss me."

    scene iodatewar37
    with dissolve

    s "Like...now?"
    i "Yeah. I’m jealous that Uta gets to and I don’t. "
    i "But I also understand if you’re disgusted by the idea of doing something like that with me since you won’t be my first. "

    scene iodatewar38
    with dissolve

    s "That doesn’t disgust me, Io."
    i "It should. "
    i "But you can take solace in the fact that this will be my first {i}consensual{/i} kiss if that helps wash away any of the grossness."
    s "There’s nothing gross about you."
    i "Yes there is. "
    s "No...there’s not."
    i "I respectfully disagree. "
    i "Actually, no. I disrespectfully disagree. I think you are wrong and dumb and that I am damaged beyond repair. "
    s "That statement implies I want to fix you."
    i "Do you not?"
    s "No. I fear that “fixed” Io would be unrecognizable, so I’m willing to accept whatever spare pieces and parts this one has left to offer."
    i "They are yours if you will have them. But I would like to ask for something of yours in return, if that’s okay."
    s "And what is it you would like?"
    i "I don’t know yet. "
    i "And to be honest, I’m not sure I ever will. So don’t be surprised if I continue to ask for something new every day for the rest of eternity. "
    i "Or at least until one of us falls into the sinkhole."

    scene iodatewar39
    with dissolve2

    s "Are you really sure you want to do this?"
    i "No."
    s "Should I...stop then?"
    i "No."
    s "I am receiving mixed signals here that I feel like I shouldn’t ignore based on your history."
    i "Frankly speaking, Sensei, I’d like to forget basically all of my history that doesn’t involve you or Uta. "
    i "And, assuming that’s possible, I think having my “first” kiss in front of a bottomless pit sounds like a pretty great memory and the perfect end to an {i}actual{/i} first date."
    s "I still feel like this is wrong and that I should give you more time."
    i "Okay. I’ll just do it myself then."
    s "You’ll-"

    play sound "static.mp3"
    scene iodatewar40 with flash
    stop sound

    s "Mmf?"
    i "Chu...chu...chu..."

    scene iodatewar41
    with dissolve2

    "I melt into her."

    i "Heheh...chu...heh..."

    "But she starts...laughing?"

    scene iodatewar42
    with dissolve

    s "Um..."
    i "Hm? Why’d you stop?"
    s "People don’t normally laugh."
    i "Really? It kind of tickles. Kissing like this."
    i "Plus, you look dumb when you have to crouch down like that. It’s cute."
    s "Io-"
    i "Keep going. I want more."

    "{i}Hah...{/i}"

    scene iodatewar41
    with dissolve2

    "I melt again."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "And all I am drips slowly from the ledge that leads into a sea of nothing."

    $ renpy.end_replay()
    $ io_love += 10
    $ dormwarsfiveio1 = True

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump dormwarsfiverin1
