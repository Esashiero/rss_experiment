label calltsukasamorning:
    if tsukasa_love >= 1 and tsubasaspring1 == True and tsukasaspring1skip == False and tsukasaspring1 == False:
        jump tsukasaspring1intro
    if tsukasarefused == True:
        "No."
        jump callmorning
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Tsukasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callmorning

label calltsukasaafternoon:
    if tsukasa_love >= 1 and tsukasaspring2 == True and tsukasaspring3 == False:
        jump tsukasaspring3
    if tsukasarefused == True:
        "No."
        jump callafternoon
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Tsukasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

label calltsukasanight:
    if tsukasarefused == True:
        "No."
        jump callnight
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Tsukasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callnight

label tsukasaspecial1:
    scene hall_day
    with fade
    play music "10c.mp3"

    "Another week as the world’s most sexually active teacher means another week to completely ruin the lives of everyone around me by simply showing up to class."
    "Oh. Sorry for the self-loathing so early in the morning. I just figured that if I got it all out of the way now, I’d be able to do whatever I want for the rest of the day without thinking at all."
    "Which, to be fair, is what I try to do most days to begin with. "
    "However, I was notified of a very particular “holiday” through a phone call from my assistant this morning that has put me in a particularly passive aggressive mood."
    "Especially since it requires my full presence in the classroom at the risk of both Imani and me losing our jobs. And Imani has been kind enough to me so far that I don’t want to do that to her."
    "Also, I’m pretty sure she’s barely hanging on by a thread financially and she kind of needs this."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    "I slide open the door and prepare myself for the start of what I imagine will be the worst holiday ever- and that is saying a lot since things like Christmas exist."

    scene tsukasaday1
    with dissolve2

    "But at least on Christmas you can come up with excuses to not pay attention to certain people."

    tk "Good morning! Happy National Tsukasa Day!"
    to "Tsukasa, how much did you pester our poor father to make this childish dream of yours a reality?"
    tk "It’s not a childish dream if I’m an ancient and powerful wizard. Just because there’s not National Touka Day doesn’t mean you can get mad at {i}my{/i} holiday."
    to "Sensei is a very busy-"

    scene tsukasaday2
    with dissolve

    to "Well...actually, that’s not true at all. Sensei is practically never busy."
    to "But he’s assuredly not going to {i}start{/i} being busy when he’s preoccupied with silly games like this."
    tk "Wrong again, dear sister. I’ve heard the games this adult plays and they are a lot louder than whatever is going on in this sorry excuse for a classroom."
    s "Why are you here?"
    tk "Because it’s National Tsukasa Day and I get to do whatever I want."
    s "So you chose to...come to high school?"

    scene tsukasaday3
    with dissolve

    tk "Yup!"
    tk "The train wasn’t very exciting, so I wanted to get a closer look at the true commoner mecca! A public school!"
    tk "I even had my personal tailor make an exact copy of my sister’s uniform so I can experience firsthand the pain she endures every day as she is turned into one of you!"
    ay "Sensei, how long is Tsukasa staying here?"
    a "While I, too, would like to know the answer to that question, I’m more concerned about what sorts of games Tsukasa has heard you playing."
    s "To Ami, I have no idea what she’s talking about. And to Ayane, I assume she’ll only be here until the end of Tsukasa Day."

    scene tsukasaday4
    with dissolve

    tk "Ahem! It is {i}National{/i} Tsukasa Day! Don’t go leaving out words that describe how important it is."
    tk "Also, National Tsukasa Day doesn’t end until next Wednesday because Father said so."

    scene tsukasaday5
    with fade

    ima "Damn. I wish I was rich enough to change the way time works."
    ay "You don’t have to be rich, Imani! All you have to do to change the way time works is get pregnant with Sensei’s baby. Well, at least according to Maya."
    a "What?"
    m "I have absolutely no clue what she is talking about."

    scene tsukasaday6
    with dissolve

    ima "With all due respect, Senpai, I think I’d rather take the money."
    ima "You’re handsome and all, but if the way you treat my body is anything like the way you treat my mind, I can’t imagine that would be a very enjoyable experience."
    s "Luckily for you, I don’t intend on getting anyone preg-"
    tk "Stop paying attention to everyone not named Tsukasa on National Tsukasa Day!"

    scene tsukasaday7
    with dissolve

    ima "Right! Uhh...yeah."
    ima "See, the issue with that is that I’m not exactly...{i}good{/i} with kids that aren’t in high school yet. They make me feel weird. And even if today is National Tsukasa Day, you kind of..."
    ima "Well, you don’t belong here."
    s "Watch it, Imani. This girl may not look intimidating, but she holds our futures in the palms of her tiny hands."

    scene tsukasaday8
    with fade

    tk "Are you two sure you are even teachers? Because I’m hearing a whole lot of slander and not so much {i}teaching{/i} right now."
    tk "And I suggest that if you two want to keep your jobs, that you...actually {i}do{/i} them."
    to "I am so sorry that this is happening today. I tried my best to prevent it, but...alas."
    ima "What can we even {i}teach{/i} with someone your age here? You won’t be able to follow along."
    tk "Do you take me for a lowly peasant? I have received only the highest forms of education from the most qualified teachers in all of Kumon-mi."
    tk "Your meaningless squibbles disguised as educational lectures mean nothing before the greatness that is Tsukasa AKA “Tsurumi” Tsukioka of the Tsukioka family."
    ima "Squibble? What’s a squibble?"

    scene tsukasaday9
    with dissolve

    tk "A word I made up that means “silly and pointless!” I call it a Tsukasology. Or a...Tsukasism. There’s another one right there."
    to "Creating new words is far detached from proper education, Tsukasa...AKA Tsurumi."
    tk "Then try me! Ask me anything. I’m sure my answers will be far more acceptable than whatever these so-called “squobbles” would give you."
    ima "But...no one calls them that."

    menu:
        "What is the world’s oldest city?":
            s "What is the world’s oldest city?"
            tk "Damascus, Syria!"
            tk "That's a highly contested topic as many people believe it to be Jericho. But Jericho was more like a large town than a city during its early years."
            tk "Mother says Damascus isn’t all it’s cracked up to be, though. She visited there on one of her travels from before Kumon-mi was isolated."
            ima "Did she get it right?"
            s "I have no clue. I just asked a question thinking she wouldn’t know the answer."
            ima "Never fear, Senpai. I will do my duties as your loyal peon and utilize the glory of my smart phone to- holy shit, she’s right."
            to "Of course she is..."

        "How tall is Mt. Fuji?":
            s "How tall is Mt. Fuji?"
            tk "Three-thousand, seven-hundred-seventy-six meters!"
            tk "I’m supposed to go there with Papa once we’re allowed to leave the city again."
            tk "He says he’s going to buy part of the mountain so I can have my own little house there."
            ay "Is that even legal?"
            tk "Everything is legal when you’re rich. But you wouldn’t know that since you’re not."
            to "That’s Ayane Amamiya you’re speaking to, Tsukasa. She comes from the second richest family in all of the city."
            tk "Sorry. Can’t hear you from all the way up here in first place."

        "Who lives at the North Pole?":
            s "If you’re so smart, how about you tell me who lives at the North Pole?"

            scene tsukasaday10
            with dissolve

            ima "Bruh."
            to "Sensei..."
            tk "The North Pole?"
            tk "Do you take me for a fool, commoner?"
            tk "Everyone knows that’s where Santa’s workshop is. That was barely even a question."
            s "Are you sure about that?"
            tk "Yes. Unless you mean to tell me it is my mother who has been returning my annual letters to him. And that would just be utter nonsense."
            s "Are you {i}sure{/i} about that?"
            to "Don’t do it, Sensei..."
            a "Even you should draw the line at telling a little kid the truth about Santa Claus, Sensei. You’re better than this."

            scene tsukasaday11
            with dissolve

            tk "The truth?"
            tk "Did something happen to Santa Claus?"
            tk "If he was evicted due to the waste produced by his workshop, I would not mind forgoing some of my allowance to assist him. He does tremendous work for this country and is an asset to all of us."
            ay "Just drop it, Sensei. Before it’s too late."
            s "Fine. But I rest my case in showing that Tsukasa isn’t as smart as she thinks she is."
            to "Yes, but that is only because you asked her a question that all of those prestigious educators dared not ever speak about."
            tk "Why is everybody acting so weird? All it takes is a little personal research to figure out the truth."
            tk "Can you people not afford computers?"

    scene tsukasaday12
    with fade

    ima "What do you think, Senpai? It would feel kind of wrong getting rid of her now. But, like I said before, I’m not really the best when it comes to kids."
    s "And you think I am?"
    ima "Well, you became a teacher, didn’t you? You’ve gotta be at least a {i}little{/i} good with them."
    s "Didn’t...you also become a teacher?"
    ima "Yeah, but I’ve still got time left."
    s "I’m only 31."
    ima "Damn, that old already? Need me to go grab a cane from the nurse’s office?"
    tk "Again! You people refuse to pay attention to the one person you should be paying {i}all{/i} of your attention to today!"
    tk "This insolence will not go unpunished! As soon as my father finds out about this, you two will never work another day in this town again! You-"
    to "Tsukasa, please! They are doing their best! And all things considered, their best seems very good based on the standards of today’s public education system."

    scene tsukasaday13
    with fade

    tk "Hah...This is exactly why the youth of the nation has become so lazy and unmotivated. No one gets the education they need anymore. Papa should really do something about that."
    to "I agree but, unfortunately, progress didn’t have much place to go after the creation of bubble wrap."
    c "Hey, Tsukasa. What are you doing here?"

    scene tsukasaday14
    with dissolve

    tk "Oh! The peasant girl from Mother’s onsen!"
    tk "And here I was thinking the strong scent of cheap perfume was just the way girls’ public schools smelled."

    scene tsukasaday15
    with dissolve

    c "Is it...really that strong? Because I’m trying something new and that wasn’t exactly the type of reaction I was looking for."
    tk "What type of reaction were you looking for?"
    c "A...positive one?"
    tk "Oh."
    tk "Well, good luck."

    scene tsukasaday16
    with dissolve

    c "Th...That aside! How are things? How’s your mom?"
    tk "Things are great! As you may have noticed from all of the banners in the hall, today is National Tsukasa Day!"
    tk "Unfortunately, Mother had other matters to attend to, so she is unable to spend it with me. But that’s okay because my big sister and her teacher are looking after me."
    tk "Which isn’t to say I wouldn’t be able to function on my own when I am much better and smarter than both of them. But laws will be laws."
    tk "You do know what “laws” are, correct?"

    scene tsukasaday17
    with dissolve

    c "Yes, Tsukasa. I do know what laws are."
    tk "Good! I never know with you people."
    c "“You people” as in...commoners, right?"
    tk "Good job! Public education has not entirely failed you yet."

    scene tsukasaday18
    with dissolve

    tk "That said, it would be wise to quit while you’re ahead and follow in the footsteps of your younger sister. She and I have big plans for this world."
    c "Yeah, you two have been talking a lot lately, haven’t you?"
    tk "Talking? We’re not just {i}talking.{/i} We’re drafting business plans that are going to flip Kumon-mi on its head. People like us do not have time to simply “talk.”"
    c "Well, would you maybe like to come over and discuss business in person sometime?"

    scene tsukasaday19
    with dissolve

    tk "Can your budget home fit more than two people inside of it?"
    c "Uhh...yes."
    c "Just...probably not more than five."
    tk "I can fit more people than that in my bathroom."
    c "Why is that...ever a thing you’d want to do?"
    tk "It’s not. But I can and I felt compelled to inform you of that."

    scene tsukasaday20
    with dissolve

    c "Either way, Chinami has been excited to see you again and I figure this would give you two a good chance to play together."
    tk "I will consider it and consult with the rest of my business associates!"
    tk "If I do agree to {i}play{/i} though, will you consider teaching Chinami and I the special game you played with your teacher at the onsen? Mother says it’s for adults, but I have proven today that I-"

    scene tsukasaday21
    with hpunch

    tk "MMMFMFMFMFMFMFFFFFMFHHFHFFF!!!!!"
    ima "Special game?..."
    ima "Onsen?..."
    c "Hahaha! Kids, right?! Always making up stories!"
    s "Oh, look. A stack of papers way at the...other end of the school that I need you to file."

    scene tsukasaday22
    with fade

    ima "..."
    s "..."
    ima "..."
    s "..."
    ima "You trying to teach Chika how to time travel, Senpai?"
    s "I have no idea what you’re talking about."
    ima "And at an {i}onsen?{/i} What does that mean for all of the other girls who had to stare at your drab-ass wallpaper while you were doin’ ‘em dirty?"
    s "Is that really what you’re most concerned about?"
    ima "I’m an advocate for equality, Senpai. We {i}all{/i} deserve onsens."
    s "Well, I’ll add you to the top of my...prospective onsen visit list now."
    ima "Think saying that might be giving me a little too much attention on National Tsukasa Day, don’t you think?"

    scene tsukasaday23
    with fade

    tk "MMMFMFMFMFMFFHFHFHFFMMFMFM!!!!!!!! MMMMM!!!!!!!"
    to "Tsukasa, what does Mother say about making a racket like that? Quiet down or you’ll attract negative press."
    tk "MMMMMMMMMM!!!!!!!!!!!!"
    c "Tsukasa...I’m gonna let you go now. {i}But I kinda need you to not say anything about the onsen, okay? Nobody is supposed to know about that.{/i}"
    tk "MMMM! MMMMM! MMMM!!!"

    scene tsukasaday24
    with dissolve

    tk "Are you out of your mind?! Do you have any idea who I am?! Do you think it’s okay to just assault a princess?! I will have your head!"
    c "But if you kill me, Chinami won’t want to do business with you anymore, so...your success kinda hinges on me in a way, doesn’t it?"

    scene tsukasaday25
    with dissolve

    tk "While it {i}is{/i} true that an ally like her would certainly take us to the next level, I’m not quite sure if it is worth my own personal safety."
    c "What if I...promise not to grab your face anymore?"
    tk "That would be a start...but I am going to need something a little more than that."
    c "Uhh..."
    c "You can eat...cereal when you come over to my place?"

    scene tsukasaday26
    with dissolve

    tk "C...Cereal? But Mother says cereal is a leading cause of diabetes and that there are much tastier and healthier alternatives."
    c "And while I’m sure she’s right...you {i}do{/i} want a taste of commoner life, don’t you? What better taste than eating the same thing Chinami eats every morning {i}inside{/i} of Chinami’s house?"
    c "Think of it as a...research...project."

    scene tsukasaday27
    with dissolve

    tk "You drive a hard bargain, peasant. That does sound like something that tickles my interest. However, I have one final adjustment I’d like to add to your offer."
    c "And that...adjustment is?"

    scene tsukasaday28
    with dissolve

    tk "Can my sister come too?"
    to "What?"
    tk "It wouldn’t be fair if I got to experience something like that firsthand and she did not. I am simply doing this so that the two of us may remain on equal footing."
    tk "It is the least I can do in exchange for intruding on her personal life by being here."
    to "Tsukasa...I don’t really need to-"
    c "Sure, yeah. That’s actually..."

    scene tsukasaday29
    with dissolve

    c "You know what? Why don’t we invite Sensei too?"
    s "What?"
    tk "That seems unnecessary. Jeeves has no place in the same room as two serious and powerful businesswomen. And also Onee-chan."
    to "Why is Sensei...suddenly a part of this as well, Chika?"
    c "Because I was looking for a good time to go do something lately and kind of need a babysitter since I have no idea how long it will take."
    c "Which isn’t to say I don’t trust you, Touka. I just...don’t really know if you'll be able to grasp any of the, uhh...commoner technology at my place."
    s "I mean...I guess I can come? I doubt I’ll be much help, though."
    tk "Jeeves can wait in the lobby while the rest of us talk. That seems fair to me."
    to "I don’t believe Chika’s home is the type to have a lobby, Tsukasa. Sensei can wait in her rose garden instead."
    s "..."
    c "Sensei? You cool with that?"
    s "Depends. Do you have a rose garden now?"
    c "Who doesn’t?"
    to "Told you so, Tsukasa. You should listen to me more often."
    tk "Stop making so many silly decisions and I will."

    scene black
    with dissolve2

    "Somehow, I wound up getting roped into agreeing to be a babysitter for both Chinami {i}and{/i} Tsukasa soon."
    "That doesn’t sound exhausting at all."
    "Thankfully, I’ll at least have Touka there with me. And while that probably won’t really help either, it will definitely help me feel a little more {i}normal{/i} as there’s at least someone who isn’t..."
    "Well, someone who isn’t a full blown child there."
    "Plus, an environment like that sounds like the perfect place to fuck with her. And that is quickly becoming one of my favorite past times."
    "Anyway, the day comes to an end- and I find myself retreating back to my office."

    $ renpy.end_replay()
    $ tsukasaspecial1 = True

    jump tsukasaspecial1p2

label tsukasaspecial1p2:
    if _in_replay:
        play music "10c.mp3"

    scene tsukasaoffice1
    with dissolve2

    "But not without a very special {i}guest...{/i}"

    tk "I’m bored. "
    s "Well, you had the opportunity to leave when that convoy of limos showed up, but you decided to follow me here instead. So you did this to yourself."
    tk "Tsukasa Tsukioka deserves more than just a convoy of limos. If Mother thinks she can buy me off with just that, she is sorely mistaken."
    s "I can’t imagine buying you off {i}at all{/i} is feasible considering how numb you already are to money at your age but, to satisfy my own curiosity, what {i}will{/i} it take for you to leave?"
    tk "I’m making Mother come here to get me on her own. It isn’t fair that I should have to be surrounded by lowly peons on my own national holiday."
    s "I thought your mother was busy?"
    tk "She won’t be if I ask enough. That’s just how important I am."

    "In just seven hours, I have gone from the world’s most sexually active teacher to the world’s most exhausted teacher."
    "Well, after Wakana- who I’m consistently shocked to see roaming the halls despite looking like she is going to drop dead at any moment."
    "Regardless, I must now play babysitter while waiting for someone to come take this brat off of my hands."
    "I guess you can call it practice for when I have to visit Chika’s house and watch both her {i}and{/i} Chinami soon, but at least then I’ll have Chinami to keep her occupied. And Touka to keep {i}me{/i} occupied."

    tk "Jeeves, tell me a story."
    s "No."

    scene tsukasaoffice2
    with dissolve

    tk "But it’s-"
    s "I know what day it is. But I will not be bossed around in my own office by someone I could pick up with one hand. "
    tk "If you’re not going to tell me a story, can you at least do {i}something{/i} to keep me entertained?"
    s "Like what?"
    tk "How am I supposed to know? You’re the adult here. Aren’t you supposed to be full of guidance and wisdom?"
    s "I don’t think you’re old enough for my guidance and wisdom yet."
    tk "What about that game you were playing with the peasant girl at the onsen?"
    s "I really hope your mom gets here within the next thirty seconds because that is a road that even I am not ready to traverse just yet."

    scene tsukasaoffice3
    with dissolve

    tk "Hah...Of course it’s not. This Tsukasa Day sucks. It’s like nobody is appreciating me any more than they normally do. "
    tk "The only difference is I got to go to high school. And even that wasn’t very fun."
    s "I’m not sure what you were expecting, but school isn’t really known for being “fun.”"
    tk "Not like I would know. I’m not allowed to go to school."
    s "Not allowed? Or just not willing to settle for a commoner school?"
    tk "I would settle for a commoner school if I had to. "
    tk "I’m the second in line to inherit the Tsukioka family business, so it’s not like I {i}have{/i} to get the highest form of education when my older sister is going to be the one to take over."
    tk "Unless staying here makes her brain turn into mush. Which, based on what I have seen here today, it might. "
    s "While what you say may be true, I’m not really sure what that has to do with you not being {i}allowed{/i} to go to school."
    tk "Mother says I’m too “advanced” to go to school with girls my age and too young to go to school with Big Sister."
    tk "So all I can do is sit at home and listen to boring old people talk about boring stuff when what I {i}really{/i} want to do is have fun."
    s "I’ve been to your house. I have a hard time believing there isn’t anything fun to do there."

    scene tsukasaoffice4
    with dissolve

    tk "Nothing’s really fun if you do it every day. Which is why I like going out and seeing other stuff that I’m not able to see at home. Like tacos. Or “the subway.” "
    tk "Or that very pale girl with the freckles who kept talking about demons."
    s "That’s Molly and she isn’t really a tourist destination."
    s "In fact, none of the things you listed are tourist destinations and you should probably do a little more research if you really want to see the outside world."
    tk "Maybe."

    scene tsukasaoffice5
    with dissolve

    tk "Or maybe you can officially accept the job as the new Jeeves Tsukioka the Thirteenth and we can go on all sorts of commoner adventures that-"
    s "No."

    scene tsukasaoffice6
    with dissolve

    tk "You are being very rude to me, Jeeves. This sort of behavior will not be tolerated."
    s "Fuck you."

    scene tsukasaoffice7
    with dissolve

    tk "Ah! I’m telling Mother that you cursed at me! "
    s "Do it. I’m pretty sure she’ll understand."
    tk "Nuh-uh! Cursing at a child is something adults should never do! I’ve gotten at least ten other Jeeves fired because of that."
    s "If ten other Jeeves cursed at you, don’t you think the problem might be...I don’t know, {i}you?{/i}"

    scene tsukasaoffice8
    with dissolve

    tk "Tsukasa Tsukioka isn’t a problem. She is gifted and talented and richer than you and everyone else you know combined."
    s "I know your sister, you know. And, unless she is a pathological liar who is only attending this school because she was excommunicated from your family, I’m pretty sure {i}she’s{/i} rich too."
    tk "She might as well be excommunicated with how often she talks about her new fun and exciting commoner life."
    tk "It’s like she doesn’t even remember we’re better than you or something."
    s "Or...she’s just starting to realize you’re not?"

    scene tsukasaoffice9
    with dissolve

    tk "But we are."
    s "How?"
    tk "We’re smarter and cleaner and more sophisticated and cleaner and are trained in a variety of different skillsets that people like you aren’t exposed to. And also, we are cleaner."
    s "I don’t know where this strange fascination with our personal hygiene comes from, but there are plenty of people out here who are just as talented as you and Touka."
    s "Like Tsuneyo. She was a national kendo champion and now she is a...noodle warrior."
    tk "A...noodle warrior?"
    s "And then there’s Otoha who’s, like...some singing prodigy or something. And Nodoka, who is also prodigious in a lot of ways when she isn’t ruining the lives of ex-Yakuza."
    tk "What about the one girl with the ponytail who kept glaring at you all day? What’s she really good at?"
    s "Uhh..."

    scene tsukasaoffice10
    with dissolve

    s "She’s good at..."
    s "..."
    tk "..."
    s "Eating?"
    tk "That doesn’t sound very impressive to me, Jeeves. If you were trying to make me realize how interesting you people can be, you should have stopped at the Yakuza part. "

    scene tsukasaoffice11
    with dissolve

    s "The fact of the matter is that there’s just a lot more to what makes a person good than how talented they are or...how “clean” they are."
    tk "Like what?"
    s "Like how...nice they are. How open to change they are. How adaptable and versatile they can be in all types of situations."
    tk "And who out of all of your students do you think is the best at all of those things?"
    s "..."
    tk "..."

    scene tsukasaoffice12
    with dissolve

    s "Touka."
    tk "See, Jeeves? The Tsukioka family is just flat out better than everybody you know."
    s "Some members at least. Others...I’m not convinced yet. But sure, you win this round, Tsurumi."

    scene tsukasaoffice13
    with dissolve

    tk "Of course I win! A Tsukioka does not pick losing battles. Not that there are many battles we’d lose in the first place, but still. "
    s "You are easily the most prideful person I have ever met and you probably can’t even ride a bike yet."
    tk "I don’t own a bike, but Big Sister lets me ride Morning Glory sometimes and I haven’t fallen off yet."
    s "Look at you, not even owning your own horse yet. And you call me a commoner."
    tk "I own seven horses. They’re just all display pets."
    s "What good is a display horse?"
    tk "You’d know if you could afford one. But sadly, unless you accept my proposition and become a real Jeeves, you never will."
    s "How did you get like this when both of the other Tsukioka women are so approachable and kind?"

    scene tsukasaoffice14
    with dissolve

    tk "Some people are just born with the gift, I suppose."
    s "Is it too late to return it?"
    tk "When you’re as rich as Tsukasarumi Tsukioka, you don’t have to return anything. You can just buy something else."
    s "On second thought, I’m just going to blame your father as I can’t imagine Tsubasa or Touka having this sort of influence on you."

    scene tsukasaoffice15
    with dissolve

    tk "It’s not Papa’s fault I’m like this. It’s probably just a side effect of being the second born in a family that typically only produces one heir."
    tk "Besides, I don’t see him that much anyway. He’s always doing stuff and never has time for me anymore."
    s "Really? With how much you talk about him, I figured you bothered- err...I figured you were {i}with{/i} him all the time."
    tk "Not really. I try to talk to him as much as I can, but I think he forgets to charge his walkie talkie sometimes."
    s "Walkie talkie?"
    tk "Mhm. Santa brought me a walkie talkie a few years ago so I could talk to Papa whenever I wanted. "
    s "Does he not have a cell phone?"
    tk "He does. But he says that it’s for work only and that I’m not allowed to call him on it during the day."
    s "I see..."
    s "What do you spend most of your time at home doing then?"
    tk "Whatever I want. Drawing pictures. Swimming. Shifting all of Big Sister’s furniture that isn’t too heavy slightly to the left and watching her get confused."
    tk "Oh, and getting the staff to do my bidding. Can’t forget about that. I have lots of bidding that needs to be done."
    s "..."

    "Her story reminds me of one I’m much closer to-"
    "Of a girl who can barely speak about her father to me without the joy draining from her eyes as she slips into quiet reflection."
    "And while I feel I should be worrying that something like this may one day happen to Tsukasa as well-"
    "Instead, I find myself wondering if Ayane saw the world through such unfortunate glass."
    "I’m sure that a lot of that is due to the fact that I just don’t really care about Tsukasa yet...but at least it helps me understand her."
    "It’s not at all unique for children to act out when they aren’t getting adequate attention from their parents after all."

    play sound "knock.mp3"
    scene tsukasaoffice16
    with dissolve

    "But Tsukasa {i}is{/i} still getting attention from one of her parents. "
    "Maybe even a little {i}too{/i} much attention if that parent is dropping what they’re doing just to come over here and pick them up despite a whole convoy of cars sent to do just that."
    "It’s just not the parent she wants, I guess."

    tb "Tsukasa, dear...please tell me you are in there..."
    tk "About time, Mother. It’s been almost an hour and this room isn’t even climate controlled. And Jeeves is {i}soooooo{/i} boring."
    tb "Jeeves? But you fired Jeeves last- oh. Oh, Tsukasa! That is so rude for someone who’s done so much for our family in just a short while!"
    tk "All he’s done is get Big Sister to blab about him and the rest of her new friends all day long. Doesn’t that bother you? "
    tb "Not at all, dear. Your sister is finally-"
    s "You know you can come in, right? You don’t have to talk through the door."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    tb "Oh! Silly me. I probably would have stood there all day if you hadn’t said that."

    scene tsukasaoffice17
    with dissolve

    tb "I’m terribly sorry for any trouble my youngest daughter may have caused you. I truly didn’t expect her to refuse {i}all{/i} of our drivers when she knew I was busy, but...Tsukasa will be Tsukasa, I suppose."
    tk "It’s National Tsukasa Day. I didn’t want to go home with someone being paid to care about me."

    scene tsukasaoffice18
    with dissolve

    tb "But what about your sister? Couldn’t you have gone with her instead of burdening her teacher?"
    tk "Burden?"
    s "It’s really no big deal. I’m usually here for an hour or two after class anyway. Tsukasa just sat on the couch. "
    tb "Tsukasa should have been a good girl and left school with one of the drivers {i}like we agreed to this morning.{/i}"
    tk "But I wanted {i}you.{/i} "
    tk "And you told me we could get ice cream after I finished my first day of high school to celebrate."

    scene tsukasaoffice19
    with dissolve

    tb "Darling...that was when I assumed I didn’t have to take an hour away from my meetings just to come and get you. "
    tb "I’m not sure if we’ll have time anymore, dear. "

    scene tsukasaoffice20
    with dissolve

    tk "But...Tsukasa Day..."
    tb "Thank you again for watching over her, Sensei. I really do appreciate it."
    s "Yeah...no worries."

    scene tsukasaoffice21
    with dissolve

    tb "Come along, dear. Sensei’s time is just as valuable as ours and we have taken up enough of it."
    tk "Yes, Mother..."
    tk "Bye bye, Jeeves..."

    play sound "dooropen.mp3"
    scene tsukasaoffice22
    with dissolve

    "Tsukasa exits the office and..."
    "And I somehow feel a little bad for her."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The feeling fades shortly after, though."
    "Things like that don’t normally last long for me."
    "But the fact that it came at all tells me she’s no longer just an arrogant waste of space in my mind."
    "She’s a girl, just like everyone else, trying to figure out how she best fits into this world."
    "And all things considered, that’s a lot better than just staying put and deciding you don’t belong at all."

    $ renpy.end_replay()
    $ tsukasa_love += 5
    $ tsukasaspecial1p2 = True

    jump afterschoolevent

label tsukasaspring1intro:
    play sound "phonebeep.wav"

    "I tap on Tsukasa’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    tk "...Hello?"

    if sawchinami == True and tsukasachosen == True:
        jump tsukasaspring1
    else:
        play sound "phonebeep.wav"

        "And I hang up the second she does because I am better than this."
        "Just because Tsubasa gave me her daughter’s number doesn’t mean I {i}have{/i} to call her. And I’m not about to give into whatever subconscious temptation compelled me to do so."
        "She doesn’t need a tutor. And she definitely doesn’t need {i}me{/i} as a tutor to top that off and put her in danger."
        "Which is what I am. {i}Danger.{/i}"
        "To her. To myself. To her family. To everyone around me. And I’ve reluctantly accepted how that won’t ever change. "
        "But just because I am completely, irreparably broken doesn’t mean I should drag someone else into this mess lest the cycle continues."

        scene black
        with dissolve

        "I slide my phone back into my pocket. She doesn’t need to know it was me that called."
        "And I spend the rest of the afternoon thinking of how things could have gone wrong if I’d done something differently."
        "How they still could."
        "And how I’ll be running from this part of me forever with a ghost who feels more like a shadow right there behind me."
        "{i}Fragments of a thread get caught in your teeth and you spit them out onto the concrete.{/i}"
        "{i}You are a disappointment and a failure.{/i}"

        $ renpy.end_replay()
        $ tsukasaspring1skip = True
        $ tsukasaspring2skip = True
        $ tsukasaspring3skip = True
        $ tsukasarefused = True

        "........."
        "......"
        "..."

        jump nightch4

label tsukasaspring1:
    play music "tsukiokamanor.mp3"

    s "..."
    tk "Hellooooo? You’ve reached the great and powerful Tsukasa Tsukioka. Speak now or I will have this number traced by my team of super hackers!"
    s "Uh..."
    s "Hey."
    tk "..."
    s "..."
    tk "Jeeves? Is that you?"
    s "I guess so."
    tk "How did you get my number? It’s supposed to be top secret. Even Nee-sama doesn’t have it."
    s "But Chinami does?"
    tk "Chinami is a business partner who I need to have important business conversations with. But you’re not a partner at all, Jeeves. You’re just a peasant. A peasant who steals phone numbers."
    s "Your mom gave it to me in the event that I decide to start tutoring again."
    tk "Hmm...I’m not sure if I trust you as a tutor anymore, Jeeves. Your methods seemed quite counterintuitive at our last meeting."
    s "I wasn’t in the right frame of mind during our last meeting."
    tk "Oh. Are you saying that you are in the right frame of mind today?"
    s "No."
    tk "Oh."
    s "In fact, I’m clearly insane for even calling you right now given how the conversation about doing this went with your mother. And you should hang up the phone immediately if you care at all about your future."
    tk "Everybody else is so boring, though. At least you’re entertaining in a pitiful sort of way."
    s "I don’t need your pity, but I’ll accept it if I’ve already stooped this low."
    tk "So, what do you want, Jeeves? Is it money? Or...have you done something unspeakable and you require my assistance disposing of the body? Or bodies. How many people have you killed?"
    s "I’d rather not talk about that."
    tk "That many? I’ll send my best men right away. Never fear, Jeeves. Your secret is safe with me."
    s "Tsukasa...I just..."
    s "I wanted to know if you’re..."
    s "If you’re free right now."
    tk "As in...you actually {i}have{/i} decided to take me on as a pupil? Even while Nee-sama is currently going uneducated?"
    s "Touka’s in good hands with someone I trust to...do a much better job than I ever could."
    s "And while I haven’t exactly {i}decided{/i} to start tutoring again...I think I need to meet with you and figure out if I’ll even be {i}able{/i} to."
    tk "Ah! Yes, I’m quite familiar with interviews like this."
    tk "Please come now so I can determine whether or not I will accept you as the man in charge of my education. But do know that I’ve made many a grown man cry during my interviews."
    tk "Oh, and dress nicely. You {i}do{/i} want to make a good impression- don’t you, Jeeves? Especially if you are about to cry."
    s "This...isn’t really the type of meeting I had in mind considering you seemed more than willing to just hand me the job up until today."
    tk "I think this is plenty considering how badly you botched your first attempt at teaching me anything."
    tk "Your interview starts in ten minutes! Tardiness will not be excused."
    s "Tsukasa, I can’t teleport."
    tk "Wow. You peasants really {i}do{/i} have it rough."
    tk "How about this, Jeeves? Close your eyes and think very hard about where you want to be."

    scene dreamsequence1
    with fade

    s "Uhh...okay."
    s "Now what?"
    tk "Open them, of course!"
    s "That’s not going to work."
    tk "You’re going to be a terrible tutor if you can’t listen to simple orders like this, Jeeves."

    scene tsukasainterview1
    with fade

    s "Tsukasa, that’s-"
    s "Wait. How the fuck?"
    tk "Behold the powers of ancient wizardry and infinite wealth! Now, bow down and kiss my foot, for you have entered {i}my{/i} domain and must now do my bidding!"
    s "Yeah, I’m not going to do that."

    scene tsukasainterview2
    with dissolve

    tk "You are refusing my command?"
    s "Yes. Now, tell me how you teleported me here."
    tk "You teleported yourself here, Jeeves. With the help of your imagination. Anything is possible if you try hard and believe in yourself."
    s "No...{i}you{/i} did this."

    scene tsukasainterview1
    with dissolve

    tk "Yes, you’re right. I suppose I did. But I’ll be keeping the source of my powers a secret until after we’re wed. Only then will I let you in on my ancient magic."
    s "This is one of the least believable situations I’ve ever found myself in and I can talk to animals."

    scene tsukasainterview2
    with dissolve

    tk "Perhaps you’re an ancient wizard too, then? I had a feeling you were concealing hidden powers, Jeeves. You’ve passed the first test. But now, you must defeat my four henchmen."
    s "You’re going to...make me fight the dudes standing behind you?"
    tk "Of course. It only makes sense for my tutor to be able to protect me. And you never know when you’ll have to fight off a swarm of bad guys who want to kidnap me for nefarious purposes."

    scene black
    with dissolve

    s "No thanks."
    tk "Jeeves? What are you doing?"
    s "Teleporting myself back home. Anything is possible if you try hard and believe in yourself."
    tk "Not so fast, commoner!"

    scene tsukasainterview3
    with dissolve

    tk "I did not free up my {i}extremely{/i} busy schedule to be toyed with by my interviewee."
    s "And I didn’t swallow the last bit of my pride to come here and fight a bunch of silent, menacing guards."

    scene tsukasainterview4
    with dissolve

    tk "What does your {i}pride{/i} have to do with anything? You should be {i}thankful{/i} to be in the presence of such power and influence. Most would jump at the chance to kiss my feet."
    s "Yeah, well, if I tell you what I meant by that, I’ll have to fight your henchmen whether I want to or not."
    tk "Now I’m confused. Are {i}you{/i} here to kidnap me for nefarious purposes? Because it would be much easier for me to just give you whatever you’re in search of rather than ransoming me for it."
    s "Tsukasa...I don’t know what I’m in search of. I don’t know why I’m here."
    s "It could be confronting a part of myself I don’t want to face or...honestly, maybe just because I see promise in you or something."
    s "Or hey, maybe I’m just so bad at socializing that I feel more comfortable around people who are still as mentally immature as you."
    tk "Are you insulting me, Jeeves?"
    s "Not intentionally. But yeah, probably. To a certain extent."
    tk "I should teleport your innards across the Pacific Ocean to make you pay for such a thing."
    s "Honestly, I’d probably prefer that over this."
    tk "You sure are weird, Jeeves. But it’s that weirdness that makes me want to hire you in the first place. And also the fact that it would make Nee-sama jealous."

    scene tsukasainterview1
    with dissolve

    tk "Interview complete! You’ve got the job!"
    s "{i}I don’t even know if I want it.{/i} Remember? That’s why I’m here in the first place."

    scene tsukasainterview5
    with dissolve

    tk "That’s why you {i}came{/i} here! But now, you’re here for a different reason! To teach me things that many others have failed to teach me! While also keeping me entertained!"
    tk "But also, I’m legally obligated to inform you that you may be executed if you fail to live up to my expectations."
    s "Don’t tempt me with a good time."

    scene black
    with dissolve2

    tk "That’s the spirit, Jeeves! Nothing shows off that commoner mentality better than the acceptance that you may quite literally work yourself to death!"
    s "Where are you going?"
    tk "To my nearest bedroom, of course! You don’t expect me to study {i}outside,{/i} do you?"
    s "Can we maybe go somewhere less {i}private?{/i}"
    tk "But I’ll get distracted if others are present. A quiet environment is conducive to better learning. Even {i}if{/i} I am already a genius."
    s "Tsukasa-"
    tk "Silence, Jeeves! You’ve subjected yourself to my rule and must now do as I say or be forever banished from...everything!"

    "Tsukasa scurries off into the manor as three of her four henchmen stick right to her tail."
    "The fourth one moves behind me and silently urges me to chase after her as best as I can."
    "He’s expressionless. Almost like a doll. And I don’t think it’s unwise of me to acknowledge that as a probability considering the family we’re dealing with right now."
    "In the several glances I’m able to spare over my shoulder, I don’t see him blink even once. But that makes me uncomfortable as I can’t tell what he’s thinking."
    "I just know that if I were lucky enough to be wearing the shoes that he is, I wouldn’t be looking favorably upon me."
    "And Tsukasa shouldn’t be doing that as well — but she’s so excited to peel off the wrapping paper covering Pandora’s box that she spares no skepticism whatsoever."

    play sound "static.mp3"
    scene tsukasainterview6 with flash
    stop sound

    "Then, before I know it, the two of us are locked inside a lion’s cage. But {i}I’m{/i} the lion and she is the plucked and skinned carcass of a game-fowl."

    tk "Welcome to the den of ultimate knowledge! Where countless fools have perished at the hands of Tsukasa Tsukioka and her...ultimate knowledge!"
    s "Your bedroom is two stories?..."

    scene tsukasainterview7
    with dissolve

    tk "This one is. But I’ve been collecting them since I was old enough to walk and will one day inherit all of Nee-sama’s as well. And she has one that’s five stories tall."
    s "That seems...completely unnecessary. And you should probably let your sister keep at least one bedroom."
    tk "Why? She doesn’t even sleep here anymore. She’s always with her weird friend who likes chairs too much."
    s "Ah. I see you’ve met Yasu, then."

    scene tsukasainterview8
    with dissolve

    tk "Come, Jeeves! Look over here!"

    scene tsukasainterview9
    with dissolve

    s "Tsukasa-"
    tk "This way, this way!"

    scene black
    with dissolve2

    "I follow Tsukasa to the other side of the room, prompting her henchmen to follow us. But instead of feeling intimidated by their presence, I’m just thankful they’re here."
    "I doubt I’d {i}do{/i} anything. At least...not purposely. But it’s good knowing that there’s a failsafe in place in the event that my mind decides to go haywire again."
    "Plus, it’ll allow me to keep my thoughts in order and actually be able to {i}teach{/i} for once."
    "I still know how to do that, right?"
    "Wait, what am I even supposed to be teaching her?"

    scene tsukasainterview10
    with dissolve2

    tk "Isn’t the view from here amazing, Jeeves? I bet the one from your tiny, peasant apartment isn’t even close."
    s "I have a house, you know."
    tk "Sorry. You’re just so low on the totem pole that I normally imagine you sleeping inside of a large cardboard box."
    s "..."

    scene tsukasainterview11
    with dissolve

    tk "Hey! Do you want to see something cool?!"
    s "You’re not going to take me to your sister’s five-story bedroom next, are you? This one is...more than sufficient for your first lesson."
    tk "Oh, no. We don’t have to leave. I just wanted to show you a cool trick that Mother taught me. Watch."

    scene tsukasainterview12
    with dissolve

    s "..."
    tk "..."
    s "Was something supposed to-"

    scene tsukasainterview13
    with dissolve
    play sound "dooropen.mp3"

    s "...Oh."
    tk "Cool, right?"
    tk "My servants have taken a vow of silence and can only communicate through hand gestures. Which is {i}kind of{/i} like me knowing a second language when you stop and think about it."

    scene tsukasainterview14
    with dissolve

    tk "I’m still way behind the many languages that Mother knows. But I’m almost guaranteed to catch up at this rate. Don’t you think?"
    s "Sure. Now show me the hand gesture that brings them back inside."

    scene tsukasainterview15
    with dissolve

    tk "Why? Won’t it be easier for the two of us to study in private?"
    s "I’d just feel a lot more comfortable if they sat in and watched."
    tk "Well, I wouldn’t. I get nervous and uncomfortable when I have to do things in front of other people."
    s "You didn’t have any problems sitting in on my class and I have way more students than you have henchmen."
    tk "I have 143 henchmen."
    s "{i}Why?{/i}"
    tk "Because seven of them “quit.”"
    s "Tsukasa-"
    tk "Do you not want to be alone with me, Jeeves? Is it because I annoyed you when we were alone in your office?"
    s "It’s not that..."
    tk "I promise to be good. I really {i}do{/i} want to learn. And if I do anything to annoy you, all you have to do is raise your right hand and I’ll stop talking until you say it’s okay again."
    s "..."

    scene tsukasainterview16
    with dissolve

    tk "Race you upstairs!"
    s "Please don’t..."

    scene black
    with dissolve2

    tk "But that’s where all of my notebooks are!"
    s "Then bring them down here..."
    tk "But I want you to meet my friends! Come on, come on!"

    "I give into her excitement when I know I shouldn’t."
    "I follow her up the stairs when I know I shouldn’t."

    play sound "static.mp3"
    scene tsukasainterview17 with flash
    stop sound

    "And I sit beside her on the bed when I know I shouldn’t."

    tk "The cat is named Trixie. The bear is named Barry. The chicken is named Super Sonic Jalapeno Meltdown Catastrophe Nine-"
    s "{i}What?{/i}"

    scene tsukasainterview18
    with dissolve

    tk "And the whale is named Franklin!"

    play sound "static.mp3"
    scene tsukasainterview19 with flash
    stop sound

    tk "Cool, right?"
    s "...Yeah. Yeah, they’re all really {i}cool.{/i}"
    tk "So, what are we going to study today? Physics? Astronomy?"
    s "Are those really the topics you want to study?"

    scene tsukasainterview20
    with dissolve

    tk "I don’t really know. I’ve always had to follow a very strict regimen when it comes to my education. Mother says it’s the best way to properly exercise one’s brain."
    tk "What I’m unsure of is how that regimen differs from that of the common man. But I imagine it’s quite a bit based on the gap in knowledge between Chinami and me."
    s "Yeah. It is. And, to be completely honest, I don’t know anything about physics."

    scene tsukasainterview21
    with dissolve

    tk "Astronomy then?"

    play sound "static.mp3"
    scene hanabi2 with flash
    scene tsukasainterview21 with flash
    stop sound

    s "Astronomy...makes me uncomfortable."
    tk "Because of the black holes?"
    s "Sure. Let’s go with that."
    tk "Well, what topics are {i}you{/i} interested in, Jeeves? There must be {i}something{/i} considering your history in teaching, right?"
    s "It’d be literature if anything."
    tk "Then, do you want to talk about that book you mentioned the other day? The Catcher in the Rye?"
    s "You..."
    s "You read it?"
    tk "I didn’t have anything else to do when you left Chinami’s room. So I read the whole thing while she watched a strange television sponge."
    tk "I particularly enjoyed the juxtaposition of the protagonist’s idealism with cynicism as it created an interesting dichotomy that paralleled how I often feel as an adventurous girl who must always obey the rules."
    s "You read the entire book in one sitting and came up with all of that by yourself?"
    tk "Did I misunderstand something? Was Holden Caulfield’s idealism naught more than a vessel to showcase hypocrisy in a believable, yet self-aggrandizing way?"
    s "..."
    tk "Jeeves?"

    play sound "static.mp3"
    scene tsukasainterview22 with flash
    stop sound

    n "Akira?"
    s "It’s “Sensei” while we’re here, Noriko."
    n "Do I really have to call you that? It feels super weird after calling you by your actual name for years."
    s "Just while we’re tutoring, okay? Now, tell me — what else did you find interesting about last night’s reading?"
    n "Mostly just the progression of Holden’s feelings concerning simple matters like “youth” and “happiness” over time."
    n "It’s really easy for stories that focus on “coming of age” to come across as preachy and inauthentic but, despite how unbearable he was at times, Holden felt like a very realistic depiction of a teenager."

    play sound "static.mp3"
    scene tsukasainterview21 with flash
    stop sound

    tk "Jeeves? Is your brain exploding again?"
    s "Huh?"
    s "No..."
    s "You just..."
    s "You reminded me of someone else just now."
    tk "Nee-sama, perhaps? It was Mother who originally taught us literary analysis, so it’s quite possible my read on this book would echo that of my sister’s."
    s "I haven’t talked about this book with your sister. And I had no idea you were even going to read it."
    tk "I had no idea we were going to talk about it. I was just bored."

    scene tsukasainterview23
    with dissolve

    tk "But now that I know what you’re interested in, you can teach me all sorts of things and we can {i}both{/i} have fun! Right, Jeeves?!"

    scene black
    with dissolve2

    s "It’s “Sensei” while we’re here, Tsukasa."

    "And so the two of us remain on that bed."

    stop music
    scene ohno

    "{b}UNTIL HER SMILE STARTS TO HAUNT ME AND OUR KNEECAPS TOUCH.{/b}"

    scene black
    play sound "seek.mp3"

    "Something tells me I could fit a ring around her ankles and take back something I have lost with age."

    scene noonsky
    $ renpy.pause(3, hard=True)
    scene nightsky
    $ renpy.pause(3, hard=True)

    $ tsukasaspring1 = True
    $ tsukasa_love += 1

    jump tsukasaspring2

label tsukasaspring2:
    play sound "static.mp3"
    scene tsukasakura1 with flash
    stop sound
    play music "bloodandsunset.mp3"

    "Something tells me that the key to moving forward lies somewhere between the ribs of a young girl, and that if I carefully remove it without damaging the shell that I can become normal again."
    "Or for the first time. Or for the last time. Or for a time I can’t describe because time is just a construct, but an ineffective one as I can’t recall a single moment in which it actually functioned the way it’s meant to."
    "Or the way we meant it to. Or the way we want it to. Or any way at all because, while I grow older mentally, the bodies I long to enrapture don’t add any inches that I’m not personally forcing into them."
    "Somehow or another, we wind up here — my least favorite room in Tsukioka Manor and the one in which I’d want to be buried upon death as it would be equal parts poetic and tragic."
    "But that’s kind of just the way I am now — a mix of somber undertones and pity-pleas that even the most righteous of onlookers can’t help but raise an eyebrow at."
    "It’s just blood and sunset as far as the eye can see, casting a neon glow on an unfortunate torch-bearer and the one he subconsciously wants to set ablaze."
    "Do not mock me, for I am but a bird with a missing voice. All the songs and psalms I want to share with you will stay locked in a journal I buried in eiderdown ‘neath the leftmost center attic floorboard."
    "I bite down on my tongue to try and wake myself back up, but it’s another sensation that halts this narration."
    "A young girl with eyes like muddied honeycomb — and its sugary voice that makes her feel less like a human and more like a sweet, little {i}it.{/i}"

    tk "You said Mother has already shown you this room once before? "
    s "That’s right."
    tk "Do you like it here? Is that why you wanted to come back?"
    s "..."

    scene tsukasakura2
    with dissolve

    tk "You know, it’s really weird. They say the sakura always bloom in spring, but it’s been spring for a while now and this is still the only tree I’ve seen."
    tk "I wonder how mother manages to keep it so perfect all year long?"
    s "Climate control or something like that. Or hell, maybe it’s just magic. If you can teleport people, I don’t even want to think of what Tsubasa might be capable of."

    "We inch closer to the infinite tree and I feel inclined to cover our eyes in duct tape."
    "I can taste sewer water on my tongue, but mistake my dislike for disgust and have to stop myself from regurgitating my breakfast and several bits of the Corey Worm all over an expensive dress."
    "For this white-fronted parrot is not the one you’ve come to abhor nor the one you hate to love — it’s a new one. One that crashed into the window of a moving car and is now minutes away from death."
    "It’s just blood and sunset as far as the eye can see, casting a sickening glow on one particular, poisonous fruit that I’d stay away from most days."
    "But I don’t know how else to detach my mouth from metal grates. And a new taste might be all I can do to rewrite the one I dislike or disgust."
    "Today is unlike all the other days. Today I am free to do as I please under the shadow of a former lover."
    "To make her jealous sounds even sweeter than muddied honeycomb."

    tk "Do you think you’ll continue to tutor me after today, Jeeves?"

    play sound "static.mp3"
    scene tsukasakura3 with flash
    stop sound

    s "It’s “Sensei” while we’re here, Tsukasa."
    tk "Sorry. Do you think you’ll continue to tutor me after today, Sensei?"
    s "Why do you ask? Are you actually having a good time?"
    tk "All things considered, I actually think you’re a rather boring individual. "

    scene tsukasakura4
    with dissolve

    tk "But I suppose there are some qualities I like. "
    tk "We {i}will{/i} need to work on your attire, though. If you’ll be coming to the manor more often, you’ll need to look the part. "
    tk "The last thing we want is the servants discovering there are clothes apart from what we provide them. And I can only imagine what sort of chaos would break loose if we couldn’t immediately identify the staff."
    s "Yeah. All of those human beings having freedom sounds awfully exhausting, doesn’t it?"
    tk "I’m glad you see things my way, Jeeves. I knew I could count on you."
    s "Hey, how about we have our next lesson on sarcasm? That way, you’ll be able to tell whenever I’m subtly belittling you for being a spoiled princess."

    scene tsukasakura5
    with dissolve

    tk "What’s wrong with being a spoiled princess?"
    s "The fact that you’ve likely never been disciplined at any point in your life."
    tk "But I’m disciplined all the time. Just last week, Mother took away my Ferrari for {i}two{/i} hours. It was {i}completely{/i} uncalled for."
    s "Why do you even own a sports car? You can’t drive. "
    tk "But I’ll be able to one day. And until then, I can use it to pretend I’m Xenia Onatopp chasing after James Bond in the 1995 hit American spy movie, “GoldenEye.”"
    s "Well, I guess I can add action movies to the list of surprising interests held by Tsukasa Tsukioka."
    tk "I did {i}not{/i} give you permission to make lists about me, Jeeves. Everyone knows that 90%% of lists end in assassination attempts. "
    tk "I’d be {i}completely{/i} disadvantaged right now if I’d not spent so much time practicing my role as a femme fatale. "
    tk "Any attempt on my life will be sure to end in equal or greater tragedy for those who...attempt it. So you. "

    scene tsukasakura6
    with dissolve

    tk "Wait! That’s why you had a change of heart, isn’t it?! You’re attempting to get close to me so you can kill me! I {i}knew{/i} that statistic about lists was true! Even {i}if{/i} I made it up."
    s "Our lesson after the one on sarcasm will be about how to stop talking."

    scene tsukasakura7
    with dissolve

    tk "If I’m not already dead by then. And who even knows at this point?"
    s "Serves you right for blindly trusting me. You could be walking alongside a very dangerous man right now and you wouldn’t even know it."

    scene tsukasakura8
    with dissolve

    tk "It’s better than walking by myself."
    s "...Is it?"
    tk "Yeah. Because, even if you’re boring, you’re still {i}less{/i} boring than an imaginary friend."
    s "And all 143 of your henchmen?"
    tk "Oh, do they count as people? I wasn’t really sure."
    s "They do. And I get that you’re lonely. I’ve known that since National Tsukasa Day. But you shouldn’t be looking at the time you spend with me as a solution to that."
    s "If I’m going to be your tutor, that’s all I’m going to be. Not your friend. Not someone you can lean on when you feel left out. "
    s "Just a tutor."
    tk "Why are you acting so serious all of a sudden?"
    s "..."
    tk "Come to think of it, you’ve been very strange ever since we left the bedroom, Jeeves. "
    s "Because I don’t want this spiraling into anything else. And I don’t like when you show your weaknesses and vulnerabilities to me."
    tk "Being lonely is a weakness?"
    s "Of course. Anything someone can leverage to take advantage of you is a weakness. "

    scene tsukasakura9
    with dissolve

    tk "Huh...I suppose that’s correct. I never really thought of it that way. "
    tk "But wouldn’t that mean you’re showing me one of {i}your{/i} weaknesses too?"
    s "..."
    tk "You’re lonely as well. Aren’t you, Jeeves?"
    tk "It’s not as if I’m paying you for this. Which means you must have been completely out of other people to talk to if you had to call {i}me{/i} for something to do."
    tk "But that’s okay. As the backup heiress to the Tsukioka Foundation, I’m used to being the “failsafe.”"
    s "Don’t call yourself a “failsafe,” Tsukasa. You’re better than that."

    scene tsukasakura10
    with dissolve

    tk "No one else seems to think so. The only reason I even used that word is because I’ve heard other people say it about me."
    s "What other people? Everyone you associate with is in this building."
    tk "Exactly. They’re the ones saying it."

    scene tsukasakura11
    with dissolve

    tk "We have many servants, Jeeves. And not all of them have taken a vow of silence like my henchmen. "
    tk "They say all sorts of things to one another when they think no one’s listening. And what I’ve learned from that is that I’m not very popular around here."
    tk "So it only makes sense to assume that I’m a “failsafe” for you as well. "
    s "..."

    scene tsukasakura12
    with dissolve

    tk "So, I appreciate your time and all...but we both know you’re only here because Nee-sama is busy."
    s "Are they actually saying things like that about you?"
    tk "Like I said, I’m used to it. "

    scene tsukasakura13
    with dissolve

    tk "But thankfully, I can fire them whenever I want. And I get peace of mind in the fact that their futures are in the palms of {i}my{/i} hands. "
    tk "Just as yours is. So {i}do{/i} remember to be very nice to me even if I {i}am{/i} your second choice."
    s "I’m sorry you have to deal with that, Tsukasa."

    play sound "static.mp3"
    scene amihair22 with flash
    scene tsukasakura13 with flash
    stop sound

    s "Everyone should feel safe inside their own home."

    scene tsukasakura14
    with dissolve

    tk "It’s okay, Jeeves! "
    tk "Besides, it’s not like I don’t hear them talking about more interesting things too!"
    s "Like what?"

    play sound "static.mp3"
    scene tsukasakura15 with flash
    stop sound

    tk "For example...there are rumors of a {i}ghost{/i} in the manor. {i}And they say she haunts this very room...{/i}"
    s "..."
    tk "Oh! Don’t you have a ghost following you as well, Jeeves? Can you ask it if it sees the one that haunts the manor? Mother won’t let me hire an exorcist. She says they’re all con artists."
    s "What else do they say about the ghost here?"
    tk "Hm? Oh. Right."
    tk "Some say that she’s the original gardener from when the manor was first built...and that she died beneath that very tree."
    tk "But {i}others{/i} say she wasn’t from the manor at all. They say she had a connection to that tree from before it was brought here."
    tk "{i}Some{/i} say she’s still buried beneath it. And that the only reason she’s haunting us is because her baby wasn’t buried with her..."
    tk "I’m not sure which one to believe, but I don’t think you can ever be too safe when it comes to ghosts, Jeeves. So if you know any exorcists-"

    play sound "static.mp3"
    scene tsukasakura16 with flash
    stop sound

    "Let them exorcise these cursed thoughts — the ones that always bring you back to me."
    "When these moments of untapped beauty disguised as the plucking of unripe fruit on branches stripped from Yggdrasil scrape against your windows."
    "When you remove yourself from the grasp of your deathbed to press your fingers to the glass and watch, terrified of what lurks beneath the leaves and that violent, whispered wind."
    "Let all of these impurities be buried ‘neath the leftmost center attic floorboard, dressed in eiderdown doused in my old perfume. "
    "Come, Aki-kun."
    "Take it."

    play sound "static.mp3"
    scene tsukasakura17 with flash
    stop sound

    "Come."
    "Take it."

    play sound "static.mp3"
    scene tsukasakura18 with flash
    stop sound

    "COME."
    "TAKE IT."

    play sound "static.mp3"
    scene tsukasakura19 with flash
    stop sound
    play music "sound.mp3"

    onu "come."
    onu "take me."
    onu "feed me."
    onu "my insides feel like heaven. my flesh is warm to the touch."
    onu "i may only be a shadow, but i am the single best shadow you will ever come to know."
    onu "become my sister-maggot and learn everything there is to know about the fruit fly’s wing."
    onu "i can not grant you a web, nor an effervescent dewdrop. but i can be your saving grace at night when the scratches on your glass begin to cut too deep."
    onu "you can feel the whole world inside of me."
    onu "you can feel everything at once."
    onu "and that surely sounds sweet to someone who has never felt at all."
    onu "come."
    onu "take me."

    scene tsukasakura20
    with dissolve4
    $ renpy.pause(3, hard=True)

    s "{i}I’m gonna fuck you so hard.{/i}"

    stop music
    scene tsukasakura21

    tk "..."
    s "..."

    scene tsukasakura22
    with dissolve

    tk "Jeeves, why are you touching my head?"

    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    s "Haaaah! Hah!.....Hah.......haaaah....."

    scene black
    with dissolve2

    "41 6e 64 20 74 68 69 73 20 6c 69 74 74 6c 65 20 70 69 67 67 79 20 63 72 69 65 64 20 77 65 65 20 77 65 65 20 77 65 65 20 61 6c 6c 20 74 68 65 20 77 61 79 20 68 6f 6d 65"

    $ renpy.end_replay()
    $ tsukasaspring2 = True
    $ tsukasa_love += 3

    "{i}Tsukasa’s affection has increased to [tsukasa_love]!{/i}"
    "{i}You feel as if you’ve started something you simply can not stop.{/i}"

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

label tsukasaspring3:
    play sound "phonebeep.wav"

    "I tap on Tsukasa’s name in my phone because it’s what you want me to do."
    "But that’s okay."
    "Because I want you to want me to do it."
    "And I want her to want me to want you to want me to do it."
    "So it’s okay."
    "What I’m doing is okay."

    play sound "phonebeep.wav"

    tk "Hello?"

    "Except it’s not okay at all."

    s "Hey."

    "None of this is."

    play music "ame.mp3"

    tk "Ah! It’s Jeeves again. "
    tk "You’ll have to excuse me as I didn’t save your number the last time you called."
    s "Should I take that as a subtle hint that you don’t want to see me anymore?"
    tk "I never wanted to see you to begin with. You’re not even fit to breathe the same air as me."
    s "Oh, okay. Well, I guess I’ll just hang up then."
    tk "Okay! Bye, Jeeves!"
    s "..."
    tk "..."
    tk "Jeeves, I understand that advanced technological devices like cell phones might be intimidating to you, but if you can figure out how to press the “call” button, surely you can also figure out how to-"
    s "I know how to hang up the phone, Tsukasa."
    tk "Then why are you still taking up my time? You should know by now that I am a very busy girl."
    s "Well, I apologize for interrupting your very busy schedule, but are you able to find any time to fit in some lessons today? "
    tk "What kind of lessons?"
    s "Lessons in Love."

    scene theend
    with dissolve2
    $ renpy.pause(2, hard=True)

    "{i}Thank you for playing!{/i}"

    tk "What was that, Jeeves? The reception in your impoverished neighborhood prevented me from hearing you for a moment."

    play sound "static.mp3"
    scene sky with flash
    stop sound

    s "Just...lessons in general. I don’t have anything else going on and figured now is as good a time as any to get some tutoring in."
    tk "Correct me if I’m wrong, but I’m pretty sure that schedule should be up to me."
    s "You’re wrong. I’m the educational professional here, aren’t I?"
    tk "{i}Former{/i} professional, Jeeves. All you are now is an unemployed hack mooching off the 1%%."
    s "{i}Technically{/i} speaking, I haven’t formally quit yet."
    tk "So you’re still on the company’s payroll despite not doing any work?"
    s "Right."
    tk "{i}Now{/i} you’re talking my language. But I’m surprised. I didn’t think you’d be calling again after the way our last session ended."
    s "Yeah, let’s not talk about that. Are you home right now?"
    tk "{i}Technically{/i} speaking, yes. But it’s not the one you’re familiar with. I’m in my commoner room right now."
    s "Don’t you mean “common room?”"
    tk "No."
    s "Oh. You mean the apartment."
    tk "Shh! If my shareholders hear that I’m spending time in an {i}apartment,{/i} ChinamiCorp is going to steal away even more of the market share than it already has!"
    s "So...am I coming over? Or are you so busy acting poor that you’d rather be alone?"
    tk "I {i}suppose{/i} I can make some time for the sake of my education. But I {i}will{/i} ask you to leave all recording devices at home as I simply can not afford ever being spotted in a place like this."
    s "Can I bring my phone?"
    tk "Yes, but do not be surprised if I ask you to lock it in a safe upon arrival."
    s "Sure, fine."

    scene black
    with dissolve

    s "Go ahead and teleport me now. "
    tk "Teleport you?"
    s "Like you did last time."
    tk "Jeeves, do you suffer from brain damage? I may be rich, but I can not {i}teleport{/i} people. Such a method of transportation hasn’t been developed yet."
    s "But-"
    tk "Anyway! I must be going now, but I’m sure you’ll be able to find the way here on your own! Bye, Jeeves!"
    s "Tsu-"

    play sound "phonebeep.wav"

    s "...kasa."

    "Sighing to myself and wondering whether or not the act of teleportation will ever again be touched on, I set off toward Tsukasa’s apartment."
    "And while I’m willing to chalk that last visit up to just one more strange, paranormal occurrence in a life that is now full of them, I’d more than welcome additional instances of {i}that{/i} one in the future."
    "Because at least {i}that{/i} one makes my life easier and doesn’t pressure me into violating every single girl I come across."

    play sound "static.mp3"
    scene tsukasaapt1 with flash
    stop sound

    tk "Jeeves!"

    "As I step into the room, I think about how this would look to everyone else."
    "Would they be surprised to see that I have fallen this far? Would they shrug it off and trick themselves into believing there’s nothing to it whatsoever?"
    "Or would they be {i}excited{/i} to be shown a glimpse into a life even darker than the ones I’ve stolen all the lights from?"
    "I think the answer would differ from person to person."
    "Right now, though, the ones who I most want to see me are the ones who would take me away. "
    "The Toukas and Futabas. The Norikos and Nikis. And everyone in between who pretends that a moral compass always points northbound when, sometimes, compasses just don’t work."
    "Right now, I am lost."
    "And all I can do is hope that this unlikely candidate can point me back in the right direction."

    s "This...looks different from the other rooms."
    tk "Cool, right? I hired a team of designers to make it look as close to the living quarters of an “average commoner girl” as possible."
    s "And...their idea of “average commoner girl” included suits of armor, crystal chandeliers, and a suitcase full of money?"

    scene tsukasaapt2
    with dissolve

    tk "The suitcase I brought from home. I intended to order a “pizza” today and am not sure what the going rate for those in today’s economy is."
    s "Well, I’m sorry to break it to you, but you might need another suitcase."
    tk "Wow. Life must be really scary out here, huh?"
    s "Yeah. But if worse comes to worst, we can always sell our crystal chandeliers."

    scene tsukasaapt1
    with dissolve

    tk "Exactly! And here you were insinuating that my designers were not accurately replicating the ideal commoner apartment!"
    s "So, remember how I was talking about how your next lesson should be on sarcasm?"

    scene tsukasaapt3
    with dissolve

    tk "That sounds so boring, though. I want to learn about {i}math.{/i}"
    s "Then there is a certain glasses-sporting porn shop employee I think you should meet as you two would get along very well."

    scene tsukasaapt4
    with dissolve

    tk "What’s a “porn shop?”"
    s "Nothing. Anyway, time to learn things."
    tk "You can not just pique the curiosity of a girl as adventurous and excitable as me and then pull the rug out, Jeeves. I could have your hands for such a thing."
    s "Or you could forget I said anything at all and we could start fresh right now. Hi. I’m Sensei. I’m here to teach you stuff."
    tk "About porn?"
    s "Do you have, like...a spray bottle I could shoot you with every time you say something you’re not supposed to say?"
    tk "Do I look like a cat to you?"
    s "Unfortunately, yes. But there’s a certain level of nuance to that answer that even years worth of careful tutoring would not help you understand. Or would. But that makes it even worse."
    tk "I’m starting to think we’re not going to be learning about math today either."
    s "And I’m starting to think this was a very bad idea."
    tk "Like I said on the phone, I’m surprised you even called again. But that’s also what I said last time, so I guess you’re just full of surprises, aren’t you?"
    s "Yeah, but not really in a good way."
    tk "I’ll say. The last person who touched my head like that was eaten by an Irish bloodhound. "
    s "Okay. Let’s move on."

    scene tsukasaapt1
    with dissolve

    tk "Good idea! I’ll get on the bed!"

    scene black
    with dissolve

    s "That’s not what I-"

    play sound "tackle.mp3"

    tk "Come on, Jeeves! It’ll be just like last time! And {i}this{/i} time, you have nowhere to run!"
    s "That’s not a good thing..."

    scene tsukasaapt5
    with dissolve2

    tk "So, I’ve been thinking."
    s "That’s new."
    tk "And {i}that’s{/i} rude. But what I mean is I’ve been thinking about you."
    s "That’s worrying."
    tk "And {i}that’s{/i} confusing. But what I mean by {i}that{/i} is that I don’t really think you’re cut out to be my tutor, Jeeves. So I’m going to have to let you go. I’m sorry it had to end this way."
    s "All things considered, this is probably the best way this could have ended. So thanks, I guess."
    s "You probably could have told me that before I came all the way over here, though."
    tk "I could have. But it would have likely prevented you from hearing my {i}new{/i} job offer. "
    s "{i}New{/i} job offer?"
    tk "Of associate executive literary entertainment coordinator. "

    scene tsukasaapt6
    with dissolve

    s "Pass."
    tk "But I haven’t even described the job yet!"
    s "Yeah, but the title is too long and I know you’d just make me say it all the time."
    tk "It fits your interests a lot better, though! I’m doing this for you!"

    scene tsukasaapt7
    with dissolve

    s "What?"
    tk "Jeeves, as both your previous and future employer, it’s only right that I be honest with you. And the truth is that I never wanted to let you go at all."
    s "You just told me I wasn’t cut out for this like five seconds ago."
    tk "Sometimes, being a CEO means making hard decisions. And also lying repeatedly until you’re caught and the business gets dragged under and you have to file for chapter 11."
    s "...Okay?"
    tk "I still {i}want{/i} you to be my teacher. But I don’t think {i}you{/i} want to be my teacher. So I thought I’d give you a job that better aligns with your specific interests."
    s "...What?"
    tk "Jeeves, I am a rather extraordinary individual. To be frank, I’m {i}very{/i} impressive. But the only time {i}you{/i} seemed impressed the other day was when I was talking about books."
    s "That’s just...what I’m good at, Tsukasa. "
    s "Math and science are important too, yeah. And it {i}does{/i} impress me that you’re willing to dive into physics and astronomy at your age, but...those things are different."

    scene tsukasaapt8
    with dissolve

    s "Anyone can memorize formulas and...star maps or whatever, but {i}not{/i} everyone can understand people. And doing {i}that{/i} is the key to getting what you want out of life."
    s "Maybe. Probably. But also, you probably shouldn’t take my word for that as I still have no idea what I want out of life and I am much older than you."
    tk "What direct correlation does literature have to {i}people,{/i} though? I was under the impression that books were just tools used to get certain themes or ideas across."
    s "And to an extent, they are. But they’re also windows into the way an author views the world. Which, in turn, helps us compare and contrast {i}our{/i} thoughts and values with theirs. Do you get it?"
    tk "I think so. But isn’t that still just like dissecting an animal at the end of the day? We’re still trying to figure something out by reading, aren’t we?"
    s "Look at this way — what’s your favorite book?"
    tk "The Secret Garden by Frances Hodgson Burnett."

    scene tsukasaapt9
    with dissolve

    s "That’s...depressing. And it makes my next question feel kind of loaded, but...how does reading that book make you feel?"
    tk "Free."
    s "..."
    tk "..."
    s "Again, dark. But still, you {i}felt{/i} something, didn’t you? "

    scene tsukasaapt10
    with dissolve

    tk "Oh, so the {i}feeling{/i} you get is the important part! Not the underlying message!"
    s "They’re both important, but that’s what sets literature apart from science. There’s an element of humanity to it that other subjects lack. "
    s "And I don’t know how possible it is to ever be happy if you can’t first grasp just how important one’s {i}humanity{/i} is."

    scene tsukasaapt11
    with dissolve

    s "There are a million complex equations out there, and it takes amazing people to solve the vast majority of them. But {i}we{/i} are perhaps the most complex equation of all. And many just...lose sight of that."
    s "The only reason I even started tutoring was because I wanted to...test that, I guess. "
    s "Because learning the way other people see things makes more sense to me than learning why Sirius is so bright. Or why water somehow keeps sandcastles standing."
    tk "So you became a tutor because you wanted to understand people better?"
    s "I...think so?"

    scene tsukasaapt12
    with dissolve

    s "I just...kind of said that without thinking much."
    tk "That’s very interesting, Jeeves. I’ve never approached literature with that perspective before, but I’ll be sure to think more about my feelings moving forward."

    scene tsukasaapt13
    with dissolve

    s "Do whatever you want. I’m just one person with one outlook when things come down to it. And the idea that {i}anyone{/i} would be willing to listen to that at all still shocks me sometimes."
    tk "I’m the same way, though."

    scene tsukasaapt14
    with fade

    s "What do you mean?"
    tk "I mean I’m confused about why you’re even spending time with me in the first place."
    tk "Nobody’s ever given me this much attention before, and I’m not even {i}asking{/i} you to. You’re just doing it on your own. "
    tk "Well, either that or Mother put you up to it. But {i}you’re{/i} the one who’s been calling {i}me.{/i} Even {i}if{/i} I previously commanded you to take the lead in terms of my education."
    tk "And while it’s nice...and fun...to be spending time with you..."

    scene tsukasaapt15
    with dissolve

    tk "It just makes me feel like you {i}want{/i} something."
    s "..."
    tk "I hope it’s just a different perspective. And if that’s the case, I’ll know why you chose me. "
    tk "But, based on personal experience, a person’s wants are never that simple. And, like you said the other day, leveraging a person’s weaknesses allows you to take advantage of them."
    tk "I’ve got a lot of weaknesses when I really think about it, Jeeves. "
    tk "You could use me for anything you want and nobody would even care."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt15 with flash
    stop sound

    s "Please don’t say things like that..."

    scene tsukasaapt16
    with dissolve

    tk "But it’s the truth. "
    tk "I’m just a failsafe, remember? Disposable. "
    tk "You could lock me in a cage and none of my family would even know about it for months."
    tk "In fact, it feels like that’s what they {i}want{/i} sometimes. All I do is annoy them. And it’s probably the same for you. "
    tk "So if you want something, just say it. You’ve been nice enough to me lately that I wouldn’t mind giving it to you so long as it’s in my power to do so."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "You’ve more than earned it, Jeeves. I mean it."
    tk "Even if it’s something irrational."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "Even if it’s something {i}evil.{/i}"

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "Even if it’s something the world would scorn you for that you’ve wanted to take ever since you first laid eyes on it."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "No one cares about me."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "We can do it right here."

    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt16 with flash
    stop sound

    tk "{b}You can lock me in a cage.{/b}"

    stop music
    play sound "static.mp3"
    scene tsukasakura22 with flash
    scene tsukasaapt17 with flash
    stop sound

    tk "Jeeves?..."
    s "...Huh?"
    tk "I just..."
    tk "I want to know if this is real or not."
    s "..."
    tk "I’m sorry for asking this so bluntly, but..."
    tk "Do you...like me?"

    menu:
        "Pull the plug":
            scene black

            s "Let’s end here for today."

            $ renpy.end_replay()
            $ tsukasarefused = True
            $ tsukasaspring3 = True
            $ tsukasa_love += 1

            "{i}Tsukasa’s affection has increased to [tsukasa_love]!{/i}"
            "........."
            "......"
            "..."

            if day >= 6:
                jump endofsatch4
            else:
                jump endofweekdaych4

        "Take it":
            scene black

            s "I’m doing this because I want to."
            s "No one else is making me."

            $ renpy.end_replay()
            $ tsukasaspring3 = True
            $ tsukasa_love += 5

            "{i}Tsukasa’s affection has increased to [tsukasa_love]!{/i}"
            "........."
            "......"
            "..."

            if day >= 6:
                jump endofsatch4
            else:
                jump endofweekdaych4

label christmastsukasa1:
    play music "tokimekilabyrinth.mp3"
    scene tsukasaxmas1 with dissolve2

    "Otoha and I make it back to the party without drawing much attention to ourselves since I don’t think anyone here really expects me to fuck her."
    "Joke’s on them though because the time has come for me to put the moves on her."

    s "Hey."
    o "Yo."

    "She totally wants me."
    "I’ll leave it here for today, though. Especially since it looks like the time has come for another Christmas tradition of spin the-"

    play sound "static.mp3"
    scene tsukasaxmas2 with flash
    stop sound

    u "Alright, gals! Who’s ready for some Christmas karaoke featuring holiday classics like Ayane’s theme song, Despacito?!"
    s "No. Do the {i}other{/i} tradition. The one where you have to kiss each other."
    o "If it’ll make you feel better, I’ll go kiss Nodoka."
    s "Would you really?"
    o "No. I just wanted to add onto your sadness. It gets me high."
    s "You’re a terrible friend."
    o "I’m a terrible girlfriend too, apparently."
    s "One day, you’re going to decide to settle down and make someone out there very miserable, Otoha."
    o "Aww, I’d be taking after you."
    u "Don’t just stare at me like that, Io! Grab a mic! You know the words!"
    i "I don’t even know the language."
    ay "Spanish! "
    u "Just like your aunt!"

    scene tsukasaxmas3
    with dissolve

    i "Don’t go rewriting people’s ethnicities while everyone is too busy to question them! Someone is going to hear that and think it’s true! "
    ay "¡Canta conmigo, Io! "
    u "¡¿Puedo ir al baño por favor?!"

    scene tsukasaxmas4
    with fade

    i "Yes! Why are you asking {i}me?!{/i}"
    u "Ha! So you {i}do{/i} know Spanish! I caught you!"
    o "Do you ever think about how weird everyone in our class is? Or are you too busy trying to figure out how you’re going to hook up with them?"
    s "Those things are not mutually exclusive. I think of both all the time. "
    o "Who’s the weirdest? If you had to rank them all."
    s "You. Easy."

    scene tsukasaxmas5
    with dissolve

    o "{i}Me?{/i} I feel like I’m super normal by comparison."
    s "Yeah, that’s what makes you the weirdest. You somehow manage to stick out due to how inconspicuous and plain you are. It’s kind of impressive, actually."
    o "Does that mean you’re the most normal then?"
    s "No. It means {i}Yasu{/i} is the most normal."

    scene tsukasaxmas6
    with dissolve

    o "Then {i}that{/i} is what I will take as the true answer to my question. Thank you for your cooperation. I will now be leaving."
    s "Really? You sure you don’t want to hang out for a little while longer? You’re supposed to be lonely."

    scene tsukasaxmas7
    with dissolve

    o "I am. I’m just gonna go be lonely all by myself. Or maybe with Nodoka or something? Stay tuned and you’ll find out."
    s "Fine. But I’m giving you a mission."
    o "No, I will not spike anyone’s drink for you."
    s "I just wanted you to go convince the girls to stop singing and start making out."
    o "I’ll see what I can do. How about you, though?"
    s "I don’t know. I’ll probably just stand here and hallucinate or something. That’s how this normally goes."

    play sound "static.mp3"
    scene tsukasaxmas8 with flash
    stop sound

    mal "How what normally goes?"
    s "Oh, god damn it."
    s "Where have you been, Malvin? I’ve been looking all over for you. Diamond keeps showing up and providing unsolicited advice in the voice of the student council president."
    mal "Spork has been fed. A glutton, he is. So I have returned to provide you advice in place of Diamond!"
    mal "I hope the voice you’ve attributed to me doesn’t cause you as much pain as the student council one does."
    s "I think it’s best if we just don’t even talk about that. What should I do now, though? Go cause a misunderstanding? Pull someone into a dark room?"
    mal "No, idiot! Those are {i}bad{/i} things! You’re a good guy deep down, Akira! We just need to figure out how to put you into a situation that won’t endanger anyone."

    play sound "static.mp3"
    scene tsukasaxmas9 with flash
    stop sound

    mal "Like talking to that one little girl who’s reading a book all by herself in the middle of a Christmas party."
    s "It’s true that I {i}am{/i} supposed to be watching her. Are you sure no one’s being put in danger by me doing that, though? I’m not exactly trustworthy in...virtually any capacity whatsoever."
    mal "Yeah! I know! But you’d never stoop {i}that{/i} low, would you? "
    s "Malvin-"
    mal "Go! Fulfill your duty! She looks so lonely, doesn’t she?"

    "She really does. But this was always going to happen from the moment Tsubasa decided to leave her in {i}my{/i} care rather than that of her ten thousand henchmen."
    "Tsukasa may be smart for her age. And in a lot of ways, she’s more mature than even {i}I{/i} am. But she’s still just “Touka’s little sister” to everyone here. "
    "So the only other person who might know how to handle her at all would be Chika, and I’m not sure Chika is mentally capable of handling {i}anything{/i} other than my penis right now."
    "The thing is, though, I don’t fit in either. Or at least that’d be the case if Imani wasn’t here. But...she wasn’t for a long time. So I know how it feels to not belong."
    "I can relate to her in that respect. And..."

    scene black
    with dissolve2

    "And it’d probably make her happy if someone were to give her attention."
    "That always works for me."
    "........."
    "......"
    "..."

    scene tsukasaxmas11
    with dissolve2

    s "Hey. What are you doing all alone over here?"
    tk "Oh. Hi, Jeeves. I’m just trying to decipher some ancient runes that will help me cast a spell to make everyone care about me."
    s "Well, it seems to have worked on me."
    tk "But I haven’t cast it yet."
    s "Well...right. I just figured that was more of a figure of speech than you {i}actually{/i} trying to learn a spell."
    tk "Why?"
    s "Because...magic isn’t real?"
    tk "Then what am I?"
    s "What are {i}any{/i} of us?"

    scene tsukasaxmas12
    with dissolve

    tk "Jeeves, is Christmas {i}really{/i} the time to get all philosophical like that?"
    tk "I am clearly very busy right now. And you clearly don’t want to be around me anyway since you’ve been running all over the place since you got here."
    tk "I’m just going to read my spellbook and wait for Mother to text me back. I’m sure there will be a helicopter here to pick me up any minute now."
    s "I’m sorry. I’m not used to babysitting. I-"

    scene tsukasaxmas13
    with dissolve

    tk "No one here is being {i}babysat,{/i} Jeeves. I’m perfectly capable of taking care of myself. I’m just...not familiar with any of the girls in your class, so we have nothing in common."
    tk "Which is to be expected, of course. It doesn’t matter how much preparation and time I put into learning their customs if I have very little practical experience...well...{i}practicing{/i} them."

    scene tsukasaxmas14
    with dissolve

    tk "I can just hire {i}other{/i} commoners to speak with for practice. And maybe, a few years from now, I’ll seem more...approachable."
    s "You can talk to {i}me{/i} if you want. I don’t have anything else going on right now."
    tk "You’re only saying that out of pity, aren’t you?"
    s "Would you prefer if just {i}no{/i} one came over to talk to you? Because, if you’re happy over here by yourself, I have no problem fucking off elsewhere."
    tk "..."
    s "..."
    tk "I suppose I wouldn’t mind if you just...also felt like sitting here."

    scene tsukasaxmas15
    with dissolve

    tk "But the moment my helicopter shows up, don’t expect me to stick around. There is no amount of this strange Latin music that I would prefer over a night on the slopes."
    s "You learn to tune it out after a while. I probably wouldn’t expect a text or call if I were you though, Tsukasa."
    tk "Why? Am I finally being put up for adoption?"
    s "What? No. It’s just...your parents are supposed to be enjoying the holiday {i}together,{/i} aren’t they? That’d be harder to do if they had to worry about you the whole time. They probably just want some privacy."
    tk "For what?"
    s "You know...things adults need privacy for."

    scene tsukasaxmas16
    with dissolve

    to "Sensei? What are-"
    tk "You mean like sexual intercourse?"

    scene tsukasaxmas17
    with dissolve

    to "S- what on earth are you talking to my little sister about?!"
    s "...Skiing?"
    to "As if I’m going to believe that!"

    scene tsukasaxmas18
    with dissolve

    tk "Jeeves is telling the truth, Onee-sama. We were just engaging in a discussion about why Mother and Father would require privacy for their ski trip."
    to "R...Regardless of whether or not it was warranted, you should know better than to broach that subject with just anyone, Tsukasa."
    tk "But this isn’t anyone we’re talking about, Onee-sama. It’s Jeeves. I’m sure you’d have no problem discussing this subject with him, so why should I?"
    to "Because it’s {i}inappropriate.{/i} There’s a time and place for topics like that, and I can assure you that a Christmas party {i}on Christmas{/i} is not one of them."

    scene tsukasaxmas19
    with dissolve

    tk "Then how about we play a game instead?! Now that it’s all three of us!"
    to "A...game? I do hope you’re not referring to the one involving the bottle that Otoha brought up to me a moment ago."

    "So she really {i}is{/i} my friend after all."

    tk "How about we play the game where we list the things we want for Christmas?! I’ve seen that show up in several Christmas-themed movies with Chinami."
    to "Is there actually a game like that? "
    s "It’s not really a {i}game.{/i} That’s just...kind of a thing some families and people do so that the totally real human man named Santa Claus knows what to deliver them."
    s "I guess neither of you two would really know about that, though, since you already have everything you could ever want."

    scene tsukasaxmas20
    with dissolve

    to "For this Christmas, I would like a teacher who does not view me as his mother."
    s "Imani exists. It’s a Christmas miracle."
    tk "And {i}I{/i} want Onee-sama’s favorite horse!"

    play sound "static.mp3"
    scene tsukasaxmas21 with flash
    stop sound

    to "{b}I will cut you into pieces, you petulant whelp.{/b}"

    play sound "static.mp3"
    scene tsukasaxmas22 with flash
    stop sound

    tk "Hahaha! Isn’t Onee-sama funny when she makes that face, Jeeves?!"
    s "Woah."
    to "{i}Ahem.{/i} "

    scene tsukasaxmas23
    with dissolve

    to "How strange. I have no idea what came over me just now. Apologies for that rather uncouth display, Sensei."
    tk "Onee-sama always does that when I make jokes about Apollo."
    s "Apollo?"
    to "My beautiful, wonderful, spectacular and prized Misaki. Though, it was my mother who named him and not me."
    to "Regardless, you have been warned many times in the past to never {i}speak{/i} that name, Tsukasa. You are unworthy."
    tk "That’s fine. All I {i}really{/i} want for Christmas is to better understand poor people, anyway."

    scene tsukasaxmas24
    with dissolve

    to "Well, that’s a rather simple wish. Isn’t it?"
    tk "Like Jeeves said — we already have everything else. So if I’m going to wish for anything, it sort of {i}has{/i} to be something immaterial, right? "
    to "I suppose that’s true. But becoming accustomed to the way things work on the outside takes a great deal more than just a {i}wish,{/i} Tsukasa."
    to "The totally real human man named Santa Claus won’t be able to simply place vague concepts and constructs beneath all of our trees."
    s "You guys...get presents underneath {i}all{/i} of your trees? I’ve seen like fifty."
    to "And yet {i}none{/i} of them reserve a place for Tsukasa’s wish."
    tk "I just think it’d be nice to understand more people so I don’t accidentally make Jeeves feel like a loser anymore."
    s "I would appreciate that. Thanks, Tsukasa."
    tk "You’re welcome, loser."
    s "Oh, okay. So you’re totally cool with making me feel like a loser on purpose then."
    tk "Yeah, that’s a different thing. And besides, I’m sure Santa can figure it out! And if he doesn’t, I’ll just ask Father to give him a raise. Santa Claus is probably on Tsukioka payroll, right?"

    scene tsukasaxmas25
    with dissolve

    to "Tsukasa...what exactly would you {i}gain{/i} from such a thing in the first place? "
    tk "Huh? What do you mean?"
    to "Just...the amount of time and energy you’re dedicating to understanding people you won’t ever come into contact with seems rather strange, does it not?"
    to "Apart from Sensei and Chinami, you barely speak to “commoners” at all. And you’ll rarely ever {i}need{/i} to since {i}I{/i} am the heir to the family business."
    to "You’re free to live a life of ease. Why bother making things more difficult for yourself in order to fit into a world you clearly don’t belong in?"

    scene tsukasaxmas26
    with dissolve

    tk "Don’t...belong in?"
    s "Touka, come on. You could have worded that better."
    to "I’m merely trying to protect her, Sensei. And while I’m absolutely not saying Tsukasa {i}doesn’t belong{/i} in your world, I don’t think it’s absurd to say she “doesn’t belong” in your world."

    scene tsukasaxmas27
    with dissolve

    to "We’re lucky enough to come from a family that already possesses all the resources we could ever need. "
    to "And while I’ve absolutely grown to love many people outside of our bubble, I am {i}challenged{/i} by that love every single day. "
    to "We simply don’t fit in here. And I fail to understand the value Tsukasa places in chasing after hardship when a mere Christmas party is enough to cast such a look on her face."
    s "Touka...that’s-"
    tk "No...she’s right."
    tk "Nobody wants me here. "
    tk "No one’s tried to talk to me...and the only reason you two came over in the first place was to keep me company out of pity."
    tk "I know I don’t fit in out there...but I don’t fit in {i}here{/i} either."
    tk "So...where {i}do{/i} I belong then?"
    to "Tsukasa-"
    tk "I just remembered I...I have to clean my room."
    to "You...Do you even know {i}how{/i} to clean?..."
    tk "I’ll figure it out."

    if tsukasaspring3 == False:
        scene black
        with dissolve2

        tk "Goodbye, Jeeves...thanks for coming over to talk to me."
        tk "I hope you get everything you want for Christmas."

        "Touka and I stand there, unsure of what to do as Tsukasa leaves the room."
        "We both know that {s}I’m{/s} we’re supposed to be keeping an eye on her for...whatever reason Tsubasa is trying to keep her away from their meeting..."
        "But we also know it would be wrong to just keep her here if she’s feeling uncomfortable."
        "Touka is clearly conflicted — like she wants to chase after her and tell her that she {i}is{/i} wanted here."
        "She just can’t..."
        "Because she’s always been a terrible liar."
        "And she probably just think she’ll make it worse."

        $ renpy.end_replay()
        $ christmastsukasa1 = True
        $ tsukasa_love += 1

        "{i}Tsukasa’s affection has increased to [tsukasa_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmasfive5

    else:
        scene black
        with dissolve2

        tk "Goodbye, Jeeves...thanks for coming over to-"
        s "Where do you think you’re going?"

        play sound "static.mp3"
        scene tsukasaxmas28 with flash
        stop sound

        tk "Huh? To...clean my room. I just said-"
        s "Yeah, I know what you said. But {i}I{/i} want you here. Touka’s just not very good at getting her point across when it comes to you."
        to "Yes, I...I never intended to make you feel {i}unwanted,{/i} Tsukasa. I just don’t want you to have to struggle if there are ways around-"
        s "I’ve got it from here, Touka. Thanks."
        to "Oh. Oh, I’ll...okay. "

        play sound "footsteps.mp3"

        to "I suppose I’ll just...go check on Yasu then."

        "Touka gets up and walks away, leaving me alone with my latest {i}pupil{/i} and whoever else is smart enough to keep an eye on me while I’m alone with her."

        tk "..."
        s "You okay? You know she didn’t mean any of that-"
        tk "You...stood up for me."
        s "I...guess I did. Yeah."
        tk "Why?"
        s "What do you mean “why?” I didn’t want you getting upset and wandering off over a misunderstanding."

        scene tsukasaxmas29
        with dissolve

        tk "But it {i}wasn’t{/i} a misunderstanding."
        tk "I’m not an idiot, Jeeves. I can tell when people don’t want to be around me. And the only people here who have even noticed me at all are you and Onee-sama."
        tk "I {i}don’t{/i} belong here...or there or...{i}anywhere.{/i} That’s how afterthoughts work and...that’s what I am."
        tk "Even on Christmas, I’ve been pawned off on you like...some kind of unwanted toy. And Mother says it’s because of a ski trip, but..."
        s "Tsukasa, shut up."

        scene tsukasaxmas30
        with dissolve

        tk "Did you just...tell {i}me{/i} to shut up? Who do you think you are?"
        s "Your tutor. And frankly, you should be glad that I’m still taking the time to instruct {i}you{/i} while neglecting my duties at the school."

        scene tsukasaxmas31
        with dissolve2

        tk "..."
        tk "I am..."
        tk "I don’t..."

        scene tsukasaxmas32
        with dissolve

        tk "I’m not really..."

        scene tsukasaxmas33
        with dissolve

        tk "I’ve never..."
        tk "Um..."

        scene tsukasaxmas34
        with dissolve2

        tk "Th..."
        tk "Thank you..."
        s "There’s no need to thank me. I just know what it’s like to be in your shoes."
        tk "You know what it’s like to be extremely rich and talented?"
        s "Uh...no. I know what it’s like to be among a bunch of people you’re completely different from. And so does your sister — which is why she worries about you."
        tk "Onee-sama doesn’t worry about me..."
        tk "She thinks I’m a burden too."
        tk "But you, Jeeves..."
        tk "You...make me feel like...somebody actually {i}does{/i} want me sometimes."
        tk "If you’re being paid for it, you’re very good at your job."
        s "I’m not being paid for it, Tsukasa. You’re just...not the burden you think you are."

        scene tsukasaxmas35
        with dissolve2

        tk "..."
        s "..."

        scene tsukasaxmas34
        with dissolve2
        stop music fadeout 10.0

        tk "I, um..."
        tk "I really do think I...need to go clean my room..."
        s "Tsukasa-"

        scene tsukasaxmas36
        with dissolve

        tk "I’m happy, though...I’m not doing it because I feel sad or left out anymore."
        s "Then why would-"
        tk "I just...um..."
        tk "I know that..."

        scene black
        with dissolve2

        tk "I think...things can only go down from here..."
        s "..."
        tk "Goodnight, Jeeves...and Merry Christmas."
        tk "I didn’t get what I wanted, but..."
        tk "This was just as good."

        "I watch Tsukasa as she walks away."
        "Touka notices and does the same, but doesn’t chase after her."
        "I think both of us are just surprised to see her look so...{i}different{/i} all of a sudden."
        "For Touka, I think that might be a good thing."
        "For me, though? "
        "It’s Hell."

        $ renpy.end_replay()
        $ christmastsukasa1 = True
        $ tsukasa_love += 10

        "{i}Tsukasa’s affection has increased by 10!{/i}"
        "........."
        "......"
        "..."

        jump christmasfive5

label tsukasaspring4:
    scene black
    with dissolve2

    "{i}Far away — where the grass is greener////{/i}"

    play sound "static.mp3"
    scene tsukasacurious1 with flash
    stop sound
    play music "happyandplotting.mp3"

    "Two young girls were spending their afternoon sitting beside one another, shielded from the cruelty of the world in this fortress of an apartment complex."
    "The only problem is that one of them had already been exposed to the cruelty of the world just a couple nights ago when a large man decided to use her room as a love hotel while she was still inside."
    "She hadn’t been able to stop thinking about this ever since it happened. None of the thoughts were good, though."
    "As a matter of fact, none of them were really bad either. They were just thoughts. Confusion. Nothing more."
    "So as she lay there beside a friend, she decided to keep her mouth shut. At least for now."
    "But as she gazed down at a line of arithmetic she’d been using to distract herself, she thought of something to distract her from {i}that.{/i}"
    "She remembered the sounds. Those slapping, wet sounds. Like a slab of meat being thrown onto the table and tenderized by the hands of an inexperienced chef."
    "Maybe she {i}should{/i} speak up? Maybe Chinami had seen something similar? Maybe she would better understand exactly what was happening if she was asked to weigh in?"
    "Which isn’t to say Tsukasa {i}didn’t{/i} understand. She was a smart girl. But there’s a distinct difference between just hearing about open heart surgery and then {i}seeing{/i} it with your own eyes."
    "There are parts that someone without any training just won’t understand. It’ll look scary. Confusing. Gross. And it {i}is.{/i} But it is because it’s {i}supposed{/i} to be. Just like that thing she saw!"
    "What was it called again? Sex? That was the word, right? She remembered the word. And she remembered something about penises and vaginas. How boys and girls have different parts. {i}That{/i} she knew."

    scene tsukasacurious2
    with dissolve

    "But then those memories of the sounds came back. Followed by the memories of the way Jeeves handled that loud woman’s body. Tsukasa had never even been that rough with her stuffed animals before."

    tk "Mmm..."

    scene tsukasacurious3
    with dissolve

    "She lets out a sound on accident. Not to be confused with the sounds that loud woman let out on purpose. She felt good, right? She didn’t {i}seem{/i} like she was in pain. But it didn’t {i}look{/i} particularly fun and-"

    ch "Is something wrong, Tsukasa?"

    scene tsukasacurious4
    with dissolve

    "Good. Now she didn’t have to be alone with her thoughts anymore. All she had to do was not mention sex and-"

    tk "Chinami, what do you know about sex?"

    scene tsukasacurious5
    with dissolve

    "Mission failed immediately. Her curiosity had once more gotten the best of her."

    ch "Wh...What?!"
    tk "Sex. It’s when a man and a woman-"
    ch "Chinami knows what it is! She’s seen it on TV! She just wants to know why you’re asking something so mature!"
    tk "You remember that we had your sister’s Christmas party at my house this year, right?"
    ch "Of course Chinami remembers! She wanted to go but had to stay home alone because the outside world hates her."
    tk "Well, I may have...seen something."

    scene tsukasacurious6
    with dissolve

    ch "Mm...Big sis Chika has been going kinda crazy lately. Chinami thinks she wants Papa to love her more. So if you saw them together-"
    tk "Your sister wasn’t involved. It was Jeeves and some other woman."

    scene tsukasacurious7
    with dissolve

    ch "PAPA, NO!"
    tk "Have you learned about that stuff yet, Chinami? Or, better yet, have you seen your sister and Jeeves do it together?"

    scene tsukasacurious8
    with dissolve

    ch "No! They don’t do that stuff in here! Or at least...not while Chinami is awake! She can’t confirm or deny what happens when she’s sleeping!"
    tk "I see, I see."

    scene tsukasacurious9
    with dissolve

    tk "Oh well. Carry on then, I suppose."
    ch "Y...Yeah. Chinami will...carry on."

    scene tsukasacurious10
    with dissolve

    "And so the two of them went back to their books. One continued to fiddle with numbers while the other was neck-deep in a fight sequence between some green guy and some orange guy."
    "She forgot their names. It was hard to focus at the moment."
    "They stayed like this for quite some time."

    tk "What do you think it feels like?"

    scene tsukasacurious11
    with dissolve

    ch "Tsukasa!"

    "Until they didn’t."

    tk "Is something the matter?"
    ch "Yes! We’re not supposed to talk about this kind of stuff! Stop trying to turn Chinami into a bad girl!"
    tk "But now is the perfect time to discuss topics we’d otherwise be banned from since there’s no one around to tell us we can’t. It’s just like when I give you insider trading tips."
    ch "Those are for Chinami’s secret 401k! She makes an exception for them since they directly impact her future!"

    scene tsukasacurious12
    with dissolve

    tk "Fine. I guess you’re just not mature enough to handle such an adult discussion then."
    ch "Chinami guesses so too. And that is fine with her."
    tk "I guess we’ll just go back to our books then."
    ch "Chinami is way ahead of you..."

    scene tsukasacurious13
    with dissolve

    tk "..."
    ch "..."
    tk "It looked kind of scary."

    play sound "static.mp3"
    scene tsukasacurious14 with flash
    stop sound

    ch "If you’re trying to kill Chinami, at least do it with peanuts!"
    tk "Penis?"

    scene tsukasacurious15
    with dissolve

    ch "Don’t pretend you didn’t actually hear what Chinami said!"
    tk "I don’t know what else to do! I don’t want to tell my mom or my sister because they’ll probably get {i}mad{/i} at Jeeves! And I don’t want to ask Jeeves because...I feel like I...wasn’t {i}supposed{/i} to see that."

    scene tsukasacurious16
    with dissolve

    ch "Did you go somewhere you weren’t supposed to?"
    tk "Oh, no. They did it in my room."

    play sound "static.mp3"
    scene tsukasacurious17 with flash
    stop sound

    ch "PAPA, NO!"
    tk "She’s not going to have a baby now, is she?"
    ch "I...uhh...Chinami...doesn’t think so?"
    ch "She thinks that...there are ways to prevent it? Otherwise she’d have a million little sisters by now."
    tk "A million? You think they do it that much?"
    ch "Chinami doesn’t want to know how many times they do it!"
    tk "Really? Why?"
    ch "Because...she doesn’t. That’s Chinami’s dad. It’s gross. Also, why were they in your room?! "
    tk "Jeeves probably just remembered how exceptional the atmosphere was and wanted to impress that woman. Some sort of mating ritual perhaps?"
    ch "Oh. Maybe {i}that’s{/i} why they don’t do it in Chinami’s house then. Your house sounds better."
    tk "It is better. But that’s beside the point, Chinami. "
    ch "Well, what {i}is{/i} the point?! Because Chinami is feeling very confused and very flustered right now and still thinks we shouldn’t be talking about this!"
    tk "It’s merely a bodily function. And surely the two of us will also be doing things like that one day. Wouldn’t it make more sense to understand them now so we’re not confused when that time comes?"
    ch "Chinami is never going to do stuff like that because Chinami never leaves the house."
    tk "Maybe Jeeves will do it with you if you ask politely?"

    play sound "static.mp3"
    scene tsukasacurious15 with flash
    stop sound

    ch "GET OUT OF CHINAMI’S HOUSE! PAPA WOULD NEVER! EVEN {i}IF{/i} HE IS A LOLICON!"
    tk "What’s a lolicon?"
    ch "SOMEONE WHO WOULD STAND OUTSIDE OF THE DOOR AND LISTEN TO THIS CONVERSATION WITH A WEIRD SMILE ON THEIR FACE!"

    play sound "dooropen.mp3"
    scene black
    with dissolve

    c "Chinami! I’m home!"
    ch "SISTER, NO!"

    play sound "static.mp3"
    scene tsukasacurious18 with flash
    stop sound

    c "Oh, Tsukasa. You’re here too. "
    ch "{i}Communicating telepathically through wizard powers ~ Shhhhh! Don’t say any of that stuff in front of Big sis Chika!{/i}"
    tk "{i}Communicating telepathically through wizard powers ~ Why not? She possesses the information that both of us lack. We can become sex experts with her guidance.{/i}"
    ch "{i}Communicating telepathically through wizard powers ~ Chinami doesn’t want to be a sex expert! She wants to read her manga and find out if the green guy beats the orange guy before Big Sis Yumi takes it back!{/i}"
    tk "{i}Communicating telepathically through wizard powers ~ Do you think Big Sis Yumi is having sex with Jeeves too?{/i}"
    ch "{i}Communicating telepathically through wizard powers ~ No! But between us, I definitely think she wants to.{/i}"
    c "Why do I feel like there’s a whole lot of telepathic communication going on right now?"

    scene tsukasacurious19
    with dissolve

    tk "Chika, can I ask you a question about something?"
    ch "{i}Communicating telepathically through wizard powers ~ Please don’t! Chinami feels like you’re about to make her life a whole lot more difficult! And it’s already too hard for her!{/i}"
    tk "{i}Communicating telepathically through wizard powers ~ Don’t worry. I won’t tell her it was Jeeves. I don’t want that woman to be murdered.{/i}"
    ch "{i}Communicating telepathically through wizard powers ~ That only kind of helps!{/i}"
    c "I still feel like there’s some telepathy going on here, but sure. What’s up?"
    tk "What does “sex” feel like?"

    scene tsukasacurious20
    with dissolve

    c "What does...what?! Where did you hear that word?!"
    ch "{i}Hah...{/i}"
    tk "I was watching one of the presentations my family provides about the reproductive system this morning, but it lacked real world context that I believe would enhance the experience."
    c "Then...ask your mom?"
    tk "My mom hates me now. You’re my only hope."

    scene tsukasacurious21
    with fade

    c "What? Tsukasa, your mom does not {i}hate{/i} you. She loves you very much. Parenting is just...complicated sometimes. But I’m sure she’d gladly help you if you asked her about this."
    tk "Can’t {i}you{/i} just tell me? I know now that’s what you and Jeeves were doing when you played that really loud game at the onsen. "
    c "Jeeves?"
    ch "She’s...talking about Papa..."
    c "I know who she’s talking about. I’ve only gone on one onsen trip. There’s no way I could ever afford to actually {i}pay{/i} to stay in a place like that. And I don’t win radio contests often. Probably since it’s 2020."
    tk "Just tell me — on a scale of one to a thousand, how good does it feel?"
    c "Two thousand. "

    scene tsukasacurious22
    with dissolve

    tk "That’s so high! No wonder you and that other woman were so loud!"
    c "{i}What{/i} other woman?!"
    tk "From...the presentation I watched, obviously! "

    scene tsukasacurious23
    with dissolve

    c "Tsukasa, since I’m only your {i}honorary{/i} sister at this point and not an {i}actual{/i} one, I’m going to keep this lesson extremely brief."
    c "Sex feels good because it’s all about establishing a connection with someone you really care about. When that happens, it’s one of the most amazing feelings in the world."
    c "And sure there are...other contexts where it {i}isn’t{/i} technically about that. But you are {i}way{/i} too young to be getting involved with that stuff, so don’t even worry about that part for now."
    tk "I’m not involved! I only watched! I’m just curious. That’s all."
    c "Watched...the presentation right? That your family put on?"
    tk "Hm? Oh. Yes. Presentation."
    c "So you promise you’re not going to command one of your henchmen to teach you?"

    scene tsukasacurious24
    with dissolve

    tk "Ew! Those guys?! I barely consider them human! If I was going to do it with anyone it’d be-"
    ch "{i}Communicating telepathically through wizard powers ~ DON’T YOU DARE MENTION ANY OF MY PAPA’S NAMES!{/i}"
    tk "American movie star, Seth Rogen!"

    scene tsukasacurious25
    with dissolve

    ch "{i}Communicating telepathically through wizard powers ~ ?!?!?!?!?!?!?!?!?!?!{/i}"
    c "You too?...Seriously?..."
    c "You and your sister both. I just...{i}what?{/i}"
    tk "I...like his laugh?"
    c "Tsukasa...don’t. Just don’t. Ask me again in like thirty years if you’re still curious, okay? Until then, just...do wizard stuff."

    scene black
    with dissolve

    c "Chinami! I’m going to start the bath. Is it okay if I go first today? I have plans in a couple hours and need time to do my makeup again."
    ch "Of course, big sis Chika! Anything for you, big sis Chika! I love you, big sis Chika!"

    play sound "static.mp3"
    scene tsukasacurious26 with flash
    stop sound

    ch "{i}You,{/i} though..."
    ch "I hope you enjoy your stay on Chinami’s shit list..."
    tk "Chinami! You know we’re not allowed to say bad words."

    scene tsukasacurious27
    with dissolve

    ch "Sex {i}is{/i} a bad word, darn it!"
    tk "It is?!"
    ch "Probably! And even if it’s not, it {i}is{/i} in this house! Especially when it’s in relation to Papa! "

    scene tsukasacurious28
    with dissolve

    tk "Fine. But one day, {i}you’re{/i} going to become a woman like me who has witnessed firsthand a bond between lovers and/or very good friends. And when that day comes, Chinami...I will not be there to help you."
    ch "Chinami sure hopes so because she feels like something really bad would need to happen for us to {i}both{/i} witness such a thing at the same time."

    scene tsukasacurious29
    with dissolve

    tk "It’s not as bad as you make it sound, you know. It was kind of just...weird. But also interesting. "
    tk "It didn’t last very long, though."
    ch "Chinami doesn’t know why, but she feels like you’re insulting her dad right now."
    tk "Do you think I should tell him I saw his secret tryst? Or would that be unbecoming of a lady like me?"
    ch "Why {i}would{/i} you tell him? "
    tk "To use it against him as blackmail, of course. What kind of fool do you take me for?"
    ch "The fool who almost made Chinami get “the talk.” Chinami’s avoided the talk forever. You put her streak in jeopardy. "
    tk "What’s this “talk” you speak of? There are many talks in relation to reproductive health. But each one is conducted by a separate-"
    ch "No, Tsukasa. “The talk” is what we peasants call it when our parents or guardians teach us about naughty stuff. We don’t get special presentations or anything like that."
    tk "Then how do you even know about “the talk” before receiving the talk?"
    ch "Everybody learns about “the talk” before getting “the talk.” That’s part of “the talk.”"
    tk "This sounds like a rather convoluted talk to me. "
    ch "It is. So ask your mom if you really want to know. You heard my sister. She doesn’t {i}hate{/i} you."

    scene tsukasacurious30
    with dissolve

    tk "Maybe “hate” is too strong of a word, but..."
    tk "She certainly doesn’t want me. She basically told me outright."
    ch "Tsukasa..."

    scene tsukasacurious31
    with dissolve

    tk "But that’s okay! Tsukasa Tsukioka is stronger and smarter and more mature than {i}anyone{/i} gives her credit for! She’ll prove to everybody just how valuable she is! Mark my...{i}her{/i} words!"
    ch "That just makes Chinami feel bad, so she’s decided to take you off her shit list until you can get back on your feet."
    tk "Nonsense, Chinami!"

    stop music fadeout 10.0
    scene black
    with dissolve2

    tk "I’ve never been {i}more{/i} confident in my future than I am right now!"

    "Life for Tsukasa Tsukioka was looking up all of a sudden!"
    "What could possibly go wrong?"

    $ renpy.end_replay()
    $ tsukasaspring4 = True
    $ tsukasa_love += 1

    "{i}Tsukasa’s affection has increased to [tsukasa_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label tsukasaspring5:
    stop music
    play sound "static.mp3"
    scene tsukasachinamilisten1 with flash
    stop sound
    play music "normalday.mp3"

    c "{i}HARDER!!!!!!!!!!!!! FUCK MY LITTLE PUSSY ‘TIL I’M OVERFLOWING WITH CUM!!!!!! AAAAAHHHHH! AAAAAHHHHHHH!!!!!{/i}"
    ch "TSUKASA!!!!! IS IT OVER YET?!?!!!!"

    scene tsukasachinamilisten2
    with dissolve

    tk "Yes!"

    scene tsukasachinamilisten3
    with dissolve

    ch "Finally! If Chinami had to listen to another second of that-"

    scene tsukasachinamilisten4
    with dissolve

    c "{i}OHHHH FUCK! IT’S SO FUCKING BIG, MASTER! IT’S SO DEEP INSIDE OF ME! CHIKA-CHAN LOVES YOUR COCK MORE THAN ANYTHING IN THE WHOLE, WIDE WORLD!{/i}"

    scene tsukasachinamilisten5
    with hpunch

    ch "AAAAAAHHHHH! YOU LIED TO CHINAMI! NOW, THERE’S NO ONE LEFT FOR HER TO TRUST!"
    tk "Could you keep it down over there? I’m trying to study."

    scene tsukasachinamilisten6
    with dissolve

    ch "Study?! For {i}what?!{/i} We’re still just-"
    tk "Wizards, I know. But {i}as{/i} wizards, shouldn’t it be our responsibility to absorb {i}all{/i} of the world’s secrets and not just the ones our parents {i}want{/i} us to?"
    ch "Chinami doesn’t have parents! They left her and then died respectively! "
    tk "Yes, but you have Jeeves now, don’t you? You’re always calling {i}him{/i} Papa. And I’m pretty sure I heard your sister call him “Daddy” a few minutes ago."
    ch "She’s probably not supposed to do that! But Chinami still doesn’t know the rules when it comes to {i}adult{/i} things!"
    c "{i}Oh my God...yes! YES! JUST...LIKE THAT! MASTER! I’M...CUMMING! I’M...FUCKING CUMMING! AAAAAH!{/i}"

    scene tsukasachinamilisten7
    with dissolve

    ch "Chinami wishes she was born deaf instead of just almost sick all the time."
    tk "They keep talking about “cumming,” but what does that mean? "
    tk "I have discerned that it bears no relevance to transportation whatsoever, and that would imply it’s sexual in nature. But how does one {i}sexually{/i} arrive?"
    tk "Chinami! Check the Internet! Google “cumming!”"

    scene tsukasachinamilisten8
    with dissolve

    ch "No! Chinami doesn’t want to look up naughty words because Tsukasa has decided to be a bad girl!"
    tk "How? It’s not {i}my{/i} fault if I just happen to overhear everything your sister is doing with Jeeves in there. It’s {i}their{/i} fault for being so loud."
    ch "Chinami is gonna give {i}them{/i} a piece of her mind too! She just...can’t go in there right now for obvious reasons!"

    scene tsukasachinamilisten9
    with dissolve

    tk "Ooh! What if you say you forgot something?! And we both just run in really quickly to grab it? That way, we could see them up close and-"
    ch "And burn our eyes out?! Be blinded for life?!"

    scene tsukasachinamilisten10
    with dissolve

    tk "Tsk, tsk, Chinami. You must be forgetting that I have {i}already{/i} witnessed Jeeves’ “alone time” with another girl."
    tk "I’m practically an expert at this now. I only want to see it again because science must be tested multiple times."
    ch "Right...{i}science.{/i}"

    scene tsukasachinamilisten11
    with dissolve

    tk "Well, of course. Why else would I take any interest in what Jeeves does with your sister? "
    ch "Chinami thinks Tsukasa is having an early awakening."

    play sound "static.mp3"
    scene tsukasachinamilisten12 with flash
    stop sound

    tk "Am not! Let’s just look up videos instead. I’ve heard of a thing called “pornography” recently that shows men and women-"
    ch "Chinami knows what pornography is!"

    scene tsukasachinamilisten13
    with dissolve

    tk "No you don’t. You’re the innocent and less smart one here. You can’t possibly know something {i}I{/i} don’t."
    ch "Chinami knows lots of things about lots of stuff! But she understands that these things are supposed to be “forbidden knowledge” at her age, so she just pretends she doesn’t!"
    tk "What’s “cumming” then?"

    scene tsukasachinamilisten14
    with dissolve

    ch "That one Chinami {i}doesn’t{/i} know. But she still thinks you shouldn’t use your computer to find out. Big sis Chika says there’s lots of evil stuff on the Internet."
    tk "There’s lots of evil stuff {i}outside{/i} of the Internet too, Chinami. Our chances of being exploited online are exponentially lower. It’s common sense."
    ch "You raise a good point...but don’t you think this is kind of {i}bad?{/i} We could get into trouble with the...{i}cyber police.{/i}"
    tk "Mother says the police won’t do anything about a Tsukioka, so you should be safe so long as it’s on my laptop. I’m not really sure where to start looking, though. "
    tk "Like, {i}pornography{/i} would obviously need to be hidden so children wouldn’t be able to access it, right? So I doubt just searching for the word would work."
    tk "Maybe...sex videos?"
    ch "Chinami thinks that’s still too direct. We might need to be smarter with what we type in."
    tk "Any ideas? We should make it a serious first try. I don’t want my computer getting flagged by the cyber-police even {i}if{/i} I can bribe them."
    c "{i}God, yes! I love it when you fuck me, Daddy! Give it to me! More! More!{/i}"

    scene tsukasachinamilisten15
    with dissolve

    ch "Sister, no! Don’t you know how thin these walls are?! You’re going to burn Chinami’s ears!"
    tk "“Boy...{i}fucks...{/i}girl.” There. Slang should bypass the filter, right? And I’m pretty sure “fuck” means “sex.” Do you think “cumming” might also be-"

    scene tsukasachinamilisten16
    with dissolve

    tk "Ah! There it is! {i}Pornhub!{/i} I guess the word isn’t banned after all."
    ch "What are we supposed to do {i}now,{/i} though? Because it says this website is for people over the age of-"

    scene tsukasachinamilisten17
    with hpunch

    ch "YOU LIED AGAIN AND CLICKED THE WRONG BUTTON! WHO ARE YOU ALL OF A SUDDEN?!"
    tk "Oh, Chinami. You’ll never last in the outside world if you aren’t willing to lie to get the things you want. This is what {i}needed{/i} to be done. And you’ll be thanking me shortly."

    scene tsukasachinamilisten18
    with dissolve

    tk "There are so many different options, though. Should we just click on one or search for something specific? "
    ch "Ch...Chinami will...let Tsukasa choose..."
    ch "She’s going to look...the opposite way so her eyes don’t bleed."
    tk "Maybe I’ll just try searching for girls our age? There’s probably {i}something{/i} on here that-"

    scene tsukasachinamilisten19
    with hpunch

    ch "Aren’t you supposed to be smart?! You {i}definitely{/i} can’t do that! You’ll get put on some kind of list!"
    tk "A list? Like...what {i}kind{/i} of list?"
    ch "Chinami doesn’t know! That’s why she said “some” kind of list! Just click on one! With adults!"

    scene tsukasachinamilisten20
    with dissolve

    tk "{i}Fine,{/i} jeez. Then how about...oh! Here we go. “Hung Stud Fucks GF’s Little Sister. MASSIVE Cock & LOADS of Cum.” So {i}that’s{/i} how it’s spelled."
    ch "Tsukasa...Chinami still thinks this is a bad idea...Big sis Chika will kill both of us if she finds out."
    tk "Stop being a scaredy-cat. Just don’t let her find out and we’ll be fine. {i}Click.{/i}"

    play sound "static.mp3"
    scene tsukasachinamilisten21 with flash
    stop sound

    ch "Aaaah! Chinami is going to Hell if Hell is real! But at least she’ll still be able to see Tsukasa there!"
    tk "Chinami, calm down. It’s important that we approach this with some level of civility so we can keep a level head when the time comes for us to-"

    scene tsukasachinamilisten22
    with hpunch

    tk "OH MY GOD?! WHAT IS {i}THAT?!{/I} IT’S GIGANTIC!"
    ch "Already?! There wasn’t even any dialogue! Why did they give the movie a title at all?!"
    tk "Is that his {i}penis?{/i} It’s like six inches long! They can {i}get{/i} that big?!"

    scene tsukasachinamilisten23
    with dissolve

    ch "N...Not that Chinami actually cares or...is interested in any capacity, which she definitely is not — but is that bigger than Papa’s was when you saw it?"
    tk "I was kind of far away and I couldn’t really get a good look at it...not like {i}I{/i} actually cared or had any interest either, so...maybe? I’m not...sure."
    tk "And you won’t volunteer to go back into your apartment with me, so there is a chance we’ll never know unless your sister tells us for some reason."
    tk "Or if he “fucks” us instead since there’s a clear precedent of that happening based on the title of this movie."

    play sound "static.mp3"
    scene tsukasachinamilisten24 with flash
    stop sound

    ch "ABSOLUTELY NOT! NEVER! PAPA WOULDN’T! "
    tk "But in the event that he {i}would...{/i}would {i}you?{/i}"
    ch "No! Chinami loves him, but not like that! "
    tk "I’m just saying, Chinami, it sounds like your sister is having the time of her life right now. Have you ever felt that good about literally anything ever?"
    ch "Probably not! But that doesn’t mean I’m going to do it with my sister’s boyfriend! Who is also kind of my dad!"
    ch "You have an older sister too! Are you telling me {i}you’d{/i} do it with my Papa if you overheard {i}them?!{/i}"

    play sound "static.mp3"
    scene tsukasachinamilisten25 with flash
    stop sound

    tk "Not if his is as big as {i}that{/i} guy’s. That just sounds like it would hurt. This girl seems to be enjoying it, though. And she’s a little sister too, so who knows?"
    ch "Ch...Chinami just doesn’t understand why you’re so obsessed with dirty stuff all of a sudden. She misses when we just played games."
    tk "That’s very rude to the actors, Chinami. They worked hard on this. You can tell by how much they’re sweating."
    tk "I still haven’t seen any “cum,” though. Does it just happen on the inside, maybe? Chinami, fetch my notebook. I want to write down some questions I have for Jeeves. {i}He’ll{/i} help me."

    play sound "static.mp3"
    scene tsukasachinamilisten26 with flash
    stop sound

    ch "Chinami begs you to not ask her Papa any questions about this. You have already made her big sister uncomfortable. He is all I have left. "
    tk "Jeeves won’t be uncomfortable answering my questions, though. He’s a teacher. "
    tk "And for all we know, those two really {i}are{/i} studying in there. Mother always said his methods were unorthodox after all. "
    tk "Besides, he’s done it in the same room as me before. And {i}probably{/i} made eye contact with me. I think. Who else {i}can{/i} I ask?"
    ch "Your mom! Like big sis Chika said!"

    scene tsukasachinamilisten27
    with dissolve

    tk "I can’t."
    ch "Why not?"
    tk "Because she’s {i}already{/i} trying to arrange a marriage for me. Asking her questions about sex now might make her speed up the process."

    stop music fadeout 10.0
    scene tsukasachinamilisten28
    with dissolve2

    ch "What?"
    tk "Oh, the little sister’s on top now. That looks far more comfortable."
    ch "Tsukasa, what did you just say?"

    scene tsukasachinamilisten29
    with dissolve

    tk "That the little sister is on top and it looks far more comfortable. You’d know that too if you’d just look at the screen and stop being so afraid of normal human functions."
    ch "Not about that...I meant the other thing."

    scene tsukasachinamilisten30
    with dissolve

    tk "Oh. Yeah. "
    tk "My mom’s trying to set up an arranged marriage. It’s a pretty normal thing in rich families. And it’ll help her get rid of me faster, so..."
    ch "..."
    tk "..."

    play music "hometown.mp3"

    ch "Are you serious?"
    tk "Mhm. And I’m not sure how old the guy will be yet, but if he’s an adult, I don’t want to be blindsided by not knowing what I’m doing when it comes to all this stuff."
    ch "{i}That’s...{/i}the thing you’re worried about? Not...knowing what to do?"
    tk "It’s not the {i}only{/i} thing. I’m worried about a bunch of stuff. Like if he’s mean. What his house looks like. If I can bring my henchmen."
    tk "This is the one thing I can control, though. So if I know all of this stuff by the time we’re married, it’ll be one less thing to worry about."
    ch "And you’re...okay with this?"
    tk "It’s my duty. And..."
    tk "The first chance I’ve ever had to be useful."

    scene black
    with dissolve2
    scene tsukasachinamilisten31
    with dissolve2

    ch "But...But you’re Chinami’s age. You can’t get married yet. That’s not legal, she doesn’t think. "
    tk "I don’t know the logistics of it. I just know that it’s been happening for hundreds of years and that it’ll continue to happen long after the two of us are gone."
    ch "Why would your mom {i}do{/i} that, though? She can’t just...give you away. Why {i}would{/i} she give you away? You guys are the richest family in Kumon-mi, aren’t you? What can you gain by-"

    play sound "static.mp3"
    scene tsukasachinamilisten32 with flash
    stop sound

    tk "Oh, {i}that’s{/i} cum! Eww...It looks kind of gross."
    ch "Tsukasa! This is serious! "

    scene tsukasachinamilisten33
    with dissolve

    tk "I {i}know{/i} it’s serious, okay?! But there’s nothing I can do about it! And chances are, I don’t have the answers to 99%% of your questions so please, just drop it!"
    ch "There’s nothing you can do?! You can’t say no?! To what happens to your own life?! "

    scene tsukasachinamilisten34
    with dissolve2

    tk "I mean..."
    tk "I {i}can.{/i}"
    tk "But why {i}would{/i} I?..."
    tk "Onee-sama is the family’s heir. No one in the manor cares about me. And Mother was part of an arranged marriage too when she was younger."
    tk "She’s the most powerful woman in the whole city now...Something {i}I{/i} will never be."

    scene tsukasachinamilisten35
    with dissolve

    tk "But I need to be {i}something.{/i}"
    tk "The name “Tsukioka” is far too big for a walking back-up plan like me..."
    tk "So maybe a new one will suit me better?"

    scene black
    with dissolve2
    scene tsukasachinamilisten36
    with dissolve2

    tk "Wait, why are {i}you{/i} crying? You’re not the one who has to marry some random person."
    ch "Because that’s the saddest thing I’ve ever heard! And I’ve heard a {i}lot{/i} of sad things, Tsukasa! A lot!"
    tk "I don’t doubt that. Your life is pretty horrible compared to mine. And there are {i}tons{/i} of people who would jump at the opportunity to marry into some rich family."
    ch "You’re not one of them, though! You don’t actually {i}want{/i} this! You’re just doing it because it’s {i}expected{/i} of you! And I...Chinami doesn’t think that’s fair!"

    scene tsukasachinamilisten37
    with dissolve

    tk "Yeah, well..."
    tk "Without knowing what I {i}do{/i} want...there’s no point trying to fight back against the life that was chosen for me."
    tk "If I can do that right, at least I can contribute something to the family before I’m gone..."
    ch "Chinami will find a way...to keep you {i}here.{/i}"

    scene tsukasachinamilisten38
    with dissolve

    tk "..."
    ch "She promises..."
    tk "She shouldn’t. "
    ch "But she does...because she knows this isn’t what Tsukasa wants. "
    ch "And she is going to find a way to protect her even if Tsukasa doesn’t want her to."
    tk "..."
    ch "..."

    scene tsukasachinamilisten39
    with dissolve

    tk "On a...{i}brighter{/i} note...I think your sister and Jeeves might finally be done? Or at least...taking a break?"
    ch "Big sis Chika probably killed him...she’s crazy now and sounded very scary with all of her yelling."
    tk "Well...at least Jeeves died doing what he loved."

    scene black
    with dissolve2

    tk "I just wish I got to ask him some of my questions first..."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ tsukasaspring5 = True

    jump chinamispring5

label tsukasaspring6:
    if _in_replay:
        play music "tsukiokamanor.mp3"

    scene tsukasasexed1
    with fade
    play sound "dooropen.mp3"

    s "The most of {i}what?!{/i} Do you have any idea what you’re doing right now?!"
    tb "Alas! I don’t! If only there was a teacher here to- ah! I’ve found one! Oh, I crack myself up."
    tk "Am I interrupting, Mother? Should I step back out and come inside again?"
    tb "Oh! Tsukasa, dear. I was having so much fun I didn’t hear you enter."

    scene tsukasasexed2
    with fade

    tb "Akira and I were actually just discussing your education and how important it is that we prepare you for {i}every{/i} aspect of life and not just the...academic parts. Isn’t that right, Akira?"
    s "No. It’s not. That’s something {i}you{/i} were talking about. Tsukasa doesn’t want to learn about this stuff from me."

    play sound "static.mp3"
    scene tsukasasexed3 with flash
    stop sound

    tk "What stuff? I’m not really sure what’s going on right now. Was I {i}supposed{/i} to have lessons today?"
    tb "You weren’t, no. But your tutor here was so concerned about your education that he came all the way over just to talk to me about it. Isn’t that kind of him?"
    tk "You really did that, Jeeves? Mother is very busy, you know. You should have just called me if you were that concerned. "
    tk "{size=-1}Without knowing what’s being discussed, however, I can not confirm nor deny whether or not I am comfortable learning something from Jeeves as I imagine there are a great deal of things I know more about than he does.{/size}"
    tb "We’re talking about the reproductive system, dear. {i}Sex,{/i} if you will."

    scene tsukasasexed4
    with dissolve

    s "{i}Tsubasa...{/i}"
    tb "I don’t understand the concern, Akira. I’m right here to supervise the entire ordeal. What could possibly go wrong?"
    tk "Is this...really how we have to do this, Mother?"

    play sound "static.mp3"
    scene tsukasasexed5 with flash
    stop sound

    s "See? Even she thinks it’s weird."
    tb "Does {i}Jeeves{/i} make you uncomfortable when it comes to this subject, Tsukasa?"
    tk "It’s not that I’m {i}uncomfortable{/i} with it, Mother. Jeeves cares more about me than any other teacher I’ve ever had. It’s just..."
    tk "It’s, um...embarrassing when {i}you’re{/i} here as well. "

    scene tsukasasexed6
    with dissolve

    s "{i}Hah...{/i}"
    tb "Embarrassing? Why? I’ve sat in on plenty of your lessons in the past."
    tk "Y...Yes! But this is...{i}different.{/i} Isn’t it? And it’s...it’s not like I’m interested anyway! Just...somewhat curious is all. "
    tb "Well, this is as good a time as any to start asking questions, Tsukasa. Akira and I are both very busy people. And we won’t hold your curiosity against you."
    tb "Just think of him as your father and I’m sure this entire process will feel all the more natural."

    scene tsukasasexed7
    with dissolve

    tb "It shouldn’t be {i}too{/i} bad if you’re just answering questions. Right, Akira? "
    tb "Or perhaps you’d like to run to the restroom for a moment first to prevent the potential onset of any untimely {i}distractions.{/i}"

    scene tsukasasexed8
    with dissolve

    s "Fine. I’ll answer your questions, Tsukasa. But let it be known that I am doing this under duress and your mother is just as capable of teaching you these things as me."

    play sound "static.mp3"
    scene tsukasasexed9 with flash
    stop sound

    tk "In that case, I have several hundred questions that I have prepared in the event that something like this happens. Which order should I ask them in?"
    s "Sorry — several {i}hundred?{/i}"
    tk "Is that too many? How many am I allowed to ask?"
    s "Whatever the bare minimum to satisfy your mother is. "
    tb "I’m quite easily {i}satisfied,{/i} Akira. I’m sure you’d have no trouble at all."
    s "Just...go ahead, Tsukasa. Let’s get this over with."

    scene tsukasasexed10
    with dissolve

    tk "Then...what does it feel like? It’s good, right? Is that why boys cum?"

    play sound "static.mp3"
    scene tsukasasexed11 with flash
    stop sound

    s "Yeah, Tsubasa — this is weird. There’s really no reason for me to be the one who does this even {i}if{/i} you’re here. "
    tk "To be honest, Jeeves, I’m probably more comfortable learning about this from you than anyone."

    scene tsukasasexed12
    with dissolve

    s "You are {i}not{/i} helping right now. Your sister hasn’t even come to me with questions like this yet and she’s {i}far{/i} closer to the age in which people normally learn about this stuff."

    scene tsukasasexed13
    with dissolve

    tb "Oh, what a splendid idea! I should have Touka join us as well. Then no one’s getting any unfair treatment!"
    s "Please don’t."

    scene tsukasasexed14
    with dissolve
    play sound "buzzer.mp3"

    tb "Touka? Can you come to my office as urgently as possible, please?"
    s "{i}As urgently as possible?{/i} Really?"
    tb "Of course. This is time-sensitive information. Tsukasa’s growing every single day."

    play sound "static.mp3"
    scene tsukasasexed15 with flash
    stop sound

    to "You wanted to see me, Mo-"

    scene tsukasasexed16
    with dissolve

    to "Wait, Sensei? Why are {i}you{/i} here?"
    tb "We’re having an impromptu lesson on sexual education. So if you have any questions for Akira here, now is the time to ask them."
    s "Obviously Touka isn’t going to-"

    play sound "static.mp3"
    scene tsukasasexed17 with flash
    stop sound

    to "Oh, excellent. I actually have over a hundred questions prepared if that is okay."
    s "Where did that second chair even come from?"
    tk "You have questions as well, Onee-sama? But you’re a teenager. Haven’t you already learned about this in school?"

    scene tsukasasexed18
    with dissolve

    to "I haven’t, no. Just the presentations we get here — which, as I’m sure you know, do not do a sufficient job of painting the whole picture. "
    tb "They are quite dated, aren’t they? How lucky we don’t need them anymore! Akira — go ahead and restate Tsukasa’s question so Touka can hear it too."
    s "Can’t. Forgot it already. Lesson’s over."

    scene tsukasasexed19
    with dissolve

    tk "It was just about how sex feels, Jeeves. And if the reason boys cum is because it's extraordinarily pleasurable."
    to "It is, yes. That much even I can answer. I {i}would{/i} like to know how such a thing feels for the woman, though. But I imagine Mother’s perspective on that would make more sense to us than Sensei’s."

    play sound "static.mp3"
    scene tsukasasexed20 with flash
    stop sound

    s "Great. Then Tsubasa can answer."
    tb "She can’t. She doesn’t remember."

    scene tsukasasexed21
    with dissolve

    tb "{size=-1}Oh! I know! Why not start by describing each step of the process? What causes it to get hard? How does it {i}feel{/i} when it gets hard? And what about penetration? Is that the best part? I bet that’s the best part.{/size}"

    scene tsukasasexed22
    with fade

    s "There’s a clear {i}best{/i} part and it’s not penetration. That answers Tsukasa’s question about cumming. Are we done now?"
    tk "Not yet! I have several hundred more if that’s okay. "
    tk "Question two — what’s a “blowjob?” Because I know you use your mouth, but it seems hard to have a penis in there and also blow at the same time."
    to "I believe the exhalation provides some sort of additional stimulation if I had to take a guess."
    s "You don’t actually {i}blow{/i} on the penis. You’re not inflating a balloon. You just suck it."
    to "Oh, wow. I’m already learning so much."
    tk "What does it taste like?"

    scene tsukasasexed23
    with dissolve

    s "How am I supposed to know? I’ve never put one in my mouth."
    tk "Not even your own? Why? Is it not big enough?"
    to "Tsukasa! That’s incredibly rude. I imagine it’s just unsanitary to do such a thing."
    tk "But it’s {i}not{/i} unsanitary to do it to other people? How does that work? You’re supposed to know more than me."
    s "Tsubasa...can I please go home now?"

    scene tsukasasexed24
    with fade

    s "..."

    scene tsukasasexed25
    with dissolve

    s "Tsubasa?"

    play sound "static.mp3"
    scene tsukasasexed26 with flash
    stop sound

    tb "How long are men supposed to last on average?"
    to "Mother?! Really?! "

    scene tsukasasexed27
    with dissolve

    tb "What? Am {i}I{/i} not allowed to ask questions? You girls aren’t the only ones curious about this kind of stuff. Let the record show that I’ve lived a mostly sheltered life as well."
    tk "Do you not have sex with Father?"

    scene tsukasasexed28
    with dissolve

    tb "I do not. But you never heard me say that, do you understand?"
    to "{i}I am sorry.{/i}"
    tk "Why not? Do you two not love each other anymore?"

    scene tsukasasexed29
    with dissolve

    tb "Of course we do, dear. But sex doesn’t always have to be about love. Sometimes, two people are just attracted to each other and want to make each other feel good. "
    tk "I see..."

    scene tsukasasexed30
    with fade

    tk "Why not do it with Jeeves then?"
    tb "I’m sorry?"
    to "Ts...Tsukasa! That’s adultery! Mother can’t do such a thing while she’s married to Father! "
    tk "Fine. Then why don’t you do it, Onee-sama? You’re not dating anyone."
    to "That’s somehow even worse!"

    scene tsukasasexed31
    with dissolve

    tk "Ugh, fine. Then you two leave me no choice. {i}I’ll{/i} do it."

    play sound "static.mp3"
    scene tsukasasexed32 with flash
    stop sound

    tk "Only if Jeeves is okay with it, though. I’ve read that consent is very important when it comes to sexual intercourse. "
    to "Um...no? Ew? Gross? Grow up?"

    scene tsukasasexed33
    with dissolve

    tb "Is that something you actually want to do, Tsukasa?"
    to "Um, Mother?! Hello?! She’s a-"
    tb "In a moment, Touka. I’m talking to your sister right now."
    tk "I don’t {i}know{/i} what I want. I don’t know what I’m {i}supposed{/i} to want. "
    tk "Because if {i}you{/i} don’t have sex and {i}Onee-sama{/i} doesn’t have sex, what age am I supposed to be for before {i}I{/i} start doing it?"
    to "Old enough to live on your own at least."

    scene tsukasasexed34
    with dissolve

    tk "We’re in the clear then, Jeeves! I have an apartment! We’re gonna need to keep it down though since I’ve heard how loud that kind of stuff can get."
    to "I will take that apartment {i}away{/i} from you if you’re going to use it for things like that! I meant you must be old enough to {i}buy{/i} one! Not have one gifted to you!"
    tb "What do you think about this, Akira?"
    s "The same way I felt thirty minutes ago — that I shouldn’t be here and this is weird."

    scene tsukasasexed35
    with dissolve

    tk "Because it’s me?..."
    s "Yes, but in whatever way is going to hurt your pride the least. "
    to "Sensei, with all due respect, I think this is the perfect moment {i}to{/i} hurt Tsukasa’s pride as it has clearly gone out of control."

    scene tsukasasexed36
    with dissolve

    tb "Now, now. The reason we’re doing this at all is for Tsukasa’s sake, dear. She’s very confused and is relying on {i}us{/i} to guide her. "
    tb "If you take advantage of her vulnerability to insult her, all it will do is make her lash out in the end. This is the exact moment we should be taking her interest to heart."
    to "But Mother...her interest is having sex with Sensei. Are you {i}not{/i} going to put your foot down?"
    tb "What she wants is a live demonstration, dear. That’s why she asked {i}us{/i} first. "

    scene tsukasasexed37
    with dissolve

    tk "Invite Chinami’s sister over if you have to! Jeeves does it with her all the time, but she won’t even let us stay in the room for it! "
    to "Well, at least {i}someone{/i} I know isn’t outright insane."
    tb "Is there a reason you want to see such a thing up close, Tsukasa? Does a Q&A not suffice to satisfy your curiosities?"

    scene tsukasasexed38
    with dissolve

    tk "Not while you two are in the room...I have a million questions for Jeeves and it’s just confusing with everybody else grabbing his attention. It’s clearly overwhelming him."
    to "You’re right. It’s clearly {i}that{/i} that’s making him uncomfortable."

    scene tsukasasexed39
    with dissolve

    tb "Why don’t you do it then? You’re the most logical pairing for a live demonstration, darling. "
    to "Because that’s crazy! You’re being {i}way{/i} too casual about this! I don’t want to have my first time in the same room as my {i}family!{/i} Have you gone mad?! "

    scene tsukasasexed40
    with dissolve

    tb "{i}Hah...{/i}okay. Looks like it’ll have to be me after all then."
    to "Fine! {i}You{/i} won’t put your foot down?! {i}I{/i} will instead!"

    play sound "static.mp3"
    scene tsukasasexed41 with flash
    stop sound

    to "Come on, Sensei. We’re leaving."
    tk "Ah! Mother! Stop them! Onee-sama is going to go have sex with Jeeves in private! This is not conducive to a proper learning environment!"
    tb "The lesson will have to wait, dear. We should let your sister have sex with her teacher in whatever environment makes her feel most comfortable."

    scene tsukasasexed42
    with dissolve

    to "We will do no such thing! I just don’t want you two badgering him into committing heinous acts for the sake of {i}your{/i} education!"
    s "You also had a notebook until like five seconds ago."

    scene tsukasasexed43
    with dissolve

    to "Being curious is not a sin and I shan’t be judged for it! I know when enough is enough!"

    scene tsukasasexed44
    with dissolve

    to "The two of {i}you,{/i} though..."
    to "This man is not your {i}plaything.{/i} He’s an intelligent, creative, and {i}kind{/i} human being who desperately wants to be {i}better.{/i} And you’re only making that harder for him."
    tb "Is Akira kind? I’ve never noticed."
    tk "He’s nice to me. And {i}very{/i} nice to Chinami’s sister. She was {i}loud.{/i}"
    tb "Oh, I’ve heard. That girl is {i}well{/i} taken care of."
    to "Disgusting..."

    scene black
    with dissolve2

    to "Utterly disgusting..."

    "........."
    "......"
    "..."

    scene tsukasasexed45
    with dissolve2

    s "Thanks for getting me out of there, but...do you really need to keep pulling my hand? I can make it on my own from here."
    to "If I let go, I risk one of {i}them{/i} snatching you up and taking you {i}God knows where{/i} to do {i}God knows what.{/i} I’ll keep my hand right there, thank you very much."

    scene tsukasasexed46
    with dissolve

    s "Just so we’re on the same page here, I really didn’t have much to do with that. Your mom just decided that-"
    to "I am better off not knowing the details. They’ll only make me angrier."
    s "Touka-"

    scene tsukasasexed47
    with dissolve2

    tk "Jeeves! Onee-sama! Wait for me!"
    to "{i}Hah...{/i}how quickly can you run?"
    s "Tsukasa’s not the one you want to be mad at, Touka. We should at least hear her out."
    to "I apologize, Sensei — but I find it hard to {i}not{/i} be mad at a girl who openly wishes to cuckold me, sister or not. "
    s "She doesn’t {i}know{/i} what she’s doing. She’s confused and she’s like that because of {i}me.{/i}"
    to "Yes, and so am I. But you don’t see {i}me{/i} trying to sleep with you in front of my mother."
    tk "Guys! Wait! Please!"
    to "{i}Hah...{/i}"
    to "I am going to regret this..."

    scene black
    with dissolve2
    scene tsukasasexed48
    with dissolve3

    tk "Hah...hah...hah! "
    tk "I’ve never had to...run that fast...for anything...in my life!"

    scene tsukasasexed49
    with dissolve

    tk "Did I do...something wrong?! What...was it?! Tell me...and I’ll...do better...next time!"
    s "Tsukasa-"
    tk "I really want...to learn!...I don’t...want to be...useless anymore!"
    s "You’re not useless, Tsukasa..."

    scene tsukasasexed50
    with dissolve

    tk "But...I am! Onee-sama is...the heir! Mother is...Mother! And I’m just...a tool! Which is fine! That part...is fine!"
    tk "But if I am...to be a tool...I at least...want to be a {i}good{/i} one! I want to know...the things adults know! I want to do...the things adults {i}do!{/i} "
    tk "I want to...grow up {i}now!{/i} So I can see this world...the way you can! Before I’m not a part of it anymore!"
    tk "I’m sorry about Mother too! I wanted to keep her out of this! But I was going to ask you either way, Jeeves! Because {i}you’re{/i} the only one who can teach me!"

    play sound "static.mp3"
    scene tsukasasexed51 with flash
    stop sound

    to "Oh, joy. The man I like is the only one who can teach my little sister about sex. I’ll be damned if this isn’t the start of a pornographic film somewhere."
    s "Tsukasa...I know why you’re trying to rush this whole “growing up” thing...and {i}that’s{/i} what I’m trying to fix right now. This all started because of that."

    scene tsukasasexed52
    with dissolve

    to "Wait...since when do you know about-"

    play sound "static.mp3"
    scene tsukasasexed53 with flash
    stop sound
    stop music fadeout 25.0

    tk "Don’t interfere, Jeeves."
    tk "This is the one chance I’ve ever had to do something good for this family."
    tk "If you take that from me, I will never forgive you."
    s "That sounds better than never being able to forgive myself for not trying."

    scene tsukasasexed54
    with dissolve2

    tk "Why {i}would{/i} you?..."
    tk "Why are you nice to me at all? You have no reason to be. I don’t understand."
    s "I just know what it’s like to be {i}rescued{/i} at your age. And the idea of being on the opposite end of that is too good to shy away from."

    scene black
    with dissolve2

    s "That’s why I’ve done this before — taken someone under my wing when the safer thing to do would be to just push them out of the nest and let them figure things out on their own."
    s "Not all wings are made equally. Some are much sharper than others. Do you know what I mean, Tsukasa?"
    tk "I...don’t..."
    tk "No..."
    to "Sensei...I think you should leave now. "
    s "Yeah..."
    s "I think you’re right."

    "Touka escorts me to the gate while Tsukasa remains in place, watching with tears in her eyes as I fade from her view."
    "But I will be back."
    "Whether I want to be or not."
    "And I will slice up one more fledgling so badly that it will have no choice but to return to its nest forever."

    $ renpy.end_replay()
    $ tsukasaspring6 = True
    $ tsukasa_love += 10
    $ tsubasa_love += 5

    "{i}Tsubasa’s affection has increased by 5!{/i}"
    "{i}Tsukasa’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    jump tsubasaspring5
