label convenience:
    if noriko_love >= 0 and norikofirsthall == True and convenience1 == False:
        jump convenience1
    if noriko_love >= 5 and norikodorm5 == True and mollydorm15 == True and convenience1 == True and convenience5 == False:
        jump convenience5
    if noriko_love >= 25 and norikodorm20 == True and convenience25 == False:
        jump convenience25
    if kirin_love >= 40 and mikuinvite2 == True and norikodate30 == True and kirinspecial40 == False:
        jump kirinspecial40
    if noriko_love >= 30 and yasuspring3 == True and norikospring1 == False:
        jump norikospring1
    if chap4active == True:
        jump norikospringconveniencegen
    if chapthreeactive == True:
        jump norikosummer2conveniencegen
    else:
        jump conveniencegen

label norikoinvite:
    if norikoinvite1 == False and day != 6 and day != 7:
        jump norikoinvite1
    if noriko_love >= 40 and norikodorm30 == True and kirinspecial45p2 == True and norikoinvite3 == False:
        jump norikoinvite3
    else:
        "I should probably wait a little while before inviting Noriko over."
        jump inviteover

label callnorikomorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if norikoblock == True:
        play sound "phonebeep.wav"

        "I tap on Noriko's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer..."
        jump callmorning
    if chap4active == True:
        jump norikospringmorninggen
    if chapthreeactive == True:
        jump norikosummer2morninggen
    else:
        jump norikomorninggen

label norikomorninggen:
    play sound "phonebeep.wav"

    "I tap on Noriko's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    n "Good morning, Sensei!"
    s "Hey. Good morning."
    s "Are you doing anything right now?"
    n "Just laying in bed. Thinking about you~"
    s "How about instead of just thinking, we go out to breakfast?"
    n "Ah! Breakfast date!"
    n "I'd love to. Just let me get dressed."
    n "Where did you want to go?"
    s "I'll send you the address in a second."
    n "Okay! I'll see you soon, then!"

    play sound "phonebeep.wav"

    "I hang up the phone, send Noriko a quick message, and then start heading over to the diner."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene norikogenmorning
    with dissolve
    play music "noriko.mp3"

    "Despite living further away from the place than I do, Noriko somehow manages to make it there first."
    "I question how this is possible and she proceeds to talk about the wonders of modern transportation and how ridesharing is the way of the future."
    "I grow tired of the lecture and remind her that we are here to eat and, as if on cue, she pulls out a box of doughnuts from seemingly nowhere, opening it up and offering me one."
    "Apparently, she did not only get here early, but purchased food before I even had the chance to pay for anything."
    "I'm not complaining since this saves me money, but I do feel a little bad that she's going out of her way like this."

    scene black
    with dissolve

    "I eat a few doughnuts and drink some coffee while listening to Noriko reminisce about the old days."
    "The days that were monumental in her life but have already been torn down in that of my own."
    "It's kind of unfortunate how, even with the way time flows here, there's no way to really go {i}backwards.{/i}"
    "I honestly do wish I could have experienced all of the stories Noriko tells me."
    "And I guess it's not impossible that I {i}did.{/i}"
    "But, if that's true-"
    "I'd really appreciate it if those memories would return."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko's affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label norikoafternoongen:
    play sound "phonebeep.wav"

    "I tap on Noriko's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    n "Hiya! What's going on, Sensei?"
    s "Hey. Are you free right now by any chance?"
    n "I'm always free for you! Do you want to meet up?"
    n "The sun's actually starting to come out so I kind of wanted to go for a walk or something."
    s "Yeah, that works for me."
    s "Is there anywhere in particular you wanted to meet at?"
    n "Uhhhh sure! Give me a few minutes and I'll send you an address."
    s "Sounds good. See you soon."
    n "Yup! Bye, Sensei!"

    play sound "phonebeep.wav"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene norikogenafternoon
    with dissolve
    play music "noriko.mp3"

    "Just like Noriko said it would, the sun rains down upon Kumon-mi and actually makes it pretty warm out for the first time in a while."
    "In fact, the only other place where I've felt this warm since summer has been at the shrine, so this is a pretty pleasant surprise."
    "We walk around for a bit, hitting up several convenience stores in search of {i}vegetarian sushi{/i}, which is apparently a thing that exists for some reason."
    "I question Noriko about how she's able to live like that, and she informs me that it's not as hard as I'd expect it to be."
    "I expect it to be the hardest thing in the world, though, so that doesn't really say much."
    "Regardless, I respect how she's trying to make a difference. Even if I don't exactly think the difference will be large enough for anyone or anything other than her organs to feel."

    scene black
    with dissolve

    "The sun eventually leaves us."
    "Winter returns."
    "Not having anything else to do and wanting to escape the encroaching cold, we head our separate ways and make plans to meet up again soon."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko's affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label callnorikoafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if norikoblock == True:
        play sound "phonebeep.wav"

        "I tap on Noriko's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer..."
        jump callafternoon
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Noriko's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."

        jump callafternoon
    if chapthreeactive == True:
        jump norikosummer2noongen
    else:
        jump norikoafternoongen

label callnorikonight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if norikoblock == True:
        play sound "phonebeep.wav"

        "I tap on Noriko's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer..."
        jump callnight
    if noriko_love >= 30 and nikilovesyou3 == True and norikodate30 == False:
        jump norikodate30
    else:
        jump norikogennight

label norikogennight:
    if convenience1 == True:
        "Noriko should be at work right now."
        "I can probably see her if I head over to the convenience store."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Noriko's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        "I guess I should call someone else."
        jump callnight

label norikoinvitegen:
    "YOU SHOULD NOT BE HERE."
    "PLEASE REPORT."
    "REROUTING."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label conveniencegen:
    scene conveniencegen
    with fade
    play music "noriko.mp3" fadein 3.0

    "I decide to head over to the convenience store to spend some time with Noriko."
    "The strange thing is that I don't particularly remember when I decided this or how I even got here."
    "But I'm here nonetheless, so I might as well have a good time talking about some of the weird stuff Noriko is into."
    "Or at least that's what I expect to do, but the conversation winds up being surprisingly natural and {i}mostly{/i} normal."
    "We walk around the store reading the ingredients on the back of bottles and Noriko explains to me what each and every one of the ingredients does to the human body."
    "Now, I'm sure you're probably thinking that this isn't normal at all."
    "But for Noriko, I think it's actually pretty good."
    "A step in the right direction, if you will."

    scene black
    with dissolve

    "But I guess when every step is so misplaced, even crooked paths are better than nothing."
    "I wind up staying at the store much later than I ever intended to."
    "I think it's around midnight by the time I finally leave."
    "Instead of leaving alone, though, I head back with Noriko."
    "She winds up calling over a ride for us and, before I know it, we're in the backseat of an unfamiliar car sitting shoulder to shoulder."
    "She stares at me the entire time."
    "I stare back at her every minute or so."
    "And then I arrive home."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko's affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label convenience1:
    scene black
    with dissolve
    stop music fadeout 5.0
    "........."
    "......"
    "..."
    scene nightsky
    with dissolve2
    play music "blueair.mp3"

    "A sudden desire to go somewhere far away washes over me."
    "I’m not sure what brings it on, but I guess that really ties into the word “sudden,” now doesn’t it?"
    "sud-den (sədn) {i}adjective{/i} - occurring or done quickly and unexpectedly or without warning."

    play sound "static.mp3"
    scene happy5 with flash
    scene tree3 with flash
    scene happy4 with flash
    scene happy3 with flash
    scene nightsky with flash
    stop sound

    "Sudden."
    "Definitions can be fun if you’re willing to swim through all of the words you don’t like."
    "What are some words you don’t like?"
    "Tell me."
    "I’m excited to hear them."

    play sound "static.mp3"
    scene tree3 with flash
    scene firstconvenience1 with flash
    play music "noriko.mp3"
    stop sound

    "Sudden."

    s "..."

    "I wind up at an unfamiliar convenience store in the blink of an eye."
    "I have...absolutely no idea how I got here or where in town this even is, but...I guess I’m going to buy a drink or something."
    "A [young_girl] sits at the counter and-"
    "Wait. Isn’t that Noriko?"
    "I’ve definitely heard her mention having a job before, and I guess something like a convenience store is suited to girls her age."
    "But it’s just all so sudden."
    "..."
    "I wonder if maybe I can take advantage of how much she likes me to get a discount on stuff?"

    scene firstconvenience2
    with dissolve

    s "Hey. How’s it going?"
    n "Can I help you?"
    s "What, you don’t recognize my voice?"

    scene firstconvenience3
    with dissolve

    n "If you’re here to start trouble, I-"

    scene firstconvenience4
    with dissolve

    n "Ah! Sensei! What are you doing here?!"
    n "Did Nee-chan tell you where I worked?"
    s "Nope. Just coincidentally happened to stumble in here."
    n "Ahh! That’s so great!"
    n "I’m glad we got our reunion out of the way in the classroom first, because breaking down behind the counter and confessing in front of the onigiri wouldn’t have been a good look for me."
    s "Sure, I’ll take the hit to all of my current relationships so the rice balls don’t think you’re weird."

    scene firstconvenience5
    with dissolve

    n "Heheh~ Thanks!"
    n "You sure you weren’t over here looking for me, though?"
    n "The old district seems like it’s kind of far from[school] to just show up in all coincidentally and whatnot."
    s "We’re all the way in the old district?"

    scene firstconvenience6
    with dissolve

    n "Wait, is this another memory thingy? "
    n "Are you sure it’s not Alzheimer’s? "
    s "Pretty positive."
    s "Are you really commuting from the dorms to the old district every day for work?"

    scene firstconvenience7
    with dissolve

    n "Yup! But I normally just take an Uber so it’s not like it’s crazy far."
    s "I’m surprised you can afford that."
    n "I still make money running errands for my sister every weekend, so I’m not totally broke. "
    n "Our parents are pretty well off now, too. Their business really took off a couple years ago."
    s "Is their business a thing I knew about?"
    n "They were just starting it up around the time you disappeared, so you probably knew a little bit about it at least."
    n "It’s just some Chinese restaurant thingy near my old[school]. If you’d like, I can take you there sometime?"
    n "I’m sure they’d be happy to see you."
    s "Maybe after I remember a little more about them."

    "Assuming that ever happens."
    "Which it likely won’t."
    "But, then again, I just happened to find this place out of nowhere tonight, so I wouldn’t say it’s entirely out of the question to find somewhere else just like it."

    scene firstconvenience8
    with dissolve

    n "Hmm..."
    s "What? What is that look?"
    n "I was just thinking that maybe your conscience led you here in search of me."
    n "What if your memories are trying to speak to you, Sensei?"
    n "Can you hear them shouting “Noriko! Noriko!” or something like that?"
    s "All I hear is a really loud song on the radio."

    scene firstconvenience9
    with dissolve

    n "The radio’s not even on, though. Are you sure you’re feeling okay?"
    n "Do you want a rice ball?"
    s "One of the sentient ones that judge you based on how you react to reuniting with a long lost love interest? No thanks."
    s "I prefer my food to not have a mind of its own."
    n "So, what? You don’t eat yogurt either then?"
    s "What?"

    if bonus == True:
        n "Yogurt. The thick sour white stuff full of living organisms that {i}doesn’t{/i} come out of a penis."
    else:
        n "Yogurt. The thick sour white stuff full of living organisms that people eat when they want to feel healthier."

    s "Yogurt is alive?"
    n "Yeah. And not only is it alive, it can {i}feel{/i}."
    s "You’re shitting me."

    scene firstconvenience10
    with dissolve

    n "I am not!"
    n "We watched a video in one of my old science classes where a bunch of researchers hooked a thing of yogurt up to a machine and then yelled at it and it got {i}scared{/i}."
    n "Or at least reacted in a way that emulated some level of fear. I guess it’s not technically possible to prove whether or not it actually {i}did{/i} display the more human type of fear."
    s "I’d like to meet whoever decided to hook yogurt up to a machine and yell at it. They sound very interesting."
    n "Hey, are we gonna do any cool experiments like that in your class, Sensei?"
    s "We’re not going to do anything in my class ever."

    scene firstconvenience11
    with dissolve

    n "Wait, ever? Why?"
    s "That’s just not how I teach."
    n "Did something happen? You used to love teaching."
    n "Like, sure there were days where you’d get all upset and mopey and just have us do worksheets, but everyone gets days like that. "
    n "Well, without the worksheets. I think that’s a thing specific to tutors and teachers and stuff."
    s "You can mess around with the science equipment if you want, just don’t burn the classroom down."
    s "Ami did something like that once and I’m pretty sure several of the girls had a near-brush with death as a result."

    scene firstconvenience12
    with dissolve

    n "Hell yeah. That’s what I like to hear."
    n "I’m a little upset that you won’t be doing any {i}actual{/i} teaching anymore, but I guess I’m already way ahead of most other girls my age anyway."
    s "Wait, really?"

    scene firstconvenience5
    with dissolve

    n "What? Are you surprised?"
    s "I’m not sure yet. How ahead are you, exactly?"
    n "I had the second highest standardized test score in my entire grade at my last[school]."
    n "Pretty cruel twist of fate, too, since I wound up transferring into Wakana’s class right beside the girl who beat me."
    s "Yup. Now I’m definitely a little surprised."

    scene firstconvenience7
    with dissolve

    n "Don’t judge books by their covers, Sensei. Especially when the books are in love with you and filled with lots of embarrassing secrets."
    s "And I’m assuming you’re going to weaponize those secrets as soon as it becomes convenient for you to do so?"

    scene firstconvenience13
    with dissolve

    n "What? No. Of course not."
    n "I have nothing to gain by embarrassing you in public. Which is why I also agree to start changing my wardrobe if I attract too much attention and you hate it."
    n "I realize some of my clothes can be a little...uhh...flashy?"
    s "Is that what the kids are calling it nowadays?"

    scene firstconvenience14
    with dissolve

    n "Or, as my sister would say, {i}trashy, tactless, and immeasurably undesirable.{/i}"
    n "{i}The complete opposite of what a girl should look like.{/i}"

    scene firstconvenience5
    with dissolve

    n "Or something."
    n "But, little does she know, this is all part of my patented strategy to show her that you can obtain everything you want in life without signing away your soul to do it."
    n "I will live free and dangerously in complete contrast to the name “Noriko!”"
    s "You do that. Just don’t get yourself into any trouble."

    scene firstconvenience15
    with dissolve

    n "Yes, Sir. I’ll be a good girl. "
    n "I mean, look at me now. I’ve already got a job. Two jobs if you count all of the PA stuff, and my grades are awesome."

    scene firstconvenience16
    with dissolve

    n "And, to top it all off, I get to spend at least seven hours of every day with the man of my dreams."
    n "This is the happiest I’ve been in a long time, Sensei."
    n "I don’t even care that Maya looks like she’s going to slit my throat every time our eyes accidentally meet."
    s "Thankfully, I don’t think Maya carries around a pocket knife like some other girl I know."
    n "Sensei?"
    s "...Yes?"
    n "I’m so happy you’re back."
    n "I know I keep saying it, but I really am. "
    s "The more times you say it, the worse I will feel for remembering literally none of it."
    n "You’ll remember. I know you will."
    n "There’s probably just some sort of...inhibitor that was implanted in your brain by aliens or something like that."
    s "Is that what the space war is all about?"

    scene firstconvenience17
    with dissolve

    n "Mmm...no. I’m pretty sure that was an economic thing."

    "What the hell is happening with the Japanese economy that provoked a war in space?"

    n "At least it would make sense for it to be. It’s not like wars have never been started for money before."
    n "In fact, war itself is a major money maker for a lot of different industries and helps bolster political favor for the powerful people neck deep inside of them."
    s "I agree and understand exactly what we are talking about."
    s "Is the ailing economy the same reason you got a job as well, Noriko?"

    scene firstconvenience5
    with dissolve

    n "Nah, I was just bored since Nee-chan only needs help on the weekends."
    n "I mean, I could have probably gone and worked at my parents’ restaurant, but being independent feels a lot better."
    n "And also, they started looking at me weirdly ever since I told them I was in love with you. Whoops."
    s "Why on earth did you do that? And how did this whole love thing even happen?"
    n "Which one of those do you want me to answer first?"
    s "The latter one. I’m just going to assume you told your parents because of an alien implant. I like that excuse and will be using it frequently."
    n "Ooooh, nice callback."
    n "But...love just happens, you know?"
    n "We were alone together a lot back in the day. And I thought you were super cool."
    n "Saying I’ve “loved” you since I was six is probably a bit of a stretch. I imagine it was something more akin to just pure admiration at first."

    if bonus == True:
        n "But it’s not uncommon for admiration to turn into something more once your thoughts on romance and sex develop."
        n "Now, here I am in [high_school] thinking about what it would be like to grow old and take over my family’s business with you."
        s "..."
    else:
        n "But now, literally all I think about is hugging you."
        s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH"

    n "What now? You want to call me crazy again?"

    if bonus == True:
        n "I can take it. I’ve heard it plenty of times."
        s "Nah. You’re just really cute."
    else:
        s "No. I just saw a spider."

    scene firstconvenience18
    with dissolve

    n "Stop...you’re going to make me blush."

    if bonus == False:
        "Wow. Noriko must really like spiders."

        s "Oh, by the way, are you hiring? Being a teacher is stressful and I may quit soon."
    else:
        s "You are very much already blushing."
        n "The boy I like called me cute. Obviously, I’m going to blush."
        s "Very cute, actually. Even if your dream of us running a restaurant together involves me having to actually work- a thing I have sworn to never do again."

    scene firstconvenience19
    with dissolve

    n "Hey, man! If you’re gonna be my second in command, you’re gonna at least have to clean the bathrooms or something."

    if bonus == True:
        s "Just hire Ami instead of me. I’m sure she’ll gladly do it if I’m involved in any way."
    else:
        s "Ewwwwww gross. Aren't you supposed to be like a sister to me or something? Cut me some slack."

    scene firstconvenience20

    n "Oh! Then it will be like, a {i}double{/i} family business! The Nakayamas and the Arakawas coming together as one! Serving fried rice to all of Kumon-mi!"
    n "The Arakawayamas! The Nakakawas!"
    n "The Nakayarakawayamas!"
    s "Please calm down, Noriko..."

    scene firstconvenience15
    with dissolve

    n "Yes, Sir. I’ll be a good girl. "
    n "Besides, we don’t have to do something like that if it’s not a future you want for yourself."
    n "Anything is possible in Kumon-mi."

    if bonus == True:
        n "Like, if {i}Nee-chan{/i} can become a top idol when all she did up until she was 18 was doodle anime characters, I'm sure the two of us can explore some options."
    else:
        n "Like, if {i}Nee-chan{/i} can become a top idol when all she for the first 4000 years of her life was doodle anime characters, I'm sure the two of us can explore some options."

    n "If...you ever want to do that, I mean."
    n "Obviously, there’s more than one person fighting for your affection right now."
    n "But remember that...even if you forget me now, everything will come flooding back eventually."
    n "And when that happens, know you can count on me to be everything you’ll ever need."

    scene black
    with dissolve2

    "The way I leave the convenience store is a lot less sudden (sədn) than how I arrived."
    "Noriko and I wind up chatting for another hour or two about random things that pop into her head and, just as always, I have a hard time understanding why Maya hates her as much as she does."
    "She’s smart, extremely kind, good at holding a conversation, and even {i}did{/i} give me a discount on a [[non-sentient] rice ball as I left."
    "But I feel like there’s something else to her that I can’t quite put my finger on yet."
    "I feel the same way when looking at sculptures."
    "There’s too much perfection on the outside for everything to possibly be the same once you work your way in."
    "Just the insides of sculptures are pure stone or marble-"
    "And the insides of Noriko are a lot less beautiful."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ convenience1 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label convenience5:
    scene norikobreak1
    with fade
    play music "noriko.mp3"

    "I show up at the convenience store to find it completely empty."
    "I steal everything and go home."
    "Just kidding."

    s "..."

    "I do stand there for a mildly concerning amount of time, though."
    "Leaving the counter in a place like this unattended isn’t exactly a good move, especially considering I could reach over and open the register whenever I want."
    "Granted, there are probably cameras installed and I can’t imagine it would be particularly hard to identify someone who looks like me."
    "So I guess I’ll just keep waiting until Noriko shows up."

    s "..."
    s "..."
    s "..."
    s "Okay, I’m done with this. "

    "I turn around to leave and-"

    n "Psst!"

    scene norikobreak2
    with dissolve

    n "Hi."
    s "Did you really just let me stand at the counter that entire time without saying anything?"
    n "I was just admiring that you’re equally as cute from behind as you are from the front."
    n "Also, I thought you’d be smart enough to maybe look behind you once or twice before giving up and going home."
    s "Always look forward, Noriko. Let this be your lesson for the day."
    n "What if somebody taps on my shoulder or something?"
    s "Just keep on walking."
    n "This sounds like bad advice."
    s "It's a lot more motivational without any follow-ups."

    scene norikobreak3
    with dissolve

    n "So...did you actually come here of your own volition today? Or did you just happen to wander in coincidentally again?"
    s "My appearance is very much intentional. I’m here to hang out with you."
    s "Are you on break or something?"

    scene norikobreak4
    with dissolve

    n "I’m pretty much always on break. "
    n "People don’t like to walk around this neighborhood at night, so we’re dead for most of the hours that I'm here."
    n "You should see the place at like 3:00 AM. Total ghost town. Or...ghost store, I guess."
    s "You don’t actually work that late do you?"
    n "Not all the time, but I have in the past. Normally during summer or winter break, though. Just for extra money and stuff."
    s "I applaud your work ethic. I can barely handle the hours I put in at[school]. "

    scene norikobreak5
    with dissolve

    n "I’m sure it’s really taxing for you to just show up and do nothing every day, huh?"
    s "You have no idea."

    scene norikobreak2
    with dissolve

    n "Well, hey. If you ever need any help around the class or anything, I’d be more than willing to lend a hand."
    n "I’m sure you’ve got loads of clerical stuff piling up by now, right?"
    s "Oh, not really. The class rep normally handles all of that for me."
    n "Is she in love with you too?"
    s "Maybe?"
    n "Well that’s just fucking great."
    s "Or maybe not. I don’t know. Please don’t kill her."

    scene norikobreak6
    with dissolve

    n "I’m not going to kill her. It’s just..."
    n "More and more people keep getting in between us and I kind of want them to at least let me catch up first."
    n "Like, I’m way behind in everything except for stuff that you can’t even remember yet."
    s "On the bright side, I’m giving you plenty of time to catch up with how much I’m starting to visit your workplace."

    scene norikobreak7
    with dissolve

    n "Yeah...But do you think that maybe you’d visit me more if I worked a little closer to the dorms?"

    scene norikobreak8
    with dissolve

    n "Oh! How do you think I would look as a maid?!"

    if bonus == True:
        n "Ami and that really short girl with the surprisingly large chest work there, right?!"
    else:
        n "Ami and Uta work there, right?!"

    n "That seems easy enough. And a lot more exciting than sitting around eating prepackaged vegan sushi all night."
    s "I’m actually not sure how you’d look in a maid uniform."

    scene norikobreak9
    with dissolve

    n "Because I’m not girly enough?"
    s "Yes. And no. "
    s "I’ve just never seen you in anything girlier than your pajamas, so it’s hard for me to envision it."

    scene norikobreak10
    with dissolve

    n "I can be girly! "
    n "Let me come over and try on Ami’s uniform. She’ll let me. "
    s "Are you sure about that?"
    n "If she doesn’t, you can hold her down and I can run into her room and raid her closet."
    s "I thought you didn’t like dressing like that? Because of...your expression or whatever it was."

    scene norikobreak11
    with dissolve

    n "Well it would obviously be different if it was for a job. "
    n "Maids are just personas those girls put on to trick gullible men like you into giving them all of your money."
    s "I can assure you that I am fully aware of how greatly I am taken advantage of inside that place. Gullibility has nothing to do with it."
    s "The last thing I need is one more girl who’s able to peer into my soul that effectively."

    scene norikobreak12
    with dissolve

    n "Are you sure about that, Sensei? "

    if bonus == True:
        n "I’ve told you before that I bring both the childhood friend trope {i}and{/i} the little sister trope to the table."
    else:
        n "Wouldn't it be nifty being so close with a girl who can {i}see inside of your heart?{/i}"
        s "Uhhhhhhhhh..."

    scene norikobreak13
    with dissolve

    if bonus == True:
        n "Unless...Onii-chan just doesn’t want to see his sister in a dress because he’ll realize how quickly she’s growing up..."
        n "I’m not the same girl I used to be, Onii-chan. I have...feelings."
        n "I have...{i}needs{/i}."

        "I look down to find that I am already reaching into my wallet for spare change."
        "Damn all of these girls."

        s "As good as I think you’d be at the maid cafe, I don’t see a need for you to relocate just for me."
        n "..."
        s "..."
        n "... "
        s "Noriko?"
    else:
        n "I swear I'd only take a little bite out of it..."
        s "Uhhhhhhhhhhh???????"

    scene norikobreak14
    stop music

    if bonus == True:
        n "Don’t you want to fulfill my needs, Onii-chan?..."
        s "..."
        n "..."
    else:
        n "Am I not allowed to take a bite out of your heart?"
        s "..."
        n "..."
        s "I mean...as long as it's a small one?..."

    scene norikobreak15
    play music "noriko.mp3"

    n "Pfft!"
    n "I can’t keep a straight face anymore, I’m sorry."
    s "You are...actually a pretty good actor."
    n "Oh, stop. A good actor wouldn’t break out in laughter after delivering a line like that."

    scene norikobreak16
    with dissolve

    n "Also...it’s not really acting."

    if bonus == True:
        n "I obviously think of you when...yeah."
        n "But it is kind of embarrassing saying it out loud."
        s "I feel like you’ve said much worse and gotten much less embarrassed."

        scene norikobreak17
        with dissolve

        n "The mood someone is in when they say something greatly impacts the way in which it’s delivered, Onii-chan."
        n "If I’m turned on while I talk to you about being turned-on, I’ll probably be a lot more reserved than I would be if I was feeling totally normal."
        s "Are you...actually turned on right now?"

        scene norikobreak18
        with dissolve

        n "I think this “Onii-chan” thing might be a kink for me."
        n "The more I think about it...the more I..."
        n "..."
        s "..."
        s "Earth to Noriko."
    else:
        s "???????????????"
        s "Noriko wtf stop"

    scene norikobreak19
    with dissolve

    n "Yes! Noriko! Me! Hi!"
    n "What’s up?"

    if bonus == True:
        s "Just trying to figure out how I should handle the horny version of you."
        n "Why would you word it like that?! That’s just going to make it worse!"
        n "Also, I..."
        s "You what?"
        n "I..."
    else:
        s "Do not eat my heart."

    scene norikobreak20
    with dissolve

    n "Job!"

    if bonus == True:
        s "What kind of job?"
        n "Mouth!"
        s "Please don’t call it a “mouthjob.”"
        n "I mean work job! Future! Plans! Help!"

        scene norikobreak21
        with dissolve

        n "I want you to help me think about stuff that doesn’t cause my innocent heart to crave less than innocent things."
        n "Especially while the rice balls are watching."
        s "Are we really back to that?"
        n "They are like children to me."
        n "Tiny, delicious Nakayarakawayamas."
        n "I will destroy anyone who comes close to them."
        s "That will likely be bad for business."
    else:
        s "Yes. You are at work right now. You should attempt to contain your cannibalistic desires as much as possible."

    scene norikobreak22
    with dissolve

    n "Let’s just...talk more about other stuff I can do. Okay?"
    n "Like, I obviously can’t work at a convenience store forever. And if you choose someone else over me, I’ll need something solid to fall back on."
    n "Preferably something where I’ll still have enough free time to dedicate to making you realize you made the wrong choice."
    s "You’re not going to give up on me even if I wind up with someone else?"
    n "I am in...{i}way{/i} too deep to ever do something like that."
    n "Nee-chan, too, probably. "
    n "I guess our whole family is just naturally weak to you for some reason, Onii-chan."

    if bonus == False:
        s "Everyone is weak to me. I am strong and brave and awesome."

    if bonus == True:
        scene norikobreak23
        with dissolve

        n "Oh no! The horny! It’s back!"
        s "There’s no way your whole family is weak to me. Like, what about your parents?"

        scene norikobreak24
        with dissolve

        n "Thanks. The horny is gone again."
        n "I thought about you and my dad and that just..."
        n "Yeah, that’s just not doing it for me."
        s "I would have much preferred if you had used your mother in that fantasy."
        n "But that could like...actually happen."
        n "She loved you just as much as Nee-chan and I did. I don’t think it’s crazy to believe someone her age looked at [teenage]Sensei and thought “You know what? I’m down.”"
        n "My dad, though..."
        s "Please stop bringing up your dad."

        scene norikobreak25
        with dissolve

        n "Oh my God! What if we actually started dating and you wanted to marry me, so like..."
        n "You went to my father to ask him for permission and he was just like..."

        scene norikobreak26
        with dissolve

        n "You can have my daughter...but only {i}after{/i} I test your abilities as a man..."
        n "And then he’d ask you to take your pants off and-"
        s "Wow, would you look at the time? I think I have to get going."

        scene norikobreak25
        with dissolve

        play sound "entrybell.mp3"

        n "Wait, no! I promise I’ll stop fantasizing about you and my dad!"

        cust "..."

        scene norikobreak27
        with dissolve

        n "Oh, hi! I’ll be with you in just a sec!"

        cust "..."

        play sound "entrybell.mp3"

        n "Okay! See you later!"
        s "She left."
        n "She did."
        s "You should probably be careful about what you yell inside of a convenience store."

        scene norikobreak2
        with dissolve

        n "Eh. It’s late. She knew what she was getting herself into when she walked in."
        n "And now {i}she’s{/i} probably adding her dad to some sort of weird sexual fantasy and is going to blame us for it."
        n "Look what we’ve done, Onii-"
        n "Sensei."
        s "..."
        n "..."

        scene norikobreak16
        with dissolve

        n "I didn’t stop myself in time."
        n "The horny returns."
        s "I’m going to have to remember this for when it comes time to choose your lust name."

        scene norikobreak2
        with dissolve

        n "What’s a lust name? It sounds fun."
        s "It’s just a thing. I wouldn’t worry about it until later."
        n "Do I get to choose one too?"
        s "No. You stay out of this."

        scene norikobreak10
        with dissolve

        n "Mmm!"
        s "You do that pouting thing a lot, don’t you?"
        n "It helps me get what I want! "
        n "Or at least it probably would if I didn’t have these “crazy eyes” people keep talking about!"
        n "The failure rate of my pouting suddenly makes a lot more sense!"
        s "Then...stop?"
        n "It’s muscle memory at this point! I can’t!"

    scene norikobreak19
    with dissolve

    n "Oh! I totally forgot to ask you something!"
    s "What’s up?"

    if brony == True:
        if bonus == True:
            n "Is it true that you’re sexually attracted to those cartoon ponies from that one TV show?"
        else:
            n "Is it true that you're a hardcore brony?!"

        s "Did Kirin tell you this?"
        n "It just slipped out, I think."
        s "How does something like that just slip out?"
        n "I don’t know, but I {i}need{/i} to know."
        s "If you {i}need{/i} to know...then, yes. "
        s "I am a proud brony. Tried and true."
        n "Do you have a favorite? I like the one with the hair that’s all like “whoooosh,” you know?"
        s "Ahh, yes. Rainbow Dash."
        n "Yeah, her! Is she your favorite too?"
        s "My favorite pony is whichever one is on screen at the time."
        s "I didn’t realize you were into them, too, Noriko."

        if bonus == True:
            n "Well...I definitely don’t get the urge to fuck them. But they’re totally cute. "
        else:
            n "Yeah! They're great!"

        n "Oh, and have you seen the human versions? They’re like, just as good."
        s "Oh. You’re one of {i}those{/i}..."
        n "...One of what?"
        s "Don’t worry about it."

    else:
        n "Have you ever played Raid: Shadow Legends before?"
        s "..."
        n "..."

        "{i}Hi guys, it’s me! Selebus!{/i}"
        "{i}I just wanted to take a second to tell you about-{/i}"
        "{i}Sike.{/i}"
        "{i}I had you going for a second though, didn’t I?{/i}"

        play sound "static.mp3"
        scene norikobreak19
        with flash
        stop sound

        n "Remember how I was talking about that one super smart girl who beat me in the standardized tests?"
        n "Is there any chance she could move to our class, too?"
        n "She was talking to me about it and apparently she’s already friends with that girl Futaba who sits by the window."

        "Smart girl...friends with Futaba..."

        s "Is her name Nodoka?"

        scene norikobreak2
        with dissolve

        n "Yeah!"
        n "She said that you two met before, but she wasn’t sure if you’d remember her or not."

        if bonus == True:
            s "I have a hard time forgetting girls who talk about seeing other girls naked. I remember her."
            n "I see Kirin naked all the time now. She’s hot."
            s "See? Like, I’m going to remember that for the rest of forever. "
        else:
            s "I remember everyone. I am 75%% magic."

        n "Boy brains are funny."
        s "They’re not funny. They’re just simple. "
        s "Leave us alone."
        n "Never~"

    s "Anyway, I should probably start heading back. "
    s "I really only came over here to see how you were doing."

    scene norikobreak22
    with dissolve

    n "You didn’t need to do that...I know it’s a crazy far walk."
    n "I’m sure Kirin wouldn’t mind if you came over to the dorm to hang out really late, so just do that instead from now on and save yourself some steps."
    s "I don’t know if I like the idea of staying up that late just to come hang out in the dorm."

    scene norikobreak5
    with dissolve

    n "Okaaaaay~ But you’ll be missing a chance to cuddle with pajama Noriko. "
    n "Or pajama Kirin, I guess. But I’m less enthusiastic about you coming over at night to choose her over me."
    s "How about I just...keep doing what I normally do and hope it doesn’t become too annoying?"
    n "That’s fine, too, I guess."

    if bonus == True:
        n "I’ll just go to sleep all alone, without my Onii-chan there to-"

        scene norikobreak15
        with dissolve

        n "{i}Ahh~{/i}"
        n "Why aren’t you stopping me from calling you that?"
        s "Why would I ever stop something as awesome as this? Do it again."
        n "Onii..."
        n "Mm~"

    scene black
    with dissolve2

    if bonus == True:
        "I stay just long enough to watch Noriko squirm in her seat a few more times before deciding to buy a drink and heading back home."
        "She texts me for the next ten minutes or so as I make my way through the dark streets of the second half of town."
        "I’m pretty sure she just wants to keep tabs on me so I don’t get mugged or something like that."
        "She’s a good girl."
        "Probably."
        "She still worries me from time to time."
        "But at least her heart is in the right place-"
        "Tightly wrapped around my fingers."
    else:
        "I sure wish girls would stop flirting with me. I am only going to disappoint them in the end."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ convenience5 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikoinvite1:
    play sound "phonebeep.wav"

    "I tap on Noriko’s name in my phone and wait for her to answer."
    "I'd normally wait a little while longer before inviting girls to the house but, considering that Noriko has apparently known me for however many years now, I think I’ve waited long enough."
    "Granted, I’ve only been consciously waiting for several weeks, but I’m sure someone who likes me as much as her is bound to agree."
    "The only issue is how I’m going to explain it to Ami. "
    "But I guess that’s something I can deal with later."

    play sound "phonebeep.wav"

    n "Sensei! Hey!"
    n "What’s up?"
    s "Hey. Are you doing anything tonight?"
    n "Not at the moment~"
    n "Did you want to go out together or something?"
    s "I was actually wondering if you’d want to come over my place."
    n "Wha-"
    n "For real!?"
    n "Like, this isn’t a joke?"
    s "Why would I joke about something like this?"
    n "Well...like-"

    if bonus == True:
        n "When you came to my dorm the other day, there was that whole thing about me being nervous. So I didn’t think you’d...call on me again so soon."
        s "This isn’t a booty call, Noriko. Ami is home."
        n "Oh..."
        n "And you’re...inviting me over anyway?"
        s "It appears that way."
    else:
        s "Get your mind out of the gutter, Noriko. I am your teacher, not your lover."
        s "Also, Ami is here. I can not hug others when she is present."

    n "Oh my God."
    n "I think I’m going to cry."
    n "Yes. Absolutely. I’ll get dressed and start heading over as soon as you send me the address."
    s "Great. I’ll send it now."
    s "See you soon, Noriko."
    n "Yeah! See you soon!"
    n "I’m so happy...holy shit."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 10.0

    "I hang up the phone and send my address to Noriko right away, sending Ami a message right after."
    "As I expected, she’s home."
    "But at least I have the entire walk back to figure out how I’m going to explain myself."
    "........."
    "......"
    "..."

    scene norikofirstvisit1
    with dissolve
    play music "normalday.mp3"

    a "Sensei! Welcome home!"
    s "Hey. Sorry for not walking home with you today. "
    a "Don’t worry about it! Everything is totally fine because now I get to have you all to myself!"
    s "..."
    a "..."
    s "..."

    scene norikofirstvisit2
    with dissolve

    a "{i}Because now I get to have you all to myself.{/i}"
    s "Ami, I have bad news."

    scene norikofirstvisit3
    with hpunch

    a "Gosh darn it! Who is it that’s stealing you away from me this time?!"
    s "I invited Noriko over."

    scene norikofirstvisit4
    with dissolve

    a "Noriko? The girl that’s head over heels in love with you?"
    a "Doesn’t inviting her here mean that...you also..."
    s "No. I mean, it’s not like I invited her here in secret or anything. I already knew you were going to be home today."
    s "And besides, you two are basically childhood friends."
    a "Didn’t we only hang out like...once? I was still in elementary[school] while you were tutoring."
    a "And I was still smart back then so I didn’t need any help."
    s "God, what happened to you?"

    scene norikofirstvisit2
    with dissolve

    a "You did! "
    a "I stopped caring as much about my education when I realized that you’d love me forever and always. Even if I stopped getting good grades."
    s "Well, either way, Noriko is coming over. And she’s actually excited to see you."

    scene norikofirstvisit5
    with dissolve

    a "Well I’m not excited to see her. If I hear her talk about loving you one more time, I’m going to punch her in the face."
    s "You’ve yet to punch Ayane and she says that every thirty seconds."
    a "I am punching Ayane in the face inside of my mind every minute of every day."
    s "And yet you still sleep in the same bed sometimes."
    a "Where I dream of punching her in the face until I wake up."

    play sound "doorbell.mp3"

    scene norikofirstvisit4
    with dissolve

    s "Oh. I'm guessing that's her now."
    a "Sensei...I don’t know how I feel about this girl knowing our address. "
    a "Maya really seems to think she’s some kind of stalker."
    s "She’s more like a puppy. If she starts hanging out in front of the house or whatever, I can just tell her to leave and she will."
    a "But still..."

    play sound "knock.mp3"

    n "Helloooo? Sensei? Ami? Is anyone home?"
    s "I’m going to answer the door now. "
    s "If you’re going to punch her, please do it in your mind like you do for Ayane."
    a "But...Sensei..."

    scene black
    with dissolve

    "I walk over to the door and let Noriko in."
    "To my surprise, she doesn’t try to hug me or jump on me the way a normal puppy would but, instead, neatly places her shoes at the front door and runs over to Ami."
    "........."
    "......"
    "..."

    scene norikofirstvisit6
    with dissolve

    n "Ami! I’m so happy to know where you live now!"
    a "Umm...why?"
    a "The only time we’ve talked was when you stole Sensei and took him to some random place that I wasn’t allowed to know about."

    scene norikofirstvisit7
    with dissolve

    n "And when we were little, too. But I guess that was so long ago that you might have forgotten."
    s "Noriko, you are aware that {i}I{/i} am the one who invited you over, correct?"

    scene norikofirstvisit8
    with dissolve

    n "Duh~ But who says I’m not allowed to be excited to see both of you?"
    n "It’s a Nakayarakawayama family reunion!"
    a "A...Naka...yaka...yama...reunion. "
    a "Yaaaay..."
    n "Yay!"

    scene norikofirstvisit9
    with dissolve

    n "So...this is what you two see every morning..."
    n "It’s nothing at all like your old place, Sensei. I like this a lot."
    n "It’s so much brighter."
    a "So...umm...how long have you known Sensei again, Noriko?"
    a "You said since you were...six?"

    scene norikofirstvisit10
    with dissolve

    n "Way before that, actually. I’ve known him for pretty much my entire life since he grew up next door to my house."
    a "Oh, okay...So he was just a neighbor."
    a "You probably didn’t actually start like, spending {i}time{/i} with him until you were old enough for...tutoring then, right?"
    n "Oh, no. I saw him all the time. He dated my sister Niki for five years and was coming over to hang out with her even before that."

    scene norikofirstvisit11
    with dissolve

    a "..."
    n "..."
    a "Come again?"
    n "Yup! He was practically family! "
    n "Everyone always said those two were going to be together forever and blah blah blah."
    a "..."
    n "..."

    scene norikofirstvisit12
    with dissolve

    a "..."
    n "..."
    s "Uh-oh."
    s "You had no idea, did you?"
    a "Nope."
    a "Why does this girl know more about your past than I do, Sensei?"

    "I guess...Sensei kept this hidden from Ami for some reason?"
    "I imagine the reason had something to do with everything happening around the same time as the accident..."
    "But I really don’t want to bring that up in front of Ami when she’s still extremely sensitive to it."
    "What I {i}can{/i} do is this, though."

    s "It’s actually Niki Nakayama. That one idol you listen to. "
    a "As if I would believe you dated Niki Nakaya-"

    scene norikofirstvisit13
    with dissolve

    a "Wait. What’s your last name again?"
    n "Nakayama. "
    a "And your sister’s name?"
    n "Niki."
    a "..."
    n "..."

    scene norikofirstvisit14
    with hpunch

    a "YOU DATED NIKI NAKAYAMA FOR FIVE YEARS AND NEVER TOLD ME ABOUT IT?!"
    a "WHO EVEN ARE YOU?!"
    a "I DON’T KNOW IF I SHOULD BE MAD OR IMPRESSED OR SAD RIGHT NOW!"
    a "I FEEL SO MANY DIFFERENT...FEELINGS!"

    scene norikofirstvisit15
    with dissolve

    n "You know I can introduce you if you want, right?"
    a "M-Me? Meeting...N-N-Niki? No way...I couldn’t..."
    s "That’s probably for the best. She’s not as nice as you expect her to be."

    scene norikofirstvisit16
    with dissolve

    a "You be quiet! I don’t even know who you are anymore!"
    s "Hey, I’ve been prioritizing you all these years, haven’t I? Isn’t that worth something?"
    a "How many other secrets are you hiding from me?!"
    a "I bet you never tutored Noriko at all! I bet she’s a...prostitute!"

    scene norikofirstvisit17
    with dissolve

    a "No offense, Noriko. You’ve been very nice to me so far."
    n "I’m...not a prostitute. I’ve never even kissed anyone before."
    a "This is comforting information, but I still have a hard time trusting anyone who openly admits to loving my [uncle]."

    scene norikofirstvisit18
    with dissolve

    n "I totally get it, Ami."

    if bonus == True:
        n "You’ve loved him for pretty much your entire life, but you’ve never been able to have him because of societal expectations and the stigma surrounding familial romantic relationships."
        n "I’m in a similar boat. Just instead of being blood-related, I was like an in-law...and also way too [young]to actually date."
        n "You and I have a lot more in common than you think."
    else:
        n "I'm kind of a fucking freak."

    n "Also, can I try on your maid outfit?"
    s "That was a very strange time to ask that question."
    n "Gotta strike while the iron is hot. I just buttered her up. There’s no way she’ll say no now."

    scene norikofirstvisit19
    with dissolve

    a "Umm...Noriko?"
    n "Yes, Ami?"
    a "Why are you being so nice to me if you know I'm a rival of yours? "
    a "We might have hung out once or twice when we were little but...we’re not little anymore."
    a "And my best friend hates your guts..."
    a "I can’t just start acting all friendly with you...it would mess everything up."
    n "Hey. Listen to me."
    n "I am {i}not{/i} going to take your [uncle] away from you. Got it?"
    n "You’ll always be his number one. "
    n "But you can’t blame me for wanting to give you a run for your money when I’ve been watching him my entire life."
    n "If anyone knows what that’s like, it’s you."
    a "..."
    n "..."

    scene norikofirstvisit20
    with dissolve

    a "Why does she have to be so nice? How am I supposed to hate someone like this?"
    n "How about we just shelve all of that negative energy for a few minutes and go put on some cute clothes?"
    n "Sound good?"
    s "I can’t tell how much of this is genuine desire to appeal to Ami and how much of it is just fuel to get into a maid outfit."

    scene norikofirstvisit21
    with dissolve

    n "My relationship with your [niece] is just as important to me as looking cute in girly clothes."
    n "I don’t think I’ll apply to the maid cafe or anything, but I need to at least confirm to myself and everyone in this house that I {i}can{/i} be cute."
    a "Yeah...I guess I wouldn’t mind you wearing it for a little while."
    a "But Sensei has to wait out here so he doesn’t see you get undressed."

    if bonus == True:
        "Yeah. God forbid I see Noriko in her underwear."
    else:
        s "I agree. That would be inappropriate."

    scene norikofirstvisit22
    with dissolve

    n "Deal! "
    n "Do you think you can help me put it on? I’ve seen the uniform and there are like, a lot of parts to it. "
    n "I want to make sure I wear it correctly, so I’ll be counting on you if that’s okay."
    a "Yeah...sure. Of course."
    a "The um...chest area...might be a little tight, though."
    n "I’ll be fine. They’re smaller than they look. "
    a "If...If you say so..."

    scene black
    with dissolve

    "I find myself standing around for several minutes, waiting to be called into Ami’s room to see the results of...coercion?"
    "The only other person I’ve seen win over Ami so quickly was Sara, and that’s probably just because she called her cute a bunch of times."
    "I don’t want to jump the gun and say that Ami has {i}accepted{/i} Noriko yet, obviously..."
    "But this seems to be going a little too well."

    n "Sensei! It’s safe to come in now!"

    play sound "dooropen.mp3"

    "I open Ami’s door just seconds after being told it’s okay to come in."
    "And yes. I {i}was{/i} eagerly pacing back and forth in front of the door in anticipation."
    "So far, every girl I have seen in the maid outfit has looked adorable."
    "And even with Noriko’s hair as...meticulously disheveled as it is, I can’t imagine it will be any different for her."

    scene norikofirstvisit23
    with dissolve

    n "Good morning, Onii-chan! Sorry for taking so long, but it was suuuuuper hard trying to figure out how to put on this darned dress."
    s "Who are you and what have you done with Noriko?"
    a "Sensei...why was she so insistent on calling you Onii-chan?"
    n "Because Onii-chan is Onii-chan and I’m just the cute little girl next door!"
    s "You don’t have to try so hard with the persona. You're perfectly fine without it."
    s "Definitely much different than normal, but still perfectly fine."

    scene norikofirstvisit24
    with dissolve

    a "Okay...that’s enough compliments for the day."
    a "It’s one thing letting her dress up in my clothes, but I’m not going to just let you stand there and ogle at her until the cows show up."
    s "It’s “until the cows come home,” Ami."
    a "You’re dumb. No cows have ever lived here. This is no home for them."

    scene norikofirstvisit25
    with dissolve

    a "She is really cute, though."
    a "I like this look a lot more than her normal...outfit."

    scene norikofirstvisit26
    with dissolve

    n "Hm? Did I hear something about my normal outfit?"
    n "Do you want to try on my clothes, Ami? I think you’d look great."
    a "Oh. Umm...no thanks. You’re taller than me and...I’d want to take a shower first and stuff..."
    n "Okay~ I think you'd make a cute little punk, though."
    n "You should come out shopping with me sometime. I know a few spots at the mall that-"

    stop music
    play sound "doorbell.mp3"
    scene norikofirstvisit27
    with hpunch

    "The doorbell suddenly rings and prompts everyone to stop dead in their tracks."
    "It’s just a doorbell, so it may seem like an overreaction."
    "But I’m pretty sure all of us are thinking the same thing."

    s "Were you expecting anyone today, Ami?"
    a "I...uhm..."

    scene norikofirstvisit28
    with dissolve

    a "I think it..."
    a "I think it might be Maya..."
    a "She mentioned something earlier about coming over, but I didn’t realize she meant like...{i}today{/i}."
    n "..."
    s "So what do we do?"
    s "Should I go out and distract her while Noriko gets dressed and...hides in the closet or something?"
    a "No. Maya will obviously know something is going on if you go out to greet her."

    scene norikofirstvisit29
    with dissolve

    n "It’s fine..."
    n "I mean, she already hates my guts, so it’s not like her opinion of me will get any worse."
    s "And I’m pretty sure she never expected me to listen to her about staying away from you."

    scene norikofirstvisit30
    with dissolve

    n "You..."
    n "Chose me over her?"
    a "I’ll...handle Maya."
    a "Just...whatever you do, don’t come out of the room until you hear us leave."

    scene norikofirstvisit31
    with dissolve

    n "Ami..."
    a "I know. I don’t have to do this."
    a "And, to be honest, I really don’t want to."
    a "But...this is what’s best for everyone."
    a "And I...think Noriko is really nice, so..."
    a "Just hang out in here for a little while."

    scene norikofirstvisit32
    with dissolve

    a "But if you so much as {i}peep{/i} at her while she’s getting dressed, I will make sure both of you never live to see another day."
    s "Remind me to give you literally anything you want for the next...forever."

    if bonus == True:
        a "What I {i}want{/i} is for Noriko to go home as soon as Maya and me are gone."
        a "I might like her, but I still don’t want the two of you alone together."
    else:
        a "What I {i}want{/i} is for you to actually be home for supper every once in a while."

    s "Okay, Mom."
    a "If you’re gonna be smart about it then-"

    play sound "dooropen.mp3"
    scene norikofirstvisit33
    with dissolve

    a "Ah, shoot! She must have used the spare key!"
    s "We have a spare key?"
    a "Of course we have a spare key!"
    n "Umm...guys?"
    a "I know! I’m going! Keep quiet!"

    scene black with dissolve
    "........."
    "......"
    "..."
    scene norikofirstvisit34
    with dissolve2
    play music "amiawake.mp3"

    a "Hey, Maya! I didn’t realize you were coming over today."
    m "I texted you like four times and you didn’t respond to any of them."
    m "Why are you touching me?"
    a "I’m just...really happy to see you."

    scene norikofirstvisit35
    with dissolve

    m "You’re weird."
    a "Yeah. I guess I...am kind of weird."
    m "No, like you’re acting weird."
    m "What’s going on?"
    m "Is everything okay?"

    scene norikofirstvisit36
    with dissolve

    m "Is Sensei-"

    scene norikofirstvisit37
    with hpunch

    a "Taking a nap!"
    a "We got karaage on the way home and...his was raw and he’s...having stomach problems."
    a "And that’s...actually why I was about to leave."
    m "You’re not going to stay here and take care of him?"
    a "I...need to go buy medicine!"
    m "I should have some in my bag if-"
    a "He only likes medicine from brand new bottles!"
    m "..."

    scene norikofirstvisit38
    with dissolve

    m "What?"
    a "Y-Yeah..."
    a "So...how about the two of us go for a walk and then just...come right back."
    m "But my legs are so tired from-"

    scene norikofirstvisit39
    with dissolve

    a "I’ll buy you something watermelon flavored~"
    m "My legs suddenly feel a lot better."
    a "Great! Then...let’s get going, shall we?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene norikofirstvisit40
    with dissolve2

    m "..."
    a "..."
    a "Maya? What’s up?"
    a "We’ve gotta get a move on before-"
    m "Did you get new shoes?"
    a "Um...y-yeah..."
    a "Sensei just got them for me...but they’re a little too big."
    a "So we have to...take them back..."
    m "..."
    a "..."

    scene norikofirstvisit41
    with fade

    m "..."
    a "..."
    m "..."
    a "..."
    a "Maya?"

    scene norikofirstvisit42
    with dissolve2

    m "They’re nice."
    a "Th-thanks..."
    a "But I won’t be keeping them, so..."

    scene norikofirstvisit43
    with dissolve

    m "Yeah."
    m "I wouldn't expect you to."
    a "..."
    m "Let’s go."
    m "I’m hungry."
    a "..."
    a "Okay..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ norikoinvite1 = True
    jump norikoinvite2

label norikoinvite2:
    scene norikofirstinvptwo1
    with dissolve

    s "Hah..."

    "I’ve lived here for how long now and I’m {i}just{/i} finding out there’s a spare key?"
    "I guess it makes locking this door pointless, but I might as well do {i}something{/i} while Noriko composes herself."
    "As soon as we heard the door close, she sprinted out of Ami’s room and ran off, presumably to the bathroom, saying that she needed a minute and will be gone before I know it."
    "Frankly, I feel like this entire situation is a little over the top."
    "I still have no idea what happened between her and Maya, but I at least hope it was something {i}big{/i} if simply being found inside of my house is enough to worry everyone."

    scene black
    with dissolve

    "I make my way back to my room and-"

    play sound "static.mp3"
    scene happy9
    with flash
    scene happy8
    with flash
    scene happy7
    with flash
    scene whythesky
    with flash
    stop sound

    "(sədn)"
    "I make my way back to the sky instead of my room."
    "It’s much brighter up here than it will ever be inside of that prison."
    "But, if you really think about it, isn’t the sky a prison too?"
    "A prison is something you are forced to live in or around or on top of or below, and the sky is at least half of those things."
    "Think back to when you were young."
    "Picture yourself in the backseat of a car, looking out of the window as your parents drive down the highway."
    "If you didn’t have parents, think of a bus."
    "When you looked up at the sky, half concealed by deceivingly tall trees in surrounding forests-"
    "Did you ever think the clouds were following you?"
    "You’d drive and drive and drive...but the clouds would never go away."
    "And you were too young to understand science or spatial reasoning (If that even counts clouds as objects and not something entirely unrelated), so you didn’t even bother considering that-"
    "Well, they’re {i}not{/i} actually following you."
    "But they {i}are{/i} following you."
    "The sky follows you!"
    "The world follows you!"
    "You can not escape!"
    "You can not leave!"
    "Fall deeper into the wishing well!"

    play sound "static.mp3"
    scene norikofirstinvptwo2
    with flash
    stop sound

    s "..."

    "I find myself back in my room, but I don’t remember walking here."
    "That seems to be happening a lot lately."
    "I’ll be just minding my own business, following a particularly slow or decrepit train of thought when-"

    if bonus == True:
        jump norikofirstinvx
    else:
        scene black
        stop music

        "Noriko runs into the bedroom with a tray of Totino's pizza rolls and the two of us have a pizza roll party."

        $ renpy.end_replay()
        $ noriko_love += 1
        $ norikoinvite2 = True
        stop music fadeout 10.0

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikospecial20:
    scene norikobow1
    with fade
    play music "wewereangels.mp3"

    a "And so the ice cream man said to Ayane, “That’s no golden retriever! That’s my landlord!”"
    s "..."
    a "What’s wrong? You normally love stories about the spontaneous yet lovable antics of Ayane Amamiya that always seem to have the beginnings cut out."
    s "Cut out of what, exactly?"
    a "What?"
    s "..."
    s "Nevermind."

    "I walk down the hall with Ami, preparing to leave[school] after a...day."
    "I don’t want to say it was a {i}normal{/i} day, though...because it was really anything but."
    "Molly is still determined to try and clear things up with me after what happened on Halloween, and I’m running out of excuses when it comes to avoiding her."
    "Sooner or later, I’m going to have to look her in the eyes and admit to what happened...but that’s kind of impossible to do when I can’t even {i}remember{/i} it."
    "The aftermath is still ingrained into my memory, though."

    if bonus == True:
        "And each time I feel myself getting harder from thinking about it, I have to slow down and remind myself that none of it was real."
    else:
        "I know it seemed like I hugged her while she was asleep, but if hug happens and no one is around to see the hug, does the hug {i}actually{/i} happen?"
        "None of it was real."

    "Or some of it was real."
    "Or none."
    "Or some."
    "Something did or didn’t happen."
    "I either liked or didn’t like it."
    "Part of me wishes that Tsuneyo would have just ended it right there, but I feel as if that part is not an actual desire of mine and just some selfish avoidance tactic buried underneath mountains of greed."
    "I’m tired of digging, though."
    "It’s impossible to know what lies beneath the surface without someone informing you, and I’ve always hated the feeling of dirt underneath my fingertips."
    "I don’t want to dig anymore. "
    "I just want someone to unearth whatever’s down there and tell me what I’m supposed to do."
    "How do I turn things back to normal? "
    "And what {i}was{/i} normal in the first place?"

    if bonus == True:
        "Emotionless sex with a handful of girls who were already attached to me before I even had to do anything?"
        "Is that what I want?"
        "Or, scratch that-"
        "Is that {i}everything{/i} I want?"

        play sound "static.mp3"
        scene lavendersgreen1 with flash
        scene lavendersgreen13 with flash
        scene lavendersgreen18 with flash
        scene lavendersgreen23 with flash
        scene lavendersgreen29 with flash
        scene lavendersgreen30 with flash
        scene norikobow2 with flash
        stop sound

        "Yes."
        "That’s everything."
        "This is my life."
        "This is who I am. "
        "Why would I ever want anything other than the easiest possible option?"
        "Working for things is exhausting."
        "I can just not work."
        "I can have Ami do everything for me."
        "She’ll do it. She loves me."
        "I didn’t do anything to Molly. I wouldn’t have done anything. "
        "Unless she wanted me to."
        "Did she want me to?"
        "Is that why she wants to talk to me?"
        "Does she want to do it again?"
        "What-"
    else:
        play sound "static.mp3"
        scene norikobow2 with flash
        stop sound

    a "Sensei?"
    s "..."
    a "What’s wrong?"
    s "..."
    s "Nothing, Ami."
    a "It doesn’t look like nothing."
    s "It’s-"
    a "Is it about Molly?"

    scene norikobow3
    with dissolve

    s "What do you know about Molly?"
    a "Uhh...nothing. I just noticed you were kinda avoiding her all day. And it seemed like it was a little more than just because she’s really annoying in...large doses."
    s "..."
    a "..."

    scene norikobow4
    with dissolve

    s "It’s not about her. "
    s "I’m just tired."
    a "I see..."
    a "Well, you can take a nap when we get home and I’ll make you dinner."
    a "It’s probably best to just stay home all day if you’re not feeling great. You can go be a weirdo dorm-invader some other time."
    s "...Yeah."
    s "Actually, can I ask you something?"
    a "Of course, Sensei. You can ask me anything you want."
    s "Is there {i}anything{/i} I could do that would make you...feel differently for me than you do right now?"

    scene norikobow5
    with dissolve

    a "Is there something specific you have in mind?"
    s "No."
    a "Quick answer."
    s "Yes. But yours isn’t. Just tell me and-"

    scene norikobow6
    with dissolve

    a "Of course not."
    a "I’ll love you forever and ever."

    if amifingered == False:
        a "The only question is whether or not that love will become too much for you one day."
        s "I don’t know what that’s supposed to mean."
        a "That’s just what you’re saying to yourself. "
        a "You know, Sensei."
        a "I think you’ve always known."
        a "But that’s a story for another-"

    else:
        a "There’s not a single thing you could do that would change that."
        a "Even if you became the most horrible person in the whole wide world, I’d still welcome you home with open arms and a warm bath."

        scene norikobow7
        with dissolve

        if bonus == True:
            a "Then maybe even a little {i}more{/i} if you know what I mean..."
            s "You only have two modes. I definitely know what you mean."
            a "I’ve got a third one, too. It just hasn’t been turned on yet."
        else:
            a "Except the bath would not be filled with water. It would be filled with {i}hermit crabs.{/i}"

        s "That's...worrying?"

    scene norikobow8
    with dissolve

    n "Sensei!"
    a "Noriko? What are you-"

    scene norikobow9
    with dissolve

    n "I’m sorry for my outburst during the Halloween party! "
    n "It was impulsive and childish and I want to put it behind us!"
    n "Please accept my apology!"
    s "..."
    a "Outburst? Is this about the bathroom thing?"

    "Why is she apologizing?"

    if bonus == True:
        "Because I fingered her sister?"
        "She’s apologizing to {i}me{/i} because {i}I{/i} fingered her sister and {i}she{/i} got upset about it?"
        "I don’t understand."
        "Why do things keep happening that I don’t understand lately?"
        "I should be saying sorry to her."

        play sound "static.mp3"
        scene nikihotel26 with flash
        scene norikosadhalloween5 with flash
        scene norikobow10 with flash
        stop sound
    else:
        "Because I keep putting vegetables in her desk when she isn't looking?"
        "I had no idea she even knew that was me."

        play sound "static.mp3"
        scene norikobow10 with flash
        stop sound

    "No. I didn’t do anything wrong."

    if bonus == True:
        "All I did was slip my fingers inside of someone she’s related to."
        "Someone I’ve done that same thing to probably hundreds of times before."
        "If she gets upset about that, that’s on her. "
        "I am not obligated to make her or anyone else happy. It would just make things better and easier if I did."
    else:
        "They were only vegetables."

    n "I understand that this is probably not the best time to do this, but if I have to go one more night without telling you how I feel, I’m going to rip my hair out."
    n "It doesn’t matter to me what you do with anyone! Whether it be Niki or...Maya...or even Ami! "
    a "It’s not {i}even{/i} Ami when I am indisputably Sensei’s number one girl, thank you very much."
    n "The point is that I need to be stronger! And less sensitive!"

    scene norikobow11
    with dissolve

    n "You don’t deserve to be burdened by the feelings of one more girl who doesn’t have her head on straight."
    n "So I want you to know that I, Noriko Nakayama, am not that!"
    n "I am impulsive! And I am selfish! And I am far too sensitive at times! "
    n "But I am strong! And independent! And so many more things that I want you to find out about!"

    scene norikobow12
    with dissolve

    n "So please...accept my apology!"
    a "..."
    s "..."

    scene norikobow13
    with fade

    a "Umm..."
    a "I’m...going to go home now and start warming up the bath for you..."
    a "I still don’t know what’s wrong, but...if it’s something involving Noriko and {i}not{/i} Molly, maybe talking to her about it will make you feel better?..."

    scene norikobow14
    with dissolve

    a "You’ve still gotta come home right away, though! Got it?"
    a "Don’t go running off with other people from your past when you’ve got the perfect [niece] waiting at home for you!"
    s "..."
    a "..."

    scene norikobow15
    with dissolve

    a "Really. Please don’t. "
    a "I know I said there’s nothing you could ever do that would make me change how I feel, but that would still hurt a lot and I’d cry forever. Also, the house would flood because we are out of tissues."

    if bonus == True:
        a "Why can’t you just use a sock or a t-shirt to do your business like a normal boy?"
        a "Not that I know what a {i}normal{/i} boy is when I’m just an innocent [niece] who-"

    s "I’ll still come home, Ami. Just let me talk to Noriko first."

    scene norikobow13
    with dissolve

    a "Okay."
    a "I love you, Sensei."
    s "..."
    a "..."
    a "............?"
    s "I love you too, Ami."

    scene norikobow16
    with dissolve

    a "Aww! I didn’t even have to tell you to say it that time!"

    scene norikobow17
    with dissolve

    a "Bye-bye, Sensei! Bye, Noriko!"
    a "Touch my [uncle] and I’ll cut your limbs off!"
    n "Thank you very much, Ami! I am humbled by the privilege to spend time with your [uncle]!"

    scene norikobow18
    with fade

    s "You know you don’t have to be that formal, right?"
    s "You don’t even have to apologize for your outburst. Let’s just ignore it and move on with our lives."
    n "I can’t do that, Sensei. "
    n "I’ve done something I promised not to do- and that’s getting in the way of you and someone else...Even if that someone else is my sister."
    n "But I made a {i}new{/i} promise to myself that I would win your heart fair and square! And that means no telling you who to see or what to do!"
    n "I want you to choose me for me! Not me as an alternative! And if your interest is going to wane, that just means I have to work harder!"
    s "..."
    n "I realize that I {i}am{/i} making a scene right now and that we have been likely receiving strange looks from some of the people in other classes...I can’t really tell because of the whole bowing thing-"
    n "But I need you to know that I am serious! And that I will accept any punishment you deem necessary!"
    s "..."
    n "{i}Any{/i} punishment! No matter how sick or twisted it may be!"
    s "..."
    n "And I know that now we’re probably getting even more stares, so it would be really nice if you would respond to me because I’m beginning to get embarrassed!"
    q "He accepts!"

    scene norikobow19
    with fade

    q "Such passion! Such determination! "
    q "Of course he accepts your apology! He’d be foolish not to!"
    s "..."

    scene norikobow20
    with dissolve

    if bonus == True:
        q "I have to admit, when I heard you screaming from around the corner of the hall, I thought “Oh great. Teenage drama. Don’t wanna touch this with a ten foot pole.”"
    else:
        q "I have to admit, when I heard you screaming from around the corner of the hall, I thought “Oh great. Drama. Don’t wanna touch this with a ten foot pole.”"

    q "But as my legs carried me closer and closer to the source of the noise, I was reminded that I {i}live{/i} for this sort of thing! And now I wish nothing but the best for the two of you!"
    s "..."

    scene norikobow21
    with dissolve

    if bonus == True:
        q "I don’t even care that this guy’s probably twice your age! Give ‘em hell, girl! "
    else:
        q "I don’t even care that this guy’s your teacher! Give ‘em hell, girl! "
        s "(Gasp)"

    q "Just remember to invite me to the wedding since I’ve been there for you from the start!"
    s "..."
    s "Who are you, exactly?"

    scene norikobow22
    with dissolve

    ima "Imani. "
    s "..."
    ima "Sorry, Imai. Keep forgetting we’re supposed to use last names first over here."
    ima "But if you want to just call me Imani, that’s cool too. What’s your name? You look like a..."
    ima "Uhhhhhhhh..."

    scene norikobow23
    with dissolve

    ima "Jose."
    s "..."
    s "No."
    s "What are you even doing here? We’re kind of in the middle of something."

    scene norikobow24
    with dissolve

    ima "Hey! Is that any way to treat the newest staff member at [kumon_mi_high]?! "
    ima "I’ve been nothing but accepting and supportive of you since the get-go and you’re already getting rid of me?! Where is my lawyer?!"
    s "You work here?"

    scene norikobow25
    with dissolve

    ima "I’m filling in for uhh...Miss Watabe, I think? Whoever the one on medical leave is."

    "Oh...right."
    "Wakana not being around means that someone obviously has to look after her students."
    "So I guess this Imani girl is just going to be around until she comes back."

    s "Well...nice to meet you, I guess. But-"

    scene norikobow26
    with dissolve

    if bonus == True:
        ima "Yeah, yeah. Hearts to break. Cradles to rock. I know how it is. "

    ima "Just take it easy on her, would ya? She seems really nice based on the five or six lines of dialogue I’ve heard from her."

    scene norikobow27
    with dissolve

    ima "Anyway byeeeeeeeeeeeeeeeeee! See you around probably maybe unless I get fired! WE’LL SEE!"
    s "..."

    scene norikobow28
    with fade

    s "Well, that was weird."

    if bonus == True:
        n "Yes. But it did not prevent me from imagining her with her clothes off."
    else:
        n "Yes. But she was nice and I am excited for her to be a recurring character in Lessons in Love from this point on."

    s "I’m glad to see that she at least managed to lighten the mood a little. It’s weird seeing you get serious like that."

    scene norikobow29
    with dissolve

    n "I {i}had{/i} to be."
    n "I hate coming off as weak or childish, and crying to you about a thing you did with my sister just made me look like some desperate loser who doesn’t want to actually {i}fight{/i} for you."
    n "But I really do wanna fight, Sensei. I’m not a kid anymore. "
    n "These feelings aren’t just...lingering traces of a first crush or...something I’ve become dependent on in order to get by. They’re {i}real{/i} feelings. For {i}you{/i}."
    n "So if bowing to you and asking for your forgiveness in the halls is the best way for me to get that across, I’ll be damned if I’m not gonna take the leap."

    "I sigh and attempt to force myself into the realization that I can’t control how Noriko or...how anyone else, for that matter, acts. "
    "She’s still just a [teenage]girl at the end of the day, no matter how “adult” she tries to be."
    "The real adult thing to do in this scenario would just be bottling up those feelings and turning a simple misunderstanding into an event that would prevent us from ever seeing one another again."
    "It’s that immature striving for forgiveness...or the hope that things can eventually change that you only get to see from girls like her."
    "And, if even for only a moment, I’m reminded of why I’ve been having so much “fun” in Kumon-mi."
    "In moments like this, where my back isn’t against the wall."
    "Where I don’t have to take the passenger seat and let my disfigured sense of morals guide my actions."
    "Where I can live without the worry of how {i}me{/i} living will impact others."
    "I wish it was possible to just ignore all of those more horrible parts of life."
    "But, then again, I’m sure that’s something everyone wishes."

    s "..."
    s "Okay. You’re forgiven."

    scene norikobow30
    with dissolve

    n "Really?!"
    s "Is it that much of a surprise? This whole time, I’ve been saying you have nothing to apologize for."
    n "Yeah, I know. But you could have been lying. People lie about stuff like that all the time."
    s "I try to only lie when I have something to gain from it. This isn’t really one of those times."
    s "Besides, just crying and begging for me to not do something isn’t really childish in my book. You’re fine, Noriko."

    scene norikobow31
    with dissolve

    n "Then, umm..."
    n "Can we maybe walk home together?"
    n "I know that Ami asked you to come home right away, but...it’s not like the dorms are that big of a detour. And it would make me really happy if-"
    s "Sure. I’m tired of just standing around here anyway."
    s "The sooner we get out of here, the better."
    n "Right!"
    n "Just, uhh..."
    n "I left my winter clothes in one of the gym lockers, so...I’m gonna run and grab them really quick."

    scene black
    with dissolve2

    "Noriko sprints off in the direction of the gym and I don’t know what else to do but just...continue standing around."
    "I don’t like standing around."
    "I want to walk."
    "I need to walk."
    "I need to leave[school]."
    "I need to-"

    n "Okay! Ready to go."
    s "Already? It’s only been thirty seconds."
    n "What are you talking about?"

    play sound "static.mp3"
    scene norikobow32 with flash
    stop sound

    n "What’s only been thirty seconds?"
    s "..."
    s "Weren’t we just in[school]?"
    n "Define “just,” because we left like ten minutes ago."
    n "Also, are you sure it’s okay for me to be holding your arm like this? I was kinda joking when I suggested it, but I’m all for it if you’re actually enjoying it."

    scene norikobow33
    with dissolve

    s "Oh. Yeah, you’re fine. I don’t really care. "
    n "Works for me! Your arms are a lot bigger now than when we were younger."
    s "That is how growing works, Noriko."
    n "I know, I know. Just...trying to make small talk since you seem a little out of it."
    s "I’m fine."
    s "I didn’t do anything."

    scene norikobow34
    with dissolve

    n "O...kay?..."
    s "..."
    n "..."
    s "..."
    n "..."

    scene black
    stop music

    if amifingered == False:
        "I walk Noriko home and everything is good."

        $ noriko_love += 1

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

    else:
        if bonus == True:
            "I go home and fuck my [niece]."
        else:
            "I go home and hug my [niece]."

        $ noriko_love += 1
        $ ami_lust += 1

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "{i}Ami’s lust has increased to [ami_lust]!{/i}"

    $ renpy.end_replay()
    $ norikospecial20 = True

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    "Bed."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    jump advancetotues

label norikodorm20:
    play sound "knock.mp3"

    "I knock on Noriko’s door and wait for her to answer."
    "And, now that she’s managed to get her completely unnecessary apology out of the way, I expect tonight to be mostly drama-free."
    "Or at least that would have been the case before I thought of that. "
    "Now, I worry that I may have jinxed myself."

    stop music fadeout 10.0

    "Oh well. Worse comes to worst, I just let her waste her breath and apologize for something {i}else{/i} she doesn’t have to apologize for when it’s all said and done."
    "I’ll truly never stop being thankful for how predictable most [teenager]s are-"
    "And how even the slightest whiff of love can cause their brains to go haywire."

    play sound "knock.mp3"

    s "Noriko, are you in there?"
    n "Oh, Sensei! Yeah! I didn’t hear the first knock."
    n "You can come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I make my way into Noriko’s room to be assaulted by the same fruity scent of energy drinks that I’ve grown used to when visiting her and Kirin."
    "Today’s scent is particularly potent, however. And if there’s anything I know about energy drinks-"
    "It’s that Noriko will be exactly the same as always because the “energy” aspect is a myth perpetuated by big beverage companies to trick [teens] into buying products that will-"
    "help them cope with the extreme mental strain of [high_school] life and its accompanying exhaustion before ultimately becoming addicted and drinking them until their kidneys are filled with stones."
    "Just kidding."
    "I’ve never had an energy drink."
    "I’m sure they’re okay."

    scene norikochinadress1
    with dissolve2
    play music "love.mp3"

    s "Oh, wow."
    n "Good wow or bad wow? What kind of wow is that?"
    s "Just...can’t say I was expecting this."
    n "How does it look? Be honest. I can take it."
    s "It looks...great. I’m just confused about why you’re wearing it."

    scene norikochinadress2
    with dissolve

    n "My parents sent it to me."
    n "They just redid the decor of the restaurant and they’re trying out new qipao to fit the color scheme. And of course Nee-chan is too busy to model for them anymore, so...voila. "
    n "Fancy Noriko."
    s "I like fancy Noriko. It doesn’t hurt my eyes trying to keep up with the outfit."

    scene norikochinadress3
    with dissolve

    n "Hey! There wouldn’t be a need for me to dress the way I do if it weren’t for the necessity to fight back against societal expectations and the inherent Japanese obsession with professionalism!"
    n "Dressing in stuff that’s overcomplicated or hard to follow is just one of many ways I push back against what people expect of me! I’m fighting the power!"
    s "Right. And what are the {i}other{/i} ways you fight back against society’s expectations of you?"

    scene norikochinadress4
    with dissolve

    n "I pierced my belly button. Does that count?"
    s "What? No. And since when? I saw you in a swimsuit very recently and I do not remember that at all."
    n "My parents made me take it out because it got infected."
    s "You truly are one of the great rebels of this generation, aren’t you?"

    scene norikochinadress5
    with dissolve

    n "I know that I’m not {i}actually{/i} rebelling in any way. But, to be fair, what could someone my age even do?"
    n "The best chance I’d have is starting a band and just hitting it big like that. But even then, there are a gajillion others trying to do the same thing."

    if bonus == True:
        n "Teenagers don’t really have a voice, Sensei. {i}Especially{/i} [teenage]girls. "
    else:
        n "But hey, if Nickelback can do it, I can too."

    s "Hey, I’m not trying to tear you down. I’m just saying that it wouldn’t kill you to look a little more...normal from time to time."

    scene norikochinadress6
    with dissolve

    n "Normal like this? Because I feel like I’d get a lot more stares going out in a qipao than I would in a brightly colored flannel with...chains and stuff."
    n "Besides, being {i}pretty{/i} is kind of Nee-chan’s thing now. "
    n "There’s no way I was ever going to be able to seriously compete with her once she started trying, so I just...wound up going a different route."

    scene norikochinadress7
    with dissolve

    n "I thought that route would be to your liking, Sensei."
    n "A brand new Noriko would mean a brand new start to our relationship, wouldn’t it?"
    s "Just changing your clothes doesn’t change the person you are. And even if it did, you’d be brand new to me anyway. "
    n "Those memories are still in there somewhere. All the parts of the me in the past that you'd want to hang onto are still there."
    n "There are just a lot of other parts that come included now as well."

    scene norikochinadress8
    with dissolve

    if bonus == True:
        n "And some {i}other{/i} parts that have been improved in a number of ways. But I’m sure I don’t need to remind you of those."
    else:
        n "And some other parts that have been improved in a number of ways. But I'm sure I don't have to remind you of my Squidward tattoo."

    s "You certainly do not. In fact, I have a picture message saved in my phone to back that claim up."

    scene norikochinadress9
    with dissolve

    n "Sure wish I had something similar in {i}my{/i} phone."

    if bonus == True:
        s "I can’t send you a picture of my penis, Noriko. That would be putting way too much power in the palm of your hand."

        scene norikochinadress10
        with dissolve

        n "I wouldn’t do anything with it, I swear!"
        n "Well...nothing involving anyone else! It would be for personal use only! "
        s "No can do. I’ll gladly accept any other photo you want to send me, though."
    else:
        s "For the last time, I am not getting a Squidward tattoo."

    scene norikochinadress11
    with dissolve

    n "Mmm...meanie."

    if bonus == True:
        s "Like...I don’t know. Maybe one in some sort of...Chinese dress?"

        scene norikochinadress12
        with dissolve

        n "If you wanna see more of this, why not come to my parents’ restaurant with me sometime?"
        n "They’d be really happy to see you {i}and{/i} you’d get to see me serve people in this thing."

        scene norikochinadress13
        with dissolve

        n "And who knows? Maybe I could {i}serve{/i} you too?"
        s "Bold claim for someone who has only dry humped me so far."

        scene norikochinadress14
        with dissolve

        n "Ah~ The best dry humping of my life, too..."
        s "...How many people have you done that with?"

        scene norikochinadress15
        with dissolve

        n "People? Just you. But then there’s stuff like pillows and...blankets if you curl ‘em up just right...and the corner of your desk..."
        s "Excuse me?"
        n "What? It smelled like you and there was no one else in the classroom."
        s "..."
        n "I’m a growing girl. I get urges."
        n "Those urges just happen to be exponentially greater around things that you have touched."
        s "If that were true you’d have already fucked Kirin by now."

        scene norikochinadress16
        with dissolve

        n "Hey...come on."
        n "I obviously know that things have happened between you two, but you don’t need to remind me about it like that. That’s just mean."
        s "I was just kidding. I didn’t mean anything by it."
        n "You don’t have to apologize or anything, just...try not to bring other girls up if you don’t have to."
        s "..."
        n "..."

        scene norikochinadress17
        with dissolve

        n "Uhh...A-Anyway! Why don’t we sit down and go back to talking about...my parents or something?! That should stave away the horny for a little while longer, don’t you think?"
        s "The last time we tried that, I’m pretty sure you imagined me fucking your dad."

        scene norikochinadress18
        with dissolve

        n "Ewwww, Dad! No! That’s {i}my{/i} boyfriend!"
        s "And apparently you are already doing it again..."
    else:
        s "Just shut up and keep modeling so we can get on with the event."

    scene black
    with dissolve2
    stop music fadeout 15.0

    if bonus == True:
        "It takes Noriko a minute or two to stop fantasizing about a thing I really wish she wouldn’t fantasize about."
        "But after that, we manage to steer clear of “the horny” and move both locations and topics into territory we’re a bit more comfortable with."
        "Well, territory {i}she{/i} is more comfortable with."
        "To be honest, if she came out right now and asked me to do what I refused to do to her outside of the Halloween party, I wouldn’t have a second thought."
        "My hand would be buried deep inside of that sleek, Chinese dress...doing the same things to her I did to her sister in that fancy hotel room."
        "I wonder if they’re just as similar on the inside as they are on the outside."
        "I wonder how long it will take for me to find out."
        "I wonder-"
    else:
        "Noriko gets angry at me for rushing the video game and immediately skips to the next part of the event, cutting out a sizable chunk of content and ruining context in the process."

    if bonus == True:
        play sound "static.mp3"
        scene lavendersgreen1 with flash
        scene lavendersgreen13 with flash
        scene lavendersgreen18 with flash
        scene lavendersgreen23 with flash
        scene lavendersgreen29 with flash
        scene lavendersgreen30 with flash
        scene norikochinadress19 with flash
        play music "blueair.mp3"
        stop sound
    else:
        play sound "static.mp3"
        scene norikochinadress19 with flash
        play music "blueair.mp3"
        stop sound

    "I don’t wonder anything."
    "I stop thinking because I have to stop thinking."
    "Thinking more will be bad."
    "Noriko loves me."
    "Noriko won’t mind if I-"

    n "You’re being weird again."

    scene norikochinadress20
    with dissolve

    s "..."
    n "Like when we walked home from[school]."
    n "You’ve done it a few times before that too."
    n "There are these like, long stretches of time where you’ll be there and you’ll be responding, but it won’t actually be {i}you{/i}, you know?"

    scene norikochinadress21
    with dissolve

    n "Well, they’re not all {i}long{/i}, I guess. Like, this time, it was really only for a minute or two."
    s "That just happens sometimes, I guess."
    s "{s}It could be dangerous.{/i} It’s not really something you should worry about."
    n "I never said I’m worried. If anything, I’m glad I can be here for them."
    n "It’s a lot better knowing that you have me as an outlet to vent to if you ever want."
    n "Not like you {i}would{/i} ever want to do that, though, when you’ve always been pretty secretive about the things that are bothering you."
    n "Like, back when we were always with Maya-"
    s "Don’t talk about Maya right now."

    scene norikochinadress22
    with dissolve

    n "I mean...fine by me. But why not?"
    s "It’s just...not a good idea, I think."

    "Half of me wants to hear whatever it is Noriko has to say."
    "But another half of me that I thought I’d kept at bay is now begging me to steer clear on the off chance that Maya’s thoughts are right and that...learning too much might be bad."
    "And here I was thinking I’d be able to not take her advice."
    "How annoying."

    scene norikochinadress23
    with dissolve

    n "What do you want to talk about instead, then?!"
    n "I feel like tonight’s been pretty much all about me, so if there’s anything you want to say-"
    s "Keep talking about yourself."
    s "You said on Halloween that you wanted me to know more about {i}you{/i}. So tell me more about you."
    s "Where do you want to go after [high_school]? What do you want to be? Just talk."
    s "I don’t really care what it’s about."

    "I just need something to distract me."
    "I need to stop slipping."
    "I need to focus on the task at hand...getting to know Noriko and everyone else without..."
    "Without thinking at all."
    "I need to grind affection points."
    "Wait, what are affection points? "
    "What am I thinking?"
    "{s}Have I really spent so much time with Molly that it{/s} {b}HAVE RECENT EXPERIENCES SOMEHOW{/b} led to me treating life more like a game than I ever thought I would?"
    "I know those were essentially {i}my{/i} words last Halloween when-"

    play sound "static.mp3"
    scene samhain21 with flash
    scene samhain33 with flash
    scene norikochinadress23
    with flash
    stop sound

    "Molly and Tsuneyo are two girls who like me and appreciate me and admire me."
    "They will forget this the next time the world resets. "
    "Ignore it and it will go away."
    "Noriko, please break this silence."
    "Please."

    n "I think..."
    n "That what I’d want to do more than anything is help people."
    s "{s}Help me{/s} How?"

    scene norikochinadress24
    with dissolve

    n "I don’t know...charity work, maybe?"
    n "Ideally, I’d love to do something along the lines of like...building homes for the homeless, or...teaching underprivileged kids how to read."
    n "But, unfortunately, there’s just not really any money in stuff like that."
    n "It’s really sad, you know? All the nicest, best things out there have to be done by people willing to sacrifice their well-being in order to do it."
    s "And that’s something you’re considering?"
    n "I don’t really know."
    n "I mean, I’m in [high_school]."
    n "Things I say right now don’t really matter. It’s what I say {i}after{/i} I graduate that matters. And anything can happen between now and then."
    n "It would just be nice to kinda...change the world. You know?"
    s "You’re never going to change the world."

    scene norikochinadress25
    with dissolve

    n "I’m not?"
    s "{s}We’re stuck here.{/s} I highly doubt it."
    s "{s}Nothing can be changed.{/s} “Changing the world” is something a lot of people your age plan on doing."
    s "{s}Something is buried underneath your feet.{/s} Then, once they get out of [high_school], they realize it’s impossible and fall into the same slump all people fall into."

    if bonus == True:
        s "{s}You will never find it.{/s} They get jobs. Go to work. Go home. Fuck whoever they’re living with. Fuck themselves if they don’t have anyone there. Sleep. And then repeat."
        s "{s}It might not even exist.{/s} The world can’t be changed. There are too many people trying to prevent it from changing that it offsets all of the people who are."
        s "{s}Does any of this exist?{/s} If you want to waste away your life pursuing such a pipe dream, feel free. But don’t let it break your spirit when it doesn’t pan out how you want."

    n "Are you sure your memories are broken?"
    s "What?"
    n "It’s just that you said essentially the same exact thing to me when I was little."
    n "Which, at the time, was pretty upsetting since I was still just a kid."
    n "But hey, it prepared me for {i}not{/i} getting upset this time around, so at least that’s good."
    s "Have we really had this discussion before?"
    n "More or less. Just, minus the whole “[high_school]” part of it."
    s "Well...at the end of the day, you’re still just a [teenager]. Any “difference” you could make wouldn’t happen until you’re much older."

    scene norikochinadress26
    with dissolve

    n "I mean...yeah. But is that {i}really{/i} all I am? Because my time with you has made me feel like I’m a little bit more than that."
    s "The time I do remember? Or the time I don’t? Because I don’t really think I’ve done anything substantial since you walked back into my life."
    n "Before."
    n "You were no normal tutor, Sensei. Like, sure you helped us with our general studies and reading comprehension and all that..."
    n "But a lot of the things you taught us were those same cynical spiels about how the world will never change or how...time is a bitch..."
    n "And all this other stuff most girls would get weirded out by."
    n "We loved you, though. So we listened."
    n "We ate up every word and, soon enough, we started to echo those feelings."
    n "But the interesting thing about feelings is that they don’t work the same way in all people."
    n "And once they’re inside of you, they evolve and adapt in ways that make them much more than echoes. They’re closer to like...screams or...encryption keys or something."
    n "But {i}you{/i} were the one that helped us realize we were more than just average girls."
    n "My decision to go down the path of finding my own sense of...individuality was a lot more than just wanting to detach myself from Nee-chan."
    n "It was me doing something I thought would make you proud. "
    n "It was me turning into a person that wouldn’t ever fit into one of those cynical analogies you’d tell some other [young_girl], still naive to the world around her."
    n "It was me following in your footsteps, even when I had no idea where they were, what they looked like, or where they were heading."
    n "Like it or not, you were always my role model. And you’ll probably always {i}be{/i} my role model."

    scene norikochinadress27
    with dissolve

    n "Even when you think you’re the worst human being in the world...that you’re absolute shit...something I {i}know{/i} you feel sometimes..."
    n "Even then, I will be here to remind you that you are more than that."
    n "Underneath all of that pain and anguish and...defeat is the man who single handedly turned me into the girl I am today."
    n "Maya, too. She {i}definitely{/i} wouldn’t be who she is if it wasn’t for you."

    scene norikochinadress28
    with dissolve

    n "But that’s why I haven’t {i}entirely{/i} given up on changing the world yet."
    n "If {i}you{/i} weren’t able to, maybe it’ll make you feel a little better if I can. "
    n "Or, at the very least, show you that you left some sort of positive mark on the world instead of just some giant shadow..."
    s "..."
    n "..."

    scene norikochinadress29
    with dissolve

    n "So! What’s the plan for Christmas?"
    n "Wanna go on a date?"
    n "I know this one bakery that has {i}amazing{/i} cakes throughout all of December."
    s "You’re just...moving right on to the next topic?"
    n "Instead of what? Making you feel even more uncomfortable by tangentially detailing all of the reasons I still love you after all these years? Of course."
    n "We’ve reached the part of the conversation where I attempt to get closer to you through future plans instead of past occurrences. And Christmas is the most romantic day of the year."

    scene norikochinadress30
    with dissolve

    s "I’m pretty sure the class will wind up having another party."
    s "That’s what happened last year and I never really got a say in it."
    n "Are we getting each other presents?"
    s "They did a Secret Santa thing last time, so I imagine they’ll do that again as well."
    n "I’m not talking about that. I’m talking about you and me."

    scene norikochinadress31
    with dissolve

    n "I..."
    n "There’s something I want to give you."
    n "I’m not sure if you’ll {i}like{/i} it...but I found it when I was digging through some old stuff recently...and I think you should have it."
    n "And...you don’t {i}have{/i} to get me anything in return, but..."
    n "But it would make me really happy if you did..."
    s "..."
    n "Forget-"
    s "Sure."

    scene norikochinadress32
    with dissolve

    n "Ah-"
    s "I’m sure I can manage to remember that much."
    s "At least I know about this present beforehand, unlike last year."

    scene norikochinadress33
    with dissolve

    n "Mmn~"
    s "..."
    s "Is everything okay?"

    if bonus == True:
        n "I got weirdly turned on by the idea of you buying me a Christmas present and now I’m trying to stay cool."
        s "..."
        n "It's a shock thing. I don't know. I get horny when things surprise me sometimes."
        s "..."
        n "..."
        s "Do you..."
        s "Do you want me to go find you a desk or something?"

        scene norikochinadress34
        with dissolve

        n "You’re really going to make me regret telling you that desk thing, aren’t you?"
    else:
        n "Yeah. I'm just suddenly really tired."
        s "Is that so? Then I will leave this place and allow you to get some sleep, as I would not want to keep you up longer than you would like to remain awake for."
        n "I hope I have an extra pair of arms in my dream."
        s "What would you do with them?"
        n "Zzzzzzzzzzzzz..."

    scene black
    with dissolve2

    if bonus == True:
        "As Noriko would say, “the horny” fades away and I wind up leaving shortly after that."
        "And, I don’t know why...but I’m actually kind of thankful that nothing else wound up happening."
        "In fact, I might even feel a little...better?"
        "Not better in the fact that I feel {i}good{/i}...but better in the fact that some of the clouds inside of my head have begun to clear up."
        "I’m sure tomorrow will be overcast as well- it always is."
        "But it was nice being reminded of what it feels like to see a little clearer, even if it’s only for a short while..."
    else:
        "Noriko falls asleep and I never figure out what she would do with her extra arms."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ norikodorm20 = True

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

    stop music

    "The clouds come back on the way home."
    "They feel a little like hands."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label convenience25:
    scene thatonefmkscene1
    with fade
    play music "noriko.mp3"

    "I make my way across town and over to the convenience store because, apparently, I feel like punishing my legs for simply existing."
    "Could I have taken the bus? Yes. But buses are overcrowded with weird people this time of night- and god forbid someone lumps me in with one of them."
    "I’m a totally normal guy with totally normal hobbies and interests."

    if bonus == True:
        "Anyway, here are two [teenager]s who want to have sex with me that I am now going to hang out with."

    s "Hello, normal human [teenager]s."
    n "Hello, normal human teacher."
    ki "Hello, really fucking weird powercouple from like six million years ago."

    scene thatonefmkscene2
    with dissolve

    n "Would it kill you to just go with the flow every once in a while, Kirin?"
    ki "When this flow involves making myself sound like an idiot, yeah. Yeah, I think that would kill me, Noriko."
    s "Sorry, Noriko. It looks like we’ll have to speak normally so Kirin can be included in this conversation."

    scene thatonefmkscene3
    with dissolve

    if bonus == True:
        ki "Hooray! Now I get to hear you two flirt with each other more instead of just going into the bathroom and banging it out like we all know you want to."
        s "I mean, I’m game if Noriko is."
        n "I don’t think you wanna bang one out in the bathroom, Sensei. This is a convenience store in the old district. It probably hasn’t been cleaned in ages."
        s "Isn’t...cleaning it part of your job?"
        n "Probably. But it’s not like I really {i}need{/i} this job, sooooo..."

        scene thatonefmkscene4
        with dissolve

        n "Maybe we could use the walk-in, though?!"
        n "It’s full of drinks and stuff right now, but since most of them are still boxed, it gives us plenty of options for different surfaces to repopulate the planet on."

        scene thatonefmkscene5
        with dissolve

        n "Oh, sorry! Did I say repopulate the planet? What I really meant was to repopulate the planet. No- to repopulate the planet. No, I mean-"
        ki "Seriously, if you’re going to be this horny all the time, just take the fucking plunge."
        ki "Do you have any idea how exhausting it is having to deal with this when losing your virginity is even easier than opening up a pickle jar?"

        scene thatonefmkscene6
        with dissolve

        n "You just have weak hands. Opening a pickle jar really isn't hard."
        ki "Yeah, and neither is getting fucked. So just shut up and screw the teacher already."
        n "You lost your virginity in a love hotel and then cried for hours once you came back to the dorm."
    else:
        n "Maybe. But Kirin is a loser who cried for the entire night after the two of you went bowling together."

    scene thatonefmkscene7
    with dissolve

    ki "I did not {i}cry!{/i}"
    s "You cried?"

    scene thatonefmkscene8
    with dissolve

    ki "No! Are you even listening?!"
    n "Sensei, I know it may not seem all that impressive to you, but I have never in my life struggled when it comes to opening a pickle jar."

    if bonus == False:
        "I don't know why Noriko just decided to tell us that, but I am proud of her regardless."

    s "That’s actually very impressive. Even I’ve struggled with that before."
    n "Well then it looks like you could use a trusty ole’ Noriko around the house full time, huh?"
    ki "Don’t just ignore me! I didn’t cry!"

    scene thatonefmkscene9
    with dissolve

    if bonus == True:
        n "Yes, Kirin. You are very strong and brave and independent and would never cry over something like prematurely giving away your virginity in some random motel you can’t even remember the name of."
        ki "I..."

        scene thatonefmkscene10
        with dissolve

        ki "I...don’t even think it had a name..."
        n "You don’t remember the name of the motel where you deflowered my roommate, do you?"
        s "I don’t like when you ask me questions like that with a smile on your face. And I like it even less knowing there’s probably a knife in your pocket."
        n "How else am I going to defend myself if I get attacked on the way home?"
        n "If anything, I think that {i}all{/i} [teenage]girls should carry knives with them at all times."
        n "Do you have any idea how drastically that would impact the amount of both reported and {i}un{/i}reported sexual assaults?"

        play sound "static.mp3"
        scene yumi14 with flash
        scene mikuthighs25 with flash
        scene lavendersgreen26 with flash
        scene thatonefmkscene10 with flash
        stop sound
    else:
        n "Yes, Kirin. You are very good at bowling and Sensei didn't absolutely destroy you when you two went out together."

    s "Let’s talk about something else."

    if bonus == True:
        ki "Agreed. Something that has absolutely nothing to do with virginity or...knives or whatever."
    else:
        ki "Agreed. Something that has absolutely nothing to do bowling or whatever."

    scene thatonefmkscene11
    with dissolve

    n "Do you want to go hang out outside? The fire’s probably still going."
    s "Fire? In a residential area?"

    scene thatonefmkscene12
    with dissolve

    ki "Are you a cop or something now?"
    n "Residential areas are the best place to start fires."
    n "Besides, it’s safely contained in a trash can. And if there’s anything I’m confident about, it’s starting and maintaining fires."
    s "I don’t really think that’s a good thing to be confident about."

    if bonus == True:
        n "The only thing {i}Kirin’s{/i} confident about is her ability to perform fellatio."
    else:
        n "The only thing {i}Kirin’s{/i} confident about is her ability to tip over cows without getting hurt."

    ki "There are...other things."
    s "Like?"
    ki "..."
    ki "You know."
    ki "Stuff."
    s "Well, I’m glad you’ve found at least {i}one{/i} thing you can be passionate about."

    scene thatonefmkscene13
    with dissolve

    ki "Same."
    n "..."
    n "Uhh..."
    n "I just want to take a second to remind you guys of the poor conditions of the bathroom and suggest that maybe you {i}don’t{/i} look at Sensei that way."
    ki "What way? This is just how I look at Sensei."
    n "Yes, Kirin. That is exactly the problem."

    scene thatonefmkscene14
    with dissolve

    if bonus == True:
        ki "Jesus Christ, Noriko! Just fuck him already! Things would be so much more exciting in this group if you’d just fucking catch up so we can have threesomes and stuff!"
    else:
        ki "Jesus Christ, Noriko! Just fucking tip one over yourself already if you're going to keep getting jealous!"

    n "I will! Soon!"
    s "You will? When?"

    scene thatonefmkscene15
    with dissolve

    n "Woah! It’s suddenly time for my break! Who could have foreseen such an inconvenient ceasefire to a conversation I was definitely prepared to have tonight?!"

    if bonus == True:
        ki "I’m starting to think you secretly have a dick and you’re just afraid to fuck Sensei because he’ll find out about it."
        s "If I were Noriko, I’d be more worried about {i}you{/i} finding out about it."

        scene thatonefmkscene16
        with dissolve

        ki "True. Noriko having a dick would solve virtually all of my problems."
        s "What would Noriko having a penis do for your inferiority complex?"

        scene thatonefmkscene17
        with dissolve

        ki "Ha."
        n "Noriko doesn’t have a penis! And Noriko is going outside to hang out by the fire now!"
        ki "Kirin is following."
        s "And I am refusing to talk in the third person, but I will follow you two regardless as I have nothing else to do and nowhere else to be tonight."
    else:
        s "Kirin. Noriko is a vegetarian. She does not want to harm farm animals the same way you do."

    scene black
    with dissolve2

    "Noriko flips the open sign around and locks the door before leading the two of us through a small store room and into an alleyway."
    "It’s the exact sort of alley you’d expect to see in the worse half of town, filled with trash bags, broken bottles, and rats (Both dead and alive)."
    "And while I’d like to say that I’m surprised Noriko is okay with hanging out around stuff like that..."
    "I’m really not."
    "In fact, I’m {i}not{/i} surprised to say that she doesn’t seem fazed by them at all."
    "And as she steps over the carcass of an animal that was once filled with life, I’m reminded once again of how truly unique and...overwhelmingly strange she is."
    "........."
    "......"
    "..."

    scene thatonefmkscene18
    with dissolve

    n "Oh, sweet! We’re just in time for Nee-chan’s interview!"
    s "Interview?"
    n "She’s appearing on some variety show tonight to promote her next album."
    n "It’s really cool that she still does stuff like this even though it’s gotten to the point where just...slapping her name on something will guarantee it sells out in minutes."
    ki "Noriko, I’ve said this before and I’ll say it again now."
    ki "I want your sister to do things to me."
    n "She’s so pretty, isn’t she?"

    if bonus == True:
        s "You seem weirdly okay with Kirin wanting to have sex with your sister."
        n "Well, I’m weirdly okay with her wanting to have sex with the guy I’m in love with and that is a significantly worse thing to accept."
    else:
        s "You seem weirdly okay with Kirin wanting to hug your sister."
        n "It's just a hug. It's not like it really matters."

    s "Fair point."

    scene thatonefmkscene19
    with dissolve

    if bonus == True:
        n "Besides, when you’re the little sister of a celebrity, you get used to how many people wack off to her."
        n "I had to set all of my social media accounts to private just so people would stop sending me cum tributes of her."
        n "Do you have any idea how many ugly looking dicks there are out there, Sensei? Because it’s a lot."
        s "Thank you for informing me, Noriko. I’m sure this information will be vital at some point."
        ki "Have you really fucked this girl, Sensei?"
    else:
        n "Besides, when you’re the little sister of a celebrity, you get used to how many people want to hug her."
        ki "Have you really hugged this girl, Sensei?"

    scene thatonefmkscene20
    with dissolve

    if bonus == True:
        s "{i}Actually{/i}, Kirin. No. No, I have not."
        ki "You fucked {i}me{/i} before an idol? Cool."
        ki "Seriously, though. Stop waiting. Hurry up and fuck her."
        n "Kirin..."

        scene thatonefmkscene21
        with dissolve

        ki "Oh. Right."
        ki "Yeah, nevermind. Maybe don’t fuck her yet. I don’t know."
    else:
        s "Uhhhhhhhhh maybe?"

    scene thatonefmkscene22
    with dissolve

    tv "Hello and welcome back! If you’re just tuning in now, {i}boy{/i} do we have a surprise for you."
    tv "Joining us today is the one...the only...Niki Nakayama, here to promote her new album, “Watermelon Fantasy!”"
    ni "Hihi! Thank you all so much for inviting me back! It’s been a while since I’ve done anything like this...so I’m really, {i}really{/i} nervous..."
    ni "If any of you are watching at home, I hope you’re cheering me on! It might be hard, but I’ll do my best! Teehee~"
    s "She sounds completely different on television."
    n "That’s just her idol voice. She switches back and forth so easily at this point that it’s kind of absurd."
    tv "So, Niki...Can you tell us a little more about this new album? There’s been a lot of buzz lately about some of the singles being a little more...{i}serious{/i} than what your fans are used to."
    ni "Hmmm...I don’t think any of the songs are any more or less serious than the rest of my music!"
    ni "I’m still the same Niki I’ve always been...and I’m putting just as much heart into my music as I have in the past."
    tv "I’m glad you brought that up! Because it seems like “the past” has been a theme in your music since your debut- but no one really knows anything {i}about{/i} that past."
    ni "..."
    ni "Is there a question there, or...?"
    tv "I was just hoping you’d be able to tell us more about your origins. What was the “old” Niki like? And this...man you’re always talking about in your songs-"
    ni "Completely made up and not real at all. Next question, please."
    tv "O-Oh! Okay then! For my next question, I’d-"
    ni "Oh no! I’m so, so sorry! But I just remembered I have something {i}super{/i} important I have to do back in the studio!"
    tv "If you could just answer this last-"
    ni "Anyway! Thanks for listening, everyone! Make sure to buy Watermelon Fantasy!"
    tv ".................Aaaand, I suppose we’ll be right back after these messages from our sponsors!"

    scene thatonefmkscene23
    with dissolve

    n "Oh, Nee-chan..."
    ki "Is that it? That was the whole interview?"
    n "She gets a little nippy when people ask about stuff from the past."
    n "But, in her defense, one of the stipulations in her contract for appearances like this is avoiding topics that could cause her to talk about it."

    scene thatonefmkscene24
    with dissolve

    n "Idols are supposed to be sort of like...idealized humans. And once that illusion is shattered and people start to realize they’re just...normal girls at heart, their popularity starts to fade."
    n "Nee-chan’s already a lot older than most other idols out there, so she needs to hang on really tightly even if she’s leagues ahead in popularity."
    ki "Huh. You know a lot about that sort of thing, don’t you?"
    n "I’ve been working as an assistant of hers since she started. You just kinda...pick up on stuff after a while."

    scene thatonefmkscene25
    with dissolve

    n "You should tune into one of the streams sometime, Sensei!"
    n "People who donate exorbitant amounts of money can even try to have Niki read their comments out loud! Imagine how she would feel if you were one of those people!"
    s "How exorbitant are we talking here?"
    n "So exorbitant that I probably shouldn’t even say it out loud."

    if chikalust20 == True:
        ki "I think Sensei’s been a little busy making guest appearances on {i}other{/i} streams in order to watch any of Niki’s anyway."

        scene thatonefmkscene26
        with dissolve

        n "Hm? What other streams?"
        s "Yeah, am I supposed to understand what you’re talking about here? Because I don’t."
        ki "So you {i}didn’t{/i} give Chika the go ahead to stream one of your recent sexual encounters?"

        scene thatonefmkscene27
        with dissolve

        n "Uhhhhhhhh what?"
        s "Yeah...{i}what?{/i}"
        ki "During the beach trip. She started live streaming in the middle of the night while I was hanging out with Miku."
        ki "And I’ve heard enough dick sucking in my time on the Internet to recognize it when I hear it."
        s "..."
        n "..."

        "{i}She was recording that?{/i}"
        "I mean, I know she sent me a picture, but..."

        ki "If you’re worried about anyone else seeing or hearing it, I wouldn’t."
        ki "It was a pretty busy night for everyone and I {i}think{/i} it was only Miku and I who caught it before she deleted it."
        ki "And even then, Miku had no idea what was happening."
        ki "So, at least for now, it looks like your secret’s safe with me. And Noriko too, I guess."
        n "I mean...it could have been something else?"
        s "Yeah. It was definitely something else. I have no idea what you’re talking about."
        n "See? Your perverted mind probably just...found something that didn’t exist or whatever because that’s what you wanted to hear."

        scene thatonefmkscene28
        with dissolve

        ki "Then how about we play a little game and see if we can figure out if there {i}is{/i} any more to our lovable teacher’s relationship with Chika."
        n "Game? What kind of game?"

    else:
        n "Oh! And Chika shows up in there sometimes! I’ve definitely seen her name floating around in the chat before."
        n "She {i}really{/i} likes the heart emoji."

        scene thatonefmkscene29
        with dissolve

        if bonus == True:
            ki "She’s probably gotten off to Niki more often than {i}you{/i} have, and chances are she's actually sucked your dick before."
            s "Niki? Or Chika?"

            scene thatonefmkscene30
            with dissolve

            ki "I was {i}referring{/i} to Niki. But if there’s something going on between you and the friendly neighborhood gyaru, I’d be interested in hearing about it."
            ki "At the very least, it would make that possessive little demonstration of hers during the Halloween party make a lot more sense."
            n "..."
            s "I’m not admitting to anything. I just wanted some clarity so I could better understand what you were talking about."
            ki "Reaaaaaaaally?"

            "Obviously not. But I’m not going to come out and say, “Yes. I regularly receive oral sex from the girl who sits next to Noriko,” when Noriko looks like {i}that.{/i}"

            s "Really. Now, let’s move on."
        else:
            s "Oh! I have a fun idea. How about we all talk about our favorite emojis?"

        scene thatonefmkscene28
        with dissolve

        ki "Actually! How about we play a little game instead?"
        n "Game? What kind of game?"

    scene thatonefmkscene31
    with dissolve

    if bonus == True:
        jump fmkx
    else:
        ki "Hopscotch!"
        ki "I drew a bunch of squares with sidewalk chalk while the two of you weren't paying any attention."
        s "I hope you know that I used to be the hopscotch champion back in elementary school."
        ki "Are you challenging me, Sensei?"
        n "What does the winner get?"
        ki "The winner gets to hug Sensei."
        s "But what if I win?"
        ki "You have to hug yourself, obviously."
        s "But that is so lonely..."

        scene black
        with dissolve2
        stop music fadeout 10.0

        "The three of us proceed to play a friendly game of hopscotch, but I am unable to win because Kirin kept throwing cans of soda at me as I was trying to jump."
        "Noriko lost before me, though, since she didn't understand the rules and started treating it like a game of Twister."
        "Fucking amateur."

        ki "Take that, Sensei!"
        s "Kirin the game is over."
        ki "Oh, sorry."

        $ renpy.end_replay()
        $ convenience25 = True
        $ kirin_love += 1
        $ noriko_love += 5
        $ chikakill = True
        $ norikomarry = True

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump kirinspecial25

label norikodate30:
    play sound "phonebeep.wav"
    stop music fadeout 7.0

    "I tap on Noriko’s name in my phone and wait for her to answer. "
    "Should I be calling Niki instead? Probably. "
    "But just because Noriko and I are hot off of a half-scheduled session of dry humping doesn’t mean that I’m calling for sexual purposes only."
    "Even if I’ve been inadvertently given the green light to start looking at her as a woman (Which is {i}kind of{/i} what I’ve been doing anyway), there are other reasons I like being around her."
    "She cares about me, for one. And carries most of the same pros as her sister, but without the ability to emotionally tear me down whenever she wants. "
    "But it mustn’t be forgotten that she’s her own person too. And that’s the one thing she wants me to know more than anything else right now."

    play sound "phonebeep.wav"

    ki "Hello?"

    "Which is why I’m quickly taken aback when it’s Kirin that answers her phone."

    play music "citylife.mp3"

    s "Uhh...hey."
    ki "Hey, Noriko’s busy right now. But I {i}guess{/i} I can talk to you instead if you’re okay with that."
    s "That’s fine, but what is she doing exactly?"
    ki "Eating me out."
    s "Excuse me?"
    ki "Oh, whoops. I mean she’s getting takeout. Didn’t mean to get your dick- err...I mean {i}hopes{/i} up."
    s "You’re coming on a little strong today, Kirin. Are you in a bad mood?"
    ki "Are you implying that my sexual proclivity directly relates to how bad my mood is?"
    s "Kind of."
    ki "...Huh. "
    ki "I guess it does. I don’t think I ever realized that."
    ki "Come blow my back out before she returns?"
    s "I don’t even know where you are right now. Nor was I expecting to see you tonight."
    ki "Wooow, rub your dick against Noriko {i}one{/i} time and suddenly you don’t like me anymore. You’re hurting my feelings."
    s "{i}Two{/i} times, actually. And I still like you just as much as I did the first time you walked into my office and decided to show me your underwear."
    ki "Best decision I’ve ever made. So, you coming or not?"
    s "To have sex with you? Or to hang out and wait for Noriko to get back?"
    ki "Can we not do both?"
    s "Get Noriko to sign off on it and I’m game. Because we both know she’d show up the second we tried anything."
    ki "Jeez, Sensei- did you give her the key to your chastity belt for Christmas or something? "
    s "No. But I’m going to have to hurt her feelings again in the near future and I’d prefer to do that without her having recently walked in on me fucking her roommate."
    ki "Oh god, what the fuck are you going to do to that poor girl now?"
    s "Don’t worry about it. Are you in your dorm room?"
    ki "No. I’ll send you an address. But seriously, Sensei...Noriko’s been through en-"

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I hang up the phone and wait for Kirin to send me the address."
    "A slew of rude text messages reiterating things I already know arrive beforehand."
    "........."
    "......"
    "..."

    scene nightsky
    with dissolve

    "As I move close to the destination on my GPS, I begin to realize that I’ve been around here before- but can’t quite remember when or {i}why.{/i}"
    "But as I round the corner and stare up at a sign glowing so brightly that it cuts the sky in half, I recall everything."

    scene norikokirinhotel1
    with dissolve2

    "And I’m flooded by a tidal wave of questions and concerns that all crash into me simultaneously."

    n "Sensei? What are you doing here?"
    s "Hopefully not interrupting anything."
    ki "We just finished making out. You missed it."
    s "Damn. Looks like you’ll have to do it again."

    scene norikokirinhotel2
    with dissolve

    ki "Hear that, Noriko? We have to make out for Sensei. You’re cool with that, right?"
    n "Kirin, did you know he was coming over here? Why didn’t you tell me?"
    ki "You would have known if you’d remembered your phone when you went out to get food. He called looking for you, after all."

    scene norikokirinhotel3
    with dissolve

    n "You...really?! Hi! What’s up? Are we going on another date? Because I will ditch Kirin right now. She’ll be fine. This is her natural habitat, after all."
    s "Yeah, why exactly are you two hanging out in a love hotel?"
    ki "Because we’re too loud for the dorms and my parents don’t like it when I finger my friends on the couch."
    n "Because I have money to blow on random stuff and it’s super cheap to hang out here. Also, you can take as many condoms as you want and they won’t get mad."
    ki "And Noriko needs those now since you’re going to fuck her brains out soon."

    scene norikokirinhotel4
    with dissolve

    n "Kirin, come on."
    ki "It’s a joke, relax. I know you’d never make Sensei wear a condom."

    scene norikokirinhotel5
    with dissolve

    n "You can ignore her. She got into another fight with her sister today and Kirin always gets really horny whenever she’s mad. And also...surrounded by sex toys. "
    ki "Did everyone know about my anger thing but me?"
    s "It’s a fun quirk and neither of us will hold it against you. "

    scene norikokirinhotel6
    with dissolve

    n "I swear that’s really all that’s going on in here, though! It’s not like Kirin and I are in a secret sexual relationship with one another! The only person who’s ever made me cum is you! So...thank you!"
    n "Thank you for...doing that."
    s "Noriko."
    n "...Yeah?"
    s "Did you just thank me for giving you an orgasm?"

    scene norikokirinhotel7
    with dissolve

    n "Yeah, I mean...that was a...cool thing you did. Really...generous."
    n "I’m gonna shut up now and let Kirin handle the horny. I wasn’t prepared for you to show up here and now my brain is melting."
    ki "Why are you still standing there? Get on the bed with us."
    s "That sentence would sound extremely tempting if it were not for the pizza and bass guitar that would also be joining our threesome."
    n "That would make it a fivesome. Pizzas are people too."
    ki "I think I could make it work with a bass guitar. Pizza, not so much."
    n "I played bass in my underwear once and the vibration felt nice when I sat on my amp, but it was never really enough to make me cum."

    scene norikokirinhotel8
    with dissolve

    ki "You did what?"
    n "Welp, that’s not a thing I meant to vocally announce to the room, but I guess it’s a thing you guys know now. That’s good. That’ll work wonders for my character."
    n "Oh well. I lasted a good two minutes before succumbing to the atmosphere and the...distant moans of girls getting railed."
    ki "I’m a little surprised about the bass, but I feel more or less the same about you after hearing it. I, too, am no stranger to sexually experimenting with different household objects."
    ki "Shout-out to Karin’s hair brush and the arm of my couch."

    if connecttrack == True:
        s "I fucked a watermelon in a dream once, but that’s the weirdest I’ve gotten."
    else:
        s "I don't think I've ever had sex with a household object, but I'd be open to experimenting."

    scene norikokirinhotel9
    with dissolve

    ki "I watched Timothee Chalamet fuck a peach in Call Me By Your Name and it made me feel things. You should try that. That’s what I would do if I had a dick."
    s "I have a feeling you would do a lot of things if you had a dick."
    n "I’d do Kirin just to get her to shut up."

    scene norikokirinhotel10
    with dissolve

    ki "Aww, Noriko! That’s so sweet. I’d say I’d fuck you too, but you’d probably just tell me that space is reserved for Sensei. "
    n "It’s not...{i}not{/i} reserved for Sensei?..."
    s "Okay, I’m going to sit down now before this gets even weirder."

    scene black
    with dissolve2

    "I kick my shoes off at the foot of the bed and slide the bass guitar (Which may or may not be the one Noriko sexually experimented with) to the side before taking my place next to my unofficial little sister."
    "Who is also technically young enough to be my daughter- but will most likely end up as either one more notch in my belt or the single most important figure in my entire life."
    "I haven’t eliminated that possibility yet."

    scene norikokirinhotel11
    with dissolve2

    "But for the meantime, I should focus on carefully navigating through this conversation without giving Kirin an opportunity to ruin it."

    ki "Hey, Sensei, do you remember when you took my virginity on this bed?"

    scene norikokirinhotel12
    with dissolve

    n "That was {i}this{/i} bed?!"

    "I was too slow."

    ki "Mhm! Why do you think I was so dead-set on {i}this{/i} specific room number?"
    n "I just thought you liked the number 23! I didn’t realize it had any special significance in regard to your sex life!"
    ki "Well, it does! And having you sit where the boy you like fucked my brains out is totally turning me on right now."

    scene norikokirinhotel13
    with dissolve

    n "Did you know this too, Sensei? That this was the exact room you banged Kirin in?"
    s "Nope. Could have been any room in here and it wouldn’t have made much of a difference to me."

    scene norikokirinhotel14
    with dissolve

    n "Oh good...that’s a relief. "
    ki "Not for me. Now, I’m just offended."
    s "You didn’t even like it, Kirin. Your entire thing was not wanting it to be special, wasn’t it?"

    scene norikokirinhotel15
    with dissolve

    ki "Well...yeah! But I just happen to have a good memory for stuff like...room numbers. "
    n "I know you cried, but was it really that bad? I know losing your virginity is supposed to hurt and stuff, but I figured it wouldn’t be like, {i}that{/i} horrible."

    scene norikokirinhotel16
    with dissolve

    ki "It was lowkey torture, but probably only because Sensei’s dick is like the size of my forearm."
    n "It did feel pretty huge. Was it hard to get it in? "

    scene norikokirinhotel17
    with dissolve

    ki "I don’t know. Was it hard to fit inside me, Sensei? The actual sex part is all a blur to me since I was on the brink of passing out the whole time."
    s "..."
    s "Is this an actual conversation that I’m taking part in now?"
    ki "Yeah. You’re gonna fuck Noriko soon, right? Wouldn’t it be beneficial for all of us if we were to brief her on what to expect?"
    s "What do {i}you{/i} have to gain from this?"
    ki "Increased threesome probability and a lower chance of Noriko pulling away when my massages start getting a little too sexual. "
    n "Kirin has tried fingering me like three times now and has a very hard time taking no for an answer."
    ki "And Noriko’s tried fingering me {i}zero{/i} times. How unfair is that? Some friend, right?"
    s "You guys are the weirdest fucking dorm room."
    ki "I refuse to believe that when Molly and Tsuneyo are actual human beings who exist."
    s "Kirin’s one thing, but...Noriko, are you really okay just openly talking about all of this?"
    n "Which part? Because I’m already sitting where you deflowered Kirin and things can’t really get any worse than that. But I’m also very close to you and don’t want to move because you smell nice."

    scene norikokirinhotel18
    with dissolve

    ki "Good. Now tell him you want to sit on his lap."
    n "I want to sit on your face."
    ki "Lap. Don’t jump the gun, Noriko."
    n "That’s exactly what I said, Kirin. "
    s "I mean...I guess if-"

    scene norikokirinhotel19
    with dissolve

    ki "Great! It’s settled! Noriko and Sensei will cuddle on the exact spot I lost my virginity and we’ll all live happily and sexually ever after!"

    scene black
    with dissolve

    "Noriko hesitates to move over at first but, with Kirin here, resisting is all but impossible."
    "Especially considering that she literally pushes Noriko at me until I’m forced to adjust my position so that she’s not just knocking me over."
    "........."
    "......"
    "..."

    scene norikokirinhotel20
    with dissolve2

    ki "Aww...look at how cute you two are."
    ki "Now fuck."
    n "Not all of us are cool with losing our virginities in a love hotel, Kirin. If Sensei and I are going to do it, it should be somewhere romantic. Like an airplane. Or an Olive Garden."
    s "Those are extremely specific and strange examples of “romantic.”"
    n "There’s nothing more romantic than unlimited soup, salad, and breadsticks."
    ki "Seriously, though. What’s taking you so long? You got halfway there during Beachmas, didn’t you? Just pull the trigger already. "
    ki "The sooner this lovey-dovey childhood attachment BS turns into daily sex trips to our dorm room, the sooner {i}I{/i} get to finger myself to it."
    ki "Hell, I’ll watch you two go at it right now."
    s "Yeah, we’re both well aware of that."

    scene norikokirinhotel21
    with dissolve

    n "I...don’t really see a need to rush things. "
    ki "Yeah, you’ve only been pining after him for {i}your entire fucking life.{/i} Wouldn’t want to make a move too quickly and scare him off."
    n "I’m sure it sounds weird to you, but I {i}like{/i} how things are now. "
    n "All these scattered moments of...intense intimacy and...the feeling that Sensei and I are {i}actually{/i} growing closer as more than just fake brother and sister are perfect for me."
    n "I wouldn’t have it any other way."
    ki "Boooooooring. Suck his dick."

    scene norikokirinhotel22
    with dissolve

    n "Maybe when we’re alone. "
    n "I do still owe you from the beach."
    s "I mean...I’m not going to turn that down. But there’s something we should probably talk about before-"

    scene norikokirinhotel23
    with dissolve

    ki "What the fuck has {i}talking{/i} ever done for anybody? I don’t get why it has to be so hard for you two to just get naked and go to town on each other right here. "
    n "I’ll admit that it {i}would{/i} be satisfying to overwrite where you lost your virginity since I know Sensei would actually {i}remember{/i} doing it with me."

    scene norikokirinhotel24
    with dissolve

    ki "Hey! He remembers it. He just doesn’t remember the room number. If I was that forgettable, he’d stop messing around with me."
    n "Or he’s just easily bored and you’re always open for business. But once he stays at Hotel Noriko, I’m positive he’ll never check out again."
    ki "Hotel Kirin is good too! "
    n "Yeah, cheap hotels can be really nice when you’re on a budget."

    scene norikokirinhotel25
    with dissolve

    ki "You fucking whore...that was really good."
    ki "But I still bet I can suck a dick better than you."

    scene norikokirinhotel26
    with dissolve

    n "Is Kirin {i}actually{/i} good at- never mind. He looked away. That’s not a good sign for me."
    ki "Hotel Kirin might not be as {i}vacant{/i} as its competitors, but it excels in one area that no one else will ever be able to touch."

    scene norikokirinhotel27
    with dissolve

    n "I don’t have a gag reflex."
    ki "..."
    s "..."
    ki "You’re kidding."
    n "Nope! I can fit a whole banana in my mouth without any problems whatsoever. "

    scene norikokirinhotel28
    with dissolve

    ki "And...{i}why{/i} have you never shown me this?"
    n "I don’t do it anymore since one time when I tried, it broke in half and Niki had to fish it out of my throat."
    n "I thought I was going to die. It was crazy."
    ki "I know I’m supposed to be worried about you or whatever, but now I’m just fantasizing about your sister putting her fingers in my mouth."
    n "It’s not all it's cracked up to be. Her nails are kind of sharp."
    s "I’d like to use this opportunity to once again reiterate that you two are the weirdest fucking dorm room. This is not a normal conversation."
    ki "What’s so abnormal about hanging out in a love hotel, eating pizza, and bonding over how we’re going to be wiener cousins soon?"
    ki "If anyone here is weird it’s {i}you{/i} for not fucking Noriko yet. Like, look at her. She’s one of the most fuckable human beings I’ve ever seen and she’s literally {i}in love{/i} with you. Whatever that means."

    scene norikokirinhotel29
    with dissolve

    n "Again, don’t pay her any mind. You can make love to me whenever you {i}want{/i} to make love to me. Not when Kirin thinks you should."
    ki "If what I wanted actually mattered, Sensei would have bent you over the podium halfway through your introduction and fucked you while Maya was still going crazy. {i}That{/i} would have been hot."
    n "We could have used my tears as lube."
    ki "Noriko, shut the fuck up. That’s like the fourth time tonight you’ve turned something really hot into something really weird in like, one sentence."
    n "Weird can be hot...right, Sensei?"
    s "I don’t know. That banana thing was actually kind of terrifying and didn’t really do anything for me."
    n "At least you don’t have to worry about your dick snapping in half while it’s in my mouth."

    scene norikokirinhotel30
    with dissolve

    n "Unless I bite it, of course..."
    s "..."
    n "..."
    ki "I don’t even have a dick and that one hurt me."

    scene norikokirinhotel31
    with dissolve

    n "I thought threats like that were hot?"
    ki "Uhh..."
    n "Are you seriously telling me that if Sensei pinned you against the wall and put a knife up to your throat, you wouldn’t even get a {i}little{/i} turned on?"
    ki "..."
    ki "Uhhh..."
    ki "Yeah?"
    n "I don’t believe you. "

    scene norikokirinhotel32
    with dissolve

    n "Sensei, you can threaten to kill me any time you want and I-"
    s "Let’s just..."
    s "Leave it at that for today..."

    scene black
    with dissolve2

    "We’re never able to escape the vicious cycle of sexual conversation but, let’s face it, that was never going to happen inside of a love hotel with Kirin."
    "Noriko doesn’t depart from my lap until it comes time for all of us to leave two hours later."
    "But as we make it outside, there’s a brief moment where she stops paying attention to me in order to call her parents...and Kirin seizes that opportunity to confront me about what I said earlier."
    "About how I need to hurt Noriko again."
    "I don’t tell her why or how."
    "But she silently promises to be there for her friend if she needs her."
    "And I silently promise to treat Noriko with the respect she deserves."
    "For living in ignorance may be easier, but it is never as close to scary or threatening as it would be otherwise."
    "She wants to taste all the flavors of life — and I will deliver them to her."
    "Even those I know she’ll hate."

    $ renpy.end_replay()
    $ norikodate30 = True
    $ noriko_love += 1
    $ kirin_love += 1
    stop music fadeout 8.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikodorm30:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "Now that Noriko is (At least presumably) not spending her free time on the bed where I deflowered her roommate, the time has come for me to hoist upon her an inconvenient truth."
    "Or to pretend that I am going to do that only to back out once things become too hard or uncomfortable."
    "Or to find a middle ground that allows me to speak {i}somewhat{/i} seriously to her while still managing to conceal the most important, life-altering bits of information I currently possess."
    "Or to just make out with her and entirely forget and/or disregard that I have serious things to discuss altogether."
    "One of those things is very likely going to happen."

    s "..."

    "But none of them at all will happen if she doesn’t answer the door."

    play sound "knock.mp3"

    s "Noriko, I know you’re in there. I can hear your music."
    n "Hm? Is someone there? I had my headphones on."
    s "Let me in. "
    n "Sensei? Why would you not just open the door? I have literally never locked it before."
    s "Because {i}nice{/i} and {i}considerate{/i} are character traits I have earned throughout my time here and the fact that I am willing to wait outside and not barge in is a subtle nod to my character development."
    s "Or at least it {i}was{/i} before you went and ruined everything."
    n "I have no idea what you’re talking about, but you’re welcome to come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Thanks. Was that so hard?"

    scene norikoknows1
    with dissolve2

    n "The hardest part of all was just realizing you were at the door. If it weren’t for every Charles Bronson song being nine seconds long, I would have never even noticed."
    s "That is not enough time for a song."

    scene norikoknows2
    with dissolve

    n "Tell that to the entirety of the powerviolence genre. So, what brings you here today? Ready to pick up where we left off on the beach?"
    s "Are {i}you{/i} ready to pick up where we left on the beach?"

    scene norikoknows3
    with dissolve

    n "Of course. I would have had sex with you right then and there if it weren’t for your incessant desire to always make Maya happier than you make me."
    n "And if that sounded passive aggressive, it’s because it was."
    n "But thank you again for the orgasm."
    s "Okay, I think we need to talk."

    scene norikoknows4
    with dissolve

    n "Is it going to be a good talk or a bad talk? Because Kirin’s been really nice to me ever since the love hotel and it’s been putting me on edge."
    s "It’s a talk about...the past, present, and future. I’m going to have one with Maya soon too. And I just had one with your sister the other day."
    n "Isn’t it a little too early for your midlife crisis, Sensei? Because it’s either that or you’re about to go all “Big Fish” on me and I’m not in the mood to cry today."
    s "You’re probably going to cry today."

    scene norikoknows5
    with dissolve

    n "Damn it! This was supposed to be my good luck band! I wore my nice underwear and everything!"

    scene norikoknows6
    with dissolve

    n "Which isn’t to say that all of my underwear isn’t nice. It is. And you’re free to help yourself to another pair whenever you like if the one I gave you earlier is starting to get worn down by all the friction."
    s "Noriko, take a seat."
    n "If you’re about to Chris Hansen me...I swear to god, Sensei. Which doesn’t mean much considering I’m neither religious nor a child predator, but still."
    s "Just sit down. There are a few things I want to talk about and it...might wind up taking a little while."

    scene black
    with dissolve2

    "Noriko sighs, removing her headphones and placing them down on the kotatsu before hopping onto the bed and pulling her knees up to her chest."

    scene norikoknows7
    with dissolve2

    "She stares at the wall for a moment, somehow managing to keep a smile plastered to her face despite the obvious red flags that both Kirin and I have been waving in front of her."
    "And while I’m more or less settled on the fact that I am going to tell her about what happened between Niki and me the other day, there’s something I need to bring up first."
    "Especially since, as of right now, the only people I have confirmed to actually know my name are Niki and {i}Otoha.{/i} And Otoha being on that list is extremely strange to me."
    "If I can confirm Noriko is on it as well, it will at least make me feel a little bit better."
    "And that I may also be subconsciously favoring the second floor as I haven’t bothered confirming that information with any of my original students yet."

    n "Okay...hit me."
    s "I didn’t realize you were into that."
    n "You totally know I’m into that."
    s "You’re right, I do. But before we deep dive into any more of your fetishes, there’s something I need to know. "

    scene norikoknows8
    with dissolve

    n "My heart is an open book with a frayed spine. If it’s something I know, it won’t be hard for you to find out."
    s "Do you know my name?"

    scene norikoknows9
    with dissolve
    stop music fadeout 15.0

    n "Your name?"
    n "Of course. It would be weird if I didn’t."
    s "Then...why have you kept calling me Sensei this whole time?"
    n "I...haven’t? "
    n "Like, yeah...I call you that more than anything else since I figured reinforcing the faux power dynamic your title creates would tempt you more, but I’ve called you by your regular name a bunch of times. "
    n "Do you really not remember?"
    s "Uhh...no?"
    n "Would it help you if I said it now?"
    s "It might. But I’m sorry in advance if I wind up tackling you or drooling on your blanket as a result of that."

    scene norikoknows10
    with dissolve
    play music "kimitoakinobouken.mp3"

    n "Akira Arakawa — thirty-one years old. Lifelong friend and the first love of my life. "
    n "Ex-boyfriend of Niki Nakayama. My surrogate brother and future {i}daddy{/i} if all goes according to plan."
    s "Okay. You can stop right-"
    n "A man who’s been put through the wringer and still manages to get out of bed every morning and pretend he’s not all broken up inside."
    n "He might be a bit of a pervert. And he might be sleeping with a bunch of teenage girls. But beneath the ephebophilia and blank stare, he’s actually a really great guy."
    n "Or {i}can{/i} be, but just decides not to be most of the time because he’s afraid of people liking him more than he thinks he deserves."
    n "Hobbies include long walks on the beach and talking to plants."
    s "Now you’re just making things up."
    n "Are you testing me or something? Why was I suddenly quizzed on the same name I’ve been scribbling next to mine in notebooks ever since I learned how to write?"
    s "Because I finally remembered it. Or...was {i}told{/i} it?"

    scene norikoknows11
    with dissolve

    n "You didn’t even remember your name?..."
    s "Nope."
    n "But...what about your bills? Or ID? Or credit cards? Or...what about Ami? She doesn’t call you Sensei while you guys are alone at home, does she?"
    s "She does, and I have no idea where my ID even is. All of my mail just has my last name on it."
    n "That makes...basically no sense at all. Are you sure you’re not just...overlooking it? Like how you apparently were all of the times {i}I’ve{/i} called you Akira?"
    s "That wouldn’t-"
    n "It would make more sense than thinking every document that’s ever been sent to your house just says “Arakawa” on it, wouldn’t it?"
    s "Hey, I don’t know how Kumon-mi handles mail. For all I know, that’s normal here."
    n "What about Nee-chan? Surely she’s been calling you Akira this whole time. That’s how we always refer to you when we talk, and we talk about you {i}a lot.{/i}"
    s "She’s actually the one I first heard it from. "
    n "When?"
    s "Well...when was the last time you saw her?"
    n "Not since right before Christmas. I think she’s still kind of mad at me for skipping out on her holiday concert this year. "
    s "Well, it was sometime after that. "
    n "Have you seriously been just living without a name this whole time? Wasn’t that a little...I don’t know, dehumanizing? "
    n "If I was just suddenly “Girl” and everyone only called me “Girl” I’d probably lose myself entirely."
    s "What you have to realize is that I’ve been “Sensei” this whole time. It’s the first thing I heard when I woke up and it’s what everyone’s come to know me as."
    s "{i}That{/i} has always been my name as far as I’m concerned. Which is why it’s so strange and unsettling for me to finally have a real one."
    n "..."
    s "Noriko?"
    n "I’m sorry, I just don’t really understand. Why is it just {i}now{/i} dawning on you that you’re an actual person? "
    n "What happened with Nee-chan that helped you remember? She must have done something, right?"
    s "That’s...the main thing I wanted to talk about today. "

    scene norikoknows12
    with dissolve

    n "Oh...no. No..."
    n "I don’t like that opening, Sen...Akira. "
    s "At least you get to find out from me directly rather than her this time."
    n "Can’t we just say I aced the name quiz and have a celebratory make out session? You know, {i}without{/i} breaking my heart again?"
    s "Something did happen between your sister and me."
    n "Sensei-"
    s "She helped me remember how important the two of you are."
    s "She helped me remember that you’ve been there from the beginning and that, unless something’s different with {i}you,{/i} you’ll both be there until the very end."
    s "That I can always count on the two of you to stay by my side and that, even if I don’t remember how things were back then, I did something horrible by abandoning you."
    s "You’re not the only one here who’s a work in progress, Noriko. And that’s painful to admit since I’m twice your age...but I’m doing that now."
    s "I want you and your sister to play more important roles in my life...and I want to go back to however things were in the past before any of this existed to either one of us."
    s "But time won’t turn back that far, so I’m stuck here and now and...need to start again. And I want you there for that. I want you there to see {i}Akira{/i} and not {i}Sensei.{/i}"
    n "I’ve seen Akira this whole time...Sensei is who {i}you{/i} saw..."
    s "In order to keep you close, though...I have to hurt you again. "
    s "It probably won’t be the last time, but seeing as you’ve already been through enough pain because of me, the least I can do is be honest this time around."
    n "..."
    s "I had sex with your sister."
    s "I love her."
    n "..."
    s "..."
    s "Nori-"

    scene norikoknows13
    with hpunch

    n "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK!!!!"
    n "DAMN IT!!!!"
    s "Uhh..."
    n "I KNEW THIS WAS GOING TO HAPPEN! GOD FORBID I EVER WIN AT ANYTHING WHEN SHE EXISTS! AND JUST WHEN I THOUGHT I FINALLY HAD A LEG UP!"
    s "Okay, good. Let it all out."

    scene norikoknows14
    with dissolve

    n "That’s basically everything."
    s "There’s no way that’s “basically everything.” You cried hysterically when you found out I fingered her. "
    n "And I’ll probably cry today when you leave the room. But right now, I’m just pissed off at myself for letting you leave that night on the beach when it could have been me instead."
    n "Because not only did you have sex with my sister before me, but you also got to hear your {i}name{/i} from her and that seems like a huge deal if everything you said earlier is true."
    s "It was a big deal. And it’s right for you to be mad at me."

    scene norikoknows15
    with dissolve

    n "Listen, I’m obviously pissed off, but it’s not at you, okay?!"
    s "It’s not?"
    n "No! Of course not! I’m super happy for both you {i}and{/i} Nee-chan! My frustration isn’t some kind of protest to that!"
    n "You two have been in love with each other my whole life! It’s amazing that you finally took things to the next level after all this time and I’m really glad things are working out!"

    scene norikoknows16
    with dissolve

    n "I just got my hopes up a little too much...you know...that it would be {i}me{/i} instead. But I’m one step behind like always and there’s nothing left for me to do but once again chase after both of you."
    s "You won’t have to chase me far. I’ve learned my lesson when it comes to putting too much space between us."

    scene norikoknows17
    with dissolve

    n "You say that, but I still don’t know what this means for you and me."
    n "Things were finally starting to move forward and now there’s no reason for you to even come at me anymore. What am I supposed to do?"
    s "You don’t have to do anything. I’m still going to “come at you.”"
    n "But...Nee-chan-"
    s "Will love me no matter what I do. And, as fucked up as it sounds, I’m sure she’ll understand if things continue progressing for you and me as well."

    scene norikoknows18
    with dissolve

    n "Maybe for you. Nee-chan would get pissy whenever I even tried her clothes on. I don’t want to imagine what she’ll do to me if I have sex with her boyfriend."
    s "I mean...it’s not like we have to {i}tell{/i} her?"
    n "Does she not deserve the same level of honesty that I do? "
    n "Why do I have to be the one to hear about the other end of your relationships while she gets to keep living in her own little world? That’s not fair at all."
    s "Because I think you can take it...and, I think it’ll help you grow up."
    s "Niki’s a special case. I know that you both spent years looking for me, but she’s-"
    n "Mentally incapable of ever moving past you?"
    s "Exactly."
    n "And you think I {i}am?{/i}"
    s "I do."
    s "And I think you {i}should.{/i}"
    s "There are tons of people out there better suited to you than I am. "
    s "You’re a borderline-genius who excels at basically everything you try to do...and you have an extremely bright future ahead of you if you just keep applying yourself."
    s "All I can do is hold you back."
    n "My future doesn’t matter if you’re not in it, Akira."
    s "It does, though. "
    s "Niki and I both have a lot of faith in you and just want you to...find all the pieces of yourself so you can be even more amazing one day."
    n "Stop talking like you two are married already. It’s making me jealous."
    s "Noriko, if you want things to keep moving further for us, I’ll make it happen. But it’s only going to hurt you more and I feel like that’s all I ever do with you now."

    scene norikoknows19
    with dissolve

    n "If you knew even half of what you actually do for me, there’s no way you’d be saying that."
    n "The reason I made it as far as I’ve had is in no small part to all the help you’ve given me...and how motivated it made me to succeed just so I could have a shot with you one day."
    n "If that shot is still there, I want to take it."
    n "I want to kiss you in your office. "
    n "I want to suck your dick in a bathroom stall. "
    n "I want to get fingered on a school bus...fuck you on a table somewhere. "
    n "I want to finish growing up with you because you’re the main reason I decided to grow up in the first place."
    n "If you’re telling me that’s not possible...and that you refuse to ever look at me as anything other than Niki’s sister...fine. I’ll try moving on. I’ll absolutely suck at it, but I’ll try."
    n "But...if you’re telling me that the only thing preventing that from happening is your “desire for me to live a more fulfilling life” or how “you don’t want to hurt me,” you can fuck right off."
    n "The one who chooses where my life leads is me. Letting you make decisions like that {i}for{/i} me just means I’ve given up. "
    s "So...you’re saying-"
    n "I’m saying that if there are going to be mistakes I make in life, which I know there will be..."
    n "I want one of those mistakes to be you."
    n "As soon as possible..."
    n "Before you and Nee-chan get even further away..."
    s "..."
    n "..."
    s "The next time I invite you over to my house, I’ll try to talk you out of this one more time."
    s "If you refuse me again then..."
    s "We can change things once and for all."
    s "And I can cement myself as the single greatest regret you will ever have."
    n "Show me the dotted line and I’ll sign it. "
    n "I’m sure it means nothing after whatever you went through with Nee-chan, but I love you just as much as she does."
    n "I’ll never regret you no matter how much you think I should."
    s "Okay..."
    n "Okay..."
    s "..."
    n "..."
    s "I should probably leave. That was a good note to end things on."
    n "Okay. Holding back the tears has gotten pretty tough anyway and I’d like to let the dam burst now."
    s "I’ll call you soon."
    n "I’ll be waiting."

    scene black
    with dissolve2

    s "I’ll start preparing my speech when I get home."
    s "Goodnight, Noriko."
    n "Goodnight..."
    n "Akira."

    play sound "dooropen.mp3"
    stop music fadeout 10.0

    "I leave the room and move further away from the comfort it provides-"
    "But make it one step closer to a life so full of missteps that we’ll all be moving backwards."

    $ renpy.end_replay()
    $ norikodorm30 = True
    $ noriko_love += 1

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikoinvite3:
    if amifingered == True:
        stop music
        scene picturepicture
        play music "moyo.mp3"

        $ norikoinv3q1 = renpy.input("type the word dirt to help summon the old one")
        $ norikoinv3q1 = norikoinv3q1.strip()

        if not norikoinv3q1.lower() in ["dirt"]:
            scene black
            "event failed."
            $ norikoinvite3skip = True
            $ norikoinvite4skip = True

            if day >= 6:
                jump endofsat
            else:
                jump endofweekday

        $ norikoinv3q2 = renpy.input("cool now do it again but this time type it backwards")
        $ norikoinv3q2 = norikoinv3q2.strip()

        if not norikoinv3q2.lower() in ["trid"]:
            scene black
            "event failed."
            $ norikoinvite3skip = True
            $ norikoinvite4skip = True

            if day >= 6:
                jump endofsat
            else:
                jump endofweekday

        $ norikoinv3q3 = renpy.input("okay one more time but this time instead of saying dirt type user 1 more like loser 1")
        $ norikoinv3q3 = norikoinv3q3.strip()

        if not norikoinv3q3.lower() in ["user 1 more like loser 1"]:
            scene black
            "event failed."
            $ norikoinvite3skip = True
            $ norikoinvite4skip = True

            if day >= 6:
                jump endofsat
            else:
                jump endofweekday

    stop music
    scene noonsky
    play sound "phonebeep.wav"

    "I tap on Noriko’s name in my phone and wait for her to come have sex with me."

    play sound "phonebeep.wav"

    n "Hey! Hi! Hello!"
    n "Is, uhh..."
    n "Is it time?"
    s "Noriko, I would like you to come to my house now."
    n "Oh man. Okay. Okay, yeah. I’ll head over right now. "
    n "Ami’s not home, right? Did you double check her bedroom? The cupboards? Bathroom? She’s tiny. She can fit in places we probably don’t even know about."
    s "Ami’s busy today. She told me this morning."
    n "Okay. I just got out of the shower but I’ll take another shower just because. And then another when I get to your house if that’s cool."
    s "Stop freaking out and just come over. Everything’s going to be fine."
    s "Unless you’ve had a change of heart, that is."
    n "If I had a change of heart do you really think I’d want to take three showers in one day?"
    s "Maybe. The shattering of a heart does sound like it could get a little messy."
    n "You have no idea."
    n "Anyway, yeah. I’m coming. Like, arriving. I’m not even thinking about sex right now. I promise."
    s "I’m going to hang up the phone now, Noriko."
    n "Not if I hang up first!"

    play sound "phonebeep.wav"

    "Noriko’s schoolgirl excitement (Which has come to mean “excitement directly related to engaging in sexual activities with an adult” in my unofficial dictionary) gets the better of her and she hangs up."
    "But I would have hung up first if given the opportunity."
    "I don’t want her to know how much I want it."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "."

    scene norikotime1
    with dissolve2
    play music "acoustic.mp3"
    $ renpy.pause(10, hard=True)

    "Let’s get this bread."

    play sound "knock.mp3"

    "[[LOUD KNOCKING]"
    "Oh joy, that must be Noriko."

    s "Come in!"

    play sound "dooropen.mp3"
    scene norikotime2 with dissolve
    play sound "cheer1.mp3"

    n "Hey! It’s me! Ready to unsuccessfully talk me out of turning my mostly-wholesome relationship with you into one filled with uninhibited lust?"
    s "..."
    n "..."
    n "Akira?"

    play sound "static.mp3"
    scene nikilovesyou37 with flash
    scene norikotime3 with flash
    stop sound

    s "Huh? What?"
    s "Noriko? When did you get here?"
    n "Just...a few seconds ago. You doing okay? You’re paler than normal and...it only took you one line to zone out."
    s "Yeah, I think I’m good now. Probably just another brain thing. I wouldn’t pay it any mind."
    n "I mean, if you’re sure...okay. But if you think you have to push yourself, we can just do this some other time. "
    n "Waiting at this point is really only prolonging the release of the horny anyway since I’ve already lost out to Nee-chan in the virginity battle."
    s "True, but if we’re going by ages, you beat her by a mile."

    scene norikotime4
    with dissolve

    n "Thanks! That’s encouraging, taboo {i}and{/i} hot! "
    n "Anyway, if you’re sure you’re good to go, take me into your room and make a fucking woman out of me already. I’ve waited long enough."
    s "Can I at least have one last chance to give you a speech meant to push you in the opposite direction?"

    scene norikotime5
    with dissolve

    n "Fine. Go ahead."
    s "Thanks. Noriko-"
    n "I can make my own decisions and my decision today is to start a sexual relationship with my sister’s ex-slash-current-boyfriend-slash-teacher-slash-brother."
    n "But I humbly beseech him to finger me first since he neglected to do that with my roommate and she had trouble walking the next day."
    s "Are you absolutely positive?"
    n "Yeah, I saw it myself. You really did a number on her."
    s "About the {i}sex,{/i} Noriko."

    scene norikotime6
    with dissolve

    n "Sensei-"
    s "Stick with Akira when no one else is around. "
    n "Then, {i}Akira,{/i} I appreciate how concerned you are for my well-being and {i}love{/i} that you’re being a little more sentimental all of a sudden...but I’m fine."
    n "I want to do this. "
    n "I thought more about what you said after you left that night...about how you’ll only hold me back and that I can do better and all that stuff...and do you know what I did?"
    s "Probably masturbated. Seems like a Noriko move."
    n "No. I almost called you myself. {i}That{/i} is how sure I was of my decision. But I decided to be good and wait for you to call me instead as I have realized I come on way too strong way too often."
    s "{i}Then{/i} you masturbated."
    n "Nuh-uh. I’ve been holding it in and waiting for you. "
    n "But now the time has come and, for some reason, we’re still in your living room. Would you mind telling me why?"
    s "Guilt, maybe?"
    n "For boning my sister right before me?"
    s "For making you wait this long for something you very obviously want."

    scene norikotime7
    with dissolve

    n "God, I’m gonna cum so fucking hard for you..."

    scene black
    with dissolve2

    "Well, after much delay, the time has finally come for me to convert Noriko from the [[much] younger girl next door to one more cornerstone in this life of many angles."
    "I take her hand and lead her into my room, where the only light we have is what little has found its way to the window, and lay her down on my bed."
    "She keeps her clothes on — probably because she wants me to remove them myself, and I take up residence beside her."

    scene norikotime8
    with dissolve

    "She stares into my eyes as my hand finds its way to her skirt, lifting it up ever so slightly and allowing the cool air of my room to assault her lower body."
    "She trembles as this happens and her breathing becomes more audible than it already was."
    "I think to myself as I look back at her that she might climax any second. And I wouldn’t be surprised if she did the moment I came into contact with her."
    "All it took at the beach was a minute or two of grinding up against me. Who knows what will happen once I’m actually playing with her?"

    n "Akira..."
    s "Yeah?"
    n "Huh?...Oh...Nothing..."
    n "I just like saying your name..."
    n "Is that okay?..."
    s "You can say it as much as you want."
    s "I can hear it now."

    scene norikotime9
    with dissolve

    n "Nn, fuck...this is better than I dreamed and you haven’t even started yet."
    s "I’m about to. Are you-"
    n "Yes...A million times yes...Play with me, Daddy..."

    scene norikotime10
    with dissolve

    n "Hah! Nnf...fuck!"
    s "Nice. I didn’t even have to {i}ask{/i} you to call me that."
    n "Oh, fuck...I...hah...wasn’t even doing that for you...I just...aaah...it turns me on...so...so much..."
    s "I’m surprised you didn’t go for the Onii-chan angle. I remember that one really got to you for a little while."

    scene norikotime11
    with dissolve

    n "Ahh...haaaah! They’re all...good! I’ll...call you...whatever you want me to!"
    s "You know what? Stick with Onii-chan. It’ll be nice to commemorate this occasion since you’re pretty much graduating as my little sister right now."

    scene norikotime12
    with dissolve

    n "Don’t...hah...say that...I’ll always be your little sister...Onii...chan~"
    s "Even though we’re like this now?"
    n "Only Onii-chan...gets to play with my pussy..."
    n "I just wish he’d...play a little harder..."
    n "I’m a big girl now...I can take it..."
    s "You’re pretty good at this roleplay thing for a complete beginner."
    n "Oh please...do you have...hah...any idea how many times...I’ve played this out in my head?..."

    scene norikotime13
    with dissolve

    n "Aah, fuck! Oh god! Just take my fucking underwear off already! I want you inside me!"
    s "Is that any way to talk to your older brother, Noriko?"
    n "Hah! Hah! Onii-chan! Please...finger me directly! I want to feel more of you! I want to cum with...Onii-chan inside!"
    s "Pull your shirt down, Noriko."

    scene norikotime14
    with dissolve

    n "Oh...ngh...like that, Onii-chan? You like seeing how much I’ve grown? You like your little sister’s tight...fucking pussy? Yeah?..."
    n "What if Mom and Dad find out?...What if they separate us?...Will you be able to live without me?...Because I can’t live without you...Onii-chan!"
    s "Alright, Noriko. Pull the brakes a little."

    scene norikotime15
    with dissolve

    n "Ohhh fuck! Fuck, fuck, fuck! If your fingers are...filling me up I...have {i}no{/i} idea how you’re going to get your cock in me...Onii-chan!"
    s "I’m sure we can figure it out. Are you close to cumming?"
    n "I’ve been close this...whole fucking time..."
    n "It’s taking everything I have to...not give in! "
    s "What are you waiting for? The sooner you finish, the soon I get to fuck your brains out. That’s what you want, isn’t it?"
    n "I want everything! Your fingers! Your tongue! Your big...fucking dick! "
    n "Make me cum...every single way! You owe me! You kept me waiting...so fucking long! Onii-chan! Onii-chan!"
    s "Your wish is my-"

    stop music
    play sound "knock.mp3"
    scene norikotime16
    with hpunch

    "[[LOUD KNOCKING]"

    n "..."
    s "..."
    n "{i}Did...you lock the door?...{/i}"
    s "{i}I...don’t think I did...{/i}"

    play sound "knock.mp3"
    scene norikotime17
    with dissolve

    n "{i}I can go out the window. I brought my shoes into your room this time. No one knows I’m here.{/i}"
    s "{i}The window doesn’t open.{/i}"
    n "{i}What do you mean the window doesn’t open?!{/i}"
    s "{i}I mean it’s stuck shut, Noriko. {/i}"

    play sound "knock.mp3"

    a "Senseiiiiii! I know you’re in there! But I’m a good girl so I won’t open the door without permission!"
    n "{i}Well, then what are we supposed to do?! She’s not going to go away!{/i}"

    play sound "knock.mp3"

    a "Give me permission please!"

    scene norikotime18
    with dissolve
    play sound "knock.mp3"

    s "{i}The...closet. Hide in the closet.{/i}"

    play sound "knock.mp3"

    n "{i}Closet! Yeah! Good idea!{/i}"

    scene black
    with dissolve
    play sound "knock.mp3"

    "Noriko gets up as quietly as she can and tiptoes her way over to the closet."
    play sound "knock.mp3"
    "Ami continues knocking."
    play sound "knock.mp3"
    "I can’t even get a thought out-"
    play sound "knock.mp3"
    "Without being reminded of whose home this is."
    play sound "knock.mp3"

    scene norikotime19
    with dissolve2
    play sound "knock.mp3"

    s "..."

    play sound "knock.mp3"

    s "..."

    play sound "knock.mp3"

    s "..."

    play sound "knock.mp3"

    s "You...can come in."

    scene norikotime20 with dissolve
    play sound "dooropen.mp3"

    a "Thanks!"
    a "You know, you should probably answer the door after {i}one{/i} knock next time. "
    a "Waiting so long will make me feel like you’re up to something."
    s "..."

    scene norikotime21
    with dissolve

    a "Are you up to something, Sensei?"
    s "I was just taking a nap."
    a "Were you?"
    a "Because it sounded like a very exciting nap."
    s "..."
    a "Well?"
    s "Fine...You got me. I was watching porn on my phone."
    a "Show me."
    s "What? No."
    a "Why not?"
    s "Because I don’t have to. That’s why."
    a "Are you lying to me, Sensei?"
    s "Ami-"
    a "There’s a girl in here, isn’t there?"
    s "No one is here other than you."

    scene norikotime22
    with dissolve

    a "Really? That’s great news! "

    play sound "static.mp3"
    scene norikotime23 with flash
    stop sound

    a "Then you won’t mind if I have a look around."
    s "You don’t-"

    play sound "static.mp3"
    scene norikotime24 with flash
    stop sound
    play music "amiawake.mp3"

    a "Hmm...now, where should I start?"
    a "There are so many places to hide a girl in here that I don’t even know where to begin my search! How crazy is that?"
    s "Ami, you’re being ridiculous. "
    a "Am I? Because it wouldn’t be the {i}first{/i} time you brought someone here without my knowledge."
    a "Or the second. Or the third. Or the fourth."
    a "For all I know, you could be doing this every single day and I’d have no idea at all!"
    a "Of course, I’m sure you’re {i}not{/i} because you love me so much, but it doesn’t hurt to check, you know?"
    s "Ami, come on. You’re creeping me out."

    scene norikotime25
    with dissolve

    a "If I were Sensei, where would {i}I{/i} hide a girl? "
    a "Or, better question, where would one {i}be able{/i} to hide on such short notice? Like when the girl who {i}takes care of this house{/i} returns home?"
    a "Could she be in the walls? Is there a secret compartment somewhere Sensei knows about that {i}I{/i} don’t?"

    scene norikotime26
    with dissolve

    a "Could she be...under his blanket?"
    a "No...it looks like that area is clear."
    a "Hmm...this is a real pickle, isn't it?"

    play sound "static.mp3"
    scene norikotime27 with flash
    stop sound

    a "It’s almost like I’m not meant to find her."
    s "Okay. That’s enough. Go to your-"
    a "I’m not done looking, Sensei. You can’t punish me until I make sure you’re safe."

    play sound "static.mp3"
    scene norikotime28 with flash
    stop sound

    a "I know that other girls can be tempting, but you need to remember that {i}I’m{/i} the only one who knows how to take care of you and all of {i}them{/i} just want to hurt you. "
    a "Family needs to stick together, don’t they? You’re all I have. {i}And{/i} you're my guardian. You have a responsibility to make sure I stay happy, right?"
    a "Just like how I have a responsibility to make sure that no one ever does anything that might harm the most important person in my whole entire world!"
    s "Ami-"
    a "Oh! I just remembered a place I haven’t checked yet!"

    play sound "static.mp3"
    scene norikotime29 with flash
    stop sound

    a "I know we use your closet for storage, but I wonder if there's still enough room inside to hide a body."
    a "Maya’s small. I bet {i}she{/i} could fit."
    a "But would Maya {i}really{/i} betray me by spending time with my uncle when she knows she’s {i}not allowed?{/i}"
    s "There’s no one in the closet, Ami. There’s no one {i}anywhere.{/i}"
    s "It’s just me."
    a "Do you really expect me to believe that?"
    s "Yes...I do."

    play sound "static.mp3"
    scene norikotime30 with flash
    stop sound

    a "Do you think I’m gullible, Sensei?"

    play sound "static.mp3"
    scene norikotime31 with flash
    stop sound

    a "Do you think I’ll believe {i}anything{/i} you say just because I’m madly in love with you?"
    a "Because everyone has limits. And I apologize if I’m misunderstanding something here, but it seems to me like you’re trying to {i}test{/i} mine."
    s "I’m not trying to do anything...I was just taking a nap."

    if amifingered == False:
        a "Then what was that noise?"
        a "Which fucking whore did you invite into {i}my{/i} house and stash in {i}my{/i} closet?"
        s "No one..."
        a "Do you promise?"
        s "..."
        a "I asked you-"
        s "Yes. I promise."
        a "Can you promise to never hide {i}anything{/i} from me?"
        s "..."
        a "Can you?"
        s "..."
        s "Yes..."

        scene norikotime32
        with dissolve

        a "Good. That makes me a little more comfortable."
        a "But, Sensei...just so you know..."
        a "If you {i}break{/i} that promise?.."
        a "I’m going to {i}make sure{/i} that no one else can ever hurt you. "
        a "Okay?"
        s "..."

        scene norikotime33
        with dissolve

        a "Great! I’m glad we’re on the same page!"
        a "On another note, what would you like for dinner tonight? I was thinking of making hamburger steak."
        s "That...sounds fine. "
        a "I’ll get started right away."
        a "I love you!"
        s "..."
        a "I said {i}I love you!{/i}"

        scene black
        with dissolve

        s "I love you too, Ami..."

        "........."
        "......"
        "..."

        play sound "slidedoor.mp3"
        scene norikotime34
        with dissolve2

        n "{i}What the fuck was that?! Since when does Ami act that way?!{/i}"
        s "{i}That’s...new. She’s not normally like that.{/i}"
        n "{i}What did she mean, “Make sure no one else can ever hurt you?” How am I trying to hurt you?! I’d never-{/i}"
        s "{i}I don’t know, but you need to get out of here.{/i}"
        n "{i}How?! She’s making dinner and your window is apparently stuck shut?! What am I supposed to do?!{/i}"
        s "{i}I’ll...think of a way to distract her. Just wait until you hear us go into her room and get out.{/i}"
        n "{i}Akira, this is totally fucking weird. That was a level of possessiveness that transcends what is socially acceptable by like, a billion. I’m seriously worried.{/i}"
        s "{i}I can handle her just fine. But I want you to get out of here before you get roped into one more thing you’re not meant to be a part of.{/i}"
        n "{i}Akira! Wait!{/i}"

        scene black
        with dissolve2
        play sound "dooropen.mp3"

        s "Ami...can I talk to you in your room for a minute?"
        a "My room? Why? Have to give your prisoner some time to escape?"
        s "..."
        a "Oh my God, Sensei! I was only kidding! Of course we can talk in my room! "
        a "{i}I’ve actually been wanting to show you this thing I drew the other day. {size=-10}It’s...{/i}"

        "Noriko manages to make it out of the house without being detected."
        "I sleep in Ami’s bed that night."

        $ renpy.end_replay()
        $ norikoinvite3 = True
        $ norikoinvite3skip = False
        $ norikoinvite4skip = True
        $ ami_love += 10

        "{i}Ami’s affection has increased by 10!{/i}"
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

    else:
        scene norikotime35
        with dissolve

        a "Didn't you say you were watching porn?"
        s "..."
        a "A nap? Or porn? Which one is it, Sensei? You should at least stick to one story if you want to trick me."
        s "I...was trying to take a nap. But then I couldn’t fall asleep and started watching porn instead. There you go. Open and shut."
        a "Did you finish?"
        s "Ami-"
        a "Where did you cum? Show me."
        s "..."

        scene norikotime36
        with dissolve

        a "Oh no! I interrupted you {i}before{/i} you finished, didn’t I?!"
        a "That’s not good, Sensei! You have to release all of that pent up energy or you’ll be grumpy all day tomorrow!"
        s "Ami-"

        scene norikotime37
        with dissolve

        a "Never fear, though! Thankfully, you have a niece who also functions as your own personal cum dump! I’ll suck that energy out of you in no time at all! Leave it to me!"
        s "I don’t want-"

        scene norikotime38
        with dissolve

        a "What’s wrong, Sensei? It’s not like we haven’t done this a million times before."
        a "It’s not like you haven’t fucked me already. Or shot your hot cum down the back of my throat. Or played with my pretty pink pussy until it was swollen."
        a "I really don’t see what the problem is...unless there’s someone else in here that you don't want to-"
        s "Fine. Just..."

        scene black
        with dissolve2

        s "Just...be quick about it."
        a "Heheh..."
        a "{i}We’ll see...{/i}"

        "For a moment, I attempt to trick myself into believing in God."
        "In doing so, I pray that Noriko closes her eyes."
        "I pray that she blocks out the noise."
        "And that this nightmare ends before a beautiful day is butchered in front of me."

        play sound "zipper.mp3"

        "As Ami’s hands find their way to my zipper, I see the closet door crack open before quickly sliding back shut."
        "And I remember why it is that I never pray in the first place."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ norikoinvite3 = True

        jump norikoinvite4

label norikoinvite4:
    scene somewhere1
    with dissolve2

    a "You’re such a silly goose, Sensei. You know darn well that I’d drop whatever I’m doing to make you feel good. There’s no need for you to {i}ever{/i} watch porn {i}ever again{/i} when I exist."
    s "Do we really have to do this in here?...Can we not use your room?"
    a "There you go, being a silly goose again. Why would we bother walking all the way to my room when you’re already this hard? I can take care of you right here."
    a "Plus, I like the way your room smells. "
    a "It’s thick with pheromones and memories of all the times I touched myself beneath your blanket."
    a "To think of how far we’ve come since then...how many times we’ve gotten off with each other’s help..."

    "Ami tightens her grip around my cock, bringing it closer to her mouth so I can feel her breath before continuing on with her sentence."

    a "Something as amazing as your cum would just be wasted on anyone or anything else."
    a "You don’t have to masturbate anymore, Sensei. You can use me. Your love is all the payment I need for all the things I do for you...The things no one else ever {i}could.{/i}"
    s "A-"
    a "Tell me you love me."
    s "..."
    s "I love you..."
    a "Tell me you want to stuff your big cock in my little mouth."
    s "I...want to..."
    a "There’s no need to be embarrassed, Sensei. I’m used to this by now. Go on. Say it."
    s "I want to...stuff my big cock in...your little mouth..."
    a "You want your baby girl to give you a blowjob?"
    s "...yeah."
    a "You want her to swallow your cum?"
    s "Ami, come on..."
    a "Fine...but only cause I can’t wait any longer to {i}taste{/i} you again..."

    scene somewhere2
    with dissolve2

    "Ami sticks her tongue out and positions my cock directly at the entrance to her mouth. "
    "She jerks me quickly, lathering the tip with hot, sticky saliva as her teeth softly and repeatedly brush up against me."
    "She’s become too good at this and is now a trophy of my inadequacies as a guardian."
    "Even if she loves me, this is not something we should be doing. And I’ve known that all along."
    "But my weakness manifests in a variety of ways — and almost all of them lead to someone getting hurt."
    "But not this one."
    "This one, I {i}can’t{/i} hurt."
    "It feels as if she won’t let me."

    scene somewhere3
    with dissolve2

    a "You like that...[amimaster]?..."
    a "You like when your little girl plays with your cock?..."
    s "..."
    a "You want me to suck it?..."
    a "You want me to make you feel good?..."
    a "I’ve been practicing in my spare time...I bet I can fit more of it inside now..."
    s "..."
    a "You don’t have to talk...I can tell you’re enjoying this...Just leave everything to me, okay?...I know what I’m doing..."

    scene somewhere4
    with dissolve2

    a "Hm!~"
    a "Mmf...shlrp...hmgh...[amimaster]..."
    a "Your cock tastes so good...I love when you let me suck it..."
    a "I love...mmf...how you let me play with you...and I love how you play with me too..."

    scene somewhere5
    with dissolve

    a "But today’s all about you, okay? Your little girl is gonna reward you for being so loyal...and for never touching anyone but her..."
    a "After you cum...I’ll make you dinner...and then I’ll warm your bath...and once you’re ready for bed...I’ll climb in with you and make you cum again...and again...and again and again and again..."
    s "..."
    a "Do you want my pussy next time, [amimaster]?"
    a "Do you want to grab my ass and help me ride you harder?"
    a "Do you want to fuck my tight little hole? Breed me? Make me yours forever and ever and ever?"

    scene somewhere6
    with dissolve2

    a "Mmf! Mngh...orwouldyou...ratherbe...the one in charge?"
    a "Dontchawanna...pinmedownand...fuck me ‘til I cry?..."
    a "Press my shoulders against the mattress...feel my legs wrapping around your back as I...desperately grip the sheets from pleasure?..."
    a "You wanna make a baby with me?..."
    s "Ami..."

    scene somewhere7
    with dissolve

    a "Lgh...glgh...Iwanna...mekabebywffyou..."
    s "Since when can you..."
    a "Prctismeks...prfct..."
    a "Dya...lkkit?"

    "Don’t give in."
    "Remember who else is here."
    "You’re not alone."

    a "Fuck...my mouth..."
    a "{i}Daddy...{/i}"

    play sound "static.mp3"
    scene somewhere8 with flash
    stop sound

    "I can’t."
    "I can’t help myself."
    "This is what I’m meant to do..."
    "It’s what I {i}want{/i} to do..."
    "I want to fuck Ami’s mouth."
    "She’s just so cute."

    a "Lgh! Mlgh! Glgh! Mmgh! Hlgh! Mmf!"

    "I grip her head and hold her still, pathetically thrusting into her mouth as if it’s my first time discovering how to make myself feel good."
    "There’s barely any room to move inside of her, but she steels her resolve and opens wider as I rapidly grow closer to climaxing."

    scene somewhere9
    with dissolve

    a "Pah...hah...hah...more..."

    play sound "static.mp3"
    scene somewhere8 with flash
    stop sound

    a "Mghllglgghghhgh PPfbbtt! Lghhlhlhhhggghh!!! "
    s "Just like that, Ami...just like that..."
    s "I’m gonna cum..."

    scene somewhere10
    with dissolve

    a "Lgh...glp...lgh...glp...mmm..."

    "I gaze down to find a beautiful girl desperate to please me, opening her throat and letting me fuck her to my heart’s content."
    "I think about what she has been through."
    "And how she must be rewarded."
    "Her eyes tell me this:"

    a "{i}I want your seed.{/i}"
    a "{i}I am a toy for you to use as you please.{/i}"
    a "{i}And I don’t like it when you play with others.{/i}"
    s "I’m gonna cum, Ami..."
    a "Lgh...lgh...lgh..."

    with sexfade
    with sexfade
    scene somewhere11 with cumflash
    with hpunch

    s "Hah......hah..........hah......."
    a "Mlgh........hngh......glp...."

    scene somewhere12
    with dissolve

    a "{i}Aaaahhh...{/i}"
    a "Lckwhutyoudidtome~"
    s "Swallow it. "
    a "Yssdaddy..."

    scene somewhere13
    with dissolve2

    a "Mlgh...mng..."

    scene somewhere14
    with dissolve2

    a "{i}Ahhhh...{/i}"
    a "{i}All gone...{/i}"
    s "..."

    scene somewhere15
    with dissolve

    a "Feel better now that you got to relieve yourself? Were my deepthroating skills okay? "
    s "..."
    a "Sensei?..."
    a "Trapped in ecstasy? I know what it’s like. You poor thing."
    s "I’m hungry..."
    a "Hungry? "
    s "Can you run to the convenience store and grab us dinner?"
    a "You don’t want me to- "

    scene somewhere16
    with dissolve

    a "Ahh...right. I almost forgot where we were for a second."
    a "Sure...I can run to the convenience store."

    scene black
    with dissolve2

    "Ami licks my cock one last time before bringing herself to her feet."
    "She straightens up her clothes before standing in front of the closet."
    "When she speaks again, she isn’t facing me."

    a "Two bentos? "
    a "Or {i}three?...{/i}"
    s "..."
    a "Just wondering how hungry you are, Sensei. "
    s "..."
    a "Hmm...I suppose I’ll get two then."
    a "If you’re still hungry after dinner, you can eat {i}me.{/i}"

    play sound "dooropen.mp3"

    a "Bye-bye! I love you!"
    a "Don’t do anything that would make me sad while I’m gone!"
    a "You never know when I'll come back."
    s "..."

    "The gap in time between Ami leaving my room and then the front door feels infinite- though that’s likely only because I am dreading what comes next."

    scene somewhere17
    with dissolve2

    "I’m dreading what will emerge from this closet."
    "I’m dreading the state it will be in and what it will mean for all that happens next."
    "But this was the safest path. "
    "This is what had to happen."
    "{i}Someone{/i} had to get hurt so Ami wouldn’t."
    "She’s my responsibility."
    "She doesn’t have anyone else."
    "She doesn’t want anyone else."
    "I need to keep her happy or she’ll dissolve into nothing."
    "I don’t want to be alone again."
    "I need her."
    "I need her to like me."
    "I need her to love me."
    "I need her to wash my sheets and {b}suck my cock{/b} and cook me dinner and {b}let me cum inside her{/b} and remind me I’m not alone and {b}lay her hands on me.{/b}"
    "I need everything."
    "Because I have nothing."

    play sound "slidedoor.mp3"
    scene somewhere18 with dissolve2

    n "..."
    s "..."
    n "..."
    s "..."
    s "Noriko-"
    n "I’m gonna go home now."
    s "..."
    n "Please don’t follow me."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    s "Noriko, wait. We need to talk."
    n "We’ve talked enough this week. I need to lie down."
    n "Bye-bye."

    "Stop."

    play sound "static.mp3"
    scene nflash1 with flash
    stop sound

    "Don’t go."

    play sound "static.mp3"
    scene nflash2 with flash
    stop sound

    "Don’t leave."

    play sound "static.mp3"
    scene nflash3 with flash
    stop sound

    "No."

    play sound "static.mp3"
    scene nflash4 with flash
    scene nflash5 with flash
    stop sound

    "Please."

    play sound "static.mp3"
    scene nflash6 with flash
    scene nflash7 with flash
    scene nflash8 with flash
    scene nflash9 with flash
    stop sound

    "{i}Don’t do to me what I did to you.{/i}"

    play sound "static.mp3"
    scene nflash9 with flash
    scene nflash8 with flash
    scene nflash7 with flash
    scene nflash6 with flash
    scene nflash5 with flash
    scene nflash4 with flash
    scene nflash3 with flash
    scene nflash2 with flash
    scene nflash1 with flash
    scene somewhere19 with flash
    stop sound

    s "Noriko!"
    n "..."
    s "I..."
    s "Let me walk you home."
    n "Don’t you have to ask Ami first?"

    scene somewhere20
    with dissolve

    s "..."
    n "You know what’s really depressing, Akira?"
    n "Years from now, when I’m looking back on the happiest days of my life, this is going to come up."
    n "The first time I was ever fingered by the man I’ve spent my whole fucking life admiring...was {i}tainted{/i} by being the same day I watched him fuck his niece’s mouth from the inside of a closet."

    scene somewhere21
    with dissolve

    s "I had no idea that was going to-"
    n "How long?"
    n "How long have you two been like that?"
    s "..."
    n "Has it been happening this whole time?"
    s "..."
    n "Is {i}that{/i} why you tossed us aside? Because you were content with the relationship you had with your {i}niece?{/i}"
    s "No. That’s-"

    play sound "static.mp3"
    scene minigod1 with flash
    scene andsoami with flash
    scene minigod2 with flash
    scene somewhere22 with flash
    stop sound

    n "I don’t get it."
    n "I just don’t get it. "
    n "Am {i}I{/i} the crazy one for thinking it’s weird for you to cum in your niece’s mouth when I’ve been chasing after you for just as long as she has? Is that hypocritical of me? Is there something I’m missing?"
    s "There’s nothing you’re missing. You’ve done everything right. I’m the one who keeps making mistakes."

    scene somewhere23
    with dissolve

    n "You were supposed to be {i}my{/i} mistake! Remember?! "
    n "How come none of the weird, socially unacceptable decisions you’ve made have ever been aimed at {i}me?!{/i}"
    n "Maya, I understand! Nee-chan, I understand! Even Kirin I can bring myself to understand! But {i}Ami?!{/i} You made a “mistake” that led to {i}Ami{/i} and not me?! What am I missing?!"

    scene somewhere24
    with dissolve

    n "This is a dream. There’s no way any of that just happened. That’s soap-opera level drama and it just wouldn’t fly in real life. Nope."
    s "I wish it {i}was{/i} a dream, Noriko. I wish none of that ever happened."

    scene somewhere25
    with dissolve

    n "Yeah, I bet. Seemed like you were suffering pretty badly when you grabbed the back of Ami’s head and told her to swallow your cum."
    n "Want a hug, Akira? Will that make you feel better? Because I’m so desperately infatuated with you that I’ll do it even {i}if{/i} I feel like throwing up right now."
    s "I’m not wishing things weren’t like that between Ami and me. That was a decision I made and...despite how it may look, I don’t regret it. She’s important to me and I’m important to her."

    scene somewhere26
    with dissolve

    n "This is going to sound rich coming from me, but I think you might be a liiiiiittle {i}too{/i} important to her if she’s going to act like {i}that.{/i}"
    s "...What I wish is that you never had to see any of that. You didn’t deserve it."
    n "Thanks! Can I leave now? I want to go sit in the corner and think about why I’m essentially the only person in your life you won’t touch. "
    s "That’s not it, Noriko...You should know after today that I’m absolutely open to that."

    scene somewhere23
    with dissolve

    n "You left me on the beach for Maya when you could have had me right then and there! And you left me in the {i}closet{/i} for Ami when we were just about to have sex! "
    n "How many more times is this going to happen?! How many more times will I be left behind?!"
    n "I don’t want to be a backup! I want you to love me just as much as you love them!"
    n "I’m tired of my special memories being poisoned by your overwhelming feelings for other girls! "
    n "I’m not even asking you to abandon them! I’m just asking for {i}one{/i} thing I can have to myself! One thing to look back on without having to remember some terrible caveat!"
    n "Is that too selfish of me?! Am I being punished for simply {i}wanting{/i} something?!"
    s "I love you just as much as them, Noriko..."

    scene somewhere27
    with dissolve

    n "Do you really, though?..."
    n "Because sometimes it feels like we would have ended up together faster if I hadn’t spent all of those years improving myself and just flat-out broke instead."
    s "Noriko...no."
    n "Is that what you want, Akira? Is that the key to your heart? I need to give up the only original pieces of myself that still remain and just let you mold me yourself? Tell me."
    s "I want you...to stay exactly the way you are."

    scene somewhere28
    with dissolve

    n "But why? "
    n "The way I am isn’t what you want. If it was, we’d be able to make it through one special moment without pulling apart. "
    s "Because you’re one of the only bright spots in my life."
    n "Then either you’re lying right to my face or you just love the dark."
    s "I’m not lying. And, believe it or not, I prefer the light."

    scene somewhere29
    with fade

    n "Then tell me what I can do to shine brighter."
    n "Tell me what steps I need to take so that one day, you walk away from someone else for {i}me.{/i}"
    n "Is such a thing possible? Is there even a future out there like that?"
    s "There is."
    s "Somewhere."
    s "But the Noriko in that future is one who didn’t change just to get closer to me- it’s one who stuck to her guns and remained true to herself throughout all of the hardships."
    n "But that’s the same thing as saying-"
    s "I need you to suffer for me."

    scene somewhere30
    with dissolve

    n "..."
    s "I tried warning you."
    s "That all I can do is hold you back."
    s "That you’ll be better off just living your life without me. "
    s "But I’m selfish. And I know I’m holding some of the pieces you need to move on in my hands."
    s "I can’t let them go. And I don’t {i}want{/i} to let them go because the idea of a future without you in it scares me...even though I know it would be a million times better for you."
    s "That’s why I need you to suffer. "
    s "I need you to sacrifice your happiness and stay addicted to me so I don’t have to feel things I don’t want to feel."
    n "That’s a horrible...{i}horrible{/i} thing to ask someone."
    s "I know. I-"
    n "But I’ll do it."
    s "..."
    n "You know I will. I’d do anything for you. "
    n "But, like Ami said, everyone has limits. And what happened back there pushed past mine."
    n "I need time to get my head back on straight...and re-evaluate some things now that I know what you two are {i}really{/i} like."
    s "Do I disgust you?"
    n "I’m much more disgusted by what you did to {i}me{/i} than what you did with her. "
    n "I’m a strong girl, Akira- but I’ve never felt more powerless in my life."
    n "You should have said no."
    s "I tried."
    n "You should have tried harder."
    n "She’s a teenage girl just like me. She doesn’t control you. And I don’t know what sort of obligation you {i}think{/i} you have to her, but you don’t."
    s "..."
    n "Ami is like a sister to me. But I swear...if I hear her speak that way to you again?...I..."
    n "I don’t really know what I’ll do. But she won’t like it."
    s "I’m sorry you have to go through this, Noriko....I’m sorry I’m {i}putting{/i} you through this."
    n "The Akira Arakawa I know wouldn’t apologize. He’d uncomfortably glance off to the side and then have some deep inner-monologue about what this means for the future."
    s "I don’t...think I know that right now."
    n "Figure it out."
    n "And skip the fingering the next time you invite me over."
    n "Because right now, I’m going to go back to the dorm and cry into Kirin’s lap..."
    n "But as soon as I see you again, I’m going to make you realize you’ve been fucking the wrong little girls this whole time."
    s "..."
    n "Got it?"
    s "Yeah..."
    n "Good."
    n "I love you."

    scene black
    with dissolve2
    stop sound

    s "I love you too..."

    "{i}Uh-oh! Looks like your incestual tendencies have been exposed to someone else!{/i}"
    "{i}Noriko needs some time to recover from the emotional scarring this has caused her, but you’re free to continue having sex with Ami in the meantime!{/i}"
    "{i}She’s very good at it and her insides feel great!{/i}"
    "{i}It’s almost like fucking an angel!{/i}"

    $ renpy.end_replay()
    $ norikoinvite4 = True
    $ noriko_love += 1
    $ norikoblock = True
    $ ami_lust += 1
    stop music fadeout 8.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "{i}Ami’s lust has increased to [ami_lust]!{/i}"
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

label sportswars2:
    play sound "static.mp3"
    scene mayanorikolockers1 with flash
    stop sound

    "A similar place at a similar time calls for a similar intro to the one you just got. "
    "Just, this time, we’ll talk about something a little different from “responsibility.”"
    "This time, we’ll talk about jealousy."
    "Maya Makinami was a normal high school girl. Well, kind of. Actually, not really. Like, she was normal-{i}ish{/i}. Especially now that her brain was a brain again. "
    "But she still enjoyed the way a specific adult male’s phallus felt inside of her, so she was about to embark on a journey to feel that again as that man was currently not being much of a man at all."
    "She was angry because of this. He’d ignored her before, but this time was different. And she wasn’t sure if Ami had anything to do with it, but she knew she’d have to confront her too as a part of this journey."
    "That’s not who she was jealous of, though. "
    "Her {i}actual{/i} jealousy was focused at three other people. But, on the bright side, one of those people was dead. "

    n "Maya?..."

    scene mayanorikolockers2
    with hpunch

    "But two of them weren’t."

    play sound "static.mp3"
    scene mayanorikolockers3 with flash
    stop sound

    "And one of them just so happens to be the {i}real{/i} subject for event numero dos."
    "Which, unfortunately, means Mayonnaise Macaroni is going to have to wait a little longer to be the center of attention again. But hey, she should be used to that by now."
    "Or...shouldn’t be?"
    "I don’t know. Do {i}you{/i} think she’s retained any of her memories?"
    "Or do you think that maybe she’s kind of always just been a bitch?"

    n "What are you doing?"
    m "..."
    n "..."
    n "Uhh..."

    scene mayanorikolockers4
    with dissolve

    m "Fuck. I thought if I stayed really still, you wouldn’t be able to see me."
    n "Are you some kind of chameleon?"

    scene mayanorikolockers5
    with dissolve

    m "It takes one to know one, you slimy whore."
    n "Reptiles aren’t slimy. That’s more of an amphibian thing. If anything, chameleons feel more leathery than-"
    m "Why are you talking to me? Why are you {i}looking{/i} at me? I’m clearly busy."

    scene mayanorikolockers6
    with dissolve

    n "Busy doing {i}what?{/i} Because it’s sports day and it looks {i}kind of{/i} like you’re getting ready to leave."
    m "Well, aren’t you just an expert at deductive reasoning?"
    n "You’re just going to leave your friends behind when they’re counting on you? Seriously? "

    "Despite directly asking Maya about her intentions, Noriko already knew the answer. "
    "She just preferred to look to the positive side of things, and sincerely hoped her “rival” would see the errors of her ways if they were just pointed out to her enough."
    "But that wasn’t the type of girl her “rival” was. "

    m "They’ll figure out a way to win without me. It’s no big deal."

    "Her rival was selfish. Stubborn. She was simple-minded, yet passionate to a point where it felt almost like some sort of over-exaggerated character flaw."
    "But despite feeling the negativity oozing out of those unfortunate traits, Noriko was jealous of {i}her{/i} as well. And she frequently wondered what it would be like to not assume the role of a martyr every morning."
    "This is what made the two rivals in the first place — that mutual jealousy and unspoken respect, pumped with negative connotations that seemed more like embalming fluid the longer it kept their hatred from decaying."

    n "Then, do you mind if I take a guess as to where you’re going?"

    "It would have to decay eventually, though...wouldn’t it?"

    m "I do, actually. I’ve already had to fend off one interrogation today and I’d much prefer to not go over my quota."

    "After all, the two of them weren’t all that different from one another."
    "They loved the same man. They were interested in the same avant-garde literature. Even their Internet histories were mostly congruous."
    "But, most importantly of all, they shared the same fear — each other."
    "Right now, one of them was terrified."
    "And the other was simply..."
    "Nostalgic."

    scene mayanorikolockers7
    with dissolve

    n "{i}Hah...{/i}"
    m "Does that sigh mean I’m free to go now? Or are you planning on telling Miss Imai about this the second I walk through those doors?"
    n "I’m not going to {i}tell{/i} on you, Maya. And I doubt Imani would give a shit even if I did. "
    n "I’m sighing because I’m disappointed."
    m "And...I’m supposed to {i}care{/i} about that?"

    scene mayanorikolockers8
    with dissolve

    n "No...I just mean that it sucks you’ve managed to make it this far without finding even one more thing you want to protect. "
    m "You want to know what sucks even more? A creepy stalker who transfers into my school so she can try and fuck my teacher. {i}That{/i} sucks. {i}And{/i} it goes against what we agreed. So die."
    n "We were kids, Maya. We said and agreed to a lot of things we didn’t understand."

    play sound "static.mp3"
    scene mayanorikolockers9 with flash
    stop sound

    n "{i}But not all of us {b}did{/b} things we didn’t understand.{/i}"

    scene mayanorikolockers10
    with dissolve

    n "So, when you and Akira are alone, what’s it like?"
    m "We’re supposed to call him “Sensei.”"

    scene mayanorikolockers11
    with dissolve

    n "Ugh! {i}You’re{/i} gonna make me do that too? It’s bad enough hearing it from him all the time. The last thing I need is you hopping on the same bandwagon of {i}boredom.{/i}"
    m "Can you please stop talking now? I’m trying to study."

    scene mayanorikolockers10
    with dissolve

    n "But we’re supposed to be studying together."
    m "Sure. But I don’t {i}want{/i} to study together. You never take anything seriously and you talk way too much. It’s annoying. {i}You’re{/i} annoying. So die."

    scene mayanorikolockers12
    with dissolve

    n "Why do you always have to be so mean to me? I’m just trying to make conversation."
    m "No, you’re trying to make {i}weird{/i} conversation about Sensei and me being alone together. It’s a leading question and I’m not going to fall into whatever trap allows you to extort information out of me."
    n "Maya, you’re here every day. I can only come once or twice a week. You guys are alone {i}a lot.{/i} And even {i}when{/i} I’m here, you’re always getting special treatment."
    m "{i}I’m{/i} getting special treatment? You keep calling him by his given name and he’s never even disciplined you for it. And that's not even counting how you’re always hanging all over him."
    n "I’ve been hanging all over him since I was a baby. He’s basically my big brother. And he’s probably {i}going{/i} to be my big brother one day if he and my sister get married."
    m "{i}If.{/i} Key word. "
    n "Would you rather it be you?"
    m "If I say yes, will you stop talking to me?"
    n "No. I’ll probably press you even harder about what happens when you guys are alone."
    m "Then I guess I’ll just shut {i}my own{/i} mouth since you seem incapable of doing that."

    scene mayanorikolockers13
    with dissolve

    n "Wanna know what he does with my {i}sister{/i} when they’re alone?"
    m "They haven’t been “alone” for months. She’s a non-factor. And also, no. Because I would like to keep my lunch {i}inside{/i} of my body."
    n "She gives him “handjobs.” Do you know what those are, Maya? It’s when-"

    scene mayanorikolockers14
    with dissolve

    m "I don’t need you to tell me what they are! I’m not an idiot!"
    n "Ooooooh? So you know already? Is that what you’re reading about over there? Practicing for having a boyfriend one day? No wonder why you want to study alone."

    scene mayanorikolockers15
    with dissolve

    m "..."
    n "It’s only a matter of time until we start doing stuff like that, isn’t it? "
    n "Do you think Akira might teach us about sex-ed next?"
    m "Shut up..."
    n "I’m pretty sure there are other “jobs” too. I heard one of the girls in my class talking about “blowjobs” but I don’t think I get it yet. Like, do you just-"

    scene mayanorikolockers16
    with hpunch

    m "Shut up!"
    n "Jeez, Maya. You don’t have to yell at me."

    play sound "static.mp3"
    scene mayanorikolockers17 with flash
    stop sound

    m "Shut up!"
    n "Jeez, Maya. You don’t have to yell at me."
    m "How can I not when you’re always such a presumptuous cunt?! You don’t know the first thing about what I {i}did{/i} back then!"
    n "I mean...I might not have {i}seen{/i} it. But the context clues at this point from {i}both{/i} of you are no longer just a pile. It’s kind of like a big context...mountain."

    scene mayanorikolockers18
    with dissolve

    m "So what, then? Are you {i}jealous?{/i} Are you just stopping me because you’re {i}still{/i} petty about the way things ended up? You wish it were you instead?"
    n "Maya...I am jealous about a lot of things. "
    n "Your eyes....Your figure...Your confidence..."
    n "There are so many parts of you that I want for myself."
    n "But being molested is {i}not{/i} one of them."

    scene mayanorikolockers19
    with dissolve

    m "You have no fucking clue what you’re talking about."
    m "Now, if you’re done ruining my life, I would like to leave you with the same words I left Ayane with."

    scene mayanorikolockers20
    with dissolve

    m "Peace."
    m "And also, die."

    scene mayanorikolockers21
    with dissolve

    m "Oh and good fucking luck or whatever. Hope you’re chosen for death ball."
    n "Death ball?"

    scene black
    with dissolve2

    n "What the hell is death ball?"

    "........."
    "......"
    "..."

    scene mayanorikolockers22
    with dissolve2

    ki "Hey, welcome back. I was beginning to think you weren’t going to join us this year. Which was kind of weird on account of how we walked to school together."
    n "Yeah, I had to show my friends around. And then I had to get dressed. And then I had to confront a ghost from my past who still haunts the halls of this very school. "
    ki "Cool. I had tacos. "

    scene mayanorikolockers23
    with dissolve

    n "{i}I{/i} want tacos. How come you always get to have all the fun while I’m stuck conquering demons? "
    ki "Because I’ve dedicated my life to doing whatever I want and you’ve dedicated {i}yours{/i} to making other people happy for whatever reason."
    n "If you’ve dedicated your life to doing whatever you want, how come you’re not a stay-at-home mom packing lunches for our former teacher yet?"

    scene mayanorikolockers24
    with dissolve

    ki "Stay-at-home mom? Oh, please. I’m just going to be the live-in housekeeper who fucks him while the wife is away and occasionally joins in for threesomes."

    scene mayanorikolockers25
    with dissolve

    n "Does this mean {i}I{/i} get to be the wife?!"
    ki "You’re probably the most likely to have a consensual threesome with me at this point, so yeah. Looks like you get to be the wife."
    n "And every Tuesday can be Taco Tuesday?!"

    scene mayanorikolockers26
    with dissolve

    ki "And every Tuesday can be Taco Tuesday."
    n "I’ve never been more excited to share the love of my life before. And that’s saying a lot because I do that every single day now."
    ki "Thankfully, everyone you’re normally sharing him {i}with{/i} is here. Minus the crazy niece and Yumi, that is. "
    n "Yumi will be here. I texted her earlier. "

    scene mayanorikolockers27
    with dissolve

    n "There’s someone {i}else{/i} missing now, though. The first floor just lost Maya. And I highly doubt she’ll be coming back any time soon."
    ki "Maya? Is {i}that{/i} who you were talking about with that whole “ghost from your past” thing? The fuck is {i}she{/i} doing bailing on the contest before it’s even gotten started?"
    n "Probably attempting the same thing you’ve been desperately holding yourself back from doing over the last few months in storming Sensei’s castle and attempting to claim his heart."

    scene mayanorikolockers28
    with dissolve

    ki "On bloomer day? Lame. I only got to stare at her ass for like two minutes."
    n "You can stare at my ass next. I think it’s a pretty good one."
    ki "Yeah, but I see yours all the time. Maya’s ass is like filet mignon in that I rarely ever get to experience it and when I {i}do,{/i} I want to take my time and enjoy it."
    n "Maya is technically my rival and I should be mad at you for saying this, but yeah. I get it. "

    scene mayanorikolockers29
    with dissolve

    ki "You sure you’re okay with staying here, though? Because I wouldn’t blame you for chasing after her given that you {i}are{/i} rivals and all. "
    n "There’s no point. I can never beat her head-to-head. She’s got too much of a lead."
    ki "Yeah, but you’ve also been saying all that shit about how she’s been {i}different{/i} lately. So maybe that won’t vibe with Sensei and he’ll decide he wants to fuck you more or something."
    ki "I don’t know. I’m trying to think positive here."
    n "All things considered, this is probably the {i}least{/i} weird thing she’s done lately. Doesn’t mean it isn’t annoying, though."

    scene mayanorikolockers30
    with dissolve

    ki "Mood. Karin’s been like that lately too."
    n "{i}Karin?{/i} Like...like {i}the{/i} Karin?"
    ki "The one who shares my DNA? Yeah. "

    scene mayanorikolockers31
    with dissolve

    n "Well, what the fuck happened to her?! She can’t act weird! She’s our perfect little ball of sunshine!"
    ki "First off, fuck you. But second, I have no fucking clue! "
    ki "She just came home bawling her eyes out one day and won’t tell me what happened. She’s barely left the bedroom outside of going to school."

    scene mayanorikolockers32
    with dissolve

    n "I hope she didn’t see an animal get run over or something. I feel like that would greatly alter her path and turn her into something none of us are ready to console."

    scene mayanorikolockers33
    with dissolve
    stop music fadeout 30.0

    ki "No, I don’t think that’s it. This seems more, like...personal. She’d tell me about an animal getting hurt."
    ki "It’s just...weird. I’ve never had to deal with her keeping a {i}secret{/i} before, so I can’t really wrap my head around what it might be."
    n "Do you think someone might have confessed to her again or something?"
    ki "I don’t know. Maybe she finally found out what a dick is and just can’t mentally process it?"
    n "Your sister knows what is a dick is, Kirin."

    scene mayanorikolockers34
    with dissolve

    ki "You can never be sure when it comes to things like this, Noriko. And if anyone knows about my sister’s history with dicks, it’s me."
    n "I want to say that’s weird, but I can also completely relate."
    ima "Okay, okay, okay! Eyes over here, girls!"

    $ renpy.end_replay()
    $ sportswars2 = True

    jump sportswars3

label norikospring1:
    play sound "static.mp3"
    scene nightsky with flash
    stop sound
    play music "noriko.mp3"

    "Somehow or another, I wind up in the second half of town again."
    "But seeing as I’ve learned my lesson (be it conscious or not) to try and stay away from bridges or overhangs or anything else I can throw myself off of, I now have to figure out something else to do."
    "But do you know what place doesn’t have any bridges or overhangs? The convenience store."
    "Unfortunately, there’s a creature with pink hair who practically lives inside of that building that is equally dangerous to me based on nothing but several blackouts and the biases of my deceased girlfriend(?)."
    "And no, I’m obviously not saying that because the creature in question lives her life with a pocketknife tucked into her waistband. I am saying it because it’s true."

    scene black
    with dissolve2

    "While the pieces of my past may no longer throw this puzzle of a life into potential world-ending turmoil, it doesn’t mean I’m ready to start filling in the blanks."
    "And something that’s a happy memory for her might be a nightmare for me. Which is why I have to be careful."
    "I {i}can{/i} learn."
    "I just don’t want to."

    n "Ah! Onii-chan!"

    scene norikokonbinifire1
    with dissolve2

    y "{i}Onii-chan?{/i}"
    n "Not legally or biologically, but somewhat historically. And history dictates that it’s normal for me to call him that while we’re in here!"
    s "Just because you have a history of doing that doesn’t make it “normal.”"
    y "Yeah, it makes it fuckin’ weird and gross."
    s "I mean...I don’t think I’d go {i}that{/i} far."

    scene norikokonbinifire2
    with dissolve

    y "Shocker."
    s "You’re welcome to call me a cute pet-name as well if you’d like, Yumi."
    y "Sure. Does Captain Rapist work for you or should I figure something else out?"
    s "Figure something else out, please."

    scene norikokonbinifire3
    with dissolve

    n "Nicknames aside- you got here at the perfect time, Sensei! I was just about to go on break."
    s "That’s nice. But Yumi has a track record of shoplifting and probably shouldn’t be left here alone. "
    y "He ain’t wrong. "
    n "Yumi’s fine. She needs money way more than candy and condoms. "
    n "But you and me? We’ve got other stuff to do. Primarily stuff of the “bonding” variety since you now treat me like the middle child and don’t let me love you as much as you used to."
    y "So is he your {i}brother{/i} or your dad? I don’t get this relationship."

    scene norikokonbinifire4
    with dissolve

    n "Brother in the streets, daddy in the sheets."
    y "How do I put in my two-weeks notice? I’ve never done it before. "
    n "You don’t. You’re stuck here forever."
    s "In more ways than you know."

    scene norikokonbinifire5
    with dissolve

    n "Which means that you and I are {i}free!{/i}"
    s "From your shift? Sure. From the never-ending cycle of misery that blankets this school year in doubt and misfortune like snow over the Arctic plains? Nope. No one is free from that."

    scene norikokonbinifire6
    with dissolve

    n "But you don’t even go to school anymore. Which means you should be more concerned with taking that blanket off of me so we don’t have to conceal our cuddling from anyone we know."
    y "Hey, before you clock out for break, do you mind if I run to the bathroom and make myself puke really quick?"

    scene black
    with dissolve2
    stop music fadeout 30.0

    n "I do, actually. Purging isn’t good for your teeth. Or really anything for that matter. So keep all of that stuff inside you while {i}we{/i} get out of your hair! Which looks very beautiful, by the way. Which shampoo do you use?"
    y "Uhh...I ain’t sure. But I hope we’re havin’ another one of those fuckin’ hotel parties soon because I’m running low on whatever it is."
    s "Are you just...using the sample bottles from the hotels?..."
    y "Beats payin’ for shit, doesn’t it?"
    n "Some may call her cheap. {i}I{/i} call her resourceful. "
    n "She’ll look gorgeous as my maid of honor on our wedding day. And save me so much money as well."
    y "{i}Blch!...{/i}Sorry...I’ll be right back!"

    scene norikokonbinifire7
    with dissolve2

    "After Yumi disobeys Noriko’s orders and regurgitates the evidence of her disgust for me into the convenience store bathroom, I grab a beer and head outside with that pink-haired creature I warned you about before."
    "Her smile stings like antiseptic and the glow of her skin near the fire reminds me less of a certain type of bug and more of a vending machine. But I think that part is kind of beautiful in its own way."
    "She never leaves because she can’t. And she’ll give me anything I want so long as I press the right button."
    "When she looks at me, I instinctively look away. I’m not sure if it’s because I’m embarrassed or not when I don’t have anything specific to be embarrassed {i}about,{/i} but it certainly feels that way."
    "I take a sip of my drink, hoping its effects take root long before they’re supposed to because maybe that will be the push I need to stare back at her while her eyes beg for the attention of mine."

    n "..."
    s "..."

    scene norikokonbinifire8
    with dissolve2
    play music "thesleepingcity.mp3"

    "But instead, we sit in silence."
    "Her excitement, like that of a loyal dog, has waned now that I’ve gotten settled in. It was only the initial shock that caused her tail to wag."
    "I’m sure she’s thinking of what we’re supposed to talk about now. And I hate that she has to do that — but it’s the result of {i}me{/i} being a terrible owner."
    "You see, “settling in” for me is more like taking my clothes off and pulling my knees to my chest in the corner of the room. {i}Of course{/i} a dog’s excitement would fade if it had to watch such a thing."
    "But she’ll figure out what to do and what I need soon enough because {i}she’s{/i} the mature one here. "

    n "Um..."

    "See?"
    "She’s already coming over to lick me."

    n "So I heard from Nee-chan about her possibly moving in?"
    s "Well, keep it to yourself because Ami hasn’t yet."
    n "So it’s true then?"
    s "Maybe. I don’t know."
    s "I’m trying to step up and play the role of a father, but there’s no denying that a mother would probably be better for Ami. And I think Niki fits that role better than anyone."
    n "Yeah. Guess it wouldn’t make much sense for {i}me{/i} to be Ami’s mother figure when we’re almost the same age."

    scene norikokonbinifire9
    with dissolve

    n "Can you imagine? Me telling her to clean her room and do the dishes and stuff like that?"
    s "No, but that’s mostly because she already does all of those things without asking. "
    n "Then what would I need to do? Hit me with the job description, Sensei. Maybe I’ll throw my hat in the ring and compete with Nee-chan only to lose for the millionth time?"
    s "Would you even {i}want{/i} a role like that in the first place? You’re young. I thought you still wanted to {i}figure out who you are{/i} and all that?"

    scene norikokonbinifire10
    with dissolve

    n "I’m just messing around. As nice as it sounds to have you as my partner in life, I can’t imagine ever seeing Ami as a daughter."

    scene norikokonbinifire11
    with dissolve

    n "So I guess maybe I really {i}am{/i} screwed if that’s going to be part of the criteria now. "
    n "Oh well. It was a good run. All that’s left to do now is wait for gay marriage to be legalized so I can marry Kirin and open a sex shop or something."
    s "You’ve got some strong competition in town, Noriko. Don’t think that path will be easy. Maybe take over your parents’ restaurant instead?"
    n "Kirin {i}would{/i} look hot in a qipao. But again, this is all just fantasy-talk and not a thing I’m actually considering. Which I need to verbally clarify so you don’t misunderstand and think I’m actually quitting you."
    s "I never figured you were in the first place. I’m not sure what you’d even do with yourself if you weren’t too busy chasing after me all the time."
    n "Like I said, just making sure. We don’t need to dwell on the fact that I’m a wannabe brocon any longer than we already have."
    n "Especially when there’s something I actually {i}want{/i} to talk about tonight."
    s "Oh good. Late night talks always go really well for me."

    scene norikokonbinifire12
    with fade

    if amifingered == True:
        n "You’re one to talk. Because I distinctly remember one of our last late-night talks ending with you telling me that I had to “suffer for you.” "
        s "And you’ve been doing a great job."
        n "Have I? It doesn’t feel like it."
        s "That’s how you know you’re doing it well."

    else:
        n "I guess our track record isn’t great when it comes to those, is it?"
        s "My track record in general isn’t great when it comes to those. But it’s not great when it comes to daytime conversations either, so I’m not sure what I’m expecting."

    n "This one might be a little awkward, Sensei."
    s "Well, that’s a great thing to hear right before I find out what it is."

    if amifingered == True:
        n "If I’m going to suffer for you...would you mind suffering for me for a little while? Even if it’s just tonight."
        s "..."
    else:
        n "My timing has never been good. Now’s no exception to that."
        s "What is it then, Noriko?"

    scene norikokonbinifire13
    with dissolve

    n "We had the Dorm Wars again recently."
    n "It was a lot of fun...But it felt really different without you. Just like class has felt different with Imani as our teacher and...the dorms without whispers of who you’re with and when."
    n "There’s a lot that feels like that now. Like this is a...slightly incorrect world that we accidentally fell into when you and Ami left school."
    n "And I don’t know if I’m the only one who’s noticed or...if everyone is just trying to save face...but sometimes, it feels like a lot of the smaller details go unnoticed by everyone but me."
    n "Maybe that’s just the type of person I am — someone who looks a little too closely at everything, but..."
    n "See, that’s kind of what I wanted to talk to you about in the first place. To see if maybe I’m just going crazy or...if you’ve noticed something too."
    s "Well...what are you talking about, exactly?"
    n "I’m talking about Maya."

    play sound "static.mp3"
    scene norikokonbinifire14 with flash
    stop sound

    s "..."
    n "Come on...don’t look at me like that. You make me talk about stuff {i}I’m{/i} not 100%% comfortable with all the time. Can’t you bear with me for a second just to hear me out?"

    scene norikokonbinifire15
    with dissolve

    s "Yeah, sorry. That just...took me by surprise."
    n "You’re still seeing her outside of school, right? Because the last thing she said to me was actually {i}during{/i} the Dorm Wars and it was about going to look for {i}you.{/i} "
    n "She bailed on the whole competition to do that. And while {i}that{/i} part of her isn’t something I’d call unusual...everything else kind of has been."

    play sound "static.mp3"
    scene norikokonbinifire16 with flash
    stop sound

    n "Maya and I...haven’t made as much progress as I would have liked since I transferred in. But we at least made {i}something.{/i}"
    n "Things changed a little bit. That...one-sided resentment she has for me never faded, but I could feel her starting to, like...I don’t know...resign herself maybe?"
    n "Kind of like a...“you stay on your side of the line and I’ll stay on mine” type of situation, but..."
    n "I mean, I guess {i}that{/i} isn’t entirely accurate either since that’s why she still hates me in the first place. I think. I don’t know."
    n "She’s always hated me and I’ve never really understood {i}why.{/i} But the point is that I felt like her hatred was starting to fade and..."

    scene norikokonbinifire17
    with dissolve

    n "Out of nowhere, it’s gone right back to how it was when I first transferred in."
    n "So I was wondering if you’ve {i}also{/i} noticed anything or...if I really am just going crazy."

    scene norikokonbinifire18
    with fade

    s "She {i}is{/i} different..."
    n "Right?! I fucking knew it! But everyone I’ve tried talking to about it has been all like, “Really? She seems the same to me.” And I’m just over here like ppfhfbfbfhfbttt?!?!! Are you BLIND?!"
    s "Talk to Ayane...she’ll agree with you..."
    n "She’s noticed it too, then? Well, what is it? If you can tell me, I mean. If it’s something personal, I probably shouldn’t pry. It was just weird to me that she started being so...well, {i}weird{/i} all of a sudden and-"

    scene norikokonbinifire19
    with dissolve

    s "Noriko, I..."
    n "..."
    s "I don’t know how to talk to you about this."
    s "And it’s probably going to make me sound insane, but I’m beginning to wonder if I {i}am{/i} insane and so...maybe that’s not really the worst thing possible."
    n "Tell me anything you’re comfortable with and not a word more. I’m not trying to play detective here, I just want an idea of what’s going on so I know how to approach her."
    s "Noriko...that person I talked about when I came back to school...the one I lost..."
    s "I was talking about {i}her.{/i}"

    scene norikokonbinifire20
    with fade

    n "..."
    s "I {i}do{/i} still see her outside of school sometimes, but it’s more like I’m seeing her reflection. Or someone walking around in her skin while the {i}real{/i} her is just...gone."
    s "Like everything we've seen and felt together over the last few years is just..."
    n "..."
    s "It's just...not {i}her...{/i}"
    n "Is this..."
    n "Is this anything like that memory thing that happened to {i}you?...{/i}"

    scene norikokonbinifire21
    with dissolve

    s "It’s {i}exactly{/i} like that. The same thing that happened to me happened to her. But I’m not sure if I can word it any differently than that without causing your brain to start instinctively interrupting me and-"
    n "But, Sensei..."
    n "If it’s the same thing that happened to you, doesn’t that mean she’s still in there somewhere?"

    scene norikokonbinifire22
    with dissolve

    s "Huh?..."
    n "Like...I don’t really get how it works, but you’re getting your memories back little by little, aren’t you?"
    s "Well...yeah..."
    s "But..."

    scene norikokonbinifire23
    with dissolve

    s "No...No, it’s {i}not{/i} the same thing that happened to me then..."
    n "But how do you know that? "
    n "It’s not like you can read her mind, can you? And, if you can, could you maybe let me know why she refuses to be my friend when everyone around her is just as guilty of loving you as I am?"
    s "If that’s..."
    s "If that’s really how it is..."
    n "If that’s really how it is, you’ll finally get to experience what Nee-chan and I have been going through these last..."

    scene norikokonbinifire24
    with dissolve

    n "Last few..."
    n "Years?..."
    s "..."
    n "..."

    scene norikokonbinifire25
    with dissolve

    n "A...Anyway! I know just how scary the thought of someone losing precious memories can be, but I also know now that it’s possible to get them back! "

    scene norikokonbinifire26
    with dissolve

    n "And that’s an adventure all on its own."
    n "It might be hard...and the road might be bumpy..."
    n "But the scenery when you get there, Sensei?..."

    scene black
    with dissolve2

    n "You’ll see such beautiful things..."

    "Noriko’s break comes to an end a few minutes later and she heads back inside to take over for Yumi."
    "But I stay out here. "
    "I’m not sure if I can walk right now."
    "And I know that Noriko would be more than happy to stay {i}with{/i} me, but she knows me. So she knows I want to be alone."
    "But the worst part is that I didn’t even have it in me to thank her for giving me the first taste of hope I’ve had since {i}she{/i} vanished."
    "Is it really possible that she’s actually in there?..."
    "And if so...how do I get her back?"
    "Do I just do what {i}she{/i} did and...ignore her until she figures it out herself?"
    "What happens if I break her again?..."
    "Will I see the same things she saw when she broke me?..."
    "I don’t know..."
    "..."
    "I have no idea..."

    $ renpy.end_replay()
    $ norikospring1 = True
    $ noriko_love += 1
    stop music fadeout 10.0

    "{i}Noriko’s affection increases to [noriko_love], but you’re too busy thinking about another girl to care!{/i}"
    "{i}This always happens to her! You should take this moment as a sign to spend more time with her and then eventually have sex with her because she deserves it!{/i}"
    "{i}Also, she is wrong! Do not have hope! Do not pass Go! Do not collect $200!{/i}"
    "{i}Go home, cum in a sock, then forget this ever happened!{/i}"

    play sound "doorslam.mp3"

    "{i}Goodnight!{/i}"
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

label norikospring2:
    scene sky
    with dissolve2
    play music "remember.mp3"

    ni "Noriko, hurry the fuck up. We don’t have enough time to look at stupid vegetarian food alternatives when starvation is always a viable option."
    n "Nee-chan, should you really be encouraging your little sister to starve? Your life would be incomplete without me and I ask that you take that back immediately or I will be forced to die."
    ni "Fine, don’t starve. But still, hurry the fuck up. The whole purpose of us going out today was to buy things for {i}Ami.{/i} And unless you’re planning on converting her-"
    n "Ami, want to go vegetarian with me? I can show you all of the best spots in town."
    a "I...don’t think I should. I’m not sure how Sensei would feel about that when he’s basically subjected to eating the same thing as me every night."

    scene molerat1
    with dissolve2

    ni "Ugh. Ami, as much as I believe you’re making the right choice, you really shouldn’t be basing all of your decisions on how your uncle feels about them."
    n "Uh...are you sure that {i}you’re{/i} qualified to be saying that, Nee-chan? Your entire career started out of spite for him."

    scene molerat2
    with dissolve

    ni "Yes, Noriko. But my {i}success{/i} is due to the fact that I am talented and beautiful and wasn’t bogged down by that asshole’s depressive ramblings during my golden years."
    n "I think we both know how you’d have really preferred to spend those “golden years.” And also, Akira isn’t Ami’s uncle anymore. He’s her dad now."

    scene molerat3
    with dissolve

    ni "Oh, right. Sorry. That’s gonna take some getting used to for me."
    a "I think it’s gonna take some getting used to for pretty much everyone. It’s fine, though. It doesn’t really matter what other people call him so long as I can call him that."
    ni "Has anything changed at all since you’ve {i}started{/i} calling him that? Any...talks, maybe?"
    ni "Also, is he giving you an allowance? Because I don’t want you buying anything for yourself today, but-"

    scene molerat4
    with dissolve

    a "I don’t get an allowance. I get all of my pocket money from my job at the maid cafe."
    ni "The one I did the promo at? They’re still there?"
    a "Yup! And as of next week, I’ll be ready to return and ready to make money again! You should come visit sometime soon. There’s a girl there who’s {i}obsessed{/i} with you."
    n "It’s that Chika girl I told you about. "

    scene molerat5
    with dissolve

    ni "The one with the little sister who wanted my autograph?"
    n "That’s what she said at least, but there’s like a 99%% chance that autograph was just for her. "

    scene molerat6
    with dissolve

    ni "I don’t care who it was for. I sign autographs all the time. But Ami, there’s no way I can go back to that place. They’ll recognize me immediately, disguise or not."
    n "Come to think of it, it’s really weird that {i}more{/i} people don’t recognize you while you’re in disguise. You’ve got a pretty {i}noticeable{/i} appearance, Nee-chan."
    ni "Blame Mom and Dad for strengthening the pink hair gene. Ami, where do you want to go next? Victoria’s Secret? UNIQLO? Or maybe Undercover so Noriko can get lost and we can run away together?"
    n "I do love that store."
    a "Anywhere is fine, Niki. I’m happy enough that you decided to take me out. Never in a million years would I have even {i}dreamed{/i} of going shopping with you."
    ni "Oh, shut up. You’re family. Let’s go to Victoria’s Secret. I know people there. I can get you free underwear."

    scene molerat7
    with dissolve

    a "What’s wrong with the underwear I have now?"
    ni "It’s so...plain. Here’s your lesson for the day — confidence stems from what you’ve got on {i}beneath{/i} your clothes, Ami. If you want to feel good about yourself, you need to-"
    n "Hey...isn’t that girl over there the one who’s been showing up at our special events lately?"

    scene molerat8
    with fade

    na "..."
    a "I can’t really see from-"
    ni "Hey, don’t pay attention to Noriko while I’m teaching you valuable life lessons. "
    a "Oh! S...Sorry! So, what’s wrong with my underwear exactly?"
    ni "What’s wrong is that you-"
    n "Nee-chan, Ami, you two can go on without me for a little while. I’ll catch up with you when you’re ready to grab lunch or something."

    scene black
    with dissolve2

    ni "Okay, guess we’re not going to Undercover then. Which is fine. They don’t really have anything in my style anyway. Come on, Ami! Let’s go! Time to bond!"
    a "Are you sure it’s okay to leave Noriko alone-"
    ni "Noriko’s fine. We come here all the time. Bye, little sister! Don’t get into any strange vans! Ami, come."
    a "Ah...okay!"
    a "Bye, Noriko!"

    scene molerat9
    with dissolve3

    n "Hi there! My name’s Noriko. You’re that girl who’s always walking around with the waitress, right? "
    na "?..."
    n "Are you lost? Do you need me to help you find her?"

    scene molerat10
    with dissolve

    na "!..."
    n "So you {i}are{/i} lost, huh? "

    scene molerat11
    with dissolve

    na "!..."
    n "You went out exploring together and got distracted by a fancy mug at a thrift store?"

    scene molerat12
    with dissolve

    na "?????...."
    n "Hm?"

    scene molerat13
    with dissolve

    n "Oh. Yeah. I’ve got a knack for figuring out what people are trying to say without actually hearing them. My sister says it’s my “kind heart” or something like that."

    scene molerat14
    with dissolve

    n "I can do it with animals too, you know."

    scene molerat15
    with dissolve

    na "?!?!?!?!"
    n "Yeah? You like animals? What’s your favorite kind?"
    na "!!!!!!!!!!!!"

    scene molerat16
    with dissolve

    n "Oh, interesting! I don’t think I’ve ever heard of that one before."

    scene molerat17
    with dissolve

    n "Come on. I’ll help you look for the waitress lady. We can hold hands so you don’t get distracted and wind up getting lost again, okay?"
    na "?..."

    scene molerat18
    with dissolve

    na "?..."
    n "No, I’m not going to {i}abduct{/i} you. I’m not one of the “bad people” she warned you about. I’m nice."
    na ".............."
    n "Yes, I...know that’s exactly what a bad person would say. But you can trust me! The whole reason I came over here was because you looked lost and-"

    scene molerat19
    with dissolve

    na "!..."
    n "Ah! You were just messing with me, weren’t you! The nerve of kids these days!"

    scene molerat20
    with fade

    n "Now, where do you think we should start looking? Where did you two first get separated?"

    stop music
    play sound "broken.mp3"
    scene molerat21
    $ renpy.pause(1, hard=True)
    scene molerat22
    $ renpy.pause(1, hard=True)
    scene molerat23
    $ renpy.pause(1, hard=True)
    scene molerat24
    $ renpy.pause(1, hard=True)
    scene molerat25
    stop sound
    $ renpy.pause(2, hard=True)
    scene molerat26
    with dissolve2

    n "Huh?..."

    play sound "static.mp3"
    scene molerat27 with flash
    stop sound

    n "..."
    n "Huh?..."

    scene molerat28
    with dissolve2
    play music "holyplace.mp3"

    n "HUH?!?!?!?!"

    scene molerat29
    with dissolve

    n "Where the fuck am I?! Why is everything so wet?! "
    n "And why am I holding an egg?!"

    play sound "pabell.mp3"
    scene molerat30 with dissolve

    vpa "Noriko Nakayama — please report to the principal’s office. "
    n "Report to the-"
    n "This..."
    n "This has gotta be a dream, right?"
    vpa "It is not a dream."

    scene molerat31
    with dissolve

    n "Like {i}fuck{/i} it’s not a dream, disembodied PA voice! I’ve never heard a school announcement {i}respond{/i} before! And this isn’t even my school!"
    vpa "This is everyone’s school."

    scene molerat32
    with dissolve

    vpa "The time is currently 7:31 PM. Today’s forecast is partly cloudy with a chance of nightfall. "
    vpa "You are happy here. There is no reason for you to leave."
    n "Okay, sure. But why am I holding an egg?"
    vpa "Reasons. "

    scene molerat33
    with dissolve

    n "Alright. I’ve seriously gotta lay off the melatonin before bed. I’ve heard of it causing nightmares, but this is just flat out weird."
    n "One second I’m shopping with Ami and Nee-chan, the next I have to bring an egg to the principal at 7:31 PM. That makes total sense."

    play sound "pabell.mp3"
    $ renpy.pause(2, hard=True)

    m "Noriko Nakayama — your attendance is required for the Transpacific Sadness Symposium in nine minutes."

    scene molerat30
    with dissolve2

    n "Maya?..."
    n "Transpacific...Sadness Symposium?..."
    m "Your guide is waiting just beyond the door. Please dry off your shoes and follow her to the best of your ability — but be warned."
    m "She skitters like a crab. And for every leg that snaps at the joint, a piece of you will be removed. "
    n "Like...my clothes? Because I’ve had some weird sex dreams before, but nothing even close to this."
    m "This is not a dream."

    scene black
    with dissolve2

    m "This is a replica of Heaven. This is the {b}DEN OF THE MOLE RAT.{/b}"

    "........."
    "......"
    "..."

    scene molerat34
    with dissolve2

    n "Wha..."
    n "It’s {i}you{/i} again..."
    na "..."
    n "Are you...a part of the dream as well?..."
    na "..."
    n "Please tell me you’re a part of the dream. Because the last thing I want to hear is that you got sucked in here {i}with{/i} me and that all of this is actually happening."
    na "..."

    scene molerat35
    with dissolve2

    na "..."
    n "You want me to go that way?..."

    scene molerat36
    with dissolve2

    n "Oh, hell no! I’ve watched enough horror movies to know that I’m never supposed to follow a little girl down a dark hallway! That’s how people die!"
    n "But...I also know that people die by staying somewhere they aren’t meant to be for too long and..."
    n "Aaah! This sucks! "

    play sound "static.mp3"
    scene molerat37 with flash
    stop sound

    n "Little girl! How do I get out of this creepy dream?! I don’t even have the egg anymore! It vanished when I walked out of the bathroom!"
    na "..."
    n "I know I told you I could understand you before, but that was {i}prior{/i} to my brain having to come to terms with whatever is going on right now! So if you {i}can{/i} talk, please do so!"
    na "..."

    scene molerat38
    with dissolve

    n "Ugh...who am I kidding? She’s clearly a part of this. And of course that means I’m going to have to play along until I get to the “scare” that wakes me up. Fantastic."

    scene molerat37
    with dissolve

    n "This is {i}not{/i} a good self-introduction! I hope you know that! Because it’s really going to taint the way I look at you from now on!"
    na "..."

    play sound "pabell.mp3"
    $ renpy.pause(2, hard=True)

    scene molerat39
    with dissolve2

    m "{i}Hah....hah....hah....{/i}"
    m "{i}Blackout sex......really is the best......{/i}"
    s "{i}Maya?...{/i}"
    m "{i}Well, well, well...{/i}"
    m "{i}Look who.....finally decided to show up...{/i}"
    s "{i}This...{/i}"
    s "{i}No....{/i}"
    s "{i}We can’t-{/i}"
    m "{i}Don’t you dare...fucking stop...{/i}"
    s "{i}But you-{/i}"
    m "{i}I repeat......{i}don’t you dare fucking stop...{/i}"
    m "{i}God that feels so good. Holy shit.{/i}"
    n "Over the PA?...Really?..."
    n "Girl seriously takes cucking me to the next level, doesn’t she?"
    na "..."

    scene molerat37
    with dissolve

    n "Fine! Okay!"

    scene black
    with dissolve2

    n "Anything that gets me away from {i}this!{/i}"

    "........."
    "......"
    "..."

    scene molerat40
    with dissolve4

    "There are special areas that exist in places and times that only gods would look. "
    "Hidden from the prying eye of the common man and tucked between the moon and its siblings, these places make wishes come true."
    "No one finds them on accident and no one leaves them on purpose."
    "They exist. I promise. But only if you believe in them."
    "If you can separate yourself from where you’re meant to be in the time you’re meant to be there, the limits of where you can be and when are endless."
    "Let’s ride the mole rat together — let’s see where it takes us. Let’s fill our mouths with dirt and rocks, swallowing bit by precious bit until our stomachs are gardens."
    "Let’s hold each other’s hands. Let’s sew them together. Let’s bite each other’s tongues until our mouths taste like metal. And let’s do all of it not because we want to, but because we can’t."
    "Water and oil don’t mix — just like greenery and gasoline or a schoolgirl’s special sex-mound with the Southern White Rhino — both just one wrong move away from non-existence. "
    "There exists a place that you can touch in an area your hands won’t reach. Where flowers won’t bloom and bodies won’t rot. "
    "The water in the pipes has been there for ages and the floors are barely clinging to life in a world all but devoid of it."
    "I think Heaven is a classroom and God is the chalkboard."
    "I think that’s where I want to go when the world ends."

    play sound "static.mp3"
    scene molerat41 with flash
    stop sound

    n "Okay...I’m here...but this doesn’t really look like a principal’s office to me."

    scene molerat42
    with dissolve

    n "I came...just like you asked me to...but I lost the egg along the way and..."

    play sound "static.mp3"
    scene molerat43 with flash
    stop sound

    m "{i}Harder...{/i}"
    m "{i}Deeper...{/i}"
    n "Maya?..."
    m "{i}Akira...fuck me...{/i}"
    n "Uhh..."
    m "{i}Fuck me, Akira...fuck me!{/i}"
    n "..."
    m "..."
    m "Ahh..."
    m "It’s no use..."
    m "My deer parts don’t work in here."

    scene black
    with dissolve2

    "There is a place."
    "It is a place just like others but this place and it won’t but it is because the place and you don’t understand."
    "Each step is a stone and each stone turns to sand so we walk but we’re hard but soft and we’re not and that’s just how the place is sometimes."
    "O, terrible danger. O, big penis sex. O, world and its whirlpool. O, mole ratted necks."
    "O, poetry, pottery, lottery, Shrek. O, rhyming - O, timing - On Dasher, On Deck!"
    "Your hands aren’t as big as mine. If we put them together, all you’ll notice is how much you need to grow. But what you don’t know is mine are shrinking. They just started out big."

    play sound "static.mp3"
    scene molerat44 with flash
    stop sound

    "What you don’t know is not all men are fit to be hunters. All men aren’t fit to tell time. Some play the oboe and some sit inside."
    "But there’s one thing they all have in common."
    "When you strip them, they’re mole rats."
    "Their instinct is to dig."
    "So I think it’s time to start again — from the beginning."
    "I think it’s time for a new world."
    "I think it’s time for a {i}new{/i} world."
    "{b}New world.{/b}"

    n "Um..."
    m "..."
    n "Maya?..."
    m "..."
    n "It’s me...Noriko...that girl you hate..."
    m "..."
    n "I get that none of this is really happening and that it’s probably just my thoughts manifesting into some dream that I’m going to have to interpret later, but..."
    n "For the sake of me feeling less worried right now, could you maybe...tell me what you’re crying about?"
    six "Everything there is to cry about."

    play sound "static.mp3"
    scene molerat45 with flash
    stop sound

    n "Ah-?!"
    six "CHAIR GOD, FLARE GOD, MEET ME IN THE AIR GOD. STARE GOD, BEAR GOD, DO YOU HAVE A SPARE GOD?!"
    n "W...What?..."
    six "SO MANY PIECES, SO LITTLE TIME. WHY SETTLE FOR THREE WHEN THREE MORE JUST MAKES NINE?"
    n "Th..."
    n "Three plus three..."
    n "Is actually six..."
    six "..."
    n "..."

    scene molerat46
    with dissolve

    six "79 6f 75 20 61 72 65 6e 27 74 20 6d 65 61 6e 74 20 74 6f 20 62 65 20 68 65 72 65 "
    n "..."
    n "What?"

    stop music
    play sound "static.mp3"
    scene molerat47 with flash
    stop sound
    play music "remember.mp3"

    ni "Ami, where do you want to go next? Victoria’s Secret? UNIQLO? Or maybe Undercover so Noriko can get lost and we can run away together?"
    a "Anywhere is fine, Niki. I’m happy enough that you decided to take me out. Never in a million years would I have even {i}dreamed{/i} of going shopping with you."
    ni "Oh, shut up. You’re family. Let’s go to Victoria’s Secret. I know people there. I can get you free underwear."

    scene molerat48
    with fade

    ni "Plus, it’ll give us more time to bond since Noriko always wanders off in there and tests the limits of just how much {i}free stuff{/i} I can get. Isn’t that right, Noriko?"
    n "..."
    ni "Noriko? Hello? Anyone home?"
    a "Hey, is everything okay? You look kinda lost all of a sudden..."

    scene molerat49
    with dissolve

    n "Oh! Uhh...yeah!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    n "So, uhh...{i}where{/i} are we going?"

    $ renpy.end_replay()
    $ norikospring2 = True
    $ nao_love += 1

    "{i}Nao-chan’s affection has increased to [nao_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label norikospring3:
    scene norikoamilesbian1
    with dissolve2

    a "Hello, Aunt Niki. I did not expect to see you back in the room so soon. What a pleasant surprise."
    ni "..."
    a "..."
    ni "You’re up to something and I’m going to find out what it is."
    a "Me? I have never been up to anything at any point in my life. I am a normal teenage girl with normal teenage interests. Like skin-care and getting abortions."
    ni "Ami, did you kill my little sister and hide her body in the bathroom?"
    n "{i}Still alive, Nee-chan! But thank you for caring!{/i}"
    ni "Well, if Noriko’s still alive and you {i}weren’t{/i} in the process of murdering her, what-"

    scene norikoamilesbian2
    with dissolve

    a "We were making out!"

    play sound "static.mp3"
    scene norikoamilesbian3 with flash
    stop sound

    s "What? And I missed it?"

    play sound "static.mp3"
    scene norikoamilesbian4 with flash
    stop sound

    ni "You and Noriko...were making out."
    a "That is correct. "
    ni "In the bathroom."
    a "Tongues and all. "
    ni "That...{i}is{/i} how that is done. Yes. "
    a "I grabbed her boobs too. I’m a lesbian now, Aunt Niki. I have seen the light. You can have my dad all to yourself."
    ni "..."
    a "Nothing but vaginas for me from here on out."
    ni "You are a terrible liar. What’s really going on in there, Ami?"

    play sound "static.mp3"
    scene norikoamilesbian5 with flash
    stop sound

    ni "Noriko! If you’ve started smoking or doing drugs or some shit, don’t do it in the hotel! "
    n "{i}Why not?! You aren’t responsible for the security deposit! Your production company is!{/i}"
    n "{i}Also, I’m not doing drugs! I’m just in here also being a lesbian!{/i}"
    a "There you have it, Aunt Niki. Case closed. Nothing to see here. Unless you also want to make out with us. But that sounds logistically improbable."
    ni "{i}Logistically improbable?{/i} Is this rehearsed? Noriko! Get out of the bathroom!"
    n "{i}I can’t! I’m lost!{/i}"

    scene norikoamilesbian6
    with dissolve

    a "Okay, okay! Fine! If you {i}really{/i} want the truth...we..."
    a "Well...we were..."
    n "{i}Having sex!{/i}"

    scene norikoamilesbian7
    with dissolve

    a "You must be so ashamed! To think that I could do such a thing behind your back and desecrate the inn you reserved us just minutes after arriving! "
    a "Please don’t tell my dad! I don’t want him to know about all of the lesbian sex I have with your little sister! "

    play sound "static.mp3"
    scene norikoamilesbian8 with flash
    stop sound

    ni "Do I look like an idiot to you, Ami?"
    a "Um...n...no? You look a lot like...the girl I just made sex-love to, though! And {i}boy{/i} was it good."
    a "Noriko does this thing with her fingers where-"

    scene norikoamilesbian9
    with dissolve

    ni "Okay, Jesus! Whatever it is, I no longer care and I no longer wish to hear about it!"

    scene norikoamilesbian10
    with fade

    ni "{i}You and Noriko can have as many secrets as the two of you want, but I will not let it interfere with the quality time we’re supposed to be sharing before my photo-shoot!{/i}"
    ni "{i}Get your towel. We’re heading to the baths.{/i}"
    a "{i}To have lesbian sex with each other?{/i}"
    ni "{i}OBVIOUSLY FUCKING NOT, AMI! I’M NOT GOING TO HAVE LESBIAN SEX WITH YOU! NOW, COME ON!{/i}"

    play sound "knock.mp3"

    ni "{i}You too, Noriko! I know you’re still alive and only half-gay in there!{/i}"
    a "{i}Wait! Don’t try to open the door! Noriko is-{/i}"
    n "I’m...cumming!"
    ni "{i}Ew! What the fuck?! Why would you say that to me even if you’re clearly lying about it?!{/i}"
    n "Oh god! I can’t stop! This is the craziest orgasm ever! Ami’s raw sexual energy still has an effect on me even though she is no longer here!"
    ni "{i}Fine! Stay in there, then! But don’t come crying to me when Patrice busts down the fucking door and drags you out of there at my command! Ami! Come!{/i}"

    play sound "slidedoor.mp3"
    scene norikoamilesbian11
    with dissolve

    "The door to the hall slides open and the two of us can hear Ami and Niki disappear into the hall."
    "Well...{i}I{/i} can hear Ami and Niki disappear into the hall. Noriko’s ears have likely been destroyed by exposure to loud music, so she’ll just have to take my word for it."

    n "{i}Hah...{/i}you see how much trouble you almost got us into, Onii-chan? "
    n "I don’t want to die in a bathroom. Do I look like Elvis to you? Do you really think I can move my hips the way he did?"
    s "No, but I’d like to find out."

    scene norikoamilesbian12
    with dissolve

    n "Is that really how you should be speaking to your little sister? And also your future daughter in law if this thing with Ami and me works out?"
    s "No, but it’s kind of just reflexive at this point and I’m sorry if it made you feel uncomfortable."
    n "Quite the opposite, actually. It made me feel {i}too{/i} comfortable. And if I wasn’t currently on an all-sister diet, I imagine I’d be on my knees and bowing down to the patriarchy right about now."
    s "How many sisters have you eaten?"
    n "None yet, but I can only assume the count will increase based on the current and inevitable trajectory your toxic polyamory will ultimately have on me in a romantic context."
    s "On the bright side, I actually don’t have an erection right now. So there’s no need for you to get on your knees for any sort of authority figure."
    n "Well, {i}now{/i} I’m just offended. What sort of brother doesn’t get a hard-on when he’s trapped in a tight space with his doting little sister?"

    play sound "static.mp3"
    scene norikoamilesbian13 with flash
    stop sound

    s "Again, there’s {i}so{/i} much room in here."
    n "No there’s not! Stop saying that!"
    s "Noriko, really-"

    stop music fadeout 10.0
    scene black
    with dissolve2

    n "Okay, okay! Fine! I’ll give you some room to {i}breathe.{/i} But just know that I’m not happy about it! And also...extremely confused about what to do now."
    s "Well again, no erection. So-"
    n "Not about that! I know how to give you one of those! I just don’t know what to do about hiding you from Nee-chan since she’ll get even {i}more{/i} suspicious when I don’t go join her in the bath."
    s "Not if Ami distracts her with lesbian sex and Niki gets to fulfill her childhood dream of fucking every surviving member of a family."
    n "Wasn’t Nee-chan’s childhood dream being a mech pilot?"
    s "Yeah. What did {i}I{/i} say? "

    play sound "static.mp3"
    scene norikoamilesbian14 with flash
    stop sound
    play music "wewereangels.mp3"

    "After waiting ten minutes for her sister and my daughter to be sufficiently naked, Noriko smuggles me out of the inn and past a sea of show-biz executives on the way to the rock garden."
    "She says that, through exploring with Kirin, she’s found a few spots where we should be able to get some privacy, but I’m still not really sure what the end goal is."
    "It’s not like she can just stay with me the entire weekend. She’ll have to go back to her sister at some point. So what becomes of me {i}then?{/i}"
    "And was coming here really worth the risk at all when it seems like Noriko just wants to...hang out?"

    n "Oniiiiiii-chan~"
    s "..."

    "{i}Hah.{/i}"
    "Why am I lying to myself again? Of {i}course{/i} it was. And of course {i}I’d{/i} want to hang out with her too as there’s probably no one {i}better{/i} suited to just being a sibling to me."
    "Which isn’t to say I’ve had good luck with such a thing in the past, but..."
    "That’s a bridge we’ll have to cross later. "
    "For now, I’ll just play along and pretend I’m happier than I really am."

    n "So, big brother — now that I’m done yelling at you for putting my life at risk, let me say thanks for how you came all the way over here just to keep me company. "
    n "Assuming, of course, that there’s no hidden motivation of wanting to either keep an eye on Ami or wanting to sleep with Onee-chan."
    s "I wouldn’t hide such motivations, I’d make them eerily apparent. But right now, you {i}are{/i} my top priority since you’re the one who invited me here."
    n "{i}Just{/i} because I’m the one who invited you here? Or because you loooove me?"

    scene norikoamilesbian15
    with dissolve

    s "You know I feel weird about saying that. You can’t just {i}ask{/i} me to out of the blue."
    n "Sure I can! It’s my job to annoy you, isn’t it? Go on, Onii-chan! Proclaim your love for your little sister! No one will hear it but her!"
    s "..."
    n "Oniiiiii-chan~"
    s "Fine. I love you."

    play sound "static.mp3"
    scene norikoamilesbian16 with flash
    stop sound

    n "How much?"
    s "What? We’re not done? I have to quantify it now?"
    n "Only if you don’t want me to cry. So yeah — no big deal."
    s "I’ve made you cry enough, so let’s just go with whatever the maximum amount is."

    scene norikoamilesbian17
    with dissolve

    n "Maximum love?! You mean it, Onii-chan? Even though you’ve given me fewer orgasms than basically everybody I know?"
    s "Is that really something you’re going to bring up in platonic mode?"
    n "It’s not “platonic mode,” it’s “sister mode.” And sister mode comes with an endless supply of flirting and teasing that ultimately doesn’t lead to anything. Except for when it does."
    n "But when it {i}does,{/i} it stays a secret. That only you and I can share. That is the glory of being siblings and knowing that, no matter what happens, you will always be number one in my heart."
    s "Always? Really?"

    scene norikoamilesbian18
    with dissolve

    n "Of course. Why would I lie about that?"
    n "I chased after you for years. You think I’d do that for just anybody?"
    s "No. But I also think you’re mature and smart enough to work your way out of the magnetic field that everyone else you know has gotten caught up in."
    n "You mean, like...falling for someone else one day? Dating them and stuff?"
    s "...Right."
    n "How does that make {i}you{/i} feel, Onii-chan? Like — if I suddenly had a boyfriend one day, what would you do about it?"
    s "I would...try not to think about it."

    scene norikoamilesbian19
    with dissolve

    n "But you {i}would{/i} think about it. Because you {i}love{/i} me. And you want to protect me and keep me all to yourself. Which is exactly how I feel about you! "

    scene norikoamilesbian20
    with dissolve

    n "But, you know...I think there’s an extra layer of suffering that younger siblings just sort of {i}have{/i} to expect since it’s the older ones who obviously get to grow up first."
    n "For example, you and Nee-chan had your first kiss before I was even old enough to comprehend what kissing {i}was.{/i} "
    n "So of course I’d be jealous of all the stuff you can do that I {i}can’t{/i} now that I’m old enough to understand the world around me. "
    s "To be fair though, I don’t think there’s anything I can do that you {i}can’t.{/i}"

    scene norikoamilesbian21
    with dissolve

    n "Sure there is when you remember what your purpose here is."
    s "To...bang your sister?"
    n "To {i}teach,{/i} Onii-chan. Or shall I say — {i}Sensei?{/i}"
    n "Because you get to experience everything first, and because we’re so close, it’s only right that you pass all of that knowledge on to {i}me{/i} so {i}my{/i} life can be a little easier."
    n "Isn’t that the sole job of an older sibling, after all?"
    s "..."
    n "..."

    scene norikoamilesbian22
    with dissolve

    n "Onii-cha-"

    play sound "static.mp3"
    scene norikoamilesbian23 with flash
    stop sound

    s "Disregarding...whatever that was leading to, do we have a plan in mind now? Or are we just aimlessly wandering around in hopes of not disturbing Niki’s motherly bonding opportunity?"
    n "..."
    s "Noriko?"

    scene norikoamilesbian24
    with dissolve

    n "Oh. Well...I guess the first thing we need to figure out is whether or not you actually want to stay the whole weekend or if this is just a...{i}today{/i} sort of thing."
    s "I’ll obviously need a place to sleep if I’m staying for more than just today. And I can’t imagine there are any rooms available if Niki’s production company booked this place for a shoot."

    scene norikoamilesbian25
    with dissolve

    n "I can try and find you an empty one and say it’s for me? Everyone here obviously knows who I am, so I could probably pull it off."
    n "And I doubt there are no vacancies anyway. I think renting out the entire place was more just so Nee-chan’s fans couldn’t catch wind of the shoot and rent out rooms to creep on her."
    s "Yeah. I don’t even want to think of what Chika would do if she knew Niki was here."
    n "Is she still deluding herself into believing you somehow don’t know my sister despite our life-long connection?"
    s "I’ve tried telling her, but I doubt she’ll believe me unless she sees it with her own eyes. The problem with that is I likely won’t live long enough afterward to know how she reacts."
    n "You think you’d be the one in danger and not Nee-chan?"
    s "I’m not the one on posters all over her wall. I just have sex with her. Which I’m sure she’d also want to do with Niki, so..."

    scene norikoamilesbian26
    with dissolve

    n "{i}I’d{/i} put your poster on my wall, Onii-chan. In fact, I’d buy out the whole stock."
    s "Ayane could probably help you make them if you really want. She’s no stranger to hanging me on her bedroom wall."
    n "I might have to do that. Especially with Ami’s birthday coming up. A shirtless poster of you would make a pretty great gift, wouldn’t it?"
    s "Better than anything {i}I{/i} could give her. At least...in terms of things that aren’t attached to my body."
    n "Are you liking being a dad? "
    s "I..."

    scene norikoamilesbian27
    with dissolve

    s "Don’t really know."
    s "It only feels a little different. But I know it makes Ami happy, so...I think that’s where any “joy” comes from if there’s any there at all."
    s "I just feel bad for your sister. She’s trying really hard and Ami just...well, you probably already know since we’re {i}here{/i} in the first place."

    scene norikoamilesbian28
    with dissolve

    n "Yeah."
    n "You know, it’s kind of weird. I haven’t seen her want something {i}this{/i} badly since she started training to be an idol just to get back at you."
    n "And until Ami, I’d never really seen any interest from her in wanting to be a mom...{i}at all.{/i}"
    n "But she’s obviously older now and...I guess reconnecting with the love of her life has made her start thinking more about a future a little bigger than a poster on some girl’s wall."
    s "That’s...why I feel so bad. I can’t give that to her. Not...the way things are now, at least."
    n "Yeah...you’ve got to prioritize Ami before her. Yourself too. So I feel bad for Nee-chan as well."
    s "..."
    n "..."
    n "Maybe someday though. Do you agree, Onii-chan?"
    s "With what? Settling down?"
    n "Yeah. Settling down. Raising kids. "
    n "Mini-vans...trips to the beach...family-pack deals on meat at the grocery store and trying to figure out how to work the new hot pot you picked up from Hard-Off last week."
    s "Sounds like {i}you{/i} do when you’re going to be that specific about it."
    n "I do."
    n "It’s just sad, though..."
    n "Because I’m always the one going with you to buy the hot pot. Or in the backseat of that mini-van, sandwiched between two kids throwing Cheetos at each other."
    n "But I’m never at the table with you when you eat. I never get to sleep in the same room. Hell, the only times I get to be alone with you {i}at all{/i} are when Nee-chan visits our parents."

    scene norikoamilesbian29
    with dissolve

    n "Why is {i}that{/i} the future I envision? "
    n "Being...what, an {i}aunt?{/i} "
    n "Is {i}this{/i} the life I subject myself to by being such a martyr all the time? I can’t even properly {i}dream{/i} now?"
    s "..."
    n "Sorry, I..."

    scene norikoamilesbian30
    with dissolve

    n "I..."
    n "{i}Yeah.{/i}"
    s "I don’t...really know what to say to that to-"

    scene norikoamilesbian31
    with dissolve

    n "Then don’t say anything. I’m content just knowing you’re still {i}there.{/i}"
    n "And that there will always be a role for me in your life, even if it’s not the one that lands me a seat at the dinner table."
    s "Yeah, well..."

    scene norikoamilesbian32
    with dissolve

    s "We were sharing that...family-pack of meat anyway, so..."
    s "You wouldn’t have been able to eat regardless. "
    s "Maybe {i}that’s{/i} why we didn’t save you a seat."
    n "Heheh...maybe. "
    n "Yeah..."

    scene black
    with dissolve2

    n "Still sucks eating alone, though."

    $ renpy.end_replay()
    $ norikospring3 = True
    $ noriko_love += 1

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump nikispring5

label norikospring4:
    "{i}Later that day...in a room so quiet we could hear each other’s hearts beat.{/i}"

    scene norikobrother1 with dissolve4
    play music "sensei.mp3"

    "It didn’t take long for Noriko to find us a safehouse of sorts — just a quick conversation with the woman at the front desk who handed her a room key, no questions asked."
    "It makes me a little jealous, if I’m being honest. How she can just use her role to get the things she wants and then hand them over to me like it’s no trouble at all."
    "I probably {i}shouldn’t{/i} feel that way given the things I have taken when {i}I{/i} wore her shoes, but I do."
    "And I’d go as far as saying it brings back bad memories if all of my memories weren’t already somewhat tainted to begin with."
    "Regardless, here we are — bathed in ambient silence disrupted only by conversations that, while nostalgic, feel more like informative briefings on my past self than anything else."
    "We talk of days past and days yet to come. "
    "Noriko embellishes each anecdote with unimportant details that walk the fine line between just existing for imagery and existing to try and help me remember something."
    "And it works. It works in both regards."
    "I {i}can{/i} remember more of the past now that the largest gaps in time have been filled in by those I’ve loved and either lost or am losing."
    "Yet those pivotal, formative memories that clog my hippocampus like red hair swallowed by the drain disrupt my train of thought when the roots they take sprawl out onto my one-track mind."
    "In taking root, however, I can feel things start to fall into place."
    "I can feel them reaching out and strangling things I’ve subconsciously suppressed, integrating them once more into a network of thoughts and feelings reminiscent of how trees talk to one another."
    "So sit in my shade and listen to the sounds of a nearby station calling out where we are or where we’re headed."
    "There’s only a stop or two left after this one. "
    "And if you miss your train, you might have to spend the night here."

    n "Nostalgic, isn’t it? Sitting next to one another in a dimly lit room — hiding from Nee-chan while we talk about whatever crosses our minds."
    n "If I didn’t know any better, I’d think you might be about to tutor me."
    s "Frankly speaking, I don’t think there’s much left I can teach you at this point."
    n "Oh? Is {i}that{/i} why you gave up on teaching? Just...ran out of relevant information? Assuming of course that you didn’t run out the {i}first{/i} time you left me to fend for myself."
    n "{i}Two{/i} times now you have put my education at risk, Sensei. Two times now, you have pawned me off on someone else and just hoped I’d be able to figure things out on my own."
    s "Three if you want to count my initial departure. But I don’t think I was tutoring you yet back when I ran away from Niki."
    n "That’s why I excluded it. It’s important to mention that you didn’t {i}just{/i} run away from Niki, though. You ran away from all of us."
    n "My mom still asks about you all the time. It’s always, “Where’s my son? Where’s Akira? When’s Akira coming to visit?” every time I help out at the restaurant or drop by to say hello."

    scene norikobrother2
    with dissolve

    s "I’m surprised she still cares at all after everything I put you guys through."
    n "{i}I’m{/i} not. She probably understood what you were going through better than either of {i}us{/i} back then. We were just confused and betrayed."
    n "But we get it {i}now.{/i} And we don’t blame you for it, Onii-chan."
    s "Niki still blames me for it. She’ll never let me live that down."
    n "Sure. But Nee-chan only blames you on the surface. Deep down, she understands. That’s why she still loves you so much when, realistically, she could bag any boy {i}or{/i} girl in this city."

    scene norikobrother3
    with dissolve

    n "That said, I can’t help but feel a {i}little{/i} angry that you keep letting me wander off on my own instead of continuing to cultivate my mind in ways only an older brother could."
    s "By filling it with worry and doubt and any other negative emotion you’d be burdened by receiving from me?"

    scene norikobrother4
    with dissolve

    n "You always say that, but you’ve been my teacher twice now and have never filled me with worry or doubt either time."

    scene norikobrother5
    with dissolve

    n "At least until you started messing around with Maya. I will concede that I may have been worried {i}then.{/i} "
    n "But back then, it was mostly just worries about how you were starting to favor her over me. And {i}not{/i} so much worrying about what I {i}should{/i} have been worrying about."
    s "Which was..."

    scene norikobrother6
    with dissolve

    n "How the {i}hell{/i} you were managing to fit it inside of that little girl."

    scene norikobrother7
    with dissolve

    s "That was...more vulgar and direct than I expected to hear. But yes. That’s exactly what you should have been worried about. But you weren’t. "
    s "So you subjected her to a life of wanting nothing but {i}me{/i} and I’m sure I don’t need to inform you how terrible {i}that{/i} is."
    n "You sure don’t..."
    n "Do you regret it, though? Doing those things with Maya? Tutoring? All of it? Is there not a single bright spot to be found in any of those years?"

    scene norikobrother8
    with dissolve

    s "Sure there is. I have you, don’t I?"
    n "Heheh~ Correct answer, Onii-chan! You’ve learned well from today’s marathon of sibling love. The time has clearly come for me to begin tutoring you instead."

    scene norikobrother9
    with dissolve

    s "It’s been a good day...yeah."
    n "Mm...it must be if it can do...whatever {i}that{/i} is to your face. "
    s "I think kids these days are calling it a “smile,” but you’d know more about that than me."

    scene norikobrother10
    with dissolve

    n "I don’t know, Onii-chan. You’re pretty clearly the one more {i}experienced{/i} with kids between the two of us."
    s "Okay. Smile gone. And remind me to never try to do that in front of you again."

    scene norikobrother11
    with dissolve

    n "Now {i}why{/i} would I do that? It’s a little sister’s sole mission in life to make her big brother smile, isn’t it? Otherwise, he won’t want to protect her from potential evil suitors."
    n "I’m too nice to face all those evil suitors on my own, Onii-chan. I need you to reject them for me. And beat them up if they try to get too handsy. "
    n "Just maybe not {i}too{/i} badly or you’ll wind up having to spend your days with Uta’s brother instead of an idol, a bunch of MILFs, and an entire high school. "
    s "Is it just me, or is that bright spot I referenced earlier starting to get a little dim?"

    scene norikobrother12
    with dissolve

    n "Hey! I take great pride in being your bright spot! And if anything, you’re super lucky I’m still glowing after all these years!"
    s "If anything, you’re lucky it wasn’t {i}you{/i} in Maya’s shoes back then. Because I imagine our relationship now would be a lot different if you were."

    scene norikobrother13
    with dissolve

    n "You mean like if you touched {i}me{/i} and stuff instead?"
    s "Yes. But not if you’re going to say something like “I wish you did” or any of those other things I know you only say to try and appeal to me when you’re clearly better than that."
    n "I {i}am{/i} better than that. And I’m {i}glad{/i} it wasn’t me in Maya’s shoes back then because I don’t think I’d be able to look at you the same way I do today."
    n "Mistakes are harder to forgive when they happen to you. "
    s "They’re {i}still{/i} happening, though. And they {i}have{/i} happened to you. Do I need to remind you of the age gap here? Or have you just forgotten about that like everyone else?"
    n "I actually think it’s more of a split between those who “forget” about it and those who lean into it because they think it’s hot. "
    s "You forgive me either way, though. And that’s because {i}you’re{/i} caught in the web as well."
    n "I do forgive you and I {i}am{/i} caught in the web, yes. But that has nothing to do with {i}why{/i} I forgive you."
    s "Then...why? What else would just let you keep overlooking {i}mistakes{/i} like the ones I’ve made? Because you’re not {i}stupid.{/i} And I know you’re impulsive, but-"
    n "Because we’re family, silly."

    scene norikobrother14
    with dissolve2

    n "And no matter what happens, you’ll always be my brother first and a {i}man{/i} second. "
    s "But..."
    s "Why...do you still so relentlessly pursue me then?"
    n "One does not {i}choose{/i} to be a brocon. One is simply born that way."

    scene norikobrother15
    with dissolve

    s "Noriko-"
    n "Don’t “Noriko” me. I’ve been nothing but gleefully platonic all day long and I’m not about to get scolded for a bunch of stuff I’ve said or done in the past."
    n "If you want me to be your sister and nothing else, that’s what I’ll be. And I’ll be happy doing it because, again, I love you like you share my blood."
    n "And that’s probably not the most appropriate or...normal way to word that, but it’s the truth. {i}You{/i} are my brother. "
    n "And every single time I get to look at you and say “Onii-chan,” it’s like there’s a surge of energy coursing through me that makes me feel like I can do anything."
    n "And with you by my side, I think I {i}can.{/i} That’s why I’m still in the background of my fantasies. That’s why I can forgive you for all the “mistakes” you make with my friends."

    scene norikobrother16
    with dissolve2

    n "I love you in ways that only a younger sibling {i}could.{/i} And you don’t need to understand it, but-"
    s "Good. Because I {i}don’t{/i} understand it."

    scene norikobrother17
    with dissolve

    s "And it’s not...{i}just{/i} because you also want to fuck me sometimes. "
    s "It’s because I inherently don’t understand why that...familial connection alone would bring you {i}joy{/i} when it did nothing but fucking...{i}terrorize{/i} me for my entire life."

    scene norikobrother18
    with dissolve2

    n "..."
    s "..."
    n "Sorry, I..."
    n "It’s just..."
    n "You mention your brother so rarely, I...forgot you even {i}had{/i} one."
    s "Yeah, well..."
    s "{i}That’s{/i} why I have a hard time understanding the way you feel about me. And how you can be so happy to have something {i}I{/i} was so..."
    n "..."
    s "So...{i}afraid{/i} of."
    n "Afraid?..."
    n "{i}Why?{/i}"

    stop music
    play sound "static.mp3"
    scene norikobrother19 with flash
    stop sound
    play music "glasswalker.mp3"

    s "He had everything I didn’t. He was everything I’m not."
    s "And He lorded it over me as if He was God himself."
    s "He blamed me for what happened to my father. He blamed me for what happened to my mother. And I {i}believed{/i} Him. "
    s "I {i}believed{/i} Him because I saw what He was and I saw what {i}I{/i} was and it was...night and fucking day, Noriko."
    s "I was weak. He was a man. I was small. He was this...fucking colossus. I can’t even...I don’t...there are no words to explain how different we were."
    s "He’d lock me in the closet for days at a time. Tear up my clothes. Piss on me. Make me act and...bark like a fucking dog just so I could {i}eat.{/i}"
    s "But it was less like being a pet and more just...something to step on. And kick...and beat...and just genuinely fucking terrorize and abuse..."
    s "And I didn’t have anyone to protect me from that."
    s "At least...not at first. "

    play sound "static.mp3"
    scene norikobrother20 with flash
    stop sound

    s "But then He met someone."
    s "A girl. "
    s "With beautiful red hair and a soft, delicate voice — who dressed like a character from an old movie and wrote poetry that could move even the most heartless of monsters."
    s "She didn’t know I existed at first. But one day, she must have heard me."
    s "I can still see it...the glare of the sun when she pulled open the door of the closet. Him, towering over her, laughing like He’d forgotten I was in there."
    s "She looked at me...and her eyes immediately doubled in size. But before I could pull the door shut, she..."
    s "She turned around and slapped Him so hard that, for the first time in my life, I got to see {i}Him{/i} on the receiving end of physical pain."
    s "“How long has he been in there?!” she asked Him. And I can’t remember how He replied, but..."
    s "The next thing I knew, she was pulling me out. And crying on {i}my{/i} behalf while I just...stood there. Sweaty. Covered in piss. Worried I’d get her dress dirty."
    s "That’s why I can’t stand when people call her a monster. Because she wasn’t."
    s "She was the first person to ever show me there was more to life than what I had."
    s "I never slept in the closet again after that. From that point on it was just-"

    play sound "static.mp3"
    scene norikobrother21 with flash
    stop sound

    s "...Wait, when did we start holding hands?"
    n "Akira...why?"
    n "Why haven’t you ever told me this?"

    scene norikobrother22
    with dissolve

    s "I haven’t told {i}anyone.{/i} You’re the first."
    n "But why did you wait so long?...Why did you keep that inside for so many years? Didn’t it hurt? {i}Doesn’t{/i} it hurt?"
    s "I mean, He’s dead now. So I got the last laugh in the end."

    play sound "static.mp3"
    scene norikobrother23 with flash
    stop sound

    n "What about Ami?...Does she know he put you through all of that? That girl was her mom, right? And she-"
    s "No, and I’d prefer it if she didn’t. So please don’t say anything to her about it. I’m trusting you, Noriko."
    n "Of course, Onii-chan. But-"
    s "If it’s okay, can we not make a big deal out of this right now? Because it’s starting to feel a lot like the time your {i}sister{/i} got me to stop repressing something and that really sucked."
    n "So Nee-chan...doesn’t know either?"
    s "Nope...just you."
    n "..."
    s "..."
    n "Why?"
    s "..."
    n "You’ve never put me first before. "
    n "Why now?"
    s "I just...didn’t like that whole “seeing you as more of a brother than a man” thing when both of those words cut pretty deeply in certain contexts. To me, at least."
    n "Should I not call you my brother anymore then?"
    s "You can call me whatever you want. It’s fine if it’s you. "
    s "But I’d feel more comfortable knowing you just look at me as “me” rather than a {i}brother{/i} or a {i}man{/i} or...even a {i}teacher.{/i}"
    s "I’m Akira. You’re Noriko. That’s it. That’s all it needs to be. "
    n "..."
    s "..."

    "I’m not sure how long we stay like this for."
    "But I’m pretty sure of where it’ll go if we don’t break apart."

    scene norikobrother24
    with dissolve2

    s "Noriko, I..."
    s "I don’t know if...we should really be...you know."
    n "Know what? Say it."
    s "..."

    scene norikobrother25
    with dissolve2

    n "..."
    s "..."
    n "{i}Say it.{/i} "
    n "What shouldn’t we do? "
    n "What don’t you want to do with me?"
    s "..."
    n "And what happens if {i}I{/i} want to do it with you?"

    scene norikobrother26
    with dissolve2

    s "..."
    n "It was a mistake telling me to look at you as just “you” Akira. "
    n "When I do that, it suddenly becomes a lot harder to stop myself from acting out on certain things."
    s "Sure. But what you’re feeling isn’t love or lust right now...it’s pity. You don’t know how to handle being the only person who knows something about me. So your mind is going haywire and-"
    n "Don’t tell me what’s going on in {i}my{/i} mind. Not when you can’t even figure out what’s going on with yours."
    n "Because I can forgive you for keeping all of this inside to protect yourself. And I can forgive you for not {i}wanting{/i} to tell anyone now because it’s hard or it hurts or it’s embarrassing."
    n "Fuck, I can forgive you for almost {i}anything{/i} because of who you are and what we {i}have.{/i} "
    n "But if you hand me a piece of yourself that I get to keep and {i}I{/i} don’t get to give any part of myself to you?..."
    n "How is that fair?"
    n "How is {i}any{/i} of this fair?"
    n "And how can you look at me — {i}Noriko{/i} — while I look at you as Akira and not find yourself drowning in a lifetime worth of wanting?"
    n "Because you might be perturbed by the thought that I would see you as a {i}man...{/i}but I {i}want{/i} you to see me as a woman.  "
    n "And I want you to love me the way {i}you{/i} love. Because if you don’t now, I might never believe you."
    s "This is exactly how it ended last time and now your sister lives in my house..."
    n "I am {i}not{/i} my sister. "
    n "I am my {i}own{/i} person who feels and thinks and wants and loves. And I am {i}tired{/i} of pushing all of that aside in favor of other people."
    n "But I will not choose {i}for{/i} you. And if you decide that you want a sister and nothing else, all you need to do is stay silent in response to the following haiku."
    s "A haiku? Now?"
    n "What’s wrong? You like poets, don’t you?"
    s "I mean...that’s not {i}exactly{/i} true. It’s just that...it’s easier for me to understand someone’s feelings when they’re conveyed in a way that-"
    n "Then understand this, Akira."
    n "If you take me here..."
    n "You will have me forever."
    n "There is no escape."

    scene norikobrother27
    with dissolve2

    s "..."
    n "..."
    s "..."
    n "..."
    s "..."
    n "..."
    s "..."
    n "..."
    s "..."
    n "..."
    s "That is fine by me."

    scene norikobrother28
    with dissolve2

    s "I’m sick of running away."
    s "You’ve suffered enough."
    n "..."
    n "A haiku..."
    s "It took me a second to think of one. Sorry for the suspense."
    n "So..."
    n "Does this mean..."

    scene norikobrother29
    with dissolve2

    s "It means you’re going to have to stop crying or I won’t be able to go through with this."
    n "I don’t think I can. All the confidence I had a second ago has now been replaced by nerves. This feels too real. Like I’m...dreaming or something."
    s "Do your dreams {i}normally{/i} begin with me trauma dumping all over you?"
    n "No. But they normally {i}end{/i} with you on top of me. "
    s "Then what do you say we make half of a dream come true tonight, Noriko?"
    n "Mhm..."
    s "You realize that by doing this, you’ll effectively be committing incest, right?"
    n "Mhm! Mhm..."
    n "It’s okay if it’s you...Onii-chan."

    scene norikobrother30
    with dissolve2

    s "Then stop looking so scared...I’ll take good care of you."
    n "I’m sure you will. {i}Very{/i} sure. Just...what if Ami is hiding in the closet or something? I still have PTSD from that."
    s "Then she takes after me in even more ways than I thought."
    n "Not funny, Onii-chan. I don’t want this to set a precedent in which you start making self-deprecating trauma jokes around me from now on."
    s "I wouldn’t worry about that. I don’t think I’ll have much time for jokes at all between everything I want to do to you."
    n "Oh god...I’m about to cum and we haven’t even started yet."
    s "Yes we have..."

    play sound "static.mp3"
    scene black with flash
    stop sound
    play sound "tackle.mp3"

    n "Aaah! Onii-chan! Or...A..Akira? What do I...uhh...how should I-"
    s "Let’s go with {i}Onii-chan{/i} today. You’re at your cutest when you’re being my little sister."

    play sound "zipper.mp3"

    s "Which is why I’m already like this."
    n "{i}Hah!{/i} Onii...chan!~ {i}Ah!{/i}"

    $ renpy.end_replay()
    $ norikospring4 = True
    $ noriko_love += 10
    $ noriko_lust += 10

    jump norikospring5

label norikospring5:
    if _in_replay:
        play music "glasswalker.mp3"

    scene norikovirginity1
    with dissolve2

    n "Wait! Wait! Stop! I need like five minutes first! "
    s "For what? You’re the one who talked me into this. I was just going to awkwardly sit there for the rest of the night."
    n "Yes, but it only just {i}now{/i} occurred to me that I’m not wearing the right panties for this! I have too many expensive pairs to lose my virginity in plain- "

    scene norikovirginity2
    with dissolve
    with hpunch

    n "Ngh! O...nii-chan! W...Wait!!!"

    "Without any intention of {i}waiting{/i} whatsoever, I proceed to grind myself against Noriko with little regard for her choice of underwear. "
    "And while the friction of the cotton on my flesh and the warmth of her body do combine to create a sensation that’s already close to walking on air, I’d be lying if I said I didn’t want more."
    "I think I’ll enjoy taking my time with her tonight instead, though. Especially when that hair trigger of hers already has her on the precipice of climaxing from mere {i}contact{/i} with me alone."

    s "You really {i}do{/i} want to cum already, huh?"
    n "Mnh...nhg...nuh-h!"
    s "Oh, okay. Then you won’t mind if I keep going."
    n "Nope! Go right ah-"

    scene norikovirginity3
    with dissolve
    with hpunch

    n "HAAAAH! ONII-CHAN! ONII-CHAN! STOP, STOP, STOP! AT LEAST PUT IT IN BEFORE-"

    play sound "static.mp3"
    scene norikovirginity4 with flash
    stop sound

    s "No. "
    n "Mnghhg?!? No?! You mean you’re just gonna keep grinding it against me like that?! But I want you to take me {i}now!{/i}"
    s "And {i}I{/i} want to keep teasing you because I like the face you’re making. Now stop holding back and just cum for me already. It’s fine."

    scene norikovirginity5
    with dissolve

    n "{i}Embarrassing{/i} is what it is! But...fine! Because it’s...ahh....what...Onii-chan wants!"
    s "Don’t close your eyes either. Look at me."

    scene norikovirginity6
    with dissolve

    n "Oh god...you have so many rules! Anything else...Onii-chan? Or can I...aah...aaaah...sc...scratch that!"

    scene norikovirginity7
    with dissolve

    n "No time...for questions! It’s happening ! Onii-chan! I’m cumming! I’m cumming! I-"
    s "{i}Look at me{/i} and say it. Don’t look away."

    scene norikovirginity8
    with dissolve2

    n "Nnghgghg! Mmmnh! Nii-chan...Nii-chan! Mnhh! Mnh!!!"

    scene norikovirginity9
    with dissolve2
    with hpunch

    n "NGAAAAAH! AAAAH! YES! CUMMING! I’M CUMMING! BUT...FUCK! FUUUUUUUCK! AAAAH!! HOW AM I SUPPOSED TO...KEEP MY EYES ON YOU IN A SITUATION LIKE THIS?!"
    n "IT’S...IMPOSSIBLE! AAAH...AAAAH! HYAAAHAHHAHHH!! ONII-CHAN! ONII...CHAAAAN!"

    "Noriko shakes and squirms beneath me, wriggling around and searching for an escape like an animal who was just hit by a car."
    "It’s something I’d normally quell by pressing down on a girl’s shoulders or applying enough pressure with my waist that it would {i}at{/i} least hold her lower body in place, but not tonight."
    "Tonight, I’ll do everything I can to make this feel less like one man’s infinite journey for adolescent pleasure tools and more like a dance between an instructor and his pupil."
    "The wetness that escapes from between her legs is undeniable now — which isn’t to say I doubted it before. But it’s a welcome reminder of what I can do to this girl with no work at all."
    "But it’s an omen too — for I imagine that the two of us will likely drown in this room if we keep this up."

    scene norikovirginity10
    with dissolve2

    n "{i}Hah...haaah...haaaah...{/i}"
    s "Easy to please as ever."
    n "Your little sister...mngh...is a naughty girl...Onii-chan..."

    "I continue grinding against her, but now that her first wave of unbearable pleasure has passed, she has less of an issue locking eyes with me."
    "I don’t flash back to when she was younger in response, though. Or internally reminisce about the days where she used to sit on my lap in her parents’ home."
    "Now, what I see is a partner. Someone I can share things with and {i}do{/i} things with. Someone I understand enough to {i}love{/i} beyond the reach of what I’m typically capable of."
    "And if she can look like {i}this{/i} despite knowing that her legs are spread for the abomination that I am, well..."
    "That makes {i}me{/i} want to cum prematurely as well."

    n "Ah.......{i}aaah.........{/i}"
    s "Mngh.....mnh...."
    n "That can’t feel...good for you, Onii-chan..."
    n "Just...rubbing against my panties like that..."
    n "Don’t you want to put it inside of me, big brother?...{i}Don’t you?{/i}"
    s "Yes, but-"

    scene norikovirginity11
    with dissolve

    n "Great. Then let me help you with that."
    s "Noriko-"

    play sound "static.mp3"
    scene norikovirginity12 with flash
    stop sound

    s "Mngh!"
    n "Sooooo {i}big...{/i}but I wonder if I can make it bigger?"
    n "You might have to work extra hard to fit this inside of me, Onii-chan. It’ll have to be a {i}reaaaaaal{/i} team effort. But don’t worry, I’ll be with you every step of the way."
    s "Noriko..."
    n "Yeah...that feels good, doesn’t it? "

    scene norikovirginity13
    with dissolve2

    n "You can feel how wet I am when I do this, right?"

    "She arches her back up to make up for the gap between our bodies she created when she decided to begin stroking me. "
    "{size=-1}And while I’ve slumped over to the degree where I can no longer make out her face, I can still feel her stare as she teases the head of my cock, smearing precum across it to prepare me for what’s next.{/size}"

    n "Do you want to cum too? It would even the score. And I don’t particularly care about this dress in the first place."
    s "I...{i}can{/i} feel it...how badly you want me."
    n "Would you believe me if I told you that’s my default setting? That just being {i}near{/i} you gets me all hot and needy, Onii-chan?"
    s "I...would, actually. You haven’t exactly been...subtle about that."
    n "Yeah, but I bet it’s different hearing it while I jerk you off. That’s why it just twitched."
    n "Go on. Cum for your little sister. I promise I won’t tell."

    play sound "static.mp3"
    scene norikovirginity14 with flash
    stop sound

    n "Ah! So aggressive all of a sudden. Am I in {i}trouble?{/i}"
    s "You’re not in trouble. I just don’t want to ruin your dress. "

    scene norikovirginity15
    with dissolve2

    n "{i}Interesting.{/i} I didn’t think you cared much for this one."
    s "I didn’t until today. It has a special place in my heart now since it’s the one you wore when I took your virginity."

    scene norikovirginity14
    with dissolve2

    n "Are we...starting then? You don’t want to...cum first? Even the score?"
    s "I just told you I don’t want to ruin your dress. "
    n "I can suck it? Find some tissues? I’ll do all sorts of things, Onii-chan."
    s "Correct me if I’m wrong, but weren’t you begging me to fuck you a minute ago?"
    n "Yeah. But then the orgasm wore off and I achieved clarity. Now I’m just regular horny again."
    s "Got it. So all I need to do is bring you close to cumming again. How hard could that be?"

    scene norikovirginity16
    with dissolve

    n "W-Wait! No! If you start rubbing me there again, I-"

    scene norikovirginity17
    with dissolve
    with hpunch

    n "{i}Ah!{/i}"
    s "So weak...so adorable."
    n "Haah...aaah...Onii-chan...it’s like...my mind goes blank...each time you...aaaah..."
    s "Do {i}you{/i} want to cum again, Noriko? Before we begin. Because I can do all sorts of things too. You loved it when I fingered you, right?"
    n "Y...Yes, but...it was...over too soon..."
    s "Everything with you seems to be over too soon. We’ve gotta work on your stamina or you’ll start passing out before I finish."
    n "Haaaah....{i}aah!{/i}"
    s "Look at me if you’re going to cum again. And try to keep your eyes open a little longer this-"

    scene norikovirginity18
    with dissolve2

    n "{i}Fuck me...{/i}"
    s "..."
    n "{i}Now...{/i}"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene norikovirginity19
    with dissolve2

    n "MNNGHHGHHGHH!!! ONII...ONII-CHAN! ONII-CHAN’S INSIDE! F...FINALLY! AAAH! OH MY GOD...IT’S SO BIG...WHY IS IT SO BIG, ONII-CHAN?!"
    s "I’ll be gentle. Don’t worry."
    n "Can...can you just...hold it there for a second?! It...aaah...haaaa!"
    s "I know it hurts, but-"
    n "No, not that! I’m cumming again! It only hurts a little!"
    s "Oh. Then no, I won’t stop if that’s why you’re asking."

    scene norikovirginity20
    with dissolve

    n "Then...ah! Wait! No! It hurts! It {i}really{/i} hurts, Onii-chan! I’ve never felt pain like this be-"

    play sound "dosex.mp3"
    scene norikovirginity21
    with dissolve
    with hpunch

    n "AAAAAHHHHAA?!?!! AAAHH! ONII...CHAAAAAN! STOP! WAIT! I CAN’T! I’M GONNA...AAAH!! AAAH! HAAAAH!"

    "Again, she wriggles around like a dying animal — contorting her body as much as she possibly can without any hope to ever {i}truly{/i} get away."
    "It’s like she said, after all. There is no escape. And I intend to make that as evident as possible as many {i}times{/i} as possible for the rest of the weekend."
    "And then again after that. Every other weekend. Every other {i}day.{/i} As many times as I can before the two of us grow old and {i}can’t{/i} do things like this anymore."
    "And if there are other timelines out there...ones where she never finds me again....the types of worlds that Maya used to dream of..."
    "I will find Noriko myself."
    "And I will take her here, to make a half a dream come true."
    "In every life, I will see to this. Because I can count the moments that have made me happy on one hand, and {i}this{/i} is among them."
    "I just always forget how much I love her when she’s just...Noriko. And I’m just Akira."

    n "Aaaah! AaaAAAaAaaah! Aaaaahhhh! Onii...chaaaaaaan!"

    "And we’re also apparently very sexually compatible."

    s "Noriko...I’m..."

    scene norikovirginity22
    with dissolve2

    n "Aaaah finally! It’s not just {i}me{/i} anymore! Do it inside!"
    s "You’re sure?"
    n "Yes! I like this dress too now! And I can only hold back this orgasm for like five more seconds max!"
    s "Not...necessary!"
    n "Onii-chan! Onii-chan! Onii-chaaaaan!"

    with sexfade
    with sexfade
    scene norikovirginity23 with cumflash
    with hpunch

    s "!!!!!!!!!!!"
    n "{i}NGH!!!!!?!!?!{/i}"

    "With a final violent thrust, one that penetrates deeper than I probably should during her maiden voyage, I spill my seed inside of her and hold myself there until everything’s been purged."
    "Her lower body twitches, siphoning my essence as she shifts herself and inches forward, pulling even {i}more{/i} of me inside as if to say we’re not done yet."

    play sound "static.mp3"
    scene norikovirginity24 with flash
    stop sound

    "And we weren’t."
    "We’re not."
    "We tear each other’s clothes off and get right back to it — with Noriko on top this time at her request."
    "She straddles me, pulling herself forward and dragging my cock along with her as it presses firmly against her dampened flesh."
    "As her hands explore my body, embarking on an adventure I couldn’t even tell you how long she’s hoped to go on, I remain fixated on her gaze."
    "At least during the moments where she isn’t wiggling her ass and I’m not tempted to break away and see how she looks from behind. "
    "The {i}rest{/i} of the time, though, it’s her stare and mine — battling one another for dominance. Like whoever looks away first is conceding that their love is weaker."
    "I’d be fine with losing that battle most nights. "
    "Not this time, though."
    "{i}This{/i} time, there is nothing that could break us apart."

    n "You know, Onii-chan — now that we’ve finally done it, I think it’s gonna be a little harder to control me going forward."
    s "As if I’ve ever controlled you at all..."
    n "I mean {i}sexually{/i} this time. So don’t be surprised if I come knocking in the middle of the night and begging for my big brother to help me cum."
    s "Well...at least it won’t take long."
    n "Ha-ha. Very funny. But you can do the same for me too, you know. Now that we’ve crossed the line, I’ll be yours whenever you want me. {i}Wherever{/i} you want me."
    n "And you’d {i}better{/i} want me, Onii-chan. Because the floodgates have opened. And you’re going to see that maybe I {i}am{/i} a little bit crazy after all."
    s "You’ll be on call then? A little sister who {i}always{/i} does what her brother asks?"
    n "{i}Always.{/i} Family comes first, after all."
    s "You’re starting to sound like Ami."
    n "Oh {i}yeah?{/i} Does that turn you on?"

    if amifingered == True:
        n "Who do you like fucking more? Me or her?"
        s "Well, the...sample size with you is much smaller."
        n "Then it looks like I’ve got some catching up to do."

    else:
        s "Not...particularly."
        n "Ooooh? Then why are you still so hard, Onii-chan? "
        s "Probably because there’s a hot teenager straddling my waist who keeps calling me “Onii-chan.” "
        s "And while I can’t speak for everyone, I’m hard pressed to believe this wouldn’t be a major turn on for most men."
        n "Just {i}most{/i} men don’t get to fuck me. Only {i}you{/i} do."
        s "Well...what are you waiting for then? You wanted to be on top after all."
        n "I’m not waiting for anything anymore."
        n "{i}Itadakimasu.{/i}"

    play sound "static.mp3"
    scene norikovirginity25 with flash
    stop sound

    n "HYAAAAH! AAAAH! YES! OH...FUCK! FUUUUUCK! IT FEELS JUST AS GOOD ON TOP! "
    s "Well you better start...brainstorming which position you want next because...we’re not even close to done yet..."

    scene norikovirginity26
    with dissolve

    n "Hah! Haaah...pick me up next...I’ve been...fantasizing about that one for...{i}years...{/i}"
    n "Granted I’ve been...fantasizing about fucking my big brother in {i}general{/i} for years now...but something about you...pounding me while...my legs are wrapped around your back...haaah...."
    n "Fuck...I’m already gonna cum again! Are other girls this...weak too?!"
    s "Not as {i}weak{/i} as you, Noriko..."

    scene norikovirginity27
    with dissolve

    n "Then I clearly just...love you the most! And I’m clearly...more respectful...of all of your hard work! Still...going so hard...even though I’m on top!"
    s "You’re not the only one who’s...uncontrollable right now...and you’re {i}definitely{/i} not the...only one who’s spent years fantasizing about this..."

    scene norikovirginity28
    with dissolve

    n "That’s...haah...creepier when it...comes from you...Onii-chan! And also...a lie!"
    n "You’ve had plenty of...opportunities to...{i}fuck{/i} me since we reunited! I can’t believe you...held on this long! You...regret it now, I bet...don’t you?!"
    s "Yes...I regret it all...Noriko...but I’ll...make up for it..."
    n "Can I get that...in writing? Just so you don’t...ditch me to go fuck one of my {i}rivals{/i} again?"
    n "Because I’m...aah...still pissed off about that...Onii-chan! I played you...a song! I came for you...in public!"
    s "A secluded spot on a beach is...hardly {i}public,{/i} Noriko..."
    n "Close...enough! You still left me there all...sad and horny! And stuck...getting cucked by Maya {i}again!{/i} Which isn’t even...counting all the times you {i}fucked{/i} my roommate!"
    n "But now, big brother?...{i}I’m{/i} the one who gets you..."
    n "It’s {i}my{/i} pussy you have the...pleasure of {i}pounding{/i} all night long while everyone else has to...be all...sad and horny! "
    n "There’s also...other stuff I want to yell at you for, but...I think I’m about to cum again, so...that stuff can wait!"
    s "Good...I find that sex is...way hotter when...I’m not being scolded..."

    play sound "slidedoor.mp3"

    n "And {i}I{/i} find that it’s...way hotter when-"

    play sound "static.mp3"
    scene norikovirginity29 with flash
    stop sound

    n "N...Nee-chan is here?!"
    s "Unexpected kink, but-"
    n "No! No! Nee-chan is here! {i}Literally{/i} here! Right there!"
    a "Oh. There they are."
    ni "...................."
    a "See? I told you I would worry if I were you. Now you don’t have to think I’m crazy anymore."

    play sound "static.mp3"
    scene norikovirginity30 with flash
    stop sound

    n "Uhh...h...heeeey! Um...you...I..."
    n "I can...explain?..."
    ni "..............."
    s "Niki?..."
    ni "{i}Akira...{/i}"
    a "Hi, guys! I tried to hold her off as long as I could. You’ve been together for a {i}while{/i} though and I would like a turn now."
    n "N...Nee-chan! I...this is actually...we’ve never...before today, I was still-"
    ni "That’s my {i}sister...{/i}"

    scene norikovirginity31
    with dissolve2

    s "I-"
    ni "You were there when she was {i}born.{/i}"
    n "Nee-chan, I started it! {i}I{/i} pressured him into this! If you’re going to be mad at anyone, be mad at-"

    play sound "dosex.mp3"
    scene norikovirginity32
    with dissolve
    with hpunch

    n "AAH! N...NII-CHAN?! WHAT ARE YOU-"
    s "Just...ignore them! Focus...on me!"
    n "Nii-chan, no! If you do it like that, I-"

    scene norikovirginity33
    with dissolve

    n "Aaah! Stop! Stop! Onii-chan! I’ll cum! You’ll make me cum! We can’t! Nee-chan is...she’s right...aaaah! AaaAAaAAaah!"
    ni "................."
    a "You know, in a really roundabout way, couldn’t you sort of call this character growth?"

    play sound "static.mp3"
    scene norikovirginity34 with flash
    stop sound

    n "AaaAAaH! HAAAH! I’m sorry...Onee-chan! I’m sorry! I can’t...aaaaAAAaaah! HaAaAAAhhh! Cumming! Don’t...look at me! Don’t...look!"
    ni "............."
    s "Mnh...mngh!"
    n "Aaah! Yes! YES! Right there! Oh...fuck! Onii-chan! Onii...chaaaan!"
    ni "Akira, is this {i}actually{/i} happening? Or am I just having a very strange, very inappropriate dream right now?"
    s "This..."
    s "Is who I am...Niki..."
    s "This...is what you...swore to never leave..."
    s "I tried to...warn you! I tried to...push you away! But you just...wouldn’t stop...loving me!"
    ni "So you {i}fuck{/i} my little sister? Weird flex, Akira. Can’t say I’m a fan."
    n "It’s...not like that...Nee-chan! I...aaah...really {i}did...{/i}pressure him! I’ve been...NGH...doing it...for years! I’ve always...mngh...had feelings...for Akira.....too! FUCK! Onii-chan! Please...slow down!"
    ni "Why are you still going? Why aren’t you stopping?"

    play sound "static.mp3"
    scene norikovirginity35 with flash
    stop sound

    s "Because that’s...unfair to {i}her!{/i}"
    s "You’re not...the only one who loves me, Niki! Noriko...she’s known me...just as long! She loves me...just as much!"

    play sound "static.mp3"
    scene norikovirginity36 with flash
    stop sound

    ni "Again — {i}you were there when she was born.{/i} She quite literally can not have known you {i}just as long.{/i}"
    s "She still...loves me...just as much!"
    ni "Think that maybe being around to help raise her plays any part in that?"
    n "Mngh...mnhh! Onii-chan...p...please...s...slow down!"
    ni "{i}Onii-chan...{/i}She even calls you that while you’re doing {i}this,{/i} huh?"
    n "It really is...the first time...Nee-chan!"
    ni "Oh, okay. Well, that’s totally fine then. "
    ni "Because if there’s a “best” time to take your girlfriend’s little sister’s virginity, it’s while that girlfriend is on a trip with your daughter, trying to learn how to be a better mom."
    s "Hngh...hngh....Noriko...you’re so fucking tight...holy shit..."
    ni "Unbelievable."
    n "Nii-chan...Nii-chan! Please...no more! You’re...hurting Onee-chan!"
    s "N...No! She just...needs to know! I can’t...hide it anymore! And I can’t...ignore {i}you{/i} anymore! "
    ni "So what? You just...take everything then? "
    ni "Is {i}that{/i} what that whore taught you when {i}you{/i} were the one being groomed?"
    ni "That you’re the center of the universe and you can do whatever you want with {i}whoever{/i} you want?"
    ni "Is that what makes you happy, Akira? Is {i}this{/i} what makes you happy?"

    play sound "static.mp3"
    scene norikovirginity37 with flash
    stop sound

    n "Akira...doesn’t want to hurt you...Onee-chan! He really...does love you! He just...haaah....he....mnhghhh! This is so hard to do while...hyaaAAaah!"
    ni "No..."
    ni "This isn’t love."
    ni "I don’t know {i}what{/i} this is."
    n "N...Nee-chan...please! Don’t...think less of him because...of me!"
    ni "Is it just {i}her,{/i} Akira?"
    s "Ngh...ngh!"
    ni "You want to come clean, right? So tell me — is it really {i}just{/i} her? Or are there other {i}little sisters{/i} out there who straddle you and call you {i}Onii-chan{/i} too?"
    n "A...Akira....aaah...tell her...it’s just...me! Tell her...it’s only me!"
    s "Just...leave...Niki! I’m...busy right now!"
    ni "Mm."

    play sound "slidedoor.mp3"

    ni "So you are..."

    play sound "static.mp3"
    scene norikovirginity38 with flash
    stop sound

    a "I’m really surprised, Dad. I figured you would have stopped the moment Niki walked in. That was a really ballsy move for you."
    s "You...leave too! This is a moment for just...Noriko and me!"
    n "Mnnghhhghh! I can’t believe...you haven’t let up...a single bit! How am I...supposed to face her now?!"
    a "Probably the same way he will. Tearful. Apologetic. And you’ll try to explain yourselves, but she won’t get it. She {i}can’t{/i} get it. Because not everyone does."

    scene norikovirginity39
    with dissolve2

    a "But this is who we are. And that’s nothing to feel bad about, I don’t think."
    a "I imagine it’s actually a load off your mind not having to outright confess to her now, Dad. Same with you, Noriko."
    a "You guys both get what you want and it’s someone else who has to hurt because of it. That’s how these things always work."
    a "And to cap it all off, you guys are inflicting all of that pain on someone who won’t leave you no matter {i}what{/i} you do. So you lose nothing, but gain everything."

    scene norikovirginity40
    with dissolve2

    a "I’m jealous of this moment, really. And I’m not just saying that because I’m more in love with this man than anyone else could ever possibly be."
    a "I can just only imagine how much the two of you are feeling right now. And I wonder what that’s like."
    s "Ngh...ngh!..."
    a "..."
    n "So are you just...going to {i}watch{/i} us now? Or..."

    scene norikovirginity41
    with dissolve

    a "{i}Can{/i} I?"
    s "No! Get...out!"

    stop music fadeout 10.0
    scene black
    with dissolve2

    a "{i}Hah...{/i}fine. And congrats or whatever to you, Noriko. "

    if amifingered == False:
        a "I know firsthand how much it sucks to {i}not{/i} have sex with him when it’s literally all you can think about."

    else:
        a "It feels like just yesterday that my dad pounded {i}my{/i} tight little pussy for the first-"

    s "OUT!"
    a "Yup! Leaving. Bye-bye!"

    "As the door slides closed and Ami’s footsteps disappear down the hall, I feel a tear or two drop heavily onto my face from above."
    "So I keep my eyes closed for the next thirty minutes, embracing Noriko tightly from below and proceeding to make love to her until I’m sure the crying has stopped."
    "Once it has, I open my eyes to find {i}hers{/i} closed. "

    play sound "slap.mp3"

    "So I shock her back to life with a quick slap of her ass before pulling her head down and burying my tongue in her mouth."
    "I cum inside of her again. I’ve lost track of how many times she’s climaxed."
    "After that, I fulfill another fantasy by sliding myself out of her and standing up, bringing her to her feet with me — but only for a few seconds as I whisk her off the ground shortly after."
    "She takes this cue perfectly, wrapping her legs around my back as I slide myself inside of her. "
    "I find it easier to assume this position by using the wall to my advantage and I prop her up against it, knocking a painting off the wall in the process."
    "It hits her head, but it must not have hurt since she just laughs about it and wraps her legs tighter around me."
    "She doesn’t cum as many times in this position, so I figure that she’s either getting tired or that it’s just not as pleasurable as the others."
    "I cum again and slide out of her once more. My seed is dripping out of her at this point, and her face is flushed so deeply that it matches her hair. "
    "I ask her to get down on all fours and she does so without question."
    "She points her ass at me as I take my place on my knees behind her, gripping my cock and sliding it between her cheeks where I proceed to grind for several minutes until I begin fucking her again."
    "She really likes this position and cums many times. I had a feeling she would. It suits her well."
    "By now, I’m lightheaded. And unsure of how much fluid I have left inside of my body."
    "Regardless, the night continues. And once she’s done receiving me from behind, I tell her to open her mouth."
    "Again, no hesitation. "
    "She does so, and I fuck her throat, making use of that lack of a gag reflex that I learned tonight was not a lie tailor-made to impress me."
    "Her eyes water and roll to the back of her head several times, but she cups my balls and swallows when I fill her mouth."
    "I’ve lost track of time by now."
    "I barely know where I am anymore."

    $ renpy.pause(15, hard=True)
    $ renpy.end_replay()
    $ norikospring5 = True
    $ norikosex = True
    $ noriko_love += 10
    $ noriko_lust += 50

    "{i}Noriko’s affection has increased by 10!{/i}"
    "{i}Noriko’s lust has increased by 50!{/i}"
    "........."
    "......"
    "..."

    jump nikispring6

label beachsixnoriko1:
    scene noonsky
    with dissolve2
    play music "acoustic.mp3"

    "Having successfully fucked the daylight away, I have now completed the world’s shortest and sexiest scavenger hunt — which means there is only one thing left to do."
    "Or two things, if you’re counting both Noriko and Kirin. Which you {i}should{/i} be because I am, at long last, going to have a threesome with both inhabitants of a dorm room at once."
    "Barring that one of them hasn’t chickened out, at least. "
    "Which Noriko {i}may{/i} because, despite having finally taken her virginity, it is slightly odd how quickly she’s become okay with more...{i}lascivious{/i} conduct."

    play sound "slidedoor.mp3"
    scene black
    with dissolve2

    "But this does not matter to me — for I quickly identify her room by the two sets of shoes placed neatly outside of the door, keeping mine in my hands so as to not alert any other passersby."
    "Then I make my way inside..."

    scene norikolustnaming1
    with dissolve2

    "And I am greeted by a staggering amount of {i}supplies{/i} in addition to the two girls that I am about to both violently and passionately pierce in sexual fashion."

    n "I hope you’ve still got some juice left in you, Onii-chan. Kirin and I are {i}really{/i} thirsty."
    ki "You sure took your time getting here, [kirinmaster]. I’d be surprised if Sana and Molly can still walk right now."
    s "To be completely honest, me too. "
    s "I believe I am doing what the youth calls “crashing out” right now. Noriko can probably tell you more about that, though."

    scene norikolustnaming2
    with dissolve

    ki "She already {i}did.{/i} "
    ki "And I know I’ve already verified their size with both my tongue and my hands, but it’s gotta take some serious {i}balls{/i} to fuck a girl in front of her older sister, Sensei. I’m impressed."
    s "No, you’re just saying that because you always want to be fucked in front of your older sister."
    ki "You are not wrong."
    n "H...How about we...{i}don’t{/i} talk about older sisters today? I would much prefer this threesome to be depression-free."
    s "Then boy do I have bad news for you."
    ki "Did you seriously keep going {i}right{/i} in front of her? And she just stood there and watched? "
    s "Ami was there too."

    scene norikolustnaming3
    with dissolve

    ki "Ughhh! Why do I always have to miss out on all of the fun?!"
    n "She says, despite being personally invited to rail my older brother with me."
    s "On that note — you’re really cool with this, Noriko?"

    scene norikolustnaming4
    with dissolve

    n "Huh? Yeah. Why?"
    s "Just...you were so adamant about this being an intimate and personal thing until a little while ago."
    s "And I know you have a history of doing things for {i}my{/i} sake that I would like to prevent if it is going to harm you."
    ki "If you two make me sit in the fucking cuck chair, I swear to god."
    n "We can still have lovey-dovey brother-sister sex, Onii-chan. Whenever you want. Like...{i}literally.{/i} Whenever you want. I forget what “no” means."
    n "But also, let the record show that I am violently bisexual and willing to engage in various threesomes with you and any other girl we know on a regular basis assuming that all participants consent. "
    s "Really? So there’s...no one off limits for you? "
    n "Nope."
    s "Not even Maya?"

    scene norikolustnaming5
    with dissolve

    n "Are you kidding?! That’d be the hottest one! "

    scene norikolustnaming6
    with dissolve

    n "I can see it now...the two of us fighting over your cock...accidentally touching tongues as we both try to suck you off at once..."
    ki "Hey."

    scene norikolustnaming7
    with dissolve

    n "I bite her lip...and she wraps her hands around my neck to try and strangle me, but realizes in that moment that she’s driven {i}mad{/i} by lust and can’t contain herself anymore!"
    ki "HEY."
    n "We kiss again as Onii-chan grabs both of our heads and slides his throbbing dick between our mouths! Then we lock eyes with one another, {i}finally{/i} bonding after all these years!"

    scene norikolustnaming8
    with hpunch

    ki "Jesus fucking Christ, Noriko! Do you even {i}need{/i} Sensei at that point? Just fuck her yourself and give {i}him{/i} to me."
    n "Sorry. It’s just that Maya and I are kind of fated to do this one day, so I’ve been thinking about it for a long time."
    s "I’m really not comfortable with so many people lusting after her all of a sudden. Noriko — you are now banned from fantasizing about anyone other than me."

    scene norikolustnaming9
    with dissolve

    n "Aye-aye, Onii-chan! You’ll always be the star in my heart! And now my vagina too!"
    ki "What about me? Am I banned from fantasizing about other people too?"
    s "Will there even be anything left of your personality if I ban you from that?"

    scene norikolustnaming10
    with dissolve

    ki "Yes!"
    ki "Probably!"
    ki "I like other things sometimes!"
    n "Onii-chan, Onii-chan~ Kirin doesn’t believe we did it all night long. She thinks I’m lying and bad at sex."

    scene norikolustnaming11
    with dissolve

    ki "Well, duh. {i}Five{/i} hours for your first time? If you’re going to make up a number, at least make it a believable one."
    n "You’re gonna prove her wrong, right? And fuck me for {i}ten{/i} hours today so we can put this little slut in her place?"
    s "I will certainly do my best, but I am not sure how much fluid is left inside of my body."
    n "That’s fine. I splurged and bought a bunch of water and snacks. And condoms. And celery too because I heard it makes you cum more. That’s in the fridge, though. Want some celery?"
    s "I don’t want some celery. And you know I’m not going to use those condoms, right? "
    n "Yeah. But I figured I’d buy them anyway in case you weren’t feeling risky since I can just turn them all into water balloons tomorrow."
    s "Risky? You’re on birth control. That’s a flawless contraceptive that has never backfired for anyone in the history of humanity. "

    scene norikolustnaming12
    with dissolve

    n "Facts!"
    ki "So, how do we do this? Who starts where?"
    s "The bed would probably make the most sense. I don’t know. This feels so casual and it’s throwing me off."
    n "It {i}is{/i} casual! And that makes it hot! Also, you have to fuck me first. Kirin already agreed. It was part of the terms."
    s "Weren’t the original terms that she gets my body and you get my heart?"
    n "Voided the first time you touched my cervix. To the bedroom we go!"

    play sound "static.mp3"
    scene norikolustnaming13 with flash
    stop sound

    n "In the bedroom, we are!"
    s "I see your {i}splurging{/i} accounted for more than just condoms and water."
    n "If you’re talking about the sex toys, we had most of those already. The only new additions are the Official Dildo Saber and the tentacle one Kirin insisted on buying."
    ki "We cleaned and sterilized all of them and give you full permission to use any of them on either one of us at any point tonight."
    s "Is that a trombone?"

    scene norikolustnaming14
    with dissolve

    ki "It sure fucking is."
    s "Noriko, what’s the trombone doing here?"
    n "If you need to ask, you aren’t ready for it."
    s "I imagine that is a fair assumption to make. "
    n "Sure is, Onii-chan! Now push me down and fuck me next to my best friend! And remember — ten hours! No less!"
    s "Before we begin, there’s actually something I want you to do."

    scene norikolustnaming15
    with dissolve

    n "Damn, Kirin. You hit the nail on the head with this one. Guess I owe you dinner. "
    ki "Called it."
    s "Called what? What just happened?"

    scene norikolustnaming16
    with dissolve

    ki "Your little sex-naming ritual. You did the same thing with me and Miku and I know for a fact you’re doing it with everyone else too. So I bet Noriko you’d jump to that before we all fucked."
    n "Kirin says you’re going to ramp up the amount of sex you have with me once this ritual is complete. But let it be known that if you choose anything other than {i}Onii-chan,{/i} I will riot."
    s "Thank you for your help, Kirin. It’s always nice knowing how “seen” and discussed I am among all of you girls."
    ki "You joke, [kirinmaster]. But like it or not, your dick brings us girls together. Like, Noriko and I are about to enter a brand new stage in our relationship thanks to you."
    n "There’s no turning back from here, Onii-chan. You’ve unlocked your very own insatiable sex-sibling! Now you’ll have to satisfy her {i}and{/i} all of her friends! Whatever will we do?"
    s "{i}Hah...{/i}are you ready for the “ritual” then, Noriko?"

    scene norikolustnaming17
    with dissolve

    n "Sure am, Onii-chan! Let’s hear it! What should I call you from now on?"

    jump norikosexnaming

label norikosexnaming:
    $ norikomaster = renpy.input("Enter a name for Noriko to call you...")
    $ norikomaster = norikomaster.strip()

    if norikomaster.lower() in ["noriko"]:
        s "Well, obviously you’re going to call me Noriko from now on."

        scene norikolustnaming18
        with dissolve

        n "Damn it! Now I owe Kirin {i}two{/i} dinners."
        s "What? Why? What was the bet this time?"
        ki "That you’d make this weird and try to get Noriko to call {i}you{/i} Noriko or something."
        s "There is no way I’m that predictable."
        ki "And yet I am once again right."

        scene norikolustnaming19
        with dissolve

        n "Onii-chan, why do you want me to call you Noriko?"
        s "Because I have always wanted to be my own little sister. And also, if I become you, your sister will like me again."

        scene norikolustnaming20
        with dissolve

        n "You know I’m in hot water with Nee-chan now too, right? Because even if you’re the one who broke her heart, I {i}did{/i} still fuck her boyfriend. Repeatedly. And made her listen to all of it."
        s "In your defense, you didn’t know she was listening."
        n "And in {i}your{/i} defense, you didn’t know she would catch us."
        s "So you agree to call me Noriko, then?"
        n "When did I agree to do that? You’re just putting words in my mouth now when you {i}should{/i} be putting your penis inside of it."
        ki "I agree. You should do that."
        s "I will. Just as soon as Noriko calls me Noriko."

        scene norikolustnaming21
        with dissolve

        n "{i}Jeez...{/i}fine. I’ll call you Noriko from now on. But {i}I’m{/i} still going to be Noriko as well because I like my name and think it goes really well with Nakayarakawayama."

        jump endofnorikosexnaming

    if norikomaster.lower() in ["kirin"]:
        s "From now on, you’re going to call me Kirin."

        scene norikolustnaming22
        with dissolve

        n "I’m going to {i}what?{/i}"
        ki "You know, this really doesn’t bother me even half as much as I imagine you thought it would. I just think that’s hot."
        ki "Will it make our impending threesome slightly more confusing in the process? Probably. But this is the exact sort of mental stimulation I need if I’m ever going to become likeable."
        n "Now look what you’ve done, Kirin 2. You made Kirin 1 self-deprecate again. She was doing so well today."
        s "Wait, how come {i}she{/i} gets to be Kirin 1 and I have to be Kirin 2? I’m older than her. I should get priority on that name."

        scene norikolustnaming23
        with dissolve

        ki "You don’t get priority on taking my name! I had it first! You’re lucky I’m letting you use it at all!"
        n "Kirin 1 makes a very good point, Kirin 2. Out of respect for her, I simply will not budge on this."
        s "Ugh...fine. I’ll be Kirin 2 then. But I won’t be happy about it."

        $ norikomaster = "Kirin 2"

        scene norikolustnaming24
        with dissolve

        n "Woo! Does that mean it’s sex time then? And I get to fuck two Kirins at once?!"
        s "You sure do, Noriko."

        jump endofnorikosexnaming

    if norikomaster.lower() in ["niki"]:
        s "From this point on, you will refer to me only as Niki."

        scene norikolustnaming25
        with dissolve

        n "Damn, you really {i}are{/i} crashing out. I had no idea you missed Nee-chan so much that you’d stoop to asking me to call you by her name in bed."
        ki "Kinda hot, though. Not gonna lie."
        s "I don’t miss your sister at all. This is a completely rational move by me that you shouldn’t look too deeply into. I am a normal man and that normal man’s name is Niki."
        n "Okay. But this does not change the fact that I may feel slightly uncomfortable shouting out my sister’s name while I am bent over a chair with my legs spread."
        ki "Again, hot. That’s exactly the name I’d want to be crying out in that position."
        s "Noriko, are you {i}seriously{/i} telling me you don’t want Niki to bend you over a chair and fuck you?"

        scene norikolustnaming26
        with dissolve

        n "Well, which one are we talking about?! Because now I’m just confused and my answer changes entirely based on the result of that question!"
        s "Psht. So much for you being the {i}fun{/i} sister."
        n "But I {i}am{/i} the fun sister! Nee-chan would never call {i}you{/i} Noriko in bed! Or...at least I don’t {i}think{/i} she would?"
        ki "Imagine she {i}did{/i} though? And you guys just like secretly wanted to fuck each other all these years?"

        scene norikolustnaming27
        with dissolve

        n "Stop projecting! Not all sisters want to fuck each other! That’s a uniquely Kirin outlook that is only {i}sometimes{/i} relevant to my interests! Like when I have too much caffeine before bed."
        s "Sorry, are you saying you have sex dreams about your sister when you have too much caffeine before bed?"

        scene norikolustnaming28
        with dissolve

        n "Well, not...{i}all{/i} the time..."
        n "And it’s not like I {i}want{/i} to either! But when you’ve been messing around with {i}her{/i} instead of {i}me{/i} my whole life I’ll obviously...you know..."
        n "Subconsciously insert myself into scenarios in which the two of you welcome me into your world of unchained lust for one another. That’s totally normal!"
        s "So you’ll call me Niki then?"
        n "No! Choose something else, Onii-chan!"
        s "Ugh...fine."

        jump norikosexnaming

    if norikomaster.lower() in ["maya"]:
        s "From now on, I want you to call me Maya."

        scene norikolustnaming29
        with dissolve

        n "Wow. My fantasy from earlier really got to you, huh?"
        s "Honestly, I’ve been planning on making you call me that ever since the first time you sent me a picture of your chest."
        n "Weird, but okay. Not really sure how my nudes threw you onto that train of thought, but I’m not against it."
        n "I’ll call you Maya. Under one condition, though."
        s "You’re in no position to be making demands, Noriko."
        n "I sure am. {i}I’m{/i} the one who has the trombone. And {i}I{/i} know how to use it."
        s "Hah...fine. What’s your condition then?"
        n "We {i}non-sexually{/i} roleplay for at least an hour prior to each round of coitus where you formally apologize for how mean you have been to me over the years."
        n "And also, you need to let me touch your butt once a day. I’ll try not to grab it {i}super{/i} hard, but I make no promises."
        s "Can you just call me Maya without me actually {i}being{/i} Maya?"
        n "Nope. The only thing {i}I{/i} half-ass is my own happiness. And if you want to be called Maya, you’re damn well gonna {i}be{/i} Maya. And {i}I’m{/i} gonna touch your butt."
        s "On second thought, I have something else I want you to call me instead. Something that {i}won’t{/i} involve you violating me."

        scene norikolustnaming30
        with dissolve

        n "Awww! I was starting to get excited, though! The fantasies were coming back! And this time, Maya had a penis! I just...don’t know if that makes her hotter to me or not!"
        ki "I like the girl version, personally. I’m fine with Sensei’s dick being the only one I fantasize about."

        scene norikolustnaming31
        with dissolve

        n "{i}{size=-2}Oh, look at me. My name’s Kirin. I’m gonna earn a bunch of good-girl points by saying cute stuff to Sensei that makes him think I only have eyes for him when I have told Noriko on at least five occasions how hot it would be if my older sister had a dick.{/i}{/size}"
        ki "Have you really been keeping track?"
        n "Not intentionally. I just agree. So I {i}accidentally{/i} kept track. Your sister would be hung like a horse and we all know it."
        s "{i}Ahem.{/i}"

        scene norikolustnaming32
        with dissolve

        n "Oh. Sorry, Onii-chan. What were you saying again?"
        s "New name. I have one. Listen."

        jump norikosexnaming

    if norikomaster.lower() in ["daddy", "papa", "father", "dad"]:
        s "From now on, you will refer to me as [norikomaster]."

        scene norikolustnaming33
        with dissolve

        n "First and foremost, hot. But second, you really prefer that over “Onii-chan?” Because, not to toot my own horn or anything, but you seemed {i}pretty{/i} into that last time."
        s "I like both. And you can continue to call me Onii-chan outside of sex. Or...during it, at the risk of breaking consistency."
        s "I’d just {i}also{/i} like to experiment with you calling me [norikomaster] as it heightens the already taboo nature of our relationship and gives me more to work with on a...narrative level, I guess?"
        n "You mean, like...calling me your little girl and praising me for how good I become at riding my [norikomaster]’s cock?"
        s "Yeah, exactly."

        scene norikolustnaming34
        with dissolve

        ki "Okay. I’m wet now."
        n "You’re literally always wet."
        ki "Yeah, but hearing you say shit like that now knowing you guys will act on it is, uhh...{i}yeah.{/i}"

        scene norikolustnaming35
        with dissolve

        n "Look what you’ve done now, [norikomaster]...I was just trying to have a sleepover with a friend from school and you had to go and turn us on..."
        n "Now, Kirin and I will be up all night long unless you {i}do{/i} something about it. It’s okay, though...we trust you. I won’t tell Mommy and {i}Kirin{/i} won’t tell hers."
        s "See, this is why I chose [norikomaster]. This is hot as hell."

        scene norikolustnaming36
        with dissolve

        n "Not to say I disagree because I definitely don’t, but...theoretically, couldn’t our dialogue there be exactly the same if we just stuck with Onii-chan."
        s "Well...{i}yeah.{/i} I guess. But still — I want to hear [norikomaster] and you are my pet now, so you are going to give me what I want."

        scene norikolustnaming37
        with dissolve

        n "Arf, arf!"
        s "..."
        n "Get it? Cause I’m your pet?"
        s "Yes, Noriko. I get it."

        jump endofnorikosexnaming

    if norikomaster.lower() in ["onii-chan", "oniichan", "big bro", "big brother"]:
        s "From now on, I will be..."
        s "Exactly what you’ve been calling me this whole time."

        scene norikolustnaming38
        with dissolve

        n "[norikomaster] prevails! Fuck yeah! Our relationship can stay just as controversially romantic and cute as it’s {i}always{/i} been! Sorry, Mom! Sorry, Dad!"
        n "And also it’s already implied given recent events, but sorry Nee-chan as well!"
        ki "Most expected outcome ever. Noriko would’ve cried herself to sleep if you’d chosen anything else."
        n "Hahah! Probably!"

        scene norikolustnaming39
        with dissolve

        n "But that doesn’t matter because [norikomaster] {i}didn’t{/i} choose something else!"
        n "He chose the objectively correct answer because he loves me and I love him and we’re going to make incest babies together!"
        s "First off, nice Ami impression. Second, we’re not {i}actually{/i} related, Noriko-"

        scene norikolustnaming40
        with dissolve

        n "LALALALALALALALA! CAN’T HEAR YOU!"
        ki "Just let her have this one, Sensei. The more {i}legitimate{/i} your connection with Noriko is, the tighter she’ll squeeze when you’re stuffing her five minutes from now."
        s "This is why I keep you around, Kirin."

        scene norikolustnaming41
        with dissolve

        ki "Oh, good. I was worried it was just the blowjob skills."
        n "So...the ritual’s complete now, right? And we can proceed to the main event where Kirin and I finally touch each other? And also you. {i}Mainly{/i} you. But also still each other."
        s "The ritual is complete...and the time has come."

        jump endofnorikosexnaming

    if norikomaster.lower() in ["rainbow dash"]:
        s "I will be known only as Rainbow Dash from this point on."

        scene norikolustnaming42
        with dissolve2

        ki "Oh, you’ve gotta be fucking kidding me."
        n "Rainbow Dash?! The best flier in all of Equestria?! The loyal pegasus pony who clears the skies of Ponyville and never shies away from competition?! {i}That’s{/i} what you want me to call you?!"
        s "I mean, you can do it in fewer words. But yeah, that’s the gist of it."
        ki "You’re {i}seriously{/i} going to enable her pony-fucking fetish, Sensei?"

        if brony == True:
            ki "I’m half-tempted to blueball you again right now."
            s "Please don’t. I’m still missing a replay because of that."

        n "I always knew you’d come around, Onii-ch...sorry! [norikomaster]!"

        scene norikolustnaming43
        with dissolve

        n "{size=-1}I just hope this isn’t like that time in The Crystal Empire Part 2 where she decides to take it easy on Fluttershy in the jousting tournament because she feels bad for her and doesn’t want her to cry...{/size}"
        s "I’m not doing this to prevent you from crying, Noriko. I’m doing this because I’ll never actually be able to fuck a pony. So the best I can do is be fucked {i}as{/i} one."

        scene norikolustnaming44
        with dissolve

        n "No, [norikomaster]. You {i}will{/i} fuck a pony. And I’ll make sure of it! No matter how many of those “weird” games the two of us have to play! On god, we’ll fuck every pony together!"
        ki "That’s it. I’ll never be horny again. Sex has now been ruined for me. Thank you, you two. I have now seen the light."
        n "Ignore her, [norikomaster]! Like all of the pets except Tank did when she got her wing caught under a boulder in “May the Best Pet Win!”"
        s "That is {i}exactly{/i} what I was thinking. And I am now ready for sex."

        jump endofnorikosexnaming

    else:
        s "From now on, I want you to call me [norikomaster]."
        n "Got it! Then [norikomaster] you shall be. Let us commence the sexing of one another."
        s "Let us commence, indeed."

        jump endofnorikosexnaming

label endofnorikosexnaming:
    s "I may require some assistance, though."

    scene norikolustnaming45
    with dissolve

    n "Assistance? You don’t suddenly have ED after Niki broke your heart, do you?"
    ki "No wonder it took him so long to finish up with Sana and Molly."
    s "{i}No,{/i} Noriko. I do not have erectile dysfunction. I’ve just climaxed way more than normal today. Remember the last hour of our first go-around here?"
    n "No. Everything after Nee-chan left is all one big sexual blur. I came so many times that I think I might actually have brain damage now."
    ki "I think he’s just saying we need to get him hard."
    s "Bingo."
    n "Soooo...go down on you? And experience the secondhand taste of both Sana and Molly’s vaginas?"

    scene black
    with dissolve
    play sound "tackle.mp3"

    ki "Say no more."
    n "Yeah, I’m in too. Me first, though!"

    play sound "zipper.mp3"

    ki "What?! Is it not enough that you get to fuck him first too?! At least let me get the first taste! You’re gonna steal it a- aah! Noriko!"

    "........."
    "......"
    "..."

    scene norikolustnaming46
    with dissolve2

    "Kirin doesn’t complain for long, electing to jerk me off into her roommate’s mouth after the two of them pull me onto the bed and yank down my jeans."
    "She locks eyes with me, seemingly waiting for me to say something as Noriko’s head bobs gently up and down on my cock."
    "Unfortunately, she can’t make much use of her missing gag reflex with Kirin’s hand in the way, but this still feels good regardless."
    "Kirin’s still better, though. But don’t tell Noriko I thought that. She just needs more practice."

    ki "I thought you said you needed {i}assistance,{/i} [kirinmaster]? You got hard in no time at all..."
    s "Yeah, well...I guess it’s hard {i}not{/i} to when...the two of you join forces..."
    n "Mnh...mnh! Mnlh......mnh!"

    scene norikolustnaming47
    with dissolve

    ki "Oh?...How convenient...Because I feel like we’ll be doing that a lot from now on. Won’t we, Noriko?"
    n "Mnh......mhmmmm..."
    ki "Yeah?...You like sucking your big brother’s cock? Even though it’s been inside your sister? {i}And{/i} me?...{i}And{/i} two other girls today alone? Heh...You’re even sluttier than {i}I{/i} am..."

    scene norikolustnaming48
    with dissolve

    n "Mmnhh! Mmmhmmm! Mnhgh...mlchp....mnghh...mlphghghnnn!!~~~"
    ki "Ah...so new to this and already {i}so{/i} dedicated..."
    ki "Be careful, Noriko...we don’t want him to cum too soon, do we? He has a...limited supply left right now..."

    "Noriko begins to speed up in protest to Kirin’s words, causing me to reach forward and grab onto the first thing I can find. Which is, conveniently enough, Kirin’s ass."

    scene norikolustnaming49
    with dissolve

    ki "Ngh...[kirinmaster]...{i}you{/i} need to be careful too..."
    ki "No matter how much I try to take care of my body, I’m still just a little girl. And {i}you’re{/i} just so...{i}big.{/i} If you’re too rough, you might break me..."

    scene norikolustnaming50
    with dissolve

    ki "You don’t {i}want{/i} to break me...do you, [kirinmaster]?..."
    ki "What?...You {i}do?...{/i}"
    n "Mnhhh....mmnhhh~"

    scene norikolustnaming51
    with dissolve

    ki "Did you hear that, Noriko? Your big, mean older brother wants to hurt me...You won’t let him, will you?..."
    n "Mnhh!....Mm...mmmm!"
    ki "Thank you, Noriko...you always make me feel better..."
    ki "I just wish {i}I{/i} could get a fraction of the attention you’re giving him..."

    play sound "static.mp3"
    scene norikolustnaming52 with flash
    stop sound

    n "Ahm~ Aaammmh...mlm...mnch...mphp....mlgh...."
    ki "Ah! Amhfh...mlmh....that’s...more like it..."

    "I begin to watch what can only be referred to as “the greatest thing of all time” unfolding right before my very eyes."
    "The two of them begin to passionately- {i}violently{/i} make out, biting each other’s tongues and swapping saliva as Kirin methodically continues to jerk me off."
    "Meanwhile, Noriko acts on instinct, lightly thrusting her ass backward in repeated and unfilled hopes of finding something there to penetrate her."
    "And each second she {i}doesn’t,{/i} her motions get more desperate. Her stifled moans grow louder. Her kisses get more violent — yet Kirin does nothing but lean into it."
    "She’s more composed, having been used much more. Having {i}experience.{/i}"
    "But her borderline stoicism and composure in the face of lust only serves to exaggerate the {i}inexperience{/i} of her friend."
    "Of my little sister."
    "And I will be damned if I let Kirin steal this undeserved attention away from {i}me.{/i}"

    s "Noriko...keep going...focus...on me!"

    play sound "static.mp3"
    scene norikolustnaming53 with flash
    stop sound

    ki "Jealous much?"
    n "Sorry...[norikomaster]! I thought you’d like watching me make out with Kirin."
    s "You were...getting a little...{i}too{/i} into it..."

    scene norikolustnaming54
    with dissolve

    n "Only because {i}you’re{/i} here, [norikomaster]! I’m sorry! I just couldn’t help myself thinking about you pounding my little pussy from behind!"
    ki "Coincidentally, I was {i}also{/i} imaging you pound Noriko’s {i}little pussy{/i} from behind. Yet here we are — {i}still{/i} “assisting” you despite you being more than ready to grant her wishes."

    scene norikolustnaming55
    with dissolve

    n "P...Please...[norikomaster]!!!"
    n "Just...th...thinking about it...makes me...want to...ngh!"

    with sexfade
    with cumflash
    scene norikolustnaming56
    with hpunch

    n "MNGHGHGHGHGHHH!!!!?!?!!!!!"
    ki "..."
    n "Mnh!......Mnhhh!"
    ki "Did...Did you just cum?"

    scene norikolustnaming57
    with dissolve

    n "[norikomaster] neglected me too much and {i}made{/i} me cum!"
    ki "Nobody even touched you. How is that even possible?"
    s "Noriko is...extremely weak."
    n "Nuh-uh! I just love you so much that I don’t {i}need{/i} to be touched in order to cum! It means I’m special!"
    s "Then how about we show Kirin how special you {i}really{/i} are by finally giving you what you want?"

    scene black
    with dissolve
    play sound "tackle.mp3"

    ki "That sounded too suggestive, [kirinmaster]. You need to watch out or you’ll make her cum a- Noriko?!"
    n "MNGHHHHH I’M HOLDING IT IN, OKAY?! DON’T JUDGE ME!!!!"

    "........."
    "......"
    "..."

    scene norikolustnaming58
    with dissolve2

    "Kirin helps Noriko onto my lap before guiding my cock inside of her."
    "And while she doesn’t {i}immediately{/i} cum from that, she certainly does once Kirin’s fingers find her clit."

    n "AAAHH! AAAH! HYAHAHAHHHAAAAA!"
    ki "Oh my fucking {i}god!{/i} I had no idea you were {i}this{/i} sensitive! That’s fucking adorable!"
    n "Don’t...ngh...make fun of me! I was...aaah...born this....aaah...aaaAaAaaaAhhh! K...Kkiiiiirin! S...Stopp!!!!"

    scene norikolustnaming59
    with dissolve

    ki "Having your clit rubbed while there’s a cock inside of you is seriously the best, right? Especially when it’s done by a friend!"
    ki "This way, {i}you{/i} get to focus on moving those hips and {i}Sensei{/i} gets to focus on ramming his thick cock all the way up your pussy! You both win!"
    n "You better not...tease me about this after...today!"
    ki "Why not? {i}You{/i} always tease me for allegedly {i}crying{/i} after losing my virginity."
    n "But you {i}did{/i} cry, you-"

    scene norikolustnaming60
    with dissolve

    ki "Clit attack!"
    n "HYAAAH! NOO! KIRIN! AAAH! S...SOFTER! THAT’S...SENSITIVE AFTER I...AAAH! NO! S...STOP!"
    s "Sorry Noriko, but...I’ll be...going harder...too now!"

    scene norikolustnaming61
    with dissolve

    n "AAAAaaaAAAHHH!! HAAAH! N...NGHGGH...!!!!! S...MNGHGHGH!!?!?!?!!!!"
    ki "Oh my fucking god! This is so fun that I don’t even {i}care{/i} that nobody’s touched my pussy yet!"
    s "I can...change that!"
    ki "Yeah, sure. Your cock’s already inside your little sister here and there’s no way those hands are leaving her-"

    play sound "static.mp3"
    scene norikolustnaming62 with flash
    stop sound

    ki "HYAH!? AH!?"

    "{i}Kirin, who’d been hovering over my leg since we made it into this position, apparently neglected to notice that all it would take to give her {i}something{/i} to hump would be a little bending of my knee.{/i}"
    "And while we all know it’s not what she {i}really{/i} wants right now, we {i}also{/i} know that she lacks the self control to not instinctively grind against the salvation I have provided her."

    ki "You...dick! Your fucking...knee?! Really?!"
    s "Like you said — I don’t really have anything else to use right now. Plus, you seem to be grinding against it pretty vigorously."
    ki "Because it...feels good...douchebag! Like...grinding against the desk at school!"
    n "Don’t...haaah...feel ashamed...Kirin! I...aaah...have also...done that!"
    ki "Yeah, but {i}you{/i} probably came the moment you fucking touched it! I don’t want to cum from a fucking {i}knee{/i} when there is a perfectly good cock inside of you right now!"
    n "Then...aah...wait your...turn! I still have...nine hours and...thirty minutes to go!"
    ki "There is no way you two are going to go on for that long!!!!"

    play sound "static.mp3"
    scene norikolustnaming63 with flash
    stop sound

    "And we didn’t. But we did go on for at least another thirty minutes until I decided to just lay there out of concern for Noriko’s health."
    "Of course that didn’t stop {i}her,{/i} though. And she’s continued to bounce on me despite my inactivity, too busy kissing her friend again to even notice."
    "I just watch this time, though. For much longer. And {i}without{/i} the jealousy."
    "Because despite the two of them finding temporary comfort in one another, {i}I’m{/i} the one setting the tone for it. {i}I’m{/i} the one driving them mad with lust."
    "And I intend to do that to everyone one day because I feel as if it’s the only way for me to truly obtain a happy ending."
    "Counterintuitive, isn’t it? Having to hurt so many people just to feel free."
    "I think it’s genius, though."
    "But when it hurts, it hurts. And it hurts a lot."
    "It hurts so much that it’s hard to keep hurting. Then {i}that{/i} hurts too."
    "So all there is to do is lie there sometimes — looking up at a girl who reminds you of another girl who reminds you of a different girl that reminds you of a girl."
    "Then the cycle continues."
    "And we circle the drain not knowing the pipes are clogged with grease and hair."

    scene black
    stop music

    "Because that’s something you {i}can’t{/i} notice until you get stuck."
    "Lodged there in the dark — somewhere close to the bottom of everything, yet refusing to touch it."
    "..."
    "Will we ever see where the drain leads, I wonder?"
    "..."
    "Will we ever {i}see{/i} at all?"

    $ renpy.end_replay()
    $ beachsixnoriko1 = True
    $ noriko_lust += 5
    $ kirin_lust += 5

    "{i}Noriko’s lust has increased to [noriko_lust]!{/i}"
    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"

    jump beachsixmakoto1
