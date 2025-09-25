label callchinamimorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if chinami_love >= 0 and chinamidate1 == False:
        jump chinamidate1
    if chinami_love >= 10 and christmas7 == True and chinamidate10 == False:
        jump chinamidate10
    if chinami_love >= 15 and day355 == True and chinamidate15 == False:
        jump chinamidate15
    if chinami_love >= 25 and tsukasaspecial1p2 == True and chinamidate25 == False:
        jump chinamidate25
    if chap4active == True:
        jump chinamispringmorninggen
    if chapthreeactive == True:
        jump chinamisummer2morninggen
    if christmas7 == True:
        jump chinamimorninggen2
    else:
        jump chinamigenmorning

label callchinamiafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chinami_love >= 5 and chinamidate1 == True and day128 == True and chinamidate5 == False:
        jump chinamidate5
    if chinami_love >= 20 and chinamidate15 == True and chinamidate20 == False:
        jump chinamidate20
    if chap4active == True:
        jump chinamispringnoongen
    if chapthreeactive == True:
        jump chinamisummer2noongen
    if christmas7 == True:
        jump chinaminoongen2
    else:
        jump chinamigenafternoon

label callchinaminight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    else:
        "I'm not really sure how I'd explain calling Chinami at this hour if Chika is around, so it would probably be best to hold off for now..."
        jump callnight

label chinamimorninggen2:
    scene chinamimorninggen2
    with dissolve
    play music "happyandplotting.mp3"

    "I wind up talking to Chika in the morning and asking her if she needs any help watching Chinami today."
    "Instead of acting suspicious or confused, she thanks me graciously and commends me for always looking out for her."
    "When I get to the house, Chika has already left for work and Chinami is just waking up."
    "She spends the next five minutes standing still in the kitchen and rubbing her eyes before she even realizes that I'm there."
    "Once she does, though, she smiles and says good morning to me, even offering to make me a bowl of cereal because she {i}is a fucking angel{/i}."

    scene black
    with dissolve

    "But, in this house, angels must not work. So {i}I{/i} make {i}her{/i} a bowl of cereal as she sits at the kitchen table watching some television show on her phone."
    "After the two of us eat breakfast, I stick around a little while longer until she's no longer in sleepy-mode and decide it's about time to get on with the rest of my day."
    "Just as always, Chinami happily says goodbye to me and reminds me that she would like a little sister one day."
    "I do not respond to her because the idea of giving Chinami a sister sounds way too troublesome for pretty much everyone involved."
    "You're going to have to wait, Chinami."
    "Probably a very long time, too."
    "A {i}very{/i} long time."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami's affection has increased to [chinami_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinaminoongen2:
    scene chinaminoongen2
    with dissolve
    play music "happyandplotting.mp3"

    "I show up at the Chosokabe house sometime in the afternoon to find Chinami decked out in her winter gear."
    "I ask her if she plans on going anywhere and she reminds me that she isn't allowed to leave the house or she'll have her phone taken away."
    "As it turns out, she just wanted to wear her winter clothes so she could pretend she was going outside and building a snowman."
    "This tragic happening sparks a struggle within me about whether I want to risk her life for her happiness and..."
    "Well, I decide to not risk killing anyone today."
    "Besides, I'm pretty sure I'd be in a lot of trouble as well if Chika found out that I even considered bringing her outdoors in this weather."

    scene black
    with dissolve

    "Chinami comes up with the {i}brilliant{/i} idea to play pretend-snowman with me- which basically involves me standing straight up and..."
    "Well, pretending to be a snowman."
    "It's a horrible game."
    "She walks in circles around me for half an hour, patting me up and down as if I were actually made of snow-"
    "And I can't help but think about turning this into a horror movie and coming to life to chase her around the house."
    "But that, too, sounds like way too much trouble."
    "So I just let her keep going until she wants to take a nap and then leave the house in search of something else to do."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami's affection has increased to [chinami_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label chinamigenmorning:
    play sound "phonebeep.wav"

    "I tap on Chinami's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ch "Hello! Thank you for calling the Chinami hotline! How may she be of service?"

    scene black
    with dissolve

    "I talk with Chinami and Chika for a few minutes before they invite me over to hang out."
    "Chika needs a Chinami-sitter for the morning and, not having anything else to do, I decide to take up the job..."

    scene chinamimorninggen
    with dissolve
    play music "happyandplotting.mp3" fadein 3.0

    "Chika leaves shortly after I arrive and I spend the morning with Chinami, still in her pajamas."
    "I'm glad to know her sister trusts me enough to not think anything of it, but I will admit that it does feel a little odd seeing her like this."
    "Regardless, the two of us chat about a plethora of Chinami-things like what kinds of candy she likes and her strange affinity for slaughtering pigs."
    "Eventually, that affinity becomes a little too much for me and I decide to head out."

    scene black
    with dissolve

    "Chinami waves goodbye and tells me to be careful on the way home."
    "I lock the door behind me as I leave, being sure to warn her to not let any strange individuals inside the house."
    "She agrees and promises to stay safe, and I feel marginally more comfortable leaving a girl like her alone..."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami's affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinamigenafternoon:
    play sound "phonebeep.wav"

    "I tap on Chinami's name and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ch "Hello! Thank you for calling the Chinami hotline! How may she be of service?"

    scene black
    with dissolve

    "I talk with Chinami for a few minutes before finding out that she's alone."
    "Apparently, Yumi was supposed to stop by but never did."
    "Not wanting to leave her alone, I decide to head over myself..."

    scene chinamiafternoongen
    with dissolve
    play music "happyandplotting.mp3" fadein 3.0

    "When I show up at the apartment, Chinami is in the middle of watching some gameshow on television."
    "But despite hearing her cheers from the front door, she turns the TV off and decides to focus her attention on me instead."
    "Sure, it feels a little weird being alone with her in the middle of the afternoon while her sister is unaware, but I shrug it off when I realize that both of them trust me."
    "{i}Why{/i} they trust me, I can't really say. But as long as it keeps providing me opportunities like this, I'm not going to complain."

    scene black
    with dissolve

    "It gets dark rather quickly and I decide to be a good person and order Chinami a pizza before I leave."
    "She thanks me and hugs my legs, telling me that if I ever decide to marry her sister that she will support it wholeheartedly."
    "It is a strange way to say goodbye, but it's one that I have grown to accept."
    "Unfortunately for her, I don't plan on marrying anyone any time soon..."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami's affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chinamidate1:
    "Come to think of it, I haven’t really spoken to Chinami over the phone yet."
    "It would probably brighten her day to hear from someone, so maybe I’ll do that?"
    "Plus, it’s not like I have any qualms spending my free time chatting with a complete angel."
    "The only issue is whether or not she’s even awake yet. "
    "But, oh well. Won’t hurt to try I guess."

    play sound "phonebeep.wav"

    "I tap on Chinami’s name and wait to see if she answers."
    "........."
    "......"

    play sound "phonebeep.wav"

    c "Hello? Sensei?"
    s "Oh, uhh. Hey."
    c "Why are you calling Chinami so early in the morning?"
    c "In fact, why are you calling Chinami at all?..."
    s "Oh, you know. I just thought she’d be happy to actually get a call from someone..."
    s "I can’t imagine she’s gotten to use her phone for its intended purpose yet so...Yeah."
    c "It’s like 9:00 AM...It really couldn’t wait until later?"
    s "I’m a busy guy, Chika."
    c "Well...I guess that’s true."
    c "Chinami’s actually sleeping right now, but I’m really glad you called. I was actually just about to text you."
    s "Really? For what?"
    c "Well, Yumi was supposed to come over to watch her this morning since I have work, but she just told me that she’s not feeling well and doesn’t want to get Chinami sick."
    c "Soooo...I’m guessing you already know what I’m going to ask, right?"
    s "Right. You want me to dog-sit again."
    c "Hahahah~ Well she won’t be wearing her mask today, so it’s just normal Chinami-sitting."
    c "I know you said you’re busy, but I’ll be eternally grateful if you could at least hang out here for a few hours so she doesn't wake up alone."

    "Well...It’s not like I had anything else going on this morning."
    "Chika’s place is pretty far, but I guess I can probably make it there in around half an hour."

    s "Yeah...I’ll head over now. You owe me, though."
    c "Heheh~ Of course I do. I won’t forget this. Promise."

    play sound "phonebeep.wav"

    "Chika hangs up the phone and, after getting dressed, I begin to head over..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene chinamifirstdate1
    with dissolve
    play music "happyandplotting.mp3"

    c "Hey~ Thank you so so so so much. Really."
    s "Don’t mention it. I’m free until the afternoon anyway."
    c "That’s totally fine. Like I’ve said before, she’s fine alone. I just feel bad leaving her that way."
    s "Is she still asleep?"

    scene chinamifirstdate2
    with dissolve

    c "Nah, she’s just sitting in front of the TV right now. I made breakfast before you got here, so you like, literally don’t need to do anything."

    if bonus == True:
        c "You can even just hang out in the kitchen if you want. I can’t imagine it’d be fun hanging out with someone so much younger than you anyway."
        s "I think you might be forgetting how much younger than me {i}you{/i} are, Chika. "

        scene chinamifirstdate3
        with dissolve

        c "Heheh~ I don’t count. You told me I’m mature for my age so I’m counting that as being on the same level as you."
        s "Do whatever you want. Not like that part matters to me anyway."
    else:
        s "I love clowns."

    scene chinamifirstdate4
    with dissolve

    c "Yeah, I think you made that pretty clear recently. "
    c "But yeah, just hang out here and do whatever for a few hours. You can leave whenever you want."
    s "When will you be back exactly?"
    c "Not until later tonight, so don’t worry about staying the whole time."

    scene chinamifirstdate3
    with dissolve

    c "You should know my schedule by now, Sensei. I’m at the mall every weekend."
    s "Well hurry up and get going then. I’ll be fine here."
    c "Yeah, yeah. I’m going. "

    scene chinamifirstdate4
    with dissolve

    c "Thanks again, though. Really."
    c "You’ve been doing way too much for me lately. I have no idea how I’m going to repay you."
    s "Figure that out later. Just go to work for now."
    c "Roger that."

    scene black
    with dissolve

    c "Chinami! Don’t annoy Sensei while I’m gone!"
    ch "Chinami will do her best!"
    ch "Have a nice day at work!"

    "Chika exits the apartment, locking the door behind her and leaving me alone with her little sister."
    "........."
    "......"
    "..."

    scene chinamifirstdate5
    with dissolve

    ch "Hello! Welcome to Chinami’s house!"
    ch "Did you wash your hands?"
    s "Yeah, your sister made me wash them as soon as I came in."
    ch "Because she doesn’t want Chinami to get sick."
    s "I don’t want Chinami to get sick either."
    ch "That’s good. "
    s "It sure is."
    ch "..."
    s "..."
    ch "..."
    s "..."
    ch "Now what?"
    s "What do you mean now what?"
    ch "Are you just going to sit there and stare at Chinami until her sister comes home?"
    s "I...I haven’t really thought of that."

    "Now that she mentions it, I have absolutely no idea what I’m even supposed to be doing right now."

    if bonus == True:
        "I know Chika said it was fine to just hang out and do whatever, but it {i}does{/i} feel kind of weird being alone with a girl this small...even if she is a 5,000 year old wizard."
    else:
        s "I am so lost and scared."

    ch "You can stare at Chinami if you want. But she’s going to watch TV if that’s okay with you."
    s "Nothing’s even playing on the TV."
    ch "Big sis says that the TV won’t come back on until tomorrow, so Chinami is pretending that her favorite show is on instead."
    s "And what exactly is Chinami’s favorite show?"

    "Knowing her, I’m assuming it’s some early morning cartoon or-"

    scene chinamifirstdate6
    with dissolve

    ch "Game of Thrones."
    s "..."
    ch "..."
    s "I know I’m not the one who’s supposed to be raising you, but aren’t you a little too [young]for that?"
    ch "Chinami is a 5,000 year old-"
    s "Wizard. I know. Does your sister know you watch it, though?"

    scene chinamifirstdate7
    with dissolve

    ch "Mhm! We watch it together on her laptop whenever she brings it home."

    "I can’t say I know much about this show...but from what I understand, it can get pretty gruesome and..."
    "Well, let’s just say I was unaware that Chinami had been exposed to those kinds of things yet."

    s "So, you’re just sitting on a cushion pretending you’re watching Game of Thrones."

    scene chinamifirstdate6
    with dissolve

    ch "Right. Chinami took a quiz on her phone that says she’s part of House Lannister."
    s "I have no idea what that means. What does that house do?"
    ch "They have a lot of money and like each other more than they’re supposed to I think."
    s "Having a lot of money is pretty much the exact opposite of you. You don’t have {i}any{/i} money, Chinami."
    ch "This is the sad truth."

    scene chinamifirstdate7
    with dissolve

    ch "But that’s okay. Because one day, Chinami is going to be rich."
    ch "And then she's going to buy a big house for her and big sis."

    scene chinamifirstdate5
    with dissolve

    ch "And you’ll get one too since you bought Chinami her first phone."
    s "Well thank you. But I already have a house."
    ch "That’s okay. You can have two houses. A Lannister always pays her debts."
    s "I’m assuming that’s a quote from the show, so I’m just going to say thanks."
    ch "You’re welcome!"

    scene chinamifirstdate8
    with dissolve

    ch "Now, watch pretend-TV with me while we wait for big sis to finish working."
    s "That’s going to be hours from now. We’re really going to stare at a blank TV the entire time?"
    ch "It’s not blank! There are dragons and zombie things and a few really funny looking old people."
    s "You’re not supposed to make fun of old people, Chinami."
    ch "Shh! This is the best part!"

    "Chinami ‘shushes’ me and I direct my attention (For reasons I don’t understand) to a blank TV screen."

    ch "..."
    s "..."
    ch "..."
    s "..."

    scene chinamifirstdate9
    with dissolve

    ch "This isn’t as fun as Chinami expected."
    s "I can’t say I was really expecting any more from this. "
    ch "Now what do we do?"
    s "I don’t know. It’s your house. You figure something out."

    scene chinamifirstdate10
    with dissolve

    ch "Wanna watch Chinami kill pigs? She’s really good at it."
    s "I’m a little worried about your enthusiasm for killing animals. You know there are other games you can play on your phone, right?"

    scene chinamifirstdate11
    with dissolve

    ch "Other games?"
    s "Yeah. Like, that one where you crush candy. Or that one with the farm."
    ch "Can Chinami destroy the animals on the farm?"
    s "That’s...not really the point of the game, but probably? I don’t really know."
    ch "You don’t seem to know as much as big sis when it comes to phones, Mr. Sensei."
    s "Just Sensei is fine, Chinami."
    ch "Okay, Just Sensei."
    s "..."
    ch "..."
    s "You did that on purpose, didn’t you?"
    ch "Chinami has no idea what you’re talking about. She’s just a little girl who is also an ancient wizard."
    s "I’m beginning to think you might be smarter than you let on, Chinami..."
    ch "Chinami is very confused right now."
    s "{i}Sure she is...{/i}"
    ch "..."
    s "..."
    ch "Are you and big sis getting married yet?"

    "This again? How does this keep coming up?"

    s "How many times do the two of us need to tell you that things aren’t like that between us?"
    ch "A few more, probably. Chinami’s memory isn’t very good."
    ch "But she thinks you should get married anyway."

    scene chinamifirstdate12
    with dissolve

    ch "If Sensei and big sis get married, Chinami will be alone less. "

    "..."

    s "Is that why you want us to get married? So I’ll come around more?"
    ch "Maybe. "
    s "You know I can just, come around more {i}without{/i} marrying her, right?"

    if bonus == True:
        ch "Chinami also wants a little sister."
        s "...Okay, that one is a little less doable. "
    else:
        ch "You dare defy me, mere mortal?"
        s "Excuse me?"

    scene chinamifirstdate11
    with dissolve

    if bonus == True:
        ch "Big sis said she’d have a baby if it’s with you, Sensei."
        s "I do not believe a word of that, Chinami. You’re deceiving me."
        ch "Chinami doesn’t know what that word means, but she’s telling the truth."
        s "Why would your sister even say that? Something’s not adding up here."
        ch "Chinami doesn’t even know where babies come from because you wouldn’t tell her. She has no reason to lie."
        s "Good. I have no intention of telling you something like that."
        ch "Okay. I’ll ask big sis."
        s "No. Definitely don’t do that either. She’ll think it was me who said something."
        ch "Then Chinami will ask big sis Yumi. She looks mature so she probably knows."
        s "..."
        s "Actually, yes. Do that. I’m sure Yumi will be willing to tell you all about it. She won’t get flustered even one bit."
    else:
        ch "I have lived for thousands of years and you will tell me what I demand you to tell me."
        s "Chinami, no."
        ch "Teach Chinami the secrets of life! What it means to be human!"
        ch "Only then will Chinami spare you destruction!"
        s "Okay, Chinami. I will do just that."

    scene chinamifirstdate13
    with dissolve

    ch "Hooray! Chinami will learn a new thing soon! And no thanks to her future daddy!"
    s "Marrying your sister wouldn’t even make me your daddy. I’d have to marry your mom."
    ch "..."
    s "..."

    scene chinamifirstdate14
    with dissolve

    ch "Hi, Mom. Can you do me a favor?"

    "Things suddenly become incredibly morbid and don’t mesh well with the background music. Such is life."

    ch "Can you marry Sensei? He is a nice man and he bought Chinami a phone."
    ch "Chinami wants to take care of a sister the way big sis takes care of Chinami."
    ch "Also Sensei has glasses and big sis says you always liked boys with glasses."
    s "Chinami..."
    ch "Shh...I’m talking to my mom. Watch pretend-TV, Sensei."
    s "...Fine."

    "I pretend to watch pretend-TV and fall into pretend-inception."
    "How did a trip to hang out with my student’s little sister turn into something so complicated?"

    scene chinamifirstdate15
    with dissolve

    ch "{i}Also, he has lots of money. He even paid for Yumi’s phone. I think he works for the government.{/i}"
    s "Chinami, what in the world are you whispering about over there? I think I just heard something about the government."
    ch "No words, Sensei. Chinami needs silence to reach her mom through the picture."
    s "...Whatever Chinami needs."

    scene black
    with dissolve

    "Chinami spends the next twenty minutes whispering to the picture of her mother while I sit next to her, pretending to not hear what she’s saying."

    if bonus == True:
        "It’s an incredibly uncomfortable morning, especially when you realize that she’s basically trying to get her mom to agree to have sex with me."
        "Now, let’s get one thing straight."
        "I am a man with very low morals."
        "But even I don’t think I’d stoop as low as having sex with the Chosokabes' mother."
        "If she were alive, that would be another story but-"
        "Wait a minute. What the fuck am I even saying right now?"

    "{i}The next few hours pass by without becoming any more comfortable.{/i}"
    "{i}But at least Chinami didn’t spend the day alone.{/i}"

    $ renpy.end_replay()
    $ chinami_love += 1
    $ chinamidate1 = True
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinamidate5:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "Chika should probably be at work already, so if I want to spend time with the mini-version of her, now would probably be best."

    if bonus == True:
        "To be fair, Chika probably wouldn’t mind either way, but the idea of asking a [teenage]girl for her permission to do what I want to do just sounds annoying."

    "........."
    "......"

    play sound "phonebeep.wav"

    ch "Chinami hotline! This is the CEO, Chinami speaking!"
    ch "How many giraffes would you like to order?"
    s "The Chinami hotline sure sells some strange things."
    s "Do you have a permit to be selling giraffes, Chinami?"
    ch "Are you buying anything or are you just calling to take up my time?"
    ch "I have a very important business to run! These giraffes are not going to sell themselves!"

    "I can see that Chika’s customer service genes must have also been passed down to her sister."

    s "Are you doing anything today, Chinami?"
    ch "Chinami never does anything. She just sits in a room and cries."
    ch "Chinami thinks you should come over and play with her!"
    s "Sure thing...I’ll head over now."
    ch "Hooray! And I will put you down for three giraffes in the meantime."
    s "I don’t want any giraffes, though."
    ch "Sorry! No refunds!"
    ch "Bye-bye!"

    play sound "phonebeep.wav"

    "Chinami hangs up the phone and I find myself already on the way to her house."
    "Hopefully the cost of three giraffes is somewhere in the realm of one pizza so I can just order her dinner in order to settle my debt."
    "........."
    "......"
    "..."

    scene chinamistorytime1
    with dissolve
    play music "happyandplotting.mp3"

    if bonus == True:
        "I sit at the table alongside a girl significantly younger than me as she looks up in admiration or...naivety or...confusion."
    else:
        s "..."
        ch "..."

    "Chinami seems to only have two facial settings."
    "One that is entirely wholesome and-"

    scene chinamistorytime2
    with dissolve

    ch "Wanna watch Chinami slaughter pigs on her phone?"

    "And one that is pure evil."

    s "You’re still playing that game?"

    scene chinamistorytime1
    with dissolve

    ch "Chinami has all the time in the world to play games since she can’t go outside."
    ch "The pig game is also the only thing she’s better than her sister at, so Chinami needs to keep polishing her skills or she'll be left behind."
    s "That’s fair but Chika doesn’t seem like that big of a gamer to begin with."
    ch "All big sis does is watch cute girls dance on her phone. Chinami’s phone-time is much better and more fulfilling."
    ch "She has also mastered geometry. "
    s "I’m very proud of you, Chinami."
    ch "So, if you don’t want to play games with Chinami, what would you like to do?"
    ch "Dance? Sing?"
    s "I can’t say I’m much of a...well, either of those things."
    ch "Maybe you can teach Chinami things since you are a teacher?"
    ch "She wants to know what kinds of lessons the big girls learn so she can be prepared when she’s allowed to go to[school]."

    "{i}If{/i} she’s ever allowed to go to[school]."
    "I don’t know much about Chinami’s situation, but the way Chika put it mixed with the fact that she can’t even go out in public without gloves and a mask is...rather telling."
    "But who knows? Maybe she’ll be able to do things the rest of us can do someday?"
    "One can only wait and see."

    s "Today is my day off. And you can’t afford to buy lessons from me either way."
    ch "What if Chinami gives you a discount on your four giraffes?"
    s "Wasn’t it only three?"
    s "Wait, I didn’t even want any in the first place."
    ch "I added another one as a penalty for you being late. "
    ch "That’s what the adults call “interest.”"
    s "That is a very strange take on the concept of interest but you’re not entirely wrong."
    ch "Can you at least read Chinami a story?"
    ch "Big sis Yumi keeps a stack of manga in her side of the closet and Chinami likes to read them when no one else is home."

    scene chinamistorytime2
    with dissolve

    ch "She likes the ones with lots of blood the most."
    s "Of course she does. "
    s "Fine. Go get something out of the closet, Chinami."

    scene chinamistorytime3
    with dissolve

    ch "Yay! Friendship!"
    ch "Chinami will be right back!"

    scene chinamistorytime4
    with dissolve

    s "..."

    "Chinami scurries over to the other side of the room and quickly opens the closet door, stopping it with her foot just before it bumps against the wall."
    "I imagine it’s something she’s been scolded about in the past judging by the chipped paint and dents near where the door handle would typically land."
    "Also, is now a good time to say that I think Chinami and Kaori would get along strangely well?"
    "The two of them seem to only want companionship and...I don’t know if Kaori even has the mental capacity to comprehend any strangeness regarding hanging out with a girl Chinami’s age."
    "But, then again, it might be difficult convincing Chika to let someone who looks like Kaori inside in the first place."

    scene chinamistorytime5
    with dissolve

    ch "Chinami has returned with a book that has no blood in it. She doesn’t want you to get scared and run away."
    s "I’m a mature adult and would not run away from something as trivial as that."
    ch "Chinami doesn’t know what {i}trivial{/i} means but she believes you."
    ch "She also has a rule when it comes to story time."
    s "A rule? What kind of rule?"
    ch "Since Chinami has read this manga so many times already, she knows the story by heart."
    ch "So she wants you to make up your own story and tell it to her."
    s "Why do I suddenly need to be creative? All I was planning on doing was reading."
    ch "Because if you don’t, Chinami will tell her big sis that you did all kinds of mean stuff to her while she was at work."
    s "..."
    ch "..."
    s "Are you...blackmailing me?"
    ch "Chinami is Chinami-mailing you."
    ch "She just wants to have fun with her friend."

    scene chinamistorytime6
    with dissolve

    ch "And will eliminate you if you don’t listen to her."
    s "..."
    ch "..."
    s "..."
    ch "Take Chinami’s book."

    "I’m starting to think that “Game of Thrones” thing might have been a bad influence on this adorable little flower."
    "She’s gone from being a daisy to some sort of...venus fly trap or something."

    scene chinamistorytime7
    with dissolve

    "I take the book out of Chinami’s hands and open up to a random page since it doesn’t really matter what I read in the first place."
    "She moves closer to the table and slides her legs underneath it, bumping into one of my knees as she does so."
    "It’s a small table, so it’s not exactly an easy fit for both of our limbs, but we make do with the space we have and I..."
    "Well, I guess I allow myself to be blackmailed?"
    "Or, excuse me, Chinami-mailed."

    scene chinamistorytime8
    with dissolve

    s "So...uhh..."
    s "A long, long time ago in a galaxy far, far away."
    ch "Chinami has seen that movie before. Try something else."
    s "..."
    s "How about you just tell me what kind of story you want to hear."
    ch "Hmm..."
    ch "Chinami wants to hear a story about a little girl who grows up to be the CEO of Chinami-Corp! The biggest Japanese dealer of cute animals!"
    ch "It doesn’t have to be a story about Chinami as long as the company is named Chinami-Corp."
    s "But why would-"
    s "Actually, nevermind. Fine."
    s "A decently long time ago in a land pretty close to here-"
    s "There was a little girl named...Chiaki."
    ch "Chiaki was Chinami’s mom’s name!"

    scene chinamistorytime9
    with dissolve

    s "Oh. Uhh...Should I change it?"
    ch "No. Chinami thinks it’s a good name. Other girls are allowed to have it."
    ch "Please continue!"

    scene chinamistorytime8
    with dissolve

    s "Okay, so...Chiaki was a pretty normal girl for most of her life."
    s "In her free time she did things like...painting or...jump-rope...or ski-ball."
    ch "What’s ski-ball?"
    s "A game that no one plays anymore."
    ch "It sounds fun. "
    s "I haven’t even told you what it is."
    ch "Chinami guesses you wear skis and kick a ball around."
    s "Wrong. This is exactly why you need to listen instead of speaking out."
    ch "Chinami is sorry. She will behave."
    s "Good. So, anyway..."
    s "One day, Chiaki was on a field trip to a museum or something and she was suddenly bit by a radioactive spider."

    scene chinamistorytime10
    with dissolve

    ch "Wow! A plot twist this early!"
    ch "Chinami is shocked!"
    ch "What color was the spider?"
    s "..."
    s "Brown."

    scene chinamistorytime11
    with dissolve

    ch "That just sounds like a normal spider. "
    s "It was only slightly radioactive."

    scene chinamistorytime8
    with dissolve

    s "Anyway, Chiaki went home and continued to live her normal life for the next three weeks."
    s "She was almost positive the radioactive spider was going to have some sort of life-changing effect on her, but sooner or later she realized that all she gained was...extreme customer service skills."

    scene chinamistorytime11
    with dissolve

    ch "Chinami found a plothole."
    ch "How did Chiaki know the spider was radioactive if it just looked like a normal spider and didn’t give her powers?"
    s "Be quiet. This is my story."

    "I feel strangely irritated by my story being interrupted all of a sudden despite not caring at all just a few minutes prior."
    "How dare this tiny human find plot-holes in my work."

    ch "Chinami is sorry. Please don’t kidnap her."
    s "Please don’t insinuate that that’s a thing I would do if I were angry."
    ch "Big sis Yumi has warned Chinami that you’ve kidnapped girls in the past."
    s "..."
    s "I don’t think you should listen to Yumi anymore. I’ve never kidnapped anyone."
    s "But, back to the story..."

    scene chinamistorytime8
    with dissolve

    s "After Chiaki gained her radioactive customer service powers, the only thing she wanted to do with her life was sell things to people."
    s "The problem was that Chiaki also lived on a farm, so all she could sell were animals."
    ch "What about vegetables? They have vegetables on farms."
    s "The other problem was that this farm only had animals."
    ch "Chinami thinks a farm with only animals just sounds like a lonely zoo."
    s "Chinami should shut up and listen to the end of the story."
    ch "Chinami thinks you’re just jealous because she’s a better story-teller than you."
    s "..."
    ch "..."

    scene chinamistorytime12
    with dissolve

    s "..."
    ch "Chinami loves your story. Please continue."
    s "It doesn’t sound like it."
    ch "She’s just excited to be spending time with her future dad. That’s all."
    s "..."

    scene chinamistorytime13
    with dissolve

    s "Hah..."

    "How in the world am I supposed to stay mad when she goes and says things like that?"
    "Is this what having a kid is like?"
    "I thought I had a grip on that with Ami, but she jumped straight into her[teen]years rather than whatever’s going on here."
    "Granted, Ami didn’t really {i}jump{/i} into her[teen]years. She’s been there since I met her."
    "But still."
    "I should just try and wrap this story up so the two of us can move onto something more-"

    play sound "dooropen.mp3"
    scene chinamistorytime14
    with dissolve

    y "Chinami! I’m back! "
    s "Uh-oh."
    ch "Big sis Yumi is home!"
    ch "Story time will have to wait!"
    y "Heh? Story time? You never have story time by yourself. Is Chika back from work al-"

    scene chinamistorytime15
    with fade
    stop music

    y "..."
    s "..."
    ch "Welcome home!"
    y "..."
    s "...Welcome home!"

    play music "yumiska.mp3"
    scene chinamistorytime16
    with hpunch

    y "D-DON’T GIVE ME THAT {i}WELCOME HOME{/i} BULLSHIT!"
    y "WHAT THE FUCK DO YOU THINK YOU’RE DOING IN HERE?!"
    y "I SWEAR TO GOD IF YOU SO MUCH AS LAY A FINGER ON HER I WILL MURDER YOU!"
    ch "Uh-oh! Big sis Yumi only uses bad words when she’s {i}really{/i} angry."
    ch "Don’t worry, big sis Yumi! Sensei said he won’t kidnap me!"

    scene chinamistorytime17
    with dissolve

    y "HOW DID THAT EVEN COME UP IN CONVERSATION?!"
    s "A better question is why you told her I’d kidnap her in the first-"

    scene chinamistorytime16
    with dissolve

    y "NO ONE ASKED YOU! GET THE FUCK OUT OF HERE!"
    y "DOES...DOES CHIKA EVEN KNOW YOU’RE HERE?!"
    s "Well...not exact-"
    ch "Yup! Chinami told her!"
    s "..."

    "Well."
    "That’s...awkward."

    scene chinamistorytime18
    with dissolve

    y "And she was okay with it?..."
    y "Ew..."
    y "Ew ew ew ew ew ew ew ew ew..."

    scene chinamistorytime16
    with dissolve

    y "AHHH THAT’S SO FUCKING GROSS!"

    scene chinamistorytime19
    with dissolve

    y "And wait a fucking minute! What are you holding?! What are you reading to her?!"
    s "Oh, Chinami told me about your manga collection so-"

    scene chinamistorytime20
    with dissolve

    y "GET! THE FUCK! OUT OF HERE!"
    y "AND NEVER COME BACK!"
    s "And that’s my cue to leave."

    scene black
    with dissolve

    ch "But we didn’t finish story time yet!"
    ch "Chinami needs to know what happens to Chinami-Corp!"
    s "I’ll tell you some other-"
    y "YOU ABSOLUTELY WILL NOT!"
    y "OUT! NOW!"
    s "Or not."
    s "Later, Chinami. Later, Yumi."
    y "DIE IN A FIRE!"

    play sound "dooropen.mp3"

    "..."
    "Well, that could have gone better."
    "I wish Chinami would have said something about Yumi being able to show up at any minute, but-"
    "To be fair, I probably should have expected something like that sooner or later."
    "That’s Yumi’s home, too, after all."
    "I guess I’ll just...need to be more careful in the future."
    "Or at least find a good hiding place."

    $ renpy.end_replay()
    $ chinamidate5 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chinamidate10:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "It’s still a little early, so I imagine Chika is getting ready to leave for work right about now."
    "I don’t think I’ll ever come to terms with how strange the idea of me calling her little sister is, but it’s definitely getting less...weird over time."
    "Kind of."
    "I don’t know. Chinami is strangely fun to be around at times."
    "Even if that strange sense of fun comes from the fact that she may or may not be some sort of super-genius disguising herself as a little girl."
    "I’m calling your bluff, Chinami. You’re up to something."

    play sound "phonebeep.wav"

    ch "Good morning, future dad!"
    s "Good morning, Chinami. I am not your future dad."

    if bonus == True:
        ch "But big sis says she’s pregnant with your baby."
        s "That is literally impossible."
        ch "No! You two kissed and that’s how babies happen!"
        s "First, don’t ever say anything like that around Yumi."
        s "Second, you know damn well that isn’t how babies are made, Chinami."
        ch "No one will tell Chinami where they really come from so she has to keep guessing until she gets it right."
        s "Or Chinami can just drop it."
        ch "And never get a little sister? No way, future dad!"
        ch "Hold my sister’s hand and get her pregnant!"
        s "Wrong again."
        ch "Rats!"
        s "Is Chika home right now?"
        ch "Big sis left a few minutes ago. She looked extra pretty today."
        ch "The perfect kind of look for getting knock-"
        s "I’m going to hang up now."
        ch "Wait! Chinami wants you to come visit!"
        ch "She is very bored and promises to not talk about babies!"
        s "..."
        s "Fine. I’m on my way."
        s "I’m leaving the second you start saying things like that again, though."
        s "There are two girls you’re very familiar with who would kill me if I was anywhere near a discussion of that nature."
        ch "Blah blah blah."
        ch "Chinami doesn’t understand what the big deal is, but she’s got a meeting coming up, so you better hurry before the doors are closed for good!"
        ch "Bye-bye, future dad!"
    else:
        ch "Yes you are! Chinami comes from the future, so she knows!"
        s "I'm sure you do, Chinami."
        ch "Are you going to come over and play now?"
        s "..."
        ch "Chinami comes from the future, so she knows you are!"
        ch "Bye bye!"

    play sound "phonebeep.wav"

    "Chinami hangs up the phone and I’m suddenly left wondering why I even called her in the first place."
    "All of those things I said about how she’s fun to be around-"
    "They were all lies."
    "She’s out to destroy me. "
    "I know she is."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene chinamibalcony1
    with dissolve
    play music "happyandplotting.mp3"

    ch "Greetings, mortal! It is I, Chinami!"
    s "Good morning, Chinami. "
    ch "Lucky for you, Chinami’s meeting just ended."
    ch "She has all the time in the world now."
    s "Who was your meeting with, exactly?"
    ch "So, you know how Chinami-Corp is the leading distributor of giraffes and giraffe paraphernalia in all of Japan?"
    s "...Yes."
    s "Also, since when has your vocabulary expanded to include those words?"
    ch "Chinami has had five thousand years to practice vocabulary. It was only a matter of time."
    s "Right, right. Please proceed with your giraffe stuff. Sorry for interrupting."

    scene chinamibalcony2
    with dissolve

    ch "It’s okay. Chinami understands that not everyone can be as business savvy as her."
    ch "You see, future dad, Chinami-Corp has acquired another company this morning."
    ch "It was a big acquisition! One that will make Chinami so much money that she can start making microtransactions in her pig game!"
    s "I don’t follow gaming, but I’m pretty sure microtransactions aren’t at the point where you need to own a company to make them yet."
    ch "You’d be surprised."

    scene chinamibalcony3
    with dissolve

    ch "Wanna buy an elephant? It would make Chinami very happy and the recent merger has added them to the Chinami-Corp catalogue!"
    s "No. Chinami-Corp still hasn’t even given me the giraffes I accidentally ordered."

    scene chinamibalcony4
    with dissolve

    ch "Pweeeeeeeeeeeease?~"
    s "..."
    ch "..."

    "Your tricks won’t work on me, demon."

    s "I hope I didn’t come all this way just for you to try and sell me things again."
    s "It’s not exactly a short walk, you know."

    scene chinamibalcony5
    with dissolve

    ch "Chinami doesn’t know. The only time she’s allowed to go outside is when she’s with big sis Chika."
    ch "She used to be allowed outside with big sis Yumi, but not since the peanut incident."
    s "The what now?"
    ch "Chinami is very allergic to peanuts and big sis Yumi let her eat some since she’s reckless and mature."
    s "It’s not very mature to feed peanuts to someone who is allergic to them."
    ch "It’s Chinami’s fault, too. She knew she was allergic and didn’t tell big sis Yumi about it."
    s "Were you trying to get yourself killed?"
    ch "No! Chinami just likes nuts! "

    "There is a glaring issue with that statement but explaining {i}why{/i} would just cause me even more of a headache."
    "I should write down to never give her anything with nuts, though. That seems like a big deal."
    "Is this what being a parent feels like?"

    s "No. Parents don’t take notes on their kids."
    ch "Future dad? Are you talking to yourself?"
    ch "Do you need to take notes on Chinami even though you’re not married to big sis Chika yet?"
    ch "Do you need the Chinami-Corp quarterly spending report?"
    s "Where in the world are you learning all of these business terms?"
    ch "Chinami has gotten really into the stock market lately and it’s opened a big can of worms!"
    ch "But big sis Chika wouldn’t let Chinami invest in GME and now they’re still poor instead of swimming in a giant pool of Jell-O. "
    s "You have a strange perception of what it is like to be rich."
    ch "Are you telling Chinami that you {i}wouldn’t{/i} swim in a giant pool of Jell-O?"
    s "I am. That doesn’t sound fun, it just sounds difficult."
    ch "Future dad, can Chinami ask you a question?"
    s "As long as it isn’t about something that’s going to get me in trouble."
    ch "What is Jell-O?"
    s "Why do you want to swim in a pool of something if you don’t even know what it is?"
    ch "I heard it on TV."
    s "It’s a...weird water based dessert thing that’s kind of...bouncy. It’s actually pretty gross."
    ch "Can we make Jell-O one day or is it only for rich people?"
    s "It’s actually really cheap so...sure."

    scene chinamibalcony6
    with dissolve

    ch "Hooray! Chinami is gonna eat a bouncy dessert with her new dad!"
    s "It will have to wait for another day, though. I obviously didn’t bring any with me this time."

    scene chinamibalcony7
    with dissolve

    ch "It’s okay~ Chinami had other plans for today."
    ch "And she asked big sis Chika already, who said it’s okay as long as Chinami puts her scarf on first."
    s "Your scarf? Why?"
    s "I’m not allowed to take you outside, am I? Not even Yumi is allowed to do that."
    ch "Because big sis Yumi tried to assassinate Chinami."
    ch "You’re not an assassin, are you?"
    ch "Please don't kill Chinami! She loves you!"
    s "Not...that I’m aware of."
    ch "Then everything is okay!"

    "I’m not sure how I feel about this."
    "I felt weird enough even walking around the mall with Chinami."
    "Taking her outside, especially in this part of town, seems like an accident waiting to happen."
    "There’s no way I could let myself be responsible for something like that."

    s "I don’t think it’s a good idea for you to go outside, Chinami."

    scene chinamibalcony8
    with dissolve

    ch "But...but Chinami got permission."
    s "Even {i}if{/i} Chinami got permission, what if something bad happened to you?"
    ch "You would protect Chinami because you love her."
    s "I have never once said I love you, Chinami."

    scene chinamibalcony9
    with dissolve

    ch "Two dads in a row don’t love Chinami! Is she doomed to live a life of sadness?!"
    s "Okay, fine. I love you. Just...don’t bring up how your real dad didn’t ever again. "

    scene chinamibalcony10
    with dissolve

    ch "So this is what love feels like..."
    ch "Her real dad is missing out on something big!"
    s "Right..."

    scene chinamibalcony4
    with dissolve

    ch "Can Chinami really not go outside, though? She was very excited..."
    s "She can’t. "
    s "I don’t even know my way around this part of town. "
    s "And if Yumi ever saw me walking around with you, she’d-"

    scene chinamibalcony11
    with dissolve

    ch "Wait."
    ch "Chinami thinks she may have left out an important detail."
    ch "Chinami didn’t expect to walk around the town."
    ch "She just wanted to stand on the balcony for a little while and then get cold and go back inside."
    s "Oh."
    s "Why did you need to ask for permission to stand on the balcony?"
    ch "Because Chinami tried to climb the railing once when she was little and almost fell down and died."
    ch "Now Chinami asks every time just to be safe."
    s "Just to clarify, when you asked your sister for permission, did you say anything about me being here?"
    ch "Not today. Chinami thought you were just coming over for business reasons."
    s "Please assume from this point forward that I will {i}never{/i} be coming here for business reasons."
    ch "That’s okay. Chinami no longer has any use for you because of the merger."
    ch "She wishes you good luck with your future endeavors."
    s "..."

    "You know, I’m kind of thankful Chinami can’t go to a regular[school]."
    "I can’t imagine there are many other girls her age (5,000) that would know how to deal with her."

    s "Go put your scarf on, Chinami. We’ll go stand on your balcony for a little while if that’s really what you want to do."

    scene chinamibalcony12
    with dissolve

    ch "VICTORY FOR CHINAMI! THERE {i}IS{/i} A GOD!"

    scene black
    with dissolve2

    "Chinami sprints into the bedroom and pulls open a drawer, removing a long white scarf out of it and wrapping it around her neck."
    "She closes the drawer with so much force that the picture of her mother falls over."
    "Chinami gasps in shock as this happens and then apologizes to the picture as if it still has the potential to feel."
    "She sits it upright once again, among a circle of candles, before running toward the back door and sliding it open, stepping aside for me to meet her out there."

    scene chinamibalcony13
    with dissolve

    ch "Wow! "
    ch "Chinami has been stuck inside for so long that she forgot what the sun even looks like!"
    ch "It hurts so much more looking at it from outside instead of behind the window!"
    s "Please don’t stare directly at the sun, Chinami. You’ll go blind."
    ch "Blindness-shmindness! Gimme those UV rays! Chinami finally feels alive!"
    s "How long has it been since you’ve been out here? This is a hell of a reaction."

    scene chinamibalcony14
    with dissolve

    ch "Chinami last went outside three days ago."
    s "That is nowhere near long enough to warrant this type of reaction."
    ch "Everything seems longer when you’re stuck inside, future dad."
    ch "Even forty-five minute TV shows feel more like an hour!"
    ch "And since Chinami has to study at night, the day time is the only time she gets to be a free woman."

    scene chinamibalcony15
    with dissolve

    ch "But one day, Chinami is gonna have her very own house and she’ll be able to stand on the balcony without asking permission."
    ch "And she’ll also have a horse, and a dog, and a plasma screen television, and a pool full of Jell-O."
    ch "And she’ll come visit you...and big sis Chika...{i}and{/i} big sis Yumi every single weekend."
    s "Yumi is going to be there too?"

    scene chinamibalcony16
    with dissolve

    ch "Of course!"
    ch "You have to marry both of them so you can be Chinami’s full dad instead of her half dad."
    ch "And then you can marry Chinami too and we can all move into my house with the horse and the Jell-O pool."
    s "You do realize you don’t have to marry someone to live with them, right?"
    ch "But you’re a boy and we’re all girls. Obviously we’d have to get married to live together. Isn’t that the rule?"
    s "Again, no. That is not the rule."
    ch "So you love all of us but don’t want to marry us? Are you cheap, future dad? "
    ch "Is it because you spent all of your money on our phones?"
    ch "Is that why Chinami can’t make microtransactions?"
    s "It has a little more to do with there being...different types of love."
    ch "That sounds too adult for Chinami to understand. She’d rather talk about quarterly sales reports and GME’s impact on the modern economy."

    scene chinamibalcony17
    with dissolve

    ch "But she still hopes you’ll marry one of her sisters one day."
    ch "They both like you a lot. "
    ch "Big sis Yumi, too. Even though she likes to pretend she doesn’t."
    ch "And Chinami likes you just as much! She’s really happy every time you come over to visit."
    ch "You talk to her like a normal girl and not a baby. She appreciates that."
    ch "{i}I{/i} appreciate that."

    scene chinamibalcony18
    with dissolve

    ch "Thank you for spending time with me."
    ch "Come over and play more, kay?"

    scene black
    with dissolve2

    "I always feel a little strange when Chinami stops referring to herself in the third person."
    "But I need to remember that she’s a lot smarter than she lets on."
    "She really takes after her sister in that regard."
    "The one {i}actually{/i} related to her. Not the one who can’t even be bothered to come to[school] every day."
    "I guess the Chosokabes are just...naturally smart and wholesome."
    "It’s really unfortunate that they were dealt the hand they were."
    "But I guess that just gives me even more incentive to keep spending time with them."
    "Even if I have to keep coming all the way to the worst part of Kumon-mi to see them, their excitement every time I arrive makes it all worth it..."

    $ renpy.end_replay()
    $ chinami_love += 1
    $ chinamidate10 = True
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinamidate15:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    c "Hihi! Chinami’s phone. This is Chinami’s secretary speaking."
    s "Chika?"
    s "Does this mean you’re not working at the mall anymore?"
    c "Heheh~ Of course I am. This is just an unpaid internship."
    c "So what’s up? Calling to check on my little sister?"
    s "Sure, let’s go with that."
    c "Well, you’re in luck! Cause we’re actually having ourselves a little pool party right now and Chinami would be suuuuuuper excited if you showed up!"
    s "How are you having a pool party without a pool?"
    c "We actually {i}do{/i} have a pool. It’s just one of those cheap, blow-up ones that we keep stashed away in the closet for most of the year."
    s "And...what better time to break it out than the middle of winter?"
    c "Right!"
    s "Chika, that was sarcasm."

    if bonus == True:
        c "Your face is sarcasm. Come get wet with my sister and me."
        s "Chika, please don’t add Chinami into sentences like that."
        c "Come stop me, then! "
    else:
        c "Be here in twenty minutes or I am going to burn the house down!"
        s "What? No. Chinami is in there."

    c "Bye bye, Sensei!"
    s "Chika-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "..."
    "Well, it looks like I am apparently starting today off with a...spontaneous pool party?"
    "I slide my phone into my pocket and begin to make my way over to the bus stop."
    "I feel as if just showing up to an event like this is going to require a fair amount of energy, so I should probably be conserving all I possibly can..."
    "........."
    "......"
    "..."

    scene chinamipoolparty1
    with dissolve
    play music "happyandplotting.mp3"

    c "Hey! Great timing. I just dried myself off."

    if bonus == True:
        s "How is that great? What happened to getting wet with you and your sister?"

        scene chinamipoolparty2
        with dissolve

        c "What happened to not wanting to drag the wizard into any of our silly euphemisms?"
        s "Touché. "
        s "You really didn’t have to go and do something like that, though."
        s "Don’t let me being here stop you from having fun."
    else:
        s "I am glad to see that the house remains unburnt."
        s "Is this pool party catered?"
        c "By {i}catered{/i} do you mean {i}awesome?{/i}"
        s "No. I want food."

    scene chinamipoolparty3
    with dissolve

    c "Ehh...I was starting to get kind of hungry anyway."
    c "Besides, Yumi is still in the pool with Chinami, so it’s not like she’s totally alone."
    s "Yumi...is in a kiddie pool?"
    c "Yumi is in a kiddie pool."

    scene black
    with dissolve

    s "Excuse me, Chika. I need to see this with my own eyes."

    if bonus == True:
        c "Heheh~ Don’t stare too hard when you’ve already got me, okay?"

    scene chinamipoolparty4
    with dissolve

    "I walk into the living room slash bedroom to find that Yumi is, indeed, in a kiddie pool."
    "And apparently having a pretty good time, too."

    ch "Thank you for all of the business tips, big sis Yumi! It makes Chinami very happy to learn about management from an experienced professional!"
    y "Hey, I ain’t {i}that{/i} experienced, twerp. Just know who you’re tryin’ to sell to and things’ll take care of themselves."
    ch "In that case, may I interest you in Chinami-Corp's latest product? It’s just like a normal giraffe, but it has a jetpack and can shoot lasers out of its eyes."

    scene chinamipoolparty5
    with dissolve

    y "Heh. Will you take an IOU? I’m still kinda searchin’ for something a little more...predictable in the finance department."
    y "But I feel like I’ve been gettin’ pretty close lately and-"
    ch "Papa!"

    scene chinamipoolparty6
    with dissolve

    y "What? "
    y "What’d I tell you about payin’ attention to people when they’re talkin’ to you?"
    ch "Sorry, big sis Yumi! Chinami was just so excited to see her favorite man in the whole wide world!"

    scene chinamipoolparty7
    with dissolve

    y "The hell are you talkin’-"
    s "Hey. "
    s "Fancy meeting you here."

    scene chinamipoolparty8
    with dissolve

    y "Wha..."
    ch "Did big sis Chika tell you about the pool party, Papa? Or are you just here to pick up an order you placed on Chinamicorp.com?"
    y "This..."
    y "It’s...not what it looks like!"
    s "You’re not enjoying yourself and teaching Chinami about business inside of a kiddie pool in your best friend’s house?"

    scene chinamipoolparty9
    with dissolve

    y "I...I was makin’ sure the water wasn’t too hot for her! She’s got sensitive skin!"
    ch "Chinami’s skin isn’t very sensitive. Her mommy used to say it was strong and smooth just like {i}her{/i} mommy’s before she went to Heaven."
    y "Whatever! Now that I know it’s fine...my job here is done!"

    play sound "water1.mp3"
    scene chinamipoolparty10
    with dissolve

    ch "No! Come back! It’s not a family pool party unless we’re all here!"
    ch "Chinami finally found happiness!"
    c "Wait, Yumi. You’re not actually going out dressed like that, are you?"
    y "When the alternative is hangin’ around and being watched by that guy, heck yes I’m going out like this!"
    y "Just...tell me when he’s gone or something! I don’t know!"
    c "Yumi! Come on!"
    c "Sensei! Watch Chinami for a sec, please!"

    scene chinamipoolparty11
    with dissolve

    "I turn around to watch Chika quickly throw a hoodie on and chase Yumi out the door."
    "Then, within a matter of seconds, there are two pantless girls wandering around the old district of Kumon-mi."

    ch "Darn it. "
    s "It’s fine. We can have a pool party with just the two of us."
    ch "Yeah. But if either one of them catches a cold, they’ll have to quarantine themselves and Chinami will spend a few days alone."
    s "Oh."
    s "Well, worse comes to worst, you can come stay at my house for a few days."

    scene chinamipoolparty12
    with dissolve

    ch "Do you have a puppy?!"
    s "No. But I have a [niece] who kind of acts like one sometimes."
    ch "Is she fluffy?"
    s "Not really. No."

    scene chinamipoolparty13
    with dissolve

    ch "Chinami really wishes you had a puppy. That would give her the incentive she needs to come visit and avoid catching a cold from her dumbo sisters."
    s "Well that’s just too bad then because I don’t want a puppy. "

    scene chinamipoolparty14
    with dissolve

    ch "Hmph. I guess big sis Yumi was right after all and you really {i}don’t{/i} have a heart."
    s "Sure I do. It’s just not bogged down with the thoughts of love and puppies. It’s doing its job and delivering blood throughout the rest of my body."

    scene chinamipoolparty15
    with dissolve

    ch "Boooooring. Chinami wants to talk about dogs."
    s "This is the worst pool party I’ve ever been to."
    ch "Because Chinami is poor and can’t afford a real pool? "
    ch "Just wait until she’s a famous CEO princess with a hundred dogs that all hate you."

    scene black
    with dissolve
    play sound "water1.mp3"
    stop music fadeout 10.0

    "Despite wanting a hundred dogs to hate me or whatever ill will Chinami is suddenly wishing upon me, she scoots her way over to the edge of the pool and looks up at me."
    "I can already tell she’s switching modes once again- the same way I’ve seen her do a few times in the past."
    "I don’t want to say that she’s putting on an act or something- in fact, I’m almost positive she’s not."
    "But for someone like her, someone who’s able to understand and acknowledge exactly how she’s different from everyone else-"
    "There is always another mode."

    scene chinamipoolparty16
    with dissolve
    play music "starvingtodeathoutofreachofthesun.mp3"

    ch "Do you know why we’re having a pool party today?"
    s "No idea, actually."
    s "You should have all just gotten into the bath together if you were going to do something like this indoors."
    ch "Big sis Chika and big sis Yumi felt bad for Chinami because she can’t go to the beach with all of the other girls."
    ch "So they tried to bring the beach to her instead."
    ch "But Chinami wishes they could have brought their other friends here, too."
    ch "Chinami’s heard so much about them."
    s "Not from Yumi, I imagine. "
    s "She’s not exactly the most popular kid at[school]."
    ch "That’s because big sis Yumi is misunderstood."
    ch "But if Chinami were her age and got to go to[school] with everyone, she’d tell them that big sis Yumi isn’t scary at all."
    s "I’m sure your actual sister has tried that on multiple occasions. "
    s "Some people just aren’t really cut out for more than one or two interpersonal relationships, I guess."
    ch "Chinami doesn’t know what inner-personal means, but she’d like to try anyway."
    ch "Unfortunately, Chinami will probably never get to go to a real[school], so we’ll never find out."
    s "Giving up on your dreams of being a “normal girl” already?"

    scene chinamipoolparty17
    with dissolve

    ch "Chinami thinks that maybe some people just aren’t really cut out for being “normal girls” she guesses."
    ch "After Chinami’s new papa bought her a smartphone, she looked up all sorts of stuff about her condition."
    ch "She wasn’t very pleased with what she read."
    s "You should probably just be using your phone to murder pigs and leaving all of that sad stuff to medical professionals."
    s "The problem with the Internet and self diagnoses is that a person’s illness is never really as cut and dry as a list of symptoms on paper."
    s "In order to have whatever is wrong with you properly discovered, you need to gather the opinions of people who have spent their life training in the field and-"

    scene chinamipoolparty18
    with dissolve

    ch "Chinami is bored again. "
    ch "You’re not very good with girls, are you Papa?"
    s "Well...I don’t think I’m {i}bad{/i} with them."
    ch "Even though you have nothing you like to talk about and say all that boring stuff about doctors?"
    s "You know what? Why don’t we go back to talking about you?"
    ch "Is Papa afraid of doctor Chinami’s professional analysis? She has spent years training in the field."

    "I suppress the urge to hold Chinami’s head underwater and sigh to myself, knowing that she’s likely just trying to get a rise out of me at this point."
    "But even with the half-jokes about self diagnoses and her apparent side job as a medical professional, I really do feel for her."
    "I’ve never been good with empathy or sympathy or whatever {i}pathy{/i} the average person would exercise at a time like this-"
    "But I do wish things would have turned out a little bit different for her."
    "Not that things are “over” yet by any means."
    "But maybe some day this wizard will learn to use her powers to change herself and not just anyone she comes into contact with."
    "Perhaps she could even change me."

    s "Doubtful."
    ch "Doubtful?"
    s "Oh, sorry. Was just thinking out loud."
    ch "About what?"
    ch "Chinami wants to hear what you think about while you talk to her so she can be sure she didn’t make you feel bad."
    s "Chinami is in for a rude awakening then."
    s "You probably don’t realize this since you spend your entire life trapped inside of this house, but people very rarely say what they’re thinking in conversation."
    ch "Why?"
    s "Because we all have thoughts and parts of ourselves that we want to keep hidden."
    ch "Why?"
    s "Because people would realize how ugly we were if we actually expressed them."
    ch "Why?"
    s "Please don’t do this, Chinami."
    ch "Why?"

    if bonus == True:
        if ami_virgin == False:
            "I’ll be sure to cite things like this the next time Ayane or Ami tell me they want babies."
        else:
            "I’ll be sure to cite things like this the next time Ayane talks about having a baby."

    s "Are you just doing this to terrorize me?"

    scene chinamipoolparty19
    with dissolve

    ch "Yup."
    ch "Chinami realized she was annoying you, so she decided to distract you by annoying you in a different way."
    s "Chinami was not “annoying me.”"

    scene chinamipoolparty20
    with dissolve

    ch "Then how come your eyebrows looked like this?"
    s "I don’t know. Maybe I’m just not good at talking to you?"

    scene chinamipoolparty21
    with dissolve

    ch "That’s true. But we already figured that out when you wanted to talk about doctors and stuff."
    s "Well forgive me for wanting you to be a little more hopeful about your future."

    scene chinamipoolparty22
    with dissolve

    ch "Chinami..."
    ch "Chinami has no future."
    ch "Or at least not the kind of future her sisters and their future husband do."
    s "First off, you do have a future."
    s "Secondly, I can’t marry both of them. I’m pretty sure that sort of thing is illegal in Japan."

    scene chinamipoolparty23
    with dissolve

    ch "Does that mean you’ll marry {i}one{/i}?!"
    s "What? No."
    ch "Which one?!"
    ch "Big sis Chika would be a better wife but big sis Yumi’s body is more womanly."

    scene chinamipoolparty24
    with dissolve
    play sound "dooropen.mp3"

    ch "Ah! You’re not thinking of marrying Chinami, are you?!"
    c "Uhhhhh...excuse me?"

    scene chinamipoolparty25
    with dissolve

    ch "Yay! Big sis Chika is home!"
    s "Welcome back."
    s "I take it you weren’t able to track down Yumi?"
    c "Ugh, no. She’s annoyingly fast when she wants to be...and I didn’t want to run around barefoot."
    c "Would you mind explaining to me why you’re suddenly going to marry my little sister, though?"
    ch "Sorry for stealing your boyfriend, big sis! Chinami is just too darn cute."
    ch "She can't help it if things like this happen."
    s "Chika, it is not what it sounds like."
    s "I never agreed to any of this."
    s "She’s forcing it on me."
    c "She’s four feet tall. "
    s "But has the personality of a giant."
    ch "And the immune system of scrambled eggs!"
    c "Chinami! Stop that!"

    scene chinamipoolparty26
    with dissolve

    ch "Chinami is sorry. Please forgive her. "
    ch "And also make her lunch because she’s worked up an appetite from all of her swimming."

    scene black
    with dissolve2

    "Chika reluctantly agrees to her sister’s demands and winds up making lunch for all three of us."
    "We wind up eating together while the Chosokabes soak in their kiddie pool and I, being the anti-fun human being that I am, remain to the side of them."
    "Yumi never comes back and probably catches a cold or something. I don’t know."
    "Either way, it’s a little worrying to hear that Chinami now has access to a plethora of information that’ll likely exacerbate her already worrisome outlook on her condition."
    "But I think she’s counting herself out a little early, personally."
    "Is she weaker than everyone else? Sure."
    "I can’t recall {i}ever{/i} having to wear an animal mask in public while...that’s just a normal thing for her."
    "But she’s still alive."
    "She just needs to be a little careful."

    $ renpy.end_replay()
    $ chinamidate15 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinamidate20:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ch "Chinami hotline! Thank you for calling during happy hour!"
    s "It’s happy hour?"
    ch "Every hour is happy hour! Life is good! Buy giraffes!"
    s "But I still haven’t received the first ones I ordered."
    ch "Sorry. You need to call our customer support line if you want help with that. This is the giraffe center."

    "I sigh to myself and wonder for what feels like the millionth time why I’m calling one of my student’s little sisters."
    "I then hang up and dial the customer support number to follow up on the giraffe situation."
    "Just kidding."

    s "Where are you right now, Chinami? It sounds kind of loud."
    ch "Would you like a hint?"
    s "Sure. Why not?"
    ch "Arf! "
    s "Oh, you’re at the mall."
    s "Is Chika there?"
    ch "Of course big sis Chika is there. Did you think Chinami came here all by herself?"
    s "That’s...a good point. I’m not really sure why I asked that."
    ch "Well Chinami is glad you did! And she’s also glad you agreed to babysit her!"
    s "I-"
    ch "Bye bye, Papa! See you soon!"

    play sound "phonebeep.wav"

    s "..."

    "I slowly shove my phone back into my pocket and begin to head over to the bus station to hang out with a girl in a dog mask."
    "........."
    "......"
    "..."

    scene chinamimeetsalesbian1
    with dissolve
    play music "happyandplotting.mp3"

    s "..."
    ch "..."
    s "..."
    ch "..."
    ch "Arf!"
    s "I can’t imagine it’s very easy to drink that with a dog mask on."
    ch "Doggies can’t drink strawberry milk. They’ll get a tummy ache."
    s "Can you remind me why I spent money on buying you a drink you can not consume?"
    ch "Because you love Chinami."
    s "I do not love Chinami."
    ch "But you bought her strawberry milk and a cell phone."

    if bonus == True:
        s "Is that really how kids are judging love nowadays?"
    else:
        s "Is that really how wizards are judging love nowadays?"

    ch "Chinami doesn’t know. She’s not old enough to fall in love."

    "I quickly scan the mall to see how any onlookers might be viewing this...scene."
    "I immediately find that it’s not very good."

    s "Chinami, is there any way we could get you a less...conspicuous costume for when you come to the mall?"
    ch "Oh right. Chinami forgot you hate puppies."
    s "This is just kind of weird any way you look at it."

    if bonus == True:
        ch "Okay! Chinami understands that it would be normal for you to be seen with a little girl without a helmet on."
    else:
        ch "Okay! Chinami understands that it would be normal for you to be seen with a girl without a helmet on."

    ch "She’ll call her people and see what they can do."
    ch "But in the meantime-"
    ch "Arf!"

    "Again, I find myself leaning back in my chair and wondering how my life has gotten to this point."
    "I don’t have to wonder for very long, though, as I quickly remember that it was my idea to call her."
    "Could I have just left her at the clothing store with her sister? Absolutely."
    "Would it have been more socially acceptable for me to do that?"
    "Again, absolutely."

    if bonus == True:
        "Should I stop calling her altogether and begin hanging out with people that I couldn’t go to jail for just looking at?"
        "For a third time, absolutely."

    "But, no matter how many times I say “absolutely,” I have a hard time believing I’ll ever {i}really{/i} figure out how to stay away from this...demon slash CEO slash wizard slash dog."

    ch "Your eyebrows are being all...eyebrowy again."

    if bonus == True:
        s "I am a grown man sitting at a table with a little girl in a dog mask who is holding a box of strawberry milk for sheer aesthetic purposes."
    else:
        s "I want to die."

    ch "Arf!"
    s "I’m glad that you understand."
    o "What...the...fuck..."

    scene chinamimeetsalesbian2
    with dissolve

    if bonus == True:
        s "Oh, good. Now I’m a grown man sitting at a table with a little girl in a dog mask with aesthetic strawberry milk who has to explain to his students exactly what is happening."
        o "I mean...yeah?"
    else:
        s "I really do want to die."

    r "Um...Hi, puppy?"
    ch "Arf!"

    scene chinamimeetsalesbian3
    with dissolve

    o "Please tell me you’re not going to pretend she’s a real puppy."
    r "Otoha, I need you to think about this."
    r "If we just accept and agree that it {i}is{/i} a puppy, we can all move on and forget that this ever happened."
    s "I like Rin’s idea."
    ch "Arf!"

    scene chinamimeetsalesbian4
    with dissolve

    o "Did you kidnap her?"
    s "What? No. What would give you that idea?"
    o "The fact that you once made plans with Nodoka and Rin to kidnap me."
    s "Hey. Noriko was there too. "
    s "We all supported yuritopia and she needs to absorb some of the blame for me."

    scene chinamimeetsalesbian5
    with dissolve

    o "Yuri...topia?"
    r "Hahaha! Hahah...Noooo idea what Sensei’s talking about."
    ch "What’s a “yuritopia?”"

    scene chinamimeetsalesbian6
    with dissolve

    r "A magical world where all dreams come true."
    s "Not all dreams. Just yours."
    ch "Will Chinami’s dreams come true in yuritopia as well?"
    s "You still have several years left to figure that out, Chinami."
    ch "Chinami certainly hopes so!"

    scene chinamimeetsalesbian7
    with dissolve

    r "Chinami?..."
    r "That name sounds kind of familiar."
    s "Care to join us, Otoha?"

    if bonus == True:
        o "And be an accessory to whatever like, fifty felonies you’re committing right now? I'm good."
        s "I’m not doing anything wrong. I’m just babysitting."
    else:
        o "I'd rather eat a hedgehog."
        s "That is a strange alternative to this."

    ch "Arf!"
    o "Are teaching wages so bad that you need to pick up a second job just to keep yourself afloat?"
    s "They’re not great. That’s definitely true. But I’m doing this job for free."
    o "..."
    o "Yeah, I'm still good."
    r "Where in the world do I know that name from?"

    if bonus == True:
        s "Rin, pull up a seat with your girlfriend and hang out with us. Having two [teenage]girls with me {i}as well{/i} as Chinami might somehow make me look...less bad."
    else:
        s "Nowhere. Now tell your girlfriend to sit down."

    scene chinamimeetsalesbian8
    with dissolve

    r "G-Girlfriend?! "
    o "Come on, man. Why would you say that?"
    s "Because it will work. Watch."

    scene chinamimeetsalesbian9
    with dissolve

    r "Um...it doesn’t have to be for long...but...it probably {i}would{/i} help Sensei out a little..."
    o "You finally summoned up the courage to come here and {i}this{/i} is how you want to spend your time?"
    r "Like I said...it won’t be for long..."

    scene chinamimeetsalesbian10
    with dissolve

    o "How did you know that was going to work?"
    s "Honestly, it would have worked even if I left the girlfriend part out. I just like when Rin gets flustered."

    scene chinamimeetsalesbian11
    with dissolve

    o "You’re a real asshole sometimes, you know that?"
    s "No one knows that better than me, Otoha."

    scene black
    with dissolve2

    "Rin and Otoha grab chairs from a nearby table and join us at ours."
    "Of course, their attention isn’t even slightly focused on me."
    "Instead, it is focused on man’s best friend- a small girl in a dog costume. "

    scene chinamimeetsalesbian12
    with dissolve

    r "So...um...Chinami, right?"
    ch "Arf!"
    r "...What?"
    o "I think that means yes. I used to have a dog."
    r "Do you...come here often?"
    s "Rin, please don’t flirt with the puppy."

    scene chinamimeetsalesbian13
    with dissolve

    r "That’s not what I’m doing! I’ve just...never talked to a dog before! I don’t really know what to ask."
    ch "Chinami comes every once in a while!"
    ch "But she can’t come very much because she gets sick easily."
    o "Um..."
    o "Arf?"
    ch "Arf! Arf arf!"

    scene chinamimeetsalesbian14
    with dissolve

    o "Arf arf...arf arf?"
    ch "Arf! Arf arf!"
    r "Ohmygodohmygodohmygod."
    s "Otoha, would you mind explaining what you’re doing?"

    scene chinamimeetsalesbian15
    with dissolve

    o "I don’t know. Playing along I guess? "

    if bonus == True:
        o "Must be boring as hell having someone like you as a babysitter, so I’m just stepping in and trying to make things less lame."
    else:
        o "I'm just trying to like, make things less lame or whatever."

    s "You’re making things {i}less{/i} lame by barking at a girl in a dog costume?"

    scene chinamimeetsalesbian16
    with dissolve

    o "Hey! Don’t blame me for being good with kids. "
    r "Umm...I’m too embarrassed to bark at you like my not-girlfriend, Otoha, but...I’m happy to meet you Chinami."
    ch "Chinami is happy to meet you as well!"
    ch "Are you also friends with her big sisters?"

    stop music fadeout 10.0

    r "Big sisters? Do they go to our[school]?"
    s "Chinami, you probably shouldn’t be talking about that to-"
    ch "There’s big sis Chika and big sis Yumi! But only big sis Chika is related to Chinami by blood."

    scene chinamimeetsalesbian17
    with dissolve

    r "..."
    r "Oh..."
    r "{i}That’s{/i} where I’ve heard your name before."

    scene chinamimeetsalesbian18
    with dissolve

    o "..."
    ch "Did Chinami say something wrong?"
    r "No. You didn’t say anything wrong."

    scene chinamimeetsalesbian19
    with dissolve
    play music "gentle.mp3"

    r "It’s...uhh..."
    r "It's nice to meet you, Chinami. I’m Rin."
    r "I’m...going to take a wild guess and assume your sister’s never mentioned me before?"
    ch "Hmm..."
    ch "Chinami’s memory is very bad, so she isn’t sure."
    s "Rin, you know we can change the topic if this is weird for you, right?"
    o "Yeah..."
    o "That's...probably what we should do."
    r "I guess it doesn’t really matter if she mentioned me or not. We’re friends, though."
    r "Or...I think we’re friends? It’s a confusing...thing."
    r "But I’m really happy to finally meet you."
    ch "Chinami is confused."
    r "Why is Chinami confused?"
    ch "Because you’re saying you’re happy but your eyes are all teary."

    scene chinamimeetsalesbian20
    with dissolve

    r "Oh. "
    r "Huh. "
    r "I guess they are."
    r "And here I thought I was done crying over this."
    ch "So you’re {i}not{/i} happy? Chinami wants to confirm."
    ch "She isn't used to the complex emotions of [teenager]s."

    scene chinamimeetsalesbian21
    with dissolve

    r "Are {i}you{/i} happy, Chinami? Cause it would make me happy if you’re happy."
    ch "Chinami is super duper happy! She has two amazing sisters and an amazing new Papa who gets to babysit her at the mall."
    o "Oh, good. As if this couldn’t get any weirder."
    s "Strangely enough, I don’t really think this is as weird as the first time people saw me with her in full costume."

    scene chinamimeetsalesbian22
    with dissolve

    o "Weirder than {i}finally{/i} getting Rin to accept the end of her crush on that girl...{i}only{/i} to show up and bump into her little sister in a dog mask? Because that's pretty friggin' doubtful, man."
    ch "Crush?"
    ch "Chinami is sorry for asking, but aren’t you a girl?"
    r "Yes, Chinami. I’m a girl."
    ch "And you know Chinami’s sisters are girls too, right?"
    r "...Yup."
    ch "And you still liked her anyway?"
    ch "Are you allowed to do that?"
    r "Well..."
    r "I wasn't."
    r "But I guess it never really mattered since she didn’t like me the same way."
    ch "Chinami is very confused. She-"

    scene chinamimeetsalesbian23
    with hpunch

    ch "Wait!"
    ch "Chinami remembers something!"
    ch "But it’s very fuzzy. Like a puppy."
    r "What...is it?"
    ch "Big sis Chika did mention someone called Rin once!"

    scene chinamimeetsalesbian24
    with dissolve

    r "She did?..."
    r "Do you...remember what she said, by any chance?"
    ch "Umm..."
    ch "Chinami thinks..."
    ch "Chinami thinks she said you had very pretty eyes. And that she wanted hers to look more like yours."

    scene chinamimeetsalesbian25
    with dissolve

    r "..."
    r "That’s it?"
    ch "Chinami thinks so. She can’t remember any other Rins and big sis Yumi never talks about {i}anybody{/i}."

    scene chinamimeetsalesbian26
    with dissolve

    r "Heheh...hahahah!"
    r "Better than nothing, I guess!"
    o "Still not as weird as the first time?"
    s "I’m not sure. This has lasted a lot longer than that did."
    s "But I feel that this is probably weirder for {i}you{/i} than any of us since you're entirely unrelated to...pretty much all of it."
    ch "Chinami is so surprised! Until today, she didn’t know that girls could like other girls!"

    scene chinamimeetsalesbian27
    with dissolve

    o "I...uhh..."
    o "Yeah, I’m not gonna lie. I'm mad uncomfortable right now, so I think I’m gonna like...go walk around or something and...let you guys finish up on your own."
    r "I...can stop? "
    r "It just kinda happened out of nowhere and...I don’t want you to feel weird about me getting all emotional over it."

    scene chinamimeetsalesbian28
    with dissolve

    o "Don’t sweat it. When you’ve gotta cry, you’ve gotta cry. "
    o "But...again...this whole romance thing is just-"
    o "Well, to use Sensei’s words-"
    o "Entirely unrelated to me."
    o "Sooooooooyeah. I’m gonna go grab a milkshake or something and-"
    r "I’ll come with you. Don’t leave."
    o "Rin, you really don’t-"

    scene chinamimeetsalesbian29
    with dissolve

    r "Nope! I’m done here. "
    r "Not gonna waste a perfectly good opportunity to hang out with you getting upset over stuff that’s in the past."

    scene chinamimeetsalesbian30
    with dissolve

    r "Thanks for talking to me, Chinami."
    r "And please don’t say anything about this to either one of your sisters. I don’t really want to confront it again after it’s already over."
    ch "Chinami will do what you say!"
    ch "But she wants you to know that big sis Chika would never hurt you on purpose. She’s a very nice girl!"
    r "Yeah..."
    r "I know she is..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene chinamimeetsalesbian1
    with dissolve

    s "Just gonna go right back to jabbing your fake tongue against that straw, huh?"
    ch "Chinami feels like she wound up in a sticky situation just now! She’s parched!"
    s "All things considered, I think you handled it really well."
    ch "Chinami had no idea what to do when the girl with more red in her hair started barking at her! What is she, crazy?!"
    s "I can’t believe I’m about to say this...but don’t ever change, Chinami."
    ch "You want Chinami to stay little forever?"
    s "Okay. Maybe change a little bit. I wouldn’t want you stunting your growth for me."
    ch "Arf!"

    play sound "texttone.wav"

    "My phone suddenly goes off and I look down to see that Chika’s about to clock out for break and that my shift as “babysitter” is over."
    "I think I’ll wind up sticking around for a little while longer, though."
    "I’m in no rush to leave and-"
    "Honestly, having both Chosokabes around at once might be the exact medicine I need to counteract the overabundance of sadness and longing I just had to sit through."

    scene black
    with dissolve2

    ch "Chinami wants another strawberry milk! Go, Papa! Go!"
    s "..."

    "I text Chika, asking her to bring her sister a drink on the way over."

    $ renpy.end_replay()
    $ chinamidate20 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chinamidate25:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."

    play sound "phonebeep.wav"
    play music "happyandplotting.mp3"

    ch "Good morning!"

    "And given the fact that she is near constantly glued to her phone, she answers after only half a ring."

    s "Good morning, Chinami. You sound...livelier than normal for this time of day."
    ch "Chinami is excited because her business partner is coming over today! And Chinami heard that you were supposed to come as well!"
    s "Was that today?"
    ch "It was!"
    s "Wow, what a convenient coincidence. Is Chika still around?"
    ch "Big sis Chika is going on a top secret mission. Chinami is unfortunately unable to tell you any more than that since the details are classified."
    s "No Yumi either?"
    ch "Big sis Yumi hasn’t come over in a little while. Chinami is starting to get worried, but she knows she’ll come back one day."
    s "So-"
    ch "Chinami thinks you should take the hint and just come over already! These questions aren’t helping anybody!"
    s "There’s no need to get impatient. I was just about to head there."
    ch "Nuh-uh. Chinami felt another question coming. That’s all you adults ever do. Just talk, talk, talk! You never look at the big picture!"
    s "Correct me if I’m wrong, but I’m pretty sure I am the only adult you know."
    ch "This is exactly what Chinami is talking about! You just don’t know when to stop talking!"
    s "Okay. I’m hanging up now."
    ch "Wait! Can you bring doughnuts? You can’t have a business meeting without doughnuts and Chinami might die if she gets them on her own."
    s "Nope. But I’ll see you soon."
    ch "So rude!"

    play sound "phonebeep.wav"

    "I hang up the phone and begin my journey over to Chika’s place."

    scene black
    with dissolve2

    "Why she’d ask {i}me{/i} to bring over food when I am both not her intern and significantly poorer than the other people she has coming over, I don’t know."
    "But expecting rational decisions out of isolated girls who spend the majority of their day slaughtering cartoons is probably not a thing I should be doing in the first place."
    "Either way, I board a bus to the old district instead of pushing my luck and trying to have Touka and whichever one of her drivers she chose today pick me up along the way."

    play sound "dooropen.mp3"
    scene chinamiplayshouse1
    with dissolve2

    "Which, of course, means that I show up later than the other two as public transportation is only reliable around 50%% of the time."
    "But on the bright side, Touka is wearing what has quickly become my favorite outfit of hers. And one that will make “babysitting” exponentially harder to do as my focus lies elsewhere."

    tk "Chinami! What’s that thing?!"
    ch "Chinami believes that is called a “stove!” It’s where big sis Chika cooks Chinami’s eggs."
    tk "Your sister cooks for you? Is that even allowed?"
    ch "Big sis Chika is the {i}only{/i} person who cooks for Chinami. Big sis Yumi has tried, but she isn’t very good."

    scene chinamiplayshouse2
    with dissolve

    tk "How come you never cook for me? Shouldn’t you try acting a little more like Chinami’s sister?"
    to "Can I start by covering your mouth so you can’t speak anymore?"
    tk "You’re lucky you’re my sister or I’d have you fired."
    s "You should really come up with a different solution for all of your problems than just firing people."

    scene chinamiplayshouse3
    with dissolve

    ch "Papa!"
    tk "Jeeves!"
    to "Oh, Sensei. You’re so late that I assumed you just forgot about our plans."
    s "Me? Forget? No way."
    ch "Chinami had no idea Papa’s real name was Jeeves! He looks like more of a Philip to her."
    tk "Philip Jeeves Tsukioka the Fourteenth!"
    s "Wasn’t it thirteen last time?"
    tk "I had to let another one go. Good butlers are just impossible to come by nowadays."

    scene chinamiplayshouse4
    with dissolve

    ch "Chinami doesn’t see any doughnuts. Who do you think you are, showing up so unprepared?"
    ch "Chinami even had to give a tour of her whole house all by herself! Do you have any idea how much work that was for her?!"
    s "If you stood in the doorway behind you, you probably wouldn’t have even had to move."
    ch "This is why Chinami needed you here. CEOs are not trained for small jobs like that. Chinami has far better things to do."
    tk "Chinami! Can we eat more cereal? It may be the last time I ever see it, so I want to cherish the experience!"

    scene chinamiplayshouse5
    with dissolve

    ch "Big sis Chika says only one bowl a day! Otherwise, Chinami will get fat and no man will ever love her!"
    tk "Can we play with your toys, then?"
    ch "Chinami doesn’t have any toys. But she will show you the super cool phone her Papa bought for her. It’s her most prized possession."

    scene chinamiplayshouse6
    with dissolve

    "Chinami and Tsukasa scurry off to the bedroom, leaving Touka and me alone in the other half of the apartment."

    to "Thank you...truly. This is not something I would have been able to do on my own."
    s "Not good with kids either?"
    to "It’s less that and more...umm...how should I put this-"
    s "The apartment?"
    to "It is an utter crime that people are allowed to live in such places."

    scene black
    with dissolve2

    "Touka follows the other two girls into the living room, prompting me to do the same as I don’t want to be the one to clean up the spilled milk and cereal all over the kitchen table."
    "Granted, I probably {i}will{/i} be the person to do just that before the day ends as I’m not sure if Touka and Tsukasa even understand the concept of cleaning on their own instead of having a maid do it for them."

    scene chinamiplayshouse7
    with dissolve2

    "I guess I could always just make Chinami do it, though. It’s about time she learned some responsibility rather than just manipulating me into doing her dirty work."

    to "What even is this strange piece of furniture? A...sculpture? I’ve never seen anything like it before."
    s "Me neither, but it’s been here since I started coming and I just haven’t had it in me to question it."
    ch "That’s the TV antenna from the room below us! Nobody lives there anymore, but Chinami heard the whole place will fall apart if we try to remove it!"
    ch "So please be careful! Chinami doesn’t want to be homeless!"

    scene chinamiplayshouse8
    with dissolve

    to "I don’t think I can do this, Sensei. This place is as good as a death trap. I’m not even sure if I’ll be able to sleep knowing this poor girl will be spending the night here."
    to "Oh. And to clarify, I meant poor in regard to the amount of pity I feel for her. That was not me suggesting how much better off I am. "
    to "Though...saying that out loud may have just had the opposite effect."
    to "What I’m trying to say is-"
    s "I get it, Touka. The apartment sucks. But it’s all the Chosokabes can afford, unfortunately."
    tk "Hey, Chinami. What’s that over there?"
    ch "That’s called a “television!” Big sis Yumi found it on the street and sometimes the picture even stays clear for ten whole minutes!"
    tk "Not that. The thing next to it."
    ch "Oh! Chinami will show you!"

    scene black
    with dissolve2

    "Chinami runs over to the same table she ran to the first time I ever came here..."
    "And lifts up the same photo frame she showed me before thinking about castles became a near daily occurrence."

    scene chinamiplayshouse9
    with dissolve2

    ch "This is Chinami’s mom! Isn’t she pretty?"
    ch "Chinami wants to look like her when she gets older. But she thinks big sis Chika will probably look more like her than Chinami will. "
    tk "Do you look more like your dad or something?"

    scene chinamiplayshouse10
    with dissolve

    ch "Chinami doesn’t really know what her dad looks like. But maybe!"
    ch "If Chinami didn’t have this picture of her mom, she probably wouldn’t know what she looked like either. She’s been gone for a long time."
    tk "I see."
    tk "So you don’t really know what it’s like to have parents at all, huh?"
    to "Tsukasa, don’t ask questions like that! It’s extremely insensitive."

    scene chinamiplayshouse11
    with dissolve

    ch "Chinami doesn’t mind! Her mom still watches over her while big sis Chika and her teacher give her all the love she needs to survive."
    ch "She does wish she was still alive, though. And she wishes her dad was still here too, but big sis Chika gets angry whenever Chinami says that, so she doesn’t say it much."

    scene chinamiplayshouse12
    with fade

    to "I am beginning to believe that everything about today has been carefully designed to reduce me to tears. It is a miracle I haven’t cried yet."
    to "It’s no wonder you chose Chika over me during the first annual Super Mega Ultimate Dorm Wars. No high end restaurant nor plate of foie gras could compete with this..."
    to "This...heart wrenching, unreserved look into the lives of those less fortunate than me. Or even {i}you,{/i} for that matter. "
    to "How do things get to this point for some people while so many others live life completely unaware of the dire straits our fellow man can wind up in for no good reason at all?"
    s "Can I say something about living inside a bubble without you making some sort of allusion to the Tsukioka bubble wrap empire?"

    scene chinamiplayshouse13
    with dissolve

    to "Not anymore, you can’t. Now, that’s going to be the only thing I can think of."
    tk "Onee-chan! Jeeves! Play with us!"

    scene chinamiplayshouse14
    with dissolve

    to "Play with you how? There’s hardly any room to do anything here and Chika advised that we must not take Chinami outside. "
    tk "Let’s play house so Chinami can know what it’s like to have a family!"
    to "Tsukasa! Please don’t say such insensitive things!"
    ch "It’s okay! Chinami wants to play too! She thinks it sounds fun and has never played a game with this many people before!"
    ch "She is afraid she will mess up, though! So please tell her if she’s doing anything wrong!"
    to "H...How exactly does one play “house?”"
    s "We have two girls with a skewed perception of standard family dynamics, one girl with virtually {i}no{/i} perception of that, and me. There is no way this is going to end well."
    tk "It’ll be fine! Chinami and I will be sisters and you two can be the parents!"

    scene chinamiplayshouse15
    with fade

    to "P-Parents?! Us?!"
    s "Where else did you think this was going?"
    to "I had {i}assumed{/i} that I was going to be your daughter as well. I have no idea how this game works."
    s "You can call me “daddy” if you want. I don’t mind."

    scene chinamiplayshouse16
    with dissolve

    to "Of course {i}you{/i} don’t mind. But that’s absolutely not something I want to be calling you in front of my little sister."
    s "So what I’m hearing is it would be okay if we {i}weren’t{/i} in front of your little sister."
    to "That is what you are hearing because that is what you {i}want{/i} to hear. The reality is-"
    ch "Chinami says stop flirting and play already! "
    tk "I think we’re already playing. Those two seem to have gotten in character rather quickly. Wouldn’t you agree, Chinami?"
    ch "Oh! Chinami has no clue. She’s never seen real parents talk to each other before."
    s "What am I supposed to call you?"
    to "“Touka” would be a good place to start, but even that seems to prove challenging for you the vast majority of the time."
    s "How about “darling?” Does that work?"
    to "I suppose, so long as it never leaves this room."
    tk "Jeeves! Uhh...I mean...Papa! We want attention! Give us attention!"
    ch "Chinami wants to eat peanuts!"

    scene black
    with dissolve2

    s "I don’t care how badly Chinami wants to eat peanuts when peanuts will kill her."
    tk "Mother! Chinami is having suicidal thoughts and must be talked back from the brink of death!"
    to "Why did we immediately jump to the hardest possible part of parenting?! I’ve only been a mother for thirty seconds! I’m not prepared for this!"

    scene chinamiplayshouse17
    with dissolve2

    "The four of us take a seat on the bed (You know, the way real families always do) and just...start staring at one another."
    "In other news, this game sucks."

    scene chinamiplayshouse18
    with dissolve

    "But at least it gives me another opportunity to gaze down at what is at least temporarily and fictionally mine. "

    tk "Mother. Mother. Father is staring at your chest."
    to "He does that, dear. It’s not something that can be helped."
    ch "Mommy, can I ask you a question?"
    to "Of course, Chinami. What is it?"
    ch "How come Chinami doesn’t look like either one of her parents?"

    scene chinamiplayshouse19
    with dissolve

    to "Father?"
    s "There can only be one explanation."
    s "Your mother is having an affair."

    scene chinamiplayshouse20
    with dissolve

    to "What?!"
    ch "Mommy, why?!"
    tk "Is it with the gardener?! I’ve seen the way you’ve been looking at him!"
    to "You’re already turning the whole family against me?! It hasn’t even been five minutes!"
    s "You did this to yourself, darling. All I ever did was love you."

    scene chinamiplayshouse21
    with dissolve

    ch "Tsukasa, what is an affair? Chinami was just playing along, but she doesn’t really know what that word means."
    tk "I’m pretty sure it’s when a mom or dad starts spending time with somebody else’s mom or dad. Which might explain why you don’t look like them, Chinami."

    stop music fadeout 10.0

    tk "What we need to do now is find your real dad! And we can start by making a list of all of the men Mother is seeing behind Father’s back!"
    s "Just how many others are there, Touka? Tell me."
    to "Hah..."
    to "I really hope Chika’s day is going better than mine so far..."

    scene black
    with dissolve2

    "{i}Meanwhile, Chika’s day...{/i}"

    $ renpy.end_replay()
    $ chinamidate25 = True
    $ chinami_love += 1
    $ touka_love += 1

    jump yumichikaspecial1

label chinamidate30:
    stop music
    scene blood1
    play music "seek.mp3"
    $ renpy.pause(3, hard=True)
    scene blood2
    $ renpy.pause(3, hard=True)
    scene blood3
    $ renpy.pause(3, hard=True)
    scene blood4
    $ renpy.pause(3, hard=True)
    scene mall1
    play music "mall.mp3"

    "{s}I GO TO MALL{/s} I go to the mall."
    "I still haven’t been paid for watching Chinami and company recently, so I figure that Chika at least owes me a discreet blowjob in the bathroom or something along those lines since she can’t actually {i}pay.{/i}"
    "But hey, I’m sure a blowjob from someone like her would be valued at quite a bit and that there would be plenty of people willing to pay for such a thing if they weren’t all dying out in space."
    "Anyway, time to fuck my fake girlfriend."

    scene black
    with dissolve2

    "scene {s}transgression{/s} transition"

    scene chinamiwormparty1
    with pixellate

    c "How much longer, Chinami?"
    ch "Just a minute! Chinami is having trouble tying her shoes!"
    c "Do you need me to come in there and help you?"
    ch "Chinami can do it! She just needs patience!"
    c "Okay! Just let me know if-"
    s "Hello."

    scene chinamiwormparty2
    with dissolve

    c "Oh, hey! I didn’t even notice you there."
    s "Yeah, I kind of just show up sometimes."
    c "Hey, if there’s anybody I want to just randomly pop up throughout the day, it’s you. So you’re not going to hear any complaints from me."
    s "What’s Chinami doing here?"

    scene chinamiwormparty3
    with dissolve

    c "Just trying on some clothes and stuff. Yumi hasn’t come back yet, so she’s been alone a lot lately and it’s been a little while since the last time I brought her here."
    c "Figured I might as well buy her some new clothes while I’m at it."
    s "From here? I didn’t realize you were suddenly rich."
    c "Oh, no. Not from here. We bought her a new outfit from The Gap. But she still wanted to try on some of the clothes here so she could feel fancy."
    c "Chinami! Are you almost done? Sensei wants to say hi!"
    s "Actually, I was kind of hoping we could be {i}alone{/i} today if you catch my drift?"

    scene chinamiwormparty4
    with dissolve

    c "Here? But I thought you said stuff like that was too risky and that you wanted to slow down?"
    s "Yes, well I didn’t have a raging erection when I said that."

    scene chinamiwormparty5
    with dissolve

    c "Well, save that thing for later and come visit me again when my kid sister isn’t literally ten feet away. There’s no way I can get away right now. "
    s "Worst girlfriend ever."

    scene chinamiwormparty6
    with dissolve

    c "Oh, I’ll make it up to you. Don’t worry at all, Sensei."
    c "The truth is that I’ve also been craving your thick-"
    ch "Chinami is back!"

    scene chinamiwormparty7
    with hpunch

    c "Meatloaf!"
    s "Nice cover."
    ch "I didn’t know future Daddy could make meatloaf. "
    ch "How come he never brings his thick meatloaf to our house?"
    s "I didn’t like that sentence at all."
    c "Chinami, please don’t say “thick meatloaf” anymore. "
    ch "But big sister Chika sounded so excited when she was talking about Papa's thick meatloaf."
    c "Chinami, stop it."

    scene chinamiwormparty8
    with dissolve

    c "Wait, where is your helmet?! What do you think you’re doing coming out here without it on?! You could get sick."
    ch "But it’s so hot! Chinami is literally dying while she’s inside the helmet."
    s "Technically, we’re all “literally dying” every second of every day."

    scene chinamiwormparty9
    with dissolve

    ch "We are?! That’s Bad News Bears!"
    c "Did you just wake up today and decide to do everything within your power to make my life harder?"
    s "Of course not. If that were true, I’d have shown up here with my arm wrapped around Yumi."
    c "Hope you’re ready to fight off the Yakuza."
    ch "That’s even more Bad News Bears! Chinami knows something like that is called an affair now!"

    scene chinamiwormparty10
    with dissolve

    c "How does Chinami know that?!"
    ch "Because Tsukasa’s big sister is having an affair with everyone in town!"

    scene chinamiwormparty11
    with dissolve

    c "She is? But she seems so innocent. "
    ch "It’s totally crazy! And really Bad News Bears!"
    s "Why is Chinami’s catch phrase suddenly the title of a 1970’s baseball film?"
    c "Where did you hear that, Chinami? Did Tsukasa tell you? Because there’s barely ever any gossip I’m not in on and-"

    scene chinamiwormparty12
    with hpunch

    c "Wait a second! Stop talking and go get your helmet! "
    ch "Chinami is sorry! Please don’t have an affair while she’s gone!"

    scene chinamiwormparty13
    with dissolve

    "Chinami darts back into the dressing room, leaving me outside with both Chika and my raging hard-on (Yes, it is still there)."

    c "Sensei...why is my little sister suddenly talking about things she shouldn’t understand the meaning of for at least another...five thousand years?"
    s "It’s gotta be the Tsukiokas. They’re bad influences, I tell you."
    c "I’ll try to find time to scold Touka in between her apparent bang sessions with all of my neighbors."

    scene chinamiwormparty14
    with dissolve

    ch "Chinami is back and doggier than ever."
    s "I don’t think your “dog” level has increased just because you got a new outfit."
    ch "Right! Chinami got a new outfit! What do you think, future Daddy? Is Chinami super cute?"
    s "Sure. Why not?"
    ch "Wouldn’t she be cuter {i}without{/i} the helmet?"
    c "The helmet stays on, Chinami. I don’t want you getting sick and you’ve already been exposed to more people than normal lately."
    ch "That’s okay! Tsukasa’s big sister washed her hands many, many times while she was at the house! She did it after almost everything she touched! It was really weird."
    s "I think that was just Touka’s inherent lack of knowledge in the face of poverty compelling her to practice better hygiene when in places she expects to be less...clean."
    ch "Maybe! Chinami only understood half of that sentence, so she doesn’t really know."
    c "Are you hungry yet, Chinami? It’s about time for me to go on break. And I still need to pay Sensei back for watching you the other day, so I can get him lunch while we’re out as well."
    s "I was kind of hoping {i}the other thing{/i} would be my payment."

    scene chinamiwormparty15
    with dissolve

    c "You mean the thing I will do literally whenever, {i}wherever{/i} so long as there isn’t a girl wearing a dog mask several feet away from us?"
    s "Chinami, take off the mask. It’s for a good cause."
    ch "If that’s what future Daddy says, Chinami has to listen!"

    scene chinamiwormparty16
    with dissolve

    c "Don’t you dare. You so much as reach for that mask and I’m taking you to the kennel."
    ch "But the other dogs don’t like Chinami! She’s too big and hasn’t learned their language yet!"

    scene black
    with dissolve2

    "Begrudgingly, Chinami keeps the mask on as Chika clocks out for her break and begins to lead us over to the mall’s food court."
    "Things are a little busy once we get there as it seems that people from many of the other shops are starting to take their breaks as well but, despite that, no one really pays any attention to Chinami."
    "I don’t know if the novelty of seeing a little girl in a dog mask has just worn out for all of these people but, at least to me, knowing we’re not the center of attention is good."

    scene chinamiwormparty17
    stop music

    "{b}Because that means no one will see anything I do to them.{/b}"

    scene chinamiwormparty18
    play music "mall.mp3"

    ch "If Chinami could have any superpower, it would be to drink things with her hands. That way, she wouldn’t feel completely helpless right now!"
    c "Can’t you fit your milk inside of the helmet? "
    ch "Last time Chinami tried that, she made a huge mess. And she doesn’t want to ruin her brand new clothes the first time she wears them."
    c "Well, keep it on while we’re in the food court. Once our food comes, I’ll let you take the helmet off in the office at my store where I can make sure everything is safe."
    ch "Will Chinami ever get to come to the mall without her helmet on?"
    c "One day when your immune system is stronger, sure. But right now, you’re still young and shrimpy and need to be extra careful so you don’t get sick."
    ch "Chinami doesn’t like it, but she understands. "
    ch "She will just try to absorb the milk through osmosis so everyone can be happy."
    c "Good girl. Maybe after I get out we can go look for a mask that’s a little less hot? It’s almost October, so Spirit Halloween is probably going to be putting up shops all around our house before we know it."
    s "I didn’t realize they were so popular in the old district."

    scene chinamiwormparty19
    with dissolve

    c "Wherever there are unused storefronts, there will {i}always{/i} be a Spirit Halloween."
    c "Spirit Halloween, for all of your Halloween related needs."

    scene chinamiwormparty20
    with dissolve2
    $ renpy.pause(5, hard=True)
    scene chinamiwormparty19
    with dissolve2

    s "Did anyone else see that just now?"
    c "Hm? See what?"
    ch "Chinami hasn’t seen {i}anything{/i} in ten whole minutes!"
    c "Hang in there, Sensei. I’m pretty sure all of that, uhh...{i}redirected bloodflow{/i} might be making you a little lightheaded right now. "
    c "You seem kinda pale too. Want me to get you a bottle of water or something? I’m friends with the girl working the sushi place right now so I can get you one for free if you want."
    s "You don’t need to-"
    c "Sensei, it’s fine. I’m going to have to head over there to pick up our food in a few minutes anyway. And I have, like...zero clue what I’d do if you were to pass out in front of me."
    s "You could always help re-{i}re{/i}-redirect some of my bloodflow, Chika. That would probably help a little more than water."
    c "Would it really, though?"
    s "{s}Fuck me while she can’t see us.{/s} Yes."
    c "Would it really though? "
    s "{s}I will wrap my hands around your throat and make your eyes roll back.{/s} Yes."
    c "Would it really though? "
    s "{s}DO YOU think I WILL NOT take you here???{/s} Yes."
    c "{b}WILL IT REALLY THOUGH???????????????{/b}"
    s "{s}DO YOU THINK I WILL NOT TAKE HER AS WELL???{/s} Yes."

    scene chinamiwormparty21
    play sound "pop.mp3"

    ch "Arf!"
    s "Huh? Where did Chika go?"
    ch "Big sis Chika went to go get you water. Chinami decided to bark since you weren’t saying anything."
    ch "You need to be careful, future Daddy. She might make you start wearing a mask soon too if you don’t start acting like you’re okay!"
    s "I...think I’ll be fine without a mask, Chinami."
    ch "Chinami thinks she’ll be fine without a mask too!"
    s "Too bad that Chinami has to-"

    scene chinamiwormparty22
    with dissolve

    ch "Gehh..."

    "Oh no. I’m the bad parent."

    ch "Chinami...is finally free..."
    s "Chinami, you’re going to get {i}both{/i} of us in trouble if you don’t put that back on."

    scene chinamiwormparty23
    with dissolve

    ch "I seriously can’t do it anymore! It’s too hot and I’m going to pass out if I stay in there any longer! "
    ch "There’s nobody else around! At least let me breathe for a few seconds until Onee-chan comes back!"
    s "Who are you and why are you talking like that?"
    ch "Uhhhhh..."

    scene chinamiwormparty24
    with dissolve

    ch "Arf?"
    s "I’m...going to ignore that momentary lapse in character and chalk it up to the early stages of heatstroke. So...fine. "
    s "You can keep it off. But as soon as Chika turns around, you’re putting it back on. I am not risking my {i}plans{/i} for later tonight just because you think it’s important to {i}breathe.{/i}"

    scene chinamiwormparty25
    with fade

    ch "Chinami thanks you for your kindness, future Daddy. She promises she won’t ask you what your plans for later tonight are either."
    s "Good because I have no idea how I would even explain them to you."
    ch "Chinami is smarter than she looks, you know. She can do ten times ten in her head. She can even say her phone number with her eyes closed."
    s "That last one isn’t that impressive."

    scene chinamiwormparty26
    with dissolve

    ch "Chinami doesn’t like when future Daddy doesn’t believe she’s super awesome and smart."
    s "And {i}I{/i} don’t like being repeatedly referred to as “future Daddy” despite having no real intention of becoming your father."
    ch "Chinami thinks this is called a crossroads and that we should both agree to talk about something more fun. Like giraffes or rabbits."
    s "How about we talk about why you’re suddenly tired of your helmet when I thought you loved it?"

    scene chinamiwormparty27
    with dissolve

    ch "Chinami does love her dog helmet! She just wishes it had air conditioning!"
    ch "Do you even watch the news?! This is supposed to be the hottest summer ever! Get your head out of the super hot clouds and read a paper or something!"
    s "No one reads the paper anymore, Chinami."
    ch "No wonder why society is collapsing! "
    s "I think the collapse of society runs a little deeper than the death of print, but that’s not something I should be getting into with a literal child."

    scene chinamiwormparty28
    with dissolve

    ch "Arf. Arf arf arf. Arf arf arf arf."
    s "What are you saying right now?"
    ch "Chinami is discussing climate change with her disembodied head. She does this sometimes when she feels there aren’t enough intellectuals around."
    s "Wow, I sure hope Chika comes back soon so you can go back to not breathing."

    scene chinamiwormparty29
    with dissolve

    ch "Do you really think it’s fair that Chinami has to wear this {i}all{/i} the time? She understands what’s safe and when to be careful. "
    s "It’s not {i}all{/i} the time, it’s just...whenever you’re out in public. And it’s for your own good, isn’t it?"
    ch "What good is a life that’s no fun?! Chinami wants to see what everybody else sees so that she doesn’t have any regrets when she’s finally gone! And Chinami can’t see anything in there!"
    s "It’s far too early to talk about being {i}gone,{/i} Chinami. Like Chika said, your immune system could get stronger one day and-"
    ch "But what if it doesn’t?"
    s "..."

    scene chinamiwormparty30
    with dissolve

    ch "What if I stay weak forever? "
    ch "What if I live my whole life never knowing what it’s like to be a normal girl?"
    ch "What if-"

    scene chinamiwormparty31
    with hpunch

    ch "Ah! Big sis Chika! Chinami must hide!"

    scene black
    with dissolve2

    "Chinami quickly shoves the dog helmet back on top of her head just seconds before Chika looks up from the tray carrying all of our lunches."
    "When she returns to the table, she thanks Chinami for being such a good girl and listening to her big sister."
    "She offers to buy her ice cream on the way home and I have to nod and agree with everything Chika says so Chinami’s secret stays safe."
    "Or at least {i}one{/i} of her secrets. "
    "Among the sea of noise pouring from the mall’s loudspeakers, I hear something on the way back to the boutique."

    stop music

    "A stifled cough, silenced by the head of a dog."
    "And a reactive “arf” to hide it."

    $ renpy.end_replay()
    $ chinami_love += 1
    $ chinamidate30 = True
    $ buckettoken = True

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "{i}You take her home along with Chika before leaving her all alone in exchange for the sight of a beautiful girl with a mouth full of cum.{/i}"

    $ chika_lust += 1

    "{i}Chika’s lust has increased to [chika_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label chinamispring1:
    if _in_replay:
        play music "comfort.mp3"

    scene chinamiwatching1
    with dissolve2

    ch "Three..."
    ch "Two..."
    ch "One..."

    play sound "dooropen.mp3"
    scene chinamiwatching2
    with dissolve

    c "I am {i}not{/i} supposed to be wearing this yet!"

    scene chinamiwatching3
    with dissolve

    ch "She’s not supposed to be working right now either. But big sis Chika has had her priorities all kinds of messed up lately!"
    s "Yeah...I can see that."

    scene chinamiwatching4
    with dissolve

    c "Okay! {i}Now,{/i} I can leave! Bye, guys! Be good! I’ll let you know when I’m on the way home!"

    play sound "dooropen.mp3"
    scene chinamiwatching3
    with dissolve

    c "{i}LET’S FUCKING GO FOR REAL THIS TIIIIIIIME!{/i}"

    "The clopping of Chika’s boots as she sprints off toward the maid cafe fades long before I want it to. And as she disappears from her now home, I envision a future in which it is ours."
    "Well...I guess, technically speaking, it {i}is{/i} ours. Just she’s not currently aware that I’m inhabiting such a place. And unless Chinami has ESP (Which is always a possibility), she’s unaware as well."
    "It’s strange and depressing how the last twenty-four hours have gone. "
    "I’ve spent time with two families who would openly allow me to insert myself into them (In any way I want) while neglecting the family I already have for reasons I can’t even properly explain."
    "It’s not fear, is it?"
    "Responsibility?"
    "I’d say it’s just me being a terrible guardian, but that’s always been the case as {i}I’ve{/i} been the one being guarded instead."
    "And when I’m most needed, I’m here — spending time with someone I have nothing in common with as an excuse disguised as obligation."
    "And as depressing as it is that the Chosokabes have lost both of their parents, the most depressing facet of all is that’s created a future in which {i}I{/i} could be Chinami’s father figure."
    "And I would break her like the china doll she is, but she doesn’t see me that way. "

    scene chinamiwatching5
    with dissolve

    "Just look at her, completely trusting and vulnerable, when her fate lies entirely in my hands for the next eight or so hours."
    "Does she not realize how easy it would be for me to snap? How many times it’s happened already? How {i}she{/i} could be the next Yumi or Molly and live the rest of her life scarred and traumatized?"
    "Of course she doesn’t."
    "Because not only are those things beyond her understanding at this point in life-"
    "It’s that the “rest of her life” is questionable to begin with when she’s probably going to die before any one of us."
    "But hey, maybe I’ll beat her there if the cards start favoring me soon. After all, they {i}do{/i} say that every dog has its day, and I’ve been nothing short of a bitch lately. "

    ch "Arf!"

    "But I guess Chinami is part-dog too."
    "I’m just not sure if death is what she’d order off the menu right now."

    s "Why are you barking without your helmet on?"
    ch "Chinami just felt like barking. Dogs do that sometimes."
    ch "A lot of people say it’s because they can see ghosts, but Chinami isn’t sure she believes in them."
    ch "Do you believe in ghosts, Papa?"

    play sound "static.mp3"
    scene fuckherdoityoupussydoit1 with flash
    scene chinamiwatching5 with flash
    stop sound

    s "Yes."

    scene chinamiwatching6
    with dissolve

    ch "Really? Chinami is surprised to hear that! Chinami was sure that Papa was about to lecture her about imagination being stupid."
    s "It’s not stupid, it’s harmful. Plus, I don’t have the energy to lecture you about anything today. So I don’t really care about whatever your stance on dead people is. "
    ch "Imagination is harmful? Why?"

    scene chinamiwatching7
    with dissolve

    s "Well..."
    s "It doesn’t always have to be."
    s "But it usually {i}is{/i} because engaging with it is like...spending time away from reality. And there’s no benefit to imagining {i}anything{/i} if the bulk of your life is going to be spent...you know, {i}living.{/i}"
    ch "But it can keep you entertained when things are boring. And if things are boring and you can’t use your imagination, what are you supposed to do?"
    s "Either sit there and watch TV like you’re doing or engage in acts I can’t talk to you about."
    ch "Is Papa in a bad mood today? He seems a lot grumpier than he was just a minute ago."

    scene chinamiwatching8
    with dissolve

    s "It’s been a tough week. I’m sorry."
    ch "Papa doesn’t need to be sorry! Chinami accepts Papa no matter who he is and how he feels! But Chinami might also just be saying that because she’s always lonely now and wants more company."

    scene chinamiwatching9
    with dissolve

    ch "Big sis Chika has been working a lot while you’ve been gone so she can save up money for stuff. And big sis Yumi is...actually, Chinami doesn’t know what big sis Yumi has been doing. But she’s been busy too."
    ch "Those two and Papa are the only people Chinami knows. Minus her business partner, Tsukasa, of course. But Tsukasa and Chinami are very different."
    s "And you and I aren’t?"
    ch "Chinami doesn’t think so! Chinami thinks Papa is kind beneath his grumpy outside. And he loves big sis Chika just like Chinami does, so they have that in common."
    s "I think I {i}love{/i} her a little differently than you do."
    ch "Like you’re going to make babies with her? Because Chinami doesn’t know how to do that and will understand if that’s what makes you different."
    s "..."
    ch "Or did you mean something else?"
    s "You were close enough. But I’ve also been rethinking just what “love” is lately, so who can say I have any idea what I’m even talking about at this point?"

    scene chinamiwatching10
    with dissolve

    ch "Does Papa love Chinami?"
    s "No."

    scene chinamiwatching11
    with dissolve

    ch "So quick! Chinami is hurt!"
    s "Like I said, the way I love things is different from how you love things. And it’s even worse because the things I love are always {i}wrong{/i} for me to love in the first place."

    scene chinamiwatching12
    with dissolve

    ch "Is it wrong for you to love big sis Chika?"
    s "It’s extremely wrong."
    ch "Why?"
    s "Because I’m thirty-one. And she’s..."
    ch "And that makes it bad?"
    s "Yeah. The only type of love I know how to have isn’t meant for girls her age. I should love people closer to mine."
    ch "Chinami thinks she understands. She watched a K-drama where a teacher kissed a student and everybody got mad. Is it like that?"
    s "Yeah...It’s like that."
    s "But it’s not bad because it makes other people mad. It’s bad because I should know better by now."
    ch "Why don’t you?"
    s "Because I’m an idiot, Chinami."
    ch "But how did Papa become a teacher if he is an idiot? Is the educational system failing us? Is it good that Chinami is homeschooled?"

    scene chinamiwatching13
    with dissolve

    s "Yeah. You’re a lot safer here. Even if it {i}can{/i} get pretty boring at times."
    ch "That’s good. Because Chinami wants to be able to have good conversations with Papa, and she can’t do that if she isn’t smart. "
    ch "But maybe she can after all if Papa is dumb too. Chinami doesn’t know what to think right now. Her brain is moving in two different directions."
    s "Well, hey. We’ve got that in common too."

    scene chinamiwatching14
    with dissolve

    ch "Like Chinami said! We have lots in common! Papa probably just doesn’t want to think so because he isn’t good at letting himself be happy."
    s "And how do {i}you{/i} know that? We barely even talk."
    ch "Chinami overheard it!"
    ch "Chinami’s heard lots of stuff about Papa over the last two months. Big sis Chika’s been going kinda crazy and it’s making her say some weird stuff sometimes."
    s "What kind of weird stuff?"
    ch "Some stuff that makes her sound really smart. And then other stuff that makes her sound really insecure."
    ch "Big sis Chika’s always been super strong and super confident. But when Papa wasn’t around, Chinami heard her blaming herself for it sometimes. And it was super-duper weird."
    s "It wasn’t Chika’s fault at all..."
    ch "Chinami knows that! Big sis Chika is too good at things to mess any of them up. So Chinami assumed Papa had other problems that nobody knew about. But that confused her too because her brain is small."
    ch "Big sis Yumi said you hate yourself, but Chinami doesn’t understand why. Is it because you love the wrong things? Like you said earlier?"
    s "That’s definitely a part of it..."
    ch "Will the other parts be easier for Chinami to understand?"
    s "Maybe in a few years, when your brain is bigger."
    ch "Chinami hopes so. She wants all the people she loves to be happy together, even if they all love each other differently."
    ch "And she was starting to worry that maybe you wouldn’t come see her anymore."
    s "It’s possible that’s true, Chinami. I need some time to myself to...think about things."

    scene chinamiwatching15
    with dissolve

    ch "So..."
    ch "This might be the last time Chinami sees you?"
    s "Maybe. Maybe not. There’s no way of knowing for sure."
    ch "Huh..."
    ch "Chinami doesn’t like that."
    s "I didn’t expect Chinami to like that."

    scene chinamiwatching16
    with dissolve

    "A moment of silence washes over us as Chinami attempts to understand what exactly I mean by this. And that moment is reinforced by {i}me{/i} wondering the same exact thing."
    "Just {i}I’m{/i} doing it earnestly. And Chinami is-"

    ch "I think that’s a bad idea, Papa."

    "Chinami is hard to understand sometimes."

    ch "If you stop coming here, big sis Chika might go crazy. And listening to her say sad and hurtful things about herself is very hard."
    s "Yeah, well, there’s someone else I love going crazy at this very moment. But all of the things she says are hurtful toward other people."
    ch "Is she a bully like big sis Yumi?"
    s "No. "
    s "She’s just confused and scared."
    ch "..."
    s "Your sister doesn’t need me the way she does. Like you said, Chika is really strong and really confident. And she’s done a great job when it comes to raising you. "
    s "There’s nothing {i}I{/i} can do for her that she can’t do for herself."
    ch "So it’s okay to hurt her? "
    s "It’s not {i}okay.{/i} That’s just kind of...how things happen when it comes to relationships sometimes. "
    ch "Should I stop calling you Papa?"

    scene chinamiwatching17
    with dissolve

    s "You never should have started in the first place..."
    ch "She won’t give up on you, you know."
    ch "If you just stop coming here, she’ll follow you. Forever. That’s the type of person big sis Chika is."
    ch "She’s loyal. And she cares about you as much as she cares about me. If you leave things open-ended, her feelings won’t just fade away. They’ll get bigger and scarier and more desperate."
    ch "If you don’t want to love her forever, that’s something you’ll have to tell her. If you don’t, it won’t ever actually end. And you’ll be running away for the rest of your life."
    s "Now, I’m not saying that’s what I’m {i}going{/i} to do...but a thing you should know about me if you want to have “good conversations” is that I’ve already been {i}doing{/i} that for my entire life."
    ch "Why?"
    s "Obviously because I don’t want what’s behind me to catch up."
    ch "What’s behind you?"
    s "..."
    ch "..."

    scene chinamiwatching18
    with dissolve2

    s "A ghost."
    ch "..."

    "Another moment of silence creeps in. But this time, I know exactly what Chinami is thinking. I’ve known since the moment she let go of that childish persona again."
    "She’s concerned."
    "She sees the somewhat happy life she’s wound up with slipping away, and she’s worried that the future she’s spent so much time alone {i}imagining{/i} is going to be harmful after all."
    "But more than that-"

    scene chinamiwatching19
    with dissolve

    ch "Come here, Papa."

    scene black
    with dissolve2

    "More than that, she’s worried about who will love her sister when she’s not there to do it anymore."
    "........."
    "......"
    "..."

    scene chinamiwatching20
    with dissolve2

    ch "Hi, Mama. Say hi to Papa. "
    s "..."

    scene chinamiwatching21
    with dissolve

    ch "Mama says hi. "
    s "Do I have to say hello back?"
    ch "That would be the polite thing to do, yes."
    s "Then...hello."
    ch "She can’t hear you. She’s just a picture."
    s "Yeah. I’m aware, Chinami."

    scene chinamiwatching22
    with dissolve

    ch "And one day, Chinami will be “just a picture” too."
    s "Picking the third-person act back up now that your mom is watching?"

    scene chinamiwatching23
    with dissolve

    ch "Chinami has no idea what you’re talking about! Her brain is small, remember?"
    s "Yeah, sure it is..."

    scene chinamiwatching20
    with dissolve

    ch "Chinami loves her new house. But her most favorite part of all is that they have a real altar now. And that Chinami can finally pay her proper respects to Mommy for giving Chinami a life."
    ch "She doesn’t want Mommy to blame herself for Chinami’s body not being perfect. Especially since Mommy’s body was never perfect either. "
    ch "She knows that sometimes, people just have bad luck. And that our luck was some of the worst ever. "

    scene chinamiwatching21
    with dissolve

    ch "But that just makes big sis Chika seem even more lucky since {i}her{/i} body is super healthy and super pretty!"
    ch "Which is why it’s super important that she lives a happy, fulfilling life since neither Mommy nor Chinami will!"
    s "Chinami, you don’t know-"

    scene chinamiwatching24
    with dissolve

    ch "I do, though. "
    ch "I don’t want to hide behind a mask forever. I want to be a normal girl...and do normal things. "
    ch "I want to know what you mean when you talk about different kinds of love. I want to make friends and go to the park and..."

    scene chinamiwatching25
    with dissolve

    ch "And pierce my ears and...try out new parfaits at fancy cafes! I want to join a club and...and I want to eat peanuts!"
    s "That last one is just asking to die, Chinami."

    scene chinamiwatching26
    with dissolve

    ch "They’re {i}all{/i} asking to die because doing {i}anything{/i} with this body is putting it in danger. But sitting inside and watching Spongebob Squarepants for eight hours a day isn’t {i}living.{/i}"
    ch "None of this is {i}living.{/i} But I put up with it because I want my sister to be happy. I want her to have something she looks forward to when she comes home from work."

    scene chinamiwatching27
    with dissolve

    ch "But there will be a time, whether we like it or not, when she comes home and I {i}won’t{/i} be here. And when that happens, I..."
    s "..."

    scene chinamiwatching28
    with dissolve

    ch "I was hoping you would take my place."
    ch "Because I know you love her. I can feel it when you’re together. I can see the way you look at one another and...it’s even better than what I see in movies."
    ch "You might not be perfect...and you might hate yourself like big sis Yumi says...but I think you can learn to live with that if you keep at it long enough, Papa."
    ch "Chinami doesn’t know the ghost you’ve been running from your whole life, but she knows that big sis Chika wasn’t there to run with you until a little while ago."
    ch "And no ghost is gonna mess with big sis Chika. She’s too strong."
    ch "She’s too {i}lucky.{/i}"
    s "..."

    scene chinamiwatching29
    with dissolve2

    ch "Aaah! Crying always hurts Chinami’s head! Look what you made her do, Papa!"
    s "I know. But I’ve never claimed to be good at babysitting."

    scene chinamiwatching30
    with dissolve

    ch "How about tutoring, then?"

    play sound "static.mp3"
    scene chinamiwatching31 with flash
    scene chinamiwatching30 with flash
    stop sound

    s "Uh..."
    ch "Papa is a teacher, right? Maybe he can make Chinami feel better by teaching her things while her big sister is at work?"
    s "I..."
    s "I don’t think that’s a good idea."

    scene chinamiwatching32
    with dissolve

    ch "It’s not?"
    s "Yeah, I don’t think that’s...a thing I should be doing here."
    ch "Rats."
    ch "We’ve got a big problem on our hands then, Papa."
    s "What do you mean we’ve got a big problem on our hands? What kind of problem do we have? I never agreed to tutor anyone. I don’t do that anymore. I don’t-"
    ch "But Chinami already told her business partner that you said yes."
    s "You did {i}what?{/i}"

    stop music
    play sound "knock.mp3"
    scene chinamiwatching33 with hpunch

    ch "That must be her now!"
    s "Chinami-"
    ch "Quick, Papa! To the door!"

    $ renpy.end_replay()
    $ chinamispring1 = True

    jump chinamispring2

label chinamispring2:
    play sound "static.mp3"
    scene tsukasaarrives1 with flash
    stop sound

    "To the door."

    play sound "knock.mp3"

    s "..."

    play sound "knock.mp3"

    "I should not have come here."

    play sound "knock.mp3"

    "I have found myself wedged between the past and the present in a space that can only be known as “doorway.”"

    play sound "knock.mp3"

    "I resist the temptation to put my shoes back on and march around in circles in hope of burning a hole through the floor, falling several stories, and then being impaled by my hip bones."

    play sound "knock.mp3"

    "I reach out my hand, which still unfortunately works, and make contact with a cold, metal handle."

    play sound "knock.mp3"

    "I keep it there for a moment, causing the small girl behind me to scratch her head in confusion."

    play sound "dooropen.mp3"
    scene tsukasaarrives2 with dissolve

    "Then I open it because I always do the wrong thing."

    play music "normalday.mp3"

    tk "Oh, Jeeves. You’re here already. Good. I was worried that Chinami was only lying to me about your presence as a means of luring me into her home so she could murder me and steal my assets."

    scene tsukasaarrives3
    with dissolve

    ch "Chinami would never do that! She values her business partner’s assets just as much as she values her own!"
    tk "Which goes to show that you are {i}clearly{/i} inferior to the great Tsukasa as you believe {i}your{/i} things are worth even a fraction of what {i}my{/i} things are worth!"
    tk "Let this be a lesson to you, Chinami. {i}Always{/i} assume the person you are meeting will be planning to kill you. That way, you’ll never be caught off guard!"
    ch "Being rich sounds scary. Chinami would like to sell her shares and move on to other ventures now."
    tk "Then Chinami will have to find a buyer."

    scene tsukasaarrives4
    with dissolve

    ch "Papa! Would you like to buy Chinami’s minority stake in-"
    s "No."

    scene tsukasaarrives5
    with dissolve

    ch "Rats!"
    tk "So! What will we be learning today, Jeeves? What is my first task as your newest pupil?"
    tk "If I’m allowed to make a suggestion, I’d like to start off on topics more advanced than what you’re currently teaching my sister. But I will settle for advanced calculus if that is not possible."
    s "Yeah, I’m not doing this."

    scene tsukasaarrives6
    with dissolve

    tk "What do you mean you’re not doing this?"
    s "I mean I never agreed to tutor either one of you. Chinami just decided I was going to."
    tk "But didn’t you have a meeting with my mother in which she explained to you that you would have to serve as my tutor going forward?"
    s "My memory’s never been great, but I recall that meeting going a little differently. "
    tk "Jeeves, are you trying to tell me I came all the way over here for nothing?"
    s "Yes. But I’m sure you’ll be able to get a ride back to your manor within five seconds so long as you have your phone on you."
    tk "I didn’t come from the manor. I came from next door."

    scene tsukasaarrives7
    with dissolve

    sch "What?"
    tk "Didn’t I tell you? I’m renting the room beside yours from my sister so I can begin to build credit history early."
    tk "What I really wanted was to rent the whole building. But unfortunately, Onee-sama has put several silly {i}rules{/i} in place that prevent me from leasing more than one room."
    ch "So Chinami has a friend who lives right next door?!"
    tk "Yes. But don’t expect me to spend too much time here as this place {i}is{/i} rather dreary and far below my standards."
    s "Well, at least that means you won’t have a long way to go to make it home. Bye, Tsukasa."

    scene tsukasaarrives8
    with dissolve

    tk "Chinami! What do you think we’ll be learning about today?! Molecular biology?! The fall of the Roman Empire?!"
    ch "Chinami needs to practice food kanji so she hopes it’s that!"
    s "You two aren’t listening to me at all, are you?"

    scene tsukasaarrives9
    with dissolve

    tk "Ancient wizards listen to no one, Jeeves. So it appears that you’re stuck doing as we tell you until my lessons are over."
    ch "Tsukasa is right, Papa. But don’t worry! If you’re uncomfortable teaching outside of the classroom, Chinami will do her best to simulate such an environment by using her very own notebook!"
    s "It takes more than a notebook to make a classroom, Chinami."

    scene tsukasaarrives10
    with dissolve

    tk "Ooh! An ancient proverb! Are {i}those{/i} what we’ll be learning today?!"
    s "What? No. That wasn’t a proverb, it was-"
    ch "Education! Wahoo!"
    s "You two...I’m not a tutor anymore. I’m not even a {i}teacher{/i} anymore. I quit."

    scene tsukasaarrives11
    with dissolve

    tk "Quit?! Onee-sama said nothing about you quitting! But she {i}has{/i} been very rude as of late, so it would not come as a surprise to me if this was true."
    ch "Big sis Chika said Papa was just taking a break! Is his break going to last forever?! Isn’t that not a break at all?!"
    s "Okay, so...maybe I didn’t {i}quit{/i} per se. But that still doesn’t mean I want to go back to my roots as a tutor. Especially when..."
    ch "..."
    tk "..."
    tk "When what?"
    s "Honestly, I don’t really know."
    ch "That isn’t good reasoning, Papa."
    s "I just don’t want to...retrace any of the steps from my past right now."

    scene tsukasaarrives12
    with dissolve

    ch "Because of the ghost?"
    tk "Ghost? What ghost?"
    ch "Papa is haunted by the ghost of his past. It forces him to make bad decisions and not love Chinami as much as he’s supposed to."
    tk "Onee-sama...mentioned nothing about ghosts in this building."
    ch "Cause it’s Papa’s ghost. He’s the one who brought it here."

    scene tsukasaarrives13
    with dissolve

    tk "Jeeves! I command you to get rid of your ghost right now! I will not have my education stalled by paranormal entities!"
    s "You’re really going to make me regret telling you about that ghost thing. Aren’t you, Chinami?"
    ch "If there is anything that Chinami has learned from watching every season of Game of Thrones, it’s that ending a popular book adaptation is hard without understanding the author’s true intent!"
    ch "But if there is anything else she learned, it’s that sometimes you have to leverage information people share with you in confidence to get them to do things you want them to do!"
    tk "Chinami is right! And this finger is me leveraging my power and influence to get you to leave the past behind and focus on the future! A future where you teach me things!"
    s "No."

    scene tsukasaarrives14
    with dissolve

    tk "Maybe if we just go sit down, he’ll follow us?"
    ch "Chinami thinks that’s a good idea. Papa gives into pressure easily."
    s "I don’t-"

    scene tsukasaarrives1
    with dissolve

    tk "{i}Hey, does your TV ever get switched to really weird channels too? Or is that just mine?{/i}"
    ch "{i}Chinami woke up late last night and a bunch of girls were taking their shirts off. Is that what you’re talking about?{/i}"
    tk "{i}What? No. Are they actually allowed to put that on TV?{/i}"
    ch "{i}Chinami doesn’t know. She just works here.{/i}"
    s "Hah..."

    scene black
    with dissolve2

    "I’ll be fine."

    play sound "static.mp3"
    scene memories33 with flash
    scene black with flash
    stop sound

    "This is just another day."

    play sound "static.mp3"
    scene memories33 with flash
    scene black with flash
    stop sound

    "What’s the worst that could possibly happen?"

    play sound "static.mp3"
    scene memories33 with flash
    scene tsukasaarrives15 with flash
    stop sound

    "{i}Answer: The worst that could possibly happen is you “falling” for one of them long before they’re meant to be fallen for, and leveraging YOUR power to make them do what YOU want them to do!{/i}"
    "{i}And it’ll be fine since THAT is what THEY are doing to you now! And THEY might want IT anyway!{/i}"
    "{i}There’s no way of knowing unless you try, Sensei! And you joined them on the blanket, so you CLEARLY want to, RIGHT?{/i}"
    "{i}Do it!{/i}"
    "{i}Collect more skin!{/i}"
    "{i}Be the PERVERT we all know you to be!{/i}"
    "{i}If she will not come back, simply MAKE A NEW HER.{/i}"
    "{i}CHOOSE.{/i}"

    menu:
        "“Choose” Chinami":
            $ chinamichosen = True
            s "Chinami."
            chi "Yes, Papa?"
            s "What do you know about The Catcher in the Rye?"

            scene tsukasaarrives16
            with dissolve

            c "Chinami is sorry, but she doesn’t know much about baseball."
            tk "He’s not talking about baseball, Chinami. He’s talking about a book some old, white guy wrote in the 1940’s."
            tk "They make teens in American schools read it because it’s supposed to teach them about growing up and losing their innocence and stuff. But I’ve never read it because Mother says it’s very boring."

        "“Choose” Tsukasa":
            $ tsukasachosen = True
            s "Tsukasa."
            tk "Yes, Jeeves?"
            s "What do you know about The Catcher in the Rye?"

            scene tsukasaarrives17
            with dissolve

            tk "Only what I’ve heard from Mother — that it’s a book aimed at young adults to help them “prepare for the world.” And also that it’s very boring."

    s "Right. Well, you see..."

    stop music
    play sound "static.mp3"
    scene tsukasaarrives18 with flash
    stop sound
    play music "shrinemaiden.mp3"

    s "The reason most people call it boring is actually-"
    m "I’m telling you! For the millionth time, there’s no way this “book” is preparing {i}anyone{/i} for {i}anything!{/i} It’s like 300 pages of some idiot kid whining about life."
    n "Oh man, here we go again."
    s "..."

    scene tsukasaarrives19
    with dissolve

    n "Maya, all I said was that you’re being a little harsh on Holden when he’s very clearly suffering from depression. It’s not like I said it was a great, interesting book that everybody should read."
    m "So what? There are millions of people suffering from depression out there. And it’s not like all of {i}them{/i} go around calling every single person they encounter fake. He’s infuriating."
    s "Those are both good points, so stop arguing with each other."

    scene tsukasaarrives20
    with dissolve

    n "I would love to, but I’m not allowed to say literally anything without Maya jumping down my throat for it."
    s "You {i}have{/i} been...unnecessarily rough on her today, Maya. Would it kill you to tone it down a bit?"
    m "{i}Kill{/i} me? Probably not. But I think you’re underestimating how hard it is for me to sit here and listen to someone vouch for the most incorrigible character in all of fiction."
    s "She’s not trying to vouch for him, though. All Noriko’s doing is trying to explain and understand {i}why{/i} he does the things he does."
    m "Yeah. And {i}I’m{/i} trying to say that it’s bullshit. You’ve got depression too, don’t you? And you’re way more bearable than Holden fucking Caulfield is. So why is {i}that{/i} what we keep coming back to?"

    scene tsukasaarrives21
    with dissolve

    m "I got absolutely {i}nothing{/i} from this book. So hearing all this stuff about its potential themes and purposes all just sounds like hogwash to me. It was a waste of time. Nothing deeper."
    n "I mean, I wasn’t a fan either. But we need to analyze it through the lens of the average reader if we’re going to understand its impact on the industry and why it’s still relevant today."
    s "Noriko’s right. You two are different from everyone else."

    scene tsukasaarrives22
    with dissolve

    s "There’s a reason I’m giving you harder reading material, after all. It’s because I {i}want{/i} to hear these types of outlooks. And I want {i}you two{/i} to be able to contrast them with the “popular” opinion."
    s "It’s important to understand and analyze why you’re different, because there are going to be times in life where you {i}can’t{/i} be. And you’ll need to figure out how to blend in whether you like it or not."
    m "Do you always have to side with her, though? It’s frustrating."
    n "Oh, stop. Sensei doesn’t {i}always{/i} side with me."

    scene tsukasaarrives23
    with dissolve

    n "I’ve just known him longer, so I know what he wants to hear!"
    m "Suck-up."
    s "Maya."
    m "..."
    s "Look at me."

    scene tsukasaarrives24
    with dissolve

    m "What do you want?..."
    s "..."
    n "..."
    s "Noriko, could you leave the room for a minute?"
    n "Can I count the seconds? Because last time you said a minute-"
    s "I’ll call you back in when I’m done talking to Maya, okay?"

    stop music
    play sound "static.mp3"
    scene tsukasaarrives25 with flash
    stop sound
    play music "normalday.mp3"

    tk "Okay!"
    tk "I get it now! This is a secret method of tutoring that Jeeves must have learned from...China! No! South Korea! The silent method!"
    ch "Chinami doesn’t like the silent method. She learns better when there are words involved."
    tk "Tsk, tsk, tsk. If you’re ever going to be a CEO, you’re going to need to master the silent method, Chinami. That way, when someone asks you for a raise, you can just stare at them until they go away."
    tk "I’ve watched Mother do it thousands of times. It helps if you have a good smile. Here! Let’s practice!"
    s "..."

    scene black
    with dissolve2

    "She wasn’t blurred this time."
    "........."
    "......"
    "..."

    scene tsukasaarrives26
    with dissolve2

    ch "Papa! Look at our smiles! Are we doing it right?!"
    tk "Do you think we’ll be able to effectively fend off lesser employees with them?!"
    s "How long have we been sitting here?"

    scene tsukasaarrives27
    with dissolve

    tk "Maybe like...twenty minutes or something?"
    ch "Chinami’s not convinced Papa was using the silent method like her business partner says. She thinks Papa might have just fallen asleep."
    s "Yeah...that’s a little closer to the truth."
    tk "So...does this mean we’re actually starting now? The first part was just a...warm-up?"
    s "We’re not starting {i}ever.{/i} I can’t do this."
    tk "But you do it for Onee-sama all the time. I watched you. On National Tsukasa Day."
    ch "Is it because we’re too young?"
    tk "I doubt that’s the problem at all, Chinami."

    scene tsukasaarrives28
    play sound "broken.mp3"

    tk "{b}IF ANYTHING, I THINK THAT WOULD MAKE JEEVES WANT TO TEACH US EVEN MORE{/b}"
    ch "{b}ARE YOU SAYING THAT HE LIKES LITTLE GIRLSSSSSSSSSSSS??????????{/b}"
    tk "{b}THAT’S RIGHT, CHINAMI. HE IS LIKELY STRUGGLING RIGHT NOW BECAUSE HE HAS WHAT IS CALLED AN “ERECTION” lol{/b}"

    stop sound

    ch "{b}CHINAMI HAS HEARD ABOUT THOSE! BIG SIS CHIKA GETS ERECTIONS INSIDE HER ALL THE TIME. SHE SAYS THEY MAKE HER insides FEEL GOOOOOOD.{/b}"
    tk "{b}WHENEVER i WANT MY INSIDES TO FEEL GOOD, I SWALLOW THE INK FROM FOUNTAIN PENS!{/b}"
    ch "{b}FOUNTAIN PENSSSSSSSSSSSSSSSS?{/b}"
    tk "{b}AM I DOING IT WRONG, JEEEEEEEEVES?{/b}"
    ch "{b}PAPO! PUT THE ERECTION INSIDE OF TSUKASA TO GET RID OF THE INK!{/b}"
    tk "{b}FIX MY TINY BODY WITH YOUR PENIS, HEEVES!{/b}"

    menu:
        "I’m a bad, bad boy":
            play sound "static.mp3"
            scene tsukasaarrives29 with flash
            stop sound

    tk "Really? So he lives in a pineapple?"
    ch "Under the sea, yeah."
    s "Uh..."

    scene tsukasaarrives30
    with dissolve

    tk "Oh, he’s back again."
    ch "Papa...Chinami’s starting to worry with how your eyes keep going away. So she thinks you should take a nap in big sis Yumi’s futon since she’s not coming home tonight."
    tk "Nonsense, Chinami. Business has only just begun, and Jeeves has yet to teach us anything at all apart from that weird story about those two angels who talk in crossed out letters."
    ch "{s}sssssssssssssssssssssssssssssssssss{/s}"
    tk "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
    s "I..."
    s "Uhh..."

    play sound "static.mp3"
    scene tsukasaarrives31 with flash
    stop sound

    n "So, now that you’re gone, how long do you think it’ll take before Sensei fucks me?"
    m "Probably not {i}that{/i} long. You’ve had your lust stat turned on since you were added to the game so, in a sense, you’ve kind of always {i}almost{/i} been there."
    n "God, I hope so. But between his grief and the fact that Ami might actually kill me if it happens, I’m just not sure if it’s even the right call anymore."

    scene tsukasaarrives32
    with dissolve

    m "Let’s just ask him. When are you going to fuck Noriko? And, if the answer is “no,” is it because I was so good that it ruined sex forever?"
    n "You should just do it right now if you’re going to. I promise that I’m not someone else and that you’re just hallucinating right now."

    play sound "static.mp3"
    scene tsukasaarrives33 with flash
    stop sound

    m "Same here, so do me instead. I promise I won’t tell anyone."

    play sound "static.mp3"
    scene tsukasaarrives34 with flash
    stop sound

    tk "Not so fast, younger version of Maya!"
    m "Crap."
    tk "It is I, Tsukasa Tsukioka, here to verify that I am {i}indeed{/i} still here and that I will {i}not{/i} be having sexual intercourse with you at this point in time!"
    tk "But that I will likely do that if you keep showing me affection because no one else will and it makes me very sad."

    play sound "static.mp3"
    scene tsukasaarrives35 with flash
    stop sound

    ch "Arf arf! Let’s do dog sex!"

    play sound "static.mp3"
    scene tsukasaarrives36 with flash
    stop sound

    tk "..."
    ch "..."
    tk "Jeeves, I think you should probably go home."

    scene black
    stop music

    s "I should never have come in the first place."

    $ renpy.end_replay()
    $ chinamispring2 = True
    $ chinami_love += 10
    $ tsukasa_love += 10

    "{i}Chinami’s affection has increased by 10!{/i}"
    "{i}Tsukasa’s affection has increased by 10!{/i}"
    "{i}iT IS never TOo lATE TO TUrn OFf thE GAMe{/i}"

    scene molech1
    $ renpy.pause(10, hard=True)
    scene molech2
    $ renpy.pause(0.5, hard=True)
    scene black

    "........."
    "......"

    jump amispring1

label chinamispring3:
    scene othersky
    with dissolve2
    play music "blueair.mp3"

    "The sky was upside down when I stepped outside today."
    "You probably can’t tell, but I can."
    "The birds were flying backwards as they tried to catch the bus, and every single parked car made it to its destination long before the ones that drove."
    "You probably don’t know what that means, but I do."
    "I’m the king of everything — with a black paper crown and cuff-links sewn by silkworms in the final days before they slither along to their sideways school on Backwards Boulevard."
    "And when they get there, they’ll think."
    "When they get there, they’ll think — why sleep in cocoons when Heaven’s Web is so much sweeter?"
    "Why drown in the darkness when there’s a room full of white just waiting to be drenched in every color we can pull from the rainbow?"
    "And they’ll think these things not because they’re silkworms, no. They will think these things because their tamer planted thoughts in those tiny silkworm brains. "
    "That was me — the slaver of the silk moth. The one who walks on his hands, opening the blinds at night and stealing money out of cash registers from each and every one of this town’s greengrocers."
    "They’re better than the blue ones."
    "They’re better than the red ones."
    "But they’ll never beat the scent nor sense of soft skin or that first glimpse of a ring in a realm where shapes are secrets, stuffed in the backseat of a car that cannot park."
    "I will never get to where I’m going."
    "I will never be what I’m supposed to be."

    stop music
    scene sky

    "But at least my legs still work."

    play sound "oldphonering.mp3"
    $ renpy.pause(6, hard=True)
    play sound "phonebeep.wav"

    s "Hello?"

    play sound "static.mp3"
    scene gpmx1 with flash
    stop sound
    play music "firstsecondmall.mp3"

    c "i got a new job at the great pareidolia mall"
    s "congratulations chika"
    c "yeah so i need you to go watch chinami"
    c "i know i got kind of crazy the other day and you might feel weird about that or whatever but she has a fever and i don’t want her to die"
    s "neither do i so don’t worry yeah i’ll handle it"
    c "okay awesome and don’t have sex with her either"
    s "but what if the voices in my head want me to"
    c "don’t listen to them lol"
    c "anyway i gotta go "
    c "there’s a hole this one girl wants me to look at or something before my shift starts"
    s "if she tells you she didn’t push her last boyfriend into it she’s telling the truth"
    c "okay"
    s "she really didn’t do it"
    c "okay sensei"
    s "really"
    s "she didn’t"
    c "uh-huh yeah i get it"
    s "okay i love you bye"
    c "i love you too bye"

    stop music
    scene black
    $ renpy.pause(5, hard=True)
    scene chinamifeverwatch1
    with dissolve4
    $ renpy.pause(2, hard=True)
    play music "happyandplotting.mp3"
    $ renpy.pause(4, hard=True)
    scene chinamifeverwatch2
    play sound "pop.mp3"

    s "I’m here and I’m ready to be a good guy."

    "Hello. My name is Akira Arakawa. I have a wife named Chika and a daughter named Chinami."
    "These are not delusions. This is my real life. And these are things I definitely believe because that’s the only thing that makes any of this somewhat acceptable."
    "Today, I will protect my daughter from the sweet release of death."
    "She has an immunodeficiency disorder that really only pops up in random sections of the game, but such is life when you have to split your time between so many vaginas."
    "I mean girls. You can never have too many vaginas."
    "But some vaginas are worse to penis than others. That’s what mall Chika was alluding to in that scene that definitely happened a few seconds ago."
    "So yeah, let’s hope I don’t accidentally get too horny and penis today too."

    stop music
    scene chinamifeverwatch3
    play sound "ohshitpartytime.mp3"
    $ renpy.pause(4, hard=True)
    scene chinamifeverwatch2
    with dissolve

    s "Lucy. I’m hoooooouuuse."

    play sound "static.mp3"
    scene chinamifeverwatch4 with flash
    stop sound
    play music "hometown.mp3"

    "Before me lies one more of God’s unfinished projects. "
    "I won’t bore you with another long-winded rant about how she’s not meant for this place, though. "
    "Such a thing would be depressing. And you already had to sit through whatever the hell was going on inside of my head on the way over, so I imagine you’re already a little exhausted or whatever."
    "And I am too."
    "It’s another one of those days — where I can’t figure out who I am or what I want or who I want or what I am. And it’s on those days where I suffer the most."
    "Yet, it’s somehow not as much as her."
    "I doubt she’ll {i}die.{/i} I mean, she hasn’t {i}so{/i} far. "
    "But there’s always the chance that she {i}could.{/i} "
    "And when I walk out of my house in the morning and glance up at that directionless sky, I can normally convince myself pretty easily that I’m not going to contract pneumonia and abandon this world."

    ch "Nn.......nh........"
    s "..."

    "Her breathing is labored. Her skin glistens in the small bit of light sneaking in through the window. And despite the AC being turned up as high as it will go, just {i}looking{/i} at her makes me feel hot."

    s "..."

    "Maybe a little too hot."

    play sound "static.mp3"
    scene chinamifeverwatch5 with flash
    stop sound

    ch "Nngh! Ackh......mngkh.......agh......."

    scene chinamifeverwatch6
    with dissolve

    ch "Mmf.........mnh........."

    "Stifled coughing — without the head of a dog to mask it this time. "
    "But...what am I supposed to do, exactly?"
    "I told Chika I’d take care of her while she’s at work (I think). But I can’t treat Chinami the way I treat Ami whenever {i}she’s{/i} feeling sick by just crawling into bed and holding her until she’s feeling better."

    s "..."

    "I should replace her towel, at least. Soak it in cold water and wipe the sweat from her- wait. No. That’s too much, isn’t it?"
    "And...am I even sure the water is supposed to be cold? Or is this like eating ramen in the summer to stay cool?"

    s "..."

    "I pull out my phone and begin frantically researching how to care for a sick girl. "
    "I’m probably just overreacting. But...still. It’s possible she caught this from {i}me{/i} the last time I came over, so I don’t want to go and make things even worse."
    "I’ve already given one Chosokabe rabies after all. And if the Internet is correct in telling me I need to make sure Chinami stays hydrated, having her averse to water might become somewhat problematic."

    scene black
    with dissolve2

    "I grab the washcloth off of her pillow and make my way over to the sink."
    "On hotter days, it takes about twenty seconds or so for the water to get cold. I think the pipes in this building might be exposed to the sun or something like that. I don’t know. I’m no plumber."
    "But in those twenty seconds, I have time to think. And even though it’s {i}only{/i} twenty seconds, as I stand there with my hand under that steady stream of water, it feels like an eternity."
    "I think of the first time I met Chinami — how she ran to the living room of that old, crumbling apartment and showed me a picture of her dead mother."
    "I remember thinking in that moment of how desperately I wanted to protect her. To build her a castle. Have her sister be my queen so she can be my princess and {i}I{/i} can be the king."
    "So why?..."
    "Why, as days go by, is that desire to {i}protect{/i} turning to one that makes me fearful of being alone with her?"
    "Is that really who I am?"
    "Have I learned {i}nothing{/i} after all these years? "
    "Or do I look back on the days when I was just as small as her and pretend that things just weren’t all that bad?"
    "Some days, I have an answer. "
    "Some days, I don’t."

    s "..."

    "Ah..."
    "How long has the water been cold?"

    play sound "static.mp3"
    scene chinamifeverwatch7 with flash
    stop sound

    "I picked up a book from a convenience store on the way over. I figured it would help distract me from anything I might do or feel today. Escapism at its finest, I say."
    "I also picked up breakfast. Two croquettes and a red bean bun. "
    "The last time I ate croquettes, I burnt my tongue. So I ate the red bean bun first this time and gave my second course a few minutes to cool off."
    "The result is that my tongue is fine — so now I can bite down on it to try and shock away any impurities that avoid the book and find me in the real world. "
    "It’s been a while since I’ve actually read. Maybe this is me turning the page? Pun somewhat intended. But also not. I want to change."
    "I want to be a better man. "
    "I want to move away from Backwards Boulevard and buy a {i}new{/i} house. Somewhere between Apathy Avenue and Sympathy Street sounds nice."
    "Anywhere I can look outside the window and immediately discern which direction the birds will be flying in today. "

    ch "Mm..."

    "A man can dream, I suppose."

    scene chinamifeverwatch8
    with dissolve2

    ch "Mnh..."

    "A man {i}has{/i} to dream. Because man is evil. Man is impure. Man is the culmination of instinct and desire and fury and spite all balled into a single, black orb that could consume the world if left alone."
    "And with that in mind, it’s no wonder that God Himself is the complete opposite. "

    scene chinamifeverwatch9
    with dissolve2

    ch "..."
    ch "Papa?..."

    scene chinamifeverwatch10
    with dissolve

    s "Oh, you’re awake."
    s "Congratulations on still being alive."
    ch "What are you doing here?..."
    s "Your sister called me. She had to go to work and wanted me to look after you."
    ch "So...does that mean you’ll be taking care of Chinami today?..."
    s "I guess so."

    scene chinamifeverwatch11
    with dissolve

    ch "Yay! That means we can play games!"
    s "No. It means you can lie there and rest because that’s what the Internet says you’re supposed to be doing right now."

    scene chinamifeverwatch12
    with dissolve

    ch "Rats..."
    ch "Chinami would hate the Internet if it wasn’t full of valuable stock tips and pictures of dogs."
    s "Do you need anything? Water? Food? I can order, like...what do sick people normally eat? Soup?"

    scene chinamifeverwatch13
    with dissolve

    ch "Peanuts."
    s "Are you {i}trying{/i} to get me to kill you?"

    scene chinamifeverwatch14
    with dissolve

    ch "No. Chinami just wanted to see if you remembered her weakness. "
    ch "She’s thankful she has such a caring Papa who keeps track of her allergies and plays games with her when she’s sick."
    s "No games. Go back to sleep. "
    ch "But Chinami isn’t tired anymore. She’s super excited that her daddy came over to play this time and not fight with anybody."
    s "..."
    ch "Can you make Chinami pancakes?"
    s "As a matter of fact, I can. I learned how to do that when my {i}other{/i} daughter was...sick."

    scene chinamifeverwatch15
    with dissolve

    ch "Yaaaay! Chinami gets to-"

    scene chinamifeverwatch16
    with hpunch

    ch "OTHER DAUGHTER?!?!?!"

    play sound "static.mp3"
    scene chinamifeverwatch17 with flash
    stop sound

    ch "What other daughter?! Is this why big sis Chika was mad and scary the last time you came over?! Does Chinami have a half-sister now?! Does-"

    play sound "static.mp3"
    scene chinamifeverwatch18 with flash
    stop sound

    ch "Ackh!!! Ackkhk...mmnfhck...ackhhh!!!!"
    s "Chinami, take it easy. I’m pretty sure you’re not supposed to be yelling like that when you’re sick."

    scene chinamifeverwatch19
    with dissolve

    ch "Of course Chinami is going to yell if you’re going to drop a bomb on her like that! She never even got to hold the baby!"
    s "I’m not talking about an {i}actual{/i} daughter. I’ve just started calling my niece that since it’s been just me and her for over half of her life now."

    scene chinamifeverwatch20
    with dissolve

    ch "Niece? You mean the one big sis Chika says is evil all the time?"
    s "That sounds about right, yeah. "
    ch "So...Chinami doesn’t have a new sister?"
    s "Nope. So Chinami doesn’t have to worry about someone else taking up even more of my time. "
    ch "That’s good news, Papa. But it would be better news if you could start coming more often again. Big sis Chika’s been kind of scary lately."
    s "Yeah...but hopefully, she and I can...figure that out or something since it’s basically all my fault."
    ch "Blah, blah, blah. Chinami doesn’t care about that stuff. Chinami wants pancakes now that her Papa knows how to make them. And Chinami will grade them very harshly."
    s "Technically, I never said I {i}would{/i} make you pancakes. Just that I {i}can.{/i}"
    ch "While Chinami understands that you may fear her grading criteria, she would like to inform you that {i}not{/i} making her pancakes could lead to great regret as Chinami could die at any moment."
    s "Don’t leverage your illness against me for pancakes, Chinami."

    scene chinamifeverwatch21
    with dissolve

    ch "What good is Chinami’s fragile body if she can’t even use it for sweets?!"
    s "I’m sorry. But the Internet says-"

    scene chinamifeverwatch22
    with dissolve

    ch "Chinami knows what the Internet says. Big sis Chika makes Chinami eat healthy food when Chinami is sick too. But Papa is irresponsible so Chinami thought Papa would be different."
    s "I can order you soup. I have, regretfully, not learned how to make that yet."

    play sound "static.mp3"
    scene chinamifeverwatch23 with flash
    stop sound

    w "How hot do we make it? Is it possible to burn soup?"

    play sound "static.mp3"
    scene chinamifeverwatch24 with flash
    stop sound

    s "And I likely never will..."
    ch "Okay. Chinami will eat Papa’s special delivery soup. But she wants to take a bath first since she’s all sweaty."
    s "Great. Do you need me to warm it up for you or do you know how to do that yourself?"

    scene chinamifeverwatch25
    with dissolve

    ch "Chinami knows how. She can do it."
    s "Okay. I’ll place an order now, then. And hopefully, by the time you’re done, it’ll be here."
    ch "Is Papa not coming into the bath with Chinami?"
    s "Absolutely not."

    if sawchinami == True:
        ch "But he’s already done it before."
        s "He certainly has not. "
        ch "He sure has. Him, big sis Chika, and Chinami all took a bath together in Chinami’s old apartment."
        s "Yeah, I don’t think you’re remembering that event correctly. I kind of just walked in and then felt really weird."
        ch "Why?"
        s "Because it’s not normal for grown men to be in the bathroom with little girls."
        ch "Why?"
        s "Many reasons, Chinami. "
        ch "Why?"
        s "Do you think you can just keep asking “why?” until I agree?"
    else:
        s "Because it’s not normal for grown men to be in the bathroom with little girls."
        ch "Why?"
        s "Many reasons, Chinami. "
        ch "Why?"
        s "Do you think you can just keep asking “why?” until I agree?"

    ch "Chinami’s just worried that she’ll fall and crack her head open and bleed everywhere and die. Or that she’ll faint in the bathtub and drown and never get to eat Papa’s special soup."
    s "Chinami needs to stop being so morbid."
    ch "Big sis Chika always gets in the bath with Chinami when Chinami is sick."
    s "She’s your sister. I’m some random guy she’s “dating.”"
    ch "No, you’re my Papa."
    s "That’s what you call me, sure. That’s not what I actually {i}am,{/i} though."
    ch "But that’s what you are to {i}me.{/i} I mean...Chinami."
    s "..."

    scene chinamifeverwatch26
    with dissolve

    ch "Pleeeeeeease, Papa? Chinami’s arms don’t bend back the way they’re supposed to and she has a hard time reaching everywhere. She needs your help or she will die."
    s "..."
    ch "Pleeeeeeeease?..."

    if sawchinami == True and tsukasachosen == True and tsukasarefused == False:
        s "Chinami...that’s a bad idea."
        ch "Chinami doesn’t think so. Chinami thinks-"
        s "Chinami is wrong. "

        scene chinamifeverwatch27
        with dissolve

        ch "..."
        s "Chinami doesn’t understand what she’s asking. She doesn’t understand {i}who{/i} she’s asking."
        s "If I was actually your dad...sure. Whatever. It’d be weird, but it wouldn’t be {i}as{/i} weird as it is with me being...{i}me.{/i}"
        ch "But you’re just Papa. You’re-"
        s "I’m not “just” anything. I’m the amalgamation of all that’s wrong with man. I’m a self-made victim of circumstance and a prisoner in my own mind and body. "
        s "But more than that, I’m a virus that would surely kill you if the right...precautions aren’t taken."
        ch "Chinami is confused by basically everything Papa just said. Are you saying you want to kill Chinami?"
        s "Of course I don’t {i}want{/i} to. That’s just..."
        s "I’m afraid that’s what would happen. And I want to {i}protect{/i} you. Which sometimes means...keeping my distance."

        scene chinamifeverwatch28
        with dissolve2

        ch "Chinami trusts you, Papa. "
        s "She shouldn’t."
        ch "But she does."
        s "..."
        ch "So she’ll ask you one more time, then leave you alone if you still say no."
        s "..."
        ch "Will you come with Chinami?"

        menu:
            "Endanger her":
                s "..."
                ch "..."
                s "Fine."

                scene chinamifeverwatch30
                with dissolve

                ch "Yay! Chinami’s persuasion skill has improved! Now, she just needs to figure out how to convince Papa to make her pancakes."
                s "It’s actually disgusting that it was easier to convince me to do {i}this{/i} than that."

                scene chinamifeverwatch31
                with dissolve

                ch "Papa’s being too hard on himself again. Chinami is sure that everything is going to be fine. And now, she’ll be extra clean too!"
                s "..."

                scene black
                with dissolve2
                play sound "tackle.mp3"

                ch "Come on, Papa! Chinami will show you how to work the bath for when you move in with us."
                s "..."

                "This is normal."

                play sound "static.mp3"
                scene imissyou12 with flash
                stop sound

                "{i}I{/i} am normal."

                play sound "static.mp3"
                scene tsukasaapt17 with flash
                stop sound

                "No. I’m {i}not{/i} normal. I am {i}anything{/i} but normal."

                play sound "static.mp3"
                scene utaparkscene25 with flash
                stop sound

                "But {i}this{/i} time, I am. And it doesn’t matter what I’ve done in the past so long as- no, wait. It {i}does{/i} matter what I’ve done in the past. But if I’m trying to get better, I-"

                play sound "static.mp3"
                scene tsukasakura19 with flash
                stop sound

                "I..."
                "Uhh..."
                "Right! If I’m trying to get better, I have to {b}CONFRONT{/b} these feelings! Running away is {b}BAD.{/b}"

                stop music
                play sound "static.mp3"
                scene 3 with flash
                scene 2 with flash
                scene 1 with flash
                scene blood3 with flash
                stop sound
                "{b}I MUST BE A GOOD BOY.{/b}"

                $ renpy.end_replay()
                $ chinamispring3 = True
                $ chinami_love += 1
                $ chikablock = False

                jump chinamispring4

            "Protect her":
                s "..."
                ch "..."
                s "I’m sorry. I just...really shouldn’t."

                scene chinamifeverwatch29
                with dissolve

                ch "Fiiiiine. But if Chinami dies, her ghost will never forgive you!"
                s "It’ll have to get in line."

                scene black
                with dissolve2
                stop music fadeout 10.0

                s "I’m already being haunted."

                "{i}You refuse to give into temptation!{/i}"
                "{i}You’re such a good guy and everyone’s really proud of you!{/i}"
                "{i}But in another life, you’re making the opposite choice.{/i}"
                "{i}In another life, you’re not afraid of LINES. You’re not afraid of WHAT ISN’T REAL.{/i}"
                "{i}In that life, you’re strong. You’re brave. You’re human! And you can face your fears without worry that your weakness will amplify them!{/i}"
                "{i}In that world, you can see things for what they are, not what they represent. And you can live freely, unburdened by the unfortunate truth that, in this world...you’re a coward.{/i}"
                "{i}You’re a creep.{/i}"
                "{i}You hate the way these lines make you feel because you haven’t figured out how to separate them yet.{/i}"
                "{i}In the dark, another string snaps. And while you pat yourself on the back for a job well done, know this-{/i}"
                "{i}Everyone else is growing.{/i}"
                "{i}And you’ll never catch up at this rate.{/i}"

                play sound "computerboo.mp3"

                "{i}Chinami enjoys the soup!{/i}"

                $ renpy.end_replay()
                $ chinamispring3 = True
                $ chinamirefused = True
                $ chinamispring4miss = True
                $ chinami_love += 1
                $ chikablock = False

                "{i}Her affection has increased to [chinami_love]!{/i}"
                "........."
                "......"
                "..."

                if day >= 6:
                    jump endofsatch4
                else:
                    jump endofweekdaych4

    else:
        s "Absolutely fucking not. Now go take a shower so I can order your food."

        scene chinamifeverwatch32
        with dissolve

        ch "Waaaaaaaah! Chinami’s Papa won’t even wash her back! Chinami will never experience real love! And at this rate, she’ll probably never even get to grow up before-"

        play sound "static.mp3"
        scene chinamifeverwatch18 with flash
        stop sound

        ch "Ackhkk! Akckk.....hckghgh.....ahgkckhck!"

        scene black
        with dissolve2
        stop music fadeout 10.0

        s "{i}Hah...{/i}"
        s "Just tell me what kind of soup you want..."

        "Chinami leaves and takes a bath on her own."
        "I’m safer here. She’s safer there."
        "And if I can keep doing this, I can..."
        "..."
        "If you’d have told me when I was younger that it’s possible to rewrite the past, I’m not sure how I would have reacted."
        "But now that I know that you {i}can,{/i} it’s almost all I think about."
        "..."
        "There are some dishes left in the sink that I decide to take care of while waiting for Chinami to finish up."
        "The water is the perfect temperature as soon as I turn the faucet on."
        "I manage to avoid thinking entirely."

        $ renpy.end_replay()
        $ chinamispring3 = True
        $ chinamispring4miss = True
        $ chinamirefused = True
        $ chinami_love += 1
        $ chikablock = False

        "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
        "{i}Chika returns home a short while later.{/i}"
        "{i}She looks like she fell through a hole.{/i}"

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4

label chinamispring4:
    play sound "static.mp3"
    scene senseichinamibathtime1 with flash
    stop sound
    play music "snowchildren.mp3"

    "Here I sit in shrink wrap, left alone to rot. To suffocate and die before I’m stuffed into a pot."
    "Today, my bones will be the soup. My skin will be the broth. My hair will be the garnish and my cum will be the froth-"
    "That coats the throats of goats and lambs, they’ll feed me to the farm. But I’ve yet to please the FDA, so there’s a chance I might bring harm-"
    "Disease/a plague/a parasite - the maddest of all cows. Never once have I been human, never once have I been proud."
    "To be what she has made of me. Ingredients, at best. A specimen — this mess I’m in won’t ever let me rest."
    "Howdy."
    "You’ll never guess where I am right now."

    stop music
    scene senseichinamibathtime2
    play sound "water1.mp3"

    ch "Papa?"

    play sound "static.mp3"
    scene senseichinamibathtime3 with flash
    stop sound
    play music "hometown.mp3"

    ch "Aren’t you going to come into the bath with Chinami?"
    s "No."
    ch "Why?"
    s "Because this is already a step further than I planned on going today."
    s "Several steps, actually. So you’ll just have to deal with me looking away until you’re ready to come out."
    ch "But Chinami’s arms! They’re not bendy enough! "
    s "Then neither are mine."

    "We’re here. And I haven’t done anything wrong. At least not yet."
    "But the fact that I {i}am{/i} here means that I {i}could.{/i} That I {i}might.{/i} That I {i}want{/i} to. But I don’t {i}want{/i} to {i}want{/i} to. So I {i}want{/i} to stop wanting that."
    "What {i}I{/i} want rarely seems to matter at all anymore, though. At least not when there are creatures who do and don’t exist pulling me into places where they know that I’ll get lost."
    "This is one of those places — a battle I’ve already returned from once. But it feels more like a suicide mission when I need to face it alone this time."
    "It’s innocent enough. And for anyone worth more than me, I’m sure it would be fine. It’d be like being sent out to take down a single spider with a barrel full of dynamite. "
    "But someone lit my hands on fire a long, long time ago. And now I can’t carry anything without the risk of burning or igniting it."

    scene senseichinamibathtime4
    with dissolve

    ch "..."
    s "..."
    ch "Is Papa only uncomfortable because Chinami is a girl?"
    s "One day, Chinami’s going to stop asking questions I don’t know how to answer without incriminating myself."
    ch "She probably won’t. Chinami is a curious girl. There are all sorts of things she wants to learn more about."
    s "One day, Chinami will {i}also{/i} stop saying things that incriminate {i}her.{/i}"
    ch "Is it wrong for Chinami to think about love sometimes?"

    play sound "static.mp3"
    scene senseichinamibathtime5 with flash
    stop sound

    s "What?"
    ch "That’s what Papa was fighting about with Chinami’s big sisters, wasn’t it?"
    ch "Big sis Chika has been talking in her sleep again. She says that you love more than one person. Was she mad because you love big sis Yumi too?"
    s "I don’t {i}love{/i} Yumi."
    ch "You just want to do naughty stuff with her then?"
    s "Wha- why is that a thing you even know about?"

    scene senseichinamibathtime6
    with dissolve

    ch "Chinami watched Game of Thrones, remember? And even if big sis Chika closed her eyes for the naughty parts, Chinami knows they exist. "
    ch "Has Papa been doing naughty things with big sis Yumi?"
    s "{i}No.{/i} Now, change the subject."
    ch "But he’s been doing naughty things with big sis Chika, right?"

    play sound "static.mp3"
    scene senseichinamibathtime7 with flash
    stop sound

    s "I can’t talk about this with you."
    ch "Why?"
    s "Because you’re too young. And your sister would kill me."
    ch "I don’t think she would, Papa. People are allowed to do naughty things together when they love each other. "
    ch "And since you love big sis Chika, Chinami is okay with you doing as many naughty things as you like!"
    s "Shut up..."
    ch "But she doesn’t really understand how those naughty things work yet since her eyes are always closed. So she hopes that someone will-"

    scene senseichinamibathtime8
    with dissolve

    s "Shut up!"

    play sound "static.mp3"
    scene senseichinamibathtime6 with flash
    stop sound

    ch "Oh no! Talking about naughty stuff made Papa mad at Chinami again!"

    scene senseichinamibathtime9
    with dissolve

    ch "Chinami is sorry. She just wants to understand and all of this stuff is super confusing to her."
    s "I’m not...{i}mad.{/i} You don’t know any better yet. But if this is something you really want to learn about, you should talk to your sister. Not me."
    ch "But if Chinami talks to big sis Chika about that, she’ll get sad that Chinami is growing up. So Chinami needs to stay Chinami. That’s what’s best for everyone right now."
    s "Yeah well, Chinami’s clearly not smart enough to know what’s best for {i}anyone{/i} right now if she’s going to put herself into situations like this."

    scene senseichinamibathtime10
    with dissolve

    ch "Does Papa think Chinami has ulterior motives?"
    s "He thinks Chinami should stop referring to herself in third person before bringing up serious topics like this."
    ch "Chinami will do that so long as Papa promises to keep it a secret."
    s "Yeah, whatever. This whole {i}day{/i} should be kept a secret as far as I’m concerned."

    play sound "static.mp3"
    scene senseichinamibathtime11 with flash
    stop sound

    ch "Which sister do you like more then? Is onee-chan right that she’s winning? Or do you like delinquent girls like Yumi more?"

    scene senseichinamibathtime12
    with dissolve

    ch "Or maybe {i}I’m{/i} your type and that’s why you’re afraid to get in the bath with me."
    s "If I had to choose between all three of you...Chika would come out on top."

    scene senseichinamibathtime13
    with dissolve

    ch "Mm. That’s the right answer. She loves you the most, after all."
    ch "But Chinami doesn’t-"
    s "You’re doing it again."
    ch "Oh. Sorry. Habit."

    scene senseichinamibathtime14
    with dissolve

    ch "What I don’t understand is why onee-chan would be so sad if you loved Yumi the way you love her."
    s "How is that a thing you’re confused about? You watch TV. You play games. You practically live on your phone. I’m sure you know {i}all{/i} about the conventional definition of “love” by now."
    ch "But there’s conflicting information everywhere, Papa! Everybody has an opinion on what kind of love is “wrong” and what kind of love is “right.” "
    ch "And that’s the part that’s confusing to me because I’m hearing from the same people who say those things that love is different for everyone. So why do some people get to choose what’s wrong?"
    ch "Like...maybe relationships are just all about two people with the same definition of love finding each other? Does that make any sense?"
    s "I think you just answered your own question."

    scene senseichinamibathtime15
    with dissolve

    ch "Hm?"
    s "Your sister’s upset because she believed we had the same definition. And I told her the last time I came over that we didn’t."

    scene senseichinamibathtime16
    with dissolve

    ch "Oohhhhhhh, okay. I think I get it now. You’re like Jaime Lannister. And Chika is Cersei Lannister and Yumi is Brienne of Tarth."
    s "I have no idea what you just said."

    scene senseichinamibathtime17
    with dissolve

    ch "Cersei and Brienne both love Jaime and Jaime loves both of them, but his love for Cersei outweighs his feelings for Brienne, so he always goes back to {i}her.{/i} "
    ch "But then that makes {i}Brienne{/i} sad because she never gets a chance to act on her feelings — which leaves {i}Jaime{/i} with the feeling of longing until-"
    ch "Are you going to watch it? Because I don’t want to spoil what happens if you’re going to watch it."
    s "Probably not, Chinami. "
    ch "I’m not gonna spoil it anyway just to be safe. Chika says spoilers are bad. But the gist is that love triangles always make somebody upset and you’re the tip of your own triangle."
    s "That’s fair. I should just probably also mention that triangle is situated neatly inside a shape with so many sides that I’m not even sure if there’s a name for it."
    ch "Then, is Chika winning {i}that{/i} competition too? Or just the tinier triangle with her and Yumi in it?"
    s "..."

    scene senseichinamibathtime18
    with dissolve

    ch "Chinami won’t tell on you if that’s what you’re worried about. She’s an expert at gossip now."
    s "But clearly not an expert at maintaining a regular speech pattern."

    scene senseichinamibathtime19
    with dissolve

    ch "Okay, {i}you{/i} try spending your entire life talking in third person and then having to switch for an entire conversation. It’s harder than it sounds, Papa."
    s "Can you call me Akira instead? That’s my actual name."

    scene senseichinamibathtime20
    with dissolve

    ch "No."
    s "That was a pretty instantaneous rejection. May I ask {i}why?{/i}"
    ch "How come you’re allowed to ask “why?” but I get in trouble whenever I do it?"
    s "Because I do it when I genuinely want to know something and you do it for the sole purpose of annoying me."

    scene senseichinamibathtime21
    with dissolve

    ch "That’s what daughters are for! Probably. I’ve never had a dad, so I don’t really know."
    s "You’re a weird girl, Chinami. But surprisingly bearable when you’re not persuading me to do things I’m uncomfortable with."

    scene senseichinamibathtime22
    with dissolve

    ch "Thank you! Does that mean you’ll get in the bath with me now? "
    s "Did you listen to my last sentence at all? Or did you just stop after the part where I called you bearable?"
    ch "I was listening. I just think you’re making too big of a deal out of being uncomfortable and I want help washing my hair."
    s "I’m in my 30’s. I’m not getting into the bath with a little girl no matter {i}how{/i} much she wants me to."

    scene senseichinamibathtime23
    with dissolve

    ch "Then Chinami will just assume that Papa is a lolicon and that he wants to do naughty things to her while her sister is away at work. Papa is a bad boy."
    s "..."

    scene senseichinamibathtime24
    with dissolve

    ch "Kidding."
    s "..."

    scene senseichinamibathtime25
    with dissolve

    ch "Wow. You really {i}are{/i} uncomfortable, aren’t you?"
    s "I’m not proud of it, Chinami. "
    s "I don’t want to be like this."

    scene senseichinamibathtime26
    with dissolve

    ch "Then Chinami will switch back to {i}regular{/i} Chinami so it’s easier for Papa to remember his role as Papa and not her sister’s lolicon boyfriend!"
    s "Where did you even learn that word?"
    ch "Big sis Yumi accidentally taught Chinami {i}lots{/i} of bad words. But Chinami isn’t going to use them right now because Papa’s in a pickle!"
    s "I think I’m going to head back out into the living room now."
    ch "No! Papa is going to wash Chinami’s hair because Chinami is sick and he needs to do what she commands of him."
    s "I’m not getting into the bath with you. It’s not happening."

    scene senseichinamibathtime27
    with dissolve

    ch "Then stay out there."
    ch "Chinami will come close to you."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene senseichinamibathtime28
    with dissolve

    ch "Nihihihi~"
    ch "Chinami knew it was only a matter of time until Papa caved. Now, she gets to enjoy a nice scalp massage while he fights his inner demons!"
    s "Right now, those demons are telling me to drown you in the bathtub."
    ch "But then you’d never get to see the grown up Chinami who won’t make you feel bad for wanting to do naughty things."
    s "You’d still be my “girlfriend’s” sister either way. Which means that any feelings I {i}ever{/i} have involving you won’t be good ones."

    scene senseichinamibathtime29
    with dissolve

    ch "Does that mean you’ll be my Papa forever, then?"
    s "..."
    ch "That’s what it means if you’re still with big sis Chika many years from now, right?"
    s "..."
    ch "Will Papa get jealous if Chinami ever gets a boyfriend?"
    ch "Will he try to scare them away in order to protect her?"
    ch "Or will Chinami have to stay single forever so Papa won’t be sad?"
    s "Don’t look up at me like that, please."
    ch "Why not? I’m having a cute moment with my daddy. It’s not {i}my{/i} fault he’s a lolicon."
    s "Well, you’re certainly not helping."
    ch "Is there any way Chinami {i}can{/i} help?"
    s "Yes. By not capitalizing on my weaknesses and coercing me into doing things like this."
    ch "Chinami learned from her friend Tsukasa that capitalizing on someone’s weakness is the quickest way to get what you want."
    s "I knew that girl was going to be a bad influence on you."

    scene senseichinamibathtime28
    with dissolve

    ch "Maybe next time, all three of us can take a bath together and {i}really{/i} put Papa in a tight spot!"

    play sound "slidedoor.mp3"

    s "Now I {i}really{/i} want to drown you."
    c "Chinamiiii!~ I’m home early!~"

    scene senseichinamibathtime30
    with fade

    c "Oh. You’re-"
    ch "Welcome home, big sis Chika!"

    scene senseichinamibathtime31
    with dissolve

    c "Are you..."
    c "What are you doing?"
    s "I..."
    c "Are you...washing her hair?"
    s "She made me do it. I tried to stay out there. But she just kept-"

    scene senseichinamibathtime32
    with hpunch

    c "KYAAAAAAAAH! OHMYGOD! THIS IS THE CUTEST THING I’VE EVER SEEN IN MY LIFE! IT’S LIKE WE’RE AN ACTUAL FAMILY! OHMYGOD OHMYGOD OHMYGOD!"
    s "Uhh..."

    play sound "slidedoor.mp3"
    scene senseichinamibathtime33
    with dissolve

    c "LET ME GRAB A CHANGE OF CLOTHES AND I’LL GET IN THE BATH TOO! OHMYGOD! I’M SO IN LOVE!"
    s "..."
    ch "..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    ch "Do you think big sis Chika is a lolicon too?"
    s "I think you should never repeat that word in front of her for as long as you live."

    "I bail out before Chika makes it into the bathroom again."
    "Just being in there with Chinami was hard enough. And knowing who I am, I...I’m not sure if I’d be able to handle {i}both{/i} of them at once."
    "Regardless, it seems like my job here is done."
    "Chinami will survive for at least one more day."
    "And I-"
    "..."
    "And I will go to sleep undeserving of the same."

    $ renpy.end_replay()
    $ chinamispring4 = True
    $ chinami_love += 1
    $ chika_love += 1

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chinamispring5:
    if _in_replay:
        play music "hometown.mp3"

    scene chinamiconfronts1
    with dissolve2

    "Fresh off the boat that carried her through seas of somewhat mandatory midday misery, Chinami Chosokabe eventually returns to her apartment to find her “Papa” wearing clothes."
    "This was good news. For after the “break” her friend mentioned at the end of the preceding event, there were at least five other bouts of what could only be described as “obnoxious sexual rampage.”"
    "It appeared that the rampage had ended, thankfully. But the sadness had not. "
    "There were other feelings as well. Confusion, mostly. The sorts of feelings {i}anyone{/i} would get after watching a little sister take LOADS of cum from the hung guy and his MASSIVE cock for the first time."
    "But those would fade in time, and the worry of what might soon happen to her friend would not."

    s "Oh...hi."
    ch "Chinami is very disappointed in you, Papa. You have defiled her home."
    s "...What?"
    ch "{i}You know what you did.{/i}"

    scene chinamiconfronts2
    with dissolve

    s "Well...at least now I know how thin the walls are."
    s "I’m sorry you had to hear that. I needed to repair your sister. Please ignore and forget all of it."
    ch "Chinami isn’t sure she can. Your actions have caused irreparable damage to her developing mind. You should be ashamed of yourself, Papa."
    s "Well, I’ve got great news for you then, Chinami. Because my shame is already infinite and being scolded by a wizard will do nothing but remind me of the walking sin that I have become."
    ch "Where’s big sis Chika? Did you fuck her into oblivion?"

    scene chinamiconfronts3
    with dissolve

    s "Woah. Okay. No more of that. Your sister will kill me if she hears you use that word."
    s "In fact, your sister will kill me if she hears you even mention that you {i}heard{/i} anything. So just do us both a favor and repeat this to no one. "
    ch "It’s big sis Chika’s fault in the first place, Papa. She’s the one who was loud. I heard that word from her while the two of you were {i}studying{/i} in here."
    s "Still, I’d prefer it if you-"

    play sound "static.mp3"
    scene chinamiconfronts4 with flash
    stop sound

    ch "And {i}Chinami{/i} would prefer it if the two of you didn’t lie to her just so you could spend time together. Chinami would have given you space if you asked. "
    s "{i}Where?{/i} You can’t go anywhere other than Tsukasa’s and that clearly didn’t help at all."
    ch "Chinami would hide in the bathroom and put loud music on instead. "
    s "Could you {i}not{/i} put loud music on at Tsukasa’s place?"

    scene chinamiconfronts5
    with dissolve

    ch "Chinami wanted to, but Tsukasa wouldn’t let her! She kept listening to you two the whole time and I just had to sit there and hold my ears closed!"
    s "Wow, this hole just keeps getting bigger. I might not even be able to climb out at this point."
    ch "Papa {i}made{/i} this hole when he did it with a girl in Tsukasa’s room!"

    scene chinamiconfronts6
    with dissolve

    s "Yup. I’m stuck here forever now. Should’ve just made Chika come to me instead."
    ch "Let the record show that Chinami is not upset about what you did today. She’s just angry that she was lied to and very confused about what happened at Tsukasa’s house."
    s "Good. You {i}should{/i} be. But that doesn’t mean I’m going to talk about it with you. Which is why you should drop it and just stay uninvolved."
    s "I’ll be more careful with Chika in the future so you don’t have to hear it anymore. And frankly, I’m surprised she wanted to do that stuff {i}here{/i} to begin with {i}because{/i} of you."
    ch "Chinami doesn’t want to be a burden like that."
    s "You just {i}existing{/i} is not burdensome, Chinami. You haven’t done anything wrong. "

    scene chinamiconfronts7
    with dissolve

    ch "Chinami never does anything wrong. It’s her job to make life easier for Big Sis Chika. Which is why she talks to you about this stuff instead of her."
    s "Yeah, well I wish you wouldn’t talk to {i}me{/i} about it either."
    ch "That leaves Chinami with nobody then."

    scene chinamiconfronts8
    with dissolve

    ch "She can’t talk to big sis Chika because she’ll get worried. And she can’t talk to {i}Papa{/i} cause he’ll get {i}sad.{/i} So what’s she supposed to do then? Never learn anything?"
    s "You’re supposed to {i}wait.{/i} You’re not ready to talk about any of this stuff yet, Chinami. "

    scene chinamiconfronts9
    with dissolve2

    ch "But Tsukasa {i}is?{/i}"
    s "..."
    ch "She never talked about any of that adult stuff until she saw you do it...and {i}now,{/i} she won’t shut up about it. "
    ch "Doesn’t that make it {i}your{/i} fault, Papa?..."
    s "..."

    scene chinamiconfronts10
    with dissolve

    ch "Big sis Chika too! She {i}never{/i} lied to Chinami before she met you! Now she does it just so she can have fun for a little while!"
    ch "And Chinami understands that big sis Chika is growing up. She understands that she’d have to be lied to eventually. She doesn’t care about that."
    ch "She just doesn’t understand why everyone starts going crazy once they meet {i}you.{/i} You’re just a normal boy."
    s "I am {i}far{/i} from normal, Chinami. That’s why I keep breaking everyone close to you."
    ch "Is it really “breaking” them if {i}you’re{/i} not the one hurting them, though?"

    scene chinamiconfronts11
    with dissolve

    s "Of course I’m the one hurting them. You’ve seen what’s happened to Chika ever since she started dating me. Everything just makes her sad now because I’m not as...{i}loyal{/i} as she wants me to be."
    ch "I don’t know, Papa. Cause Chinami doesn’t know a lot about adult stuff, but she can definitely say that it didn’t sound like big sis Chika was {i}hurting{/i} in here."
    s "That’s different, Chinami. It’s a lot easier to make someone feel good physically than it is mentally. I excel at that first part. I’m utterly horrible at the second."
    ch "Papa makes Chinami feel good mentally all the time, though. And the way big sis Chika smiles when you’re coming over makes me think you do that for her too..."
    s "Where’s this even going, Chinami? What do you {i}want?{/i} Because if you’re just desperate to learn about sex, you have access to the Internet. And {i}no,{/i} that’s not an endorsement. "

    scene chinamiconfronts12
    with dissolve

    ch "Chinami...doesn’t really know yet. "
    ch "She feels sad about a lot of things right now, but doesn’t fully understand why. It’s new...and weird."
    s "Welcome to the club. We’re all miserable about something. And I know {i}I’ve{/i} been struggling to explain how I feel since before I was even your age."
    ch "You learned about all this adult stuff before you were Chinami’s age?"
    s "...Yeah."
    s "Something like that."
    ch "..."
    s "Now, are we done? Because I’d like you to go back to being the one girl that I can just entirely avoid this subject with."

    play sound "slidedoor.mp3"

    ch "Chinami doesn’t know if that’s possible anymore, Papa..."
    c "Wha- Chinami?!"

    play sound "static.mp3"
    scene chinamiconfronts13 with flash
    stop sound

    c "What are you doing here? You’re supposed to be at Tsukasa’s."
    ch "Chinami came back when the noise stopped. She didn’t want to watch the same movies Tsukasa was."
    c "Noise? What noise? There was no noise. We were just studying."
    ch "Then why are big sis Chika’s legs shaking so much?"

    scene chinamiconfronts14
    with dissolve

    c "Because she loves to learn and there is only so much knowledge this body can hold!"
    s "It might be time to look into soundproofing if you want to be reckless again in the future, Chika."

    scene chinamiconfronts15
    with dissolve

    c "I...uh...no! Tsukasa’s the rich one! She can soundproof her {i}own{/i} room if she thinks she’s hearing things in there! Which she isn’t because nothing happened."

    scene chinamiconfronts16
    with dissolve

    c "A-Anyway! Do you need something? I have to leave for work in twenty minutes, but I can make you some instant ramen if you’re hungry and-"
    ch "No thank you! Chinami will wait for Papa to buy her the fancy dinner he promised as thanks for being good and giving you two alone time."

    scene chinamiconfronts17
    with dissolve

    c "Wait, Sensei — you did that for us? Really? That’s so sweet."
    s "Yes. I did this for us and Chinami is not subtly blackmailing me right now."

    scene chinamiconfronts18
    with dissolve

    c "Awwww! So you two are gonna hang out here while I’m at work? Have a cute little daddy-daughter dinner?"
    ch "Yup! That’s the plan! Chinami’s so excited to spend the night with her papa! "
    s "Can’t wait. It’ll be a blast."
    c "You two are so cute..."

    scene black
    with dissolve2

    c "I can’t believe I doubted anything for even a second..."

    play sound "static.mp3"
    scene chinamiconfronts19 with flash
    stop sound

    "Chinami and I are left alone again when Chika leaves for work. And since I planned on spending the rest of the day here once I started heading over, I’m not {i}too{/i} beaten up about this."
    "Sure, the amount of sex I have will exponentially decrease and reach nowhere remotely close to the sum total of all the sex ever, but it’s less travel and easier on my feet."
    "I just {i}now{/i} have to figure out what to do about the demon gazing up at me and trying to figure out the best way to make me uncomfortable next."

    ch "So! What’s Papa buying for Chinami? She wants to try eel."
    s "I think Chika mentioned something about there being instant ramen here. I’ll just start boiling some water and-"

    scene chinamiconfronts20
    with dissolve

    ch "Boy! Chinami sure is excited for her daddy-daughter dinner! "
    ch "It’s the one thing that will help her forget about everything that happened in this room today so she won’t blab to her big sister about it once Papa is gone!"
    s "You continue to be the most evil person I have ever met. "

    scene chinamiconfronts21
    with dissolve

    ch "Then Chinami must take after you! There aren’t many people so evil that they’d have an affair in a little girl’s room after all."
    s "Chinami-"
    ch "Why did you do it? Why Tsukasa?"
    s "..."
    ch "Do you {i}love{/i} her? The same way you love big sis Chika and all of the other girls Chinami always hears her complain about?"
    s "Of course I don’t {i}love{/i} her...that’s ridiculous."
    s "I was just..."
    s "I wasn’t in the right state of mind that night. I was self-destructing and...she was the most helpless thing I could find."

    scene chinamiconfronts22
    with dissolve

    ch "You...wanted to take her down {i}with{/i} you then?"
    s "No...it’s not like that either. I don’t...really {i}know{/i} how to describe it. {i}Why{/i} I did what I did. None of it makes any sense."
    ch "Chinami’s helpless too, though. And the only time you’ve done adult stuff near her, you made her leave the room."
    s "Technically, your sister made you leave the room."
    ch "So Papa would have let Chinami stay if the choice was his?"
    s "Well..."
    s "No. Probably not."
    s "I probably would have asked you to leave as well. "
    s "But you weren’t there that night. Things might have been different if you were."
    ch "That’s the part Chinami wants to understand. Because if Papa wants to do those things with Tsukasa-"
    s "No. Chinami, that’s not what-"
    ch "Chinami thinks it’s okay."
    s "..."

    scene chinamiconfronts23
    with dissolve2

    ch "..."
    s "..."
    s "{i}What?...{/i}"

    scene chinamiconfronts24
    with dissolve

    ch "Only if he’s {i}very,{/i} very careful though! Which means none of that stuff he was doing to big sis Chika in Chinami’s house!"
    s "..."
    ch "Understood?"
    s "You don’t know what you’re talking about..."
    ch "You’re right! I don’t! But if you were willing to do that stuff in front of Tsukasa, Chinami thinks you’d be willing to do it {i}with{/i} her too! "
    s "No. Absolutely not. Like...I’ve been alone with you before. In the bath. And none of that has ever led to-"
    ch "Papa won’t even look at Chinami in the bath, which means he’s probably trying to hide something. Like him being a lolicon."
    s "Wh...Why are you even bringing this up? Did Tsukasa put you up to it? Because her mother would-"
    ch "Nobody put Chinami up to anything. Tsukasa is very curious {i}because{/i} of you, but Chinami is more worried about what will happen if somebody {i}else{/i} gets to her first."
    s "What do you mean? No one’s going to get to Tsukasa {i}first.{/i} She’s under near-constant surveillance. Anyone who’d lay a finger on her has a death wish."

    scene chinamiconfronts25
    with dissolve

    ch "Chinami’s just saying — if Papa wanted to teach her best friend about the birds and the bees, Chinami would keep it a secret! And Tsukasa’s {i}really{/i} into birds all of a sudden!"
    s "..."
    ch "..."

    scene chinamiconfronts26
    with dissolve

    ch "Are you interested yet?"
    s "I don’t get it..."
    ch "Did Chinami get the analogy wrong? Is it bees and something else instead?"
    s "No, Chinami. I don’t get why you went from being completely oblivious to my sex life to trying to get me to {i}teach{/i} your friend over the course of two hours."

    scene chinamiconfronts27
    with dissolve

    ch "It’s not like Chinami {i}wants{/i} to do this! She just {i}has{/i} to!"
    s "Why?! Don’t you understand what pushing me in this direction will {i}do?!{/i} Don’t you know how dangerous it is for me to have an {i}excuse{/i} for something?!"
    ch "No! Chinami just doesn’t want to lose her friend!"
    s "So you’ll have {i}me{/i} taxidermize her instead?! And hang onto the husk that’s left of her once I {i}do?!{/i}"
    ch "Papa, no! Tsukasa’s mom is trying to get rid of her and Tsukasa is too stubborn to say no!"

    stop music fadeout 10.0
    scene chinamiconfronts28
    with dissolve2

    s "..."
    ch "..."
    s "What do you mean she’s “trying to get rid of her?”"

    scene chinamiconfronts29
    with dissolve

    ch "Tsukasa says her mom is trying to do one of those “arranged marriage” things for her...and that she might have to marry some guy she’s never even met before..."
    ch "But Chinami knows Tsukasa doesn’t want that...Tsukasa just wants to be useful to somebody and...have somebody love her and care about her."
    s "..."

    scene chinamiconfronts30
    with dissolve2

    ch "Chinami can’t get through to her, though..."
    ch "She won’t listen to a thing I say..."
    ch "But I want to protect her from a future she doesn’t want...because the thought of her being even more sad and alone than she is now hurts."
    s "..."
    ch "..."
    s "What do {i}I{/i} have to do with this though, Chinami?..."
    s "How am {i}I{/i} any better than some random guy?"

    scene chinamiconfronts31
    with dissolve2

    ch "Chinami thinks that...Tsukasa looks up to Papa. "
    ch "That she’ll listen to {i}his{/i} advice instead of hers."
    ch "But..."
    s "..."
    ch "She also thinks that..."
    ch "It will be harder to arrange a marriage..."
    ch "If she’s already been......."
    s "..."
    ch "That happens in movies sometimes..."
    ch "A man no longer wants a girl if she’s already been with another man..."
    ch "And if Papa is interested in Tsukasa like Chinami thinks he is..."
    s "..."
    ch "She won’t tell if he wants to be that man."
    s "..."
    ch "..."
    s "You watch too many movies."

    scene chinamiconfronts32
    with dissolve2

    ch "..."
    s "If she can say no...that’s all she has to do."
    s "Tsubasa would never force her daughter to do something like that."
    ch "But Tsukasa {i}won’t{/i} say no. She refuses."
    s "Then...I’ll talk to her. If she really {i}does{/i} look up to me. "
    s "But that’s all."
    ch "But if the two of you like each other-"
    s "Chinami."
    s "That’s all."
    ch "..."
    s "We’re done with this topic. Are you ready to order food?"
    ch "Papa-"
    s "{i}Are you ready to order food?{/i} Or do I need to start boiling some water?"
    ch "..."
    s "..."

    scene chinamiconfronts33
    with dissolve2

    ch "Chinami’s not a baby. She knows how to boil water..."
    ch "She’ll drop it, though...as long as you promise you’ll talk to Tsukasa."

    scene black
    with dissolve2

    s "Fine..."
    s "I promise."

    $ renpy.end_replay()
    $ chinamispring5 = True
    $ chinami_love += 1

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump chinamispring6

label chinamispring6:
    "{i}Several hours later...{/i}"

    play sound "dooropen.mp3"

    c "{i}Chinami! I’m home!{/i}"

    scene chinamibalconycatch1
    with dissolve2

    c "I bought stuff to make pancakes tomorrow morn- ah. The lights are off?"
    c "Is she asleep already?"

    scene chinamibalconycatch2
    with dissolve

    c "Chinami? Is everything-"

    scene chinamibalconycatch3
    with dissolve

    c "Ah...Sensei’s still here too?"

    scene black
    with dissolve2
    scene chinamibalconycatch4
    with dissolve2

    c "Aww...she must have worn him out."

    "A warm feeling (the type that could not be confused for arousal) flooded through Chika Chosokabe so quickly and so deeply that she felt as if her heart was full."
    "It was everything she wanted (minus one mother) all in one room. Defenseless. Sleeping. Adorable."
    "And she was filled with that sort of cute-aggression that made her want to strangle both of them until they were dead and frozen in this scene for all eternity (or until the cops come)."

    scene chinamibalconycatch5
    with fade

    "But she would not do this — for she was not a murderer. And she loved the two of them so dearly that even the thought of harm befalling them made her want to kill herself instead."
    "What she did not yet understand is that harm befell the man below her before he’d even reached Chinami’s age. "
    "And if he was a better student, Chika may have walked in on him perpetuating the cycle and violently fucking her little sister instead of just peacefully sleeping beside her."
    "But again, this was not a thought that occurred to her — for she was a good girl. Who did good things."

    c "Look at them..."
    c "Look at what I have..."

    "But she was blinded by love."

    scene black
    with dissolve2

    "And that blindness clouded her judgement sometimes."

    c "I’ll just let him crash here tonight. It’s too late to send him home anyway."
    ch "Mnh...big sis Chika?...When did-"
    c "{i}Shhh...{/i}go back to sleep, Chinami. I’ll be right back after I put my pajamas on."
    ch "Is Papa-"
    c "He’s still here...just go back to sleep, okay?"
    ch "Mnh...nh...okay..."
    ch "Goodnight...big sis Chika..."
    c "Goodnight...I love you."

    "Chika washed her face. "
    "Brushed her teeth. "
    "Then put on her pajamas before crawling into the futon with her make-believe husband."
    "It was a dream come true — but it was also a dream that would deprive her of sleep as she didn’t want to wake up and find that he had gone back home without saying goodbye."
    "So she lied there, staring up at the ceiling for at least an hour. But it felt like longer."
    "Her gaze would linger occasionally toward her sister to see if she was still asleep. And she was. Every time."
    "In those moments, she’d place a hand on the back of the man beside her, stroking him softly and hoping that he’d wake up and find her there."
    "But {i}he{/i} didn’t wake up either. So she was alone with her thoughts."
    "And those thoughts grew impure each time she caught his warmth."

    scene chinamibalconycatch6
    with dissolve3


    "Which brings us here."

    c "..."
    s "..."
    c "..."
    s "Mn..."

    scene chinamibalconycatch7
    with dissolve2

    c "{i}Ah...{/i}"
    s "Mnh..."

    scene chinamibalconycatch8
    with dissolve2

    s "Chika?...What are you-"
    c "{i}Shh...{/i}"
    c "{i}You’ll wake up our daughter...{/i}"

    scene black
    with dissolve2
    scene chinamibalconycatch9
    with dissolve2
    play music "asobeatsex2.mp3"

    s "Is she...mngh...are you...for real right now?..."
    s "Isn’t she...right next to you?..."
    c "{i}Mhmm...but it’s fine if she’s asleep, right?{/i}"
    c "{i}It’s normal for parents to have fun while the kids are conked out. Probably.{/i}"
    s "Chika-"
    c "{i}Shh...{/i}"
    c "{i}This is the least I can do to repay you for today...just close your eyes and let me take care of you...kay?{/i}"

    scene black
    with dissolve
    scene chinamibalconycatch10
    with dissolve2

    s "Easier said than done with you...pressed up against me like that..."
    c "You were so cute that I couldn’t help myself..."
    c "But I was surprised to find that you were already hard when I reached over to touch it..."
    c "Were you dreaming of me...[chikamaster]?"

    scene chinamibalconycatch11
    with dissolve2

    s "Sure...let’s go with that."
    c "I don’t like that answer, [chikamaster]. Here I am, overflowing with love and desire for you and only you, and you respond with “sure?”"
    c "If it wasn’t me, who was it? Go on...tell me. I won’t get jealous."

    "It was a divine being that was approximately 30%% tiger, 45%% breasts, and 25%% household appliances. Its name was Harimanti and It was the God of Milk."
    "Of course this was ignored in favor of an easier answer."

    scene chinamibalconycatch12
    with dissolve2

    s "Fine...it was you. Is that {i}direct{/i} enough?"
    c "What were we doing in your dream?..."
    c "Wanna act it out now?..."
    c "I can’t sleep...I want you too badly..."
    s "{i}Well, I’m not gonna fuck you right next to your sister.{/i}"

    scene chinamibalconycatch13
    with dissolve2

    c "You don’t have to..."

    scene black
    with dissolve2

    c "I have a balcony..."

    "........."
    "......"
    "..."

    scene chinamibalconycatch14
    with dissolve2

    "Reckless behavior like this is common in those who spend so long tunneled in on something that they can’t even tell when they’re approaching a cliff to nothingness."
    "Which is why Chika Chosokabe assumed that the kind and seductive gesture of waking her {i}husband{/i} up with a handjob couldn’t possibly go wrong."
    "And if this is were the beginning of the game, she would probably be right."

    scene chinamibalconycatch15
    with dissolve2

    "But it’s {i}not{/i} the beginning of the game anymore. And every second that goes by, someone {i}else{/i} is falling off of a cliff to nothingness. "
    "Recklessness now is more reckless than ever before. And it’s this exact thing that will carry us away from here."
    "But where will it take us I wonder?"

    scene chinamibalconycatch16
    with dissolve2

    ch "Big sis Chika?...Chinami wants a glass of-"

    scene chinamibalconycatch17
    with dissolve2

    ch "Huh?..."
    ch "Is Chinami alone now?..."

    scene black
    with dissolve2

    "Groggy from being torn from her sleep, Chinami Chosokabe remembered very little about her last hour before passing out."

    scene chinamibalconycatch18
    with dissolve2

    "It wasn’t common for her sister’s boyfriend to stay the night, so she assumed he had already gone home by now."
    "But without anywhere left to go and no one waiting for him at home, he had no issues passing out right beside her."
    "So as she scanned the apartment looking for her sister, a trace of him was the last thing she expected to find."

    scene chinamibalconycatch19
    with dissolve2

    "Which is precisely what made the following scene unfolding before her eyes all the more shocking."

    scene chinamibalconycatch20
    with dissolve2

    ch "Big sis Chika?...What are you doing out-"

    scene chinamibalconycatch21
    with dissolve2

    ch "Ah..."

    scene black
    with dissolve2
    scene chinamibalconycatch22
    with dissolve2

    "There they were — locked in a pose befitting animals, diving so deeply into a world of their own that they’d forgotten she exists at all."
    "She observed her sister's trembling legs as she hung precariously over the railing Chinami had been warned to never approach. "
    "But instead of fearing for her sister’s safety, Chinami couldn’t help but think of other things. Things she {i}hadn’t{/i} been warned of."
    "Like how this pose was reminiscent of the video she’d watched earlier. And how it seemed exponentially more {i}lewd{/i} now that it involved people she knew."
    "She was angry, but she didn’t know why. She was sad, but she didn’t know why. She felt guilty, but she didn’t know {i}why.{/i} Yet she couldn’t look away."
    "This amalgamation of negativity did not blend in with the scene unfolding before her. It only made her feel {i}worse{/i} that she could not bring herself to flee."

    scene black
    with dissolve4

    "For ten minutes she watched them, standing still as a statue and hoping she’d be caught. But she wasn’t."
    "And she would fetch her {i}own{/i} glass of water before taking one sip, then crawling back into her futon where she would sleep soundly until the following morning."

    stop music
    play sound "static.mp3"
    scene chinamibalconycatch23 with flash
    stop sound
    play music "happyandplotting.mp3"

    if day == 6:
        $ day = 7
        $ totaldays += 1
        hide saturday onlayer date
        show sunday onlayer date
    else:
        $ day = 1
        $ totaldays += 1
        hide sunday onlayer date
        show monday onlayer date

    "And the following morning was brighter. Not just {i}literally{/i} either."
    "Chinami awoke to the scent of pancakes and the sounds of her sister cheerfully humming."
    "But it filled Chinami with conflicting emotions as her sister hadn’t even bothered changing her pajamas after being defiled in them on the balcony."
    "“Perhaps this is not something I should think about so negatively?” she thought, thinking negatively."

    scene chinamibalconycatch24
    with dissolve

    "So she approached her sister and greeted her with a merry, “Good morning” in an attempt to alleviate the new-found discomfort she was feeling."

    ch "I saw what you did last night."

    scene chinamibalconycatch25
    with dissolve

    "Just that wasn’t what she actually said."

    c "Oh! Morning, Chinami. I didn’t realize you woke up. What was that again? I couldn’t hear you."

    play sound "static.mp3"
    scene chinamibalconycatch26
    with flash
    stop sound

    ch "Nothing..."
    c "But-"
    ch "Chinami just said “good morning.”"
    c "Uhh...okay! Well, I tried telling you I bought stuff for pancakes last night, but you were asleep when I came in. Soooo...surprise! Pancakes exist now. How many do you want?"
    ch "Chinami wants to learn about sex."

    play sound "static.mp3"
    scene chinamibalconycatch27 with flash
    stop sound

    c "Six? Okay! Seems like a lot, but you {i}are{/i} a growing girl, I guess."
    ch "Mngh..."

    scene chinamibalconycatch28
    with dissolve

    c "Oh, I can finally ask now! How did your daddy-daughter dinner go? What’d you get Papa to buy for you?"
    ch "Chinami...got to try eel for the first time..."
    c "Ooooh, fancy. Did you like it?"

    scene chinamibalconycatch29
    with hpunch

    ch "DID {i}YOU{/i} LIKE IT?!"
    c "I...didn’t have any. I was not there."
    ch "Did you like what you {i}did{/i} have, though?! When you came home?!"

    scene chinamibalconycatch30
    with dissolve

    c "Oh, did he leave something for me in the fridge? I didn’t even know. I haven’t had eel in-"
    ch "THAT’S NOT WHAT CHINAMI MEANS! CHINAMI SAW WHAT YOU DID ON THE BALCONY AND IT WAS VERY UNSAFE AND VERY CONFUSING!"

    play sound "static.mp3"
    scene chinamibalconycatch31 with flash
    stop sound

    c "....................."
    c "No she didn’t."
    ch "She did...and she thinks you guys were out there for a really long time...maybe."

    scene chinamibalconycatch32
    with dissolve

    c "Hah...hahahahaha! Oh, you kids and your crazy dreams! Like, I don’t know what you {i}think{/i} you saw, but I came home and went right to bed!"
    c "So whatever it is, just forget about it and never bring it up again! Hahahahahaha!"
    ch "If big sis Chika won’t teach Chinami about sex, can Chinami have permission to watch pornography and learn that way?"

    play sound "static.mp3"
    scene chinamibalconycatch33 with flash
    stop sound

    c ".................."
    ch "Big sis Chika?"
    c "..................."
    ch "Big...sis Chi-"

    play sound "static.mp3"
    scene chinamibalconycatch34 with flash
    stop sound

    c "Six pancakes, coming right up! That’s it! That is {i}all{/i} we’ve talked about today! The end!"
    ch "Big-"
    c "{size=+15}THE END!{/size}"
    ch "Chinami...has to learn eventually, doesn’t she? And if big sis Chika has to keep hiding from her in order to do it-"
    c "You said six, right?! Are you sure that’s enough?! How about twelve?! Just to be safe!"
    ch "Maybe Chinami will just look answers up on her phone."
    c "Oh, that reminds me! I read an article the other day about how our phones are tracking us and stuff, so I’ve decided that I’m going to get rid of {i}both{/i} of ours! Hope you don’t mind!"

    play sound "static.mp3"
    scene chinamibalconycatch35 with flash
    stop sound

    ch "Chinami {i}does{/i} mind! And she thinks big sis Chika might be overreacting right now! Chinami has nobody else to teach her about this stuff! She has to rely on {i}you{/i} for that!"
    c "Hahah! Hahahahah! R-Right she does! But I...there are just so many pancakes I need to make and...so little time! Hahahah! {i}You saw nothing.{/i}"
    ch "SISTER, PLEASE!"
    c "{size=+20}NOTHING!{/size}"

    play sound "static.mp3"
    scene chinamibalconycatch36 with flash
    stop sound

    c ".................."
    ch "..................."
    c "You know what? On second thought, I don’t think I’ve made enough yet. I need to go make five hundred more pancakes."
    ch "Chinami thinks we don’t have enough ingredients for that..."

    scene chinamibalconycatch37
    with dissolve

    c "Darn it! Looks like I have to run to the store then! Hahahaha-"
    ch "Can you take this seriously?! Chinami’s been watching you make pancakes for a full {i}hour{/i} now! She’s already eaten ten! She isn’t hungry anymore!"
    c "But you will be in the future, right? So I should just make as many as possible so you’ll be taken care of for the rest of forever!"
    ch "You would rather give Chinami diabetes than teach her about sex?!"

    scene chinamibalconycatch38
    with dissolve

    c "Good point! I should buy the {i}sugar-free{/i} pancake mix instead."
    ch ".............."
    c ".............."

    scene chinamibalconycatch39
    with dissolve2

    c "{i}Hah...{/i}"
    c "Chinami...your big sister made a mistake. She shouldn’t have done that while you were home. And she is very sorry you had to see it."
    ch "Chinami doesn’t {i}care{/i} that she saw it. She understands that big sis Chika loves Papa and that’s a thing adults do when they love each other."

    scene chinamibalconycatch40
    with dissolve

    ch "That’s sort of...{i}all{/i} she understands, though. And she thinks she is ready to learn more."
    c "Well...let me ask you this — why do you {i}want{/i} to learn more? Because {i}I{/i} was an early bloomer, but you’re even younger than {i}I{/i} was when mom taught me about this stuff."
    c "Are you, like...{i}noticing{/i} things about yourself? Do you {i}feel{/i} any different when you think about boys?"
    ch "Chinami doesn’t know any boys, so she doesn’t really think about them."
    c "Does...Chinami feel different when she thinks about {i}Tsukasa?{/i} Or any of big sis Chika’s friends?"

    scene chinamibalconycatch41
    with dissolve

    ch "Not really...is she {i}supposed{/i} to?"
    c "You’re not {i}supposed{/i} to feel anything specific. Everyone thinks about this stuff differently. It’s just...you’re a little {i}too{/i} young to be thinking about this at all."
    c "Did...Tsukasa put you up to this? Because I know {i}she{/i} was asking and-"
    ch "Tsukasa didn’t put Chinami up to anything."
    ch "It’s just sex, sex, sex, everywhere Chinami looks now and it’s making her head hurt."
    c "It’s scary, right?"

    scene chinamibalconycatch42
    with dissolve

    ch "Kind of...but Chinami can’t really explain why."
    c "I was the same way. Mom practically had to strap me down to teach me about the birds and the bees. I kept getting nervous and running away."
    c "So...major props to you for just confronting me about it, I guess. You’re stronger than I was."
    c "I just...I don’t really know...how to approach this."

    scene chinamibalconycatch43
    with dissolve

    c "I’m still...kind of {i}new{/i} to a lot of this, Chinami. This whole “filling two roles” thing. And I {i}knew{/i} this day would come eventually, but..."
    c "As you can probably guess from all of the pancakes, I kept pushing it away every time the thought came up."

    scene chinamibalconycatch44
    with dissolve

    c "So I’ll {i}teach{/i} you, but..."
    c "I need time to figure out {i}how{/i} first. This is a sensitive topic and I don’t want to, like...accidentally mess something up and mess {i}you{/i} up in the process."
    c "Is that okay? Can you give me a little time?"
    ch "Can Chinami have permission to watch pornography in the meantime?"

    scene chinamibalconycatch45
    with dissolve

    c "Never."
    ch "Yeah...she had a feeling you were going to say that."
    c "And I’m sorry again for...last night, Chinami. I’m sorry for confusing you. I just..."
    c "It won’t happen again, okay?"
    ch "But then...where will you and Papa-"
    c "That is {i}not{/i} something you should worry about. It’s not something you should even {i}think{/i} about. And it is {i}definitely{/i} not something you should talk to Papa about."
    c "Do you understand?"
    ch "Yes, big sis Chika...Chinami understands."
    c "Good. I love you."
    ch "Chinami loves you too..."

    scene chinamibalconycatch46
    with dissolve

    c "On another note, though...what are we going to do with all of these pancakes? Because we can’t really {i}save{/i} them despite what I said in my earlier fit of anti-sex mania."
    ch "Maybe Chinami can throw them off the balcony when birds come by to feed them?"
    c "Big sis Chika would very much like to deep clean the balcony first. And the bedroom. And the-"

    scene chinamibalconycatch47
    with dissolve

    c "Oh no."
    ch "What’s wrong, big sis Chika?"
    c "Uhh........nothing!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    c "I just...have to clean the kitchen really quick! Don’t eat any more pancakes! No matter what!"
    ch "Chinami think she’ll die if she eats another pancake, so that shouldn’t be a problem."
    ch "Also, shouldn’t big sis Chika clean that shirt too? Since that’s the one she was wearing when-"
    c "Aaaaaaah! Go take a shower or something! I don’t want any more information on how much you saw!"
    ch "Can Chinami ask one more question first?"
    c "Mnngnhhhhgh fine! But just {i}one!{/i}"
    ch "Is it normal for them to be as big as Papa’s?"
    c "NEVERMIND! SHOWER! NOW!"

    "And so one more fruit began to ripen."
    "How far will it fall from the tree, I wonder?"

    $ renpy.end_replay()
    $ chinamispring6 = True
    $ chinami_love +=5
    $ chika_love += 5

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4
