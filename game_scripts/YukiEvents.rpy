label yukibar:
    if yuki_love >= 25 and yukidate20p2 == True and day > 4 and day < 7 and yukidate25 == False:
        jump yukidate25
    if chap4active == True:
        jump yukispringbargen
    if chapthreeactive == True:
        jump yukisummer2bargen

label callyukimorning:
    if yukiblock == True:
        "I tap on Yuki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callmorning
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callmorning

    play sound "phonebeep.wav"

    "I tap on Yuki's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    "There's no answer."
    "Guess I'll call someone else."

    jump callmorning

label callyukiafternoon:
    if yukiblock == True:
        "I tap on Yuki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callafternoon
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callafternoon
    if chap4active == True:
        jump yukispringnoongen
    else:
        play sound "phonebeep.wav"

        "I tap on Yuki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callafternoon


label callyukinight:
    if yukiblock == True:
        "I tap on Yuki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callnight
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callnight

    if yuki_love >= 0 and streets30 == True and ramen20 == True and yukidate1 == False:
        jump yukidate1
    if yuki_love >= 5 and yumidorm30 == True and yukidate1 == True and yukidate5 == False:
        jump yukidate5
    if yuki_love >= 10 and yukidate5 == True and kirindorm25 == True and yukidate10 == False:
        jump yukidate10
    if yuki_love >= 20 and nikilovesyou3 == True and day == 5 and yukidate20p1 == False:
        jump yukidate20p1
    if chapthreeactive == True:
        "Yuki should be at work right now. I can probably see her if I go to the bar."
        jump callnight
    else:
        jump yukigennight

label yukigennight:
    play sound "phonebeep.wav"

    "I tap on Yuki's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    yu "Yo."
    s "Hey. Are you free tonight?"
    yu "Free every night. This mean what I think it means?"
    s "Does what you think it means involve a sketchy ramen joint?"
    yu "Always does."
    yu "You there now?"
    s "No, but I'll start heading over now if you want to meet up."
    yu "Sounds good."
    yu "Want me to order for you since you're a bike-fearing pansy without a license of your own?"
    yu "I'm obviously gonna get there first, so..."
    s "..."

    play sound "phonebeep.wav"

    "I hang up the phone after not hearing whatever Yuki was saying at the end there."
    "I'm pretty sure she was going through a tunnel."
    "I'll just take my time and walk over to the second half of town at the same speed I always do."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yukigennight
    with dissolve
    play music "kashiwagi.mp3"

    "I arrive at the ramen shop to find Yuki already halfway through her meal and quickly order the same thing in an effort to catch up."
    "We spend the night discussing the past, present, and future and how none of those sections have been all that enjoyable for either one of us."
    "Sure, my present is a lot better than hers right now given that I'm actually able to spend time with her daughter-"
    "But it's not like that time ever yields anything worth noting."
    "We're just cogs in a machine that we can't even figure out the function of, and my cog happens to be a little bit larger."

    scene black
    with dissolve

    "But that's okay."
    "Because one day, the machine will stop functioning entirely."
    "The parts of my section will be disassembled for the sake of renovating another machine-"
    "While the parts of hers will be discarded or turned into scrap metal."
    "Yuki and I finish our meals and head our respective ways without making any serious progress as far as our relationship goes."
    "But at least we seem to have enjoyed the time we spent together."

    $ yuki_love += 1
    stop music fadeout 5.0

    "{i}Yuki's affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yukidate1:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I haven’t really seen her at all since our last run-in at the bathhouse, and it definitely seemed like she had some things to...discuss with me."
    "Granted, it’s possible she just wants to drag me into an alley and beat me up. "
    "And I’m pretty sure she could since she wears a leather jacket."

    s "..."

    "If you can’t tell, I may be slightly nervous given how horrible I am at dealing with Yumi’s temper...and this is the woman who started it all."

    play sound "phonebeep.wav"

    yu "Yeah?"
    s "Hey. "
    yu "Hey. "
    yu "Who’s this?"
    s "It’s...your daughter’s teacher."
    yu "Oooooh, shit. I was startin’ to think I’d never hear from you."
    yu "You hungry? Dinner offer’s still on the table."
    s "Does accepting make this a date?"
    yu "Pfft. Yeah, right. "
    yu "I haven’t been on a date in ten fuckin’ years. "
    yu "Just think of it as payment for bothering the shit out of you for a little while."
    s "That sounds significantly less fun. But I’m in, I guess."
    s "Tojo Ramen?"
    yu "Yeah. Need a ride?"
    s "You drive?"
    yu "I’ve got a bike I could swing by on."
    s "Oh."
    s "Yeah, I’ll walk. I’m not a fan of motorcycles."
    yu "What?"
    yu "You fuckin’ scared or something?"
    s "Nope. Not scared at all."
    s "See you soon, Yuki."
    yu "Uh-huh. Don't forget to tell your mom you’re going to be out late-"

    play sound "phonebeep.wav"

    "I hang up the phone before Yuki begins to talk about how brave and manly I am, a thing she was definitely about to do."

    scene black
    with dissolve
    play music "kashiwagi.mp3" fadein 10.0

    "I walk deeper into the winter winds, heading toward the old district with my hands buried inside of my pockets."
    "It will be nice not having to pay tonight, sure."
    "But I wonder how a conversation between Yuki and me could possibly go?"
    "........."
    "......"
    "..."

    scene yukifirstdate1
    with dissolve

    yu "Yo. "
    yu "Sure took your sweet ass time gettin’ here."
    yu "The bike probably doesn’t sound so scary now, huh?"
    t "Hello and welcome to Tojo Ramen. Is it your first time here?"
    s "Tsuneyo, I’m here all the time."
    t "Fuck you."
    s "..."

    "Well that's one way to greet someone, I guess."

    yu "So...you two are still {i}fucking{/i} each other, I see."
    s "I am very glad that she cleared up that misunderstanding with you instead of me."
    yu "Same. "
    yu "Weird experience, walkin’ in to get dinner and seeing the waitress and your daughter’s teacher talkin’ about boning."
    t "What is “boning?” This is one more term I am not familiar with."
    s "Don’t worry about it, Tsuneyo. "
    s "In fact, why don’t you stay out of this conversation entirely? I’m here to talk with Yuki."
    yu "Ooooh, look at you sounding all serious."
    s "Well, that’s why we’re meeting up, right?"
    s "Since you made it clear that it’s not a date, I mean."

    scene yukifirstdate2
    with dissolve

    yu "Well, yeah. But that doesn’t mean we’ve gotta act like we're holdin’ a fuckin’ meeting or something."
    yu "Just eat, drink, and talk. "
    yu "Pretend we’re friends or something. I don’t give a shit."
    yu "Long as neither one of us makes this weird, it’ll wind up being easy as hell."
    s "What will wind up being easy, exactly?"

    scene yukifirstdate3
    with dissolve

    yu "Gettin’ a progress report on my daughter, numbnuts. "
    yu "How’s she doing? Beat the shit out of anybody yet? Any teachers?"
    yu "Wait, wait. You’re probably scared of me because she fucked you up already, didn’t she?"
    s "Uhh...no. That is not a thing that has happened."

    if bonus == True:
        yu "Well if you’re not boning her and she ain’t doing shit to you, how come you two are hanging out together after[school]?"
    else:
        yu "Well it could. You're a fucking pussy and she would kick the shit out of you."
        s "That was not necessary, Yuki."

    s "You know, I had a feeling Yumi would be the topic of conversation tonight, but I can’t say I was expecting the world’s most informal PTA meeting."
    t "Your daughter has a very unique attitude. "
    t "I believe she would make an exceptional drill sergeant. "
    s "Tsuneyo."

    scene yukifirstdate4
    with dissolve

    t "Ah-"
    s "Let me handle this, please."

    scene yukifirstdate5
    with dissolve

    yu "I just fuckin’ said that we don’t need to treat this like a meeting."
    yu "I really just want to know how she’s doing."

    if bonus == True:
        yu "And also whether or not we need to have a {i}talk{/i} about you getting closer to her than someone in your “position” probably should be."
    else:
        yu "And also if you're adequately teaching her algebra and shit."

    s "You say that as if I’m not a model teacher."

    scene yukifirstdate6
    with dissolve

    yu "Well, if what Io tells me is true, you definitely aren’t."

    if bonus == False:
        s "Io is a bitch. Don't listen to her."
    else:
        yu "But I also don’t think Yumi would be dumb enough to go after someone your age, so I’m curious about what’s going on."
        yu "And it’s not like I can ask her myself. "
        yu "You saw how she reacted the last time we ran into each other."

    "I sit down at the table and realize that I’m already too deep into this topic to be able to order any food without killing the momentum."
    "I guess I’ll just have to go with the flow until Tsuneyo realizes that I am also a human being who needs to eat in order to stay alive."

    s "Yumi is...definitely a student."
    yu "..."
    s "..."
    yu "Is that it? That’s all you’re gonna give me?"
    yu "Of course she’s a fucking student. What else?"
    s "Can I ask why you want to know all this? "
    s "It just seems a little weird for you to start showing concern out of nowhere after all I’ve heard from her about you."

    scene yukifirstdate7
    with dissolve

    yu "And what did you hear from her?"
    yu "That I’m a shit mother and a junkie and that I used to beat her or something?"
    s "She definitely didn’t mention that last part."
    s "That’s not something you actually did, is it?"

    scene yukifirstdate8
    with dissolve

    yu "No! She’s my kid! I’d never fuckin’ do something like that!"
    yu "Can’t even tell you how many people I had to fuck up for just makin’ her cry."
    yu "It was like, a whole fuckin' thing back when I was still hangin’ around that place."
    yu "The second Yumi would start crying, everyone would book it because they were all afraid they’d have to answer to me."
    s "And the other stuff? The drugs and the...abandonment?"

    scene yukifirstdate9
    with dissolve

    yu "That..."
    yu "Yeah. She wasn’t lyin’ about that."
    yu "Kind of surprised she didn’t start saying anything worse, though."
    yu "Thought for sure she’d make me out to be fuckin’ Satan reincarnated by now."
    s "Well you’re certainly no angel."
    yu "Yeah, yeah. I’m a bad fucking parent. You think I don’t know that?"
    yu "But that doesn’t mean I don’t want to know how she’s doing."
    yu "Just to check in and shit. "

    if bonus == True:
        yu "She’s around the same age I was when everything started fallin' apart, so it’s...nice seeing that she’s not completely fucked up yet."
        s "What exactly happened to you when you were her age?"
    else:
        yu "She's startin' to act like Bigfoot back when I used to track him."
        s "Tell me more about that."

    scene yukifirstdate10
    with dissolve

    yu "That’s a story for another time. "
    yu "You’ve been chill so far, so I wouldn't mind talkin' about it. Just not today."

    if bonus == False:
        s "But I need to know where he is so I can blog about it."

    yu "All you {i}really{/i} need to know is that I ain’t doin’ that shit anymore."
    yu "Not like I expect it to change anything at this point, but yeah."
    yu "Either quit now or wind up in a fuckin' dumpster, you know?"
    s "Not really. I can’t say this is an area I have much experience with. "
    yu "Oh, good. Thanks for reminding me that my life is shit and everyone else’s is so much better."
    s "..."
    yu "..."

    scene yukifirstdate11
    with dissolve

    yu "Dude, it’s a joke."
    s "Your delivery is somehow just as bad as Tsuneyo’s."

    scene yukifirstdate12
    with dissolve

    t "It’s true. But I have only been associating with people for several months now."
    t "You have no excuse. Please stop trying to be funny."
    yu "Jesus Christ, sorry. Didn’t realize everyone here was so dead inside."

    scene yukifirstdate13
    with dissolve

    yu "So, you said before you were helping her find a job or some shit, right?"
    yu "How’s that going? Anyone bite yet?"
    s "Not yet. But it’s not like she’s particularly...adept when it comes to job interviews."
    yu "What’s that mean? She ain’t qualified or some shit?"
    s "More like she threatened to beat the shit out of customers who stole from the store during one of her last interviews."
    yu "..."
    yu "And?"
    s "And that’s not a thing you can really say during a job interview."
    yu "Well, why the fuck not? Think showin’ that level of dedication would be a huge plus for managers and shit."
    yu "I’d hire her."

    "Well, she is definitely Yumi’s mother, if not anything else."

    s "Let’s look at things this way...what was your first job?"
    yu "Uhh...my parents owned a candy shop when I was little. "
    yu "I kind of helped out there until I was a [teenager], I guess."
    s "I don’t think helping out parents really counts. What about the first job you had as a [teenager]?"
    yu "Oh. None."
    s "None?"
    yu "Nah. "
    yu "I was one of those “This town is boring. I’ve gotta get away.” kind of girls."
    yu "So I left when I was in [high_school] and fell in with some gang."
    yu "Just chilled with them for a few years until I met Yumi’s dad and then mooched off of him after that."
    yu "Fucking lowlife, by the way. She tell you about him, too?"
    s "Just that he’s in the yakuza. "
    s "She hasn’t mentioned that much about either one of you, to be honest."
    s "The two of us aren’t exactly friends."
    yu "Does she have {i}any{/i} friends? Can’t imagine it’s easy makin’ any given her upbringing."
    s "One. "
    s "Well, one and a half."
    yu "How the fuck can you have half of a friend?"
    s "It’s her friend’s little sister. Yumi looks after her sometimes."

    scene yukifirstdate14
    with dissolve

    yu "{i}Yumi{/i} does?"
    yu "Like, {i}my{/i} Yumi? Looking after a kid?"
    s "Yeah. "
    s "She’s surprisingly good at it, too."
    yu "Well isn’t that a fuckin’ steaming pile of irony."
    yu "You gonna tell me she’s running a charity next, too?"
    s "No. But she {i}does{/i} steal and resell old TV’s in order to feed herself."

    scene yukifirstdate15
    with dissolve

    yu "There we go. There’s that good ole entrepreneurial spirit."
    yu "Must be takin’ after her grandpa."
    yu "Pretty soon, she’ll have her own fuckin’ candy store for some other little rebel to come steal from."
    yu "The cycle fuckin’ continues."
    s "This is a strange thing to seem proud about."
    yu "Hey, she’s out there trying to build something for herself. ‘Course I’m gonna be proud."
    yu "Think I’d have these bags under my eyes if I did the same thing at her age instead of just fallin’ in with some punks and livin' the easy way?"
    s "That is a weirdly positive way to look at things, but I’m pretty sure I agree."

    scene yukifirstdate16
    with dissolve

    yu "Shit, man. Her own business."
    s "I...don’t know if I’d call it a {i}business{/i}-"

    "Yuki remains silent for a few moments and I get caught up in watching the smoke trail off of her cigarette, only to be sucked up by the hoods of Tojo Ramen."
    "She seems strangely content right now. More content than a normal woman would be after learning her child is a semi-professional shoplifter."
    "But hey, with so many horrible things on this planet, I guess it wouldn’t be right to look down on anyone for managing to siphon some joy out of something slightly {i}less{/i} horrible."
    "I do wish that I didn’t feel compelled to ask things like this, though-"

    s "Do you want to see her again?"

    scene yukifirstdate17
    with dissolve

    yu "Huh?"
    s "If she agreed to it, would you want to meet up with her?"
    yu "..."
    s "I’m pretty sure Yumi doesn’t know you’re sober. "
    s "Maybe it would change things if she figured out you were trying to be a better person?"
    yu "..."

    scene yukifirstdate18
    with dissolve

    yu "That’s not what this was about, man."
    yu "I wasn’t planning on getting to know you so I could find a way back into my daughter’s life or some shit."
    yu "I just wanted to check in on her."
    yu "Make sure she’s not still hangin’ out with all those yakuza punks and shit."
    yu "You can’t just run out on your kid and then expect to walk back into the picture after gettin’ a little better."
    yu "That’ll fuck ‘em up even harder once things get bad again."
    s "Do you think there’s a chance things will get bad again?"

    scene yukifirstdate19
    with dissolve

    yu "Heh."
    yu "You don’t deal with people like me often, do you?"
    s "I can’t say I do, no."
    yu "Rule #1 - Things can {i}always{/i} get bad again. "
    yu "Doesn’t matter how fine I look now or how fine I look tomorrow. "
    yu "The day after that, somethin’ could snap and I could wind up in a bag."
    yu "Goal is just makin’ it through each day so you can start fresh on the next one or whatever other “enlightened” shit they’re preaching in NA nowadays."
    yu "Just the way things work, unfortunately."
    s "And here I thought {i}I{/i} was the one who didn’t want to make an effort to change anything."
    yu "Oh, shit...if only it were as easy as just “making an effort.”"
    yu "Listen, man. You can say whatever the fuck you want. I’ve heard it all before. "
    yu "But I’ll tell you the same thing I tell everybody else-"
    yu "It’s not that simple."
    yu "I really wish it was."
    yu "But it’s not."

    scene yukifirstdate20
    with dissolve

    yu "I’d be happy to meet up with her if she wanted to. "
    yu "But I’m not asking you to try and make shit like that happen when she has bigger fish to fry."

    scene yukifirstdate21
    with dissolve

    t "Did I hear fried fish?"
    t "Are you ready to order?"
    s "Just...give me the same thing Yuki is having. "
    t "There’s no fish in that at all. Are you sure this is what you want?"
    s "Give me literally anything, Tsuneyo. I’m starving."
    t "I understand. "
    t "I will go get you one of everything."
    s "That’s not-"

    scene yukifirstdate22
    with dissolve

    s "And she’s gone."
    yu "You expect anything else? She’s a fuckin’ weird kid."
    s "They all are. Everyone in my class."
    yu "Sorry to put you on the spot, but...you really think Yumi would want to see me again now that I’m not all...fucked up?"
    s "I have no idea what Yumi wants literally ever. But I don’t think it would hurt to ask."
    yu "Well...again, I’m not askin’ you to go out of your way for something like that."
    yu "I’m fine just hearing she’s doing okay. "
    yu "But...I ain’t gonna try and stop you."
    yu "I know how fuckin’ hardheaded guys get when they think about doin’ something."
    yu "And...yeah, I guess I {i}do{/i} kind of want to see that brat."
    yu "Don’t say anything to Io about it, though. Girl’s weirdly attached to me for whatever reason."
    yu "Don’t want her to get jealous and wind up gettin’ the shit kicked out of her after starting something with Yumi."
    s "I will...definitely not mention anything to Io."
    s "And I’ll think more about saying anything to Yumi, too."
    s "It just feels strange meeting up with you to give you a progress report when A: I hate progress reports. And B: This is the first time we’ve ever really {i}talked{/i}."

    scene yukifirstdate23
    with dissolve

    yu "Well, hey. You’ve got my number now, so you can call whenever you want."
    yu "Can’t guarantee you’ll like hangin’ out with me at all. But it’s kinda nice havin’ somebody to talk to in a place like this, you know?"
    yu "Also, the food’s fuckin’ great and Tsu-chan is hilarious."
    t "Ah-"

    "A gasp rings out from the kitchen and the sound of a metal pan being dropped rings throughout the ramen shop."
    "It’s hard to tell if this is the result of Tsuneyo’s name being said (Albeit in short form) or if she’s just shocked that someone has acknowledged her...rare form of comedy."

    scene black
    with dissolve2

    "Tsuneyo reappears and serves me the same bowl of ramen that Yuki has."
    "We eat our respective dinners and, just as she promised, Yuki winds up paying for me."
    "I still have no idea how I should progress with the Yumi situation, but it’s good knowing that things aren’t even half as bad as I thought they were at first."
    "Or, who knows? Maybe they are?"
    "I can’t imagine what it’s like being in either of their shoes."
    "So all I can really do now is just pull on every lever and press every button I can find until something happens."
    "So basically, life."
    "Yuki offers to give me a ride home but, once again, I decline."
    "Not because I am afraid of motorcycles-"
    "But because I am afraid of how much hope I may have given her for something that will likely never happen."

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate1 = True
    stop music fadeout 5.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukidate5:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I don’t exactly call bearing great news or anything like that, but since Yumi seems adamant about keeping her distance, I should at least let Yuki know."
    "I’m sure she was expecting as much anyway."
    "I’m foolish for expecting anything else."

    play sound "phonebeep.wav"

    yu "Yo. Sup?"
    s "Hey. Are you doing anything tonight?"
    yu "Nope. If I answer, just assume I ain’t doin’ shit. "
    yu "Want to meet up at the usual spot?"
    s "Are you paying again?"
    yu "Ha. Not a chance."
    yu "That was a one-time only thing, pal. Don’t have enough to be buying dinner for you every time we meet."
    yu "Aren’t you a fuckin’ teacher anyway? Figured you’d be pretty much loaded or some shit."
    s "Teachers don’t make as much as you think they do."
    yu "That so? Sucks."
    yu "We’ll just buy our own shit then."
    yu "I’m close, so I’ll just wait for you there."
    s "Not going to offer to give me a ride again?"
    yu "And waste my gas on someone who ain’t even buyin’ me dinner? Nah. You’re walking."
    yu "See you soon."

    play sound "phonebeep.wav"

    "Yuki hangs up before I have the chance to retort and I quickly find myself shoving my hands back into my pockets and setting course for Tojo Ramen."
    "Tonight, I’m going to upset someone."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Well, probably at least."
    "But I seem to inadvertently do that pretty often."
    "Does something like this still count as inadvertent if it’s a situation that I manufactured entirely on my own?"
    "Or do I need to rely on a term like “accident” and fall back on the hope that her own low expectations will act as a cushion for this poor turn of events?"
    "There is only one way to find out."
    "........."
    "......"
    "..."

    scene yukioutside1
    with dissolve2
    play music "thingsthathurt.mp3" fadein 5.0

    yu "Yo."

    "I turn the corner to find Yuki waiting outside of Tojo Ramen and make my way over to her."
    "I can smell cigarette smoke clinging to her jacket like her daughter clings to the hole inside of her heart."
    "A hole so big she can fit her fingers through it."
    "And, if she cares enough about her future, she might even have the chance to suture it back together."
    "Of course, there’s no chance it will ever work as well as the original version- the one that still had a mom."
    "But a heart is a heart."
    "Even if it’s ripped into pieces."

    s "Why are you out here? It’s freezing."
    yu "Is it?"
    yu "The cold never bothered me much, I guess."
    yu "But I imagine all those days of sleepin’ outside probably have somethin’ to do with that."
    yu "If you want to go in, we can. Just figured it’d be easier to talk out here."
    s "But Tsuneyo always has so much to add to the conversation."

    scene yukioutside2
    with dissolve

    yu "Hey, now. Leave the kid alone. She’s trying her best."
    yu "I didn’t even know she left this fuckin’ place until recently."
    s "Probably because she {i}didn’t{/i} leave this place until recently."
    yu "Then you should damn well know to cut her some slack. Unless you want to answer to me, of course."
    s "Are you threatening me now?"
    yu "I’ve got a history of lookin’ out for kids when I’m not too busy abandoning ‘em."
    s "Correct me if I’m wrong, but weren’t you in a biker gang?"
    yu "The fuck you think biker gangs do? Ride around and beat the shit out of people for no reason whatsoever?"
    s "..."
    s "Yeah. Pretty much."

    scene yukioutside3
    with dissolve

    yu "Yeah, well...you’re definitely not alone in thinkin’ that."
    yu "It’s a little more complicated, though."
    yu "Gangs for a lot of people are like families."
    yu "A place you can run away to and...start over, I guess."
    yu "Like a whole ass support group for people who fell on tough shit, lost their way, or just want to try something different."
    yu "People like me."
    s "Well that doesn’t sound intimidating at all."

    scene yukioutside2
    with dissolve

    yu "What, you scared of me or somethin’?"
    s "Not anymore now that I know you’re just a babysitter in a leather jacket."
    yu "Good. Means I don’t have to tell you about what happens to anyone that messes with people I care about."
    s "And now I’m back to being intimidated."

    scene yukioutside4
    with dissolve

    yu "Shit. Was {i}this{/i} close to havin’ somebody around who doesn’t think I’m some kinda scumbag."
    s "What about the rest of your...people? Or whatever gang members are called."
    yu "Most of ‘em are gone by now."
    s "Oh. "
    s "Well...I’m sorry to hear that."
    yu "Not {i}gone{/i} gone. Like they moved somewhere else and shit. Before the city closed up."
    yu "Not like I can follow after ‘em now."
    s "Why ever leave in the first place?"

    scene yukioutside5
    with dissolve

    yu "Good fucking question."
    yu "Answer is simple enough, though."
    yu "You ever meet someone who you think can turn your life around only to find out later that getting to know them made everything ten times worse?"
    s "I...don’t think so?"
    yu "Lucky."
    s "That’s what happened to you, I’m guessing?"
    yu "Yup."
    yu "Teenage girl. Poor as shit. Only one outfit to my fuckin’ name. Relyin’ on other girls in the gang just so I could eat a few nights a week."
    yu "Then along come these dudes who think they’re tough shit for walking up on some tiny ass runaway out by herself at night."
    yu "Cornered me. Pushed me to the ground. Fucked up my only shirt."
    yu "And then I bashed their fucking brains in with a loose pipe I pulled off the side of some building."
    s "The way this story began, I had the feeling that someone was going to come rescue you or something."

    scene yukioutside6
    with dissolve

    yu "Nope. The complete opposite, actually."
    yu "The guy I’m talking about, Yumi’s dad, was one of those fucking punks."
    yu "Granted, he never laid a finger on me. Just cowered in the corner while I fucked his stupid ass goons up."
    yu "But, after all that was done, he came up to me and started sayin’ all this shit about how he’d never seen a girl so strong before. "
    yu "Offered to buy me new clothes. Said he wouldn’t rat me out and shit and that all those guys were scum anyway."
    yu "Just...kept spittin’ out all these nice words that I couldn’t even process because I was still high off adrenaline."
    yu "In hindsight, he was probably just fuckin’ fearing for his life."
    yu "But when you’re a runaway without a penny to your name and some dude in nice clothes pulls out his wallet and starts offering to buy you shit, it’s hard to just fuckin’ walk. You know?"
    yu "Like, what if he was my ticket out?"
    s "So you...went home with some guy who was going to just sit there and watch a bunch of other guys do god knows what to you?"

    scene yukioutside7
    with dissolve

    yu "I was a fuckin’ naive [teenage]girl who’d never seen so much money before. "
    yu "Plus he was kind of cute, I guess."
    yu "So it was either take a chance on him, a dude I knew I could fuck up if he tried anything on me-"
    yu "Or wander back to my crew with my tits basically hangin’ out of my shirt without any idea of when I’d be gettin’ a new one."
    yu "Easy choice then and there. But {i}fuck{/i} if it's not the biggest regret of my life."
    s "And here I was thinking Yumi’s dad was some intimidating mob boss."

    scene yukioutside8
    with dissolve

    yu "Intimidating? That piece of shit? Not a chance."
    yu "There are some people who work for power and some people who are just born with it."
    yu "Which one do you think he is after hearing all that?"
    s "I’m pretty sure I can guess, but..."
    s "I’m still not really getting why you wound up staying with him if he was so horrible."

    scene yukioutside9
    with dissolve

    yu "What part of “he was fucking loaded” do you not understand?"
    yu "I could eat. Get high. Sleep in an actual futon. "
    yu "And, shit...I could even afford to dress nice when I wanted to."

    if bonus == True:
        yu "And all I had to do was suck his tiny fucking cock every once in a while in order to keep doing all that."
    else:
        yu "And all I had to do was read him bedtime stories and tell him everything was going to be okay in order to keep doing all that."
        s "That sounds nice."

    yu "Shit went on for years."

    if bonus == True:
        yu "Wasn’t a bad gig at all until he fuckin’ took advantage of me while I was high out of my mind one night."
        s "..."
        s "Is that..."
    else:
        yu "Wasn’t a bad gig at all until the stork came."
        s "So {i}that{/i} is how Yumi happened."

    scene yukioutside10
    with dissolve

    yu "Yup."
    yu "Was so fuckin’ out of it that it took me two months to even realize I was knocked up."
    yu "Guess you can probably figure out what happened after that."
    s "Does Yumi know all this?"

    scene yukioutside11
    with dissolve

    yu "No. And you’re not going to fucking repeat a word of it to her either, got it?"
    yu "It’s bad enough that she had to pop out of {i}me{/i}. You have any idea how much it would fuck her up to hear how it actually happened?"
    s "But something like that might completely change her outlook on-"
    yu "And what if it did?"
    yu "Think we’d be able to just start over after she finds out she was never planned?"
    yu "Think it will excuse all of the times I passed out while watching her?"
    yu "Will it excuse me leaving?"
    s "..."
    s "No."
    s "It won’t."

    scene yukioutside12
    with fade

    yu "She was such a cute fucking kid. And I fucking hate babies. They never shut the fuck up."
    yu "Do you want to know what her first word was?"
    s "I’m guessing “Mama?”"
    yu "What? No. Her first word was “Fuck.”"
    yu "Shit was hilarious."
    s "I am somehow not at all surprised by this."

    scene yukioutside13
    with dissolve

    yu "I’m assuming you talked to her about meeting up with me, right?"
    s "..."
    s "It didn’t exactly go well."
    yu "I didn’t think it would."
    yu "Thanks for trying, though. "

    if bonus == True:
        yu "Probably the first guy I’ve ever met who’s done something for me without trying to get into my pants."
        yu "But I’m still not convinced you’re not fucking my daughter. So you’re probably pretty satisfied in that area already."
        s "Uhh..."

    scene yukioutside14
    with dissolve

    yu "God, she’s so fucking pretty now."
    yu "She looks nothing like me either. Good for her."
    s "You have the same eyes at least."

    if bonus == True:
        yu "Yeah but her tits are like two sizes bigger than mine and she’s not even half my age. The fuck is that about?"
        s "I’m still slightly intimidated by you, so I’m going to try and refrain from commenting on your [teenage]daughter’s breasts."

        "That does not mean I won’t think about them, though."
        "They are...very nice."

    scene yukioutside15
    with dissolve

    yu "Whatever you two are doing together is fine. I don’t care."
    yu "Like I said, you seem like a good guy. And it’s not like I’m a good judge of character anyway."

    if bonus == True:
        yu "Just wear a fucking condom so she doesn’t also wind up pregnant before she’s ready."
        s "Okay, let’s talk about something else now."
        yu "Nah, fuck that. Not until you agree to the condom thing. "
        s "I agree to the “condom thing.” Now please stop talking about my entirely wholesome and not-at-all suspicious relationship with your daughter."

    yu "So, now what then? "
    yu "You done hangin’ out with me now that you know Yumi’s not gonna be involved?"
    s "I was actually thinking of asking you the same thing."
    s "You’re the one who wanted to check in on her and have made it very clear that our meetings aren’t dates. "
    s "I just figured you wanted to probe someone close to her for info without really getting in the way."
    yu "Well, yeah. That’s definitely true."
    yu "You’re alright, though. We can still chill if you want. "
    yu "Not like I ever have anything to fuckin’ do."
    s "No dates, though?"

    scene yukioutside16
    with dissolve

    yu "The fuck is it with you and all this dating shit? "

    if bonus == True:
        yu "There are like thirty different [teens] trying to jump your bones and you’re hitting on a recovering addict in her late 30’s. "
        s "I hit on virtually everyone. I’m sure you’ll get used to it."
        yu "We’ll see about that."
    else:
        s "I just want to feel loved."

    yu "I’m kind of staying out of the game for now, though."
    yu "As you’ve heard, my track record with men is kind of shit. "
    yu "I’m better off stayin’ a loner. And {i}you’re{/i} better off not gettin’ involved."
    yu "‘Specially since my daughter would kick your fucking ass if she found out we were together right now."
    s "I’m going to keep this hidden from her at all costs. Don’t you worry."
    yu "Appreciated."

    scene yukioutside17
    with dissolve

    yu "Oh, and sorry for dumping all of that shit on you tonight."
    yu "I realized halfway through that I was ventin’ to some dude who probably did not give two shits, but it’s been a long time since I’ve actually been able to say any of that."
    yu "Only other person in Kumon-mi who knows outside of the fuckin’ Yakuza is Tsu-chan."
    s "I can’t imagine Tsuneyo was very helpful in that regard."
    yu "She’s actually a really good listener. "
    yu "Io, on the other hand..."
    yu "Yeah, it’s probably better if she never hears any of that."

    if bonus == True:
        s "Is this that “protecting kids” setting of yours that you were talking about earlier?"

        scene yukioutside18
        with dissolve

        yu "It’s the best I can do since mine has already given up on me."
        yu "They’re all good girls."
        yu "Hurt any one of them and I will rip your fucking dick off."
        s "..."
        s "You and Yumi really do have a lot in common."

    scene black
    with dissolve2

    "Yuki and I head into Tojo Ramen and order a quick dinner."
    "It’s already really late by the time our food arrives, so we scarf it down, pay for ourselves and head on our way."
    "I’m not exactly sure what this means for the beginning of our relationship-"
    "And I’m even less sure of how (And if) Yumi will ever fit into it."
    "But at least I have one more person to talk to in the middle of the night now."

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate5 = True
    stop music fadeout 10.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukidate10:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I haven’t really spent any time with her since the Halloween party, and even then, I don’t know if what I did would really count as {i}spending time with her{/i} to begin with."
    "I just kind of showed up, revealed her long-lost and no longer comatose niece to her, and then went on my way."
    "But I guess that’s just how things go sometimes."
    "But hey, if anyone I know is able to roll with the punches, it’s probably Yuki. "
    "For all I know, she’s completely come to terms with that aspect of her life being flipped on its head- given that she spent years personally flipping everything else over on her own."

    play sound "phonebeep.wav"
    play music "recovery.mp3" fadein 3.0
    scene black
    with dissolve

    yu "Yo. Sorry, but I can’t really talk right now."
    s "What? Why?"
    yu "Uhh...because I have a job now?"
    yu "Can’t just fuckin’ eat noodles with you whenever you want anymore. Gotta pay bills and shit."
    s "What kind of bills do you even have?"
    yu "The fuck is that supposed to mean? Same kinda bills everyone else has to pay. Water...gas-"
    yu "I don’t know man, whatever comes in the mail. I can’t be bothered to keep track of all that shit."
    s "And here I was thinking you were still living on the streets. No offense."
    yu "How am I not supposed be offended by- wait, Kaori! I already went that way!"
    s "You’re with Kaori?"
    yu "Hm? Yeah. "
    yu "Sara was tired of bein’ cold and shit so she sent the two of us out here to pass out fliers. "
    s "And where is {i}here{/i} exactly?"
    yu "Urban district. Why? You gonna come help? "
    s "No. But I wouldn’t mind standing around and talking to you while you work."
    yu "Yeah, I’m sure that- wait. That actually might be a good idea."
    yu "Boss lady seems dead set on the whole idea of me bringin’ in new customers by bein’ the closest thing all these girls can get to an actual dude now, but...well, you’re {i}actually{/i} a dude."

    if bonus == True:
        yu "Could save me the effort of turning down a bunch of desperately horny women and actually getting rid of all these papers."
        s "I don’t know, Yuki. I’m not really that great at turning down desperately horny women."
        yu "Then maybe I can show you a thing or two."
        s "Maybe {i}I{/i} can show {i}you{/i} a thing or-"
    else:
        s "That's true. But only just barely."

    play sound "phonebeep.wav"

    s "...two."

    "Yuki hangs up on me (Likely on accident) and I’m suddenly faced with the question of whether or not I want to go all the way across Kumon-mi just to see her and her no-longer estranged niece."

    s "..."

    "I sigh to myself and accept that, at this point, I’ve pretty much already decided. "
    "It’s very rare that I make it this far into a conversation only to back out and, well...I guess it’s been getting a little warmer out lately anyway."
    "A trip to the urban district might not actually be all that bad with that in mind."

    if bonus == True:
        "Besides, maybe Yuki and I can...bond over the fact that we...both have nieces or something."
        "I don’t know."
        "I just need to keep myself occupied."
        "Nothing good ever comes from wandering around aimlessly. "
        "And if I can focus on something, I’m sure I’ll-"
    else:
        "I just hope I don't get a blister because that would make me sad."

    play sound "static.mp3"
    scene beforewefall5 with flash
    scene everythingg5 with flash
    scene dust3 with flash
    scene yukiflier1 with flash
    stop sound

    "Oh. Okay."
    "I guess I’m here now."

    yu "You fuckin’ run here or something? I feel like I just hung up on you like five minutes ago."
    s "I was just really excited to see you, I guess. "

    scene yukiflier2
    with dissolve

    yu "Yeah? Lucky me."
    yu "Want a flier? I’ve only got like two hundred more to get rid of, and Sara didn’t say shit about not givin’ ‘em out to people who have already been to the bar."
    s "That’s great, because if you can give one to me and every other customer you’ve ever had, you’ll only have around 195 left."

    scene yukiflier3
    with dissolve

    yu "Shit’s actually been pickin’ up lately, believe it or not."
    yu "Granted, I don’t really know how it was before I started goin’ there, but we’ve basically always got {i}somebody{/i} inside. "

    "That’s actually pretty surprising given how horrible the name of the place is."
    "And the fact that Sara is confident enough in it to put it on a flier makes it all the more surprising that-"

    s "..."
    yu "What? Somethin’ wrong with the flier?"
    s "Apart from the name of the bar? Yeah. "
    s "Did Sara design these?"

    scene yukiflier4
    with dissolve

    yu "Nope. She gave me complete creative control or whatever."
    s "Well...I’m glad that she trusts you."

    scene yukiflier5
    with dissolve

    yu "Wait, I didn’t spell anything wrong, did I? "
    yu "I ain’t really the best when it comes to writing and shit on account of the whole no education thing."
    s "No, it’s all fine. You just normally want to be a little more...polite or...precise when it comes to marketing, I think."
    s "And saying “You have drinks and shit” doesn’t really scream “You should come to this bar.”"
    s "All bars have drinks and shit. That’s the entire purpose of a bar."

    scene yukiflier6
    with dissolve

    if bonus == True:
        yu "Well, what the fuck else do you want me to put on here? “Come to Sakaki-bar-a: We’ve got a horny barmaid and her reclusive daughter?”"
    else:
        yu "Well, what the fuck else do you want me to put on here? “Come to Sakaki-bar-a for a chance to hug a barmaid?"

    s "You joke, but that would bring me in quicker than the other sign."

    scene yukiflier7
    with dissolve

    yu "Yeah, but you’re a fucking creep and normal people probably don’t think the same way as you."
    s "You remind me more and more of your daughter every time I talk to you."

    scene yukiflier8
    with dissolve

    yu "Oh, speaking of which...were you able to give my present to Yumi?"
    s "Oh, yeah. I guess I should have probably called you about that or something."
    s "I gave it to her at the Halloween party, but I didn’t really stick around to see what she thought of it. "
    s "In fact, I don’t even think I asked what it was you gave her."

    scene yukiflier9
    with dissolve

    yu "Nothing that impressive. Just a case for her phone and some gift cards and shit."
    yu "Figure that if you’re gonna be payin’ her phone bill, least I can do is get her something to protect it from breakin’ or...getting wet or whatever."
    s "..."
    yu "If she’s anything like me, she’ll break that shit quicker than you can cook a pot of rice."
    s "I’m going to ignore the irony of this analogy and just re-confirm that I did give Yumi the present."
    s "I am sure that whatever happened after that went entirely according to plan and that her phone is both dry and protected as we speak. "

    scene yukiflier10
    with dissolve

    yu "Heh. Look at us- both payin’ for her shit. It’s almost like I’m actually her mom again."
    s "True, but that would make me her dad and I don’t think any of us would particularly enjoy that sort of change in our relationship status."

    if bonus == True:
        yu "Hey, can’t be any worse than her last dad. Unless you’re plannin’ on makin’ me suck you off in exchange for a bed or some shit."
    else:
        yu "Hey, can’t be any worse than her last dad. Unless you’re plannin’ on makin’ me hug you in exchange for a bed or some shit."

    yu "But I’m starting to think you’re not that type of guy."
    s "I will continue working hard to prove to you that I’m not that type of person."
    s "Unless you’re offering. In that case, you can sleep in my bed whenever you like."
    yu "Noted. "
    s "Not going to use this opportunity to remind me that you’re too old for me or...not interested in that sort of thing, or whatever it is you always say?"

    scene yukiflier11
    with dissolve

    yu "Nah. You’ve heard that shit enough by now. No point in repeatin’ myself anymore. "
    yu "But hey, if any of that changes, I’ll make sure you’re the first to know."
    s "..."

    if bonus == True:
        "Did Yuki just openly admit that there’s actually a prospect of the two of us sleeping together eventually?"
        "Because even if those doors stay closed forever, the fact that I’m the first in line outside of them means that, if I time everything well enough, I might be able to squeeze my way in at the first sight of an opening."
        "I’ll mark this down as a victory and file it in a completely separate cabinet from the one where I keep the prospect of fucking her daughter."
        "Then, before I attempt to carry on the conversation like a normal human being, I chuckle to myself at the idea of a cabinet full of written documents full of different girls’ sexual characteristics and traits."
        "I wonder how many more loops it will take before Maya is forced to forge something like that instead of just her weird journal of my {i}original{/i} ten students."

        s "So, about us fucking-"
    else:
        "Did Yuki just openly admit that there’s actually a prospect of the two of us hugging?"
        "I should hurry up and ask her."

        s "So, about us hugging-"

    yu "Shove it, asshole. "

    "I appear to have failed at carrying on the conversation in a believable and normal way."

    scene yukiflier12
    with dissolve

    k "Tired-looking woman of familial relation to me! I have finished passing out the rectangular remains of annihilated natural wood pillars! What would you have me do next?"
    yu "That’s all, Kaori. You don’t have to stick around anymore. I’ve got this scrub keeping me company now."

    if bonus == True:
        s "If I’m a scrub, how come I’m at the top of your sex list?"
    else:
        s "=("

    scene yukiflier13
    with dissolve

    if bonus == True:
        yu "Oh, good. I say one nice thing to you and you’re already twisting it into a secret list of people I’m deciding whether or not to bone."

    k "Friend! If I had known your body would be in the same location as mine, I would have contacted you through my communication cube!"
    s "I could have sworn I’d heard you say “cell phone” before. "
    s "You’re not...getting {i}worse{/i} at talking...are you, Kaori?"

    scene yukiflier14
    with dissolve

    k "Friend has too many {i}other{/i} friends to make regular contact with me, so I have been taking it upon myself to do the studying of human vocabulary as my own person! Without his help!"
    k "To speak is to communicate! And to square is to cube! I am learning!"
    yu "Kaori, are you sure it was okay for you to be released from the hospital?"

    scene yukiflier15
    with dissolve

    k "There are some things that juice can not cure, Yukiburger! I shan’t return to the jungle of uncomfortable beds and fluorescent brightness tubes!"
    s "Yukiburger?"
    yu "She added the burger part to my name earlier today. I have no idea why. And she gets mad any time I try to tell her to take it out."
    k "Yukiburger! Are you confident that I can depart? Are all of the trees dead?"
    yu "Yup. All dead, Kaori. Thanks for helping out."
    yu "I’ll ask Sara to like...wire you the money or however the fuck she’s been paying you."

    scene yukiflier16
    with dissolve

    k "Wires are unreliable, Yukiburger. Money is far too large to fit inside of them."
    k "I will return to the Sara and collect my payment in the physical realm sometime before the end of the year."

    scene yukiflier17
    with dissolve

    k "But...until then, hello!"
    k "Press buttons and say goodbye to me soon, Friend! I miss you very much!"
    s "Will do, Kaori. Have a good night."

    scene yukiflier18
    with dissolve

    "Kaori runs off and disappears into some alleyway, probably on the hunt for more chickens or...other animals or something."
    "I don’t see much point in trying to figure out what she’s doing in her spare time."

    yu "You know, it’s starting to make sense why you decided against telling me my niece was still alive."
    s "Sure. Let’s just say that I was doing this for your own good and that it wasn’t just something that completely slipped my mind."

    scene yukiflier19
    with dissolve

    yu "For real, though. Is she like...{i}okay{/i} to function in the real world? Cause I ain’t one to really talk when it comes to shit like that, but I feel like even {i}I’ve{/i} got a leg up compared to her."
    s "She actually functions really well apart from frivolously spending roughly 90%% of her income on trying to free animals. "
    s "I’m pretty sure she’s simultaneously holding six thousand jobs- and you’re somehow only holding {i}one{/i}."
    s "So maybe you should be taking pointers from her, Yuki?"

    scene yukiflier20
    with dissolve

    yu "Hm. You know, when you put it like that, yeah. I guess maybe I could be taking some pointers from her?"
    s "I...wasn’t really being serious. Kaori is an enigma and I don’t think it would be a good idea for any of us to try and live our lives the same way she lives hers."

    scene yukiflier21
    with dissolve

    yu "I’m just glad she’s okay. "
    yu "If my daughter’s not gonna fuckin’ acknowledge my existence, I guess a niece doing it is like...the next best thing."
    yu "‘Sides, Kaori seems actually kind of excited to have someone she can call family. Even if she’s adding fucking “burger” onto the end of my name."
    s "Well hey, maybe one day, all {i}three{/i} of you can sit down and...do whatever it is the three of you did when you were younger."
    yu "Yeah. And maybe I’ll win the lottery and get elected prime minister of Japan as well."
    yu "Don’t feel the need to provide hope where there ain’t none, man. "
    yu "There’s some shit that stays broken forever once you’ve fucked it up...and no amount of glue or...tape, or...any other sticky shit can put it back together."
    yu "What really surprises me, though, is that Yumi doesn’t want to see her."
    yu "The two of them weren’t like...{i}inseparable{/i} or anything like that back then, but she’s one of the few people I’ve actually seen who was able to make her smile."
    yu "...heh. She had a real cute smile back then, too. The kind where there’d be like, missing teeth and shit. But in a “kid” sort of way. Not like a...gross sort of way."
    s "You have such a way with words sometimes."

    scene yukiflier22
    with dissolve

    yu "Right, right. Which is exactly why you had such an issue with what I decided to put on all of our fuckin’ fliers."
    s "Speaking of which, aren’t you supposed to be passing those out?"

    if bonus == True:
        yu "What, am I not allowed to take a fuckin’ break to hang out with the dude at the top of my secret sex list?"
    else:
        yu "Yeah, but I'm allergic to paper and holding them for so long is starting to make my throat close up."

    s "I {i}knew{/i} it. "
    yu "It was a joke, asshole. "
    yu "I don’t care if you’re Yumi’s new dad or...sugar daddy or whatever the fuck you are-"
    s "I believe it’s pronounced “teacher.”"
    yu "Sure, let’s go with that."
    yu "What I’m sayin’ is I don’t care what your role is. I’m just glad I’ve got someone like you to hang around who actually feels like a decently good person."
    yu "That shit’s hard to come by."
    s "I feel like you are, once again, gravely misinterpreting the kind of person I am."
    yu "Am I?"
    s "Absolutely. And this isn’t me just being a self-loathing piece of shit again- that’s what inner monologues are for."
    yu "Uh-huh. Right."
    s "What I’m saying is that you can’t really judge a person by just...how they act around you. You need to think about what’s underneath the surface as well."
    s "You barely know me. Have I been mostly kind to you? Sure. But what about how I treat other people? "
    s "What about how I treat Yumi?"
    yu "You mean when you’re paying her phone bill and taking her job hunting? Yeah, you sound like a real douche."
    s "No, Yuki...that’s not what I mean."

    if bonus == True:
        yu "Then...you mean like when you’re boning her?"
    else:
        yu "Then...you mean like when you’re hugging her?"

    s "You know what? I feel like getting into a philosophical debate right now probably isn’t the best thing for either one of us."
    s "Just know that I’m not as great as you think I am."
    yu "Oh, I don’t think you’re great at all."
    yu "I’m sure you’ve done plenty of shit that you regret- but we’ve all got stuff like that."
    yu "You think I look back on all of the mistakes I’ve made and just shrug them off because I’m like...above them now or something? Course not."
    yu "I think I’m the fuckin’ scum of the earth. And I’m sure you feel the same way about yourself most of the time."
    yu "But those thoughts are our own, man. You’ve gotta look at shit from the outside."
    yu "You obviously don’t think I’m fucking Satan. If you did, you wouldn’t be helping me out all the fuckin’ time."
    yu "So I can think whatever the fuck I want about you and you can’t do shit about it."
    yu "We can hate ourselves as much as we want inside of our heads, but until we go out there and show {i}every single person in the fucking world{/i} that we’re against them-"
    yu "There are going to be some people who are just...on our side for no reason whatsoever."
    s "..."
    yu "What? I’m older and more experienced than you. Don’t tell me you’re surprised to hear some words of wisdom out of me?"
    yu "Now, help me figure out what to do with the rest of these fliers. And don’t suggest that I just throw them out or whatever. The more customers Sakaki-bar-a gets, the more I get paid."
    s "Can we just go back to calling it “the bar” please? I get irrationally angry each time I remember the real name."
    yu "We can do whatever the fuck you want as soon as we finish handin’ these out. "
    yu "Here-"

    scene black
    with dissolve

    "Yuki hands me roughly half of her stack of fliers and the two of us set off in opposite directions to...distribute them, I guess."
    "I don’t really know how I allowed myself to get roped into this, but it is what it is."

    if sarasex == True and bonus == True:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks (And blowjobs) she’s given me."
    else:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks she’s given me."

    "I do my best to hand them out to people, but “my best” only survives for a matter of minutes before being brutally murdered in the form of me stashing my entire pile in a nearby shoe store."
    "But hey, my job was to get rid of all of my fliers without throwing them away, and that is precisely what I did."
    "I send Yuki a text to figure out where she is and whether or not she wants to continue hanging out after she’s done with “work.”"
    "Fortunately, she also found a shoe store to offload her fliers in, and the two of us reconvene at our original meeting spot and decide to head to a nearby convenience store for dinner."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate10 = True
    jump yukidate10p2

label yukidate10p2:
    scene yukiconvenience1
    with dissolve2

    yu "So, what do you want? Choose any one food item in the store and it’ll be my treat for pretending to help me tonight."
    s "Hey, for all you know, I successfully distributed roughly one hundred fliers just now. Who says I was pretending?"
    yu "Only way you could have actually handed off that many bar ads in just a few minutes is if you just conveniently waltzed into the world’s largest AA meeting."
    s "I think that’s the sort of place that’s supposed to make it {i}harder{/i} to hand out bar ads."
    yu "Yeah. You’d {i}think{/i} that. Sad truth is that half the people that go to those meetings are ready to jump on the first fuckin’ excuse they can think of to relapse."
    yu "Take it from someone who has experience, kid."
    s "I don’t know how I feel about being called “kid” when I’m only a few years younger than you."
    yu "Right, right. My b. Just keep seein’ that baby face of yours and thinking you’re only a little older than my daughter."
    s "My face is not childish and I would greatly appreciate it if you’d take that back."
    yu "And I’d {i}greatly appreciate it{/i} if you’d get a fuckin’ move on and pick your poison already before the people workin’ here think I’m stealin’ shit."
    s "..."
    s "{i}Are{/i} you stealing shit?"

    scene yukiconvenience2
    with dissolve

    yu "What? No. Obviously not."
    s "I don’t think it’s obvious if you said yourself that people are going to be assuming that-"
    yu "I have a job now, man. I don’t have to steal shit."
    yu "Remember? I pay bills. I’m a normal person. All that gang shit’s a thing of the past as of a little while ago."
    s "You can’t even name all of your bills yet. "
    yu "Well, forgive me for not fuckin’ memorizing ‘em. "
    yu "You have any idea what the longest time I’ve held down an apartment is? Go on. Take a guess."
    s "I feel like anything I guess here is bound to offend you."

    scene yukiconvenience3
    with dissolve

    yu "Three months."
    yu "In all fairness, it should {i}probably{/i} be two. But I’m pretty sure the owner of the place I’m talkin’ about was too scared to remind me that I actually needed to {i}pay{/i}."
    s "How do you keep finding living arrangements with such a horrible track record as a tenant?"

    if bonus == True:
        yu "How do you keep finding preppy girls with perky tits ready to jump your bones despite being twice their age? Just happens. Best not to question any of it."
        s "I’m glad to hear you’ve been...paying attention to my students’ chests?"
    else:
        yu "How do you keep finding cute girls who want to hug you and shit?"
        s "How do you know they're all cute? They could be hideous. Or even worse, old."

    yu "They’re fuckin’ teenagers, man. Their bodies ain’t had time to get all mature and saggy and shit yet. Just safe to assume, you know?"
    s "At the risk of you hitting me, I’d like to say I wouldn’t go as far as describing you as “mature and saggy.”"

    scene yukiconvenience4
    with dissolve

    yu "I’d sure fuckin’ hope not."

    scene yukiconvenience5
    with dissolve

    yu "Might not be the same as they were back when I was Yumi’s age, but there’s still some life left in these things for now."
    yu "Maybe cause I’ve been goin’ to the gym? "
    yu "I don’t know. What do you think?"
    s "Uhhhhhhhh..."

    scene yukiconvenience6
    with dissolve

    yu "Sup?"
    s "Not...much? I just didn’t expect you of all people to wind up groping yourself in the middle of a convenience store."
    yu "Wanna cop a feel yourself?"

    if bonus == True:
        s "There is no way this isn’t a trap."
    else:
        s "No thank you, madam."

    scene yukiconvenience7
    with dissolve

    if bonus == True:
        yu "Oh, stop. It’s not like I was planning on putting you in an arm lock the second you reached for my chest or anything. That would have just been rude."

    "I take a moment to thank my intuition and self control for at least improving in...some sort of way recently."

    yu "Color me surprised, man. You normally don’t waste any time at all when it comes to hittin’ on me for whatever reason."
    yu "And here I was actually givin’ you a chance, only for you to pussy out. You’re all talk after all, ain’t ya?"
    s "I’m definitely not all talk. You’re just being suspiciously handsy and surprisingly flirty for someone who’s apparently not interested in romance or sex or anything."

    if bonus == True:
        s "Well, apart from keeping me at the top of your secret sex list, I mean."

    scene yukiconvenience8
    with dissolve

    yu "Handsy? The fuck you talkin’ about?"
    s "Probably the hand you’re repeatedly tapping me with."
    yu "That’s just me fuckin’ with you, dude. Just because a girl touches you doesn’t mean she’s tryin’ to sleep with you."
    s "Sure. Just like how girls who pick on boys in school by pushing them around on the playground don’t actually have crushes on whoever they’re bullying."
    yu "I didn’t, at least. I used to pick on kids just for lookin’ weird and shit."

    "Is bullying just a genetic trait for the Yamaguchi family or something?"
    "Well, I guess Yuki’s maiden name would be something different...but I’m not really in any rush to figure out whatever it was."

    scene yukiconvenience9
    with dissolve

    yu "There. Do you feel a little safer now that the big, bad ex-biker lady isn’t trying to take your lunch money?"
    s "The fact that you were offering to buy me dinner just a minute ago is making this sudden roleplay thing a little harder to follow."
    yu "{i}Still{/i} offering. Just waiting for you to fucking pick something instead of waiting for me to keep “flirting” with you. "
    s "But the flirting is so much more fun."
    yu "Maybe if it was actual flirting and not just two friends going on a late night sandwich run after work."
    s "This late night sandwich run is probably the closest you’ve been to being on an actual date literally ever."

    scene yukiconvenience10
    with dissolve

    yu "Yo! That ain’t even remotely-"

    scene yukiconvenience11
    with dissolve

    yu "...true?"
    s "..."
    s "You seem confused."
    yu "Hold on. I’m tryin’ to think."
    yu "..."
    s "..."
    yu "Well, shit. I think you’re right."
    yu "I’m sure there were some in the past, but either I was too fucking high to remember ‘em or they just weren’t worth rememberin’ in the first place."

    scene yukiconvenience12
    with dissolve

    yu "So now what? Wanna hold hands or somethin’? Take turns tellin’ each other what we like about each other?"
    s "..."

    if bonus == True:
        s "Is the opportunity to grope you still on the table?"
    else:
        s "One hug, please."

    scene yukiconvenience13
    with dissolve
    play sound "entrybell.mp3"

    if bonus == True:
        yu "Only if you don’t mind gettin’ your dick ripped off the second you try."
    else:
        yu "How about we just go beat up some old people instead?"

    s "Like mother, like daughter, I guess..."
    y "Wha-"

    scene yukiconvenience14
    with fade

    s "Uh-oh."
    yu "Yumi..."
    y "..."

    "It appears that yet another unfortunate coincidence has befallen me once again."
    "Well, I suppose it’s not really unfortunate for {i}me{/i}. At least not yet."
    "I’m sure the inevitable fallout of this will result in Yumi’s problems finding a way to bring me down in one way or another."
    "But, on the bright side, this might actually be kind of {i}convenient{/i} for Yuki if she ever plans on patching things up with her daughter."
    "She just needs to make sure she doesn’t do anything to set her off during what I expect will be an incredibly short conversation."

    y "..."
    yu "..."

    "Or...maybe not even a conversation at all?"

    s "...I’ll be the one to talk, I guess."
    s "Hi, Yumi."

    scene yukiconvenience15
    with dissolve

    y "Yeah. {i}Hi.{/i}"
    y "Would you mind explaining what you’re doing all the way in bumfuck nowhere with {i}her{/i}?"
    s "This is the most populated part of the city and you have weird criteria for what constitutes “bumfuck nowhere.”"
    s "As for why I’m with {i}her{/i}-"

    scene yukiconvenience16
    with dissolve

    yu "We’re on a date."

    "Oh no."

    s "{i}What are you doing?{/i}"
    yu "Hm? Flirting, obviously."
    y "You expect me to believe that {i}you two{/i} are on a date?"
    y "Even this guy, who’s one of the scummiest people I’ve ever met, would have to be drunk out of his fucking mind to even {i}consider{/i} going on a “date” with someone like you."

    scene yukiconvenience17
    with dissolve
    stop music fadeout 20.0

    yu "Maybe he just likes girls who are a little rougher around the edges? Don’t ask me, ask him."
    s "Don’t ask me. We are not on a date and I have no idea why she is doing this."
    yu "Oh, come on. You could have at least played along a {i}little{/i}."

    if bonus == True:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m screwing her mother when I {i}definitely am not.{/i}"
    else:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m hugging someone evil."

    scene yukiconvenience18
    with dissolve

    y "Great. Consider yourself lucky then for not catching one of the millions of STDs the world’s greatest mom over here is carrying."

    if bonus == False:
        "Oh no. Can you catch those from hugging?"

    s "Okay, Yuki was clearly in the wrong with pretending to date me, but-"
    yu "Nah, she’s right. Well, apart from the STD thing. I deserve whatever she throws at me. "
    yu "Besides, this is the first time she’s said anything to me in years. I’ll take what I can get."

    play music "undersea.mp3"

    if yumiknows == True:
        y "What you can {i}get{/i} is the fuck away from my teacher who, coincidentally, also happens to be {i}dating my best fucking friend.{/i}"

        scene yukiconvenience19
        with dissolve

        if bonus == True:
            yu "Wait, you never told me that."
            yu "I thought you were fucking Yumi?"
        else:
            yu "Wait, you never told me that."
            yu "I thought Yumi was you huggy buddy."
    else:
        y "What you can {i}get{/i} is the fuck away from my teacher, you dumb bitch."
        yu "{i}Just{/i} your teacher?"
        s "Yuki, no."
        y "Well, what else would he fucking be?"

        if bonus == True:
            yu "Beats me. I just thought you two were screwing or something."
        else:
            yu "I thought he was your hugging partner."

    scene yukiconvenience20
    with dissolve

    y "You thought fucking {i}what?{/i}"
    yu "Well...yeah. Because I’ve seen you two around together and...I don’t know. I just kinda figured there was some shit goin’ on."
    yu "Sensei always told me that wasn’t the case, but I kinda just figured that was because I’m your mom and that would make shit real awkward for him."
    y "Are you fucking kidding me?"
    yu "What? It’s a misunderstanding. It’s not a big deal."

    scene yukiconvenience21
    with dissolve

    yu "But, uhh...apart from that..."
    yu "You...got taller?"
    y "Yeah. It’s a little known fact, but most kids continue growing once their parents walk out on them."
    s "Okay, I’m just...gonna...go over there."

    scene black
    with dissolve

    "Yuki lets go of my collar and I quickly make my way over to the magazine rack to make it look like I’m...doing anything but being involved in this discussion."
    "And while I’d like to say it will only be a matter of time until one of the staff breaks things up (Which probably {i}should{/i} be my job), it looks like the only person working really doesn’t want to get involved."
    "And I don’t blame them. Neither Yuki nor Yumi look particularly friendly...especially when they’re at each other’s throats."

    $ renpy.end_replay()
    $ yukidate10p2 = True
    jump yumispecial40

label yukidate20p1:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer. "
    "I figure that there’s a decently high chance she’s working tonight given that Sara’s bar is somehow [[probably] no longer the least successful business in all of Kumon-mi-"
    "But I try my luck regardless as I tend to get lucky when I start monologuing. Plus, I’m curious about where things stand in the relationship between her and Yumi."
    "Just before I coerced her daughter into sleeping at my house, albeit for good reason, Yumi made it apparent that the two of them were talking again."
    "And while I highly doubt that means they’ll be going on mother-daughter spa trips anytime soon, it {i}does{/i} mean that Yuki may have noticed something."
    "If I’m remembering correctly, Maki caught onto Makoto’s changes in demeanor around the time she first started acting all miserable. {i}Before{/i} the dad thing."
    "It seems like aeons ago at this point, and Yuki is nowhere near as effective a mother as Maki (Which is saying a lot), but it’s still possible she’s noticed {i}something.{/i}"

    play sound "phonebeep.wav"

    yu "Yo. What up?"

    "Though, I guess it’s entirely plausible that she {i}didn’t{/i} and that we’re just going to eat ramen or something."

    play music "recovery.mp3"

    s "I’m bored."
    yu "Cool. The fuck you want me to do about it?"
    s "Invite me over to hang out and make me feel young again."
    yu "Ain’t you got like fifty girls who make you feel young every day? How the hell can {i}I{/i} help with that?"
    s "By not reminding me of the age disparity between us every five seconds. And by also being allowed to drink with me. And by looking old."
    yu "Well, you don’t have to be a prick about it. But yeah, you can come chill. Sara gave me off tonight anyway."
    s "Was it really Sara who gave you off? Or was it {i}me{/i} thanks to my internal narration about how convenient it would be for you to not have work right when I call you?"
    yu "Unless your weird ass brain is the one writin’ my paychecks, I’m gonna say it was Sara."
    s "Fair enough. Are you at Tojo Ramen?"
    yu "Nah, actually ain’t been there much lately. I’m at my apartment right now, but it’s cool if I bring people over."
    yu "Just don’t go braggin’ about havin’ a house or some shit while you’re here or I’ll kick you in the nuts. "
    s "I will definitely remember that. I need those and would like to keep them safe. But yeah, send me your address and I’ll head over now."

    play sound "phonebeep.wav"

    "I hang up the phone and wait for Yuki to-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Nevermind. It’s here."
    "........."
    "......"
    "..."

    scene yukiapt1
    with dissolve2

    "I let myself in after knocking on the door and hearing Yuki shout something about how her lock is broken."
    "It’s probably not a thing someone should be screaming about in a low-income housing complex like this, but I assume anyone who were to waltz in uninvited would be promptly beaten to death."
    "Also, I’m pretty sure Imani lives next door, but I’m not going to text or call her about it because I want her to hear my voice through the walls and feel confused."

    yu "Yo. Find the place okay?"
    s "Yeah. I’ve actually been here before."

    scene yukiapt2
    with dissolve

    yu "You stalkin’ me or some shit?"
    s "What is it with your family and always interpreting my extreme fortune as predatory behavior?"
    yu "Idunno. Doesn’t help that you always look like you’ve been hiding behind a tree and waiting for a pretty girl to walk by or some shit. "
    s "I’m not at that level yet, but thank you for the backhanded insult regardless. Where should I sit?"
    yu "Ain’t like you have many options. The floor or the couch. Take your pick."
    s "You won’t hit me if I join you on the couch, will you?"
    yu "You think I would have invited you into my apartment if I planned on beating the shit out of you? "
    s "No. Which is precisely why I {i}should{/i} be on guard as it would make this the perfect moment for you to strike."

    scene yukiapt3
    with dissolve

    yu "Man, can you stop treating me like I’m some kind of violent criminal? I’m an ex-junkie who just {i}happened{/i} to have beaten the shit out of a lot of people back during my heyday."
    yu "Ain't like I went out lookin' for that kinda shit."
    yu "'Sides, my lungs ain’t built for that anymore. But if you keep fuckin’ poking me about the person I {i}used{/i} to be, I might just have to give ‘em a workout again."
    s "So...if I don’t stop assuming you’re a violent person, you’re going to get violent with me?"
    yu "That-"

    scene yukiapt4
    with dissolve

    yu "Well..."
    yu "Of course it’s gonna sound bad if you put it that way. But really, I ain’t gonna do shit. And if you’re gonna hang out in my place, you’re gonna respect me. Got it?"
    s "Sure. I wasn’t being serious anyway. I know that you’ll protect me if anything goes down while I’m here."

    scene yukiapt5
    with dissolve

    yu "You {i}always{/i} been a beta or is this a new development for you?"
    s "I’m going to ignore that and join you on the couch now."
    yu "Need me to hold your hand and guide you over here? Or are you old enough to do it on your own, big boy?"
    s "Please never call me “big boy” again."

    scene black
    with dissolve2

    "I successfully and flawlessly manage to make it across Yuki’s living room without hurting myself."
    "However, just as I’m about to sit down, she points toward a small mini fridge underneath a desk and asks that I grab her another can of beer."
    "I oblige, grabbing one for myself as well. But, when I go to close the door, I accidentally shut my finger inside of it."
    "Thankfully, she doesn’t notice and I am able to maintain the illusion of being a strong alpha-male who will, in no way, ever submit to this woman."

    scene yukiapt6
    with dissolve2

    yu "Damn. Can’t remember the last time I was alone in my own place with a guy."

    "Actually, on second thought, I’d probably submit to her if that’s what she wanted. "
    "She’s surprisingly attractive when her eyes are mostly open and she’s not taking a drag of a cigarette."
    "The apartment does reek of smoke, of course...but I kind of expected it to given that she’s the  closest thing to a chimney I’ve ever encountered that isn’t, you know, an actual chimney."

    yu "Feels a little different than hangin’ out at the ramen shop or the bar, huh?"
    s "Is this the part where we make out?"
    yu "Maybe. Feel like I might need to get a permission slip from your parents first, though."
    s "Well, there goes the thing I said earlier about you not bringing up the age disparity thing."
    yu "That was bullshit from the get-go. I bring that up all the time. Feels weird as fuck to be hangin’ out with a dude so much younger than me. Ain’t you young enough to be my kid?"
    s "I feel like you’re grossly misrepresenting the gap in our ages. We’re both in our thirties, aren’t we?"
    yu "You’re in your thirties? You act like so much of a bitch all the time that I must have forgotten. "
    s "Sometimes, I have a hard time remembering why we’re friends."
    yu "Same here. If anything, {i}you’re{/i} the one who should be off doin’ other shit. I ain’t gonna complain about havin’ somebody around here to help connect my oxygen tank and..."
    yu "I don’t know. Fix electronics and shit. Other stuff old people can’t do."
    s "Again, you are in your thirties."
    yu "Yeah, but it ain’t like I’m gonna be there much longer. I’ll be 40 before either one of us knows it. Might as well start plannin’ my funeral now."
    s "If you die, it’ll be from all of the smoking and drinking, not your age."
    yu "Amen to that, brother."
    s "That was me gently nudging you toward quitting."
    yu "Gonna have to nudge a little harder than that. I ain’t givin’ up the shit that makes me happy for a few extra years of a life I’ve already made it further into than I ever should have."
    s "I just don’t get why you’d bother getting sober at all if you’re just going to start abusing {i}other-{/i}"

    scene yukiapt7
    with dissolve

    yu "Blah, blah, blah. Can we talk about something other than my shitty ass backstory for once? It ain’t like I’m wanderin’ around town drunk as shit. I’m in my own apartment. I ain’t hurtin’ anybody."

    scene yukiapt8
    with dissolve

    yu "Other than myself, I mean. But fuck if I don’t deserve it at this point."
    s "Yuki-"

    scene yukiapt9
    with dissolve

    yu "Ah- nope. Don’t “Yuki” me. Didn’t I {i}just{/i} tell you it’s about time we got together without wadin’ through all my bullshit? Hit me with somethin’ that ain’t depressing as fuck."
    s "But all I know is sadness."
    yu "Well, know somethin’ else for a few minutes you fuckin’ buzzkill. Tell me {i}your{/i} story, cause I’m tired as fuck of tellin’ you mine."
    s "I can assure you mine is not nearly as exciting."
    yu "Yeah? And why’s that?"
    s "Because I can’t remember it."

    scene yukiapt10
    with dissolve

    yu "You get smacked in the head a few too many times or some shit? Wait, do {i}you{/i} actually have a dark past I don’t know about since I’m always the one runnin’ my mouth?"
    yu "Drugs can make your whole ass life a blur man. I’d tell you more but I’d be takin’ over the conversation again."
    s "It’s nothing like that. But, seeing as I am both horrible at telling stories and wouldn’t know {i}how{/i} to tell the story in the first place, let’s just move on to something everyone can understand and appreciate-"
    yu "You ain’t gonna ask me to make out again, are-"
    s "The two of us making out."

    scene yukiapt11
    with dissolve

    yu "You really just want me to beat the shit out of you, huh?"
    s "Probably not in the way you’re thinking."
    yu "Why? You like, can’t {i}actually{/i} be into me like that, right? We’ve got nothing in common save the whole beer and ramen bullshit. Ain’t no way I’m your type."
    s "Well, what’s {i}your{/i} type?"

    scene yukiapt12
    with dissolve

    yu "{i}My{/i} type?...Huh. That’s a good question. "
    yu "I don’t know if I have a type. I ain’t sure I’ve ever even thought of it before. "
    s "I get that you’re not the romantic type, but there has to be {i}some{/i} sort of guy you’d be into, right?"
    yu "Hmm..."
    yu "Someone who wouldn’t fuck me while I’m unconscious would be nice."
    s "That is...probably the lowest bar that has ever been set."
    yu "Someone with money so I wouldn’t have to do shit and could just hang around all day. Maybe a dude with a cool bike. Tattoos. "
    yu "Maybe just me with a dick. That sounds like it would be the easiest kind of relationship."
    s "So basically, the exact opposite of me."

    scene yukiapt13
    with dissolve

    yu "Guess so. Surprised?"
    s "Surprised? No. Hurt? Maybe."
    yu "Hey, you ain’t {i}so{/i} bad. A little soft, sure. But you’re kinda cute in like, an innocent sorta way. "
    s "Innocent is not a word that is typically associated with me."
    yu "Just the vibe I get. And hey, who knows? Maybe if we met like, twenty years ago or some shit, we could’ve hooked up? "
    yu "Not like I ever had much time for that kinda shit since I was always movin’ around, but I at least would’ve {i}thought{/i} about it if you hit on me back then."
    yu "Now, though? That’d just be weird. Like pickin’ up a kid from the candy store."
    s "I feel like this would have been {i}significantly{/i} weirder if it was twenty years-"
    yu "It ain’t {i}just{/i} about age, man. You’ve got a, like...{i}mental{/i} age too. I’ve seen shit. Experienced shit. "
    yu "And until I learn more about whatever the fuck your deal is, it’s gonna seem to me like you’re just a kid. Or...maybe not a full on {i}kid.{/i} But at least nowhere near as old as me."
    yu "Plus, I ain’t gonna make you tell me your “type” or whatever, but we both know it ain’t me. "
    s "Sure, but that doesn’t stop me from thinking you’re cute."

    scene yukiapt14
    with dissolve

    yu "Uh-huh. Sure. You think I’m cute."
    yu "What’s really going on here? Yumi tell you I’d blow you in exchange for better grades or some shit? Spill it."
    s "What’s going on is I think you’re cute."
    yu "..."
    s "..."

    scene yukiapt15
    with dissolve

    yu "{i}Me.{/i}"
    yu "{i}I’m{/i} cute."
    yu "I look like I haven’t slept since I was twenty. At my peak, I was like, half a step above being a zombie."
    yu "You think {i}I’m{/i} cute. Bullshit. Not when you’re around girls like Yumi and that gyaru friend of hers all the time. {i}They’re{/i} cute. I’m washed up. You don’t want me."
    s "Would it be so bad if I did, though? "
    yu "Bad? No. Just...fuckin’ weird. Only dudes who have ever tried gettin’ with me were just fuckin’ scared out of their minds I was gonna kill ‘em."
    s "Has that happened with other people apart from Yumi’s dad?"

    scene yukiapt16
    with dissolve

    yu "Nope."
    s "..."
    yu "..."
    s "You’ve only been with one guy?"
    yu "Can’t say that definitively as I was unconscious a fucking {i}lot{/i} back in the day. But he’s the only one I ever, like, had a {i}thing{/i} with."
    yu "Dudes just didn’t see me that way. And there ain’t no way in hell {i}you{/i} do when basically everyone you know is prettier or cuter or hotter or...you know. Other shit."
    yu "So, funny joke, but nah. You don’t think I’m cute. And if Yumi wants good grades, she’ll suck your dick {i}herself.{/i} I ain’t doing it for her."
    s "..."
    yu "..."
    s "So can we make out now?"
    yu "Sure. Go ahead. Try."
    s "I can’t tell if that translates to “Try and I will hurt you” or “You don’t actually want to do that and I am calling your bluff.”"
    yu "Just try. All I’m sayin’. "
    yu "The closer you come, the more you’ll realize I ain’t {i}cute{/i} at all. "
    s "That’s not true. We’ve never really been {i}this{/i} close before and I haven’t changed my opinion at all."
    yu "You will. You’re fuckin’ with me."

    scene yukiapt17
    with dissolve

    s "I’m not fucking with you."
    yu "Yo, that’s my leg."
    s "Yuki, look at me."

    scene yukiapt18
    with dissolve

    yu "..."
    s "..."
    s "I am attracted to you."
    s "Maybe “cute” isn’t the right word for it, but it’s not like I’m just lying to get a rise out of you. And I already give Yumi good grades."
    yu "This is such a weird way to admit to me that my daughter is sucking your dick."
    s "She’s- no. What? I give her good grades without making her work like that for them."
    yu "She’d probably work “like that” for them if you asked. But good on you, I guess. Also, get your hand off of my leg. I’m starting to think you’re serious."

    scene yukiapt19
    with dissolve

    s "I am."
    yu "Wha...why the fuck are you trying to act all cool all of a sudden?! The hell’s gotten into you, man?"
    s "I can be cool when I want to be."
    s "There also wasn’t a wall for me to slam my hand against, so this will have to do. "
    yu "That one sentence just took away like 50%% of the coolness on display here."
    s "Yeah, well no one’s perfect- and that includes you."
    s "You {i}do{/i} look like you haven’t slept since you were twenty."

    scene yukiapt20
    with dissolve

    s "You’re pale, your breath smells like smoke, and your hair is a weird shade of blonde that probably needs to be bleached again."
    yu "Well, fuck you too dude."
    s "I am also very intimidated by your presence and am fully aware you could kick my ass whenever you want."
    s "But, should you ever decide to stop thinking I’m just fucking around with you-"
    s "I’d be honored to be the first person you ever decide to have recreational sex with. "

    scene yukiapt21
    with dissolve

    yu "..."
    s "..."
    yu "..."
    s "I think this is the part where we make out."
    yu "I...kinda do as well, but..."
    yu "I’ve got some bad news for you."
    s "What kind of-"

    play sound "knock.mp3"
    scene yukiapt22
    with dissolve

    y "Yo! I’m here. Your lock still busted?"
    s "Oh, shit. I forgot she was a part of the opening monologue."
    yu "Uhh...yup! Come on in!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yukidate20p1 = True
    $ yuki_love += 1

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    jump yukidate20p2

label yukidate20p2:
    if _in_replay:
        play music "recovery.mp3"

    scene yumiapt1
    with dissolve2

    y "That {i}your{/i} bike parked outside? The fuck you pay for-"

    scene yumiapt2
    with dissolve

    y "Wait, what the fuck is my douchebag teacher doing here?! This some kinda intervention?! Cause I ain’t done shit!"
    yu "Yeah, I know. He was just telling me about how good your grades are without even having to-"
    s "Hi, Yumi. Nice seeing you here. Anyway, about the apocalypse-"

    scene yumiapt3
    with dissolve

    y "Why the fuck didn’t you tell me he was gonna be here?"
    s "Welp, there goes that."
    yu "I didn’t know he was gonna be here. But he called and you were takin’ your sweet ass time, so I got bored and invited him over. "
    yu "Also, am I actually cute? Just wondering."

    scene yumiapt4
    with dissolve

    y "The fuck? Obviously not. You look like you belong in a fucking alleyway surviving off of rats or some shit. Do you have any food?"
    yu "Nah. I’ll pick something up tomorrow. You wanna sit?"
    y "Depends. Is Douchebag McDouchefuck staying?"
    yu "Ha! Douchebag McDouchefuck. Ain’t she creative? "
    s "I was just leaving actually."
    yu "Bullshit, you’re staying. Need someone to defuse the situation if she snaps and she seems to like you. Or at least as close to likin’ somebody as she can come."

    scene yumiapt5
    with dissolve

    y "Since when?! I’d rather chop my pinky off than spend the night hanging out with him!"
    yu "Too soon, Yumi. Gary {i}just{/i} had to give his up like a week ago. Anyway, you sitting or not?"

    scene yumiapt6
    with dissolve

    y "Yeah, whatever. Fine. But only cause I ain’t got other shit goin’ on tonight."
    s "It’ll be great to have you-"
    y "Don’t talk to me."

    scene black
    with dissolve2

    "It’s hard to tell if the progress I’ve recently made with Yumi has gone out the window because of the universe’s mechanics or because she’s in front of her mom."
    "Which isn’t to say that our progress was {i}substantial{/i} by any means. But Yumi {i}has{/i} gone out of her way to spend at least {i}one{/i} night with me and no pinkies were involved at all."
    "Also, who is Gary?"

    scene yumiapt7
    with dissolve2

    y "So, you gonna tell me why you’re hangin’ out with my fuckin’ mom when I've told you probably a million times to {i}not{/i} do that? Or..."
    s "..."
    y "..."
    y "Well?"
    s "You literally just told me not to talk to you."
    y "Yuki, the fuck is this guy to you?"

    scene yumiapt8
    with dissolve

    yu "I don’t know. Thought we were just friends until a few minutes ago, but I think he might have the hots for me."
    y "Don’t be too flattered. He’d fuck a dog if it had a nice wig on."

    scene yumiapt9
    with dissolve

    if chikalust25 == True and brony == False:
        s "That is ridiculous, Yumi. It is perhaps your most absurd accusation yet."

        "I have no need for an {i}actual{/i} dog when I already have Chika to fulfill all of my...dog-related urges."
        "Which, I’d like to clarify, are a thing I do not have."
        "Or...didn’t have until recently."
        "Anyway."
    elif brony == True and chikalust25 == False:
        s "Or a pony."
        s "It doesn’t even need a wig either."
        y "Uhh...what?"
        s "Nothing. "
    else:
        s "It would have to be a {i}very{/i} nice wig. "

    y "See what I mean? This creep has the hots for literally anything he can stick his tiny dick inside. Inviting him over’s no better than flat-out {i}askin’{/i} to be raped."

    scene yumiapt10
    with dissolve

    yu "Yo, cut that shit out. Ain’t much I won’t let you joke about, but don’t go sayin’ shit like that rape thing. Know a lot of girls who had to go through that and it ain’t easy."
    y "Didn’t mean to strike a chord. Just sayin’ he ain’t exactly the most trustworthy person around. It’s a warning. Ain’t startin’ anything."
    y "Also, let’s get another thing straight. You ain’t {i}letting{/i} me joke about anything. I can say whatever the fuck I want, {i}whenever{/i} I want and you can’t do shit."
    yu "I can kick you out of my fuckin’ apartment, for one. But other than that, fair. "
    y "Go ahead and kick me out if you want. I’m only here cause I was hungry anyway."
    s "Sorry to interrupt this incredibly heartfelt interaction, but...since when is this a thing?"

    scene yumiapt11
    with dissolve

    yu "Since when is what a thing? Yumi being hungry? Cause she’s been a fuckin’ bottomless pit since she was an ugly fuckin’ potato. "
    yu "Only reason my tits are so small is she sucked the life force out of ‘em when she was a baby."

    scene yumiapt12
    with dissolve

    y "Okay, hold up! First off, that is {i}not{/i} how tits work! Second, you didn’t even breastfeed me! So don’t go makin’ shit like that up! Specially if it makes me sound gross!"
    yu "Ohhh yeah, right. Had so many drugs in my system at the time that I didn’t think it was safe puttin’ you anywhere {i}near{/i} my tits. Good memory, Yumi."
    y "Thank you! "
    s "Again, how long has this been going on?"
    yu "I just fucking told you. Forever, dude."
    y "He’s obviously talking about the two of us speaking again, you stupid bitch! Not how hungry I am!"

    scene yumiapt13
    with dissolve

    yu "Oh, well why the fuck didn’t you just say that? Yumi’s been stoppin’ by for, like...a month or two now?"
    yu "We ain’t on good terms or anything. She still wants me to die and I still think she needs to have some sense smacked into her, but we’re aight."
    y "We’re not {i}aight.{/i} I told you I’m only here because I wanted food."

    scene yumiapt14
    with dissolve

    yu "Yeah, yeah. Food or a couch to crash on — I know. Ain’t gonna hear me bitchin’ about it. Letting you sleep on the couch every once in a while’s the least I can do for spending your whole ass life elsewhere."
    y "Gee, thanks Yuki. All those years of growing up without a mom are totally worth it now that you’ll let me borrow your grimy-ass, beer-stained couch."

    scene yumiapt15
    with dissolve

    yu "Hey! At least half of those stains were on the couch when I snagged it off the side of the road! Don’t accuse me of shit I didn’t do!"
    s "I’m...happy for you two?"

    scene yumiapt16
    with dissolve

    yu "Was that a question? Either you’re happy or you’re not. Don’t be a fuckin’ sketch about it."
    s "I’m just saying it’s nice that you can be in the same room without killing each other. I wasn’t sure if that day would ever come."
    yu "Same here. Kinda fitting though how the thing that brought us together was Yumi getting kicked out of school."
    s "She’s back now, though. And all it took was a totally sincere apology speech that I’m definitely sure she remembers giving."
    y "What? What apology speech?"

    scene yumiapt17
    with fade

    s "Didn’t we talk about it during Christmas? How there was some speech that neither one of us-"
    y "The fuck are you talkin’ about? There was no {i}speech.{/i} Only reason I made it back into school was because Chika and the class prez vouched for me."
    s "Makoto? Why would Makoto ever do {i}anything{/i} for you?"
    y "Fuck if I know. Probably to get back at Nodoka for beatin’ her ass during the first Dorm War thing. "
    y "Also, I didn’t even fuckin’ talk to you on Christmas. I was babysitting. In fact, I’ve barely seen you at all lately. Kinda peaceful, now that I think about it. "
    s "So all of that stuff with the slumber-"
    y "Sorry, can we go back to why you’re hanging out with Yuki again? Because if you’re trying to fuck my mom, uhh...don’t? "
    yu "Yo, don’t tell your teacher who he can and can’t bone. Pretty sure that’s against the rules."

    scene yumiapt18
    with dissolve

    s "Thanks, Yuki. But I really wish you would have stepped in when you let her comment on the size of my penis earlier."

    scene yumiapt19
    with dissolve

    yu "Hey, man. I’m sorry you’re sensitive about the size of your penis or whatever, but if my daughter wants to say some dude has a tiny dick, she can say he has a tiny dick."
    yu "That ain’t even an insult. It’s just a thing we do to remind you that we’re the ones who run this shit. Not you."
    s "I wish you’d do that in a way that wasn’t inherently hurtful."
    yu "I wish you had a bigger dick so you wouldn’t be crying about this right now."
    y "Can we not talk about my teacher’s dick?!"
    yu "Why? You’re the one who brought it up first. Don’t write a check you can’t cash."

    scene yumiapt20
    with dissolve

    yu "Oh, did you know you have to go to like a “financial institution” or whatever to cash those? Because I tried doin’ that shit at the convenience store and they looked at me like I was a fucking alien."
    y "That’s probably the only useful piece of information I’ve ever heard from you."
    y "All that’s left now is to find an actual job, I guess."

    scene yumiapt21
    with dissolve

    yu "I’ve been tellin’ you, come work at the fuckin’ bar. Sara needs the help with shit gettin’ kinda busy now."
    y "And be around you for more than one hour a day? I’m good. I’d rather clean toilets or some shit. "
    yu "Even better. None of us like cleaning the toilets so we can just leave that to you. "
    s "Yumi, do you really not remember anything about-"
    y "I don’t know, Yuki...your boss seemed really fucking annoying. And I’m pretty sure her daughter is terrified of me. "
    yu "Oh, fuck yeah she is. But that’s cause you’re my daughter and intimidating people is just in our blood or whatever. But it’s no big deal. "
    yu "Just give it some thought. If somebody like me is able to make enough to find a place to live, you’d probably be able to make even more."
    yu "Plus, I can tell you now that the women who come to that place are fucking {i}deprived{/i} and those tits are gonna get people in the doors. "
    yu "I already dragged in all the girls who want to be dominated or beat up or whatever. You can handle the rest. Learn how to behave and you’ll probably land even more."
    y "Ew! Fucking ew! I’m not going to work somewhere where I just get hit on all day!"
    yu "Why not? They seem to like it when you’re mean to them."
    s "I think that might just be a you thing, Yuki."

    scene yumiapt22
    with dissolve

    yu "That {i}your{/i} thing too? Because if you want me to be mean to you, I can just do it. We ain’t gotta make out first."
    y "Okay, I’m out. Any more of this and I’m going to fucking puke."

    scene yumiapt23
    with dissolve

    yu "Nah, nah. Hold up a sec. I’ll kick this fucker out in a minute."
    s "You will?"
    yu "There’s just something I wanna talk to him about first."
    y "And I am needed here...why?"
    yu "You’re hungry, ain’t you? I’ll order a pizza or whatever. Just chill inside while I go talk to Douchebag McDouchefuck. Grab a beer for all I care. I don’t give a shit."
    s "I really hope that nickname doesn’t stick. Your family renames me too often and that is especially annoying now that I know my-"
    y "You realize I’m underage, right? I can’t drink."
    yu "Since when do you give a shit about the law? You steal TVs and had no problem buying me cigarettes the other day."
    y "Okay, fine. Beer just kinda tastes like shit. I’ll grab a water, though."
    y "Oh, and if he comes back in here with you, I’m out. Ain’t got time to watch you two be all buddy-buddy and shit all night."
    yu "Got it."

    scene black
    with dissolve2

    yu "Come on, McDouchefuck. Me and you are gonna have a little chat."

    "........."
    "......"
    "..."

    scene yumiapt24
    with dissolve

    s "..."
    yu "..."
    s "It’s “You and I.”"
    yu "What?"
    s "You said “me and you are going to have a little chat” when it should be “You and I are going to have a little chat.”"
    yu "Do you want to keep your balls?"
    s "I would prefer them to remain attached to my body, yes."
    yu "Cool. Then don’t correct me like that. I know I’m a fucking idiot, but it’s annoying when people just remind me."
    s "Gotcha...So, about what happened in there..."
    yu "What about it?"
    s "Isn’t that...what you wanted to talk about?"

    scene yumiapt25
    with dissolve

    yu "You mean about the thing with you wanting to hook up with me? Nah. That ain’t got shit to do with this."
    yu "Surprised the fuck out of me, though. Figured you were just messing around this whole time."
    yu "I also think it’s a shit idea for the two of us to go down that path since I’ll only wind up draggin’ you into my never-ending sob story, but that ain’t what I wanted to talk about."
    s "Then what-"
    yu "I want to know what the fuck happened with Yumi and that Nodoka girl. She won’t tell me shit."
    yu "I was fine with that at first, but the more I think about it, the more fucked up I’m getting."
    yu "I didn’t teach her much, we all know that, but I know damn well she wouldn’t fuck someone up {i}that{/i} bad unless she had a reason to."
    s "And what makes you think I know that reason?"
    yu "She told me."
    s "Oh."
    s "Well yeah, that’s pretty damning."

    scene yumiapt26
    with dissolve

    yu "The fuck you have to gain from hiding it? Ain’t like I’m gonna do anything. I just want to know what the fuck is going on."

    scene yumiapt27
    with dissolve

    s "This isn’t really something I should let myself get dragged any further into. If Yumi can tell you that I know what’s going on, she can definitely tell you what happened herself."

    scene yumiapt28
    with dissolve

    yu "Just because she’s sleeping on my couch and eating my TV dinners doesn’t mean she’s gonna just spill her heart out to me."
    yu "Doubt we’ll ever get to that level after the shit we’ve been through. But I’m still gonna worry about her. "
    yu "And...I don’t want to say I {i}deserve{/i} to know what’s going on in her life, but..."

    scene yumiapt29
    with dissolve

    ima "Uhh...hello? The hell are you doing here? You can’t just come all the way to my apartment complex and then only hang out with my neighbors. "
    ima "I’ll admit that I’ve heard your voice in my head on several occasions, but I seriously thought I was going insane tonight with how much of it I heard. You’ve got some explaining to do."
    yu "Friend of yours?"
    s "Subordinate. "

    scene yumiapt30
    with dissolve

    ima "{i}Subordinate?!{/i}"
    ima "Is that all I am to you? Because I’m all about power dynamics, Senpai, but not like this!"
    s "Surprise. I’m here because I missed you."
    yu "I was just the appetizer. He’s all yours now...whatever your name is."

    scene yumiapt31
    with dissolve

    ima "Imani Imai. Nice to finally meet you, intimidating onee-san in the room next to mine."
    yu "Yuki Yamaguchi. Think I gave you a beer during that weird ass contest thing you guys had at Sakaki-bar-a. Nice to actually meet you for real this time."
    ima "You know, I {i}knew{/i} I recognized you from somewhere and-"
    ima "Sorry, did you say “Yamaguchi?”"
    yu "Yup."
    ima "Welp, that certainly explains the other familiar auditory hallucination I just had as well. Glad that mystery is over and done with."
    s "Are you going somewhere?"
    ima "My boyfriend’s house."
    s "Cool. Have fun."

    scene yumiapt32
    with dissolve

    ima "He doesn’t mean that. We’re closer than this. Oh, Senpai. You’re so funny."
    s "She’s probably just going to the bar to meet up with some of our other friends. We do that sometimes."
    yu "Really? Only saw her there the one time, I think. Maybe two, but that’s pushing it."
    s "Not your bar. Another bar."

    scene yumiapt33
    with dissolve

    yu "{i}Another{/i} bar?! You’re cheating on us?"
    ima "{i}Us?...{/i}"
    s "I can explain. "
    yu "Sara’s heart’s gonna fuckin’ shatter. "
    s "Then don’t tell her."
    ima "Senpai, just out of curiosity, is there any woman in Kumon-mi that you are not having sex with?"

    scene yumiapt34
    with dissolve

    s "Yes, but {i}not for long.{/i}"
    ima "I really worry about you sometimes."
    yu "Uhh...anyway, sorry Imani, but this guy and I were in the middle of a pretty private conversation and...you’re gonna have to get the fuck out of here."

    scene yumiapt35
    with dissolve

    ima "Understood! I’ll go be jealous somewhere else! But, should you ever find yourself without anything to do, you should join us at that dive around the corner! That’s our spot now."
    ima "How cool is that? We have a spot. We’re a group of friends with a spot. I’m finally popular after all these years!"
    s "It’s time to leave, Imani."

    scene yumiapt36
    with dissolve

    ima "You’re going to appreciate me one day. Mark my words, Senpai."
    s "I would appreciate you more off-screen."

    scene yumiapt37
    with dissolve

    ima "God, is this really what Makoto’s been dealing with all year long?! Why are you so mean to the people who help you the most?!"
    yu "..."
    s "..."
    yu "Are you two-"
    s "No. Not yet at least. We’re just friends."
    yu "Gotcha..."

    scene yumiapt38
    with dissolve

    s "Anyway, about the Yumi thing-"
    yu "Let’s...take a rain check on the Yumi thing. I’ll see if I can get any more out of her since I know you ain’t gonna tell me shit."
    yu "Go join your friend at the bar. Seemed nice. And a lot closer to your age than a certain someone you almost made the mistake of kissing tonight."
    s "It wouldn’t have been a mistake."
    yu "It would have. But it’s cool. Sometimes people get caught up in the moment or whatever. Ain’t gonna hold it against you."
    yu "But, before you go telling me I’m wrong again, do me a favor and get the fuck out of here. Yumi’s gonna bail if I stay outside any longer and the cheapest pizza place around is gonna be closing soon."
    s "You sure you don’t want to come to the bar as well? One of the girls is both older {i}and{/i} more heavily tattooed than you."
    yu "Oooh, tempting. She have an unruly daughter as well?"
    s "If by “unruly” you mean “impulsive and horny” then yes."
    yu "Maybe some other time. Secretly, of course. "

    scene yumiapt39
    with dissolve

    yu "Got somethin’ else I should be doin’ right now. Would be an idiot to walk away from that again, even if it is temporary."
    s "I’m proud of you, Yuki. "
    s "You’re doing well."

    scene yumiapt40
    with dissolve

    yu "Save it for the next girl you try to seduce, won’t ya? Got at least one both older {i}and{/i} more heavily tattooed than me waiting for you right now."
    s "Yeah...but she’s kind of..."
    s "Uhh..."
    s "I’ll just...wait until you meet her."

    scene nightsky
    with dissolve2

    "Yuki heads back into her apartment as I make my way down the stairs."
    "Seeing as I am now abandoning my original plans and heading to the dive bar instead, I send Imani a text and manage to catch up with her just before she heads inside."

    scene black
    with dissolve2

    "I hope that everything went well with the Yamaguchis, but I guess I probably won’t know that until the next time I’m able to see Yuki."
    "It’s strange, though. I remember Yumi saying something about how she spoke to her mom, but...I don’t think it was at {i}this{/i} level prior to the last reset."
    "This has to be some sort of aftereffect from that, doesn’t it?"
    "I guess I’ll just have to...keep an eye out."
    "Because as nice as it is that the two of them were able to grow a little closer without me around-"

    stop music

    "I am frightened by the idea of anyone progressing without me."
    "I want to be there for the ups and down."
    "I want to watch the world move."

    $ renpy.end_replay()
    $ yukidate20p2 = True
    $ yuki_love += 1
    $ imani_love += 1

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukidate25:
    scene yukibikeride1
    with fade
    play music "calmbar.mp3"

    sar "Are you sure you’re okay with doing this for me? Because I know it’s a pretty big ask."
    yu "Ain’t nothin’ I haven't done a million times before. Don’t worry about it."
    sar "Thank you, Yuki. And if there’s anything I can do to pay you back, let me know."
    yu "I mean...you can literally pay me. That would work."
    sar "If there is anything else I can do to pay you back, let me know."
    s "What’s going on? Sara trying to coerce sexual favors out of you again?"

    scene yukibikeride2
    with dissolve

    sar "Hah...{i}no.{/i} I gave up on that months ago."

    if sarasex == True:
        sar "No offense, Sensei. You’re an exceptional bedroom partner and I wouldn’t trade our moments of intimacy for the world...but Yuki is {i}Yuki.{/i}"
        sar "There are simply some things a woman can do to another woman that a man would never be able to. And Yuki seems to have missed the memo that everyone is bisexual in 2020."
    else:
        sar "You know, back in the old day, {i}everyone{/i} wanted a piece of this. Now, {i}no one{/i} does and it’s making me very self-conscious."

    yu "Yo. You ain’t got shit going on tonight, do you? Could use some help with something."
    s "Is it the thing Sara just asked for {i}your{/i} help with? Because I’m still not convinced it isn’t sexual."
    yu "Just some work shit. Reason she’s bein’ all thankful is my shift already ended."

    scene yukibikeride3
    with dissolve

    sar "And with the amount of money I’ve been pumping back into the business lately, I can’t really afford to pay Yuki overtime. "
    s "What does she need to do exactly? Because I think you guys may have pushed the whole handing out fliers thing as far as it can go."
    yu "Gotta go pick up some machine or whatever. Ain’t a problem. Moved plenty of shit back when I was a drifter. "
    sar "Isn’t Yuki the coolest? Like, who can actually say “back when I was a drifter” and be serious about it? "
    s "It becomes a little less cool when you realize half of that shit probably didn’t belong to her and was pawned off so she could get high."
    yu "Hey, there was other shit. I bought food too. And bike parts. You’re underestimating just how cheap drugs are, man."
    sar "Would you mind going with her? I feel bad making Yuki lug a whole appliance all the way back here by herself."
    yu "Ain’t like this guy’ll be much help. Might look kinda big, but I’ve run into plenty of guys even bigger than him who wound up being total fuckin’ pansies."
    s "I’ll go if Yuki promises to stop insulting me."

    scene yukibikeride4
    with dissolve

    yu "What? It ain’t an insult if it’s the truth. If you’re gonna bring up the drugs, I’m gonna bring up how your bones are probably made out of marshmallows or some shit."
    s "Well, it sounds like my only choice is to tag along and show you just how much of a man I am."

    scene yukibikeride5
    with dissolve
    stop music fadeout 20.0

    sar "Just don’t show her {i}too{/i} much or I will be very jealous! And remember that it takes significantly less to impress me!"
    s "I am well aware, Sara. But thank you for reminding me."
    yu "Ready to hit the road, then? Should get a move on now before it gets too late. Gotta go all the way downtown to pick this shit up."
    s "Downtown? But how are we going to-"
    yu "Follow me outside and I’ll show you."

    scene black
    with dissolve2

    "Yuki didn’t get a car, did she?"
    "The apartment is one thing — and a thing I was able to overlook for the most part seeing as it is not a very {i}nice{/i} apartment. "
    "But a car? In a city with cheap, functional public transportation? No wonder Sara isn’t able to pay her for overtime if her wage has gone up that much."
    "The two of us step outside of the bar as Sara slips back into work-mode and attempts to hold down the fort while her only other employee tonight is away."
    "But considering Yuki’s shift already ended, Sara probably knows-"

    s "Wait, what the fuck is this?"

    scene yukibikeride6
    with dissolve2
    play music "retrospect.mp3"

    yu "My pride and joy, obviously."
    s "Your pride and joy has double D’s and anger issues. This is a motorcycle."
    yu "Why even ask if you already know what it is, fucker?"
    s "Aren’t we going to pick some up appliance or something? How are we supposed to do that on a motorcycle?"

    scene yukibikeride7
    with dissolve

    yu "This ain’t just a {i}motorcyle,{/i} man. It’s an 1,100 cc-"
    s "Yuki, I’m going to cut you off right there as I can already tell I’m not going to understand anything you’re about to say. The moral of the story is that I’m not riding that. The end. See you later."

    scene yukibikeride8
    with dissolve

    yu "What happened to showin’ me how much of a man you are, huh? You a little pussy ass bitch after all? Worried you’re gonna get a boo-boo?"
    s "I’m worried I’m going to {i}die.{/i} Not to mention how there is literally no way we’ll be able to-"

    scene yukibikeride9
    with dissolve

    yu "Relax, man. Ain’t nothin’ to be scared about. Been riding for almost as long as I’ve been walking. You’re safe with me."
    yu "Plus, ain’t a way in hell I’d let anything happen to my baby."
    s "The disparity between how much you like your motorcycle and how much you like me is so great that I can’t even pretend to think you were referring to me as “your baby” just now."
    yu "Uh-oh. You goin’ cougar-hunting again? Things not work out for ya at the bar after last time? There’s an easier target right inside, you know. And that one’s only a {i}little{/i} bit older than-"
    s "Whatever, fine. I’m not here to go “cougar hunting.” I’m here to prove my masculinity. Plus, you wouldn’t be a cougar anyway because cougars actually {i}go after{/i} prey."
    s "All you do is pretend you don’t want to have sex with me."

    scene yukibikeride10
    with dissolve

    yu "Oh, come on man. You know damn well I’m just fuckin’ around and I wouldn’t-"
    s "Yeah, whatever. Let’s just do this before I change my mind."

    scene yukibikeride11
    with dissolve

    yu "You sure? Cause I ain’t stoppin’ once we’re on that thing."
    s "I’m sure."
    yu "Don’t have a helmet either. If we wipe out, we’re basically fucked."
    s "You should probably invest in a helmet if you’re going to be actively riding this thing, but yeah. I’m still in. "
    s "I’m trusting you, though. And I will not hide the fact that I am only doing this because I think it will increase the probability of you accepting my advances."
    yu "Luckily for you, we’re gonna have to get {i}real{/i} close on there. Hope you don’t pop a boner just from grabbing onto my waist."
    s "I make no promise. Now, let’s do this."

    scene black
    with dissolve2

    "Yuki hops onto the bike and pats the space behind her for me to come sit down. "
    "Up until now, I’ve successfully avoided ever having to do anything like this. And while I definitely {i}could{/i} have walked away tonight as well, I felt like I...shouldn’t for some reason."
    "Call it a desperate lunge forward if you will — a chance to further myself in an area I have stagnated in for no reason other than to hopefully have sex with a student’s mother."
    "It’s not a car. "
    "I don’t know how it will make me feel and I don’t know how safe I will truly be."
    "But it’s not a car."
    "I tell myself that repeatedly as I sit down behind her and wrap my hands around her waist."
    "........."
    "......"
    "..."

    scene yukibikeride12
    with dissolve2

    yu "Comfortable?"
    s "It’s not...the worst."

    "Yuki starts slow and cruises through the neighborhood surrounding the bar at what I imagine is well below the speed limit."
    "The sensation of the wind in my hair, while I’m sure it’s liberating for some, feels to me as if I’m being repeatedly pelted by the fists of a half-corporeal god."
    "It is there and it is tangible, though it moves right through me the way an arrow would if I was any good at thinking up metaphors on the back of a metal death trap."

    yu "Just hang in there, aight? I don’t mind if you grab me a little bit tighter."
    yu "I know I’ve been kinda flighty in the face of your “advances” lately, but I’m willing to make an exception while we’re on my bike."
    s "So it’s cool if we make out now?"
    yu "Sure, so long as you want to die. I’m good, but not “ride with my eyes closed” good."
    yu "If you wind up grabbin’ my tits on accident, though, I ain’t gonna kick the shit out of you."
    s "It’s not like there’s much to grab in the first place."

    scene yukibikeride13
    with dissolve

    yu "Oi, only I get to mock my chest. Ain’t cool when you do it. Just sounds like you’re tryin’ to compensate for somethin’."
    s "Maybe I am."

    scene yukibikeride14
    with dissolve

    yu "Oh yeah? That shit Yumi say the other night about you havin’ a tiny dick have any truth to it? "
    yu "Ain’t gonna hold it against you if she’s right. Ain’t cool to measure how much of a man someone is by the pistol they’re packin’."
    s "Oh, no. My penis is massive. But being back here does sort of emasculate me."
    yu "Em...asculate? What’s that? That a sex thing? You ain’t gonna cum on my jacket, are you?"
    s "For lack of a better term, it makes me feel like a bitch."
    yu "A bitch? Nah. I don’t see it that way at all. "
    yu "A bitch would have...you know, bitched out. You’re tryin’ something new and you oughtta be respected for that."
    s "Even if it means hanging onto the waist of someone who is both smaller than me {i}and{/i} a woman?"
    yu "The fuck’s bein’ a woman have to do with anything? You think you’re supposed to be bigger and stronger than me just cause you’ve got a dick? Nah. "
    yu "Maybe fifty years ago, but it don’t work like that anymore."
    s "I know. I’m just, and please excuse the pun, not in the backseat very often. "
    s "So it makes me feel a little more submissive and...I guess more feminine than I’m used to. That’s what I meant by being emasculated."
    yu "Well, I still don’t know shit about this whole “emasculated” thing, but I really ain’t all that concerned about any of that “feminine or masculine” crap at the end of the day."
    yu "People are people, man. Why are we always assignin’ weird ass words and titles to ‘em when everybody’s different?"
    yu "You think {i}I{/i} ever felt “feminine?” Nah. Been gettin’ shit for not bein’ {i}girly{/i} enough my whole life. Just look at me. But like, who even gives a shit? "
    yu "Not like it makes any sorta difference when we’re all just tryin’ to get by out here."
    yu "If the world wants to think I’m not bein’ a “real” girl cause I’m sittin’ in the front while there’s a dude in the back holdin’ onto me, the world can go fuck itself."
    yu "All that shit’s just meant to keep us down, you know. "
    yu "Be this...Be that...Boys don’t cry...Girls play with dolls. All bullshit. If you want to cry, {i}fuckin’ cry.{/i} You want to play with dolls? {i}Play with fuckin’ dolls.{/i}"
    yu "Don’t feel pressured to label yourself just cause you’re doin’ somethin’ people think is weird or different. All that’ll do is a paint a fuckin’ target on your back."
    yu "It’s like gangs, dude. Same people, same ideals — killin’ each other over fucking colors because that’s what they were told to do. "
    yu "People nowadays are so focused on bein’ a part of somethin’ that they’re missin’ out on all life has to offer. "
    yu "We gotta stop forming teams and just accept that we’re all fuckin’ weird when it really comes down to it. "
    yu "It ain’t our balls or tits that tell us how we’re supposed to be or act, its our brains and our hearts. And that shit looks the same no matter who you pull it out of. You know?"
    s "Yeah...but I’m a little surprised you went on such a heated rant about it based on one offhand comment I made."
    yu "I just hate people thinkin’ they’re {i}supposed{/i} to be a certain way, you know?"
    yu "I like you cause you’re you. You don’t gotta be the fuckin’ 1950’s poster-boy for manliness. You’ve just gotta respect me and not make me feel like a piece of shit all the time. That’s all."
    yu "Should be that way for everyone...but we all just want to hate each other now."

    scene yukibikeride15
    with dissolve

    yu "I don’t know. Maybe I’m just too old for this shit and I ain’t really gettin’ it or something."
    yu "Just know I ain’t gonna judge you for sittin’ back there. And I’d be hard pressed to think you’d judge {i}me{/i} for sittin’ up {i}here.{/i}"
    s "..."
    yu "..."
    s "Thank you for the motivational speech. I now no longer feel emasculated in telling you to keep your eyes on the road."

    scene yukibikeride16
    with dissolve

    yu "You got it, princess. Or {i}prince.{/i} Or whatever the fuck you want to call yourself cause they’re all the same exact fuckin’ thing. Same crown, different jewels. Feel me?"
    s "I...don’t think that’s accurate. Nor do I even know if princes and princesses even wear crowns?"
    yu "I ain’t got a fuckin’ clue either. Just talkin’ outta my ass at this point. Feels good rantin’ to somebody for once, though."
    yu "Ridin’ for me has always been a time to get my thoughts together. Everything always clogs up once I stop movin’, so the wind helps rattle my brain and make shit clear again."
    yu "Ain’t sure if you’ll ever wanna do this again after tonight, but..."
    yu "Would be nice havin’ you."
    s "I’ve barely even said anything, Yuki..."
    yu "I know, I know."
    yu "But the wind can get cold at night. And right now?..."

    scene black
    with dissolve2

    yu "You’re keeping me warm as fuck."

    "........."
    "......"
    "..."

    scene yukibikeride17
    with dissolve2


    s "I’m going to puke. "
    yu "First ride’s always the hardest. You’ll do better on the way back. "
    s "I’ll call us a taxi. I don’t think I can do that again."
    yu "Ain’t gonna be able to fit Sara’s big ass espresso machine in a taxi."

    scene yukibikeride18
    with dissolve

    s "But we can fit it on a motorcycle?..."
    yu "Hell yeah we can. We’ll just ride carefully. Don’t have to worry about the roof of a car holdin’ us down. How’s your upper back strength? Need a quick massage?"
    s "Right now is probably the only time in recent memory that I don’t want to be touched by you...or anyone, for that matter."
    yu "Well, take a few minutes to catch your breath or whatever. But after that, we’ve gotta move our leg-hands. "
    s "Oh no...Not you too..."

    scene yukibikeride19
    with dissolve

    yu "Come to think of it, you seen Kaori lately? Cause she’s been actin’ weird as shit the last few times I’ve called her."
    s "Is she ever...{i}not{/i} weird?..."
    yu "Like...weird by even her standards. Which is probably hard to understand, but...I don’t know. Just keep an eye out for her, I guess."
    yu "Worried all those jobs she has might finally be catchin’ up with her. Don’t want her burnin’ out."
    s "I’ll see what I can do..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "After a few minutes go by and I’m still no better than when I first got off the bike, Yuki gets tired of waiting and drags me by the arm toward a restaurant supply store."
    "As it turns out, a normal espresso machine (Which, might I add, is not a thing a bar even needs) just wasn’t going to cut it and Sara felt compelled to order the deluxe one instead."
    "And while I am in no physical or mental state to question this [[horrible] business decision of hers, I will say that it’s good to see she’s at least {i}trying{/i} to do something."
    "What is {i}not{/i} good, however, is that it now falls on Yuki and me to get this thing all the way back to the bar..."
    "And it is {i}very{/i} heavy."

    $ renpy.end_replay()
    $ yukidate25 = True
    $ yuki_love += 1

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saraspecial30p1

label yukicamp1:
    scene sky
    with dissolve2
    stop music fadeout 30.0

    "I peer up at the sky through a break in the trees and find a moment of comfort in convincing myself I’m not surrounded when I know I really am."
    "That, too, is somewhat poetic. Yet less so than it would be to die in the same way that I was more symbolically killed many, {i}many{/i} years ago."
    "There’s poetry in everything, though. "
    "That’s something I’ve believed forever. "
    "But I often find myself wondering whether I believe that because it’s what’s real to me or because it’s what someone else made me see after peeling away the covers."
    "And I often find myself wondering if those two thoughts are mutually exclusive because there’s a fine line between reality and what’s really {i}real,{/i} you know? "
    "It’s interesting how deeply the people we look up to when we’re young are able to affect us, isn’t it? "
    "And how, despite all the adversity and turmoil in the face of those teachings, changing {i}at all{/i} when you get to my age seems nigh impossible."
    "Ami’s still young. So, if I want to mold her world, I need to do it now. "
    "Because waiting any longer not only runs the risk of ill-preparing her for what surely awaits us in this infinite life of ours-"
    "But runs the risk of turning her into an actual monster who will pry open my ribcage before ripping my heart out and swallowing it whole."
    "Girls these days will do crazy things for sustenance, you know. Or perhaps even leisure if you want to make her out to be even worse than she actually is."
    "But I know the truth."
    "She’s just broken and in love. And the two of those things can easily drive us mad on their own."
    "When they’re combined, though?..."

    yu "Yo!"

    "When they’re combined, there’s nothing that can stop the metamorphosis other than someone who exhibits the same symptoms."

    scene yukicamparrive1
    with dissolve2
    play music "recovery.mp3"

    "As much as I’d love to inform you of our proper diagnoses, I’m afraid there’s not a doctor in the world we could pay to make sense of how our insides look or how they communicate with and respond to one another."
    "I just know that they do."
    "So maybe that’s “love” working its magic again. Or maybe it’s just the worm."
    "Whatever it is, though- know this one thing for sure."
    "Our time is numbered."
    "This will almost certainly be fatal. "

    yu "Took you guys long enough. Been waitin’ here for like an hour already."
    sar "I’m surprised your bike even made it here. I kind of assumed you’d just be hiking or something."
    yu "Nah, I just brought my crappy old one. Had to drag it through a few puddles on the way over, but it got here in one piece either way."

    scene yukicamparrive2
    with dissolve

    a "Sensei, who is that? She looks...kind of familiar."
    s "Yumi’s mom. You’ve probably seen her at Sara’s bar for one of the parties."
    sar "Call it by its proper name! My ancestors didn’t come up with such a great pun just for it to be ignored by someone with no sense of humor!"

    scene yukicamparrive3
    with dissolve

    yu "I’m Yuki. Ami, right?"
    a "Oh, yeah. Sorry. It’s...nice to meet you?"
    yu "Likewise. Sorry if my daughter’s ever picked on you before. Which she probably has because she’s a fuckin’ bitch."
    h "Are you staying the night, Yuki? We’re giving Sensei and Ami the second tent, which means the rest of us will have to get kind of close."

    scene yukicamparrive4
    with dissolve

    yu "Wasn’t plannin’ on it, but now I definitely ain’t plannin’ on it. Y’all can enjoy your fuckin’ slumber party on your own. I’m just gonna head back and crash once it gets dark."
    h "Worth a shot. "
    sar "Are you sure, Yuki? We don’t open back up until tomorrow night, so it’s not like you have anywhere to be unless you have a secret Yakuza boyfriend you haven’t told any of us about."

    scene yukicamparrive5
    with dissolve

    yu "Just because the only dude I’ve ever {i}been{/i} with was in the Yakuza doesn’t mean that’s my {i}type,{/i} you know. I can like normal dudes."
    sar "So you have a normal boyfriend instead? "
    yu "Sure. Yeah."
    sar "What’s his name?! When can we meet him?!"

    scene yukicamparrive6
    with dissolve

    yu "It’s that guy right there. We got together for Yumi’s sake and he just finished movin’ into my place. Got a dog and everything, which means we’re basically a real family now."
    s "Please don’t make jokes like that in front of Ami or you’ll wind up waking up with fewer body parts than you’re accustomed to."
    yu "Damn, now I {i}definitely{/i} ain’t sleepin’ here."

    scene black
    with dissolve2

    "A brief argument about my relationship status subsequently takes place, but I decide to black most of it out as I can tell it’s making Ami uncomfortable."
    "I can tell this entire {i}trip{/i} is making Ami uncomfortable. But it’s not like I didn’t expect that to happen. And, to be completely honest, I’m probably even {i}more{/i} uncomfortable than she is."

    if amifingered == True and sarasex == True and makisex == True and harukasex == True:
        "Like, I’m having sex with {i}all{/i} of these girls apart from Yuki and that could spiral into something {i}horrible{/i} pretty quickly if I say or do just one thing wrong."

    if amifingered == False and sarasex == False and makisex == False and harukasex == False:
        "Like, every single one of these girls wants to fuck me except Yuki (maybe) and I’ve yet to touch {i}any{/i} of them, so I’m practically a sitting duck out here."

    "But I don’t matter today — and that’s saying a lot as someone who’s practically the symbol of self-loathing narcissism. "
    "I’ll just stick to my guns and try to not let anything put me on the back foot for the next twenty-four hours so I can focus more on Ami."

    yu "So! Wanna go for a walk, big dog?"

    scene yukicamparrive7
    with dissolve2

    s "Please never call me “big dog” again. I was quite literally just thinking about how I don’t want anything to put me on my back foot so I can focus on Ami."
    sar "Then I’ve got {i}extra{/i} bad news for you since I’m going to kidnap her now."

    scene yukicamparrive8
    with fade

    s "Why is everything I don’t want to happen suddenly happening in very quick succession? Are even my inner monologues not safe anymore?"

    play sound "static.mp3"
    scene yukicamparrive9 with flash
    play sound "broken.mp3"

    "{b}lmaoooooooooo{/b}"
    "Oh, come on."

    play sound "static.mp3"
    scene yukicamparrive8 with flash
    stop sound
    play music "recovery.mp3"

    a "You’re kidnapping me?"
    sar "Yeah! Let’s go set up your tent while Maki and Haru-chan put the other one together. Then, after that, I can show you a trick that’ll help you get rid of those dark circles."
    s "I don’t think-"
    h "We’ve got a long day ahead of us, Sensei. It’s probably best to just let Sara get all of her motherly energy out of the way now since {i}her{/i} daughter’s not here to serve as the outlet for that."
    maki "Just not {i}that{/i} kind of motherly energy."
    h "No one said anything about {i}that{/i} kind of motherly energy, Maki."
    maki "But we were {i}all{/i} thinking it."
    h "We most certainly were not."
    s "I was."

    scene yukicamparrive10
    with dissolve

    a "You {i}were?{/i}"
    maki "See?"
    h "I admit defeat. I have underestimated the depravity of this group. Which, in hindsight, was extremely foolish of me."

    if harukapredator == True:
        "And doubly foolish as she is essentially my sex-slave now and would suck me off in front of everyone here with just the snap of my fingers."

    scene yukicamparrive11
    with fade

    yu "The fuck’s even goin’ on right now?"
    sar "Don’t worry about it, Yuki. If Maki keeps talking, her words will sully your status as the most innocent woman here."
    yu "There’s a friggin’ teenager here. Ain’t no way I’m more “innocent” than her."

    "If only she knew."

    a "Uh...Sana’s mom? Can we-"
    sar "Stop calling me that! Just Sara is fine. Or Mom! Or Mama. Or Mommy."
    sar "Actually, no. Mommy might be kind of weird. But the others are-"
    a "{i}Sara...{/i}do we really need to do this now? I’m...okay with spending time with you, of course. But right now, I want to-"
    sar "Shh! It’s fine! We can get to know each other a little better while your uncle explains the different types of motherly energy to Yuki — a woman who, despite being a mother, is unfamiliar with all of them."

    scene yukicamparrive12
    with dissolve

    yu "You really gonna throw shade at me all casually like that? I’ve barely even said shit."
    s "Is there a reason you want to go for a walk? Because, if not, I kind of want to stay here and make sure Sara doesn’t force Ami to sign any adoption papers."
    sar "Now just sign here and-"
    h "Yoink."
    sar "Noooo! My newest daughter!"

    scene yukicamparrive13
    with dissolve

    yu "There’s somethin’ I wanna talk about, but I ain’t good at doin’ that shit in front of other people. Shouldn’t take long, though. You can get right back to chaperoning your niece in a few minutes."
    s "Then, I guess it can’t be helped."

    scene black
    with dissolve2

    s "I’ll be right back, Ami. Just humor Sara for now. "
    a "If...that’s what you think is best..."

    "Yuki leads me into the woods and given that she is much stronger and more intimidating than me, I can’t help but trick myself into thinking I’m about to be mugged for everything I’ve got."
    "Which isn’t much, to be honest."
    "But she could probably fetch a pretty penny for auctioning off my niece to some underground organization specializing in human trafficking or the selective breeding of redheads."
    "I doubt Sara would be in on that, though. She seems to like young girls a little too much to try shipping any of them off. "
    "Which kind of sucks for Haruka if you think about it. Because she likes them a lot too, but in a completely different way."
    "So yeah, that’s what I’m thinking about as we move further into the woods."

    yu "So..."

    "But, of course, Yuki is thinking about something completely different."

    scene yukicamparrive14
    with dissolve2

    yu "Sara tells me you’re lookin’ to be like more of a dad to Ami or some shit?"
    s "Do secrets just not exist to women or something?"
    yu "That shit don’t exist to anybody, man. Sure you’d be gossipin’ with your guy friends too if you weren’t a creep who only hung out with people who have vaginas."
    s "Well, forgive me but my options are pretty limited in a city where men basically just don’t exist."

    scene yukicamparrive15
    with dissolve

    s "You’re right, though."
    s "I doubt much would change even if they did."
    yu "Ain’t nothin’ wrong with sharin’ secrets so long as it gets more people on your side, I think. And Sara only told me to begin with since I’m goin’ through the same shit with Yumi right now."

    scene yukicamparrive16
    with dissolve

    s "You are?"
    yu "Yeah. Tryin’ to, at least. But it ain’t exactly easy when I’ve been even more absent than you’ve been for the entire time you’ve known Ami."
    yu "Which means you’ve still got the benefit of havin’ her like you and that’s a thing I ain’t ever had. But I also get that shit’s probably a little more confusing on account of you not bein’ her actual {i}dad{/i} in the first place."
    s "So that’s why you wanted to go for a walk? Are we going to give each other tips on how to be bad parents?"

    scene yukicamparrive17
    with dissolve

    yu "That ain’t it, man. Just want you to know that I understand what you’re goin’ through and that it’s totally fine if all of this makes you feel like shit."
    yu "Knowin’ you failed somebody you could have turned into a great person stings. And it sucks extra hard because that shit just hits you outta nowhere sometimes."
    yu "Like, I ain’t gonna lie, there were long periods where I forgot I even {i}had{/i} a daughter. But bein’ around her again has been makin’ me realize just how fuckin’ dumb I was to not, like...keep her in my thoughts, you know?"
    s "Do you love her?"

    scene yukicamparrive18
    with dissolve

    yu "{i}Love,{/i} huh?"
    s "Yeah."
    yu "Do you love Ami?"
    s "I do."
    yu "How do you know that? Like...what’s different about the way you look at her than you would look at somebody like Sara or...any of your other friends I don’t know shit about?"
    s "I think it comes down to how much pain you’re willing to withstand to prevent that person from going through the same thing."
    yu "Does it really work that way?"
    s "No. But I still think that’s a good way to measure it. So, if you’d be willing to hurt yourself in exchange for Yumi’s continued “happiness,” I don’t think it’s crazy to say you love her."
    yu "See, that’s where shit gets hard though, isn’t it? Because you and me don’t really give a fuck about ourselves. "

    scene yukicamparrive19
    with dissolve

    yu "But at least you’re healthy and shit. I’ll be lucky to get another ten years outta life with how much smoking and drinking I do. And that ain’t even countin’ all the doping I did the last couple decades."
    yu "So yeah, I’d be fine with gettin’ hurt if it’d prevent Yumi from feelin’ that shit. But I’d probably do the same thing for you as well and I sure as fuck don’t love {i}you.{/i}"
    s "Maybe you do?"

    scene yukicamparrive20
    with dissolve

    yu "That boyfriend joke from earlier go to your head or something? "
    s  "Maybe. Or maybe I just liked the idea of being a real family and want to hear your daughter call me Daddy?"

    scene yukicamparrive21
    with dissolve

    yu "I’m just gonna go ahead and pretend you meant that in the less creepy way."
    s "You took that better than I thought, so maybe you don’t love her after all?"
    yu "Maybe I do, maybe I don’t. Shit’s complicated. Can’t really make sense of how I actually feel."
    yu "But I’ve been seein’ her more often lately..."
    yu "I buy extra shit for her when I go to the store now."
    yu "Even text her to see if she wants to get dinner or some shit a few nights outta the week. And, you know...sometimes she does. And I like that."
    yu "But it feels fuckin’ weird because, like...{i}why?{/i} Why’s she still showin’ me kindness like that after all the shit I put her through? Cause if my parents pulled that shit with me, ain’t no way I’d crash on their couch."
    s "Probably because {i}she{/i} loves {i}you.{/i}"
    yu "Yumi doesn’t love me. She’s smarter than that."
    s "Love isn’t really something you can apply logic to, Yuki. "
    yu "You think?"

    scene yukicamparrive22
    with dissolve

    s "Probably. "
    s "I’m also kind of in the dark when it comes to that."
    s "But right now, what matters most to me is making sure that Ami doesn’t wind up feeling like this one day. And I think you’re doing a good job of doing that same thing for Yumi."
    yu "Truth be told, I think we’re doin’ pretty shitty jobs when push comes to shove. But in a race, it ain’t how ya start that matters, it’s how ya finish. And there ain’t no way that growin’ up isn’t a race."
    yu "Blink once and a year goes by. Blink twice and suddenly it’s harder to breathe. Blink a third time and you’re five inches shorter."

    scene yukicamparrive23
    with dissolve

    yu "Life goes by too fuckin’ fast, man. And we’re terrible people for forcin’ those girls to go through it."
    s "Technically speaking, I’ve never brought anyone into this world. So I’m not {i}forcing{/i} anyone to do anything."
    s "But I’m not helping either. And that’s what this trip is about."
    yu "I feel you there. I tried inviting Yumi but, of course, she had other shit going on."
    yu "She has a job now. Did you know that?"
    s "Yeah. I ran into her the other night when I was about to jump off a bridge."

    scene yukicamparrive24
    with dissolve

    yu "She save you?"
    s "In a way, maybe."
    yu "That’s my girl."
    s "You could show a little more concern for {i}me{/i} you know."
    yu "You really think I’ve got the emotional capacity to worry about more than one person? "

    scene yukicamparrive25
    with dissolve

    yu "Just thinkin’ about Yumi’s hard enough to-"

    scene yukicamparrive26
    with dissolve

    yu "Woah, what the fuck? Is that Kaori over there?"

    scene yukicamparrive27
    with fade

    s "That...is Kaori. Yes."
    yu "Did she...kidnap somebody?"
    s "Technically? Yes. But it’s a little more complicated than that."

    scene black
    with dissolve2

    yu "Yo! Kaori! "
    k "Who goes to the place where we are located?! Stand back or face the wrath of my liquid pepper!"
    k "Wait...Aunt Yukiburger? And uncle Friendburgerhamfriendburgerman?!"
    na "???!!!!??!"

    scene yukicamparrive28
    with fade

    k "Why are the three minus one of you spending your unday with an S inside the town where trees live?"
    yu "Same question goes to you, yo. The fuck you doin’ out here in the woods with a kid?"
    na "!!!"
    s "Hello, Nao. Cool frog."

    scene yukicamparrive29
    with dissolve

    na "!!!!!!!!!!"
    k "This is no childburger, it is Nao-chan. And I am her mothermom, which makes you her motheraunt."
    yu "It makes me what?"
    k "Motherauntmomburgermomyuki."
    s "Nao doesn’t speak. And if you feel a strange, otherworldly presence emanating from her, you are not alone for I, too, feel that way."
    yu "So Kaori kidnapped a mute kid and dragged her into the woods so she could play with a frog? Aight."
    k "Frog Boy is a living day-of-birth present. The reason we are in the same location as you is for a special human treasure hunt."
    yu "Treasure hunt?"
    k "It is what humans call the act of hunting for treasure."

    scene yukicamparrive30
    with dissolve

    na "!!!"
    k "Friend! Surely you remember the last flattened tree corpse that sent us on a similar hunt! Do you shoelaces?!"
    s "Was that supposed to mean “do you not?”"
    yu "I think it’d be “knot” technically."
    s "Thanks for the added clarity, Yuki. Conveying audio-based jokes through text boxes is hard."
    k "So you don’t shoelaces! Just as I presumed!"
    s "Are you saying you got another treasure map? And that you brought Nao here to help you investigate?"
    na "!!!"
    k "Nao-chan is correct!"
    yu "But she didn’t say anything."
    k "Her mouth words do not matter when her heart words are much louder! But either which way, I am excited to greet you on this day, Friend and Auntfriend! "
    k "Treasure is easier to find when the amount of hand-arms reaching for it increases."

    scene yukicamparrive31
    with dissolve

    yu "Well, you have fun with that. I’m gonna go celebrate being out in the wilderness by day drinking until I have a migraine. "
    k "Aunt Yukiburger?"
    s "I think she just wants to relax today. But I’ll try and find the time to help you with your treasure hunt if I’m able to."

    scene sky
    with dissolve2
    stop music fadeout 25.0

    k "Excellence! "
    k "Nao-chan and I have to make nine minus three more preparations first, but we will await your un-departed departure as soon as you are shoelaces-shoelaces ready! "
    k "In the angry-time...come, Nao-chan! I will show you the correct way to search for felinefish!"

    "Nao excitedly hurries after her “mothermom” and the two of them disappear inside of a tent that...I’m surprised they were able to set up without the help of an actual adult rather than whatever Kaori is."
    "Either way, I should probably take a page out of Yuki’s book and attempt to relax as well if Sara is going to be keeping Ami occupied for the time being."
    "I just hope that things are going well."
    "I’m worried enough about her as-is and the last thing I need is today making things even harder than they’ve been lately."
    "I just want her to get back to normal or...something that resembles it."

    s "..."

    "Which means I need to do the same."
    "But that also means I have to figure out how to spend the next hour or two. That being said..."
    "What do I want to do?"

    $ renpy.end_replay()
    $ yukicamp1 = True
    $ yuki_love += 1

    jump campmenu1

menu campmenu1:
    "Fish with Maki" if makicamp2 == False:
        jump makicamp2
    "Drink with Yuki" if yukicamp2 == False:
        jump yukicamp2
    "Treasure hunt with Kaori" if naocamp1 == False:
        jump kaoricamp1
    "Call someone" if mollycamp1 == False:
        jump mollycamp1
    "Go back to the camp" if mollycamp1 == True and naocamp1 == True and yukicamp2 == True and makicamp2 == True:
        jump amicamp2

label yukicamp2:
    scene yukiwater1
    with dissolve2

    "There’s some sort of riverbank or something along those lines that runs through the campsite. "
    "And, after following it for several minutes out of sheer boredom or despondence or the inability to currently spend time with my niece, I wind up at a clearing made less clear by the inclusion of Yuki."
    "Which isn’t to say she’s an unwelcome contaminant despite the fact that her blood is the least drinkable of everyone’s here. Probably."
    "I don’t know much about cannibalism, but I do know that she’d be the last one among us I’d be willing to eat and it wouldn’t be due to the way I feel about her."
    "But how even {i}do{/i} I feel about her?"

    play music "starvingtodeathoutofreachofthesun.mp3"

    "I like her enough to not cannibalize her. That much is true."
    "But does that “like” extend beyond the reaches of Armin Meiwes and into a basket you could strap to a bicycle on a long ride through Rotenburg?"
    "The implied proposal here is meant to isolate each trace of carnality and force you into an escapable (yet entirely metaphorical) line at your local department of motor vehicles or grocery store or something of the like."
    "Anywhere you could go reluctantly before finding yourself in a row full of other somewhat depressed and dejected people while thinking to yourself, “I’m in too deep now” or “If I leave, I’ll look awkward or weak.”"
    "I think that not knowing how you feel about someone is a lot like finding yourself in one of those places. Or finding yourself hovering over the corpse of one who has agreed to be eaten."
    "I think I’d allow Yuki to eat me if she really wanted to."
    "She probably doesn’t, but I think I would let her. And I think I would let her because I think it’d be what I deserve."
    "But love and like are more than just bleeding out into a bathtub, right? Love and like and lovely and likely. But they’re also hateful in the fact that I’d hate to ever love or like love or like."
    "In the midst of this half-hearted delusion or doubt or whatever you want to call it, my mind takes a dip in the river — but my heart is in Rotenburg."
    "And so is every other piece of me."
    "If anyone is reading this or hearing this or watching this or whatever it is you’re supposed to be doing or think that you’re doing or are only doing because I think you’re supposed to hear or read or listen, know this."
    "I’m not very fond of bugs."
    "But I will never take pleasure in killing them."

    s "Yuki."

    scene yukiwater2
    with dissolve

    yu "Hm?"
    yu "The fuck you doin’ over there? Just standin’ around and watching me like that makes you look like some kind of stalker."
    s "I didn’t know what else to do."
    yu "Don’t wanna hang out with any of the others? Figured you were way closer to them than you are to me."
    s "Is that why {i}you’re{/i} alone? You feel like you don’t fit in?"

    scene yukiwater3
    with dissolve

    yu "Nah. It ain’t anything that dramatic. Just trying to relax a little."
    yu "I ain’t got a lot of experience with camping and shit, but I ain’t no stranger to sleepin’ outside. Shit like that was actually pretty normal back when I was younger."
    yu "But hey, when you ain’t got a place to live, you make do with what you’ve got. "
    yu "And sometimes, all you’ve got is a bench in some town you can’t even remember the name of and a bunch of other girls drinking and laughing while you just want to sleep."
    s "Do you ever miss it? Being wild and free?"
    yu "Miss when my knees didn’t hurt. And when I wasn’t so fuckin’ tired all the time."
    yu "And yeah, maybe I {i}do{/i} miss the “freedom” part a little. But what I’ve got goin’ on now ain’t all that bad when you compare it to everything else I’ve lived through."
    s "Everything apart from how your upbringing wasn’t ever terrible to begin with, right?"

    scene yukiwater4
    with dissolve

    yu "You remember that, huh?"
    s "My memory’s pretty terrible, but there are certain things that’ll always stick out to me."
    yu "Things like girls who grew up in candy stores?"
    s "Things like the minor details that have turned the people I like spending time with into people I like spending time with."
    yu "Then tell me, what else do you remember about me?"
    s "I remember how Yumi was made."
    yu "Oh yeah? {i}You{/i} the one who came inside me when I was passed out? Answer carefully or I’ll be on your case for over a decade’s worth of child support."
    s "That’s not what I was implying."

    scene yukiwater5
    with dissolve

    yu "Then why the fuck did you word it like you were there watching the magic happen? You don’t know shit, man. "
    s "I wish I had a better answer for you, but even the words inside of my head are sewn together strangely at times."
    yu "Yeah, well you’re one of those {i}creative{/i} types, ain’t ya? Complete opposite of people like me who never stuck around to learn about proverbs or pronouns. "
    s "On the bright side, you could beat me in a fight. So if the world breaks out into a war-zone, you’ll probably outlast me."
    yu "World’s already turned into a war-zone. But somehow, people like us have managed to avoid it."
    s "You’ve avoided it because you have a vagina. I’ve avoided it because I-"
    yu "Also have a vagina?"
    s "..."

    scene yukiwater6
    with dissolve

    yu "Sorry. Did I hurt your feelings?"
    s "Yes. And I am ending our friendship as a result of this. Goodbye, Yuki."
    yu "Damn, really? Oh well. Guess I’ll have to just empty out this entire cooler all by myself."
    s "Are you apologizing in the form of giving me free alcohol?"
    yu "Free? No way. I’m a bartender now. You tip me for this shit."
    s "Unfortunately, I left all of my cash at home on account of convenience stores not existing in the woods."

    scene black
    with dissolve2

    yu "I’ll just add it to your tab then. Been keepin’ a close eye on that shit since Sara’s always givin’ you booze for free."
    s "I have a tab?"
    yu "Damn right. And I’m the type of girl who always {i}collects,{/i} if you know what I mean."
    s "It’s always impressive how you’re able to both strong-arm me and flirt at the same time."

    scene yukiwater7
    with dissolve2

    yu "Aight, first and foremost — I don’t {i}strong-arm{/i} you into anything. And, if I do, it ain’t intentional. Probably just a result of me being a badass or some shit. But second, this ain’t flirting."
    s "How would you know? You’ve never been in a real relationship before."
    yu "Have {i}you?{/i} Because it seems to me like you’re just the town bimbo a lot of the time."

    scene yukiwater8
    with dissolve

    s "That’s not far off, but..."
    s "I have."
    yu "Oh? Then maybe you {i}do{/i} know what you’re talkin’ about. But still, we’re two different weight classes. And I ain’t about to go punchin’ at someone so much weaker than me."
    s "That’s fair. And I was just kidding in the first place. You’ve been surprisingly kind to me for someone who could kick my ass at any moment. "
    yu "Thank you for admitting that."
    s "And thank you for not eating me."

    scene yukiwater9
    with dissolve

    yu "For {i}what?{/i}"
    s "When you were outside of Kumon-mi, what was it like?"
    yu "What do you mean? "
    s "Like...you’ve been in this city long enough to understand how it feels, right? How no one comes in and no one goes out. "
    yu "That ain’t entirely true. Had a whole ass group of European dudes come into the bar the other night and I had to kick ‘em out since I’m the only one of us who knew any English."

    scene yukiwater10
    with dissolve

    s "You know English?"
    yu "Just the basic shit. “Hello. How are you doing? Where is the restroom?” Shit like that."
    s "Why?"
    yu "Picked it up from an old friend. One of those creative types, like you."
    s "Someone in your gang?"

    scene yukiwater11
    with dissolve

    yu "Something like that. But yeah, wound up havin’ to kick ‘em out since Sana and Sara were too embarrassed to even try. "

    scene yukiwater12
    with dissolve

    yu "Why do you think it’d be any different outside of here, though? You ain’t thinkin’ of hoppin’ the wall, are you?"
    s "Is that even possible?"
    yu "Not with that attitude it ain’t. Moment you doubt yourself is the moment you fall several hundred feet and turn into a fuckin’ Sensei puddle."

    scene yukiwater13
    with dissolve

    s "Fair enough."
    s "I’ve just been wondering a lot lately about what it would be like to sort of...start over. But I feel like, as long as I’m here, that’ll never be possible."
    s "There’s too much tying me to this place. Too many things I’d rather just forget at this point because they make just getting through each day way harder than it should ever be."

    scene yukiwater14
    with dissolve

    yu "Mm."
    yu "Well, sorry to burst your bubble, but that shit’ll follow you even if you {i}do{/i} manage to make it out of here, man. Just changin’ scenery ain’t enough to “start over.” I know that better than anybody."
    yu "Like yeah, a new town might be exciting for a little while. You might be able to distract yourself from all that shit you’d “rather forget.” But the second you start to remember, you’ll have to move {i}again.{/i}"
    yu "So you’ll move and you’ll move and you’ll move, but you’ll never get any further away from the shit you’re trying to escape from. And, soon enough, all those places will start to blur together."
    yu "That’s sort of where I’m at. How there’s no “one town” that sticks out to me from my past because, if there was, I’d still {i}be{/i} there."

    scene yukiwater15
    with dissolve

    yu "Nobody can escape the past, man. All you can do is confront it. And hey, maybe you get your ass beat. Maybe you don’t. "
    yu "But there’s a lot more honor in goin’ down with a fight than just lying down and letting life kick the shit out of you."
    s "That may be true. But what good does something vague like “honor” do in the first place?"
    yu "What good does being a bitch do?"
    s "Nothing really."
    yu "Exactly. Cause nothing matters at all when shit really comes down to it."
    yu "It’s up to {i}us{/i} to figure out what we value. And honor’s kinda fuckin’ bred into us since our ancestors were probably samurai or some shit."
    yu "If that doesn’t mean anything to you, then fuck it. But to me, honor and respect are, like...all I’ve got. Especially now that I’ve got a kid who might look back at me like you’re lookin’ at {i}your{/i} past some day."
    yu "I don’t wanna be something she’s gotta run from, you know? And the best way of doin’ that is by not settin’ an example and running away myself."
    s "You...You {i}did,{/i} though. You {i}did{/i} run."

    scene yukiwater16
    with dissolve

    yu "Yeah, and look how {i}that{/i} worked out. Shit didn’t change until I {i}stopped.{/i} So maybe it’ll be the same for you."

    scene yukiwater17
    with dissolve

    s "I hate talking to you. You’re always wiser than I expect and none of my counterpoints ever last more than a second."
    yu "Well, maybe {i}you’ll{/i} be as wise as me in another decade or so. And this ain’t me sayin’ I’ve been through more since I don’t really know what your deal is yet, but..."
    yu "It’s clear you’ve been through a lot. And it’s that kinda shit that makes people call us “wise” when we’re wastin’ away our morning getting drunk by the river."

    scene yukiwater18
    with dissolve

    s "Thank you, Yuki."
    yu "Hm? For what? Givin’ you advice even though you never asked for it?"
    s "Everything, really."
    s "I’m glad you never gave up because that means I get to spend time with you now."

    scene yukiwater19
    with dissolve

    yu "Wha-"
    yu "Ain’t...{i}you{/i} just flirting now? Didn’t you just give me shit a few minutes ago after accusin’ me of the same damn thing?"
    s "I wasn’t giving you shit. I was just trying to mold another conversation into a shape that wouldn’t force me to accept something I’m already beginning to understand."

    scene yukiwater20
    with fade

    yu "Well...I’ve got no fuckin’ clue what you mean by that, but...be careful about what you say and shit."
    s "Why?"
    yu "Because I said so, okay?"
    s "Is just admitting that I enjoy spending time with you really enough to make you this bashful? Is that seriously your only weakness?"

    scene yukiwater21
    with dissolve

    yu "Okay. Listen up, douchebag. Ain’t nobody ever actually shown me that sorta {i}kindness{/i} before. So sorry if I’m reacting weirdly to it after fuckin’ decades without any experience at all."
    s "Why are you apologizing? I like this side of you."

    scene yukiwater22
    with dissolve

    yu "Jesus, fuck! Stop! "
    yu "I might be your senior, but I’m still a fuckin’ girl, you know? And between this and all that shit about callin’ me cute a while ago, you’re gonna fuckin’...confuse me or something."
    s "I wish everyone reacted to honesty this way. It would make my life a hell of a lot easier."

    scene yukiwater23
    with dissolve

    yu "Yeah, well...all it does is make mine harder."
    s "How so?"
    yu "..."
    s "Yuki?"
    yu "I wonder how you would’ve felt about me if we met when we were younger. Like...teenagers or some shit."
    s "You’re almost ten years older than me, aren’t you? I can’t imagine you’d have had any interest in me back then."
    yu "I meant more, like...it’d be cool if we were the same age back then. Just wanna know how you’d feel about the old me rather than the burnout you’re wastin’ your time on now."
    s "I doubt we would have meshed well, to be honest."
    yu "Yeah, you’re probably right."
    yu "We’re practically opposites even now, aren’t we?"
    s "Yeah, but...is that really a bad thing?"
    yu "It ain’t bad, but...it ain’t really {i}good{/i} either. Not sure if we’ll ever, like...see eye-to-eye on anything."
    s "That’ll just keep our talks interesting then."
    yu "..."
    s "Well...I’m gonna-"
    yu "Listen...uh...{i}Sensei...{/i}"
    s "..."
    yu "If you, like..."
    yu "If you’re actually...like..."
    yu "If you actually think I’m...you know...{i}cute{/i} or whatever..."
    yu "Could you, like...not say that anymore?"
    s "..."
    yu "Sara’s my boss, but like...she’s also a friend and shit. And she’s crazy about you whether you like that or not, so...I ain’t about to go, like...makin’ that more complicated, if you know what I mean."
    yu "This is all just...assumin’ you ain’t bullshittin’ me, though. Cause I ain’t really got any idea..."
    s "Do you actually like me, Yuki?"
    yu "Fuck if I know, man. All I know is that this blows and I keep wishin’ the fuckin’ circumstances were different. Cause I feel like Yumi’d be pissed about this too and I ain’t about to ruin shit {i}again{/i} with her."
    s "Yeah..."
    s "I wouldn’t want to do that to you either."

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "I’m gonna walk around for a little while. But I’ll see you around the campsite."
    s "Thanks for the beer. And also the advice."
    s "And also for existing."
    yu "Just...get lost, man. You’re interrupting my alone time."

    scene sky
    with dissolve2

    "I leave Yuki by the riverside with all the same decaying parts and pieces she had when I first showed up."
    "But, for a brief moment in time, I imagine how much better they’d have tasted if we could turn back the clocks."
    "They’re all without hands now."
    "They’re just like dinner."

    $ renpy.end_replay()
    $ yukicamp2 = True
    $ yuki_love += 1

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "What should I do now?"

    jump campmenu1

label yukispring1:
    play sound "knock.mp3"
    scene yukicheckup1
    with dissolve2

    sar "Yuki! It’s your debatably closest friend and employer, Sara! Are you in there?"
    s "..."

    "We finally make it to Yuki’s place and, after ascending what can only be referred to as “an annoying amount of stairs,” we make our presence known."
    "Or at least we attempt to."
    "Honestly, I think I’d {i}prefer{/i} if she isn’t around right now as that would all but eliminate the possibility of us forcing our way in and finding something {i}no one{/i} wants to see."

    play sound "knock.mp3"

    sar "Hellooooo? Yuki? Open up, please!"
    s "Maybe she’s just...out with other friends?"
    sar "What other friends? I’m pretty much the only one she’s got. That “debatable” part earlier was only there to stop her from feeling bad if she was listening."

    play sound "knock.mp3"

    sar "Which I am starting to believe she is not."
    s "Then...what if she got a new job? It’s not unheard of for people to just bail on workplaces once they find something else to do, right?"

    scene yukicheckup2
    with dissolve

    sar "Speaking from experience, huh?"
    s "I think my situation might be a little different on account of all the sudden trauma. Also, what are you doing?"
    sar "Unlocking the door, duh. If she’s not going to answer, I’m going to let myself in."
    s "Yuki gave you a key to her apartment?"
    sar "Hm? Nope."

    scene yukicheckup3
    with dissolve

    sar "Skeleton key. I’ve had it for years."
    s "You just...happen to have a key that unlocks all doors?"

    scene yukicheckup4
    with dissolve

    sar "Not {i}all{/i} of them, technically. Most houses have fancy locks now, so stuff like this doesn’t work as well as it did when I was a teenager."
    sar "With low-income apartments like this, though — all you really need to do is shove this bad boy inside, wiggle it around, and voila. Kind of like sex."
    s "Sara."
    sar "Yes?"
    s "{i}Why{/i} do you have that?"
    sar "Excellent question, Sensei."

    scene yukicheckup5
    with dissolve
    play sound "lock.mp3"

    sar "Let’s go in."
    s "What?..."
    sar "Yuki! Last chance!"

    scene black
    with dissolve2

    sar "You have three seconds to respond before we enter the room!"
    s "Are you really sure this is a good idea?..."
    s "You don’t want to turn around and just...try again tomorrow?"
    sar "Okay, Yuki! Time is up!"

    play sound "dooropen.mp3"

    sar "Pardon the intrusion..."

    "........."
    "......"
    "..."

    play music "itsingsinitssleep.mp3" fadein 4.0
    scene yukicheckup6
    with dissolve4

    sar "Ooooh boy..."
    s "..."
    yu "Nm......mngh......."
    sar "Well...she’s {i}breathing.{/i} That’s good at least."

    "Upon entering the apartment, the worst of our fears is dispelled. But that doesn’t make the sight before us any more pleasing to look at."
    "The scents of smoke and alcohol permeate the room, clinging to the walls and combining with the already unpleasant odor that’s been emanating from the carpet since she first moved in."

    sar "Is it...just beer? You don’t see anything else?"
    s "I see...water."
    sar "Oh, good. So she’s staying hydrated. "
    s "I’m not really sure what else you-"
    sar "{i}Drugs.{/i} "
    sar "Needles...Pipes...Small plastic baggies...You don’t see any of that, do you?"
    s "Yuki’s clean. And I’d prefer to keep giving her the benefit of the doubt."
    sar "So would I, obviously. But addicts take advantage of that sort of thing, Sensei. You’ve gotta remember, I don’t exactly come from the happiest of households."
    s "..."
    yu "Angh......mmmblff.......mmffngh...."

    "Despite the sounds that leak from her mouth — that bleed through her pillow and find their way to us, I take solace in the fact that she fell asleep face down and can’t choke to death on her vomit."
    "But again, that is no {i}bandage.{/i} There’s a wound that’s opened up in me — and it’s spurting blood all over her carpet but refusing to mask those other scents."
    "All this gash will do is stain what’s meant to be a sanctuary. And when blood is spilled on holy ground, divinity must be questioned."
    "Was this ever safe at all? Or did having a place to call her own do naught but grant her the opportunity to look on in awe as she burns it to the ground?"

    s "So...now that we know she’s alive...what do we do?"
    sar "We wake her up and tell her to get her shit together, that’s what."
    yu "Mmfgh.....blch ch......"
    s "But-"

    play sound "static.mp3"
    scene yukicheckup7 with flash
    stop sound

    sar "Yuki. Come on. It’s time to wake up."
    yu "Mmlgh......mlphph......blch....."
    s "Is it even okay to wake people up when they’re like this? Shouldn’t we maybe let her...sleep it off?"
    sar "Then what? Let her wake up tomorrow and wash away the aftertaste of old beer with {i}new{/i} beer? You’re being too easy on her."
    s "Sorry, I just..."
    s "This isn’t something I’m used to dealing with."
    sar "Then leave it to the professionals. I come from a long line of people who drink more than they probably should. "
    sar "Yuki, rise and shine. I {i}will{/i} shake you if I have to."
    yu "Mmnh......go away......"
    sar "Sensei, could you get the lights?"
    yu "Noooooo....leave ‘em off.....I’m tryin’ to......fuckin’ sleep......just come back......tomorrow......."

    scene yukicheckup8
    with dissolve

    sar "Sure, Yuki! I’ll {i}gladly{/i} come {i}all the way{/i} to your apartment {i}tomorrow{/i} too because you’re {i}tired{/i} right now! You got it!"
    s "Sara-"
    sar "Sensei, lights!"

    play sound "static.mp3"
    scene yukicheckup9 with flash
    stop sound

    "I do as I’m told since that’s all I’m good for once you take away what I hide between my legs. And all that I have room for there right now is my tail."

    play sound "slap.mp3"

    sar "Chop chop! Up and at ‘em! Time to rejoin us in the real world."

    "Sara claps her hands and shakes Yuki by her shoulder. "
    "There’s a brief window where I can see her face- covered in drool from sleeping in a puddle of it. But she wipes it away and turns to face the couch once her lagging brain manages to get the message of the light."
    "As she shields her eyes, I once again tell myself that we’re in the wrong here. "
    "But I told myself I was in the right when I let a girl not even half her age abuse unprescribed medication for months, so I guess that Sara’s probably right this time."
    "I guess I {i}should{/i} leave this to the experts. I mean...it’s not like I can just {i}fuck{/i} someone’s addiction away."
    "But imagine how much I’d be able to accomplish if I {i}could.{/i}"

    yu "Fine! Jesus...I’m up, I’m up..."

    play sound "static.mp3"
    scene yukicheckup10 with flash
    stop sound

    yu "The fuck are you two doin’ here?...Don’t feel like hangin’ out tonight..."
    sar "I’m the one who should be asking {i}you{/i} that. You skipped work {i}again{/i} tonight and Sana’s stuck working on her own for the third time this week."

    scene yukicheckup11
    with dissolve

    yu "Oh, shit...I was on the schedule?"
    sar "Yes...I texted you about it like ten times today."
    yu "I must’ve...forgot again or some shit. Sorry, Sara. I’ll...go get...dressed now..."
    yu "I swear it won't happen again...I-"
    sar "Yuki, no. I don’t want you coming to work when you’re like {i}this.{/i}"
    yu "Like what? I’m just tired...You guys woke me up in the middle of the fuckin’ night. The hell you want from me?"
    sar "Honesty would be a good place to start. Maybe an admission that you’re hammered out of your mind and not just “tired.”"

    scene yukicheckup12
    with dissolve

    yu "Okay. Fine. So I got drunk. Who gives a shit? You drink at the bar all the fuckin’ time. What difference does it make if I do it too?"
    s "The difference is Sara’s never missed a shift."
    yu "Sara lives at the fuckin’ bar. All she’s gotta do is walk downstairs. It ain’t hard."

    play sound "static.mp3"
    scene yukicheckup9 with flash
    stop sound

    s "Sara was really worried about you. We both were. You should at least thank her for coming all the way over here to check on you."
    sar "We thought you might be dead, Yuki..."

    play sound "static.mp3"
    scene yukicheckup13 with flash
    stop sound

    yu "{i}Dead?{/i} Gimme a fuckin’ break. If I ain’t been killed by all the shit I’ve already been through, ain’t nothin’ killin’ me now."
    sar "{i}I{/i} might if you quit dancing around the fact that you’re an addict and could have relapsed for all we knew."
    yu "Well, what’s the fuckin’ point in makin’ sure if I’m alive if you’re just gonna kill me yourself?"

    scene yukicheckup14
    with dissolve

    sar "Yuki! I’m being serious! You can’t be acting this way! You have a job and a {i}daughter{/i} again! Are you {i}trying{/i} to throw that away?!"
    yu "Jesus. Can you be serious without yelling? Fuckin’ head hurts and this shit ain’t helping."

    scene yukicheckup15
    with dissolve

    sar "Are you using again? Just because I don’t see anything lying around doesn’t mean you’re innocent. Show me your arms. Now."

    scene yukicheckup16
    with dissolve

    yu "Jesus. Here. Look at ‘em. I ain’t done shit. "
    sar "No, you just haven’t been {i}caught.{/i} And your arms might pass the test, but that {i}still{/i} doesn’t mean anything."

    scene yukicheckup17
    with dissolve

    yu "You bring a fuckin’ cup for me to piss in too? The fuck do you want, huh?"
    sar "I want you to get your shit together. It’s one thing missing a shift or two. But doing it multiple times a week because you’re passed out in your apartment? You’re supposed to be better than that, Yuki."

    scene yukicheckup18
    with dissolve

    yu "Me? {i}Better{/i} than something? You forget who you’re fuckin’ talkin’ to, Sara? "
    yu "I’m a fuckin’ deadbeat, dude. All I do now is just work...or ride my bike and drink when I {i}ain’t{/i} workin’."
    yu "Hell, sometimes I do both of those at the same time. So you should be happy I ain’t doin’ fuckin’ doughnuts in your damn bar, okay? "
    yu "You wanna fire me? Fire me. I’ll just fuckin’ melt into the couch and bum money off my ex or some shit. Who even gives a fuck anymore?"
    sar "{i}I{/i} do. And the fact that you’re willing to bum money off of your ex after all of the things you’ve told me about him explains {i}everything,{/i} Yuki."

    scene yukicheckup19
    with dissolve

    sar "What happened?..."
    yu "Nothin’."
    yu "I just fuckin’ suck."
    yu "This is what I do. "
    yu "Y’all just ain’t been around long enough to see it happen yet."
    sar "How can we help?"
    yu "I mean...{i}not{/i} gettin’ fired would be pretty cool. Ain’t like I’m {i}tryin’{/i} to skip work. That’s just how it’s been goin’ lately."
    sar "Yuki- you {i}can’t{/i} keep doing that, though. I’m your friend and your boss, not your sponsor. I can’t babysit you every day and make sure you haven’t drunk yourself to death."
    yu "I ain’t sure what to tell you other than you should’a seen this coming, Sara. Shit happens when you hire junkies."

    play sound "static.mp3"
    scene yukicheckup20 with flash
    stop sound

    s "Are you trying to say this is somehow {i}her{/i} fault?"
    yu "Oh, hey. Been so quiet I forgot you were here."
    s "Yeah. I’ve been a little busy trying to wrap my head around how you’re so nonchalant about this while two of the only people who actually {i}care{/i} about you are trying to help."

    play sound "static.mp3"
    scene yukicheckup21 with flash
    stop sound

    yu "What fuckin’ reason would you two have to possibly care? Ain’t like your lives would be any worse without me. Hell, they’d probably be {i}better{/i} since you wouldn’t have to do shit like this."
    sar "You don’t need a reason to care about someone, Yuki. "

    scene yukicheckup22
    with dissolve

    sar "I met you. I like you. And I want to keep seeing you, so I’m {i}okay{/i} with looking after you when I need to. But {i}you{/i} need to put in effort too. "
    sar "You can’t just return to your old ways whenever you feel like it. Not when you’ve come {i}so{/i} far. You’re finally living a somewhat normal life. Why ruin it?"
    yu "I don’t know."

    scene yukicheckup23
    with dissolve2

    yu "Maybe I don’t like “normal?”"
    yu "All my life, I’ve been runnin’ from {i}somethin’.{/i} Home. Cops. Yakuza. Yumi. Drugs. There’s always some fuckin’...{i}evil.{/i} Even if that evil ain’t {i}actually{/i} evil, you know?"
    yu "Just somethin’ to fight back against or avoid and..."
    yu "Heh."
    yu "For the first time ever, I ain’t got that. "
    yu "Went from there always bein’ something in the background I need to look out for to...my own couch. Buyin’ TV dinners for two people instead of one. {i}Money.{/i} "
    yu "I don’t fuckin’ deserve any of that. I’ve seen girls way better than me — ones who ain’t ever did anythin’ wrong get fuckin’ killed by the same shit {i}I{/i} used for years. Why {i}them?{/i}"
    yu "That’s how I know there ain’t no god. Fucker’s fine with me doin’ everythin’ in my power to burn this world to the ground while lettin’ the ones who could do some good rot. I don’t get it."
    sar "Neither do I, Yuki...but {i}this{/i} isn’t the answer."

    scene yukicheckup24
    with dissolve

    yu "What {i}is{/i} then, Sara?..."
    yu "How’s a fuck-up like me ever supposed to live with herself?..."
    sar "By...doing all you can with what time you have left. Life isn’t over until it’s over, Yuki."
    yu "Maybe...But I ain’t got enough time left to do {i}shit.{/i} "
    sar "You don’t know that..."
    yu "Neither do you. Just how life works. "
    yu "Or doesn’t..."
    yu "Get it?"

    scene yukicheckup25
    with dissolve

    sar "You’re seriously going to make jokes right now? {i}That’s{/i} how you want to handle this?"
    yu "Why you askin’? You got a better idea?"
    sar "Yeah. Clean up your fucking act and stop shitting all over the people who care about you."
    sar "You miss one more shift, you’re done. Got it?"
    yu "Sir, yes, sir..."

    scene black
    with dissolve2

    sar "Goodnight."
    s "Wait, you’re leaving? "
    sar "Yeah...I need to go cool down."
    sar "If I hear one more word from her, I’m going to slap her so hard she’ll forget she’s even shit faced."
    yu "Damn, yo. You should’ve just started with that. Would save me from a hangover in the morning."
    sar "You fucking- UGH!"
    sar "You have {i}no{/i} idea what this does to other people, do you?! How can you be so selfish?! How can-"
    s "Sara...yelling isn't going to help."
    sar "I know that! But watching her {i}ruin{/i} everything she worked so hard for is just- UGH!"
    sar "Goodnight for real this time!"

    play sound "doorslam.mp3"
    scene yukicheckup9
    with hpunch

    s "..."

    "Sara slams the door behind her and Yuki slumps back on the couch. "
    "To be honest, I wish I followed her. "
    "Not just because I’d feel more comfortable knowing she has company on the way home-"
    "Not just because I know she can probably relate to this on some level-"
    "Not just because I want to see the various expressions on her face — the various sobs and moans and cries she will make as she relives a prior Hell-"
    "But because I’m mad too."
    "And I know I shouldn’t be as someone who also struggles to live with himself."
    "But I feel sick each time I look in the mirror — and my reflection isn’t far from here."

    s "Do you feel good about yourself right now?"
    yu "Man, I haven’t felt good about myself in almost forty years. Were you even fuckin’ listening to any of that?"
    s "Sara really cares about you, Yuki. And I get that burning bridges is “your thing” and all, but this is one you {i}really{/i} want to leave intact."

    $ renpy.end_replay()
    $ yukispring1 = True

    jump yukispring2

label yukispring2:
    scene yukirikavisit1
    with fade

    yu "{i}Hah...{/i}Probably. Guess that could’ve gone a little better now that you mention it."
    s "Technically, it still went probably five times better than I expected it to."
    yu "Yeah, but it still could have gone {i}better.{/i}"
    s "I’ll agree that it probably would have been nice to not watch you spit all over the only real friend you’ve got."

    scene yukirikavisit2
    with dissolve

    yu "Still got you, don’t I? Take it you’re the type who’d {i}want{/i} me to spit on him, though. "
    s "Maybe under the right circumstances. But if you were to do that right now, I’d probably just want to take a shower."
    yu "Ya mean you aint already feelin’ grimy as shit watchin’ an addict do what an addict does best?"
    s "What’s that? Relapse?"
    yu "{i}Lie.{/i}"
    s "..."

    scene yukirikavisit3
    with dissolve

    yu "Kinda funny, actually. How easy that is. But I’ve always wondered if it’s for selfish reasons or just because dealin’ with confrontation kinda sucks."
    s "It’s selfish no matter what way you look at it when you need to trample over other people’s feelings to get to where you are now."
    yu "Yeah well, they ain’t gonna have to be trampled much longer at this rate. "

    play sound "static.mp3"
    scene yukirikavisit4 with flash
    stop sound

    s "So...you {i}are{/i} using drugs again?"
    yu "Maybe. Maybe not. I can say whatever I want and you won’t know what to believe."
    s "If you are, I’d like to extend my gratitude. I’m very thankful that you’d trust me to be the only one burdened by this knowledge instead of someone who could actually help."
    yu "See, that’s the part you ain’t gettin’. This ain’t the kinda shit other people can help with. "
    yu "It’s a constant battle against yourself and even when you think you’re {i}safe,{/i} you ain’t. Takes just one thought. One mistake. Then you’re right back where you started."
    s "And what was that thought this time?"
    s "Was there even a thought at all? Or do you just despise this world for letting you breathe for a change?"

    play sound "static.mp3"
    scene yukirikavisit5 with flash
    stop sound

    yu "What’s it like for you?"
    s "What’s {i}what{/i} like for me?"
    yu "Hatin’ yourself without a clear-cut reason to do that. Cause you’re in the same fuckin’ boat. Just nobody ever blames you when the ship starts sinkin’."
    s "..."
    yu "Just wanna know if it’d be any easier to forgive myself for any of this shit if there wasn’t such a fuckin’ obvious problem."
    s "I doubt it, Yuki."
    yu "Yeah...figures."
    s "..."
    yu "..."

    scene yukirikavisit6
    with dissolve2

    yu "You know..."
    yu "You might be the first guy I’ve ever actually had feelings for."

    play sound "static.mp3"
    scene yukirikavisit7 with flash
    stop sound

    s "And you pick {i}now{/i} to tell me that?"
    yu "Better now than never, right?"
    s "Yuki-"
    yu "I ain’t expecting much to come of it. And I already told you I wouldn’t wanna have to drag Sara into any of that shit since she likes you way more than me. "
    yu "Just figured...you know. Ain’t worth keepin’ it to myself anymore. And if I’m gonna give you one reason to think about me, might as well keep pilin’ ‘em on."

    scene yukirikavisit8
    with dissolve

    s "..."
    yu "It’s weird how this shit works, huh? You ain’t my type at all. Feels like I’m rockin’ the cradle a bit too hard."
    s "So it’s {i}my{/i} fault you-"
    yu "Pfft. Don’t give yourself {i}that{/i} much credit. Just because I think about you sometimes doesn’t mean I’d throw my life away if you don’t look at me enough."
    yu "This happened because I’m weak. None of y’all had shit to do with it. "
    yu "Just..."
    yu "..."
    yu "Some bad decisions catchin’ up to me. That’s all that’s goin’ on here."

    scene black
    with dissolve2
    play sound "knock.mp3"

    s "..."
    yu "And on that note, looks like Sara’s had enough time to “cool off.” Place your bets now on whether or not you’ll ever see me around the bar again."

    "I sigh to myself and move toward the door as Yuki sinks deeper into her couch."
    "But as I attempt to imagine how the smell of a rotting corpse would blend into the cacophony of other unpleasant aromas in here, I’m hit by a truck."

    play sound "static.mp3"
    scene yukirikavisit9 with flash
    stop sound
    play music "recovery.mp3"

    "Because this isn’t Sara at all. This is someone I plucked off the street and dragged into a funeral."

    ri "Oh."
    s "Oh."
    ri "Uhh..."

    play sound "static.mp3"
    scene yukirikavisit10 with flash
    stop sound

    ri "Am I interrupting something here?"
    yu "Just the world’s worst intervention. Sup?"
    ri "You are naked."
    yu "Not all the way."
    ri "This pleases me."
    yu "...What?"

    play sound "static.mp3"
    scene yukirikavisit11 with flash
    stop sound

    ri "Nothing. I speak my thoughts out loud when I feel too many things at once sometimes. Please ignore them."
    s "So that’s where Rin gets it from."
    yu "The fuck are you holdin’? Also, the fuck are you doin’ here? Forget which room is yours?"

    scene yukirikavisit12
    with dissolve

    ri "Oh! No! Uhh...These are...I made..."

    scene yukirikavisit13
    with dissolve

    ri "They’re...Halloween cookies. I just...made too many and figured you might want some of the extras."
    s "You made these specifically {i}for{/i} her, didn’t you?"

    scene yukirikavisit14
    with dissolve

    ri "{i}Shh!{/i} "
    yu "Heh...Halloween, huh? Figures. You really made those for me?"

    scene yukirikavisit15
    with dissolve

    ri "Yes! I mean...no? Only if you wanted me to make them for you. But the point is that I made cookies and cookies now exist because of me. Please put them in your mouth and be happy."
    yu "Sure. Just leave ‘em on the table and I’ll have ‘em for dinner when I’m not busy destroying everything."

    scene yukirikavisit16
    with dissolve

    ri "Well, actually...I..."
    ri "I was kind of hoping we could...eat them together and like...become friends? If that’s not weird? It’s probably weird."
    s "It’s just...not really a great time, Rika."

    scene yukirikavisit17
    with dissolve

    ri "{i}Stop fucking all of my neighbors!{/i}"
    s "I’m not fucking either of your neighbors. And you {i}want{/i} me to fuck one of them."
    ri "{i}Not this one! I’m trying to be cute and I can’t because you’re over here macking it with my crush! Now, beat it or it’ll have to be a threesome!{/i}"
    s "Oh no. Whatever will I do if something like that occurs?"
    yu "Can you two stop fuckin’ whispering and just bring the damn cookies over here? I ain’t eaten {i}shit{/i} all day."

    scene yukirikavisit18
    with dissolve

    ri "Coming! Hahah!"
    s "..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yukirikavisit19
    with dissolve2

    "The three of us sit down at the table, causing an entire liquor store worth of beer cans to fall over as our legs take their places beneath it."
    "Rika doesn’t seem to pay any mind to it though, as she’s currently entranced by Yuki for...whatever reason. Probably the “cool” factor. "
    "But I wonder if her feelings would change upon finding out that Yuki isn’t exactly as “cool” as she looks. And I worry that letting Rika fall further might mean having to learn who she really is."

    yu "So, uh...sorry. What’s your name again?"
    ri "Rika. I’m Rin’s mom."
    yu "And...who is Rin?"
    ri "My daughter. She’s adorable. Do you like Mexican food?"
    yu "Uh...sure. It’s fine, I guess."
    ri "We have so much in common."
    s "Did you really turn a straight girl into a lesbian? Because you’re just as awkward when it comes to flirting as your daughter."

    scene yukirikavisit20
    with dissolve

    ri "{i}I’m seriously going to kill you!~{/i}"
    yu "Flirting?"

    scene yukirikavisit19
    with dissolve

    ri "Nope! Not me. Just sharing some sugary treats with neighbors in preparation for everyone’s favorite holiday."
    yu "Not mine. Halloween ain’t exactly full of happy memories for me."

    scene yukirikavisit21
    with dissolve

    ri "What? Really? How come?"
    s "It’s her daughter’s birthday."
    ri "Shouldn’t that make it even better then? "
    yu "Could’ve if I never ran out on her. Now, all it really does is remind me of all the birthdays she had to spend alone."

    scene yukirikavisit22
    with dissolve

    ri "O...Oh. Well...I’m sure you had your reasons!"
    yu "Drugs and Yakuza shit. Mostly drugs. "

    scene yukirikavisit23
    with dissolve

    ri "...Oh."
    yu "Yeah. Thanks for the cookies, though."

    "Update: It did not take very long for Rika to find out who Yuki really is."

    ri "You, uhh..."
    ri "Are you still involved in that kind of stuff?"
    yu "You ain’t a cop, are you?"

    scene yukirikavisit24
    with dissolve

    ri "Me? No. I’ve actually been arrested before, so...I’m not sure they’d even let {i}me{/i} be one if I wanted to. I just...well, you know. That stuff is dangerous. {i}Both{/i} of those things."
    yu "The Yakuza’s only dangerous if you get yourself involved with ‘em. They rarely fuck with anyone on the outside."
    ri "Well, yeah. But you {i}are{/i} involved with them. And the drugs-"
    yu "Is it a hobby of yours to come into people’s apartments and interrogate them?"

    scene yukirikavisit25
    with dissolve

    s "She just wants to be your friend, Yuki. Rika’s a good person. "
    yu "Then she probably shouldn’t be my friend. You saw earlier how well I do with “good people.”"
    ri "I was just...I have friends who used to do that stuff too. And one of them runs an NA group in the Urban District. Figured you just...might wanna-"
    yu "The one that meets in the old expo center? Or the one that meets in the church?"

    scene yukirikavisit26
    with dissolve

    ri "The church! You already know about it, then?"
    yu "Yeah, they don’t like me over there. Granted, I was still probably your age when I last tried going, so shit might’ve changed by now."
    s "Rika is 42."

    scene yukirikavisit27
    with dissolve

    yu "What? This girl? Are you fucking kidding me?"
    ri "You can call me “Onee-san” if you want. In fact, please do. I insist."
    yu "How the fuck do you look so young if you’re older than me? That ain’t fair."
    s "I imagine the part where she isn’t a drug addict might have something to do with it."
    ri "I exercise a lot. But also, yeah. I’ve never done any hard drugs. I used to grow pot when I was in my twenties, though. That was fun. And very illegal. Not why I was arrested, though."

    scene yukirikavisit28
    with dissolve

    ri "But, that said, you don’t look {i}that{/i} old. Your skin’s still nice. Maybe a little pale, sure. But you look soft. I want to touch you."
    yu "Don’t."

    scene yukirikavisit29
    with dissolve

    ri "Honestly, though? I feel like figuring out how to get rid of those dark circles will knock like ten years off the way you look. Maybe some more bleach too. Your hair looks kind of faded."
    yu "First an interrogation, now a makeover? Am I gonna have to find a new apartment or are you gonna learn how to back off a little?"
    ri "Hey, you asked this time. I’m just sharing my secrets with you. "
    ri "So if {i}you{/i} want to share some secrets with me. Like...oh, I don’t know, how likely you are to ever kiss a girl? That’d be cool. Like, I definitely wouldn’t tell anybody. Nope."
    yu "You know what? Why don’t we go back to talkin’ about {i}less{/i} personal shit? "
    yu "Cause the {i}last{/i} fuckin’ thing I need is one more person to let down and you’re gettin’ way too close way too quickly."
    ri "Well, what do you want to talk about instead? Because I figured the Halloween part of the conversation would take up least fifteen minutes and we never even got into that part."
    yu "Beats me. How’d the two of {i}you guys{/i} meet anyway?"
    ri "He walked in on me while I was wearing nothing but a towel."

    scene yukirikavisit30
    with dissolve

    yu "And you...became friends?"
    ri "I mean, yeah. It’s not like anything sexual happened."
    s "It wasn’t until a little while later that she grabbed my penis."

    scene yukirikavisit31
    with dissolve

    ri "I did it to protect my daughter."
    yu "..."
    yu "Well, I’m about ready to hit the sack now."
    ri "You don’t have to hit it. Just sorta firmly grasp it and you can get a feel for- oh, you’re tired."
    s "Can’t really blame her since she was passed out drunk until just before you showed up. If she had it her way, we wouldn’t even be here right now."
    ri "As someone new to the world of alcohol, I’ve found it’s best to stop drinking {i}before{/i} you get to that part. So no one can take advantage of you and whatnot."
    s "Probably best to not say things like that around Yuki."
    ri "Say what? I’m in kind of a trance right now and am only barely conscious of what I’m actually saying. It’s all just words."
    yu "Rika, thanks for the cookies and shit. But I feel like you and I ain’t as...{i}compatible{/i} as you might’a thought. So I think it’d be cool if you just left or-"
    ri "Can I see your tattoo?"

    scene yukirikavisit32
    with dissolve

    yu "{i}Hah...{/i}"
    ri "Sorry. It’s just a nice piece and gives me an excuse for my skin to touch your skin."
    yu "{i}Fine.{/i} Just make it quick."

    scene yukirikavisit33
    with dissolve

    ri "Yay!"
    s "I’m surprised you’re even letting her with how annoyed you appear to be getting."
    yu "Feels like a lost puppy wandered into my apartment and now I’ve gotta reluctantly feed it so it won’t fuckin’ die."
    ri "That’s funny because that’s exactly how I’ve felt ever since my partner kicked me out to the curb!"

    scene yukirikavisit34
    with dissolve

    ri "Some of the detail here is really nice. Where’d you get it done? Why didn’t you get it finished? Was it a money thing?"

    scene yukirikavisit35
    with fade

    yu "Why you askin’? You got another friend who runs a tattoo shop somewhere? "
    ri "Yes, actually. She’s the one who does all of my work. And I could probably get you a good deal if you-"
    yu "That ain’t just a regular ass tattoo on my back, you know. It was the start of my horimono. And it ain’t filled in because I bailed on the Yakuza."
    yu "Now, it’s just a big fuckin’ dragon-shaped scar that reminds me of how I let myself get sucked into a life of crime rather than taking over a fuckin’ countryside candy shop."
    ri "You like candy? I like candy. How about you cast aside your disdain for Halloween and we go trick or treating together?"
    yu "Jesus Christ, you really are a puppy."
    ri "You’re right. I am loyal and you can pet me as much you want. Additionally, I have a very impressive tongue and I love to lick. "
    s "Oh, I get it now. You turned Rie into a lesbian through persistence."
    ri "Shush."
    yu "I ain’t into chicks, Rika. It ain’t happenin’."
    ri "Can we be {i}friends,{/i} though? "
    yu "Why? You want to try and “fix” me? All the hints I’ve been droppin’ about who I really am not doin’ enough to push you away? You gonna literally make me drag you outta here?"
    ri "If I {i}do{/i} want to fix you, is that bad?"
    yu "..."
    ri "Isn’t the whole point of a friendship or a relationship in general for two people to fill in gaps we can’t figure out how to fill on our own?"
    ri "You’re unhappy, aren’t you? Maybe I can help. And maybe you can help {i}me{/i} feel a little less alone too."
    ri "Everyone I know already has someone. And so did I until a little while ago. But I {i}do{/i} feel kind of lost now. And you’re right next door. So maybe we-"
    yu "Beat it."

    scene yukirikavisit36
    with dissolve

    ri "..."
    yu "There’s already one happy-go-lucky girl dead set on makin’ my life all exhausting and shit. I don’t need another one. Even if we {i}do{/i} have some shit in common."
    ri "But-"
    yu "{i}Beat it.{/i}"
    yu "I ain’t sayin’ it again."

    scene black
    with dissolve2

    ri "Sorry for...bothering you."

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene yukirikavisit37
    with dissolve2

    s "..."
    yu "..."
    s "Pretty soon, I’m going to be the only thing you have left to throw away."
    yu "I’m doing her a favor and you know it."
    yu "It’s bad enough that I already pulled Sara into this."
    s "Is there {i}anything{/i} I can do for you, Yuki? Anything that will actually {i}help.{/i}"
    yu "Just take care of Yumi if some shit ever happens to me, aight?"
    s "..."

    scene yukirikavisit38
    with dissolve

    yu "She needs somebody to look up to. And she’s gonna realize really fuckin’ soon that ain’t ever gonna be me no matter how much she tries to tell herself it will be."
    s "Are you going to try to get clean again?"
    yu "I ain’t ever technically admitted I ain’t."
    s "You’re right. But I’m also well-versed in hiding the truth from people. And we both know this goes deeper than just drinking."
    yu "..."
    s "I care about you, Yuki."
    yu "I care about you too. "

    scene black
    with dissolve2
    stop music fadeout 10.0

    yu "It’d be nice if that actually made a difference."

    "I leave her apartment unsure of whether or not she’ll go to sleep the way she is now or if she’ll find something to help her."
    "And when I make it home and sit down at my desk, I realize I’m the same way."
    "Illuminated by the blue glow of my computer monitor, I unzip and unbutton my jeans, then slide them down until they’re in a ring around my ankles."
    "I cum hard into a bundle of tissues as a silent video plays before me."
    "They say it feels better than sex."

    $ renpy.end_replay()
    $ yukispring2 = True
    $ yuki_love += 1

    if sarasex == False:
        $ saraspring2miss = True
        $ tsubasaspring2miss = True
        $ tsubasaspring3miss = True

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
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

label yukispring3:
    play sound "static.mp3"
    scene yukiatthedoor1 with flash
    stop sound

    y "{i}Can you shut the fuck up about my tits?! It’s every fucking day with you! You literally never stop!{/i}"
    yu "..........?"
    y "{i}Oh my fucking- fine! I’ll leave! She’s probably not fucking here anyway. I have a better chance of finding her passed out in a fucking alley somewhere.{/i}"

    play sound "footsteps.mp3"
    scene yukiatthedoor2 with dissolve2
    play music "hometown.mp3"

    y "{i}{size=-2}Oh — and if I do, I’ll fucking kill her myself. Mark my fucking words. Stupid piece of shit fucking worthless mother! Fuck!{/i}"
    yu "Mm..."

    "Yuki Yamaguchi could do little more than let her cigarette burn as she sat there, pressed against the wall and listening to the footsteps of her daughter fade away."
    "At first, she wanted to talk to her. She wanted to try and explain things or {i}apologize{/i} or...really just do {i}anything{/i} but vanish."
    "But upon reflection, she understood that vanishing was what would be best for the girl. And that reappearing {i}at all{/i} was a mistake."
    "She should have never come back. She should have died, passed out in a fucking alley somewhere, just like her daughter said. "
    "But old habits got the best of her and forced her to fight. To try and preserve the little bit of life she still clung to. "
    "In that context, fighting meant turning things around. It meant getting clean — sifting through countless trash bins to find the puzzle pieces that fell from her pockets on laps around the city."
    "She remembers the wind in her hair. She remembers the lights. {i}God,{/i} she loved those lights — and how they’d always guide her home, even when they were blurred by the speed of her bike."
    "Nowadays, everything was blurry — a side effect of pumping every illicit substance she could find into her body to try and shock it back to life."
    "Gone were the days of fighting to live. Now, she just wanted to {i}fight.{/i}"
    "And it didn’t matter what. It didn’t matter who. So she settled on fighting herself as a means of accelerating a long overdue punishment she’d always known would catch up to her."

    scene black
    with dissolve2

    "She never thought it’d be like {i}this,{/i} though."

    scene yukiatthedoor3
    with dissolve2

    "She takes another drag of her cigarette, unsure of what sort of effect its toxicity would have on her decaying physical form. But again, that didn’t matter much now."

    scene yukiatthedoor4
    with dissolve2

    yu "{i}Hah...{/i}"

    "The locks had been changed. Yumi’s number had been blocked. And she’d even taken the liberty of informing her neighbors that she didn’t want her daughter around here anymore."
    "Of course that raised questions — but people seldom questioned {i}Yuki.{/i} Because even when she was in the wrong, which she so commonly was, she could {i}sound{/i} like she wasn’t."
    "A skill acquired to better get the things she wanted whenever she wanted them. And one not at all dissimilar from those who ran the same laps around the city. "

    scene yukiatthedoor5
    with dissolve2

    "But still, there was one thing she wanted that she would deprive herself of — and it must have been halfway around the block by now."
    "This could be the last time she ever heard her voice."
    "It probably {i}wouldn’t{/i} be. But it {i}could{/i} be. And despite how accustomed she had become to thinking such a thing, it did little to numb the pain. That’s where the drugs came in."
    "But even those were losing their luster. And Yuki was quickly learning that despite how {i}good{/i} they could make her feel, they would never kill the fear of death."
    "After thirty-eight years, she had finally run out of gas. "
    "And she would die in this room whether she liked it or not."

    scene yukiatthedoor6
    with dissolve2

    "She taps on a name in her phone and takes a sip from a potion she used to believe would grant her eternal life. Or at least it was something she would joke about when it was still fun to joke at all."
    "All things considered, alcohol was the least of her worries. It wasn’t her liver that was rotting, after all. That much she knew."
    "But it didn’t change the fact that this very elixir was the same one that took the lives of girls she used to know before venturing off into the world alone."

    scene yukiatthedoor7
    with dissolve2

    "As the phone continued to ring, she remembered a friend who’d drink mouthwash when she couldn’t get her hands on alcohol."
    "And as she, in her drunken stupor, kicked over a stack of cans that spilled violently onto a small bundle of hypodermic needles, she thanked herself for never being {i}that{/i} pathetic."

    play sound "phonebeep.wav"

    s "{i}Hel-{/i}"
    yu "‘Bout fuckin’ time you picked up."

    play sound "static.mp3"
    scene yukiatthedoor8 with flash
    stop sound

    s "About time you {i}called.{/i}"
    yu "{i}Guessing you’ve already heard the news then, huh? Fucking brat — sharing personal information with her goddamn teacher of all people.{/i}"
    s "Are you drunk?"
    yu "{i}I’m a whole fuckin’ bunch of things, Akira. Drunk is just one of ‘em.{/i}"
    s "..."
    yu "{i}Anyway, you still want to fuck me? So bored that I’m fuckin’ dying over here. Get it?{/i}"
    s "That’s not funny, Yuki."

    play sound "static.mp3"
    scene yukiatthedoor9 with flash
    stop sound

    yu "Oh, would you fuckin’ grow a pair? Come on. That was a {i}little{/i} funny. Admit it."
    s "{i}I disagree. But I’m sure I have at least one friend who would find it hilarious.{/i}"
    yu "Oh yeah? Bring them over too. I’m fuckin’ everybody tonight. Gotta go out with a bang, you know?"
    s "{i}So you get cancer and...what? You just start using puns all the time?{/i}"
    yu "Who cares? You coming or not?"
    s "{i}No, Yuki. I am not coming over there to fuck you. I’m pissed off at you for hiding this from me and even more pissed off that you think I’d overlook that just to get in your pants.{/i}"
    yu "The fuck do {i}you{/i} have to be mad about, huh? Yumi, I get. You, though? You’re just some random fucking guy. We don’t actually give a shit about each other, do we?"

    play sound "static.mp3"
    scene yukiatthedoor10 with flash
    stop sound

    s "..."
    yu "{i}Hello? Helloooooooo?{/i}"
    s "I’m trying not to hold it against you because I know you’re fucked up right now. But that hurt, Yuki. I really do care about you."
    yu "{i}Oh yeah? Then name three good things about me. Go on. I’m listening.{/i}"
    s "I don’t think I can, to be honest. You’re a pretty terrible person."
    yu "{i}Ha! Now THAT is funny!{/i}"
    s "There don’t need to be any good things about you for me to like you, though. For example, there’s nothing good about me and {i}plenty{/i} of people like me."
    yu "{i}Well hey- that’s fuckin’ great, man. It’s really cool you’ve got a whole fuckin’ fan club and I’ve got god damn fucking Rika and that’s it.{/i}"
    s "You had Sara too until you shat all over her. How’s that working out for you?"

    play sound "static.mp3"
    scene yukiatthedoor11 with flash
    stop sound

    yu "Fuckin’ horrible. I’m broke as shit now- which is actually the {i}real{/i} reason I’m calling. Can you lend me some money for laundry? I’m outta clean clothes."
    s "{i}How much do you need?{/i}"
    yu "{i}Hundred-grand maybe?{/i}"
    s "{i}A hundred-thousand yen? You really expect me to believe you have that much laundry when I’ve only seen you wear a total of three outfits?{/i}"
    yu "Aww, you kept track? Tell you what — you come over now and I’ll let you fuck me in all three of them."
    s "{i}I’m not lending you any money, Yuki. Not knowing what you’d use it for.{/i}"
    yu "Not even if I say it’s for hospital bills?"
    s "{i}...{/i}"
    yu "That’s what Yumi found, you know. She tell you that? Bitch ripped up the damn bill and left it in pieces all over the floor. Hell of a thing to come home to, you know."
    yu "Like, it’s one thing to find out you’re dying. But not knowing what you owe on top of that? Man. Life’s fuckin-"
    s "{i}Are you actually dying, Yuki? Like...what...what is it, exactly?{/i}"
    yu "Like, what kinda cancer? How long do I have? That what you want to know? You don’t want to be surprised?"
    s "{i}By you suddenly dying one day? Not really, no.{/i}"
    yu "What if I told you I only have a week left?"
    s "{i}Yuki-{/i}"
    yu "Would you spend all of it with me?...Read me bedtime stories?...Hold me in those fuckin’ wimpy ass noodle arms of yours and kiss me on the forehead all cute-like?"
    s "{i}Please don’t joke with me right now.{/i}"
    yu "What if it was a month? A year, even. How long could I get you to stay with me before you leave, Akira? Tell me. How long?"
    s "{i}I’m not the one you really want by your side right now. We both know that.{/i}"

    scene yukiatthedoor12
    with dissolve2

    yu "..."
    s "{i}You need to talk to her, Yuki. She’s not taking it well.{/i}"
    yu "She was..."
    yu "She was just here...a little while ago."
    s "{i}She was? So you talked to her then?{/i}"

    scene yukiatthedoor13
    with dissolve

    yu "No, I...kinda just sat up against the door and...didn’t do shit."
    yu "She might’ve been with somebody? Was talkin’ to someone. Either that or I’m just high as fuck. Hell, maybe she was never here at all and I just hallucinated the whole damn thing?"
    s "{i}Please talk to her. You owe her that much. And if things are really as bad as you’re making them sound-{/i}"
    yu "I don’t..um..."
    yu "I don’t really know...{i}how{/i} bad things are...exactly..."

    play sound "static.mp3"
    scene yukiatthedoor14 with flash
    stop sound

    s "...What?"
    yu "{i}Yeah...I had other appointments and like...follow-up shit scheduled, but...{/i}"
    s "..."
    yu "{i}I sort of just...didn’t go...{/i}"
    s "You...didn’t go..."
    yu "{i}It’s in my lungs, Akira. Surprise, surprise.{/i}"
    s "Yuki, what the fuck do you mean you didn’t go? How much do you know? Did they tell you how serious it is? "

    scene yukiatthedoor15
    with dissolve

    s "They can still do something, can’t they? I’ll go with you if you want. But if you sit back and just let this happen, who knows how bad it can get? Why don’t you just-"
    yu "{i}Because I’m fucking scared, okay?!{/i}"

    play sound "static.mp3"
    scene yukiatthedoor16 with flash
    stop sound

    yu "{i}That’s{/i} why I haven’t gone back! Am I not allowed to be scared?! "
    yu "I don’t want to fucking die, Akira! Why is this happening to me?! Why {i}now?!{/i} Everything was so good! I’m so fucking scared! I don’t know what to do!"
    s "{i}Neither do I, but I know that running away from it will only make it worse. You need to fight, Yuki.{/i}"
    yu "All I’ve ever done is fight! But this is...it’s different! I don’t think I...I don’t think I can win this one, Akira...I don’t know if...I just..."

    scene yukiatthedoor17
    with dissolve

    yu "I don’t have it in me anymore..."
    yu "If the news is bad...then what? Do they tell me how long I have? Because {i}you{/i} might want to know, but {i}I{/i} don’t..."
    yu "{size=-2}I don’t want to know any of it...what’ll happen to my body...my lungs...and that’s not even mentioning my fucking brain. I’ve been smoking since I was like eleven. I don’t know how {i}not{/i} to.{/size}"
    s "{i}So what then? You’re just going to sit in the dark and hide from your daughter until Rika finds you dead on the floor? Is that the plan?{/i} "
    yu "There is no plan...I’m just scared..."
    yu "I’m so fucking scared...I don’t want to die..."

    play sound "static.mp3"
    scene yukiatthedoor18 with flash
    stop sound

    yu "{i}I don’t want to die! I can’t do this! I’ve never been this scared about ANYTHING before and I’ve had fucking GUNS pointed at me, Akira! Why were those less scary than this?!{/i}"
    yu "{i}What if there’s nothing after this?! What if it’s just fucking...dark and...what if everything just ends?! What then?! Am I just gone?! After all of this, am I just gone?! {/i}"
    yu "{i}What good was trying to fix everything then?! What good was trying at all?!{/i}"
    yu "{i}That’s why I’m fucking using and drinking and killing MYSELF again because it’s better for me to do it than a fucking SICKNESS, Akira! Fuck! I’m so scared! I’m so-{/i}"
    s "..."
    s "Yuki? Are you there?"
    yu "{i}...{/i}"
    yu "{i}Someone’s here.{/i}"

    play sound "static.mp3"
    scene yukiatthedoor19 with flash
    stop sound

    s "{i}What?{/i}"
    yu "It’s Yumi...she never left..."
    yu "Oh God, she never fucking left and now she’s heard me screaming all of that shit?! What do I do now?!"

    play sound "knock.mp3"

    s "{i}You hang up on me and talk to her instead. If anyone can convince you to get help, it’s her. Not me.{/i}"
    yu "She’s gonna fucking hate me, Akira...more than she already does...I came back into her life just to fucking die and she’s never going to trust {i}anyone{/i} again...it’s all my fault..."
    yu "It’s all my fucking fault!"

    play sound "knock.mp3"

    s "{i}Hang up. The fucking. Phone. And answer. The door.{/i}"
    yu "Can I keep you on speaker?..."
    s "{i}Yuki, I love you. I hope you get help. I’m hanging up now.{/i}"
    yu "Akira, wait!"

    play sound "static.mp3"
    scene yukiatthedoor20 with flash
    stop sound

    yu "Oh god...oh no..."
    yu "How do I...where do I even..."

    play sound "knock.mp3"
    scene yukiatthedoor21 with dissolve

    yu "JUST GO AWAY! PLEASE! I’M SORRY FOR EVERYTHING! "
    yu "I’M SORRY FOR LEAVING YOU! I’M SORRY FOR BEING AN ADDICT! I’M SORRY FOR COMING BACK AND I’M SORRY FOR ABANDONING YOU AGAIN! I’M SORRY! I’M SO FUCKING-"

    play sound "knock.mp3"

    k "{i}Aunt Yuki! Open the door! Right now!{/i}"

    scene yukiatthedoor22
    with dissolve2
    stop music fadeout 5.0

    yu "...Kaori? Is that you?..."
    k "{i}Yes, Aunt Yuki...{/i}"
    k "{i}Now please...{/i}"

    scene black
    with dissolve2

    k "{i}Open the door...{/i}"

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ yukispring3 = True

    jump yukispring4

label yukispring4:
    scene yukikaorishere1
    with dissolve2
    play music "merrychristmasmrlawrence.mp3"

    k "The words that fell from your mouth just now...how much truth do they possess?"
    yu "..."
    k "You are...dying?"
    yu "You...weren’t supposed to hear any of that, Kaori."
    k "But...I {i}did{/i} hear it. And your appearance is not that of one who dies even if your color is less colorful now than it has been in the past."
    yu "Yeah, well...life fucking sucks. What do you want from me?"
    k "Honesty..."
    k "If there is fear in your heart, it helps to have someone who will listen to its beating. Someone to strike fear into the heart of fear itself so the fear’s heart becomes fearful itself."
    k "But I fear that you won’t do that. Which makes {i}me{/i} fearful. "
    k "Will I lose you too now?"
    yu "You...shouldn’t be here, Kaori..."
    yu "Why...{i}are{/i} you here anyway? I haven’t seen you in months."

    scene yukikaorishere2
    with dissolve

    k "My reasons lack importance now! What matters is that I {i}am{/i} here! Even if I am not the one you want, I am the one you have! So have me! Speak the words that deserve speaking!"

    play sound "static.mp3"
    scene yukikaorishere3 with flash
    stop sound

    yu "But everything...becomes more {i}real{/i} when I start to talk about it...and I...it’s just..."
    k "Things have already become real now that there are tears where there haven’t been before."
    k "The Yukiburger I know is strong...And violent, but not necessarily in a negative way. She would not stand here in the dark with a wet face and an armful of secrets!"

    scene yukikaorishere4
    with dissolve

    yu "That Yuki’s already gone, Kaori...You get the {i}old{/i} me now. The one who’d trade anything and everything for one more night of feeling alive."
    yu "And yeah...I’m probably dying. If you want the truth...I’m probably dying. Which means I might not have many nights left at all. So do yourself a favor and just..."
    yu "Just bail out while you can, okay? Every second you stay here adds another day you’ll have to mourn me."

    play sound "static.mp3"
    scene yukikaorishere5 with flash
    stop sound

    k "And every second I am {i}not{/i} here adds another where you will be afraid."
    k "I will mourn for however long you think it takes to prevent that for you. That is what it means to be family. I think."
    yu "Haven’t you mourned enough already?..."
    k "If I have, I can’t remember it. So it’s like I’ve never mourned at all. Maybe I will enjoy it? And spending each day remembering you will not be as sad as you expect."
    yu "..."
    k "Now explain to me — why are you leaving this place? "
    k "Please let me listen to your heart."

    scene yukikaorishere6
    with fade

    yu "Why?..."
    yu "What’s even the point?"
    yu "It’s not like you’d hear anything if I did. "

    scene yukikaorishere7
    with dissolve

    yu "In fact, I don’t think it’s beaten a single fucking time since I was a teenager. "
    yu "So...heh...maybe I’m overreacting?..."
    yu "Maybe I’ve been dead this whole time and you’ve been cozying up to a fucking zombie pretending to still have some reason to be here."
    yu "What’s that say about {i}you,{/i} huh? That you’d waste so much time and effort on something already beyond saving? Don’t you have better shit to do, Kaori?"
    yu "Just get the fuck out of here, okay? You never should have come in the first place."

    play sound "static.mp3"
    scene yukikaorishere8 with flash
    stop sound

    k "You opened the door."
    yu "...huh?"
    k "You would not have opened the door if you did not want to be saved. So there is something inside of you that is begging for help."
    k "Would you like me to keep you alive, Aunt Yuki?"
    yu "And how would you do that, Kaori?...Not everyone can be fucking...Frankensteined back to life like you were. And not all of us {i}deserve{/i} it either."
    k "It is not up to you to decide who is and is not worthy of life. The gods don’t like it when you pretend to be them, Aunt Yuki."

    play sound "static.mp3"
    scene yukikaorishere9 with flash
    stop sound

    yu "What- you religious now? Is {i}that{/i} what you meant by “keeping me alive?” Think a prayer circle’s gonna fix my lungs?"
    k "Not at all."
    k "In fact, I think breathing as a whole isn’t all it’s cracked up to be."

    scene yukikaorishere10
    with dissolve

    yu "...huh?"

    play sound "static.mp3"
    scene yukikaorishere11 with flash
    stop sound

    k "Look at you — flailing around like a fish washed ashore, waiting for your bones to be picked clean by some sort of carnivorous bird."
    k "What would you say to those who died fighting? Who actually {i}tried?{/i} That they were foolish for wanting to stay here — in a place that has so regularly {i}fucked{/i} you, Aunt Yuki?"
    k "Should {i}I{/i} have died too? For {i}I{/i} had done nothing to deserve life besides {i}want{/i} it. "
    k "Or perhaps {i}I’ve{/i} become a zombie as well? Perhaps I {i}did{/i} die. And everything I do now is pointless and dull and just delaying an inevitable {i}second{/i} death."
    yu "Jesus...between Yumi talkin’ to herself and your eyes fuckin’ changing colors, I’ve gotta be way higher than I thought I was."
    k "Your time will most assuredly come — but only if the clock keeps ticking."
    k "Which means that all you need to do is stop it. And that’s much easier than it sounds, I think."

    play sound "static.mp3"
    scene happy9 with flash
    scene happy8 with flash
    scene yukikaorishere12 with flash
    stop sound

    k "Ah."
    yu "Yeah...you think a lot of shit, Kaori. And with all due respect, basically all of it is bullshit."

    play sound "static.mp3"
    scene yukikaorishere13 with flash
    stop sound

    yu "But I’ve gotta applaud your...{i}positivity{/i} at least. You and Rika do a damn good job of making me slightly more optimistic about decomposing in the near future. "
    k "J...Just tell me what I can do to help you! Anything!"
    yu "..."
    k "..."
    yu "You got any money?..."
    k "Money?"
    yu "Yeah...need it for laundry and shit like that. "
    k "How many moneys do you require? My portable rectangle holder is inside of my housebox right now, so all I have are circles. Would you like the big circle? The medium circle? The small-"
    yu "I...uhh...I can wait until you have your...{i}rectangle holder{/i} again. Got...lots of clothes to wash..."
    k "I know this is true because you are currently naked. I thank you for no longer lying to me."
    k "But what about fixing your body? How many moneys-"
    yu "Nothing’s fixing me, Kaori. It ain’t happenin’."
    yu "But there’s shit that can make what’s left of my time here more bearable...and it just..."
    yu "I feel more comfortable focusin’ on that instead of what comes after..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yukikaorishere14
    with dissolve2

    "Despite the incessant pleas for her departure, Kaori Kadowaki refused to leave her aunt’s side — offering up her lap as a pillow in the dying woman’s time of need."
    "But was she {i}really{/i} dying at all? Because {i}dying{/i} implies that a result will be reached. And based on what the girl inside of the girl said, that would require some help from time itself."
    "If that final day could never be reached, would it really still be {i}dying?{/i} Or would she simply just be sick?"
    "These are the questions I must ask myself as an observer deprived of the facts that would necessitate the completion of an unending thought. "
    "And this thought is just one that serves as the foundation for this place as a whole. "
    "{i}What if{/i} the ones we loved could never leave? "
    "What if {i}everyone{/i} loved us in general?"
    "How would that world look? And if you were to somehow, by unconventional means, find out how to venture outside of it — how would things look {i}there?{/i}"
    "Maybe you’d be an unwelcome visitor in someone else’s paradise?"
    "Maybe you already {i}are?{/i}"
    "In any case — squatters have rights too. And Yuki Yamaguchi was {i}all{/i} too familiar with this as she’d spent the vast majority of her life sleeping anywhere she could find."
    "That said, if she were to die in this room, that alone could be called a victory — albeit one much too small for how hard she’d fought to get here."
    "Unfortunately, with no source of income, {i}this{/i} could be gone at any moment. And the chances of her continuing her fight dwindled by the minute as her opponent was a dragon this time."
    "And despite Yuki having been a bit of a dragon herself in her younger years, those days were long gone. She healed slower. Got tired quicker. Lacked any sort of substantial motivation."
    "But the thing that pushed her closer to retirement wasn’t any of that. In fact, it was something much simpler."
    "She just didn’t know what she was even trying to “win” anymore. "
    "What was the prize? Just more of {i}this?{/i} "
    "More pain? "
    "More knowing that something terrible could happen at any moment and take everything away?"
    "She was right to be scared."
    "And everyone who isn’t is wrong. "
    "But does that mean one should just give up?"
    "This is one more question I must ask myself as an observer deprived of the facts that would necessitate the completion of an unending thought. "
    "Just there is no thought {i}more{/i} unending than the one currently swimming through the drug-addled mind of a thankless burnout."

    yu "I’m scared, Kaori..."
    k "I know, Aunt Yuki..."
    yu "I don’t want to die..."
    k "You {i}won’t...{/i}"
    k "You will stay here...and we will go somewhere nice with Nao-chan. Somewhere with all the dizzy drinks and smoke-tubes your heart could ever desire."
    yu "Don’t give me hope...it’s the last thing I need."
    k "But it {i}could{/i} be the first."
    k "What if hope is {i}all{/i} you need? And everything else comes after?"
    yu "That sort of thing doesn’t save people. Just makes them angrier when it don’t work out the way they want."
    yu "Knew this girl once...young. Got attacked one night. Found her beaten so bad she couldn’t move. "
    yu "We rushed her to the hospital. Stayed there for a week, livin’ off of free coffee and food we’d snatch off carts left out in the halls."
    k "Did you not drink the juice? I drank many juices when I was in the hospital. So many that I became juice myself."
    yu "Sometimes, maybe? But anyway, five days in, girl regained some feeling in her legs. Doctors said it was a good sign. That she might be able to walk again if things kept improving."
    k "And...did they?..."
    yu "What do {i}you{/i} think?...Wouldn’t be tellin’ this story if it had a happy ending."
    yu "We all got in on it. Started hyping her up. Tellin’ her she’d be fine in no time at all."
    yu "Day seven, the feeling was gone again. Just...went away. "
    yu "And never came back."
    yu "Still remember the look on her face. The...realization. Panic. The tone of the doc’s voice from the hallway when we heard him ordering more tests."
    yu "She was a little fireball, that girl. Started throwin’ shit around and screaming at the nurses about how fucked up it was to make her think she had a shot at bein’ normal again."
    yu "That’s when they made us leave. Surprised they let us stay as long as they did, to be honest. "
    yu "But ever since then, I’ve had a hard time tryin’ to look on the bright side when it comes to shit like this. Think that expectin’ the best just makes anythin’ {i}else{/i} feel like the worst."
    yu "I don’t want my last thoughts on this planet to be cursin’ out whoever it is that made me think I had a shot."
    k "I’m sorry, Aunt Yuki..."
    k "I don’t know what other words would help right now..."

    scene yukikaorishere15
    with fade

    yu "I already told you...there ain’t nothin’ that can help, Kaori."
    yu "But...thank you for being here..."
    yu "It’s nice...this warmth..."
    k "If only you did not have so much laundry to feed to the clean-machine. Then you could put on a thick jacket-coat and become even less cold."
    k "Do not worry, Yukiburger. Soon, I will provide you with all of the paper rectangles in my-"
    yu "Just keep the money, Kaori. I changed my mind."
    k "What? But how will you-"
    yu "I got one lifeline, still. Don’t worry. "
    yu "You mind doin’ somethin’ else for me, though? Doesn’t have to be now, just...whenever I’m gone."

    scene yukikaorishere16
    with fade

    k "I do not like the idea of making a promise that will only matter after you have left me behind."
    yu "It’s {i}because{/i} I’m leavin’ you behind that I’m askin’ at all."
    k "Then...what would you like from me?"
    yu "I..."
    yu "Kaori, I...know you don’t remember her...and I know she’ll probably make it difficult for you, but..."
    yu "If you could look after Yumi when I’m gone...I’d really appreciate that..."
    k "The Yumi is your daughterburger, yes?"
    yu "That’s right...and your cousin..."
    yu "You two would play together when you were little...you were kind of like a role model to her...being older and...shit like that..."
    k "Can you tell me what sorts of roles I modeled so I may better replicate our prior connection when you have departed?"
    yu "I ain’t askin’ you to be your old self and take her under your wing or anything like that, just..."
    yu "She could use some friends...and I know you like makin’ em..."
    k "But what if she doesn’t like me? There are many people who seem to misunderstand the person I am. "
    yu "Honestly, she probably {i}won’t{/i} like you. It won’t be personal, though. She doesn’t like anybody."
    k "Then why do you want me to-"
    yu "Because you’re all she’ll have. "
    yu "You and that fuckin’ blonde girl who nearly killed Gary at least...but she doesn’t like me much and I can’t imagine she’d feel any better about me {i}now.{/i}"
    k "Does the Yumi know that you think you are dying as well?"

    scene yukikaorishere17
    with fade

    yu "I don’t just {i}think{/i} it...I know it. It’s real, Kaori. And yeah...Yumi knows. She found out by bein’ a fuckin’ nosy bitch. Same as you."
    yu "Guess it runs in the family."
    k "I am sorry that I overheard your secret...but I am also glad because it brought us together."
    yu "Mhm...sure..."
    yu "Now, you gonna tell me why you came over here in the first place? Or do you want me to go fuck myself one last time before I can’t anymore?"
    k "I can give you privacy if that is something you would like to do. I do not believe I am supposed to watch other people’s private time."
    yu "Not like that, you fucking idiot."
    k "I am sorry, Aunt Yukiburger. I am still only a fucking novice."
    yu "Whatever you are, promise me you’ll look after Yumi...okay? "
    yu "I’m trusting you to do what I couldn’t."
    k "..."
    yu "Please...it’d..."

    scene yukikaorishere18
    with dissolve2

    yu "Make me..."

    scene yukikaorishere19
    with dissolve2

    yu "Mn...hngh!"
    k "Aunt Yukiburger?! Is it happening?! Should I dial the numbers?!"
    yu "Just a...sudden headache! Don’t...worry about it!"

    scene black
    with dissolve2

    k "I will obtain the blood of the ocean for you to consume! Stay right there!"
    yu "There’s...a can of beer I haven’t finished near the-"
    k "Refused! The ocean blood will fix your head. You have not done enough of the hydrating."
    yu "Mn...aah...f...fine! Just fucking...ngh!"

    stop music
    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    s "..."
    s "..."
    s "..."

    "I hope that Yuki was able to tell Yumi everything tonight."
    "But more than that, I hope that Yumi was able to understand it."
    "And I hope that soon enough, I’ll be able to as well."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    "I crawl into bed beside someone who’s already asleep and silently whisper “goodnight” to her."
    "And while I half-expect to hear someone uninvited whisper it back from the corner of the room, there is nothing but silence."
    "There is nothing but silence."
    "There is nothing."

    $ renpy.end_replay()
    $ yukispring4 = True
    $ yuki_love += 1

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
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

label yukispring5:
    $ totaldays += 1
    $ day = 1
    hide sunday onlayer date
    show monday onlayer date

    "{i}The following morning...somewhere in the Old District...{/i}"

    play music "bloodandsunset.mp3"
    scene yukineedsmoney1 with dissolve4

    "If there was anything in life Yuki hated more than the Yamaguchi estate, it was the man who ran it."
    "That wasn’t always the case, though. "
    "To be clear, she never had any respect for him. But back when taking his name sounded like a good idea, her feelings hadn’t blossomed into {i}hate{/i} yet."
    "That would come over the next several years between the bouts of willing sedation that he’d thrust upon her in exchange for sex."
    "“A fair trade,” she thought. And it’s not as if she would remember most of it anyway as the showering of {i}presents{/i} would be a blanket she could hold over her face to ignore what was happening."
    "“Just a few more minutes. One more mouthful. Then the world will be mine again. And I can forget why I’m here in the first place.”"
    "It became less bearable as time went on. And the salty aftertaste of poor decisions went from tolerable to cancerous each time she’d wake up in a pool of her own spit. "
    "She was still doing that nowadays, but at least the salt was gone. "
    "The shame never left, though. And it was more prevalent now than it had been in a very long time as she promised herself she’d only come here if and {i}when{/i} she ran out of options."
    "Because she always knew it was only a matter of time. And she knew that, one way or another, her past would catch up to her and force her back underwater."
    "And while the specifics this time were somewhat different than they’d been in the past, the end result remained the same."
    "She needed money. And she had {i}access{/i} to money. "
    "But it would come at a cost."

    yu "..."

    scene black
    with dissolve
    scene yukineedsmoney2
    with dissolve2

    yo "It’s been a while since you last showed up here, Yuki."
    yo "At least since deciding to show yourself in front of {i}me.{/i}"
    yu "..."
    yo "I remember hearing something about you coming to visit the girl, though. When it was her turn to come crying back."
    yu "She has a name..."
    yo "Of course she does. You gave her one. Which makes it all the more surprising why you just quit after that."
    yo "Normally, people get at least a {i}little{/i} attached to something after naming it."
    yu "I’m not here to talk about Yumi..."
    yo "Oh? Why {i}are{/i} you here then?"

    scene black
    with dissolve
    scene yukineedsmoney1
    with dissolve2

    yu "..."
    yo "You need money, don’t you?"
    yu "I had a job, but..."
    yo "But you fucked it up, didn’t you?"
    yu "..."
    yo "You do that a lot, huh?"
    yu "..."
    yu "Yeah...I do that a lot."
    yo "How much?"
    yu "As much as you’ll allow me..."
    yo "For drugs?"
    yu "..."
    yo "You look like shit. What is it this time? Heroin again?"
    yu "It doesn’t matter..."
    yo "It {i}does{/i} matter when you come here asking for {i}my{/i} money. So if I ask you a question, you will answer it. Then {i}I{/i} can make an informed decision. Understood?"
    yu "Yes, Yoshitsugu..."
    yo "Did I give you permission to address me so casually? It’s {i}Danna-sama.{/i} We used to {i}kill{/i} women for disrespecting their husband, you know."
    yu "Yes...Danna-sama."

    scene black
    with dissolve
    scene yukineedsmoney2
    with dissolve2

    yo "Good girl. {i}Obedient.{/i} You must be desperate."
    yu "...Yes. Danna-sama."
    yo "Heh...you must be {i}very{/i} desperate. You won’t even {i}look{/i} at me."
    yo "Where’s that {i}fire,{/i} Yuki? You used to be a terror. Half of these men have never even met you and they’re {i}still{/i} afraid because of the stories."
    yo "You’re going to make me look like a liar if you keep this up."

    play sound "static.mp3"
    scene yukineedsmoney3 with flash
    stop sound

    yu "I apologize...Danna-sama. I’m very tired these days. I don’t have it in me to fight anymore."
    yo "You know, that’s kind of funny. Because I recall hearing something just a short while ago about you breaking one of my captain’s bones just for {i}talking{/i} to a girl. Is this true, Yuki?"

    scene yukineedsmoney4
    with dissolve2

    yu "Mnh..."
    yo "Is it true? Or is {i}he{/i} the liar here?"

    scene yukineedsmoney5
    with dissolve2

    yu "With all due respect, Danna-sama..."
    yu "If that man was a captain, I can only imagine how weak the rest of your men are."
    yo "Ha! {i}There’s{/i} the Yuki I know. {i}There’s{/i} the {i}Dragon.{/i}"
    yo "Rest assured — I still took his pinkie. You {i}are{/i} still my wife, after all."
    yo "And even if {i}you’re{/i} still out there fucking everything up the way you always do, I can’t have you making {i}me{/i} look bad. Just maybe mind your own fucking business from now on."
    yo "After all, what’s the point in running away if you’re just going to keep getting involved?"

    scene yukineedsmoney6
    with dissolve2

    yu "I apologize for causing you trouble...I am only here to beg for your assistance as I am afraid that I will die without it."
    yo "Right...And what happens when you run out {i}again?{/i} When can I expect you back? Would you like to schedule your next meeting {i}now?{/i}"
    yu "This is the last time...I swear."
    yo "Mm...I wonder how many “last times” it’s been now."
    yu "Please...Danna-sama."
    yo "Why not just move back in? I have plenty of new recruits to make up for the ones who were shipped off. They could use someone to train them."
    yo "And you know how {i}well{/i} you’re taken care of here. That’s what made me so {i}appealing{/i} in the first place, isn’t it?"
    yu "I...can’t do that. I apologize, Danna-sama."
    yo "Hmm...unfortunate. Don’t even want to give it a shot? I’ll even let you choose who to kick the shit out of first."
    yo "It was always fun watching you {i}lose{/i} yourself. I’d hate for that to just be a memory."
    yu "I will do anything you ask...but I can not stay here. I do not wish to burden you any more than I already have."
    yo "Just the money then?"
    yu "Please, Danna-sama...anything you can spare. I have no one else to turn to..."
    yo "Yeah, probably because you’ve fucked every other relationship you’ve ever had up. But alright. Fine. Let’s see it. On your knees."
    yu "Yes...Danna-sama."

    scene black
    with dissolve
    scene yukineedsmoney7
    with dissolve3

    "Chatter erupts throughout the room as the dragon is brought to its knees. And as she prostrates herself before the man who downed her, a fit of violent laughter erupts from out of his throat."
    "The rest gaze on in a mix of shock and awe. Those who know her can not believe their eyes, while those who {i}don’t{/i} glance skeptically at one another, unsure of what to make of this."
    "Was {i}this{/i} really the woman they were taught to fear? This frail, decaying sack of flesh with so little pride left that she would dogeza without quarrel in front of each and every one of them?"
    "She holds herself there with her head against the floor, breathing in the scent of the tatami and wishing {i}desperately{/i} that this is where it ends."

    scene yukineedsmoney8
    with dissolve2

    "But of course that would be too easy. And of course she’d have to swallow the {i}rest{/i} of her pride along with the true cost of what she needed from this man."

    yo "Oh, Yuki. You know that’s not what I meant."
    yu "Please, Danna-sama..."
    yu "I can’t."
    yo "What do you mean you {i}can’t?{/i} You’re my wife. It’s your duty to please me. And in this state, it’s the only use you {i}have{/i} now."
    yu "I beg you...anything else."
    yo "Yuki...I think you’re misunderstanding something."

    scene yukineedsmoney9
    with dissolve2

    yu "Ngh?!"
    yo "I am not {i}asking{/i} you. I am {i}commanding{/i} you."
    yo "When I say “bark,” you bark. When I say “jump,” you jump. And when I say to get down on your fucking knees and open your fucking mouth, what do you do?"
    yu "Please...don’t..."
    yo "What...do...you...{i}fucking...{/i}do?"

    scene black
    with dissolve4

    "Exactly as he says..."

    scene yukineedsmoney10
    with dissolve4

    "Because that’s what {i}needs{/i} to be done if she wants to survive."
    "And just like in the old days, a mouthful of salt would soon be worth the payoff."
    "She’d just first need to get her hands on something to help her forget as she was coasting on fumes right now."
    "So she felt every vein — every pubic hair that crept into her mouth despite desperate attempts to dodge them while he proceeded to degrade her in front of a crowd of his underlings."
    "And for {i}him,{/i} this was perfect. The {i}power{/i} he felt slaying a dragon bled out like fanfare and echoed throughout the room, rallying his troops behind him as they shouted their praise."
    "For her, it was much worse."

    yu "Mlgh...mlgkhhhk!.......Mrglrlh.......glmpckhkc?!...."
    yo "Ah, yes...just like I remember..."
    yo "Crowd and all..."
    yu "Mmmlggh....mmngh....grllrplppl!"
    yo "You like that, don’t you?...You’ve always fucking liked it, Yuki..."
    yo "You talk...big, and...you...ngh...{i}act{/i} tough...but deep down...you love it when you’re...fucking used like this..."
    yu "Mlmgll!! MMmghh! Mlmrlrlpp!"

    scene black
    with dissolve2
    scene yukineedsmoney11
    with dissolve2

    yo "Yeah...that’s right...just a little longer..."
    yo "Juuuust like you used to do it...then you can shoot up as much as you want..."
    yu "Mllgh....mlgghgh!!!"
    yo "Yeah, I {i}bet{/i} you’re excited...You’d do {i}anything{/i} for money, wouldn’t you? And you’d like it too, you little slut..."
    yu "Mmmngh....mlmgpgp....mmlglpppp!!!"

    "She wanted to puke. She hated his taste. His smell. The sound of his voice. How he’d force her down without regard for whether or not she could breathe."
    "But she had to endure. Just a little while longer."
    "Just a little while longer."
    "Just a little while-"

    yo "Mngh...fuck...get ready to swallow, Yuki...Get ready to...fucking swallow, you...junkie bitch!"
    yu "Mmmlgh! Mmllghlg! Mmmnhgh! Mmllgchklprllpr!!"

    scene yukineedsmoney12
    with dissolve3

    "As he filled her mouth with liquid disdain, she remembered a mantra she used to think to herself during times like this."
    "It went something like — “Don’t bite down. Don’t bite down. Don’t bite down.”"

    scene black
    with dissolve2

    "And it was that exact mantra that carried her through to the end of his violent, hateful ejaculation."

    scene yukineedsmoney13
    with dissolve3

    "He shoves her backward by her shoulders once he’s finished, but she manages to stay upright, quickly wiping away the mix of juices left clinging to her mouth."

    yo "Ahh...what a nice trip down memory lane that was. Thanks for coming all the way here just to catch up, Yuki. Same time next week?"
    yu "Phfht....pfhht...blech...we done here?..."
    yo "Are we done here {i}what?{/i}"

    scene yukineedsmoney14
    with dissolve

    yu "Are we done here...{i}Danna-sama?{/i}"
    yo "Are we? You still haven’t told me how much you need."
    yu "I already said...whatever you can spare."
    yo "See, that’s just the thing. I have {i}plenty{/i} to spare. And for as little as ¥20,000, I could have a girl half your age and five times as attractive shipped right to my door."
    yo "That said, how about ¥10,000? That should get you high a few times, right?"
    yu "{i}You know I need more than that...{/i}"
    yo "Oh? What happened to “anything you can spare?”"
    yu "Yoshitsugu..."
    yo "{i}Danna-sama.{/i}"
    yu "Forgive me, {i}Danna-sama...{/i}but I must ask you kindly...to consider a larger amount..."
    yu "This is for more than just {i}getting high...{/i}"
    yo "Hey now, ¥10,000 could go a long way if you just quit doing drugs again. You’ve done that...what, fifty times before, haven’t you? Should be good at it by now."
    yu "What else do you want?..."
    yo "Come back to the family. Train my men."
    yu "{i}Bite me.{/i}"
    yo "Fine, fine. Since that’s {i}so{/i} out of the question, how about this then? Stand up. Strip."

    scene yukineedsmoney15
    with dissolve

    yu "So what? You just want to {i}degrade{/i} me now? Because we both know you ain’t gettin’ hard again for at least an hour, you limp-dicked piece of shit."
    yo "You {i}fucking-{/i}"
    yu "Sorry. You limp-dicked piece of shit, Danna-sama."

    "Chatter again. Louder this time as the dragon attempts to roar."

    play sound "static.mp3"
    scene yukineedsmoney16 with flash
    stop sound

    "But it’s brought down once more when she comes to her senses."
    "This would all be for nothing if she leaves empty-handed. And if she had to stand around and wait for an hour just to get what she came here for, so be it."
    "She’d do whatever she had to."
    "But the way these men encircled her made her fear as if that would be more than she ever expected."

    yu "The fuck are you lookin’ at? Back off."
    yo "I imagine he’s looking at you, Yuki. Which I’d probably be flattered by at your age."
    yo "Tell me — have you found someone else yet? Or are you still running around pretending wolves can survive without a pack?"

    scene yukineedsmoney17
    with dissolve

    yu "The fuck do {i}you{/i} think, {i}Danna-sama?{/i} Think I’d really come here if I had someone else I could suck off for money?"
    yo "There are plenty of people you can suck off for money. You’re probably just not looking hard enough."
    yu "Yeah, guess not. Can we do this now? I ain’t got all fuckin’ day. I’ll just shove my fist up your ass or something. That’ll probably get you hard, right?"
    yo "I knew your pleasant attitude was too good to be true. You’ll never change. That’s why you’re still fucking up and still desperate for me to come rescue you to this day."
    yo "I can’t do that forever, Yuki. Not for you. For my daughter maybe, but some whore I picked up off the street? Yeah, I don’t think so."
    yu "You married me, dipshit. I ain’t a fuckin' street whore."
    yo "Right, yeah. You’re {i}my{/i} street whore."
    yo "And seeing as you’re {i}my{/i} street whore, I am free to do as I please with you. Is that correct?"
    yu "Sure. {i}Fine.{/i} You don’t give a shit about my blessing anyway if you’re just gonna tell me these are all {i}commands.{/i}"
    yu "I sucked your filthy dick. I stripped in front of your fucking evil henchmen. Now, I {i}assume{/i} you’re gonna fuck me. What’s after that, {i}Danna-sama?{/i} Want to {i}hold hands?{/i}"
    yo "How much would {i}that{/i} cost? Sounds quite uncharacteristic for a street whore."
    yu "First ten minutes’ll run ya ¥100,000. Every ten after that, price gets shaved down to ¥50,000."
    yu "You in? Might be the first time you’ve ever been touched without havin’ to force it."
    yo "Aww, you’re saying you’d do it willingly? Maybe you {i}have{/i} changed."
    yu "Are you gonna fuck me or not? I’m gettin’ bored."
    yo "Hmm...sorry. No can do, Yuki. Like you said, I’m still not hard yet."
    yo "There are plenty of other men here I’m sure you could satisfy, though. And hey? Maybe watching {i}them{/i} degrade you might turn me on? I’ve always liked that."

    scene yukineedsmoney18
    with dissolve2

    yu "You fucking wouldn’t..."
    yo "I wasn’t {i}going{/i} to if you stayed obedient. But {i}now{/i} you’ve made me mad. And I honestly just don’t really give a shit about you at this point, so yeah. Have at her, boys."

    scene yukineedsmoney19
    with dissolve2

    yu "No- don’t you fucking touch me! You have any idea who you’re laying your hands on?!"
    yo "Oh, give it a break. How about ¥50,000 for each one you get off? Saves me a trip to the soapland next week."

    scene yukineedsmoney20
    with dissolve2

    yu "I’m your fucking {i}wife!{/i} What’s this say about you, you fucking cuck?! You think these guys will still respect you after they watch you jerking off to this?!"
    yo "{i}I{/i} think it says that I’m very grateful for their loyalty and that I don’t mind sharing. Which you too will soon reap the benefits of at ¥50,000 a head. Have fun, Yuki!"

    scene yukineedsmoney21
    with dissolve2

    yu "No! Fuck that! And who the fuck are {i}you?!{/i} Do you have any idea how {i}fucked{/i} you are once I’m-"

    scene yukineedsmoney22
    with dissolve2

    yu "{i}MMNGNGHH?!?!!?!{/i}"
    nr1 "This really the same person you’ve been talkin’ about, Boss? Thought you said she was stronger than all of us put together."
    y1 "She used to be...probably getting older now. Or just high. I’m staying out either way. I don’t want to be on her bad side next time she comes back."

    scene yukineedsmoney23
    with dissolve2

    yu "{i}LMMMGO!!!! ILLFCKNGKLLYYOU!!!! YFCKINGMNGHHGH!{/i}"
    nr1 "Oh, okay. I can feel it now. Yeah, I can see how she was strong once."
    yu "{i}MMNNGHGHGHHHH!{/i}"
    nr2 "Can we really, like...you know...do her, Boss?"

    scene yukineedsmoney24
    with dissolve

    yu "{i}MMMNMNNHHHHH!!!{/i}"
    yo "{i}Hmm...{/i}"
    yo "You know...she {i}is{/i} the mother of my child. And I {i}do{/i} still have hope for Yumi...so I {i}would{/i} like to stay on her good side."
    yu "{i}MMM! MMMMMHHH!!{/i}"
    yo "But at the same time, she really needs the money and I wouldn’t want to hold her back from such a great opportunity."
    yu "{i}MMMMMMMM!!!!!!{/i}"
    yo "So again! Have fun, Yuki!"

    play sound "static.mp3"
    scene yukineedsmoney25 with flash
    stop sound
    play sound "dosex.mp3"

    nr1 "God damn...she ain’t even a {i}little{/i} wet. Feels like I’m fucking a tube-sock."
    yu "{i}MNLGLGHGLLGL! MMNGHGHGHH!!{/i}"
    nr2 "Don’t worry, dude. I’ll fix that. My ex told me I have “magic fingers.” The trick is to stimulate her clit with brief and delicate motions and you can start by making little circles around-"
    nr1 "You fucker! You totally just touched my dick!"
    yu "{i}MMMNGHH! MMMNGHHGHHG! MMNFHHGHGHGH?!?!?!!{/i}"
    nr2 "Oh, sorry. My bad."
    nr1 "You good over on the front end, man? You sure you want to, like...be in her mouth? You ain’t afraid she’s gonna bite you or something?"
    y2 "Hah...hah...it’ll be...worth it if she does! I’ve been...wanting to do this...for {i}years{/i} now!"
    nr2 "Oh yeah, you grew up around here didn’t you? Wasn’t your dad a captain? He get sent off to space with the rest of the other old guys?"
    y2 "Hah...yeah! He...sure did! I’ve been...hanging out here since...I was a kid!"
    nr1 "Oh damn, you must’ve seen her in her prime then. Was she hot?"
    y2 "She...still is! God...I’m gonna fucking cum! Oh fuck, it’s a dream come true!"

    scene yukineedsmoney26
    with dissolve2

    yu "{i}MNNGHGHGHGHGHHG!! MMMPPLSLSSSSLSSS!!!!!{/i}"
    y2 "Oh, no...oh, fuck! She looks so sad! Oh fuck! Aaah! I can’t help it! I’m sorry, Yuki! I’m...so sorry!"

    "Just a little while longer."

    play sound "static.mp3"
    scene yukineedsmoney27 with flash
    stop sound

    "Just a {i}little{/i} while longer..."

    nr10 "Jesus...fuck! I can’t tell if she’s...wet or...if that’s just...cum from the last guy..."
    y8 "Yeah...sorry...probably me! Been...ngh...holding it in for...weeks now! Couldn’t...help myself!"
    yu "{i}Mnh......................mnhhh.....................{/i}"

    "She’d stopped fighting back."
    "Her hand moved mechanically as it wrapped around the curved cock of yet another man she couldn’t see the face of."
    "But on the bright side, she couldn’t taste much of anything anymore now that her sinuses had swollen shut from hours of crying."
    "The man who ran the estate still loomed in the back of the room — his eyes fixated on the broadcast of a soccer game while his men proceeded to violate his wife."
    "The volume was loud enough for Yuki to keep track of the score, so she kept herself distracted by doing that for a while until the lack of air made it nearly impossible to focus."
    "Just a little while longer."
    "Just a little while longer."
    "Just think of the money."
    "Just think of the high."

    play sound "static.mp3"
    scene yukineedsmoney28 with flash
    stop sound
    play music "heartbeat.mp3"

    "Just think of {i}something.{/i}"

    yu "..............."

    "{i}Anything.{/i}"

    yu "................"

    "This isn’t where you’re meant to die."

    nr15 "Uhh...boss?"
    yo "Hm? What?"
    yo "Oh — Yuki. Right. She still breathing?"
    nr15 "Shaking a lot, but yeah. She’s still breathing."
    yo "Good. Because I’d be taking {i}all{/i} of your pinkies if you fuckers killed my wife. Yuki! Time to wake up!"
    yu "................"
    nr15 "I’m, uhh...not sure she can walk right now, Boss. Or...speak. A few of the guys really did a number on her."
    nr1 "{i}You’re{/i} the one who wanted to fuck her ass. She was totally fine before that."
    nr15 "I’d never gotten to try before. I wanted to see what it was like."
    yo "If she can’t walk, just fucking...toss her out onto the street or something. I don’t know."
    nr2 "What about her clothes?"

    stop music fadeout 10.0

    nr15 "Yeah, and doesn’t she need to get paid still? I think there were twenty of us so that’s...what? A million, right?"
    yo "Yuki! How many dicks did you take tonight? Got a number?"
    yu ".................."
    yo "None? Sounds good to me. Throw her outside. She smells like shit now and we literally {i}just{/i} got the tatami cleaned."
    nr15 "But Boss-"

    scene black
    with dissolve2

    yo "I told you to fucking throw her out! When I say “bark,” you bark. When I say, “jump-“"
    nr1 "Yeah, yeah. We all jump. Come on, I’ll help you carry her. I just want to find, like...gloves first."

    "........."
    "......"
    play sound "tackle.mp3"
    "..."

    play music "rainloop.wav" fadein 3.0
    scene yukineedsmoney29
    with dissolve3
    $ renpy.pause(5, hard=True)

    "Somewhere in the midst of everything, it started to rain."
    "How long had it been since then?"
    "..."
    "Yuki Yamaguchi was tossed outside of the estate grounds, left there like a bag of trash to be collected the next time the truck came around."
    "It was cold, but it was a welcome cold. Worsened only by the fact that the water pouring down from the sky did little to wash away the sins of man."
    "It was like this when she’d shower too, though."
    "Because from Yuki’s point of view, she was permanently unclean. And it’s not as if any of this mattered now that her life was coming to an end."
    "She wasn’t even {i}thinking{/i} about the money anymore."
    "She was just glad to be alive — if even for a minute longer."

    stop music fadeout 2.0

    "But then there was a sound."

    play sound "footsteps.mp3"

    "Footsteps, coming closer."
    "Footsteps that {i}weren’t{/i} dying out."

    scene yukineedsmoney30
    with dissolve2

    yu "{i}Ah...{/i}"

    "A last burst of energy grants her the strength to lift her head and witness the truck pull up to carry her away."

    scene yukineedsmoney31
    with dissolve2

    yu "{i}Aaah...{/i}"

    "But when she lifts her head, what she sees is not a truck. Nor the headlights that signal the end of her days."

    q "Well, well, well..."

    scene black
    with dissolve2
    $ renpy.pause(2, hard=True)
    play music "yorunoakachan.mp3"
    scene yukineedsmoney32
    with dissolve4

    "And yet..."
    "She will {i}still{/i} be collected."

    yu "........"
    tb "If it isn’t the Dragon herself."
    yu "........"
    tb "Tough day, I take it?"
    yu ".........."
    yu "Nee...sama?..."
    tb "Long time, no see..."

    scene black
    with dissolve4
    stop music fadeout 12.0

    tb "Yuki."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ yukispring5 = True

    scene bedroom_night
    with dissolve4

    "I haven’t seen Niki or Ami since we made it back from the beach..."
    "But everyone else will still accept me..."
    "Won’t they?"

    s "..."

    "I should...figure out what to do next."

    jump ch4nightmenu
