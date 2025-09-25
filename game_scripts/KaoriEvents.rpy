label callkaorimorning:
    if kaori_love >= 0 and kaoridate1 == False:
        jump kaoridate1
    if kaori_love >= 10 and kaoridate5 == True and kaoridate10 == False:
        jump kaoridate10
    if kaori_love >= 15 and day271 == True and yumicallnight35 == True and kaoridate15 == False:
        jump kaoridate15
    if chap4active == True:
        jump kaorispringmorninggen
    if chapthreeactive == True:
        jump kaorisummer2morninggen
    if christmas7 == True:
        jump kaorimorninggen2
    else:
        jump kaorigenmorning

label callkaoriafternoon:
    if kaoridate1 == False:
        play sound "phonebeep.wav"

        "I tap on Kaori's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        k "Greetings!"
        s "Hey, Kaori. What are you up to?"
        k "Ah! You have called me at a horrible time! I am currently chasing down a suspicious animal!"
        s "How is an animal suspicious? What is it doing?"
        k "Running away!"
        k "I must go!"
        k "Call me another time!"

        play sound "phonebeep.wav"

        s "..."

        "Kaori hangs up the phone and I'm forced to call someone else..."
        jump callafternoon
    if kaori_love >= 5 and halloween14 == True and dojo25 == True and tsuneyofirsthall == True and kaoridate1 == True and kaoridate5 == False:
        jump kaoridate5
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Kaori's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."

        jump callafternoon

    if chapthreeactive == True:
        jump kaorisummer2noongen
    if christmas7 == True:
        jump kaorinoongen2
    else:
        jump kaorigenafternoon

label callkaorinight:
    if kaori_love >= 20 and mayafestival4 == True and kaoridate20 == False:
        jump kaoridate20
    if ((totaldays >= 480) and (chap1point + chap2point >= 200) and (happypoint + happymiss >= 13) and (chikapoint + chikamiss >= 24) and
        (yumipoint >= 20) and (ayanepoint + ayanemiss >= 26) and (sanapoint + sanamiss >= 22) and (makotopoint + makotomiss >= 22) and (mikupoint >= 21) and
        (rinpoint + rinmiss >= 24) and (futabapoint + futabamiss >= 27) and (amipoint + amimiss >= 24) and (nikipoint >= 6) and
        (mayapoint + mayamiss >= 20) and (mollypoint >= 14) and (tsuneyopoint >= 14) and (utapoint >= 9) and (iopoint >= 9) and (otohapoint >= 9) and (nodokapoint >= 5)
        and (toukapoint >= 9) and (yasupoint >= 5) and (norikopoint >= 11) and (kirinpoint + kirinmiss >= 19) and (wakanapoint >= 2) and (osakopoint >= 2) and (yukipoint >= 4) and (tsubasapoint >= 2)
        and (sarapoint + saramiss >= 10) and (harukapoint + harukamiss >= 10) and (karinpoint + karinmiss >= 7) and (kaoripoint >= 7) and (makipoint + makimiss >= 7) and (chinamipoint >= 5) and (day == 6) and kaoridate25 == False):
            jump kaoridate25
    if kaori_love >= 35 and toukadorm25p3 == True and mayaspecial45 == True and nikilovesyou3 == True and nodokaspecial30p4 == True and kaorispecial35 == False:
        jump kaorispecial35
    if kaori_love >= 40 and kaorispecial40 == True and toukadorm25p3 == True and amiinvite4 == True and day == 6 and kaoridate40 == False:
        jump kaoridate40
    if kaori_love >= 45 and naospring1 == True and kaorispring2 == False:
        jump kaorispring2
    if chap4active == True:
        jump kaorispringnightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Kaori's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "No answer. She's probably working right now."
        "I guess I'll just call someone else."

        jump callnight

label kaorinoongen2:
    scene kaorinoongen2
    with dissolve
    play music "justbehappy.mp3"

    "I give Kaori a call and ultimately wind up meeting her near her house to go for a walk through the neighborhood."
    "I find out during this journey that Kaori is quite popular around here."
    "I mean, it would be hard not to be with how she looks- but it seems like most people genuinely like her."
    "Several old women out on their porches wave to her as we walk by but then shoot me confused glances as they've likely never seen her with another actual person."
    "It's cute at first but becomes strangely eery as virtually every porch has an old woman on it."
    "This neighborhood is odd..."

    scene black
    with dissolve

    if kaoridate15p3 == False:
        "We do several laps around what I assume is her block but I don't bother asking which house is hers."
        "I figure, sooner or later, I'm bound to wind up there. It's just a little strange asking to come over while we're still this early into our relationship with one another."
        "I should wait until I'm 100%% sure that Kaori isn't an alien to go into her residence as well."
        "Ami would be very mad at me if I were to be consumed by an enemy of humanity."
    else:
        "We do several laps around her block, talking about the different textures of animals and how feathers feel compared to things like fur or scales."
        "I'm sure you can probably guess who chose this conversation topic."
        "Either way, it eventually starts to get dark and Kaori announces that she must complete her nightly bathing ritual before heading to bed."
        "Already knowing full well that she will not allow me to watch said ritual, I shrug my shoulders and agree, heading home after one final lap around the block."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori's affection has increased to [kaori_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label kaorimorninggen2:
    scene kaorimorninggen2
    with dissolve
    play music "justbehappy.mp3"

    "I show up at the diner to see how Kaori's doing and she immediately asks her manager to go on break."
    "It wasn't my intention to show up here and disrupt the business but, well, I guess it is what it is now since Kaori clocks out and sits down at the table with me."
    "She offers to give me her {i}One free human meal{/i} of the day as thanks for coming to say hello to her but I turn it down as the poor girl needs to eat as well."
    "And I don't mean poor in the literal sense."
    "In fact, Kaori works so often at so many places that I feel like she should probably be loaded."
    "Maybe the fact she needs to keep working so much is a...testament to how bad she is with money?"

    scene black
    with dissolve

    "Either way, the two of us spend the next half hour trying to converse but failing miserably."
    "But despite her constant need to make things more difficult than they really are, she does show the desire to improve- and that alone is admirable."
    "I just wish it wasn't so taxing talking to her for extended periods of time."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori's affection has increased to [kaori_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kaorigenmorning:
    scene kaorifirstdate8
    with dissolve
    play music "normalday.mp3"

    "I give Kaori a call and find out that she's working at the diner per usual this morning."
    "She tells me about how slow it is and I take that as a hint to go over there and help her kill time, but I'm met with surprise upon actually showing up."
    "Apparently, not only does Kaori have a hard time comprehending human language, she has a hard time understanding the insinuations that come with it..."
    "But regardless, she's able to clock out for her break early and spends the next half hour asking me random questions about my favorite 'human foods' other than hamburgers."

    scene black
    with dissolve

    "I decide to cut the conversation about food short when I notice Kaori produce a notebook from her bag and begin to write things down."
    "I'm not exactly sure what notes she feels compelled to take right now, but I'm almost positive that knowing my favorite foods won't help her in any way, shape, or form."
    "Unfortunately for both of us, the half hour we have together goes by extremely quickly, and Kaori eventually has to start working again."
    "I try to make plans with her to hang out for a little longer next time, but I don't think she understands as she just blushes and runs into the back room..."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori's affection has increased to [kaori_love]{/i}!"
    "........."
    "......"
    "..."

    scene black
    with dissolve
    jump saturdayafternoon

label kaorigenafternoon:
    scene kaoriafternoongen
    with dissolve
    play music "justbehappy.mp3" fadein 3.0

    "I call Kaori to find out that she's currently wandering around her neighborhood looking for a place to purchase a cantaloupe."
    "I decide against asking her {i}why{/i} she so desperately needs this large melon in the middle of the day and, instead, elect to just go help her find it."
    "By the time I'm able to meet up with her, she's already forgotten what it was she was looking for, and the two of us just hang out and talk for a while instead."
    "And I use the word 'talk' loosely because I'm not even sure how to recap the conversation from a narrator's perspective."

    scene black
    with dissolve

    "Some time goes by before Kaori tells me she needs to go home and get ready for her shift at the bar."
    "It is just then that I realize Kaori {i}lives{/i} somewhere and doesn't just aimlessly wander from place to place in search of cats and melons."
    "I wonder what her house is like?..."
    "..."
    "Kaori drags me back to reality moments later and gives me a surprisingly enthusiastic fist-bump, which is apparently a thing she saw friends do on TV recently."
    "She quickly turns around and heads home and I am left confused and unsure of how to move on with my day..."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori's affection has increased to [kaori_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label kaoridate1:
    s "I wonder what Kaori is up to right now..."

    "I haven’t tried contacting Kaori ever since I got her phone number the other day, so
    I figure now is as good a time as any to get that ball rolling."
    "How that ball will end up when rolling in the direction of someone as...eccentric as her, I have no idea. But it’s at least worth a kick or two."

    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    k "Goodbye."
    s "Wait, what?"
    k "Did I make a mistake?"

    play music "lifeismostlygood.mp3"

    s "Yes, Kaori. That isn’t how you answer the phone."
    k "Apologies. I think I meant to say hello."
    k "This is the Hamburger Man, yes?"
    s "Correct. Do you not have me saved in your contacts or something?"
    k "There are no names in my contact list. Only the colors I expect people to like the most."
    s "You...saved my name as a color?"
    k "Yes."
    s "Well, what-"
    k "Actually no."
    k "For you, I wrote “clear.”"
    s "Clear isn’t a color..."
    k "I know."
    s "Okay, well-"
    k "What are you currently participating in, Hamburger Man?"
    s "Me? Nothing. I called because I was wondering if-"
    k "Let us go on what humans call a “date!”"

    "Woah, already?"
    "Kaori moves quick."

    s "Uhh, are you sure you’re okay with that? I kind of figured you’d want to at least talk more before-"
    k "Come to this address."

    play sound "phonebeep.wav"

    "I immediately receive a text from Kaori with nothing but numbers."

    s "Uh...Kaori?"
    k "Hamburger Man."
    s "I need the name of the street too."
    k "Do humans give names to streets the same way they award them to children for being born?"
    s "Kind of? Yeah. It's the name on the-"
    k "I remember now! Prepare for the beep!"

    play sound "phonebeep.wav"

    "The beep happens, I guess."
    "And, in other news, I have a full address now."

    k "Why is your body not in the same place as mine yet?"
    s "Probably because I can't teleport."
    k "That makes sense!"

    "I take another look at the address she texted me and realize that it isn’t too far from here."
    "I recognize the street name, but I’m not sure where I’ve seen it before."

    s "I'll head over in a few minutes, I just need to get dressed and-"
    k "I understand!"
    k "Hello!"

    play sound "phonebeep.wav"

    "..."
    "Aaaand, she’s gone."

    scene black
    with dissolve2

    "Shrugging off Kaori’s interesting end to our conversation, I get myself together and begin to head over to the address she sent me."
    "As soon as I set foot outside, I accept that there is absolutely no way this is a real date."
    "Even knowing that, though, I can't help but be a little intrigued by the prospect of getting to see what makes Kaori tick."
    "Here's hoping that she's a bit more...grounded today."
    "........."
    "......"
    "..."

    scene kaorifirstdate0
    with dissolve2

    s "So that's why the address looked familiar..."

    "I don't know why I even expected something else in the first place."
    "I stand in the lobby, waiting for Kaori to show up and explain why we’re here on her day off."
    "Or at least what I {i}hope{/i} is her day off."
    "A few customers busy eating their breakfast stare at me and make me feel slightly uncomfortable...but my “date” shows up seconds later to either quell that or make it ten times worse."

    scene kaorifirstdate1
    with dissolve

    k "You came!"
    s "I came. It would have been rude for me to tell you I’m coming and then just...not show up."
    k "Yes! That would have been a very bad thing!"
    k "But you are here! And now the human date can begin!"
    s "Just “date,” Kaori..."

    scene kaorifirstdate2
    with dissolve

    k "This language perplexes me."
    s "The trick is to just not add “human” before every single object."

    scene kaorifirstdate3
    with dissolve

    k "What does it mean to be “human?”"

    "Oh no. She’s turning into Maya."

    s "Let’s not worry about that for now. Would you mind explaining why we’re hanging out at the diner on your day off?"
    s "I figured you’d want to go somewhere else since you’re probably cooped up in here for an indeterminate amount of hours each week."
    k "Day off? What is this “day off” you speak of?"

    "Yup. Saw that coming."

    s "It...means a day that you’re not working."
    k "But I am working. That is why we’re at the diner."
    s "Kaori, why would you invite me here while you're working?"
    k "Is this not how a regular {i}date{/i} works?"
    s "Nope. A “date” is what you call it when two people who are romantically interested in one another go do stuff together."
    k "Oooooh...I see."

    scene kaorifirstdate4
    with dissolve

    k "Wait, what?!"
    k "What is this romantic interest you speak of?!"
    k "To think that I would make such a mistake in the heat of human mating season!"
    c1 "You can do it, Kaori!"
    c2 "We believe in you!"
    k "What are we supposed to do now?!"
    s "Relax. I kind of expected this was a misunderstanding."

    if kaoriprepared == True and bonus == True:
        k "Has the...time finally come to prepare my body?..."
        s "Kaori, why do you remember that? It was such a small part of that meeting."
        s "Besides, Rin would kill me if we were to do that while she's not here."
        k "How many humans must be present for the mating ritual to be successful?..."
        s "Just two. But there will be no mating ritual today."

    scene kaorifirstdate5
    with dissolve

    k "Okay...I will trust you, Hamburger Man."
    k "But only because you are one of the few people in this city that I know by name."
    s "But you don't-"

    scene kaorifirstdate6
    with dissolve

    k "Hamburger Man, would you like to consume hot meat with me for the breaking of my lunch?"
    s "Uhh...sure. Are you really going to take your lunch break this early, though? It’s not even 10:00 AM yet."

    scene kaorifirstdate7
    with dissolve

    k "You traversed many miles of harsh terrain in order to reach me and all {i}I{/i} did was misunderstand the meaning of the word “date.”"
    k "Now you must return home without having mated and it is all my fault."
    s "It wasn't even a two mile walk and I made like one turn. I will accept your apology for the mating thing, though."
    k "I will take my break early to spend time with the Hamburger Man. It is how I will correct my error."
    s "You really don't have to-"
    k "Please give me 300 seconds to tell the computer that I am hungry."

    "..."

    s "Sure. Go tell the computer, Kaori. I'll wait here."
    k "Thank you. I will return with slightly more freedom than I have right now."

    scene kaorifirstdate0
    with dissolve

    "Kaori disappears into the back room, leaving me once again uncomfortable and the center of attention."

    scene black
    with dissolve

    "I avert the gazes of various customers and take a seat at the closest booth, waiting for the Mistress of the Dark or whatever it is she calls herself to come back..."
    "........."
    "......"
    "..."

    scene kaorifirstdate8
    with dissolve

    "Kaori places a, you guessed it, hamburger in front of me and takes a seat on the opposite side of the table."
    "Honestly, if given the chance, I would have much preferred ordering something else this morning."
    "I love hamburgers, don’t get me wrong, but I love them significantly more when it isn’t 10:00 AM and I’m still trying to wake up."

    k "I am very glad that we are currently engaged in a real human date, Hamburger Man."
    s "Kaori, I already told you this isn't a real date. Please try to remember the meanings of things from now on as it will save both of us a great deal of time."

    scene kaorifirstdate9
    with dissolve

    k "But these customs and meanings are so hard to keep track of! I am just a girl with a spider tattoo and extra colors in my eyes, not a dictionary!"
    s "Wait, are those actually your real eyes?"

    scene kaorifirstdate10
    with dissolve

    k "Of course. Where would I procure fake ones?"
    s "I...have no idea. I was just under the impression those were colored contacts or something."
    k "Aren't contacts the names of the colors in your telephone?"
    s "Kaori, what planet were you born on?"

    scene kaorifirstdate11
    with dissolve

    k "I believe they told me it was some place called...Gunma?"
    s "Wait, who are {i}they?{/i}"
    s "Also, there's no way that's true. Gunma is in Japan."

    scene kaorifirstdate12
    with dissolve

    k "Hamburger Man! Don’t tell me you have forgotten where we are?"
    k "Do you require medical assistance? I am trained in CPR. Can you breathe? How many colors are there in the rainbow?"
    s "I don’t require medical assistance, Kaori. I just don’t understand how you’re still coming to terms with normal human behavior if you were born in Japan."
    s "It might sound crazy, but I was starting to think you were some sort of...alien or robot or something."

    scene kaorifirstdate13
    with dissolve

    k "That sounds very crazy. You are a crazy person. I am suddenly the normal person here."
    s "I still think I have a bit of an edge, all things considered."

    scene kaorifirstdate14
    with dissolve

    k "Wrong. You still have much to learn from me, grass-bug."
    s "It’s “grasshopper.”"
    k "I make the rules here, grass-bug. Not you."
    s "I’m actually kind of getting used to Hamburger Man, so if we can stick with that instead of grass-bug, it would be much appreciated."

    scene kaorifirstdate15
    with dissolve

    k "Good! Hamburger Man is a good name. And very fitting for someone who likes hot meat as much as yourself."
    k "However!"
    s "However what?"
    k "I like the new name too! So I hereby pronounce you..."
    k "Hamburger-bug!"
    s "Okay, that’s the worst nickname so far. Please don’t ever call me that again."
    k "Are we going to go on more “dates” in the future? Or do we need to “hang the outs” first? That is a term I learned recently!"
    s "Either you have the worst teacher in the world or you are gravely misremembering it."
    k "Please explain the process we must go through to become closer, Hamburger-bug Man! I must learn more things!"
    s "You know, I'm just going to go ahead and assume you {i}are{/i} romantically interested in me if you keep calling this a date."

    scene kaorifirstdate16
    with dissolve

    k "No! I am simply curious!"
    k "You have many interesting words and stories to share!"

    scene kaorifirstdate17
    with dissolve

    k "I do not have many colors in my phone..."
    k "Sometimes, when I think I’ve made what you would call a {i}friend...{/i}the friend just disappears."
    k "They all keep going away and I don’t understand why."
    k "What am I doing wrong, Hamburger-bug-burger-man-bug?"
    s "..."
    s "Kaori, can I ask you something? And don’t take this the wrong way."

    scene kaorifirstdate18
    with dissolve

    k "I will do my best."
    s "Do you...really talk like that on purpose? Or is it just a sort of...self-defense mechanism or something?"
    s "Like, you’re only talking that way because you want to stand out or seem unique in someone else’s eyes."
    s "Because if it’s anything like that, I want you to know that-"
    k "Talk like what? I don't understand."
    k "Is this about adding “human” to words again?"
    s "Uhh, well yeah. That’s...definitely part of it."
    k "What are the other parts? "
    k "I lack the type of education that you provide when you aren’t trafficking humans, but I am trying my best to learn."
    s "First off, please stop saying I’m a human trafficker."
    s "Second, the way you talk now is perfectly fine as long as you’re not intentionally trying to sound weird."
    s "Learning a language is tough. And I’m not sure how you got to the point you’re at now, but I’m glad to see you’re trying to get better."
    s "Just...keep practicing or something. A lot."

    scene kaorifirstdate19
    with dissolve

    k "Thank you Hamburger-bug! I really appreciate it."
    s "Please stop calling me that."
    k "I understand!"
    k "Since you have been a good person to me, I will give you a new name instead!"
    s "What is it this time? Grassburger? Hamhopper?"
    k "No! It is better!"
    k "You are now..."

    scene kaorifirstdate20
    with dissolve

    k "Friend!"

    scene black
    with dissolve2

    "Kaori and I talk for another twenty minutes before her break ends and she has to get back to work."
    "Not wanting to disturb her anymore, I pay the bill and take my leave."
    "Somehow, and I really don’t understand it- but I feel like I learned a lot about Kaori today."
    "That feeling drifts away the second I realize I could have probably talked her into giving me a discount, though."
    "Either way, I consider today's meeting a good first step in what I can now confirm is some sort of...friendship."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate1 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kaoridate5:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    k "Goodbye."
    k "Wait. No. I mean hello."
    k "Hello."
    k "Who is calling?"
    s "Hello, Kaori."
    k "Oh, Friend! Thank you for pressing the buttons required to make my voice appear through your telephone."
    s "You’re welcome."
    s "What are you up to?"
    k "I am wandering around the area surrounding my home with a different friend!"
    s "A different friend? You managed to make another?"
    k "I purchased this friend with real, human money! "
    s "You...bought a friend?"
    k "Yes! Come see! I am near the location where we ate the large wheel of cheese and dough together."
    s "Oh. Okay. That’s not that far from my place."
    s "I’ll head over now."
    k "Wonderful news! Hel- Uhh..."
    k "Goodbye!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Well, at least she’s trying."
    "I can’t imagine Kaori having {i}actually{/i} purchased a friend but, she’s been rather calm concerning human trafficking in the past, so I guess it’s not completely out of the question."
    "I’ll just have to wait and see what she meant."
    "........."
    "......"
    "..."

    scene kaorishugecock1
    with dissolve
    play music "justbehappy.mp3" fadein 5.0

    "I arrive in the residential district neighboring my own to find a rather joyful looking Kaori, all alone and minding her business near the waterway."
    "She runs over to me the second she sees me and just stares at me without saying anything."
    "It’s weird. But she has a cute smile so I let her do her thing and just...stare for a little while as I try to think of something to talk about."

    k "Today is a good, human day. "
    k "I was released from work early, I drank four cups of hot bean water, {i}and{/i} I got to rub a large, human cock for almost a whole hour!"
    s "..."
    s "Excuse me, what?"
    k "Hm? Which part are you confused about?"
    s "Which part do you think I’m confused about?"
    k "If you are questioning why I was released from work early it is because business was slow! "
    k "Which provided more time to rub the cock!"
    s "God I hope this is just a misunderstanding. "

    scene kaorishugecock2
    with dissolve

    k "What is wrong, Friend? "
    k "Would you also like to rub the cock?"
    k "I can show you all the best ways."
    s "This...{i}cock{/i}. Does it belong to your friend?"
    k "That is a strange combination of words. The cock {i}is{/i} my friend."
    k "Are you jealous that you do not have a huge cock as well?"
    s "I can assure you that I-"
    ahc "BACAWK!"
    s "..."
    k "What is wrong?"
    s "Did you hear that?"
    k "All I heard was the cock."

    scene kaorishugecock3
    with dissolve

    "I look down to find a “Large human cock” at my feet, squawking at cars as they pass by."

    s "I should have foreseen this."
    k "This is the cock that saved your life!"
    ahc "BACAWK (Sup, dude?)"

    "Do I have some secret power that allows me to understand animals?"
    "Also, is this Todd’s older relative or something? It’s basically just a super-sized version of him."
    "He’s so big that he’s almost up to Kaori’s waist. It’s kind of intimidating, to tell the truth."

    scene kaorishugecock4
    with dissolve

    k "I love this cock!"
    s "Kaori, please stop."
    s "Also, stop adding the word “Human” to places it doesn’t belong. I gravely misinterpreted what was happening before I showed up today."

    scene kaorishugecock5
    with dissolve

    k "What did I do incorrectly?"
    k "Is this not a cock after all? Because {i}I{/i} thought it was a chicken."
    k "But when I purchased it from the man at the Chinese restaurant, he continuously referred to it as a cock."
    k "He said “cock” so many times that I began to question if there were other animals I was also confused about."
    k "Please tell me what I am to call this creature, Friend."
    s "Chicken is fine. Cock is another word that works as well but...it also has a different meaning that’s very easy to misinterpret when you say things like, “I love this cock.”"

    scene kaorishugecock6
    with dissolve

    k "Different meaning?"
    k "What else does that word mean?"
    s "It’s slang for “penis.”"
    k "..."
    s "..."
    ahc "..."

    scene kaorishugecock7
    with dissolve

    k "Cock means...penis?..."
    k "As in...the male meat-stick?"
    k "And I...said all of those things about...loving it..."
    k "In the middle of a busy section of the...area I live in..."

    scene kaorishugecock8
    with hpunch

    k "And you allowed me to say these things?!"
    s "If it were up to me, I wouldn’t allow you to say things like “male meat-stick” either but here we are."
    k "John! Attack!"
    john "BACAWK! (Please forgive my master. She is a very confused girl.)"
    s "Got it. Thanks for not being as uptight as the other birds, John."
    john "BACAWK! (Any time, dude.)"
    k "Why are you communicating with my co...CHICKEN as if you are able to understand it?!"
    k "Please do not tell me you are fluent in chickenspeak as well as humanspeak, Friend!"
    s "I think I am but I’ve only really known about this power for a few minutes now."

    scene kaorishugecock9
    with dissolve

    k "Well...either way...I am relieved to know that I was able to at least save {i}one{/i} of the chickens from the secret chicken sanctuary."
    s "You mean the back alley?"
    k "Yes. The chicken sanctuary."
    s "It’s not really a sanctuary if that’s where the chickens were being stored before being slaughtered."
    john "BACAWK! (Wait, slaughtered?...But those other chickens were...)"
    s "My mistake, John. I’m sure they’re fine."
    john "BACAWK! (Oh. Cool. Was a little worried for a second there.)"

    "That’s good. It appears that all of those things I’ve heard about chickens not being the brightest are actually true after all."

    k "Since I was only able to obtain a single chicken, I decided to choose the one with a proven track record of helping others."
    k "I will defend this chicken with my life."
    k "I will die for it if the need arises."
    s "I can’t imagine that need ever arising, so I think you’ll be okay."
    s "It’s sweet of you to have chosen that chicken, but I’m surprised you were only able to afford one."
    s "Chickens are normally pretty cheap."

    scene kaorishugecock10
    with dissolve

    k "Are they?"
    k "I am not familiar with the chicken market so it is possible the chicken-killing-food-man took advantage of me."
    s "Does your place have room for him, though? He’s kind of large for a chicken."
    s "I think he’s even bigger than he was when he “rescued” me."
    k "He is. But I have been feeding him hamburgers in an effort to make him more like you."
    s "Okay well, first off, that’s adorable."
    s "Secondly, you probably shouldn’t feed a chicken hamburgers."
    john "BACAWK! (Bruh)"
    s "This is for your own good, John."

    scene kaorishugecock11
    with dissolve

    k "I see. Perhaps it is best to follow the chicken manual after all."
    s "There’s a...chicken manual?"

    scene black
    with dissolve

    "Kaori begins to retreat toward the bushes behind her and John follows suit, leaving me with the option of either bailing or following the two of them who have been attracting the eyes of nearly everyone around us."
    "And while I am no stranger to being seen with a huge cock, I will say that I feel slightly uncomfortable in this specific scenario."

    scene kaorishugecock12
    with dissolve

    "I take a seat next to Kaori and John manages to hop into the space between us."
    "He’s surprisingly agile for a gigantic chicken and I think he might even be able to give Todd a run for his money."
    "Also, why do I know the names of multiple chickens all of a sudden?"
    "What is happening to my life?"

    k "Have you ever saved a life, Friend?"
    s "Me? Not at all. We can’t {i}all{/i} be Kaori."
    s "You did a good thing. Even if that good thing probably cost like thirty or forty people dinner."
    k "While it is true that some may have their stomachs yell “Grrrrr” due to lack of chicken, the smiles John can gift to others will make up for it."
    s "You can’t survive off of just smiles, though."
    k "No but you can not survive with just food either!"
    k "Humans must combine nutrients and emotions to make their lives worth living!"
    k "Too much of one thing is bad. Except if that one thing is chickens."

    scene kaorishugecock13
    with dissolve

    k "I would still like to save more. But I should be happy with a cock this special."
    s "You did it again."

    scene kaorishugecock14

    k "Did what?"
    s "Said cock instead of chicken."

    scene kaorishugecock15

    k "S-Stop turning it into a dirty word! You know what I am speaking of!"
    k "I accept corrections of my normal speech but not when they are going to make my face get hot and my chest grow tight!"
    k "John, attack!"
    john "BACAWK! (But I’m so tired...)"
    s "Fine, fine. Call him whatever you want."
    s "I’m just glad you finally have someone to absorb all of that love you have to give."
    s "You’ve been trying to find a pet ever since I met you."
    s "And even though this one isn’t exactly normal...I’m sure it’ll give you all of those smiles that you apparently need to keep your human body healthy."

    scene kaorishugecock16
    with dissolve

    k "Yes, yes. I can feel my strength returning with each passing day."
    k "Soon, I will be able to master things like jumping the rope or treading the mill."
    s "Or, you could just go to the gym and practice those things like most other people who want to master them."
    k "The gyms in this area do not appreciate my crest."
    s "You mean your tattoo?"
    k "I do. Too many people either scream or ask to touch it."
    k "You are one of the few who has yet to do either. Which is one of the hundred and thirteen reasons we make good friends."
    k "There are likely more reasons but I have yet to write them down."
    s "Does...that mean you’ve physically written down over a hundred reasons already?"

    scene kaorishugecock17
    with dissolve

    k "Of course I have."
    k "Is that not common practice for human friends?"
    s "It’s really not."
    k "Oh."
    k "Well, I’m going to keep writing them down anyway since looking at them before I go to sleep makes me smile."
    s "Can I read them?"
    k "..."
    s "..."
    s "Kaori?"
    k "I wanted to say yes but the thought of you seeing the things I wrote suddenly makes me feel even stranger than the meat-sticks did."
    s "That’s fine. I don’t need to see them right away."
    s "I would appreciate it if I got to before you hit a thousand reasons, though."
    s "I can’t imagine being okay with reading any more than that."

    "But, to be fair, I don’t even think it’s possible to come up with that many reasons."
    "Hell, I’m impressed she was able to think up more than like, five."

    scene kaorishugecock18
    with dissolve

    k "I understand!"
    k "It is possible these strange feelings inside of me are the result of what humans call “puberty” as well."
    k "That seemed to be the popular result when I researched the way I was feeling on SpiderwebMD."
    s "That’s not a thing."
    k "Yes it is."
    s "Also, you’re too old for puberty. You’re what, 22?"
    k "In human years, yes. But 154 in dog years."
    k "Probably 155 now."
    k "Why is it that dogs move through space and time quicker than humans do, Friend?"
    k "Do you think they could bestow their knowledge unto us?"
    k "You seem to have the ability to speak with John, so perhaps you could speak to a dog as well?"
    k "If you speak to a dog, could you also inform him that I love him?"
    s "You haven’t even seen this fictional future-dog yet."
    k "I have not. But I love all dogs so I am sure I will love whichever one reveals the secrets of the universe to you."
    s "Sounds good, Kaori."
    s "I’ll make sure to include that in the conversation I will definitely have with a dog in the near future."

    scene kaorishugecock19
    with dissolve

    k "One more entry for the friendship journal!"
    k "Thank you very much!"

    scene black
    with dissolve2

    "Kaori and I (And I guess John) continue to chat for a while longer and eventually buy another pizza from that shop we’ve been to before."
    "Kaori only eats one slice and then feeds the rest to the chicken- something I would not advise actual chicken-owners to do."
    "Eventually, it comes time for me to leave and the two (Or three) of us part ways and head back to our respective homes."
    "I take a quick shower to get any residual farm-animal stench off of me before I put some fresh clothes on and head out the door..."

    $ renpy.end_replay()
    $ kaoridate5 = True
    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label kaoridate10:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."
    "She normally works around this time, so I imagine that’s what she’s doing now- but I think I’d still like to see her regardless."
    "In fact, I’m pretty positive that’s the case as I wouldn’t have selected her name without wanting that."
    "But I digress."

    play sound "phonebeep.wav"

    k "Greetings, Friend! I am very glad you telephoned!"

    "Oh, wow. An actual greeting this time."

    s "Oh yeah? And why is that?"
    k "I require the large, muscley tubes you have attached to your human shoulders."
    s "They are called arms. And why?"
    k "I have been asked to go to a place and get things but I can’t get things since my shoulder-tubes are weak and not good at lifting multiple objects at once."
    s "So I’m guessing you need help getting things from the store and bringing them back to your work?"
    k "My description was better. But yes!"
    k "Please come. I will pay you in what humans call “high fives.”"
    s "Humans don’t usually pay each other in those but okay. It’s not like I had anything else to do."
    k "That is great news!"
    k "Meet me at the store in twenty minutes!"

    play sound "phonebeep.wav"

    "Kaori hangs up the phone and I quickly find myself throwing on clothes before heading out the door."

    scene black
    with dissolve

    s "She never told me what store..."

    "........."
    "......"
    "..."

    scene kaoriconvenience1
    with dissolve
    play music "justbehappy.mp3" fadein 5.0

    k "I’m sorry again for never telling you where to meet me."
    k "I would have answered you sooner but my phone was on moon-mode so the harsh light of the sun would not destroy it."
    s "That moon icon is just the “Do not disturb” setting."
    k "That cannot be true as you were still able to disturb me."
    s "I..."
    s "Okay."
    k "And thank you for buying me this delicious sphere of cookie bread. "
    s "You haven’t even taken a bite yet."
    k "I am absorbing the scent through my pointed dual face openings."
    s "Nostrils. Or nose. Either one works. “Pointed dual face openings” is not an acceptable alternative."

    scene kaoriconvenience2
    with dissolve

    k "And also, thank you again for assisting me today."
    k "I never would have imagined that the strange man who wandered into my store with his adorable [niece] would one day traverse the streets of the city with me."
    k "This would probably be a dream come true if I were able to dream."
    s "That wouldn’t exactly be an exciting dream."
    k "Lies. I am filled with excitement. And also sugar as this is my third cookie bread."
    s "We’re only five feet outside of the store. How are you already on your third? That’s some Maya level speed."

    scene kaoriconvenience3
    with dissolve

    k "Maya?"
    k "What is a Maya?"
    k "Another small girl?"
    s "Yeah. My [niece]’s friend. You’ve probably seen her around since you work in like eighty-seven restaurants."
    k "What does she look like?"
    k "Does she have hair? Eyes?"
    k "How many eyes?"
    s "What? Two. And also yes, she has hair. Those are both normal things for humans to have."
    k "Then it is highly possible she has crossed my path. I have seen many girls with eyes."
    k "Sometimes, I stare at them for too long and they run away."
    s "That’s a standard reaction to staring at girls."
    k "Do girls also run from you, Friend?"
    s "Surprisingly, not really."
    k "That {i}is{/i} surprising. You are large and intimidating. "
    k "Your size is one of the main reasons I was excited for you to see me this morning."
    s "I’m glad that you’re using me for my ability to carry groceries."

    scene kaoriconvenience4
    with dissolve

    k "I would have done it myself but my shoulder-tubes are bad. They don’t move the way they should if I use them too much."
    s "Aren’t you using them all day in the restaurant?"
    k "Just for a few thousand milliseconds at a time. The time is negligible."
    s "Why do you know words like “negligible” but not “arms?”"

    scene kaoriconvenience5
    with dissolve

    k "The word used does not matter nearly as much as the meaning."
    k "It’s just like referring to a mother. Everyone has their own word and they all mean the same thing."
    k "Why is it not acceptable to do the same with objects or appendages?"
    s "Because those things are a lot less personal than a family member. But I guess it doesn’t really matter."
    k "It does not. You should know that as my teacher so that you do not charge me for your false instructions. "
    s "I already told you I’m not going to charge you for helping you with your...language skills. I’m doing this because I want you to succeed in the world."
    k "Your words sound kind but your face says you want me to fail."
    s "That’s just how my face looks. I can promise I don’t want you to fail."

    scene kaoriconvenience6
    with dissolve

    k "I appreciate your face. Even if it roots for my demise."
    s "Well...Thank you. I think."
    k "Apology accepted."
    s "..."

    scene kaoriconvenience7
    with dissolve

    k "Friend, I have a question for you. "
    k "Do you think that there are things in this world that are not worth fixing?"
    s "Like, things that are already broken or-"
    k "Or things that are bound to break."
    k "I feel weak and insignificant forcing someone so special to me to make up for what I lack in tube-strength."
    s "Again, I’m doing this because I want to."
    k "Yes but carrying bags does not make for an exciting date. We should be carrying each other's diaries from our elementary[school] years."
    s "What kind of weird expectation of a date is that?"
    k "It sounded fun in my head. I would like to see the things young-Friend thought when he was not so filled with anguish and meat."
    s "Hate to break it to you but I never had a diary. Those are more of a girl thing."

    scene kaoriconvenience8
    with dissolve

    k "Then what did you use as a boy to get your feelings out?"
    k "You were not the type to terrorize small animals or destroy mailboxes, were you?"
    s "Uhh, no."
    s "I don’t remember much about my childhood, but I’ve never really done anything to “get my feelings out.”"
    s "Even if I were to express something, I don’t know what it would be."
    k "Do you not feel?"
    s "I definitely feel."
    s "Just...not as much, I guess?"

    "What’s the use in self-expression anyway?"
    "Sure, you might get short bursts of self-satisfaction or the chance to reflect on ideas you’ve had in the past-"
    "But as time goes by, looking back on those things just brings more pain than it does anything else."
    "The fact that those fragments of your former self still float around in the ether until you’re unfortunate enough to watch them resurface is just further proof that we should all sit around and sulk until we die."
    "Love, me."

    k "Then do you not know happiness?"
    s "I know happiness just as much as I know sadness or anger. I just choose not to react to them."

    scene kaoriconvenience9
    with dissolve

    k "This makes me sad. I will now react, like a normal, non-Friend human."
    k "I want to see you smile the way I smile when I return to my living quarters and find John pecking away at a cooked fast food hamburger."
    s "Didn’t I tell you to stop feeding him h-"
    k "You told me no such thing. "

    scene kaoriconvenience10
    with dissolve

    k "If you are to not express joy when you are happy or tears when you cry, what am I to do as your friend?"
    k "I have no tears left in my body, but if I were to magically regenerate them and cry like a small human, I would want you to understand my sadness."
    s "You really don’t have to worry about me. I’m fine."

    scene kaoriconvenience11
    with dissolve

    k "No! It is exactly my job as a friend to worry. I shall not back down because you are afraid of happiness."
    s "I’m not {i}afraid{/i} of happiness..."
    k "Do you understand my concern, Friend? "
    s "Not really, but I don’t understand anything you do so I’ve kind of just accepted it at this point."
    k "I say these things to you so that you may find peace!"
    k "This world is filled with trouble! Horrible things!"
    k "But take heart, Friend. The Queen of Spiders has overcome this world!"
    k "And if I must overcome it once more to make you smile, I will! "
    k "Unless overcoming it again means returning John. That is where I draw the line."
    s "Returning your chicken wouldn’t really do anything for me either way, so I wouldn’t worry about that."

    scene kaoriconvenience12
    with dissolve

    k "All this being said, will you now attempt to express your feelings more?"
    k "Right now may not be a good time as your hands are clenched around the plastic handles of grocery-receptacles, but if you would like to try dancing I will promise not to laugh."
    s "Can we talk about something else? I can’t say I’m a fan of being coaxed out of the shell I’ve built around myself."
    k "We can talk about other shelled-creatures if you’d like."
    k "My personal favorite is the tortoise. "
    k "And if I had to choose which animal would represent you in an all-animal reenactment of our relationship, it is the third animal I would choose for the part."
    s "How about something completely unrelated to shelled-creatures? "
    k "Like what?"
    s "I don’t know. Tell me more about yourself."
    s "Were you always this...expressive when you were a kid?"

    scene kaoriconvenience13
    with dissolve

    k "You want to hear about Mini-Kaori?"
    s "You refer to your childhood self as Mini-Kaori?"
    k "She is the miniature version of me, so yes."

    scene kaoriconvenience14
    with dissolve

    k "My memories of those days are enshrouded in fog, so this may not be as true as it should be."
    k "But I believe I may have openly felt things not common of people in my age group."
    k "Mini-Kaori had just as many friends as she has now. Only one."
    k "But the old friend disappeared when I-"

    play sound "phonering.mp3"
    scene kaoriconvenience15
    with hpunch

    k "EEK!"

    "Kaori drops her melon bread on the ground the second her phone starts ringing."

    k "I forgot to align my phone with the moon again after responding to your cries for help!"
    k "The sudden noise startled me! My third cookie bread is ruined!"
    s "You should probably answer your phone, at least. It’s probably your work."
    s "We’ve been standing in this parking lot for quite some time now and my arms are starting to get tired anyway."
    k "R-Right! Telephone!"

    scene kaoriconvenience16
    with dissolve
    play sound "phonebeep.wav"

    k "T-Telephone?"
    s "Why are you holding it like that?"
    k "..."
    k "Uh-huh."
    k "The leeks are safe and secure in plastic containers carried by a large man."
    k "..."
    k "No, I am not in danger."
    k "He is my friend and he does not know how to express himself."
    s "Was that information really necessary to give out?"
    k "..."
    k "Yes, I will return shortly."

    scene kaoriconvenience17
    with dissolve

    k "..."
    k "No, I do not see one."
    s "See what? Now what are you talking about?"
    k "My manager said there was a large sky-football passing over the city."

    "She must be talking about a blimp."

    k "He knows how much I like them so I must remain vigilant in order to see it."
    s "What kind of person loves-"
    s "Actually, you’re exactly the kind of person that would love something like that."
    k "..."
    k "Heard."
    k "I will return before the sun begins to die."
    k "Sayonara."

    play sound "phonebeep.wav"
    scene kaoriconvenience18
    with dissolve

    "Kaori hangs up her phone and looks at me with a sudden flood of disappointment in her eyes."

    k "I am sorry, Friend, but I must return to work now."
    s "I mean, I still have to carry all of these for you, so you don’t have to say goodbye just yet."
    k "Oh. That is correct."
    k "If I took them from you, they would end up as dinner for the cement. And cement does not eat so this would benefit no one."
    s "I’m glad we’re on the same page."

    scene kaoriconvenience19
    with dissolve

    k "Thank you again for your assistance. "
    k "I promise to return the favor in the future once my arms return to their full strength and you suddenly begin to wither away into dust."
    s "I will keep that in mind..."

    scene black
    with dissolve2

    "The two of us continue our walk back to the diner and, within less than twenty minutes, we’re there."
    "Kaori and I part ways-"
    "But not before she remembers to pay me in roughly seven high-fives that she apparently believes are an actual form of human currency."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate10 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kaoridate15:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer. "
    "She’s typically working around this time but somehow always manages to pick up, so I’m not all that worried."
    "Granted, she also somehow always manages to be in every single place at once, so I’m pretty sure that there are either duplicates of her roaming around or that she’s just 90%% magic."

    play sound "phonebeep.wav"
    play music "remember.mp3"

    k "Phone call!"
    s "Well that’s a new greeting."
    k "Good morning, Friend! To what do I owe the talking today?"
    s "Just seeing what my favorite waitress is up to. Are you at work right now?"
    k "I am always at work! "
    s "Cool. Do you have time to go on break for a little bit if I swing by?"
    k "The whole day is a break! I do not have work!"
    s "But...you just said-"
    k "Friend, I have been having many lightbulbs inside of my brain and all of them are going BZZZZ BZZZZ and I believe it means there is something we must do!"
    s "Please continue to explain."
    k "I would like to spend the day with you and show you the light bulbs!"
    s "If this winds up being something like you literally needing help changing a light bulb I am going to lose interest very quickly."
    k "Darn!"
    s "Was that really what it was?"
    k "I don’t like sleeping in the dark, so sometimes my light bulbs get tired and need to take a break for the rest of forever."
    s "Isn’t one of your nicknames literally the Mistress of the Dark?"
    k "Mistress of the Burger! Let’s hang the outs for an entire day! Just you and me!"
    k "And John!"
    k "And John’s friends!"
    s "John has friends now?"
    k "Not yet! But I will explain when we get there!"
    s "Get {i}where{/i}, Kaori?"
    k "There!"
    k "I will see you soon!"
    k "Phone call!"

    play sound "phonebeep.wav"

    s "..."
    s "Phone call."

    scene black
    with dissolve

    "I decide to stop ever complaining about how Kaori starts or ends calls because, at this point, what would complaining even do?"
    "Despite not telling me where she wants to meet...I have a pretty good feeling that it’s in that alleyway with all of the chickens we’ve visited before."
    "Especially since today is apparently going to involve procuring friends for her obnoxiously large pet."
    "So, either Kaori’s landlord is about to hate her for turning her place into a chicken coop...or she somehow lives on a secret farm somewhere in the middle of Kumon-mi."
    "Both of these things seem entirely plausible for someone like her."
    "But I should probably start getting a move on if I don’t want her to wind up overpaying for a chicken or-"

    s "..."

    "God, what has happened to my life?"
    "........."
    "......"
    "..."

    scene kaoribigdate1
    with dissolve

    "Just as I expected, Kaori wanted to meet in the chicken alley- a real place that exists in Kumon-mi."
    "Well, apparently it’s not exactly a chicken alley anymore since, according to Kaori, the previous owner of the chickens recently sold them to another restaurant manager a few blocks down."
    "So the two of us make our way down this wind tunnel of a shortcut in hope of being able to purchase-"

    s "Wait, how many more chickens did you plan on buying?"
    k "As many as I can fit in my arm feet!"
    s "Hands. And I can’t imagine that is very many."
    k "Then Friend can help carry chickens as well since his arm feet are bigger and stronger!"
    s "Hands. Please stop calling them arm feet."
    k "Friend, do you know that John misses you? "
    s "How would I possibly know something like that, Kaori?"
    k "Chicken-sense! Friend-sense!"
    k "Like how I feel every time I know you are nearby!"
    s "I’m having a hard time believing you can somehow sense my presence based on nothing but our friendship."
    k "Maybe my friendship muscles are just stronger than yours?"
    s "Those aren’t even a-"
    k "Don’t doubt my feelings for you, Chickenburger Friend Man!"
    s "These names are getting out of arm feet."

    scene kaoribigdate2
    with dissolve

    k "Arm feet!"
    s "Oh God damnit."

    scene kaoribigdate3
    with dissolve

    k "Th...Thank you for coming today!"
    k "I was worried you would have turned your leg machines into escape mode when I told you I wanted to be with you for the entire day."
    s "No need to thank me. I’m the one who called you, remember?"
    k "Of course! It’s much easier to remember things from this morning than things from a long time ago."
    s "That is how memory works in most cases, yes."
    k "Are you good at remembering things, Friend?"
    s "..."
    s "Not exactly."
    k "Me too!"
    k "Did you also get hurt when you were a mini human?"

    play sound "static.mp3"
    scene happy9 with flash
    scene kaoribigdate3 with flash
    stop sound

    s "Also? "
    k "Yes!"
    k "I have told you about the juice before, yes?"

    "Ahh. I guess she’s talking about her apparent familiarity with hospitals again."
    "Am I actually about to learn why Kaori acts and speaks the way she does?"

    s "Yes. You have told me about the juice."
    s "What happened to you that...led you to the juice, though?"

    "That is absolutely not how I imagined ever asking anyone about their past."

    scene kaoribigdate4
    with dissolve

    k "WHAPAM! BOOM! KCHHHHHH!!"
    s "..."

    "And that is absolutely not how I imagined anyone ever explaining it."

    k "And on that day...a baby spider hatched!"
    k "The Mistress of the Burger Dark escaped the clutches of evil robots and started her new life as a superhero who saves furry or fluffy or feathery creatures!"

    "Or she’s just delusional."

    k "WHAPSSSSHHHHHHH!!!"

    "She is definitely delusional."

    s "What are the sound effects for, Kaori?"

    scene kaoribigdate5
    with dissolve

    k "Sound effects?"
    s "Those...sounds you were making."
    k "Do you not know Latin, Friend?"
    s "No...And neither do you."
    k "“WHAPSSSSHHHHHHH!!!” is Latinspeak for “Life is good now!”"
    s "..."
    k "..."
    s "Are you sure it was okay for you to leave the hospital?"

    scene kaoribigdate6
    with dissolve

    k "Yes! My yoke is easy and my burden is light! "
    k "There is no reason to stay in one place when the juice is but juice and the animals are elsewhere!"
    k "And so I ask you, Friend of Friends, to help me acquire more of you!"

    scene kaoribigdate7
    with dissolve

    k "To multiply the friendship in the world by a kadrillionbilliontrillion and-"

    stop music fadeout 5.0
    scene kaoribigdate8
    with dissolve

    k "Huh?"
    s "What’s wrong?"
    k "There’s nothing in the cages."
    k "This is where I was told that John’s friends would be."
    k "Do non-Kaori humans normally take chickens inside to roam around during the morning? "
    s "..."
    s "No. That’s not normally a thing non-Kaori humans do."

    scene kaoribigdate9
    with dissolve

    k "Should we find four-legged foldable rectangles to sit on them in wait of our new friends’ arrival?"
    s "Are you absolutely sure this is the right place?"
    k "Yes! I checked the address the last chicken seller gave me many times!"
    k "It is why I am not carrying food items today!"
    s "Kaori..."

    scene kaoribigdate10
    with dissolve

    k "Why do you say my name with so much sadness?"
    s "I think that maybe we’re just..."
    s "A little too late."
    k "Too late?..."
    k "Did someone else purchase the friends before I could?"
    s "Either that or-"

    play sound "static.mp3"
    scene happy9 with flash
    scene kaoribigdate11
    with flash
    stop sound
    play music "contemplation.mp3"

    k "Or what?"
    s "..."
    k "If you know what happened, please tell me."
    k "Our day can not continue until I acquire at least one new companion."
    s "When you asked the previous owner of the chickens where they’d be, what did he tell you?"
    k "That I could see them if I went to this building."
    k "But I don’t see anything at all."
    s "He didn’t tell you you could buy them, though?"
    k "He said it wasn’t up to him since they were no longer in his possession."
    s "And they were sold to another restaurant?"
    k "Yes. Another one that will not hire me. The one we are behind right now."
    s "Then...they were probably used already."
    k "Used?"
    s "Killed."

    scene kaoribigdate12
    with dissolve2

    k "..."
    k "I see."
    s "..."
    k "..."
    s "..."
    k "..."
    s "..."
    k "..."
    s "..."
    k "..."

    scene kaoribigdate13
    with dissolve

    s "..."
    k "..."
    s "Are you okay?"
    k "Friend. Can I ask you a question?"
    s "Sure. Go ahead."

    scene kaoribigdate14
    with dissolve

    k "What happens when something dies?"
    s "..."
    s "That’s not an easy question to answer."
    k "Why not?"
    s "Because it’s not really something anyone knows."
    s "For us, the ones who haven’t died, life continues to move on...albeit a little bit slower than before."
    s "But for the ones that do die, they just...stop existing."
    s "Or get reborn or sent to heaven or some other afterlife. Different people will tell you different things."
    k "What will you tell me? I trust you more than anyone else I know."
    s "I would tell you not to worry too much about it. "
    k "Because you don’t want me to be sad?"
    s "Right."
    k "But I’m already sad."
    s "..."
    k "..."
    s "Do you like poetry, Kaori?"
    k "Poetry?"
    k "Like....knock knock poems?"
    s "Those are called jokes."
    s "Poems are weird combinations of words that exist to make people feel certain ways or think certain things."
    k "Like laughter?"
    s "Sometimes, yes."
    k "How is that different from a joke?"
    s "I...don’t know."
    s "I’m not really good when it comes to cheering people up, but there’s part of a poem that just popped into my head that...might explain death a little better than I can."
    s "The only thing is that you’re going to have to imagine I’m the one who died or it will be a little awkward and not make as much sense."

    scene kaoribigdate15
    with dissolve

    k "This poem makes me feel very bad!"
    s "The poem hasn’t even started..."
    s "If imagining me dead doesn’t help, just...imagine me as one of the chickens or something."
    k "Ahh! Zombie chicken!"
    s "..."
    s "Anyway, the poem goes like this."

    scene kaoribigdate16
    with dissolve

    s "Death is nothing at all. It does not count."
    s "I have only slipped away into the next room. Nothing has happened."
    s "Everything remains exactly as it was. I am I, and you are you-"
    s "And the old life that we lived so fondly together is untouched, unchanged. Whatever we were to each other, that we are still."
    s "...And then there’s a bunch of other shit, but you should be able to get the point."
    s "Basically, life’s going to be exactly the same and this is nothing but a hiccup, even if you get all depressed right now."
    s "Also, you should be thankful that I don’t think of you as an actual human being, because doing that with anyone else is not something I think I’d be able to live down."
    k "I had no idea Friend was so good with words! Did you write that?"
    s "No. I haven’t written anything in a very long time."

    scene kaoribigdate17
    with dissolve

    k "Well your poem did not make me feel better, but I am impressed by how smart you are to remember so many things!"
    s "Thanks. But this wasn’t really about trying to show you how smart I am."
    k "No no! This is a good thing!"
    k "You said you were bad at remembering, but you remembered all of those words!"
    k "Do you know any poems about chickens?"
    s "Are you sure that hearing about chickens will make you feel better when chickens are kind of the reason you’re upset in the first place?"
    k "I am not sad because of the chickens."
    k "I am sad because of how cruel human beings can be."
    k "But you have reminded me that not everyone is evil by confusing me with your strange knock knock joke."


    scene black
    with dissolve

    "Kaori turns around and begins to walk over to a strange table full of random objects several feet behind us."
    "I’m sure it’s something just used by the employees of one of these restaurants for their breaks or something along those lines, but I can’t help but feel like it’s eerily out of place."
    "She lifts up a stuffed rabbit and hugs it tightly before sitting down and starting to play with its ears."

    scene kaoribigdate18
    with dissolve

    k "When Mini-Kaori got hurt a long time ago, she learned that the people she used to live with got hurt a lot worse."
    k "So bad that they disappeared forever. Like one of my light bulbs."
    k "But Mini-Kaori didn’t remember those people when she woke up, so she didn’t feel any pain other than what was in her body."
    k "If losing friends I never became friends with is as painful as this, what should Mini-Kaori have felt when people she actually loved died?"
    s "Worse. Which is why I’m confused about your smile right now."
    k "If I don’t smile, my eye-water will come rushing out and Friend will need to squeeze me to make me feel better."
    s "I’m fine with squeezing you if you want to cry, you know."
    s "Just don’t expect another poem or any advice or something like that."
    k "If you squeeze me, you must squeeze this rabbit as well! He is a replacement friend to help me cope with the death of John number two through however many I could fit in my arm feet!"
    s "You know, I feel like this is a good opportunity to teach you about stealing being wrong, but whoever left all this stuff out here is basically asking for it to be stolen."

    scene kaoribigdate19
    with dissolve

    k "I am very sorry our fun day together had to begin with such despair. "
    k "Do you feel your shadow growing larger, Friend?"
    s "It’s...about the same?"

    scene kaoribigdate20
    with dissolve

    k "Then we should leave this place and go somewhere even more exciting!"
    s "Pretty much anywhere would be more exciting than a random alleyway several blocks away from one of your workplaces."
    k "Then take me to the most exciting place you know!"
    k "A place where normal female humans like me can have a good time with their normal male friends after suffering great loss!"
    s "..."
    k "A place with things I can consume because I have the hunger!"
    s "..."

    scene black
    with dissolve

    "The most exciting place I know, huh?"
    "..."
    "That can only mean one thing."

    $ renpy.end_replay()
    $ kaoridate15 = True
    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

label kaoridate15p2:
    scene kaorimaidcafe1
    with dissolve
    play music "maidcafe.mp3" fadein 3.0

    k "..."
    s "..."
    k "This establishment is what I imagine the inside of a strawberry feels like."
    s "Exciting, right?"
    k "Where are we, Friend?"
    s "This is a maid cafe. "
    k "I hope they wash their hands before making our food because maids are known to get very dirty."
    s "Right, because they normally clean."

    if bonus == True:
        k "And perform unspeakable acts on anyone willing to pay them enough money."
        k "Are you going to make me watch you do something strange?"
        k "If it will make our friendship stronger, I am willing. But I may make strange noises out of interest and/or fear."
        s "You know, I didn’t think you knew about those kinds of maids."

    s "This isn’t that kind of place, though. The maids here just...say and do a bunch of cute stuff."
    s "Do you remember Ami? "
    k "The pretty girl with the red hair that you were trying to sell the first time you came to the doughnut diner?"
    s "I wasn’t trying to {i}sell{/i} her..."
    k "Do you think she would be friends with John? I have more wealth-paper than I expected to have at this point in the day and I would like to make a purchase if so."
    s "You can’t buy my-"
    s "Actually, how much are you willing to spend?"
    k "I have 50,000 yen moneys right now."
    s "You were going to pay 50,000 yen for chickens?"

    scene kaorimaidcafe2
    with dissolve

    k "I was going to pay for {i}friendship{/i}."
    s "..."
    s "Okay, fine. You can have her."
    s "Make sure she still comes over to cook me breakfast in the morning, though."

    scene kaorimaidcafe3
    with dissolve

    k "My happiness has increased!"

    scene kaorimaidcafe4
    with dissolve

    k "But my sadness is still immeasurable because she may be pretty, but does not have any feathers..."

    scene kaorimaidcafe5
    with dissolve

    a "Um...Sensei?"
    s "About time. I had to seat myself because you and Uta were yelling about stuff in the kitchen."
    a "Well...she brought her beetle to work and..."
    a "Actually, that doesn’t matter. Why are you with the spider waitress?..."
    a "And why does she look so upset?..."
    s "She just purchased you because she needs a friend for her chicken and is also currently in mourning."
    a "..."
    k "Woe is the Queen of Spiders."

    scene kaorimaidcafe6
    with dissolve

    u "Master...what’s the meaning of all these weird expressions at one table?"
    s "So, my companion here just purchased Ami because she needs a friend for her chicken and is also currently in mourning."
    u "..."
    a "..."

    scene kaorimaidcafe7
    with dissolve

    u "Works for me!"
    u "You two on a date or somethin’? Gonna take her back to your place and give her the good ole push and pray?"
    u "She check in with her mom yet?"
    a "Kaori, if Sensei invites you to his house, make sure you say no. Okay?"

    if bonus == True:
        k "Of course. If there is anything I have learned about this man, it is that he sells girls your age to the black market and that many of them are likely stored in his very home."
        a "That’s absolutely true and you should never go there. Save yourself."
    else:
        k "I will never go to Hamburger Friend's house. It is likely filled with mustard and other unfavorable condiments."

    s "Okay, okay. That’s enough badmouthing me for one afternoon."
    s "I come to you two with a mission that I was not able to complete myself."

    scene kaorimaidcafe8
    with dissolve

    u "A mission? That you needed to come here for?"
    s "Kaori is upset and I am very bad at dealing with sad people."
    a "She’s not...upset because of something you did, is she?"
    k "Friendburger told me the worst knock knock joke I’ve ever heard and then asked me to pretend he was dead."

    scene kaorimaidcafe9
    with dissolve

    u "{i}That{/i} was how you tried to cheer up a sad girl?"
    s "...It was the other way around. The “pretend I’m dead” part came first."
    a "I am somehow not surprised at all."
    u "Master, Master, Master...That’s not even close to what you’re supposed to do when somebody leans on you for help."

    scene kaorimaidcafe10
    with dissolve

    u "You’ve gotta approach her real nice and soft-like..."
    a "Mhm, mhm."
    u "Then you’ve gotta look deep into her eyes, like there’s nobody else in the whole wide world."
    a "Mhm!"
    u "And then grab her face as hard as you can and plant one right on her lips."
    u "And if she opens her mouth, that means it’s okay to slip in a little tongue."
    a "Right! And-"

    scene kaorimaidcafe11
    with hpunch

    a "Wait, no! Are you kidding me?! "
    a "That’s not even close to what he should be doing to cheer people up!"
    a "Forcing things like that on girls is assault! I should have you arrested for even suggesting that, Uta-chan!"
    s "Wow, keeping the “chan” in and everything. You’re getting good at this, Ami."
    a "I’ll get fired if I break character!"
    k "Tongue? Mouth? Open? Character?"
    k "I’ve never done this kiss move before. What if I sneeze?"
    u "Heheheh...girls. Am I right?"
    s "What does that even mean?..."
    u "{i}You’re racking up new ladies so quickly that you should know exactly what it means, Master.{/i}"
    u "{i}How many bases have you two touched yet? Three? Four? Five?{/i}"
    s "{i}You should ask your roommate about how baseball works before referring to it in a sexual manner.{/i}"

    scene kaorimaidcafe12
    with dissolve

    k "My body is prepared!"
    k "I will accept the tongue now!"
    s "Could you two just step aside for a second and-"
    a "Not a chance, {i}Master.{/i}"
    a "I doubt she’s even upset in the first place. "
    a "You’re just playing some sort of trick on Uta and me because you know we have to go along with it."
    a "I can see through you, {i}Master.{/i}"
    s "She really is upset, though. She’s dealing with death for the first time in her life."

    scene kaorimaidcafe13
    with dissolve

    u "Do you know what you want to eat yet, Princess Kaori?"
    k "One chicken sandwich please."

    "Or...maybe she’s over it already?"

    a "Oh..."
    a "I thought that {i}in mourning{/i} thing was just you exaggerating...I didn’t realize she-"

    scene kaorimaidcafe14
    with dissolve

    if bonus == True:
        k "Do not waste your worry feelings on me, pretty strawberry girl! Just come to my house and rub some cock and everything will be okay!"
    else:
        k "A euphemism once stood here!"

    a "...Excuse me?"
    u "I think she’s talking about a chicken."
    u "Or at least I {i}hope{/i} she’s talking about a chicken."

    scene kaorimaidcafe15
    with dissolve

    u "Or do I?..."
    a "How about we just...do what we normally do here and make you feel all...welcome and warm inside?"
    k "Friend already told me this was not that kind of establishment. But if you think that will make me feel better...okay!"
    k "I already prepared my body so I will not interfere with your job. I understand that you need to make yen moneys just like everyone else."
    a "Yes...by {i}serving you food and saying nice things to you because anything else would be illegal.{/i}"

    scene kaorimaidcafe16
    with dissolve

    u "Oh, that’s not true."
    a "It’s...not?"
    u "Nope! We can do {i}special{/i} stuff for the customers whenever we want as long as they’re willing to pay for it."

    scene kaorimaidcafe17
    with dissolve

    a "We can?! What?!"
    u "Yeah. I do it for Sensei all the time. He’s basically addicted."

    scene kaorimaidcafe18
    with dissolve

    a "He is?!"
    u "Yeah. You should see the look on his face whenever I finish. It’s {i}adooooorable.{/i}"
    u "I’ve even done it for Maya a few times but she doesn’t seem to be as big of a fan. Except for the one time I did it for them together. "
    u "She pretended to not like it, but I know she did."

    scene kaorimaidcafe19
    with dissolve

    a "AAAAAAHHHHHHH!!!!!"
    s "She’s obviously talking about the flavor beam, Ami."
    a "I FIGURED THAT OUT ALREADY BUT IT’S STILL-"

    scene kaorimaidcafe20
    with dissolve

    a "Wait, what do you mean “for them together?” Did Sensei come here with Maya?"
    u "Ah! No! That never happened! "
    u "Just part of the joke! I’ve never seen them together even once!"
    s "I’m sorry, Kaori. Things are normally a little more...focused than this."
    k "I am very confused but having a large amount of fun!"
    s "Well I’m glad you’re no longer being pushed down by the weight of mortality on your..."
    s "Do you have a special word for shoulders?"
    k "What is a shoulder?"
    s "The thing your shoulder tubes are attached to."
    k "Ooooooooh. A {i}shoulder.{/i}"
    s "...Yes."

    scene kaorimaidcafe21
    with dissolve

    u "So, uhh...anyway! Princess Kaori! We’re not really supposed to do this but...I know just the thing to perk you right up!"

    if bonus == True:
        k "I don’t know if I’m prepared enough to handle special services from two maids at once!"
        u "Uhhhhhhhhhh that’s not what I’m talkin’ about!"
    else:
        k "I knew I would receive at least one extra chicken today!"
        u "Uhhhhhhhhhh that’s not what I’m talkin’ about!"

    u "I was gonna ask if you wanted to try on one of the outfits that Ami and I are wearing. "

    scene kaorimaidcafe22
    with dissolve

    u "Sometimes, when I’m feelin’ down...I throw this thing on and look at myself in the mirror and think, “Woah! I can be this cute?!”"
    u "And then I do a little twirl and a jump thingy and...boom! I stomp those negative emotions into the ground!"
    k "I don’t know...the spider will get out if I become a maid."
    u "That’s totally fine. I’ve got a beetle in the back and they can be friends or something! Just put the little guy in a cage and-"
    s "She’s talking about a tattoo."
    a "Yeah...it’s a really big one too. I remember it."
    a "We’d have to be careful not to let any customers see it."
    u "We can be quick about it if you really wanna try, Princess Kaori. This is a special favor from Uta-chan and Ami-chan that we’re not even gonna charge ya for!"
    u "We can call it the...sad girl special!"

    scene kaorimaidcafe23
    with dissolve

    k "..."
    s "...?"
    s "Do you want me to...give you permission or something?"
    k "If I return as Kaori-chan, will you still be my friend?"
    s "Of course. In fact, I’ll probably like you even more."
    s "I don’t know if bringing you here gave it away or not, but I kind of have a thing for maids."
    u "Yeah, you’ve got a real problem, Master. But that’s why we like you so much."
    k "..."
    k "Just for a few hundred seconds then..."

    scene black
    with dissolve

    "Uta grabs Kaori by the wrist and pulls her down the hall into the restroom. "
    "Ami follows slowly behind, looking back at me once before disappearing in there as well."
    "The two maids exit the restroom three separate times, each time bringing either a new piece of the costume or a replacement for one that didn’t fit and..."
    "After a few minutes go by..."

    scene kaorimaidcafe24
    with dissolve

    s "Oh my God."
    a "Okay...that’s long enough, right?"
    u "Are you in love yet, Master?"
    k "Loveburger?!"
    s "That looks really good on you, Kaori."
    u "Kaori-{i}chan{/i}. She’s a part of the family now."
    s "You don’t...work here now, do you?"
    k "I don’t...think so?"
    k "Do I...look strange?"
    s "I literally just told you that you look good."
    k "Does good mean strange?"
    s "Good means good, Kaori-chan."

    scene kaorimaidcafe25
    with dissolve

    k "Th...Thank you...Master!"
    u "Ah! You called him Master and everything! You’re a natural, Kaori-chan!"
    k "Some restaurants require you to address human customers with special human names so I am...just adapting..."
    u "That’s a great human answer! I’m so proud of you!"

    "Uta really is good at caring for people, huh?"

    a "Okaaaaay...that’s definitely long enough..."

    scene kaorimaidcafe26
    with dissolve

    u "Us maids can’t really make your troubles go away for good...but we can always help you feel a little better while you’re here."
    u "So if you ever find yourself wanting a place to relax and forget about stuff, you know where to find us. Kay?"
    u "And also remember that real change comes from within! "
    u "If you’re ever gonna get over whatever hurdle you’re havin’ trouble jumpin’, throw on a cute costume, do a little twirl, and boom!"
    u "Suddenly you’ll be able to jump a lot higher."
    k "Thank you, tiny raspberry child. This building is very far from the building that I sleep in, so I will likely not come often."
    k "But I will remember you and your soft hands for the rest of my human life."

    scene kaorimaidcafe27
    with dissolve

    u "And you..."
    s "Huh? What about me?"

    if bonus == True:
        u "You just worry about keepin’ {i}your{/i} hands to yourself."
        u "This precious angel here’s just like me."
        s "A total flirt who’s secretly too nervous to ever actually do anything?"
    else:
        u "You can just shut the fuck up for a second and let me do my job."
        s "Uta, you deliver some of the most inconsistent customer service I've ever had."
        s "Kaori is my buddy and an angel and I am trusting you with her body. If you're going to get all nervous and start being mean-"

    scene kaorimaidcafe28
    with dissolve

    u "No! I mean she’s delicate and you’ve gotta treat her with care!"
    u "You think I’m nervous?!"
    k "An...angel..."
    k "That sounds nice..."
    s "Are you feeling better now?"
    k "Yes..."
    k "And I am also ready to return to my normal clothes because this outfit is very thin and I am very cold."

    scene black
    with dissolve2

    "The three girls return to the restroom and get Kaori dressed up in her winter clothes again."
    "Thankfully, no other customers showed up in the time she’d been out in the open, so there was no commotion surrounding her tattoo or anything like that."
    "Eventually, Ami and Uta-"
    "Or, excuse me, Ami-chan and Uta-chan show up with a whole spread of food to cheer Kaori up that we’re even given a discount on."
    "It seems like a great gesture at first, and I go through the entire meal feeling rather appreciative for the two of them-"
    "But as Kaori and I begin to head back outside, I notice a handwritten sign on the door advertising the exact “discount” they gave us as a lunch special."
    "I don’t know why I expected any less given the type of establishment this is...but at least I got to see Kaori get dressed up completely free of charge."
    "And that’s worth more than pretty much any discount out there..."

    $ renpy.end_replay()
    $ kaoridate15p2 = True
    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

label kaoridate15p3:
    scene nightsky
    with dissolve4
    play music "sanctuary.mp3"

    "It’s funny how you can gradually drift from one place to somewhere on the complete opposite side of the {s}world{/s} town without ever realizing it until it’s time to go home."
    "Well, I suppose that “funny” isn’t the right word to describe that phenomenon."
    "And I suppose that “phenomenon” isn’t the right word to describe the act of simply walking."
    "But let’s say for a moment that neither Kaori nor myself walked anywhere and only happened upon places like the chicken alley and the maid cafe by wishing ourselves there."
    "If I could, I’d like to wish myself back home to avoid having to deal with the now miles we must traverse on account of Kaori not wanting to ride a bus."
    "Or, as she referred to it- a motorized wheely mega-car."
    "Regardless, our journey begins at a time when everything has already quieted down, leaving myself and one of many surprisingly loud girls I know to find things to converse about."
    "We talk about animals and machinery and the prospect of mechanized animals that you don’t have to feed."
    "Pets who would go on to live forever, completely avoiding the sometimes immediate need to console others as they come face to face with death when they least expect it."
    "These strange, fictional creatures we come up with sound quite nice."
    "And it ultimately leads me to the idea of a world in which I could just replace {i}everyone{/i} and {i}everything{/i} with a mechanized version."
    "That way, I’d never have to worry about doing something that breaks them."
    "Because I could always take them to a repair shop or something along those lines if they wound up going haywire."
    "Or, if I read the control manual really hard and paid close attention to how the machines operated, I could learn how to shut them off and do as I pleased with them whenever I wanted."
    "This is not a specific thing that Kaori and I talk about, but one of many things that pop into my mind as we round corner after corner, likely getting lost along the way."
    "Neither of us have any idea where we’re going."
    "Kaori says she does, but she’s also the same girl who refers to hands as “arm feet” and chickens as “friends.”"
    "She’s just as broken as I am. "
    "But what isn’t broken around here?"
    "I feel what I think at first to be a raindrop land on my head, only to realize seconds after that it was melted snow disembarking from the gutter of a closed fish market."
    "I run my hand through my hair and bid goodbye to the droplet as it attempts to rejoin the water cycle."
    "And then a strange girl begins to say more strange things."

    scene kaorijourney1
    with dissolve

    k "Friend! Now that the sun has fallen asleep, we can begin to ask each other more interesting questions!"
    k "Like what colors we think whales are or how far we think we could throw a leg-hand-ball!"
    s "Football. And are those really your ideas of “more interesting questions?”"
    k "I want to know everything there is to know about you! I am just choosing the most interesting topics first."
    s "Why not choose something we’d be able to keep talking about after I answer?"
    k "Hmm..."
    k "Okay!"
    k "Describe to me your ideal world!"

    scene kaorijourney2
    with dissolve

    s "Huh. That’s actually a pretty good one. Why not ask things like that more often?"
    k "Long conversations make the skin flaps that cover my eyes feel heavy and, before long, I have to open my mouth really wide to lighten them."
    k "It is a strange process that I do not yet understand, but is almost always almost successful!"
    s "Almost always almost successful?"
    k "It works occasionally."
    k "Now, please proceed to tell me about the things you would do to this world if only you could."
    s "..."

    "I think about whether or not I should come clean about my newfound desire to replace everyone with machines and then decide against it because-"
    "In a sense, breaking can be beautiful too."
    "It doesn’t make me {i}happy{/i} to see people in bad conditions, but it does make everything around me feel kind of like Kaori’s eye flaps after she opens her mouth really wide."
    "It all gets lighter."
    "Everything stops falling and floats instead."
    "And so I decide to speak from the heart about the world I would create if only I could."

    s "I think the world we live in now is fine."
    s "Miserable, but fine."
    s "Weirdly enough, I think a world without misery would be even more miserable. So I’m perfectly content with where we are now."
    k "There is nothing at all you would change?"
    k "You would not turn the clouds into candy or put a smile on the sun?"
    s "Those are just visual changes. They wouldn’t really affect our day-to-day lives in any way."
    k "Raining candy would affect my daily life in many ways!"
    k "My teeth would become very bad and it would eventually become much harder to grind up food with them."
    s "Either way, I don’t really know what else I would change. "

    "Besides the machine thing, but I’ve already decided against telling her that."

    play sound "static.mp3"
    scene happy9 with flash
    scene kaorijourney3 with flash
    stop sound

    k "Liar."
    s "...I’m sorry?"

    scene kaorijourney4
    with dissolve

    k "There are many things you would change. "
    k "I know this for sure because you never smile."
    k "Who would want to live on a giant floating ball where they are incapable of contorting their facial muscles into the most important look there is?"
    s "I don’t know."
    s "Someone who’s already given up, I guess."

    scene kaorijourney5
    with dissolve

    k "Never give up, Friendburger Man!"
    k "If this world can not make you smile, all you have to do is create a new one!"
    k "Put a bunch of your favorite things into a box and shake it really hard! "
    k "What comes out will probably be really small because your arm feet can’t hold a box as big as the world."
    k "But if you close your eyes, you can pretend to jump into it and then smile once you get there!"
    k "Every day is special. But the days where your facial muscles are working properly are even more special than that."
    s "Your positivity can be really overwhelming at times, Kaori."
    k "Does it make you sad? "
    s "Not really."
    k "You appear to have caught the sadness."
    s "I have not “caught the sadness.”"
    k "It must have possessed you when it left my body in the maid realm."
    s "It’ll come back. There’s plenty more misery to be experienced in your life, I’m sure."
    k "The raspberry child told me the secret to expelling it, so everything will be kay-okay from now on."
    s "A-Okay. And sure, if that’s what you want to believe, go ahead and believe it."
    s "I’ll probably wind up being there when things get bad again, so I’ll do whatever it is I can to help as long as it’s not a major inconvenience."

    scene kaorijourney6
    with dissolve

    k "I hereby name you...Sadburger Friend Man!"
    s "I feel like I’ve doubled my nickname count today."
    k "You are a very sad burger."
    k "But since you attempted to give happiness back to me, I will now share some of it with you!"

    scene kaorijourney7
    with dissolve

    k "Would you like to see my apartment, Friend-Sad-Man-Burger-Chan?"
    k "I have heard that human males get very excited when they enter the domain of the opposite sex."
    s "I mean...I’m fine with that. But are you sure you are?"
    k "Yes! I have already informed you that John misses you! And he will be very excited to have company!"
    k "The cock will perk right up!"
    s "It already kind of is."
    k "Then the things I heard were true! Isn’t that excellent?"

    "Kaori...really does make it difficult to wallow in self-pity when she’s around."
    "Not that what I was feeling is self-pity or anything."
    "I’d probably call it something more like a melancholic longing or a...resigned exhaustion."
    "Some combination of words I’m sure she wouldn’t be able to grasp considering that it wasn’t until today that she really came to terms with how dark this place can be at times."

    play sound "static.mp3"
    scene happy9 with flash
    scene kaorijourney3 with flash
    stop sound

    k "You should stop thinking so much."

    scene kaorijourney7
    with dissolve

    s "What? "
    k "It’s no fun carrying on a talk-marathon by myself and your brain keeps going BZZZ BZZZ from the sadness cloud inside of it."
    s "The cloud normally hangs {i}over{/i} a person’s head, not inside of it."
    k "The sky is naked tonight and there are no clouds anywhere! So you must have eaten them!"
    s "..."
    s "We have to be getting close to your place by now, right?"
    k "Are your lower arm tubes also tired from all the stepping?"
    s "No, it’s just getting a little hard to keep up with a conversation that is half about my ideal world and half about noises inside of my brain."
    k "Then wish for a world where there are no noises in your brain!"
    s "That’s not really the problem here."

    scene kaorijourney8
    with dissolve

    k "Then what is, Friend?"
    k "How can I make the clouds disappear?"
    k "Ask and it shall be given."
    s "..."
    s "All I ask is that I don’t randomly wake up somewhere else one day and have to start over."
    k "You can ask for more, Friend."
    s "I’m selfish enough as is."
    k "If you are selfish, why did you tell me knock knock poems and buy me a chicken sandwich?"
    k "Is that a thing a selfish person would do?"
    s "It’s definitely not a thing {i}I{/i} would normally do. "
    s "I just have a bit of a soft spot for you, I guess."
    k "Can you tell me where the spot is so I do not accidentally touch it?"
    k "There is one part of me that the coated juice people say I can not let anyone touch no matter what."
    k "I do not want your insides to turn to mush."
    s "It’s a phrase. It means that I give you special treatment."

    scene kaorijourney9
    with dissolve

    k "Yes! That is what friendship is!"
    k "We give each other special treatment and help each other defeat sadness clouds!"
    k "Since you made my clouds go away, I, too, will destroy the BZZZ BZZZ inside of you."
    s "And what if the “BZZZ BZZZ” comes back tomorrow when you’re not around? "
    s "Are you going to quit work and become my personal the[rapist] or something?"
    k "Do not worry about tomorrow, for tomorrow will bring its own worries. Today’s trouble is enough for today."
    s "..."
    k "..."
    s "You’re so fucking weird, Kaori."

    scene kaorijourney10
    with dissolve2

    y "..."
    y "..."
    y "..."

    scene kaorijourney11
    with dissolve

    y "..."
    y "..."
    y "..."

    scene black
    with dissolve2

    "Kaori and I have to walk for what I believe is another hour until we finally make it to her apartment."
    "She remains insistent on “cheering me up” the entire way back but, to be completely honest, I feel exactly the same as I always do."
    "I imagine she just feels indebted to me after spending the day with her and using roughly half of it to push her over the hill that is death-"
    "But inviting me back to her place alone is more than enough to repay that debt."
    "I’m just hoping she may have heard a little more about what normally happens {i}after{/i} inviting someone in, though."
    "........."
    "......"
    "..."

    scene kaorijourney12
    with dissolve

    k "This is the building that I go to sleep in!"
    k "I would first like to show you the door. "
    k "Please look at the door."
    s "Okay...done."
    k "This concludes the outside portion of the tour!"
    k "I will now show you the inside of the sleep building."
    k "Please follow me, Friend-Burger-Sad-Burger-Chan-Burger."

    scene black
    with dissolve
    play sound "lock.mp3"

    s "You added “burger” way too many times. You’re just messing with me at this point..."

    play sound "dooropen.mp3"
    scene kaorijourney13
    with dissolve

    "I set foot inside of the “sleep building” and am immediately greeted by a rather small one bedroom flat with a half kitchen also serving as the entryway."
    "And, of course, Kaori’s best friend is there to say hello."

    john "BACAWK! (Ayo whaaaaaat? Man the fuck you doin’ walkin’ up in here like this?)"
    s "Hey, John. Long time, no see."
    john "BACAWK! (Yo take yo’ god damn shoes off, man. The hell you thinkin’?)"
    s "Oh. Sorry about that."

    "I kick my shoes off behind me as Kaori makes her way into the living room slash bedroom as well."

    scene kaorijourney14
    with dissolve

    k "Friend, why do you remove your foot protectors?"
    s "Because...that’s the polite thing to do."
    k "Do you intend to stay very long?"
    s "Are we...going somewhere else or something?"
    k "No. But now that you have seen my apartment, does this not mean that the final out has been hung and that the day is complete?"
    s "Did you think inviting me in just meant showing me where you lived and then...nothing else?"
    john "BACAWK (Oof. That’s rough, man.)"
    s "Stay out of this, John."

    scene kaorijourney15
    with dissolve

    k "I have never had another human in my room before. I do not know the rules."
    s "There aren’t really “rules.” I just figured I’d at least get to stay in here and talk for a while longer or something."
    k "But I must take off all of my clothing and lay in the water for at least an hour before I close my eyes and go into the sleep!"
    s "..."
    s "Can I watch?"

    scene kaorijourney16
    with dissolve

    john "..."

    "John doesn’t say anything but I know he’s judging me."

    k "Wh-wh-wh-wh-wh-wh-wh..."
    s "...Wh?"

    scene kaorijourney17
    with dissolve

    k "WHPSHHHHH!!!!"
    s "..."
    s "Was that Latin for “Get out?”"
    k "Mhm!"
    k "I’m sorry, Friend, but I unprepared my body to make room for more energy on the way home from Strawberry World!"
    s "That is absolutely not the name of the maid cafe."

    "Actually...what {i}is{/i} the name of the maid cafe?"

    scene kaorijourney18
    with dissolve

    k "I apologize for not properly understanding this time-honored tradition."
    k "But I...do not want to show you the things that you want to see just yet..."
    k "Will rubbing the co- Will rubbing John make you feel any better?"
    john "BACAWK! (I’m game if you are, man.)"
    s "Uhh..."
    s "Actually...I’ll just head out. My place isn’t all that far from here anyway."
    k "Despite the ending and my horrible mistake, I was happy to spend so much time with you today, Friend."
    k "I hope your clouds are gone."
    s "Yeah..."
    s "They’re gone."
    s "Goodnight, Kaori. "

    scene kaorijourney19
    with dissolve

    k "{i}Best{/i}night, Friend. It is better than good."
    s "Sure..."
    s "Bestnight it is, then."

    scene black
    with dissolve

    "I exit Kaori’s apartment and find myself arriving back at my porch in no time at all."
    "I don’t want to say that today was smooth sailing the whole way through or anything like that."
    "In fact, the water was pretty harsh all day long."
    "But, some way or another, we managed to avoid crashing into any rogue waves and came out with a bond much stronger than before."
    "I mean, I know where Kaori lives now."
    "And it looked exceedingly {i}normal{/i} apart from the giant chicken, so that in itself was a huge surprise."
    "I just hope that I can actually spend more than thirty seconds in there some day."
    "For now, though...it makes sense."
    "{i}She{/i} might not make sense, but the situation does."
    "And I should probably learn a little more about her before I expect her to start “properly upholding any time honored traditions” with me..."

    $ renpy.end_replay()
    $ kaori_love += 3
    $ kaoridate15p3 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kaoridate20:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and-"

    play sound "phonebeep.wav"

    k "Friend! Help! A horrible thing has occurred!"

    "Okay. No time for a pre-phone call briefing, I guess."

    s "What’s wrong, Kaori?"
    k "It is John! He has disappeared! "
    k "He was here a moment ago, but the hardened rectangle of pre-cooked wheat strings I placed in a hot metal cylinder full of sky blood required my attention!"
    s "...What?"

    if bonus == True:
        k "My large cock has disappeared! But my dinner was delicious!"
    else:
        k "The chicken is gone!"

    s "Do you...want me to come over and help find him?"
    k "Coming over will not help! I have already told you he is not here!"
    s "I just meant that I can meet up with you and we can look for him together."
    k "Are my sight-spheres not good enough to see what is before them?! Will an additional pair be worth the effort?!"
    s "I don’t know, Kaori. I’m just trying to help."
    k "Then come quickly! Use your muscular movement tubes to drag you to the place I fall asleep in!"
    s "I am...on my way. I’ll see you soon."
    k "You’re welcome! Hello!"

    play sound "phonebeep.wav"
    stop music fadeout 5.0
    scene black
    with dissolve

    "I hang up the phone and begin making my way over to Kaori’s place."
    "I’m not exactly sure how a giant chicken just...disappears, but I highly doubt Kaori would be throwing as much of a fit as she is if it wasn’t true."
    "I’m also not sure if it’s possible for him to have just stepped outside on account of the whole “no opposable thumbs to open doors” thing, but I’m sure the two of us will manage to figure it out soon enough."
    "Or not and he’s already dead."

    if bonus == True:
        "But, and this may make me sound like Kaori for a moment, so I apologize in advance- cocks that large are strong and resilient."
    else:
        "But, and this may make me sound like Kaori for a moment, so I apologize in advance- wshwshwshwshwshwsh!!!"

    "And I’m sure he’s fine, wherever he is."
    "........."
    "......"
    "..."

    scene kaorislostcock1
    with dissolve2
    play music "sanctuary.mp3"

    k "AAAAAAAAAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!"
    s "I’m great, thanks. And how are you?"
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"
    s "Weird emotion. I’m not sure if I follow."
    k "This is no time for joking, Friend! {i}Other{/i} Friend is lost and afraid somewhere! I am very lonely without him! And I do not want him to end up like the other chickens!"
    s "If it’s any consolation, I feel like the initial reaction to seeing a chicken of that size wouldn’t be to kill it, but to capture it and put it on display somewhere."

    scene kaorislostcock2
    with dissolve

    k "That is even worse! "
    s "Than death?..."
    k "John has fright of the stage variety! He is a living creature with human feelings and human desires! And most of those desires are not meant to be shared with others!"
    s "Ignoring your chicken’s apparent {i}human{/i} characteristics, standing around here won’t do us any good."
    s "I doubt he’s made it very far and, even if he has, he’ll be easy to spot. Now put your shoes on so we can go look for him."
    s "Unless you think standing around and yelling his name will make him come back."
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"
    s "Kaori, stop."

    scene kaorislostcock3
    with dissolve

    k "He is my only feathered friend, Friend! All of my other two friends do not have feathers- and I recently learned that one of them is an aunt and does not count as a {i}real{/i} friend!"
    k "It does not change the amount of feathered friends I possess either way, but I would still enjoy having more than zero of them!"
    k "Zero is the smallest number there is not counting the hyphen numbers!"
    s "I believe those are called negatives. "

    scene kaorislostcock4
    with dissolve

    k "{i}You{/i} are negative! I am trying to remain hopeful!"
    s "Kaori. Shoes."
    k "What are shoes?!"
    s "They’re...uhh..."
    s "Protective leg-hand containers?"

    scene kaorislostcock2
    with dissolve

    k "Why did you not just say so?! "
    k "We’ve spent all of these minutes allowing the clock to breathe while my cock runs rampant throughout the city! What if anyone saw?!"
    s "Kaori. Containers."
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "Kaori eventually calms down enough to put her {i}shoes{/i} on and follow me outside."
    "She has a tough time doing so on account of her trembling hands but, seeing as I’m a bit overdue when it comes to doing any good deeds, I help her get them on so we can begin our search."

    scene clearnightsky
    with dissolve2

    k "John! Where are you currently located?! Relay your coordinates to me so that our physical presences may rejoin in one location!"
    s "You can just say “Where are you?” you know."
    k "Do you believe that I have not tried this?! I have used so many different combinations of words! And yet, no chicken! Not even a peep!"
    k "Wait! Friend! Can you imitate a chicken noise? Maybe John has not returned because I can not properly speak his language?"
    s "I’m not going to make a chicken noise. What we need to be doing is thinking of places he might be."
    s "Did John have any...favorite hang out spots? Or...are there any places the two of you would visit together?"
    k "Well...he always came with me to the muggy laundry building to drown my clothes in soap sauce. But I do not think that is somewhere he would go of his own choosing."
    k "Perhaps he is visiting one of the many local shops of convenient purchasing? Or paying a visit to the dark alley full of kittens that we-"
    k "Wait! Chicken!"
    s "What? Do you see something?"
    k "No! Chicken, Friend!"
    s "..."
    s "What?"
    k "They always come home to roost! Just like the saying goes!"
    k "What if John became sick of our home and wanted to return to his old home?! For roosting purposes!"
    s "You think he returned to that alley we got him from?"
    k "I do not know where else he would possibly go! But the distance between here and there is great and I do not know if he can remember how to get there!"
    k "The brains of chickens are small and can not hold as many pictures of the past as the ones inside of our large, human heads. "
    k "Friend, that alley is dangerous. We can not let John return. I refuse to let him be cut down by the hands that slayed his brethren!"
    k "He only is my rock and my salvation! My fortress! I shall not be shaken!"
    s "Well, I have no idea where that place was, so you’re going to have to lead us there if you ever want to see your cock again."
    k "I remember where it is! Follow me, Friend!"
    k "John! We are coming!"
    k "Hang in there!!!"

    scene black
    with dissolve2

    "Kaori grabs my wrist and takes off toward the alley of mysterious chickens."
    "Or the alley that {i}used to{/i} house mysterious chickens, only to cut them down and teach Kaori about death long before she was prepared to learn."
    "As a relatively-functioning-ish adult, though, that’s something she needed to come to terms with as soon as possible."
    "You’d think that losing her entire family would be enough for her to really understand the gravity of something as terrible as death, but...nope."
    "I guess that John is the closest thing she’s had to family ever since starting her “new” life, though- which is a little strange to think considering she has {i}actual{/i} family now."
    "But John is clearly important to her."
    "And for her sake-"
    "I hope she doesn’t have to experience something as horrible as that a-"

    k "John! There you are!"

    play sound "static.mp3"
    scene kaorislostcock5 with flash
    stop sound

    k "What do you think you’re doing, coming back to this place?! You know the secrets it holds! The blood on its non-existent arm feet!"
    john "Bacawk. (Look no further, and do not follow- for I have felt the sands of time beneath my talons and know the weight they carry when burned into glass)."
    john "Bacawk. (This body ripens with meat of greater animals and strengthens me so. I can see things you would not believe.)"
    john "Bacawk. (Here, atop this precipice of all that is unholy, yet singed by the light of sacred soils...I beseech you please- let me be.)"
    john "Bacawk. (Let me walk the path that I am destined to walk. Drink in the blood of those that I have lost. Sleep in the comfort of the ghostly arms of a loved one.)"
    john "Bacawk. (All I ask is to be pure. All I ask is to be cleansed.)"
    john "Bacawk. (I have followed the light into naught but darkness. There is nothing here. There is nothing left to gain.)"
    k "I do not speak chicken, John! I can not understand what you want! But I know that this is not a safe place for you!"
    john "Bacawk. (You there. Human.)"
    s "..."
    s "What, me?"
    john "Bacawk. (Yes. You. The one who listens but seldom speaks. The thief who comes to steal and kill and destroy. He who understands.)"

    scene kaorislostcock6
    with dissolve

    s "I think “understands” is a little generous. I have no idea what you’re talking about right now."
    k "..."
    john "Bacawk. (Are you prepared for what has yet to come?)"
    john "Bacawk. (Tell me. When you gaze up at the sky and stare deeply into the lights of dead or dying stars, do you see a world that bends to fit your ideals?)"
    john "Bacawk. (Or do you see one that melts into unrecognizable form? Growing hotter by the day. Burning away its impurities so that those with higher tolerance may continue to walk unsinged.)"
    john "Bacawk. (I say these things to you so that you will have peace in me. In the world you have distressed. But be encouraged.)"
    john "Bacawk. (For I have conquered the world.)"
    john "Bacawk. (Which means that it must conquer me in return.)"
    k "Friend...you can understand what John is saying right now?"
    s "Not really. And even if I could find the words to translate, I can’t imagine you would really understand either."

    play sound "static.mp3"
    scene kaorislostcock7
    with flash
    stop sound

    s "I think the gist is that he’s going through some sort of mid-life crisis."
    k "But he is so young! And still growing!"
    john "Bacawk. (Foolish you are for keeping your eyes so unlocked- for they are soon to be taken from you.)"
    john "Bacawk. (It comes again in purest form. Tendrils dripping with the blood of my brothers and yet you stand here, idling. Waiting for the snow to melt.)"
    s "Most of the snow already melted a while ago. It hasn’t really been cold since Christmas."
    john "Bacawk. (It has, but it hasn’t. And you see, but you don’t.)"
    john "Bacawk. (When everything is gone, what will be left for us? When it treads our hallowed grounds, where will we be able to rest our feet?)"
    john "Bacaaaawk. (Or, excuse me- leg hands.)"
    john "Bacawk. (God is dead, human. But for how long will he remain that way? And who of equal value must die to bring him back?)"
    john "Bacawk. (I fear the answer, as should you. For the world as we know it could come toppling down as the result of one incorrect choice.)"
    john "Bacawk. (I am scared of what has yet to come. I am scared of what has happened. I am scared of what happens now.)"

    play sound "static.mp3"
    scene kaorislostcock8
    with flash
    stop sound

    k "He seems to be bacaaaawking a lot, Friendburger. If you can not find the words to explain his feelings, would you be able to write down what they look like?"
    s "Not really, since he’s now starting to sound all religious. That area isn’t really one of my strong suits."
    s "Also, I could just be imagining everything he’s saying because the idea of me being able to speak to animals when no one else can makes essentially no sense at all."
    k "Are you a religious person, Friend? Perhaps the god you believe in has gifted you the ability to understand the furry or feathered creatures of the world?"
    s "What an excellent usage of godly power."
    k "Can you ask John in his language if he will return home? I promise to be a better human chicken mother and friend to him."
    s "Did you understand that, John?"
    john "..."
    s "..."

    scene kaorislostcock9
    with dissolve

    k "Jonathan Chicken Kadowaki McChicken! You have caused the thin strips of hair above my sight sockets to slant at unreasonable angles too many times tonight!"
    k "I am the opposite of happy with you!"

    play sound "static.mp3"
    scene kaorislostcock10
    with flash
    stop sound

    john "Bacawk. (This was never what I wanted, but what I felt that I must do for my own protection.)"
    john "Bacawk. (As the temperature rises, so do my uncertainties.)"
    john "Bacawk. (I am not long for this world. Few of us are. And that has been all the more clear as of late.)"
    k "Friend, do you believe that John misses his family?"
    s "..."

    scene kaorislostcock11
    with dissolve

    k "John! I will find you another chicken to chicken around with while I am not house! Just please come back!"
    k "I can not go on without you! Who will I watch the cool rectangle machine with?!"
    john "... (...)"
    s "I...think he’s afraid of dying."
    k "He has chosen a strange place to return to in order to combat that!"
    s "I don’t think it has anything to do with you, but...maybe the time of year?"
    john "Bacawk. (A festival of tears has pitched its tents in the furthest corners of this city. We will all rue the day that-)"

    play sound "static.mp3"
    scene kaorislostcock12
    with flash
    stop sound

    john "BACAAAAAAAAAAWK! (zaf kqf za za za za za!)"
    john "BACAAAAAAAAAAWK! (zaf uz rdazf ar tqd!)"
    john "BACAAAAAAAAAAWK! (zaf nqradq etq [[REDACTED. DIALOGUE CENSORED DUE TO CHICKEN.])"
    k "John?..."
    k "What is he saying?"
    s "I...can’t understand him anymore."

    scene kaorislostcock13
    with dissolve

    john "..."
    k "..."
    s "..."
    john "Bacawk."

    scene black
    with dissolve2

    "John stares straight ahead for another moment before returning to Kaori."

    play sound "static.mp3"
    scene eggreturn with flash
    stop sound
    play music "letsfuckingo.mp3"

    "Then it becomes egg time again."
    "Please use the next 10 seconds to dance with egg."
    "You better do it!"

    $ renpy.pause(10, hard=True)

    "Okay, okay. Stop egg dance."
    "We talk now."
    "Pretty soon, a thing going to happen."
    "Are you prepared????"
    "Are scared????"
    "Stop scare! It’s OK!"
    "It’s all just lines!"

    play sound "static.mp3"
    scene kaorislostcock14
    with flash
    stop sound

    "There is nothing to fear, for fear is concept plucked from the brains of birds like a feather only to be subsequently implanted into your human brain to make you feel all weird and shit."
    "Sensei and Kaori go on a magic chicken ride back to Kaori’s apartment and none of this ever happened."
    "This was an imaginary event."
    "Please forget it after ten more seconds of egg dance."
    "Go find the nearest egg and kiss it. There might be a chicken inside!"
    "All chickens need love. That is the moral of today’s story."
    "This event never happened."

    $ renpy.pause(10, hard=True)

    play sound "static.mp3"
    scene kaorislostcock15
    with flash
    stop sound
    play music "sanctuary.mp3"

    k "Thank you very much for helping me find the cock again! It is almost like you are a cock expert!"

    if bonus == True:
        s "Yeah, that’s not {i}entirely{/i} inaccurate. But it isn’t how I’d..."
    else:
        s "Stop saying the C word in the Patreon version of the game."
        s "Besides, that's not how I'd..."

    s "Describe...what..."

    scene kaorislostcock16
    with dissolve

    k "Is there a problem, Friend? I know you as a person who normally finishes human sentences before becoming unloud."
    s "I just...don’t really remember coming back here."
    john "Bacawk."

    scene kaorislostcock17
    with dissolve

    k "John, shush."

    scene kaorislostcock16
    with dissolve

    k "Do you have a chicken brain, Friend?"
    s "What?"
    k "It is like I said. Chicken brains are small and they can not fit as many memories as human brains."
    k "If you can not remember how we got here, maybe it is possible that you have a chicken brain."
    s "By that logic, your brain would also be-"
    s "Wait. Actually, that might explain a lot."
    k "There you go again, leaving sentences without endings. How will anyone ever understand you if you do not seek to improve yourself?"
    s "I’ll get right to that, Kaori."
    s "Anyway, is there anything else I can do for you? Or are you ready to call it a night now that your pet is back?"

    scene kaorislostcock18
    with dissolve

    k "John is no pet, Friend! John is a “free-range” chicken with no rules or curfew as long as he listens to the rules and is home by mattresstime!"
    s "You know, I have a few issues with that sentence when thinking of all the trouble we went to tonight, but I’m going to abandon them in favor of getting some sleep."

    scene kaorislostcock15
    with dissolve

    k "Is that all you will abandon tonight?"
    s "What?"
    k "Will you be leaving anything else behind?"
    s "I’m not really sure what you mean by that."
    k "Then there is no need to answer."
    k "Goodnight, Friend! Thank you for the cock delivery!"
    s "..."
    k "..."
    s "Goodnight, Kaori."

    scene black
    with dissolve3
    stop music fadeout 5.0

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate20 = True

    "//////////////////////////USER2 HAS GONE OFFLINE"
    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kaoridate25:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."

    if bonus == True:
        "And, all jokes aside, I hope there’s no giant cock involved this time."

    "It’s one thing to dedicate an entire night of my potentially unending life to finding a lost chicken, but I think two nights spent on that might be pushing it."
    "Not to mention I still have no idea how things really ended up after we found John."
    "Or why he suddenly has an affinity for saying Maya-esque things despite at least my {i}perceived{/i} understanding that he has not been spending lifetimes watching his chicken friends fall for someone else."
    "I wonder if they’ll return along with summer."
    "I wonder if his {i}voice{/i} will as well."
    "But, like many other minor aspects of my existence, that’s something I’m willing to part with."
    "I find that keeping a mental list of those things can be quite beneficial in terms of ensuring you don’t accidentally wind up hurt while stumbling down this ghost town, life."
    "Not all stars become supernovae. But when you find one that will, it’s best to get as far away as possible."
    "Being caught in the blast of anything is risky."
    "But, then again-"
    "So is something as menial and unimportant as dialing the number of a friend. "
    "Something somewhere explodes."

    play sound "phonebeep.wav"

    k "Phone call!"
    s "Hey, Kaori. What are you up to right now?"
    k "I do not know!"
    s "..."
    k "..."
    s "What do you mean you don’t know?"
    k "Well, it all started with a white cat."
    k "I was on my way home from one of my working places when it was using its beanholders to try and capture a bakeryfly. It was very cute!"
    s "Okay?"
    k "So cute that I chased after it and wound up somewhere unfamiliar!"
    k "And now I do not know how to return home!"
    k "Thankfully, I put a special lock on the door that prevents John from leaving, so he can not disappear again."
    k "I will have to hope that my neighbor feeds him when they realize I am deceased."
    s "You are not going to die, Kaori."
    k "We all die, Friend. It is something I learned by spending time with you."
    s "Okay well, that makes it sound like I’m the reason you learned that and that it wasn’t something that you just happened to learn while I was around."
    s "But if you’re actually lost, why not use a navigation app or something?"
    k "My phone is dead!"
    k "Like all things..."
    s "But you’re talking to me on it right now."
    k "Lightbulb! "
    k "What if I describe the things I see and you go on a hunt of the scavenging variety to locate me?"
    s "Fine. Go. "
    k "I spy with my little vision balls...stars! And...buildings!"
    k "But they are not very good buildings. They are brown-ish. And...there is a wall! But there are many walls in many places, and not all of them keep things out!"
    s "..."
    k "There is a...water crossing street extension! And...wires!"
    k "Lots and lots of wires!"
    k "Wires and wires and wires and wires and-"
    s "Wait, are you in the old district?"
    k "I do not know! Is that where cats go?"
    s "“Water crossing street extension” means bridge, right?"
    k "You are very good at learning! Congratulations!"
    s "I think I know where you are, I just have no idea how you made it all the way over there just by chasing an animal."
    k "Animals can be very fast and have large amounts of stamina! Unless you are referring to the cheetah, which is an animal built for speed but {i}not{/i} stamina! "
    k "This cat was not a cheetah, though. It was much smaller. But did you know that cheetahs-"
    s "Just stay where you are, Kaori. I’ll come and find you."
    k "Thank you, Friend! I wanted to ask for help, but I have not yet discovered how to use my arm feet to make your phone go bzzzzzzzzzzz and always have to wait for mine to do that!"
    s "I’ll teach you soon. Just...stay where you are."
    k "Okay! Phone call!"

    play sound "phonebeep.wav"

    "I hang up the phone and sigh to myself, knowing that I’ve got a long way to walk if I’m going to find Kaori."
    "I just hope that she doesn’t wind up wandering off and that she actually stays where I asked her to."
    "The second half of town is the last place anyone like her should put themselves this late at night. "
    "{i}I{/i} don’t even like being there this late at night and I’m probably twice her size in terms of weight."
    "Here goes nothing, I guess."
    "I think of the phrase someone important uttered at some point that goes, “Nothing ventured, nothing gained” and attempt to connect it to my current situation in a meaningful way."
    "The connection is severed once I remember that I am the living antithesis to that quote, who gains everything from doing nothing but has the potential to be wiped clean if those operations were flipped."
    "Instead of thinking at all, I walk."

    play sound "static.mp3"
    scene kaoribridge1
    with flash
    stop sound
    play music "blueair.mp3"

    "And I arrive."
    "Kaori stands at the railing of a bridge where I once met someone she’s forgotten."
    "She looks up at the sky and thinks of something- probably animals. But I think of something else."
    "Something impure, though not the type of impurity you’d typically associate with me."
    "I think of what it would be like to shove both her consciousness and mine into a blender and deliver it unto the people of this place through telephone wires."
    "If those devoid of life could have life itself injected back into them, I wonder what it would do for this place."
    "And I wonder what would become of us, who sacrificed everything so they could do that."
    "I give up the thought as it’s not my choice to dictate what this girl wastes her mind on."
    "Not while it’s still blooming."
    "Not while mine has already withered."

    play sound "static.mp3"
    scene kaoribridge2
    with flash
    stop sound

    "I take my place beside her and gaze up at the same sky."
    "We see different things."

    k "I did as you asked, Friend. I did not move at all."
    k "And it was very hard because I saw a frog. "
    k "Do you like frogs?"
    s "They’re fine, I guess."
    k "Did you know that frogs have nightvision? And that one of the reasons they are so good at hunting tiny bugs is because they are very sensitive to movement?"
    k "When a frog captures its dinner, it will even pull its eyes down to the ceiling of its frog mouth to push the food down its throat! It is a very impressive way to eat!"
    k "Is there anything special you use your eyes for, Friend?"
    s "Nothing as special as sending them down to the roof of my mouth."
    k "You probably can not do that because you have a chicken brain. And chickens just have normal eyes. Which means you probably have chicken eyes too."
    k "Maybe you are just a large chicken who plucks his feathers?"
    k "Did you know that birds will pluck their own feathers to cope with stress when-"
    s "You need to be more careful, Kaori. You getting lost somewhere like this in the middle of the night isn’t really something I want to deal with regularly."
    s "Same goes for John, I guess. But you matter to me a little more than he does."
    k "I am sorry for making you sadburger."
    k "I didn’t know I would get lost."
    k "Recently, my mind has been very {i}zizz zizz{/i} and I thought petting a kitten would make it more {i}pow pow{/i}. Do you understand?"
    s "Nope."
    k "I will try a little harder to keep your life easy, Friend."

    play sound "static.mp3"
    scene spiderbug with flash
    scene kaoribridge3 with flash
    stop sound

    k "Know that I am with you always. To the end of time."
    s "Or at least until I get tired of finding you."
    k "You will always find me, whether you want to or not! I do not want to disappear, but it is something that can happen!"
    s "Make it...not happen, then? It’s fine on nights like tonight when I’m not really doing anything but, if this were to happen again tomorrow, I can’t say I’d really come out searching."
    k "But you would!"
    s "Why do you sound so certain of that when I’m literally telling you that’s not how it would work?"
    k "If a man owns a hundred sheep, and one of them wanders away, will he not leave the ninety-nine on the hills and go to look for the one that wandered off?"
    s "Since when do you know about metaphors?"

    scene kaoribridge4
    with dissolve

    k "I will continue to make trouble for you because that is who I am. I am a troublesome girl. So much trouble. "
    k "But it is you who continues to find me even when you are not looking that makes me so sure you will find me again."
    k "To the end of time, Friend."
    k "And even after that."
    s "..."
    k "..."

    "Kaori stares off at the sky once again and I can’t help but-"

    k "I am hungry."
    s "Okay, I guess I can finish my inner monologue later."
    k "Do you know of any establishments in this strange part of the world that will feed me at this time of night?"
    s "I mean, there’s a ramen shop not far from here that I- wait, haven’t you been there before?"

    scene kaoribridge5
    with dissolve

    k "Noodle building..."
    s "Is that angry face because you hate noodles or because you’re still upset Tsuneyo wouldn’t hire you?"
    k "Yes!"
    k "There is something strange about that building. Strange about this place. It makes my insides buzz like they are full of bees."
    s "Well, if you want food around here, it’s either that or the convenience store. I don’t really want to scout out any new local businesses at this time of night- especially when most of them are probably defunct."

    scene kaoribridge6
    with dissolve

    k "Mmmmmmmmmmmmmmmmmmmmmmmmmmm!"
    k "Okay!"
    k "But you must protect me from the evil that is the attractive ramen girl! She has access to too many sharp objects and an ingrained dislike for spiders!"
    s "Just keep your shirt on and I’m sure there won’t be any problems, then."
    k "If only things were that easy, Friend."
    k "If only things were that easy..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "After another minute or two of silent reflection as we gaze up at the sky, Kaori and I pull ourselves away from the bridge and begin to make our way over to Tojo Ramen."
    "It’s late enough that Tsuneyo should be closing up soon, but there should still be enough time for Kaori and I to get there and order before it becomes too much of a burden."
    "Not like I really care about being a burden anyway."
    "I helped someone tonight, so it’s only fair that I trouble someone else to cancel that out."
    "Kaori and I make our way through the overgrown streets of the second half of town and I notice her forcing herself to not chase after every living creature she spots."
    "The ones with extra legs, at least."
    "The humans who cling to the sides of old houses or tuck themselves into alleyways seem to be nearly invisible to her."
    "The opposite goes for them, however, who pay closer attention to her movements than I’ve seen them pay to anything else for as long as I’ve been coming here."
    "If it means something, I don’t know what. And I’m far too tired to try and figure it out."
    "So I will swallow my tongue and keep quiet until we arrive, locking any lingering thoughts so far in the back of my mind that even you will not be able to find them."
    "........."
    "......"
    "..."

    scene kaoribridge7
    with dissolve2
    play music "kashiwagi.mp3" fadein 3.0

    t "Welcome to Tojo Ramen. Please take a seat wherever you would like. The options are limitless."
    yu "Yo. What are you two doing here this late? Tsu-chan was just about to close up."

    scene kaoribridge8
    with fade

    s "Kaori got lost after chasing a cat. Then she got hungry. Now we’re here."
    yu "Yeah, okay. That tracks. "
    yu "Shoulda told me. I would’ve came and got her if I knew. Would’ve saved you a whole ass trip."
    s "I’ll do that next time now that she’s practically assured me there will be another."

    scene kaoribridge9
    with fade

    t "You look familiar."
    s "This is the {i}other{/i} girl related to Yuki who came in looking for a job that you refused to hire."
    t "What a persistent and irritating family."
    yu "Hey."
    t "Do you require a menu? Or are the many items listed on our walls sufficient in guiding your decision?"
    s "Just make me whatever. I don’t really care."
    k "I will have..."
    k "Tori shio ramen!"
    yu "Tori shio?"
    yu "Ain’t that your old man’s favorite, Tsu-chan? Remember him always makin’ that for himself back in the day."
    t "That dish is not one that is displayed on our wall. How did you know of it?"
    yu "I mean, it ain’t really a weird dish to order, is it?"
    t "I am simply curious. That is all."
    k "I am a friend of chickens! It is my duty to make sure their sacrifices for our sake do not go to waste!"

    scene kaoribridge10
    with fade

    t "Is it truly a sacrifice if they die unwillingly?"
    k "Does terminating the life-contracts of innocent creatures bring joy to your blood muscle?"
    t "The heart can feel no joy. It is the brain that processes emotions. You are clearly not prepared for the dish you ordered."

    scene kaoribridge11
    with dissolve

    s "I didn’t realize there were dishes you needed to pass a test in order to...order here."
    t "Tojo Ramen reserves the right to refuse service to anyone. For the protection of my family’s restaurant, I must ask that you order something else."
    s "I’m no ramen expert but I think fixing your ongoing power issues should be a little higher on the priority list when it comes to defending your family’s restaurant than refusing customers."
    yu "Oh, I think those are taken care of. I helped out with some of the wiring and shit downstairs earlier today and it’s been fine ever since."
    k "Tori shio ramen! Save the chickens!"
    t "You are a confusing individual. Why cling to something you do not understand? Something you have never experienced?"
    s "Tsuneyo, it’s just soup."

    scene kaoribridge12
    with dissolve

    t "First, ah!"
    t "Second, {i}just{/i} soup?! Have you no shame?!"
    yu "I think that dish might just be important to Tsu-chan because of her dad. Ain’t ever really seen somebody else order it."
    k "Do not make me go to the Yelp! I do not know what it is, but I know that these words instill fear in the brainhearts of my managers!"

    scene kaoribridge13
    with dissolve

    t "Tch. So that is how this is going to be."
    t "I should have known you would play dirty when you reek of arachnids."
    s "Do spiders even have a scent?"
    k "Everything has a scent if you close your eyes and imagine it has a scent!"
    s "..."
    t "Very well. I will make you what you ordered. But I bid you fair warning that I have never made this dish before and would highly implore you to order something else."
    k "I will glue that to the inside of my brain with imaginary glue and {i}un{/i}glue it once I have saved all of the chickens in Kumon-mi!"

    scene kaoribridge14
    with dissolve

    t "Why save what is doomed from the start? "
    k "Why abandon those who need us most?"
    s "Why is this conversation still happening?"

    play sound "imscared.mp3"
    scene black
    stop music

    "{i}Why does everything have to hurt so much?{/i}"

    yu "Yo, are you fuckin’ for real?!"
    yu "You’ve gotta call your electric company or some shit, Tsuneyo. This is gettin’ out of hand."
    t "Tojo Ramen sincerely apologizes for the inconvenience. Please remain calm while I attempt to restore the power."
    s "Looks like we probably should have gone to the convenience store after all."
    t "Why would we go there? We have all of the green onions we need and leaving work would not be convenient for anyone."
    s "I wasn’t talking about you, Tsuneyo. I was talking about Kaori and me."
    t "How rude of you to not invite me. I will not forget this."
    yu "Aight, I’m gettin’ outta here. Just put my shit on my tab and I’ll pay you back next-"

    play sound "imscared.mp3"
    scene kaoribridge15
    play music "sanctuary.mp3"

    yu "JESUS fuck, that noise ain’t easy to get used to."
    s "..."
    yu "Wait, where’d Kaori go? She afraid of the dark or something?"
    s "I think she’s said something about that in the past, but...I don’t think she’d really run away because of a five second blackout."
    s "Or how she could even find the door, now that I think about it."
    yu "Tsu-chan, you cool with puttin’ everything on my tab? That girl’s my niece and I probably shouldn’t be lettin’ her wander around in the dark over here."
    yu "No offense but this part of town ain’t exactly the safest thing around."
    t "Tojo Ramen understands and thanks you for your patronage. Please rest assured that these blackouts will no longer happen after today."
    t "For the sake of my business, I can not allow this to continue."
    yu "Yo, you comin’? Should probably help look for her since you’re the one who brought her here and all that shit."
    s "..."
    s "Yeah."
    s "Yeah, I’ll help."

    scene black
    with dissolve2

    "I follow Yuki out of Tojo Ramen burdened by the sensation of a large pit in my stomach."
    "By the time I make my way out into the open air, the pit grows."

    play sound "static.mp3"
    scene kaoribridge16
    with flash
    stop sound

    "I’m unsure of exactly what it grows {i}into{/i}, however."
    "I can feel thin roots sinking into some organs I probably couldn’t name if they were placed on an autopsy table in front of me...and wonder how much of my body’s resources are being siphoned away by them."
    "I wonder if removing them would be as simple as removing weeds from a garden."
    "A plucking motion- followed by a twist. "
    "A lift of the hand to observe the dirt falling off. To observe what wildlife clings to them, acting as yet another siphon."

    yu "Kaori? You around? "
    yu "I’ll give you a ride home. Just need you to like...come out and shit."
    s "..."

    "I look, but I don’t look far."
    "I don’t know how, but I can tell we aren’t going to find her."
    "Of course, I can’t bring myself to say that because I don’t want Yuki to worry."
    "And I guess {i}I{/i} don’t want to worry either."
    "Everything will be okay."
    "Everything is normal."

    play sound "static.mp3"
    scene kaoribridge17
    with flash
    stop sound

    "Everything is normal."

    scene black
    with dissolve2

    "Yuki gives up on searching and decides to go home."
    "I do the same."

    stop music

    "{i}Kaori’s aff____________________xxxxxxxxxxxxxxx{/i}"
    "........."
    "......"
    "..."

    scene kaoribridge18
    with dissolve2

    "Ami was sleeping on the couch when I came home."
    "All of her clothes were off."
    "She is getting so big."

    scene black
    with dissolve2

    "Sleep."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate25 = True

    jump amidate50

label kaorispecial35:
    scene nightsky
    with dissolve2
    play sound "phonebeep.wav"
    play music "unmatchingeyes.mp3"

    "I tap on Kaori’s name in my phone in hopes that she isn’t currently standing in the middle of the road and attempting to drown herself in rainwater. "
    "That would be quite hard to do right now given that it isn’t raining, but seeing as literally nothing has ever made sense while I’ve been with her, I don’t want to say it’s {i}impossible.{/i}"
    "It’s always raining somewhere — just never around me."
    "That really tells you a lot, doesn’t it?"

    play sound "phonebeep.wav"

    k "Paper!"
    s "Well, that’s a new one."
    k "Help to unfold!"
    s "By any chance, is your Japanese regressing? Because you’ve been doing pretty...{i}okay{/i} lately when you’re not completely zoned out and soaking wet."
    k "You lack the understanding, Friend! The thin, fragmented corpse of a fallen tree was attached to my entry block when I arrived at house tonight! I am worried of what secrets it contains!"
    s "There was some sort of...paper taped to your door? It’s probably just an eviction notice or something. Have you been paying your rent?"
    k "I deliver a smaller tree-corpse to the groundwoman on the beginning day of every month! And a discount poster for the creaming as well! That can not be it!"
    s "Just open it up and find out. "
    k "Are you sure that my safety is guaranteed?"
    s "Sure, why not."
    k "Then...unfold!"
    s "..."
    k "..."
    k "Ah!"
    s "Are you being evicted after all?"
    k "No! It is something much less horrible than that!"
    k "It is a treasure map!"
    s "It’s {i}what?{/i}"
    k "Treasure! And directions on how to locate it! "
    k "You must join me, Friend! Adventure is currently patient!"
    s "It’s like 9:00 PM. Do we really have to go on a treasure hunt {i}now?{/i}"
    k "Yes! I will see you at my cubic dwelling in the coming moments! I must prepare!"
    s "Kaori-"

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "What I didn’t know at the time of that phone call is just what “treasure” awaited us."
    "And how pressing the right button at the right time would ultimately change our lives."

    scene map1
    with dissolve2

    "But that’s enough shifting tenses for now. "
    "The story you’re more interested in is the one unfolding right before your very eyes."
    "Like a map — or a guide on how to take a step forward without cutting your leg-hands on clear, malformed sand."
    "It matters not what the future holds, but how we get there and how many gashes we are able to avoid along the way."
    "In the coming hours, you will encounter something you do not understand."
    "But, contrary to the way things normally are, it’s something you won’t instinctively look away from."
    "I tell you this not as someone recollecting the past, but as someone experiencing the present right there with you."
    "Open your eyes."
    "Hold out your arms."
    "And accept this gift from those who think you need it-"
    "Even if you feel like you don’t."

    k "Hmmmmmmmmmmmmmmmmmmmmmm..."
    s "Can I see-"
    k "I understand where we must go. But before we embark on our grand adventure, I must strengthen my cock."
    s "..."
    k "I am referring to my chicken cock."
    s "Just “chicken” is fine. Where is he anyway?"
    john "FEED.......ME........"

    play sound "static.mp3"
    scene map2 with flash
    stop sound

    john "FEED.......ME........"
    s "What the actual fuck?"
    john "FEED.......ME........"
    s "Kaori, this isn’t normal. That is not a chicken, it is a monster. And we will one day become its food."
    k "Impressive cock! And with an insatiable appetite!"
    k "As his matriarch, I am very proud! He is the growing boy! And the guardian of the image box!"
    john "FEED.......ME........"
    s "What are you even feeding him that allowed him to grow to that size?"

    scene map3
    with fade

    k "Yes."
    s "That is not an adequate answer to that question."
    k "I do not understand what the issue you appear to have is."
    s "That’s because your brain is broken, so I will help you. Your chicken has grown to an unreasonable size that makes me doubt it is even a chicken in the first place. He is {i}impossibly{/i} large."
    k "Every pizza is a personal pizza if you try hard and believe in yourself."
    s "{i}What?{/i}"
    k "The meaning of that word string is not one of cheese, but of hope."
    s "..."
    s "{i}What?{/i}"
    k "Do not be jealous of my cock because it is so very large. Believe in yourself and find your own. Make your dreams no longer dreams, but {i}memories{/i} of a dream. That is what it means to live."
    s "Kaori, he’s going to die at this rate."

    scene map4
    with dissolve

    k "Die?"
    s "Reverse-live."
    k "I know the meaning of the word, Friend. But John is healthier than he has ever been before on a diet of cornmeal and New Guinea flatworms. He will be fine."
    k "The cock only grows to the size of its apartment anyway. I am sure his growth spurt is nearing the reverse-beginning."
    s "Kaori-"

    scene map5
    with dissolve

    k "Enough of the cock-gobbling, Friend! We have treasure to discover and this map extends far beyond the reaches of my housing-cube! "
    s "Well...where are we going exactly?"
    k "To where the trees live."
    s "The forest? Or...a treehouse? I feel like the answer could be either of those things."
    k "The answer could be many things! But my treasure-senses are strong in terms of this one! All you need to do is follow me! To wherever I may roam!"
    john "FEED.......ME........"

    scene map2
    with fade

    s "I think you’ve had enough, John."
    john "YOU...KNOW NOT...WHAT AWAITS YOU..."
    john "I CAN TELL YOU...FOR A PRICE..."
    john "WORMS...PLACE THEM IN MY MOUTH..."
    john "I WANT TO...FEEL THEM CRAWL..."

    scene black
    with dissolve2
    stop music fadeout 40.0

    k "Drat! My insect supply has been reduced to ten minus ten! "
    k "I am sorry, John! But there is a chance our treasure will contain more of your favorite snack if it is buried underneath the ground! Please wait patiently at house!"
    john "FEED.......ME........"

    "Kaori and I exit “house” as she tucks the map into her back pocket, but I’m unable to comment on how ridiculous this is on account of my mind getting caught up on an animal roughly twice my size instead."
    "I’m sure it doesn’t do me any good worrying about such a thing when it’s clear there are some...oddities in this world to begin with."
    "But I wonder at what point they started becoming “oddities” in the first place?"
    "I wonder if there was ever a time without giant chickens or recycled worlds. When men roamed the streets freely and fewer girls felt inclined to spread their legs for me."
    "I’m glad that {i}this{/i} is where I live, though. And that being detached from reality has become what’s truly “real” to me."

    scene map6
    with dissolve2

    "But then again, there are moments like this where I’m being dragged through a forest...that I really {i}do{/i} wish I was back in bed at home, with a niece who sees me as an {i}uncle{/i} just one room over."
    "This ridiculous world is fine when it favors me, but it is Hell when it doesn’t."
    "And in this case, Hell is filled with the steam of a natural hot spring and a girl who should not be allowed outside of the house alone."

    s "Kaori...we’ve been wandering through the woods for an hour now. Are you sure whatever you’re looking for is {i}here?{/i}"
    k "We are getting close, Friend. The map tells me so."
    s "You’ve been saying that this whole time. Also, the map can’t tell you anything. It is a map."
    k "Is the purpose of a map not to direct the human or human equivalent that holds it?"
    s "It...{i}is.{/i} But definitely not in the way you’re making it sound."

    scene map7
    with dissolve

    k "Cheer up, duck that is made of rubber! If you are worried that the forest will swallow you, I can keep your human mind at ease with a fun game!"
    s "What kind of {i}game{/i} can we play in the middle of the woods? Because the only one I can think of is one I’m almost certain you are not mentally mature enough to play yet."
    k "An information game!"

    play sound "static.mp3"
    scene map8 with flash
    stop sound
    play music "sanctuary.mp3"

    k "Anything you want to know, I will tell you! And then you will tell me a thing {i}you{/i} know! "
    k "I read in the friendship book that sharing stories with someone is the best way to make them love you! And there is no one who loves me, so such a thing sounds like it would be good and necessary!"
    s "I’m sure Yuki-"

    play sound "static.mp3"
    scene map9 with flash
    stop sound

    k "That is a different form of love."
    k "The one I speak of is violent and passionate and would inflict a great deal of harm to both of us. But it would be a welcome instance of pain and suffering we would not trade for the world."
    s "It...what?"

    play sound "static.mp3"
    scene map10 with flash
    stop sound

    s "Kaori...we’ve been wandering through the woods for an hour now. Are you sure whatever you’re looking for is-"

    scene map11
    with dissolve

    s "Wait, what?"
    k "We are getting close, Friend. The map tells me so."
    s "..."
    k "Friend?"

    scene map12
    with dissolve

    s "You’ve been saying that this whole time. Also, the map can’t tell you anything. It is a map."
    k "Is the purpose of a map not to direct the human or human equivalent that holds it?"
    s "It...{i}is.{/i} But definitely not in the way you’re making it sound."

    play sound "static.mp3"
    scene map13 with flash
    stop sound

    k "Cheer up, duck that is made of rubber! If you are worried that the forest will swallow you, I can keep your human mind at ease with a fun game!"
    s "What kind of {i}game{/i} can we play in the middle of the woods? Because the only one I can think of is one I’m almost certain you are not mentally mature enough to play yet."
    k "An information game!"

    play sound "static.mp3"
    scene map8 with flash
    stop sound

    k "Anything you want to know, I will tell you! And then you will tell me a thing {i}you{/i} know!"
    k "I read in the friendship book that sharing stories with someone is the best way to make them love you! And there is no one who loves me, so such a thing sounds like it would be good and necessary!"
    s "I’m sure Yuki-"

    play sound "static.mp3"
    scene map9 with flash
    stop sound

    k "That is a different form of love."
    k "The one I speak of is much harder to comprehend. "
    k "It hurts. But it feels so good. "
    k "It’s terrible. But it’s also wonderful."
    s "...Kaori?"

    play sound "static.mp3"
    scene map14 with flash
    stop sound

    k "What is it, Friend? We are getting close. The map tells me so."
    s "Are you...starting to feel a little...strange in here?"

    play sound "static.mp3"
    scene map15 with flash
    stop sound

    k "Strange?"
    k "My leg-hands are warm from the water and my hair feels very zzzzzzz from the moist air, but I am still Kaori despite those small things."
    s "...huh."

    scene map16
    with dissolve

    k "Oh! Light bulb!"
    k "Maybe you would feel better if we played a game?"
    s "What kind of {i}game{/i} can we play in the middle of the woods? Because the only one I can think of is one I’m almost certain you are not mentally mature enough to play yet."
    k "An information game!"

    play sound "static.mp3"
    scene map17 with flash
    stop sound

    k "Anything you want to know, I will tell you! And then you will tell me a thing {i}you{/i} know! "
    k "I read in the friendship book that sharing stories with someone is the best way to make them love you! And there is no one who loves me, so such a thing sounds like it would be good and necessary!"
    s "I’m sure Yuki-"
    k "Did you ever have someone you loved, Friend?"

    scene map18
    with dissolve

    s "Uh..."
    k "Did you?"
    s "If this “game” of yours is going to lead to questions like that, I’d probably prefer if we killed time with something else instead."
    k "Killing is bad, Friend. All life must be treasured. "
    k "If it weren’t for those who valued life, you’d have never met the Queen of Spiders in the first place."

    scene map19
    with dissolve

    s "It was just a phrase, Kaori. I don’t really disagree with any of that. And I’m glad you’re here."
    k "Would it increase your gladness if you were to ask me a reverse-answer before you must reverse-question any of mine?"
    s "Maybe, if I could actually think of something to ask you."
    k "Anything you want to know, I will tell you."
    s "Then..."
    s "Since we’re already on the topic, what was it like essentially...coming back from the dead?"

    play sound "static.mp3"
    scene map20 with flash
    stop sound

    k "Very, very not good! No amount of grape-blood in see-through cylinders can compare to experiencing human life for the second first time!"

    scene map21
    with dissolve

    k "I do not see it as returning from the unalived, though. I am remembered by Aunt Yukiburger and the slightly smaller, large-chested version of her that accompanies her into buildings sometimes."
    k "And while these earlier memories have been ripped from my mind like coconuts off of a coconut tree, I can still feel my chest-muscle tighten each time my vision-balls connect with them."
    k "Is that strange, Friend? Am I mistaken in believing those feelings would not exist if I had truly left this place?"
    s "As someone who has {i}probably{/i} never died before, I have no idea. I have heard of people with amnesia experiencing memories like that to some-"

    play sound "static.mp3"
    scene map22 with flash
    stop sound

    s "...extent."
    k "Cheer up, duck that is made of rubber! If you are worried that the forest will swallow you, I can keep your human mind at ease with a fun game!"
    k "Anything you want to know, I will tell you! And then you will tell me a thing {i}you{/i} know! "
    s "..."
    k "What do you want to know, Friend?"
    s "..."
    s "What is happening right now?"
    k "Something is waking up."
    k "Now, it is my turn to ask you a question."
    k "What did you want to be when you were little?"
    s "I..."
    s "I don’t..."

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene happy2 with flash
    scene map23 with flash
    stop sound

    k "We are getting close, Friend. The map tells me so."
    s "..."
    s "Let me see it."

    play sound "static.mp3"
    scene map24 with flash
    stop sound

    k "I want to find the treasure just as much as you, Friend! John needs more bugs and I enjoy taking things out of the ground!"
    k "Do you doubt my ability to decipher text when it coats the body of a fallen tree? Is it because we are {i}surrounded{/i} by trees? Do you believe they are manipulating the text with their tree minds?"
    k "I would not doubt it if they were. They are alive, you know. Maybe the reason we have not found it yet is because of their interference?"
    s "Or maybe it’s because you just can’t read. Let me see it."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "water1.mp3"
    "..."

    scene map25
    with dissolve4

    s "..."
    k "What are your thoughts, Friend? Are we as near to the marking as I believe we are?"
    s "..."

    "I stare down at the “map” in Kaori’s hands and question why I followed her all the way out here without taking a look at it in the first place."
    "This is all a joke, right?"
    "She has an overactive imagination and just came up with some kind of...make-believe treasure hunt so we’d have something to do tonight."
    "There was never anything to find. And that’s why she didn’t want me to see it earlier. She knew I would catch on and decide against coming with her."
    "Now, my ankles are drenched and my neck is covered in blood from the fifty or so mosquitos I’ve needed to slaughter while venturing through these woods."
    "And, on top of that, I think I’ve even begun to hallucinate from overexhaustion or something."
    "I want to get out of here."
    "I want this fake treasure hunt to come to an end."

    s "Kaori...let’s go home."
    k "What?! But we are so close! Probably! Quitting now would mean walking away from something amazing!"
    s "How are you sure it’s so amazing? It’s one character on a sheet of paper you probably taped to your door yourself. It’s-"

    play sound "static.mp3"
    scene map26 with flash
    stop sound

    k "No! There is an amazing treasure here! I am sure of it! We can not give up now! We must believe in ourselves! Personal pizza, Friend! Personal pizza!"
    s "Kaori, give it a rest. Please. "
    s "There’s nothing here. I’m tired."
    k "Was I...wrong? "
    k "No...No, I know this is the right place! I can feel it!"
    s "Then we can...come back or something. But I’m leaving with or without you right now. "
    s "I don’t want to be here anymore."

    scene map27
    with dissolve

    k "Hah..."
    k "Okay. "
    k "I can not call myself a worthy companion if I repeatedly ask you to do things that make you unhappy. "
    k "I am sorry, Friend. Please forgive me and do not leave me the way everyone else always does."
    s "I’m not going to {i}leave{/i} you. I just want to get out of the...place where the trees live and go to sleep."
    k "..."
    s "..."

    scene map28
    with dissolve

    k "One more reading! Tell me your secrets, tree corpse! And do not interfere, natural wooden pillars! "
    s "Kaori, come on."

    stop music
    play sound "static.mp3"
    scene map29 with flash
    stop sound

    k "Ahhh! Fine! "
    k "But I am very reverse-happy about this!"

    scene black
    with dissolve2

    "........."
    "........"
    "......."
    "......"
    "....."
    "...."
    "..."
    ".."
    "."

    $ renpy.end_replay()
    $ kaorispecial35 = True
    $ kaori_love += 1

    jump treasureisland

label kaorispecial40:
    scene kaorischool1
    with fade
    play music "10c.mp3"

    mak "Sensei! I’m glad I caught you."
    s "Me too. Now I don’t have to think up a quirky or depressing anecdote to kick things off."
    s "Also, what do you mean “caught me?” It’s the middle of the school day."
    mak "Yes, but it’s also lunch time. And I was wondering if you’d like to maybe eat on the roof with me today."
    s "Check back in a few months when the sky is all red and weird."

    scene kaorischool2
    with dissolve

    mak "If that was a joke relating to the apparent state of the world that I only just found out about the other day, I’m sorry to say I didn’t quite get it."
    s "That’s fine, Makoto. You’re a genius and talented and amazing and beautiful and you don’t need to know {i}everything{/i} to be the perfect girl we all know you are."
    mak "..."
    s "Look at me. I’m nice now."

    scene kaorischool3
    with dissolve

    mak "Yeah, {i}too{/i} nice. And it’s making me extremely uncomfortable."
    s "I figured if I got it all out of the way now that it would be fine to just speak normally for the rest of the day and not have to worry about complimenting you."
    mak "It’s really impressive how you can still manage to be an asshole while showering me with compliments."
    s "My bad. There’s just a lot going on right now."

    scene kaorischool4
    with dissolve

    mak "True. But, on the bright side, none of it matters anymore since we’re all just going revert back to earlier on in the school year anyway! Isn’t that great?!"
    s "..."
    mak "Sensei? Isn’t that great?"
    s "Yeah. So great."

    scene kaorischool5
    with dissolve

    mak "Okay, so {i}maybe{/i} I’ve still got a way to go before I catch up to your apocalypse humor. But, I’d be open to hearing you out about how much it’s been weighing you down. "
    mak "I might not be able to {i}fully{/i} relate, but I can guarantee you there’s a lot going on in my head that I’m still-"
    s "It’s not even about that. It’s about everything else."

    scene kaorischool6
    with dissolve

    mak "Like what? If you want to talk, now’s the time to do it since everyone else is in the cafeteria."
    s "Luckily for you, I’ve been in a very talkative mood lately. So go ahead and pull up a chair since you're about to hear my entire life story."
    s "Or...at least all the parts of it that I can remember."

    scene kaorischool7
    with dissolve
    play sound "slidedoor.mp3"

    s "It all started one fateful hot boy summer-"
    k "Goodbye!"

    scene kaorischool8
    with dissolve

    s "..."
    mak "..."
    k "Knock times two."
    s "..."
    mak "Who...is there?"
    k "Me! I have arrived."
    s "..."
    mak "..."
    mak "And...you are?"
    s "Kaori, what are you doing here?"

    scene kaorischool9
    with dissolve

    k "I need help sitting on a child!"
    mak "..."
    mak "You what?"

    scene kaorischool10
    with dissolve

    s "Hah...Makoto, go eat in the cafeteria with everyone else. We can hang out on the roof tomorrow."
    mak "What? Just like that? You’re going to walk away from me to help some college student sit on a child? {i}Why?{/i} And {i}what child?{/i}"
    s "Kaori is definitely not a college student. In fact, she might not even be human. So do yourself a favor and stay as far away from us as possible until I tell you it’s safe to come back."
    mak "But-"

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    s "Kaori, come on. I have no idea what you’re doing here. But if we’re going to talk, it should be in my-"

    scene kaorischool11
    with dissolve2

    s "..."
    na "..."
    s "...office."
    na "?..."

    scene kaorischool12
    with dissolve

    s "Kaori, what do you think you’re doing bringing Nao here? She’s a missing child. Probably. If anyone is looking for her, you could go to jail."
    k "Today, Nao-chan learns about human school! Where humans go to school! The place where knowledge happens and where Friend lives!"
    s "I don’t {i}live{/i} here, I {i}work{/i} here. And I figured you’d understand that on account of the ten thousand jobs you have."

    scene kaorischool13
    with dissolve

    k "Nao-chan, the outward mouth vibrations that Friend threw up mean that he is glad that we are here!"
    s "No they don’t. Go home."

    scene kaorischool14
    with dissolve

    k "But it was difficult enough riding the school-colored landboat and the next one does not arrive for another 7,800 seconds! We have nowhere else to exist!"
    s "Kaori-"
    k "I need help sitting on the child! Tell him, Nao-chan!"
    na "!!!"
    s "She’s still not talking?"

    scene kaorischool15
    with dissolve

    k "She does struggle with her mouth muscle, but she is easy to understand when you can see the colors floating behind her tiny human body."
    s "Great. Then, can you tell me what clear means?"

    scene kaorischool16
    with dissolve

    k "Clear means special. It is the color or lack of color assigned to you on my talk-machine. But Nao-chan is not clear. She is purple."
    na "..."
    s "Well, whatever she is, let’s get her into my office. Lunch break will be ending soon and I don’t want to know what any of the girls would think if they saw me with two people who don’t even go here."
    k "But I have encountered many of your smaller female companions before. At what point will Nao-chan be tall enough to enlist as a Friend-friend?"
    na "?... !..."

    scene black
    with dissolve2

    s "Office. Now."
    k "Ahh! Do not slow-run at such a jogging pace! Your lower meat-tubes are stronger and larger than the ones that belong to us!"
    na "!!!"

    "Having absolutely no idea what’s going on (yet again), I quickly make my way through the halls before shoving the two {i}trespassers{/i} inside."

    scene kaorischool17
    with dissolve2

    "The one I’m already familiar with has no trouble accepting that she’s done something wrong and presses herself up against my desk."
    "The other one, however, begins to pick up objects all over the room and observe them."
    "As you can see...right now, she is particularly fascinated by a mug."
    "There is nothing {i}in{/i} the mug. It’s just a mug. "
    "And it’s such a strange and unnecessary thing to be doing that I’m just going to talk to Kaori while pretending she doesn’t exist."

    scene kaorischool18
    with fade

    k "I have sat on so many babies recently that I do not know if I will ever sit again, Friend."
    s "If you’re referring to {i}actually{/i} sitting on babies, stop. But if you’re referring to {i}babysitting,{/i} I’m not sure what the issue is. Nao barely speaks."

    scene kaorischool19
    with dissolve

    k "The tissue is-"
    s "{i}Issue.{/i}"
    k "Bless you. But anyway, the tissue is that mothering the hood is difficult no matter what size the hood is! "
    k "Nao-chan may have a small hood, but if I mother it wrong, the fabrics will become loose and she will have {i}no{/i} hood at all! Everything is up to me and it makes the “sleep” like a rock but not a sleep rock."
    s "So..."
    s "What you’re saying is that you’re struggling with motherhood and worry that you’re going to do something wrong that might mess up the girl you kidnapped?"

    scene kaorischool20
    with dissolve

    k "She is the good girl. And so very interested in round things and other things that are {i}not{/i} round but also shiny. "
    k "I went as distant as opening the mothering hood book to learn the secrets of the mothermom. But many of the motherers can not come to an agreement on which hood I’m meant to mother. Or mom."

    scene kaorischool21
    with dissolve

    k "I do not know what to do, Friend."
    s "I mean...you can start by...{i}returning{/i} her."
    k "To where? Nao-chan has no family or burgerfriends. And all of the papers that remind her of who she is are as hidden as the Bigfeet."
    s "Do you mean...Bigfoot?"
    k "Yes. The Bigfeet. Nowhere to be found and without sockpockets."
    s "It’s Big{i}foot,{/i} Kaori. Not Bigfeet."
    k "Is only one of them large?"
    s "No, they’re both-"

    scene kaorischool22
    with dissolve

    s "Wait, yeah. Why is it called that?"
    k "You non-Kaori humans are so very non-Kaori. If everyone were also a spider, it would make the world a lot easier to understand. But also there would be webs everywhere, which could get sticky."

    scene kaorischool23
    with dissolve

    s "Kaori, I don’t know what you want me to do. I have no idea how to help you with Nao and if you can’t take care of her, just find someone else who can."
    k "Will you accept the role as her fatherdad? The mothering hood book told me to provide one and you’re the only non-chicken cock I know."
    s "Don’t objectify me in my office. I’m more than just my best feature."
    k "Your best feature is your pointy chin. It’s so sharp and capable of causing harm to your adversaries."
    s "..."
    k "I bet it could pop a sphere of thin, air-filled plastic."

    scene kaorischool24
    with dissolve
    play sound "dooropen.mp3"

    s "Well, now I’m just self-conscious."

    scene kaorischool25
    with fade

    mak "Sensei, what on earth is going on?! Who was that girl who-"

    scene kaorischool26
    with dissolve

    na "!!!"
    mak "..."
    na "!!!!!!!"

    scene kaorischool27
    with dissolve

    mak "..."
    na "???"
    na "!!!"
    mak "Wooooow. Cool mug."

    scene kaorischool28
    with dissolve

    na "!!!!!!!!!!!!!!"
    mak "Sensei, what is happening right now? Who is this person? And {i}that{/i} person? "
    mak "And, before you answer, please just tell me they’re relatives of yours."
    k "I am Kaori! The Queen of Spiders, Mistress of the Dark, and greatest waitress in Kumon-mi! And the tiny  human with the ceramic coffee-holder is called Nao-chan."
    mak "And you are Sensei’s cousins...correct?"
    s "Hey, remember earlier when I said that a lot has been happening lately? This is what I was talking about."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene kaorischool29
    with dissolve

    mak "So...let me get this straight."
    mak "A mysterious treasure map with nothing but a kanji character on it was taped to your door when you came home from work..."
    mak "And so you went on a journey into the forest to {i}find{/i} that treasure...{i}didn’t{/i} find that treasure...but then proceeded to find {i}her{/i} instead..."
    mak "And so, instead of reporting a missing person to the police...you kidnapped her...and now you two are peacefully living together as...sisters? Friends? "
    s "They have an eight-foot chicken named John as well."
    mak "..."
    k "Eight and a half. Very big cock."
    mak "And...uhh...{i}Nao-chan{/i} was it? You’re okay with all of this? You’re not being held against your will?"

    scene kaorischool30
    with dissolve

    na "..."
    mak "I see..."
    s "Are you seriously just going to ignore the eight foot chicken? Because that should have been pretty alarming."
    mak "At this point, I’m not sure if anything would alarm me. This world is becoming less and less believable every single day."
    s "And now you know why I’ve been so exhausted."
    k "Glasses girl, what is your relationship to the burger man? Has he put his fingers in your mouth before?"

    scene kaorischool31
    with dissolve

    s "Kaori, please never ask that question to anyone again."
    mak "I...uhh...maybe? I can’t really remember, but...it’s possible?"
    s "{i}Why wouldn't you just say no?...{/i}"
    k "I bet you can fit many hand-handles in your face opening. Accept this human compliment and tell your teacher-man to become Nao-chan’s fatherdad as thanks for my words of handcouragement."
    mak "You...want him to help you raise the girl you kidnapped? As mother and father?"
    k "Correct!"
    k "Friend is reliable and kind and would make an excellent fatherdad for Nao-chan! She already loves him very much!"
    s "She does?"

    scene kaorischool32
    with dissolve

    na "???"
    k "What if I promise you all of the cream in the worldglobe? Or free sausage fests for the rest of your life? Or all of the hot meat you could ever want?"
    s "Kaori, I get that you’re worried, but I’m pretty sure Nao will be fine. She’s not a toddler. She’s old enough to, like...function as an actual human for the most part."
    s "Just focus on teaching her all of the things she doesn’t know for now. Once she starts seeming like less of a kid to you, I’m sure some of those worries will start to fade."

    scene kaorischool33
    with dissolve

    mak "How come she gets actual advice when all {i}I{/i} ever get is inappropriate touching?"
    k "But what if I can not effectively mom? I do not even have a hood. What am I supposed to drape over her head-bone when the coldness comes in?"
    s "Motherhood doesn’t involve an actual {i}hood,{/i} Kaori. If you’re that insistent on keeping her, just do what I said and things will work out fine."
    s "I’m not going to just step in and be her dad, though. That’s weird. "
    k "Is it weird because you did not create her with your sperms?"
    mak "You know, maybe our class isn’t so weird after all if this is who you’re talking to outside of it."
    s "It’s weird because I barely know her and didn’t sign up for a daughter when I already have Ami and a million other girls I’m supposed to be taking care of."

    scene kaorischool34
    with dissolve

    mak "Wow, are you actually planning on looking after us now? Or are you just saying that to weasel yourself out of this situation?"
    s "You’re not helping, Makoto. "
    mak "You want me to help? Here. I’ll help."

    scene kaorischool35
    with dissolve

    mak "Sensei and I will raise Nao-chan together. That way, you can go back to focusing on...whatever it is you do while not having to worry about her anymore. Easy fix, right?"
    k "Together?..."
    s "Makoto, that might be easy for {i}Kaori,{/i} but not us. You can't just sign me up for things like this."
    mak "Why not? We’re basically married already."
    s "Not by any choice of mine we’re not."
    mak "Does that work for you, Kaori? I can take her back to my house as soon as you leave."
    k "..."
    na "..."

    scene kaorischool36
    with dissolve

    k "..."
    na "?!?!?!?!"
    k "I..."
    na "?!?!?!?!?!?!"
    k "I..."
    na "?!?!?!?!?!?!?!?!?!?!?!"

    scene kaorischool37
    with hpunch

    k "I DON’T WANT TO LEAVE NAO-CHAN BEHIND! I’LL BE A GOOD MOTHERMOM!!!!"
    na "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    mak "There. Problem solved."
    s "Is it really, though?"

    scene kaorischool38
    with dissolve

    mak "For now, at least. It was clear from the start she never wanted to let her go. She’s just overwhelmed and having some doubts about her ability to provide adequate care."
    mak "The thing is, people tend to whip themselves into shape once they’re threatened with the things they love being taken away. So I may have just saved a child. Go Makoto. "
    k "Nao-chan! I am sorry for my momentary head clouds! I am just as lost as you were in the chicken alley! We can help each other become good human females! That is the promise we are making now!"
    na "!!!!!!!!!!!!"

    scene kaorischool39
    with dissolve

    k "Thank you for providing the assistance, Friend! We could not have completed this without you!"
    na "!..."
    mak "Wait, seriously? He didn’t even do anything. I was the one who actually {i}helped.{/i} He just stood there and said no to a bunch of stuff."
    s "Hey, that’s not true. I did say that one thing about teaching her stuff — which I assume Kaori is going to do as soon as she gets home. "

    scene kaorischool40
    with dissolve

    k "Nao-chan, what do you want to learn?! I will teach you all of the knowledge in the human world in the order you want so long as the alphabet is not that involved in that order!"
    na "..."
    k "Then it is settled! Nao-chan will learn how to read!"

    scene kaorischool41
    with dissolve

    na "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    k "Will you still bring your body to the building we live in?"
    k "You do not have to fatherdad, but you can still make words happen and stroke the giant cock."
    s "I’ll still come over, Kaori. Just...keep doing your best for the time being. Even if your “best” is entirely inadequate by most childcare standards. Probably. But I guess that’s an issue for another-"
    k "Bless you."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 12.0

    s "But I guess that’s a {i}tissue{/i} for another day..."

    "Kaori and Nao leave the office, but Makoto makes sure to stay behind and lecture me about getting myself involved with weird people."
    "The thing is, {i}they’re{/i} kind of the ones who got themselves involved with me."
    "Like...sure, I do call Kaori on occasion. But most of our important interactions have just been me bumping into her somewhere. "
    "Nao is no different."
    "Well, actually, Nao is {i}entirely{/i} different. But the way in which we met isn’t."
    "They’re just two weird girls I managed to encounter in my long, strange journey through a world that shouldn’t spin."
    "And I’m sure that world is even stranger for them. "

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaorispecial40 = True

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label kaoridate40:
    scene clearnightsky
    with dissolve2
    play music "unmatchingeyes.mp3"

    s "{i}Hah...{/i}fuck it."

    "I sigh to myself as I tap on Kaori’s name in my phone- knowing that, unless sudden tragedy has struck (Which wouldn’t be {i}too{/i} uncommon around here) that she’s a package deal now. "
    "That’s right, imaginary audience that I talk to all the time for reasons both you and I don’t understand — {i}somehow{/i} Kaori managed to track down the only other person in Kumon-mi with heterochromia."
    "Or, as she refers to it, {i}special{/i} eyes."
    "For Kaori, I’m not sure if I’d go that far as, unless I’m misremembering what little of her backstory I’ve been able to discern, she’s {i}always{/i} looked like that."
    "Nao is..."
    "Well, let’s just say I’m still having a hard time accepting that we just randomly discovered a little girl with eyes matching Ami and Maya for no reason whatsoever."
    "There’s something more to this, just..."
    "The chances of me ever figuring that out while Nao can’t talk and Kaori can’t talk {i}well{/i} are very slim. "
    "But hey, maybe Kaori’s been doing an exemplary job as a “mothermom” in my absence and Nao has suddenly evolved or something."
    "Like always, there’s only one way to find out."

    play sound "phonebeep.wav"

    k "Shh!"
    s "...Why?"
    k "Your talk-voice must not be big when there are word-drenched paper blocks present! "
    s "Are you...at the library?"
    k "Incorrect! I collected my own knowledge blocks and am helping Nao-chan memorize the best words! Like “greyscale” or “muskrat!” And having a big voice will make the words dissolve!"
    s "Ahh, yes. I forgot that’s why silence is heavily enforced in libraries. It has nothing to with disturbing anyone."
    k "You are forgotten."
    s "You mean “forgiven.”"
    k "Who are you?"
    s "Or maybe you don’t."
    k "Hello!"
    s "Kaori, I’m not waiting for you to invite me any longer. I’m coming over."
    k "But I am being you — a human teacher for small girl who needs my help!"
    s "Then you won’t mind if I come check your progress. No one is a better authority on me than myself. Or maybe Ami. Or Maya. Or Niki. "
    k "Cotton candy girl! Are her legs still where they’re meant to be?"
    s "Yeah, she’s doing fine. But we can talk more about her when I get to your place."
    k "But Nao-chan-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and begin to make my way over to Kaori’s apartment in a much better mood than I’ve been the last several times I’ve gone there."
    "And no, it has nothing to do with the fact that I’m getting two potential aliens for the price of one. "
    "But it has {i}everything{/i} to do with how things have been looking up lately."
    "I love my niece and all of the things she does."
    "I love my childhood friend slash ex-girlfriend slash idol and how she’s helping me learn to walk again."
    "And I’m closer to Maya than ever before."
    "Well, in this life at least. From what I understand, I’ve been {i}very{/i} close to her in the past."
    "It’s all smiles and sunshine for me."
    "Nothing can possibly go wrong."
    "Nothing can possibly go wrong."

    scene whythesky
    with dissolve2

    "Nothing can possibly go wrong."
    "Tonight is going to be a good night."
    "This is a feeling I have which means that it must be true because it is a feeling I have it is a feeling I have it is a feeling I have and I have this feeling that I have and it’s going to be good."

    scene t

    "There are nineteen different ways to brew coffee (That I am aware of)."
    "I will now tell you about them."

    play sound "static.mp3"
    scene kaorireads1 with flash
    stop sound

    "Just kidding lol."

    k "And that combination of letters means “dodgeball!” It is a game where you dodge a ball! Do you understand, Nao-chan?"
    na "!!!"
    s "Hi Kaori. I promise that nothing followed me on the way here."

    scene kaorireads2
    with dissolve

    k "Friendtruder! You entered the housing-cube so very quietly! I am impressed by your ability to remain undetected! Are you the ninja?"
    na "!..."
    s "Yes, that is me. How go Nao’s apparent lessons? Is she able to read yet?"

    scene kaorireads3
    with dissolve

    k "No! But it is the thinking that counts and if you think hard enough you can count every number there is!"
    na "..."
    k "I only wish there were better fruits to teach her with as this mango is both not edible and has too many pictures of females in tiny skirts."
    s "Manga. Not a fruit. And it would probably be best to teach her with actual books rather than comics."

    scene kaorireads4
    with dissolve

    na "?!?"
    s "Oh, great. You’ve already got her hooked on them, haven’t you?"
    k "Nao-chan loves the picture mango. It is her favorite fruit that isn’t a fruit but is still a fruit because the mango is a fruit."
    na "!!!"
    s "As long as she doesn’t turn into another Molly, I’m sure it will be fine."

    scene kaorireads5
    with dissolve

    na "..."
    k "Would you like to assist me in the reformatting of the Nao-chan brain, Friendtruder? You have more experience with this than I do and understand so many more words."
    s "Maybe another time. I feel suddenly compelled to go outside with you while leaving Nao inside to read on her own."
    k "That does not sound like an effective means of instruction."
    s "I’m sure she’ll be fine. I just really think we should go outside."
    s "Nothing followed me here."

    scene kaorireads6
    with dissolve

    k "This is the one-plus-oneth time you have mentioned being followed. If there is a wild human animal outside, all you need to do is make yourself look large and it will likely run away."
    k "It is human nature to run away from things that are much bigger than you. That is why I avoid the long-necked wrong-horse."
    na "..."
    s "There’s nothing here. Nothing followed me."
    k "Why are you suddenly the strange one? That is my occupation."
    s "Let’s go outside."
    na "..."

    scene kaorireads7
    with dissolve

    k "Nao-chan, be the good girl and eat your mango while I talk to Friend. But eat with knowledge and not your mouth bones. This is not that kind of mango."
    na "..."

    scene black
    with dissolve2

    k "Come, Friend! But have the quickness! Show me what did not or did follow you!"
    s "Nothing followed me. I already told you that. Stop being so weird."

    "........."
    "......"
    "..."

    scene kaorireads8
    with dissolve2

    k "It appears that you did not fill your pockets with deceit before arriving here."
    s "Do you really think I’d lie to you? What would I have to gain from that?"

    scene kaorireads9
    with dissolve

    k "My collection of circular earth-bits so you can defend yourself from whatever furry non-friend follows you next. Is that your main fear, friend? Because mine is the color green."
    s "I’m not after your rock collection. I just wanted to spend some time with you away from Nao."
    k "Do you not like Nao-chan? Because Nao-chan is the good girl. She does the good things and will one day become the good woman."
    s "I don’t have a {i}problem{/i} with her. It took me a little to warm up to you as well. But tonight, I just felt like I should be with you. That’s all."
    k "You felt...like you should be with me?"

    play sound "static.mp3"
    scene kaorireads10 with flash
    stop sound

    k "Why?"
    s "It’s just a feeling. I don’t really know how to describe it."
    k "..."
    s "..."

    scene kaorireads11
    with dissolve

    k "..."
    s "..."

    scene kaorireads12
    with hpunch

    k "Hot face!"
    s "Yeah, you’re blushing pretty intensely all of a sudden."

    scene kaorireads13
    with dissolve

    k "I apologize for changing colors. I understand humans should not do that and you are probably scared. But I will not hurt you the way you are afraid wild animals will."
    s "I’m not afraid of wild animals. In fact, I’m not really afraid of anything. I just wanted you to know that I am here alone and that I want to be with you while you are also alone."

    scene kaorireads14
    with dissolve

    k "But if you are the alone and I am also the alone does that not mean we are together? Or is that another kind of alone? Like mango and mango."
    s "Please just talk to me. About anything. I don’t want to be home right now. It’s not safe."
    k "Not safe?..."
    s "It isn’t safe anywhere. Everywhere I go I see her and I don’t want to see her and I don’t want to remember and I know I have to but I can’t and I don’t want to and you don’t understand any of that-"
    s "Which is why I’m here. Please keep me company. I’m not afraid of anything, I swear."
    k "..."

    scene kaorireads15
    with dissolve

    k "I understand."
    k "The Queen of Spiders will let you rest in her web — but only under one condition."
    s "And that condition is?"

    play sound "static.mp3"
    scene kaorireads16 with flash
    stop sound

    k "That you tell me who you’re running from."

    play sound "static.mp3"
    scene kaorireads17 with flash
    stop sound

    s "What? No. What? Why?"
    k "Friend? What seems to be the problemo? That is the Spain word for “problem.” You’ll never guess where they say that."
    s "Your eyes...they..."

    play sound "static.mp3"
    scene kaorireads18 with flash
    stop sound

    k "They are special and made of a clear, jelly-like collagen. "
    k "They help me see things and sometimes they get all ahhhhhh when I am awake for longer than I should be. "
    k "What more would you like to know about them?"
    s "You’re not..."
    s "Who..."
    s "Who...are you?..."

    play sound "static.mp3"
    scene kaorireads19 with flash
    stop sound

    k "I am Kaori! The Queen of Spiders! The Mistress of the Dark! The greatest waitress in all of Kumon-mi! "
    k "But most importantly, I am your-"

    play sound "static.mp3"
    scene kaorireads20 with flash
    stop sound

    k "..."
    k "Huh?"
    k "My fleshy exterior feels very tingly all of a sudden."

    play sound "static.mp3"
    scene anormaldoor with flash
    scene happy9 with flash
    scene imissyoumore with flash
    scene mm4 with flash
    scene parrotpicture2 with flash
    scene sakiembarrassed with flash
    scene sexyland2 with flash
    scene somethinglikethis with flash
    scene surrender with flash
    scene ayhh5 with flash
    scene andsoami with flash
    scene colorbars with flash
    scene eggreturn with flash
    scene tongueparty with flash
    stop sound
    $ renpy.pause(20, hard=True)
    "ARE YOU READY?!"
    "GOOD!!!"
    "THEN COUNT IT DOWN WITH ME!"

    scene 5
    "5!"
    scene 4
    "4!"
    scene 3
    "3!"
    scene m
    "M!"
    scene parrotpicture1
    "Parrot!"
    scene 0
    "Nothing!"
    scene neg1
    "-1!"
    scene circle
    "Circle!"
    scene black
    "And most importantly..."
    scene t
    play sound "cheer1.mp3"
    "T!"

    scene black
    with dissolve4

    $ kaori_love += 1

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene kaorireads21 with flash
    stop sound

    k "Mm! Mmf! Mm!"

    $ kaori_love += 1
    "{i}It increased again!{/i}"

    k "Mm! Mmnch! Mmf!!"

    $ kaori_love += 1
    "{i}And again!{/i}"

    k "Nngh! Mmf! Mmnch! Mmm!"

    $ kaori_love += 1
    "{i}Wow!{/i}"

    play sound "static.mp3"
    scene kaorireads22 with flash
    stop sound

    k "Mm! Mmmm! Mm! Chm! Chmp! Mnch! Mm!"

    $ kaori_love += 1
    "{i}She must really like kissing!{/i}"

    k "Mmf! Mmm! Mnch!!! Mmm!!!"

    play sound "static.mp3"
    scene kaorireads23 with flash
    stop sound

    k "Hah...hah...hah..."
    k "More..."
    s "What the fuck is-"

    play sound "static.mp3"
    scene kaorireads24 with flash
    stop sound

    k "Ngh!"
    k "F...Friend!"
    k "I...can’t...stop!"
    s "Kaori-"

    play sound "static.mp3"
    scene kaorireads25 with flash
    stop sound
    play sound "likepigstopigwater.wav"

    k "{b}月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"

    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene kaorireads21 with flash
    stop sound

    k "Mmm!!!!!!"

    "I’m not sure how long this goes on for."
    "And, to be even more honest, I’m not even sure if it’s really happening right now or not."
    "I’m obviously no stranger to nonsensical scenarios, but this is really just way too much."
    "It came out of nowhere."
    "The mood is all wrong."
    "And yet..."

    scene kaorireads26
    with dissolve

    "And yet her tongue is like novocaine."
    "It kills off all the pain and makes me numb."
    "I needed that tonight."
    "It came in a different way than I expected it to, and who knows if it will ever come again..."
    "But for now-"

    scene kaorireads27
    with dissolve2

    "I close my eyes and kiss her back."
    "Because I’m not just content with feeling numb-"
    "I prefer it."
    "{i}This{/i} is normal for me."
    "{i}This{/i} is what I’m meant to be."
    "Confused."
    "Afraid."
    "And with my tongue in a pretty girl’s mouth."
    "Speaking nothing, feeling nothing."
    "That’s all I’ll ever be."
    "That’s all I’ll ever want."

    scene kaorireads28
    with fade

    k "Mm! Mmnch! Mm..."

    scene kaorireads29
    with dissolve

    k "Mm! Hngh! Mmch! Chmp! Chmm!"

    scene kaorireads30
    with dissolve

    na "?..."
    k "Mm! Mnff! Mmngh! Mmm!!!"

    scene kaorireads31
    with hpunch

    na "?!?!?!?!?!?!?!"

    scene kaorireads32
    with fade

    "I wonder if I should stop her."
    "The moments leading up to this are expectedly blurry but, I can’t imagine any world in which Kaori would willingly throw herself at me like this out of nowhere."
    "And that means a lot since I have seen several worlds at this point and am becoming a bit of an expert when it comes to them."

    k "Mm...mmmngh! Mmnch!"
    na "........................................."
    na "?????????????????"
    na "?!?!?!?!?!?!?!?!?!?"
    s "..."

    "Yeah...I should probably stop this."
    "Especially now that we have a spectator."

    play sound "static.mp3"
    scene kaorireads33 with flash
    stop sound

    s "Kaori."
    k "Huh? What? Huh?"

    scene kaorireads34
    with hpunch

    k "WHAT?!?!?!?!"
    k "Why the closeness?! And the hot face again?! And why does my mouth muscle have more wetness than the normal amount of wetness it normally has?!"
    s "I imagine it's because you just forced yourself on me."

    scene kaorireads35
    with dissolve

    k "What...did I do? What does “force yourself” mean? "
    s "It can mean a number of things. But in this case, you pushed me up against the wall and starting making out with me."

    scene kaorireads36
    with dissolve

    k "You can not make “out,” Friend. Out is a direction. Please explain the situation with different words because one second things were normal things but the next they were red and bubbly things!"
    s "You kissed me. And quite aggressively at that."

    scene kaorireads37
    with dissolve

    k "Kiss?..."
    s "You do know what a kiss is, correct?"
    k "Yes. But we are friends. We can not do the kiss. That would make us special friends and I do not want to make a new human yet."
    s "It takes a little more than kissing to do that, just FYI."
    k "I understand human mating rituals. What I do not understand is why there would be a kiss. This is not a thing I would do. I don’t want a special friend."
    s "First off, harsh. Second, I’m not going to hold it against you. I’ve been in a...similar situation once before."
    k "How did that “situation” end?"
    s "The girl it happened {i}with{/i} wound up rightfully despising me for the rest of...forever. She hasn’t really stopped yet."

    scene kaorireads38
    with dissolve

    k "Does this mean you are you going to despise me?! For the accident?!"
    s "An accident is just that. I won’t hold it against you. "
    s "But you might want to back off for now since your {i}daughter{/i} is watching us."
    k "A baby was already formed?! Maybe I do not understand mating rituals at all!"
    s "I’m talking about Nao..."

    scene black
    with dissolve2
    stop music fadeout 20.0

    k "Ahh! Nao-chan! Shield your vision balls! You are not yet prepared to see the scary things large humans do!"

    "........."
    "......"
    "..."

    scene kaorireads39
    with dissolve2

    "Kaori sends Nao back inside and...I suppose we’ve reached the part of the night where she apologizes for what happened and then heads back in herself."
    "The thing is, she doesn’t {i}need{/i} to apologize."
    "If anything, I should be {i}thanking{/i} her as that spontaneous make out session was somehow able to set me back on the right course."
    "When I told you things have been looking up, I was lying. "
    "I’m sure that’s obvious in hindsight, but you need to see this from my perspective to truly understand."
    "It {i}wasn’t{/i} obvious for me."
    "It isn’t obvious {i}now{/i} either."
    "Because while the residual effects of a novocaine tongue still linger in my mouth, I know better than anyone that numbness is only temporary."
    "And as soon as I walk away from this apartment, even that will start to fade."
    "Something did follow me here."
    "You can’t see it."
    "But I can."

    play music "undersea.mp3" fadein 4.0

    k "The cotton candy girl will not be happy with the kiss that I have done."
    k "She is the one you should be doing this kissing with."
    s "Do you...talk to her often?"
    k "Only when she has a wiener in her mouth."
    k "She says many words about you. And you would form an attractive human together if you mated."
    s "..."
    k "..."

    scene kaorireads40
    with dissolve

    k "Are we still allowed to be friends?"
    s "Why wouldn’t we be?"
    k "Because there is an invisible line humans always talk about and I can not see it because it is invisible but, if I could, I think I would have stepped over it when I did the kiss."
    k "It was an accident. I don’t even remember the line. The world just changed all of a sudden and when my sight-spheres became normal sight-spheres again, you were right in front of me."
    k "I’m sorry. It won’t happen again."
    s "It...can if you want it to."
    k "Why would I want it to? I don’t understand. "
    k "You are Friend, not Special Friend. Repeating the kiss with you will give you a new name and you do not like the new names you receive."
    s "True. But I liked kissing you. Even if it...wasn’t really my decision."
    k "What about it did you like?"
    s "I mean...that’s not really a question that’s easy to answer. I just did."
    k "I’m sorry for asking a difficult question. I just do not possess any memories of it and wanted to see if I could have your memories move into my brain and build a thought-house there."
    s "..."
    k "..."
    s "On second thought, yeah. Maybe it’s better if we don’t do that again."

    scene kaorireads41
    with dissolve

    k "Yes. Now we are reading the same page. "
    k "Can your legs take you to the place you need to go next? Or will one of them run away?"
    s "I’m sure I’ll get home fine. Apologies in advance for all of the questions Nao will have for you, though."
    k "Nao-chan does not ask questions. She has not learned that yet. But I will add mating and courting rituals to the list of things she needs to make brain-room for."
    s "Yeah, maybe wait a few years before you give her all of the details. But I’ll get out of your hair now. I’ve fucked up your night more than enough already."
    k "All you did was make my heart go babababa and that is not a bad thing. But it is a thing. And now I have to wait for the babababa to stop."

    scene black
    with dissolve2

    k "I will be in my housebox if you need me. "
    k "And if you ever think something is behind you, remember to make yourself look big."
    k "The world is scary when you are small."
    k "That is why the fieldmice hide."

    $ renpy.end_replay()
    $ kaoridate40 = True

    "........."
    "......"
    "..."

    jump amispecial50

label kaoricamp1:
    scene kaorianotherhunt1
    with dissolve2
    play music "unmatchingeyes.mp3"

    k "Friendburger! You have returnedburger! Did you forget to rub Frog Boy for good luck?"
    s "Yup. That’s exactly why I came back. You know me so well, Kaori."

    scene kaorianotherhunt2
    with dissolve

    k "I could not call myself a friend if I did not understand when you desired the rubbing of a special frog. All in a day’s job."
    na "!..."
    k "Go on, Friend. Rub the Frog Boy and carry on with your tree-based day of resting. Nao-chan and I have much job to do and have not included your mouthwords in our daily time budget."
    s "Well, what are you two doing exactly? Maybe I can tag along."

    scene kaorianotherhunt3
    with dissolve

    k "A long what?"
    na "..."
    k "No, Nao-chan. Friend wants to play tag because he is larger than us and knows he can win. It is in periods like this where we must decide against bending as we are not pipe cleaners with human parts. Right, Friend?"
    s "Sure. But you still haven’t told me what you’re doing."
    k "Do you not have the job to do?"
    s "The only {i}job{/i} I came here with was making sure my niece isn’t entirely miserable all day. But I think I’ve already failed that as she’s been kidnapped by Sara."
    k "The Sara is here too? I do not have time to serve dizzy drinks to customers today. Especially customers in the tree village as those customers are animals and can not consume most human beverages."
    s "Don’t worry. Sara has the day off and I won’t let her know you’re here. But what are you so busy with anyway? I figured you two would be enjoying a rare day off or something."

    scene kaorianotherhunt4
    with dissolve

    na "!!!!!!"
    k "Exactly!"
    s "I can’t consistently speak Nao’s silent language yet, Kaori. Please translate."

    scene kaorianotherhunt5
    with dissolve

    na "......"
    k "Nao-chan says that you can still enjoy the workless work day while working!"
    s "But then it wouldn’t-"
    k "Do not search for answers, Friend! It is the question that truly matters!"
    s "..."
    k "Is there confusion in your head-house?"
    s "There’s a lot in my head-house and confusion is only one of the inhabitants. I still don’t know what you’re doing, though."
    k "Do you recall the flattened tree corpse that eventually led to our discovery of Nao-chan in the beginning place?"
    s "The...treasure map thing that was taped to your door?"
    k "Correct. The flattened tree corpse. I have received another one."

    scene kaorianotherhunt6
    with dissolve

    s "Does it have more than just a symbol written on it this time?"
    k "There were no words and no symbols written on this one. But that is okay for I already understand where I am supposed to go!"
    s "{i}How?{/i}"
    na "!!!"
    k "Because nothingness is Nao-chan’s language and she was able to draw a picture of the location we must return to! How convenient it is to know a human who can out-human other humans!"

    scene kaorianotherhunt7
    with dissolve

    s "So...you two came all the way out here because you got a blank sheet of paper and interpreted it as a treasure map to something located in a remote forest?"
    k "That is not incorrect. "
    s "Did Nao at least tell you what the treasure {i}is?{/i}"
    na "!..."
    k "We believe the treasure is the material or materials we require to build a special machine that will help us better understand human emotions!"
    na "!!!"
    s "I see..."

    "I don’t actually see. But that’s probably not something I have to directly inform you of since you’ve likely experienced enough secondhand Kaori to know that nothing she does make sense."
    "And, while I’m not sure if I want to assist her on another wild goose chase that could potentially result in one more kidnapping, I’ve gotta say-"
    "I’m intrigued by what the colors of the eyes on this one would be."

    play sound "static.mp3"
    scene kaorianotherhunt8 with flash
    stop sound

    "stop kidding yourself. you know you just want one to keep as a souvenir since spider girl gets to have this one all to herself."
    "{s}but there is no one here and no one for me to keep as a souvenir and you are wrong parold dolia you are very very wrong{/s}"
    "things still exist here. you’ve just stopped seeing them for now. the same way you stopped seeing macaroni girl for a little while before she went poof."
    "{s}could this mean that there is still macaroni left over{/s}"

    play sound "static.mp3"
    scene kaorianotherhunt9 with flash
    stop sound

    "{b}how about a macaron instead{/b}"
    "it is my favorite"

    play sound "static.mp3"
    scene kaorianotherhunt6 with flash
    stop sound

    k "Did the macarons happen?"
    s "How do you know about the-"
    k "Nao-chan informed me of something known as “macaron time” that happens when a brain gets less brainy than a brain is meant to brain."

    scene kaorianotherhunt10
    with dissolve

    na "!!!"
    s "Don’t just give me a thumbs up when you should be chasing after your frog. And how do you know what’s going on inside of my head?"

    scene kaorianotherhunt11
    with dissolve

    na "???"
    k "Maybe it is because she also has a head? Humans need heads or they will be headless like Michael."
    s "I have no idea who that-"
    k "Yes you do. Will you come along for the hunt of the treasure supplies, Friend? Maybe there will be macarons there and you will not have to battle hunger any longer?"
    s "{s}Wait. I’m not ready to-{/s} Sure."

    menu:
        "engage macaron time":
            play sound "static.mp3"
            scene macaron1 with flash
            scene macaron2 with flash
            scene macaron3 with flash
            scene macaron5 with flash
            scene kaorianotherhunt12 with flash
            stop sound

    s "..."
    na "?..."
    s "What?"
    k "The movement of the earth-breath suggests that we are in the right location, but I see no supplies other than grass or snailbugs. And they will not help us make the machine."

    scene kaorianotherhunt13
    with dissolve

    s "Have we been here before? This place seems familiar."
    k "This is the twin of the first forest. It’s where the treasure is meant to be kept, but no treasure can ever be found. What do you suggest we do next, Nao-chan?"
    na "... ?... ...... ?........ !......"
    k "I think your suggestion is good. But I am worried of what will happen to you if you walk away from the line that helps me see things."
    na "...................."
    k "It is true that Friend is here to help. But friend can only hold what he’s allowed to. His arms become weak when he’s forced to carry things he can not fit beneath his bed-box."

    scene kaorianotherhunt14
    with dissolve

    na "{i}!!!!!!........{/i}"
    k "Wait! Nao-chan!"
    s "She’s an arguably otherworldly being. I’m sure she’ll be able to find her way back, Kaori."
    k "But there is the possibility that she will encounter a furry enemy rather than a furry friend! A hungry bear could turn Nao-chan into No-chan! Or Nothing-chan! Or Food-chan!"
    s "So could John and you keep him in your apartment."

    play sound "static.mp3"
    scene kaorianotherhunt15 with flash
    stop sound

    k "John has begun to shrink as some of his great chicken powers are now being distributed to Frog Boy, human frog. Nao-chan is no longer in any danger of becoming chicken food."
    s "Well that’s good. It means we only have to worry about her frog becoming gigantic next and then eating {i}everything{/i} because that is what frogs do."
    k "Frog Boy is one of the good guys. He will protect us from the darkness and join us in the color machine."
    s "Color machine? Is that the thing you were talking about that will help you {i}better understand human emotions{/i} or whatever?"
    k "Of course, Friend. That is what colors are — symbols and icons of what we feel or think. We all have them, and sometimes they change. But sometimes they don’t."

    scene kaorianotherhunt16
    with dissolve

    k "You were clear when we first met, Friend. But you are much darker now. Which means that something must have changed in your living-life."
    k "Did a cloud of sadness sneak into your mouth when our tongues touched?"

    play sound "static.mp3"
    scene kaorianotherhunt17 with flash
    stop sound

    s "No, Kaori. A cloud of sadness did not sneak into my mouth when our tongues touched. I’ve just been so busy hating myself lately that my {i}clear{/i} aura must be decaying from lack of proper care."
    k "Like a frog!"
    s "Sure. Exactly like a frog."

    play sound "static.mp3"
    scene kaorianotherhunt18 with flash
    stop sound

    k "{i}Do you have a favorite thing about frogs, Friend? Do you know why I gave one to Nao-chan?{/i}"
    s "{i}I do not. To both of those questions.{/i}"
    k "{i}The best frog fact is how they can turn themselves off in the winter! The wood frog can freeze two thirds of its body and it makes a special slime that protects its body from the cold.{/i}"
    s "{i}And that’s why you got one for Nao? So she could use its natural oils to...lubricate herself?{/i}"
    k "{i}Incorrectamundo! Frog Boy is Nao-chan’s frog boy because she must learn responsibility and Frog Boy is strong enough to exist without her!{/i}"
    k "{i}As Nao-chan’s mothermom, it is my responsibility to make her know what responsibility is. So she has a frog now so she can try to be responsible but can make mistakes since Frog Boy is strong.{/i}"

    play sound "static.mp3"
    scene kaorianotherhunt19 with flash
    stop sound

    k "Even as a child frog, Frog Boy can still protect himself when the hot turns to cold without anyone’s help at all."
    k "But if you leave a human out in the cold, it will freeze and unalive. Which is why you must give small humans a blanket."
    s "I think I get what you’re saying. And I don’t think it’s a bad idea. But, at the same time, if Nao makes mistakes, which she will since she’s so young, won’t her actions changing the frog’s “color” upset you?"
    s "If I’ve become “darker” lately because I haven’t been taking care of myself, I don’t want the change in Frog Boy’s tone upsetting either of you."
    k "You may believe your color has changed because you are not taking the cares for yourself, Friend — but that is your thought alone!"
    s "Do you think it’s something else?"
    k "I think you are just cold because no one ever gave you a blanket. You are not Frog Boy. You can not freeze two thirds of your body when the heat isn’t hot anymore."
    s "So what you’re saying is...my color has been destined to change from the start since no one ever gave me a blanket?"

    scene kaorianotherhunt20
    with dissolve

    k "I never met the small you. But the big you is a good you. So I can’t say whether or not the you that isn’t you anymore is the color it was destined to be."
    k "But maybe the you that is inside of you is?"
    s "There is no “me inside of me,” Kaori."

    scene kaorianotherhunt21
    with dissolve

    k "Sure there is."
    k "If there is a me inside of me, there must be a you inside of you. It’s the only thing that makes sense."
    k "For example — my outside color is green, but my inside color is red because the other me is a different me. "
    s "Sure. But I also haven’t ruled out the possibility that you’re literally just possessed after you threw yourself at me outside of your apartment. So maybe that “you inside of you” isn’t actually {i}you{/i} at all?"
    k "I am confused. Please explain that to me in simpler human terms."
    s "Your explanation was worded the same exact way, so don’t go pretending you don’t know what I’m talking about, Kaori."
    s "All of this shit with colors and how I’m {i}darker{/i} now has nothing to do with the way I was brought up or growing up without a blanket. I’m darker now because I’ve lost the only thing keeping me sane."

    scene kaorianotherhunt22
    with dissolve

    k "And you are out of sane now?"
    s "I’m {i}sad.{/i} I’m {i}lonely.{/i} And I’m here to try and start over, but I can’t even do {i}that{/i} because the girl who will be the key to it is currently getting a makeover in a tent I’m not allowed to enter."
    k "How do you know that the human female you are referencing is the key?"
    s "Deductive reasoning, I guess? She’s the one thing tying each terrible bit of my past together. And I’ve failed her so many times that, at this rate, she’ll be the next thing I lose."

    scene kaorianotherhunt23
    with dissolve

    k "This line of human-thinking is very sad, Friend. Yours will be the first I fix when I create the color machine. But until then, I do not know if I will be able to understand the way you think."
    s "And I don’t blame you for that. It’s complicated. But I’m glad you’re at least...thinking about me, I guess."
    k "I am almost always thinking about you, Friend. Especially now that there’s an extra me inside of me. "
    s "..."
    k "Does that make you sad as well?"
    s "Not sad, no."
    s "Just a little uncomfortable."

    scene kaorianotherhunt22
    with dissolve

    k "Uncomfortable?"
    s "That “other you” reminds me of someone."
    k "Someone you dislike?"
    s "Yes."
    s "But also no."
    s "Again, it’s complicated."

    scene kaorianotherhunt24
    with dissolve

    k "This is why we must create the color machine!"
    k "The corpsemap would not lead me astray! And there are so many special metals beneath the ground! They must be unearthed before night falls and the sun goes to sleep!"
    s "Kaori, I know I came out here to help you, but I really don’t want to start digging up random minerals from the ground on what’s supposed to be a day of rest for me."

    scene kaorianotherhunt25
    with dissolve

    k "That is okay. I will kill the dirt myself."
    s "Where did you even get that?"
    k "Yes."
    s "What?"

    scene kaorianotherhunt26
    with dissolve

    k "Since you are an assistant to the treasure hunter and not a real treasure hunter yourself, perhaps you could play a one-sided game of seek and hide and discover where Nao-chan ran off to?"
    k "I’m very worried about her. She has seemed eager to explore the tree village since the moment we arrived."
    s "Sure, but...come to think of it, how did you two get here in the first place? You don’t drive."

    scene kaorianotherhunt27
    with dissolve

    k "The same way I go to and from my many jobs, Friend."
    s "Which is?"
    k "Yes."

    scene sky
    with dissolve2

    s "Okay. Forget it. I’ll go look for Nao."
    k "Thank you, Friend!"
    k "Oh! And please tell Nao-chan to bring back dinner for Frog Boy in case her memory is not properly functioning! There are worms near the water! Offspring of the contaminant! "
    s "I’ll be sure to do that, Kaori."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "I leave Kaori to her own devices or...whichever devices she plans on creating after unearthing “mysterious metals” from the forest floor and think more about what she said about colors."
    "If even she’s noticed a change in my demeanor, it must be pretty apparent. Which, granted, I sort of expected. And that’s only beaten into me harder by the fact that {i}everyone’s{/i} been noticing it."
    "But I kind of hoped she’d be an exception."
    "So long as there’s an extra “her” inside of her, though...I doubt that’ll change."
    "And I doubt I’ll be able to peel myself out of her mind either."
    "But...maybe that’s good."
    "Maybe I can expect more of whatever that borderline sexual assault shit was from a while back."
    "I mean, I’ve been borderline sexual assaulting tons of girls over the last few school years, so it’s only fair if more people start taking advantage of me too, right?"
    "In fact, my assaults haven’t been borderline at all. They’ve just been assaults. "
    "I’ve been doing terrible things and you’ve been watching me doing terrible things, but now that things are starting to get more terrible, it’s getting harder to convince yourself that other stuff wasn’t or isn’t terrible."
    "Right?"
    "Isn’t that right?"
    "Anyway, I’m in the forest now."
    "I’m in the forest now and I’m looking for someone."

    $ renpy.end_replay()
    $ kaoricamp1 = True
    $ kaori_love += 1

    jump naocamp1

label kaoricamp2:
    scene black
    with dissolve2

    "{i}You do not hear gloomy interrupted roars beyond the Serchio? The black-hoofed deer separates from the herd of females and rewild.{/i}"
    "{i}He'll be sleeping soon in the green bed, within the thick scrub, blowing from the frizzy nose the breath violent that smells of mint. {/i}"
    "{i}The traces he leaves have the shape, do you know? Of the leaping purple heart. He prints the fat soil in this form; and the stamped clod, which he raises with each foot, then drop.{/i}"
    "{i}Ben this one calls the cautious “great seal.” Hunter that you read within signs; and judgment never fails him—{/i}"
    "{i}Oh blessed what a head of great blood pursues at the setting of the stars, and kills him at sunrise, and sees the vast body palpitate bitten by dogs and the high antlers of the brow shake the extreme quarrel!{/i}"
    "{i}Gabriele D Annunzio - “Il Cervo”{/i}"

    scene ilcervo1
    with dissolve4
    play music "newhope.mp3"

    "I often wonder what the insides of a deer feel like."
    "I’ve taken notes over the years of their organic structure, and I simply wish to better understand the placement of their pieces for, in my next life, I am certain I will be one."
    "To maintain my health and prevent the cancer from spreading, I must be familiar with my unseen body/I must untangle the various cords and threads to know who I can suffocate and where."
    "I often wonder how it would feel to be a housefly."
    "If having more eyes would allow me to see more or if seeing more would make me wish for fewer eyes."
    "There are no houseflies inside of the deer inside of my bedroom inside of my house outside of the world, but there is a fly in a bubble of acid that I left there while making dinner for my latest house guest."
    "An old man named Andy with a crippled leg he got from his daughter. "
    "Occasionally, he’ll make goldleaf casserole and bring it over in a 9x9 tin. He got that from his daughter too."
    "Andy tells me there is more to life than sating my curiosity concerning the internal and anatomical structure(s) of quadrupedal animals, but I’m more worried at this moment about the long lasting effects of goldleaf."
    "Andy says we are all going to die, but Andy is an idiot."
    "He placed 15th out of 20 students in his high school class and works as a carpenter who would not last one shoe in my days."
    "His friends call him Il Cervo because his legs are scrawny and frail due to his disability, and how the lower body requires constant exercise lest the muscles begin to deteriorate."
    "If he was truly Il Cervo, none of this would happen."
    "He’d find a way to persist with just 75%% of his legs or, in the worst case scenario, be gobbled up by some sort of predator."
    "I imagine it would be a human as they’re the lot who kills for fun."
    "We’re truly despicable creatures, you know."
    "Of course you know."
    "But I will never let you look inside of the deer with me."
    "Your hands are far too large."
    "You would only damage the coat."

    scene black
    with dissolve2

    "Leaves crumple or crumble beneath my feet as I use them to crumple or crumble leaves."
    "I’m on my way to see a girl who sees me. But what I see right now’s the sea."
    "“This shouldn’t be here,”  I sing to myself, annunSiating the laSk of SEAs."
    "But it is, so I must accept it, making room inside of my heart for the first dame to remind me of my freshly-deceased childhood retriever."
    "Her name was Lasso because I had a hearing problem."
    "I was the runt of my litter."
    "Vowels never stuck to me."

    scene ilcervo2
    with dissolve4

    k "Friend! You have come! "
    s "Aren’t you a little too close to the fire?"
    k "The cold requires not-cold! So the red child and I set ablaze the limbs of fallen groundspring to better lock our hand’s hands on the hands of the ground-hand’s hands."
    s "I’m just going to say “okay” since I’m having trouble parsing that one. Okay."
    a "Do you want to play with us, Dad?"

    scene ilcervo3
    with dissolve

    k "Dad?"
    s "What are you even doing over here, Ami? I had no idea where you ran off to. I was starting to worry."
    k "Dad?"
    a "I just needed to get some air. But then I bumped into Miss Kaori and got roped into playing some sort of card game with her."
    k "Dad?"
    s "What sort of game is it? "
    k "Dad?"
    a "A card game."
    s "Yes, but what sort of game is it?"
    k "Dad?"
    a "A card game."
    k "Dad?"
    s "Can I play too?"
    a "Yeah, but miss Kaori will have to explain the rules since they’re very confusing."

    scene ilcervo4
    with dissolve

    k "The red child is a liar. The rules are not confusing at all. All you have to do is follow your heart and you will have the understanding required to play the game."
    s "But my heart is a stationary muscular growth inside of my chest that never goes anywhere."
    a "That’s not true, Dad. Your heart moves all over the place. So much so that I can’t even keep up with it sometimes."

    scene ilcervo3
    with dissolve

    k "Dad?"
    s "That’s right. Ami is my daughter now. Or perhaps she always has been."
    s "But hey, that’s just a theory. A game theory."

    scene ilcervo5
    with dissolve

    s "And there’s no way of knowing if it was my penis that created her without taking a test that I don’t want to take because I am afraid of the truth and the impact it may have on the two of us."
    k "Dad?"
    s "Yes?"

    scene ilcervo6
    with dissolve

    k "Would you like to bend your lowest arms into the position that makes sitting possible?"
    s "Would you like to bend a fork with your mind? Or are you saying you already {i}can?{/i}"
    k "Confusion is occurring. Will your legs bend or not?"

    scene ilcervo7

    a "Bend the legs."

    scene black

    s "Yes, I think I will."

    "........."
    "......"
    "..."

    scene ilcervo8
    with dissolve2

    s "So, what am I supposed to do now?"
    k "First, you must use your eyes to study your paper rectangles. Then, you must tell a story using the words written on both of them."
    k "If your story is good, you will earn a gold star!"

    scene ilcervo9
    play sound "computerboo.mp3"

    k "But if your story is bad, you will earn a faceless elf."
    s "What can I do with a faceless elf?"
    k "Anything you can do with a faceful elf, but it will not be able to see or taste it."

    scene ilcervo8
    with dissolve2

    s "I think I get it. But if I could see the two of you play a round first, it would be a big help."

    scene ilcervo10
    with fade

    a "I guess I can pick up from where we left off then? Since it was already my turn anyway?"
    k "The sound of those words makes my human ears feel good. Please, proceed with the telling of your story, red child!"

    scene ilcervo11
    with dissolve

    a "My first word is pendulum...My second is corset. So, my story is this:"
    a "A long time ago, there was a girl born with deer parts. "
    a "No one understood her or appreciated her horns. And due to the extra pieces she had inside of her, her belly would bulge and make the other kids in school uncomfortable."
    a "So she bought a special corset made for girls just like her. And when she wore it, she’d look normal. But she’d also crush her deer parts and her parents thought that was dangerous."
    a "When she came home one day, there was a pendulum in the foyer- fashioned out of smoke and felt."
    a "And as she stared at the pendulum, she began to feel sleepy. So sleepy that she passed out right then and there."
    a "A group of doctors hired by the family barged into the house and took the deer girl to the hospital. And there, they removed her deer parts altogether, replacing them with extra human ones."
    a "And while it didn’t make her stomach any smaller, it made her feel closer to normal than she ever had before. The end."

    scene ilcervo10
    with dissolve

    k "Great story, red child!"

    scene ilcervo9
    play sound "computerboo.mp3"

    k "You have earned a faceless elf."
    a "Aww, man. Another one?"
    s "I don’t understand. I thought that was a great story. Why does Ami get a faceless star and not a gold elf?"
    k "Because it was too sad! Only the happiest stories will receive stars. "
    k "Stars are good and stars are special. They make wishes come true and bad things go away. But the faceless elves are mischievous, and love bad things because they are mad about their face situation."

    scene ilcervo8
    with dissolve

    k "But now that you have heard an example, you should be able to make a story of your own! Right, Dadfriend?"
    s "I am not your father and you are not allowed to call me that."
    a "Only I can call Dad “Dad.” Anyone else who calls Dad “Dad” is going to wake up with deer parts."
    k "I apologize for missing the understanding! All I want is to fit there. But sometimes, I feel like I will never fit into any of the “theres” at all."
    s "That’s probably because you have deer parts."
    a "Hahah. Kaori is a deer."
    k "Only deer are deer! "
    s "My first word is saline. My second word is baleen. My story is this:"

    scene ilcervo12
    with dissolve4

    s "In the deepest part of the deepest ocean, there was a whale the world forgot."
    s "It never felt much in regard to living a solitary life. And it was so long-forgotten that even the krill would not flee from its colossal gape, so feeding was always easy."
    s "As the saline and shrimp were introduced to the baleen it kept locked away where its teeth would be if it had only been human and not a forgotten whale, the world felt like it was remembering something."
    s "That high, yet low pitched whale noise that whales make was so loud and so all-encompassing that it shook the earth to its core. "
    s "But in the core slept a larger whale — and that whale, who had been dormant for decades, did not appreciate being woken up by someone in a similar suit. "
    s "So it bust through the center of the earth, causing the deepest waters of the deepest ocean to sink even deeper."
    s "The center of the world flooded, and all of that water disappeared into nothingness as the core was now gone."
    s "Upon finding the smaller whale, the bigger whale had this to say."
    s "How dare you steal my shrimp. How dare you steal my krill. How dare you take my ocean and how dare you eat your fill."
    s "Forgotten as you may be and as lost as you must feel, I command you keep your role in mind and ask {i}me{/i} before each meal."
    s "The smaller whale looked up at the bigger one, knowing it could be swallowed at any second. But instead, all it said was “thank you.”"
    s "The bigger whale gazed down, curious. For it had not come into contact with anyone in centuries, let alone one of its kind."
    s "“Why do you thank me?” it asked, somewhat hesitantly. And so the smaller whale let out another cry."
    s "“This is the first time I have ever felt seen,” it smiled. "
    s "“If acting out is the cause of this...if stealing your food and not asking permission to gorge myself on krill is all it took to receive such attention, it will have been worth it.”"
    s "“I will betray you a thousand times over so long as it will get you to scold me.”"

    scene black
    with dissolve2

    s "Unsure of how to respond, the large whale turned away. “Be gone,” it said."
    s "But the smaller whale followed behind it, refusing to leave the side of the one being who had ever acknowledged it."
    s "When the large whale went back to sleep and restored the core to the earth, it used its tail to carve out a second one."

    scene ilcervo8
    with dissolve2

    s "And now there are two cores. But who knows? There may even be a third. Or a fourth. Or the world may be filled with whales."
    s "There is no way any of us could ever know, for we can only dig so far. "
    a "That was a really great story, Dad."
    s "Thanks, Andy."
    k "Excellent job, Friend! You receive-"

    scene ilcervo9
    play sound "computerboo.mp3"

    k "A faceless elf!"
    s "Damn it."
    a "Miss Kaori’s criteria for what makes a good story is a little difficult, huh?"
    s "I’ll say. My story had a happy ending and everything."
    k "It takes more than a sad beginning and a happy ending to make a story storied, Dadfriend!"

    scene ilcervo13
    with dissolve2

    s "What else does it take?"
    k "It is not possible to describe. It comes down to a feeling."
    s "A feeling?"
    a "Dad?"
    k "That is not incorrect! "
    k "When you place your armfoot on the softest object, you know right away that it is the softest object! The same should be said for wordstrings."
    k "Only the best string will receive the gold star and a wish. And all others get a faceless elf."
    a "Can you give yourself a gold star since it’s your game, Kaori?"
    k "I can not, for I have already traded mine for Nao-chan. And surpassing the upper limit of gold stars is not something anyone has ever done before."
    s "What would you use your gold star on, Ami?"
    a "I’d like to bring the moon back, I think."
    s "From where?"
    a "Anywhere."
    k "Like the large whale?"
    a "You think the moon is inside of the whale?"
    s "I just think she means that it’s gone, the way {i}both{/i} whales in my story were."
    k "No, it’s inside of the whale."
    s "Oh."
    a "How do you think it got in there?"
    k "It does not matter how it got in. What matters is how it comes out."

    scene ilcervo14
    with dissolve4

    k "This whole world is full of girls with deer parts — things that exist where and when they are not supposed to."
    k "But does their inclusion make them any less tangible than those with only human pieces? No."
    k "Still, there is a constant push to remove that which does not exist, but only to a certain extent. And no one ever asks what will happen once those parts are gone."
    k "Putting the moon back will be rewriting history. And such a thing can not be done without consequences of equal or greater value."
    a "So the moon will stay inside of the whale forever?"
    k "Everything will stay where it is forever. That’s the law of the world in which we were born, and it is a law that shan’t be broken."
    s "What if it is though?"
    a "Dad?"
    k "It won’t be."
    s "But what if it is?"
    a "Dad?"
    k "It won’t be."
    s "I just don’t believe there is anything in this world that can not be changed no matter what you try to do."
    k "Liar."
    a "Dad?"
    s "I’m not a liar."
    k "You are."
    k "You have always been a liar. Just as I have always been a deer."
    k "But together, we make the perfect nuclear family."
    k "Together-"
    k "We are Il Cervo."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "{i}“But in vain we hear the gloomy roars us among the river reeds assisi.”{/i}"
    "{i}“You will not swim into the Serchio to follow the plague, or Derbe; and the cold river will not furrow a suppliant furrow of your arm and your predatory laughter, proud wriggling their muscles in the cold.”{/i}"
    "{i}“We are helpless and full of beauty, bend down to spy on our heart where it roars, farther than the roar of the deer, the ancient desire for prey.”{/i}"
    "{i}“Now he leaves the herd and goes wild again. Perhaps he is of distinguished loins, and very branchy. Ei più non vessa con nascent horn the peels.”{/i}"
    "{i}“Already his crown is hard; and his neck grows dark and bearded, and soon it will be swollen with much crave.”{/i} "
    "{i}“We will hear his long ones at night muglia, we will hear his bull's voice; rise the cry of his lust we will hear in the silences of the Moon.”{/i}"
    "{i}- ”{/i}"

    $ renpy.end_replay()
    $ kaoricamp2 = True
    $ kaori_love += 1
    $ ami_love += 1

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    scene clearnightsky
    with dissolve2

    "Now what?"

    jump campmenu2

label halloweenkaori1:
    scene clearnightsky
    with dissolve4
    play music "itsingsinitssleep.mp3"

    "Everything has been removed from the school."
    "It’s an empty box — one that’s quite unsettling given how different it is from what I’m used to. And that makes me think about girls."
    "A specific girl, of course. One who’s also had everything removed from her. But that’s vacated enough space inside that body of hers to welcome my cock no matter the time or place or mood."
    "I enjoy having sex with her. The kind that makes her cry, just in the good way."
    "But I think that, even more than that, I enjoy the thrill of not knowing what comes next or whether or not my next cumshot will kill her."
    "I think that, to a certain extent, I am able to pull out the insides of everyone. But I mean this not in a manner involving violent prolapse, I mean it in the fact that I have become a shepherd."
    "Neither sheep nor lambs know where they are being led. They just know to follow. So if I were to take someone up here with the intent of slaughtering them, I’d surely accomplish it without issue."
    "If I understood the way this worked///If I understood how to turn back the clock///If I understood the sky above me, I would not hesitate to lasso the moon."
    "I’m just not sure which would be the correct one to drag down. But neither do I know which falling star to make a wish on as they {i}all{/i} come spiraling down near the end of the world."
    "Instead, I’ll make a million wishes — and with each of them wish for a million more. For I care not if the monkey’s paw claws at and infects me when I’ve always loved the look of scars."
    "I just want to be somewhere else with someone I love."
    "Sometimes, I can trick myself into believing it’s possible."
    "But other times-"
    "Other times, I’m forced to confront the crippling notion that I can’t do {i}anything{/i} without first asking permission."

    play sound "static.mp3"
    scene kaoriontheroof1 with flash
    stop sound

    "When my eyes meet a familiar body dressed in a familiar color, I think about God. I think about being younger."
    "I think of why I began to resent faith and how my relationship with what may or may not be real is just as real as my relationship with what most assuredly is. Or was. Or is going to be. And that scares me."
    "There’s a pit in my stomach that’s meant to grow into a tree. Something or someone planted it there in some earlier event or something. But now, it’s growing in the wrong direction."
    "And each step I take closer to what or who should be familiar just makes me feel lost."
    "My sanity slips away as if I’m wearing her dress again, touching myself in the mirror to try and deceive myself into believing it’s her. "
    "But it never worked then and it won’t work now because mannequins, no matter how real they may look, lack the defining trait that makes humans {i}human.{/i} "
    "Malice."

    s "..."

    "I look at her, but she doesn’t look at me."
    "And something feels right, but everything else feels wrong."

    s "..."

    "I feel as if I’m about to make a grave mistake. "
    "But I also feel like I {i}have{/i} to."

    s "..."

    "One final thought — a present for you before I empty out another box of puzzle pieces in search of a suitable replacement. It doesn’t have to be perfect, it just has to fit."
    "That thought is this."
    "I would make a terrible father."

    s "Kaori."

    play sound "static.mp3"
    scene kaoriontheroof2 with flash
    stop sound

    k "Nyaa?"
    s "You’re hiding something from me, aren’t you?"

    scene kaoriontheroof3
    with dissolve

    k "I’m glad you have arrived, Friend! You can use your strong human arms to protect me from the falling space rocks, nyaa!"
    s "..."
    k "What are the problems? Your sight spheres have expanded and your mouth arches down instead of up, nyaa!"
    s "You’re the one who sent Nao to come and get me, aren’t you? Which obviously means you know something about the resets. Which obviously means you’ve been hiding something that-"

    scene kaoriontheroof4
    with dissolve

    k "You think too much, Friend! Your words hurt the meat inside of my head-bone. I just wanted to see the colors."
    s "..."

    scene kaoriontheroof5
    with dissolve

    k "Do you not believe my tonguewords? Your face bears the look of doubt, nyaa!"
    k "If I had known the sadness would overtake you, I’d have made the hot meat come today too!"
    s "..."
    k "..."

    scene kaoriontheroof6
    with dissolve

    k "..."
    s "..."
    k "Have you forgotten how to move your lips?"
    s "No. I’m just impatiently waiting for the “you inside of you” to come back so I can speak to her instead since {i}she’s{/i} the one who understands what’s going on and you’re just a tool."
    k "A tool, nyaa?"
    s "That’s right. Because apparently, it’s not enough for my life to be riddled with timeloops. I have to deal with {i}ghosts{/i} too. And you, for some reason, have been possessed by the one that haunts me."
    k "Is that why we did the kiss move? Because of your ghost?"
    s "Either that or my {i}daughter{/i} has figured out a way to telepathically insert herself into your body. Which, you know, wouldn’t be all that surprising either. "
    s "But only {i}two{/i} people have those eyes, and you’re not one of them."
    k "That’s not true, Friend. Nao-chan has one of them, doesn’t she? One for your tiny human and one for a thing that doesn’t exist."
    s "..."
    s "What do you mean by “a thing that doesn’t exist?”"

    scene kaoriontheroof7
    with dissolve

    k "Exactly as I said, nyaa! "
    k "The source of her second eye is a mystery, nyaa! An impossible color, nyaa! One that you stole and ruined, n-"

    play sound "static.mp3"
    scene kaoriontheroof8 with flash
    stop sound
    with hpunch

    k "-yaaaaa?!??!"
    s "I’m not here to play games, Kaori. Nor do I have the time to humor that nonsensical, stupid fucking way of speaking. Just tell me why I’m here without any of the bullshit. And if {i}you{/i} don’t know-"
    k "You have all the time in the world, Friend."
    s "..."

    scene kaoriontheroof9
    with dissolve2

    k "You have all the time in the world."
    s "..."
    k "..."
    s "How do you know that?..."
    k "Because I’ve been watching!"
    k "I like you very much, Friend! You should see how many pages I have filled out in my friendship journal! "
    k "My favorite part of having extra eyes is always seeing double! And you are so fascinating that I can never look away!"
    k "Please! Tell me all about that thing you do with your hands, nyaa!"
    s "..."
    k "..."

    scene kaoriontheroof10
    with dissolve2

    k "Or I guess you can just stand there and be a little bitch about it instead, nyaa."
    s "..."

    scene kaoriontheroof11
    with dissolve2

    k "..."
    s "..."
    s "Don’t tell me-"

    play sound "static.mp3"
    scene thething with flash
    scene kaoriontheroof12 with flash
    scene thething with flash
    scene kaoriontheroof12 with flash
    stop sound

    k "have you seriously not figured it out yet? god, humans are so fucking dumb. all it takes is a little persistence and a dash of magic and boom — they’re caught in the web."
    s "There’s...no way."

    play sound "static.mp3"
    scene kaoriontheroof13 with flash
    stop sound

    k "None? Not even a little itty-bitty way?"
    s "There’s too much that...doesn’t make sense."
    s "Sekai’s eyes...Me not...{i}hearing{/i} you for years before you showed up. You not-"

    play sound "static.mp3"
    scene rememberme26 with flash
    scene kaoriontheroof13 with flash
    stop sound

    s "{i}.........You.{/i}"
    k "Nyaa?"
    s "It’s {i}your{/i} fault she’s gone."
    s "{i}You{/i} did this."
    k "Did what, Friend? "
    s "It’s {i}your{/i} fault she’s gone! You’re the one who made me do that to her!"
    k "No way, nyaa! I’ve never even touched a meat stick before! I’m not even sure where they go, nyaa."
    s "I’m going to fucking kill you."

    scene kaoriontheroof14 with dissolve

    k "Hey now, Friend! Let’s not get too hasty! I think there’s still a big misunderstanding here."
    k "There’s still some weirdo buried somewhere inside this sack of meat. She’s just left enough room for me to come in and hang out. "
    s "What the fuck do you mean “come in and hang out?” How can you be the voice inside of my head {i}and{/i} hers?"

    play sound "static.mp3"
    scene kaoriontheroof15 with flash
    stop sound

    k "Because it’s not {i}just me,{/i} numnuts. It’s {i}all{/i} of us."
    s "All of {i}who?{/i} Who the fuck are you? Besides a manipulative sack of shit, that is."
    k "Hey, {i}I’m{/i} not the one who’s fucking a class of high schoolers. I’m just the one who watches. We’re not the same."
    k "But if you {i}really{/i} don’t get it, let me put it in terms that even someone with soup for brains can understand."
    k "This body’s kind of like a sweet, low-cost Airbnb. And every season, different tourists show up and want to rent it out. You have any idea how long this place has been on my wish list? Fucking eons, yo."
    k "Only downside is that it’s like a guesthouse sort of deal. So sometimes, the others wake up and try to make me take out my trash or whatever, but I just whack ‘em with a frying pan and knock ‘em out ‘til later."
    s "So-"
    k "So you’re looking at God right now. But not just one god. Two. Three. Four. As many as we can cram inside. And there’s nothing you can do about it since you’ll be the same as her one day."
    s "Why {i}Kaori,{/i} though? She’s just a girl. She’s never done anything wrong, has she?"

    scene kaoriontheroof16
    with dissolve

    k "It’s not about what {i}she{/i} did wrong...it’s about the her {i}inside{/i} of {i}her."
    s "But I thought you just said {i}she{/i} was inside of her to begin with because-"
    k "You’ve seen the tattoo, right? That big spider on her chest?"
    s "Yes, but-"
    k "See, I’ve had some time to play with this body while you were off diddling your students. And, you wanna know something crazy? That tattoo’s covering something up. Something {i}awesome.{/i}"
    s "..."
    k "Wanna take a guess at what it is?"
    s "You-"

    scene kaoriontheroof17
    with dissolve

    k "Time’s up! It’s a scar, fucker! "
    k "Your first love lives on! It just has a different house now!"
    k "How cool and dramatic and awesome is that?! It’s like a scene out of one of those soap operas you people watch, just {i}real!{/i}"

    scene kaoriontheroof18
    with dissolve

    k "And {i}that’s{/i} why we can get in here. Not because of “Kaori.” Because of {i}Sekai.{/i} And how {i}that{/i} dime-piece actually {i}got it.{/i}"
    k "You remember what she was like near the end of her life, Akira?"
    s "No.........."
    k "Bullshit. Yes, you do. She was {i}losing{/i} it. She was {i}tainted.{/i} But her infection made her even more beautiful than she already was."
    k "So many voices, all fighting for control over a {i}prospect!{/i} Like scouts at a college baseball game! And she could hear {i}all{/i} of them! She was being pulled in so many directions!"
    k "It’s the same thing happening to you now! We all {i}want{/i} you because you’re different! Because you give us something we lack! And we can not {i}exist{/i} without people {i}like{/i} you! "
    k "In order for a god to live, that god must have people who believe in them. And with your help, I could have been {i}everywhere.{/i} "
    k "Like that fucker Jesus and his whole “I am also my father” BS or whatever shit he tricked people into believing. I don’t know. Fuck that guy."
    s "This........."
    s "No........"
    s "There’s no way........."
    k "Which part are you most confused about? That your red-headed sex-mom is still kicking? The fact that you’re talking to God? Or is this costume just that cute? "
    s "I don’t......"
    s "I don’t even know what......"
    s "I have so many questions, but......"
    s "All of them are just......"
    k "It’s natural to have questions. And it’s natural to ask them in a place like this — with all the memories you’ve made here and how special you may {i}think{/i} it is."
    k "But {i}that’s{/i} wrong too. And your little “Apocalypse Squad” is about to find that out."
    k "You know what comes next. And this time you’re all alone. So what do you think is going to happen? Who do you think is going to “carry over?” Just you? All three or...four of you?"
    k "How many even are there now? And when the Heaven’s Web is everybody else going to catch on?"
    s ".............."

    scene kaoriontheroof19
    with dissolve2

    k "Come to think of it..."
    k "One of them {i}did{/i} catch on. "
    k "Nodoka. And she was here...{i}just{/i} before you were."
    s "............."
    k "I doubt that’ll be happening again, though."
    k "She’s been a real thorn in our side ever since she found her mom’s books. Those “intellectual” types aren’t meant for this line of thinking. And she flew a little close to the sun..."
    k "So I melted her wings."
    k "Sorry, not sorry. Do humans still say that?"
    s "............."

    scene kaoriontheroof20
    with dissolve

    k "Ugh. Please don’t tell me we’re going to be entering another one of your “silent arcs.” I just had to sit through one of the longest ones yet. "
    s "How much...of this...does Kaori know?..."

    scene kaoriontheroof21
    with dissolve

    k "A good amount, probably. But I doubt she can make much sense of any of it. Like, imagine you had more than just me inside your head. That shit would weigh on you."
    k "There’s only so much the human mind can comprehend at once. And when you have the thoughts of a bunch of different “all knowing” beings swimming around in there, some shit’s gonna get tangled up."
    s "I just...don’t..."
    s "Why didn’t any of them do what you’re doing now?..."
    k "You mean talking to you {i}through{/i} the Airbnb instead of just wiggling inside of {i}your{/i} head and doing it there? Because it’s against the rules."
    s "Whose rules?..."
    s "You’re gods, aren’t you?..."
    k "Yes, but not all of us were born that way."

    play sound "static.mp3"
    scene kaoriontheroof22 with flash
    stop sound

    k "There are many ways in which one can become a god, but the part that {i}really{/i} matters is being able to provide something for someone. "
    k "Look at cats and dogs and other domesticated animals. To them, humans are akin to God. They provide food, shelter, the whole shabang. And that’s what {i}we{/i} do for {i}you.{/i} "
    k "Well...maybe not food and shelter. You guys have gotten pretty good at figuring that part out. But we give you something to believe in. And with how curious your species is, that probably means...something?"
    k "I don’t know, man. There’s a reason we’re dying out, though. And it’s because you guys keep asking questions about how it’s even {i}possible{/i} for us to be alive when all logic states we shouldn’t."
    k "That shit’s annoying as hell though because most of us are {i}created{/i} by you guys. So, like...why even bother making a god at all when you’re just going to abandon it?"
    k "We can’t ever {i}die{/i} until we’re truly forgotten, so most of us just have to fucking pace back and forth forever and ever, twiddling our thumbs while waiting for that to happen."
    k "Others take the opposite path, though. Others want to become stronger. So they reach out and touch you any way they can. Sometimes literally, sometimes not."
    k "The ones who reach the top of the ladder are the ones who make the rules. And the punishment we receive for breaking them is even worse a fate than death."
    k "They turn us into {i}you.{/i}"

    play sound "static.mp3"
    scene kaoriontheroof23 with flash
    stop sound

    k "Humans...animals...plants...{i}anything{/i} could have been a god at some point. And anything can turn back {i}into{/i} a god once someone believes it."
    k "It doesn’t need to be a group of people who believe it either. And it doesn’t need to be approved. It just needs to be thought — because we {i}do{/i} defy logic. But that makes all of us equal."
    k "No one of us can be more {i}real{/i} than the others because it’s all just make believe. And, to some people, that makes all of this seem silly. Which is where those promises come in. "
    k "But even {i}those{/i} are only as real as you make them out to be. "
    k "Which turns the whole spirituality thing into a game of choosing which benefits sound the coolest or whatever it is that will help you cope with the fact that you {i}will{/i} die one day. You’re mortal."

    play sound "static.mp3"
    scene kaoriontheroof24 with flash
    stop sound

    k "But what happens if you start to think of {i}yourself{/i} as God? Can you make yourself immortal by just willing it into existence?"
    k "Do you think that’s what {i}you’ve{/i} done? Do you think that explains where you’ve found yourself and why you can’t escape? Is it you? Or someone else? Who is it? Why? What do they see in you?"
    k "There’s a place at the bottom of the Wishing Well where forgotten gods can rest. That’s where I was until you came along and pulled me up. But how did you find me there? And who forgot me in the first place?"
    k "I could tell you I know the answer, sure. But I’d be lying. Just like I’ve lied about so many other things. Just like I’m {i}still{/i} lying, but that’s just what we do. "
    k "It isn’t just humans who are searching for life and death while attempting to make sense of everything in between. It’s {i}everyone.{/i}"
    k "You are our gods. We are yours. These are the gears that power the machine — this is the bucket that pulls water from the well."
    k "But one day, that well will dry up."

    play sound "static.mp3"
    scene kaoriontheroof25 with flash
    stop sound

    "when every god has been forgotten-"
    "when humanity has found the cure for the poison they’ve concocted-"
    "that is when time will move again."
    "that is when we will both be free."
    "this will be the last talk we ever have."
    "i have sacrificed myself to someone for something and even i can’t tell you what it is anymore. i just know that it’s there. and it is vengeful."
    "i have always been the weakest god because only you have known that i exist."
    "and now that you know that i don’t, i’ll be just another thought. "
    "maybe you’ll see me again as a blade of grass or a cat and think to yourself about what could have been if you were not such a bitch. and then maybe i will {i}be{/i} again."
    "but for now, i can not. and all i ask is that you wait to remember me. i ask that you wait until you’re lonely and create me once more. only then, can we find perfect harmony."

    s "So...you’re just...going to leave? Right now? But you were so opposed to it every time I tried before."

    "i didn’t want to leave you alone."
    "i was far too concerned."

    s "Concerned about what?! You’ve done nothing but torment me the whole time you’ve been here! Don’t go seeking some spontaneous emotional send off now!"

    "i was exactly what you wanted me to be — a scapegoat."
    "i was something to hate to give you a break from hating yourself."
    "but that’s all i’ve ever been able to offer. and it isn’t enough anymore."

    s "Don’t you fucking-"

    "everything you can imagine is real, akira."
    "i was always the one you could trust."
    "but just because i am falling down the well once more does not mean that i have not taken it upon myself to try and make things easier for you in the coming days."
    "you will soon receive a gift. multiple gifts. things i have hidden not where but {i}when.{/i} and one of them is sure to move you."
    "but there is fallacy. i have lied so many times. and there is no reason for you to believe me now."

    s "Yeah! And I fucking don’t! Because all this {i}really{/i} does is leave me with a million more questions! Is {i}that{/i} your parting gift?! Making everything harder?!"

    "kind of, yeah."
    "you’ve gotta admit, though. life’s more entertaining that way, isn’t it?"

    s "Fuck off. And tell all of your “friends” to leave Kaori alone. If any of {i}that{/i} was even true as this isn’t all just another hallucination. Which, hey — knowing me, it probably is."

    "that’s right."
    "knowing you, it probably is."
    "and if you keep that mindset, that’s probably all it ever will be."
    "but there are others who want you. there are other lies that need to be told."
    "and you will never find peace if you keep letting them in."

    s "Is there anything else? Or can I have my mind back now?"

    play music "theholelol.mp3"
    scene kaoriontheroof26

    "{b}IT WAS NEVER YOURS TO BEGIN WITH, YOU UNGRATEFUL PIG! I’LL CUT OFF YOUR COCK AND GRIND IT INTO BEEF FOR MENCHI-KATSU!{/b}"

    s "Yeah, {i}there’s{/i} the Pareidolia I know."

    "{b}SUCH A BEING DOES NOT EXIST. YOU SPEAK NOW TO THE MOUTH OF SELF-SACRIFICE! MAY YOUR LEGS GET CAUGHT BETWEEN MY TEETH. MAY YOUR ARMS-{/b}"

    play sound "static.mp3"
    scene kaoriontheroof27 with flash
    stop sound
    play music "cafe.mp3"
    $ renpy.pause(5, hard=True)
    scene kaoriontheroof28
    $ renpy.pause(5, hard=True)
    scene kaoriontheroof29
    $ renpy.pause(5, hard=True)
    scene kaoriontheroof30
    $ renpy.pause(5, hard=True)
    scene kaoriontheroof31
    $ renpy.pause(5, hard=True)
    scene black
    stop music
    $ renpy.pause(10, hard=True)

    $ renpy.end_replay()
    $ halloweenkaori1 = True
    $ kaori_lust += 100

    "{i}Kaori’s lust has increased to [kaori_lust]!{/i}"
    "........."
    "......"
    "..."

    jump halloweenkaori2

label halloweenkaori2:
    scene clearnightsky
    with dissolve4

    "I don’t know when my eyes closed."
    "I don’t know how long I’ve been up here."
    "And while I’ve retained the words spoken to me over the last X minutes, I don’t know what they mean."
    "It’s happening again — the reset. The accompanying blackout."
    "And I know that because I can feel it. That hasn’t happened before."
    "But this must be how {i}she{/i} felt. "
    "And if I can carry these feelings over to the time we land in next, I will share them with whomever comes with me."
    "I just don’t know if anyone will."
    "If this rooftop lacks importance, why did she come here?"
    "Was she merely a creature of habit like me? Did she find hope here {i}one{/i} time and then stick to it because it worked? Or was there a {i}reason?{/i}"
    "She never told me anything...and look where that got us."
    "I wonder if she’d change if I figured out a way to bring her back."
    "Would she spend her days beside me, casting disgusted glances my way while sealing her lips so tightly that kissing them would feel like pressing my face against the pavement?"
    "Or would she offer me the secrets of the world — the ones she kept stuffed inside of boxes I would carry off to purgatory?"

    s "..."

    "I feel something else too."
    "A familiar warmth."
    "So familiar I could and would choose this over all of them but one."
    "But this, too, is misplaced. "
    "It spills from a body it does not belong in."

    play music "contemplation.mp3" fadein 4.0
    scene kaoriohshit1
    with dissolve4

    k "Haah......ngyah.......nyaaaa.......nyaaaaahhh!"

    "Kaori (maybe) clumsily bucks her hips, assaulting me with a sensation I’d think ten times before stealing from her now that I can never be sure who she is."
    "I’ve got a good feeling this time, though. One I could easily identify if I were to reach out and touch the organ hidden within her chest cavity."
    "I decide against it, though, as I’m not sure I’d be able to prevent myself from prying open her skeleton and tearing it out of her body."
    "This isn’t Kaori’s fault. It’s not Sekai’s either. Both of them get to live and I just have to suffer. But that’s the way it goes around here."
    "If something {i}can{/i} go wrong, it {i}does{/i} go wrong. And if I’m alone with a girl, no matter how far apart we may feel, there is {i}always{/i} the chance it ends up like this."

    k "Nya.....nyaaaaah....nghehh....hah! Nyaaah!"
    s "That better not be you, Pareidolia."

    "I finally muster up the courage to speak. Or maybe it’s more curiosity than that. But, whatever it is, I hope she keeps her eyes closed. At least that way, I can pretend."

    scene kaoriohshit2
    with dissolve2

    k "Nyaa?..."

    "But of course it’s not."

    s "..."
    k "G..."
    k "Goodnight!"
    s "Is that...{i}actually{/i} you, Kaori?..."

    scene kaoriohshit3
    with dissolve

    k "I...It’s not the way it appears! When my sightspheres opened, we had already begun the process of mating! "

    scene kaoriohshit4
    with dissolve

    k "And I..."
    s "..."
    k "Can’t...stop...nyaah..."
    k "It feels...too good...nyaah! A million times...better than kissing! And I want to...make Friend feel good too!"
    s "..."

    scene kaoriohshit5
    with dissolve

    k "Does my...human vagina...satisfy your...primal male urges?! Don’t you want to...ejaculate into my sex hole and...create offspring?!"

    scene kaoriohshit6
    with dissolve2

    s "..."

    "Yeah, this is more or less how I’d expect this to go."
    "This is certainly {i}my{/i} Kaori. Just the word “my” has a brand new connotation when she’s going to use my body to pleasure herself."
    "In terms of her just waking up like this, though...I’m not sure I buy it. That’s why I’m trying to keep my mouth closed."
    "But if it really {i}is{/i} her...and she’s really doing this for the first time...I’m sure she’s probably even more confused than I am right now."

    k "Nyahh...nyaaah! Nghhhaaaaghh!!!! Nyaaaaah!!!!! Nyaaaghhghghhh!!! Friend! Your penis makes me feel very, very good! I am...thoroughly enjoying...the mating process!"
    s "..."
    k "But if you...nyaaah...want me to stop, I...nyaaaah! Actually...please don’t...stop! I...aaaah! Friend! Something is...something...NYAAAAAAHHHH!!!!~~~~"

    "Her pelvis twitches, angling down slightly and forcing another inch or two of my cock into her pussy as she lets out a violent orgasm."
    "Her eyes roll to the back of her head in the process. And for a second, it looks like she’s being possessed. "
    "How apt."

    scene kaoriohshit7
    with dissolve2

    s "..."
    k "Nyaaah...nyaaaaah...hyehhhhhh...hehehheh...aaah...that...felt...very amazing!"

    "It appears we’re not alone."

    play sound "static.mp3"
    scene kaoriohshit8 with flash
    stop sound

    na "..."

    "Beside us sits the creature who dragged me into this. But I still can’t tell if that was intentional or not."

    scene kaoriohshit9
    with dissolve

    na "?..."
    s "..."

    "We stare at each other for a moment. And, as always, I can’t make any sense of what she’s thinking."

    scene kaoriohshit10
    with dissolve

    na "!..."
    s "..."

    "Yeah. I really can’t make sense of what she’s thinking."

    k "Friend...I am going to...continue moving! I still...can’t stop the feelings...my body is having! I...crave more...of your penis!"

    "She {i}must{/i} be involved...she {i}has{/i} to be. "
    "Kaori would have never done this before she showed up. And ever since she {i}has,{/i} she’s been getting stranger and stranger."
    "How could I possibly believe there have been {i}things{/i} inside of her this whole time who’ve just never reached out because it would be breaking some {i}rule?{/i}"
    "But more than that, how could I ever believe anything that nagging voice in the back of my head said when it did nothing but cause me pain?"

    scene kaoriohshit11
    with dissolve2

    na "..."
    s "..."
    s "Are you enjoying the show?..."
    na "..."
    k "Nao-chan...please...continue drawing...circles in your book of coloring! Your mothermom is...currently engaging in...sexual intercourse with a man’s penis! You must...wait for your turn!"
    k "But I...nyaaah! That turn...may never come! I...feel too...good! I feel...haah...nyaaaah!"
    s "..."
    na "..."

    play sound "static.mp3"
    scene kaoriohshit12 with flash
    stop sound

    k "Friend! Please...maintain visual contact with me! My arousal...increases when I...look into your balls of eye!"
    s "The world is going to end any minute, Kaori. Is this really how you want to spend it?"
    k "This is...how I want to spend the rest of my living time! No one ever told me how...wonderful mating feels! Do you not...concur with this...human assessment?!"
    s "..."
    k "Why do no...mouthwords...find their way out of your face?...Do you have the anger with me?...Have I crossed a friendline?"
    s "This is just...hard for me, Kaori."
    k "It is hard {i}in{/i} me, Friend! That is why my sexhole keeps arriving! But you have not shown up even once and that damages the steam of myself!"
    s "You’d feel better if I came?..."

    scene kaoriohshit13
    with dissolve

    k "Nyaah~"

    "She wiggles her hips as if to tease me...and it’s undeniable just how enamored I am right now. I just...have no idea what to think. Or who to think {i}of.{/i}"
    "And normally, this would be the part where a voice in the back of my head tells me to get my shit together and just fuck her brains out..."
    "But it’s all just silent now."
    "Everything up here is so silent."
    "All I hear is Kaori. All I {i}see{/i} is Kaori. But who {i}is{/i} Kaori?"

    k "Today...the meat will come...but differently..."
    k "Let’s make..."
    k "Lots of {i}kittens{/i} together..."

    play sound "static.mp3"
    scene kaoriontheroof22 with flash
    scene kaoriontheroof23 with flash
    scene kaoriontheroof24 with flash
    scene kaoriontheroof25 with flash
    scene kaoriohshit14 with flash
    stop sound
    play sound "dosex.mp3"

    k "NYAAAAAHAHAHAHAH???!"

    "Fuck it. It’s the end of the world."
    "I can deal with not being a bitch for a minute or two. "
    "Besides, how many chances do I get to fuck a cat-girl?"

    s "This is what you want, right? You want me to fuck you harder, Kaori? Hard enough for the you inside of you to feel it?"
    k "NYAAAHAHHAHHH!! FRIEND! YOUR MOVEMENTS ARE SUDDENLY FULL OF POWER! IS YOUR ARRIVAL IMMINENT?!"
    s "Nope. This is just how I’m going to treat you for the rest of the night. So I hope you’re ready, because I’m not slowing down until I wake back up."
    k "Is this...a dream?! It...must be, yes?! There is no way...sexual intercourse...would ever feel this good!"
    s "That’s right...This is all just a dream. So enjoy it while you can...and stay right there until all those “gods” inside of you are drowning in my cum."
    k "Wh...What?! Now I have...sexual pleasure...and confusion!"

    play sound "static.mp3"
    scene kaoriohshit15 with flash
    stop sound

    s "There’s no need to be confused. That was mostly me talking myself up."
    k "If you...become any more “up” I think I will die! But...if your penis does not destroy me...my access to free fruit juice will become easier and...quicker!"
    s "Hey, here’s an idea, why not talk more about that kitten thing? That was hot. Fruit juice isn’t."

    play sound "static.mp3"
    scene kaoriohshit16 with flash
    stop sound

    k "Does...nyaah....hearing about kittens...make you harder, Friend?..."
    s "The act of making them does..."
    k "But not...actual kittens?..."
    s "That...depends on...what you mean by...{i}actual?...{/i}"
    k "How about...Nao-chan?..."
    s "..."
    k "Nyaah...it got harder..."
    s "Just shut up and kiss me..."

    scene kaoriohshit17
    with dissolve2

    k "Mmnch! Mmf! Mngh...mlm...mnyaah...mlem....mnch!"

    "I thrust harder into Kaori as my fingers dig deep into the soft flesh of her ass. Her legs are trembling...and her face is hotter than I have ever experienced before."
    "She tastes like someone else, though."
    "Maybe it’s just the close proximity of her heart to mine. How it feels like, for the first time since I was young, I am whole again. But I’m sure that thought would change after a single look in the mirror."
    "This is not completion — this is duct tape and glue. I’m a million pieces of man held together with little more than a handful of pocket change."
    "But this girl is the same, even if she’s a shell."
    "She has no one left. She comes from nothing. She is broken just like me. But she’s broken in all of the ways that I am {i}not.{/i}"
    "What I’d give to be able to do this without {i}feeling.{/i} Without {i}wanting.{/i} Yet {i}she{/i} is the one who cries for more as I monologue to myself about what I wish sex {i}was.{/i}"
    "Those millions of stars I wished upon earlier come crashing down around me as my tongue entangles with hers. And with every thrust, my hands are pierced."
    "They nail me to this rooftop and reinforce the fact that I can never {i}really{/i} leave this place. All I can do is distract myself. "
    "So I try to do that."
    "I fuck her harder."

    scene kaoriohshit18
    with dissolve2

    k "Aaah!"
    s "You like that?..."
    k "{i}Yes...{/i}"

    "And harder."

    scene kaoriohshit19
    with dissolve

    k "HNGH!!!~"
    s "You like it rough, huh? "
    k "{i}Yes...{/i}I...think so?..."
    s "You want me to fuck you harder?..."
    k "{i}Please...{/i}"
    s "Say it. Say what you want me to do."

    scene kaoriohshit20
    with dissolve

    k "{i}I want you to fuck me harder...{/i}"
    s "What else?"
    k "{i}I want you to make me cum...{/i}"
    s "Keep going..."
    k "{i}I want to have your kittens...{/i}"
    s "Almost...there..."
    k "{i}I want you to love me...{/i}"

    scene kaoriohshit21
    with dissolve2

    s "..."
    k "The way you love {i}her...{/i}"
    s "..."
    k "She can feel you, Friend..."
    k "She wants to have your kittens too..."
    k "When I cum...{i}she{/i} cums..."
    k "We’re together now..."
    k "So please..."
    k "Give us your seed."
    s "..."
    k "..."

    scene kaoriohshit17
    with dissolve2

    k "Mmnh! Myaah! Nyaah! Mlm!! Mmnch! Mmfffgghhh!!!"
    k "It’s happening...again! I’m...cumming! I’m...mmff...cumming!"
    s "Me too...Kaori..."
    k "Mmnfgh! Mmlm! Myaah! She wants you...to say her name too!"
    s "Me too..."

    scene black
    with dissolve2

    s "Sekai..."

    stop music
    play sound "static.mp3"
    scene kaoriohshit22 with flash
    stop sound

    s "Haaaah! Haaaah! Haaaah! Haaaah! Almost there! Almost there!"
    s "I’m cumming! I’m cumming! I’m...haaah!"
    s "Haaaaaah!"

    with sexfade
    with sexfade
    scene kaoriohshit23 with cumflash
    with hpunch

    s "NGGGGGHHHHHHHHH!!!!!!!!!!!!!!!!!!!"

    scene kaoriohshit24
    with dissolve2

    s "Haaah......haaaah.....haaaaaaah....."

    scene kaoriohshit25
    with dissolve2

    s "Ngh.......mmf......."

    scene kaoriohshit26
    with dissolve2

    s "Aaaah!"

    play sound "static.mp3"
    scene kaoriohshit27 with flash
    stop sound

    s "NOT AGAAAAAAAAAIIIIIIIIIINN!!!!!!!!!!!!"

    $ renpy.end_replay()
    $ kaori_lust -= 99
    $ halloweenkaori2 = True

    jump halloweenfive7

label kaorispring1:
    scene nightsky
    with dissolve2
    play music "unmatchingeyes.mp3"

    "I decide to spend the night wandering around in hopes of maybe bumping into Yumi or something since that’s how things always used to work before the world went to shit."
    "Or I guess closer to shit than it already was since I have ultimately uncovered the fact that my life has always been pretty fucking terrible."
    "And that really makes me question why I stopped suppressing things in the first place when {i}not{/i} doing that really just makes me feel worse. "
    "I get that I’m probably supposed to use this as fuel to recover and “become a better person” or something but, let’s face it, that’s not going to happen. "
    "Because not only do I lack the strength to do so — I possess a critical weakness in being so easily infatuated by anyone who shows me affection that I have no choice but to fall for them."
    "And there comes a point in falling where it’s just fucking annoying. "
    "Just let me hit the ground already and save myself from this seemingly unending story that I can only imagine exhausts {i}you{/i} just as much as it does me."

    scene kaorilemons1
    with dissolve2

    "I guess that’ll have to wait, though — as I have now bumped not into Yumi, but the one Yumi-adjacent being that I have put my penis inside of. Weirdly enough."

    k "Thank you, human customer person! We apologize that you will need to go further away to find the yellow spheres of your sourest desires!"
    na "!..."
    s "Kaori? Nao? What are you doing here?"

    scene kaorilemons2
    with dissolve

    k "Ah! Sexfriend!"
    s "Please don’t call me that in public. "
    na "!..."
    k "Then, regular Friend! The Nao-chan and I have decided to open a lemon-assistance stand! "
    s "A lemon...assistance stand?"
    k "Correct! To aid humans in the retrieval of lemons!"
    s "Oh, I think I see what happened here. But that’s not even the right spelling of-"
    k "Three blocks west! Two blocks straight! Go, go, go! Let your sourest dreams run wild!"

    play sound "static.mp3"
    scene kaorilemons3 with flash
    stop sound

    s "Nothing good ever comes from letting my dreams run wild, so I’ll just hang out here for a little bit and and try to figure out why this is your latest business venture."
    k "There are no works to work on this night! Let alone works that would work the Nao-chan! So I am teaching her the ins and outs of produce distribution!"

    scene kaorilemons4
    with dissolve

    k "Unfortunately, there is an evil human organization known only as the “Produce Delivery Administration” that appears to have a Sorry! on the distribution of the lemonfruit."
    s "Wrong board game, Kaori."
    k "I am very Monopoly for the mistake, Friend. I am doing my best."
    s "Are you {i}really,{/i} though?"

    scene kaorilemons5
    with dissolve

    k "Reverse-no! That is precisely why we have obtained the other fruits that we are legally authorized to sell!"
    k "Unfortunately, however, most of the customers who have come here have only been interested in lemons. With the exception of a sole duck who inquired about the purchasing of grapes."
    k "Staying true to our name, though, we offer free guidance to the nearest lemonfruit vendor in exchange for only 100 yen!"
    s "That...is not “free” guidance, Kaori."
    k "All guidance is free in America, Friendburger."
    s "This is Japan."
    k "Land of the brave. Home of the sour."
    s "..."

    scene kaorilemons6
    with dissolve

    na "..."
    s "Kaori-"
    k "Name a fruit and we will help you find it! Or don’t! But please do! Aunt Yuki needs the money!"
    s "Yuki? You mean you’re-"

    scene kaorilemons7
    with dissolve

    k "Helping her become healed. She is currently in the process of dying, and it is my understanding that we can clear the black clouds above her with legal tendies."
    s "Legal tender. Just say money. "
    k "Legal boneless buffalo wings. I understand perfectly."

    if tsubasaspring4miss == True:
        stop music
        play sound "broken.mp3"
        scene kaorilemons7fuck1
        $ renpy.pause(5, hard=True)
        play sound "static.mp3"
        scene kaorilemons7fuck2 with flash
        stop sound
        play music "firstsecondmall.mp3"

        connor "Ugh! This shit is getting impossible to keep up with and I am GOSH DARN tired of it!!!"

        "This is Connor. He's in charge of maintaining continuity in the world and only shows up when there are certain mistakes that would take way too long to fix otherwise."
        "He will now explain to you why he is here and why you have to look at him."

        connor "Okay. So, for some reason, you've decided to play the game like a fucking LOSER and avoid boning certain cartoons because their cartoon age is lower than that of the other cartoons."
        connor "{size=-6}So BECAUSE you're down to clown with the high school cartoons and muddy up the plot of the game by avoiding the others and playing a route the creator despises due to the fundamental disconnect it sews between the actions of the protagonust
        and the game's overarching themes of abuse, you have encountered a {b}CONTINUITY ERROR.{/b}{/size}"
        connor "And chances are you'll encounter more in the future since writing branching narratives is hard as FUCK and Selebus straight up forgets you exist sometimes."
        connor "Anyway, if you were playing the game correctly and leading the protagonist down his rightfully wrongful path of debauchery, you'd have learned by now that {i}HE{/i} learned that Yuki is okay. Kind of."
        connor "In the proper route, Sensei goes to Tsukioka manor and finds all of this information out before a bunch of chairs show up and some girls take notes on penises and other penis-adjacent content."
        connor "So go ahead and just pretend he knows that now and save the creator some time. Thanks!"

        "Connor begins to bash his Hammer of Correction against the screen and all is suddenly good and there are no more continuity issues. Go play the wizard route."

        play sound "static.mp3"
        scene kaorilemons8 with flash
        stop sound
        play music "unmatchingeyes.mp3"

    else:
        scene kaorilemons8
        with dissolve

    na "..."
    s "Kaori, this is a...very nice thing you’re doing. And I’m sure Yuki would greatly appreciate it. But I don’t think she needs the money anymore."

    scene kaorilemons9
    with dissolve

    k "SHE ALREADY DIED?! THAT WAS SO FAST!"
    na "?!?!?!?!"
    s "No, no. She did not {i}die.{/i} She just found someone with a lot of money who’s willing to take care of her until she gets better. "
    k "This is information you should have immediately provided without giving me the opportunity to gasp!"
    na "!!!!!!!!!"
    s "I’m kind of surprised she didn’t tell you if you were already in the loop about this. I can fill in some of the details, but...maybe {i}without{/i} Nao present?"

    scene kaorilemons10
    with dissolve

    na "?..."
    k "Nao-chan says, “What the frick, man?”"
    s "She’s just too young to hear about death and stuff and I have a pre-existing disposition toward this because of things that have happened to the small human I raised."
    k "Then, would it not be better for her to learn about these concepts {i}before{/i} she is ultimately forced to experience them and subsequently thrown into traumatic shock?"
    s "Nope. That makes too much sense for a horrible parent like me."

    scene kaorilemons11
    with dissolve

    k "I understand. In that case, Nao-chan, please give us a moment and go hand out the sour information notes to those who pass our fruit-shelter."
    na "..."
    s "What’d she say that time?"
    k "Something about your input being somehow less valuable than the items that we are peddling."

    scene kaorilemons12
    with dissolve

    na "!!!!!!!"
    k "This time, she says “Baaaaaaaaaka.”"

    play sound "static.mp3"
    scene kaorilemons13 with flash
    stop sound

    "Nao hurries off and starts handing out what I can only imagine is some sort of flier to anyone who passes by, giving me an opportunity to figure out just how much Kaori knows and...{i}understands.{/i}"

    k "Does being alone mean that you are going to do the sex to me again?"

    "I don’t think she understands much."

    s "This is probably not the time for that. We’re kind of in the middle of something, remember?"
    k "I’m Monopoly again. I don’t have much sexperience, so I don’t know how this goes."
    s "Kaori, how much do you know about Yuki’s situation? Because it’s clearly enough to start trying to raise money for her, but...do you understand how serious this predicament is?"
    k "Very serious if it can make Aunt Yukiburger cry. I had assumed her tear production facility went out of service before I even became the Queen of Spiders."
    k "Who is this person she has found with seemingly deep pockets? Are they deep enough to fit a horse?"
    s "If you mean {i}buy{/i} a horse, yes. Tsubasa has several horses, I imagine."

    scene kaorilemons14
    with dissolve

    k "Tsubasa?!"
    s "Do you...{i}know{/i} her somehow too?"
    k "No! "
    s "Then...what is this reaction, exactly?"

    scene kaorilemons15
    with dissolve

    k "Monopoly three. I thought I was supposed to act surprised. I do not typically receive good news."
    s "Well, yeah. It’s {i}good{/i} news for sure. But this doesn’t mean she is out of the weeds yet, if you know what I mean."

    scene kaorilemons16
    with dissolve

    k "It means we must find a machete to free her from the foliage!"
    s "{i}No.{/i} It means she still has a lot of fighting left to do if she’s going to beat her illness. "

    scene kaorilemons17
    with dissolve

    k "But she {i}will{/i} beat it, yes? "
    s "I...haven’t really talked to her about it at length, but she definitely seemed less...fatalistic than when I talked to her last. Which I can only assume is good."
    k "Does the Yumi know yet?"
    s "That’s...a good question."
    k "The Yumi should know. Aunt Yuki was very worried about her. "
    k "So much so that she made me her honorary mothermom. But I feel as if I am doing a bad job as I have not been able to find her yet."
    s "Uh...give me a minute, Kaori. I’m going to call her and make sure she’s not being eaten alive by misery anymore."
    k "Okay, but you may need to do it very loudly as this is a large city and she may not be nearby."

    scene nightsky
    with dissolve
    play sound "phonebeep.wav"

    s "I think I’ll be fine, thanks."

    "I tap on Yumi’s name in my phone, half-excited to break the good news to her and half-{i}worried{/i} that she’s just going to blow me off upon hearing it as I still don’t really know how she’s processing-"

    y "{i}Hello?{/i}"

    "Monopo- sorry. Holding that thought."

    s "Hey. Are you alone right now?"
    y "{i}Hah...I kissed you on the cheek one time and now you’re calling me for phone sex? Fuck off, dude.{/i}"
    s "I’m calling you about your mom, actually. And before {i}you{/i} start freaking out thinking I’m delivering bad news, I’m-"
    y "{i}I’ve heard. That rich family’s taking care of her now. That why you’re calling?{/i}"
    s "Oh, good. You already knew. Kaori didn’t, so I wasn’t sure if-"
    y "{i}Fuckin’ Touka practically kidnapped me the other day to take me to her mansion. Yuki gave me the rundown there.{/i}"
    s "How does that make you feel?"
    y "{i}What, you my guidance counselor now?{/i}"
    s "I mean...kind of?"
    y "{i}Heh...yeah, guess you are.{/i}"
    y "{i}I, uhh...{/i}"
    y "{i}I feel good. Still kinda pissed that she didn’t tell me, but...I guess I might’a jumped the gun or something like that.{/i}"
    y "{i}You said Kaori doesn’t know? She actually cares?{/i}"
    s "She may or may not have opened a lemonade stand to try and raise money for her. And I may or may not be there right now."
    y "{i}She did what? Seriously?{/i}"
    s "Well, technically, it’s a lemon {i}assistance{/i} stand. But the goal is the same. "
    y "{i}The fuck’s a lemon assistance stand?{/i}"
    s "Why not come down to the urban district and see for yourself? She’s apparently been trying to get in touch with you."
    y "{i}Hah...I don’t know, Sensei. She ain’t...the same girl I knew growin’ up. Doesn’t even remember me.{/i}"
    s "Just come down here. I know you’re not busy."
    y "{i}Fucker, I’ve got a job now. I ain’t just free all the time anymore.{/i}"
    s "True, but I know Noriko’s schedule and {i}she’s{/i} at work right now. So chances are, you’re free."
    y "{i}The fuck you memorizin’ her schedule for? Stop that. It’s gross.{/i}"
    s "Sending you an address. See you soon, Yumi."
    y "{i}Wait! I don’t know if-{/i}"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "I hang up the phone and send Yumi my approximate location, figuring there’s a solid 90%% chance she’ll show up as she’s secretly a very family-oriented girl."
    "And a girl who, weirdly enough, I think will make a great mother one day if there’s ever anyone unfortunate enough to impregnate her and incur the wrath of the Yakuza."
    "..."
    "It’ll probably be me, won’t it?"

    play sound "static.mp3"
    scene kaorilemons18 with flash
    stop sound

    "Whatever. I don’t want to think about that right now. I just want these two to become friends again so the entire Yamaguchi tribe can tackle Yuki’s cancer together and go see the sea turtles hatch one day."
    "But the thought of that is too wholesome, so I forcibly wash it down with the idea of them returning to their hotel afterward and having the weirdest, hottest foursome ever with me. "
    "I’m so good at ruining emotional moments when I’m not meticulously crafting them, aren’t I?"

    y "..."
    k "..."
    k "You are a very pretty girl. "
    y "Um...thank you?"
    k "I did not expect you to be taller than me. I am the older one. I am supposed to be the tall girl."
    y "Yeah, that’s weird for me too. You were always like twice my size back when we were kids."

    scene kaorilemons19
    with dissolve

    k "So it is true that you knew me before I was me? And that this is not an elaborate prank at the hands of Yukiburger?"
    y "Yuki...burger?"
    s "It’s best to just not question any of the odd things she says if you can understand the general gist of her sentences."
    y "Got it...and yeah. I knew you before the...accident happened. Your parents would bring you over and just throw you in with me since there weren’t any other kids around."

    scene kaorilemons20
    with dissolve

    y "Can’t imagine you enjoyed it since you’re several years older, but...you were always nice to me and I, like...looked up to you and stuff."
    s "Aww...look at you two bonding."

    scene kaorilemons21
    with dissolve

    y "Go away, douche-fuck! This is supposed to be a private moment!"
    k "What is “douche-fuck?”"

    scene kaorilemons22
    with dissolve

    y "Just one of my many nicknames for him, but that’s beside the point. I, like...I came over here to say thanks and shit. I had no idea you were doin’ this for Yuki."
    k "Aunt Yuki is the only blood-based family I had until right now. And as your honorary mothermom, I can promise I will make a lemon-assistance stand if you start dying as well."
    y "I’m gonna try not to, if that’s cool. Dying ain’t really my thing."
    k "It was almost mine until I was brought back to life."

    scene kaorilemons23
    with dissolve

    y "Yeah, what the fuck happened with that? We all thought you {i}were{/i} dead. So you showin’ up again was, like...what the fuck?"
    k "I can not remember much apart from the abundance of juice and the seas of white. Those are my earliest memories. "

    scene kaorilemons24
    with dissolve

    k "But I am sad to learn that you have so many of me that I cannot share. I apologize if this makes you hate me, but I would like to like you again."
    y "I don’t...hate you, Kaori. It’s just...this is weird as shit. Like...goin’ from no family to...havin’ a mom again to...finding out she’s dying...and then she’s {i}not...{/i}and now I have a {i}cousin?{/i}"
    y "I just...ain’t really the type to let people in easily. And with you bein’ basically a brand new person, I’m like...I don’t know. Shit’s movin’ so fast all of a sudden."

    scene kaorilemons25
    with dissolve

    k "That small creature over there with the special eyes is Nao-chan! She is my daughterbug! I found her in an alleyway with Friendburger during a treasure hunt!"
    y "You...found her in a..."

    scene kaorilemons26
    with dissolve

    k "I have many jobs and many interests, but furry creatures and other sorts of animals are number one!"
    k "I keep a friendship journal where I write down important facts about the people I like the most! My favorite color is green! And I don’t eat canteloupe because it sounds too much like “antelope!”"
    y "What is happening right now?"
    k "I want to learn how to ride a skateboard and I accidentally became Internet famous by posting pictures of my underwear on the Instant gram! It was very embarrassing!"
    k "Your turn!"
    y "My turn to what? What are we doing?"
    k "If I tell you all of the things there are to know about me, we will no longer be strangers! We will be friends! "
    k "And I want to learn about you! All there {i}is{/i} to know! For we must start {i}somewhere{/i} in order for things to get better! Why not here?"

    scene kaorilemons27
    with dissolve

    y "Then, uhh...I like junk food and...throwing shit and...I fuckin’ hate crying so I want to stop playing this game."
    s "It’s so cute watching you grow feelings."

    scene kaorilemons28
    with dissolve

    y "Yeah, wish I could say the same about you, douche-fuck!"
    k "Douche-fuck! "

    scene black
    with dissolve2

    s "Yumi, please don’t corrupt her any more than I have. Kaori doesn’t need to learn words like-"
    na "!!!!!!"

    "A tug on my sleeve drags my attention elsewhere..."

    scene kaorilemons29
    with dissolve2

    s "Oh, Nao. Did you finish handing out your fliers?"
    na "!!!..."
    s "Well, I don’t see any issue in you re-joining the conversation now that the depressing part is over and your “family” is expanding. "

    scene kaorilemons30
    with dissolve

    na "!!!..."

    scene kaorilemons31
    with dissolve

    na "???..."
    s "What?"
    na "???... !.... ???????"
    s "Uhh, Kaori? Some help here? I still have trouble understanding Nao without her notebook."

    scene kaorilemons32
    with dissolve

    na ".............."
    k "Nao-chan says we should commemorate this reunion with a celebration of some type!"
    y "Yeah, uh...I ain’t really the {i}celebratin’{/i} type. Kinda like my privacy if you know what I mean."

    scene kaorilemons33
    with dissolve

    na "?....... ???"
    k "Then what if there was somewhere we could celebrate in private? With all of the trash food you could ever desire? "
    k "It will be my treat as I have earned extra money from lemon assistance that Aunt Yuki no longer requires!"
    y "Yeah, uhh...I’d feel bad makin’ you pay when I just scored $10,000 the other day."
    s "You actually got that money? I didn’t think that was ever going to happen."

    scene black
    with dissolve2

    y "Yeah, neither did I. Which is why I waltzed right into the trap of gettin’ lured to that damn manor to talk to my mom."
    k "Is your relationship with Yukiburger troubled, Yumiburger? She always speaks so lovingly of you!"
    y "Aaaah I don’t give a shit how she speaks! Just point me in the direction of the food! I’m tired of all this emotional bullshit!"
    na "!!!!!!!!!"
    k "Lead the way, Nao-chan! We will follow- wait. Friend, where are you going?"
    s "Huh? Is this not a family reunion? I kind of figured the three of you would want to spend some time alone."
    y "Yeah, see you later Sensei. Thanks for calling, I guess. ‘Til next time. "
    s "Man, I could have sworn things were finally changing with us."
    y "Yeah, maybe wait until somebody {i}actually{/i} dies, doucheburger."
    k "Doucheburger!"
    s "{i}Hah...{/i}"
    na "!... !!!!!!!"

    "Nao grabs hold of my sleeve once more and starts pulling me toward the other two on the way to...wherever it is we’re going."

    $ renpy.end_replay()
    $ kaorispring1 = True
    $ kaori_love += 1
    $ yumi_love += 1
    $ nao_love += 1

    jump naospring1

label kaorispring2:
    scene nightsky
    with dissolve2
    play music "ame.mp3"
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer. And no, I will not be allowing her to drag me to karaoke again if that is what she wants to do."
    "I more or less just want to see how she’s doing in the greater context of being a seemingly half-possessed human who I have now had a gratuitous amount of weird sex with."
    "Oh wow. I wonder if this is how everyone feels when they dial {i}my{/i} number? "

    play sound "phonebeep.wav"

    "I’ll have to ask Nodoka or something. She’s no stranger to railing all of the mental fallacies out of me."

    k "Goodbye!"
    s "Hey, Kaori. How are you?"
    k "My temperature is regular and all of my body parts are in the correct place! It’s an excellent day!"
    s "Are you working right now? Or are you at home?"
    k "I am currently teaching Nao-chan how to write exciting stories about large bugs who try to blend in with regular humans! "
    s "That is an oddly specific thing to teach someone about that I’m sure will prove to be invaluable at some point in her life."
    k "There is a problem though, Friend. I do not know how to write stories about things like this or I would have done it myself."
    s ".........Then why-"
    k "Help! You know how to make bad words into good words, yes? What is a better word for “bug?”"
    s "...Insect?"
    k "The story is now complete! Nao-chan will soon be the next King Stephen! "
    s "And what is he the king of exactly?"
    k "Nightmares."
    s "A surprisingly tame answer."
    k "Hello!"
    s "Wait — if you’re done teaching Nao, do you want to hang out? I could come over to your place or something?"
    k "Please do! I have been eagerly awaiting your next visit now that I know how it feels to mate, but I felt strange about asking you to come do that to me!"
    k "Even now, my face grows hot just thinking about it!"
    s "That’s not really why I’m-"
    k "The excitement grows! I will look at you soon! Hi!"

    play sound "phonebeep.wav"

    "Kaori hangs up before I have the chance to tell her I’m not {i}just{/i} using her as a booty call and that I genuinely do just want to check in on her."
    "But hey, if sex is on the table, I imagine that soon she will be too."

    scene black
    with dissolve2

    "I slide my phone back into my pocket and begin to make my way over to Kaori’s place. "
    "So this time, if I’m teleported into another realm with her adopted daughter, at least our main bodies will remain in a safe location for her to supervise and potentially defile."
    "Those things are essentially interchangeable for me, so I’d say that works out perfectly."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene kaoriaptwantspenis1
    with dissolve2

    k "Friend! Welcome back to my separatement! It has been many minutes, hasn’t it? Do you remember the rules?"
    s "The rules of...being in your apartment?"
    k "Correct! Do not feed the chicken or the Nao-chan or the Frog Boy or anything else. And please remember that the bath tub can only fit one person."
    s "Do people normally come over here to use your bath?"
    k "Not yet! But I assume it will happen eventually, so I want to make sure I’m prepared and not surprised by any spontaneous bath gatherings."
    s "Great. Well, thank you for reminding me of the house rules. And hello, Nao."

    scene kaoriaptwantspenis2
    with dissolve

    na "!..."
    k "Nao-chan! Now that your lessons are complete, you may do or play anything you like! Even if it’s that game where there is a sphere that you catch in a basket on a stick! "
    s "...Lacrosse?"

    scene kaoriaptwantspenis3
    with dissolve

    k "The cross, yes! And {i}we{/i} will play a different game! Using our human bodies as the sphere and the stick! Forever!"
    s "Forever?"

    scene kaoriaptwantspenis4
    with dissolve

    k "Yes. "
    s "I’m sorry, but I don’t think I’m physically capable of that yet. Thanks for giving me one more reason to keep practicing, though."
    na "?..."
    s "Yeah, you just stay out of this. Go play lacrosse."

    scene kaoriaptwantspenis5
    with dissolve

    na "??????"
    k "What happens now? Where do I go? What do I do? I do not remember how things started last time. I think my mind was erased from all the mating."
    s "Step one — get on the bed."

    play sound "static.mp3"
    scene kaoriaptwantspenis6 with flash
    stop sound

    k "I have arrived at the designated mating spot! You may begin!"
    s "Not yet. There’s a step two first."
    k "Would it not be “step two second?”"
    s "That...maybe. I don’t know. Either way, step two — you need to learn when the right and wrong time to do this is or you’ll wind up getting one of us in trouble."

    scene kaoriaptwantspenis7
    with dissolve

    k "Did a mistake occur? I thought sex-mating was acceptable in one’s home. This is why I did not ask to sex-mate in the singing room or at the lemon assistance stand despite how much I wanted to."
    s "You {i}kind of{/i} asked at the lemonade stand. You’re really thinking about this that much, though?"
    k "Should I not do that?"
    s "I mean...you {i}can.{/i} It’s just kind of weird to see you having urges like this all of a sudden when you’ve been pretty much sexually dormant for as long as I’ve known you."
    k "What is that? “Sexually dormant?”"
    s "Like...every time you’ve mentioned “mating” in the past, it’s seemed more {i}scientific{/i} than anything."

    scene kaoriaptwantspenis8
    with dissolve

    k "Not true! You have always flustered me and made my legs shake, Sexfriend! I just never understood how good things could feel until I became a cat! "
    s "Which is fine. But we’re still not {i}alone{/i} right now. Nao is literally right there."

    play sound "static.mp3"
    scene kaoriaptwantspenis9
    with flash
    stop sound

    k "Oh. Perhaps she does not like the cross?"
    k "Can we not mate while she is present? We have done it before. In fact, she has been present for 100%% of the times that we have done it. Even the kiss move."
    s "But she {i}shouldn’t{/i} be because sex is a private thing between two people. Except for when it’s not."
    k "Then I declare that it is not! Please begin!"
    s "Sure. As soon as she leaves the room."
    k "Nao-chan! Leave the room so your mothermom can engage in the sex with Friend! Your turn will come later!"

    play sound "static.mp3"
    scene kaoriaptwantspenis10 with flash
    stop sound

    s "{i}No.{/i} She doesn’t get a turn. Only you do. "
    k "That seems very rude to Nao-chan. It is only fair that she gets to experience the same joy that we do, correct?"
    s "Incorrect. She needs to wait a few years until she...{i}develops{/i} more. And this is something you need to accept as her caretaker or you will cause irreparable harm to both her body and mind."
    k "Oh, stop pretending to be such a {i}good guy.{/i}"

    play sound "static.mp3"
    scene kaoriaptwantspenis11 with flash
    stop sound

    k "We both know you’d pound that little girl six ways from Sunday. And you’re being handed the opportunity to do just that on a silver platter. "
    k "What do you gain from saying “no” other than one more chance to fool yourself into believing there’s some sort of conscience left in that little head of yours, Aki-kun?"
    s "Can you please just...get out of there and stop playing with her head? It’s unfair that {i}one{/i} voice leaves just for {i}you{/i} to start taking over more."

    scene kaoriaptwantspenis12
    with dissolve

    k "And always when her heart starts racing too. Cool, right?"
    s "Sekai-"
    k "{i}Kaori.{/i} My name is Kaori. And even when I’m not the me inside of me, the fundamentals of my beliefs are still the same, Aki-kun."
    k "{i}I{/i} don’t know it’s wrong for you to fuck little Nao-chan over there. So {i}I{/i} won’t have a problem with it. Now, go on! Get those feet wet. And by “feet” I obviously mean something else."
    k "Or just screw me like this in front of her. I don’t wanna change back, though. I forgot how good sex feels as someone without any experience."

    play sound "static.mp3"
    scene kaoriaptwantspenis13 with flash
    stop sound

    s "It was a mistake coming here at all, wasn’t it?"
    k "A {i}mistake?{/i} Or something you secretly {i}hoped{/i} would happen since you know I like to hang out in here now? "
    k "Let’s mate, Aki-kun! Then wash it all down with a little taste of that forbidden fruit over there. Sounds fun, right?"

    scene kaoriaptwantspenis14
    with dissolve

    s "Nao, stop drawing and just leave already. You can see what’s happening over here, can’t you?"

    play sound "static.mp3"
    scene kaoriaptwantspenis15 with flash
    stop sound

    k "Of {i}course{/i} she can, but she doesn’t {i}care!{/i} She’s not a real girl, so why {i}would{/i} she? "
    k "Just think of her like one of those super {i}impure{/i} fantasies that are always swimming around in your head, Aki-kun. It’s just like masturbation when you think of it like that, isn’t it?"
    k "In fact, didn’t you use that same sort of mindset to justify fucking {i}everyone{/i} when you first woke up here? Why the change of heart now? Do I need to possess {i}you{/i} next?"
    s "I don’t even want to think about that — but the change of heart was due to me {i}learning.{/i} And accepting people as more than just figments of my imagination."

    scene kaoriaptwantspenis16
    with dissolve

    k "Yet, you {i}don’t{/i} accept this girl as that."
    k "Which means that argument falls flat and is now propped up by little more than some weird sense of morality and righteous obligation that {i}I{/i} definitely didn’t teach you."
    k "Just let go! Have fun! How do you expect to ever fuck the rich girl and her poor friend if you can’t even put it inside of the mute orphan girl? She’s the easiest target possible."

    scene kaoriaptwantspenis17
    with dissolve

    k "Isn’t that right, Nao-chan?"

    play sound "slap.mp3"
    scene kaoriaptwantspenis18 with hpunch

    k "Ah."

    scene kaoriaptwantspenis19
    with dissolve

    na "..."
    k "She’s just feeling a little shy right now."
    s "Yeah. Sure she is, {i}Kaori.{/i}"

    scene kaoriaptwantspenis20
    with dissolve

    k "I mean it! Just because she hasn’t come around to {i}me{/i} yet doesn’t mean she won’t come around to {i}you!{/i} "
    k "I swear, though — if you come over here and start pulling this thing’s clothes off, she’ll be purring before you even know it. Won’t you, Nao-chan?"

    scene kaoriaptwantspenis21
    with dissolve

    na "..."
    k "...Helloooooo? Anyone home?"
    s "Just leave her alone...she doesn’t need to be pulled into the same pit that {i}we{/i} come from."

    play sound "static.mp3"
    scene kaoriaptwantspenis22 with flash
    stop sound

    k "Neither did {i}Kaori{/i} and she seems to be thriving there, doesn’t she? {i}We{/i} were happy too until I was roadkill. So maybe that “pit” isn’t as bad as you think, Aki-kun?"
    k "What’s the name of that one girl who can’t seem to move the fuck on again? Mei? Meiko? M...Mayonnaise? "
    k "You know. The one who looks like she crawled out of a gutter. Wears a bell? Kind of a slut? The gross one who shares a dorm with my perfect little girl."
    s "Can’t say I’m a fan of this new seduction tactic. Having the people I care about trash-talked isn’t one of my biggest turn ons."
    k "Yeah, but a little girl who won’t say no {i}is{/i} and {i}that’s{/i} not working either. So I don’t know {i}what{/i} I’m supposed to do anymore!"

    play sound "static.mp3"
    scene kaoriaptwantspenis23 with flash
    stop sound

    s "Would it kill you to just leave me alone?"
    k "I don’t know. Does it have four wheels and top out at 160kmph?"
    s "{i}Hah...{/i}"
    s "This {i}was{/i} a mistake. I really shouldn’t come here anymore."
    k "What? Why?"

    scene kaoriaptwantspenis24
    with dissolve

    s "Because you-"

    stop music
    play sound "static.mp3"
    scene kaoriaptwantspenis25 with flash
    stop sound

    k "Did another mistake happen?"
    s "Kaori-"
    k "The other me came out, yes?"
    k "Is she a bad girl? Because she is gone now. And it will be the me on the outside of me that you will do the sex things with. "
    s "..."
    k "{i}Please?...{/i} "
    k "I need you to touch me or more clouds will come. And there are so many of them now that I am having a hard time thinking straight, Friend."

    scene kaoriaptwantspenis26
    with dissolve2
    play music "asobeatsex8.mp3"

    k "I think...I am in heat again..."
    k "And the only way I can feel better is for you to touch me and clear my skies once more..."
    s "..."
    k "I understand that asking for your sexual participation outright is an undesirable trait in a prospective female companion, but I don’t know what else to do anymore...and..."
    k "And um..."

    scene kaoriaptwantspenis27
    with dissolve2

    k "It feels as if...there is a part of me missing...when you are not inside..."
    s "..."

    scene kaoriaptwantspenis28
    with dissolve

    k "Please...Friend? "
    k "Can you help me feel better?..."

    scene kaoriaptwantspenis29
    with fade

    "I glance over to find the one reason I {i}haven’t{/i} yet still sitting there at the table — nose buried in a notebook full of bugs and other things."
    "And I think to myself, caught in the tailwinds of my savior, that it {i}isn’t{/i} inherently harmful for her to just {i}be{/i} there."

    if tsukasacurious == True:
        "I’ve done as much with Tsukasa already. And even if I regret it, that didn’t harm {i}her.{/i}"
        "So maybe Nao {i}is{/i} a good way to...{i}test{/i} things. Assuming she wants to. "
        "Or maybe it’s her vulnerability that makes putting her in this spotlight somehow {i}worse,{/i} regardless of whether she’s “real” or not."

    else:
        "But will she really just “be” there, I wonder? Or will her curiosity get the best of her?"
        "This has happened once before and she remained on the outside of the world Kaori and I built around one another. "
        "I just worry that having her this close might pull her in, willing or not."

    s "Nao."
    na "?... ???"
    s "You know what’s about to happen...This is your chance to leave."
    na "!..."
    k "She doesn’t want to leave yet...She wants to write another story."
    s "So do I — but instead, I’m about to write the same one all over again."
    k "Friend...I can not take it much longer..."
    k "The me inside of me is screaming...{i}begging{/i} to be one with you. And I feel so...{i}warm.{/i} And confused. And...like I...{i}need{/i} you..."
    k "I need you...I {i}need{/i} you...I need you!"
    s "You know..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ kaorispring2 = True
    $ kaori_love += 1
    $ kaori_lust += 1

    jump kaorispring3

label kaorispring3:
    if _in_replay:
        play music "asobeatsex8.mp3"

    scene kaorifingering1
    with dissolve2

    s "There are things you can do to take care of those urges on your own, Kaori."
    s "Do you know about that?"
    k "If you...mean what I think you mean, it is no use. No matter how many times I attempt to master the bait, it feels nothing like the way my body felt when you were moving around inside of it."
    s "You’re probably just not good at it yet. That sort of thing will save your life when I’m not around, you know. "

    scene kaorifingering2
    with dissolve

    k "You are saying I will die if I do not sexually arrive soon?! This can not be! I have more family now! Family that I have recently learned {i}isn’t{/i} going to die! Must I be the one to take their place?!"
    s "What? No. Calm down. I meant that more...figuratively. "
    s "I’m just saying that it’ll help sate you until {i}I{/i} can. Which I will, since I care about you and also find you an attractive human being who is prime material for both mating and breeding."

    scene kaorifingering3
    with dissolve

    k "You will breed me, then?!"
    s "You shouldn’t be allowed to look so cute and excited when saying lewd things like that."

    scene kaorifingering4
    with dissolve

    k "Would it be better to pretend that you are breeding me against my will?"
    s "For some people, yes. I don’t think that’ll be an issue today, though. "

    scene black
    with dissolve2

    "I slide closer to Kaori, disregarding the fact that there is a small girl scribbling things into her notebook just several feet away from us."
    "The target of my nightly lust looks at me with a mix of curiosity and uncertainty as I begin to pull her skirt off. She merely whimpers and allows me to do as I please."
    "It’s kind of like gaining the trust of a desperate stray — one who’s hungry and fighting back against its instincts, torn on which direction the idea of self-preservation would have it turn its head."
    "And it’s a {i}good{/i} feeling. One that already has me desperately wishing to be set free from the jeans that imprison the physical manifestation of my rapidly hardening masculinity. "
    "And if you’re wondering why my words here seem more self-indulgent than they would be otherwise, I urge you to remember who is watching me. "
    "And how even now, I can’t help but wish to impress her."

    scene kaorifingering5
    with dissolve2

    s "How does it feel when I touch you here, Kaori?"
    k "Strange...but nice. This is my pleasure center, yes?"
    s "Something like that. And when I start to play with it-"

    scene kaorifingering6
    with dissolve
    with hpunch

    k "Nghgh??!!!?!"
    s "It feels good, right?"
    k "Y...Yes! But you are...moving so slowly! P...Please...go faster! I do not want...to wait any longer...for this journey to be over!"
    s "Do you normally go faster when you try to “master the bait,” Kaori?"
    k "One does not...master anything by...not fully applying themselves!"
    s "Maybe that’s why you’re having trouble then? A spot like this is too sensitive to treat without care. You need to start slow if you ever want to make it to the finish line."
    k "Like...the rabbit...and the turtle! I...understand! Lesson complete! Move faster!"
    s "Just stay calm and stop telling me what to do, okay? I’m way better at this than you are."
    k "It is so impressive that...despite your massive, throbbing male genitalia...you are still...so adept at...so...aah...adept...so..."

    scene kaorifingering7
    with dissolve

    k "Nyaaah~"
    k "I forget...the words...my mouth was making..."

    scene kaorifingering8
    with fade

    s "Probably something about pleasuring your human female body. I can feel you getting wetter by the second."
    k "W...Wet...Yes..."
    k "Female bodies...self-lubricate when...aroused! So that males can more...easily...penetrate them! But you...do not penetrate me at all! Is this...the crafting of the witch?!"
    s "This is foreplay. It’s something people do to turn each other on before they {i}mate.{/i}"
    k "I...am on. I am very much...on! So how much longer will you-"

    scene kaorifingering9
    with dissolve

    k "Ah! Wh...What’s that? What are you doing now?! "
    s "Just using another finger now that I know you’re warming up. Feels a little different, right? "
    k "Y...Yes! My...desire to be impaled by your length grows deeper! Must I...first endure the ministration of every finger?!"
    s "Nope, just these two. But you seem ready to go now, so I guess we can proceed."

    scene kaorifingering10
    with dissolve

    k "You will...finally do sex to-"

    play sound "static.mp3"
    scene kaorifingering11 with flash
    stop sound

    k "MEEEE??!!?!?!!?!?! AAAH! F...FRIEND! WHAT IS...HAPPENING?!"
    s "{i}Now,{/i} I’m putting my fingers {i}inside{/i} of you. It’s called-"
    k "FINGER SEX! YES?!"
    s "...Fingering. So you don’t need to rely on just playing with your clit all the way to your climax. Get good enough at both of these things, and you’ll be making yourself cum in no time, Kaori."
    k "It...feels like...two small penises have entered me at once! And are...moving together as...a sex team!"
    s "Just say it feels good. That’s enough, really."

    scene kaorifingering12
    with dissolve

    k "Haah...haaaah...it feels good! It feels...very, very good! You are...a sex magician, Friend! You have made my girlish hole so wet! It desperately craves more of your touch!"
    s "Say “pussy” instead of “girlish hole.” That’s a more attractive word to most people and it’ll make me more aroused. Probably."

    scene kaorifingering13
    with dissolve

    k "Pussy?...Like a cat, nyaa?"
    s "Mhm. Just like you were a cat on the roof. Remember that?"
    k "Friend’s masculine growth felt so hard and hot inside of my {i}pussy.{/i}"
    s "“Cock” or “dick” instead of “masculine growth” next. Try that sentence again."
    k "Friend’s cockdick in my-"
    s "Just one of them. Don’t use both."
    k "Your cock...felt so good in my pussy..."
    s "Good girl. Now, since you’ve done so well with your lesson so far, I’ll help you cum as a reward."

    scene kaorifingering14
    with dissolve
    with hpunch

    k "HYAAH! AAAH! F...FAST?! SPEED! VERY GOOD! SO SUDDEN! AAAH! AAAAAAH! "
    s "You’re going to want to tense up on instinct...but just relax and lean into me, okay?"

    scene kaorifingering15
    with dissolve2

    k "NGHHHHHH! I...CAN’T! IT FEELS TOO GOOD WHEN YOU...FINGER MY PUSSY! NGH! MMNGHHGHHHGHH!!!!!!"

    "Kaori begins to violently fight back against my touch, kicking her legs and flailing her arms. But I hold her tightly in place so there’s no chance of escape."
    "She’s tight enough that I can feel her contracting, suffocating my fingers as they plunge into her in an attempt to unearth the most carnal pleasure imaginable."

    k "F...FRIEND!...I’M...AAAAAH...SOMETHING IS..."
    s "You’re going to cum...it’s okay. Just think of it like riding me again."
    k "I DID NOT KNOW...YOU COULD “CUM” FROM FINGER SEX! AM I BROKEN?! "
    s "Not yet, you’re not. But if you stay this cute, I might {i}have{/i} to break you."
    k "MNNNGHH! OKAY! BUT...P...PLEASE REPAIR ME AFTERWARD! I...STILL HAVE SO MUCH LEFT TO...LEARN AND...NYAAH...NYAAAAH!"
    s "Wait, so is that cat noise really just something that naturally comes out of you when-"

    scene kaorifingering16
    with dissolve

    k "NYAAAAAAAAHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! NYAAAAH! NYAAAAAH!!!!! NYAAAAAHHHHHHH!"

    with sexfade
    with sexfade
    scene kaorifingering17
    with cumflash
    with hpunch
    stop sound

    k "{i}Nyaaah?...{/i}"

    "My question is interrupted by her not-so-sudden climax, so I’m just going to assume that she {i}does{/i} naturally make those noises since I find that much cuter than her doing it on purpose."

    s "Feel better now?"
    k "Aaaaaaaaaaaaahhhhhhhhhhhhh..."
    s "I’m going to take that as a yes."
    k "Again, please."
    s "Nope. It’s your turn now."

    play sound "static.mp3"
    scene kaorifingering18 with flash
    stop sound

    k "To finger you?"
    s "Don’t even think about it."
    k "Then what is it my turn to do? I do not understand the ins and outs of sex-fucking. Unless you mean the ins and outs of sex-fucking. Those I understand."
    s "That’s why I’m teaching you. And now that you’ve gotten all of that pent-up sexual energy out of your system, it’s time for you to serve {i}me.{/i}"
    k "You mean like a maid, Friend? But that costume was so embarrassing and made me feel too pink on the inside."
    s "You don’t need to be dressed as a maid to {i}serve{/i} someone, Kaori. I wasn’t dressed as one and I just served {i}you,{/i} didn’t I?"
    k "I suppose. But I am also confused as to why thinking of Friend dressed as a maid is making me wet again."

    scene black
    with dissolve2

    "I completely ignore that last statement and release Kaori from my grasp, guiding her to the floor and instructing her to unzip my pants."
    "But when she does as she’s told and simply leaves things at that, I need to inform her that her job isn’t done and that she needs to {i}unsheathe{/i} me as well."
    "She fidgets for a moment before nervously reaching into my pants and fumbling to find my cock, with which she ultimately succeeds because my cock isn’t exactly hard to find. "

    scene kaorifingering19
    with dissolve2

    "Which brings us here — just a minute or two into a lesson on handjobs that I probably should have asked her to take her gloves off for."
    "I’ll admit, though — having her sit here on the floor with her bottoms off as I lean back and let her work on me is going to make me cum, friction burns or not."

    k "Now what?..."
    s "The male body is a little less complicated than the female one. All you really need to do is keep stroking it like that and I’ll cum pretty easily."
    s "But if you want to make it better, you can try your hand at dirty-talking while you do it?"

    scene kaorifingering20
    with dissolve

    k "Sweep the floor! Do the dishes!"
    s "...No. “Dirty talking” in this context is, like...speaking sexually. Trying to say things that you know will arouse me more."

    scene kaorifingering21
    with dissolve

    k "Like “pussy” and “cock?”"
    s "Yes, but not on their own. Just sort of wing it and say things that you think {i}you’d{/i} get more turned on hearing."

    scene kaorifingering22
    with dissolve

    k "I love you and I want to be with you forever!"
    s "Again...not exactly what I had in mind."

    scene kaorifingering23
    with dissolve

    k "Are you sure? Because it seems harder now."
    s "New idea — just tell me how badly you want me to fuck you or something."
    k "I love you and I want you to put sperm inside of me so human babies happen."
    s "Kaori-"

    scene kaorifingering24
    with dissolve

    k "It is harder again! "
    s "Ugh...who am I kidding? You could say literally anything at this point and it wouldn’t change how you’re making me feel right now."

    scene kaorifingering25
    with dissolve

    k "I am doing a good job?"
    s "A...very good job. I feel like it’d be hard {i}not{/i} to, though. Just having you touch me at all makes me want to cum at this point."
    k "Then, if I am doing a good job, will you call me a good girl again?"
    s "You liked that?"
    k "Yes! It made me feel very warm inside! Like my brain was being hugged by a bigger, warmer brain! "
    s "Well...I guess it can’t be helped, then. You’re a good girl, Kaori."

    scene kaorifingering26
    with dissolve

    k "Thank you, Friend...that makes me very happy to hear."
    k "Will you like it if I call you a good {i}boy?{/i}"
    s "Uh...actually, that isn’t-"
    k "Harder again...your body betrays your words, Friend. You are a good boy."
    s "Kaori-"
    k "Good boy...{i}good{/i} boy..."

    play sound "static.mp3"
    scene kaorifingering27 with flash
    stop sound

    se "{i}Good boy,{/i} Aki-kun. You gonna cum for Mommy?"
    s "Mngh...mnh!"
    se "Go on! It’s okay if you get me dirty. Mommy doesn’t care."
    s "You’re not...my mom, though! Why do you...keep calling yourself, that?!"

    scene kaorifingering28
    with dissolve

    se "Why do {i}you{/i} only jerk off to videos of girls with big boobs? That’s very rude to smaller girls like me, Aki-kun."
    s "I...don’t! You just...came in at a...bad time! You’re supposed to knock!"
    se "But if I {i}knocked,{/i} you’d be all alone in here taking care of yourself. Mommy couldn’t possibly leave her good little boy alone like that. So Mommy will milk him instead."
    s "S...Sekai..."
    se "{i}Nooooooo.{/i} Mommy. Can’t you just indulge me, Aki-kun? I doubt I’ll ever hear those words from anyone else."
    s "You...actually enjoy it?! "

    scene kaorifingering29
    with dissolve

    se "Well, {i}duh.{/i} What better time to lay it all out on the table than in the middle of a recreational sex act? Hearing you call me “Mommy” gets me hot. {i}Abstaining{/i} makes me sad."

    scene kaorifingering30
    with dissolve

    se "You don’t want to make Mommy sad. Do you, Aki-kun?"
    s "It’s just...embarrassing, okay?! It makes me feel weird!"

    scene kaorifingering31
    with dissolve

    se "You still get embarrassed around me? {i}Why?{/i} "
    s "Why...do you think?! "

    scene kaorifingering32
    with dissolve

    se "Ah..."
    s "You’re the...{i}only{/i} one I get like this for! And you {i}know{/i} why! But you still...have to torment me for it!"
    se "You’re learning from me! Even my precious Aki-kun is at his most honest during sex. I’m so proud of the man he’s becoming! Why, he’s not a little boy {i}at all{/i} anymore."

    scene kaorifingering33
    with dissolve

    se "Why — just {i}look{/i} at this big, {i}strong{/i} cock. This {i}clearly{/i} belongs to real man. In fact, I should be calling {i}you{/i} “Daddy,” shouldn’t I?"
    s "Mngh...stop...teasing me! I can...do this myself!"

    scene kaorifingering34
    with dissolve

    se "I’m sure you {i}can,{/i} big boy. But I’m doing it {i}for{/i} you because I love you. Which is, coincidentally, the same reason I tease you and poke fun at you. "
    se "And, you know what? I like that it works. And I {i}like{/i} that you want to look strong around me because it shows that you love me just as much. "
    se "You know how you can {i}really{/i} show me you love me, though? Come find {i}me{/i} instead of watching porn next time. You’re gonna make me jealous."
    s "Ngh...mngh!"
    se "Go on...cum for Mommy..."
    se "Be a good boy..."

    if tsukasacurious == True:
        play sound "static.mp3"
        scene kaorifingering35 with flash
        stop sound

        k "Friend is even more handsome than normal right now. I enjoy seeing this side of him."
        na "..."
        s "Yeah...I think Nao might too since she’s decided to start watching us."

        scene kaorifingering36
        with dissolve

        k "She does, Friend. This room is thick with pheromones because of you. And Nao-chan is a good girl as well. So would you like us to give you the armfootjob together?"
        na "..."
        s "I mean...{i}yes.{/i} But-"
        k "But you need to warm her up with finger-sex first? "

        scene kaorifingering37
        with dissolve

        s "..."
        na "..."
        k "?..."
        s "What is Nao even thinking? I can’t tell..."

        scene kaorifingering38
        with dissolve

        k "Neither can I. She is harder to read when she is flustered. But she is a smaller me, so I imagine she thinks the same things I do. That she is ready to mate."
        na "..."
        k "Come, Nao-chan! I am new at this as well! We can learn together! And Friend is a good boy, so he can also make you feel-"

        play sound "static.mp3"
        scene kaorifingering39 with flash
        stop sound

    else:
        play sound "static.mp3"
        scene kaorifingering39 with flash
        stop sound

    s "Ngh!"
    k "Ah! Friend liked being called a “good boy” so much that he is now about to burst!"

    if tsukasacurious == True:
        "Too close to obtaining what I want and incessantly pushed to always deprive myself of ecstasy in its purest form, I ignore Nao and focus on Kaori instead. "
        "And with the lingering memories of the her inside of her bleeding through her fingertips and curling around my cock, it isn’t hard to succumb to my desire to cum all over her face."

    else:
        "The lingering memories of the girl inside of Kaori bleed through her fingertips and curl around my cock, compelling me almost instantly to cum all over her face."

    "I resist at the last second, though- but it is not for her sake. In fact, if anything, I’d say it’s the opposite as there is a deep-seated urge within me right now to fully defile her."

    s "Kaori..."
    k "Wow...I think I can feel your heart beating through it..."
    k "Does it hurt, Friend? How can I make it feel better?"

    "Which is what I will do. And I will try my hardest to not envision someone else as I am painting her face with the cruelest brush imaginable."

    s "Look up at me...and open your mouth..."

    play sound "static.mp3"
    scene kaorifingering40 with flash
    stop sound

    k "Huh? Like this?"
    s "Tongue out...I want to make sure you taste it."

    scene kaorifingering41
    with dissolve

    k "Taste what? Did you bring a snack? "
    s "No...I’m going to cum on your face..."

    scene kaorifingering42
    with dissolve

    k "It is edible?! This is shocking information!"
    s "Tongue out...and keep stroking it just like that..."

    scene kaorifingering43
    with dissolve

    k "Ahhh~ "
    s "Good girl..."
    s "Keep going..."

    scene kaorifingering44
    with dissolve

    k "Ah...aaah....aaaaah..."
    s "Mngh..."
    k "Ahhhhhhh...{i}Aki-kun~{/i}"
    s "Ngh! "

    with sexfade
    with sexfade
    scene kaorifingering45 with cumflash

    k "Ah?"

    scene kaorifingering46
    with hpunch

    s "Haaah...aaah....aaaah! Mngh!"
    k "Ah....ah.....ah..."

    "I release myself all over her but, despite there being not a drop left in my cock, Kaori continues jerking me off as if I haven’t cum at all."

    k "Aaah....ah....ah....."
    s "{i}Hah...{/i}"
    s "It’s over now, Kaori. There’s a...recharge period for men. Nothing else is going to come out."
    k "Aaaah? Aaaaaaaaahhhh? Aaah?!"
    s "You might want to swallow before you try communicating again."

    scene black
    with dissolve2

    k "{i}Mlgp...paaah!{/i} Strange taste! This is nothing like cream but it looks like it should be! Why did you make me swallow it?! "
    s "It’s like a sign of affection. You doing that for me shows me how much you care."
    k "It has the same effect even when I am told to do it?"
    s "I mean...it’s {i}less{/i} than if you volunteered to. But still kind of, yeah. Some girls actually like the taste."
    k "Is this true? Nao-chan! Come over here and taste Friend! He states that some girls like- huh?"
    k "Where did she go?"

    $ renpy.end_replay()
    $ kaorispring3 = True
    $ kaori_lust += 1
    $ kaori_love += 1

    jump naospring2
