label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
    if uta_love >= 5 and utamaid1 == True and day > 5 and utamaid5 == False:
        jump utamaid5
    if uta_love >= 10 and dormwar17 == True and utamaid10 == False:
        jump utamaid10
    if uta_love >= 20 and bathhouse20part2 == True and utadorm15 == True and utamaid20 == False:
        jump utamaid20
    if uta_love >= 25 and utaarchery1 == True and utamaid25p1 == False:
        jump utamaid25p1
    if osako_love >= 15 and wakanaspecial15 == True and osakodate15 == False:
        jump osakodate15
    if chap4active == True:
        jump utaspringmaidgen
    if chapthreeactive == True:
        jump utasummer2maidgen
    else:
        jump utamaidgen

label utaarchery:
    if io_love >= 20 and makiinv3 == True and ioarchery1 == False:
        jump ioarchery1
    if chap4active == True:
        jump utaspringarcherygen
    if chapthreeactive == True:
        jump utasummer2archerygen

label callutamorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if uta_love >= 35 and utaspecial35 == True and utadate35 == False:
        jump utadate35
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Uta's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. She might be at her club right now."

        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Uta's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        u "Guhhhhhhhh..."
        u "Sensei?...Why are you callin' me so early?..."
        u "What's goin' on?..."
        s "Hey, Uta. I just wanted to see what you were up to."
        u "{i}Now?...{/i}"
        u "I'm trying to sleep..."
        s "Sorry, but you're just so irresistable that I can't keep my mind off of you for even a second."
        u "Guhhhhhh damn it...Why do I have to be so cute?"
        s "Come with me to the cafe and I'll buy you coffee or something."

        "Uta yawns and then proceeds to knock something off of a table, pausing for a moment as she figures out if she wants to-"

        u "Ugh...fine."
        u "But don't be expecting any interesting conversation."
        s "Sounds good. See you soon."

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene utamorninggen
        with dissolve
        play music "cafe.mp3"

        "Uta and I meet up at the cafe and it quickly becomes apparent to me just how hard it is for her to do virtually anything in the morning."
        "I offer to buy her a drink and she accepts but, once we sit down at the table, she barely even touches it and just falls asleep instead."
        "I am forced to spend the morning talking to a girl who may or may not be able to hear me and look like an idiot in the process."
        "But at least I am an idiot in the company of a cute girl."
        "Several of them, actually, as Rin comes over to the table and glances confusedly between the two of us on several occasions throughout the morning."
        "Regardless, I somehow manage to get closer to Uta. Probably."

        scene black
        with dissolve

        "At the very least, I know that she is comfortable sleeping around me."

        $ uta_love += 1
        stop music fadeout 5.0

        "{i}Uta's affection has increased to [uta_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label callutaafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Uta's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Uta's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        u "Yooooooooooo! What's up, dawg?"
        s "Sorry. I think I may have called the wrong number."
        u "Nonononono! It's me! Uta! The world's most adorablest maid and your best bud!"
        s "Please don't ever call me {i}dawg{/i} again. I am a human."
        u "Blah blah blah bark bark bark. Let's do karaoke!"

        if bonus == True:
            s "Are you going to try and kiss me again?"
            u "Me? Kiss {i}you{/i}?"
        else:
            s "Are we actually going to hug this time? Because I feel like we've been pretty close-"

        u "Sensei, you must be misremembering something. I would never ever {i}ever{/i} do that!"
        s "That really hurts."
        u "Well, quit your whining and meet me at the singing booth so I can knock out some songs before work!"

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "Uta hangs up on me, one of the greatest taboos of all, and I quickly find myself heading over to the karaoke place."
        "........."
        "......"
        "..."

        scene utanoongen
        with dissolve
        play music "utasings.mp3"

        "As expected, minimal attention is provided to me this afternoon."
        "But that's okay- because intentional neglect is still a form of attention."
        "However, neglect itself calls into question whether or not it {i}is{/i} intentional and-"

        s "..."
        s "Uta, do you want to stop singing and maybe talk for a little while?"
        u "No can do, Sensei! I'm on a hot streak!"
        u "Grab a mic and sing along if you're so desperate for some Ushibori time!"
        s "..."

        "I decide against grabbing a microphone and elect to continue watching Uta instead."

        scene black
        with dissolve

        "This goes on for roughly half an hour before she runs out of breath and needs to take a break."
        "During that time, I avoid being neglected and manage to grow a little closer to Uta."
        "Even if she would likely take karaoke over {i}me{/i} any day of the week."

        $ uta_love += 1
        stop music fadeout 5.0

        "{i}Uta's affection has increased to [uta_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label callutanight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if chap4active == True:
        jump utaspringnightgen
    else:
        "Uta should be working right now."
        "I can see her if I go to the maid cafe."
        jump callnight

label utamaidgen:
    scene utamaidgen
    with fade
    play music "maidcafe.mp3"

    "I decide to spend the night at the maid cafe and lose most of my savings to the bundle of joy in front of me."
    "Uta pulls out all the stops and easily coerces me into believing that I am the only man in the world who has ever mattered to her."
    "It is all a lie. I am being used."
    "And yet, I am unable to fight off any of it."
    "I don't {i}want{/i} to fight off any of it."
    "The darkness swallows me."
    "All I know is Uta. All I can see is Uta."
    "All there will ever be is Uta."
    "She truly is a monster...and this place is Hell."

    scene black
    with dissolve

    "After I come to terms with my meaningless existence and the perpetual struggle against all things cute, our conversation returns to normal."
    "It's a mostly dead night inside of the cafe, so the two of us are able to spend a good amount of time together."
    "Apparently, an added benefit to being friends with Uta is the ability to bypass the hourly charges here."
    "So, somehow or another, I manage to not wind up penniless when it finally comes time for me to leave."
    "Ami is going to be so proud of me."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta's affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label utamaid1:
    scene utafirstmaidcafe1
    with dissolve
    play music "maidcafe.mp3"

    "I walk into the maid cafe to find it pretty much deserted- which I guess makes sense considering that they close in around an hour."
    "There’s a little bell near where you walk in that I guess they want you to ring in the event of something like this happening, but..."
    "I am a man."
    "I shall ring no bell."
    "I will remain standing right here until a maid emerges from the kitchen and awkwardly discovers that there is someone waiting to be taken advantage of."

    u "Uta-chan’s maid-senses are tingling! Someone has arrived!"

    "That someone is me. "
    "She could probably sense my unrivaled love for her."

    scene utafirstmaidcafe2
    with dissolve

    u "Ah! Sen- Master! You came to visit me!"
    s "Woah. Did you almost break character just now?"
    u "Uta-chan is the perfect maid who never breaks character and makes all of her masters leave with full hearts and full tummies!"
    u "And, in return, she gets to leave with a full coinpurse!"
    s "That last part didn’t seem like a very maid-like thing to say."

    scene utafirstmaidcafe3
    with dissolve

    u "Sorry, Master. I just feel so comfortable around you that I guess I let a little bit of my true self slip. "
    u "Teehee~"
    s "God, you’re good at this."

    scene utafirstmaidcafe4
    with dissolve

    u "I like taking care of people. "
    u "I talked about it in class but I was looking after my grandpa before coming here."
    u "Most people would probably get bothered by something like that after a while but I thought it was kinda fun!"
    u "Like taking care of a baby except the baby is like four times your age and smokes cigarettes."
    s "Ahh, yes. I can totally see the correlation."

    scene utafirstmaidcafe5
    with dissolve

    u "Good! Cause today, since nobody else is around, Master gets Uta-chan all to himself!"
    u "I’ll be sure to make you even happier than I used to make grandpa before the cancer spread."
    s "..."
    u "..."

    "She doesn’t even realize how dark that was, does she?"

    s "You sure that’s okay? I feel kind of bad for showing up so late in hindsight- like you’re supposed to be cleaning right now or something."
    u "Of course it’s okay! I’m not really supposed to be spending so much time in the back anyway."
    u "I need a stepping stool to reach most of the stuff back there and it’s led to a few more broken glasses and dishes than I’d like to admit."
    u "But it’s no fun talking about things like that when you’re here to unwind! Come take a load off, Master! I’ll sit you down at my favorite table!"

    scene black
    with dissolve

    "Uta breaks the no-contact policy she informed me of the first time I came here and grabs my wrist, pulling me to a table near the window."
    "She doesn’t sit down beside me. But she {i}does{/i} slam her hands down onto the table like some sort of detective interrogating a murder suspect."

    scene utafirstmaidcafe6
    with dissolve

    u "So, Master...how can I make your dreams come true today?"

    if bonus == True:
        s "You can start by calling your parents."
        u "Sorry, Master. I can’t talk about things that frisky while I’m on the clock."
        u "Unfortunately, Uta-chan will have to reject you once again."
        u "But if there is anything slightly more legal that you’re interested in, all you need to do is let me know!"
        s "I can just wait an hour or two until you’re off the clock. It’s fine."
        u "Such determination. You’re really cute when you set your sights on something, Master! "
        u "I’m not weirded out at all!"
        s "Saying that makes me feel like you are..."
        u "Hey, know what’s even better than all of those dirty thoughts you’re having right now, Master? "
        s "...Nothing?"
        u "A nice...hot...plate of dinner!"
        s "That’s not really better but I guess I’ll have to settle for it."
    else:
        s "I am just here for food. I do not wish to converse with you."

    scene utafirstmaidcafe7

    u "Do you need a menu? Or do you want me to just have them make you something I know you’ll fall in love with?"
    u "Besides me, I mean~"

    if bonus == True:
        s "Uta, I want you to know that you make it very hard to not flirt with you when you say things like that."
        u "Of course. That’s the whole point of places like this, silly. "
        u "I say things to make you feel good and, in return, you spend all of your money on little-ole Uta-chan so she can buy more socks and underwear."
        s "And I’m guessing you tacked underwear onto the end of that as another part of the maid-strategy?"
        u "It worked, right? Are you thinking about my panties now? "
        u "It makes you want to spend more money on me, right?"
    else:
        s "The service here is entirely inappropriate and not at all welcome."
        u "Then why are you already trying to tip me?"

    "I look down at the table to find that I’ve already begun subconsciously sliding my wallet toward Uta."

    s "When did this even happen?"

    if bonus == True:
        u "You reached into your pocket the second I said underwear."
        u "Even girls do that sometimes. It’s kinda crazy how well it works."
        u "I guess I’m pretty good at this, huh?"
        s "Yes. You’re going to bankrupt me one day."
    else:
        u "Just now."
        s "Did you use one of your secret maid tactics on me? Is the flavor beam actually a curse?"
        u "Yes."
        s "Why would you do this?"

    scene utafirstmaidcafe8
    with dissolve

    if bonus == True:
        u "Uta-chan can’t help it if Master lets his mind wander. But as long as he’s happy and keeps his hands to himself, he can do whatever he likes."
        u "And, in the meantime, I’ll go put your order in! Try not to stare at my butt as I walk away, okay? "
        u "My skirt’s a little short today so I’m kinda worried you might accidentally catch a peek~"
        s "..."
    else:
        u "Idunno. World domination maybe?"

    s "Are you actually a genius, Uta?"

    scene utafirstmaidcafe9
    with dissolve

    u "Just a maid~ We’re all like this. "
    u "Ami will be exactly like me soon. Just you watch."

    scene utafirstmaidcafe10
    with dissolve

    if bonus == True:
        "Uta walks away and I realize that her skirt isn’t any shorter than normal. I know this for sure because I {i}always{/i} stare at her as she walks away. "
        "I’ve been deceived."
        "And also, now I have to worry that Ami will be using these same tricks on me soon."
        "This is no haven for degenerates. It’s a prison."
        "It sucks us in under the false pretenses of cute girls who will unconditionally care about us-"
        "When in all actuality, it’s just a cash-vacuum that they use and abuse until they can line their pockets with our hard-earned money."
        "I shall not be defeated by a place like this."
        "I am a man."
        "I didn’t even ring the bell."
        "All I have to do is hold out a little while longer..."
    else:
        s "No. Anyone but her."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene utafirstmaidcafe11
    with dissolve

    "Uta comes back several minutes later with a plate of omurice, but instead of blessing it with the ritualistic flavor-beam, she sits across from me and presses her fingers together."
    "This time it feels less like the work of a criminal-investigator and more like some sort of...seductive older woman. "

    u "You know, Master. It just occurred to me while I was in the kitchen that I can {i}really{/i} take advantage of you if I want."
    s "Have you not already been doing that?"
    u "Of course not. Uta-chan’s been nothing but affectionate and attentive toward you. "
    u "She even went as far as infusing all of the love in her little heart into this omelette."
    s "If you’re looking for more money, I don’t know what else I’d even be able to give-"

    scene utafirstmaidcafe12
    with dissolve

    u "Calm down. I’m not actually going to do anything."
    s "You say that, but I have a hard time believing this isn’t part of your scheme as well."

    scene utafirstmaidcafe13
    with dissolve

    u "Heheh~ It’s not. Really."
    u "I was just thinking that it’s a little risky for someone working in public education to even come to a maid cafe this close to the[school] in the first place."
    u "The only reason I got a job here instead of somewhere closer to my old[school] was that I was worried about being caught."

    if bonus == True:
        u "But here you are, an actual teacher, throwing all of his money at Uta-chan and thinking about her underwear and stuff."

        scene utafirstmaidcafe14
        with dissolve

        u "Aren’t you worried about getting caught?"
        u "Like, what if a girl from a different class saw you here and ratted you out to one of the other teachers or something?"
        s "Well...that would probably make me look bad. But I think they’d also be revealing that they have a job in the process, so they’d be effectively ratting themselves out as well."
    else:
        s "That seems like a rational concern. Can you please serve me now?"

    scene utafirstmaidcafe15
    with dissolve

    u "Wait, are we not allowed to have jobs at this[school]?"
    u "My other one was fine with them as long as they were part-time and we kept our grades up."
    u "Oh, wait! You’re actually here to blackmail Uta-chan, aren’t you?!"

    if bonus == True:
        u "You want to get freaky with her so badly that you’re abusing your power because you know you can get her on her back-foot!"
        u "Or even worse- her back!"
        s "...While the desire to “get freaky with you” may almost certainly be true-"
        u "Almost?! Uta-chan’s not even a definite candidate in her ultimate form?!"
        s "...I have no intention of blackmailing you."
        s "You keep my presence here a secret and I’ll keep yours a secret in return."
    else:
        s "I am just here to eat food in peace."

    scene utafirstmaidcafe16
    with dissolve

    u "Ah! Back-scratching! It’s finally shown up!"

    if bonus == True:
        s "That’s right. We’re both breaking rules by being here, so the least we can do is help each other continue to break them instead of abiding by them."
        u "I agree. Rules are dumb. Like, there’s that one rule at the mall where you can’t even bring more than like five things into the dressing room at once."
        u "But what if I wanna try on more than five things? You know?"
        u "And also, what’s the deal with not being able to use your cell-phone on planes? I hate rules."
        s "None of that really has anything to do with what I was trying to say, but I feel you."
    else:
        s "What are you talking about? Go get the manager. This is unacceptable."

    scene utafirstmaidcafe17
    with dissolve

    u "Whaaaat? You want to {i}feel{/i} me? Master! Keep your voice down."

    if bonus == True:
        s "You know, that’s not what I meant, but it’s true so there’s no sense in denying it."
        s "I would like to “feel” you immediately, if at all possible."

        scene utafirstmaidcafe18
        with dissolve

        u "Wait, no. It feels kinda weird if you just go along with it like that."
        u "We’re supposed to keep going back and forth for a little while and then I’m supposed to shoot you down and apologize. "
        u "You’re breakin’ out of the pattern here. Next thing I know, you’re going to be telling me you weren’t even staring at my butt as I walked away."
        s "Oh, I can guarantee that I was doing just that."
        s "Your skirt is also the same size as always."
    else:
        s "What? No."
        s "I have absolutely no idea what you are talking about."
        s "I am so hungry."

    scene utafirstmaidcafe19
    with dissolve

    u "Stooooooooop right there, Master!"
    u "As flattered as I am to hear that you think I’m cute enough to stare at me as I walk away, I’m afraid that I can’t let things go any further."
    u "So I am sorry but, once again, I must reject you. Please do not hold this against me or take it out on my report card."

    if bonus == True:
        u "I am willing to do several special things to increase my grades after hours but probably not the things you want me to do."
        s "What does that even mean? What sort of things would you do to increase your grades?"
        u "I can’t tell you that or you’ll lower them on purpose. Please forget I said anything and enjoy your omurice."
        u "It was made with love. Lots of love. All of the love in my tiny body."
        s "..."
        u "..."
    else:
        s "Someone please help me."

    scene utafirstmaidcafe20
    with dissolve

    u "Heheh~"
    u "Talking to you is fun."
    u "And I’m not just saying that as Uta-chan. "
    u "Did you ever get annoyed with me those first few days I transferred in? How I stuck to your side the whole time?"

    if bonus == True:
        s "Annoyed? Not really. "
        s "You talk a lot but it’s not like you do anything that actually disrupts my day."
        u "Well, that’s good. I’m glad I asked. "
    else:
        s "Yes."

    scene utafirstmaidcafe14
    with dissolve

    u "Question, and you can say no if it makes you feel weird, but did you maybe want to give me a ride back to the dorm after this?"
    u "I’m still new-ish to the area and not totally comfortable going alone yet."
    u "Io was gonna come meet me but I’m pretty sure she fell asleep or something."
    s "I don't have a car, so I can't give you a ride. But we can walk back if you'd like."

    scene utafirstmaidcafe15
    with dissolve

    u "An adult without a car?!"
    s "This is the city. We don’t really {i}need{/i} cars with all the public transportation here."
    u "Oh right. I’m not in the country anymore."
    u "Well then, did you want to walk back with me instead?"
    u "As long as I have some big guy like you next to me, I’ll feel a lot safer."
    u "That crazy brawl with Yumi really gave me a wake-up call about how weak I am."
    s "That crazy brawl was a two-second arm-wrestle, but sure. I’ll walk back with you."

    scene utafirstmaidcafe16
    with dissolve

    u "Yay! "
    u "But remember, no holding my hand unless I ask you to. "
    s "Right. Keep my hands in the vehicle at all times. You’ve said that before."
    u "Yes. Uta-chan is not for sale."
    u "Unless you hire me to come clean your room or your house or something. I’d probably do that for you."
    s "Ami normally handles all of that, but I’ll let you know if she just suddenly...stops for some reason. "
    u "Works for me!"
    u "Now- dig in, Master! Your food’s probably cold by now!"

    scene black
    with dissolve2

    "I hang around the cafe for the next hour until it’s time for Uta to leave."
    "The two of us walk back together and she tells me a little bit more about what life in Nara was like."
    "Apparently, before she came here to take care of her grandfather, she also did all of the cooking and cleaning around the house."
    "She seems a bit worried about how they’re all getting on without her over there, but it doesn’t seem to break her spirit at all."
    "Eventually, we make it back to the dorm and she trots up the stairs, thanking me again for bringing her back."
    "Then, the next thing I know, I’m headed back home to a {i}different{/i} maid."
    "Life sure has gotten interesting lately."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid1 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid5:
    scene utamaidfive1
    with fade
    play music "maidcafe.mp3"

    "I arrive at the maid cafe and find that it’s actually kind of busy for some reason tonight."
    "So busy that I don’t even have to deal with the inner struggle about whether to ring the bell or not as Uta immediately notices my presence and greets me at the entrance."

    scene utamaidfive2
    with dissolve

    u "Maaaaaasteeeeeeer~"
    u "Welcome baaaaaaack~"
    s "Are you crying right now?"
    u "I’m just so...{i}sniff{/i}...happy to see you..."
    u "It has nothing to do with how I’ve been on my feet for a million years...I’m totally fine..."
    s "Why not take a break or something?"

    scene utamaidfive3
    with dissolve

    u "Ugh...Spoken like a true non-customer-servicey-person..."
    u "I can’t just take a break when we’re this busy."
    u "We’re having a crazy sale thingy this weekend to try and bring in more customers-"
    u "And, on top of that, I’ve gotta train a new maid as well. I’m beat. I didn’t even get to have lunch today."
    s "Is that even allowed? Aren’t you a-"
    u "Part-time employee? You bet your butt I am. But that doesn’t change how I’ve gotta step up when there are...steps that need to be...stepped up."
    u "Or something."
    s "This is not the Uta-chan I know. That Uta-chan wouldn’t get so easily stumped by her own words."

    scene utamaidfive4
    with dissolve

    u "The Uta-chan you know and love is no more. She’s with her grandpa now."
    s "Can you stop bringing up your dead grandpa all the time, please?"
    u "Alas. I miss him dearly."

    scene utamaidfive5
    with dissolve

    u "Hey. You wouldn’t wanna put on a uniform and help me out by any chance, would you?"
    s "That might be the worst thing anyone has ever asked of me."
    u "So is that a no? Even though you love me to pieces?"
    s "There isn’t anyone I love enough to wear a costume like that."

    if bonus == True:
        u "Not even if it’s one I wore? "
        u "You wouldn’t put it on and think something lewd like “Uta-chan’s beautiful, bare skin touched this fabric. I can’t contain myself!” or something like that?"
        s "Okay, I’m definitely bad- but I’m not {i}that{/i} bad."
    else:
        s "Okay, you know what? I {i}do{/i} want to wear it. I just...shouldn't do that anymore."
        u "Anymore?"

    s "Also, there is no chance in hell that something you wore would ever fit me."

    scene utamaidfive6
    with dissolve

    u "That’s it. You and Io both hate me. She wouldn’t wear the costume either and she’d probably look even cuter in it than you would."
    s "I don’t think the “probably” is needed there. She’d look much better than me in a maid outfit."
    u "Now Uta-chan’s friend is being praised instead of Uta-chan. What a horrible day."

    play sound "dishes.mp3"

    s "..."

    fv "Ah! Shit!"
    fv "Um...U-Uta?..."
    u "I hope we never have to do something like this sale ever again..."
    s "Careful, Uta. You’re breaking character."
    u "I hope we never have to do something like this sale ever again, Master..."
    s "Better. Hang in there."
    s "Can I just take a seat wherever?"
    u "Of course, Master..."

    scene utamaidfive7
    with dissolve

    u "But...if you want my recommendation-"
    u "There’s this really cute girl over in the corner that would love your company if you’d be so obliged."
    u "And she hasn’t even placed her order yet, so you’ll probably be served faster if you sit with her as well."
    s "Beautiful girl?"

    scene utamaidfive8
    with fade

    s "Oh, Io is here."
    u "That’s right, Master!"
    u "The cute and cuddly bathhouse girl you know and love, Io Ichimonji. Slender, soft, and ripe for the plucking!"
    s "Aren’t you supposed to be upselling desserts and not actual human beings?"
    u "If she’s going to auction me off, I’m gonna auction her off! This is war!"

    scene utamaidfive9
    with fade

    u "Come on, Master. Don’t you think she looks all lonely over there by herself?"
    u "I’m sure she’d love a little bit of company. "
    u "Also, if you sit with her, I can kill a bunch of birds with a rock and have the new maid come out and take {i}both{/i} of your orders at once."

    "So it was just about efficiency..."

    u "I was planning on just testing things out with Io since she’s a friend of mine and won’t leave any bad reviews-"
    u "But two friends at the same time? This is a gold mine I can’t let slip away."
    s "..."
    u "What’s wrong? Why the silent treatment all of a sudden, Master?"
    u "Does Io make you nervous?"
    s "I kind of...you know."
    u "..."

    scene utamaidfive10
    with dissolve

    u "Ah! Master!"
    u "Were you upset because you wanted {i}me{/i} to be your maid, no matter what?"
    s "You are the only maid that matters to me, Uta-chan."
    u "Really?"
    u "Even though your [niece] works here?"
    s "Oh."
    s "Right..."
    u "Don’t worry. I won’t tell her you like me more."

    "That’s really comforting to hear from a girl who introduced herself to the class with “I will probably let things about you slip on accident. Don’t hate me for it.”"

    s "Thanks..."

    scene utamaidfive9
    with dissolve

    u "You don’t need to worry, though, Master. I’ll be right there with the new girl."
    u "I’ll shadow her while she takes your order so I can be sure she’s taking care of you just as well as I would."
    u "Well, maybe not {i}just{/i} as well. There’s no one that likes caring for you as much as your faithful Uta-chan does~"
    s "God I love you."
    u "Then go sit with Io and wait for me to come over there. "
    u "I’ll be back soon, kay? I’ve already kinda talked to you over here for too long."
    u "But this was the closest I had to a break all day, so at least I can be happy I got to spend it with you~"

    scene black
    with dissolve

    "Uta winks at me, doing a twirl as she skips away to the kitchen."
    "I need to squeeze past a few other customers who had pulled their chairs out a bit too far on my way to Io-"
    "But I eventually make it there and...I guess I startle her as she jumps up in surprise the second I sit down."

    scene utamaidfive11
    with dissolve

    i "Oh my God...Hey. "
    i "You scared the crap out of me."
    i "I thought you were just some random person sitting down at the table with me for a second."
    s "Hey Io. Independent as ever, I see."

    scene utamaidfive12
    with dissolve

    i "Nahh. Just bored. "
    i "Thought I’d come see Uta since I didn’t have anything else to do tonight."
    i "You’re here for the same reason, I guess?"
    s "Yeah. I think I’m starting to develop a bit of a maid addiction."

    scene utamaidfive13
    with dissolve

    i "Really? You don’t seem like the type who would be into that...cutesy sort of thing."
    s "You don’t either but...here we are."
    s "A maid cafe is actually on the list of places I’d least expect to see you given your apparent distaste for girls."

    scene utamaidfive12
    with dissolve

    i "I wasn’t planning on staying long. Was just going to eat and then probably go out for a walk or something."
    i "I think Uta said something about needing my help, too, but I have no idea what it’s about."
    s "I think I do. "
    s "She’s training a new girl and I think she wants us to be her first test subjects."

    scene utamaidfive14
    with dissolve

    i "Oh."
    i "Uhh..."
    i "Want to order for me?"
    s "..."
    s "Really?"
    i "Have you ever dealt with an inexperienced employee before? It’s awkward and uncomfortable and I already have a hard time dealing with Uta’s fake maid personality."
    s "To be honest, she seems mostly the same to me."
    i "Nuh-uh. Hearing her call herself Uta-{i}chan{/i} makes me cringe harder than some crummy 80’s slasher film."
    s "Weird comparison but I think I get it."
    fv "Wait, already?! I thought I was just doing backroom stuff today?"
    u "You can’t hide from customers forever, Osako! The floor is where all the real money is!"

    scene utamaidfive15
    with dissolve

    s "Osako?"

    "Isn’t that my karate instructor’s name?"

    i "Someone you know?"
    s "..."
    s "No way. The only person I know with that name is a total badass and would never work somewhere like this."

    u "Uta-chan hidden technique...maid-push! Aaaaand-"
    u "...Ngh!"
    u "Why aren’t you moving?! I pushed you as hard as I could!"
    fv "I didn’t even feel anything..."
    u "No, really!"
    u "Are you wearing some sort of...vest?...Why the heck is your body so hard?"
    u "What is on you, Osako-chan?!"
    fv "That’s just how my body is, okay?! There’s no need to touch me..."
    fv "I’ll go out there and try but...I still don’t have any idea what I’m doing and I-"
    fv "Well..."
    u "Worried about the way you look?"
    fv "..."
    u "Don’t worry. The guy at your table’s a real go-getter and I’m sure he’ll think you’re beautiful."

    scene utamaidfive16
    with dissolve

    i "Ooooh. A real go-getter, huh?"
    s "I don’t go and get anything. It just comes to me with minimal effort."
    i "Uh-huh. Likely story."
    i "Try not to flirt too hard while you’re with another girl, Sensei."
    i "And don't forget to order for me."
    s "Am I still doing that?"
    i "I wouldn’t have it any other way."

    scene utamaidfive17
    with dissolve

    fv "Um...Good evening...Master..."
    fv "Are you ready to..."
    fv "..."
    fv "Oh...you’ve gotta be kidding me."

    scene utamaidfive18
    with dissolve

    os "Why? Why are you here?"
    os "Hanging out with [high_school] girls during the afternoon isn’t enough, you need to do it at night, too?"
    s "I could be asking you the same question. Why are you even working here?"

    scene utamaidfive19
    with dissolve

    os "Job security, okay? I still don’t have a guarantee in writing from that damn rich family that I’ll be keeping my instructor job, so I’m...weighing other options."
    s "And...a maid cafe was in that list of options?"

    scene utamaidfive20
    with dissolve

    os "Yeah...I bet I look really out of place up here, huh?"
    s "Wait, I didn’t mean it like that. I think you look-"

    scene utamaidfive21
    with dissolve

    u "Oof. Bad move, Master."
    u "Osako-chan was finally brave enough to come say hi to you and you cut her down just like that."
    u "For someone who spends so much time with girls, you really have no idea what to say to them, do you?"

    scene utamaidfive22
    with dissolve

    os "It’s fine. I spend so much time bossing this guy around that he’d probably greet me that way no matter how I looked."

    scene utamaidfive23
    with dissolve

    u "Bossing him around?!"
    u "Master is an M when I thought he was an S this whole time?!"
    os "S?..."
    os "M?..."
    os "What does that even mean?"
    s "I think she’s misinterpreting our relationship."

    scene utamaidfive24
    with dissolve

    i "I believe she is. Sensei is clearly an S."
    u "Io! I forgot you were even here!"
    os "What’s with all these letters?..."
    i "I didn’t plan on joining in on this conversation, but I don’t mind fighting for Sensei’s honor when he is clearly not an M."

    if bonus == True:
        scene utamaidfive25
        with dissolve

        os "Dude...are you really stringing along these ones, too?"
        os "Ayane alone isn’t enough?"

        scene utamaidfive26
        with dissolve

        u "Ah! So the girl in the bath was Ayane! I knew it!"
        u "I need to add that to the list!"
        s "Please don’t add anyone to any list, Uta."
        os "You...{i}bathe{/i} with her too?"
        s "Does such a detail really surprise you at this point?"
        i "Sure. As a bathhouse employee, I can confirm that there are plenty of co-ed family members that bathe together all the time."
        i "Granted, some of them have gotten up to some pretty raunchy stuff without realizing there are cameras, but not {i}all{/i} of them are like that."
        i "Just...most."
        s "Thanks, Io. That really helps."
        i "Really? Because it doesn’t sound like it would after hearing it out loud."
        s "I was being sarcastic..."

    scene utamaidfive27
    with dissolve

    os "Um...Uta? Can I go back into the kitchen now?"
    u "Huh? But you haven’t even taken their orders yet."
    os "Are they still going to order after all of this? I would just leave if I were in their shoes."

    scene utamaidfive28
    with dissolve

    s "Io and I will both have whatever today’s special is."
    u "Why are you ordering for Io?! Are you two dating now?!"
    u "What happened in the three minutes you were alone together?!"
    i "What happened is I told him he could order for me. We’re not dating."
    u "Really?! Cause you never know with this scoundrel!"
    os "Alright, so...I feel really awkward right now, but I heard your order and...I think that means my job is done."
    os "I’ll go tell the kitchen staff and..."
    os "Um..."

    scene utamaidfive29
    with dissolve

    os "If you could...not tell anyone else in the dojo about me working here on the side, that would be kind of awesome."
    s "Deal. As long as you don’t tell Ayane you saw {i}me{/i} here either. She gets jealous pretty easily."
    os "Consider it done. "
    u "Yes. {i}Consider it done{/i}, indeed."
    s "Do you even know what we’re talking about, Uta?"
    u "No. I’m too busy scowling at you."
    u "Does it look intimidating? Do you {i}fear{/i} Uta-chan?"
    s "I'm utterly terrified."

    scene utamaidfive30
    with dissolve

    i "Hey, I don’t work here so correct me if I’m wrong, but..."
    i "Don’t you two need to, you know, get back to work? "
    i "There’s a huge line of people at the door right now."
    u "Ah! Osako-chan! Retreat! "
    u "If we’re quick enough, they might think this is just a normal restaurant and not a maid cafe!"
    os "Uhh...no. I think they’re all pretty sure this is a maid cafe."
    u "Either way! Run! Now!"

    scene black
    with dissolve2

    "Uta grabs Osako by the sleeve and pulls her into the back room."
    "Roughly thirty seconds later, Uta is pushed back out onto the floor by someone who I imagine is her supervisor and proceeds to handle everyone all on her own."
    "That poor girl."
    "Customer service really seems rough- especially in a place like this."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid5 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid10:
    scene utamaidten1
    with fade
    play music "maidcafe.mp3"

    "Once again, I find myself spending way too much time and way too much money at the maid cafe."
    "I’ve been here for going on two hours so far and, despite several other customers coming in, I’ve managed to keep Uta-chan all to myself."
    "This has, of course, come at a great cost."
    "And if Yumi winds up being cut off of my phone plan as a result, I have no regrets."

    s "Hey, Uta. How would you feel about Yumi working here so I don’t have to pay for her cell phone anymore?"

    scene utamaidten2
    with dissolve

    u "Yumi? Working here?"
    u "Not just anybody can be a maid, Master. This line of work takes a surprising amount of skill and perseverance."
    s "True. She might be a “business owner,” but I don’t think she’s quite conniving enough to hold down the fort here."

    scene utamaidten3
    with dissolve

    u "Now you’re startin’ to get it."
    s "Also, aren’t you going to ask about why I’m paying for her phone bill?"

    if bonus == True:
        u "Is it cause she’s poor and you want her to touch your wiener?"
        s "That-"
        s "I mean, you’re not entirely wrong."
        s "I don’t think you’re allowed to say “wiener” while you’re working, though."
    else:
        u "Nope! Cause I know you'd do it for me too if I asked!"

    u "Master is a special customer who won’t tell my boss even if I start doing really mean things like spitting in his food or stealing money directly out of his wallet."
    s "To be fair, I think I’ve already proven that my wallet is as good as yours."

    scene utamaidten4
    with dissolve

    u "Poor Ami. She’s so dedicated to you and yet here you are, flirting with her senpai. "
    s "Yes but, on the bright side, she at least has some spending money now."

    scene utamaidten5
    with dissolve

    u "But not as much as {i}I{/i} do..."
    u "You know, Master...maybe if you bought Uta-chan a car...you would get to see her a little more often."
    s "I haven’t even bought a car for myself yet."
    u "Wanna share one?"
    u "You’ve gotta put it in your name, though, cause I don’t have any credit history yet."
    s "Please don’t push me on this because I {i}will{/i} cave if you’re the one asking."
    u "Pleeeeease, Master? Uta-chan’s been such a good girl."

    scene utamaidten6
    with dissolve

    u "She even made all this delicious food for you all by herself."
    s "I know for a fact that you have other maids cooking in the back room. "
    u "But if you use your imagination, it’s exactly like {i}I{/i} made it, right?"
    s "Wrong. And you’re not getting a car."

    scene utamaidten7
    with dissolve

    u "But...but I wanted to take you somewhere special to me..."
    s "..."
    u "I guess you hate me, though..."
    s "What is this “special” place you were going to take me to, Uta-chan?"

    scene utamaidten8
    with dissolve

    u "The mall. "
    s "That’s hardly special."
    u "Isn’t any place special as long as you leave happier than you were when you arrived?"
    s "Not if it comes at the cost of half of my salary and-"
    s "Oh. Wait. That's around the same amount I'm spending here."

    scene utamaidten9
    with dissolve

    u "Yup! And this place is the most special place on earth to you!"
    u "You’ve really got to stop being so easy, though, Master. Uta-chan might be the perfect maid and she might like you very much, but you still work just as hard as-"
    s "I’m going to stop you right there because we are both well aware that I do not work hard at all."

    scene utamaidten10
    with dissolve

    u "Thanks, I don’t know if I was gonna be able to finish that sentence anyway."
    u "In fact, I’m pretty sure I worked harder on the whole dorm wars thing than you’ve worked since I transferred in."
    s "That’s a very fair assessment. However, I implore you to remember who it was that {i}judged{/i} those competitions."

    if bonus == True:
        u "Did having your childhood girlfriend ride your morning wood while Makoto and I spectated tire you out?"
    else:
        u "Did having your childhood girlfriend giving you a sleeping potion tire you out?"
        s "Well, that {i}is{/i} the purpose of a sleeping potion. Also-"

    s "Noriko’s {i}sister{/i} was my childhood girlfriend. Not Noriko."
    s "Also, how do you know that?"

    scene utamaidten11
    with dissolve

    u "I didn’t..."
    u "I was just makin’ a joke and now I know a thing that’s gonna really upset Maya when she finds out you’re cheating on her."
    s "For the millionth time, Maya and I are not dating."
    u "Does Maya know that?"
    s "Maya will tell you the same exact thing."

    if bonus == True:
        u "Maya told me you two go at it all night long."
    else:
        u "Maya told me you like to sleep under the bed sometimes."

    s "I know Maya well enough to confirm that this is not a thing she would ever say."

    scene utamaidten12
    with dissolve

    u "A-ha! So you {i}are{/i} dating!"
    s "No."

    if bonus == True:
        u "I bet you two bang like bunnies in her dorm room while Ami is here at the cafe!"

        "{i}God I wish.{/i}"

        s "Ami works mornings. Even I’m not so much of a degenerate that I would wake up extra early just to go have sex with someone."

        scene utamaidten13
        with dissolve

        u "Wh...What if that someone was..."
        u "Me?..."
        s "..."
        u "..."
        s "I would go a year without sleeping if it meant even seeing you naked."
    else:
        u "So you admit it!"
        s "No."

    play sound "thump.mp3"
    scene utamaidten12
    with hpunch

    u "A-ha! I knew it!"

    if bonus == True:
        u "And sorry, Master! But you’re still a bajillion years away from seeing Uta-chan’s little girls up close and personal!"
        u "Maya, though-"
        s "I feel like that’s somehow even further off."

    scene utamaidten14
    with dissolve

    u "I feel like you’re a bad judge of character."
    u "Didn’t you see how she freaked out when Noriko transferred in? Why would she have done that if she didn’t feel something for you?"
    s "Because she feels many {i}negative{/i} things about Noriko."
    u "And that’s not just you in denial?"
    s "You know what? Let’s just talk about something else."
    u "Must be kinda exhausting having so many people you’ve gotta split your time between, huh?"
    s "It’s less exhausting if I can manage to keep all of that time a secret from literally everyone."
    u "Aren’t ya telling the wrong person? I can’t be trusted with that kinda info."
    s "It’s fine because I’m telling Uta-chan and not Uta."

    scene utamaidten15
    with dissolve

    u "Ah! Loophole!"
    u "Uta-chan doesn’t go to[school], so all of the secrets she knows disappear and reset each time she switches character modes!"
    u "You’re a genius, Master!"
    s "No, I’m just very good at concealing inevitable truths from myself and everyone around me."

    if dormwarfloor1win == True:
        scene utamaidten16
        with dissolve

        u "Speakin’ of inevitable truths...enjoy your stay with the stupid floor one girls during the beach trip and not with us cuter, spunkier gals from the second floor!"
        s "Sounds to me like someone is still a little bitter about losing."
        u "As bitter as the black coffee that I also made for you all by myself."
        s "It’s a little less impressive making coffee than it is making like four different entrees."
        s "Thankfully, you didn’t make any of those, so it’s not something we should worry about right now."

        scene utamaidten14
        with dissolve

        u "Did you at least have fun?"
        u "Makoto and I busted our butts and, even if my floor doesn’t get to keep you overnight, I still feel like we all got a little closer to you and everybody else."

    if dormwarfloor2win == True:
        scene utamaidten12
        with dissolve

        u "Speakin’ of inevitable truths, how ‘bout those second floor gals, right?!"
        s "Is it time to brag about your recent victory?"

        if bonus == True:
            u "It’s time to brag about Uta Ushibori’s recent victory! Uta-chan has no affiliation with that tiny bundle of boobies!"
            s "Well, I’m glad that you won. It was a well fought battle and I’m excited to-"
            u "Get busy with a bunch of thirsty girls in the middle of the night?!"
            s "Shh. Maya could be around the corner and we don’t want her to get jealous."

            scene utamaidten15
            with dissolve

            u "Ah! Good point! If you’re cheatin’ on her, we’ve gotta keep it a secret!"
            s "Thank you for understanding, Uta-chan."
            u "Yeah! If Maya finds out and kills you, who else will buy every item on the menu three times a week?"
            u "I’ve gotta make money somehow, Master!"
            s "Oh."
            s "Oh..."

            scene utamaidten14
            with dissolve
        else:
            u "We're the fucking best! Ain't nobody got shit on us!"
            u "Fucking floor one chumps think they're all that. They ain't shit! Fuck 'em!"
            s "You are so vulgar in the Patreon version."
            u "Fuckin' right I am!"

        u "Did you have fun, though?"
        u "During the dorm war, I mean."
        u "Makoto and I busted our butts on that thing."

    if dormwartie == True:
        scene utamaidten16
        with dissolve

        u "Speakin’ of inevitable truths, how the heck did the dorm war end in a tie?!"
        s "Uta, do you understand what the word “inevitable” means? Because that outcome was definitely not something predetermined and it’s my fault things ended up that way."
        u "Then why’d ya let that happen?! That was a great chance to prove to us second floor girls that we’re not too far behind the rest of the crowd!"
        s "I just judged the competition based on who I thought should win. It wasn’t about who is further ahead or further behind in terms of relationships with me."

        scene utamaidten14
        with dissolve

        u "I know, I know..."
        u "Just kinda anticlimactic to spend the whole weekend fighting and then not even have a winner."
        u "Did you at least have fun, though?"

    s "Yeah. I had a lot of fun. And I’m sure the beach will be just as good."

    scene utamaidten17
    with dissolve

    u "Yeah...what’s up with that, by the way?"
    s "What do you mean?"
    u "I mean like, why organize a trip to the beach in winter? Isn’t that a little weird?"

    "It’s not like that was the {i}original{/i} plan."
    "We just...apparently do that every other cycle or something?"

    if bonus == True:
        "I still have no idea how or why it works, but I’m not about to question the mysteries of the universe if they're going to create more opportunities for me to see girls with less clothing on."

    s "Beats me. But a vacation is a vacation."

    scene utamaidten18
    with dissolve

    if bonus == True:
        u "Ahh, yes. Yes. Of course you wouldn’t question the reasoning behind it because you know you’ll get to stare at my butt for {i}real{/i} this time."
        s "Exactly."
        u "Do what you must. But please do not touch the merchandise without first putting a down payment on it."
        s "Is everything I spend here not enough of a down payment?"
        u "Cheating is bad, Master. I can not support your efforts to mislead Princess Maya no matter how much you like my butt."
    else:
        u "Here's hoping I don't see anyone drown this time."
        s "What?"

    u "On a more serious note, though, I am kinda worried about this whole beach thing."

    if bonus == False:
        s "How is that more serious?"

    u "We had a couple ponds and stuff in Nara, but I’ve never been in the ocean before."

    scene utamaidten19
    with dissolve

    u "You gonna protect me from sharks and stuff? And make sure I don’t drown?"
    s "I was kind of planning on just watching from the sidelines and then probably going back to my room to relax."

    if bonus == True:
        "And by relax I mean have sex with an assorted variety of girls because it is much harder to contain myself in situations where I am permanently erect."

    scene utamaidten20
    with dissolve

    u "Ugh! You and Io are exactly the same! Always bein’ so...antisocial and stuff."
    u "Like, what’s so hard about goin’ out there and havin’ fun?! Jeez!"
    s "Having fun is exhausting. I’d much prefer to keep myself separated from that side of existing and simply reap the benefits that come from {i}other{/i} people having fun."

    scene utamaidten21
    with dissolve

    u "Guh. No wonder she snuck into your room instead of joining in on our slumber party."
    s "Uhh..."
    s "I’m just going to assume she told you and that you’re not secretly surveilling my every move."

    scene utamaidten22
    with dissolve

    u "Yeah, but don’t get mad at her about it. I kinda forced it out of her."
    u "Io can be really complicated, but I know how to deal with her for the most part."
    u "Takes one to know one and all that."
    s "I definitely don’t see any sort of resemblance between the two of you, so I’m not sure how accurate that last statement is."

    scene utamaidten23
    with dissolve

    u "Okay. Maybe I’m a little {i}less{/i} complicated than her...but that doesn’t mean what you see is what you get."
    u "We’re all a little complicated in our own ways, Master."
    u "Io...me...you..."
    u "But that’s what makes us people. Nobody can be happy all the time and we’ve all gotta do everything we can to keep a smile on our faces, even when it seems impossible to do that."
    s "Am I going to be charged extra for this life lesson? Because I’m kind of running out of money."

    scene utamaidten24
    with dissolve

    u "Course not."
    u "I’m just sayin’ that you can never really know what somebody is like unless you spend lots and lots of time with them."
    u "That’s why I feel comfortable saying I’m not much different than Io."
    u "We’ve just got...unique ways of handlin’ the stuff that hurts us the most."
    u "I’m sure you do too."
    u "But it’s not up to me to point out your bad sides. ‘Specially not while I’m wearin’ a maid outfit."
    s "Excuse me, Uta-chan, but you shouldn’t be pointing out or acknowledging that I even {i}have{/i} bad sides while you’re wearing that outfit."

    scene utamaidten25
    with dissolve

    u "R-Right...I’m sorry, Master."

    scene utamaidten26
    with dissolve

    u "So, back to happier things!"
    u "How ‘bout you tell me what exactly went down with you and Io at your hotel room?"
    u "She kinda skimped me on the deets."
    s "I wish the answer was exciting or interesting, but it’s actually kind of depressing."
    u "I’m all ears, Master! Let Uta-chan wash those worries away!"

    scene black
    with dissolve2

    "I tell Uta about the morning after Io snuck into my room, but conveniently leave out all of the details about how said morning ended up."
    "It’s one thing having Io know about Chika, but trusting someone like Uta with that information seems like it could lead to catastrophe rather quickly."
    "It’s strange having one girl who loves secrets but can’t keep them paired with a second girl who hates secrets and {i}does{/i} keep them."
    "But I guess there’s not much helping it."
    "Maybe the two of them do have more in common than I realize."
    "But, at least on a surface level-"
    "I can’t see it at all."
    "I stay for another hour or so before Uta needs to stop talking to me and focus on closing the store."
    "And, as always, I head home with my hands in my pockets- one of them wrapped tightly around a wallet that is much lighter than normal."
    "This girl is going to bleed me dry."

    $ renpy.end_replay()
    $ utamaid10 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid20:
    scene nightsky
    with dissolve2
    play music "justlights.mp3"

    "It’s cold."
    "But you’ve heard that before."
    "You’ve heard virtually everything before, haven’t you?"
    "One of the downsides of sharing your thoughts with people is that it’s very easy to lose track of who you’ve told what or how many times you’ve said {i}that.{/i}"
    "I think this to myself, for what may be the millionth time (Even I have lost count) and wonder who it is I’m referring to."
    "Who am I sharing these thoughts with?"
    "I look up at the stars and hope, for some reason, that it starts to snow."
    "Maybe it’s just because I’m looking for a change of scenery."
    "Or maybe it’s something a little more confusing in nature."
    "Like there’s something I associate the snow with that will subconsciously wipe away any and all of the lingering negativity coursing through my veins."
    "I think more about veins and the circulatory system. "
    "Of how our bodies are machines."

    if bonus == True:
        "Of how each and every part of us just naturally falls into place as the result of a man cumming inside of a woman."
        "And I realize that nothing in this world is really strange at all when entire existences and consciousnesses are being formed as the result of rough doggystyle sex in bathrooms."

    "I think more about veins and the circulatory system. "
    "Of how it’s all just a bunch of wires, not much different from what it would look like if you were to tear open one of your walls."
    "My mind races, but moves not even half as effectively as a horse who breaks its leg at the midpoint of a race and needs to be put down."
    "I think of splaying myself out on the concrete and letting someone put {i}me{/i} down while a group of children watch on in shock."
    "But I stop when I realize that I have so much left to live for. "
    "I stop when I realize I have not yet begun to live at all."

    s "..."
    s "..."
    s "..."
    u "Uhh..."
    u "You okay, Sensei?"

    scene utakaraoke1
    with dissolve2

    s "What?"
    u "You kinda just walked up to me and Osako and started lookin’ at the sky."
    u "Has Io been sneakin’ you some of her pills? Do we need to schedule an intervention?"
    s "I’m pretty sure I’m fine. What are you doing outside, though?"
    s "Aren’t you two supposed to be at work?"

    scene utakaraoke2
    with dissolve

    u "I already told you when you first showed up..."
    u "We close at 10:00 and it’s like 10:30 right now."
    s "When did it get so late? I feel like it was the afternoon just a few minutes ago."

    scene utakaraoke3
    with dissolve

    u "Ah! Dementia!"
    u "It’s grandpa Ushibori all over again!"
    u "Who am I, Sensei?! Tell me you remember me!"
    s "You are my girlfriend and personal maid."

    scene utakaraoke4
    with dissolve

    u "Phew...it looks like you're okay after all."
    os "Can you two take your flirting somewhere else? I’m starting to get a headache."
    u "Osako-chan is just sad that her girlfriend isn’t here to pick her up yet."
    s "Don’t worry, Osako. Uta and I will hang out with you and keep you safe until she gets here."
    os "You are...aware that I’m a fifth degree black belt, right? I could hold my own against basically everyone in this city."
    s "We will protect you. Don’t worry."

    scene utakaraoke5
    with dissolve

    os "You know, sometimes, I wish that rich girl {i}did{/i} buy the dojo."
    u "So, whatcha gonna do now that ya can’t be pampered by Uta-chan and stuff your face with cupcakes for the rest of the night?"
    s "Probably follow you around like some kind of stalker or something."

    scene utakaraoke6
    with dissolve

    u "Uhh...hahah..."

    if bonus == True:
        s "If you want the realistic answer, I’ll probably just go home and watch porn or something."
    else:
        s "If you want the realistic answer, I’ll probably just go home and cry myself to sleep."

    scene utakaraoke7
    with dissolve

    u "Here’s an idea! How about you come out with me instead?"

    if bonus == True:
        u "I obviously can’t do for you what those sexy porn ladies would do, but we can at least find our own non-sexual ways to have fun!"
        s "Non-sexual fun is an oxymoron."
    else:
        s "Why would I do that? Life is miserable and I just want to frown in isolation."

    u "Sounds to me like a certain somebody has never experienced karaoke before."
    s "Every experience I have with karaoke is bad."
    u "Well, looks like we’re gonna have to break the streak!"
    u "This is what I normally do after getting off work anyway. "
    s "You leave the maid cafe at 10:30 to go do karaoke by yourself?"
    u "I’m not always alone! Osako comes with me sometimes."
    s "Does she now?..."

    scene utakaraoke8
    with dissolve

    os "Don’t sound so surprised about it..."

    if bonus == True:
        u "Unfortunately, Osako-chan’s gotta get home and give her woman some of that sweet, sweet lovin’, so I was gonna go alone tonight."
        s "Have fun, Uta. I’m going to go back to Osako’s place and watch the whole loving thing."
    else:
        s "I am so surprised."

    if day333part2 == True and bonus == True:
        s "Which is more than she can say since she apparently likes being blindfolded and-"

    scene utakaraoke9
    with dissolve

    os "Excuse me?"

    if bonus == True:
        u "I guess I’ll tag along too. We can watch ‘em together as long as we stay on opposite sides of the room."
        s "Deal."
        os "Fuck off. We’re probably just going to watch a movie and fall asleep anyway."
        s "Don’t be like that. Wakana looks like she could use a good orgasm or two to be brought back to life."

        scene utakaraoke10
        with dissolve

        os "She’s plenty alive and plenty satisfied, thank you very much! "
        u "Sounds to me like Osako-chan could use a good rubdown herself, right Sensei?"
    else:
        s "You are weak and your arms are noodles."

    scene utakaraoke11
    with dissolve

    os "I...I’m going for a walk! "
    os "And if Wakana shows up, don’t you dare try hitching a ride back to our place or I’ll kick both of your asses!"
    s "Osako, really? Karate is supposed to be used for self-defense, not picking on people weaker than you."
    os "I’m...defending my honor. Now, goodbye."

    scene utakaraoke12
    with dissolve

    "Osako leaves and suddenly it’s just Uta and me."
    "She wastes no time in pressing the issue at hand, however, as we’re immediately discussing the probability of karaoke again."

    u "So, you gonna come with me? Or are you gonna let a defenseless lil’ girl like me wander around Kumon-mi all by herself?"
    s "You’ve already said that’s something you do all the time."
    u "Doesn’t mean I wouldn’t be happy to have a big strong man like yourself to protect my pint-size body from bein’ snatched up and thrown into a van."
    s "I’ll gladly accompany you. But know now that I’ll just be awkwardly staring at you as you sing for the entire night."
    u "You think I’m not used to you staring at me by now? Come on, Sensei. "
    u "You’ve barely taken your eyes off of me since I strolled into[school] that fateful winter day."
    u "You know, when you were hanging out with your girlfriend Maya at her locker."
    u "Actually, wanna invite her to karaoke with us?"

    if bonus == True:
        u "I’ll even sing some cute lil’ love songs to get you two in the mood!"
        s "If there is any song that will put Maya in “the mood,” I highly implore you teach it to me."
        u "That I can do, Sensei! But not if we’re out here."
        u "The karaoke place is on the way back to the dorm, so just stick with me and you’ll be learnin’ how to woo your lady in no time at all!"
    else:
        s "No. She's always mean to me and it makes me feel bad."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Uta begins to march away from the gate outside of the maid cafe and the two of us start heading over to the karaoke place."
    "I’m not sure if it will be the same one I’ve been to with Ami and the others before but, if it {i}is{/i}, I really hope Ayane isn’t there."
    "There’s only so much Despacito one person can take, and I have already greatly surpassed my lifetime allowance of it."
    "Uta and I remain close together, just an inch or two apart, as we wander down the streets."

    if bonus == True:
        "I think of veins and the circulatory system once again, but in an exponentially more suggestive way this time."
        "I can’t be blamed for this, though."
        "Karaoke this late at night with just one guy and one girl typically only means one thing."
        "And even though Uta may only be in this to sing and get some of the energy out of her system, I’m sure she knows how it’ll look too."
        "And yet we walk."

    "And, after ten minutes or so, we arrive at our destination..."
    "........."
    "......"
    "..."

    scene utakaraoke13
    with dissolve
    play music "utasings.mp3"

    if bonus == True:
        "I’m forcibly dragged into a private karaoke booth as soon as the two of us reach the place and, just as things start to look like they’re going to get exciting, Uta grabs a microphone and breaks out into song."
    else:
        "I’m forcibly dragged into a private karaoke booth as soon as the two of us reach the place. And just as I think we're about to hug, Uta grabs a microphone and breaks out into song."

    "I can already tell in just the several minutes we’ve been here that it’s something she’s done hundreds of times before."
    "Probably thousands if we’re taking the whole time loop thing into consideration and-"
    "Actually, that wouldn’t be right, would it?"
    "I know she worked at the maid cafe before transferring into [kumon_mi_high], but I highly doubt she was doing something like this before commuting all the way back across town."
    "Either way, I awkwardly stand around as she cycles through different pop songs and, of course, she also has somewhat of a dance routine for each one."
    "It’s a lot different than when Ami and the others come here but, even though her voice isn’t perfect, her energy and presence are mildly exhilarating. "
    "If I was into idols (Sorry, Niki) and other stuff like that, I’d probably find myself falling for her right about now."

    if bonus == True:
        "The only thing is, I’ve kind of already cemented Uta as an ideal woman in my eyes and I would not want to sleep with her any less even if she was absolutely horrible at singing and dancing."
        "Thankfully, she isn’t."
        "So...that’s just a plus I guess."

    scene utakaraoke14
    with fade

    "Every once in a while, she’ll make eye contact with me and try to get me excited, but..."
    "I am me. "

    if bonus == True:
        "And excitement is, unfortunately, not a trait I inherited from whoever it was that decided to have rough doggystyle sex and lay out the wires inside of my body."
        "I {i}am{/i} at least respectful enough to stand, though. "
        "Also, it gives me a better view of Uta because she tends to bounce a lot when she dances and...I’m sure you can guess what that means."
        "Sidenote: I really wish she wasn’t actually a prude and that she shared my same opinions on the idea of fun and its correlation to sexual contact."
        "But alas."
    else:
        "I am a sad boy."

    scene utakaraoke15
    with dissolve

    u "Sing with me, Sensei!"
    s "I don’t know this song."
    u "Who cares?! The words are right there on the screen!"
    s "I don’t sing."
    u "What if I let ya put your arm around me? That enough to get you to act happy?"
    s "Just have fun on your own and I’ll keep watching. "
    u "You’re not even looking, though!"
    s "If I look at you, I’ll have a harder time saying no."
    s "You’re annoyingly cute."

    scene utakaraoke16
    with dissolve

    u "Sing!"
    s "No."

    if bonus == True:
        "Uta grabs my chin and tilts my face toward her, making it incredibly hard to not grab her and not only ruin her song but break several of this establishment’s rules in the process."

    u "Sing!!"
    s "Why?"
    u "Because it’s fun!"
    u "You’ve gotta smile, Sensei!"
    s "I’m perfectly content with just watching."

    scene utakaraoke17
    with dissolve

    u "Sing, damn it!"
    s "Karaoke is bad."
    u "You will have fun with me and you will like it!"
    s "Stop it."

    scene utakaraoke18
    with dissolve

    u "AHHHHHH!"
    s "You’re messing up the song."
    u "You don’t care about the song! You don’t care about Uta-chan! You don’t care about anything!"
    s "Uta, I’m starting to lose balance."
    u "I’m starting to lose {i}patience!{/i} I’m on my fifth song and I haven’t even heard a peep outta you yet! "
    s "Uta-"

    scene utakaraoke19
    with dissolve

    u "How do you expect to ever marry me if you can’t even sing a little song?! It’s not that hard!"
    s "I am going to fall now."
    u "I’m 4’11! Are you really about to be taken down by a girl my size?!"
    s "Yup. Brace for impact."
    u "Sensei!"

    scene black
    with hpunch
    play sound "thump.mp3"

    "Now, I know what you’re thinking...and I’m sure it’s exactly how Uta put it."
    "And yes, I did get taken down by a girl 100lbs lighter and an entire foot shorter than me."
    "But A: My foot had gotten wrapped around a wire. And B: Why would I try and prevent this?"
    "Because now the two of us look like this."

    play sound "static.mp3"
    scene utakaraoke20 with flash
    stop sound
    play music "heartbeat.mp3"

    u "..."
    s "..."
    u "Um..."
    u "Hi..."
    s "Hey."
    s "Are you okay?"
    u "Me?"
    u "Yeah."
    u "I’m...fine."
    u "You kinda broke my fall."
    s "It appears that I did."
    u "Um..."
    u "Thanks for...protecting me?"
    s "No problem."
    s "I kind of warned you that this was about to happen, though."
    u "It wouldn’t have happened if you’d have just sung."
    s "All things considered, I’m kind of glad I didn’t."
    u "You’re...breakin’ a bunch of Uta-chan’s rules right now, Sensei."
    s "You’re the one on top of me."
    u "..."
    s "..."

    scene utakaraoke21
    with dissolve

    u "Huh. "
    u "I guess I am."
    s "..."
    u "..."
    s "And...you’re okay with that?"
    u "..."
    s "..."
    s "Uta?"

    scene utakaraoke22
    with hpunch
    stop music

    u "Ah! S-Sorry! I just..."
    u "The...blood rushed to my head from the fall!"
    u "I’ll get up!"

    scene black
    with dissolve2

    "Uta quickly hops off of me and pats herself down to straighten out her clothes."
    "The song that had been playing comes to an end and fills the room with silence."
    "Then, after a moment of respite for each of us, we quietly sit down on the couch and wait for the awkwardness to fade."

    scene utakaraoke23
    with dissolve2
    play music "thesleepingcity.mp3"

    s "..."
    u "..."
    s "So-"
    u "What’s that phrase about the elephant in the room again?"
    s "I believe that would be “the elephant in the room.”"
    u "We should probably talk about that."
    s "You mean how you got all red and looked like you were about to kiss me just now?"

    scene utakaraoke24
    with dissolve

    u "Uhh...yeah."
    u "You clearly didn’t buy the blood thing, so...I figure I’ve gotta explain myself or stuff will get weird."

    if bonus == True:
        s "Why didn't you just do it?"
    else:
        s "We should have just hugged instead."

    scene utakaraoke25
    with dissolve

    u "Sensei, I understand that you may be head over heels in love with me, but please don’t mistake my moment of confusion for the desire to smooch you."
    u "I just needed a second to figure out what the right move for everyone was."
    s "Everyone?"
    s "But we’re the only two people here. No one would have known if anything happened."

    scene utakaraoke26
    with dissolve

    if bonus == True:
        u "Bet you’re regretting missing that once in a lifetime opportunity, huh? We got really close to doing something really naughty. "
        s "I didn't realize it was up to me to make the first move there."
        s "Also, I don’t consider kissing “really naughty.”"
        u "That wasn’t just normal kiss territory. That was tonsil hockey territory. It was only gonna get crazier from there."
        s "I wish it did."
        u "Of course you wish it did. Uta-chan’s stolen your heart the way you’ve stolen a bunch of other people's."
        s "And I’m guessing those people are the ones you’re talking about when you say you “wanted to make the right move for everyone?”"
    else:
        u "I would have told everyone because I plan on sabotaging all of your hug-based relationships from this point on."
        s "Uta no."
        u "Sensei yes."
        s "With {i}everyone?{/i}"
        u "Everyone."
        s "Who does that entail?"

    scene utakaraoke27
    with dissolve

    u "Everyone means everyone."
    u "I’m glad you think I’m cute and that you wanna kiss me and stuff, but I’m really not as great as you think I am."
    s "What do you mean?"
    u "I mean that I’m really dumb and that I’d like to be forgiven for any dumb things I do around you."
    u "Like givin’ into that late night karaoke booth mood and gettin’ all up in your face."

    scene utakaraoke28
    with dissolve

    u "Or usin’ this opportunity to invite you back to my dorm room because it would be safer in there than it is in here."
    s "You are aware how that sounds, right?"
    s "Inviting someone back to your room after nearly making out with them can kind of only be interpreted one way."

    if bonus == False:
        s "It means you want to hug."

    u "{i}Sensei.{/i} I don’t care how much you want to make out with me or how you interpret my invitation. "
    u "It is now my duty as both your friend and your student to make up for invading your personal space and almost making you commit adultery. "

    if bonus == True:
        s "Are you sure you don’t want to just stay here and make out?"
    else:
        s "Are you sure you don't want to just stay here and do the hug thing without having to walk a bunch of miles?"

    scene utakaraoke27
    with dissolve

    u "Can you do me a favor and not bring that up anymore?"
    u "It really was just a spur of the moment thing. People do stuff like that all the time."
    u "It’s not like anything actually {i}happened{/i}. We just accidentally got our faces a little closer to each other than they’d ever been before."
    s "But what does that have to do with {i}everybody?{/i}"
    s "Because one of my least favorite qualities in people is selflessness. Think about yourself and what you want before worrying about how anyone else feels."
    u "No."
    s "No?"
    u "No. I don’t wanna."
    u "I’m happy the way I am."
    u "And that way involves lookin’ out for others."

    if bonus == True:
        u "So, sorry...but you’ll just have to keep wackin’ it to what the Uta in your imagination does and not worry about what the real Uta does."
        u "Cause the real Uta’s not gonna be ready for the stuff you wanna do with her for a long time. "
        u "Maybe not even ever."
        s "We’ll see about that."
    else:
        s "We should race go-karts sometime."

    scene utakaraoke29
    with dissolve

    u "Is that a challenge? "
    u "Are you still so excited about the dorm war that you need to start a {i}new{/i} contest just to keep the adrenaline up?"
    s "If that’s what you want to call it, sure."
    s "But I’m not going to let you forget that this happened and I am going to use it as a weapon against you whenever possible."
    u "Then I’ll just have to learn to deflect you even harder."
    u "Game on, Sensei. No one beats Uta."
    s "We’ll see about that..."

    scene black
    with dissolve2

    "Strangely enough, Uta doesn’t retract her dorm invite and, after checking out of the karaoke place, we begin to head over there."

    if bonus == True:
        "We’re both fully expecting Io to be around, though, so I’ve mostly given up on the prospect of pushing things any further with Uta for the time being."
        "It is really peculiar, though."
        "Maybe all of those deflections really aren’t deflections at all?"
        "Maybe Uta {i}does{/i} want something more with me but just...isn’t pursuing it for some reason."
        "It’s not because of Maya, is it? Or Io?"
        "..."
        "What did she mean by she’s not as great as I think she is?"
        "And why does that remind me of something Io said recently?..."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid20 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump utadorm20

label utaarchery1:
    scene utadownbad1
    with dissolve2

    u "Sensei? When did you get here?"
    s "Somewhere around when you started holding hands with Wakana. I left though since I figured you two probably wanted to be alone."

    scene utadownbad2
    with dissolve

    u "Ah...Yeah, I don’t really know how Osako-chan would feel about me stealin’ her girlfriend out from underneath her. "
    s "I’m honestly surprised she even kept that job. I figured it was just a temporary thing while the dojo was stuck in limbo."

    scene utadownbad3
    with dissolve

    u "Gotta make that money somehow, Sensei. Osako-chan’s gotten a taste of that sweet nectar and ain’t ever looking back. "
    s "Don’t talk about Osako tasting nectar anywhere near Wakana. She’s already worried I’m going to steal her woman."
    w "I can hear you, Arakawa."
    s "See? She’s terrified."

    scene utadownbad4
    with dissolve

    i "Are you done being an archer now? Can we go back to being friends?"
    u "Do we always stop being friends whenever I do something for myself?"
    i "Uta, I have extreme social anxiety. We stop being friends whenever I can’t see you."
    u "Io, the fact that you function at all is something I think we should be proud of. "
    i "I’m not sure if I’d call what I do “functioning,” but I am in an extremely good mood right now, so...what the heck. Sure. Let’s all be proud of me for a minute."
    i "Just a minute, though. Any longer than that and I will actually die."

    scene utadownbad5
    with dissolve

    u "You?...In a good mood?..."
    u "You and Sensei weren’t playing tonsil hockey behind the storage building, were you?"
    i "Even better. He was opening up to me."
    s "I said literally one thing."

    scene utadownbad6
    with dissolve

    u "Hah...it’s like the leaderboard of this harem changes every time I close my eyes. "
    u "Gonna have to break out my notebook when we get back home and see which spot you’re in now, Io."
    s "You don’t actually have a harem leaderboard, do you?"

    scene utadownbad7
    with dissolve

    u "Well, what else am I gonna do in class? You don’t make me study anymore. "
    u "I’m like four pages of harem notes away from starting a whole betting ring, Sensei. Do you have any idea how much money there is to be made off of this?"
    s "Am I just a toy to you?"

    scene utadownbad8
    with dissolve

    u "No. But you {i}are{/i} a toy to Uta-chan. And I can swap personas any time I like, Master."
    s "Marry me."

    scene utadownbad9
    with dissolve

    u "What do you think you’re doing, Sensei? Proposing to someone in the bottom ten when you’ve got a higher ranked girl right next to you?"
    i "In his defense, I am definitely not marriage material. In fact, I think even the concept of marriage is archaic and stupid. Why should we have to sign a sheet of paper to prove that we-"

    scene utadownbad10
    with dissolve

    u "Shush."
    i "Okay."
    s "Can I ask who number one in your...weird ranking thing is?"

    scene utadownbad11
    with dissolve

    u "I mean...you {i}can.{/i} I’m just not sure if you want to know the answer."
    s "Why wouldn’t I want to know the answer?"
    u "Cause it’s Ami."
    s "..."
    i "{i}Hah...{/i}"
    u "See? Even Io’s disappointed in you and she’s your number one fan."
    s "First off, no one should be disappointed in me when this ranking clearly has nothing to do with-"
    u "Ah-ah-ah. Before you go saying “this ranking has nothing to do with how I treat girls and is based on how much they love me,” it {i}absolutely{/i} has {i}everything{/i} to do with how you treat us."
    u "Ami gets more special treatment than anybody. "
    u "Combine that with the fact that she’s also one of the most vocal about her love for you {i}and{/i} how you guys go way, way back and you’ve got a combined Uta-chan certified compatibility score of...9.7/10."
    s "That is way too high of a score for my compatibility with my {i}niece.{/i}"

    scene utadownbad12
    with dissolve

    u "Love comes in all kinds of forms, Sensei."
    s "Is that why you had a crush on a sponge?"

    scene utadownbad13
    with hpunch

    u "Don’t bring the sponge into this! That was basically a zillion years ago! My tastes have changed since then! I like humans now!"
    i "Uhh..."
    u "Great! Now Io knows about the sponge! Look what you did!"
    s "I thought Io already knew about the sponge."
    i "I feel like I know less and less every time you say “sponge.”"

    scene utadownbad14
    with dissolve

    ki "Io! Wakana says you have to come help me clean up the storage room since you sat around all day being worthless."
    i "What? Since when is that a thing I get punished for?"
    w "Kanda-san, if you call me “Wakana” one more time, I will see to it that you’re removed from this club and sent off to practice kyudo in the sinkhole."
    s "I think this is your chance, Io."

    scene utadownbad15
    with dissolve

    i "But I want to keep hanging out with you and Uta. My day finally became bearable."
    u "We’ll be here when you get back, Io. I ain’t doing anything today. Sensei and I will just hang out and..."
    u "And I guess that’s it. We’ll just hang out."
    ki "Greenie! Hurry the fuck up! I have shit to do after this!"

    scene utadownbad16
    with dissolve

    i "Stop calling me that, you incorrigible bimbo! I have a name!"
    ki "Yeah but you throw a hissy fit whenever I use that as well. Just get over here and help me clean already. "
    i "Fine. But if you expect me to talk to you while we’re in there, I’m walking right back out."

    scene utadownbad17
    with dissolve

    i "I’ll be back, I guess..."
    u "Uhh...yeah. Have fun. "

    "Io wanders off to join Kirin in the shed and, despite my suggestion that she try and befriend her just a short while ago, I have a creeping feeling that that won’t be happening today."
    "On the bright side, though...she {i}did{/i} agree to contributing in some way, which is more than I’d typically expect from her. "
    "Who knows? Maybe she really {i}is{/i} so desperate to please me that she’s going to actually start taking a few steps forward?"

    u "..."

    "Or maybe she’s just trying to somehow increase her place in the unofficial harem ranking."

    scene utadownbad18
    with dissolve

    u "So, now that you’re alone with Uta-chan (Archer form), what do you wanna do? You ever use a bow before?"
    s "Do I look like the type of guy who has used a bow before?"
    u "No. But you look like the type of guy who’s {i}about{/i} to."
    s "What?"

    scene black
    with dissolve

    u "Come on! Take this! I’ll show you how it’s done!"
    u "I’m not as good of a teacher as Miss Watabe, but if you’re gonna learn this from anybody else, I’m probably the one you wanna come to!"

    "Uta hands me the bow (Which I have no idea how to hold properly) before grabbing my waist and redirecting me toward the targets at the far end of the range."
    "That part I probably could have figured out on my own, but I’m not about to deny any amount of physical contact from Uta-chan."

    scene utadownbad19
    with dissolve2

    "{i}This{/i} level of physical contact is not what I expected, though."
    "Instead of coaching me from the sidelines or nearby like I expected her to, Uta takes her place directly behind me and rests her hands on my arm and my wrist respectively."
    "Her chestguard presses up against my back and robs me of a sensation I have longed for, but my imagination does its job and fills in the blanks for me so I don’t miss out entirely."
    "Then, from what feels like miles below, a bright and joyous voice with a mild rasp to it cuts through the air, crawls up my back, and nests in my ears."

    u "Don’t pay any attention to me, okay? Just straighten out your limbs and try to stand up straight."
    u "Also, please don’t let go of the string. I don’t want it to snap back and break all of my fingers off."
    s "You’re sure asking a lot out of a first-timer, huh?"
    u "Yeah, but only cause I think you’d be pretty good at this with some practice."

    scene utadownbad20
    with dissolve

    u "Your body’s kinda huge, Sensei. And your figure is great too. "
    u "If a girl my size is able to handle a bow as well as I can, just imagine how the snap will sound when {i}you{/i} launch your arrow."
    s "I’d say we should find out, but I think you said something about wanting to keep your fingers."
    u "That is correct. Updating my harem ranking will be hard if I can’t write anymore."
    u "Also, don’t get cocky thinking your shot will echo across the range on the first try. There’s a lot more to kyudo than raw power. That’s only a tiny part of it."
    u "I’m just saying it {i}could{/i} sound beautiful one day. And that you {i}might{/i} be great at this if you keep practicing."
    s "I’m open to practicing as much as you want so long as we can always do it like this."

    scene utadownbad21
    with dissolve2

    u "Uh..."
    s "What’s wrong?"
    u "..."
    s "..."
    u "..."
    s "..."

    scene utadownbad22
    with dissolve

    s "Uta? "
    u "We can practice whenever you want."
    s "I get that. But you’re-"
    u "I’m just making sure your posture stays good. You can keep ignoring me."

    scene utadownbad23
    with dissolve

    s "I think that might be a little easier said than done."
    u "I’d say I’m happy to hear that, but that would basically be the same thing as admitting that-"
    i "What are you guys doing?"

    scene utadownbad24
    with hpunch

    u "UHH! NOTHING! ARCHERY! POSTURE! "
    u "JUST...HELPING SENSEI WITH HIS FORM!"
    i "Cool, but...why are you yelling?"
    u "Because I’m...in the zone?"
    i "Huh. Well, I’m done for now if you guys want to-"
    u "Actually! Uhh...I have to talk to Sensei about something he just told me!"

    scene utadownbad25
    with dissolve

    s "You do?"
    u "SHH! She saw me hugging you! Act sad."
    s "But I-"
    u "Sensei! Please!"

    scene utadownbad26
    with dissolve

    s "I’m sad and I need Uta’s help for some reason."
    u "S-See?! The poor guy’s basically in tatters! But give me a few minutes with him and I’ll whip him right back into shape for you, Io!"
    i "For me? Why would that be for me? If Sensei’s actually feeling down, shouldn’t you be doing that for {i}him?{/i}"
    u "That’s...yes! That’s what I meant! But you are also here, so...when I return, you will also reap the benefits of...his happiness!"
    i "..."
    u "..."

    scene utadownbad27
    with dissolve

    i "You’re acting really weird right now. "
    u "I just..."
    u "I feel really...bad for him...because of the sad thing he told me..."
    s "It really is sad."
    u "{i}Just start walking away. She’ll wait.{/i}"
    s "I’m going to start walking away now."

    scene utadownbad28
    with dissolve

    u "We’ll be back in a few minutes, Io! Don’t...go anywhere!"
    s "I sure hope I don’t stay sad any longer."
    u "{i}Give it a break, Sensei! Your acting sucks!{/i}"
    i "..."
    i "..."
    i "..."
    i "What the heck just happened?"

    scene black
    with dissolve2

    "........."
    "......"
    play sound "slidedoor.mp3"
    "..."

    scene utadownbad29
    with dissolve2

    u "(Screaming internally)"
    s "I feel like you could have handled that a little better."
    u "Yeah, you’re one to talk with all of that “I’m so sad! Woe is me!” crap! Those acting chops wouldn’t last you one minute in a maid cafe!"

    scene utadownbad30
    with dissolve

    s "Hey, you sucked too. I’m starting to think you get your powers from the uniform."
    u "It definitely helps!"
    s "So, are you going to tell me why you pulled me into this-"

    scene utadownbad31
    with dissolve

    s "Wait...where even are we?"
    u "The tea ceremony room. "
    s "We have a tea ceremony room?"
    u "We have a whole tea ceremony club. They just happen to use one of the buildings near the archery range since this is where they keep all the...old school stuff, I guess."
    s "Okay, but then...why exactly did you pull me into the tea ceremony room?"

    scene utadownbad29
    with dissolve

    u "I have no idea! It just happened! "
    u "At first, it was probably because I didn’t want Io to think anything suspicious was going on, but now I realize that this just makes everything look even {i}more{/i} suspicious!"
    s "Then...should we go back out there?"
    u "No! Because coming in here for just one minute would make everything even {i}more{/i} suspicious!"

    scene utadownbad32
    with dissolve

    s "You really dug yourself into a hole this time, didn’t you?"
    u "Ahhhh! What am I doing, Sensei?!"
    s "You’re being suspicious as hell, that’s what."

    scene utadownbad33
    with dissolve

    s "Or...wait. I think the word is “sus” now. I’ve been hearing the other girls say that lately."
    u "Okay. I need to sit down."

    scene black
    with dissolve2

    "Uta takes her shoes off and sits down on the tatami mat, pulling her knees up to her chest and gently rocking back and forth as I lower myself to meet her."
    "It’s clear that, for some reason, this spur of the moment decision has already turned into spur of the moment regret, but that doesn’t mean we can’t figure out some way to enjoy it."
    "Especially since her best friend is probably still standing exactly where we left her and attempting to wrap her head around everything currently going on."
    "But hey, that’s fine. Because I’m doing the exact same thing."

    scene utadownbad34
    with dissolve2

    "Or, at least that’s what I {i}was{/i} doing before finally getting to look at Uta’s face- which is currently redder than I have ever seen it before."

    s "..."
    u "..."
    s "You just wanted to be alone with me for a little while longer, didn’t you?"
    u "Wh...What makes you think that?"
    s "The face. The rocking back and forth. The nervous poke war your index fingers are having with one another right now."
    u "I’m just...really nervous around tea. "
    s "You know, you’ve said a lot of questionable things over the brief time I’ve known you, but that one really makes me question just what type of person you are, Uta."

    scene utadownbad35
    with dissolve

    u "I’m...not good at thinking things through, okay?! My whole life is a series of weird, impulsive decisions! This is just the first time you’ve gotten wrapped up in one."
    s "There was also the one time in-"
    u "The karaoke collision was an accident! Not an impulse!"
    s "Was almost kissing me {i}after{/i} the collision an accident too?"
    u "Nope! Because that part never happened and it’s all one big fantasy you dreamt up!"
    s "Ahh, okay. Just making sure."
    s "For the record, though- I don’t really think being impulsive always has to be a bad thing. I {i}like{/i} being alone with you. Just...probably not when Io is also expecting to be here."

    scene utadownbad36
    with dissolve

    u "AAAAAAAAAHHHHHHHHHHHHH! "
    s "Uta, chill. It’s really not a big deal. "
    s "Io knows all about you, right? Because, if that’s the case, explaining to her that you just impulsively dragged me in here should fix pretty much every misunderstanding you’re worried about."
    u "It’s {i}because{/i} she knows me so well that I’m worried, Sensei! I’m only like this under very specific circumstances!"
    s "And those circumstances are?"

    scene utadownbad37
    with dissolve

    u "Circumstances I must be very careful with."
    s "And why is-"
    u "Because I don’t want them to get me in trouble. "
    u "And because I’m..."

    scene utadownbad38
    with dissolve

    u "I’m afraid it might happen again..."
    s "Afraid that...{i}what{/i} might happen again?"

    scene utadownbad39
    with dissolve

    u "You mind just giving me a minute to catch my breath and...not make any more impulsive decisions? Cause I’ve only made one so far and even that’s got the potential to flip my life on its head."
    s "I still think you might be overthinking this. I’m pretty sure Io will understand."
    u "I might be using the word wrong, but I’m pretty sure that would be ironic."
    s "How come?"
    u "Because my history of {i}not{/i} thinking about things is the only reason I ever met Io in the first place."

    scene black
    with dissolve2

    "When we leave the tea ceremony room, we find Io crouched over the body of a dead caterpillar- slowly allowing dirt to sift through her fingers and cover it up."
    "She hosts a makeshift funeral for the bug with Uta and I as guests...and doesn’t once question where we disappeared to."
    "She’s too happy to have us back."

    $ renpy.end_replay()
    $ utaarchery1 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label utamaid25p1:
    scene utabeforerain1
    with dissolve2
    play music "love.mp3"

    u "Guhhhhhhhhh..."
    u "Why does being cute have to be so exhausting, Master? All of this adorableness is giving me a headache."
    s "As much as I appreciate still being called “Master” after the cafe has closed, I feel like I should remind you that you’re not really {i}obligated{/i} to say that anymore."
    u "Right, sorry. It’s hard to get out of character while I’m still wearing the outfit- even if I’ve already started taking it apart."
    s "Feel free to continue taking it apart if that helps you relax. No sense in removing the sleeves if you’re going to keep the top on, right?"

    scene utabeforerain2
    with dissolve

    u "Even {i}if{/i} I took the rest off, it’s not like I’ve got the energy to get freaky right now. Being with Uta-chan in this state would be no better than being with some kinda puppet or...a sock."
    s "I don’t think I’ve ever been this attracted to a sock before."

    scene utabeforerain3
    with dissolve

    u "Yeah, yeah. Save it for the Uta-chan who’s in the mood to flirt back. Right now, I just wanna fall into bed and die."

    "I wound up overstaying my welcome at the maid cafe long enough to watch Uta slowly shed her professional persona and begin transitioning into a state I rarely see from her."
    "But given just how much money I spent here tonight, I feel like I should at least be {i}offered{/i} some sort of additional service at this point."
    "Unfortunately, I have accepted by now that those sorts of services are not offered here. Nor do I believe Uta would be cheap by any stretch of the imagination if they were."
    "And I am not about to sell my house for a single blowjob from my niece’s coworker."

    scene utabeforerain4
    with dissolve

    u "Master...if you carry me back to the dorm...I’ll let you do whatever you want with me..."

    "Nevermind."

    s "Deal."

    scene utabeforerain5
    with dissolve

    u "So easy. And literally right after I told you I wasn’t in the mood to flirt anymore. You’ve got a serious problem. "
    s "Stop reminding me. I was just contemplating the idea of selling my house to see what else I could get tonight."

    scene utabeforerain6
    with dissolve

    u "Oh?"
    s "Yeah. I’d tell you more, but you’ve already reiterated the fact that your fun, suggestive banter is a no-go for the rest of the night. "
    u "Well, that was before there was a whole house involved. I might go an extra mile or two for a permanent place to live. "
    s "I’d expect you to go at least ten miles for something of that size."

    scene utabeforerain7
    with dissolve

    u "Size doesn’t matter, Master. Stop trying to overcompensate. I’d still love you no matter what size your {i}house{/i} is."
    s "Oh, if you only knew..."

    scene utabeforerain8
    with dissolve

    u "So...what are you still doing here anyway? Was me telling you that we’re about to close a kadrillion times not enough to give you the hint?"
    s "It was. I just couldn’t stand the thought of being away from you for even a second."
    u "No wonder I’m feeling so exhausted. Being excessively loved really takes it out of a girl, you know?"
    s "I will love you so hard that you’ll go into a coma for the next ten years."

    scene utabeforerain9
    with dissolve

    u "It’s crazy how busy it was tonight, huh?"
    s "Don’t just ignore my amazing pick-up lines."
    u "Master, you should know by now that no pick-up line will ever work on Uta-chan. Especially not any lines about putting her into a coma."
    s "Not even if that coma is a direct result of being aggressively and viciously loved?"
    u "You can’t be aggressive and vicious with girls like me until at least the fourth time, Master. I’ve gotta get warmed up first. "
    s "How much more money do I have to spend until I can start warming you up?"

    scene utabeforerain10
    with dissolve

    u "How much ya got?"

    "I drop my wallet onto the table, showing Uta that she has, once again, sucked me dry in the least interesting way possible."

    u "Rough. And here I was about to go the extra...what was it- {i}ten{/i} miles, for just a little bit more."
    s "I’d ask you to start logging all of my purchases but I worry about what Ami would do if she ever found out the number."

    scene utabeforerain9
    with dissolve

    u "Doin’ something like that would just be extra work anyway. And as you can see, maid cafe stuff can be crazy exhausting when business picks up."
    u "I think summer’s gonna be good for us at this rate. And I’m not just saying that because you are singlehandedly financing my college education fund."
    s "I didn’t even realize you were planning on going to college."
    u "I might. I haven’t really decided yet. "
    u "That is if I can actually get into one, though. As you may have noticed from my transcript, the whole “learning” thing doesn’t really work well for me."
    s "Are you implying that I actually would have gone through the effort to look at your transcript?"
    u "Right, right. We can’t all be hard workers. Can we, Master?"
    s "We certainly can not. But when you think about it, you {i}are{/i} getting a decent chunk of my income. So it’s not like your hard work isn’t exactly rewarded."

    scene utabeforerain7
    with dissolve

    u "The duties of the world’s greatest maid never cease."
    s "I don’t know. You seem pretty checked out to me."
    u "And yet I’ve still called you “Master” throughout this entire conversation. Uta-chan truly is amazing, isn’t she?"
    s "She’d be more amazing if she didn’t treat me the same way she treats all of the other customers when I am clearly the highest bidder for her love."

    scene utabeforerain6
    with dissolve

    u "You say that as if I wasn’t planning to reward you tonight~"
    s "You’re {i}not{/i} planning to reward me tonight. That’s just your second wind kicking in as you remind yourself that your sole purpose on this planet is to lead me on."
    u "That’s my {i}second{/i} purpose. My {i}first{/i} purpose is making you smile."
    u "Which is precisely why..."
    s "..."
    u "Tonight...and tonight only..."
    s "..."
    u "I’m going to close up this store...and take you into the back..."
    s "..."
    u "Make sure we’re all alone...where no one will ever find us..."
    s "..."

    scene utabeforerain11
    with dissolve

    u "And give you an all-inclusive, behind the scenes tour of the secret world of maids!"
    s "Wow, exactly what I wanted."

    scene utabeforerain6
    with dissolve

    u "It might not be the inside of my dress, but at least it’s something my parents would approve of! And I know just how much that means to you, Master."
    s "Yeah. I guess if you’re ever going to actually give me your hand in marriage, winning them over is going to be kind of necessary."

    scene utabeforerain12
    with dissolve

    u "Hah...hahah...yeah. "
    u "Yeah that would, uhh..."

    scene utabeforerain13
    with dissolve

    u "Uhh...anyway! I guess now’s as good a time as any to start this tour thingy, right? Still got a whole store to clean up and...and then I’ve gotta get back to the dorm, so..."
    u "I guess...follow me? "

    scene utabeforerain10
    with dissolve

    u "Oh, and don’t think that being alone in a private room gives you permission to get handsy, Master. "
    u "I have absorbed some of Osako-chan’s strength through sheer willpower, so you’d be in serious trouble if you actually tried anything."

    scene black
    with dissolve2

    "Uta’s second wind turns into a tornado, ripping her from her place at the table and sending her crashing through a door in the side of the room."
    "I get caught up in it as well and follow her through an opening I imagine no man has ever moved through- into a place filled with wonder and mystery..."

    scene utabeforerain14
    with dissolve2

    "And that place is just a kitchen."

    u "Our first out of a whopping {i}two{/i} stops on this official, Uta-chan sanctioned tour of the maid cafe is the kitchen! Or, as I like to refer to it, the place where wishes come true! "
    s "I don’t think any of my maid-related wishes involve a kitchen."
    u "Yeah, because you’re a pervert. But there are plenty of people who are happy just receiving attention and food from us!"
    u "It isn’t weird to want to be cared for! And it isn’t weird to want to care {i}for{/i} people either!"

    scene utabeforerain15
    with dissolve

    u "Just look at me! I love what I do. I love making people happy. I just also love all of the money I can make {i}while{/i} doing that."
    u "So, if you ever decide to be a little less of a pervert and can come up with some kinda kitchen-related wish that doesn’t involve bending me over the rice cooker, just let me know!"
    s "What about the counter?"
    u "No wishes at all involving the defilement of Uta-chan’s purity."
    s "For someone so pure, you come across as annoyingly evil in the face of my perversions, you know."

    scene utabeforerain16
    with dissolve

    u "Oh? Well, luckily for you, our next stop is the perfect place to indulge in those perversions, Master. Or at least it would be if I weren’t accompanying you. "
    u "But, if you’d like some time alone to truly {i}indulge{/i} in what many others have only dreamt of, I suppose I might be able to step out for a little while."
    s "This sounds much better than a kitchen."
    u "Yes. It’s much more suited to the tastes of a creepazoid like you."

    scene black
    with dissolve2

    "Once again, a gust comes and sweeps us away. "
    "The sweet scent of pastries vanishes along with the bright fluorescent light of the kitchen and is replaced by one much more stale and much more dim."

    scene utabeforerain17
    with dissolve2

    "A room full of lockers. Lockers which likely contain the clothes and personal belongings of the cafe’s entire (Albeit very limited) staff."
    "The important thing, however, is that this staff contains Uta. Which means that Uta routinely undresses in this very room."
    "Which means that I must now prevent myself from getting an erection and inadvertently disproving her earlier statement about overcompensation."
    "In other words, this is much better than the kitchen."

    u "Welcome to the locker room. Or, as I like to refer to it, the {i}other{/i} place where wishes come true."
    s "This is definitely much closer to what I would wish for. "

    scene utabeforerain18
    with dissolve

    u "Well, you sure as heck aren’t the only one. Because I’m pretty sure Osako-chan and Miss Watabe get it on in here at least once a week."
    s "You wouldn’t happen to be hiding any cameras in here by any chance, would you?"

    scene utabeforerain19
    with dissolve

    u "Nope! So if you were to go really crazy and take Uta-chan for yourself right now, nobody would ever know."
    s "That is...not something you should be saying to me."
    u "Why not? You were already thinking it, weren’t you?"
    s "That has nothing to do with whether or not that’s something that should be said out loud, though."

    scene utabeforerain20
    with dissolve

    u "Master, please. You’re making it sound as if I’m not already aware of how badly you want to watch me undress right now."
    s "This {i}would{/i} be the place to do that, after all."
    u "It {i}would{/i} be...under normal circumstances."
    s "And I’m assuming normal circumstances are when I’m not here?"
    u "Correct!"

    scene utabeforerain21
    with dissolve

    u "But also, I spilled soy sauce all over my street clothes earlier and I don’t want to change back into them now because it would be embarrassing."
    s "More embarrassing than being dressed as a mildly risque maid?"

    scene utabeforerain22
    with dissolve

    u "Is taking the sleeves off really all it takes to make this getup mildy risque? They’re just sleeves."
    s "You’d be very surprised at what even the mildest of wardrobe changes are able to accomplish."
    u "Boy brains are silly. You could take off your whole shirt right now and I probably wouldn’t even feel a thing."
    s "Want me to try?"

    scene utabeforerain23
    with dissolve

    u "I mean...this {i}would{/i} be the place to do it."

    scene utabeforerain24
    with dissolve

    u "But nope! "
    u "Wanna know what you {i}can{/i} do, though? "
    s "Help you take the rest of your costume off? Deal. Great end to the tour, Uta. So glad I didn’t have to {i}actually{/i} pay for this."
    u "Not quite! What I’d have you do is actually even better than that! "
    s "That isn’t going to be true, but tell me what it is anyway."

    scene utabeforerain25
    with dissolve

    u "Can you maybe walk me home?"
    u "Even if there aren’t many men around here, a journey through the dark in a maid outfit is {i}probably{/i} gonna attract some negative attention."
    s "Just wear the clothes you spilled stuff on. It’s not a big deal."

    scene utabeforerain26
    with dissolve

    u "But then people are going to think I’m a slob!"
    s "I don’t mean to offend you, but I have seen your room and that statement might not be as untrue as you think it is."
    u "You knowing is different than random people knowing! "
    s "Why?"
    u "Because...I said so! That’s why! "
    s "..."
    u "Are you gonna walk me home or not?!"
    s "Depends. Are you going to stay in character the whole time?"
    u "Do I...have to? Or can I maybe just be normal Uta who just happens to be cosplaying as Uta-chan?"
    s "You can be whichever one you are right now. The blushing is cute and I would like to see more of it."

    scene utabeforerain27
    with dissolve

    u "B-Blushing? But I’m not- wait, what the heck? Why is my face so hot?"
    s "Beats me. Maybe you’re just flustered because you’re holding yourself back from tackling me again?"

    scene utabeforerain28
    with dissolve

    u "For the last time, we fell! I didn’t tackle you!"

    scene black
    with dissolve2

    s "Right, right. The falling part is still a little hazy to me. All I really remember is how we almost kissed."
    u "We...did not! That never happened!"
    s "Are you going to stay in the locker room all night? Or am I going to walk you home now?"
    u "You can obviously walk me back to- wait. I still haven’t mopped. Or...really done anything to close the store yet."
    s "Just let whoever the opener is take care of it. I’m sure they won’t mind."
    u "Guh. You don’t know the first thing about this line of work, do you?"

    "........."
    "......"
    "..."

    scene utabeforerain29
    with dissolve2

    u "Thanks for walking me home again, Sensei. I’d feel a little bad about getting you to do this all the time if you weren’t so obsessed with me."
    s "Are you sure you’re not the one who’s obsessed with {i}me?{/i}"
    u "If I’m so obsessed with you, how come I’m in the bottom ten of Uta-chan’s official harem ranking?"

    scene utabeforerain30
    with dissolve

    s "Probably because you won’t let yourself get any higher when you know you could."
    s "Or because you’re not {i}actually{/i} interested in me and are just overcome by curiosity and hormones."
    u "Wha..."
    u "What’s with that really {i}real{/i} answer all of a sudden? "
    u "Are we still joking around or, like...are we actually talking now? Cause I wasn’t ready for that mood swap. "
    s "Either one is fine. "
    s "It’s just a little exhausting having to deal with people who are always hiding things."
    u "You..."

    scene utabeforerain31
    with dissolve

    u "Hah..."
    u "This is exactly why Io likes you so much, Sensei. "
    s "Io likes me because I just happened to be there when she {i}wanted{/i} to like someone. That could end just as quickly as it started."
    u "That’s a good point, I guess. I don’t think it will, though. She’s pretty attached now."
    s "Are you attached as well?"
    u "To Io?"
    s "To me."

    scene utabeforerain32
    with dissolve

    u "..."
    s "..."
    u "Do..."
    u "Do you have any interest in visiting Nara one day, Sensei?"
    s "Is that you just dodging my question?"
    u "Does answering like that mean you’re dodging {i}mine?{/i}"
    s "Even if I was interested, it’s not like we can go anywhere. The city’s still closed off."
    u "But it won’t be that way forever, right? Especially now that we’re gettin’ like, actual news about the space war that I forgot was even a thing."
    s "Just hearing about who died and who didn’t isn’t exactly {i}news.{/i}"
    u "Then...in a perfect world, without any space war and without any barrier, would you ever want to see where I come from?"
    s "Would I be going with you? Or by myself?"
    u "Whatever...you’d prefer..."
    s "Then sure."
    s "It just sucks that probably won’t ever happen."
    u "Yeah..."
    u "Yeah, that does suck."
    u "I’d like to take you there one day. And not just on an official Uta-sanctioned tour. "
    u "Like...{i}actually{/i} take you."
    u "To show you what I grew up with."
    u "Because the more time I spend with you, the more I want you to, like...actually know stuff about me. "
    u "It just sucks because the only things I can think of telling you would make you like me less."
    s "..."
    u "..."

    "A silence spreads itself between us."

    scene utabeforerain33
    play sound "thunder.wav"
    stop music

    "It is promptly killed by something that disagrees with its existence."

    scene utabeforerain34
    with dissolve4
    play music "rainloop.wav" fadein 3.0

    u "Jeez! That scared the heck out of me."
    s "..."

    scene utabeforerain35
    with dissolve2

    u "And now it’s raining too?..."
    u "Since when does it ever rain around here?"
    s "..."

    scene utabeforerain36
    with dissolve2

    u "Well, we’re not just gonna stand around and wait for it to stop, are we?! I’m already low on wearable clothes and I’ve gotta work tomorrow!"
    s "I told you to wear the other outfit, but you were insistent on not looking like a slob for all of the...zero people we have passed on the way back."
    u "Scold me later! Keep me dry for now! You’re big! You can be my umbrella!"
    s "Let’s just find somewhere to go instead. That way we {i}both{/i} won't have to-"
    u "Whatever! Anything is fine! Just choose a building and get inside! Hurry! "

    scene black
    with dissolve2
    stop music fadeout 5.0

    "Uta pushes me toward the closest awning to try and shield us from the rain, but it’s to no avail as the wind rages on and ensures that we remain in peril."
    "It isn’t until we finally find a building that isn’t locked a good ten minutes later that we are finally safe..."

    $ renpy.end_replay()
    $ utamaid25p1 = True
    $ uta_love += 1

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump utamaid25p2

label utamaid25p2:
    scene utalovehotel1
    with dissolve2
    play music "citylife.mp3"

    "Or at least safe-{i}ish.{/i}"

    u "Man, just how many fluids am I going to get all over my clothes before the end of the day?"
    s "Don’t you think saying something like that might be a little too...{i}suggestive{/i} considering where we are right now?"

    scene utalovehotel2
    with dissolve

    u "Obviously. But, more important than that-"

    scene utalovehotel3
    with fade

    u "What the heck is up with this cliche?!"
    u "Taking shelter from the rain in a love hotel?! Since when is this an anime?!"
    u "And just how crazy do they expect us to get?! There are like five hundred condoms on that bed! "
    s "That’s five hundred more than I’d ever intend to use, so..."

    scene utalovehotel4
    with dissolve

    u "Sensei..."
    s "What? Am I not allowed to dislike condoms?"
    u "Did you plan this? Were all of those buildings you tried going into before this one {i}actually{/i} locked? Or were you just holding out hope that we’d come across somewhere like this eventually?"
    s "You got me. I also summoned the rain with my magical, pervert powers. "
    u "I {i}knew{/i} it."
    s "Anyway, I guess we have to have sex now."

    scene utalovehotel5
    with dissolve

    u "No way, no way, no way! A love hotel for my first time?! That sounds like something Kirin would do!"
    s "No comment."
    u "I’m just not ready! Especially not with the guy my best friend likes!"
    s "But you’re already so wet."

    scene utalovehotel6
    with dissolve

    u "How do you know that?!"
    s "..."
    s "I was talking about the rain."
    u "Oh!"

    scene utalovehotel7
    with dissolve

    u "Uhh..."
    u "Me too! "
    s "..."
    u "..."
    u "Sensei, all I can hear are other people getting it on. We’re going to have to keep talking or I’m at risk of being tainted forever."
    s "If you’re going to act so weird about taking shelter in a love hotel, how come you’re the one who paid for it?"

    scene utalovehotel8
    with dissolve

    u "Because you spent all of your money on me and couldn’t afford it! Also, I didn’t think they’d let me {i}actually{/i} pay! There’s no way I look old enough to check into a place like this!"
    s "If you keep yelling, you’re going to ruin the mood for all of the people who actually came here to, you know, have sex."

    scene utalovehotel9
    with dissolve

    u "That is seriously so many condoms."
    s "They’re probably trying to offload a massive stockpile that’s been around since before all the men were drafted."
    u "They want us to have sex with three year old condoms? There’s no way that’s up to code."
    s "If you go complain, we might be able to get some of my money back."

    scene utalovehotel10
    with dissolve

    u "{i}My{/i} money."
    s "We all know whose money it really is."

    scene utalovehotel11
    with dissolve

    u "Hah...No, it’s fine. "
    u "I’m soaking wet and cold and don’t wanna bother going back out into the lobby since they might try to card me."
    u "I have no idea how I’d even {i}start{/i} explaining that to my parents."
    s "I bet you’re feeling like a real idiot for leaving your other clothes behind now, aren’t you?"

    scene utalovehotel12
    with dissolve

    u "You know, Sensei, I’m pretty sure there are rules against inviting a girl to a love hotel if you’re just going to poke fun at her the entire time."
    s "Sure. Except I didn’t actually {i}invite{/i} you. So technically I can do whatever I want so long as I’m not breaking any laws."

    scene utalovehotel13
    with dissolve

    u "Yeah, I think it may be a little too late for that."
    u "You wouldn’t happen to have any spare clothes in those oversized man-pockets of yours, would you?"
    s "I would not. But if we’re both cold, I heard something about-"
    u "If you seriously suggest getting naked and sharing body heat right now I’m going to death beam you. "
    s "There’s...a {i}death{/i} beam now?"
    u "I have tons of beams for tons of occasions. I’ve just only showed you the flavor one so far."
    s "There’s no “heat beam” or “drying beam” is there?"
    u "I haven’t yet mastered those, unfortunately."
    s "What are we supposed to do then? Just stand here, not having sex, and freezing our asses off?"

    scene utalovehotel14
    with dissolve

    u "I mean...there {i}is{/i} a bathtub. And it looks like there’s a shower too. The only issue is that the glass is see through and...yeah."
    s "Do you...want to shower together?"

    scene utalovehotel15
    with dissolve

    u "What?! Absolutely not! I was just saying that if {i}you{/i} want to take a bath or something, I can just close my eyes or...watch videos on my phone until you’re done."
    u "At least that way you wouldn’t be cold anymore."
    s "I feel like this is the part where I’m supposed to be a gentleman and insist that you go first but, honestly, that sounds good and I’m probably going to take you up on it."

    scene utalovehotel13
    with dissolve

    u "Don’t you think you might be a little {i}too{/i} carefree sometimes, Sensei? "
    s "That means nothing from a girl who spent her hard earned money getting the two of us a room in a love hotel."
    u "Make up your gosh darn mind about whose money it is already. "
    s "Fine. It’s mine. Now, give the rest of it back or I’m going to go see if the couple next door wants to come and join us for a foursome."
    u "That’s a whole lot of people and not a lot of Uta."
    s "Don’t worry. I wouldn’t be open to sharing you anyway."
    u "So you can take, but you won’t give. I see how it is."

    scene utalovehotel16
    with dissolve

    u "I’ll tell you what...tonight’s {i}clearly{/i} been a slog for both of us, so..."
    u "How ‘bout you get into that bathroom..."
    u "Take off all of your clothes..."
    u "And let me swap places with Uta-chan one more time so she can provide a little...{i}special{/i} service to make your night {i}that{/i} much better..."
    s "That sounds great. Now tell me how this “special service” is going to differ from what I want it to be."
    u "Well, I can’t just tell you while you still have all of your clothes on, Master."
    s "I really wish I could bring myself to believe that there is any hope for sexual gratification in those words, but I just really can’t at this point."
    u "Why not?"
    s "Because you have broken me."
    u "Then I guess I’ll just have to be {i}really{/i} gentle when I’m putting you back together, won’t I?"
    s "..."
    u "..."
    s "God damn it."

    scene utalovehotel17
    with dissolve

    u "Don’t forget to make sure all of the surfaces are properly wiped down first! This is a sketchy hotel and it would be a real shame if Uta-chan were to be sullied by {i}another{/i} surprise fluid tonight!"
    s "Keep talking and I’ll give you all of the “surprise fluid” you’ll ever need."

    scene utalovehotel18
    with dissolve

    u "{i}Oh my God...what am I doing?{/i}"
    s "Are you sure you don’t want to just take a bath together? You-"

    scene utalovehotel19
    with dissolve

    u "Yup! "
    u "And I know that saying this will probably have the reverse effect, but please don’t look over here for the next thirty seconds! I have to do something really quick!"

    scene black
    with dissolve2
    play sound "water1.mp3"

    "I fill the bath with water, making sure its warm before stripping down and getting inside."
    "I also defy all expectations and don’t look Uta’s way for the full thirty seconds I promised to abstain for."
    "At second thirty-one, though, you can bet your ass that’s exactly where I looked."
    "Unfortunately, by then, she was finished with whatever she needed to do...and so I turn my gaze back to the water as she makes her way across the room and over to me."

    u "So...are you ready for your {i}special service,{/i} Master?"
    s "Ready to be disappointed, you mean? Yes."
    u "Don’t get testy with me. Do you have any idea how many people would kill for what you’re about to experience?"
    u "Up until now, I’ve only done this for my family. "
    s "Okay, well that just means my opinion of you is going to change dramatically if this actually does wind up being sexual."
    u "Master, please. If it’s incest you’re looking for, you’re going to need to come back during the morning shift and ask for the one with twintails. She’ll have what you need for sure."

    scene utalovehotel20
    with dissolve2
    play sound "water1.mp3"

    s "Wow, what a surprise. Something completely G-rated."
    u "Oh, hush. You know you’re enjoying this."
    u "Besides, you should be happy since the last person I did this for died of brain cancer and you’re still alive and kicking."
    s "Yeah, that makes me feel great."
    u "On a serious note, though...just relax, Master. Let your worries wash away. "
    u "It must be so nice finally being out of the cold, huh? Can you feel your body warming back up?"
    s "Yeah. But it does feel a little bad knowing that you’re still soaking wet when you should be in my place right now."

    scene utalovehotel21
    with dissolve

    u "Yeah, uhh..."
    u "Probably not a good idea for me to take my clothes off in here."
    s "Do you not trust me?"
    u "Uhhhh..."
    u "{i}I...do...{/i}"
    u "But whether or not I trust you isn’t really the problem."
    s "What is the problem then?"

    scene utalovehotel22
    with dissolve

    u "Can’t say this sounds like letting your troubles wash away, Master."
    s "Just “Sensei” is fine right now. I like being called “Master” and all, but I’d like for this to be a memory between Uta and me. Not Uta-{i}chan{/i} and me."

    scene utalovehotel23
    with dissolve

    u "(Screaming internally and also horny)"
    s "Is there a problem?"
    u "....{i}Nope!{/i} Just a cramp in my arm! Don’t mind me!"
    s "Anyway, if you’re not going to get in with me, you should probably dry yourself off. There’s no way it’s comfortable being in those clothes right now."

    scene utalovehotel24
    with dissolve

    u "It’s no biggie. I used to play in the rain a lot when I was little, so feeling like this is actually a big ole’ nostalgia trip for me right now."
    u "It’s really only my underwear and socks that bother me when they’re wet and I already took those off like a minute ago."

    scene utalovehotel25
    with dissolve

    s "Is that what you were doing when you made me look away?"
    u "What’s this? You actually {i}looked away?{/i} Who knows when the next chance you’ll get to see me in that state is, Sensei?"
    s "I’m sure the day will come. I’m surprised you’re just...okay with talking about that, though."
    u "Why? Are you getting excited?"
    s "Would you join me if I was?"
    u "I’d have to make a phone call first."

    scene utalovehotel26
    with dissolve

    s "If that is what must be done, so be it. Just maybe don’t mention my age. Or my job. Or even my appearance as I don’t want your parents trying to track me down."
    u "I’m not telling anybody anything, Sensei. Don’t you worry."
    u "What matters now is enjoying our time here before the rain stops."
    u "This is all just one more cliche we’ll scratch into our memory books. And when we look back on it years from now, if you’re still putting up with me then, I’m sure we’ll laugh."

    scene utalovehotel27
    with dissolve

    u "Unless you and Io really {i}do{/i} run away, that is. Which you shouldn’t, because losing both of you at once would make it hard for even me to keep on smiling."
    s "Maybe I will? I bet {i}Io{/i} would get in the bath with me."

    scene utalovehotel28
    with dissolve

    u "PFFFT! HAHAHAHA! HAHAHA!"
    s "...Did I say something funny?"

    scene utalovehotel29
    with dissolve

    u "Oh, no! No no no! I shouldn’t have laughed there! I’m sorry! It wasn’t funny. "
    u "That just...it took me by surprise, that’s all. I wasn’t like...doubting you or anything."

    scene utalovehotel30
    with dissolve

    u "I, uhh...{i}would{/i} like to hear why you think that, though."
    u "Unless it’s something you don’t want to talk about. Which, if it is, we can go back to being silent and listening to all of the other couples have sex."

    scene utalovehotel31
    with dissolve

    u "Oh! And when I say “other” couples, I’m not implying that {i}we’re{/i} a couple. No way. We’re just two people stuck inside a room full of condoms, trying to keep each other comfortable without using any!"
    u "Classic Uta-Sensei relationship, right?!"
    s "..."
    u "..."
    u "Please talk. You’re making me feel like I made a huge mistake just now."
    s "I just think you’re acting a little weird, that’s all."

    scene utalovehotel32
    with dissolve

    u "Well...just..."
    u "What makes you think Io would do something like that?"
    u "You...know you can like somebody without wanting to get in their pants, right?"
    s "But that’s the best part."

    scene utalovehotel33
    with dissolve

    u "Not everybody’s like that, Sensei. Some people just want somebody they can be close to or...somebody they don’t get bored of. "
    u "I’m sure there are plenty of girls in the class, cough cough Ami, who’d be happy to jump your bones, but you’re smarter than expecting {i}everybody{/i} to just be on board right away, aren’t you?"
    s "Of course I am. For example, I know {i}you’re{/i} in no rush to “jump my bones,” which is why I’m able to constantly joke about it the way I do."
    u "Hahah...yeah...funny jokes..."

    scene utalovehotel34
    with dissolve

    s "I can’t accurately judge everyone, though. So if you know something I don’t know and are at liberty to share it, I implore you to do so."
    u "Those are dangerous words to say to a girl who’s notoriously bad with secrets, Sensei."

    scene utalovehotel35
    with dissolve

    u "But...umm...for your sake...and because we need more stuff to talk about so all of those couples in the other rooms don’t start makin’ me feel some kind of way..."
    u "I just..."
    u "Well, I wouldn’t get my hopes up if I were you. Least not until you know for sure."
    u "Last thing you wanna do is make a move too early and scare somebody off, you know."
    s "How early is too early?"
    u "That..."
    u "That depends on the girl, I guess..."
    s "How early would be too early for you?"

    scene utalovehotel34
    with dissolve

    u "..."
    s "..."
    u "Um..."

    play sound "texttone.wav"
    scene utalovehotel36
    with hpunch

    u "Oh! My phone! And at the worst possible time!"
    u "Welp, better go answer it!"

    scene black
    with dissolve

    s "Uta-"
    u "S-Sorry, Sensei! It could be important! Like...maybe it’s front desk apologizing for overstocking the condoms?! Or maybe it’s...my mom calling to check in! Yeah! That’s probably it!"

    scene utalovehotel37
    with dissolve

    u "Don’t worry, though! I won’t tell them that we’re in a love hotel! And we don’t have to worry about her asking me to send a picture of where I am either since I still can’t send picture messages!"
    s "If you didn’t want to answer the question, all you had to do was say so."
    u "What question? Did you ask me a question? I don’t remember any questions."

    scene utalovehotel38
    with dissolve

    u "Anyway, phone time! Don’t answer any of the things I just said."

    scene utalovehotel39
    with dissolve

    s "I hope you’re planning on making it up to me when you get back in here. Being neglected in favor of a mysterious text message is not typical maid behavior."
    u "You literally asked me to be normal Uta like five minutes ago. Stop being so needy."

    play sound "phonebeep.wav"
    scene utalovehotel40
    with dissolve
    $ renpy.pause(3, hard=True)
    stop music
    play sound "static.mp3"
    scene utalovehotel41 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "doorslam.mp3"
    scene utalovehotel42
    with hpunch

    s "Uta?..."
    u "{i}Something came up!{/i}"

    scene black
    with dissolve2

    "A voice shouts back at me from outside of the door, overpowering the endless medley of orgasms that have all but lost their impact by now."
    "I can not hear Uta run away, but I know that she does."
    "I finish bathing and hang my clothes up to dry on an old towel rack. "
    "When I return to bed to kill time while waiting for the rain to stop, I notice something out of the corner of my eye."
    "A maroon pair of panties, wet from the rain and lustful teen martyrdom. "
    "I lift them off of the ground."
    "And I dirty them."
    "Repeatedly."
    "Until the rain stops."

    $ renpy.end_replay()
    $ utamaid25p2 = True
    $ uta_love += 1

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "{i}You have acquired [[The Cum-Soaked Panties of a Genki Girl]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm30:
    play sound "knock.mp3"

    "I knock on Uta’s door, figuring that this might be a good time to ask her about what caused her to storm out of the love hotel the other day."
    "I also figure it’s a good time to return her underwear that I may or may not have used to pleasure myself multiple times."
    "And before you ask, yes. I washed them."
    "To be perfectly honest, I thought about keeping them instead. But the idea of her wearing them {i}after{/i} what I did is simply too good for me to pass up."

    u "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "The question now is whether I want to just drop them on the floor of her room without drawing any attention to it, or leverage this position of power to embarrass her."

    scene utadormpanties1
    with dissolve2

    u "Oh, Sensei! What’s up? I was actually just thinking about you."
    s "Was it about how you left your panties behind at the love hotel and how they’re currently stuffed into my pocket?"

    "I leverage my position of power to embarrass her."

    u "..."
    s "If you’re waiting for a punchline, there isn’t one."
    u "You...You’re just carrying around my panties?"
    s "I am."
    u "The...panties that I was wearing? The ones that I took off because they got soaked from the rain?"
    s "Is there something about that you’re not understanding?"
    u "Yes. The part where you took them. And the part where you stuffed them into your pocket. And the part where you are now confessing your evils to me instead of just keeping them and preventing this talk."
    s "I just figured you’d want them back after randomly storming out."

    scene utadormpanties2
    with dissolve

    u "Me storming out has nothing to do with whether or not it’s okay to just walk around with my underwear like they’re some kind of badge of honor!"
    u "You don’t see me walking around with your underwear, do you?"
    s "No. But I don’t wear underwear, so."
    u "What? But you wear jeans like, every day. Doesn’t that make you uncomfortable?"
    s "I find that my pants are off enough for that not to be much of an issue."

    scene utadormpanties3
    with dissolve

    u "Hah...You know, if I didn’t grow up with an older brother who saw my panties on the floor every time he came into my room, this would be a real shock for me right now."
    u "I expected better from you, Sensei. Especially after our night of passion together should have gotten all of that pent up energy out of your system."
    s "I can’t say that spending the majority of the night in there alone while waiting for the rain to stop was the happy ending I was looking for."

    scene utadormpanties4
    with dissolve

    u "Well, you’re smiling now, aren’t you? Which means that the ending had to be at least {i}kind of{/i} happy. Otherwise, you’d be all like, “Uta! I hate you and I’m keeping your panties!”"
    u "Or something. "
    s "Uta-"
    u "What? The conversation is over. Just toss the panties into the pile and we can move onto why I was thinking about you rather than what you did with my underwear."

    scene utadormpanties1
    with dissolve

    u "Wait, you didn’t actually do anything with my underwear, did you? Because that would be weird and gross and not entirely unexpected."
    s "Of course not."
    u "Are you lying to me, you panty-stealing coward?"
    s "No more than you’re lying to me about why you left the hotel."

    scene utadormpanties5
    with dissolve

    u "Hah...Sensei, it’s not really {i}lying{/i} if I just...don’t tell you certain things, is it?"
    s "Not really. But I think there’s an argument to be made about whether or not certain scenarios arise in which that {i}would{/i} be lying, right?"
    s "If I were to get a mysterious text and storm out of the room right now, you’d definitely think I was hiding something, wouldn’t you?"
    u "So, what? You want to know who sent me that message? Will that make you drop this?"
    s "It would be a start."

    scene utadormpanties6
    with dissolve
    stop music fadeout 20.0

    u "Well, sucks for you because I don’t even know."
    s "I don’t believe that."
    u "Believe whatever you want. If it was something I thought you should know, I wouldn’t have just left without saying anything."
    s "Didn’t you just say the other day that you want me to know more about you, though?"
    u "Do you remember what I said after that?"
    s "No. I tend to pick out the best parts of conversations and just hang onto those instead of letting whatever negative connotations they ride in on weigh them down."
    u "Well, {i}I{/i} remember, because both parts of what I said are still true."
    u "I {i}do{/i} want you to know more about me. I just don’t want you to know anything that might make you look at me differently."
    s "Is that not the purpose of learning more about someone? Changing the way you look at them?"
    u "Not when I already like the way we look at each other."

    scene utadormpanties7
    with dissolve
    play music "thesleepingcity.mp3"

    u "So anyway! That was embarrassing! But I’m glad we’ve finally moved on!"
    s "Have we?"

    scene utadormpanties8
    with dissolve

    u "You know, I like you a lot better when you’re not trying to pry into my personal life."
    s "I just want to know more about you. Whether or not that changes the way I look at you is up to me."
    s "Even if it does, though, wouldn’t that just mean I’m {i}not{/i} someone you want to get closer to anyway? Wouldn’t your interest be better spent on someone who will, you know, {i}understand{/i} you?"

    scene utadormpanties9
    with dissolve

    u "No."
    s "Why not?"
    u "Because it’s better for everyone if you never understand me. "
    u "It’s better if I’m Uta-chan."
    u "Uta-chan is the perfect girl who always makes the right decisions. Who cares about everyone else first and herself last."
    u "She never makes mistakes or does things she looks back on with regret."
    u "And that’s all Uta Ushibori ever does."

    scene utadormpanties10
    with dissolve

    u "W...Why do you want to get to know me, Sensei?"
    u "Why did you ask me to stop being Uta-chan when we were in that hotel?"
    u "What can Uta Ushibori do for you that she can’t? You love Uta-chan, right? You’ve asked her...err, {i}me{/i} to marry you like a billion times already."
    u "I’m...fine with just always being that if you want! I don’t have to swap back and forth if the change gets annoying or exhausting."
    u "It’s not like...It’s not like that’s not still part of who I am, you know? It’s all the best parts! I learned to separate them so that...so that we can all move forward and..."

    scene utadormpanties11
    with dissolve

    u "And not get caught in the thorns of decisions Uta Ushibori made."
    s "..."
    u "..."
    s "Our pasts aren’t what define us, you know."
    s "They might help shape us into who we become, but it ultimately rests on us to figure that out ourselves."
    s "If there are things you did in the past that turned you into the person you are today, even if those things are ten times uglier by comparison, I still want to know about them because they made {i}you.{/i}"
    s "Uta-chan is great because she’s perfect. But Uta Ushibori is great because she’s so heavily flawed."
    s "Uta Ushibori is great because she’s an actual human being who makes mistakes and {i}suffers{/i} for those mistakes. "
    s "And Uta-chan knows no suffering at all."
    u "Are you telling me you want me to suffer?"
    s "It might sound mean, but yeah. I am."

    scene utadormpanties12
    with dissolve

    u "Of course you’d be a sadist. Why am I not surprised?"
    s "If you’re going to flirt instead of {i}talk,{/i} at least do so in a way that-"

    scene utadormpanties13
    with dissolve

    u "I’ll talk. I just..."
    u "You’ll be the first person other than Io or my family who’s ever heard any of this."
    u "It’ll be with less, uhh...{i}specifics,{/i} though...because I still {i}am{/i} worried that you’ll figure me out one day and not want anything to do with me anymore."

    scene utadormpanties14
    with dissolve

    u "That would be a huge blow financially. And I don’t know if I’d ever be able to recover from losing my number one customer."
    s "I think Uta-chan is slipping out again."

    scene utadormpanties13
    with dissolve

    u "Right. Yeah."
    u "It’s hard to tell the difference sometimes."
    u "Uhh...let’s see..."
    u "So...um..."
    u "Okay, I guess the easiest way of putting it would be..."
    u "I’ve, uhh..."
    u "I’ve done some...{i}stuff...{/i}that I’m not very proud of in the past..."
    u "Impulsive stuff. Like...when I pulled you into the tea ceremony room the other day but, like...worse than that."
    u "A lot worse."
    u "Stuff that seemed like a really great idea at the time..."
    u "But...when you’re a little kid, it’s...uhh...it’s easier to not really understand the possible, uhh...consequences for your actions..."
    u "And so some of those great ideas wind up coming back to bite you."

    scene utadormpanties15
    with dissolve

    u "I, uhh...I guess I haven’t ever told you the real reason I moved here, have I?"
    s "You’ve told me about your dead grandpa a hundred times. I’m not sure if that’s the full story, though."
    u "That was part of it. But, uhh...the bigger part is that I was dealing with this, uhh...{i}issue{/i} back at home."

    scene utadormpanties16
    with dissolve

    u "That stuff about bad decisions and...consequences we don’t really think of when we’re that young..."
    u "Well, that...uhh...that put me into a pretty...unsafe position..."
    u "I kinda...may have had a bit of a...stalker problem..."
    s "How...big of a problem, exactly?"
    u "Uhh..."
    u "It was...pretty bad..."

    scene utadormpanties17
    with dissolve

    u "N...Nothing ever happened to me, though! He never laid a hand on me! I’m still a...a certified virgin and...it was really just the {i}prospect{/i} of something bad happening that landed me here!"
    s "You didn’t have to-"
    u "I wanted you to know that part! That I’m not...completely tainted yet! That I’m clean! I swear!"
    s "Uta-"
    u "It was just a series of bad decisions that I am still paying for in ways I never expected! Which is why I left the other day! Because I am {i}still{/i} paying for those things and..."

    scene utadormpanties18
    with dissolve

    u "Hahah...I said that I wouldn’t give you any specifics but, here I am, about to give you {i}all{/i} the specifics because I don’t want to cause any misunderstandings and..."
    u "You know, this story is a lot harder to tell to someone who isn’t family. I didn’t have to worry about any of {i}them{/i} leaving me because of stupid stuff I did."
    s "You don’t have to worry about me leaving you, either. Not over something like this."

    scene utadormpanties17
    with dissolve

    u "But you don’t even know the half of it yet, Sensei. This isn’t something that’s going to go away. We’ve {i}tried{/i} that. "
    u "The whole reason my brother is in jail is because he beat the guy who was stalking me until he couldn’t even move anymore. But the problem wasn’t {i}just{/i} him."
    u "The problem is {i}everywhere.{/i} The problem is {i}me.{/i} "
    u "{i}I{/i} am everywhere. "
    u "Do you understand what I’m saying?"
    s "I..."
    s "Understand that this is something we should probably shelve for right now. You’ve told me enough and I get that it’s overwhelming for you."

    scene utadormpanties19
    with dissolve

    u "Do you get it now? Why I have to be someone else?"
    u "I changed everything...Completely reinvented Uta..."
    u "But I still can’t shed the parts of me that made me have to change in the first place."
    u "The real me keeps wanting to bleed through...keeps wanting to do more things I {i}know{/i} are mistakes...but that doesn’t change a thing."
    u "This is just who I am."
    u "One big mistake."
    u "And nothing will ever change that."

    scene utadormpanties20
    with dissolve

    u "Which is why I didn’t want you to know."
    u "I wanted this to keep going without you ever realizing there’s another side to all of this."
    u "But I’m not allowed to want anything."
    u "I haven’t suffered enough yet."
    s "Well, as someone who claimed just moments ago that I {i}want{/i} you to suffer, I beg to differ."

    scene utadormpanties21
    with dissolve

    s "It seems to me that you’ve suffered more than enough. And I don’t know if the source of that will ever go away, but I’m sure it will probably become easier to deal with over time."
    u "I don’t think it will."
    s "Then don’t think at all."
    u "Not thinking at all just makes it harder to deal with when it comes back to bite me again. Which it always does."
    u "{i}I was just a kid, Sensei.{/i}"
    u "I had no idea what I was doing. I {i}still{/i} have no idea what I’m doing and I’m in high school now. "
    s "Something you did that long ago would never change the way I look at you today."
    s "And while I won’t say I’m thankful it happened as it’s clearly made your life very hard to manage, I will reiterate once more that I like both forms of Uta Ushibori."
    s "And that my opinion of you hasn’t lessened in the slightest."
    u "..."
    s "..."

    scene utadormpanties22
    with dissolve

    u "Hah..."
    u "Sharing your feelings is exhausting. I have no idea how Io does it literally all day every day."
    s "Yeah, but I’m sure there’s a lot I don’t know about her either."
    u "Course there is."

    scene utadormpanties23
    with dissolve

    u "Girls like us aren’t exactly open books. And even when you get us open, it’s like everything’s in a completely different language."
    u "I’m sorry for dumping that on you, Sensei. I tried to spare you, but you just kept on pushing and I ain’t good at dealing with stuff like that."
    u "It does feel a little better to...clue you in on the different sides of me, though. I was really worried that you’d see that as a big ole red flag and just book it once I started talking."
    s "Nah. You let me borrow your underwear for over 24 hours, so the least I could do was hear you out until the end."

    scene utadormpanties24
    with dissolve

    u "Thanks. But please download CashApp and shoot me some money next time you decide to do that. I’m letting you off the hook for last time as a free trial, but I’m charging hourly from now on."
    s "Noriko lets me borrow her underwear for free and hers are a lot fancier than yours."

    scene utadormpanties25
    with dissolve

    u "That offended me a lot more than I thought it would. A girl takes great pride in her panties, you know."
    s "Not enough pride to keep them on in a hotel, apparently."
    u "They were wet and I was uncomfortable. I regret nothing other than the fact that they wound up in your hands."
    s "Well, I’ll be more than happy to {i}make you comfortable{/i} in my own way next time."

    scene utadormpanties26
    with dissolve

    u "Saying that right after I open up about my history of impulsive and bad decisions? Have you no shame, Sensei?"

    play sound "phonebeep.wav"
    scene utadormpanties27
    with dissolve

    u "And now your {i}phone{/i} is going off?! You should know darn well you’re supposed to silence your phone during heart-to-hearts with a cute girl! You really {i}do{/i} have no shame!"
    s "It’s probably just Ami asking when I’ll be home for dinner."
    u "Damn that top contender and her unflappable uncle love! We’re supposed to be having a moment here!"

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I tap on my recent messages, expecting Ami’s name to show up at the top of the queue."

    stop music

    "But what I find is something completely unexpected."

    play sound "phonebeep.wav"

    if uta_custom_name != "":
        "{i}You have 1 new message from [uta_custom_name]!{/i}"
    else:
        "{i}You have 1 new message from Uta Ushibori!{/i}"

    play sound "static.mp3"
    scene utalolinude with flash
    stop sound
    $ renpy.pause(5, hard=True)

    u "Sensei? Is something wrong?"

    play sound "static.mp3"
    scene utadormpanties28
    with flash
    stop sound

    u "Is it Ami like you expected? Or is it Noriko asking when you’re going to return her fancy underwear?"
    s "..."
    u "..."
    u "Sensei?"
    s "It’s..."
    s "It’s nothing."

    scene utadormpanties29
    with dissolve

    u "Oh?"
    u "Don’t tell me it’s Princess Maya summoning you for a late night booty call?"

    scene utadormpanties30
    with dissolve

    u "Let me see your phone. I know how to deal with-"
    s "Don’t."

    scene utadormpanties31
    with dissolve

    u "Huh?"
    s "Don’t touch my phone."
    u "Oh. Uhh...sure."
    u "I wasn’t trying to get up in your bubble or anything."

    play sound "phonebeep.wav"
    scene utadormpanties32
    with dissolve

    s "I have to go."
    u "What?..."
    u "This isn’t just payback for how I left you hanging the other night, is it? Do you really have to go? Or are you just saying that?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "I really have to go. But I’ll see you in school."
    u "Really? You can’t even stay just...a little while longer?"
    s "I can’t."
    s "I don’t want to make a mistake."

    "I leave Uta’s room."
    "The walk home does not cling to my memory."
    "But the glow of a dim blue light does as I indulge in the rotten fruit of her past impulses."

    play sound "phonebeep.wav"
    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm30 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
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

label utaspecial35:
    scene hall_noon
    with dissolve2
    play music "morningmoon.mp3"

    "As both the school day and my counseling hours come to an end, I’m left with nothing to do but mindlessly roam the halls in hopes of encountering someone or something."
    "And while it is true that I carry a small, electronic device that enables me to create {i}opportunities{/i} for things to happen, I find that it’s often more interesting to let the world decide my schedule instead."
    "As such, here I am — alone and melancholic, letting the warm sun creep through the windows and illuminate my body with the light and luster of longing and loss."
    "What I long for is a way to fill this void with something that won’t sink through my stomach when I lie in bed tonight."
    "What I’ve lost is the will to make that happen."

    u "{i}Ngh!{/i}"
    s "..."

    "Or have I?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene utalibrary1
    with dissolve2

    u "Ngh......mmngh!"

    "I enter the library and come face to face with what I’m pretty sure is my first soirée into the cliché, yet realistic trope of a short girl trying to reach something on a shelf that’s just a little too high."
    "This, of course, opens up a window of infinite choices on how I’m going to tackle the situation."
    "Would it be best to just stand here and wait for her to ask for my help? "
    "Should I take the more aggressive and dramatic approach of lifting her up and letting her grab her desired book on her own?"
    "Or should I maybe plunge this world into total chaos, knocking the shelf completely over and potentially killing Uta in the process?"
    "The possibilities are endless."

    u "Nnnghhhhh!!"

    "But if I don’t do something soon, Uta could dislocate or permanently damage her arm- which would make it harder for her to provide daily handjobs to me when we are ultimately married."

    scene utalibrary2
    with dissolve

    "So, I guess I’ll cut her some slack and lend a hand so that I may one day fully experience hers."

    u "Huh? Where’d you come from?"
    s "Which one are you trying to reach? "

    scene utalibrary3
    with dissolve

    u "Oh. Uhh...that red history book a little to the right. I can’t really see the full title from all the way down here."
    s "And you were reaching for it anyway? Since when is your interest in history that pure?"

    scene utalibrary4
    with dissolve

    u "My interest in history doesn’t exist. I just texted Futaba asking which one covers some of the stuff Imani’s been teaching us lately and...this is me following her directions."
    u "Or trying to at least. She forgot to mention this book had a height requirement."

    scene utalibrary5
    with dissolve

    s "Here. This one, right?"
    u "Yeah. That’s the one."

    scene utalibrary6
    with dissolve

    u "What do you want in return, though?"
    s "Return?"

    scene utalibrary7
    with dissolve

    u "I know how this works, Sensei. {i}You{/i} hand me the book. Then {i}I{/i} try to thank you. Then you say something like, “Thanks ain’t enough, sugar. There’s somethin’ else I’m after, ” while staring at my body."
    s "You could have at least made the dialogue more...{i}me-{/i}like. I can’t really envision ever calling anyone “sugar.”"
    u "Just tell me what kinda prize you’re after so I can figure out whether or not the book is of equal value."
    s "I was going to give it to you out of the kindness of my heart. But now, I’m curious as to what I can actually {i}get{/i} for it."

    scene utalibrary8
    with dissolve

    u "{i}You{/i} were gonna do something out of the kindness of your heart? Even though this is the exact type of tropey situation guys like you dream about? I’m surprised you didn’t just pick me up."
    s "You should be happy I didn’t pick you up. If I did, who even knows when I’d be willing to put you down again?"

    scene utalibrary9
    with dissolve

    u "So you’re after the whole package after all, huh?"
    s "Or just a kiss."

    scene utalibrary10
    with hpunch

    u "Huh?!"
    s "Why does that embarrass you more than the “whole package?” "
    u "That package doesn’t include kissing!"
    s "What does it include then? "
    u "A night of fiery passion, a morning of deep regret, several moments of intense pelvic pain, and a phone call to my parents! Nobody ever said anything about kissing!"
    s "In that case, I will take one night of fiery passion. Thanks."

    scene utalibrary11
    with dissolve

    u "No, that doesn’t work either! I was just listing the contents! I never agreed to the fiery passion!"
    s "Just take the book, Uta."

    scene utalibrary12
    with dissolve

    u "Can I?"
    s "Yeah. Like I said, I planned on doing this out of the kindness of my heart and was fully prepared to keep all of my fantasies about you to myself."
    u "Just...out of curiosity...are we talkin’ like...one or two fantasies? Or..."
    s "You’re missing about ten zeros."

    scene utalibrary13
    with dissolve

    u "T..."
    u "Ten...zeros?"
    s "I said what I said."
    u "That’s..."
    u "That’s a lot of fantasizing..."
    s "I’m starting to think you don’t even want this book."
    u "Do you really..."
    s "..."
    u "..."

    scene utalibrary14
    with hpunch

    u "A-hah!"
    s "“A-hah” what? Why am I being “A-hah”ed?"
    u "You’re just messing with me! You think throwing out a huge number with ten zeros will get me to compromise and give you some kind of consolation prize! I know your tricks!"
    s "There are no tricks. You’re just a little delusional and very sexually repressed."
    u "That may be true! But the library isn’t the place to discuss it!"
    s "Shall we take this outside then?"
    u "Outside?! Are you an exhibitionist?!"
    s "I {i}can{/i} be."
    u "I knew it!"
    s "..."

    scene utalibrary15
    with dissolve

    u "..."
    s "So, do you get like this every time someone gets something off of a shelf for you?"
    u "We all do. Everyone knows that us short girls wait our entire lives for tall people like you to walk by and remind us of all the things we can’t do on our own. It really gets us going."
    s "Wow. I really should have just picked you up, huh? "
    u "I...I can’t think of a safe way to answer that question, so I’m just going to take my book now! Thank you!"

    scene black
    with dissolve2

    "Uta snatches the book out of my hands and retreats to the corner of the library to...presumably read it."
    "But seeing as the world has decided that {i}she{/i} will be the one to fill my void today, I have other things in mind."
    "........."
    "......"
    "..."

    scene utalibrary16
    with dissolve2

    u "You’re...staying with me?"
    s "Is that a problem?"
    u "It’s not a problem. I just thought it was kind of obvious that I need to study, so...I don’t want to bore you or anything."
    s "I’ll never be bored while I’m looking at you, Uta."

    scene utalibrary17
    with dissolve

    u "Could you maybe...stop saying stuff like that to me? Just...Just for today, I mean. I’m not going to be able to focus if you’re all...flirty like that."
    s "Why do you need to focus in the first place? Do you actually, like...{i}care{/i} about learning all of a sudden?"

    scene utalibrary18
    with dissolve

    u "I don’t really have much of a choice. I’ve been getting a lot of extra work from Imani lately so I can catch up to everybody else and stay in the class."
    s "Stay in the class? Did she threaten to kick you out or something? Because I’m pretty sure that’s above her pay grade."

    scene utalibrary19
    with dissolve

    u "I think it’s more of a testing...formality thingy than her actually wanting to get rid of me. Our grades for all those important school-wide tests get sent to our parents and mine...well..."
    u "Let’s just say they aren’t really the happiest when it comes to my performance. Which...is fair. I’ve been slacking off."

    scene utalibrary20
    with dissolve

    s "Do you...need my help?"
    u "Hm? No. I appreciate the offer, but I’ll manage on my own. I get too distracted in groups."
    s "Well, that’s a relief because I know next to nothing about history and wouldn’t have been much help anyway."
    u "You already did your part by being tall. Uta-chan can handle the rest. But if you want to sit there and watch her while she reads, she’ll let you do it for cheap."
    s "How about I just help instruct Uta-chan in the subjects that I {i}do{/i} specialize in instead?"
    u "Is this the part where you make a biology joke?"
    s "..."
    u "..."
    s "No."
    u "It was, wasn’t it?"
    s "You don’t know me."

    scene utalibrary21
    with dissolve

    u "No, but I {i}do{/i} know your tricks. And I’m not about to let you get the upper hand on me {i}again{/i} when I’ve practically lived on the...lower...hand?"

    scene utalibrary22
    with dissolve

    u "Why is “upper hand” a thing but not “lower hand?” Who comes up with phrases like that?"
    s "Again, this isn’t really an area of expertise for me. But feel free to inquire if you have any questions about cute girls or obscure poets."

    scene utalibrary20
    with dissolve

    u "Quite the specializations you’ve got there. Figured there’d be a few more given your {i}age and experience{/i} though."
    s "There are. You just get a little too flustered whenever I talk about them. "

    scene utalibrary23
    with dissolve

    u "Hahah...hah......hah.....you must be...confusing me with someone else."
    s "Right, yeah. I’m probably thinking about the other Uta. If you’re Uta-chan, you’re probably not interested in me {i}at all,{/i} right?"
    u "Did...did somebody tell you that...normal Uta {i}is?{/i}"
    s "Nope. Just a hunch."
    s "I figure if normal Uta {i}is{/i} interested in me, though- it’s only a matter of time until she cracks since her best friend has already given her the blessing to go ahead and make some moves."
    u "And I...think you might be...misreading the situation a little, but..."

    scene utalibrary24
    with dissolve

    u "But that’s a...topic for another day! Hahah! Look at us, pretending to be all...whatever...whatever that was just now."
    s "You used “flirty” a few minutes ago. I feel like that sums it up well enough."
    u "Yeah, but...you’re like that with everybody. Is it really flirting if that’s just your default setting?"
    s "I feel like you would know, if anyone. You’re the one who’s figured out a way to monetize that setting. {i}And,{/i} on top of that, you have {i}another{/i} one you can switch to after work. I envy that."
    u "You shouldn’t. It’s a lot more exhausting than I make it look. And most of the time, I’m kind of just...internally screaming."
    s "About what?"

    scene utalibrary25
    with dissolve

    u "..."

    play sound "static.mp3"
    scene utadownbad29alt with flash
    stop sound

    u "(Screaming internally)"

    play sound "static.mp3"
    scene utalovehotel23alt with flash
    stop sound

    u "(Screaming internally and also horny)"

    play sound "static.mp3"
    scene utalibrary25 with flash
    stop sound

    u "Oh...nothing in particular..."

    scene utalibrary24
    with dissolve

    u "B-Besides! I’m sure there are plenty of other people who you’d like more than me. And I’m not just talking about Io or any of your other girlfriends this time either."
    s "Did Io get promoted to “girlfriend” status without my knowledge?"

    scene utalibrary26
    with dissolve

    u "That’s hard to say..."
    u "I know you two haven’t, like...kissed and stuff yet. But I also know she actually, like...{i}talked{/i} to you."
    u "About...her thing...."
    s "She certainly did. Right around the same time the possibility of a triad was brought up."
    u "Probably goes without saying, but...Io doesn’t...talk about that kind of stuff with just anybody, Sensei. You must be really special to her if she felt comfortable enough to admit all that."
    s "You did the same thing, didn’t you? Admitted something about your past that you have trouble looking back on."
    u "But my thing was me being young and stupid. Io was never at fault for anything she did."
    s "Neither were you."

    scene utalibrary27
    with dissolve

    u "Huh?"
    s "Like you said, you were young and stupid. Expecting you to make rational decisions back then would be a little...unreasonable."
    s "You got caught up in a feeling and did something you felt like you should do. That’s more of an accident than something done with true intent."
    u "But it’s still...it’s still something {i}I{/i} did. That {i}I{/i} pay the price for."
    s "I get that. But I’d look at you the same way whether or not any of that happened."

    scene utalibrary28
    with dissolve

    u "..."
    s "..."

    scene utalibrary29
    with dissolve

    u "Let’s...you know...we, um..."
    u "Another topic...this one is...I’m starting to feel a little...uh..."

    scene utalibrary30
    with dissolve

    u "Uhh...Dorm Wars! How did you..."
    u "How did you feel about this year?"
    s "It was...different. It felt more like our regular beach trip but with a few contests sprinkled in. I might just be saying that this time since there were several that didn’t involve me, though."

    scene utalibrary31
    with dissolve

    u "I agree. I think it worked for Halloween since that’s normally just a one day event, but there were a lot of girls on the beach who kind of just wanted to relax for the weekend."
    u "Some of the contests went pretty well, though. Like...the swimsuit one was pretty fun. And Io told me she enjoyed herself with the raft thingy. Plus, Futaba’s horror story was actually pretty cool."

    scene utalibrary32
    with dissolve

    u "Now...Nodoka’s on the other hand..."
    s "..."
    u "I don’t know if I was just...maybe expecting a little too much since she’s apparently an amazing writer or...or if I just didn’t get it, but..."
    u "I can’t really wrap my head around whatever hers was supposed to be."

    scene utalibrary31
    with dissolve

    u "Do you have any thoughts, Sensei? You seemed pretty interested once she finished, so I figured that maybe there was a part of it {i}you{/i} got that I was just too dumb for."
    s "..."
    u "..."
    u "Sensei?"
    s "It’s weird."
    s "It definitely had some sort of effect on me, but I can barely remember any of it and...it’s hard to put into words what the effect even {i}was.{/i}"
    u "Maybe it was one of those open-ended thingies? Somethin’ that people are supposed to interpret in...different ways? Like...like psychic readings or something. Do you believe in that stuff, Sensei?"
    s "Not even remotely."

    scene utalibrary32
    with dissolve

    u "Is that so? That’s a shame. Uta-chan was about to offer you a special palm-reading and it could have been the only chance you’ll ever get to touch her. Too bad you don’t believe in her psychic powers."
    s "Do {i}you{/i} believe in psychic powers, Uta?"

    scene utalibrary33
    with dissolve

    u "Mmm...I guess a little. No more or less than most girls my age, I think."
    u "I’m sure a lot of it is fake, but I think there’s gotta be some kind of truth to it. Even if it’s just kinda...manifesting whatever it is the psychic tells you further down the line."
    s "The problem with believing things in a roundabout way like that is that you’ll never really be able to prove yourself right or wrong. You’ll always just be stuck with a “maybe.”"

    scene utalibrary16
    with dissolve

    u "Why is that a problem?"
    s "It’s less of a problem and more of just...a depressing uncertainty. Like, what do you gain from living your life under the pressure of so many “what ifs?”"

    scene utalibrary34
    with dissolve

    u "Well...for me, it’s like...{i}what if{/i} the truth is...the opposite of what you want?"
    u "What if the thing you find out winds up making it even harder to be the person you were {i}before{/i} you found out? "

    scene utalibrary31
    with dissolve

    u "So what if people believe in a thing that isn’t actually there? If believing in that thing makes them happy, I say go for it. You don’t need a definitive answer- just a little hope and..."
    u "And the knowledge to know when you should probably stop listening."

    stop music
    scene black

    "I stop listening."

    $ renpy.end_replay()
    $ utaspecial35 = True
    $ uta_love += 1

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadate35:
    play sound "phonebeep.wav"

    "I tap on Uta’s name in my phone and wait for her to answer."
    "It’s still early, so the chances of her being asleep are pretty high. But, then again-"

    play sound "phonebeep.wav"

    u "Hello? Sensei?"
    s "Hold on. Inner monologue isn’t done yet."
    u "Oh, okay. I get it."

    "But, then again, with the archery club actually being the only {i}real{/i} club at Kumon-mi High and Uta being the ace of it, I wouldn’t be surprised if she was already on her way over there."
    "Which, by the sound of it, she likely is."

    play music "summerwind.mp3"

    s "Okay. Done. Please continue."
    u "Continue what? You called {i}me.{/i}"
    s "Oh, right. What are you doing right now?"
    u "Right now? Talking to you and attempting to put my socks on with one hand. It’s way harder than it sounds."
    s "Exciting. What else are you wearing?"
    u "Thaaaaat would be a secret, Sensei. But it’d be easier to guess what I am {i}not{/i} wearing."
    s "Of course it would be easier to guess that. You literally just told me you were still putting your socks on. Which means you are either not wearing socks or...you’re just weird and you wear more than one pair."
    u "Not...really what I was...uhh..."
    u "Anyway! Why are you callin’ so early? What can little ole’ Uta do for ya?"
    s "She can stop whatever she’s doing right now and come hang out with me."
    u "I can’t even put on socks first?"
    s "Depends on if it’s your first or second pair."
    u "Also, wait- no! I have practice this morning. Miss Watabe will probably tie me up and do weird things to me if I’m late."
    s "That should be even more of a reason to show up late."
    u "You know, you’re kinda right. That doesn’t sound so bad apart from the part where I’d be betraying Osako-chan and she could kick my head off."
    u "I really can’t hang out, though."
    s "I really think you should."
    u "Ngh. Ain’t teachers supposed to talk their students {i}out{/i} of skipping school-stuff? What do you think you’re doing here? What’s your end game, Sensei?"
    s "My end game is just getting you to choose me over your responsibilities. It’s the ego boost I need first thing in the morning."
    s "Plus, you’ve yet to come to my house while no one else is home and I think the time has come."
    u "PFBPFBPFBFBFFBGHGHB!?!??!?!!? WHAT?!"
    s "What even was that?"
    u "I just spit my friggin’ tea all over my bed, that’s what! You’re inviting me to your house?!"
    s "Yeah."
    u "While no one else is home?! It would be just the two of us?!"
    s "That is what is happening, yes."
    u "Do you have any idea how many phone calls I have to make now?! Do you have any idea what you’ve done?!"
    s "Are you coming or not?"
    u "No! No way! That’s the point of no return! I don’t know what kinda crazy morning wood you had to wake up with to propose something like this, but it’s not happening! No way!"
    s "I bet you’d come over if I was that talking sponge you used to have a crush on."
    u "Stop bringing up the sponge!"
    s "If you’re not going to come over, could you at least meet up with me somewhere?"
    u "Ugh...why are you so pushy today? And why does it have to be when I already have a thing to do?"
    s "Because I know you’ll cave and choose me if I keep pestering you about it."
    u "Mngh..."
    s "And I want to see you."
    u "..."
    s "..."
    u "I..."
    u "{size=-15}I want to see you too...{/size}"
    s "Say that again?"
    u "Aaah! I said meet me at the park! Bye!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Uta hangs up the phone and my first victory of the day comes as soon as I wake up."

    scene sky
    with dissolve2

    "I feel a little guilty about making her skip the one [[non-extortionate] thing she’s really good at, but it will all be worth it soon enough."
    "Because after the bashfulness wears thin and the first few steps in cracking her mask of reluctance have been made, she’ll be something worth treasuring."
    "She’s that right now, of course. But she can be {i}more.{/i} "
    "And I know she {i}wants{/i} to be more."
    "I can feel it when she’s near. "
    "I can see it in her eyes and hear it when she speaks."
    "And it feeds the evil part of me."
    "I had a dream last night."
    "That dream made me wake up hungry."

    play sound "static.mp3"
    scene utaparkscene1 with flash
    stop sound

    u "There...are you happy now? You got a teenage girl to skip morning practice for you."
    s "You look nice today."

    scene utaparkscene2
    with dissolve

    u "Th...Thanks...but...I don’t know if it’s the best idea to say that sort of stuff with all these people around. They might get the wrong idea about us."
    s "That’s kind of the point."

    scene utaparkscene3
    with dissolve

    u "Well if your {i}point{/i} is trying to get yourself in trouble, you’re pretty darn close to making your dreams a reality, Sensei."
    s "Yeah, it’s probably for the best if that {i}doesn’t{/i} happen. We can come close, though."

    scene utaparkscene4
    with dissolve

    u "Huh? Close to what? I feel like I’m missin’ some context here."
    s "You are. And you should. But that doesn’t concern you right now as we’re here on a date and we’re supposed to look like we enjoy each other’s company."

    scene utaparkscene5
    with dissolve

    u "Ah! I knew this was a date! You tricked me into meeting you here by throwing out an idea like coming over to your place because you knew I’d refuse and have to meet you in public instead! "
    s "Uta, I can be a very calculating person at times. That much is inarguable. But you are giving me way too much credit and putting way too much thought into what I’m actually calculating."

    scene utaparkscene6
    with dissolve

    u "Is this...really okay?"
    s "Why would it not be okay?"
    u "Because you have Io. And Maya. And Chika."

    scene utaparkscene7
    with dissolve

    u "And Ayane and Makoto and Futaba and Imani and Nodoka and Touka and Noriko and Kirin and-"
    s "Okay, I get it. I’m...talking to a bunch of girls. But it’s not like I’m involved with all of them."

    scene utaparkscene8
    with dissolve

    u "But...{i}some{/i} of them?"
    s "Why does it matter who I am with any of them when I’m with you right now? "

    scene utaparkscene9
    with dissolve

    u "Because...they’re my friends..."
    u "And the way you’re acting today is...making me feel like you’re kind of, just..."
    u "Like you think I’m..."
    s "..."
    u "..."
    s "Do you want it to be a date or not? Because it doesn’t have to be. We can just hang out like...any other platonic couple of...an adult male and a high school girl."

    scene utaparkscene10
    with dissolve

    u "The...the people around us are probably looking at this as some sort of compensated dating thing...You know that, right?"
    s "Does that make you uncomfortable?"
    u "Does that make {i}you{/i} uncomfortable? Because it’s one thing for people to look at me as...desperate for cash or...just...just {i}easy{/i} or something, but..."
    u "It’s kind of...always buried in the back of my mind that people are going to look at me that way anyway, so..."
    u "So you’re the one I’m worried about right now..."
    s "You don’t have to worry about me, Uta. I’m old enough to make my own decisions."

    scene utaparkscene11
    with dissolve

    u "And I, unfortunately...am not. Not for a few more years at least. Or until I get off my parents’ phone plan."

    scene utaparkscene12
    with dissolve

    u "I’ll stop dragging down the mood now, though."
    u "But...to...to get back to the {i}date{/i} thing...could we maybe, like...{i}not{/i} call it that? Because that makes it feel like I’m doing something wrong and..."
    u "And just meeting up is fine if nothing happens, right? Like, this isn’t me going behind anybody’s back or...or anything like that. "
    u "This is, like...this is normal. I’m not...I’m not jumping the gun or...like...l...leading you on or...something?"
    s "You look way too nervous for a girl who is platonically meeting her platonic friend in the park on their way to go do...platonic things."

    scene utaparkscene13
    with dissolve

    u "Thank you..."
    u "And...and sorry for being weird about this. And...I guess I’ll just apologize in advance for every other meeting we have like this in the future, where I will also be flighty and awkward."
    u "Which isn’t me assuming there will be more meetings like this in the future, of course. Just...you know. Precaution."
    u "I...I kind of have to be careful because I...you know...I’ve got a history of...bad decisions and-"
    s "You’re dragging down the mood again."

    scene utaparkscene14
    with dissolve

    u "God, I know. I’m the worst compensated date ever. There isn’t even any compensation involved."

    scene black
    with dissolve

    s "You can compensate me by joining me over there where there are less people to eavesdrop on us."
    u "Thanks, Sensei. I- wait a minute! Ain’t it me who’s supposed to be getting compensated?!"
    s "Probably not something you should yell in broad daylight."
    u "I...hahah! Nothing to see here, folks! That’s just...that’s my older brother! Haha! We’re just friends!"
    s "You’re making it worse."
    u "Yeah, because you abandoned me when I needed you most!"

    "........."
    "......"
    "..."

    scene utaparkscene15
    with dissolve2

    u "Hah..."

    "Uta and I retreat to a corner of the park where the passersby are minimal, leaving us to wallow in momentary self-pity and stifled arousal."
    "And yes, I may have jumped the gun by using her obvious feelings for me as bait in an attempt to reel her in, but things are clearly a little more complicated than that, and..."
    "And I didn’t really think about how this would look from her perspective."
    "It wasn’t all that long ago where she was opening up about her past to me. And for me to learn all of that and subsequently jump to “You should come over to my place” isn’t really a good look."
    "It’s an accurate one. That I won’t deny. But it’s not {i}good.{/i}"
    "And I can {i}be good{/i} now."

    u "Well, that didn’t go perfectly."

    "{i}She’s just so attractive.{/i}"

    s "No. But, on the bright side, I gained a little sister."

    scene utaparkscene16
    with dissolve

    u "You wouldn’t want me as an actual little sister, Sensei. I was a big ole pain in my brother’s butt growing up."
    s "Not enough of a pain for him to avoid getting arrested for defending your honor."
    u "I don’t have any {i}honor.{/i} And siblings kind of just look out for one another regardless of their relationship."

    play sound "static.mp3"
    scene happy1 with flash
    scene o with flash
    scene happy2 with flash
    scene utaparkscene17 with flash
    stop sound

    u "Still, though...we had a good relationship. Even {i}if{/i} I was annoying. "
    u "It was always out of admiration at least. Just the...typical “little sibling trying to impress big sibling” kind of stuff."
    s "..."
    u "I really hope he’s doing okay. It’d be nice if you got to meet him one day."
    s "Sure. I can introduce myself as your {i}new{/i} brother and the reason your education has plateaued. "

    scene utaparkscene18
    with dissolve

    u "{i}Or{/i} you could introduce yourself as my teacher. {i}Without{/i} the plateau part. "
    s "And then what? Go out for drinks and bond over our shared desire to make you feel significant?"

    scene utaparkscene19
    with dissolve

    u "You’ve got a lot more in common than that. He’s a little more...social than you, but you’ve got the same sort of attitude going on. Like you’re always observing everybody and...thinking about stuff."
    u "Plannin’ out your next moves and all that."
    s "I’ll be sure to send him my regards when I am sent to jail over your incredibly suspicious “he’s my brother” act a few minutes ago."

    scene utaparkscene15
    with dissolve

    u "Please don’t. One person goin’ to jail over me is one thing. But if there’s a second, I might have to just stop talking to boys altogether."
    s "That bisexuality sounds like it might come in handy soon."

    scene utaparkscene20
    with dissolve

    u "I’m not letting you go anywhere, Sensei. {i}Especially{/i} jail. "
    s "I didn’t realize you had that sort of pull with the legal system."

    scene utaparkscene21
    with dissolve

    u "{i}I{/i} don’t. But Touka probably does and I think I’m in pretty good with her at this point."
    u "Matter of fact, you could probably go on as many fake compensated dates with me as ya want and it’ll be totally fine!"

    scene utaparkscene22
    with dissolve

    u "{i}If{/i} you can convince me to come out for them, of course. You might have gotten the best of me today, but it could very well be a one time thing, Sensei. Uta-chan’s time is highly sought after, you know."
    u "There are tons of boys and girls all over Kumon-mi desperately emptying out their wallets to try and spend time with her."

    play sound "static.mp3"
    scene utaparkscene23 with flash
    stop sound

    u "Uta-chan won’t blame you for wanting a turn as well, Sensei. The new {i}her{/i} is the perfect specimen, after all."
    s "What?..."

    "{i}You recall a moment not long ago where you pleasured yourself to an image that no one can find out you have.{/i}"

    play sound "static.mp3"
    scene utaparkscene24 with flash
    stop sound

    s "What? No I don’t."
    u "Sensei?"

    "{i}Yes you do. You recall masturbating to it three times that night. Then an additional twenty-eight times in the days to follow.{/i}"

    s "No...that never happened."

    "{i}Based on prior thought patterns, that number is expected to increase again tonight!{/i}"

    s "It won’t. That won’t happen. Who are you?"

    "{i}A ghost!{/i}"

    stop music
    play sound "static.mp3"
    scene utaparkscene25 with flash
    stop sound

    u "Who are you talking to?"
    u "Was...somebody calling out to you or something?"

    "{i}Despite how much you don’t want to believe it, you long for a taste much sweeter than what’s lingered on your tongue in the year/years past!{/i}"
    "{i}You long to {b}re{/b}-experience the most delectable and forbidden fruit of all!{/i}"
    "{i}And you now have a chance to vicariously do that through the tiny body of a girl who was exposed to the world at a young age! Hooray!{/i}"

    s "I...I just need a minute, Uta."
    u "Yeah...Yeah, okay."

    "{i}Uta thinks about your fat cock and how she wants you to ram it so deep inside of her little pussy that it leaves permanent damage so she won’t be so fucking horny all the time anymore.{/i}"

    s "Just...one minute..."

    "{i}You think about that fucking bastard who got her pictures before you did and worry that he showed them to all of his friends and that they all jerked it together while staring at them.{/i}"
    "{i}You think she’s unclean. You think of the moments leading up to her decision to go through with such a stupid thing but, more than anything, you wish you were there.{/i}"
    "{i}You wish you were the one teaching her to pleasure herself. You wish you were fucking her.{/i}"
    "{i}You wish you broke into her fucking house when her parents weren’t home and fucked her because that’s what she wanted. She wanted to get FUCKED. She wanted an older man to FUCK her.{/i}"
    "{i}You’re an older man, aren’t you? So why aren’t you FUCKING her?! Huh?! What do you think you’re doing?! Fuck her! Fuck any form you want!{/i}"

    play sound "static.mp3"
    scene utaparkscene26 with flash
    stop sound

    "{i}Remember it!{/i}"
    "{i}Remember what it was like. Remember the fucking PUSSY and its fragility and the crying and how fucking GOOD it was you disgusting fucking PIG!{/i}"
    "{i}This is you! You jerk off to little girls! You’re a man who jerks off to little girls! You’re a disgusting husk of a man who jerks off to little girls! Tell her! Tell her you know! Tell her you’ve seen her!{/i}"
    "{i}Show her how hard your cock gets for her childish mistakes! Then fulfill both of your wildest fantasies and fuck her! Fuck her hard! Do it!{/i}"

    m "Is...something wrong?"
    s "Yes."
    m "I see."
    s "..."
    m "Do you want to talk about it?"
    s "No."
    m "I see..."
    s "..."
    m "Would it be any easier if this all just went away?"
    s "..."
    m "..."
    s "Yes."
    m "Okay."
    m "That’s all you had to say."

    play sound "static.mp3"
    scene utaparkscene27 with flash
    stop sound
    play music "summerwind.mp3"

    u "{i}If{/i} you can convince me to come out for them, of course. You might have gotten the best of me today, but it could very well be a one time thing, Sensei. Uta-chan’s time is highly sought after, you know."
    u "There are tons of boys and girls all over Kumon-mi desperately emptying out their wallets to try and-"
    s "I’m sorry."

    scene utaparkscene28
    with dissolve

    u "Hm? Sorry for what? Makin’ me skip practice? Because I ain’t that worried about-"
    s "For something else."
    u "Something...else?"
    s "I’m just..."
    s "I’m sorry."
    u "..."
    s "I couldn’t help it."
    u "..."
    s "..."
    u "Sensei."
    s "..."
    u "You jerked it into Uta-chan’s panties, didn’t you?"
    s "..."

    scene utaparkscene29
    with dissolve

    u "Hah...I knew you had to be lying when you gave them back to me. But I understand. And I will not hold it against you. "
    u "You are only human. And Uta-chan is a goddess."

    scene black
    with dissolve2

    u "But, as I was saying before your random admission of guilt, I..."

    "The rest of the “date” carries on normally."
    "And I forget what it was I dreamt last night."

    $ renpy.end_replay()
    $ utadate35 = True
    $ uta_love += 1
    stop music fadeout 7.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label utadorm40p1:
    play sound "knock.mp3"

    "I knock on Uta’s door and make a silent promise to myself that I am going to be more normal today than I was during our fake date at the park."

    s "..."
    s "..."
    s "..."

    "But, in order to do that, I’m going to need her to answer the door as I can’t exactly be “normal” while standing in the middle of the hall and blankly staring at it."

    s "..."

    "Then again, I {i}could{/i} just go in."

    play sound "static.mp3"
    scene boundariesredux1alt with flash
    stop sound

    "But that hasn’t exactly worked out well in the past."
    "At least...not by any {i}standard{/i} definition of the word “well.”"
    "I did get to see boobs, though."
    "And getting to see Uta’s-"

    play sound "static.mp3"
    scene utalolinude with flash
    scene iovisityuki1 with flash
    stop sound

    "And getting to see the almost fully grown version of Uta’s sure sounds like it would be nice."

    s "..."
    s "..."
    s "..."

    "I’m just going to go inside."

    scene black
    with dissolve
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene utaiobath1
    with dissolve2

    s "..."

    "There’s no one here. "

    s "..."

    "I’m alone in Uta and Io’s room and there is no one here."

    s "..."

    "I can do anything I want."

    scene black
    stop music

    "I can do anything I want."

    play sound "static.mp3"
    scene utaiobath2 with flash
    stop sound
    play music "ame.mp3"

    u "{i}Hah...{/i}I really needed this. Between all that extra course work and the time I’ve been putting into archery, my back and my head are friggin’ killing me."
    u "Having a best friend who works at a bath house is something everybody needs to put on their to-do list. This is the life, Io. This is the life."
    i "It is certainly {i}a{/i} life, Uta. But this particular bath house girl is all booked up on friends, so “everyone else” is going to have to look elsewhere for their free bath benefits."
    i "Or, you know, just bathe at home and leave people like me out of the equation altogether."
    u "Your anti-socialness is ruining my bath. If you’re going to talk, keep it to stuff like, “You’re the best, Uta!” Or, “You’re so pretty and your grades are going to get better soon and everyone will love you!”"
    i "If grades had any impact on how much a person was liked, Nodoka would have more people to talk to than the fat girl and her lesbian companions."

    scene utaiobath3
    with dissolve

    u "That was mean. What has Futaba ever done to you?"
    i "Nothing. And that did sound rude. I just forgot her name and wasn’t sure what else to call her."
    u "The nice one? The one who’s always reading? The library girl? The one who smells like lavender all the time? Even just “Nodoka’s friend” would have been fine."
    i "Now you’re ruining {i}my{/i} bath. And you understood what I meant, so I don’t see what the big deal is."

    scene utaiobath4
    with dissolve

    u "The “big deal” is that we’ve been in Sensei’s class for over two years now and you’re still the same Io you’ve always been. Would it really kill ya to just not be mean to people until they do something to you?"
    i "Maybe. People have an easier time taking advantage of you once you start opening up to them. If I never do that, it greatly limits the opportunities people will have to ruin my life."

    scene utaiobath5
    with dissolve

    i "I’ve decided Miku is fine, though. She’s not as bad as I thought she’d be. Plus, I don’t think she’s smart enough to actually hurt anybody."
    u "Are you guys still hanging out? I kinda figured you’d have gotten fed up with her by now. She talks even more than I do."
    i "She does. But you two are a lot alike in a bunch of ways, so maybe I’m just...predisposed to dealing with that type of girl? "
    u "And...what type is that exactly?"

    scene utaiobath6
    with dissolve

    i "I don’t know. Loudmouth ex-tomboy looking to get in touch with her feminine side for reasons beyond Io-comprehension?"
    u "That’s a really specific answer for apparently not knowing."
    i "Yeah, I guess it is. "
    u "Also, I’m pretty sure Miku isn’t trying to abandon her tomboy side like I did. She’s just...also trying to do other stuff."
    i "You haven’t abandoned it either. You’re the ace of the kyudo club and you have a pet beetle. Those aren’t exactly the most “girly” traits out there, Uta."

    scene utaiobath7
    with dissolve

    i "I wouldn’t mind if you changed stuff like your wardrobe or the music you listen to, though. That would be the ideal setup for me."
    u "There’s a problem with my wardrobe now?"
    i "Too many bright colors. And like half of your bras have hearts on them. I don’t get it."
    u "You don’t get it because you’re anti-cute and don’t even {i}wear{/i} a bra half the time. "

    scene utaiobath8
    with dissolve

    i "Why {i}would{/i} I? It’s not like I’ve got anything to keep in check. The only reason I wear one with my uniform is because it’s uncomfortable if I don’t. But if I’m at work or home or something, what’s the point?"
    i "What I fail to understand is why you need hearts or strawberries or other stuff like that on your underwear unless you’re showing it off to other people. Which-"

    scene utaiobath9
    with dissolve

    i "Wait. Nope. Gonna just catch myself right there and clarify that I wasn’t insinuating what it sounded like I was insinuating. That was, like...a generalization. Not a specifically-tailored Uta-based comment on-"
    u "I know what you meant. Besides, it’s not like I even have the liberty to show anyone {i}anything{/i} now that my phone’s locked."
    u "If I wanted to do that, it’d have to be in-person, and that’s...kind of...yeah."
    u "I just like feeling cute. That’s really what it comes down to."
    i "Uta...I’m sorry. You know I’m bad at thinking before I speak and I wasn’t trying to bring that up right-"
    u "You know...it’s kind of good that you did, though."

    scene utaiobath10
    with dissolve

    i "Uh...{i}why{/i} is it good that I did?"
    u "Because if you didn’t, I’d have to."
    u "I got another one the other day. From another different number."

    scene utaiobath11
    with dissolve

    i "Seriously?..."
    u "And I don’t even remember taking this one."
    i "How does this keep happening? Your phone’s supposed to block all picture messages, isn’t it? Can’t you complain to the carrier or something?"

    scene utaiobath12
    with dissolve

    u "And say what? Hello, Mr. Verizon- somebody keeps sending me nudes I took of myself when I was a kid. Can you make it stop, please?"
    i "You don’t have to be that...direct about it. "
    u "It’s fine. I’ll just get another new phone. That normally stops it for a month or two."
    i "What if you just, like...stop using a phone altogether?"
    u "In 2020? How would I keep in touch with my parents? Carrier pigeon?"
    i "You could use {i}my{/i} phone to call them. And all of your friends live in the same building, so it’s not like you’d be missing out on contact with any of {i}them.{/i}"
    u "Something tells me doing that would just end up with {i}you{/i} getting those pictures instead of me. And that’s not a thing I want for either one of us."

    scene utaiobath13
    with dissolve

    i "Ugh...how many is that this month?"
    u "..."
    u "Nine...I think."
    u "Five if we’re not counting duplicates."
    i "God fucking damn it. Maybe it really {i}is{/i} time for a new phone then. That’s way more frequent than normal."
    u "It sure is..."
    i "Whoever is doing this to you is fucking disgusting, Uta. I’m sorry you keep having to deal with it."
    u "As long as nobody else finds out, it’s...it’s fine, I guess. It’s obviously not like I haven’t seen myself naked before, so...yeah."
    i "Fucking...ugh. Literally nothing good ever comes from {i}anything{/i} sexual. It’s all just fucking gross and creepy."
    u "I’m sorry for being gross and creepy, Io. I’ll try to do better in the future."

    scene utaiobath14
    with dissolve

    i "That’s not what I-"
    u "No, you’re right. All of this started because I couldn’t keep my stupid feelings in check, and now I have to deal with it for the rest of forever because I’m a disgusting pervert who bit off more than she could chew."
    i "Uta..."

    scene utaiobath15
    with dissolve

    u "Even today, I’m {i}still{/i} like that. And I’d probably make the same stupid mistakes if I had never gotten burnt the first time around. That’s who I really am, Io. I’m gross. And I’m creepy. And I’m fucking {i}sad.{/i}"

    scene utaiobath16
    with dissolve

    u "I am {i}so{/i} fucking sad, Io. "
    u "All I wanted was to feel cute and...pretty...and {i}wanted.{/i} But I was none of those things and just the fact that I {i}wanted{/i} them wound up ruining my brother’s life {i}and{/i} mine. "
    u "No one’s going to ever want me. Like, {i}really{/i} want me. They’re going to find out what I’m all about and just pivot to thinking I’m a whore who chases after older dudes to feel validated. "

    scene utaiobath17
    with dissolve

    u "Like, {i}look at me.{/i} I work at a maid cafe. I basically get paid to make people think about having sex with me. And the more they want it, the more I make. But that’s {i}all{/i} they really want."
    u "The second it’s Uta and not Uta-{i}chan,{/i} it’ll all come crashing down because {i}Uta{/i} is a failure. She gave away her pride for temporary bliss, and now she’s got nothing left to give."
    u "I am so fucking sad. "

    scene utaiobath18
    with dissolve

    u "{i}I am so fucking sad.{/i}"
    i "I’d hug you if we weren’t naked right now..."

    scene utaiobath19
    with dissolve

    u "{i}Hah...{/i}that felt good to get off my chest. It’s been a while since I’ve had my very own Io-style self-loathing session."
    i "Well, it didn’t feel good for me. I hate hearing you talk about yourself like that. And I hate that my inability to properly word things is what ultimately led to that happening."

    scene utaiobath20
    with dissolve

    u "It was coming sooner or later, Io. It wasn’t your fault. Just have to...reset or something."
    i "Listen, this..."
    i "I know I’ve said this a million times before and...I know you probably don’t believe me because, if you did, we wouldn’t keep coming back to it...but you’re wrong."
    i "You’re {i}so{/i} wrong."
    i "Someone is going to love you for real one day because you’re amazing and strong and the fact that you’re able to put on a brave face after all that’s happened and {i}still happens{/i} to you is {i}insane.{/i}"

    scene utaiobath21
    with dissolve

    i "Sex is...it’s not as...I get that I look at it differently from most people. And I get that {i}I’m{/i} the one who’s weird for doing that, not you. You’re totally normal and not creepy or gross at all."

    scene utaiobath22
    with dissolve

    i "And if someone as fucking backwards as {i}me{/i} can see that about you, someone else obviously will."
    u "Io..."

    scene utaiobath23
    with dissolve

    i "In summation, I am very clearly not a person who has the right to tell {i}anyone{/i} to stop self-deprecating when that very trait is roughly 50%% of my personality."
    i "But Uta, if I ever hear you talk down on yourself to that extent again, I am going to slap you so hard that you’re going to forget that naked pictures of you were ever leaked in the first place."
    u "Well, damn. If you have that power, just hit me now. "

    scene utaiobath24
    with dissolve

    i "If I really did have that power, you know I would."
    i "You’re the only person I’d do anything for, Uta. I mean that."
    u "Maybe a couple years ago, sure. But you’ve got Sensei now. It’s not {i}just me{/i} anymore."
    i "I wouldn’t do anything for Sensei. If I would, there’d be no need for a throuple in the first place since I could just take one for the team and let him violate me."
    u "This conversation’s about to get weird, isn’t it?"

    scene utaiobath25
    with dissolve

    i "I’m telling you- it really {i}is{/i} the best option for everyone. Plus, you probably wouldn’t think of yourself as such a pervert anymore if you were standing next to Sensei all the time as his powers far surpass yours."

    scene utaiobath26
    with dissolve

    u "Calling them “powers” is all sorts of wrong when they are actively making my life a living hell."
    i "He could love the real you too, Uta. I know he could. Like, he puts up with {i}me{/i} and I’m infinitely worse than you are."
    i "Maybe that’s what you’re missing? Or just...not understanding, I guess."
    u "You’ve got that right, Io..."
    i "No, listen. It’s like...I know he could love you because it’s the broken people like us who work the best together."
    i "When you’ve got nothing left to give, natural instinct is to {i}take,{/i} right? And who better to take from than someone who doesn’t realize how much they actually have?"

    scene utaiobath27
    with dissolve

    i "Both of you are like that. You think you’re all washed up and unworthy of anyone’s feelings, so you flail and you fumble until you’re so desperate for companionship that you’re talking to people like {i}me.{/i}"
    i "That’s probably why I fell for him in the first place. Like {i}really{/i} fell for him. Because I saw pieces of you in there and they made me feel at home."
    i "At the end of the day, I can want and wish and hope for his approval until I’m old and gray..."
    i "But I think {i}you two{/i} would be a far better match than he and I ever would."

    scene utaiobath28
    with dissolve

    u "Just because...we’re perverted? And broken and sad and stuff?"
    i "Because I think you complement each other well. And that you can fill each other’s voids in a way that nobody else I’ve come across really can."
    i "Though, I also won’t deny that part of it might be because I can’t imagine anyone ever complementing {i}me{/i} to that extent. I’m probably just better off alone, all things considered."
    i "To be honest, if you actually {i}did{/i} have feelings for Sensei, my biggest fear would probably become the two of you leaving me since I know I’d have no purpose anymore."
    u "How could I leave you alone at this point in our lives? I need you just as much as you need me."
    i "But wouldn’t having someone else ease that burden a little? It’d be like walking with two crutches instead of just one. We could all lean on {i}each other.{/i}"
    u "..."
    i "Also, if you {i}really{/i} spend as much time thinking about all of that “physical” stuff as you say you do, you might actually be able to sate his {i}appetite.{/i}"

    scene utaiobath29
    with dissolve

    u "..."
    i "That’s just my opinion, though."
    u "You..."
    u "You’ve really thought this through, huh?..."
    i "It’s less “thinking it through” and more just a vibe. But the best outcome is never what either one of us ends up with, so this will probably always just be a pipe dream of mine."
    i "If your feelings ever change, though...and you {i}do{/i} start to see Sensei in the same light that I do..."

    scene black
    with dissolve2

    i "Don’t let me be the barrier between you."
    i "Because I know you."
    i "And I know you would. "

    $ renpy.end_replay()
    $ utadorm40p1 = True

    jump utadorm40p2

label utadorm40p2:
    if _in_replay:
        play music "ame.mp3"

    scene clearnightsky
    with dissolve2

    "Apparently, what I meant earlier by “I can do anything I want” is “I can stand around and feel awkward while waiting for one of the room’s two tiny inhabitants to return.”"
    "As you may be able to tell by another contemplative walk home, neither one of them ever showed up. So now, there’s nothing left to do but put an end to this night the only way I know how."
    "By vigorously masturbating in the blue glow of my computer’s light while wondering what has become of me and where I could be if I’d actually apply myself."
    "Maybe Wakana is onto something. Maybe I {i}should{/i} start writing again."
    "I mean, it’s not like I haven’t {i}tried.{/i}"
    "I {i}wanted{/i} to submit something for her stupid contest. Just...none of it felt right."
    "And it’s highly probable that nothing will {i}ever{/i} feel right again because I’m not the same person I was back then."
    "Or at least I think I’m not."
    "I’m not really sure."
    "Looking back at the past is kind of difficult when the universe itself is constantly pulling the wool over your eyes."

    scene utanightdate1
    with dissolve2
    stop music fadeout 15.0

    "My efforts are more focused on the future for now."
    "It’s easier to see."
    "And there are things there I’ve yet to experience. Things I {i}want{/i} to experience because, like any other creature, I’m entirely and helplessly incomplete."

    u "Ah..."

    "But maybe there’s someone out there-"
    "Someone unexpected-"
    "Who can help complete me in a way no one else would ever anticipate."

    s "Well, if it isn’t Uta Ushibori."
    u "What...what are you doing out here? It’s kind of late, isn’t it?"
    s "I’m on my way back from your room."
    u "My room? But-"

    scene utanightdate2
    with dissolve
    play music "starvingtodeathoutofreachofthesun.mp3"

    u "Okay. Hold on one second, mister. I’m gonna need you to empty out your pockets so I can be sure you’re not going around and stealing more precious Uta-chan mementos to defile while Ami is asleep."
    s "I promise I did not take any of your underwear this time."
    u "I’m going to need a more specific promise, Sensei. Just saying you didn’t take any leaves open the possibility that I come home to a very sticky surprise in my panty drawer later."
    s "I didn’t do {i}anything{/i} inappropriate."
    u "Besides breaking into my room, you mean."
    s "Is it really “breaking in” if the door was unlocked?"

    scene utanightdate3
    with dissolve

    u "Hah...no. I guess it’s not."

    "(She’s wrong. It is.)"

    scene utanightdate4
    with dissolve

    u "Why go all the way over there, though? If you wanted to see me, you could have just called or something. I’ve already proven that I’m willing to drop my responsibilities for you. So it’s not like I’d say no."
    s "I’ve found that the element of surprise often triggers more interesting events in the past, but I’ll keep that in mind going forward."
    s "Better question, though. What are {i}you{/i} doing out this late?"

    scene utanightdate5
    with dissolve

    u "Coming back from the bath house. Me and Io wound up talking for a really long time, so she’s just going to sleep there when she’s done cleaning and {i}I{/i} am going to go home and be lonely."
    s "No. You’re going to hang out with me again."

    scene utanightdate6
    with dissolve

    u "What? I am?"
    s "Yes. I’ve decided."
    u "It’s the park scene all over again. How come you keep deciding my schedule for me lately?"
    s "Because you’re letting me. Why would I stop doing a thing I like when I don’t get anything out of putting an end to it?"
    u "I’m not saying I have a problem with it. We’ve just gone so long doing our back-and-forth act that the sudden switch to your assertive side is giving me butterflies."
    s "Platonic butterflies? Or butterflies that I’m supposed to ignore so your mind doesn’t start spiraling out of control like it did at the park?"

    scene utanightdate7
    with dissolve

    u "Rest assured, there will be no Uta spiral tonight. There was enough of that at the bath house and I kinda hoped I’d be able to just put all of my feelings on hold until tomorrow morning."
    s "Should I just...leave you alone then?"

    scene utanightdate8
    with dissolve

    u "Honestly? You probably should."
    s "Then-"
    u "But..."
    s "..."
    u "Uh..."
    u "I...um..."

    scene utanightdate9
    with dissolve

    u "I feel like I’ll really regret it if I...don’t take you up on your offer tonight..."
    u "Even if that offer was...more of a command than anything else."
    s "You “feel like you’ll regret it?” Correct me if I’m wrong, but weren’t you trying not to {i}feel{/i} anything just a few seconds ago?"
    u "Yeah, and then you had to go and ruin that by showing up when I least expected. "
    u "I swear, you have either the worst or the best timing ever. I can’t figure out which one it is."
    s "I’m not really sure if I get what-"

    scene utanightdate10
    with dissolve

    u "You don’t have to be sure of anything, just..."

    scene clearnightsky
    with dissolve2

    u "Just take me somewhere no one will see us..."

    "Of course, a million different things run through my head the moment she says that. "
    "But, as desperate as I am for it to mean what I want it to mean, something about the tone of her voice and its mild tremolo tells me there’s more to it than that."
    "The thing is, those same qualities tell me that if I {i}do{/i} follow through..."
    "If I {i}do{/i} take her somewhere we can be alone...in the context that {i}I{/i} want..."
    "She’d likely give in."
    "She might {i}want{/i} to give in. And making me grab the reins might just be her forcing me to take the first step so she doesn’t have to."
    "But it might be a test as well."
    "It might be a trap."
    "If I were to take her hand and follow my heart down streets dyed red, I wonder what would cross her mind."
    "I wonder if, somewhere between the clouds of cigarette smoke in a neon-pink lobby and the incense that attempts to mask it, what her last words would be before we turn the key."
    "I wonder if she’d close her eyes when we kiss."
    "If she’d wait for me to touch her first, or if she’d get too caught up in the moment and touch {i}me{/i} instead."
    "I wonder if she’d smile. Playfully bite my lip. Ask me to “mess her up” with her cheeks flushed red and her eyes halfway closed."
    "But among that garden of pleasant thoughts, there’s one {i}un{/i}pleasant one."
    "It whispers to me that the flowers here are not done blooming yet- and that one wrong step could spell their end."
    "And so I am left with the choice to immerse myself in their unfinished beauty and risk destroying them..."

    scene utanightdate11
    with dissolve2

    "Or to come back when they’re stronger and brighter."
    "When they can put up with being trampled for a little while."
    "It’s hard walking away from something so beautiful...so {i}entrancing.{/i} But I dilute the difficulty with the idea that I’m walking toward something {i}else{/i} instead."
    "I’m trading one night for thousands. {i}Millions,{/i} maybe. "
    "Because taking her anywhere but here would do nothing but show her I’m exactly what she fears the most."
    "That I’m one more person who cares more about getting her into bed than waking up beside her."
    "And you know what? Maybe I am. "
    "But if believing I’m not can ease the ever-growing burden placed on her shoulders all those years ago, fuck it. "
    "I can suffer another night of self-pleasure if it means that Uta can gain a little more confidence in the way she approaches me, because I {i}know{/i} she’s getting there."
    "And I {i}know{/i} how hard she’s trying {i}not{/i} to."
    "And I don’t want to give her an excuse to turn back around."
    "I want {i}her{/i} to lead {i}me{/i} down streets dyed red. I want {i}her{/i} to turn the key. To push me down onto some cheap, vibrating mattress."

    u "Have you been here before, Sensei?"

    "And none of that will happen if I don’t let her bask in the light a little longer."

    s "Nope. In fact, I have absolutely no idea where we are. I just followed a sign that said “outlook.”"
    u "Well, we are certainly looking out. "
    s "That we are, Uta. That we are."
    u "Do you like stuff like this, Sensei? Stargazing and nature and all that."
    s "Not really, no."
    u "Yeah, I didn’t think so."
    s "Do you?"
    u "Mmm...nature is fine. I like being outside. The stars and sky and stuff are kind of boring though."
    s "It appears that I have failed you."
    u "Hahah! No, you haven’t failed me. I asked you to take me somewhere we can be alone and that’s exactly what you did. This is nice."
    u "Plus, just because neither one of us is particularly into stargazing doesn’t mean that we can’t acknowledge that the sky is kinda pretty like this, right?"
    s "Yeah, I guess you’ve got a point there."
    u "Tch. That was your cue to say, “But it’s not nearly as pretty as you, Uta. The stars aren’t even half as bright as your smile.” Or something like that. Way to go."
    s "I think we both know that you’d just laugh if I actually said something like that."
    u "It depends on the mood, I think. There’s not really a better time than this to say corny stuff like that, don’t you think?"
    u "It’s just you and me...in the middle of the night...down a winding path with no one else around..."
    u "This sort of thing would be super romantic if I wasn’t just your rental-girlfriend."
    s "Ah, yes. The girlfriend I rented for the large sum of zero yen."
    u "Teacher discount. Valid until I graduate. Just make sure to leave me a good review."
    s "Seems I’m a repeat customer for basically everything you do, huh?"
    u "Yeah, but that’s not really impressive since I only do two things and one of them is just an inside joke."
    s "Sorry, I guess that line wasn’t direct or flirty enough to hit your romantic criteria. What I really meant to say is “I’ll follow you to the end of the earth.”"
    u "Where does the earth even end?"
    s "Okay, I guess I’m just not good at this. Which, to be fair, is exactly what both of us expected."
    u "Heheh...no, that one was fine. I’m just being a brat."
    s "Yeah, what else is new?"
    u "..."
    s "..."
    u "..."
    s "..."
    u "Soooo...."
    s "So..."
    u "Stars. Am I right?"
    s "Stars, indeed. I have no idea what Maya sees in them."
    u "Ah! No talking about other girls on a secret rendezvous. That’s against the rules. "
    s "Well, how else am I going to continue a conversation on a topic I know nothing about? You had a million options for something else to choose and you went right back to a thing we’re both not interested in."
    u "There’s gotta be something! Like..."

    scene clearnightsky
    with dissolve2

    u "Like...what’s your favorite constellation?"
    s "..."
    u "..."
    s "Probably..."
    s "The Summer Triangle."
    u "Ooooh. Romantic."
    s "It’s the only one I know anything about."
    u "Altair and Vega, right? I remember that story from some camp thingy I went to when I was little. It’s actually pretty sad when you really think about it, isn’t it?"
    s "The Altair and Vega story? Or the fact that you used to go camping?"
    u "Hey! There’s nothing wrong with camping. Like I said, nature is fine. Besides, it was less of an actual “camping” thing and more of just a way for kids to meet and play with each other and stuff."
    u "The sky was really nice in Nara, though. It felt...bigger."
    s "Yeah, well, Nara didn’t have the same level of light pollution we have here. The urban district’s effect probably covers all of Kumon-mi."
    u "You think so? I think the sky looks pretty clear some nights."
    u "It doesn’t happen all the time, but...tonight for example. This is beautiful."
    u "It’s just not Nara."
    s "You really miss it there, don’t you?"

    scene utanightdate12
    with dissolve

    u "Sometimes, yeah."
    u "I like being close to the city. But every once in a while, there’s a night like tonight where I think it’d be nice to be somewhere a little more peaceful."
    u "It’s harder to relax over here, you know? There’s always something going on. Especially in the dorms since there are friggin’ twenty of us."
    u "Sometimes, I just miss my old futon. And the way my nightlight lit up the shoji whenever I went to sleep. And the fifteen deer who lived in our living room."
    s "I feel like that last one is an exaggeration even by Nara standards."
    u "What would you know? You’ve never been there."
    s "I’ve never had a reason to go."

    scene utanightdate13
    with dissolve

    u "..."
    s "..."
    u "Do you want one?"
    s "I have no interest in meeting your parents, Uta."
    u "We don’t have to go when they’re around. It can be just you and me."
    s "Is this about that “Uta-sanctioned tour” or whatever it was you mentioned last time we talked about this?"
    u "Mmm...yes and no."
    u "There would obviously still be a tour. Just my reasons for inviting you are a little different from wanting to show you more about me now."
    s "Different how?"

    scene utanightdate14
    with dissolve

    u "I’d tell you, but I’d have to kill you."
    s "Then kill me. I want to know."
    u "Are you sure? If you die, you’ll never get to meet the council of living room deer and trade them a piece of oak bark in exchange for eternal life."
    s "Nara sure has some strange customs."
    u "If only Grandpa had some oak bark..."
    s "And here we go again."

    scene utanightdate15
    with dissolve

    u "Hmhmhm...ahahah! Hahahah!"
    s "I’m glad that {i}you’re{/i} at least getting a laugh at how uncomfortable you make everyone whenever you bring your grandfather up."
    u "It’s not that! It’s not that..."

    scene utanightdate16
    with dissolve

    u "I just..."
    u "Um..."

    scene utanightdate17
    with dissolve

    u "..."
    s "Uta?"
    u "I’m really stupid, Sensei."
    s "I know that already."

    scene utanightdate18
    with dissolve

    u "You only know half of it and it’s not the half I’m talking about."
    s "Well, then tell me the half you’re talking about or I’m just going to keep accidentally insulting you."
    u "I-"
    s "Even if you have to kill me afterward. It’s fine."

    scene utanightdate17
    with dissolve

    u "Hahah...fuck. "
    u "Fuck fuck fuck fuck fuck."
    s "I agree. Good talk."

    scene utanightdate19
    with dissolve

    u "Sensei, I..."
    u "You..."

    scene utanightdate20
    with dissolve

    u "Us?..."
    s "Wow. You’re really bad at this."

    scene utanightdate21
    with dissolve

    u "Shut up! I want to do {i}this{/i} more often! That’s what I wanted to say!"
    s "Is that {i}all{/i} you wanted to say?"
    u "No! But just that was hard and it’s all I {i}can{/i} say right now!"
    s "Uta-"
    u "No, listen! I..."
    u "You’re..."

    scene utanightdate22
    with dissolve

    u "Mngh..."
    s "..."
    u "..."
    u "Like I said earlier...me and Io talked about a lot of stuff tonight....And you were one of the things we talked about."
    u "I still don’t...I don’t fully get what it would be like for all three of us to be a {i}thing{/i} and...that’s not something I’m really...uh..."
    u "Anyway, there was...there was something she said to me about how...how she sees the two of {i}us.{/i} And how she thinks we’d...um..."
    s "She thinks we’re a good match, doesn’t she?"

    scene utanightdate23
    with dissolve

    u "Sensei, when I’m with you...it’s like..."
    u "It’s like there’s a {i}third{/i} Uta. "
    u "It’s not just Uta and Uta-chan anymore, there’s like...a broken one too. Or a...{i}more{/i} broken one, I guess. "
    u "And all she does is wonder what you’re thinking of her and whether or not she’s saying the right stuff or..."
    u "Or just...trying to make you laugh. Or smile...Or {i}like{/i} her...and I don’t know how to make it stop."
    s "Do you {i}want{/i} it to stop?"
    u "{i}No.{/i} Because having all of those things going crazy inside of my head stops me from thinking about all the stuff I hate about myself."
    u "But at the same time, I’m worried {i}you’re{/i} going to hate me. And Io says you won’t, but-"
    s "Io’s right. I won’t."
    u "But what if you change your mind? "
    u "My...{i}situation...{/i}"
    u "It wasn’t just one picture...and it wasn’t just one {i}guy{/i} either. I don’t think I made that...clear last time."

    scene utanightdate24
    with dissolve

    u "It was the one guy who took things too far, yeah...but...there were others {i}before{/i} him. And they could still {i}have{/i} pictures of me that I don’t even {i}know{/i} about."
    s "You don’t have to-"

    scene utanightdate25
    with dissolve

    u "No, I {i}do{/i} have to tell you this because I don’t want you to waste your time on someone who isn’t worth it! And I don’t want to get my hopes up just to have you leave when you realize what I am!"
    s "You’re {i}not{/i} what you think you are."
    u "No, I’m not what {i}you{/i} think I am! "
    u "I’m not just some girl who made {i}one{/i} stupid decision when she was little and wound up getting screwed over! I made a million of them! And I {i}liked{/i} it!"
    u "And...and I’d probably {i}still{/i} like it if it never came back and bit me in the ass! Like, who even knows what I’d be doing now if that never happened?!"
    s "But it did happen. And it changed you."

    scene utanightdate26
    with dissolve

    u "Except it {i}didn’t{/i} change me. The only thing it changed is who I’m in contact with and how reluctant I am to let anyone in. I’m still the same filthy pervert I was back then, I just keep it to myself now."
    s "So...if I were to have taken you back to a love hotel tonight instead of here, what do you think would have happened?"

    scene utanightdate27
    with dissolve

    u "I think..."
    u "I think I probably would have made another bad decision..."
    s "Would you have liked that more than {i}this?{/i}"

    scene utanightdate28
    with dissolve

    u "Huh?..."
    s "Would you have preferred we did that? Or are you happy we came here instead? "
    u "I..."
    s "To be honest, I wanted to take you to a hotel. It was the first thing I thought of."
    u "Then...why would you..."
    s "To show you that there’s more to you than just that — which is something I’m pretty sure you’re aware of, yet you keep bringing your past to the forefront because, like you said-"
    u "I’m reluctant to let anyone in..."
    s "Bingo."

    scene utanightdate29
    with dissolve

    u "..."
    s "..."
    u "I’m really happy we came here instead..."
    s "I knew you would be. That’s why I did it."
    u "Ugh...damn it, Io. How come you’re always so wrong when it comes to yourself, but you hit all the nails with {i}my{/i} name on them right on the head?"
    s "She {i}is{/i} a builder after all."
    u "Does my past really not gross you out, Sensei?"
    u "Did I not...make it clear enough just how young I was when all of this happened?"
    s "I’m not concerned about the past. I’m more focused on spending time with the two- or apparently {i}three{/i} Utas I have here right now."
    u "And if one of those Utas starts to want more from you than you’re able to give...what then?"
    s "I’ll just take something from {i}her{/i} to make up for it."
    u "And if {i}she{/i} doesn’t have anything to give?"
    s "Then she’s probably just not looking hard enough."
    u "..."
    s "..."
    u "..."
    s "Are you regretting your choice to hang out with me tonight yet?"

    scene utanightdate30
    with dissolve

    u "I would never."
    u "Are you regretting inviting me?"
    s "Nope. All good here."
    u "That’s reassuring."
    u "Do it more often."
    s "Do what? Invite you out?"
    u "Yeah."
    u "Spend all of your free time on me from now on."
    u "Every single second of it."
    s "Is my money not enough?"
    u "You can keep your money. What I really want is {i}you.{/i}"
    s "Can I take that as an official confession?"

    scene black
    with dissolve2

    u "Not yet."
    s "Well, how long am I going to have to wait for one? Because all signs within a ten mile radius point to you having feelings for me."
    u "Feelings? What are those? I thought I said I was done with them tonight."
    s "That was like three hours and three hundred feelings ago."
    u "Three hours? There’s no way it’s been- oh my God, it’s been three hours."
    s "Do you need to start heading back?"

    if day == 5 or day == 6:
        u "Mmm...nah. We don’t have school tomorrow. I’ll be fine."
    else:
        u "Am I going to get in trouble for sleeping in class tomorrow?"
        s "Do you ever? "
        u "Good point."

    u "Another hour wouldn’t hurt..."

    stop music fadeout 10.0

    "One hour becomes two."
    "Then two becomes three."
    "And before I know it, my walk back home is illuminated by the glow of the rising sun."
    "I met another match tonight."
    "I hope I’ll see her again tomorrow."

    $ renpy.end_replay()
    $ utadorm40p2 = True
    $ uta_love += 5

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
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

label utaspring1:
    stop music fadeout 5.0
    scene black
    with dissolve2

    "{i}Meanwhile...deep within the beating heart of Kumon-mi...{/i} "
    "........."
    "......"
    "..."

    scene amimaidreturn1
    with dissolve2
    play music "normalday.mp3"

    a "I sincerely apologize for being away for so long!"
    a "And also for maybe saying a few things about how I would take your organs!"
    a "Please let me work here again! I need money!"
    u "Ami, calm down! You don’t need to bow! It’s okay! We didn’t hire anyone in your place!"
    c "No, but we probably {i}should{/i} have. She’s been gone for months and the customers have barely even noticed."
    a "That’s only because Uta is super good at her job and steals all of the regular customers! But you’re right! I don’t deserve to be here anymore!"

    scene amimaidreturn2
    with fade

    u "Chika, come on. Ami’s technically your senpai, you know. And she’s been going through a really tough time lately. We need to be {i}understanding{/i} in her time of need."
    u "For example, when my grandpa was dying of brain cancer-"
    c "Blah, blah, blah. My mom died too and you don’t see me using that as an anecdote to explain away all of the times I’ve had to stick up for Yumi. Save the dead grandpa card for when it’s needed or it’ll lose its impact."
    os "I don’t mind if Ami comes back. She can handle some of the cooking again since I had to pick up the slack for her."
    a "Of course! I’ll do anything!"

    scene amimaidreturn3
    with dissolve

    c "Really? Then surrender Sensei to me. Platonically, of course. I just don’t feel comfortable with him being in the hands of a psychopath."
    os "You too? Really?"
    a "I will do {i}almost{/i} anything! Sensei has to stay with me or we’ll both burst into flames! It’s part of the Arakawa family curse!"
    u "I would like to exercise my seniority here to remind Chika that she’s still technically the newest employee. Even if she {i}has{/i} managed to build up a bit of a following in Ami’s absence."

    scene amimaidreturn4
    with dissolve

    a "Wait, really? How? I’ve been here way longer and no one’s ever asked for me who I’m not already friends or relatives with."
    c "What can I say? I’m just better than you. It’s as simple as that."
    u "It’s not as simple as that. Chika caters to two demographics at once between her being half-Filipino and also a gyaru. "
    c "{i}Former{/i} gyaru mostly. I’m a cool rocker chick now."
    u "And also, since you sucked at being tsundere, you were checking the same boxes that {i}I{/i} check but at a much lower rate. You’ll never steal cute-type customers away from Uta-chan. That’s impossible."
    a "Well...what am I supposed to do now? Because I can’t put myself in twintails anymore and Osako already caters to the customers looking for a boyish maid."

    scene amimaidreturn5
    with dissolve

    os "Hey!"
    u "We just need to reinvent you!"
    c "Or you could find another job. Les Vetements might be hiring a replacement for me soon if they’re still there after the mall is finished being renovated."
    u "Ignore Chika. She’s just upset that she won’t be able to cover your shifts anymore and is going to slip back into poverty."

    scene amimaidreturn6
    with dissolve

    c "Hey!"
    u "It doesn’t matter who you are or what you want to be, Ami. What matters is that you’re back. We can figure out your new archetype over your next few shifts. "

    scene amimaidreturn7
    with dissolve

    u "But for now — we’ve got a show to run, ladies! Fix your clothes! Fix your makeup! Then get on out there and show our guests a good time! "
    u "Just not {i}that{/i} kind of good time because this isn’t that kind of place!"
    c "Fine. But Ami’s SOL if she didn’t bring her uniform with her since we don’t have any extras."

    scene amimaidreturn8
    with dissolve

    u "She’s not gonna work today anyway. I’ll have her start again next weekend or something. "
    u "For now, just let me go over some of the stuff that’s changed with her while she’s been gone and I’ll get back with you and Osako-chan in a sec. Think you can hold down the fort?"
    c "I’m sure we can figure it out."

    scene black
    with dissolve2

    c "Come on, Osako-chan. Let’s leave Uta alone with the gremlin and hope that she isn’t eaten alive."
    os "There isn’t going to be any sort of drama in here from now on, is there? Because I’ve kind of enjoyed how peaceful things have been lately."
    c "Beats me. Ami’s the one you want to ask."
    u "That’s Ami-{i}chan{/i} to you!"
    c "Not while she’s not in unifoooooorm!~"
    u "Out! Be gone! Vanish!"

    "........."
    "......"
    "..."

    scene amimaidreturn9
    with dissolve2

    a "Thanks a lot for sticking up for me, Uta..."
    a "You really didn’t have to do that after I was so mean to you when you...well...broke into my house..."
    u "Relax! And let’s not talk about anything either one of us may have done that may or may not have been illegal!"
    u "I’m glad you’re back, Ami. I like your hair."

    scene amimaidreturn10
    with dissolve

    a "Do you really? Sana’s mom did it when we were camping the other day. You don’t think it’s a little too masculine?"
    u "Maybe a little bit, but I think you can pull it off. And I’m not just saying that because no one would be able to tell that you’re a girl from fifteen to twenty feet away."

    scene amimaidreturn11
    with dissolve

    a "Please don’t remind me. I’m dealing with enough as-is right now. The last thing I need is even more breast envy."
    u "Don’t feel bad! Mine were small once too!"

    scene amimaidreturn12
    with dissolve
    stop music fadeout 5.0

    u "But I guess you already know that since you saw my pictures in Sensei’s phone!"
    a "..."

    scene amimaidreturn13
    with dissolve

    a "Ahh, crap."
    u "Mhm. We’re gonna talk about this now."
    a "I know...I completely forgot about those until you said something."
    u "That’s perfectly fine! Because I’ve been waiting a really long time for you to not be completely miserable so I can tell you all about how that made {i}me{/i} feel!"

    scene amimaidreturn14
    with dissolve
    play music "hometown.mp3"

    a "Nothing has changed here while I’ve been gone, has it?"
    u "We have a new parfait. Orientation done. Now, about those pictures!"
    a "What do you want to know? You’ve always been nice to me, so I have no reason to lie to you."
    u "How many were there? What was I doing in them? Did he send them to anyone else? Are there copies? Does he still have them? Did you delete them? Did he say anything about them?"
    a "Do you have a preference on...which one of those I answer first?"
    u "Maybe answer this one instead and we can go from there."
    u "What kind of girl do you think I am, Ami?"

    scene amimaidreturn15
    with dissolve

    a "What kind of...girl?..."
    u "Yeah. "
    u "Like, I’m sure you think {i}I{/i} sent that stuff to him, don’t you? Which would mean you think I’m probably a desperate whore or something along those lines, right? "

    scene amimaidreturn16
    with dissolve

    a "I don’t know how he got them...but I can tell you weren’t the one who sent them based on how you’re reacting to this."
    u "What kind of girl do you think I am, Ami? Answer the question."
    a "..."
    u "You really {i}do{/i} think I’m just a thirsty slut, huh?"
    a "No, I..."
    u "Because I am."

    scene amimaidreturn17
    with dissolve

    a "..."
    u "I took all sorts of pictures like that when I was younger, you know. Sent them to tons of guys...didn’t even get anything in return most of the time, but I was okay with that."
    u "Doing those things made me feel wanted. They made me feel {i}pretty.{/i}"

    scene amimaidreturn18
    with dissolve

    u "And I was still learning how my body worked, so I did {i}tons{/i} of self-exploring back then, if you catch my drift."
    a "Uta..."
    u "And I mean {i}tons.{/i} Several times a day. It was kind of like an addiction. But I’m sure you know how it is, right?"
    u "I’m sure you got a little too handsy with yourself once {i}you{/i} realized how to make yourself feel good. Right?..."
    a "..."

    scene amimaidreturn19
    with dissolve

    u "Not much has changed on that end, to be honest. "
    u "I still do it all the time. Still spend way too many hours with my mind in the gutter."
    u "But you know, Ami?...That’s exactly where I belong."

    scene amimaidreturn18
    with dissolve

    u "I can’t even make a {i}guess{/i} about how many guys must have jerked off to me when I was growing up. But I’m sure it’s a lot since those pictures have been following me {i}everywhere.{/i}"
    u "That’s why I {i}really{/i} moved, you know? Taking care of my grandpa was just a thing I also happened to do when I got here."
    u "But I wouldn’t be here at all if I wasn’t a needy, naughty girl who sought attention from the wrong people."
    u "One of them wound up stalking me. I guess the Internet wasn’t enough and he wanted a taste of the real thing. "
    u "But that didn’t last long since my brother caught wind of it and attacked him before he could lay his hands on me."

    scene amimaidreturn20
    with dissolve

    u "You think I would have done it, Ami? "
    u "You think I would have let some old guy fuck me back then? "
    a "I don’t know, Uta..."
    u "Me either. "
    u "And that’s what’s so fucking scary about it."

    scene amimaidreturn21
    with dissolve

    u "Even now...even though it terrifies me...makes me nauseous...and quite literally makes my life borderline unlivable sometimes, I {i}still don’t know.{/i}"
    u "Part of me {i}still{/i} gets excited thinking about that stuff. But then part of me wants to throw up and it all cancels out."
    a "You don’t think Sensei is...sending your pictures around, do you?..."

    scene amimaidreturn22
    with dissolve

    u "Probably not. But if there’s anything I know about older guys — and again, I know {i}a lot {/i}— it’s definitely safe to say he’s jerking off to them. And I know how that makes {i}me{/i} feel..."
    u "But how does it make {i}you{/i} feel? How has it changed the way you look at him? And how are you going to look at {i}me{/i} from now on knowing that I'm into it?"
    u "Can we still be friends? Am I in danger? What happens if those pictures aren’t enough for Sensei anymore? What if {i}he{/i} comes after me next? Then what, Ami? "
    a "..."
    u "Don’t hold back. I want to hear what’s on your mind. It’ll distract me from what’s going on in mine."

    scene amimaidreturn23
    with dissolve

    a "Nothing will ever change the way I look at Sensei. But {i}that...{/i}"
    a "That’s a part of him I’ve kind of...known about for a really long time."
    u "..."

    scene amimaidreturn24
    with dissolve

    a "I was the same when I was younger, Uta. Desperate to be {i}wanted.{/i} To feel {i}love.{/i} But the main difference between us is that my feelings were aimed at one person and yours were just...everywhere."
    a "So while you were sending pictures of yourself to people all over the Internet, I was touching myself in my uncle’s bed...hoping he’d wake up and have his way with me."
    a "Which one of us do you think is worse now?"
    u "..."

    scene amimaidreturn25
    with dissolve2

    a "You were really cute back then. I don’t blame Sensei one bit for touching himself to your pictures. I’m just a little jealous, that’s all..."

    scene amimaidreturn26
    with dissolve

    u "Jealous?..."
    a "Yeah..."
    a "I’ve seen the way he looks at you...the way you look at him...and that makes me want to tie him up and do all of the things that you’re too afraid to."
    u "Um..."
    u "This isn’t really...how I thought things would go when I told you about-"

    scene amimaidreturn27
    with dissolve

    a "It’s hard to predict how things will go...What...wrong decision or...{i}mistake{/i} we’ll make next..."
    a "Even when you think you know how things are going to play out...one wrong turn and everything gets thrown into chaos."
    a "I don’t blame you for what you did back then...or how it impacted who you are today..."
    a "Because the truth is, Uta..."
    a "I think you’re perfect."
    a "{i}That’s{/i} the kind of girl I think you are..."
    u "You..."
    u "N...No...I just told you all of those things about me. That’s...That isn’t perfect...It’s not even...close..."
    a "There’s a reason Sensei looks at you as much as he does...and it’s so...{i}so{/i} clear when I can see you up close like this..."

    scene amimaidreturn28
    with dissolve

    u "Ami...what’s going on?..."
    u "What are you doing?..."
    a "What do you {i}want{/i} me to do?..."
    u "I...um..."
    a "You feel it too, don’t you?..."
    u "I feel...a lot of things right now...but we haven’t really finished our conversation about..."
    a "Are you sure?...I think we did..."
    u "No...I need to know what you’ll do if..."
    a "If what?..."
    u "If...Sensei does something...when I confront him about this..."
    a "You’re gonna confront him?..."
    u "I can’t just...ignore this...I need to know...how he got them..."
    a "Will you let him touch you if he asks?..."
    u "Will..."
    u "Will you hate me if I do?..."

    scene amimaidreturn29
    with dissolve

    a "Will you let {i}me{/i} touch you if I ask?..."
    u "{i}You?...{/i}But...Wait a second...Hold on! Aren’t you straight?! Are you just messing with me right now?! You are, aren’t you?!"
    a "Are you nervous?..."
    u "Isn’t that obvious?! This isn’t how this conversation is supposed to go!"
    a "I’m sorry...you’re just..."

    scene amimaidreturn30
    with dissolve

    a "So cute up close..."
    u "Wha..."
    a "Uta..."
    u "..."

    if amifingered == True:
        a "Let’s be needy {i}together...{/i}"
    else:
        a "Let’s do for each other what {i}he{/i} won’t do for us..."

    stop music
    scene black

    u "I..."

    play sound "doorslam.mp3"

    u "{i}I’ve gotta get back to work!{/i}"

    play sound "static.mp3"
    scene amimaidreturn31 with flash
    stop sound

    a "Ah..."
    a "..."

    scene amimaidreturn32
    with dissolve2

    a "Well...that might make things a little awkward."

    play sound "static.mp3"
    scene amimaidreturn33 with flash
    stop sound
    play music "maidcafe.mp3"

    c "Oh, hey. How did your talk with Ami go?"
    u "We almost kissed."
    c "Cool. We’ve got a party of seven coming in at-"

    scene amimaidreturn34 with hpunch

    c "YOU WHAT?! "
    u "Uta-chan’s powers...work against her again..."
    c "You almost {i}kissed?!{/i} How?!"

    scene amimaidreturn35 with hpunch

    u "With our mouths, obviously!"
    c "I know that, idiot! But what could have possibly happened in the five minutes you were in there that led to that?! Weren’t you just teaching her about parfaits?!"
    u "I was teaching her about the long-term effects of trauma and how some nuts are easier to crack than others! "
    c "We’re selling nuts now?!"

    scene amimaidreturn36 with hpunch

    os "Can you two stop yelling?! We have customers in here!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    c "Uta almost broke the biggest rule of the cafe! And Ami definitely shouldn’t be allowed to work here anymore!"

    play sound "dooropen.mp3"

    a "Hi! Uhh..."
    a "Bye."

    play sound "doorslam.mp3"

    u "Oh my God. Did she look at me? I was looking away. Chika-chan! Did Ami look at-"

    play sound "slap.mp3"

    c "Get with the program, Uta-chan! We’ve got nuts to sell!"
    u "Aaaaah!!!!! What just happened?!?!?!?!"

    $ renpy.end_replay()
    $ utaspring1 = True

    "{i}Uta’s affection with Ami has...increased?{/i}"
    "........."
    "......"
    "..."
    "{i}Meanwhile...wherever Sensei is...{/i}"

    jump noonch4

label utaspring2:
    scene clearnightsky
    with dissolve2
    play music "ame.mp3"

    "I can do anything I want."
    "And for the most part, I have."
    "My life is a series of resets and repeats — one where I return to the same habits and hobbies I’ve blanketed myself in because I’m always in need of warmth. Always in need of {i}something.{/i}"
    "And right now, that something is air."
    "I’ve expelled my worries from the depths of my lungs in an attempt to envelop myself in happier days, but I’ve been left a step or two away from suffocating and must now replenish what I’ve lost."
    "I’m not sure how a blanket is going to help me in this case, though."
    "And while I’m trying a little harder than I have been to not immediately think of fashioning it into something I can hang myself with (for Ami’s sake), that’s the only thing that comes to mind."
    "The problem is, that puts me in quite the predicament as I’m now going to die in this metaphor no matter what I do considering my options are “hang” or “stop breathing.” Both of which are essentially interchangeable."
    "So for the sake of my life and your entertainment, please allow me to start all over."
    "I can do anything I want."
    "And for the most part, I have."

    u "Ah..."

    "So maybe tonight, I’ll reset or repeat something meaningful."

    scene utanaragain1
    with dissolve2

    "Maybe tonight, I’ll replay something I haven’t seen in quite some time — a silent, contemplative night with a younger girl that doesn’t end in sex."
    "We have been here before."
    "But that was before I knew that she knew something. "

    s "Well, if it isn’t Uta Ushibori."

    "That’s okay, though."
    "Because we both want to ignore it."

    u "What...what are you doing out here? It’s kind of late, isn’t it?"
    s "I’m on my way back from your room."
    u "My room? But-"

    scene utanaragain2
    with dissolve

    u "Hey, wait a second! Are you actually on your way back from my room? Or are you just repeating our dialogue from the last time we met like this?!"
    s "I’m surprised you remember that."

    scene utanaragain3
    with dissolve

    u "I’m surprised {i}you{/i} remember. Aren’t you supposed to have memory issues or something? Or is Uta-chan just so unforgettable that she’s exempt from them?"
    s "You’ve always been my favorite, after all."

    scene utanaragain4
    with dissolve

    u "By design, of course. Uta-chan is the result of painstaking research into the entire concept of cuteness. Your love for her is simply a byproduct of my hard work."
    s "Are you free again tonight?"

    scene utanaragain5
    with dissolve

    u "Heh..."
    u "It doesn’t really matter if I’m free or not. I don’t know how to say no to you."
    s "Technically, you’ve said no to me probably a thousand times now. You definitely know how."
    u "I’ve said no to sexy stuff because my chastity must be protected at all costs or humanity will collapse. I’d never turn down an invitation like this, though."

    scene utanaragain3
    with dissolve

    u "But I guess that doesn’t really matter since I’m free anyway."
    s "So you were just giving me the runaround out of habit?"
    u "Would you expect any less at this point?"
    s "Depends on which Uta I’m talking to. One of them is actually really nervous all the time."
    u "I’m pretty sure that one’s busy tonight. But Uta-chan can keep you company so long as you promise to keep your hands in the vehicle at all times."
    s "Are we just returning to our spot, then? Or did you want to try somewhere else tonight?"

    scene utanaragain6
    with dissolve

    u "It’s cute that you’d call it “our spot.”"
    s "That’s what it is, isn’t it?"
    u "Doesn’t change how cute it is."
    s "Is Uta-chan allowed to be so forward with her flirting? Or did you want to try and add a few more suggestive layers to those past couple sentences?"

    scene utanaragain5
    with dissolve

    u "It doesn’t matter how many layers there are when I’m just going to wind up shedding all of them for you no matter what happens."

    scene black
    with dissolve2

    u "Come on! Let’s head to our spot."

    "........."
    "......"
    "..."

    scene utanaragain7
    with dissolve2

    "So far, so good, I guess."
    "Uta seems a little off. But I imagine it’s hard {i}not{/i} being a little off when you’re alone in the dark with a man who could lift you up and carry you away without any effort at all."
    "I doubt tonight’s the night for that, though. "
    "And to be honest, I doubt I’ll even {i}have{/i} Uta-chan for much longer as its only a matter of time until we have to address the elephant in the gazebo."
    "If Io knows, Uta knows. "
    "And if Uta knows..."
    "I don’t know. "
    "I have no idea what she’ll do."
    "And based on her rare silence, I’m not sure she does either."

    u "So...what’s new, Sensei? How are things now that life is getting back to normal for you?"
    s "Horrible. But I have a daughter now, so that’s new."

    scene utanaragain8
    with hpunch

    u "You {i}what?!{/i} With {i}who?!{/i} And how do you just casually drop a bomb like that without even changing expressions?! "
    s "Relax. I’m just talking about Ami."
    u "You had a baby with Ami?! Is {i}that{/i} why she was acting so hormonal at the maid cafe the other day?!"
    s "No, Ami {i}is{/i} the daughter I’m referring to. We decided it’s best if she stops calling me her uncle and- wait, what do you mean “hormonal?”"

    scene utanaragain9
    with dissolve

    u "Nothing."
    s "Uta...if Ami is acting strange again, I need to know. I had a feeling she wasn’t ready to go back to work yet, but she’s been adamant about getting out of the house and-"
    u "Yeah, I don’t know what you’re thinking might have happened, but I can promise you it was something completely different."
    s "Different...how?"

    scene utanaragain10
    with dissolve

    u "Hey! Here’s a new topic! Have you seen Io lately?"
    s "..."
    u "...Sensei?"
    s "Why do you ask?"

    scene utanaragain11
    with dissolve

    u "Just...cause she’s been acting a little weird, that’s all. She’s staying over at the bathhouse more often than normal, so I wasn’t sure if something happened with {i}you{/i} or..."
    u "If maybe she's still upset about something {i}else{/i} that happened or..."
    s "I haven’t seen her, no."

    scene utanaragain12
    with dissolve

    u "Really?"
    s "Yeah. I’ve been too busy trying to get my life back in order."

    scene utanaragain13
    with dissolve

    u "Darn it. It’s probably just her stupid brain being a stupid brain again, then. "
    u "I keep trying to check on her, but she’s being really stubborn about dealing with stuff on her own this time."
    u "I just hope she doesn’t hurt herself. But if you don’t know anything, I guess I shouldn’t get you involved."

    "Has Io really not said anything to Uta about what happened at the bathhouse the other night?"
    "That’s both a huge relief and...also kind of worrying. I didn’t think she kept secrets from Uta like that."
    "Is it possible she...doesn’t know about the picture, then? "
    "Am I in the clear?"

    scene utanaragain14
    with dissolve
    stop music fadeout 15.0

    u "Anything else you want to tell me about, though?"

    "Ah..."
    "Of course that’d be too simple."

    s "..."
    u "..."
    s "Can we maybe just stand here in silence for a little while longer?"
    u "Sure."
    u "But if you have something you want to talk to me about, now’s the time to do it."
    u "There’s no one else around. I’m the only one who will hear whatever it is you have to say."
    u "And I might talk a lot...but I’m a good listener, Sensei. I promise to hear you out no matter what it is."
    s "..."
    u "..."

    scene utanaragain15
    with dissolve2
    play music "undersea.mp3"

    "And just like that, the tone shifts."
    "Just like that, the mirage vanishes — and in its place sits the sad truth of a sad man, blaming sadness for all of the sad things he does."
    "It’s him and some girl — barely up to his shoulders in height. One who’s made some questionable decisions in the past, but doesn’t really {i}deserve{/i} any of the bad things that have happened to her."
    "Yet here she is, putting herself in harm’s way once more. Like she {i}wants{/i} bad things to happen to her. "
    "Or at least that’s what I’d say if I didn’t know her as well as I do now."
    "Now, I know that it’s {i}less{/i} about a love for danger, and {i}more{/i} about being so desperate for something {i}good{/i} to happen that she’ll put herself at risk over and over and over again."
    "It’s kind of sickening, really — that level of carelessness. Of {i}stupidity.{/i} How she runs the ramps of recklessness in a way that sends that tiny body of hers speeding toward inevitable destruction."
    "But at the end, there is no blanket — nor a pit of foam to break her fall. "
    "It’s just me — with arms stretched out wide, staring deep into her soul as if to say “{i}I{/i} will be that good thing.” But I am the devil."
    "I am the snake crawling up her leg. "
    "The shadow of a past that she wishes to escape, yet can’t bring herself to stop looking back at."
    "It may not have started with me...and it may not {i}end{/i} with me either."
    "But I will be a pit stop on her long road to hell if this side of her never changes."

    s "..."
    u "..."
    s "Why don’t you ask me a question?"

    scene utanaragain12
    with dissolve

    u "A question?..."
    s "Yeah. As many as you want, actually."
    u "Why?"
    s "It’ll be easier to tell you if I don’t have to take the initiative."
    u "So you want to, like...turn it into a game?"
    s "Cowardly, I know."

    scene utanaragain7
    with dissolve

    u "No, I get it..."
    u "Talking about stuff can be hard. I see that all the time in all sorts of people. I’m not really an exception either. Surprising, I know — seeing as I can never keep my mouth shut and all."
    s "Yeah, but you have parts of you that you excel at keeping hidden. Of course you wouldn’t blab about those."
    u "You have parts just like that too, Sensei..."

    scene black
    with dissolve2

    u "So I guess it’s time to start connecting some dots..."
    u "And see the ways in which we line up..."

    "........."
    "......"
    "..."

    scene utanaragain16
    with dissolve2

    u "Question one — how do you feel about me?"
    s "Which one?"
    u "Uta-chan."
    s "Is that still the one I’m talking to? Because I was under the impression you body-swapped again."
    u "Then why not tell me how you feel about both? Just starting with Uta-chan."
    s "I think Uta-chan is the perfect girl. Just like you want her to be."
    s "I think she’s funny and cute. And way too good at her job. And she drives me insane with her endless cycle of flirting that leads to nothing. Not to mention I’ve spent probably half a million yen on her by now."
    u "And how do you feel about Uta Ushibori?"
    s "I think she’s a fucking mess."
    s "I think the complex she’s created in which she can’t function unless there’s a failsafe version of her tucked into her back pocket is juvenile. I think she’s perverted and lacks common sense."
    s "I think the way she cares for everyone is actually {i}careless{/i} since it opens her up to the possibility of being hurt by so many different people."
    s "I despise that there are so many other men just like me who sit in front of dimly lit computer screens, jerking off to her pictures and I hate that she’s figured out a way to monetize those fantasies at her work."
    s "I hate so many things about her. It’s infuriating. But it’s like watching a train-wreck...and I can’t look away. "
    s "I like her so, {i}so{/i} much more..."

    scene utanaragain17
    with dissolve2

    u "That was a much better answer than the one Ami gave me."
    s "What’d {i}she{/i} say?"
    u "That she used to touch herself in your bed."
    s "Yeah...that sounds about right."

    scene utanaragain18
    with dissolve

    u "I probably should have acted a little more surprised than I did, but...honestly, I kind of had a feeling."
    s "She doesn’t really do a good job of hiding it, I’ll be the first to admit that."
    s "But why were you two talking about that in the first place?"
    u "So I would know what to say when the time came to talk to {i}you.{/i}"
    s "..."

    scene utanaragain19
    with dissolve

    u "Question two..."
    u "How did you get them?"
    s "..."
    u "..."
    s "It’s not {i}them.{/i} It’s just one."

    scene utanaragain20
    with dissolve

    u "Then...how did you get {i}it?{/i}"
    u "Like...did you go out of your way to {i}look{/i} for my pictures when I told you about them? Because I get them taken down from websites and stuff pretty regularly, but..."
    u "There are probably some I...don’t know about...and stuff..."
    s "I didn’t look for anything. Some...random number sent it to me out of nowhere one day."

    scene utanaragain21
    with dissolve

    u "Mm..."
    u "That’s what I was afraid of."
    s "I mean...isn’t that better than me going out of my way to look for them, though?"
    u "Of course not. Because this means it could happen to {i}anyone.{/i}"

    scene utanaragain22
    with dissolve

    u "I really am {i}never{/i} safe, huh?"
    s "You were never supposed to know, Uta. I’m sorry."

    scene utanaragain23
    with dissolve

    u "You were really just going to secretly jerk off to it for the rest of forever? What do you {i}mean{/i} I was never supposed to know? "
    s "I mean that {i}you{/i} should know better than anyone how fucked up it is for me to {i}have{/i} something like that in the first-"

    scene utanaragain24
    with dissolve

    u "Sensei, {i}I{/i} took those pictures! I am the {i}last{/i} person who should be telling you about how wrong it is. I {i}created{/i} this problem. You’re just a dumb boy with really creepy taste."
    s "But you were just...stupid and needy back then. You had no idea what you were doing. You said it yourself."

    scene utanaragain25
    with dissolve

    u "I have no idea what I’m doing {i}today{/i} either."
    u "All logic says I should be totally skeeved out right now."
    u "I should report you to the police or...tell the rest of the girls about the person you {i}really{/i} are. Which, granted, isn’t {i}that{/i} much different from who we already {i}know{/i} you are."
    u "And, you know...maybe I kind of am a little grossed out. But I’m also {i}not.{/i} I’m also {i}happy.{/i}"
    s "You shouldn’t be happy, Uta..."

    scene utanaragain26
    with dissolve

    u "You think I don’t know that?! Do you think I {i}want{/i} to be such a degenerate?! Because my life would be so much friggin’ easier if I wasn’t, Sensei! This wouldn’t have ever been a problem in the first place!"
    s "I..."
    s "I have no idea what you want me to say to you right now. "
    s "I was ready for you to cut things off for good. I thought this was going to be the last time we ever came out here."

    scene utanaragain27
    with dissolve

    u "You could tell me to my face you’re never coming back and I would still wait for you here."
    u "That’s how I really feel about you, Sensei."
    u "Yes, it’s messed up that you never told me about that picture. But it’s also kind of flattering in a...really creepy...super illegal way..."
    s "..."

    scene utanaragain28
    with dissolve

    u "Just please don’t tell Io I said that. I think she’s kind of expecting me to start hating you or something and I...don’t really know how to tell her I’m sort of...okay with it."
    u "Just for you, though..."
    u "I wouldn’t do this for anybody else..."
    s "..."
    u "..."
    u "Um..."
    u "Question three..."
    s "We’re still playing?"

    scene utanaragain29
    with dissolve

    u "Do you need help?"
    s "...What?"
    u "Because I think there’s like..."

    scene utanaragain30
    with dissolve

    u "So there are, like...people you can talk to, I think..."
    u "Me and Io met in a similar kinda way, but...like..."
    u "If there are parts of you that...you want to change...you know, like...if you don’t want to be interested in the...same sort of...{i}stuff{/i} anymore..."
    u "Like...I’m not really sure if it’s therapy, or...I don’t know what to call it..."
    u "But if you don’t want to be who you already are anymore...I could try and...help you find a way..."
    s "..."

    scene utanaragain31
    with dissolve

    u "..."
    u "None of that made sense, did it?"
    s "Why?..."

    scene utanaragain32
    with dissolve

    u "Sensei?..."
    s "Why does everyone keep trying to help me?..."

    scene utanaragain33
    with dissolve2

    s "I don’t understand..."
    s "I don’t understand!"
    s "I’m doing everything wrong and you {i}still{/i} want to help me!"

    scene utanaragain34
    with dissolve2

    s "When will one of you hold me accountable?! Where will any of you draw the line?! Is there no end to what I can do?! Can I seriously do anything I want?! {i}Anything?!{/i}"

    stop music
    scene black
    with hpunch
    play sound "tackle.mp3"

    u "Sensei! Shh!"

    scene utanaragain35
    with dissolve4

    "The girl from Nara wraps her arms around me."
    "She must think I have deer parts."

    u "I can’t speak for anyone else, but I’m stupid..."
    s "Ngh..."
    u "You said it yourself, didn’t you?..."
    u "I’m a fucking mess...I can’t function unless there’s a failsafe version of me tucked into my back pocket... "
    u "I’m a filthy pervert...who lacks common sense..."
    u "There are thousands of men in front of dimly lit computer screens, jerking off to pictures of me..."
    u "But I’m happy that you’re one of them...and I won’t call you a bad person because {i}I{/i} don’t have the right to..."
    u "Let’s be stupid together, okay?..."
    s "You’re making a mistake..."

    scene utanaragain36
    with dissolve2

    u "I’ve always been good at that..."
    u "But there are other things I can be good at, Sensei..."
    u "And I want you to find out what those things are with me..."
    u "It doesn’t matter if it’s here or Nara..."
    u "It doesn’t matter if it’s in this life or another..."

    scene black
    with dissolve2

    u "I want a future with you..."
    u "I don’t care what shape or size..."
    u "I don’t care if you think you deserve it or not..."
    u "It’s what I want..."
    s "..."
    u "Please..."
    u "Will you let me take a bite out of your heart?..."

    $ renpy.end_replay()
    $ uta_love += 25
    $ utaspring2 = True

    "{i}Uta’s affection has increased by 25!{/i}"
    "{i}You decide to keep the picture.{/i}"
    "{i}You’ll look at it together one day.{/i}"

    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    s "Oh..."
    s "It’s happening again..."

    scene black
    with dissolve2

    "{i}Blackest night, envelop me-\nProtect me from my dreams{/i}"
    "{i}For in them, I hear nothing\nNot the cherub, nor its screams{i}"
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

label beachfive14:
    play sound "static.mp3"
    scene utaioinn1 with flash
    stop sound

    "Because it surely shan’t help you no matter what it was, but that alone doesn’t put an end to my curiosity."
    "You see, it rains every day where I come from. But that’s simply a side effect of losing someone you love. "
    "I never have to worry about my plants getting thirsty. I never have to worry about my balcony getting covered in dust. But I do have to worry about floating away from time to time."
    "Just like you do now."
    "Can you feel it? The tide closing in? The way fish feel against your calves as broken shells dig deep into the wounds you earned when you walked on glass?"
    "I hope you can. "
    "Because you are the reason it rains every day here. "
    "{i}You{/i} are the reason I am wounded. "
    "But I will never stop loving you because-"
    "Well..."
    "You’ll find out one day."
    "Anyway, here’s Io. It’s relevant."

    i "You don’t have to sit here with me all night, Uta. Go be social and...have {i}fun{/i} with people or whatever it is you do. I’m fine."
    u "Like heck you’re fine. You haven’t been fine in weeks. In fact, you’ve gotten even {i}worse{/i} since the Dorm Wars and you’re gonna have to tell me why eventually."
    i "Can you not just chalk it up to me being an unlovable meat-sack this time? That’s always worked in the past."
    u "Maybe for you. But you’re the {i}most{/i} lovable meat-sack to me."

    play sound "static.mp3"
    scene utaioinn2 with flash
    stop sound

    i "I’m confused. Was that supposed to be a compliment?"
    u "It sounded better in my head, okay? I’m just trying to remind you that you can-"
    i "Talk to you whenever I want. I know. You’ve told me that probably fifty times today alone."
    u "Yet you haven’t even {i}tried!{/i} I can tell when something’s wrong, Io. I’ve known you for years."
    i "Well, look at it this way — if something was {i}really{/i} wrong, would I have bothered coming here at all?"

    scene utaioinn3
    with dissolve

    u "Yes! That’s exactly when you {i}would{/i} bother coming here because you’d think something like, “If I don’t come, Uta will think something is wrong and I don’t want her to think that.”"
    i "So you wouldn’t think anything was wrong if I actually stayed at home?"
    u "No, I’d think something is wrong then too because your thought process would be, “Uta wants me to come but I am so beaten up that I don’t even have the energy to humor her right now.”"
    i "Wow. I sound just as exhausting in your head as I do in mine."
    u "You are!"

    scene utaioinn4
    with dissolve

    u "In fact, you’re {i}so{/i} exhausting that it makes me wanna blow my frickin’ brains out with my crossbow! And that’s not even a guaranteed instant kill! I’ve seen it happen! It’s gross!"
    i "I thought you weren’t allowed to kill deer in Nara?"
    u "We're not, but that’s never stopped my brother. I’m not even talkin’ about that though. My uncle’s a matagi. He hunts bears in Akita."
    i "With a {i}crossbow?{/i}"
    u "He says it “softens them up” but that’s beside the point, Io! I’m tired of you hiding things from me when all it does is make it impossible to cheer you up! Let me help you!"
    i "I’d love to, Uta. Except, here’s the thing — we both have stuff about our past that we quite literally found out we {i}can’t{/i} help each other with. That’s why we’re friends. Remember?"

    play sound "static.mp3"
    scene utaioinn5 with flash
    stop sound

    u "Of course I remember! But-"
    i "We’re done here. If you want to have girl-talk, there are like fifty other girls in the rooms down the hall you can go hang out with. "
    u "Io..."
    u "She didn’t, like...show up again...did she?..."

    scene utaioinn6
    with dissolve

    u "I thought you said she was still outside of Kumon-mi? I thought-"
    i "I’d have asked for your help burying a body by now if that’s what happened, Uta."
    u "But...why would you bring up the things we {i}can’t{/i} help each other with if that’s not what’s going on here? I don’t get it. Why do you make it always so hard to understand what’s wrong?"
    i "It’s just better off that way."

    play sound "static.mp3"
    scene utaioinn7 with flash
    stop sound

    i "Sometimes...the less you know, the better. "
    i "Life’s messy enough as is. The last thing either one of us needs is one more thing to cry about. Mostly you, though. Crying is exhausting and makes my head hurt."
    u "So something {i}did{/i} happen and you’re just purposely choosing to keep me in the dark."

    scene utaioinn8
    with dissolve

    i "Yeah. That’s right."
    u "Don’t smile at me, Io. Do you have any idea how mad that makes me?"

    if iospring3 == True:
        i "Do you have any idea how mad you’d be if I told you the truth? Because it’s way worse. So just let me feel like shit for a little longer and you’ll get to keep your entire world-view intact. Sound good?"
        u "Horrible, actually. It makes me feel like you have zero faith in me when I would trust you with my life."
        i "Trusting me with anything more than tools is just an accident waiting to happen, so I implore you to reconsider."

    else:
        i "I mean, yeah. You’re making that pretty obvious right now. But, at the same time, you’re kind of blowing things way out of proportion."

        scene utaioinn10
        with dissolve

        u "How am {i}I{/i} the one blowing things out of proportion when all I’ve done over the last couple weeks is try to get ahold of you?"
        i "Repeat that last sentence, just a little slower."
        u "Okay. So I’m clingy. Yeah. But I’ve always been clingy. And you-"
        i "And I’ve always been a scared and confused piece of shit. "

        scene utaioinn11
        with dissolve

        i "But, like..."
        i "It’s been mostly just “confused” lately. That’s why I’ve been so absent."
        i "Like yeah, a thing happened. I had to confront some stuff I hate confronting. But for the first time in my life, it didn’t end in complete and utter tragedy."
        i "Maybe I’m just having a hard time figuring out what that means and where to go from here. It’s all sort of...uncharted territory for me. But it’s nothing personal."
        i "I’m just keeping you out of it since you have more than enough on your plate already."

    scene utaioinn9
    with dissolve

    u "So you’re really not gonna tell me?..."
    i "I’m really not gonna tell you."
    i "Trust me. You’ll be way happier this way."
    u "But what about you?"

    if iospring3 == True:
        i "Uta, come on."
        i "There’s barely a “me” left at this point."

    else:
        i "What {i}about{/i} me?"
        u "Are {i}you{/i} really going to be happy about this if you just bottle everything up again?"
        i "You know..."
        i "For the first time ever, I think I might."

    play sound "slidedoor.mp3"

    mi "Attention, roommates! "

    scene utaioinn12
    with fade

    t "The most attractive women in Kumon-mi have returned."
    mi "And we’ve come bearing gifts!"
    u "Is that a friggin’ crab?"
    mi "This little guy wandered up to us while we were diggin’ in the sand earlier and now Tsuneyo’s gonna kill him."
    t "I have provided for this family. I am a strong, independent woman who don’t need no man."

    scene utaioinn13
    with dissolve

    mi "You feelin’ any better over there, Io? Still want me leavin’ you alone?"
    i "Are you really going to kill that thing in our room?"
    u "You need to stop dodging the question when people ask you how you’re feeling."
    i "Don’t worry about me. I just think that thing’s cute and I don’t want to watch it die."
    t "I understand now. She is unwell because she never learned how to close her eyes."

    scene utaioinn14
    with dissolve

    t "How horrible she must feel for my attractiveness to be entirely inescapable."
    mi "Nah, I think she’s just got that depression thingy Makoto has."
    i "{i}Hah...{/i}"
    mi "See? Ya can tell by the sigh."
    u "You two might wanna close the door before Io goes on a crazy rant about depression again."

    scene utaioinn15
    with dissolve

    t "Understood. But please advise as to whether or not the two of you will be partaking in our crustaceous bounty."
    mi "Yeah. It’s only a matter of time ‘til this thing latches onto me. I just hope it’ll be easier to get off than the friggin’ blobfish."
    i "I’m not hungry. Thanks, though."
    u "We’ll both eat. Thanks for cooking, Tsunecchi."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    t "Your wish is my command."
    mi "Wish? You some kinda genie n’AAAAAAH FRICK! HE’S GOT MY FINGER! I’M GONNA HAVE TO USE MY OTHER HAND FOR...STUFF NOW!"

    scene utaioinn16
    with dissolve2

    i "Uta, what the hell? I just said I wasn’t hungry."
    u "Yes, but it is my duty as your best friend to feed you when you’re not feeling like yourself. "
    i "Is it? Have I been neglecting my duties for the entire duration of our friendship?"
    u "I love you. Okay?"
    i "Yeah, I love you too. But why do you need to be three inches from my face to tell me that?"
    u "Because I need you to understand it."
    u "I get that you don’t want to talk about whatever it is that happened. And yeah, that makes me really sad, but I’ll accept it so long as you {i}promise{/i} to come to me if it ever gets unbearable, okay?"

    scene utaioinn17
    with dissolve

    i "Okay."
    u "You really promise?"
    i "I really promise."
    u "Really really? "
    i "Really really."

    scene utaioinn18
    with dissolve

    u "Okay..."
    i "Okay."
    u "..."
    i "Now it’s your turn!"

    scene utaioinn19
    with dissolve

    u "My turn to what?"
    i "Attempt to withstand my verbal assault as I become a hypocrite once more and say some stuff about how you should talk to me when you have problems."
    u "I have problems?"
    i "Mhm."
    u "Current ones?"
    i "Mhm."
    i "Unless you’ve already managed to forget that our teacher had some very inappropriate pictures of you on his phone. "

    scene utaioinn20
    with dissolve

    u "Oh...{i}that.{/i}"
    i "So you really did forget then? Wish I could do that. Life would be like five hundred times easier."
    u "I haven’t forgotten, but..."
    u "Maybe, like..."

    scene utaioinn21
    with dissolve2

    u "Maybe that’s...not as big of an issue as...it sounds?...."
    i "..."
    u "..."
    i "..."
    u "Io?..."
    i "Not an issue, Uta? Really?"

    scene utaioinn22
    with dissolve

    u "..."
    i "Have you forgotten why you’re here too? Why you had to leave your hometown behind? Come up with a brand new style and persona? Have you forgotten {i}all{/i} of that?"
    u "Of course not..."
    i "Then how can you look me in the eyes like that and tell me it’s not a problem?"
    u "..."
    i "Uta-"
    u "I think I’m in love with him."

    scene utaioinn23
    with dissolve

    i "You’re..."
    i "You’re {i}what?{/i}"
    u "And so...I don’t mind...so long as it’s {i}him.{/i}"
    i "You mean like...you’re in love with him like you were in love with Spongebob Squarepants?"
    u "Wha- of course not..."
    i "Or that boy who used to work at the convenience store? Or Tony the Tiger? Or that boy who used to work at the library? Or whatever the Cheetos cat’s name is? "
    u "Chester. But Io, this is different from all of those things..."
    u "And the reason I’m telling you is because you specifically {i}told{/i} me to not let you be the barrier between us. And you {i}won’t{/i} be. I just..."
    u "I really don’t know if I can hold back any longer."

    scene utaioinn24
    with dissolve

    i "Any {i}longer?!{/i} How long has this been going on for?! "
    u "Too long...and I’m sorry. I just didn’t want to hurt you and-"
    i "Uta, you fucking moron! I literally {i}told{/i} you I wanted this to happen so the {i}three{/i} of us could be together!"

    scene utaioinn25
    with dissolve

    u "You did, yeah! But that was a really fucking weird thing to suggest and I refused to believe you were actually serious!"
    i "Of {i}course{/i} I was serious, you idiot. God, this changes everything! Why didn’t you tell me sooner?"
    u "Because I {i}don’t{/i} want to be part of a throuple, Io!"

    scene utaioinn26
    with dissolve2

    i "..."
    u "I want to be with him as a traditional couple. Two people. That’s it. "
    u "I don’t want anyone else holding his hand. I don’t want anyone else cuddling with him. I don’t want anyone else kissing him. I want him and all of him and I would give him all of me in return."
    u "But, Io...I will throw away even the {i}idea{/i} of that right now if you ask me to. Because you are even {i}more{/i} important to me than he is."
    i "What the fuck do you expect me to say to that, Uta?..."
    i "Do you really think I’m going to look you in the eyes and tell you not to follow your heart when I want {i}you{/i} to find happiness even more than I want that for myself? Do you really think I’d do that?"
    u "That’s not-"
    i "Go after him, Uta. "
    i "Get married. Buy a house. Adopt Sir Meowington the 5th. Make babies. Do {i}all{/i} of that shit and leave me behind because I clearly {i}am{/i} a barrier between you two."
    i "But promise me that you’re 10000%% sure. Because you’ve said it yourself that you’re impulsive and-"
    u "I’m 10000000%% sure...but I am {i}not{/i} leaving you behind. Ever."
    i "I’m just going to get in the way."
    u "Then I’ll make room so you can fit."
    i "So the throuple is back on?"
    u "I..."

    scene utaioinn27
    with dissolve

    u "Ugh...I don’t know. This is all so confusing."
    u "There are like seven billion people in the world and we both had to fall for the same one. It’s not fair."
    i "Yeah, but at least {i}you{/i} can give him what he wants."

    scene utaioinn28
    with dissolve

    u "You don’t know for sure {i}that’s{/i} what he wants, Io. "

    if iospring3 == True:
        i "God, I wish you were right...but you’re not."
        i "I {i}do{/i} know that’s what he wants...now more than ever. Which also means that I know it just...wouldn’t work."
        i "So go. Don’t even think about me. I’ll just...watch the game from the dugout or something."
        u "Io-"

    else:
        i "..."
        u "You have just as good of a chance as me..."
        i "You’re asking me to compete with literal perfection."
        u "I’m asking you to compete with the hollowed out shell of a girl whose head keeps falling off of her shoulders every single time she hops out of bed."
        u "I’m a mess, Io. It’s Uta-{i}chan{/i} who’s perfect."
        i "They’re both you, Uta. They’ve always {i}been{/i} you. And none of those flaws are actually flaws to me. "
        i "So go. Don’t even think about me. I’ll just...watch the game from the dugout or something."
        u "Io-"

    stop music fadeout 15.0

    mi "{i}Oi! Food’s almost done! You two gonna eat out here with us or do ya wanna come grab some yourselves?{/i}"
    u "Pause?"
    i "Pause. You were right. I’m hungry now."
    u "Do you still love me?"
    i "Do you still love {i}me?{/i}"
    u "I’ll always love you."
    i "I’ll always love you too."
    u "Wanna just leave Sensei behind and go get married ourselves?"
    i "Can we eat first? I haven’t had anything since last night."

    scene black
    with dissolve2

    u "And this is exactly why best friends feed one another..."

    "And so the four girls partake in the consumption of the body of Christ."
    "I mean crab."
    "The four girls partake in the consumption of the body of crab."
    "But you and me go somewhere more fun."

    $ renpy.end_replay()
    $ beachfive14 = True

    jump beachfive15

label utaspring3:
    scene nightsky
    with dissolve2
    play music "summerwind.mp3"

    "Yet another inconsistency in weather has prompted me to seek out a means of thermoregulation as I make my way over to the bath house."
    "And while this constant swapping of cold for heat and heat for cold does wonders in keeping me on my toes, sometimes I just want to feel a lot of one thing."
    "Normally, that thing is sadness. Or boner. But tonight, that thing is being hot. So I will submerge myself fully in the hottest water I can find while some girl with green hair complains to me."

    u "Welcome in!"

    scene utaisio1
    with dissolve2

    s "Wow. You look different today, Io."

    scene utaisio2
    with dissolve

    u "Really? Must be my new medication. One of the potential side effects was larger boobs and purple eyes."
    s "Don’t worry. I still like you more than Uta either way."

    scene utaisio3
    with dissolve

    u "Hey! That hurts! Even if you already knew it was me and you’re only saying that to get on my nerves!"
    s "Oh, wow. Is that actually you, Uta?"

    scene utaisio4
    with dissolve

    u "Stop pretending you don’t immediately recognize me! I have a complex, remember?!"
    s "I just don’t think I can know for sure it’s you unless you flash me."

    scene utaisio5
    with dissolve

    u "Ah-hah! A trick! Now there’s the Sensei I know and love."

    scene utaisio6
    with dissolve

    u "{size=-5}Which means I must now apologize as what you are asking is beyond the capabilities of what I am legally allowed to do as an employee of the bath house and the daughter of parents who are already very disappointed in me.{/size}"
    s "They don’t need to know."

    scene utaisio7
    with dissolve

    u "They do, though. You know the rule. No freaky business until there’s a really uncomfortable phone call."
    s "How would that call even go?"
    u "Probably like..."

    scene utaisio8
    with dissolve

    u "Hi, Mom! Hi, Dad! It’s your beloved little girl, Uta! So — remember that time you made me move to Kumon-mi because some creepy old guy wanted to screw me? "
    u "Yeah. Well, that’s happening again. But I like him this time so I want your permission to-"
    u "What’s that? I need to move {i}again?{/i} Darn!"

    scene utaisio9
    with dissolve

    u "Then a helicopter comes and carries me away to Nagano or something where the cycle repeats and I fall for someone else who’s way too old for me."
    s "Which is precisely why you should avoid the phone call entirely and just flash and/or marry me already."
    u "Did you bring a ring this time?"
    s "No."

    scene utaisio10
    with dissolve

    u "Then both of your wishes will {i}not{/i} come true!"
    s "What are you even doing here, Uta? Where’s Io? And...is that her robe?"

    scene utaisio11
    with dissolve

    u "Oh, no. I have my own. I help out here sometimes when Io and her aunt can’t make it. They’re at the doctor’s office right now."
    s "The doctor’s office? Is everything-"
    u "Totally fine, no worries. Doctors just make you do this thing sometimes where you have to physically show up if you want to keep getting the {i}good{/i} stuff."
    u "So Io and her aunt make a big trip once a year where they just try to knock out as many of her doctors as they can in one go. They won’t be back until tomorrow."
    s "Wouldn’t it make more sense for her to just have everything prescribed by {i}one{/i} doctor?"
    u "Yeah. I think there might be some kinda fraud thing going on. I haven’t ruled out that Io’s aunt isn’t running a secret drug cartel yet."
    s "Oh great, another subplot."

    scene utaisio12
    with dissolve

    u "Either way! Yours truly is here to make sure that you and anyone else can get naked with ease! Now please hand over your wallet as you so normally do, Sensei. Tipping is not mandatory, but expected."
    s "I have never had to tip Io in my life."
    u "Do I look like Io to you?"
    s "Like I said, I can’t be convinced you’re {i}really{/i} Uta until you flash me."
    u "Well, I’m not gonna {i}flash{/i} you before I’m paid. I don’t show these babies to just anybody, Sensei. It’s not 2015 anymore. "
    s "See, we’re going to have a problem then. I didn't bring my wallet because Io stopped charging me a long time ago and just lets me bathe for free now."
    u "And why should Uta do the same?"
    s "Because she’ll get to see my penis on the cameras I know she has access to."

    scene utaisio13
    with dissolve

    u "And faint again?! You saw what happened the last time you showed me that thing! I was out for like twelve hours!"
    s "Technically, I didn’t {i}show{/i} you. You busted in and saw it on your own."
    u "Maybe I thought Io was in danger?! That thing was so big I could feel its presence from all the way down here!"
    s "Can you feel it now, Uta?"

    scene utaisio14
    with dissolve

    u "Mh?!"
    s "{i}Can you feel my penis?{/i}"

    scene utaisio15
    with dissolve

    u "Okay, fine! You don’t have to pay me! Just take that thing outta here before it robs the register and impregnates everyone within a five mile radius!"

    scene black
    with dissolve2

    s "Nice. Thanks, Uta. Enjoy the camera feed."
    u "I will! I-I mean I {i}won’t!{/i} Because we definitely don’t have one!"
    s "Feel free to join if-"
    u "OKAY BYE!"

    "........."
    "......"
    play sound "phonedial.mp3"
    "..."

    scene utaisio16
    with dissolve2

    u "Come on, come on, come on..."

    play sound "phonebeep.wav"

    i "{i}Hello?{/i}"
    u "Io, we’ve got a code blue over here."

    play sound "static.mp3"
    scene utaisio17 with flash
    stop sound

    i "Someone {i}died?{/i} Why is it always on my day off?"
    u "{i}Nobody died! But somebody is about to die and that somebody is me!{/i}"

    scene utaisio18
    with dissolve

    i "Uta, I understand that Tsuneyo girl may be considered “conventionally attractive” by all of you. But if she’s there again, please don’t use the cameras to-"
    u "{i}No! I mean Sensei is here right now! He’s getting undressed as we speak!{/i}"

    scene utaisio19
    with dissolve

    i "Oh."
    i "So what?"
    u "{i}What do you mean SO WHAT?! How am I supposed to deal with this?!{/i}"
    i "By...continuing to sit at the counter and helping other customers who come in?"
    u "{i}Oh...yeah. I guess that makes sense. Sorry for the false alarm.{/i}"
    i "Or you could go have sex with him."

    play sound "static.mp3"
    scene utaisio20 with flash
    stop sound

    u "PHBHTBHTHBTHBTHTHTHTH?!?!?!"

    scene utaisio21
    with dissolve

    u "What?!"
    i "{i}Yeah. Use my bed, though. Don’t make the bath all gross, please.{/i}"
    u "What do you think you’re saying, Io?!"
    i "{i}What? That’s what you...sex people do, right? Spare me the details, though. And please thoroughly clean my sheets when you’re done.{/i}"
    u "I don’t want to have sex yet! I’m not ready!"
    i "{i}You sure sound ready. Your voice is like two octaves higher than normal.{/i}"
    u "Because penis, Io! Sensei penis! So close to Uta! What do?!"
    i "{i}Dude, what do you want me to tell you? Either do stuff or don’t do stuff. You like him, right? This could be your shot.{/i}"
    u "But you like him too! And I’m at {i}your{/i} house! It’s sacrilegious!"
    i "{i}Technically, it’s my aunt’s house. Do you want to talk to her? {/i}"

    scene utaisio22
    with dissolve

    u "NO! OBVIOUSLY NOT!"
    i "{i}Cool! Bye then! Have fun!{/i}"

    scene black
    with dissolve
    play sound "phonebeep.wav"

    u "Io, you don’t- AAAAH! SHE HUNG UP! "
    u "WHAT AM I SUPPOSED TO DO?!?!?!?!"

    scene utaisio23
    with dissolve2

    "It was a sticky situation for Uta Ushibori — a girl who had just recently brought her “I’ve masturbated to my teacher” count into the triple digits. "
    "Because on one hand, she {i}was{/i} perfectly capable of sitting behind the counter and just serving customers like Io suggested. "

    scene utaisio24
    with dissolve2

    "But on the other, this {i}was{/i} a perfect opportunity to try and take things up a notch with someone she’d been borderline obsessing over for months, if not {i}years{/i} on end now."
    "The days all seemed to blur together. But in the midst of that incessant fog, there was one thing that was abundantly and permanently clear."
    "She had not learned a thing."

    u "Um...{i}Ahem...{/i}"

    scene utaisio25
    with dissolve2

    s "Hm?..."
    u "..."
    s "..."
    s "I like where this is going."

    play sound "static.mp3"
    scene utaisio26 with flash
    stop sound

    u "Y...You don’t mind if I join you, right?"
    u "I...I uhhhh closed. The...shop. Early. B-But there are still some customers in the women’s side, so..."
    s "So you’d rather be naked and alone with your male teacher instead of other women."

    scene utaisio27
    with dissolve

    u "It sounds so...{i}impure{/i} when you...put it that way..."
    s "Probably because it {i}is.{/i} You know what you’re doing right now. "

    scene utaisio28
    with dissolve

    u "That’s...uhh...yeah! I...know...but..."

    scene utaisio29
    with dissolve

    u "D...Don’t just put me on the spot like that, Sensei..."
    u "Just because I know doesn’t...mean it’s not...{i}embarrassing...{/i}"

    scene utaisio30
    with dissolve

    s "I want to destroy you."
    u "Hm? What? I didn’t-"
    s "Nothing. Just know that you are putting yourself at risk by doing this and that I am not going to stop staring at you for the rest of the night."
    u "Y...You can stare. I like it when...you stare, but...uhh..."
    u "B-Before you start! Can you give me, like...five seconds to take my towel off and get in the bath?"
    s "You are going to walk in here looking like that and then tell me I can’t watch the best part?"
    u "B-Baby steps! Okay? We’ll...um...yeah. You’re...hot. Wow. Uhh. What was I...towel! Right. Towel. Eyes! Close. Five...s...seconds."
    s "..."
    u "P...Please..."
    u "M...{i}Master...{/i}"

    scene utaisio31
    with dissolve

    s "Fine. But only because you called me “Master.”"

    scene black
    with dissolve2

    u "Yes, Master! Anything for you, Master! "
    s "Anything? Then you don’t mind if I-"
    u "Ah! Aaah! No! Eyes! Keep closed! Almost there! No peeping! I’ll scream!"
    s "You’re screaming now. "
    u "If you think {i}this{/i} is bad, you should hear what’s going on {i}inside{/i} of my head!"

    play sound "static.mp3"
    scene utaisio32 with flash
    stop sound

    "It was a cacophony of unrepentant lust aimed directly at the heart and cock of a man who excelled when it came to the latter, but was completely undeveloped in terms of the former."
    "This was quite the contrast to Uta Ushibori — a girl who, while ravenously horny, {i}still{/i} prioritized love and affection over carnal desire."
    "It would be so easy for her to just traipse her way over to the opposite end of the bath and ride this man until {i}both{/i} of them passed out from heat exhaustion, but she kept her distance."
    "She covered herself up — and while {i}some{/i} of that was designed to tease him and keep him wanting more, a greater portion of it was brought on by uncertainty."
    "She’d accepted she wouldn’t be the first. But if she timed things properly, she believed she could {i}still{/i} be the last. "
    "It was that type of immature and wishful thinking that kept her broken, though. For she was chasing after the right thing — just it was, at the risk of sounding repetitive, on the opposite end as well."

    u "You can open your eyes now."
    s "Tch. I was hoping you’d be closer when I heard those words."
    u "Are you not as tempted to try and do naughty stuff to me when I’m all the way over here?"
    s "My penis might be big, but it’s not {i}that{/i} big, Uta."

    scene utaisio33
    with dissolve

    u "I don’t know about that, Sen...{i}Master.{/i} I’ve seen lots of penises in my time on the Internet and I...definitely think you’ve got them all beat if I’m remembering correctly."

    play sound "water1.mp3"

    s "If you need a reminder-"

    scene utaisio34
    with dissolve

    u "No! Totally fine! I can only handle so much!"

    play sound "water1.mp3"
    scene utaisio35
    with dissolve

    s "If you insist."
    u "Hahah.....hah......yeah...."

    scene utaisio36
    with dissolve

    u "So you’ve, like...been here with other girls before, right?"
    s "A few times. Not always on the same side of the fence, though."
    u "But...{i}sometimes...{/i}right?"
    u "Sometimes you’ve...been in here with other girls."
    s "Right..."
    u "You ever like...you know..."
    s "Why? You want details?"
    u "Just...curious. "
    s "Then no. I have never done anything {i}inappropriate{/i} in here with anyone before. Which is actually...kind of surprising."
    u "Surprising cause you...waaaant to? Or you just feel like that would be a...normal thing for you to do at this point?"
    s "Is this line of questioning leading anywhere in particular, Uta?"
    u "Just...you know..."
    u "Trying to see how different we are."

    scene utaisio37
    with dissolve

    u "I’ve never done anything like this before. Be...so close to someone I’m interested in while...so {i}vulnerable...{/i}you know?"
    u "Like, I’m trusting you with all of me right now and it’s...really intimate."
    u "It makes me really happy."

    scene utaisio38
    with dissolve

    u "And I don’t use that term “intimate” lightly. I know I’ve...done some questionable and...stupid stuff in the past. But that was all sorta...{i}fake{/i} intimacy, you know?"
    u "Right now is like...{i}real.{/i} Really real. And I’m scared but I’m...comfortable."

    scene utaisio30
    with fade

    s "This seems really heavy coming from someone who was trying to get me to pay her to flash me just ten minutes ago."
    u "Th-That was {i}not{/i} real! This is different!"
    s "So if I offer to pay you {i}now-{/i}"
    u "I’ll question why you suddenly have your wallet again when you told me you left it at home. Then probably deny your request again because I’m nervous and horny."
    s "Say that again please. Nervous and what now?"

    scene utaisio39
    with fade

    u "...horny."
    s "I like this."
    u "You’re, like...really hot...and I’m a...pervert, so..."
    u "You’re not the...only one who has it really hard right now..."
    s "Yeah. “Really hard” is an understatement."

    scene utaisio40
    with dissolve

    u "Oh my god, this was a terrible idea."
    s "There’s nothing to be ashamed about, Uta. If anything, {i}I’m{/i} the one who should be ashamed right now because {i}I{/i} am supposed to know better."

    scene utaisio41
    with dissolve

    u "And I’m not?"
    u "Some people would say this is the craziest thing I’ve done yet, Master."
    s "You can go back to “Sensei” now. We’re being real with each other. No need to use nicknames."
    u "Then...can I use your real name?"
    s "Do you {i}know{/i} it?"
    u "Akira...right?"
    s "I...guess you do."

    scene utaisio42
    with dissolve

    u "We all...kinda know now. Word gets around and stuff."
    s "Well...sure. I guess you {i}can{/i} call me that then."
    u "Akira..."
    u "It’s a good name."
    u "How do you spell it?"
    s "With autumn and music."

    scene utaisio43
    with dissolve

    u "Music?"
    s "Or comfort. Ease. Whichever one you like most."

    scene utaisio44
    with dissolve

    u "The first one, obviously! We can match that way!"
    s "That’s why I said it. "

    scene utaisio45
    with dissolve

    u "Huh?"
    s "Well, you were trying to see how different we are, right? "
    s "Maybe we’re not so different at all at the end of the day."

    scene utaisio46
    with dissolve

    s "Granted, your name is much prettier than mine."
    u "I don’t think I agree...{i}Akira.{/i} "
    u "Like, maybe your name on its own isn’t super unique. But at least the way you write it is cool. Everybody else is like “bright” or “light” or something. Which wouldn’t really fit you at all, would it?"
    s "You mean to tell me you can look at me and not see a massive ball of sunshine?"

    scene utaisio47
    with dissolve

    u "No, autumn is way better! Not quite summer, yet not quite winter. Warm colors, but chill weather. At least...typically. "
    u "It fits you."
    s "And Uta fits you. Perhaps too well."

    scene utaisio48
    with dissolve

    u "Heheh. My parents say the same thing. They always joke about how they knew I’d be a {i}song.{/i} Cheerful. Exciting. Someone who’d appeal to everyone."
    u "Just...took me a little while to grow into that."
    s "Yeah. I’m still growing into my name too."

    scene utaisio49
    with dissolve

    u "It’s really okay that I call you that? It doesn’t make you feel weird or anything?"
    s "Well, do you feel weird when I call you Uta?"
    u "Define weird? Because it does give me butterflies. But I get those whenever you’re around in the first place, so maybe I’m just noticing more of them now?"
    s "God, you are so fucking cute."

    scene utaisio50
    with dissolve

    u "You can have me forever so long as you buy a riiiiiing~"
    s "You could also just buy yourself one with all of the money I have given you."
    u "Not the saaaaame!"
    s "I’m well aware. But if we talk any more about a future where I can have you all to myself, I’m going to come over there and {i}actually{/i} destroy you. So yeah."

    scene utaisio51
    with dissolve

    u "Yeah, I’m like five lines away from throwing myself at you too. This sexual tension is seriously killing me. "
    s "Which means we either need to get out now or have sex."
    u "Well, figure it out right now because I only have four lines left."
    s "Uhh...we could go watch a movie or something?"
    u "There is zero way that would not end sexually."
    s "Well, why are we even {i}avoiding{/i} that if we both want it?"
    u "The timing isn’t right. One line left."
    s "..."
    u "..."
    s "..."
    u "..."
    s "Does this count as edging you?"

    scene utaisio52
    with dissolve

    u "Yes, and it’s hell!"
    u "But I know a place where we can go be alone and not be tempted to do sexy stuff!"
    s "You underestimate just how many locations I am willing to have sex in. Also, I’m pretty sure you’ve passed your five lines and are supposed to be throwing yourself at me right now."
    u "Fine! Close your eyes and get ready for my body! Here it comes!"

    scene black
    with dissolve

    s "Done. But if you-"

    play sound "water1.mp3"
    stop music fadeout 10.0

    u "UTA-CHAN ESCAPE ROUTE GOOOOO!"

    "Uta manages to snatch her towel and exit the bathing area so quickly that I’m not-"
    "Well, I’m not sure {i}what{/i} exactly. But I {i}do{/i} know that this raging erection is going to need to wait until it tastes her flesh."
    "I’ve grown used to her teasing, though. And honestly, I’d be fine with it lasting for the rest of our lives. But chances are, one of us is going to explode by then."
    "Will it be me? Will it be her? There’s no way to know until we let the future play out."
    "And in the event that it doesn’t play out the way we want..."
    "Maybe we can just reset?"

    $ renpy.end_replay()
    $ utaspring3 = True
    $ uta_love += 1

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump utaspring4

label utaspring4:
    play sound "footsteps.mp3"
    scene nightsky
    with dissolve2

    s "Uta, where the fuck are we going?"
    u "Just trust me, okay?! I know a spot."
    s "We already have a spot, though. "
    u "Yes, but this time we’re going to my {i}Io{/i} spot."
    s "I knew you were Io this whole time. From the moment I set foot in the bath house. Don’t think I’ll be deceived by your surprisingly large and clearly fake breasts."
    u "Fake?! You wound me, Sen- no. Mas- no. Akira! "
    s "That’s the point, U- no. I- no. Uo."
    u "I’m a fish now?!"

    "I torment her tirelessly. It’s my way of getting back at her for the amount of times she’s blue-balled me so far."
    "It’s also just fun, though."
    "Being {i}with{/i} her is fun."
    "And...weirdly different in a way that’s hard to quantify."
    "Almost natural to a certain extent. "
    "Maybe it’s just because she’s so experienced when it comes to dealing with Io — and {i}that{/i} is a girl I have a lot in common with."
    "But maybe it’s something better. Brighter. Bigger? "
    "Whatever it is, I’m content — for I could stare at the back of her head in every single context for the rest of my life and still believe I’ve done all I was put here to do."

    scene black
    with dissolve2

    s "Wait, here?"
    u "Mhmmm. Just {i}trust{/i} me. Like I said."

    "Uta slides a lighter out of her pocket. I’m not sure why she has one or what she plans to do with it."
    "But as we make our way below ground, it begins to become clear. "
    "She leads me to the end of a long tunnel and tells me to sit down."

    play music "blueair.mp3" fadein 3.0
    scene utatunnel1
    with dissolve3

    "Which is what brings us here."

    u "... "
    s "..."
    s "Where are we?"
    u "A secret tunnel. Like in Avatar."
    s "The James Cameron movie?"
    u "I can’t believe you just said that to me."
    s "Uta, why do you know about a secret tunnel? And why does it look like people live down here?"
    u "Because they probably do. This thing runs from here all the way to the old district. "
    s "What? Why?"

    scene utatunnel2
    with dissolve

    u "Ooooh? You don’t know?"
    s "I wouldn’t have asked if I did. I’m not the type to do that just to let someone feel good about knowing stuff."
    u "Well, Akira — legend has it that when Kumon-mi was first being built, it was only meant to be the old district."
    s "I assumed as much based on the fact that it is literally called the “old district.”"
    u "Right, because you didn’t let me finish. But what if the {i}new{/i} district was actually the older of the two?"
    s "Then the people in charge of city planning here are chaotic and terrible at naming things."

    play sound "static.mp3"
    scene utatunnel3 with flash
    stop sound

    u "That’s one possibility, yes. {i}Or...{/i}we have a conspiracy on our hands. "
    u "Because {i}I{/i} heard that these tunnels were constructed in secret to bridge the gap between the two districts without the {i}true{/i} older district ever finding out."
    s "Mhm. I feel like you might be underestimating how hard it is to build a tunnel of this magnitude in secret."
    u "Maybe if it was built by conventional means...but what if the old district is actually {i}alive?{/i}"

    scene utatunnel4
    with fade

    s "..."
    s "What?"
    u "What if, and hear me out here, the tunnel...{i}built itself?{/i} To try and connect to something that already existed! Like a-"
    s "Like a parasite?"

    play sound "static.mp3"
    scene utatunnel5 with flash
    stop sound

    u "Bingo! When Kumon-mi was first being built, they wanted to create a new type of city that was self-sustainable. But little did they know...it would actually come to life!"

    scene utatunnel6
    with dissolve

    u "But it was starved for resources and energy! And the ones in charge, desperate to create a brand new type of city, ran out of funding halfway through and had to quit!"

    scene utatunnel7
    with dissolve

    u "This left the old district scared and desperate...so it sunk its roots into the earth and connected itself to the first thing it found!"

    scene utatunnel8
    with dissolve

    u "Which brings us here!"

    play sound "static.mp3"
    scene utatunnel9 with flash
    stop sound

    s "Okay."
    s "So do you know what this tunnel {i}actually{/i} is or should I just pretend to believe all of that?"
    u "Well, let me ask you this — does anybody {i}actually{/i} know anything about Kumon-mi? "
    u "Because I couldn’t find like, any info on it at all before I moved here. And all of the stuff I’ve heard about the way it {i}used{/i} to be is stuff people heard from people who heard it from...other people."
    s "I guess it {i}is{/i} kind of weird if there’s no...information on that stuff. But the weirdest part of all is just straight up what goes on in the old district. "
    u "Yeah, that place gives me the heebie-jeebies. But that’s further proof that something’s wonky about it, don’t you think?!"
    s "I don’t think we need a full blown conspiracy to land on the fact that that place is creepy, Uta."
    u "No, we don’t. But the fact that the difference between here and there is so drastic just...I don’t know. I think there’s something weird going on. So {i}I’m{/i} going to keep believing the city is alive. Just like our dorm."
    s "So the dorm is alive too now?"

    scene utatunnel10
    with dissolve

    u "Well, yeah! It’s gotta be! There are so many floors and we only use three of them. What if all its organs and stuff are in the floors above us and that’s why the other classes haven’t moved in yet?"
    s "Because...the school doesn’t want to...kill a sentient building?"

    scene utatunnel11
    with dissolve

    u "Yes."
    s "..."
    u "..."
    s "You’re a bad theorist."
    u "I just go off vibes."
    s "Well, can you {i}vibe{/i} out an explanation as to why you and Io hang out in a weird tunnel that you think is alive?"

    scene utatunnel12
    with dissolve

    u "We’ve been coming down here since before we even transferred. Barely do it anymore, though...now that there isn’t really much of a need for it and stuff."

    scene utatunnel4
    with fade

    u "Io can’t do her hardcore woodworking stuff at her aunt’s house, and our last school wouldn’t let her use the woodshop unsupervised. And me — I just wanted a place to shoot my crossbow."
    s "So the two of you would sneak into a creepy tunnel that is definitely inhabited by homeless people for the sake of woodworking and archery?"
    u "Yup! That about sums it up."
    s "And that mattress behind you?"
    u "Idunno. Probably belongs to one of the homeless people."

    play sound "static.mp3"
    scene utatunnel13 with flash
    stop sound

    u "We’ve never actually {i}seen{/i} anybody down here, though. And the only reason we know it’s connected to the old district is because we overheard some people talking about it at our old school."
    u "They always said this place was impossible to find, though. Which is weird because me and Io found it after, like...two nights of searching."
    s "Probably just another urban legend or something. Those are popular in schools nowadays, aren’t they?"
    u "Were they not when you went to school?"
    s "I...can’t remember much about school, to be honest. They might have been?"

    scene utatunnel14
    with dissolve

    u "Come to think of it, Kumon-mi High doesn’t really have any. At least none that can’t be traced back to stuff Nodoka makes up whenever she gets her crazy eyes."
    s "She’s not doing that in school now, is she?"

    scene utatunnel13
    with dissolve

    u "Oh, right. I guess you wouldn’t know unless somebody told you. But yeah — she’s been all sorts of weird ever since the Halloween party. In like a...less Nodoka-ish way, though."
    s "Which means...what, exactly?"
    u "Well, when she’s not going crazy, she mostly just keeps to herself now. I haven’t even seen her hit on Miss Watabe recently. That was the biggest tip that something was off."

    scene utatunnel15
    with fade

    s "Is there...anything else you’ve noticed?"
    u "With Nodoka?"
    s "Or anyone. I don’t normally ask Ami about what goes on in school, so..."
    u "Hmm...Kirin’s a little nicer. Chika’s...uhh...{i}odd.{/i} And I think Rin might like her again because she’s always staring at her recently."
    u "Oh, also! I want Noriko and Yumi to make out. Their sexual tension rivals even ours."
    s "Yumi is straight."

    play sound "static.mp3"
    scene utatunnel16 with flash
    stop sound

    u "She can have a curious phase! It happens to all of us. Just...mine happened to last forever. And is only worsened by the fact that everyone in our class is highly kissable."
    s "But none are more kissable than you, Uta."

    scene utatunnel17
    with dissolve

    u "Yet alas — no ring."
    s "You’re really set on this ring thing, huh?"

    scene utatunnel18
    with dissolve

    u "Believe it or not, I’m very traditional. I’m just also...highly irresponsible when it comes to...Internet communications."
    s "So, like...you {i}actually{/i} want to wait until marriage?"

    scene utatunnel19
    with dissolve

    u "I mean...I don’t think it has to be {i}marriage.{/i} But I’d definitely want to be dating somebody before anything actually {i}happens,{/i} you know?"
    s "So {i}that’s{/i} why you’ve so easily avoided my advances this whole time."

    scene utatunnel20
    with dissolve

    u "There’s also the fact that none of those “advances” have been real. It’s always just flirting."
    s "But-"
    u "Jerking off to mini-Uta doesn’t count. That’s not an advance either. But yeah, I’m all talk. I’m sure you’ve figured that out about me by now."
    s "You’re not {i}all{/i} talk if you keep putting yourself in situations like this where we’re all alone. Because the {i}last{/i} person who did that with me-"

    scene utatunnel21
    with dissolve

    u "Bzzt. No talking about other girls when your attention should be on Uta. You’ll make her jealous and cause what few morals she has left to begin blurring."
    s "You’re one of the most morally good people I know, Uta. You’ve just...done some questionable things out of loneliness in the past. Which isn’t bad. We all break every now and then."
    u "Yeah..."

    scene utatunnel22
    with dissolve

    u "In a way, though...me “breaking” brought us closer together."
    u "Like...if I’d never found out about the picture thing, I don’t know if I’d have {i}ever{/i} gotten the courage to tell you how I really feel. "

    play sound "vibrate.mp3"
    scene utatunnel23
    with dissolve

    u "So being unclean isn’t {i}all{/i} bad, right?"
    s "You’re not {i}unclean,{/i} Uta. "
    u "No, I’m just fap material for a whole bunch of horny losers all over the globe. "

    scene utatunnel24
    with dissolve

    u "Akira not included, of course."

    scene utatunnel25
    with dissolve

    s "Well, thank you for making an exception to-"
    u "God fucking damn it, it happened again."
    s "Wait, just now? Seriously?"

    scene utatunnel26
    with dissolve

    u "Yup! The timing’s so great that I get to worry about my phone being bugged now! Hooray!"
    s "Can’t you, like...turn it into the police or something?"

    scene utatunnel27
    with dissolve

    u "I do. Or...did. But after doing it a zillion times and nothing coming of it, I just don’t even find it worth it to file the reports anymore. "
    u "This person or...{i}people{/i} want to torment me. That much is obvious. All I can really do is just...learn how to deal with it, I guess."

    scene utatunnel28
    with dissolve

    u "Still sucks, though. But hey — I wanted attention and {i}now{/i} I’m getting it."
    s "You still shouldn’t have to deal with that."
    u "Yeah..."
    u "Maybe I should just ditch my phone entirely? Start living more...disconnected."
    s "You can be like me. Like 50%% of my phone usage is just telling Ami I’m going to be coming home late."

    scene utatunnel29
    with dissolve

    u "Or I could lean fully into the virtual world instead and coerce you into {i}connecting{/i} as well so we can follow each other and send each other selfies all day."
    s "I thought you couldn’t send picture messages?"
    u "Not normally. Social media exists, though. Don’t tell my parents."
    s "I’ve never wanted to join social media more than I do right now."

    scene utatunnel26
    with dissolve

    u "I’m very easy to coerce into sending nudes too!"
    s "Uta, come on-"

    scene utatunnel30
    with dissolve

    u "Do you want to see it?"
    s "What?"

    play sound "static.mp3"
    scene utatunnel31 with flash
    stop sound

    u "I hold in my hands what could potentially be the {i}holy grail{/i} of your spank bank until you finally make your move, Akira."
    s "You’re...seriously not {i}offering{/i} to-"
    u "I told you. It doesn’t bother me when {i}you{/i} see them. I {i}like{/i} the attention, remember? Don’t you want to see me literally {i}begging{/i} for it?"
    s "..."
    u "..."

    scene utatunnel32
    with dissolve

    u "Don’t you?..."
    s "{i}Yes.{/i} "
    s "That’s the problem."
    u "It’s...not, though."
    s "Didn’t you personally ask me if I wanted help? "
    s "Is {i}this{/i} really your answer to that? Tapping into my biggest weakness? My biggest flaw?"

    scene utatunnel33
    with dissolve

    u "Oh my god..."

    scene utatunnel34
    with dissolve

    u "You’re right...you’re so right! What the fuck am I doing?!"
    u "I’m sorry! I...it’s how I...feel better about...my...oh my god."

    scene utatunnel35
    with dissolve

    u "AAAAAH! Forget I said that! I...wasn’t thinking! I just...I saw it and my mind went to...aaah! I’m such a fucking whore! I’m such a desperate piece of filthy fucking-"
    s "Uta...stop."
    u "I wish I could! But I’m a useless piece of shit and I just can’t, Sensei! I can’t take it anymore! I can’t-"
    s "Akira."

    scene utatunnel36
    with dissolve

    u "Huh?..."
    s "You’re supposed to call me Akira now."
    u "..."
    s "..."

    scene utatunnel37
    with dissolve2

    u "..."
    s "..."
    u "How are you not disgusted by me?"
    s "I ask myself the same question constantly, just with the roles reversed."
    s "I’m far more abhorrent than you’ll ever be though, Uta."
    u "{i}Sniffle.{/i}"
    u "What does abhorrent mean?..."
    s "Repugnant."
    u "Oh..."
    u "{i}Sniffle.{/i}"
    u "What does repugnant mean?..."
    s "That I’m disgusting and undesirable and unfit for love."
    u "Then why am I still so horny?..."

    scene utatunnel38
    with dissolve2

    s "I think you’re just doomed to always feel that way until I become someone worthy of your time."
    u "There’s no one {i}more{/i} worthy of my time than you. I’d take every hand off every clock if it would help you realize that."
    s "What would you do about the digital ones?"
    u "I don’t know...turn them off, I guess. {i}Sniffle.{/i}"
    s "Here, use my sleeve. "
    u "No...{i}sniffle.{/i} I have a handkerchief...it’s okay. But thank you..."
    s "Of course. "
    s "So, is this the first time you’ve ever cried in a sewer?"
    u "Heheh...{i}sniffle.{/i} No...my bowstring snapped once and hit me in the eye. Io had to make me an eye patch and walk me out of here."
    s "Then I guess I can be thankful you’re still capable of moving around on your own right now."
    u "I don’t know, Akira...my body feels really heavy all of a sudden. I think you might have to carry me."
    s "Uta-"

    play sound "tackle.mp3"

    u "Ah...sweet death has come to claim poor Uta-chan..."
    u "So horny that...her body...simply could not go on any longer..."
    s "I’ll make sure to mark that down as a note for your gravestone once you get your head out of my lap. You’re on top of my phone."
    u "Oh, I thought that was something else."
    s "You thought my penis was rectangular?"
    u "No, I thought it was your wallet."
    s "Oh."

    play sound "tackle.mp3"

    u "What’s this?"
    s "{i}That{/i} is my penis."
    u "R..."
    u "Really?..."
    s "No, that’s my wallet."
    u "Mm! Akiraaaa! Don’t tease Uta-chan! She’s very sensitive right now! That’s- ah!"

    scene nightsky
    with dissolve2

    "I gently stroke her hair as she lays her head in my lap. Her ears are a shade of red so bright that they rival the fire beside us."

    u "What are you-"
    s "Trying to calm you down. Is it working?"
    u "Mm..."
    u "A little yes...a little no."
    s "Why not close your eyes then?"
    u "Close my eyes? But what if I fall asleep?"
    s "Well, we’d have two options. I could either put you to bed in that homeless person’s mattress...or I could carry you back to your room like you were begging me to do just a minute ago."
    u "Okay...can you make me a promise, though?"
    s "What’s that?"
    u "If I invite you inside once we get there...can you say no?"
    s "Uhh...{i}probably not.{/i}"
    u "Can you try?..."
    s "You...really want to keep waiting?"
    u "Mhm..."

    scene black
    with dissolve2
    stop music fadeout 12.0

    u "I kinda..."
    u "Never want this to end."
    s "..."
    u "But I also {i}really{/i} want you inside of me."
    s "Welp."
    u "Oh. {i}That’s{/i} gotta be your penis."
    s "Sure is, Uta. Thanks for just lying on it."
    u "It’s not a very good pillow. I’m going to adjust. ‘Scuse me!"
    s "I hate you..."

    "And..."
    "Something else I don’t want to say."

    $ renpy.end_replay()
    $ utaspring4 = True
    $ uta_love += 1

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump utaspring5

label utaspring5:
    scene utafirstkiss1
    with dissolve2
    play music "thesleepingcity.mp3"

    "She did wind up falling asleep, but she wouldn’t let me carry her back."
    "I offered, of course. I can’t imagine she weighs more than a large backpack. And considering I carry the burden of thousands if not millions of years of having my mind rewritten, I don’t think it’d be a problem."
    "We stopped by our gazebo, but only for a few minutes. Only out of habit."
    "It’s nearly 3:00 AM now. And while I feel bad for keeping her out so long, I’ve come to accept that she {i}wants{/i} this."
    "{i}Why{/i} she wants this, I’ll never be able to understand. But of course that’s just me {i}telling{/i} myself I’ll never be able to understand when, in all actuality, I was just like her once. Just more physical and less virtual."
    "I know what it’s like to want someone you shouldn’t. And while that’s taken on a new meaning as I’ve gotten older, I’ve sort of always been that way. "
    "Uta can still grow out of it, though. There’s a chance she realizes once more how close to destruction she is. There’s a chance {i}I{/i} could be the next one physically harmed for wanting her."
    "But there’s a problem."
    "I don’t {i}want{/i} to protect her. I want to hurt her. Every day. Every night. Every minute for the rest of my life — because there is something {i}different{/i} here. I just..."
    "I haven’t figured out how to explain it yet."

    u "..."
    s "..."
    u "I had fun tonight, Sensei."
    s "I’d hope so considering how late I kept you out."

    scene utafirstkiss2
    with dissolve

    u "If anything, I’d say that I’m the one who kept {i}you{/i} out by dragging you across town to a secret tunnel and then falling asleep in your lap."
    s "Yeah, I guess so. But on the bright side, the break in flirting gave my penis a chance to not be erect anymore. So that’s cool."

    scene utafirstkiss3
    with dissolve

    u "Reaaaaaally? Even though you’re right outside of my room? "
    s "I sure am. But this is just one more night of unending temptation since I know you aren’t actually going to invite me in."
    u "So? Doesn’t mean there won’t be fantasies. I know just how much you adore Uta {i}and{/i} Uta-chan. There is no escape from the effect I have on your penis."
    s "Same goes for you and the way you look at me then."

    scene utafirstkiss4
    with dissolve

    u "You wanna know what I’m gonna do when I get inside, Akira?..."
    s "Yes. A thousand times, yes."

    scene utafirstkiss5
    with dissolve

    u "Pass the frick out, that’s what. I’m still eepy from the lap-nap. And I’ve gotta wake up to get ready for school in like two hours."
    s "A tease right up ‘til the end. Like always."

    scene utafirstkiss6
    with dissolve

    u "That won’t ever change either. "
    s "Not even if we were together?"
    u "Probably {i}more{/i} if we were together. Teasing you makes me happy. It’s how I check to see you’re still interested. And the fact that you still are after all you’ve learned..."
    u "That means a lot to me."
    s "..."
    u "I hope we get to wake up next to each other some day."
    s "There’s always two hours from now."

    scene utafirstkiss7
    with dissolve

    u "Oh, please. We both know neither one of us would get to sleep at all if you came in tonight. "
    s "Yeah..."
    s "I guess I...should just let you go then."

    scene utafirstkiss6
    with dissolve

    u "Should you?"
    s "I mean, yeah. You’re tired. I’m tired. And if I don’t jerk off after all of this teasing, I think my dick is going to actually explode."
    u "Hm."
    s "Why? Second thoughts at work again? Am I actually going to be invited in after all?"
    u "No..."
    u "I just think you’re forgetting something."

    play sound "static.mp3"
    scene utafirstkiss8 with flash
    stop sound

    s "Forgetting something?"
    u "Mhm~"
    s "..."
    u "You know {i}I’m{/i} not gonna make the first move. That’s all on you, buddy."
    s "You...want me to kiss you?"
    u "Seems like a fitting way to end the night, doesn’t it? And you’ve missed a million other chances so far, so I figured I might give you a hint this time."
    s "..."
    u "Is there a problem? Because I know you want me. And you know I want you. So what’s the hold-up?"
    s "The hold-up is I won’t be able to stop myself."
    u "Sure you will. "
    s "I think you underestimate just how badly I want to fuck you right now."
    u "I think {i}you{/i} underestimate just how much you {i}actually{/i} like me. "
    u "And {i}because{/i} you like me, I know you aren’t going to do anything I’m not ready for."

    scene utafirstkiss9
    with dissolve

    u "Either way — worst case scenario is I’m wrong and I finally get to live out my number one fantasy of sleeping with you. I can’t really lose, can I?"

    scene black
    with dissolve2
    scene utafirstkiss10
    with dissolve2

    "Standing right in front of her always makes me feel like a giant — yet {i}she’s{/i} the one who seems confident right now."
    "I guess knowing what you want and only wanting {i}one{/i} thing can do that to a person. "
    "I’m the type who wants everything, though. So while I’ve become very skilled in terms of separating myself from {i}other{/i} desires in moments like this, I’m still not great at just accepting them."

    s "..."
    u "..."

    "But maybe..."
    "I can convince myself there {i}is{/i} only one thing I want."
    "And that it’s something she can give me."
    "Someone I can grow old with and die before. "
    "Someone who will tease me by day and pet me by night. Who will stay faithful so long as I am. "
    "Someone who can help me and hold me and a million other things I can already do with other people I have and know, but-"
    "Again..."
    "Something just feels different."

    s "The height disparity makes this difficult."
    u "The best things in life normally are."

    scene utafirstkiss11
    with dissolve2

    s "You’re sure about this?"
    u "More sure than you are, apparently. I’d have caved already if I was in your shoes. "
    u "But I fall hard and I fall quickly, so...maybe I’m just hoping I’ll be caught this time."

    scene utafirstkiss12
    with dissolve

    s "Uta Ushibori."
    u "Akira Arakawa."
    s "I do not have a ring...and I can not promise you that I am worthy of your time {i}or{/i} capable of remaining loyal to you. Do you accept this?"
    u "Yes. But know that I plan on crying a lot every time you break my heart in an effort to make you stop."
    s "I will not protect you...nor will I abandon you. You will give yourself to me and only me...and you will receive nothing in return. I can not make you happy and I can not sit still. Do you accept this?"
    u "Yes. I will give myself to you and only you. But it’s not like I won’t be getting anything back. It’s time for me to invest in you for a change."
    s "By entering into this unofficial covenant with me, you are hereby renouncing your quality as a human being and greatly reducing your self-worth. Do you accept?"
    u "Yes. You’ve always made me sound more valuable than I actually am anyway."
    s "..."
    u "Any more questions?"
    s "One more...and it’s big."
    u "I’m ready."
    s "Do you love me?"

    scene utafirstkiss13
    with dissolve2

    u "Yes..."
    u "A thousand times, yes..."

    scene utafirstkiss14
    with dissolve3
    $ renpy.pause(3, hard=True)
    scene black
    with dissolve2

    "And so one more wish comes true in this world of infinite possibilities."
    "But each and every one comes with a caveat."

    play sound "tackle.mp3"
    scene utafirstkiss15 with hpunch

    u "{i}Mmm!{/i}"

    "For Uta Ushibori abhorred the idea of entering into {i}any{/i} covenant with someone who didn’t plan on remaining loyal to her and her alone."
    "But in her mind, if this was the only way it could ever happen, she was willing to make certain concessions. "
    "After all, it was like she said — the best things in life normally {i}are{/i} difficult. And the fact that he was honest about this up front must count for something, right?"
    "In her constant observations of him, she had come to realize that several girls {i}didn’t{/i} know he was stringing them along. "
    "Was he only telling {i}her{/i} because he thought she wouldn’t care? That it didn’t matter because she really {i}was{/i} “easy?” No. No, that couldn’t be it. He actually liked her. She could tell. She could {i}feel{/i} it."
    "But she’d been feeling all sorts of things with no payoff lately. Something had to change."

    play sound "static.mp3"
    scene utafirstkiss16 with flash
    stop sound

    "But was this “change” really a change at all? Or was her history of giving herself to anyone who showed any amount of interest just setting her up for disaster once more?"

    u "Bye, Kyousuke! Bye, Tomo-kun! See you in lunch!"
    fg "Mmm! My bangs are acting up again. How am I supposed to face Koga-sensei like this?"

    scene utafirstkiss17
    with dissolve

    u "What are you talkin’ about?! You look fine! Just be yourself! That’s what boys {i}really{/i} like, isn’t it?"
    fg "Tch, easy for you to say. You get to go home to a cool older brother and all of his cool friends who probably walk around shirtless and...chop wood and...ugh! These bangs!"

    scene utafirstkiss18
    with dissolve

    u "My brother and his friends do not walk around shirtless and chop wood. I’m just repeating what I’ve heard the guys say."
    fg "There is zero way Kyousuke and Tomo-kun talk about liking girls who just “be themselves.” Boys our age only care about boobs."
    u "Y...Yeah..."

    scene utafirstkiss19
    with dissolve

    u "Yeah, I think we’re both kinda...done for in that department."
    fg "See, this is why I like Koga-sensei. A distinguished gentleman like him is most definitely the type to appreciate a girl for her personality, not her chest."

    scene utafirstkiss20
    with dissolve

    u "Why do you care so much about your bangs then?"
    fg "Shut up."
    xoxo "Akemi, have you really not heard the rumors about him lately?"
    fg "Rumors? What rumors? I haven’t heard anything. "
    xoxo "Somebody saw Koga-sensei walking out of a love hotel with a high school girl last week."

    scene utafirstkiss21
    with dissolve

    fg "What?! No. No, that can’t be true! He would never!"
    u "High school? Really? I thought you needed to be 18 to get into places like those."
    xoxo "Fake ID maybe? I heard a lot of places don’t even check. They sit behind these window things and just take your money."
    fg "Well, whatever you heard is definitely not true! Koga-sensei is refined and pure and-"

    scene utafirstkiss22
    with dissolve

    sb "Uta! Come to the cafeteria with us! They have curry today!"
    u "Maybe next time! I told one of the teachers I’d help them make copies of the handouts for tomorrow! "
    sb "Laaaaame! You’re still coming to Mizuya Chaya after school though, right?"
    u "Yup! I’ll meet you guys there! Later!"
    fg "So effortless. How do you even do that?"

    scene utafirstkiss23
    with dissolve

    u "Who? Me? Do what?"
    fg "Talk to boys! Isn’t he the fieldstop for the school baseball team?"
    u "Do you...mean shortstop?"
    fg "Whatever! You just talk to them like they’re no different from us! How?"
    u "I...just do? I’ve never really thought about it."
    xoxo "Suuuuure, Uta. Like we’re going to believe that."

    scene utafirstkiss24
    with dissolve

    u "What?! I’m being serious! I’ve known him and most of the other guys in our class since kindergarten. They barely even register as boys to me."
    xoxo "Mhm. Right. I’m sure that’s what Koga-sensei’s girlfriend would say too."

    scene black
    with dissolve

    fg "Oh my god, Becki! Stop! Koga-sensei doesn’t have a girlfriend! He-"
    u "Hey, do you guys know what time it is?"
    fg "Just look at the clock. I’m busy making myself beautiful."
    xoxo "It’s 11:33. Fourth period is-"
    u "Ahh, shoot! I didn’t realize it was that late! Sorry, guys! Gotta run! I told the teacher I’d have those copies done by next period!"
    fg "Okaaaay, but you’re still not forgiven for being friends with the baseball goalie!"
    xoxo "Are you just being dumb on purpose? Do you think that makes you cuter or something?"

    play sound "static.mp3"
    scene utafirstkiss25 with flash
    stop sound
    $ renpy.pause(4, hard=True)
    scene utafirstkiss26
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss27
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss28
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss29
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss30
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss31
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss32
    play sound "notif.mp3"
    scene utafirstkiss33 with dissolve2
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss34
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss35
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss36
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss37
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss38
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss39
    play sound "notif.mp3"
    $ renpy.pause(3, hard=True)
    scene utafirstkiss40
    with dissolve
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss41
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss42
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss43
    play sound "notif.mp3"
    $ renpy.pause(2.5, hard=True)
    scene utafirstkiss44
    play sound "notif.mp3"
    $ renpy.pause(2, hard=True)
    play sound "slidedoor.mp3"

    g1 "Hey, have you heard the rumor about Koga-sensei?"

    scene utafirstkiss45
    with dissolve

    g2 "How he was caught leaving a hotel with some high school girl? Duuuuh. Everyone’s heard that by now."
    g1 "I heard he got called into the principal’s office and put on “administrative leave” last period."
    g2 "Ugh, thank God. I had an essay due."
    g1 "Hahah! Thank Ushibori, not me."

    scene utafirstkiss46
    with fade

    g2 "Ushibori? You mean Uta? Why? What does she have to do with this?"
    g1 "I heard from Kyousuke’s group this morning that it was probably {i}her{/i} leaving that hotel with him, just wearing a different uniform as a disguise."

    scene utafirstkiss47
    with dissolve

    g2 "Uta? Are we thinking of the same girl? Tomboy Uta? “Only hangs out with boys after school” Uta?"
    g1 "That’s the one. You’ve seriously never noticed how close she is with like {i}all{/i} of the male teachers? She clearly has a thing for older guys."

    scene utafirstkiss48
    with dissolve

    g2 "No way. Kyousuke’s probably just trying to start something since she rejected him last year. Uta’s not like that."
    g1 "Hmm...do you think it could be like one of those compensated dating things then? Maybe her family’s poor? I heard her brother gets into a lot of fights. Maybe he’s in a gang or something?"
    g2 "You’ve been talking to Becki too much. Uta’s just an average girl. I doubt she’d be able to land Koga-sensei even {i}if{/i} he was into that."
    g1 "Maybe...I definitely wouldn’t blame her if she {i}did{/i} nail him, though. I know I would. Koga-sensei is a total hottie. "
    g2 "God, yes. Seven days a week."

    play sound "static.mp3"
    scene utafirstkiss49 with flash
    stop sound

    u "{i}Hah...{/i}"
    u "It was only a matter of time, Uta."
    u "You were always destined for this. "
    u "Everyone’s always known."
    u "..."
    u "Why couldn’t you just be normal?"

    scene utafirstkiss50
    with dissolve

    u "Why couldn’t you just fall for a boy your own age and..."
    u "..."
    u "Wait..."

    scene utafirstkiss51
    with dissolve2

    u "He never said it back..."
    u "..."
    u "He made me admit I love him...and he never even said it back."
    u "..."

    scene utafirstkiss50
    with dissolve

    u "Whatever. First kiss — complete. Future Uta can figure out how to make him love her."

    scene black
    with dissolve2
    stop music fadeout 10.0

    u "That’s all she ever thinks about anyway."

    $ renpy.end_replay()
    $ utaspring5 = True
    $ uta_love += 10

    "{i}Uta’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
