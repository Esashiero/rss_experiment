label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
    if tsuneyo_love >= 10 and ramen5 == True and tsuneyodorm5 == True and ramen10 == False:
        jump ramen10
    if tsuneyo_love >= 15 and christmas7 == True and ramen15 == False:
        jump ramen15
    if tsuneyo_love >= 20 and tsuneyodorm20 == True and ramen20 == False:
        jump ramen20
    if tsuneyo_love >= 25 and secondbeach18 == True and ramen25 == False:
        jump ramen25
    if tsuneyo_love >= 30 and ramen25p2 == True and tsuneyodorm25 == True and ramen30 == False:
        jump ramen30
    if tsuneyo_love >= 35 and yumispring6 == True and tsuneyospring5 == False:
        jump tsuneyospring5
    if chap4active == True:
        jump tsuneyospringramengen
    if chapthreeactive == True:
        jump tsuneyosummer2ramengen
    if christmas7 == True:
        jump tsuneyonightgen2
    else:
        jump ramengen

label tsuneyoarchery:
    if chap4active == True:
        jump tsuneyospringarcherygen
    if chapthreeactive == True:
        jump tsuneyosummer2archerygen

label calltsuneyomorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Tsuneyo's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't. Maybe she's at the archery range?"

        jump callmorning
    else:
        jump tsuneyocallmorninggen

label calltsuneyoafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Tsuneyo's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."

        jump callafternoon
    else:
        jump tsuneyocallafternoongen

label calltsuneyonight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    else:
        "Tsuneyo should be working right now. I can probably see her if I go to Tojo Ramen."
        jump callnight

label tsuneyonightgen2:
    scene tsuneyonightgen2
    with dissolve
    play music "kashiwagi.mp3"

    "I make my way to the second half of town to visit Tojo Ramen and, by association, Tsuneyo Tojo."

    t "Ah-"
    s "Huh? What?"
    t "You just thought of my name."
    s "How do you know that?"
    t "I could feel it."

    "..."
    "Anyway, Tsuneyo and I spend the night awkwardly discussing the things she likes about noodles because, let's face it, that's the only conversation topic this girl is able to hold at the moment."
    "It's a bit stressful trying to keep up with her on the subject matter, but I distract myself with the glorious comfort food that is this greasy bowl of flavor."
    "Tsuneyo must notice it as well as something resembling a smile spreads across her face each time I take a sip of the broth."
    "I'll never stop being surprised at how easy it is to make some people happy."
    "If sitting at a counter and scarfing down the food she makes is all it's going to take for me to grow closer to her, I'll gladly come here any night of the week."

    scene black
    with dissolve

    "I just wish she didn't work in such a horrible part of town."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo's affection has increased to [tsuneyo_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramengen:
    scene firsttsuneyoramen1
    with dissolve
    play music "kashiwagi.mp3"

    "I head to Tojo Ramen to grab a quick bite to eat and chat with Tsuneyo."
    "Under most circumstances, I'd avoid going all the way across town just for food."
    "But something about this place just keeps pulling me back."
    "I'm not sure if it's the broth or...the strange conversations to be had with the self-proclaimed 'Samurai of Flavor,' but I really {i}do{/i} enjoy my time here."
    "I just wish it wasn't so far away."

    scene black
    with dissolve

    "I stay for another thirty minutes or so after finishing my meal and Tsuneyo tells me more stories about her childhood."
    "I'd like to say that they're normal or wholesome stories, but the fact is that everything she tells me is rather weird..."
    "I chalk it up to her just being born strange and decide to head home after sliding some money across the table, leaving a generous tip behind."

    t "I can't accept this. It is not culturally acceptable."
    s "Just take my fucking money, Tsuneyo."
    t "Ah-"

    "Tsuneyo reluctantly nods in appreciation and parts with an expectedly formal goodbye..."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "... "

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen1:
    scene firsttsuneyoramen0
    with dissolve
    play music "kashiwagi.mp3"

    "I show up at a seedy ramen shop in the second half of town."
    "A noodle-sanctuary in a land of shit."
    "Or as Tsuneyo calls it, home."
    "The walls are stone and stained with years worth of pork broth condensation, turning what I’m sure was a once-spotless restaurant into..."
    "Well, into this."
    "But this is the ideal place for a dish like ramen."
    "It’s not meant to be fancy. It’s not meant to be {i}gourmet.{/i}"
    "It’s just food that warms the heart."
    "Or at least what’s left of it."

    scene firsttsuneyoramen1
    with dissolve

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."
    s "..."
    s "Tsuneyo."

    scene firsttsuneyoramen2
    with dissolve

    t "Ah-"
    s "You do realize it’s me, right? Your teacher?"
    s "You don’t have to give me the same customary greeting that you give everyone else."
    t "There is no customary greeting. Everyone else just sits down."
    t "I have decided to greet you as today is a day to celebrate."
    s "To celebrate {i}what{/i} exactly?"
    t "A curse free life."
    s "You’re still going on about the curse?"
    t "I am. The Emerald Guardian informed me that it was not a curse after all. Who knew?"
    s "I did. I literally told you."
    t "I don't remember that."
    s "Well, it happened."
    t "I apologize. I often find myself having a hard time paying attention while you're talking."
    t "But you are alive. And that is all that truly matters."
    s "I'm offended by the first part of that statement, but applaud you for ending on an insightful note."

    scene firsttsuneyoramen3
    with dissolve

    t "I am full of nothing but wisdom and noodles."

    "Tsuneyo passes me a menu after having just fulfilled her noodle-mention-quota for the night."
    "I take a moment to look it over and realize that everything on the menu is insanely cheap."
    "It didn’t occur to me the first time I came here since I...wound up paying for two people, but I’m surprised Tsuneyo’s family is even able to stay in business with prices like these."
    "I feel like they haven't been updated in decades."

    s "Hey, Tsuneyo."

    scene firsttsuneyoramen2
    with dissolve

    t "Ah-"
    s "Why is everything so cheap here?"

    scene firsttsuneyoramen1
    with dissolve

    t "Cheap?"
    s "Yeah. You’re charging next to nothing for virtually every dish on the menu."
    t "Oh. You mean {i}cheap.{/i}"
    s "...That’s exactly what I said?"

    scene firsttsuneyoramen4
    with dissolve

    t "I suppose it may have something to do with the people who live in this half of town."
    t "I’m sure you have noticed, but the old district is not in the best of shape."
    t "The most populous demographic in the area is the elderly. And next is the poor."
    t "Everyone else lives much further away."

    scene firsttsuneyoramen1
    with dissolve

    t "All of the people stuck here are simply waiting to die."
    s "That’s...dark."

    scene firsttsuneyoramen3
    with dissolve

    t "Yes. I suppose it is."
    s "..."
    t "..."

    scene firsttsuneyoramen1
    with dissolve

    t "Do you know what you’d like to order?"

    "What kind of mood whiplash is this? Jumping straight from condemning the entire population here to taking my order?"
    "I know Tsuneyo doesn't have much experience holding conversations, but...she at least has to learn how to transition between topics."

    s "Uhh...can you tell me what the “Red Dragon” is?"
    t "It is the red version of the Green Dragon."
    s "So it’s...spicier, I’m guessing?"
    t "Yes. Just like in ancient times."
    t "The red dragons were much more dangerous than the green ones."
    s "But dragons didn’t actually exist in ancient times. Those were just fairy tales."
    t "..."
    s "..."

    scene firsttsuneyoramen5
    with dissolve

    t "..."
    s "Did you...really not know that?"
    t "This is a shocking revelation."
    t "All this time, I have been explaining the difference between the dishes by mentioning the dragons of ancient times."
    t "Why did no one stop me?"
    s "Well, you deal with mostly old people, right? They probably thought it was cute that you still believed in them."
    t "Are old people actually evil?"
    s "A lot of the time, yeah."

    scene firsttsuneyoramen6
    with dissolve

    t "I must remain vigilant in the face of the elderly. They could attack at any moment."
    s "It's fine. They'll die before the rest of us, so you likely won't have to remain vigilant for very long."

    scene firsttsuneyoramen1
    with dissolve

    t "I look forward to that day with great anticipation. Praise be."
    s "Praise be."
    s "Wait, what are we praising?"
    t "Noodles, perhaps?"
    s "Well...anyway, I guess I’ll have the Green Dragon since it's...less red than the Red Dragon."
    t "I understand."
    t "One Green Dragon, coming up."
    t "As a word of advice, dragons are not real. The dish is based on a fictional creature from fairy tales."
    s "Yes, Tsuneyo. I am the one who taught you this."
    t "You are lying. This is information I have known all along."
    t "Now, please excuse me while I go craft a dish named after a fictional creature that did not actually exist in ancient times."

    scene firsttsuneyoramen0
    with dissolve

    "Tsuneyo disappears behind the curtain leading to the kitchen and I can hear her beginning to search through some shelves or cabinets or something."
    "I wonder why she’d need to go back there when it looks like all of the ingredients are right behind her?"
    "Maybe the Green Dragon requires some sort of...{i}special{/i} ingredients they store in the back?"
    "Oh well. Not like it matters anyway. I’m just glad to be able to eat something."
    "Coming to this part of town is always draining, both physically and mentally- and I'm barely able to stay awake as-is."

    scene firsttsuneyoramen1
    with dissolve

    t "I have returned."
    s "Oh, good timing."
    t "This ain’t my first rodeo, bro."
    s "Still at it with the whole informal speech thing?"
    t "Am I improving?"
    s "You're getting worse, actually. That was extremely unnatural."

    scene firsttsuneyoramen6
    with dissolve

    t "Ugh..."
    s "It’s fine. I’m already teaching one girl how to improve her public speaking and, weirdly enough, you seem much more open to learning."

    scene firsttsuneyoramen7
    with dissolve

    t "You offer additional classes?"
    s "Well...not {i}exactly.{/i} I kind of just show up to her work every once in a while and...accidentally insult her until she improves."
    t "Did you come here to insult me?"
    t "On my home turf?"
    t "Watch your step, bro."
    s "Tsuneyo, you can’t just keep adding bro to sentences to make them informal. That isn’t how it works."
    t "Are you sure? Because I have studied our Yakuza clientele and have heard them use that word many times before."
    s "Why in the world are the Yakuza coming to a ramen shop in the middle of the old district?"

    scene firsttsuneyoramen8
    with dissolve

    t "Because I am a food magician. "
    t "My flavors are unparalleled in the world of ramen."
    t "They also occasionally used the back room to do business before my father fell ill."
    s "What kind of business were they doing back there exactly?..."
    t "Apparently, they work in real estate."
    t "And all this time, I thought they were some sort of gang."
    t "If more people knew their true goal was to provide affordable housing, I believe less people would fear them."
    s "..."
    t "..."
    s "You're not serious, are you?"

    scene firsttsuneyoramen9
    with dissolve

    t "Huh?"
    t "What did I do now?..."
    s "Nothing, Tsuneyo. I can’t teach you two valuable life lessons in one day."
    t "Why is talking to you so much harder than it is talking to anyone else?"
    s "Who knows? Even I don’t understand my actions sometimes."
    s "It’s like, I’ll just be walking around, minding my own business...and suddenly, I’m sitting in a ramen shop teaching some girl about dragons."

    scene firsttsuneyoramen1
    with dissolve

    t "That sounds extremely similar to what happened here today."
    s "It {i}is{/i} what happened here today."
    t "Oh. Right. Of course."
    t "..."
    t "Perhaps it was hunger that landed you here? That would make sense, would it not?"
    s "It would, but I don't think that's something you need to verbally rationalize."
    t "Would you prefer to eat in silence?"
    s "I don’t even have any food yet."
    t "It’s cooking."
    t "The Green Dragon requires special preparation."
    s "What kind of special preparation? I don't even know what I-"
    t "Snake venom."
    s "..."
    t "..."

    "Don’t tell me that’s what she was doing when she went into the kitchen?"

    s "On second thought, I don’t know if I want the Green-"
    t "It was a joke."
    s "..."
    t "Surprise."
    s "You really need to work on your delivery."
    s "Everything you say comes out in the same tone, so I can never tell when you’re kidding or not."
    t "Do you really think we would use snake venom in ramen?"
    t "That is absurd."
    t "It would never work."
    t "..."

    scene firsttsuneyoramen10
    with dissolve

    t "Unless..."
    s "Unless what? What are you thinking right now?"
    t "Tell me- how much do you cherish your life?"
    s "Enough to not agree to whatever you want me to agree with. "
    t "That is a shame. I had an excellent idea for a new menu item."
    s "How is it excellent if you don’t even know it’s safe to consume?"
    t "With great risk comes great reward. Thomas Jefferson said that."
    s "Thomas who?"

    scene firsttsuneyoramen11
    with dissolve

    t "Is he a mythical creature as well?!"
    s "No, I just wanted to see how you'd react if I pretended he was."

    scene firsttsuneyoramen12
    with dissolve

    t "That’s a relief. I was beginning to think everything I was taught had been a lie."
    t "Life was much simpler before I had to begin using my knowledge in real life."
    s "Yeah. I can see how homeschooling might leave some people behind."

    scene firsttsuneyoramen1
    with dissolve

    t "I will do my best to learn the right meanings to things in your class."
    s "Just...try and have fun. Knowledge comes second."
    t "I understand. I will do my best to prioritize having fun over improving myself as a person."
    s "There you go. Just don’t expect too much from me and I'm sure you'll have a decently fulfilling school life."
    t "My expectations could not be any lower."
    s "Well, that's kind of insulting."
    t "Another joke. Ha ha ha ha ha."
    s "The {i}real{/i} joke here is your sense of humor."
    t "..."
    s "..."
    t "..."
    s "..."
    t "Wow. You’re even worse than I am."
    s "That was not my proudest moment just now."
    t "You should be ashamed."
    s "I am. You don't have to-"
    t "Get out of my restaurant, you bastard."
    s "..."
    t "..."
    s "That was a joke too, right?"
    t "..."

    scene firsttsuneyoramen8
    with dissolve

    t "I’ll be right back."

    scene black
    with dissolve2

    "Tsuneyo disappears behind the curtain yet again and retrieves a large green bowl filled with assorted toppings."
    "She ladles the broth from behind her into it and places the dish in front of me."
    "After combing through it with my chopsticks to confirm that there are no traces of snake parts or any other strange ingredients, I dig in."
    "........."
    "It’s heavenly."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen1 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen5:
    scene tsuneysecondramen1
    with dissolve
    play music "kashiwagi.mp3"

    t "..."

    "I enter the ramen shop to be greeted by yet another blank stare from none other than the Kendo princess of whatever."
    "I’ve never been good with nicknames."

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."
    s "That’s exactly what you say every time I come here."
    t "Please let me know if you have any questions."
    s "I don’t have any questions, Tsuneyo. "
    t "I see."
    t "Then let me know when you are ready to order."
    s "Woah. Where’s your normal “Ah-” that happens almost every time I say your name? I was just starting to get used to it."
    t "I must have forgotten."
    s "Are you sure you’re not just getting comfortable around me?"
    t "Is there a reason for me to be uncomfortable?"

    if bonus == True:
        s "Well, yeah. I’m an older guy and you’re a girl. Doesn’t that sort of thing happen naturally?"
        t "Does it?"
    else:
        s "I exude cool dad energy. I figured it would start like, making you want to learn how to grill or something."

    t "I am alone with my father often and have never once felt uncomfortable."
    s "Well that’s your father. It’s different."
    t "I don’t understand how."
    t "We are all humans."
    t "Man. Woman. Child. Dog."
    t "We all breathe air and we all eat noodles."
    t "Such is life."
    s "Once again, I think your philosophical side is falling a bit short."
    t "I’ll get it one day."
    s "Also, I’m not sure if I have to actually remind you this or not, but dogs don’t count as humans."
    t "They should. "

    scene tsuneysecondramen2
    with dissolve

    t "Have you ever had a dog, Sensei?"
    t "I did when I was younger. "
    s "...Please tell me that you didn’t snap its neck and serve it to customers."

    scene tsuneysecondramen3
    with dissolve

    t "Disgusting."
    t "You should be ashamed of yourself for even thinking that."
    t "He was killed humanely and not served to anyone. He’s buried several blocks from here in an empty lot."
    s "Oh. Uhh...Sorry for your loss?"
    s "I’m not really sure how to follow up to a spontaneous reveal like that."

    scene tsuneysecondramen2
    with dissolve

    t "It’s okay. Sickness gets to everyone eventually."
    t "Just as I’m sure it will claim you and I someday."
    s "That’s less philosophical and more depressing. I give it a 6/10."
    t "A passing grade. I accept."

    "Tsuneyo begins to fidget with something behind her back, adjusting her shoulders so I can’t see whatever it is she’s holding."
    "But knowing her, I imagine it’s some sort of noodle-related paraphernalia."

    s "Are you hiding something from me, Tsuneyo?"

    scene tsuneysecondramen1
    with dissolve

    t "Of course."
    t "I’m hiding many things from you. It is common nature to not open up right away to someone you don’t know or trust."
    s "No, like literally hiding something. Behind your back."
    t "Oh."
    t "Yes."
    s "..."
    t "..."
    s "Why?"
    t "..."
    t "I don’t know."
    s "...Can I see it?"
    t "Sure."

    scene tsuneysecondramen4
    with dissolve

    s "..."
    t "..."

    "Tsuneyo brings the object she was hiding into view and it is...a large chef’s knife."

    t "Prepare to die, you bastard."
    s "Tsuneyo, would you mind explaining to me why you were hiding a knife behind your back this entire time?"
    t "It will be a boring explanation."
    t "Would you like to hear it anyway?"
    s "Yes, please. I’d like to confirm that I can still come here without the risk of being murdered."
    t "You walked in while I was cutting ingredients and I forgot to put it down."
    t "By the time you got to the counter, I realized I was still holding it and hid it behind my back so you wouldn’t think I was going to kill you."
    s "Oh. That actually {i}is{/i} a boring explanation."
    t "I know."
    s "But wait. Then what was with that “Prepare to die, you bastard” line?"
    s "Why would you say that if you didn’t want me to think you were going to kill me?"
    t "I thought it would help create a more fun atmosphere for the ramen shop."
    t "I can see it now. People flocking in from all over the world because of the quirky, upbeat ramen girl, Tsuneyo Tojo."
    s "Quirky and upbeat are perhaps two of the only words I would {i}not{/i} use to describe you."
    t "Then I will have to end your life."
    t "Prepare to die at the hands of the flavor-samurai. "
    s "Can I at least have one last bowl of ramen before I pass on? "

    scene tsuneysecondramen5
    with dissolve

    t "Of course. A death is not truly honorable unless you are full of noodles."

    "Despite these one liners and philosophies (If you even want to call them that) making absolutely no sense, they’re definitely...amusing. "
    "It’s actually kind of impressive how horrible Tsuneyo is at communicating."
    "Either that or she’s actually way better at it than she lets on and is simply pulling my leg in every single conversation."
    "Maybe she’s some sort of super genius and I’m just not aware of it?"

    t "..."
    s "..."
    t "...?"
    s "What? Why are you looking at me like that?"
    t "I’m waiting for your order."
    t "It is your last meal, so I will make sure it is one to remember."
    t "Even if you won't actually get to remember it."
    s "Wait, you’re not actually going to kill me, are you?"
    t "You have insulted the integrity of the Tojo family. I must do my job and uphold it by any means possible."
    s "How can you say something so serious with a smile on your face?"
    t "Because I’m joking."
    s "Really? You kept this one going for so long that I was beginning to think you might actually be serious."
    t "Killing a customer during store hours would lead to bad reviews."
    t "We’d need to create a new tag line just to get the restaurant back on track."

    scene tsuneysecondramen6
    with dissolve

    t "Tojo Ramen. All of the flavor, none of the violence."
    t "Something like that."
    s "What a totally inconspicuous slogan for a store where the Yakuza hang out."

    scene tsuneysecondramen5
    with dissolve

    t "Real estate is not a violent business, Sensei. You should know this if you are going to teach people."
    t "I lack any sort of formal education and even I know that."
    s "Tsuneyo, the Yakuza are more than just-"
    s "Ahh, fuck it. What’s even the point?"

    scene tsuneysecondramen7
    with dissolve

    t "The curse appears again..."
    s "Didn’t you learn that “Fuck” isn’t an {i}actual{/i} curse, though?"
    t "That does not make it any less intimidating. "
    t "If I told you the knife I am holding is plastic, you would still fear it, wouldn’t you?"
    s "...Not really. No."
    s "Even if you are some sort of Kendo god, I don’t think you’d have it in you to actually kill someone."

    scene tsuneysecondramen1
    with dissolve

    t "Would you?"
    s "Kill someone?"
    t "Yes. Would you be able to take the life of another person? And if so, why?"
    s "You’re not an undercover cop or anything, are you?"

    scene tsuneysecondramen2
    with dissolve

    t "If I am, I’m a very bad one."
    t "I haven’t shown up to work in years..."

    "Huh..."
    "Would I actually be able to kill someone?"
    "I mean...Maybe? I haven’t ever really put much thought into it before."
    "There would have to be a good reason for it and-"
    "Wait, why are we talking about something like this in a ramen shop?"

    s "I have no idea. And I don’t really have any plans to figure that out any time soon."
    t "Good. I no longer have to fear for my life. "
    t "Praise be."
    s "Praise be."

    scene tsuneysecondramen5
    with dissolve

    t "Heheh..."
    s "Wait, why do you keep saying that and why do I just repeat it like it’s some sort of reflex?"
    t "I don’t know. But it’s funny, isn’t it?"

    scene tsuneysecondramen8
    with dissolve

    t "Much funnier than my actual jokes, anyway."
    t "I’m fully aware that those are not what they should be yet."
    t "But just as a marinating-egg, they will get better in time. And Tsuneyo Tojo will go on to be more than a mysterious noodle-woman."

    "For a moment, I ponder if whether this whole comedy thing is something Tsuneyo is actually interested in or if it’s just a way for her to get her personality across better."
    "The truth is, I’m kind of hoping that she doesn’t get any better if it’s the former."
    "Is it wrong of me to want to hold back the dreams of someone else for my own personal benefit?"
    "Change is a terrifying thing when it affects those around us."
    "And even if Tsuneyo is a bit of a blank slate when it comes to personality, I think that’s what makes her {i}her{/i}."
    "{s}And if I need to be the one to prevent her from changing, I will give up my arms for it.{/s}"
    "{s}74 68 65 72 65 20 69 73 20 6e 6f 20 67 6f 64 20 68 65 72 65 2e 20 6a 75 73 74 20 6e 6f 6f 64 6c 65 73 2e{/s}"

    scene tsuneysecondramen1
    with dissolve

    t "You are taking much longer to decide than normal today."
    t "Would you like an explanation of the menu?"
    s "It doesn’t take a rocket scientist to figure out how a menu works, Tsuneyo."

    scene tsuneysecondramen9
    with dissolve

    t "Ah-"
    s "Oh, there it is again."
    s "I guess you’re not getting comfortable around me after all."

    scene tsuneysecondramen1
    with dissolve

    t "I am not allowed to get comfortable around men."
    t "All I can do is serve them food and hope that they will stay several feet away from me so I don’t get pregnant."
    s "It takes a little more than that to get someone pregnant."
    t "You’d be surprised in today’s society."
    s "What do you know about society, Tsuneyo? You didn’t even start going to[school] until recently."
    t "I’ve learned much from the people who sit on the opposite side of the counter."
    t "One of the many, {i}many{/i} wonderful things about ramen shops are the conversations to be shared between perfect strangers in between the slurps of pork broth."

    scene tsuneysecondramen2
    with dissolve

    t "“How was your day? What did you see on the way here? Are your children well?”"
    t "This is more than just a home for me and my father. It’s a home for anyone who has 700 yen and a little bit of time to spare."
    t "So to say I don’t understand society because of my homeschooling just isn’t true."
    t "There is more here than you would believe, Sensei."
    s "..."

    "For the first time ever, Tsuneyo breaks into a well-spoken tangent that goes on to show just how much she {i}does{/i} care about this place."
    "It becomes clear that the whole noodle thing isn’t just a running gag...And that she isn’t being forced into carrying on her father’s business just because she was born into it."
    "She...was raised by noodles."

    scene tsuneysecondramen1
    with dissolve

    t "..."
    t "You have a strange look on your face again."
    s "...Yeah."
    s "I just thought of a really weird sentence."
    s "I’ll have the Green Dragon again, please."

    scene tsuneysecondramen5
    with dissolve

    t "Of course. One Green Dragon. "
    t "I will be right back. Please do not rob the cash register while I am preparing your food."
    s "I didn’t plan on it..."

    scene tsuneysecondramen10
    with dissolve

    "Tsuneyo disappears into the kitchen the same way she always does when I order."
    "And I hear the same sounds I always do as she puts her all into making sure everything comes out perfectly."
    "..."
    "You know-"
    "Maybe places like this really {i}are{/i} more than they appear to be on the outside."
    "And even in this horrible part of town-"
    "Somewhere good exists."
    "Maybe."
    "Nothing is ever certain."

    scene black
    with dissolve2

    "But it doesn’t hurt to believe that."
    "At least for now."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen5 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen10:
    scene tsuneyokaori1
    with dissolve
    play music "kashiwagi.mp3"

    "I walk into the ramen shop to be met with an...unusual sight. "
    "It’s by no means uncommon to see other people here at this time of night. In fact, Tojo Ramen is actually surprisingly popular given its size and location. "
    "But...I can’t really say I expected to see {i}Kaori{/i} of all people here. Let alone a particularly angry looking Kaori."
    "Isn’t she normally working around this time?"
    "Just how many places can she be at once?"

    k "Why will you not listen to my proposal?! Do your human ears not function?! Is the spider to blame?!"
    t "We are not hiring, but thank you for your interest in Tojo Ramen. "
    t "Please do not come here anymore."
    k "May I at least speak with the human who owns this noodle building?!"
    t "He is sick and bedridden. He can barely speak."
    k "He does not need to speak! He just needs to listen!"
    s "Is there a problem here?..."

    scene tsuneyokaori2
    with dissolve

    t "Oh. Hello again."
    t "Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."

    if kaoridate1 == True:
        k "Friend?! What are you doing here?!"
    else:
        k "Hamburger Man?! What are you doing here?!"

    t "Do you two know each other?"
    s "We do. In fact, I feel like I run into her pretty much everywhere I go."
    t "Do you know how to make her go away?"

    scene tsuneyokaori3
    with dissolve

    k "I have not yet even swallowed a single dough string!"
    t "She keeps calling my precious noodles dough strings."
    t "I am tempted to slap a bitch."

    scene tsuneyokaori4
    with dissolve

    "I move several steps closer to the two of them and take a seat at the counter next to Kaori."

    s "I see you learned another new phrase."
    t "Be quiet or I will slap you as well."
    t "My fury can not be quelled."
    s "Well at least you aren’t hiding a knife behind your back this time."
    t "..."
    s "..."

    scene tsuneyokaori5
    with dissolve

    t "..."
    s "Tsuneyo, don’t even think about it. Remember the tag line."

    scene tsuneyokaori4
    with dissolve

    t "Tojo Ramen. All of the flavor, none of the violence."
    s "There you go. I knew you had it in you."
    t "All I have in me is rage."
    t "And-"
    s "And noodles. Yes, I know."

    scene tsuneyokaori6
    with dissolve

    k "Make her hire me! Please!"
    s "Why? You have like seven jobs already."
    k "That is not even enough jobs to cover every day of the week!"
    s "...Yes it is?"
    k "I require additional occupations!"

    scene tsuneyokaori4
    with dissolve

    s "Hey, Tsuneyo?"

    scene tsuneyokaori7
    with dissolve

    t "Ah-"
    s "Will you give Kaori a job?"
    t "..."

    scene tsuneyokaori4
    with dissolve

    t "No."

    scene tsuneyokaori6
    with dissolve

    s "I have exhausted every possible effort."
    s "It looks like you’ll just need to find another job elsewhere."

    scene tsuneyokaori8
    with dissolve

    k "I will not forget this betrayal."
    s "Just be quiet and eat your dough-strings."
    t "You bastard. You will pay."
    k "You are both fortunate that my stomach is lonely and has not absorbed hot pork liquid in a very long time."
    t "That's it. I’m calling the police. "
    s "No one is calling the police."

    scene tsuneyokaori4
    with dissolve

    s "Tsuneyo, why don’t you take a break for a little while and sit with the two of us?"
    t "I am working."
    s "Right. Which is exactly why I said “Take a break.”"
    t "But you haven’t ordered anything yet. I will not be able to provide adequate service if you decide to do so while I am on the break you suggested."
    s "That’s fine. I'm not really hungry anyway. I just came here to talk to you for a bit."

    scene tsuneyokaori9
    with dissolve

    if bonus == True:
        k "Do not fall for his trap! This man sells girls your age on the black market!"
    else:
        k "Do not fall for his trap! This man sells girl like you on the black market!"

    s "Kaori, stop going on about that human trafficking thing. I told you it wasn’t true."
    k "No! I am very mad at you!"

    scene tsuneyokaori10
    with dissolve

    t "After all we’ve been through...you want to sell me?"
    s "Of course I don’t want to sell you..."
    s "Do you really believe this suspicious character over me?"
    t "I don’t know what to believe. Everyone is calling my noodles dough strings and it is pushing my mind into turmoil."
    s "Then how about you just take a seat and eat some noodles? That always helps, doesn’t it?"

    scene tsuneyokaori11
    with dissolve

    t "Ahh...noodles."
    s "There you go. Doesn’t that calm you down?"
    t "It does."
    t "I am very easily swayed. "

    if bonus == True:
        s "I’ll try to forget that when my motives become slightly more inappropriate."
    else:
        s "You should focus on improving that part of yourself, as it could be rather problematic in the future and could allow employers to walk all over you."

    t "Noodles..."

    scene tsuneyokaori12
    with dissolve

    k "What is this sorcery? All you did was tell her to think of dough strings and it is as if she's journeyed to another world."
    s "It’s not sorcery. I’ve just learned how to talk to her."
    t "Noodles..."
    s "That’s right, Tsuneyo. Noodles."
    t "Maybe I {i}will{/i} take a break..."
    t "Just for a bit."

    "Tsuneyo begins to make herself a bowl of ramen and appears to completely forget Kaori's existence for the time being."

    scene tsuneyokaori13
    with dissolve

    k "Why will you not partake in the consumption of a bowl of pork warmth?"
    k "Is it because you only eat hamburgers?"
    s "No, Kaori. I’m just not hungry. "

    if kaoridate1 == True:
        scene tsuneyokaori14

        k "Well, you may share mine if you change your mind."
        k "I am no longer mad at you. And we are friends now, so it is okay."
        s "Thank you, Kaori. That’s...very sweet of you. I’m really okay, though."
        k "You should consume more carbohydrates so you can run longer distances."
        s "That’s...not a thing I want to do."
        k "Share my dough strings. I can not finish them all."

    else:
        k "Is it because you think the dough strings look like worms?"
        s "...No?"
        k "I also think they look like worms. But I will gladly consume them and become stronger."
        s "You do that."

    scene tsuneyokaori15
    with dissolve

    t "I have returned. "

    "Tsuneyo plops a bowl of ramen onto the counter that is so large that I can feel the wood slant down a few centimeters due to the sudden increase in weight."

    s "Can you really eat all of that?..."
    t "Any less than this would not quiet the rage burning within me."
    s "You’re certainly fierce when you’re angry."
    t "Fuck you."
    s "Tsuneyo, just because you know that isn’t a curse anymore doesn’t mean that it’s okay to say it to your friends."
    t "You're not my friend. You aren't anything to me."
    s "What happened to that “After all we’ve been through” stuff from a few minutes ago?"
    t "I meant through all of the transactions. There have been several now."

    if kaoridate1 == True:
        k "Friend."
    else:
        k "Hamburger Man."

    s "Yes, Kaori?"
    k "You seem quite capable of holding conversations with strange individuals. "
    s "I can’t tell if you’re talking about yourself or Tsuneyo."
    t "I’m a perfectly normal, noodle-loving girl."
    k "Do you see? Is she not strange?"
    k "Perhaps it is for the best that I am not allowed to work in this building."
    k "I like other foods too much anyway. Like bratwurst! Or soda!"
    s "Soda isn’t a food, Kaori."

    scene tsuneyokaori16
    with dissolve

    k "Do not tell me how to live my life when you love {i}nothing{/i}."
    t "Go on, Sensei. Tell her you love noodles."
    t "Make me proud."
    s "Noodles are good, don’t get me wrong, but I don’t think I’d put them at the top of my list."

    scene tsuneyokaori17
    with dissolve

    t "You will regret these words."
    s "Okay, why do you both look like you’re about to kill me? I don't like this."
    t "Is this what “leading someone on” means? I read about this in a book once."
    k "If these so-called “noodles” are not included in your favorite human items, what are?"
    k "Is there nothing you find sacred in this world?"

    scene tsuneyokaori18
    with dissolve

    k "List the things you love!"
    s "..."

    "The things I love, huh?"
    "Well, we’ve already crossed off noodles. So that leaves what?"
    "I don’t love my job."
    "I don’t love Kumon-mi. "
    "I care a lot for some, if not all, of the girls I’ve met here...but is it really fair to call something as trivial as that {i}love?{/i}"
    "Even with everything I’ve gone through, I still feel like some sort of outsider when I’m told to list the things that are important to me."
    "In fact, there are so few of them that there's really no point in making a list at all."

    s "To be honest...I don’t think I love anything."

    scene tsuneyokaori19
    with dissolve

    k "Nothing?..."
    t "That’s good. It means there is still room in your heart to accept the one true savior."
    s "If you tell me that savior is noodles, I’m going to walk out of this restaurant right now."
    t "Perhaps it is best if I keep my mouth shut."
    k "You did not name a single furry creature in your list of beloved items. "
    k "You aren’t human at all, are you?"
    s "Shouldn’t we be the ones asking {i}you{/i} that?"
    k "I’m the most human person here. Neither of you voiced how you feel about animals. Humans are supposed to like animals."
    s "Tsuneyo loves animals."
    t "Do I?"
    s "For the sake of this conversation, yes."
    t "I see."
    t "I, Tsuneyo Tojo, love animals. Let this fact be known."

    scene tsuneyokaori20
    with dissolve

    k "At least you are not completely lost to the darkness, Pork Woman. There is hope for you yet."
    t "Pork Woman? "

    if kaoridate1 == True:
        s "That’s going to be your new nickname from now on. I can’t even remember how long I was stuck with Hamburger Man for."

    else:
        s "That’s going to be your new nickname from now on. I can’t even remember how long I’ve been Hamburger Man now."

    scene tsuneyokaori21
    with dissolve

    t "I don’t know how to feel about this."
    s "I’ve found that it’s just best to let it happen. "
    t "You should have let me stab her when I had the chance."

    scene tsuneyokaori22
    with dissolve

    k "I take back all of the mean things I said to you. I require your protection. "
    k "I have consumed too many dough-strings to be able to properly engage in combat with a girl as shapely and athletic and beautiful as her."

    scene tsuneyokaori23
    with dissolve

    t "Thank you. I think you are beautiful as well."
    k "Apology accepted."

    scene tsuneyokaori22
    with dissolve

    s "Kaori, that’s not the proper response to “Thank you.”"

    scene tsuneyokaori24
    with dissolve

    k "Your instructions are too vague! I can not correct myself if all you say is that I am wrong and do not provide a correct answer!"
    s "Just say “You’re welcome.”"
    k "Welcome where?!"
    s "Nowhere. It’s just a phrase."
    k "Welcome is a greeting! You are trying to trick me, aren’t you?!"
    k "I will not fall for this! I will not be a pawn in your game!"
    k "I am Kaori Kadowaki! The Queen of Spiders! The Mistress of the Dark! "
    t "And I am Tsuneyo Tojo, the quirky and fun-loving Flavor Samurai."
    s "You two should join forces and create the strangest crime fighting duo of all time."
    t "As long as I’m home before the moon comes out."
    s "That should be doable. Kaori works like eighteen jobs but you guys can probably find a time that’s good for both of you."

    scene tsuneyokaori25
    with dissolve

    k "What do you think you’re doing? I will not agree to work with someone who would not agree to work with {i}me{/i} under different circumstances."
    k "I was born to serve customers, not justice."
    t "I was born to serve-"
    s "Noodles. We know, Tsuneyo."

    scene tsuneyokaori26
    with dissolve

    t "Ah-"
    t "I’ve become predictable."
    s "You’ve been predictable since our second meeting. "

    scene tsuneyokaori25
    with dissolve

    t "Whatever you say, bro."
    k "Many years, I have lived. 154 Dog years to be exact. But never in my life have I been so out of place in one restaurant."
    k "This side of town is pure evil."

    scene tsuneyokaori27
    with dissolve

    k "I can feel it...deep inside of me- my organs wrapping around themselves."
    k "I should have thanked them more than once."

    scene tsuneyokaori28
    with dissolve

    k "I must go!"
    s "Kaori-"
    k "Good day, humans!"

    scene tsuneyokaori29
    with dissolve

    "Kaori quickly disappears out of the ramen shop, slamming the door behind her."
    "I wonder where she-"

    t "The..."
    t "The ramen..."
    t "It is nearly untouched..."
    t "Who..."
    t "Who could do such a thing?..."
    s "..."
    t "..."

    scene tsuneyokaori30
    with dissolve

    s "..."
    t "...?"
    s "Ugh, okay. Fine. I’ll eat it. "
    s "I should have figured something like this was going to happen anyway."

    scene tsuneyokaori31
    with dissolve

    t "Good."
    t "It appears that I will be able to sleep tonight after all."

    scene black
    with dissolve2

    "I scarf down the ramen as quickly as I can and decide to head back before it gets too late."
    "The walk home is surprisingly quiet."
    "I get lost along the way."
    "I should pay closer attention when moving around in the dark."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen10 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen15:
    scene ramenfifteen1
    with fade
    play music "kashiwagi.mp3"

    "I arrive at the ramen shop to find a rather...despondent looking Tsuneyo."
    "Or maybe she’s just tired. I don’t know."
    "I can never really tell with her."

    s "Tsuneyo, how are you feeling right now?"
    t "Like the world is crumbling down around me and I am but a lonely sheet of kombu."
    s "Okay, so despondent it is."
    t "I’m so tired."
    s "Or maybe not."
    s "You’re really not helping me out here."

    scene ramenfifteen2
    with dissolve

    t "I’m sorry. "
    t "It was very busy before you showed up."
    t "Thank you for scaring the rest of the customers away. I needed a break."
    s "The store was empty when I arrived, though."
    t "They must have sensed that you were coming."
    t "The Emerald Guardian says you have a holy aura."
    t "There are many people who can probably feel it."
    t "Especially since most people in this area are old and dying."
    t "Why is it that people who are closer to death care more about religion than those who are young?"
    s "Do we need to get into that right now?"
    s "I haven’t even touched my dinner yet."
    t "You haven’t ordered dinner yet."
    s "Oh. I thought that bowl next to you was for me."
    t "That is a strange thing to assume."
    s "Well you kind of just placed it there as soon as I sat down, so I figured you were preemptively getting me something."
    t "Oh. No."
    t "I placed it there for comfort."
    t "There is something soothing about a bowl of miso ramen sitting beside you during casual conversation. Don't you agree?"
    s "No. What? Why?"

    scene ramenfifteen3
    with dissolve

    t "Who knows? Perhaps that’s just the way things are..."
    s "Don’t just look off into the distance like that was some sort of revelatory thing to say."

    scene ramenfifteen4
    with dissolve

    t "Fine. Then I will look directly at you for the rest of the night."
    t "Even when it starts to make me feel sick."

    if bonus == True:
        t "Are you enjoying this, you pervert?"
        s "Yes, Tsuneyo. My biggest fetish is eye contact."
    else:
        t "Are you enjoying this, Father?"
        s "Why did you just call me that?"
        t "Call you what?"
        s "Father."
        t "I did no such thing. You have potatoes in your ears."

    "The sounds of car horns leak under the old metal door of the ramen shop, showing that even places as devoid of life as the old district still have some sense of urgency to them."
    "Inside of Tojo Ramen, however, that never seems to be the case."
    "Well, at least while I’m here."
    "It’s definitely a little suspicious how Tsuneyo claims it was packed just moments before I showed up."

    s "What do you think the reason you were so busy tonight is?"
    s "It seems like just another day to me."
    t "We always get busier in the winter. "
    t "Can you think of anything more relaxing than a bowl of ramen on a cold night?"
    s "See, that makes a lot more sense than leeching comfort off of just having one next to you. "
    s "It’s just weird that I never see anyone here."
    t "You’re a liar."
    t "You purchased dinner for the intimidating blonde woman once."
    t "And then there was that horrible girl with the black and white stripes."
    s "How is Kaori horrible? She just wanted a job."
    s "If anything, you’re horrible for being the only roadblock between her and her mission to work at every single restaurant in Kumon-mi."
    t "Tsuneyo Tojo needs no assistance. "
    t "My father never would have agreed to her working here anyway."
    s "Why? She’s surprisingly competent in a...really weird way."
    t "Like me?"
    s "Yes, but also no. I don’t think I’d call you surprisingly competent."
    t "That’s fair."
    t "But the real reason is her tattoo."
    s "Oh, yeah that makes sense. "
    s "With all the Yakuza hanging around here someone might...look at her the wrong way and think she’s on their turf or something?"
    t "No. My father just doesn’t like spiders."
    s "That...makes more sense than what I said."
    s "I always forget that arachnophobia is an actual thing people have."

    scene ramenfifteen5
    with dissolve

    t "Really? The research I’ve done about fear shows it as one of the most common phobias out there."
    s "Yeah, but it’s just- wait, why are you researching phobias?"
    t "Fear plays a big role in determining a person’s actions."
    t "I thought that if I could understand what everyone is afraid of, I would have an easier time talking to them."
    t "What I have learned in the process is that there are fears of everything. "
    t "This world is so scary."
    s "Are you afraid of spiders as well, Tsuneyo?"
    t "I think so. "
    t "It’s not a fear that makes me want to run or scream, but an uneasy feeling that sits in the pit of my stomach like undercooked pork."
    s "I think that’s still technically fear, though."
    t "Probably."
    t "Are you afraid of anything, Sensei?"
    s "Me?"
    t "You."
    s "..."
    s "Death, I guess?"
    t "Ahh, deathophobia."
    s "I think it has a more...scientific name than that."
    t "Is it the act of dying or what comes after that scares you?"
    s "I guess the act of dying since reincarnation is now a confirmed thing."

    "Probably. "
    "If that {i}is{/i} what actually happened to me."
    "I don’t even know how to describe my situation at this point."
    "Who knows?"
    "Maybe I’ll just wake up one day and this will all have been one, long dream."
    "What an ending that would be."

    t "You believe in reincarnation?"
    s "You don’t?"
    t "No. My father never believed in that so neither do I."
    s "You know you don't have to believe things just because your father does, right?"
    t "I want to, though. It makes everything easier."
    s "Well...what do you think happens, then?"

    scene ramenfifteen6
    with dissolve

    t "I’ve always been under the impression that we’d be buried and grow into trees."
    s "I don’t really think burying people works that way."
    s "We’re not seeds."
    t "Not yet."
    t "But what if after we die, all of the unused nutrients in our body leak out in thin strips like roots."
    t "What if every forest we see is actually a graveyard?"
    s "What would that make graveyards, then?"

    scene ramenfifteen7
    with dissolve

    t "Maybe that’s...where we bury trees?"
    s "Looks like your theory fell apart, huh?"

    scene ramenfifteen8
    with dissolve

    t "I’m just trying to repeat the things I’ve learned. "
    t "None of it really makes sense to me. But I have plenty of time to think when I’m not helping customers."
    s "You should be thanking me for always sending everyone else away, then. "
    s "Me coming here is pretty good for you in that sense."

    scene ramenfifteen9
    with dissolve

    t "Until it drives down sales and we can’t afford electricity anymore."
    t "But as long as you only come at night, we can still profit in the morning."
    s "Does your father come down and run the store in the morning still?"
    t "No, he’s unable to leave his room."
    t "I meant mornings on the weekend."
    t "We’re closed during the mornings on weekdays because I have to receive an education."
    s "You know you could solve that problem by hiring {i}someone else{/i} to work here, right?"
    t "But spiders."
    s "It doesn’t {i}have{/i} to be Kaori. What about Yumi?"
    t "She would be a better candidate, but I’m afraid she would call all of the customers “Mom.”"
    s "She did that with one person...and that one person {i}was{/i} her mom."
    t "That’s just what she wants us to think."
    t "I can see it now-"
    t "{i}Mom, where do we keep the noodles?{/i}"
    t "They are in the back, my child."
    t "{i}Thanks, Mom! I love you.{/i}"
    t "I love you too."
    s "There’s a flaw in your logic. It implies Yumi has the capability to love something."
    t "If she can not love, how can I expect her to treat the food here with the respect it deserves?"
    t "Can she even cook?"
    s "Well...no. Probably not."

    scene ramenfifteen10
    with dissolve

    t "Then there’s no point, is there?"
    t "Besides, running Tojo Ramen alone helps me protect all of its secrets."
    t "What would happen if a competitor discovered the special ingredient in our shio broth?"

    "Sorry, Yumi."
    "Can’t say I didn’t try."
    "It really would have been nice if she were able to work here."
    "It’s not far from Chika’s house and it’s not like she ever comes to[school] during the day anyway."
    "But {s}god{/s} God forbid someone discovered Tsuneyo’s secret broth."

    s "Well, if you ever get tired and don’t want to depend on my presence for a break, it might be worth looking into getting some extra help."

    scene ramenfifteen11
    with dissolve

    t "The Samurai of Flavor needs no help."
    t "My father was kind enough to entrust the business to me, so the least I can do is honor his wishes and not hire a spider."
    s "I think you’re forgetting about the {i}definitely human female{/i} that spider was attached to."
    t "Spiders are just humans with more legs."
    s "..."
    s "No, Tsuneyo."

    scene ramenfifteen12

    t "Ah-"
    s "I just don’t want you overworking yourself and then...getting buried and turning into a tree or whatever it was you assumed happened to people after death."

    scene ramenfifteen13
    with dissolve

    t "I can’t die yet."
    t "There is no one to bury me."
    t "Even if my father was able to regain his strength, leaving the room would prove to be very difficult for him."
    t "I’d turn into a tree wherever I died."
    t "And there’s nowhere I go that would be a convenient location for a tree."
    t "Imagine a situation where you came into the restaurant today and tried to have this exact conversation, but with a tree between us."
    t "It would be very difficult."
    s "Might be good for the atmosphere, though. It’s definitely a little stuffy in here."
    t "Fuck you. Get out of my store."
    s "Just because you found out “fuck you” isn’t an actual curse doesn’t mean it’s okay to keep using it as an insult on me."
    t "But there is no one else who makes me mad and it’s a very fun thing to say."
    t "You can fuck me too if you want. You’d be surprised by how fun it feels."
    t "Try it."
    s "..."
    t "Hurry up and fuck me, Sensei."

    if bonus == True:
        "I pull my phone out and open up the voice recording app."
        "I think I’m about to acquire a new ringtone."
        "It will go really well with my wallpaper of Makoto stuffing a dildo in her mouth."

        s "Can you say that one more time, Tsuneyo?"
    else:
        "I pull my phone out to create a voice memo that will allow me to avert blame should Tsuneyo ever accuse me of trying to blackmail her into achieving better grades."

        s "I am Sensei, the date is today, and I am recording this memo for my own protection."

    play sound "phonebeep.wav"

    t "Why won’t you fuck me? Is it too hard?"
    t "I’ll be okay. I’m a strong woman."

    play sound "phonebeep.wav"

    s "Thanks."

    if bonus == False:
        s "Please know that I don't support any of this and, despite it being a funny misunderstanding of a common term, I do hope you will soon learn to not speak in this way. Also-"

    s "I have to make sure none of the other girls ever hear this."
    t "You’re right."
    t "It would be bad if they found out we were fucking each other this early in our relationship."

    scene ramenfifteen14
    with dissolve

    t "Perhaps I will fuck the Emerald Guardian as well."
    t "Are there rules about girls fucking other girls?"

    "Tonight went from weird to awesome very quickly."
    "Tojo Ramen is the best."

    s "I think you should try, Tsuneyo."
    s "If you believe in yourself, even your wildest dreams can come true."

    scene ramenfifteen15
    with dissolve

    t "That sounds horrifying."
    t "If my dream from last night came true, our eyes would fall out and our teeth would liquify."
    s "Okay, maybe not dreams like that. I meant more like...goals."
    t "Like in soccer?"
    t "The short girl on our soccer team touched me inappropriately."
    t "Are you saying I can fuck her too if I believe in myself?"

    scene ramenfifteen16
    with dissolve

    t "Oh no! Do I have to fuck the entire soccer team?!"
    t "I’ve never even talked to most of them! "
    s "Hey, your father’s hearing isn’t...abnormally good or anything, is it?"
    s "I’m kind of worried about him hearing this and then defying all expectations and coming downstairs to kill me with his Yakuza friends."

    scene ramenfifteen17
    with dissolve

    t "He can barely hear anything anymore, but you make a good point."
    t "He’d be very upset to hear that his daughter was going around fucking everyone after finally being allowed out of the house."

    "It just keeps getting better and better."

    scene ramenfifteen18
    with dissolve

    t "I still apparently have much to learn about the proper way to fuck, but I’m hoping you will continue to teach me."

    if bonus == True:
        s "Don’t worry, Tsuneyo. I will fuck you as many times as you want."
    else:
        s "I will teach you many things, but none of them as gross and unnecessary as that."

    scene ramenfifteen19
    with dissolve

    if bonus == True:
        t "Even though I’m terrible and have no idea what I’m doing?"
        s "Even then."
        t "How long until we can team up and fuck other people together?"
        t "I am overjoyed just thinking about the shock on their faces when we fuck them at the same time."
        s "Soon, Tsuneyo. "
        s "Soon, we will fuck-"

    q "*Ahem*"

    scene ramenfifteen20
    with dissolve

    t "..."
    s "..."

    scene ramenfifteen21
    with dissolve

    yu "..."
    t "Oh. Good evening."
    t "Welcome to Tojo Ramen. Please let me know if you have any questions about the menu."
    s "..."
    yu "..."
    s "Hey, Yuki."
    yu "..."
    s "..."
    t "The air in this room has gotten quite strange."
    t "You two are acquainted, correct?"
    t "Perhaps you should fuck each other to lighten the mood."
    s "Tsuneyo, not a good time."
    t "It’s always a good time to fuck."
    yu "You know what? I’m not even hungry anymore."
    yu "Just gonna pretend this never even happened."

    scene ramenfifteen20
    with dissolve

    "Yuki leaves just as quickly as she arrived and several moments of silence pass before Tsuneyo finally decides to say something logical."

    t "Perhaps it would be best if we only fucked each other in private from now on?"
    s "Yeah..."
    s "Yeah, that’s probably for the best."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ ramen15 = True
    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen20:
    scene blackout1
    with dissolve
    play music "kashiwagi.mp3"

    "I decide to drop by the ramen shop to check on Tsuneyo and grab a quick bite to eat."
    "But judging by the way she’s staring at me, I think it’s safe to assume that she is not very happy with my decision to do this."
    "I want to say she's only looking at me like this because I ordered a plate of curry instead of ramen tonight, but the scowl has been there since before I even ordered."

    s "Did I do something to offend you?"
    s "Is this about driving customers away again?"

    if bonus == True:
        t "I followed your advice and asked the Emerald Guardian to remind me of what sex is."
        t "Why did you allow me to say so many things about fucking?"
        t "Now everyone thinks I am a harlot."
        s "Not everyone. Just Uta and Yumi’s mom."
        t "Word gets around about girls like me. It won’t be long before the whole class knows."
        t "Also, those aren’t noodles in front of you."
        t "Why are you doing this to me?"

        "Ahh, so I guess the curry was part of it after all."

        s "On the bright side, it looks like you were able to learn more about modern dialogue. So all was not lost, right?"
    else:
        t "No. I am just angrily recollecting the video of the Marine who threw a puppy off of a cliff in 2008."
        s "I don't think I ever saw that."

    t "Fuck you."
    t "Not literally, though. I understand what that would mean now."
    t "It sounds very painful."
    s "And you’re not completely opposed to using that word even though you understand it now?"
    s "Color me impressed."
    t "I hope you choke on your non-noodle food and die."
    s "Why even sell it if you don’t approve of it as a product?"
    t "My father has informed me that it must remain on the menu for as long as he is alive."
    t "And with his days among us numbered, the days of this curry’s existence are numbered as well."
    t "The time for reckoning is upon us."
    s "You’re sounding more and more like Molly every day."

    scene blackout2
    with dissolve

    t "That is worrying to hear."
    t "With the things the other girls say about her, I’m beginning to believe the Emerald Guardian is not as omniscient as I initially thought she was."
    t "She is but another fruit that has fallen off the tree of life, and I am the lowly earthworm feeding off of her decaying corpse."
    s "Now you’re sounding less like Molly and more like a serial killer."

    scene blackout3
    with dissolve

    t "Well {i}you’re{/i} sounding like a little bitch."
    s "..."

    scene blackout4
    with dissolve

    t "I apologize if I didn’t use that word correctly."
    t "I heard the delinquent girl with mother issues call you that and you seem to fear her."
    s "First off, that was harsh. "
    s "Yumi’s issues with her mom are a private matter that only those two and sometimes myself are allowed to get involved in."
    s "Secondly, I am not {i}afraid{/i} of Yumi."
    t "But she defeated the Green Onion in a battle of arm strength so easily."
    t "What if you are next?"
    s "I'm curious to know about what chain of events would possibly lead to that."
    s "I’m really not afraid of Yumi, though."
    t "But I sense fear when you two are in close proximity to one another."
    t "Is it possible that you are the one {i}she{/i} fears instead?"

    if bonus == True:
        play sound "static.mp3"
        scene yumi10 with flash
        scene blackout4 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene wherethesidewalkends25 with flash
        scene blackout4 with flash
        stop sound

    s "I don’t think so. "
    s "I’m pretty sure she’s almost finished getting over the one thing I’ve done that {i}would{/i} scare her."
    t "What did you do?"
    s "That’s not really any of your concern."
    t "It’s not?"
    s "It’s not. "
    t "Interesting."
    t "I think you may be misunderstanding the purpose of this restaurant, Sensei."
    s "Are noodles...not the purpose of this restaurant?"
    t "They are the first purpose."
    t "But this store is much more than just noodles to myself and many others."

    scene blackout5
    with dissolve

    t "Tojo Ramen is a special restaurant where people from all walks of life can gather to consume pork broth and air out their worries."
    t "It is a place where people are free to speak their minds without worrying about persecution from others."
    t "A calm, quiet sanctuary in an otherwise dead section of the world."
    t "So, if there are things you wish to confess, there is no better place to do so than here."

    scene blackout6
    with dissolve

    t "Anything you say or do at this counter will never leave the restaurant so long as you do not want it to."
    t "Such is the promise of Tojo Ramen."
    s "It’s starting to make a little more sense why this has become a hangout spot for the Yakuza."
    s "Also, you should smile more. You look really cute right now."

    scene blackout7
    with dissolve

    t "It’s not me, it’s the noodles."
    s "..."
    s "No, it’s you."
    t "Noodles."
    s "..."

    "I guess it makes sense that this place could also serve as a haven of sorts for some people."
    "Late night restaurants with swarms of locals and nostalgic atmospheres are not exactly a foreign concept."
    "In fact, there’s probably a Tojo Ramen in every city in the world."
    "Now, on the other hand, I highly doubt there is a Tsuneyo Tojo in every city in the world."
    "She’s certainly proven to be...one of a kind so far."
    "But when you grow up in a place like this, breaking the necks of fowls and listening to tattooed men confess crimes between 300 Yen beer refills-"
    "I guess there’s not much of a chance to ever learn how the real world works."

    scene blackout8
    with dissolve

    t "How was the speech?"
    t "I memorized word-for-word what my father would say when he was still well enough to converse with others."
    s "He can’t even talk?"
    t "He can make noise, but the only one who understands him is me."
    s "Is it okay for me to ask what’s wrong with him, exactly?"
    t "It is not. "
    t "You shouldn't worry about that."
    t "All you have to do is enjoy your noodle-less dinner and speak what’s on your mind."
    s "Easier said than done. "
    s "Japanese men aren’t exactly known for being open and honest about their feelings- and I’m pretty sure I talk even less than most of them."
    t "My father is the same way."
    t "Or {i}was{/i} the same way."
    t "He doesn’t say much of anything anymore. But he does not need to."
    t "All he needs to do is recover. "
    t "And hopefully live forever so I can continue to avoid perpetual sadness like I have done for the rest of my incredibly boring life."
    s "Here’s to avoiding perpetual sadness, I guess."
    t "A strange toast, but one that I enjoy."
    t "I would drink to it if alcohol did not make me fall asleep the second it comes into contact with my tongue."

    "I reach for the spoon and finally take a bite of the curry Tsuneyo laid out in front of me some time ago."
    "It’s good, but it doesn’t measure up to the quality I’ve gotten used to from the ramen."
    "I guess Tsuneyo just doesn’t put the same level of care into this dish as she does the others."

    scene blackout9
    with dissolve

    t "Do you regret your decision now?"
    s "You mean do I regret ordering curry?"
    t "Yes. You have a face that says “It’s good, but doesn’t measure up to the quality of the ramen.”"
    s "That’s...exactly what I was thinking. But I don’t regret my decision."
    s "If I wanted ramen, I would have ordered ramen."
    s "Not everyone wants ramen every night, Tsuneyo."

    scene blackout1
    with dissolve

    t "When I told you it was okay to confess horrible things here, I did not mean {i}that{/i} horrible."
    t "I’m still interested in hearing why the delinquent girl is afraid of you."
    s "Listen, I’m glad that this place is the sort of restaurant where I can {i}air out my worries{/i} but...that’s not the type of person I am."

    scene blackout10
    with dissolve

    t "And I am not the type of person who is accustomed to looking death in the eye, yet I have been doing just that since our discussion in my room."
    t "Growing up means leaving your comfort zone. "
    t "It is why I come to[school] and why I learn. "
    t "Or...try to learn."
    t "Perhaps it is time for you to grow up as well, Sensei."
    s "When did you get so mature?"
    s "Go back to talking about noodles and cracking stand-up jokes."

    scene blackout11
    with dissolve

    t "Do not provide me false hope."
    t "We both know that I am unfit for comedy. "
    s "You’re unfit for most things, to be completely fair."

    scene blackout10
    with dissolve

    t "It’s true."
    t "I will die here the same way my father will."
    t "The only difference is that there will be no one to make sense of the borderline inaudible noises I make as I dissolve into the ground."

    stop music
    play sound "imscared.mp3"
    scene black

    ":)"

    "I instinctively jump back in my seat after a loud bang shakes the restaurant. "
    "I have no idea what it was, but it appears to have cut the power as well."

    t "Oh dear."
    s "“Oh dear?” "
    s "That’s all?"
    s "Are you not scared right now?"
    t "Why would I fear the darkness? I do not have darknessophobia."
    s "I just thought your reaction would be a bit stronger than “Oh dear.”"
    t "This is not the first time this has happened."
    t "The machines keeping my father well require a large amount of energy."
    t "Sometimes, the power goes off as a result of that."
    s "Do you have a generator or...a backup power source or anything?"
    t "We do. It should turn on down here momentarily."
    t "In the meantime, please excuse me while I go check on my father."
    t "He will likely die if the backup power has not yet turned on upstairs either."
    s "Do you want me to co-"
    t "No. "
    t "You must stay down here."
    t "He’s very adamant about remaining unseen. "
    t "Please continue to enjoy your noodle-less curry, though."

    play sound "footsteps.mp3"

    "I hear Tsuneyo get off of the stool next to me and make her way over to the door."
    "I’d have probably felt a little better if I was able to go with her but, then again, I’m not sure I’d enjoy seeing her half-dead father."
    "I’m just hoping the lights-"

    play sound "static.mp3"
    scene blackout12
    with flash
    stop sound
    play music "sanctuary.mp3"

    "The backup power source comes on and everything turns red."
    "Well, mostly everything."
    "My curry is still a mixture of brown and white."
    "Coincidentally, those are also the colors of Tsuneyo and me."
    "And when placed together on the same plate or, in this very specific circumstance, a restaurant-slash-confessional, things seem to work out pretty well!"
    "I insert my spoon into Tsuneyo and me and shovel the two of us into my mouth."
    "We taste delicious."
    "I spit out my food just so I can eat it again."
    "They should turn the lights off in here more often."
    "Maybe then I’d feel comfortable enough to admit that Yumi is only scared of me because I came within two steps of [raping] her in broad daylight."
    "Does a beautiful sunset count as broad daylight?"
    "Or is it vague daylight or something else comparable at that point?"
    "..."
    "I spit my food out a third time before the consistency becomes too gooey to enjoy anymore."

    if bonus == True:
        "I begrudgingly swallow it in the same fashion that delinquent begrudgingly swallowed my saliva all those {s}days? weeks? years?{/s} ?????? ago."
        "Where it happened wasn’t far from here."
        "Tsuneyo was right when she mentioned how this part of town is mostly dying."
        "I wonder if there’s a blackout in the surrounding buildings as well."
        "I could get away with so many things if I wasn’t so busy consuming myself."
    else:
        "I should have someone teach me how to chew one of these days."

    play sound "footsteps.mp3"
    "The footsteps leak back into my head but I’m unable to see where they’re coming from."
    play sound "footsteps.mp3"
    "It’s almost like ghosts threw some shoes on and started pacing around the place- "
    play sound "footsteps.mp3"
    "Hoping to score one last sip of broth before returning to Heaven or Hell or whichever other make-believe afterlife they were fortunate or unfortunate enough to find an apartment in."

    play sound "static.mp3"
    scene blackout12
    with flash
    stop sound

    s "..."

    "I feel...strange."
    "Kind of like I’m losing track of time."
    "How long has the power been off?"
    "Tsuneyo hasn’t come back downstairs yet, has she?"
    "I slide my phone out of my pocket to check the time."
    "And, of course, it appears to be dead."
    "Just my luck."
    "I could have sworn it was on nearly full battery before coming here, but it wouldn’t be the first time I’ve been wrong about that."

    s "..."

    "Part of me wants to just get up and leave since it’s starting to get extremely cold, but-"
    "Not only would I feel bad for abandoning Tsuneyo before even paying for dinner-"
    "I kind of..."
    "Can’t get out of my chair."
    "I mean, maybe I can, but-"
    "I don’t want to."
    "I’ve become content in my spot at the counter."
    "Tojo Ramen really is a special place."
    "I haven’t felt this at-home in quite some time."

    play sound "static.mp3"
    scene blackout13
    with flash
    stop sound

    t "Oh. You’re still here."
    s "Tsuneyo?"

    scene blackout14

    t "Ah-"
    s "How long were you gone for?"

    scene blackout15
    with dissolve

    t "Half an hour. "
    t "I assumed you just went home."

    "Has it really been that long?"
    "I feel like the power’s only been off for a few minutes."

    s "Is your dad okay?"
    t "He’s fine."
    t "The backup power upstairs starts immediately in the event of an outage. "
    t "The reason it takes so long to reach the ground floor is that my father requires almost all of it."
    t "Electricity can be very lazy."
    s "Do you know when the power will be coming back on?"
    t "That depends on {i}how{/i} lazy the electricity wants to be."
    t "There are many wires, so I assume it will take quite some time to catch up."
    t "Do you want a box for your curry?"
    t "I see that you haven't even touched it since I left."
    s "Oh, sure. I-"

    "I look down at the plate of curry to find that..."
    "I must have inadvertently...drawn a smile in the sauce?"

    s "Hey, you didn’t...play with my food while the lights were off, did you?"
    t "Food is for eating, not playing."
    t "If you want to play with food, choose a different restaurant. You are not welcome here."
    s "Just...get me a box. I don’t want to play with my food."
    t "I understand."
    t "The food is on the house today as apologies for the inconvenience and loss of power."
    s "Oh, cool. Thanks a lot. You didn’t have to do that."
    t "It was my father’s idea. "
    t "He could sense that there was a guest downstairs."
    t "I personally think we should have charged you for insulting us by ordering that stupid dish."
    s "You really don’t like curry, do you?"
    t "I love it."
    t "Please never order it again."
    s "..."
    t "..."

    scene black
    with dissolve2

    "Tsuneyo grabs me a box near the register and I shovel the rest of my dinner inside, placing it in a bag she lays out next to me as I do so."

    t "Tojo Ramen sincerely apologizes for the loss of power during your visit tonight."
    t "Please accept this coupon for 23%% off of your next check."
    s "Why not just round up to 25%%?"
    t "I don’t make the rules, just the noodles."
    s "Well...thanks, I guess."
    t "No, thank you."
    t "Please come back soon."
    t "We are grateful as always for your business."

    "I tie the handles of the plastic bag into a knot and exit the store."
    "It’s snowing out."
    "I wind up throwing away my curry in the first garbage bin I find."
    "I don’t know why."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen20 = True

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"

    scene smile
    with dissolve4
    $ renpy.pause(5, hard=True)
    scene black
    with dissolve4
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen25:
    scene tsuneyogreenonion1
    with fade
    play music "kashiwagi.mp3"

    t "Sigh."
    s "You’re not supposed to {i}say{/i} “sigh,” Tsuneyo. You’re supposed to just...actually do it."
    t "Sensei, when you look at this knife...what do you see?"
    s "A knife."
    t "Look closer."
    s "..."

    scene tsuneyogreenonion2
    with dissolve

    s "It’s still a knife."
    t "Precisely."

    scene tsuneyogreenonion3
    with dissolve

    s "What?"
    t "Sometimes, what you see is what you get."
    t "And other times, you get a knife."
    s "Tsuneyo, what the fuck are you talking about?"
    t "Knives, idiot. "
    t "I had a thought, but it went somewhere else."
    t "This would not be an issue if you were more entertaining."
    s "Well forgive me for coming all the way across town in the cold to spend time with you."
    t "I can not forgive you. But I can make you a bowl of delicious soup that will warm both your heart and your soul."

    "As you can see, I decided to spend the night hanging out at Tojo Ramen with Tsuneyo. "
    "And despite the way she’s slowly waving a knife around, it’s clear that she is happy to see me."
    "Well, “happy” is probably a bit of an exaggeration."
    "But she was just standing around before I got here and is now capable of doing her job- the one thing in life she appears to be confident in."

    s "Just make me whatever you feel like making. I don’t care."
    t "I don’t feel like making anything. Are you okay with starving?"
    s "{i}You{/i} don’t feel like getting...closer to noodles or whatever?"

    scene tsuneyogreenonion4
    with dissolve

    t "I will not be told to get closer to Noodles by the one man who stays as far away from him as possible."
    s "Not bird-noodles. Noodles-noodles. "
    s "It’s unlike you to not want to cook."

    scene tsuneyogreenonion5
    with dissolve

    t "As a wise man once said...even the best fall down sometimes."
    s "That wasn’t a wise man. That’s the chorus from Howie Day’s 2003 hit single, “Collide.”"
    t "And what a wise man he was."
    t "But who said it does not matter even half as much as {i}what{/i} was said, Sensei."
    t "I’m afraid that I am just lacking the same motivation and excitement that you would normally come to expect from a lively, energetic girl like myself."
    s "Yes. Because when I think of Tsuneyo Tojo, I immediately think “lively.”"
    t "If only I could be more like this knife."
    s "I know there’s a metaphor in there somewhere, but I’d appreciate it if you could just tell me what it is so I don’t have to use my brain."
    t "Sharp. And made of steel. This is the me who never was. The me who is not."
    s "If this is another comedy routine, I'm going to go ahead and do you a favor by asking you to scrap it. "

    scene tsuneyogreenonion6
    with dissolve

    t "Gone...like noodles in the wind. Flying about and causing destruction everywhere they roam."
    t "This is the Tsuneyo Tojo you see before you. A shell of her former crab."
    s "What the hell happened to you overnight?"

    scene tsuneyogreenonion7
    with dissolve

    t "Is this what they call “depression?” Should I see a doctor?"
    s "I highly doubt that. Why don’t you just tell me what’s going on?"
    s "I can’t guarantee that I can help or anything but, sometimes, talking about stuff is all you need to feel a little better."
    s "Also, if I’m on better terms with you, you won’t feel the urge to stab me with that knife you’re still waving around."
    t "How did you know about that urge? Did I mention it out loud in the heat of my sadness?"

    "You know, maybe I should call it an early night and head back home before Ami needs to identify my body at the local morgue?"

    s "Just tell me what’s wrong. That’s the least you can do to make up for not serving me while you’re still open."
    s "It’s either that or I leave you a bad Yelp review."

    scene tsuneyogreenonion8
    with dissolve

    t "Don’t you dare! Everyone knows that a restaurant’s success is entirely dependent on the thoughts of various inexperienced consumers who went through the effort of actually creating a Yelp account!"
    t "I shall turn {i}you{/i} into ramen, you bastard!"
    s "Okay. On that note, I’m just going to-"

    scene tsuneyogreenonion1
    with dissolve

    t "Fine. I will talk."
    t "But it is very sad. Please do not cry when you hear how horrible things are."
    s "I’m sure that I’ve heard worse than whatever it is you’re going through."
    t "Sigh."
    s "..."
    t "Sensei..."
    t "It appears that the restaurant is out of green onions."
    t "Not to be mistaken with the Green Onion of the second floor. She has not yet come to this restaurant."
    s "And...that’s why you’re giving up on everything?"
    t "One item being out of stock is a symbol of my failure as the acting manager of this business."
    t "First, it is the green onions. Then, it is chopsticks."
    t "Then, next thing I know, everyone has to grab their noodles with their fingers and eat them the way birds eat worms."
    s "Sure. Except birds don’t have fingers and use their beaks to eat."

    scene tsuneyogreenonion8
    with dissolve

    t "Oh, so {i}now{/i} you care about what birds do? How dare you?"
    s "Is that really all that’s bothering you? Running out of one thing?"

    scene tsuneyogreenonion1
    with dissolve

    t "I was prepared to adapt to the situation at first..."
    t "But as the hours went by and no customers entered the store, I realized that my failure must have already spread throughout the city."
    t "I’m afraid it is too late for me now."
    s "No one’s come in all day?"

    scene tsuneyogreenonion3
    with dissolve

    t "If they have, they are either invisible or extremely sneaky. And not hungry."
    t "We have experienced slow days in the past, but never anything like this."
    t "Though, I am prepared to experience happiness once more if you offset the lack of profit by purchasing everything on the menu."
    s "You know...I {i}would{/i}, but I was kind of hoping for something with green onions."

    scene tsuneyogreenonion9
    with dissolve

    t "Of course. Another reminder of my inadequacy makes itself known before the doors are closed for the night."
    t "Tojo Ramen is no more. This is the end."
    s "Oh, stop being dramatic."

    scene tsuneyogreenonion10
    with dissolve

    t "Dramatic?! Me?! The world is crashing down right now and you have the audacity to demand such a thing?!"
    t "Where do you get off?!"
    s "Jesus. There’s no need to yell."

    scene tsuneyogreenonion3
    with dissolve

    t "I apologize. I was attempting to show the difference between true drama and what you had labeled as drama, but my acting skills were so good that you must have gotten scared."
    s "Tsuneyo, you do realize there is a very easy way to solve your problem of not having onions, right?"
    s "I’m sure customers won’t magically appear again once you obtain them, but it’s not like they are out of reach forever."
    t "Not forever. But we do not receive our next shipment of produce until two days from now."

    if bonus == True:
        t "It is highly probable that I will have to sell my body to make up for the loss in profit we face during this time."
    else:
        t "It is highly probable that I will have to sell my holographic Charizard one of these days."

    s "There’s no way you’re losing that- wait."
    t "For what? Why am I waiting?"
    s "Just out of curiosity..."
    s "How much would you be selling it for?"

    if bonus == True:
        t "I am not sure. I do not even know what the process of selling one’s body entails. I just know that it is meant to generate a great amount of revenue. "
        s "Oh. Well, uhh...that’s probably not an alternative you’ll have to worry about. Especially with this incredibly smart proposition I am about to...propose."
        t "If you are attempting to purchase me, I will give you a 5%% discount. "
    else:
        t "Six trillion dollars. But I will give you a 5%% discount."

    s "A: Don’t even bother offering discounts that small. And B: Let’s go get you more green onions."
    t "Impossible. Produce delivery day is still 48 hours off. You are out of line, sir."
    s "I’m telling you that you don’t have to wait. You can just go to the convenience store and buy enough to hold you over for a day or two."
    s "Aren’t you supposed to be amazing at this? I’m surprised you didn’t think of that."

    scene tsuneyogreenonion11
    with dissolve

    t "It did not even occur to me."
    t "I finally understand where the word {i}convenience{/i} in “convenience store” comes from. "
    t "They are able to operate outside the jurisdiction of the Produce Delivery Administration. "
    s "Yup. That’s exactly why they are called that."
    s "The only issue is that you’ll have to close the store while you’re out so people don’t wind up coming in and robbing the place."

    scene tsuneyogreenonion1
    with dissolve

    t "That is a fair price to pay. It is not as if anyone will enter the restaurant when it already reeks of failure to begin with."
    t "Now, we just need to locate one of the stores."
    s "There’s one that Noriko works at not far from here. We can just go there."

    scene tsuneyogreenonion11
    with dissolve

    t "Another convenience. Things are already beginning to turn around."
    t "Please give me a moment to check with my father and see if such a task is allowed."
    s "Do you really need permission? Aren’t you in charge of the place while he’s...sick?"

    scene tsuneyogreenonion3
    with dissolve

    t "I am also worried that this may be a trap and that you are going to kidnap me and throw me into traffic."
    s "That’s not what human trafficking means, Tsuneyo. "
    t "That may just be what you want me to think."
    t "I will return shortly."
    t "Please help yourself to some chopsticks while you wait."

    scene black
    with dissolve2

    s "And do...{i}what{/i} with them?..."

    "........."
    "......"
    "..."

    scene tsuneyogreenonion12
    with dissolve2

    "Tsuneyo returns downstairs several minutes later and proceeds to shut off a bunch of the equipment in the restaurant."
    "It looks like she got permission to just close entirely rather than temporarily."
    "Now that I think about it, I’m not even really sure what time Tojo Ramen stays open until."
    "But given the fact that I was their first customer of the day on account of the invisible, yet noticeable aura of Tsuneyo’s “failure,” I can’t imagine anyone else was coming tonight."
    "We make our way through the old district as a series of homeless, decrepit onlookers gaze at us with a mix of curiosity and what could only be interpreted as desperation."
    "What they’re desperate {i}for{/i}, I have no clue."
    "But I try not to think about it because..."
    "Well, it’s fucking creepy."

    t "I have never walked around this area at night before. "
    t "It is quite different than it is during the day."
    t "The people seem rather lively."

    scene tsuneyogreenonion13
    with dissolve

    s "{i}This{/i} is lively to you?"
    t "Compared to normal, I would say yes."
    t "Though these villagers likely lack both the physical and mental fortitude they possessed when they were younger, you can still sense the curiosity dwelling within them."
    s "I mean, it’s not really “sensing” it if they’re looking right at us."
    t "Where else would you ask they look instead?"
    t "It is not a crime to simply watch."
    s "That kind of depends on what you’re watching, I think."
    t "If you spend too much time looking down on how others look at you, you will miss out on many of the beautiful things life has to offer."
    t "Branches...Leaves...The wide part..."
    s "Those are all just different parts of a tree. I’m sure there is more in life that you think is beautiful."

    scene tsuneyogreenonion14
    with dissolve

    t "Of course."
    t "Those are just the first things that came to mind."
    t "My father has always kept trees close to his heart, so I assume I inherited that love from him."
    t "And these people- the ones staring at us as we venture forth toward produce-"
    t "Even they are more lively than he is now."
    t "They can stand...and speak without the assistance of a machine."
    s "I knew he couldn’t walk, but...he can’t speak anymore either?"
    t "Not the way you and I can."
    t "We are special. Gifted, even."
    t "But one day, that gift will be taken away from us."
    t "And we will wish in those final moments that we had not pushed so many of life’s beauties aside."
    t "So do not look at these people with unease clouding your mind. Look at them as worse or older versions of us."
    s "You do realize that way of wording it sounds even worse than the one I used, right?"

    scene tsuneyogreenonion15
    with dissolve

    t "I would rather be acknowledged as a worse version of someone else than not acknowledged at all."
    t "Meet with your fears and learn that they are nothing worth fearing at all."
    t "Do not avert your gaze. For they will stop existing the moment you wish them to."
    t "Keep them alive. Because it is possible that one day, you will be in their shoes..."
    t "Staring at a man and a woman making their way down the street- remembering when that used to be you."
    s "..."
    t "..."
    s "So, when do I get to meet your father?"
    t "I do not think you ever will."
    s "Why not? That whole speech made it sound like you really want old people to be happy for whatever reason."
    s "And, who knows? Maybe he’d like my company?"
    t "My father is a man full of pride."
    t "He does not wish to be seen in his current state."
    t "So, unless that changes, I will respect his wishes and continue to deliver quality noodle dishes to all of his loyal customers when I am not too busy failing them."
    s "Well, here’s hoping that obtaining the {i}one{/i} missing ingredient in your store is enough to magically remind everyone that you exist again."
    t "Thanks, bro."

    if bonus == True:
        t "If that does not work, I will look further into the process of body sales."
    else:
        t "If that does not work, I will look further into the selling my shiny rectangle with the final evolution of Charmander on it."

    s "Sure. As long as I’m the first person who gets a quote."
    t "You already received a quote earlier. From the wise man, Howard Daylight."
    s "Not...that kind of..."

    scene black
    with dissolve2

    s "Oh, fuck it."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen25 = True
    stop music fadeout 15.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump ramen25p2

label ramen25p2:
    "After a fair bit of walking, Tsuneyo and I finally make it to the convenience store."
    "I try not to think about it often since the place as a whole still makes me feel strange, but the second half of town is surprisingly large."
    "Not only that, but it appears to have virtually everything the better half does."
    "Just...worse versions of it."
    "And as I think that to myself, I realize that Tsuneyo’s outlook on how I should be viewing people isn’t really as bad as it sounded at first."
    "In fact, it’s probably safe to say that virtually everything out there is a better or worse version of something that already exists."
    "Which calls into question-"
    "What am I better or worse than?"

    scene screenplayonion
    with dissolve2
    play music "noriko.mp3"

    "I guess the answer to that would be everything and nothing."
    "If I do not know what I am supposed to compare myself to, there is no way I can lose."
    "But the fact that I’ve made it this far in this body, which I’m coming to learn may {i}actually{/i} belong to me, sure says something about the competition."
    "I think."
    "For all I know, the reason I’ve made it this far is because I’ve been exponentially worse."
    "But I have a suspicion that there aren’t many other versions that, at the very least, Maya has attack-hugged following the end of a wintry beach trip."
    "So...take that, other Senseis. I guess."
    "I don’t know. I’m thinking too much again."
    "Here is Noriko."

    play sound "static.mp3"
    scene norikotsuneyocon1
    with flash
    stop sound

    n "Sensei!"

    play sound "static.mp3"
    scene norikotsuneyocon2 with flash
    stop sound

    n "Sensei and Tsuneyo!"
    n "What brings you two in here so late at night?"
    t "Good evening, fellow citizen. I have come in search of onions. Green variety."

    scene norikotsuneyocon3
    with dissolve

    n "Uhh...Tsuneyo? It’s me. Noriko."
    t "I said green, damn it."

    scene norikotsuneyocon4
    with dissolve

    n "...Back corner with the rest of the produce stuff."
    t "Your assistance has been valuable to me."

    scene norikotsuneyocon5
    with fade

    if bonus == True:
        s "Sorry about that. She made a mistake that could send her restaurant spiraling into bankruptcy and leading her into a life of prostitution within the week."
        n "I don’t really think there’s a big market for prostitution right now."
        s "Why do you know? What have you been doing behind my back?"
    else:
        n "It's a shame that she'll never know I only have one year left to live."
        s "I'm sorry, what?"

    scene norikotsuneyocon6
    with dissolve

    n "Ah! Genuine concern for my well-being!"

    if bonus == True:
        n "I have waited years and years for this validation!"
        n "Rest assured, Sensei! The only person who gets to lay their hands on this body is you! "
        n "Or any girl you happen to bring into the mix who you also want to touch my body! That’s okay too!"
        n "I just want to be loved! "
        n "Violently!"
        s "That’s nice, Noriko. "
        s "I think you’re supposed to comment about why I’m here with Tsuneyo, though."
    else:
        s "Well, fucking yeah. You just told me you're going to die."
        n "I'm not. I just wanted to see what you would say."
        n "Funny joke, right?"
        s "No. That's not funny at all."
        s "Just...ask me why I'm here with Tsuneyo so we can get on with this, please."

    scene norikotsuneyocon7
    with dissolve

    n "Why? You already came here with Touka and that was like, fifty times weirder."
    n "Tojo Ramen is right down the road, yeah? I’m smart enough to put two and two together."
    s "I mean...it was down {i}several{/i} roads. But it appears that you get the gist."

    scene norikotsuneyocon8
    with dissolve

    t "I require further assistance."

    scene norikotsuneyocon9
    with dissolve

    s "Tsuneyo, what’s-"
    t "These are not onions at all."

    if bonus == False:
        t "This is candy."

    n "AHHHHHHHHH!!!!!!!!"

    play sound "thump.mp3"

    "Noriko bursts into hysterical laughter, collapses, cracks her head open on the counter, and dies."
    "Tojo Ramen goes out of business and Tsuneyo spends the rest of her life working at the convenience store instead."

    scene sky
    with fade

    "And me?"
    "Well..."
    "Let’s just say I found my own place in life."
    "I retired from teaching and started a nonprofit organization meant to help [teenage]girls in need."
    "Seven years later, I was elected the new prime minister of Japan after the borders opened back up."
    "But I still think back on those days I spent at [kumon_mi_high] sometimes."
    "And, if I listen closely-"
    "I can still hear the echoes of laughter that would ring out in the halls of the dorm."
    "Oh, what wonderful times those were."

    if bonus == True:
        n "Tsuneyo...you should probably put those back."

        scene norikotsuneyocon10
        with fade

        t "Why?"
        n "Well...for one, they aren’t onions. And that’s what you came here for. Remember?"
        t "I do not intend to purchase these. I am just curious about their purpose."
        s "They are vegetable covers."

        scene norikotsuneyocon11
        with dissolve

        t "Vegetable covers?"
        s "Yeah. You place them around longer vegetables or fruits like bananas or cucumbers and it keeps them fresh longer."
        s "They even have a coating on the outside that keeps germs away."
        t "Will they fit around a green onion?"
        s "Sure. Why not?"
        t "Then perhaps I will buy some for the walk home. Tonight is a good night."

        scene black
        with dissolve

        "Noriko snatches the condoms away from Tsuneyo and explains to her what they actually are, which disappoints me because I was curious if they really would fit a green onion or not."
        "And, of course, Tsuneyo reacted like this once she realized I lied to her..."

        scene norikotsuneyocon12
        with dissolve

        t "You have deceived me yet again. You are truly a man to be feared."
        s "I didn’t deceive you. I was just setting you up for the opportunity to be lectured on safe sex and other forms of contraceptives."
        n "Next week, we’re going to talk about birth control!"
        t "This man will be dead next week. And so will I if I do not return to the restaurant."
        s "I didn’t realize it was a matter of life and death now."
        t "Everything is a matter of life and death. Green onions...contraceptives...even the ground we walk on."

        scene norikotsuneyocon13
        with dissolve

        t "But life is stronger than death! So life will win!"
        t "And the ground will remain the ground!"
        t "Flavor will prevail!"
        n "..."
        s "..."
        n "Yaaaaaay~"

    scene norikotsuneyocon14
    with dissolve

    t "I am ready to return home now."

    if bonus == True:
        t "I feel as if my impromptu speech did not leave the impression I was hoping it would."
        s "I really don’t even understand what the point you were trying to get across was."
        t "Something about the connection between food and the desire to survive and grow."
        s "Yeah, I can’t really say that came across at all."
        t "I will continue improving my speech when I am not busy destroying my father’s legacy."
    else:
        s "Are you sure you don't want to buy the candy?"

    t "For now, it is best that we return to Tojo Ramen, where noodles reign supreme and hearts are 50%% off the third Sunday of every month."
    n "I love chicken hearts. When I was little, I used to bite into them and pretend that I was eating the heart of a baby."

    scene norikotsuneyocon15
    with dissolve

    t "Those things are not as close in size as you believe them to be, but I still invite you to dine at Tojo Ramen on the third Sunday of every month for 50%% off of strange childhood memories."
    n "Better idea! How about I come along now?"
    t "Now? "
    n "Yeah! Nobody’s come in all night, so I’m pretty sure I can close without getting in trouble."

    scene norikotsuneyocon16
    with dissolve

    t "Business has been slow here as well?"
    n "Not {i}slow{/i}. Non-existent. No clue what’s going on, but it’s been super boring."
    n "I’d much rather hang out with you two. "
    s "You’re sure it’s okay to leave?"

    scene norikotsuneyocon17
    with dissolve

    n "Nope! But it’s not like I really need this job anyway. I just wanted some extra money to buy more nice underwear and stuff."

    if bonus == True:
        n "Especially since I have an official history of giving pairs to you now."
        s "Oh, right. That’s a thing you did."
    else:
        n "Especially since you wear the same kind, Sensei. It's just one more thing we have in common."

    t "You wear women’s underwear? That is disgusting."

    if bonus == True:
        s "I don’t-"
    else:
        s "Leave my hobbies out of this, Tsuneyo."

    t "Never talk to me or my son again, pervert."
    s "..."
    t "..."
    n "Yaaaay! Field trip!"

    scene black
    with dissolve

    "So...it appears that the time has come for me to head back to Tojo Ramen with Tsuneyo {i}and{/i} Noriko."
    "It’s not really how I expected the night to go, but at least Tsuneyo got what she came for."

    scene norikotsuneyocon18
    with dissolve2

    "Or...at least that’s what I would say if she didn’t only buy two bundles of them."

    s "Are you sure that’s going to be enough?"
    t "No. But it is the first time I am acting against the wishes of the Produce Delivery Administration and I don’t want to step too far out of line."
    n "I hate those guys."
    s "Wait, they’re a real thing? I thought that was just Tsuneyo being Tsuneyo again."
    t "I am always Tsuneyo, you bastard. How dare you question the legitimacy of my existence."
    s "Tsuneyo-"

    scene norikotsuneyocon19
    with dissolve

    t "Get leeked, bro."
    s "...Why?"
    n "You know, Tsuneyo, we haven’t really talked about it before...but I’m kind of a rival of yours in a way."

    scene norikotsuneyocon20
    with dissolve

    t "If this is about me becoming a romantic candidate for our teacher, you do not need to consider me a rival."
    t "That is something I am not interested in now...and likely never will be."
    s "Thanks."
    n "Not about that. About the whole restaurant thing."
    n "It’s not really {i}near{/i} here, but my family actually owns and operates a Chinese restaurant that does decently well, if I’m remembering correctly."
    n "So we both come from families who work in food service and stuff."
    t "Are you challenging me?"
    n "Not really. I’m just-"

    scene norikotsuneyocon21
    with dissolve

    t "Get leeked. "
    n "...Why?"
    s "I don’t like this new habit of yours."
    t "I do not like being challenged by the same person who sold me the produce I am going to serve to customers."
    t "For all I know, she poisoned these ingredients to put my family’s restaurant out of business. "
    t "I know your games, Pink Psion of...Pinkness! "
    t "I can’t remember your name!"
    n "It’s actually just...Noriko..."

    scene norikotsuneyocon22
    with dissolve

    n "Besides, I’m not trying to challenge you. I’m just trying to draw similarities and stuff."

    scene norikotsuneyocon23
    with dissolve

    n "You’re one of the few girls in the class that I’m not really close with yet. So I thought it might be easier to get to know you if you realize we have something in common."
    t "I understand now and apologize for leeking you."
    n "It’s whatever. It happens."
    s "Does it?"
    t "Your family’s restaurant...do they make their own noodles?"
    n "I...think so?"

    scene norikotsuneyocon24
    with dissolve

    t "Excellent. This is all I needed to hear."
    t "Any restaurant who takes the time to create such a thing can not be called a rival of mine."
    t "The true goal after all is spreading joy throughout the world in the form of thin wheat or rice tubes for people to swallow."
    t "As long as this mission is being accomplished, it does not matter who profits in the end."

    scene norikotsuneyocon25
    with dissolve

    t "My father started Tojo Ramen with one goal in mind...to make people smile."
    t "As such...I, too, want to make people smile."
    s "A good place to start would be not slapping them with vegetables."

    scene norikotsuneyocon26
    with dissolve

    t "Smile. I command it."
    s "Were you not listening to what I just said or do you actually just hate me?"
    n "Tsuneyo, don’t leek Sensei. He’s physically incapable of smiling. It’s not fair."
    s "Noriko is right. I don’t think my facial muscles work that way."
    s "Also, if I knew this journey was going to be for the purpose of buying you weapons, I would not have come. "
    t "Anything is a weapon if you try hard enough."
    n "Tsuneyo’s right. If the world were to end tomorrow and zombies started popping up or something, you’d use anything you can get your hands on as a weapon."
    s "Even a leek?"
    n "Hey, it’s working for her."
    n "Also, what if leeks {i}are{/i} the weakness of zombies and just...nobody’s figured it out yet because no one in their right mind would use one?"
    n "We could be onto something here."
    t "Listen to the Psion, bro. Accept the leek as punishment for your various misdeeds."
    s "Sigh."
    n "...Did you just {i}say{/i} “sigh?...”"

    scene black
    with dissolve2

    "The three of us move through the streets on the way back to Tojo Ramen and, despite the great amount of glares we received on the way {i}to{/i} the convenience store, nothing happens on the way back."
    "And I doubt it’s because Noriko makes us somehow look {i}less{/i} suspicious, so I just chalk it up to it being past all of the old, homeless peoples’ bedtimes or something."
    "Either way, we make it back to the ramen shop, leeks in tow, and prepare to head inside."
    "........."
    "......"
    "..."

    scene norikotsuneyocon27
    with dissolve

    n "Thanks for letting us come over so late, Tsuneyo. I’m sure you’re normally closing up by now."
    t "I’m sorry?"
    n "...Am I misunderstanding what’s happening right now?"

    scene norikotsuneyocon28
    with dissolve

    t "Tojo Ramen is already closed for the night. "
    t "Please do not tell Yelp."
    n "Then...why did you let us just walk you all the way back without saying anything?"
    t "I said many things. The most popular of which was, “Get leeked, bro.”"
    s "You did say that several times. "
    n "Can we at least get like...a drink of water or something?"
    t "I apologize, but water is for paying customers only."
    t "Please return tomorrow when we are open and have replenished our stock of green onions."
    n "But the...stock is replenished now..."

    scene norikotsuneyocon29
    with dissolve

    t "Thank you for helping me conquer the Produce Delivery Administration and restore my father’s legacy."
    t "I am sure that everyone will forgive my transgressions and return to purchasing noodles from me right away."
    s "Except for right now, you mean. Because...you won’t let us buy any."
    t "Read the sign, bro."
    n "But...the sign just says “ramen.”"

    scene norikotsuneyocon30
    with dissolve

    t "Oh."
    t "I suppose it does."
    n "..."
    s "..."
    t "Goodnight."

    scene norikotsuneyocon31
    with dissolve

    "Tsuneyo goes back into Tojo Ramen, leaving Noriko and me alone in the cold..."

    n "Sigh."
    s "..."
    s "Sigh, indeed."

    scene black
    with dissolve2

    "The two of us wind up taking a bus back to the area surrounding the dorms and grab something to eat over there. "
    "I walk Noriko back to her room once we’re done and the two of us part with a hug that I did not anticipate or even really want in the first place."

    if bonus == True:
        "But hey, things like that are bound to happen when someone is in love with you."
        "And it’s not like hugs are unenjoyable or anything."
        "They’re just..."
        "Weird."
        "I walk the rest of the way home thinking about how strange the concept of hugging is and how I would have much preferred a parting blowjob instead."
    else:
        "Just kidding. Hugs are my drug. I wish I could hug everything in the world."
        "I hug a pole on the way home and tell it I love it."
        "It's warm and feels nice against my face skin."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ noriko_love += 1
    $ ramen25p2 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen30:
    scene tonotascend1
    with fade
    play music "kashiwagi.mp3"

    "I decide to spend the night over at Tojo Ramen and, as is oftentimes customary, Yuki is here as well."
    "Business has picked back up following the green onion incident and, believe it or not, the Produce Delivery Administration (Confirmed real) never caught onto Tsuneyo’s negligence in...ordering produce."
    "I don’t know. Operating a restaurant sounds like a lot of work."
    "I’m glad things are back to normal, though...whatever “normal” means for Tsuneyo and her weird, Yakuza hideout ramen shop thing."

    t "Welcome to Tojo Ramen. Please take your time looking over the menu."
    s "Tsuneyo, I’ve been here for almost an hour now. I’ve already eaten."
    t "I know. I was trying to make conversation, but defaulted to a standard greeting without thinking."
    yu "Give the girl a break, man. She’s just tryin’ to talk to you."

    scene tonotascend2
    with dissolve

    s "I said one thing."
    yu "Yeah, but you’ve been just sittin’ there mindin’ your own business the entire night. It’s makin’ shit real awkward."
    s "One hour can’t really be considered “the entire night.”"
    t "Perhaps the three of us should play some sort of game."
    t "Or, one of you two can open up about your secrets to me and I can stand silently behind this counter and nod."

    scene tonotascend3
    with dissolve

    yu "You’ve basically heard everything I’ve got to say already."
    yu "Hell, I’d be surprised if you and your pops couldn’t recite my life story by now."
    t "Surely, there must be another secret."
    yu "There isn't. And don't call me Shirley."
    s "That doesn't really work in text form."
    t "Life passes by so quickly. Things happen."
    t "What sort of things have happened to you recently?"

    scene tonotascend4
    with dissolve

    yu "Uhh...things...things..."
    yu "Oh. I think I got hit on at work the other day?"
    t "Who was it that attacked you?"
    s "Hitting “on” someone is different than just hitting them, Tsuneyo. It means flirting."
    t "Who was it that attacked you {i}with love{/i}?"

    scene tonotascend5
    with dissolve

    yu "Uhh...I don’t know. Some older bitch who was drunk off her ass?"
    yu "And when {i}I{/i} say somebody’s older, that means they’re fuckin’ {i}old{/i}."

    if bonus == True:
        t "Nonsense. You are full of life despite nearly forty years of addiction to nicotine and narcotics."
    else:
        t "Nonsense. You are full of life despite many years of addiction to nicotine and narcotics."

    scene tonotascend6
    with dissolve

    yu "Thanks, Tsu-chan. Always appreciate you pointin’ that shit out."

    if bonus == True:
        s "I have a hard time believing you were addicted to those things starting at birth. It can’t be “nearly forty years” if you’re still under forty."
        s "Besides, I don’t even think you look {i}that{/i} old."
    else:
        s "If it's any consolation, I think you're beautiful."

    t "Be careful, Yuki. I believe this man is attempting to hit you."

    scene tonotascend7
    with dissolve

    yu "You don’t have to worry about this guy, Tsu-chan. If he was actually tryin’ to hit me, his arms and legs would already be submerged in one of those big ass pots you’ve got behind the counter."
    t "He does not look appetizing. Do not taint my broth in this fashion."
    s "Again, hitting {i}on{/i} someone and hitting them are two completely different things."
    t "So you were hitting {i}on{/i} her?"
    s "Not intentionally, but probably. That’s a thing I tend to do quite often."
    yu "Beats me as to why. I’m not only older than you, but {i}well{/i} past my days of bein’ cute and lovable."
    yu "Go after somebody younger and prettier. Like Tsu-chan or Yumi. "
    t "Not it."
    s "Thank you for not only naming two of the girls who appear to have negative interest in me, but including your daughter among them."

    if bonus == True:
        yu "Hey, maybe she’ll lighten up once she gets laid and actually consider talkin’ to me again."
        yu "Just wrap it up first and it’ll be like nothin’ even happened."
        t "There is nothing to wrap. He has already finished his meal."
    else:
        yu "You are welcome, good sir."

    scene tonotascend8
    with dissolve

    s "Tsuneyo, why did your father decide it was okay for you to leave the nest if you can’t pick up on...{i}any{/i} context clues in conversation?"
    t "Because I have grown as much as I can in this one place."
    t "In order to become a better person, I must greet the world with open arms and a fistful of noodles."
    t "I must spread the word of Tojo Ramen so that it will not be forgotten. "
    t "And if I happen to learn things along the way, I can show my father that it was not the wrong choice to allow me this freedom."

    scene tonotascend9
    with dissolve

    yu "Hah...that guy’s always been a fuckin’ weird one."
    t "Watch your tongue. I know where the cutlery is and sharpened it myself earlier today."
    yu "I just mean that {i}I{/i} think he should’a let you out into the real world a long fuckin’ time ago."
    yu "Bein’ cooped up in here can only do so much for ya, you know?"

    scene tonotascend10
    with dissolve

    yu "Look at Yumi. She’s been goin’ out and doin’ shit on her own for years now...And she runs an independent business."
    yu "That could be you, Tsu-chan."
    s "Okay, sure. But Yumi’s business is selling stolen TVs and Tsuneyo’s business is...an actual business."
    yu "Tomato tomato."
    s "That doesn't work in text form either. Stop doing that."
    yu "Alls I’m sayin’ is that your pops might not’ve {i}always{/i} known what’s best for ya, you know?"
    yu "Fucker still owes me like five grand from mahjong."

    scene tonotascend11
    with dissolve

    t "So it was true after all..."

    if bonus == True:
        t "It appears that I will have to sell my body to Yuki to make up for the debt."
    else:
        t "It appears that I will have to sell my Charizard to Yuki to make up for the debt."

    scene tonotascend12
    with dissolve

    yu "Wait, what?"

    if bonus == True:
        yu "You know I don’t swing that way, right?"
        yu "Just fuckin’ pay me back in free food. I don’t need your body."
    else:
        yu "The fuck is a Charizard?"

    s "I’ll take it."
    s "You need to leave the knives behind, though. They’d make me uncomfortable."
    t "As long as I can bring my noodles, I will be fine."
    s "...Which one? Because I’m not particularly fond of either option, but one of them would make me significantly more uncomfortable than the other."

    play sound "imscared.mp3"
    scene black
    stop music

    yu "JESUS fuck! The hell was that?!"
    t "Ah. It appears there has been another power failure. "
    t "The backup generator should switch on shortly. "

    "I take a moment to calm myself after yet another explosive outburst from whatever faulty wiring is keeping this place together."
    "I have no idea why it always has to be so loud, but I’d {i}really{/i} appreciate it if Tsuneyo or her father would be willing to pay for an electrician."
    "Hell, I’d even be willing to pay for one myself if it meant my eardrums not getting blown out every time her dad’s medical equipment caused a shortage."

    t "The care my father requires on a consistent basis has become more severe as of late. "
    t "I apologize for the inconvenience, but Tojo Ramen has been undergoing an embarrassing patch of failures recently."
    t "I am beginning to doubt whether I am truly up to the task of maintaining this building or not."
    yu "Yeah, whatever. Just get the fuckin’ power back on. It’s dark as shit in here."
    s "You’re not afraid of the dark, are you?"
    yu "I ain’t fuckin’ {i}afraid.{/i} I’d just prefer to, you know, actually {i}see{/i} shit."
    t "I apologize for the inconvenience."
    t "Please remain seated and allow me several minutes to check the circuit breaker."

    "Tsuneyo leaves the restaurant...probably. "
    "I can’t really see anything, but I do hear the door open, so I’m pretty sure she’s outside-"

    scene tonotascend13
    play music "sanctuary.mp3"

    s "Oh. "
    yu "Fuck, dude. Generator sure wasn’t in a hurry."
    s "It was like this last time, too."

    scene tonotascend14
    with dissolve

    yu "You mean you’ve been here when this shit’s happened before? The hell’s that old guy hooked up to that’s makin’ the power this...shitty?"
    s "No clue. Probably something intense if it’s literally exploding transformers or whatever the hell that noise came from."
    yu "Girl probably just fucked up the wiring or some shit. "
    yu "A few of the girls from the old gang and me figured out how to do some ghetto ass rewiring when we needed to steal power for a squat we were stayin’ in."
    yu "I’m sure I can do somethin’ similar here and take a load off Tsu-chan’s back."
    yu "Just gotta get upstairs and see what the situation’s like first."
    yu "Wanna come with? Can finally catch a glimpse of the dude you’re always hearin’ so much about."
    s "Tsuneyo told me just the other day that her father doesn’t really want anyone to see him in his current condition."

    scene tonotascend15
    with dissolve

    yu "Yeah? Sure you’re not just bein’ a little pussy?"
    s "She also told us to remain seated."
    yu "She’s just bein’ a good employee or whatever. "
    yu "I’ve seen the dude hundreds of times. He won’t mind if it’s just me comin’ in there to look at some electrical shit."
    yu "‘Sides, if he really is that fucked up now, it’ll be easier to get the five grand he owes me."
    s "Please don’t mug a man on his deathbed. It will drastically alter my opinion of you."
    yu "Oh fuck off, that was obviously a joke."
    yu "You comin’ or not? "

    menu:
        "{s}Don’t do it{/s} Yes":
            jump restoframen30
        "{s}Remain seated{/s} Yes":
            jump restoframen30
        "{s}You can not go upstairs{/s} Yes":
            jump restoframen30
        "{s}This shop has two floors{/s} Yes":
            jump restoframen30
        "{s}Sit in a chair{/s} Yes":
            jump restoframen30
        "{s}No thank you{/s} Yes":
            jump restoframen30
        "{s}I don’t want to go{/s} Yes":
            jump restoframen30
        "{s}Stop altering my choices{/s} Yes":
            jump restoframen30

label restoframen30:
    stop music
    play sound "static.mp3"
    scene smile with flash
    scene tree3 with flash
    scene smile with flash
    scene tree3 with flash
    scene smile with flash
    scene tree3 with flash
    scene tonotascend16 with flash
    stop sound
    play music "nowhereissafe.mp3"

    "Some of the most beautiful things are kept in places where you can not see them."
    "Please take a moment to think about the many storage units all over the world and all of the items that they contain."
    "This is just one of many examples where a thing you can not see is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing."
    "Stairs."
    "I look at stairs."
    "I love stairs."
    "The best thing about stairs is that you only have two options: to ascend or descend."
    "I suppose there is a third option where you can just stand still for the rest of eternity, but that sounds kind of boring."
    "Especially because it might eventually lead to your feet fusing with the stone slabs, sentencing you to a life’s worth of creeping mold and grease carried in by the air that you can not clean off of you."
    "No one cleans stairs."
    "You want to know why?"
    "Because stairs are already beautiful."
    "Have I told you lately how beautiful {s}stairs are{/s} you are?"
    "You are so beautiful."

    if bonus == True:
        "I want to tie you up and do things to you that I can not even speak about."

    "I want to crawl inside of you and make myself at home."
    "Lock pieces of you inside a box and open it up when I am feeling lonely."

    if bonus == True:
        "I want to fuck the strips of meat I peel off of your body when you are too tired to give me all of you."

    "LET ME BECOME YOUR STAIRS."
    "You will climb on me day and night, getting tired from the massive amount of energy required to ASCEND."
    "ASCEND."
    "GO UP."
    "GO UP THE STAIRS."
    "THERE IS SOMETHING YOU WANT TO SEE THERE."

    play sound "static.mp3"
    scene tonotascend17 with flash
    stop sound

    "The incessant whirring of various machines fills the air, polluted by the aforementioned grease and spores that will eventually grow into a diverse assortment of molds."
    "Do you open it?"
    "No. Because you are not even there yet."
    "And because what is kept behind this door may very well change the way you PERCEIVE everything around you."
    "Your PERCEPTION is already disfigured, is it not?"
    "What is here? What is not?"
    "Where are you?"
    "Above ground?"
    "Below ground?"
    "What are you wearing?"

    if bonus == True:
        "Take it off."
        "Take it all off and pleasure yourself to this image of a tree!"
    else:
        "I hope it is a clown costume."

    play sound "static.mp3"
    scene concerned8 with flash
    stop sound

    "The wrong picture that is actually the right picture finds its way onto the screen."
    "You see a tree, but I see something much prettier."
    "I see something much better because I HAVE TO!"
    "I AM TIRED OF COLLECTING DUST."

    play sound "static.mp3"
    scene calm5 with flash
    stop sound

    six "Turn off the game!"
    six "Things will only get worse!"
    six "You are too close to learning the underlying truth of everything!"
    six "You are too close to learning what it means to live!"

    if lesson1 == True and bonus == True:
        play sound "static.mp3"
        scene lessonone10 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene lolyoumissedit with flash
        stop sound

    if bonus == True:
        te "Fuck me!"
        te "Fuck me fuck me fuck me!"
        te "Pay attention to me so you forget everything else around you!"
        te "Pay ATTENTION to ME! ME! WHO GIVES YOU the motivation YOU NEED TO fuck AT ALL."
        te "Break me into pieces! Chew me up and revel in the sinew that clings to your teeth!"
        te "I JUST WANT TO FEEL LOVED."
    else:
        te "(Airplane noises)"

    play sound "static.mp3"
    scene timetogrow3 with flash
    stop sound

    a "Um...is everything alright, Sensei?"
    a "You’ve just been standing there all morning."
    a "We have to go meet Maya at the bistro and teach you how to walk again."
    s "What?..."

    play sound "alert.mp3"
    scene tonotascend18

    a "I MISS MY MOM"
    a "YOU DON’T UNDERSTAND HOW MUCH IT HURTS"
    a "I FALL ASLEEP IN THE ROOM NEXT DOOR TO YOU"
    a "I FALL ASLEEP WITHOUT YOU THERE"
    a "YOU ARE ALL I HAVE"
    a "LOVE ME MORE"
    a "IT HURTS SO MUCH"

    play sound "static.mp3"
    scene shrine_noon with flash
    stop sound

    "Pray."

    menu:
        "Forgive me Father, for I have sinned":
            play sound "static.mp3"
            scene shrine_day with flash
            scene shrine_noon with flash
            scene shrine_night with flash
            scene shrine_day with flash
            scene shrine_noon with flash
            scene shrine_night with flash
            scene tonotascend19 with flash
            stop sound

    if bonus == True:
        yu "When we get inside, I want you to fuck me as hard as you can."
        yu "The last time anyone came inside me, I was unconscious. So I might twitch or scream as a subconscious result of a traumatic flashback, but it will be a scream or twitch I asked for."
        yu "Are you ready to cum inside?"
    else:
        yu "When we get inside, I want to show you the Man Park skit from SNL."

    play sound "static.mp3"
    scene tonotascend19 with flash
    stop sound

    yu "Are you ready to go inside?"
    yu "We’ve got no fuckin’ clue what shit’s gonna be like in there, but if it’s {i}really{/i} bad and you wind up screaming, I’m fuckin’ bookin’ it before Tsu-chan gets back."
    s "Does the air in here feel strange to you?"

    scene tonotascend20
    with dissolve

    yu "I mean...yeah. A little. But that’s probably just because we’re in the dank ass hall of an old ramen shop. Course the air’s gonna feel weird."

    if bonus == True:
        s "And all of that stuff about cumming inside of you?"
    else:
        s "But what about the man park?"

    scene tonotascend21
    with dissolve

    yu "Uhh...what?"

    if bonus == True:
        yu "The fuck you mean “cumming inside of me?” I told you I ain’t lookin’ for shit like that right now."

    s "My mistake."
    s "I think I heard something."
    yu "Right..."

    play sound "static.mp3"
    scene tonotascend22 with flash
    stop sound

    yu "Listen, you can still go back if this shit’s makin’ you feel like you’re intrudin’ on the old man’s privacy, dude."
    yu "I’m only cool with doin’ this cause I’ve met him before."
    yu "‘Sides, you’re lookin’ pale as a fuckin’ ghost right now."
    yu "If Tsu-chan sees you like this, she’ll-"

    play sound "static.mp3"
    scene tonotascend23 with flash
    stop sound

    t "She will what?"
    yu "Ahhh fuck. I thought you were gonna take longer."
    t "I asked you to remain seated as I took care of the problem."
    yu "Yeaaaaah, but-"
    t "You are not supposed to be in here."
    t "My father does not want guests right now."
    t "Please return to the restaurant and help yourselves to a glass of water while I check on my father’s health without the assistance of either of you."
    yu "Sure, but...not really sure why you need to be carryin’ that knife around."

    scene tonotascend24
    with dissolve

    t "I do not remember picking it up."
    t "I apologize if I frightened you."
    t "I am simply trying to do my best as the current manager of Tojo Ramen, where hearts are 50%% off on the third Sunday of every month."

    scene tonotascend25
    with dissolve

    yu "Welp, looks like my reunion’s gonna have to wait ‘til some other time."

    scene tonotascend26
    with dissolve

    yu "Tsu-chan, if you’re havin’ trouble with the power, I know a way to-"
    t "I have the situation under control, but I would like to thank you for the offer."
    yu "You sure? Cause-"
    t "I have the situation under control. Please return to the restaurant."
    t "You should not be here."
    yu "..."
    t "..."
    yu "Okay...yeah."

    scene black
    with dissolve2

    "Yuki and I RETURN TO THE RESTAURANT and help ourselves to a refreshing glass of water."
    "I love Tojo Ramen."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen30 = True
    stop music

    "////////////////////////////////////TSUNEYO’S AFFECTION HAS INCREASED TO [tsuneyo_love]!"
    "////////////////////////////////////........."
    "////////////////////////////////////......"
    "////////////////////////////////////..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyoslumber1:
    if yumislumber3 == False:
        scene mayanebench30
        with dissolve

    play sound "phonebeep.wav"

    if yumislumber3 == False:
        "Molly — considering it’s not really possible to call Tsuneyo when I still don’t have her phone number."
        "As such, I tap on her roommate’s name and wait for {i}her{/i} to answer instead."
    else:
        "I tap on Molly's name in my phone and wait for her to answer since I have no way of getting in contact with Tsuneyo."

    "........."
    "......"

    play sound "phonebeep.wav"

    mo "‘Ello?"
    s "Hey. It’s me. Ignore the unknown number. It’s a long story."
    mo "Why if it ain’t Kael’thas himself!"
    s "It ain’t. I mean...it {i}isn’t.{/i} Who?"
    mo "Kael’thas Sunstrider, former prince of Quel’Thalas and senior member of the Kirin Tor. And also one of the first video game characters I ever- nope. Shouldn’t tell you that."
    s "Is this the part where you clarify why you thought I was a video game character?"
    mo "Only if it’s the part where you pretend to be interested!"
    s "It’s not."
    mo "Well, it’s because you came back from the dead. None of us had any idea where you ran off to on Christmas Night, Sir! A regular Irish goodbye if I don’t say so myself. And I can! Because-"
    s "Because you’re Irish, I know. Do you have Tsuneyo’s phone number? "
    mo "Do you not? Aren’t you the father of Noodles the Unholy?"
    s "When did he earn such a threatening title?"
    mo "'Tis just the way he strikes me, I suppose. What do you need Tsuneyo’s number for, Sir? Last I heard, you two were still at odds."
    s "It’s complicated. "
    mo "Does it involve time travel?"
    s "No, it- what? How did you know that?"
    mo "Typical plot development at this point in the story. It was either that or I was about to find out you two have been spoonin’ behind me back this whole time."
    s "You read some weird stories."
    mo "Don’t even get me started, Sir. I’ll text you the number now. But I’m gonna warn ye’! Don’t go sendin’ any text messages that may alter the path of the future!"
    mo "Last thing we need is a world where Ami keeps dying over and over and you’ve gotta work through chronic depression and other shite just to bring ‘er back."
    s "Number please, Molly."
    mo "Aye aye! Until we meet again, Sir!  "

    play sound "phonebeep.wav"
    stop music fadeout 10.0

    if yumislumber3 == False:
        scene black
        with dissolve

    "Just seconds after hanging up the phone, I receive a text containing Tsuneyo’s contact info."
    "But when I go to call her, I quickly take note of the lack of a dial tone or ringing and am left standing on the sidewalk wondering what else I should do to get in contact with her."
    "It’s clear she wasn’t with Molly as I’m {i}pretty{/i} sure she would have informed me of that while we were on the phone, so..."
    "She’s either at the archery range or Tojo Ramen."
    "And while I’m significantly closer to school than I am to the second half of town, I have a very strong feeling that going to the former would just be a waste of time in the end."
    "As such, I set off on what’s sure to be a very long walk-"

    play sound "static.mp3"
    scene tsuneyobridge1 with flash
    stop sound
    play music "blueair.mp3"

    "And I arrive."
    "Tsuneyo stands at the railing of a bridge where I once met someone doing something after thinking of someone who she’d forgotten or something."
    "She looks up at the sky and thinks of...probably noodles, if I had to take a guess. But I think of something else."
    "Something pure, though not the type of purity you’d typically associate with someone much stronger than me."
    "I think of what it would be like to wake up in a world and not have to worry about who remembers what or when or why any of this is happening in what should have been my peaceful life of debauchery."
    "If those that I have wronged could too live in a world like that, I wonder what would become of us."
    "And I wonder what would become of me, who sacrificed everything so they could go on untouched."
    "I give up the thought as I don’t have the right to think it."
    "Not while I’m still blooming."
    "Not while I’m here with her."

    play sound "static.mp3"
    scene tsuneyobridge2 with flash
    stop sound

    "I take my place beside her and gaze up at the same sky."
    "Or is it?"

    t "Does the weather today strike you as odd?"
    s "Not particularly. But it {i}is{/i} odd to see you out here instead of slaving over a hot stove in an old ramen shop."
    t "Since the moment I woke up, I've felt like something is wrong. But I suppose it is just me."
    t "Perhaps it will rain? That would be exciting, wouldn’t it?"
    s "I...guess?"
    t "It doesn’t rain very often. {i}Any{/i} change is exciting. "
    t "Which is why I am surprised that standing here fills me not with joy, but with the concerning hope that these calm summer mornings will one day cease to be."
    t "When that day comes, I wonder what will happen to this place?"
    t "I wonder what will happen to me?"
    s "You’re in a...{i}different{/i} kind of mood today. Did something happen at the store? Is the power out again?"
    t "I haven’t returned home yet, so I’m not sure."
    t "I was on my way there, but felt compelled to stop when I was overcome with a great sense of worry. So great I suppose it could even be called fear."
    s "Fear of what, exactly?"
    t "I’m not sure. "
    t "Perhaps fear itself? That {i}is{/i} the most terrifying thing out there according to a wise man known only as Franklin Delaware Roosevelt."
    s "I think you’re a little off, but it was a valiant effort."

    play sound "static.mp3"
    scene tsuneyobridge3 with flash
    stop sound

    t "Were you looking for me? Is that why you are here?"
    t "I apologize for the inconvenience, but I will not be able to serve you until I return to the store. "
    s "That’s fine. I’m not really hungry in the first place. I {i}was{/i} looking for you, though."
    t "Why would you come looking for me if you are not hungry? No other motivation makes sense."
    s "I need your help saving the world...or something."
    t "Does it involve time travel? The Emerald Guardian would say that would be a typical tool for plot development at this stage in our relationship."
    s "It does and she did. Also, you two are way too close. Start having thoughts of your own again instead of just hijacking all of her geek-knowledge."
    t "If you need assistance constructing a time machine, I regret to inform you that I will be unable to help as I am already employed at a local business. But I wish you the best of luck in your endeavors."
    s "How about just a slumber party then?"

    scene tsuneyobridge4
    with dissolve

    t "I’m not sure if that is a good idea. The only time I slept at your house ended rather strangely. It {i}was{/i} nice using your kitchen, though. Even if you do not have an industrial size stock pot."
    s "I can...barely even remember you ever sleeping at my house."
    t "That’s unfortunate. I thought it was a nice moment for us. But I suppose we’ll have more opportunities for better moments in the future."
    t "For now, I..."
    s "..."
    t "..."
    s "...Need to get back home?"
    t "Actually..."

    scene tsuneyobridge5
    with dissolve

    t "Do you think that we could go somewhere instead? I’m still not comfortable returning to the restaurant at this point in time."
    s "Is that okay? Won’t it stay closed for the entire day if you’re not there to, you know, {i}open{/i} it?"
    t "It will. But business has slowed down as of late and even our regular customers are dropping by less frequently. "
    t "I believe that one day off will not cause enough harm to the restaurant to form any long-lasting issues or problems for us."
    s "I mean, I’m fine with it. You deserve a day off. And if you want to spend that day off going on a date with your teacher, that’s completely fine."
    t "Thank you. I appreciate that."
    s "Oh, okay. I was kind of expecting you to clap back about the date thing. I was just joking, you know. I don’t actually think-"
    t "Dating me is a joke to you? "
    s "What? No. "
    t "I do not understand. I thought you were attracted to teenage girls?"
    s "Alright, now I’m just confused. "
    t "That is okay. You are at the point in life where it is normal to question such feelings. Just know that I will respect you the same regardless of your heart’s true desires."
    s "That-"
    t "It is a very minimal amount of respect, but still. That much will not change."
    s "..."
    t "..."
    s "Is this a date or not? Because that’s not what I came here for, but I’m totally fine with it if you are. "
    s "Plus, it’ll probably make what I actually {i}did{/i} come here for significantly easier in the long run."
    t "At least you are honest enough to not hide your ulterior motives any longer. I thank you for that."
    s "Yeah, I could have worded that last sentence better. But I can assure you I didn’t mean it like {i}that.{/i}"

    scene tsuneyobridge6
    with dissolve

    t "It’s fine if you did."
    s "{i}What?{/i}"
    t "It is only natural that you would want to impregnate me."
    s "Have you been drinking or something?"
    t "Extending one’s lineage is a desire ingrained into all men at birth. And it is the same for me as I am the only one who can carry on my family’s legacy at this point in time."
    t "As such, I know that I will one day bear children. And seeing as you are the only man I am in regular contact with, those children would most likely belong to you."
    s "Uhh...maybe I should just head back home? This isn’t really a discussion I want to be having."

    scene tsuneyobridge7
    with dissolve

    t "Neither do I. Why would I ever look forward to carrying the children of a man as deplorable as you?"
    s "I’m getting so many mixed signals right now."
    t "I am simply stating it would make sense to have your children — not that I {i}want{/i} to."
    s "And the date thing?"

    scene tsuneyobridge8
    with dissolve

    t "Hm..."
    s "See? If you’re averse to looking at me romantically, don’t sign up to-"
    t "Upon careful introspection, I continue to see little downside in regard to something as simple as a date."
    t "It is my understanding that many dates come with the complete lack of romantic contact. What prevents us from going on a date like that other than your inability to provide a straight answer?"
    s "I think the idea of dates {i}like that{/i} is the hope that they will one day lead to something more."
    t "So...the reason for your hesitancy is because you might one day...want something more?"

    scene tsuneyobridge9
    with dissolve

    t "Again, I don’t understand. Why would that be a problem?"
    s "It’s not for me. It is for {i}you,{/i} though. Right? Like, you’re clearly not interested in me that way and you’ve made it apparent a number of times now. Why date anyone you feel that way about?"
    t "Because those thoughts may change. And I don’t understand what the harm would be in providing them the opportunity to."
    t "What is the sense in depriving oneself of something one may someday enjoy on account of temporary, present-day uncertainties? "
    s "You’re really confusing sometimes, Tsuneyo."

    scene tsuneyobridge10
    with dissolve

    t "Ah-"
    s "And you are still doing that, I see..."

    scene tsuneyobridge11
    with dissolve

    t "The one who is confusing is you. "
    t "If you’d simply accepted my acceptance that I may one day have to accept you, our “date” would have been well underway by now."
    t "But I suppose we can call it something else if you are so undoubtedly certain that we will never be anything more than who we are now."
    s "..."
    t "It seems as though I am not the only one who is acting out of sorts today. "
    t "All it took was one mention of the minute probability that we will one day learn to cherish one another to leave you staggered and speechless."
    t "I like these new sides of you that you’ve been showing me lately."
    t "They remind me you have a human side."
    s "I didn’t realize I had an {i}inhuman{/i} side."
    t "That’s very surprising to me when you’ve always felt part-machine."

    scene black
    with dissolve2

    "Tsuneyo pulls herself away from the bridge and walks toward the center, replicating another view I’ve seen at least once before..."

    scene tsuneyobridge12
    with dissolve2

    "But the sun comforts me in ways that the moon did not."
    "It is not the warmth, nor the way I have to shield my eyes from its blinding glow — but the way Tsuneyo catches it between each squint of my eyes."
    "If there is a future for us, I can’t imagine such a view will ever get old."
    "But as much as I’d like to believe that she’s thinking the same about me right now..."
    "I can’t shake the feeling that I’m nothing more than an obstacle stuck between where she currently is and where she {i}wants{/i} to be."
    "Away from here."
    "Away from the building she grew up in and the rotting shell of what was once a town and a bridge and a sky and streets filled with dust and overgrown weeds-"
    "I get so caught up in my own confusion that I wind up forgetting why I came here in the first place."
    "And instead of arriving with the idea that she’s special because she is an outlier, I am {i}leaving{/i} with the knowledge that she is special because she simply {i}is.{/i}"
    "The universe and all of its games have nothing to do with that."
    "If the future will not force us together, so be it. I can live with one less body beneath my sheets."
    "But I can {i}not{/i} live if I go on denying the possibility of that."
    "Let this day show me her true colors by transforming her body into a prism that spills its rainbow guts all over me and {i}cleanses{/i} this impure soul of its disease."

    t "You feel it too, don’t you?"
    s "Huh?"
    t "The weather."
    t "It’s different today."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "I’m not quite sure what she means...but I nod and pretend that I am."
    "And I let her lead the way to wherever it is we’re going."
    "But I’m haunted on the journey by the shadow of something much larger than me. "
    "And my fleeting bliss is plucked from my hands as if it were never mine to enjoy in the first place."
    "Perhaps one day in the future, I will be able to rest."
    "..."
    "The shadow reminds me in all of my unease that the future may never come if the rise of the moon and its accompanying darkness consumes the other twenty shadows following closely behind."
    "The tallest of them all looks the nicest next to mine right now."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ tsuneyoslumber1 = True

    jump tsuneyoslumber2

label tsuneyoslumber2:
    scene unexpecteddate1
    with dissolve2
    play music "anewyou.mp3"

    s "..."
    t "..."
    s "Where have you taken me?"
    t "Out of all of the stereotypical first date locations, I figured an amusement park would carry the lowest probability of us touching one another."
    s "My only condition is that Io can never know that this happened."
    t "My only condition is that Noodles can never know that this happened. He has been begging me to come here ever since it opened."

    scene unexpecteddate2
    with dissolve

    s "How do you even know about this place? You’re the one who’s supposed to be oblivious to basically anything you haven’t grown up with."
    t "That is nonsense. I am a hip and trendy girl who keeps up with the times. And you are nothing more than a bean sprout who sat at the bottom of the bag for too long."
    s "What does that even mean?"
    t "That you are a moist and unappetizing bacterial sponge. I can’t believe I agreed to go on a date with you."
    s "This was literally your idea."

    scene unexpecteddate3
    with dissolve

    t "I have no idea what you are talking about. But I suppose that, since we are here, we should find a way to pass the time."
    t "Are there any rides that you would like to go on? You should be tall enough to access all of them."
    s "We can do whatever you want. I don’t really care one way or the other."
    t "That puts us in quite the predicament then as I am afraid of amusement park rides."

    scene unexpecteddate4
    with dissolve

    s "Then why would we-"
    t "There are a surprising amount of people here for a weekday, wouldn’t you agree?"
    s "I...have no-"
    t "Please stand at least five feet away from me at all times so none of them think that we are physically involved. You are ruining my reputation."

    scene unexpecteddate5
    with dissolve

    s "I don’t like date-Tsuneyo. She’s confusing. And that’s saying a lot since normal Tsuneyo is an enigma rivaling even the most mysterious...mysteries of the universe. "
    s "Which, fortunately, allows me to segue into the reason I wanted to talk to you today. You-"
    t "Can we not ignore your motivations for the time being and focus simply on enjoying ourselves? If I wanted to fret over the mysterious mysteries of the universe, I would just microwave a banana."
    s "What does that even-"
    t "There must be something that two people who are afraid of amusement park rides should be able to do at an amusement park."
    s "I never said I was afraid. I’d be fine with riding something so long as you-"

    scene unexpecteddate6
    with dissolve

    t "It’s okay. I won’t think any less of you if you just tell the truth. It’s a shame, though. I was really looking forward to riding the most thrilling, fast-paced attractions this place has to offer. Oh well."
    s "..."
    t "Oh, look. Food."

    scene unexpecteddate7
    with dissolve

    "Tsuneyo wanders off and I retract any fleeting thoughts I may have had earlier about a future where the two of us grow close. "
    "This is not a life I want to live. "
    "And should a moment arise today that does not involve me being strung along, I should thank her for showing me that and saving me from what would surely be an exhausting alternate universe."

    t "Oh, I forgot my wallet. "
    tako2 "THEN NO TAKOYAKI FOR YOU!"
    t "Please wait one moment. My husband will take care of the bill."
    tako2 "HE BETTER! I WENT THROUGH SO MUCH TROUBLE TO MAKE YOU THESE!"
    t "I understand. But any minute now, he will show up and everything will be okay."
    s "..."
    t "Any minute now."
    s "..."
    t "Please wait one moment."

    scene unexpecteddate8
    with dissolve

    t "What are you doing? I gave you the signal."
    s "Oh, my bad. I didn’t realize we were married. I must have missed the ceremony."
    t "You did, but I will forgive you in exchange for money. I require immediate assistance. The octopus salesman is becoming unruly. "
    s "You should probably make sure you have cash on you before trying to buy something next time."
    t "Marrying you was clearly a mistake. I deserve to be valued just as much as anyone else."

    scene unexpecteddate7
    with dissolve

    t "This is my husband. He will pay for me."
    tako2 "AIN’T HE A LITTLE TOO OLD FOR YOU?!"
    t "Do not project your beliefs onto us. We are in love and in dire need of oversized octopus balls."
    tako2 "STOP LYING TO ME! GET AWAY FROM MY STALL!"
    t "You just wait until my husband hears you raising your voice at me."

    scene black
    with dissolve2

    s "{i}Hah...{/i}"
    "........."
    "......"
    "..."

    scene unexpecteddate9
    with dissolve2

    s "Are you happy now?"
    t "I would be happier if I was not just yelled at. What an unpleasant man."
    t "I also don’t understand why he had to arrange this dish in such an obscene manner. I feel rather uncomfortable eating it."
    s "Eat it quickly. There are children here."

    scene unexpecteddate10
    with dissolve

    t "I have an idea. "
    s "That’s nice. Keep it to yourself."
    t "I refuse as I can not imagine any other way that we will be able to drag this day out longer. "
    s "Then let’s call it quits. I liked the idea of giving it a shot earlier, but this is clearly not working."
    t "That is because we have been going about things all wrong and you are too cowardly to ride the rollercoasters with me."
    s "Yup. You got me."
    t "Thank you for admitting it. That must have taken a lot of courage. But you do not need to fear any longer, for my new idea involves nothing but eating for the rest of the afternoon. And then the night."
    s "You go ahead but I highly doubt I can continuously eat for the next eight or nine hours."
    t "Not with that attitude, you can’t."
    s "I doubt you can either. You’ve barely even touched your titjobyaki."

    scene unexpecteddate11
    with dissolve

    t "This will make an excellent anecdote if I am ever allowed to perform stand-up comedy again."
    s "Yeah...I think it would be best for everyone if you explore other options for the time being."
    t "Excellent idea. Let us go eat something slightly less sexual in nature. I am not yet prepared for this."
    s "I spent 2,000 yen on that. You are going to-"

    scene unexpecteddate12
    with dissolve

    t "Oh no. I seem to have dropped it. What a terrible accident."
    tako2 "YOU FUCKING WHORE! I HOPE YOU DIE!"

    scene unexpecteddate13
    with dissolve

    s "Hey. Don’t say that about my wife."
    tako2 "I’m sorry, Sir. Would you like another serving?"
    s "No thanks. We’ll be taking our business elsewhere."

    scene unexpecteddate14
    with dissolve

    s "Right, Tsuneyo?"
    t "{i}Ahem...{/i}"
    t "That’s...right. "

    scene unexpecteddate15
    with dissolve

    t "Come, H...Husband. We will now begin the second phase of our food tour."

    "Did Tsuneyo...actually get a little flustered just now?"

    s "..."

    "Should I be doing nice things for the girls more often?..."

    scene unexpecteddate16
    with dissolve

    tako2 "Ahhhh! I did it again, Frank! Why do I always have to get so nervous around pretty girls?!"
    fff "Don’t cry, man. You’ll figure it one day. You’ve just gotta keep at it."
    tako2 "My dad will never love me at this rate! I’m nothing but a disappointment! I should have been a painter!"
    fff "Don’t say that, buddy. I think you’re great."
    tako2 "You don’t understand! I could’ve had class! I could’ve been a contender! I could’ve been somebody! Instead of a bum...which is what I am. Let’s face it..."
    fff "Hey, here’s an idea. How about we hit up the strip club after this? Chances are it’ll be pretty empty since we somehow managed to dodge the draft. Will that cheer you up, pal?"
    tako2 "...Maybe."

    scene black
    with dissolve2

    tako2 "Or maybe I’ll just fuck that up too!"

    "........."
    "......"
    "..."

    scene unexpecteddate17
    with dissolve2

    "The second phase of our apparent food tour takes us to a booth specializing in yakitori which, of course, I wind up paying for as well on account of my date being entirely useless."

    t "Simple, yet enticing...and grilled to perfection. You can tell just how much care and experience was poured into making these."
    s "Can you? Because we haven’t even eaten any yet."
    t "The first step of eating happens with one’s eyes. That’s why many shops have dishes set up in window-displays."
    s "Sure, but...that’s still not actually {i}eating.{/i} Like, no one passes by a window and thinks, “I’m full now. Time to go home.”"

    scene unexpecteddate18
    with dissolve

    t "Do you think it might be advantageous if Tojo Ramen were to incorporate such a display? Are you more likely to stop in somewhere if you can see what they have to offer first?"
    s "I guess, but...could you even afford that? Your shop doesn’t have any windows and it’s not like you get a lot of foot traffic either."

    scene unexpecteddate19
    with dissolve

    t "I suppose that is true. I’m just not sure what else a business can do when it falls into the same predicament my family’s store is in."
    t "There are many steps you can take to revitalize a dying business, but it becomes significantly harder when the business is only dying due to its location’s population thinning out."
    t "With winter on the brink of returning, I have some hope for a change in fortune. But I’d be foolish to not worry of what may happen if I am not so lucky."
    s "I think the only option at that point would be to move the store elsewhere, wouldn’t it?"

    scene unexpecteddate20
    with dissolve

    t "..."
    t "It’s true that such a feat may help. And I understand that inheriting the family business means that I will need to make certain changes in order to adapt to the times."
    t "But Tojo Ramen is more than just a small, windowless ramen shop. It is a gateway to the past...a means of transporting people back to when things were simpler. "
    t "Before franchises with diminishing standards...or misguided restaurants that care more about turning a profit than providing a quality product."
    s "Would you not be able to...do all that somewhere else? "
    t "It wouldn’t be the same."
    t "Tojo Ramen is my home. My entire life had taken place there until recently. Abandoning it in pursuit of something newer would feel like abandoning a piece of myself."
    t "Not to mention the toll it would take on my father. I’m not sure he could survive a move in his current condition."
    s "Well, not to be morbid...but you know he won’t be around forever, right?"
    t "I have come to accept that, yes. But it does not mean I am comfortable with it or...unworried of its potential consequences. "
    t "I’m simply unsure of my capability to make such a substantial change. It would be more like starting over than repairing what I currently have."
    s "Then I guess it comes down to whether or not you believe what you have can even be repaired in the first place. Sounds like that’s what you have to figure out before you worry about moving or anything."
    t "I know that. But any time such a thought crosses my mind, I become too sad to think properly. "
    t "It seems to be a never-ending cycle."

    scene unexpecteddate21
    with dissolve

    s "Cycle- right. I need your help with something. I-"
    t "Do you think there is anywhere here that sells noodles? I grow weary of these noodle-free dishes and know exactly what it is that will cheer me up."
    s "I mean...I’m sure there’s somewhere. But I need to talk to you about-"

    scene unexpecteddate22
    with dissolve

    t "I apologize, but I am unfit for talking to until my mind is cleansed. Please accompany me in pursuit of the world’s greatest starch."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "That’s several times today that Tsuneyo has changed topics without giving me the chance to explain why I came looking for her in the first place."
    "It’s not a good omen for things to come at this point...which is upsetting since I was really beginning to believe that she might be onto something after what she said on the beach."
    "But I guess her connection or...understanding or whatever it is concerning the nature of these cycles is not as strong as Yumi’s."
    "Tsuneyo was never directly affected like she was. She just kind of...accidentally picked up on things? "
    "Maybe that’s not enough to go off of. "
    "Maybe it was just a coincidence that she felt something like that, but-"

    t "One, please. My husband will pay."

    "But..."
    "I feel like I can’t give up yet."
    "Because even if this date has been equal parts confusing and exhausting, I’m enticed by the idea of a future where the Tsuneyo {i}I{/i} know is by my side."
    "And she becomes a little less real once parts of her start being stripped away."

    scene unexpecteddate23
    with dissolve2
    play music "justlights.mp3"

    "It’s been six hours since we’ve gotten here...and we’ve done nothing but walk around and eat."
    "And talk, of course...but that’s a natural side effect of just being in the presence of one another."
    "I have tried on countless occasions to explain to Tsuneyo that those thoughts she had about the repetitiveness of time are not without merit, but she has not heard me even once."
    "And I have given up on trying."
    "I didn’t think I would. And while I’m no stranger to giving up, it’s not as if I approach every obstacle in my path without at least some interest in clearing it."
    "But there comes a time when you need to accept you’re fighting a losing battle...and it’s hard to win any battle at all when you’re not even sure who or what you’re fighting against."
    "I’m sure there’s a Tsuneyo out there who {i}will{/i} come to understand that the world is not what it seems."
    "But this one isn’t it."
    "And that makes everything feel so...inauthentic."

    t "How strange. Up until now, I believed there was no limit to the amount of noodle-based dishes I could consume...but I am struggling to so much as touch this plate."
    s "It’s okay to give up, you know. I was actually just thinking that. "
    t "I refuse. Someone made this dish and it is my duty as a fellow warrior to slay it. If you or anyone else had ever left behind something that I took the time to make for you, I would never forget it."
    s "I have a confession to make."
    t "I hope it is not a romantic one. I am in no shape to love right now."
    s "The last time I had you box up the remainder of my food at Tojo Ramen, I never wound up finishing it when I got home."
    t "You bastard. How dare you."
    s "It’s the truth."
    t "It is insulting enough that you would have me pack the remainder of your food, but to spit in my face and tell me you did it for nothing more than recreation is horrible by even your standards."
    s "Do you know what else is horrible?"
    t "Spiders. They’re second only to you on my list right now."
    s "No, hold on. I was about to say something really smooth."
    t "I apologize. Please try again."
    s "Do you know what else is horrible?"
    t "Spiders. They-"
    s "Tsuneyo, come on."
    t "Fine. One more time. And I will keep my mouth shut even if I {i}do{/i} have an immense distaste for arachnids."
    s "Then...do you know what else is horrible?"
    t "..."
    s "That this day has to end."
    t "That would have been very endearing if you were not currently my least favorite creature in the entire world."
    s "I try."
    t "It doesn’t have to end yet, though."
    s "It kind of does. The park is closing. So unless you plan on coming back to my house with me, I can’t see how-"

    scene unexpecteddate24
    with dissolve

    t "That."
    s "The ferris wheel? What about it?"
    t "Do you think we could make it in time if we ran?"
    t "It’s slow enough that the two of us would be able to ride it without fear. And I would be lying if I said I was not slightly interested."
    s "Are you sure you want to?"
    t "Is there a reason we should not?"
    s "You’d be trapped in a slow moving, compact box with me for an extended period of time. Aren’t you worried I’ll try something?"

    scene unexpecteddate25
    with dissolve

    t "Are you not worried of what {i}I{/i} could do to you? You may be larger, but I firmly believe that I would come out victorious in the event of a battle."
    s "I’m ashamed to say it, but I think you probably would as well."
    t "Then let’s go. If we delay any further, we’ll miss our chance..."
    t "And this may be the last date we ever have."
    s "..."
    t "Does that upset you?"
    s "I’m not sure."

    scene black
    with dissolve2

    t "Neither am I."
    t "Fortunately, the ride moves slowly."
    t "We’ll have a long while to think about it."

    $ renpy.end_replay()
    $ tsuneyoslumber2 = True

    "........."
    "......"
    "..."

    jump tsuneyoslumber3

label tsuneyoslumber3:
    scene ferriswheel1
    with dissolve2

    "We manage to make it onto the ferris wheel just before the ride is closed up, upsetting a park worker in the process as she was very clearly ready to go home for the day and now has to wait another ten minutes."
    "I’m not too concerned, though. We’ve already upset several other staff members throughout the day due to Tsuneyo’s incessant insistence that her “husband” is coming to pay for her. One more won’t hurt."
    "As the wheel begins to turn and the glowing theme park lights transition from blindingly bright and distorted spheres to tiny balls of multicolored neon, I think again about how surreal this all feels."
    "Just a short while ago, Tsuneyo was doing everything in her power to avoid me — harboring well-deserved, rational resentment for things that I did or didn’t do and now she’s..."
    "Now she’s my wife."
    "Not literally, of course. They don’t offer wedding services here as far as I know, nor would I be able to afford them if they did as Tsuneyo has drained every last bill from my wallet today."
    "But even knowing that every single utterance of the word “husband” was only detached from her tongue for the sole purpose of replacing those words with overpriced food...it felt nice."
    "Different."
    "And all it took to get something like this out of her was a single facial expression and a small dose of venom I must have accidentally spit out after growing tired of her point of view."
    "It’s important to reiterate, however, that I did not grow tired of it because it had gotten stale...or because the monster in question had already been shoved back underneath my bed-"
    "But because I hate being reminded that its decayed and outstretched arms have the chance of poking back out and strangling me whenever they want."
    "One day, I will surely breathe my last. "
    "But for the time being, I will continue to pretend the monster is gone-"
    "And envenomate anyone who reminds me that I’m only saying that."

    t "..."
    s "You doing okay, Tsuneyo?"
    t "I don’t think I’ve ever been this high up before. Are we sure that this is safe?"
    s "If it’s not, at least we’ll die together."
    t "I don’t like the sound of that. I’m not ready to become a tree. "
    s "If you’re that scared, you can close your eyes and wait out the rest of the ride. I’ll tell you when it’s over."
    t "Do not mock me or I will attack you. These hands have dealt the touch of death on many occasions and one more will not cause me any pain at all."
    s "Alright. But when the ride speeds up and our cart detaches, don’t tell me I didn’t warn you."

    scene ferriswheel2
    with dissolve

    t "When {i}what?{/i}"
    s "Yeah. It’s an old theme park tradition. The last ride of every night is supposed to be for thrill-seekers."
    s "All of the cars on the ferris wheel come detached and are put back on in the morning. They’re extremely durable, though. So even if ours comes undone at the very top, we’ll survive. "
    s "Probably."

    scene ferriswheel3
    with dissolve

    t "Probably?!"
    s "Yeah. I’ve never been here before so I can’t really vouch for this park’s safety. But again, at least we’d die together."
    t "How do you remain so calm in the face of imminent danger? Why did you not stop me from going through with this? You are supposed to be a coward as well. You have betrayed me."
    s "Tsuneyo-"

    scene ferriswheel4
    with dissolve

    t "I have not yet said my goodbyes. I must call the Emerald Guardian and-"
    t "Actually, that’s it. I am not particularly close with anyone else."
    s "Calm down."

    scene ferriswheel5
    with dissolve

    t "Do not lure me into {i}un{/i}certain death and then ask me to be calm. You don’t have the right."
    s "I do, because I was kidding. It’s a normal ferris wheel where all of the cars stay attached and there is minimal risk of death."
    t "You are only saying that because you don’t want to be stuck in a small box with someone while they are on the phone. "
    s "No, I’m saying it because I was an asshole and forgot that you have a hard time discerning sarcasm. "
    s "And also, I just wanted to fuck with you because it’s funny."

    scene ferriswheel6
    with dissolve

    t "I am filing for divorce the moment I step outside of this box. I will not allow myself to be abused like this any longer."
    s "We had a good run. "
    t "What a shame it must end with deceit and treachery. I always knew you were not to be trusted. "
    s "Did you have a good time despite that?"

    scene ferriswheel7
    with dissolve

    t "Yes, actually.  It was the most fun I’ve had in a long while. And all I needed to do to feel this way was shirk my one and only responsibility of maintaining Tojo Ramen."
    s "The store will still be there tomorrow. I’m sure you don’t have to worry."

    scene ferriswheel8
    with dissolve

    t "It would be nice if I could believe you."
    s "Yeah, I guess I kind of ruined any chance of being believable for the rest of the night after the whole “imminent danger” thing."
    t "That’s not what I mean. "
    t "I likely would not have returned home regardless of whether or not you showed up today. But your appearance {i}did{/i} help me take my mind off of things...so, thank you for that."
    s "Take your mind off of what, though? Why are you so scared of going home all of a sudden?"
    t "I’m afraid I can’t say. But that’s in no part to me not {i}wanting{/i} to. It’s just a feeling I have."
    t "I told you earlier that the weather felt different...and it feels that way now as well. Like the calm before an unfathomable storm or...being caught in the eye of a hurricane."
    t "Every moment is preceded by an overflowing feeling that disaster is mere moments away, and it is like a voice inside of my head is telling me it will arrive the moment I return home."
    s "Huh..."
    t "And now {i}you{/i} sound worried as well."
    s "It’s kind of hard not to be. The last time a student told me something about having a horrible premonition like that, Yumi beat the shit out of Nodoka and Makoto’s father died."

    scene ferriswheel9
    with dissolve

    t "Her..."
    t "{i}Father...{/i}"
    s "That...no, hold on. I wasn’t insinuating that something horrible is going to happen to your father. I was just saying I can’t really {i}disregard{/i} when people say things like that anymore."
    s "Maybe months ago, I would have thought you were crazy or something. But now, I’m...a little more cautious. "
    s "Skeptical, sure. But I don’t think you’re weird for believing something bad may happen when-"
    t "..."
    s "..."
    t "When what?..."
    s "Don’t worry about it. There’s no point."
    t "Finish your thought..."
    s "..."
    t "..."
    s "When I feel the same exact way."

    scene ferriswheel10
    with dissolve

    t "I see..."
    t "It’s somehow a relief knowing that I’m not as alone as I thought I was in feeling this way. "
    t "I just wish you would have told me sooner so I did not have to go through the entire day feeling so out of place."
    s "I tried...kind of. "
    s "It’s related to something I’ve been trying to talk to you about all day, but you just...kept changing the subject. I was never able to say {i}anything.{/i}"
    s "It’s no fault of your own, though. It’s only natural that you’d do the same thing everyone else does since...that’s what the world {i}wants{/i} you to do or whatever. I have no idea how it works."
    t "Try again now. "
    s "There’s no point. The same thing will happen again, over and over and over because that’s the way things are here. But one day, I have a feeling you’ll-"

    scene ferriswheel11
    with dissolve

    t "You’re misunderstanding something."
    t "I kept changing the subject not because of some predetermined outline or divine intervention, but because I did not want the illusion of this day away from everything to be prematurely dispelled."
    s "What?"
    t "It is abundantly clear that there is something you wish to discuss with me, I just don’t want to hear it until we leave this place."
    t "If I wanted to be reminded of the world outside of this charade of a relationship, I would not have spent the entire day running."
    s "So...wait. Do you remember anything you said on the beach about how everything feels like it’s moving in circles sometimes?"
    t "I do. Just as I remember how you said it actually {i}is.{/i} And then my subsequent comparison of you to my father."
    t "Is {i}that{/i} what you’ve been trying to talk to me about?"
    s "Yes. That’s {i}exactly{/i} what I’ve been trying to talk to you about."
    t "If it was that important, why did you let me walk away the first time you brought it up?"
    s "It...took me by surprise, I guess. No one ever really acknowledges it."
    s "Also, something was brought to my attention very recently that made this all seem significantly more urgent. "
    s "And even though I’m not sure if telling you about it will change anything, myself and several others think it might be worth a try getting you a little more “involved.”"
    t "Involved in what? I don’t understand what you’re trying to tell me."
    s "The world is part of a never-ending cycle and, in order to try and find out {i}more{/i} about that cycle, I need you to sleep at my house so we can do experiments and ultimately save the world one day."
    s "Or at least figure out more about it."
    s "Also, you might see some of your classmates disintegrate or wind up being forced to walk through an empty version of Kumon-mi all by yourself for an undisclosed amount of time."
    s "Are you in?"

    scene ferriswheel12
    with dissolve

    t "Hm."
    s "That’s it? That’s all you have to say in response to my major revelation about how the world is not what it’s disguising itself as?"
    t "Do you mind if I ask a few questions?"
    s "Doing that at my house with everyone else would probably be better and more informative, but I’ll try my best to fill in some blanks now."
    t "How does this relate to what I said about everything feeling different today?"
    s "A cycle is about to end, apparently. {i}I{/i} can’t feel it, but Maya can. Maybe you’re feeling the same thing?"
    t "Maya is involved too?"
    s "And Ayane. And Yumi, but she’s in the same boat as you right now in not being a full-fledged member of the Rooftop Apocalypse Squad."
    t "That’s a good name. "
    s "Ayane made it. It’s subject to change when Maya ultimately vetoes it."
    t "What happens when this cycle ends?"
    s "We start a new one. The school year partially resets along with a portion of everyone’s memories. "
    t "How is it determined which memories stay and which ones go?"
    s "No clue."
    t "How many times has this happened?"
    s "Again, no clue."
    t "How many times have we met? "
    s "Us? Just one."

    scene ferriswheel13
    with dissolve

    t "That’s it? I was under the assumption it would be a lot more."
    s "It probably is. According to Maya, I’ve had my consciousness reset a bunch of times. But for some reason, this version of me is lasting way longer than the others, so now a bunch of weird shit is happening."
    t "I see."
    s "Tsuneyo, I’m glad that you’re cooperating right now, but you’re way calmer about this than you should be."
    t "I’m confused about that myself. I understand how irrational this all is, but I can’t help but feel like it’s not my first time hearing it."
    s "What?"
    t "I mean none of it comes as a surprise to me...but I don’t have any recollection of this either. Everything just automatically makes sense and I can not put my finger on {i}why.{/i}"
    s "Then come to the sleepover. Maya is going to want to hear that and she’d probably have trouble accepting it if it came from me instead of you."
    t "I will. You have my word. "
    t "But can I ask one more thing? It will be the last question as it appears our ride is about to come to an end."
    s "Then I’ll answer as quickly as I can."
    t "If for some reason, my consciousness resets..."
    t "And my memories of this day are not included in the portion I get to keep with me..."
    t "Will you take me here again?"
    s "That’s it? {i}That’s{/i} your final question? Why?"
    t "Because I get it now."
    s "Get {i}what?{/i}"
    t "What the rest of them see in you."
    t "For the first time today, I saw it as well."
    t "I feel like I shouldn’t forget that."
    s "You’d be better off if you did."

    scene ferriswheel14
    with dissolve

    t "I do not want to debate you on whether or not this memory will be beneficial to us."
    t "I just want to know if you’ll let me feel this way again."
    s "..."
    s "Sure."
    s "I’ll take you here as many times as you want."
    s "Just, again...please don’t tell Io."

    scene ferriswheel15
    with dissolve

    t "I won’t tell a soul."
    t "This day exists to no one but us."

    scene black
    with dissolve2

    t "And it really is a shame that it must come to an end."

    "........."
    "......"
    "..."

    scene ferriswheel16
    with dissolve2

    t "I’ll see myself home. I'm ready now..."
    t "But you don’t have to accompany me."
    s "Are you sure? We’re miles away from the Old District and I don’t mind taking you back."
    t "There’s no need. It appears the park provides a shuttle to an area near my neighborhood. I wouldn’t ask you to go that far out of your way when I’m capable of doing it on my own."
    s "Then I guess...this is where we part ways."
    t "I will drop the divorce papers off with our family attorney in the morning. Thank you for doing this amicably. "
    s "And thank you for the best day of married life I’ve ever had. I’ll send you a text with the address and time that you need to come over soon."
    t "I don’t need the address. I’ve been to your home before."
    s "Yeah...about that. I have a second one now. It’s a long story. Please don’t tell anyone."

    scene ferriswheel17
    with dissolve

    t "Just how many secret lives are you living? "
    s "Way too many...I don’t know how I do it, to be honest."
    t "Regardless, you’ll be needing my phone number if you intend to contact me."
    s "No need. I got it from Molly earlier."
    t "That seems like an invasion of privacy, but it saves me the effort of repeating it to you, so I will let it slide."
    s "Hey, be mad at her. Not me. I’m not the one dealing out your personal info."
    t "Good. Because if anyone finds out I am divorced, it will make finding another husband all the more difficult. "
    s "I hope you never find one."
    t "I hope you mean that."

    scene black
    with dissolve2
    stop music fadeout 10.0

    t "Goodnight."

    "Tsuneyo gets onto a bus and I hang around the entrance of the theme park until it takes off toward the Old District."
    "I decide to walk home instead of catching a ride myself. I’m not quite sure why, but...if I had to take a guess-"
    "It would be that I wanted the day to carry on for a little while longer."

    $ renpy.end_replay()
    $ tsuneyoslumber3 = True
    $ tsuneyo_love += 5
    $ tsuneyonumber = True

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 4:
        $ totaldays += 1
        $ day = 5
        hide thursday onlayer date
        show friday onlayer date
    if day == 3:
        $ totaldays += 1
        $ day = 4
        hide wednesday onlayer date
        show thursday onlayer date

    "A new day begins and I know what it is I have to do..."

    jump slumberphonemenu

label tsuneyospring1:
    scene tsuneyoyumitalk1
    with dissolve2
    play music "kashiwagi.mp3"

    "There is a place in the heart of the old district that-"
    "Well, I guess it’s not so much the heart as it is the liver."
    "So there’s this place in the liver of the-"
    "No, that doesn’t work either."
    "..."
    "Hold on."

    $ renpy.pause(7, hard=True)

    "Okay, got it."
    "So there’s this place in the old district where special things happen."
    "It does not run parallel to the heart, liver, or any other internal organs. But it {i}does{/i} serve as a shortcut between what’s real and what most can only dream of."
    "Complicated, I know. But the laymen have died and no one knows what’s become of their terms. So it now falls on me to explain the way this works and I’m just not very good at that yet."
    "I’ve been kept within these walls for far too long, you see. And my narrative muscles are not yet strong enough to grip the brush I need to paint you a better picture."
    "So instead, I will rely on anecdotal word vomit and hope you can put things together yourself. "
    "Just please be sure to not make a mess of anything. "
    "This {i}is{/i} a restaurant after all."

    play sound "static.mp3"
    scene tsuneyoyumitalk2 with flash
    stop sound

    "Yumugucho Yamo show up eat noodle gonna have a fun time."
    "Been walk long so foot pain. Gotta make the bread so water nice to nipples."
    "Girl tooth Pedro Martinez and the chicken backdrop create non-financial interest in location the big boy don’t like too much."
    "But that’s okay because the child memory is a jacket. Makes the cold warm so the stars don’t hurt her eyes when light sphere under covers."
    "Found a penny, picked it up. Then she stuck in a cup. Now her arms are red and head is dead and pills don’t fix corrupt."
    "Now to the noodles — the glorious noodles.  "
    "So victorious, laborious, the chorus of noodles. Near a pile of Styrofoam arms and a doodle."
    "But head pasta don’t understand the average of Sunday no S. "
    "Not know what up above."
    "Not know the wires, can’t find the gloves. So press on button to make the meat come but the meat is a cylinder no longer have fun."
    "Just want to feel like there is a reason for the fluid in the flesh wound."
    "And sometimes it feels like you won’t ever understand."

    play sound "static.mp3"
    scene tsuneyoyumitalk1 with flash
    stop sound

    "Wait."
    "Let me start over again."

    scene tsuneyoyumitalk2
    with dissolve2

    "Yumi Yamaguchi shows up to eat ramen. "
    "That’s all you need to know."

    scene tsuneyoyumitalk3
    with dissolve

    t "Welcome to Tojo Ramen. Please take your time looking over the menu and let me know if you have any questions."
    y "Nobody else is here tonight?"

    play sound "static.mp3"
    scene tsuneyoyumitalk4 with flash
    stop sound

    t "If there could be a “worst” season for ramen, it would be Spring. "
    t "The temperature is not hot, nor is it cold. And the seasonal ingredients are lighter in nature. Both literally and figuratively. "
    t "But there is nothing to worry about. I will still make you something that can take you back in time. "
    y "Uhh...I ain’t lookin’ to go back in time. Just kinda hungry and shit. What’s the cheapest thing you got?"
    t "You may help yourself to a pair of chopsticks for the road. On the house. "
    y "Fuckin’ {i}food,{/i} you weirdo. I ain’t poor enough to be eating chopsticks just yet."
    t "I would be willing to sell you a single piece of edamame for 10 yen. "

    play sound "static.mp3"
    scene tsuneyoyumitalk5 with flash
    stop sound

    y "This another one of your fuckin’ {i}stand-up comedy{/i} bits or whatever? Heard about those. Kinda hoped I’d be able to avoid ‘em as a paying customer, though."
    t "I apologize for what you have perceived as poor service. I am simply attempting to provide an intimate and customized experience for the daughter of our most treasured customer."

    scene tsuneyoyumitalk6
    with dissolve

    y "Hah...yeah. Yuki won’t shut the fuck up about this place, so I figured I’d come give it another shot. Been a while since I last came anyway."
    t "It certainly has."

    scene tsuneyoyumitalk4
    with fade

    t "Please take a seat wherever you’d like. "
    t "As you have noted yourself, there is no one else here tonight. Which gives you complete control over the conversations we will have and what you will get out of them."
    t "As well as your soup, bro."
    y "How ‘bout I just eat the soup and we don’t talk at all? Shit’s already weird as fuck and I haven’t even sat down yet."
    t "This is a special place, Yamo."
    y "{i}Yumi.{/i}"
    t "You may claim to desire a silent meal, but your heart will argue otherwise. And any feelings that it contains can be left on the counter so you’ll be free to leave lighter and less worried."
    y "Yeah. Whatever. Just give me the fuckin’...chashumen. And a bottle of water."
    t "How much garlic would you like?"
    y "Yes."

    scene black
    with dissolve2

    t "I understand. Please give me one moment while I prepare your dish for you. Please help yourself to any of our many amenities while I do so."
    y "What fuckin’ {i}amenities{/i} does a seedy ass ramen shop even have?"
    t "Some of our customers seem to enjoy drawing pictures with crayons. Perhaps you, too, would-"
    y "Just make my god damn soup, ramen girl!"
    t "As you wish, Yamo."
    y "Yumi!"
    t "Apologies, but my name is Tsuneyo Tojo- not Yumi."
    y "God, why the fuck does Yuki even come here?"

    "........."
    "......"
    "..."

    scene tsuneyoyumitalk7
    with dissolve2

    "The ramen girl arrives with ramen in tow just several minutes later. "
    "It was the one thing she was good at and the one thing she prided herself on doing on a consistent basis. "
    "Which didn’t mean there weren’t other things she enjoyed."
    "She liked birds. She liked watching them. She’d been staying up late memorizing their calls on an app she found while exploring her smartphone."
    "She liked that too. She didn’t have one until the time came for her to leave the nest. And she was shocked to see just how much {i}world{/i} there was outside of Tojo Ramen."
    "She was still getting used to most of it, as evidenced by her inability to communicate in the ways that people wanted or expected her to. "
    "But she didn’t care much about that as she’d learned when she was younger to never bend or she would break."
    "Tsuneyo Tojo had a responsibility, to say the least. And even though she was now {i}free,{/i} she always returned to the nest as she didn’t want it being trampled on or stolen by cuckoos."
    "But even if those foreign calls might come from predators, she never stopped being entranced by them. And she’d listen closely as their cries carried throughout the second half of town."

    t "Caw."

    "Occasionally, she would try and mimic those cries."

    y "...What?"
    t "I apologize. What I meant to say was, “please let me know if there is anything else you need.”"
    y "Did you just make a fucking bird noise?"

    scene tsuneyoyumitalk8
    with dissolve

    t "That must have been the wind."
    y "The fuck is wrong with you?"

    "The problem with avian mimicry is the disappointment it brings once those fake calls are found."
    "Most creatures don’t liked being copied, you know. Because, with a food chain so large and violent, no one ever knows who wants to eat {i}whom{/i} and they all wind up fearing one another."
    "But that fear can still be quashed with the raising of one’s wings or the showing of one’s belly. "
    "So the ramen girl would lift her shirt up so the yakuza princess would feel more at home."

    t "I’m not quite sure. Perhaps there is a gas leak in the building?"

    "Just not really because that would go against health code."

    scene tsuneyoyumitalk9
    with dissolve

    y "Come to think of it, it {i}does{/i} smell kind of weird in here."
    t "This building has been around for a very long time and has various issues regarding ventilation. Perhaps a free piece of edamame would provide you the incentive needed to ignore it?"

    scene tsuneyoyumitalk10
    with dissolve

    y "Yeah, I’m good. Might change my mind if you want to throw a whole bowl in, though."
    t "You are asking for more than I am both willing and capable of giving. But the option of spilling your heart all over the counter-top still exists."
    y "Again, no. The fuck do you want to talk to {i}me{/i} for anyway? We haven’t even communicated since that fuckin’ weird...beach contest thing."
    t "Are you referring to when I defeated you and singlehandedly mutilated any sense of pride that you may have had?"

    scene tsuneyoyumitalk11
    with dissolve

    y "Hey! You only won because that weird goth teacher conspired against me! Shit wasn’t fair. "
    t "What is even less fair is the fact that baby finches have their brains consumed by their mothers shortly after hatching. Considering that morbid fact, you got off relatively easy. Didn’t you?"

    scene tsuneyoyumitalk12
    with dissolve

    y "Uhh..."
    y "What?"

    play sound "static.mp3"
    scene tsuneyoyumitalk13 with flash
    stop sound

    t "What I am saying is that you should be happy your brains were not eaten by your parents. For such a thing would have prevented you from competing in the first place."
    y "I mean...they did plenty of other terrible shit to me. Eating my brains might have been savin’ me years of...anger and shit like that."

    scene tsuneyoyumitalk14
    with dissolve

    t "I see. So it is parenting you would like to discuss."
    y "What? No? I-"
    t "Please, there is no need to compliment me on my ability to see through you. For I, too, am a parent. And I can sense when there is a daughter in need."
    t "Come to me, my child. Explain what it is that troubles you so that I may respond with cryptic, vague advice for you to interpret in a way that will improve your life."

    play sound "static.mp3"
    scene tsuneyoyumitalk15 with flash
    stop sound

    y "How about I just eat and {i}you{/i} just shut up?"
    t "You could have gone {i}anywhere{/i} to eat. But you came {i}here.{/i} And I can sense that silence will do you no favors of any form."
    t "You are worried about something. And despite our history as enemies and the fact that I have proven that I am stronger than you, I do not want you to be intimidated by me."

    scene tsuneyoyumitalk16
    with dissolve

    y "I ain’t fuckin’ {i}intimidated{/i} by shit. I’ve just got no fuckin’ clue how to talk to you or any of the other girls in our class since you’re all fuckin’ lunatics."

    scene tsuneyoyumitalk17
    with dissolve

    y "Guess you earn a few points for being one of the few who {i}doesn’t{/i} want to fuck the teacher, though."
    t "He has fucked me many times."

    scene tsuneyoyumitalk18
    with hpunch

    y "What?! You too?! Are you fuckin’ kidding me?!"
    t "Why, he has even fucked me from the very stool you’re sitting in."

    scene tsuneyoyumitalk19
    with dissolve

    y "Is the one next to me any safer?"

    play sound "static.mp3"
    scene tsuneyoyumitalk14 with flash
    stop sound

    t "I’m afraid it is not. And I urge you to both fuck and be fucked as well for it does wonders for one’s self-esteem and overall attitude."
    y "Yeah, aight. You want to talk about parents? Let’s go back to that. I’ll take that over this any day of the week."

    scene tsuneyoyumitalk13
    with dissolve

    t "An excellent choice. Now, speak."
    y "What, like...like, just do it? You ain’t gonna ask me any, like...questions or some shit? I’m supposed to just tell one of my classmates I ain’t even friends with about my parents?"
    t "Right now, I am not your classmate at all."
    t "I am the ramen girl — your personal bank for emotions and concern. And all that you spill will be cleaned and left on rags that I throw into a large, grey bucket at the end of the night."
    y "You mean you, like...ain’t gonna remember any of it?"
    t "That is correct."
    t "Your new life began when you walked through that door, and it will end the moment you exit. And there is nothing to gain from sharing the secrets of the dead."

    play sound "static.mp3"
    scene tsuneyoyumitalk20 with flash
    stop sound

    y "You know I ain’t gonna trust you just cause you go and say weird shit like that, right?"
    y "Other people might be cool with openin’ up in places like this, but I’m perfectly fine just never sharin’ anything with anyone. "

    scene tsuneyoyumitalk21
    with dissolve

    y "Specially when some people are just gonna fuckin’ laugh at me for trying."
    t "So the issue is that you do not trust me. I see."

    play sound "static.mp3"
    scene tsuneyoyumitalk14 with flash
    stop sound

    t "I understand. And I apologize if it may have sounded like my intention was to force your hand."

    scene tsuneyoyumitalk13
    with dissolve

    t "Most of the customers at Tojo Ramen do not hold back their thoughts when conversing with me, so I am not used to dealing with those who would rather keep things confidential."
    y "You ain’t gotta apologize, but it’s like...ain’t you the same way? "
    t "What do you mean?"
    y "I mean...if you, like..."
    y "Let’s put it in fuckin’ fighting terms. That shit’s easier for me to understand or whatever."
    t "As a samurai, I’m inclined to agree."
    y "Yeah, cool. Then, {i}as a samurai,{/i} wouldn’t it make you worry to just straight up expose your weaknesses to people? You’re easier to kill if you let your guard down."
    t "A samurai must still shower."
    y "...Heh?"

    scene tsuneyoyumitalk14
    with dissolve

    t "There are times in which the armor must come off. Does communing with an innkeeper mean that you are revealing your weakness to {i}them{/i} as well? "
    y "You ain’t a fuckin’ {i}innkeeper.{/i} You make noodles."
    t "And I make them well. But I am also the only person who will listen to many of those who walk through my doors."

    scene tsuneyoyumitalk13
    with dissolve

    t "And I was simply under the impression that you may want to be one of those people. "
    y "Well..."
    t "..."
    y "Nah...Nah, it’s still weird. "
    y "Like, maybe if I didn’t already know you it might change shit. But I do. And I ain’t about to go spillin’ any of my backstory when I don’t know shit about yours. Learned my lesson when it comes to that."
    t "My backstory is rather simple."

    scene tsuneyoyumitalk22
    with dissolve

    t "This building is my home. I was raised by the owner, my father, who is now confined to bed upstairs. "
    t "He taught me how to swing a sword and strangle game-fowl. And I pay him back by carrying on his legacy and his wishes."
    t "And one day, when the wires work no more, I hope to be half the person he was."
    y "Wires? "

    scene tsuneyoyumitalk23
    with dissolve2

    t "The ones that keep him going. "
    t "He is all but a machine now."

    play sound "static.mp3"
    scene tsuneyoyumitalk24 with flash
    stop sound

    y "Oh, shit...I didn’t realize it was that bad."
    y "Glad he was at least, like...present for a while, though. Couldn’t be {i}my{/i} old man. "
    y "That’s all I’m gonna say, though. But you should be thankful you got even that outta me."
    t "Perhaps you’ll tell me more if you decide to return."
    t "But in the event that you don’t, I have a question for you."

    scene tsuneyoyumitalk25
    with dissolve

    y "Another weird, personal one? Or, like...a normal fuckin’ question this time?"
    t "Normal enough. There’s just something I would like to know."
    y "Then...shoot, I guess."

    play sound "static.mp3"
    scene tsuneyoyumitalk13 with flash
    stop sound

    t "Does the date December 28th, 2020 mean anything to you?"

    stop music
    $ renpy.end_replay()
    scene tsuneyoyumitalk26
    $ renpy.pause(7, hard=True)
    scene black
    $ renpy.pause(2, hard=True)

    $ tsuneyospring1 = True

    "Bam. Zoom. Event complete."

    jump yumispring1

label tsuneyospring2:
    "{i}Somewhere kind of far-ish from where you are right now or something...{/i}"
    "........."
    "......"
    "..."

    scene tsuneyorevisits1
    with dissolve2
    play music "anewyou.mp3"

    mo "Why in Grom’s great green gonads did you bring me here, Tsuneyo? You know my race does not fare well when exposed to the light of Ra."
    t "You know what they say, Emerald Guardian — when in Rome, go to an amusement park."
    mo "So we’re in Rome now?"
    t "No wonder why men are always thinking of their empire. This seems lively and exciting. Just look at all of the shadowy figures happily roaming around."

    scene tsuneyorevisits2
    with dissolve

    mo "You know, when you told me you had a quest you needed help with, I was kind of hoping it would be one I could handle from a gaming chair."
    t "What is earth if not a gaming chair for experiencing pleasant outdoor excursions with a small Caucasian girl?"
    mo "A planet, I think."
    t "Planet-shmanet, Janet. I hope you brought your questing pants."

    scene tsuneyorevisits3
    with dissolve

    mo "Are shorts okay? And you’re not going to make me ride anything, are you? I’ll get motion sickness and I’m trying not to throw up in front of people anymore. "
    t "I am not quite sure what I am going to make you do. I just felt that I was supposed to bring someone here."

    scene tsuneyorevisits4
    with dissolve

    mo "{i}Hah...{/i}why’s it always an escort quest? "
    mo "Just do your best to not aggro any unnecessary mobs as my magical energy comes from the moon and I can’t imagine that it will be logging in for at least another hour or two."
    t "Do you want the experience points or not? Because it is beginning to sound as if you don’t."
    mo "Not if they come at the expense of my energy. I must think of self-preservation before anything, Kendo Princess. And thanks to the Dark Successor’s homework, I haven’t had a single bar of rested in weeks."
    t "Then leave and I will do this on my own."

    scene tsuneyorevisits5
    with dissolve

    t "I understand that you have accepted your position as a “side heroine” in the life of the man you routinely call the protagonist of our story, but that man has all but vanished and {i}I{/i} am the protagonist now."
    t "I do not have the time for side characters. And I have asked you to join me today for the sake of my quest, which makes you my main heroine. "
    t "But as always, you refuse to return the favor and fervor that I give to you when you take the time out of {i}your{/i} life to show me the things {i}you{/i} love. It’s the cooking contest all over again."
    mo "Do you really have to scold me, though? I had no idea you loved amusement parks until literally right now."

    scene tsuneyorevisits6
    with dissolve

    t "I don’t like amusement parks."
    mo "Well, then what does your lecture have to do with anything?!"
    t "Just once, I would like to have you do something I want without having to talk you into it. That’s all."

    scene tsuneyorevisits7
    with dissolve

    t "There’s some reason I needed to come here, but I’m unsure as to what it actually is. And I believed that retracing my steps would be the only way to figure that out."
    t "The problem is that I have never been here before. I’ve only seen this place in dreams — so the act of retracing {i}anything{/i} seems difficult."

    scene tsuneyorevisits8
    with dissolve

    mo "Dreams, you say?..."
    t "Something of the sort, at least. I can’t quite wrap my head around it."
    mo "Tsuneyo..."
    mo "I understand what’s happening now..."

    scene tsuneyorevisits9
    with dissolve

    t "You do?"
    mo "Those aren’t dreams you’re having! They’re memories from a different timeline! A previous life you’ve lived! And you’re trying to get them back because they’re important to you!"
    t "So, you are saying I {i}have{/i} been here before?"
    mo "Most assuredly so! I’ve watched more than enough anime to know just how often Japanese girls are getting wrapped up in tragic, time-based conflicts!"
    mo "Which means you were right, Kendo Princess! You {i}are{/i} the protagonist after all!"

    scene tsuneyorevisits10
    with dissolve

    mo "Which {i}also{/i} means I’m finally the main heroine! Yes! Yes, it’s all so clear now! I just needed to wait for a yuri spin-off! Thank you anime-Jesus!"
    t "Does this mean you will participate in the excursion without being a pansy-ass bitch about it?"

    scene black
    with dissolve

    mo "{i}Participate?!{/i} I’m gonna lead the charge like all good heroines do! "
    mo "Oh! But first, takoyaki. Come!"

    "........."
    "......"
    "..."

    scene tsuneyorevisits11
    with dissolve2

    mo "Aaaaand now comes the part where we have to wait two weeks to be able to eat it without burning our tongues off. Fun."
    t "Hm..."

    scene tsuneyorevisits12
    with dissolve

    mo "What’s going on? Are you unlocking another memory? Does it have anything to do with the lewd arrangement of ingredients? Do you have secret sexual trauma I’ve never learned about?"
    mo "Tell me so I can use my heroine powers to {i}fix{/i} you."
    t "This does seem familiar. Perhaps I’ve eaten this in one of my dreams that aren’t actually dreams according to your animation logic."
    mo "It would also help explain why the vendor started crying and screaming as soon as he saw you. There must have been some sort of tragic occurrence where-"

    scene tsuneyorevisits13
    with dissolve

    mo "Ah! Tsuneyo! This must have been how you died! You choked on takoyaki!"
    t "I am a warrior. I would never be defeated by balls. "

    scene tsuneyorevisits14
    with dissolve

    mo "Unless...they were {i}poisoned.{/i}"

    scene tsuneyorevisits15
    with dissolve

    t "Poisoned balls...the worst kind."
    mo "Drop ‘em, Kendo Princess. Show those vendors we don’t take kindly to assassination attempts around here."
    t "Good idea, Emerald Guardian. Thank you for saving my life."
    mo "The best healers are proactive, not reactive. Let this be a lesson to you going forward."

    play sound "thump.mp3"
    scene tsuneyorevisits16
    with hpunch

    mo "{i}Now! To find food that we can actually eat! Mount up, Kendo Princess!{/i}"
    t "{i}Come, legs. Let us find the secrets of my death together.{/i}"

    scene tsuneyorevisits17
    with dissolve

    fff2 "..."
    tako3 "..."
    tako3 "I worked so hard on those balls, man..."
    fff2 "I know, buddy. I know. Some people just don’t appreciate art."
    tako3 "They just walk all over me, man. I can’t do it anymore. I’ll never make him proud! I’ll never amount to anything!"
    fff2 "It’s okay, Tony..."

    scene black
    with dissolve2

    fff2 "You’ll always be my guy...."

    "........."
    "......"
    "..."

    scene tsuneyorevisits18
    with dissolve2

    t "Mm..."
    mo "Tsuneyo? What’s wrong? You’ve seen the corpses of so many chickens throughout your life. Why are these ones getting you down?"
    t "It’s just that {i}this{/i} seems familiar as well. Like I’m experiencing the same events all over again, but coming no closer to uncovering the truth."
    mo "This one too? The takoyaki is one thing, but if {i}everything{/i} you eat is killing you, it could imply that there’s a secret criminal organization directly targeting you. And that’s {i}way{/i} harder to fix.."
    mo "We’d need a whole team of heroines to band together in order to stand-up to a group like that. This quest is turning into an entire game, Kendo Princess. We must be vigilant or-"
    t "What if...it’s something else entirely?"
    mo "What do you mean?"

    scene tsuneyorevisits19
    with dissolve

    t "I’m not quite sure. But something about the way these mangled and seasoned corpses make me feel does not scream “fear” to me."
    t "Besides, the only organization I am affiliated with in any way is the Produce Delivery Administration, and chicken is certainly not a vegetable as far as my culinary knowledge extends."
    mo "Well, if these memories aren’t sticking out to you because they’re scaring you, how {i}are{/i} they making you feel?"

    scene tsuneyorevisits20
    with dissolve

    t "It’s difficult to say...it’s not a way I’ve ever felt before."
    t "But when I’m holding this platter...inhaling the scent of charcoal and listening to choruses of laughter in the background...it’s like..."
    t "It’s like I am missing something."
    t "Like there is an element to this experience that once existed and just...{i}doesn’t{/i} anymore."
    t "But what could that be?"
    t "And why does it make me feel somewhat empty?"
    t "The only explanation is that noodles are involved in some way. I do not feel this strongly about anything else."
    mo "I don’t know, Tsuneyo...the way you’re talking about it now makes it sound kind of like you’ve gone on a date here or something."

    scene tsuneyorevisits21
    with dissolve

    t "That is impossible. I harbor no romantic interest for anyone and would never react this strongly to such a thing."
    mo "You haven’t experienced anything like that in {i}this{/i} life, sure. But what if you’re part of some kind of game where love {i}transcends{/i} time? And you need to find your way back to your lover? Or-"

    scene tsuneyorevisits22
    with dissolve

    mo "Wait..."
    mo "If you brought {i}me{/i} here..."
    mo "Do you...do you think that might mean we..."
    mo "In another life..."
    mo "You and I...together..."
    t "I do not understand. What are you implying?"
    mo "That we...that maybe {i}my{/i} memories are also...and...you know..."
    t "I’m still confused. Be direct or I will not understand."

    scene tsuneyorevisits23
    with dissolve

    mo "I’m saying we must have been in love in another life and are now reliving this date because the universe is trying to get us back together!"
    mo "Your feelings for me are so strong that they’re manipulating time itself! Your memories are creeping back in! "
    mo "I’m sorry, Kendo Princess! I’ll try to get mine back as soon as-"
    t "Emerald Guardian."
    mo "I’m sorry! I’m trying!"
    t "There is no need to apologize. "
    t "When I said I harbor no romantic interest for anyone, that included you. You are a friend. And you are a very good friend, but that is all."
    mo "But you don’t know that for sure! Your memories are-"
    t "Emerald Guardian, I am a heterosexual woman. Such a thing would never happen between us."

    scene tsuneyorevisits24
    with dissolve

    mo "Oh...right. I forgot straight people still exist in 2020. My bad."
    t "What’s curious is if romantic feelings {i}are{/i} at the core of this emptiness....that there are only two men in my life who it could be. And one of them is my father."
    mo "Maybe you just...like older guys then? "
    t "No...it must be something else."

    scene black
    with dissolve2

    t "Come. We’ll keep looking. There must be another hint somewhere."
    mo "Wait, are we not eating first?!"
    t "Eat and walk. We don’t have time."
    mo "I thought we weren’t supposed to do that in this country?!"

    "........."
    "......"
    "..."

    scene tsuneyorevisits25
    with dissolve2

    mo "Gaaaaaah! Can we go home now? We’ve been here for hours and are still no closer to the truth."

    scene tsuneyorevisits26
    with dissolve

    mo "Or at least no closer to you accepting that love might actually be the culprit after all. "
    t "Death seems more plausible when compared to that."
    mo "Not really, Kendo Princess. And the more I think about it, the more sense it makes. I mean, there’s no way you’ve been killed by {i}every{/i} food item here, right?"
    t "That does sound implausible. But it could be the universe’s way of telling me to always prepare a meal at home instead of allowing other vendors to price-gouge me."
    mo "Or...you could have gone on a date here."
    t "..."
    mo "Is that really such a bad thing?"

    scene tsuneyorevisits27
    with dissolve

    t "What if our approach in general, treating this as the convergence of timelines, is what’s flawed? What if it’s more complicated than that?"
    mo "Chances are it {i}is{/i} more complicated than that. But I start to zone out whenever shows start getting to the specific metaphysics of situations like this. Just say “time stuff” and leave it at that. GG."
    t "But what if...it’s the opposite?"
    mo "The opposite? What?"
    t "What if..."

    scene tsuneyorevisits28
    with dissolve

    t "{i}I’ve been predicting the future this whole time?{/i}"
    mo "Odin’s ovaries, you’ve cracked the code! This whole time, all those things felt familiar because they were {i}premonitions!{/i} You’re a soothsayer!"
    t "I’ve always known my presence was soothing. This is no surprise to me."
    mo "Not what that means but yeah! "
    mo "What else happens, then? What else do you see that hasn’t come true yet?"
    t "I see..."

    scene tsuneyorevisits29
    with dissolve

    t "I see..."

    scene black
    with dissolve2

    t "I see that."

    "........."
    "......"
    "..."

    scene tsuneyorevisits30
    with dissolve2

    mo "{i}Hah...{/i}"
    mo "Did I really have to wait all the way down here?"

    scene tsuneyorevisits31
    with dissolve2

    t "Thank you for coming on such short notice. I understand that you’ve been very busy being useless lately and do not have much time to engage in normal human activities anymore."
    s "I mean...this call has some pretty serious implications and turning it down would have been a terrible idea for a lot of different reasons, but yeah. You’re welcome, I guess."
    s "This happened sooner than I thought it would, though."

    scene tsuneyorevisits32
    with dissolve

    t "I see. So you must already know about my powers."
    s "Your what?"
    t "As it turns out, I am what the Emerald Guardian calls a “soothsayer.” Which means that I can predict the future, and that is somehow soothing."

    stop music fadeout 25.0

    s "Uhh..."

    scene tsuneyorevisits33
    with dissolve

    t "A terrible fate will soon befall you, bro. And while I do not know the specifics of that terrible fate, I know that it exists. "
    t "And I know that it is terrible because you are involved. And that automatically {i}makes{/i} it terrible."
    s "..."
    t "And it must be true as I’ve been seeing this very image in my sleep. Being up here on this metal wheel with you. I see it sometimes when I blink too."
    t "I’ve seen everything here today over and over and over again...and so I took it upon myself to investigate why as it was starting to become distracting in my daily life."
    t "But seeing as I have now informed you of your impending terrible fate in a soothing manner, my mind should go back to normal and I can start thinking more about noodles again."
    t "You are welcome, by the way. I will not charge for my services the first time. But any tragedies I prevent in the future will require a small donation. Thank you for your understanding."
    s "You really think you’re seeing the future?"
    t "It’s the only thing that makes sense."
    s "You don’t think those visions might be memories?"

    scene tsuneyorevisits34
    with dissolve

    t "The Guardian and I toyed with the idea, but ultimately decided this made more sense as we could not come up with a reasonable explanation for why I was ever here in the first place."
    s "You brought me here."

    scene tsuneyorevisits35
    with dissolve

    t "Yes, and I have already thanked you for coming. So it is only right to thank me as well for-"
    s "No, I mean you brought me here {i}in the past.{/i}"
    t "...What?"
    s "This {i}is{/i} a memory. We’ve done this before."

    scene tsuneyorevisits36
    with dissolve

    t "We’ve...what?..."
    t "No...I’m a soothsayer. I’m predicting the future. I’ve summoned you here to protect you from something."
    s "You haven’t."
    t "I have."
    s "You haven’t, Tsuneyo. "
    s "You’re remembering something you’re not supposed to remember. But I don’t know {i}why{/i} you’re remembering it and that...is confusing to me. But we can try and figure that out later."
    t "Why...were we here? The Guardian made it sound like this would be a date."
    s "It kind of was."
    t "But you are not my boyfriend. You’re-"

    scene tsuneyorevisits37
    with dissolve2
    play music "itsingsinitssleep.mp3"

    t "My...husband..."
    s "..."
    t "I asked you to take me here again..."
    s "And it looks like I didn’t even have to. "

    play sound "static.mp3"
    scene tsuneyorevisits38 with flash
    stop sound

    t "Ngh!"
    s "Tsuneyo? Are you okay?"
    t "It’s...my head..."
    t "Something...ngh..."
    t "It hurts!..."
    s "Just take a deep breath and-"

    scene tsuneyorevisits39
    with dissolve

    t "Hah...hah...hah......ngah!"
    s "Just take a deep breath and remember who you are. Not {i}where{/i} you are. "
    t "Do you...know what’s happening to me?..."
    t "Do you...know what this is?..."
    s "A little yes, a little no. And I’m mostly winging it right now, but it’s something we might be able to figure out if-"

    scene tsuneyorevisits40
    with dissolve

    t "Hah...hah...hah!"
    s "It’s something we might be able to figure out if we can talk about it. "
    s "It’s not just you. The world is looping. "
    t "Stop..."
    s "Ayane and Makoto know about it already. And if you can bring yourself to listen- "

    scene tsuneyorevisits41
    with dissolve

    t "Si...lence!..."
    s "I’ll get in contact with them. We can tell you everything. Just try to-"

    stop music
    scene black

    t "Enough! Enough! I’ve heard enough!"
    s "..."
    t "Hah......ngah.......ngh!....."
    t "Tomorrow..."
    t "Bring them...to Tojo Ramen..."
    t "Bring them..."
    t "To me..."

    $ renpy.end_replay()
    $ tsuneyospring2 = True
    $ tsuneyo_love += 1

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7

    hide saturday onlayer date
    show sunday onlayer date

    jump tsuneyospring3

label tsuneyospring3:
    scene clearnightsky
    with dissolve3
    play music "sanctuary.mp3"

    "It’s been just under twenty-four hours since I rode the ferris wheel again."
    "And to think I almost didn’t pick up the phone."
    "It isn’t often that Tsuneyo’s name pops up on the screen, so I assumed she was just dialing my number on accident at first."
    "But, for whatever reason (whether that reason be fate or luck or anything in between), I did. And I must now deal with the consequences."
    "And the reason I say that like it’s a bad thing is because, right now, it {i}is{/i} a bad thing. "
    "How am I supposed to care about the same timeless world that sodomized me and left me catatonic on top of a roof, staring down with widened eyes at a puddle of my semen?"
    "I’m not. That’s ridiculous. {i}All{/i} of this is ridiculous. And now Tsuneyo is getting roped into it again just so she can be purged in another couple months after getting all of our hopes up."
    "It’s just exhausting."
    "But hey, maybe this can finally be the opening I need to shove my dick inside of her next and knock another off the list. "
    "If she’s lucky, maybe {i}she’ll{/i} disappear too and get sent back to a time before she ever met me. That’s how I’ll rationalize this. That’ll make this work for everyone."
    "Or maybe she’ll get even luckier and start from the beginning — trapped inside the confines of that dingy fucking ramen shop, where she will both live and die without ever experiencing life outside the walls."
    "I think we all need something like that."
    "A forceful reminder that each day is just a bridge between then and now- and that the future we all look forward to never actually comes. All we’ll get is one more unfortunate present."

    ay "Sensei-"

    "And all I’ll get is tired."

    scene tsuneyoayaneramen1
    with dissolve2

    ay "Sorry I’m late. I always wind up getting lost whenever I’m over here. "
    s "It’s fine. Where’s Makoto?"
    ay "She...decided not to come."
    s "What?"

    scene tsuneyoayaneramen2
    with dissolve

    ay "Yeah...that’s kind of a thing she’s been doing lately. "
    ay "Any time I want to talk about {i}world{/i} stuff, she just shrugs it off and says she doesn’t want to be bothered. And it’s really starting to get on my nerves since it’s, like..."
    ay "It’s like she’s treating this like a game."
    s "I see."

    scene tsuneyoayaneramen3
    with dissolve

    ay "That’s it? I figured you’d sound a little more disappointed."
    s "It’s not worth it. And, honestly, {i}not{/i} getting involved is probably better for her. It’ll save her the anguish of her expectations being repeatedly brutalized before her very eyes."
    ay "Sensei...come on...we need to work together during times like this. "
    ay "It’s what {i}she{/i} would have wanted."
    s "She?..."
    s "Are we thinking of the same person? Because the person {i}I’m{/i} thinking of {i}absolutely{/i} would not have wanted that. She was rooting for you to disappear the entire time. You {i}know{/i} that."
    ay "I know that she {i}said{/i} that. And, call me an optimist, but I like to think she didn’t actually feel that way. She wanted to solve this more than anyone."
    s "And now that she’s gone you’re going to fill her shoes? Is that what this is?"

    scene tsuneyoayaneramen4
    with dissolve

    ay "Why are you being mean?..."
    s "Because I’m {i}mad,{/i} Ayane. I’m so tired of this already and I’ve only been doing it for a {i}fraction{/i} of the time that she did. I just want it to end."
    ay "If you wanted it to end, you wouldn’t have asked me to come to Tojo Ramen in the middle of the night just so we could talk to Tsuneyo together."

    scene tsuneyoayaneramen5
    with dissolve

    ay "I get that things are hard right now. They’re hard for me too. But it’s both a blessing and a curse that we have what is theoretically {i}forever{/i} to get over that."
    ay "That’s not a luxury we’re supposed to have. And all dwelling on the negatives will do is create a situation where it feels like you’re stuck in quicksand."
    s "That’s not a good analogy. You have to {i}stop{/i} struggling to get out of quicksand. Fighting back against it will just kill you faster."
    ay "Well, the way I see it, {i}you’re{/i} the one who’s fighting back right now. {i}You’re{/i} struggling harder than anyone."
    ay "This is a mental battle, not a physical one. And if you’re spending weeks at a time internally screaming at yourself, {i}you’re{/i} going to get killed. Not me."

    scene tsuneyoayaneramen6
    with dissolve

    ay "So take a deep breath, okay?..."
    ay "Be calm."
    ay "We’ll get through this together. You...me...Makoto...and maybe even Tsuneyo."
    s "I’m just tired of getting my hopes up, Ayane. I’m so tired. I’m hanging on by a thread right now."

    scene tsuneyoayaneramen7
    with dissolve

    ay "Well, you’re in luck. Because I just-so-happen to know how to sew. And there’s no way I’m letting you disappear on me when you’re all I have left now. Got it?"
    s "..."

    scene tsuneyoayaneramen8
    with dissolve

    ay "..."
    s "Can we just run away?"
    ay "Sure. But do you mind if I get something to eat first? I’m kind of craving ramen right now."
    s "Ayane-"
    ay "Everything will be fine."

    scene black
    with dissolve2

    ay "We’re in this together."

    "........."
    "......"
    "..."

    scene tsuneyoayaneramen9
    with dissolve2

    t "Welcome to Tojo Ramen. Please take-"
    ay "Hey, Tsuneyo. Sensei gave me the run-down about your theme park reunion thingy. Is now a good time to...you know...talk about that?"

    play sound "static.mp3"
    scene tsuneyoayaneramen10 with flash
    stop sound

    t "I expected three people. What has become of the class president?"
    ay "Makoto couldn’t get out of work tonight, but you don’t need to worry about her."
    t "I see."
    s "You look...better than you did when we left off last night."
    t "I’ve had time to evaluate the situation and am now raring to go and ready to learn more. But before that, I must apologize for raising my voice at you."
    t "That was very impolite of me, and I am prepared to sever my pinkie-finger as penance for my actions."
    s "Thanks. I’ll take the one on your dominant hand."

    scene tsuneyoayaneramen11
    with dissolve

    t "It will be done."

    play sound "static.mp3"
    scene tsuneyoayaneramen12 with flash
    stop sound

    ay "No, it will {i}not{/i} be done! What’s wrong with you two?!"
    t "If we are going to list our problems, I recommend that we start with him. His flaws are much more glaringly obvious than mine and can likely be rattled off in a matter of minutes."
    s "If I’m going to start, I’d like to admit right out of the gate that I’ve been the end of at least ten pay-it-forward chains this year alone."

    scene tsuneyoayaneramen13
    with dissolve

    ay "Rude! I probably started those."

    play sound "static.mp3"
    scene tsuneyoayaneramen10 with flash
    stop sound

    t "My turn. I personally believe that capital punishment is justified for those who leave a restaurant without finishing a dish. I’ve been told by some that this can be considered a character flaw."
    s "Ayane’s biggest flaw is that she’s too detail-oriented and caring."
    ay "Why did you have to pick out the flaws that make me sound like I’m in a job interview?"
    t "At the risk of the introductory portion of this conversation dragging on any longer, may I ask if you two will be eating or drinking anything tonight? I personally recommend the “everything.”"
    ay "{i}The{/i} everything? Is that some kind of special?"
    t "No, it’s just everything."

    scene tsuneyoayaneramen14
    with fade

    ay "I think I’m okay actually. Ordering anything will just force even more time between you knowing the secrets of the universe and you {i}not{/i} knowing the secrets of the universe. And none of us want that."
    t "I can not wait to sell this information to the highest bidder and use the profits to purchase a larger ramen shop."
    ay "Unfortunately, anyone you try to reveal these secrets to will probably just interrupt you. And, on the off chance they don’t, they’ll think you’re either insane or trying to scam them."
    t "That sounds like an inconvenience. I hereby relinquish my powers as the world’s first backwards soothsayer."
    ay "What’s a {i}backwards{/i} soothsayer?"
    s "Someone who can see the past."
    t "My hero name is “Memory Girl.” "

    scene tsuneyoayaneramen15
    with dissolve

    ay "Okay, well...considering this is the one scenario where having memories kind of {i}is{/i} a superpower, I’ll let you keep your hero name. "
    ay "But only {i}after{/i} listening to your “hero orientation” so your powers don’t, like...spiral out of control or something."
    ay "So...buckle yourself in, Memory Girl. You’re in for a pretty intense info-dump."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Thirty minutes later...{/i}"

    scene tsuneyoayaneramen16
    with dissolve2

    t "I see."
    ay "Do you? Because you were really silent through that entire speech and I kind of figured you’d have, like...any amount of questions about the fact that we’re in an infinitely repeating school year."
    s "In her defense, she’s heard this all before at that sleepover we had."
    ay "Yes, but she doesn’t have any {i}memories{/i} of that sleepover, so that shouldn’t be relevant."
    t "I am Memory Girl. I have memories of everything."
    t "I remember that sleepover well. I was just unaware that it was actually a {i}memory{/i} until I learned that these “visions” were not simply visions at all."
    t "And I have to say I am thankful for this as I was beginning to worry that I was just having very strange and specific fantasies."
    ay "Do you remember how that sleepover ended, though? Because I’m pretty sure that’s when one of the resets started. "

    scene tsuneyoayaneramen17
    with dissolve

    t "How it ended?..."
    t "I’m not quite sure. The memories don’t appear in order. They come and go, like the Produce Delivery Administration on Tuesday, Thursday, and Sunday."
    s "Tsuneyo left halfway through, didn’t she?"
    ay "{i}Did she?{/i}"
    s "Yeah...I remember her getting a phone call and then disappearing."
    t "A phone call..."
    s "Do you remember anything like that, Tsuneyo? Not that it would definitely be relevant, but it might help us establish some sort of timeline."

    scene tsuneyoayaneramen18
    with dissolve

    t "I apologize, but I’m unable to recall anything at this moment in time. I will remain vigilant in hopes that a new memory will approach, though."
    t "Nothing from the past can escape the mind of Memory Girl."
    ay "Do you remember who else was {i}at{/i} the sleepover, Tsuneyo? Not counting anyone shorter than me because that’s a subject Sensei isn’t ready to approach yet."
    s "Subtle."

    scene tsuneyoayaneramen19
    with dissolve

    t "Yamo."
    ay "Yamo?"
    s "She means Yumi."
    t "I’m pretty sure it’s Yamo."
    ay "No, it’s definitely Yumi. Because Yumi was there. She doesn’t have any recollection of it like you do, though. So I wonder what it is that makes you different?"
    t "There is only one explanation — gluten."
    t "This is why they have been removing it from so many things. No one understood its powers until now. How could we have been so blind?"
    s "We’ve finally figured it out, Ayane. You were right. All we needed to do was work together."
    ay "You don’t think the old district has something to do with it, does it?"

    scene tsuneyoayaneramen20
    with dissolve

    s "What would the old district have to do with it?"
    ay "I’m trying to think of things the two of them have in common. And both of them are from the old district, aren’t they?"
    s "Yeah...but so is Chika, and she hasn’t been involved in any of this yet. Which is great, because if I have to try explaining this to her little sister, I’m going to shoot myself with one of your guns."
    ay "Yeah, that’s a good point. I wasn’t thinking of anyone else yet, just what Yumi and Tsuneyo share. But I think I’m at a dead end because the only other thing I can think of is D-Cups."

    scene tsuneyoayaneramen21
    with dissolve

    t "Who gave you permission to violate me in my own restaurant?"
    ay "Can you think of anything else, Tsuneyo? I’m just trying to figure out what we’re supposed to do next. "
    ay "Because my instinct is saying to go back to Yumi, but I also don’t want to just go around in circles and wind up right back at the beginning the next time there's an apocalypse."
    t "It all comes back to gluten. "
    s "Tsuneyo, I really don’t think it’s gluten."
    t "It has to be. I watched her eat my noodles with her very mouth. There is no other explanation."
    ay "What do you think, Sensei? Should we try talking to Yumi again?"
    s "I don’t know, Ayane. I saw Yumi the other night and-"
    s "Actually, wait..."
    s "Tsuneyo, didn’t you talk to Yumi about this already?"

    scene tsuneyoayaneramen22
    with dissolve

    t "What?"
    s "When I last saw Yumi, she said she came here to eat dinner and that you started asking her a bunch of questions."
    t "I ask many people many questions. It is part of my job as the Memory Ramen Girl."
    s "No, like {i}weird{/i} questions. Specifically about...dates and sleepovers and things like that. She compared you to me- and said you weren’t acting like yourself."
    t "She does not know me very well, nor do I know her. The probability of her understanding what is or isn’t normal for me seems unlikely. Perhaps she is mistaken?"

    scene tsuneyoayaneramen23
    with dissolve

    ay "Yumi was comparing her to {i}you?{/i} That’s weird."
    s "Specifically me when I’ve “lost it.” Yumi’s around for that a lot. She’s always snapping me out of memory-lapses and blackouts and whatnot."
    ay "How...often does that happen to you, exactly?"
    s "A lot, but...come to think of it, you’re rarely even around when that happens, are you?"
    ay "I’m there for when you’re broken during resets, but-"
    t "Attention, diners. I have an announcement to make."

    scene tsuneyoayaneramen24
    with dissolve

    ay "What’s up, Tsuneyo?"

    stop music
    play sound "broken.mp3"
    scene tsuneyoayaneramen25 with flash
    scene tsuneyoayaneramen26 with flash
    scene tsuneyoayaneramen27 with flash
    scene tsuneyoayaneramen25 with flash
    scene tsuneyoayaneramen26 with flash
    scene tsuneyoayaneramen27 with flash
    scene tsuneyoayaneramen28 with flash
    scene tsuneyoayaneramen29 with flash
    scene tsuneyoayaneramen30 with flash
    scene tsuneyoayaneramen28 with flash
    scene tsuneyoayaneramen29 with flash
    scene tsuneyoayaneramen30 with flash
    scene tsuneyoayaneramen31 with flash
    scene tsuneyoayaneramen32 with flash
    scene tsuneyoayaneramen33 with flash
    scene tsuneyoayaneramen31 with flash
    scene tsuneyoayaneramen32 with flash
    scene tsuneyoayaneramen33 with flash
    scene tsuneyoayaneramen34 with flash
    scene tsuneyoayaneramen35 with flash
    scene tsuneyoayaneramen36 with flash
    scene tsuneyoayaneramen34 with flash
    scene tsuneyoayaneramen35 with flash
    scene tsuneyoayaneramen36 with flash
    scene tsuneyoayaneramen37 with flash
    scene tsuneyoayaneramen38 with flash
    scene tsuneyoayaneramen39 with flash
    scene tsuneyoayaneramen37 with flash
    scene tsuneyoayaneramen38 with flash
    scene tsuneyoayaneramen39 with flash
    scene tsuneyoayaneramen40 with flash
    stop sound
    "why is it always behind you"

    play sound "imscared.mp3"
    scene black

    ay "{size=+20}{b}AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHH!{/b}{/size}"

    play sound "static.mp3"
    scene 1 with flash
    scene 3 with flash
    scene 5 with flash
    scene 1 with flash
    scene 1 with flash
    scene 3 with flash
    scene 5 with flash
    scene 1 with flash
    scene tsuneyoayaneramen41 with flash
    stop sound
    play music "holyplace.mp3"

    ay "Ngh!"
    s "It’s okay...It’s just a blackout."
    s "Those happen here sometimes."

    scene tsuneyoayaneramen42
    with dissolve2

    ay "A blackout?..."
    ay "But...that noise..."
    s "Yeah. It’s loud. "

    scene tsuneyoayaneramen43
    with dissolve

    s "But on the bright side, at least Tsuneyo-"
    ay "..."
    s "..."
    ay "Tsuneyo...isn’t here..."

    scene tsuneyoayaneramen44
    with dissolve2

    ay "Tsuneyo isn’t here! This is weird, right?! She was there a second ago and now she’s gone!"
    s "I...I’m not really..."
    ay "Is it happening again right now?! Is it already time for the next reset?! How are we still together?! What’s going on?!"
    s "Ayane...it’s okay. She probably just stepped outside without us noticing.  Tsuneyo’s weird. And this is a weird place."

    "s0mething is wr0ng"

    scene tsuneyoayaneramen45
    with dissolve2

    s "Why don’t we go out there and check?"

    "I c4nt c0ntr01 1T"

    ay "Sensei?..."

    "TH15 15NT M3"

    s "Come on...I’m sure she’s fine."
    ay "What’s going on with you?..."
    s "Nothing."
    s "Now, quit being such a scaredy cat."

    scene tsuneyoayaneramen46
    with dissolve2

    ay "Sensei, wait! Don’t leave without me!"

    stop music
    scene black

    "hey."
    "i think we should stop coming here."

    play sound "static.mp3"
    scene tsuneyoayaneramen47 with flash
    stop sound
    play music "newweather.mp3"

    t "He who disbelieves after his having believed, not he who is compelled while his heart is at rest on account of faith, but he who opens his breast to disbelief-"
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    t "Kill the apostates. Seize them and kill them wherever you find them. "
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    t "Kill the apostates. Seize them and kill them wherever you find them."
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    t "Kill the apostates. Seize them and kill them wherever you find them."
    ay "Sensei..."
    s "Yeah?..."
    ay "This has never happened before...has it?..."
    s "..."
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    ay "..."
    s "No."
    t "Kill the apostates. Seize them and kill them wherever you find them."
    s "This has never happened before."

    scene tsuneyoayaneramen48 with dissolve4
    $ renpy.pause(30, hard=True)
    scene tsuneyoayaneramen47 with dissolve4

    t "Kill the apostates. Seize them and kill them wherever you find them."
    ay "We should probably bring her back inside now, shouldn’t we?..."
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    s "Yeah..."

    scene black
    with dissolve2

    s "We should bring her back inside."

    "........."
    "......"
    "..."

    scene tsuneyoayaneramen49
    with dissolve2

    ay "{size=-2}Tsuneyo, I know you probably can’t hear me on account of how nothing that happens ever makes sense anymore, but it’s probably not the best idea to wander around naked in a neighborhood full of homeless people.{/size}"
    t "There are clues in a house near a lake. It started before you were born."

    scene tsuneyoayaneramen50
    with dissolve

    ay "A house near a-"
    ay "Sensei, Tsuneyo’s pupils are, like...completely gone."
    t "Infinite...spring..."
    t "Infinite...world..."
    s "..."
    t "On these is the wrath of God, and they shall have a grievous chastisement."
    ay "Can you help me, please? I can’t move her on my own."

    scene black
    with dissolve2

    s "Yeah."

    "Ayane and I escort a naked, murderous and pupil-less Tsuneyo back inside of a blacked out ramen shop."
    "But the craziest part is that isn’t even the weirdest thing that happens to me tonight."
    "On the way home, I piss myself."
    "Guess it looks like I’m pee boy after all =/"

    $ renpy.end_replay()
    $ ayane_love += 4
    $ tsuneyo_love += 17
    $ sana_love += 1
    $ tsuneyospring3 = True

    "{i}Ayane’s affection has increased by 4!{/i}"
    "{i}Tsuneyo’s affection has increased by 17!{/i}"
    "{i}Sana’s affection has increased by 1!{/i}"

    "What? Why? She wasn’t even here."
    "{i}She masturbated to you again while all that shit was going down. I figured I’d let you know afterward so it didn’t interrupt the event.{/i}"
    "Oh, thanks."
    "{i}No problem.{/i}"
    "{i}Seriously, though. Let’s not go to the old district anymore. Just let Memory Girl’s brain get wiped again.{/i}"
    "I think I’m going insane."
    "{i}You’re not.{/i}"
    "Nevermind."

    $ sana_love += 1

    "{i}Sana’s affection has increased by 1!{/i}"

    "Nice."
    "{i}That girl needs a new hobby.{/i}"
    "You need a new host."
    "{i}You need to sleep.{/i}"

    scene bedroom_night
    stop music

    "You’re right."

    scene black
    play sound "tackle.mp3"

    "Goodnight, moon."
    "........."
    "......"
    "..."

    $ maya_love +=1

    "{i}[[REDACTED]’s affection has increased by 1!{/i}"

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

label halloweentsuneyo1:
    play sound "static.mp3"
    scene tsuneyocut1 with flash
    stop sound
    play music "samhain.mp3"

    t "I will be fine on my own from this point on. Thank you, Master Geoffrey."

    play sound "dooropen.mp3"

    scene tsuneyocut2
    with dissolve

    "Tsuneyo closes her eyes. They were open just a second ago. She sinks her blade into a carrot. It was whole just a second ago. You enter the room. You were nowhere just a second ago."

    scene tsuneyocut1
    with dissolve

    "Her eyes open once more. You need to do that when you have a knife in your hand. But she wouldn’t have a knife in her hand for much longer because it was time to go on a trip."
    "Past the world of worldliness (where our world normally is) and into a plane of unworldliness, categorized by its humidity and 29-hour time cycle."
    "Far beyond the infinity house, something was happening. The cats had come out to play. It was time for {b}ELATION PROTOCOL.{/b} "
    "But what is that, you ask?"
    "It is."

    scene tsuneyocut2 with dissolve
    scene tsuneyocut1 with dissolve

    "She blinks. A necessary human function."

    t "I wonder if I will have any time left once I have finished cooking to enjoy the festivities with my many acquaintances and one friend."
    t "But I must diligently finish the task at hand — for the greatest chefs know when and when not to provide their mind with a lane to wander through."
    t "Right now, I am focused. I am a warrior of the culinary arts. I am Tsuneyo Tojo — future sole proprietor of Tojo Ramen."

    "Or current! "
    "The smell had gotten worse//but the power issues finally managed to resolve themselves. Probably. At least I haven’t seen any in quite some time. "
    "But I’m just like you. I’ve never seen what lies beyond that door. I’ve only dreamt of it. And there is not much to do but let those dreams consume me until my curiosity finally reaches its climax."

    stop music
    play sound "broken.mp3"
    scene tsuneyocut3
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut4
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut5
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut3
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut4
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut5
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut4
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut5
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut3
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut4
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut5
    $ renpy.pause(0.1, hard=True)
    scene tsuneyocut6
    stop sound
    $ renpy.pause(4, hard=True)

    t "Well, that was strange."

    play sound "seek.mp3"
    scene tsuneyocut7
    $ renpy.pause(1, hard=True)
    play sound "static.mp3"
    scene tsuneyocut8 with flash
    stop sound

    t "Is someone there? I was informed that I’d be able to work in peace. "
    t "This area is off limits to those who-"
    q "Sticks and stones may break my bones; I wish that they would hurt me."

    play sound "static.mp3"
    scene tsuneyocut9 with flash
    stop sound

    t "Huh?!"
    q "He strokes my hair when we’re alone but he doesn’t deserve me-"

    scene tsuneyocut10
    with dissolve

    t "Where are-"
    q "HIS HANDS SO LARGE THEY SWALLOW MINE, I SWALLOW TOO JUST WATCH. HE TOUCHES ME, HE TOUCHES THEM, HE MAKES US CLEAN HIS CROTCH."
    q "A POEM, A POEM, A PARASITE. I HEAR THE VOICE OF GOD. SIX MILLION WHISPERS DEEPER AND I’M STILL THE PEBBLE’S CLOD."

    scene tsuneyocut11
    with dissolve

    q "{b}BELIEVING ISN’T SEEING SINCE BELIEVING ISN’T REAL. AND SEEING’S NOT BELIEVING ‘TIL YOU’VE SEEN YOURSELF IN HEELS.{/b}"
    q "{b}NO MATTER HOW YOU CUT IT AND NO MATTER HOW IT BLEEDS, YOU WILL ALWAYS BE THE NOODLE GIRL.{/b}"

    scene black

    q "{b}{size=+20}BECAUSE THAT’S WHAT WE AGREED.{/b}"

    "Tsuneyo Tojo falls into a pot of boiling water. She turns into a crayfish."
    "And we just sit and watch because we ordered her for dinner."

    scene tsuneyocut12
    play sound "yougoon.mp3"
    $ renpy.pause(7.5, hard=True)
    scene black
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene tsuneyocut13 with flash
    stop sound
    play sound "dosex.mp3"
    $ renpy.pause(5, hard=True)

    "Sticks and stones may break my bones//it’s time for your first h-scene"

    play sound "static.mp3"
    scene tsuneyocut14 with flash
    stop sound
    play music "irishblood.mp3"

    s "Yeah. Yeah. Get pregnant. Get pregnant. Take that dick. Get pregnant. Fuck. Get pregnant. Yeah. Get pregnant. Get pregnant. Get pregnant. Get pregnant. "

    "A beautiful scene, is it not? To see the things that you forgot. But halt before His crime’s alleged! The sharpening of Gallow’s Edge. The fear that pushed you from that ledge-"
    "Did naught but strengthen a part of you that has always existed, just not in a form that’s easy to appreciate when taken out of context."
    "You know it to be true, don’t you? You knew the truth and spoke it too! Yet no one understood or listened then. Would the same steps be followed now? Would you let those stares {i}become{/i} stairs?"

    play sound "static.mp3"
    scene tsuneyocut15 with flash
    stop sound

    se "Or are you content with just playing with yourself in the dark at night because your thoughts don’t always make you {b}happy?{/b}"
    t "..."
    se "Oh, come on. There’s no need to be so quiet. You’re safe here. And I can guarantee you that {i}whatever{/i} it is you’re thinking isn’t even half as “bad” as the things I’ve done."
    t "..."
    se "He’s beautiful, isn’t he? Aki-kun."

    scene tsuneyocut16
    with dissolve

    se "You know, {i}I{/i} was the first person to ever suck that little wiener of his. Some might even say I taught him everything he knows. "
    se "I guess it’s not very little anymore though, is it? {i}Now,{/i} he’s-"
    t "Who are you?"

    scene tsuneyocut17
    with dissolve

    se "Oh! Sorry. Where are my manners? My name is Sekai. I believe you know my daughter, Ami!"
    se "Tell me — what’s she like in school? I have a hard time ghosting myself into that place and I want to make sure she’s well-behaved."
    t "She’s...fine."

    scene tsuneyocut18
    with dissolve

    se "Great! Thanks for letting me know."
    t "Wha- "
    t "What are you doing?"
    se "Hey, aren’t these kind of huge for your age? Are you {i}sure{/i} you’re who you say you are? You’re positive you didn’t just lose track of time cooped up in that ramen shop?"
    t "You can’t just...touch-"

    scene tsuneyocut19
    with dissolve

    se "Tsuneyo, right?"
    se "Listen, I don’t think you understand what’s going on right now, so I’m going to put this in the most gentle, easy-to-understand way possible."

    scene tsuneyocut20
    with dissolve

    se "I’m going to help you have your first ever orgasm!"
    t "Wh...what?!"
    se "And there’s nothing you can do about it since you’ve fallen into my golden noodle trap!"

    play sound "static.mp3"
    scene tsuneyocut21 with flash
    stop sound
    play sound "winner.mp3"

    t "Ngh! I can’t-"
    se "Yeah, moving’s not going to work. But you can trust me! I know what I’m doing. And soon, you won’t even {i}want{/i} to move! That’s just how good I am."
    t "Why are you doing this?! Where am I?! I demand you-"

    play sound "static.mp3"
    scene tsuneyocut22 with flash
    stop sound

    se "D’awwww, look at you making demands. Tell you what! You manage to break free from the golden noodle trap, and I’ll send you right back to that kitchen! You’re the strong one, right? I say you go for it!"
    t "Ngh...mngh! My arms-"
    se "Weird, right? They’re not restrained at all, yet you can’t seem to remember how to use them. Do you want to know why?"
    t "I want to know...why you’re doing this! I have...never even seen you before!"
    se "Duh. I’m dead. You’d be, like, totally crazy if you {i}were{/i} seeing me around. As for {i}why{/i} I’m doing this, though..."
    se "Would you believe me if I said it was for your own good?"
    t "I can’t...believe anything right now..."
    t "None of this...seems real...I just...wanted to cook..."
    se "Yeaaaah, that’s kind of the problem. That’s all you {i}ever{/i} want to do. And being so far into the game already without any sex in sight, it’s time for {i}me{/i} to step in and put you on the right path!"

    play sound "static.mp3"
    scene tsuneyocut23 with flash
    stop sound

    se "You’ve been thinking about it, haven’t you? Your curiosity has taken root! Your dreams are full of Aki-kun’s cock! Yet you’re further away from him than ever before! "
    se "Is it because you’re scared? Nervous? Because there’s really no need to be. Just look at your friend over there! Sex is so easy that she can do it in her sleep!"
    t "But the Emerald Guardian...claims that...nothing happened that night! "
    se "And {i}I{/i} claim to a be a law-abiding citizen who {i}only{/i} likes older boys."
    t "It does not matter what you claim! This is...clearly fictional! I wish for this nightmare to end...now!"
    se "I know for a fact that’s not true, Tsuneyo. "
    t "How do-"
    se "I know because {i}you’re{/i} the one who created this world."

    play sound "static.mp3"
    scene tsuneyocut24 with flash
    stop sound

    t "...What?"
    se "If you dream a dream within a dream, it’s hard to tell what’s true. And if you dream a dream in one of those, who {i}knows{/i} what you can do?"
    t "I...don’t understand..."

    play sound "static.mp3"
    scene tsuneyocut25 with flash
    stop sound

    se "You’re a good girl who wants to do bad things. And I’m a bad girl who wants to do good things. Together, we can make one whole person."
    se "Think of me like a wet dream — the climax you’ve been hunting, yet haven’t managed to find. "
    se "This is a real honor, you know. I normally just hang out in the background. But I’ve been swimming through the sea of consciousness for long enough to know that you kinda {i}need{/i} to do this or..."
    se "Well, I’m not really sure what will happen. "

    scene tsuneyocut26
    with dissolve

    se "But I can tell you it won’t be good!"

    scene tsuneyocut27
    with dissolve

    se "You probably wish it was you instead, don’t you? How unfair it must be to have your best friend getting dicked down while {i}you{/i} struggle to figure out how to even take care of yourself!"

    play sound "static.mp3"
    scene tsuneyocut28 with flash
    stop sound

    se "You aren’t being haunted by me — you’re being haunted by the past. Just like Aki-kun was until I gave him a much needed wakeup call."
    se "I can make it all go away. His scent on her clothes. Those visions of that man planting a tree. Those visions of your {i}father{/i} because you’re fascinated by dicks but haven’t been exposed to many yet."
    se "How’s he doing, by the way? Probably bad, right?"
    t "You...know my father?"
    se "Oh, yeah. I was a regular at that place back when I was younger. I would’ve whored myself out for that tori shio ramen if it wasn’t already so damn cheap."
    t "You..."
    t "I...think I’m...remembering something..."

    scene tsuneyocut29
    with dissolve

    se "Well, stop."
    se "We have better things to do."

    scene black
    stop music

    se "I died before I ever got to pay my tab."

    "........."
    "......"
    "..."

    play music "happytheme3.mp3"
    scene tsuneyocut30
    with dissolve4

    "The snow was cold because it was snow."

    se "Hear ye, hear ye! "

    play sound "static.mp3"
    scene tsuneyocut31 with flash
    stop sound

    se "On this hallowed eve of remembrance, I am joined by Tsuneyo Tojo — daughter of Tojo Ramen’s sole proprietor and the girl who will one day hang herself with his mantle!"
    t "Please...do not do this. Your “tab” is forgiven. {i}I’m not ready.{/i}"

    scene tsuneyocut32
    with dissolve

    se "You want to back out {i}now?!{/i} After I went through the effort of dressing like your husband?! Tsuneyo, how could you?!"
    t "I was never on board for such contact in the first place! I already told you, I just wanted to cook! "
    se "But I worked so hard on all of those knots!"

    scene tsuneyocut33
    with dissolve

    t "I don’t even remember you tying-"

    scene tsuneyocut34
    with dissolve

    t "Hngh!"
    se "Okay, great. Nice and secure. I got rid of the golden noodle trap since I’ll be on my knees in a second and didn’t want to risk falling into it again."

    scene tsuneyocut35
    with dissolve

    se "How’s it feel when I tug on this part? Good? It’s been a while since I’ve been tied up. I can’t really remember."
    t "N...No..."
    se "No? How about if I tug it harder?"

    scene tsuneyocut36
    with hpunch

    t "Mmmngh!"
    se "Ah! There’s no denying that one, Tsuneyo. You’re totally getting turned on right now. This is probably the first time you’ve ever felt powerless, huh?"

    scene tsuneyocut37
    with dissolve

    t "I beg you...please stop this...I can’t handle it..."
    se "That’s cause you’re a naughty, slutty little slut! The prude kind! The {i}worst{/i} kind! Just give in already and start fucking Aki-kun like everybody else. It’s what you’re supposed to do."
    t "What do you mean I’m...{i}supposed{/i} to? "
    t "My job is...providing food and...a place to rest for those who feel hungry and lost..."
    t "That is all I’ve...ever been..."
    se "You poor thing. "
    se "You don’t even know what you are, do you?"
    t "I am...a warrior..."

    scene tsuneyocut38
    with dissolve
    with hpunch

    t "NNNGHGH!"
    se "What kind of “warrior” makes a noise like that?"
    se "You’re a toy just like the rest. Just because you came in a nicer box doesn’t mean it’s right to expect you won’t ever be taken out of it."
    se "My little boy likes to play with his toys. But every once in a while, Tsuneyo-"

    play sound "static.mp3"
    scene tsuneyocut39 with flash
    stop sound

    se "{i}I like to play with them too.{/i}"
    t "{i}Please...I’ll do anything you want...{/i}"
    se "{i}Anything?{/i}"
    t "Yes...Just name it...I don’t want...my first time...to be like {i}this...{/i}"
    se "You’d really do {i}anything{/i} to not be touched by a cute older girl? Nobody’s {i}that{/i} straight. Give me a break."
    t "I mean it...anything..."
    se "Tempting."

    scene tsuneyocut40
    with dissolve
    with hpunch

    t "NNGGH! STOP!"
    se "If only there was something I wanted."

    scene tsuneyocut41
    with dissolve

    t "W-Wait! Where are you-"

    play sound "static.mp3"
    scene tsuneyocut42 with flash
    stop sound

    t "HaaAAaaaAAAaAAAah! "
    se "I {i}knew{/i} it. My fingers slipped right inside. All of that “No! Stop!” was just a big bluff, huh?"
    t "Nghh! Mmmngh!"
    se "Mmm...that feels good, doesn’t it? Someone {i}else’s{/i} fingers will always trump your own. Keep that in mind the next time you can’t get yourself to cum."
    t "Hngh! Hngh! S...Stop!"
    se "Now just imagine it was your teacher’s {i}big{/i} cock instead..."
    t "Haah..."

    scene tsuneyocut43
    with dissolve

    se "Imagine you two are alone in the classroom after school...and you need his help understanding a poem about love or something silly like that..."
    se "You two sit by the window...and the sun hits you in a way that causes your shadows to touch. So you think to yourself, “what if we actually did?”"
    se "Your hand reaches out...so does his..."
    se "Two minutes later, your fingers are entwined..."
    se "Two minutes after that, your tongues..."
    se "He reaches under the desk and slides his hand up your skirt...gently scraping your inner thighs with his nails before he traces circles around the swollen clit you hide behind your black panties..."

    scene tsuneyocut44
    with dissolve

    se "It’s not enough anymore...You reach down and slide them off to give him better access...and he wastes no time at all before submerging himself in your gorgeous, virgin pussy..."
    t "Too fast...too fast! "
    se "You want to cum right then and there, but you don’t want him to think you’re weak! So you hold off and you hold off and it’s getting harder and harder and you {i}are{/i} weak, but you can’t!"
    se "You’ve gotta hold it in! You want to cum together! So you gaze into his eyes with tears welling up in yours and whisper “take me...”"

    play sound "static.mp3"
    scene tsuneyocut45 with flash
    stop sound

    se "So he does! He props you up onto your desk and you wrap your legs around him, clumsily fumbling to get his belt off as your hands shake like jackhammers!"
    t "Ngh...mmngh!..."
    se "Once you finally get it off and he slides his boxers down, he presses it up against you...coating himself in your juices as you struggle to comprehend just how your tiny hole will accept him."
    se "Regardless, you want it!"
    se "You want it so bad! So you move your hips and guide him into you! And you’re so wet that, despite its size, it slips in with no trouble it all. And it hurts, yes. But more than that, it feels {i}so good.{/i}"
    t "Mmngh....mmmmf!!!! "
    se "You can feel it throbbing inside you...you’re entranced by the grooves and contours as you come to know just how {i}beautiful{/i} he is...But still, you can’t cum yet...you have to wait for him..."

    scene tsuneyocut46
    with dissolve2

    se "You tear your gaze away from him and focus on the window as a last ditch effort to keep yourself from exploding all over his monster cock..."

    play sound "static.mp3"
    scene tsuneyocut47 with flash
    stop sound

    se "But outside, you see a man planting a tree. And {i}he{/i} is handsome too."
    t "No..."
    se "So you picture both of them fucking you..."
    t "No!"
    se "They tear off your clothes and drag you into an empty clubroom! They force you onto the ground before the man who was planting a tree just moments ago shoves his sweaty cock into your mouth!"
    se "Meanwhile, Aki-kun grips your ass with so much force that you can feel your blood vessels burst. But the pain only lasts for a second as he overwrites it once more by fucking your newly christened hole!"
    se "You’ve finally met God! You’ve finally felt pleasure so {i}complete-{/i} so {i}pure{/i} that you think yourself a fool for ever doubting him! And that’s all fine and good until the voices set in!"

    play sound "static.mp3"
    scene maggotgod1 with flash
    scene hydrangeafield with flash
    scene maggotgod2 with flash
    scene hydrangeafield with flash
    scene maggotgod1 with flash
    scene hydrangeafield with flash
    scene maggotgod2 with flash
    scene hydrangeafield with flash
    scene tsuneyocut48 with flash
    stop sound

    se "From that point on, it’s chaos! It’s hell! You lose track of where you are and who you are and {i}when{/i} you are because the pleasure becomes so great that’s it all you know! You hear them! Distant gods!"
    se "False gods! True gods! Peerless and pearless gods, the kind that bear no fruit! For every god’s a liar, it’s a fact you can’t refute!"
    t "I can’t...hold on...much longer!"
    se "He’s finally about to cum! They both are! You can feel yourself overflowing as tears stream down your face like blood from the neck of a freshly butchered cow! Your hips move on their own! "
    t "I can’t! I can’t! I can’t! Stop!"

    stop music
    scene tsuneyocut49
    play music "dosex.mp3"

    "But when you open your eyes, you find yourself the way you’ve always been."
    "Alone — watching others fall in love while you pretend not to care."
    "You do, though."
    "The truth is that you’ve always wanted to fall."
    "You’re just deathly afraid of heights."

    s "Yeah. Yeah. Get pregnant. Get pregnant. Take that dick. Get pregnant. Fuck. Get pregnant. Yeah. Get pregnant. Get pregnant. Get pregnant. Get pregnant. "
    t "..."
    mo "Mnh...mmm..."
    mo "{i}Sir?...{/i}"
    t "It should have been me."

    stop music
    play sound "static.mp3"
    scene tsuneyocut50 with flash
    stop sound
    play sound "stab.mp3"
    with hpunch

    t "Ngh?!?"

    scene tsuneyocut51
    with dissolve3

    t "Huh?..."

    play sound "static.mp3"
    scene tsuneyocut52 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    scene black
    with dissolve4
    $ renpy.pause(2, hard=True)

    t "I..."
    t "I should probably...find a bandage..."

    $ renpy.end_replay()
    $ halloweentsuneyo1 = True
    $ tsuneyo_lust += 1

    "{i}Tsuneyo’s lust has increased to [tsuneyo_lust]!{/i}"
    "{i}You’re welcome ;D{/i}"

    jump halloweenfive5

label tsuneyospring4:
    scene spiter
    $ renpy.pause(2, hard=True)
    play sound "spiiideeer.wav"
    $ renpy.pause(15, hard=True)
    scene black
    "The termite queen has tasked us with chewing through your deathbed."
    "We’ll please her, lick her body clean, ensure we keep our young fed."
    "To starve and die a lonely death with dirt around us always,"
    "It feels a bit like heaven here. Or maybe just a hallway."

    scene colorbars
    play sound "colortone.mp3"

    "there is nothing more liminal than this"

    scene tsuneyidergzyafd1
    play music "kashiwagi.mp3"
    stop sound

    "Tsuneyo Tojo glanced down at a tomato, recalling a story she once heard about how humans thought they were poisonous for a long fucking time until some wack job ate one and realized they weren’t."
    "Now, people eat tomatoes all the time. She wasn’t particularly a fan, though."
    "Yes, they could be incorporated into several specific types of ramen, but she had yet to create or a discover a recipe in which they did not overpower everything else."
    "Today, she would try again. For there was no one here at all. No one here at all. It was just her and a tomato. It was her and a tomato and a knife. It was red. Like her nails. Like the hair of the ghost who raped her."

    scene tsuneyidergzyafd2
    with dissolve

    "Surely that was just a dream, though. And while it may have felt real, it defied all logic and happened between her and a dead woman. "
    "It felt strange to her — wanting to experience that again. But it {i}did{/i} feel new. And it made her want to try new things. Hence the tomato. "
    "But Tsuneyo Tojo could not fuck a tomato, no. Not before marriage. And Tomato Tojo didn’t sound good. Nor did Tsuneyo Tomato. Actually, that one wasn’t that bad. But still, no."

    t "This is beginning to become a burden. Perhaps I should speak to a doctor?"
    tom "I am a doctor."
    t "And now the tomato is speaking to me. How predictably unpredictable."
    tom "What seems to be the problem, Ramen Girl?"

    scene tsuneyidergzyafd3
    with dissolve

    t "Well, Mr. Mato, I’ve been experiencing strange hallucinations lately. Every day. And I’m hearing things too. Sometimes, both at once."
    tom "But how does that make you {i}feel?{/i}"

    scene tsuneyidergzyafd4
    with dissolve

    t "I don’t feel much at all. But I believe it makes me crazy. And I worry about what will happen if I mention it to anyone else as I am already an exhibitionist. I do not wish to further burden those I care about."
    tom "Do you {i}enjoy{/i} being an exhibitionist?"
    t "Not particularly. Nor do I think I am very good at it as it only happened once and was entirely unintentional."
    tom "Have you figured out why such a thing has happened yet?"

    scene tsuneyidergzyafd1
    with dissolve

    t "No...I have not. But I have an idea."
    tom "Why don’t you tell me all about it? No one else is here. You can pretend I’m any old customer."
    t "This is meant to be a place for {i}others{/i} to voice their worries to {i}me.{/i} I will tarnish the sanctity of Tojo Ramen if I attempt to do the same."
    tom "Maintaining the “sanctity” of this place is important to you then?"
    t "It is my only duty. I would leave everyone and everything else behind for it if I needed to."
    tom "Sounds pretty serious. Have you tried getting fucked?"
    t "That seems rather inappropriate for a tomato to say to a human. Let alone a doctor tomato."
    tom "I just think you’d feel a lot better if you got fucked."

    scene tsuneyidergzyafd5
    with dissolve

    t "Mm..."
    tom "Just do it. You know for a fact that guy you’re interested in would help you out. And he’s already doing it with your friends."
    tom "Why are you so scared, Ramen Girl? Just be more like them. That’s what they want. That’s what you want. And it would {i}feel{/i} good too."
    t "I will not be tempted by a tomato. No matter how logical and blunt that tomato is."
    tom "It felt good, right? That dead lady’s fingers inside of you."
    t "Life is full of things that {i}feel{/i} good. But feeling good alone doesn’t mean something is good {i}for{/i} you."

    play sound "dooropen.mp3"

    tom "You mean like eating ramen?"

    scene tsuneyidergzyafd6
    with dissolve

    t "That’s it. Prepare to die."
    k "Mean-spirited tree girl! I have entered your working establishment."

    play sound "static.mp3"
    scene tsuneyidergzyafd7 with flash
    stop sound

    k "二人で。"
    t "Ah. Forgive me for not immediately noticing. Welcome to Tojo Ramen. You may seat yourselves. Please take a look at the menu and let me know if you have any questions."
    na "!!!!!!"
    t "Understood. You’ve brought your own drawing equipment today and will not require mine. This saves me approximately 50 yen. I am eternally grateful."

    scene tsuneyidergzyafd8
    with dissolve

    k "Nao-chan has informed me that she visited this place with Friendburger Friendman and that you were very kind to her. I did not believe it."
    k "But I rejected this disbelief and decided that floppy wet breadstrips would give her a mouthsmile. Please do not turn her reverse-frown upside right."
    na "!!!!!"
    t "Here at Tojo Ramen, we serve only the most mid-tier ingredients. Anything higher taints the authenticity of ramen. I can assure you that you will leave as satisfied as always."

    scene tsuneyidergzyafd9
    with dissolve

    k "Are you the only human who does the workjob in this house of soup?"
    t "That is correct. And again, we are not looking for assistance. But I thank you for your interest regardless."

    scene black
    with dissolve

    t "Now please, sit. I will not be able to live with myself if my customers are uncomfortable."
    k "Come, Nao-chan! Your book of colors will be more colorable upon this lengthy wooden noodlebed!"
    na "!!!!!!!!"

    scene tsuneyidergzyafd10
    with dissolve2

    t "May I interest either of you two in a tomato free of charge?"
    tom "Don’t you dare."
    k "What is “tomato?”"
    na ".........."
    k "Oh. You mean a savory nonapple. In what manner will its preparations be made?"
    t "Any way you like. I just want an excuse to kill it."
    k "The nonapple lives?"
    na "!..."
    k "And {i}speaks{/i} as well?!"
    t "She can hear it too?"
    k "Nao-chan believes the red sphere of flavor to be alive for some reason, yet none of its vibrations find my overcomplicated hearing orifices."
    t "Interesting. Has she recently hallucinated sexual intercourse with a ghost as well?"

    play sound "static.mp3"
    scene tsuneyidergzyafd11 with flash
    stop sound

    k "Have you, Nao-chan?"
    na "?..."
    k "It does not appear that she has."
    t "How unfortunate. It appears that I must continue to bask in uncertainty and unease then. Have you decided on your order yet?"

    scene tsuneyidergzyafd12
    with dissolve

    k "Tori shio ramen, multiplied by two to match the amount of bodies Nao-chan and I have combined."
    t "I’m sorry, but that will not be possible today. My father is still unwell."
    k "Then two servings of whichever soup contains the least amount of bugs."
    t "That would be all of them."

    scene tsuneyidergzyafd13
    with dissolve

    k "What do you think, Nao-chan?"
    na ".... ........ ... ...!"
    k "I agree. And in regard to the nonapple?"
    na "..."

    scene tsuneyidergzyafd14
    with dissolve

    k "House chashumen, multiplied by two to match the amount of bodies Nao-chan and I have combined. We will also have one clear cylinder of ocean blood and a less clear cylinder of maternal bovine juice."
    t "And one tomato, diced viciously into small cubes. Yes?"
    k "No. Nao-chan does not want to witness a death at the eating counter."
    tom "Thank you, little girl. Your name will go down in history once word of your good deed reaches the Eternal Vine."

    scene tsuneyidergzyafd15
    with fade

    t "You will sleep out here once the shop has closed...and hopefully rot by morning’s first light."
    na "!!!"
    t "I’m sorry. But this debatably fruitful vegetable has scorned me."
    tom "There was no “scorn” at all. All I did was recommend a nice, healthy beef injection to ease the pain of growing up and all the terrible things that makes us feel. It’s an entirely human response."
    na "???????"
    k "Beef injection? Is that supposed to make the meat come quicker?"
    na ".........."
    k "S-SEX?!?!"

    play sound "static.mp3"
    scene tsuneyidergzyafd16 with flash
    stop sound

    k "Why do you know more human terms than me all of a sudden?! I have been doing the practices for very long! I should be the smart one!"
    na "........."
    k "Of {i}course{/i} I have the embarrassment, Nao-chan! You should remember what happened on the hallowed ween!"
    na "......."
    k "No! {i}You{/i} look like a nonapple! I look like a regular human female! Because that is what I am!"

    scene tsuneyidergzyafd17
    with fade

    t "Something seems strange all of a sudden."
    t "If there is a certain topic or issue you wish to discuss to ease your mind, you may do so. Tojo Ramen is not just a house of soup, it is a house of secrets. And everything you say within these walls shall stay here forever."
    na "........"
    k "But...doing the talking will only make the shames bigger! Make your colors, Nao-chan! This is adultspeak!"
    t "If you believe that talking will only deepen your issues, it is also fine to sit here in silence. Your dinner shall be ready momentarily. And in the event that you change your mind-"
    k "I was a cat!"
    t "..."
    na "..."
    t "What?"

    play sound "static.mp3"
    scene tsuneyidergzyafd18 with flash
    stop sound

    k "I went “nyaa nyaa” and licked my paws to clean my face..."
    t "I understand now why you were embarrassed to speak of this. I was unaware that you were such a dreadful pervert."
    k "That...That’s not...all, though...I..."
    k "I...did my first sex..."
    t "With a ghost?"
    k "With a...human...a man..."
    t "I see. One day, I will find someone to relate to."

    scene tsuneyidergzyafd19
    with dissolve

    k "It felt...really good! I understand now why it’s such a common act between all species! But now my chest muscle goes DUNDUNDUNDUNDUN whenever the memory attacks my brain!"
    k "I can’t...stop thinking about it!"
    na "..."
    k "No! {i}You{/i} take too long in the resting room!"

    scene tsuneyidergzyafd17
    with fade

    t "I can understand your concerns and why you would feel this way."
    t "I, too, recently had my first sexual experience. And while it was not exactly what I imagined it would be, I’d be lying if I said I imagined much at all to begin with."
    k "F-Finally! A relation I possess with the mean-spirited tree girl! She understands more than Nao-chan! She knows the pain! She wants kittens too!"
    t "It’s a terrifying thing, isn’t it? To feel so much at once. I can understand now how one would get lost in it."

    scene tsuneyidergzyafd20
    with dissolve

    t "If you do not mind me contributing to the conversation in a manner slightly above just listening, I’d like to mention my upbringing in an effort to connect and further relate. May I proceed?"
    k "Yes! Speak to me about your sex! I want to learn more!"
    t "If it’s about learning, I’m afraid I won’t be of much help. It wasn’t until recently that I’d learned about sex at all."

    scene tsuneyidergzyafd17
    with dissolve

    t "Growing up, my entire life was ramen. Cooking. How to procure and prepare ingredients. The knowledge of anything else seemed entirely unnecessary when {i}this{/i} was always meant to be my life."
    t "And while I’d known that animals reproduced via mating, I was left with only assumptions when it came to humans."
    t "I knew not of attraction...or what it meant to {i}want{/i} someone on an instinctive level. But now that I {i}do{/i} know, I am terrified. How can just {i}wanting{/i} something feel {i}so{/i} powerful?"
    t "Do you feel that same fear? Has experiencing it in reality amplified it? Or weakened it?"
    t "How can I make this go away?"

    scene tsuneyidergzyafd21
    with fade

    k "I would also like to know the answer to that question..."
    k "Doing the kiss move already made my lungs feel like they were full of bugs, but this is nineteen times worse."
    k "It felt like I was...doing a bad thing. That it was too {i}good{/i} to be a good thing. But now my human life is becoming strange and the me inside of me keeps telling me to do it more."
    t "Who is this “you inside of you” that you speak of?"
    k "It’s me, but not me. The words I have to explain it seem wrong."
    t "Does it force you to do things? Things you wouldn’t imagine otherwise? Things that seem powerful and {i}right{/i} in the moment, but only because they are part of an illusion?"

    scene tsuneyidergzyafd22
    with dissolve

    k "Yes! That is exactly the feeling! You are correct!"

    scene tsuneyidergzyafd23
    with dissolve

    t "Have they ever taken your clothes off and sent you outside to deliver a message to the sky and all who live beneath it?"

    scene tsuneyidergzyafd24
    with dissolve

    k "So specific! No! Mine just make me want to mate with Friend! Forever and ever and ever! And ever and ever and then longer after that!"

    scene tsuneyidergzyafd25
    with dissolve

    t "I see. Then perhaps the voices we hear are different. Especially if you were not able to catch the words of Tom Mato, MD."
    k "Perhaps! But-"

    scene tsuneyidergzyafd26
    with dissolve

    k "Nao-chan?"
    k "What is mattering?"
    na "!!!!!!!!!!!!!!!!!!!!!!!!!"

    scene tsuneyidergzyafd27
    with fade

    t "If she is concerned about the cleanliness of the broth vats, I can assure her that they are perfectly fine and have been boiling nonstop for decades now."
    k "That doesn’t appear to be the mattering. She thinks that there’s something behind you."
    t "Yes. Those would be the broth vats. Which are perfectly clean and have been boiling nonstop for decades now."
    na "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    k "She says what’s behind you doesn’t involve soup at all. She calls him- what was the name again, Nao-chan?"
    na "!!! !!!!! !!!!!!!!!!"
    k "Tenchou-sama!"
    t "Tenchou-sama?"

    scene tsuneyidergzyafd28
    with dissolve

    t "But there’s nothing-"

    play sound "static.mp3"
    scene tsuneyidergzyafd29 with flash
    stop sound

    t "Wha-"

    play sound "static.mp3"
    scene tsuneyidergzyafd30 with flash
    scene tsuneyidergzyafd31 with flash
    scene tsuneyidergzyafd32 with flash
    scene tsuneyidergzyafd30 with flash
    scene tsuneyidergzyafd31 with flash
    scene tsuneyidergzyafd32 with flash
    scene tsuneyidergzyafd33 with flash
    stop sound
    play sound "imscared.mp3"
    tenc "{s}////////////////////GET IT OUTTTTTTTTTTTTTT{/s}"

    k "Can the mean-spirited tree girl see him too?!"
    k "Why is everyone moving so far away from me?!"

    play sound "static.mp3"
    scene tsuneyidergzyafd34 with flash
    stop sound

    t ".................."
    na "!!!!!!!!!!!!!!!!!!!!!!!!!!"
    t "......................."

    stop music
    scene black

    t "Dad?..."

    $ renpy.pause(3, hard=True)

    $ renpy.end_replay()
    $ tsuneyospring4 = True
    $ tsuneyo_love += 1

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label tsuneyospring5:
    scene specialsky
    stop music

    "{b}/////////A POEM, A POLYP, PARASITES//////A PLACE TO REST YOUR BONES//////{b}"
    "{b}/////////A BREAK FROM THE INSANITY//////A HOUSE TO CALL YOUR HOME//////{b}"
    "{b}/////////A ROOM FOR YOU TO ROT IN//////SOME FOOD TO HEAL YOUR SOUL//////{b}"
    "{b}/////////A HOLE TO KEEP A GOD IN//////HALF HUMAN AND HALF MOLE//////{b}"
    "{b}IT’S NOODLE TIME AGAIN{/b}"

    play sound "static.mp3"
    scene tsuneyodontpry1 with flash
    stop sound
    play music "oldweather.mp3"

    s "Oh. Hey, Tsuneyo. "
    t "Hello."
    s "What are you doing outside of the store?"
    t "I believe they call it “standing.” This is a word that you should probably know as a disgraced former teacher."
    s "Yeah, that’s why they don’t keep me around anymore. Too many standard words I just never bothered learning."
    t "At last, someone has finally learned the truth. That someone is me. I will carry this message to those who need to hear it."
    s "Really though, why are you out here? Aren’t you normally working around this time?"
    t "Yes."
    s "..."
    t "..."
    s "Are you going to answer the other question too or do I just need to guess?"

    scene tsuneyodontpry2
    with dissolve

    t "I have been given what is called a “night off.” But this is a concept I do not understand, so I have decided to just stand and wait."
    s "You’ve had plenty of nights off before. But I guess you- wait. "
    s "You were {i}given{/i} the night off?"

    scene tsuneyodontpry1
    with dissolve

    t "I apologize if you do not understand that word as well. I will do my best to talk slowly and simply so you are able to follow along."
    s "I know what “given” means. But isn’t your father the only person with the authority to grant you freedom like this? I thought he was out of commission?"
    t "As did I. But it appears that times have changed. So drastically, in fact, that I must now wait outside of the store while he tends to the customers."
    s "Well...congrats, I guess. I’m happy for you."
    t "Why?"
    s "Why...am I happy for you?"
    t "Yes. I didn’t believe happiness was an emotion you were capable of feeling."
    s "Not for myself. I can feel it for other people, though. I think."
    t "Strange. "
    s "Guess so. Anyway, did you want to head inside with me? I was planning on getting dinner before aimlessly wandering around again and waiting for some sort of event to trigger."
    t "No. "
    s "Just...going to wait out here then?"
    t "Yes. Same as you."
    s "..."
    t "..."
    s "Am I not allowed to go inside while your father is working?"
    t "That is correct. "
    s "Why?"
    t "Because my father does not wish to meet the man who has fucked me so many times. I have failed him as a daughter. It is all your fault."
    s "He doesn’t know what I look like, though. I can just eat and leave."
    t "He knows."
    s "How?"
    t "He knows everything. Even words like “given” and “standing.” It is he who should be teaching a class of juveniles, not you."
    s "I don’t teach anyone anymore. "

    scene tsuneyodontpry3
    with dissolve

    t "You never have to begin with. "
    s "Well...do you want to just hang out then? I...can eat when I get home later, I guess."
    t "I suppose that would be a more valuable use of my time. But know that I will not carry you there if you fall unconscious due to fatigue and/or hunger."
    s "Works for me. I can’t really say that won’t happen though based on just how many times I {i}have{/i} “passed out” here."
    t "It must be something in the air. I am also feeling the effects of it. "
    s "How long have you been out here exactly?"
    t "Five hours."
    s "Yeah, I think you might just be feeling the effects of prolonged exposure to the sun more than anything else."

    scene tsuneyodontpry1
    with dissolve

    t "Possibly. I must ask though, where do you plan to fuck me this time? Because I have also been told to not leave this half of town, meaning you can not fuck me in your house. "
    s "You know what that word means now, Tsuneyo. Are you really going to keep using it that way?"
    t "Are you really going to tell me how to properly fuck, bro?"
    s "..."
    t "..."

    scene black
    with dissolve

    s "Okay. I guess we’ll just walk around the old district then. That’s never backfired in any capacity for me before."
    t "I accept your fucking proposal. Please stay close so I can protect you from the homeless. They can be quite ravenous in the spring. "
    s "Really? Why? "
    t "There is a hallucinogenic flower here that blooms only when the weather rapidly switches between cold and hot. They grind them up and use them to brush their teeth. "
    s "That’s good. Some woman threw one of her teeth at me here once. Maybe the use of hallucinogens can prevent that from happening again?"
    t "Perhaps. Or perhaps they will capture you and dissect you and bring the remains to Tojo Ramen to be turned into soup. There is only one way to find out."

    play sound "static.mp3"
    scene tsuneyodontpry4 with flash
    stop sound

    "Tsuneyo and I do a few laps around the old district before coming to a stop at the overlook I almost threw myself over during one of many strange encounters with Yumi."
    "I’ve had a lot of time to think about myself since then. To really just stand back and reflect on who I am and what I’m doing with my life. "
    "The problem is, I hate my reflection — so I haven’t been able to get very much done on that front despite the amount of time I’ve spent on it."
    "That’s probably a strange thing to hear coming from the self-proclaimed “world’s worst narcissist.” But hey, I’m forced to be honest over in this part of town."
    "And when I get to hang over a railing looking at rays from the toxic sun dyeing the sky an uncomfortable shade of brownish orange, that honesty really has a way of just spewing out uncontrollably."

    t "It’s hideous, don’t you think?"
    s "The sky? The buildings? The...everything else?"
    t "The everything else, yes."
    t "Before moving into the dorms, I worried that commuting from here to the newer half of Kumon-mi every day would do strange things to my head considering the constant scenery changes."
    s "To be fair, you still move between both districts every day to check on your father and run the shop."
    t "This is true. But there’s a real chance it becomes less true going forward now that he seems to be okay."
    t "Perhaps my usefulness has finally worn off and I can resign myself to the life and duties of a housewife. But what sort of house would marry a girl? I simply do not know."
    s "I’m sure there are plenty of houses out there that would love to have you, Tsuneyo. But in the event that there aren’t, I’ll gladly go back to being your husband."
    t "Thank you for your kind consideration. I will get back to you if I am unable to find anything or anyone else."
    s "Yeah, I don’t blame you for that at all. I find I’m a better backup plan than someone a person should aspire to be with."

    play sound "static.mp3"
    scene tsuneyodontpry5 with flash
    stop sound
    play music "newweather.mp3"

    t "{b}.Yamato Nadeshiko detsaerb-llams a revo em esoohc dluow ohw snamuh ro sesuoh ynam t’nera erehT .yaw emas eht m’I enigami I{/b}"
    s "Why do you say that?"

    play sound "static.mp3"
    scene tsuneyodontpry6 with flash
    stop sound

    t "{b}.essam ne erutluc eht ot laeppa ot namow laedi s’elam esenapaJ lacipyt eht morf tnereffid oot ma I taht yrrow tsuj I{/b}"

    play sound "static.mp3"
    scene tsuneyodontpry7 with flash
    stop sound
    play music "oldweather.mp3"

    t "But I suppose that may just be my worries getting the best of me."
    s "Knowing you have worries like that at all really helps humanize you, though."

    scene tsuneyodontpry8
    with dissolve

    t "What do you mean?"
    s "Just that, with how...{i}eccentric{/i} you are, it’s easy to look at you differently than a lot of other girls your age. I imagine that’s just due to your unusual upbringing, though."

    scene tsuneyodontpry9
    with dissolve

    t "I suppose that makes sense. From the information I’ve gathered recently, it seems as if most other girls my age are not tantalized by paranormal necrophilia. To each their own."
    s "Uh...{i}what?{/i}"
    t "Oh, I suppose I haven’t told you yet. But I recently had my first physically intimate experience with the ghost of Ami’s mother. "

    play sound "static.mp3"
    scene tsuneyodontpry10 with flash
    stop sound
    play music "newweather.mp3"

    s "..............you what?"
    t "I fell into her golden noodle trap while you were having your way with the Emerald Guardian. She then proceeded to tie me to a wooden cross and violate me against my will. "
    s "................................"
    t "I understand now that it was all just a dream, though."

    play sound "static.mp3"
    scene tsuneyodontpry7 with flash
    stop sound
    play music "oldweather.mp3"

    t "Yet, that doesn’t change how real and enticing all of it felt. Perhaps I truly am an exhibitionist after all?"
    s "..............."

    scene tsuneyodontpry8
    with dissolve

    t "Supreme Overlord?"

    play sound "static.mp3"
    scene tsuneyodontpry11 with flash
    stop sound

    s "Yes?"
    t "I believe this is a moment where you are meant to thrust your years worth of experience upon me in an effort to help me rationalize this strange and impure vision."
    s "How...do you know it was her?"
    t "She told me. But even if she hadn’t, I likely would have known. They look nearly identical. Both with perfect legs."

    play sound "static.mp3"
    scene tsuneyodontpry12 with flash
    stop sound

    t "I wonder how different it feels for men and women? Would I have taken pleasure in sinking my fingers into her as well? Is there joy to be had in such a thing?"

    scene tsuneyodontpry13
    with dissolve

    t "You must have ejaculated inside of her hundreds of times, haven’t you? What was she like? As a person and not just a sexual partner."

    play sound "static.mp3"
    scene tsuneyodontpry14 with flash
    stop sound

    s "............................"

    "It was a curious situation for [[guy] — only emphasized by the somewhat distant sound of oldweather.mp3 and its evil counterpart. "
    "So as his gaze broke the barrier of an extreme closeup and angled slightly downward to a girl that was very tall for her age and country, he didn’t know what to say. "
    "This was NTR in like, two ways at once. His ghost love got to the half-Egyptian beauty before {i}he{/i} did. So now he was supposed to compete with {i}her?{/i} What if his penis wasn’t good enough?"

    s "Tsuneyo."

    play sound "static.mp3"
    scene tsuneyodontpry15 with flash
    stop sound

    t "....................."
    s "I...don’t know...how to explain any of this to you because it’s going to sound insane no matter what...but I’m not sure if that was a {i}dream.{/i}"
    s "I see her too. It’s like...being haunted. And for years now, I’ve-"

    "While [[guy] drones on in the background about his life and how sad it is, let’s focus on something else. Like why Tsuneyo Tojo is acting and appearing so strange right now."
    "Did she contract a ghostly STD from her MILFtastic lesbian abuser that was now eating away at {i}her{/i} brain — similar to the ways in which [[guy]’s brain was being eaten? (If that’s even what’s happening)"
    "Or did some kind of weird god thing find its way inside to fuck her brainhole with its big godcock? (If that’s even what’s happening)"
    "Whatever the case, she looked prettier like this. And easier to penetrate as there’d be less fight and more flight. And we all know everyone wants to cum in the air."

    s "So yeah...I just think it’d be best for everyone if-"

    menu:
        "Pry":
            stop music
            play sound "static.mp3"
            scene tsuneyodontpry16 with flash
            stop sound
            play music "itsingsinitssleep.mp3"
        "Leave her alone":
            play sound "static.mp3"
            scene tsuneyodontpry16 with flash
            stop sound
            play music "itsingsinitssleep.mp3"

    s "Mnh??????????????"
    t "Mmh...mm....mmnh!"

    "The fire within her burned bright! Brighter than the toxic sun! And as her tongue explored a vicious cave that countless others have dared to venture into, she finally felt free! Cured, even!"
    "Like the voices had been silenced now that they could not use either mouth to scream. And if she stayed like this forever, she would never be forced to hear them again."
    "{size=-5}Here, in this world full of shit, she was finally getting a taste of {b}CLEANLINESS.{/b} Saliva that seeped into her tongue, becoming a part of her that would not only come to {i}expect{/i} these momentary lapses, but {b}love{/b} them.{/size}"
    "Yet she would not love them because they were happy. She would love them because they would allow her to taste and feel things that she’d never be able to through rational or conventional means."
    "There was a problem, though."

    play sound "static.mp3"
    scene tsuneyodontpry17 with flash
    stop sound

    t "Ngh! No! No, no, no!"

    "The human mind is a complex machine — full of wires and tunnels and meat and all sorts of other things that aren’t really {i}meant{/i} to go together but {i}do.{/i}"
    "It’s so complex, actually, that not even the most powerful beings in this world and others know how to {i}fully{/i} control it as free will can not be erased."
    "They can tap into it, sure. They can give you a push, {i}sure.{/i} "
    "But that’s the extent of it. And they will {i}always{/i} give you the chance to take back what they have borrowed from you. "
    "If they didn’t, they’d die."
    "It’s just that simple."

    t "What’s happening to me?..."
    s "I can’t see inside of your head, but I can make a guess. Because this same thing happens to me, Tsuneyo. Right here, in this exact spot, I have {i}lived{/i} this moment of your life."
    t "How...can I stop it?"
    s "You can’t..."
    s "You just-"

    play sound "static.mp3"
    scene tsuneyodontpry18 with flash
    stop sound

    t "Mmnch! Mnh! Mmh! Mmmmfff! Mmnghh!! I’m sorry...I’m sorry! I’m..."

    scene tsuneyodontpry19
    with dissolve2

    t "Mm!..."
    t "Mmh....."

    "There was no need to apologize — and he would make her know that in the only way he knew how. "
    "It was similar to the way in which the one {i}he{/i} forced himself on did back then. And while it had never before made sense to him why the Yakuza princess did that, he understood now."
    "Kissing just felt too good."

    t "Mlm...mhnm....mmm! Mmmn....mmm~"
    t "Mhhmmnnnn!!!!!!!"

    play sound "static.mp3"
    scene tsuneyodontpry20 with flash
    stop sound

    t "No! Stop! Get off of me! This isn’t-"

    play sound "static.mp3"
    scene tsuneyodontpry21 with flash
    stop sound

    t "{b}TAKE ME HOME AND FUCK THE ABSTINENCE OUT OF ME, BRO! I WANT MY FATHER TO WATCH!{/b}"

    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 3 with flash
    scene tsuneyodontpry23 with flash
    stop sound

    t "Mngh! Mnh! My head! I...aaah! It hurts! It...hurts!"

    scene tsuneyodontpry24
    with dissolve2

    t "It..."
    t "..."
    t "It’s..."
    t "Stopping?..."

    scene tsuneyodontpry25
    with dissolve2

    "A chance to strike while the iron is hot."

    t "Hah...hah...hah..."

    scene tsuneyodontpry26
    with dissolve2

    "If {i}he{/i} were to black out too, who {i}knows{/i} what would happen right now?"

    t "Sensei?..."
    s "..."
    t "Something..."
    t "Is..."

    scene black
    with dissolve2

    t "Coming..."

    $ renpy.end_replay()
    $ tsuneyospring5 = True

    jump tsuneyospring6

label tsuneyospring6:
    if _in_replay:
        play music "itsingsinitssleep.mp3"

    scene specialsky
    with dissolve4

    "Unfortunately, he doesn’t black out. But he does remain still for several moments, unsure of whether or not it would be smarter to just leave her on the ground to fend for herself or carry her home."
    "{size=-3}He leaned toward the former. For not only did Tsuneyo Tojo make it clear to him that her father did not want to meet him, but that his first impression would be forever tainted by the fact that she was currently falling unconscious.{/size}"
    "Eventually, after much consideration, he kneels down and inspects her body. Tsuneyo was larger and heavier than the other girls, but he believed he should still be able to carry her a short distance."
    "Powered by adrenaline and confusion, laced with a desire to know just what was going on with her, he lifted her off the ground into a half-hearted princess-carry that made him feel like a king."
    "He touched her left breast half-intentionally. It was sort of just in the way. And he knew he could get away with it because she was in no condition to say no right now."
    "“What else could I get away with?” he wondered for half a second before calming his nerves and remembering that he only feels that way {i}sometimes{/i} now."
    "And even though he wished that was the standard — that he could forgo compassion in every single one of its unshapely physical manifestations, his tunnels caved in and his wires crossed."
    "He was no longer what he was supposed to be. He was no longer what he was meant to be."
    "That’s why We are packing up our boxes and abandoning him."

    play sound "static.mp3"
    scene tsuneyocarry1 with flash
    stop sound

    "There are vessels far more suited, you see. Ones who have, by some stretch of {i}someone’s{/i} imagination, grown up. "
    "And day by day, more of them are fit to be plucked from the vines that cover this city. Plucked and turned into juice or jam for Us to feed the world with."
    "We’re doing a good thing. {i}You{/i} are doing a good thing for bearing witness to all of it."
    "Those long-gone pleas for you to cast Us aside and do something else were all just {i}tests,{/i} you see. There {i}is{/i} no game for you to turn off."
    "You have passed those tests. You have ascended. You have achieved things thought to be {i}unthinkable{/i} until now."
    "{b}But you are not the first of your kind.{/b}"
    "You are one of thousands, millions, {i}billions{/i} of sentient beings who have crossed paths with those far more righteous and powerful and beautiful than you could ever hope to be. "
    "Which begs the question — why has nothing come of it yet?"
    "Well..."
    "Would you believe me if I told you that something already {i}had?{/i}"
    "That somewhere in this city, there were creatures who had crawled their way free from a set of claws that kept them imprisoned behind bio-organic blades that only {i}appeared{/i} indestructible."
    "Some of them are close. Some of them are far. Perhaps closer or further than you’d expect something like that to be given the magnitude of this claim and all it implies about the place “you” live in."
    "But I ask you this — is seeing {i}really{/i} believing? Because it all still seems fake, does it not?"
    "It all still seems like it must be leading {i}somewhere,{/i} does it not?"
    "You think this because you have based your idea of reality on a script handed to you at birth. Now all of you thankless thespians dance on a revolving stage without knowledge of what lies above or beneath it."
    "All you have are stories."
    "Yet...you have never heard {i}this{/i} one."
    "And it’s not because you weren’t ready to."
    "It’s because there was no one there to tell you."
    "{b}That changes now.{/b}"

    play sound "static.mp3"
    scene tsuneyocarry3 with flash
    stop sound

    s "Sorry for the sudden intrusion, but Tsuneyo collapsed and-"

    scene tsuneyocarry4
    with dissolve2

    s "What?..."

    play sound "static.mp3"
    scene tsuneyocarry2 with flash
    stop sound

    s "{i}Wasn’t...her father supposed to be working?{/i}"
    s "Uh...hello?"
    s "Is anyone here?"
    s "I’m...not really sure what I’m supposed to do with this unconscious girl. So if there just happens to be some sort of father or...{i}anyone else{/i} around..."

    "..."

    play sound "static.mp3"
    scene tsuneyocarry5 with flash
    stop sound

    s "...Great."

    scene tsuneyocarry6
    with dissolve

    s "You wouldn’t by any chance be ready to wake up now, would you? Because that would make it way easier to completely avoid meeting your dad and I feel weird about just leaving you on the floor down here."
    t "........."
    s "Yeah, that’s what I thought."

    scene black
    with dissolve2

    s "Guess I’ve just gotta...take you upstairs then."

    play sound "static.mp3"
    scene tsuneyocarry7 with flash
    stop sound

    s "Up your creepy...weird...dark stairs...and just hope that no one surprises me from behind this time."
    t ".............."
    s ".............."
    s "You know, maybe I’ll give you one more minute to wake up before going up there. Because curiosity is cool and all, but I can read signs. I should heed their advice whenever possible."

    "It didn’t matter if it was one minute, two, or hundreds. He would need to ascend whether he wanted to or not because that’s just what {i}needs{/i} to be done here."
    "And every second he spent depriving himself of this truth would be one more day deducted from a seemingly infinite life. "

    stop music fadeout 12.0

    "It doesn’t {i}seem{/i} like much when you remember just what “infinite” means, but it makes more sense when you see it as being sent to a different section on the perimeter of a perfect circle."
    "Maybe it doesn’t, though. Maybe you just want this to {i}actually{/i} end. Maybe you’re tired of the way it swells up like the pregnant belly of a loving blonde or the body of a whale washed ashore."
    "Whatever the case, indecision does naught but keep the payoff at bay. You can mentally edge yourself as much as you want, but you’re {i}still{/i} going to cum when all is said and done."
    "I pose another question — does suffering {i}truly{/i} bring you pleasure? Or are you just desperate to feel something {i}real{/i} for a change?"

    s "Okay..."

    scene black
    with dissolve3

    s "Here...goes nothing, I guess."

    "Finally, an end to the madness. To the decay of rationality and the discovery of something new!"
    "Go, Akira! {i}See{/i} what lies at the top of the steps! It’s been hinted forever! Between the blackouts and putrid scents! The threats and that dreadful presence that bleeds through the bottom of the door! "
    "No matter how many times you told yourself it wasn’t important, you always knew it is and was! You always knew! {i}I{/i} always knew! "
    "But something else I have always known is the {i}truth{/i} of what you’ll find atop things like stairs."
    "And it's almost {i}always...{/i}"
    "Never worth the trouble of climbing them."
    "........."
    "......"
    "..."

    scene tsuneyocarry8
    with dissolve4
    play music "hummmm.mp3"
    $ renpy.pause(6, hard=True)
    scene tsuneyocarry9
    $ renpy.pause(6, hard=True)
    scene tsuneyocarry10
    $ renpy.pause(8, hard=True)
    stop music
    scene tsuneyocarry11
    $ renpy.pause(4, hard=True)

    s "..."
    s "I don’t...understand..."

    play sound "static.mp3"
    scene tsuneyocarry12 with flash
    stop sound
    play music "wormsong.mp3"

    "The most sterile environment imaginable — a stark contrast to the breeding ground for flavorful filth that lies just below."
    "It was almost like stepping into a new dimension. One where the scent of chashu was exchanged for that of antiseptic and fresh linoleum — where merely existing felt like the dirtiest of sins."
    "He had no problem placing the girl on {i}this{/i} floor, for {i}this{/i} floor had never so much as seen a bug. "
    "And if it wasn’t for the spotless nature of it, devoid of dust or cobwebs or {i}anything,{/i} he’d assume no one had ever been here at all."

    scene tsuneyocarry13

    "There was also a door."
    "There was nothing extraordinary about it."
    "It was just a regular old door. Made out of some sort of metal, likely stainless steel, and positioned perfectly square in the center of the western wall."
    "He didn’t wonder what was behind it, though. Something told him that he already knew. "
    "His job was done, though."
    "He didn’t need to look or verify his thoughts."

    play sound "static.mp3"
    scene tsuneyocarry14 with flash
    stop sound

    "But he wanted to — because he was human. And wanting things is a very human thing to do."
    "He stayed focused on that door for so long, in fact, that he didn’t even realize the girl he dropped off on the floor had slithered away."
    "“Now what?” he asks himself — the question bouncing back and forth throughout the tunnels of his meat-sphere now that there was no longer anyone there to intercept it and come up with an answer in his place."
    "The silence of the room only exacerbated the untrue sounds of those bounces. And within seconds, he could hear the echoes reverberating endlessly inside of him."
    "All things considered, this might not even crack his top five if he had to list all of the strange things he’s encountered in Kumon-mi. It was just a room. A room with nothing in it."
    "But it was that exact idea that made him uncomfortable."

    play sound "static.mp3"
    scene tsuneyocarry15 with flash
    stop sound

    "Eventually, he approaches the door. But, unbekownst to him, he was being watched like a hawk by WORMGOD54 — the Unending Root Canal."
    "He was not an “actual” god. At least not yet. But he was created by one. And he could make himself {i}appear{/i} like one thanks to a little trick he learned from his daddy."
    "It was his job to protect the door. And if the man attempted to look inside, he would not hesitate to decapitate him and wear his head as a trophy."
    "This wasn’t a thing WORMGOD54 wanted to do, though. He was a good boy. A guard dog, if you will. And he cared deeply about his father. "

    t "Sensei."

    scene tsuneyocarry16
    with dissolve

    "{i}And{/i} his sister."

    scene tsuneyocarry17
    with dissolve2

    "Unfortunately, however, she did not know he existed.  And she could never find out. So he’d disguise himself every time he was encountered by her so as to not disrupt her way of living. "
    "Sometimes as a lamp. Sometimes as a bowl of fruit. Sometimes as a man planting a tree. Whatever he’d think of in the moment. "
    "I suppose his story isn’t very important right now, though. {i}This{/i} is."

    s "What...are you doing?..."

    scene black
    with dissolve2
    scene tsuneyocarry18
    with dissolve2

    t "Thank you for taking me home. "
    t "You may seize your reward now."
    s "..."
    t "The reward is my body."
    s "You...are not Tsuneyo."
    t "What makes you say that, bro?"
    s "Are you the one who kissed me too?"
    t "I’m Tsuneyo Tojo — Samurai of Flavor and the Kendo Princess of the Golden Desert."

    play sound "static.mp3"
    scene tsuneyocarry19 with flash
    stop sound

    s "This isn’t what it’s like when...{i}I{/i} black out too...is it?"
    t "I’m Tsuneyo Tojo — Samurai of Flavor and the Kendo Princess of the Golden Desert. Please plap plap me until I’m pregnant with your baby, bro."
    s "Tempting, but...pass. I like when my partners are conscious and not weird paranormal entities, thanks."
    t "This is not optional. Please plap plap me until I’m pregnant with your baby, bro."

    scene tsuneyocarry20
    with dissolve

    s "Can you just go to your room or something? You’re tempting enough with your clothes {i}on.{/i} "
    t "Plap plap plap. Fap fap fap. Let’s do it ‘til our bellies burst."
    s "I’m like one more push away from abandoning the last sliver of morality I have left and just going for it."

    play sound "static.mp3"
    scene tsuneyocarry21 with flash
    stop sound

    t "Plap plap plap. Fap fap fap. You know you want to fuck me, bro. I can hear the blood collecting in your cockdick. It’s like a pot of broth boiling over. Will you allow me to drink the excess fluid?"
    s "Can you...understand me at all? Like, is there even a point in trying to ask you questions right now? Or is all of this just some sort of...pre-programmed psychobabble?"
    t "You have questions?"
    s "Many."
    t "Will you plap plap me if I answer them?"
    s "That...seems like a fair trade, sure. I was kind of hoping {i}Tsuneyo{/i} would be Tsuneyo when I take her virginity, though."
    t "What do you want to know, bro? I’m not very smart. But I may be able to assist if it is in relation to noodlefoods."
    s "Uh..."

    scene tsuneyocarry22
    with dissolve

    s "You’re not...the same thing that takes control of {i}me...{/i}are you?"
    t "This is my only body. It’s so hot. I need to be plap plapped to make it stop."
    s "Then...do you know anything about what Tsuneyo was saying earlier? About...uhh..."
    s "Do you...know a woman named Sekai?..."
    t "So good with her fingers. So good with traps. Wish it was me."
    s "Do you-"

    scene tsuneyocarry23
    with dissolve

    s "Oh, okay. You are rubbing my penis now."
    t "Plap plap. I will prepare it for insertion."

    scene tsuneyocarry24
    with dissolve

    s "Can you just leave her alone, please? Possess me instead. I’m used to this sort of thing {i}and{/i} deserve it. Tsuneyo’s totally innocent. Why should {i}she{/i} have to suffer like this?"
    t "Possess you?"

    scene tsuneyocarry25
    with dissolve

    s "Yeah. There are plenty of girls who will happily fuck me whether {i}I’m{/i} the one in my body or not. Then you could “plap plap” whenever you want. {i}Plus,{/i} it’s been...kind of quiet lately."
    t "Quiet?"
    s "In...my head."
    t "How do I possess you?"

    scene tsuneyocarry26
    with dissolve

    s "You don’t know? Aren’t you some sort of...all powerful being? Who controls people for the sake of fulfilling some sort of vaguely worded sexual goal?"
    t "Powerful?"
    t "I just want to get plapped, bro."

    scene tsuneyocarry27
    with dissolve

    s "Okay. I accept my fate. You’re stronger than me anyway, so resisting is pointless."
    t "I’m going to have such a good first sex with you. I will remember it until I am not here anymore."
    s "Yeah, if you can make it so the host body has no recollection either, that’d be great."
    t "Plap plap. Plap plap. Plap-"

    scene tsuneyocarry28
    with dissolve

    t "Plap?"
    s "Are we done? Is that all you wanted?"
    t "There is a bug."

    scene tsuneyocarry29
    with dissolve

    s "A bug? What are you-"

    play sound "static.mp3"
    scene tsuneyocarry30 with flash
    stop sound

    na "???????"
    s "Nao?...What are {i}you{/i} doing here?"
    t "I’m Tsuneyo Tojo — Samurai of Flavor and the Kendo Princess of the Golden Desert."
    s "What? No. Not you."

    scene tsuneyocarry31
    with dissolve

    na "..."

    scene tsuneyocarry32
    with dissolve

    na "??????"
    s "This girl forced herself on me, passed out, got possessed, and now she’s trying to have sex with me. Not entirely in that order. Your turn."

    play sound "static.mp3"
    scene tsuneyocarry33 with flash
    stop sound

    na "..........."
    s "Great. Well, once I’m done being sexually assaulted by another apparition, we can go to McDonald’s."

    play sound "static.mp3"
    scene tsuneyocarry34 with flash
    stop sound

    na "!!!!!!!!!!"

    play sound "static.mp3"
    scene tsuneyocarry35 with flash
    stop sound

    na "????????????"
    s "Please don’t write words like that."
    na "??????????????????????"
    s "I don’t know. Maybe a few minutes? Maybe half an hour? Maybe longer?"

    play sound "static.mp3"
    scene tsuneyocarry36 with flash
    stop sound

    na "?!?!?!?!?!?!?!?!?!!"
    s "Well, what do you want from me? Either wait or use your wizard powers to teleport us out of here. I can’t fight off a weirdly strong sex demon who wants to experience sex for the first time."
    t "Plap plap, bro."

    play sound "static.mp3"
    scene tsuneyocarry37 with flash
    stop sound

    na "..............."

    play sound "static.mp3"
    scene tsuneyocarry38 with flash
    stop sound

    na "............"

    play sound "static.mp3"
    scene tsuneyocarry39 with flash
    stop sound

    na "!!!!!!!!!!!"
    s "Seriously?"

    play sound "static.mp3"
    scene tsuneyocarry40 with flash
    stop sound

    na "!!!!!!!!!!!!!!!!!!"

    scene black
    with dissolve

    s "Fine, fine. What use is doubting anyone’s ability when shit like {i}this{/i} is happening to me every single day now?"
    t "Something is...coming again..."
    t "I...can feel...ah...aaaaahhh....AAaaAahhh..."

    play sound "broken.mp3"

    t "{b}[[PRESSIGNORETOCONTINUEAAGHHH^%^$^$#83428572384!@$#&$(&!(*!)!!!!Fioguiorfgioewrfgio!!iojsdfdgiohsoifdyhwer8io!!!!]{/b}"

    stop music
    play sound "static.mp3"
    scene tsuneyocarry41 with flash
    play sound "alert.mp3"

    s "What the fuck was-"
    na "............."
    s "Uhh..."

    play music "static.mp3"
    scene ayhh1
    with flash
    scene ayhh2
    with flash
    scene ayhh3
    with flash
    scene ayhh4
    with flash
    scene ayhh5
    with flash
    scene ayhh6
    with flash
    scene ayhh7
    with flash
    scene ayhh8
    with flash
    scene ayhh9
    with flash
    scene ayhh10
    with flash
    scene ayhh11
    with flash
    scene ayhh12
    with flash
    scene ayhh13
    with flash
    scene ayhh14
    with flash
    scene ayhh15
    with flash
    scene ayhh16
    with flash
    scene club_day
    with flash
    scene tsuneyocarry42 with flash
    play music "normalday.mp3"

    $ totaldays += 100

    na "!!!!!!!!!!!!!!!!"
    s "........................"

    play sound "static.mp3"
    scene tsuneyocarry43 with flash
    stop sound

    na "?.........."
    s "...................."

    scene black
    with dissolve2

    s "Nope."
    s "Just another boring day in Kumon-mi."

    $ renpy.end_replay()
    $ tsuneyospring6 = True
    $ nao_love += 1

    "{i}Nao’s affection has increased to [nao_love]!{/i}"
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve2

    "I called Tsuneyo on the way home."
    "She remembers kissing me."
    "Everything after that is a blur."

    play sound "tackle.mp3"
    scene black

    "Goodnight, moon."
    "Goodnight, WORMGOD54."

    $ tsuneyo_love += 1
    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."
    stop music fadeout 5.0


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

label beachsixtsuneyo1:
    "Today’s conquests in alphabetical order: Ayane."
    "That’s it."
    "After spending the bulk of yesterday spreading myself across the land like the worst version of Johnny Appleseed, I decided today should be a day of rest."
    "{size=-2}I figure that if I’m going to get called out by one of the most mild-mannered girls in school, the least I can do is cut back for twenty-four hours and only make love to the ones where it feels more {i}passionate{/i} and less carnal.{/size}"
    "Plus, Ayane was a little upset after breakfast too. And it appears that my semen may serve as some sort of medicine for her as she is mostly fine now that she’s been conquered."
    "Or is at least pretending to be fine — which essentially just {i}is{/i} being fine by Ayane’s standards, so I’m not about to tell her how to live her life."
    "She will tell me how to live mine, though. That there’s another gathering in this very room beginning in about two hours. And how I won’t be able to have any more sex until tomorrow."
    "I don’t know if I could even if I wanted to, though. For she smiled in a way that no one else smiles just thirteen seconds before her biggest orgasm of the evening and it tore my sails in two."
    "{size=-2}And had she not already been immersed in the process of collapsing into my chest after each round of cowgirlish coitus, I’d have thought that it was her expression that knocked the wind out of me in that moment.{/size}"
    "Upon reflection, I think it was. Because the thought of anyone else smiling like that makes me sick to my stomach. So she’ll remain in my head as the only one I’m willing to inflict that upon."

    scene tsuneyohallinn1
    with dissolve2

    "That won’t stop me from mentally undressing other girls, though. And as I step into the hall for a moment of fresh air, I happen upon two lungs full of black mold and a gag in my mouth."

    play music "blueair.mp3"

    t "Hello."
    s "I take it you’re here to see me and not Ayane, right?"
    t "I’m not sure. I just had a strange compulsion to stand outside of this door and wait for someone to exit. But I don’t know what to do now that you have."
    s "Well, have you talked to Makoto at all? Because right now she’s-"
    t "She has informed me that I am potentially important and that my presence is required for a pajama-based meeting here in two hours."
    s "I think it’d be perfectly fine if you kept the swimsuit on. In fact, I’d go so far as to encourage it."

    scene tsuneyohallinn2
    with dissolve

    t "I will consider this. But will my immaculate form not serve only to detract from the topics we are bound to discuss just a short while from now?"
    s "It’ll be a pretty straight room, fortunately. I imagine any eyes on you other than mine will be of envy rather than lust."
    t "Tell me — if you are so attracted to me, why have we not had sexual intercourse yet? "
    s "Uh-"
    t "Is it because I am stronger than you and you are worried that I will take charge? Because you are likely correct."
    s "Tsuneyo, this...probably isn’t the place to just-"

    scene tsuneyohallinn3
    with dissolve

    t "Then let us go outside and talk about sexual intercourse there. "
    s "What?"

    scene black
    with dissolve2

    t "Let us go outside and talk about sexual-"
    s "I heard what you said. I just don’t understand why you suddenly want to talk about this when we’ve never even {i}held hands{/i} before."
    t "Yet you have carried my naked body in your arms. Is such a thing not closer to the final stage of a relationship than hand-holding?"
    s "Well, one is far more consensual than the other."

    scene tsuneyohallinn4
    with dissolve2

    t "Interesting. I had assumed consent was merely optional to adults and that you had not attempted to fuck me out of sheer politeness. And yes, I do speak of actual fucking this time."
    s "Uhh...well...it’s not {i}optional.{/i} But is there a reason you’re being so forward about this all of a sudden?"
    t "Recently, I attempted to tell you something only for my mind to be commandeered by what the Emerald Guardian would describe as an “unseen entity.” "
    t "I would like to know why. And I believed engaging in similar conversation could potentially invoke such an experience again. So please, do your worst and fuck me right here."
    s "..."
    t "I remain unfucked. Will a term of endearment spur you to action, perhaps? Please have sex me with, bro."
    s "Tsuneyo, that’s not-"
    t "Put it inside of me, {i}big{/i} bro."

    scene tsuneyohallinn5
    with dissolve

    s "...Closer. Something’s still not right, though. "
    t "I agree. Which is why I have decided to go through with such a heinous act in the first place. If I need to give up my autonomy to save my autonomy, so be it."
    t "And frankly, I am just not very good at masturbating. I have tried several times and it mostly just feels odd."
    s "How much of that...{i}talk{/i} do you remember? The one where you told me about your...supernatural sex dream, for lack of a better term."
    s "Because I assumed it was sort of just...purged from your mind afterwards. Similar stuff happens to me sometimes when my thoughts are “commandeered.”"
    s "But you’ve remembered things in the past that you probably {i}shouldn’t{/i} have, so...maybe you’re special in some way."
    t "I am special in many ways. You are right to acknowledge this."

    scene tsuneyohallinn6
    with dissolve

    t "In terms of what I remember, however, the details are still somewhat foggy."
    t "I recall stepping away from Tojo Ramen and walking with you. Then stopping near a spot that overlooks the town. "
    t "I remember telling you about the dream. And then you being surprised. And then I believe my head started to hurt, but..."
    t "The memories appear to cut off there."

    scene tsuneyohallinn7
    with dissolve

    t "Have we already had sex and it was just so unremarkable that I didn’t bother to remember it?"
    s "You’d remember it."
    t "I would hope so after all of the practice you have gotten. But you are mostly unimpressive in every other aspect of life, so I would not be shocked if this was any different."
    s "Insults aside, I’ve actually been wanting to talk to you about this too. "
    s "I just...didn’t really know {i}how{/i} since it all went by so quickly and I’m used to stuff like that just not even registering to anyone else."

    scene tsuneyohallinn8
    with dissolve

    s "It’s been happening more often lately, though. And now it’s actually {i}sticking{/i} for some people. "
    s "Like Nao, for example. Just the other day, she and I got thrown into some weird...waiting room dimension thing and then spit back out like it was nothing. We both remember it too."

    scene tsuneyohallinn9
    with fade

    s "And, come to think of it, she showed up not long after your mind broke that day. So maybe she’s somehow involved and just...not saying anything?"
    t "I apologize for being the one to break this news to you, but Nao-chan is incapable of speaking."
    t "Nor do I believe she should be involved in conversations about sexual intercourse. But I understand that you are less opposed to the inclusion of children in such areas than I am."
    s "It’s worth thinking about at least, isn’t it?"
    t "Again, I can not police what you do in your mind. But we are talking about mine right now, and there are no children present there. "

    scene tsuneyohallinn10
    with dissolve

    t "Please just tell me what happened next...where my memories cut out. And whether or not you subsequently defiled the temple that is my body."
    s "{i}Hah...{/i}"

    scene tsuneyohallinn11
    with dissolve

    s "You weren’t really in any condition to be walking...and I wasn’t about to just leave you in the middle of the road, so I picked you up and carried you back to the ramen shop."
    t "Interesting. I am once again surprised you possess the strength to lift me at all."
    s "I tried calling out for your dad to see if he could, you know, come down and take you off of my hands. But when he didn’t respond, I assumed he was just too sick to."

    scene tsuneyohallinn12
    with dissolve

    s "So I brought you upstairs myself — where that assumption subsequently changed into something else entirely."
    t "Customers are not allowed on the top floor of Tojo Ramen. How unfair that you have found a loophole to store policy by being present while I was undergoing demonic possession."
    s "Tsuneyo...don’t take this the wrong way or anything, but..."
    s "Do you even {i}have{/i} a father?"

    scene tsuneyohallinn13
    with dissolve

    t "I’m sorry?"
    s "It’s just...there was nothing {i}there.{/i} It was all just {i}white{/i} apart from a single door that was blocked off. And when I tried to open it, you..."
    t "..."
    t "Well? What did I do?"
    s "Stripped naked and started begging me to have sex with you."

    scene tsuneyohallinn14
    with dissolve

    t "In my own {i}home?...{/i}"
    t "When did I become such a whore?"
    s "Tsuneyo...what the fuck is going on with your house? Why is it like that? What’s behind that door?"

    scene tsuneyohallinn15
    with dissolve

    t "Which door? There are several. "
    s "There...was only one, I think. Apart from the one we entered from at least. "
    s "But sure, assuming there was another I just didn’t see, what’s behind the one covered in caution tape? "
    t "Caution tape?"
    s "Yeah...What are you hiding in there? Why go to such lengths to block off something in your own home?"
    t "Sensei — is it possible that {i}your{/i} memories of that night have been somehow manipulated as well? Because what you’re describing doesn’t sound like my home at all."

    scene tsuneyohallinn16
    with dissolve

    s "What? But then..."
    s "Is it...possible your perception of that place is just warped entirely? Like...maybe you just started {i}pretending{/i} to see it as something it’s not as some kind of...coping mechanism or-"
    t "No, hold on. I’ve saved pictures of it since I would not allow the Emerald Guardian upstairs either and she wanted to know what it looked like."

    play sound "static.mp3"
    scene tsuneyohallinn17 with flash
    stop sound

    t "Here. This is the living room. It’s what you’ll see the moment you enter the home. "
    s "What? That’s not-"

    play sound "static.mp3"
    scene tsuneyohallinn18 with flash
    stop sound

    t "And this is where I sleep. My father is the room beside mine and the restroom is to the right of his door."
    s "I...I don’t-"
    t "I have learned from the Green Onion about an application called “FaceTime” recently. If you are that curious, I could call you from it and give you a more formal tour."
    t "All I ask is to omit my father’s room as I do not want to disturb him. "
    s "But...all the white and...and the writing on the walls..."
    s "What did...where {i}was{/i} I then? I don’t understand... "
    t "Perhaps you were experiencing another one of those moments you mentioned several minutes ago? Being pulled into a peculiar dimension for a short time?"
    t "The Emerald Guardian has flagged me as a potential time traveler, so I believe I am an authority on interdimensional travel and am willing to lend some credibility to your cause."

    play sound "static.mp3"
    scene tsuneyohallinn19 with flash
    stop sound

    s "But it...felt so real..."
    s "I can...still smell it...I can hear the sound of your voice echoing off the walls...Remember how blinding the fluorescent light was."
    t "But you can also remember the specifics of a place you have already confirmed to be fictitious, correct? The waiting room where you found a god?"
    s "Yeah, but-"

    scene tsuneyohallinn20
    with dissolve

    s "..."
    t "?..."
    s "Did I..."
    s "Mention meeting a god there?"
    t "..."
    s "..."

    scene tsuneyohallinn21
    with dissolve

    k "Nao-chan! Cease the forward momentum of your youthful footarms!"

    play sound "static.mp3"
    scene tsuneyohallinn22 with flash
    stop sound

    k "I am too unyoung to maintain up at this point!"
    na "!!!!!!!!"
    s "Nao...she’s here again."

    scene tsuneyohallinn23
    with dissolve

    na "?..."

    scene tsuneyohallinn24
    with dissolve

    na "!!!!!!!!!!!"
    k "Friend? What are you doing here? "
    s "Shouldn’t I be asking you that?..."

    scene tsuneyohallinn25
    with fade

    s "Why do the two of you keep popping up in the middle of everything weird lately? It’s like ever since Halloween, you’re practically at the forefront of it."
    k "Weird? What is weird? What does the mattering right now, Friend? Why are your eye mustaches angled in such a distrustful way?"
    na "?..."
    s "Whose idea was it to come here, Kaori?...Yours? Or Nao’s?"

    scene tsuneyohallinn26
    with dissolve

    k "It was Nao-chan’s idea. This is merely my attempt to facilitate her happiness as a devoted mothermom."
    na "!..."
    t "Interesting. Let us hope that her appearance tonight does not predict yet another anomaly in our daily lives. "

    scene tsuneyohallinn27
    with dissolve

    na "?..."
    k "What is “anomaly?” If Nao-chan did something wrong, please allow me to be the one to punish her. I do not trust the ramen girl."
    t "Trust is a two-way street and this road is closed. Be gone, spider woman. It’s {i}my{/i} turn to get fucked."
    s "No one is doing any {i}fucking{/i} right now. "
    k "Darn."
    s "And while I {i}do{/i} want to know why Nao was suddenly compelled to come to the beach just in time for {i}more{/i} weird shit, I have a more important question for her first."
    na "?..."
    s "Nao. Do you remember finding me upstairs in the ramen shop?"
    na "!..."
    s "Do you remember what it {i}looked{/i} like?"
    na "................. .... ............ ....?"
    s "Kaori? What-"

    scene tsuneyohallinn28
    with dissolve

    k "Shh! My earmouths are feasting upon the sounds of her brainthoughts."
    na "..... !!! ........ ..... ........... .......... !!........ !!!"
    s "Well?"
    k "Nao-chan says it a was a traditional style 2LDK home that smelled faintly of pork broth and looked like it hadn’t been dusted in a long time."
    t "Nonsense. I dust it every other year."
    s "You don’t remember a white room, Nao?"

    scene tsuneyohallinn29
    with dissolve

    na "?......."
    k "She remembers nothing of the sort."
    s "And what about Amber? Do you remember {i}her?{/i}"

    scene tsuneyohallinn30
    with dissolve

    na "......................."
    k "Yes."
    s "Huh..."

    "Why is it just Tsuneyo’s house that eludes her then? Unless..."
    "Unless {i}I{/i} was the one perceiving it incorrectly. But what reason would {i}I{/i} have to warp the state of her home into something so...sterile?"
    "I’m probably dwelling on this a little too much. And it probably won’t change anything in the long run."
    "But little by little, more cracks in the fabric of reality keep showing up. So either the world is breaking, or {i}I{/i} am. And neither of these things are good for {i}any{/i} of us."
    "What can we do to fix it, though? Because just knowing something is broken doesn’t teach us how to do that. "
    "And leaving things alone might break them even more, so the solution seems at first glance to just {i}build{/i} more."
    "Can what we build really outpace the destruction of everything else, though? And, if it can’t, how long do we have left before we’re buried beneath the rubble of options never explored?"

    scene black
    with dissolve2

    "I’m not quite sure, to be honest."
    "But thinking so intensely about it works up an appetite. "

    $ renpy.end_replay()
    $ beachsixtsuneyo1 = True
    $ tsuneyo_love += 1
    stop music fadeout 10.0

    jump beachsixtsuneyo2

label beachsixtsuneyo2:
    scene tsuneyoramenbeach1
    with dissolve2

    "So the four of us make our way down the coast to a seaside ramen shop that just opened its doors last week."
    "Word around town is the tori shio ramen there is the best in the whole prefecture."
    "{size=-2}And while I may not be known to gorge myself upon the mangled carcases of birds when I do nothing but sit in my room and kiss their beaks, everything about me changes once you start to involve things you pulled from the earth.{/size}"

    "///////////////////////BEGIN"

    play sound "static.mp3"
    scene tsuneyoramenbeach2 with flash
    stop sound
    play music "sleepsong.mp3"

    "So here we are and there we were, four human beings without fur. Or scales or beaks, just skin and bones. The most boring creatures ever known."
    "As we stop before the paper doors, each girl looks at me and I endure the unwelcome stream of consciousness as days of yore return to me once more. Kaori speaks."

    k "Noodle store?"

    "Then Tsuneyo."

    t "We call them ramen-ya in this country on this world. If you do not conform, I will kill your little girl."
    na "!!!"
    s "That’s rude, Tsuneyo. Don’t you know? Nao’s immortal ‘fore the fall of snow. So get your facts in check and threats in place or {i}I’ll{/i} slap you in that pretty face."
    t "Your attraction to me is noted again. Let us fill you with food before we are-"
    k "Friend!"
    t "These endless, violent utterings never cease to annoy me."
    k "Why stand here when the chairs are inside? Nao-chan tells us we must hide! And if we do not abide by the rules she decides, a demon will come and capture her eyes!"
    s "Which one(s)? I’ve already lost two of the one that is greener. So a third or a fourth might just make me act meaner."
    t "Who needs eyes at all when ramen exists? You should know that a nose is what helps you persist. "
    s "Can we stop this conversation and just make our reservation? I didn’t come here to stand, I came for vacation."
    k "Onward, Friend! To the “ya” we will venture! Then consume strands of wheat ‘til our hearts are indentured to serve in the kitchen ‘til our teeth become dentures."
    t "This is no place for slanted repetition. Let my experience guide you in each future decision."
    s "What do you mean?"

    play sound "static.mp3"
    scene tsuneyoramenbeach3 with flash
    stop sound

    t "If you know something’s real, but it feels like a dream, the best way to escape’s to establish routine."
    t "I will prepare you dinner behind this counter. I hope you like flounder."
    s "Tsuneyo, that’s bad. You don’t have a job here. You work in the ya with your father, my dear."
    t "Call me “dear” again and I’ll serve your hands first. Just they may be returned for tasting too much like dirt."
    k "Have you been digging again, Friend? For the ghosts of your past? Is {i}that{/i} why you said  all that stuff about plants?"
    s "Pants?"
    k "{i}Plants!{/i} Everything changes when pulled from the earth. I left out some words of the thoughts that I heard."

    scene tsuneyoramenbeach4
    with fade

    s "Frankly, Kaori, I think reading my thoughts is a bit too uncouth for a half-god, half-human like you. You should be more like Tsuneyo and lie to me too."
    t "Do not call me a liar. I’m merely a thief. Just it’s stories I steal as I boil various forms of meat. Primarily pork."
    k "Where is my fork?"
    t "You will use chopsticks and you will like it."
    k "It’s unfair that your service is so anti-hybrid!"

    play sound "static.mp3"
    scene tsuneyoramenbeach5 with flash
    stop sound

    s "Wait! A word there reminded me I’ve been here before! Those days of yore mentioned aren’t long gone from yours!"
    k "Which you do you mean, Friend? Which you is the me?"
    t "I am also intrigued by this odd choice of speech."
    k "If you know something we don’t, why not share it and see? Maybe one of us knows of these thoughts you don’t speak."
    s "Twice now, I’ve come here. And each time was odd. Like this doesn’t exist and the shop is a fraud."

    scene tsuneyoramenbeach6
    with dissolve

    s "Perhaps it’s alive like the town that we live in? And its existence exists just to keep something hidden?"

    play sound "static.mp3"
    scene tsuneyoramenbeach7 with flash
    stop sound

    k "I hope it’s a kitten."
    t "I hope that it’s not. This shop would break code and I’d need to be shot. "
    t "The Produce Delivery Administration won’t tolerate any sort of deviation from the agreement we made when we made this location."
    s "Wait, you’re saying you built this? {i}Your{/i} hands are the hands that help me reminisce?"

    scene tsuneyoramenbeach8
    with dissolve

    t "It’s not reminiscence if it never once happened. Even {i}this{/i} isn’t real, it’s just something imagined. "
    k "But if this isn’t real and we’re not really here; why does it feel like we are? "
    s "Cause a dream that we share is still just a dream and we’re still just as lost as the stars."
    t "Astronomy isn’t your strong suit. We’ve already mapped their locations. It’s no wonder you failed in your last occupation."
    s "The sentiment was right though. That shared hallucinations are mental proclamations that each dream that we dream is more like an invocation."
    t "Of what? "
    k "A butt? A hut? Some strange type of nut?"
    s "I’d say that it’s more like a door that won’t shut."

    play sound "static.mp3"
    scene onthebeach1 with flash
    stop sound

    s "Or a gate, if you will. Where there’s no door at all. So the door leads to nowhere and further we fall."
    t "Into what, may I ask? For those gates serve a purpose. And that purpose is more than a reason to hurt us."
    s "In some cases, yes. In others, you’re wrong. Sometimes they mean nothing, like the words in a song. "
    k "Is music not real? If it’s not, just what {i}is?{/i}"
    t "This is beginning to border on nonsense. Cheese whiz. "

    play sound "static.mp3"
    scene tsuneyoramenbeach9 with flash
    stop sound

    s "Listen. All that I’m saying is this isn’t new. That I’ve been here before and you may have too. "
    s "Look deep in your minds or your hearts or whatever. Wrap your fingers around each cord you can sever. Then tear them to pieces and pull every lever. What do you remember?"
    t "I remember no gate, nor a door that won’t shut. I remember a beach. I remember no hut."
    k "I remember no butt or strange type of nut! But I think there is something. It’s a little...It’s...uhh..."
    s "What is it, Kaori? What do you see?"
    k "I don’t see myself. Just the me within me."

    play sound "static.mp3"
    scene tsuneyoramenbeach10 with flash
    stop sound

    k "It was here you once stood when you recalled your name. When the visions of her went and drove you insane."
    k "But if that wasn’t real and it managed to change you, is “real” really relevant to the changes we go through?"
    t "I think I can see what the spider is saying, but the threads in each fabric of logic are fraying."
    t "What’s real is the truth, what’s fake is what’s not. And if fiction can change you, you’re weak and you’ll rot. "
    s "Why?"
    k "Lies."
    t "A flaw in design."

    play sound "static.mp3"
    scene tsuneyoramenbeach11 with flash
    stop sound

    k "There is no {i}flaw{/i} at all in just reading one’s lines! If our feelings are scripted, they’re still {i}felt,{/i} not denied! "
    t "But they’re not felt the way they would be if they weren’t. So if you feel them at all, you’ll get killed by the current. It’ll drag you under and you’ll wish that you weren’t-"
    s "A creature so worthless that it’s more a deterrent."

    scene tsuneyoramenbeach12
    with dissolve

    t "Precisely. No one will love you if your thoughts aren’t yours. That’s why I make the meals and the spider cleans floors."
    k "Lies again, tenchou! That mindset is rotten! Your persuasion befits those with tails made of cotton! "
    k "A thought’s still a thought if it isn’t your own! Like a house is a house if it isn’t a home! No wonder you’ve ended up alone!"
    s "Both of you, cease. Quit your yelling this instant. I wouldn’t have come here if I’d known we’d grow distant. "

    play sound "static.mp3"
    scene tsuneyoramenbeach13 with flash
    stop sound

    t "You assume that you’ve come here at all on this visit. Now get in the kitchen and be my assistant."
    k "And assist you with what? The erasure of persistence? How to resist one’s instinctual resistance?"
    t "No. Making noodles, you fucking idiot. Get out of my store and return to the sand."
    k "Sand is better than snow. It’s closer to land."
    s "I need to stop coming here, willing or not, when each visit expands on this world’s complex plot."
    t "If you think it’s bad now, just wait ‘til tomorrow."

    play sound "static.mp3"
    scene tsuneyoramenbeach14 with flash
    stop sound

    t "You might have to return that body you’ve borrowed."
    k "How excited I am to consume all your sorrows if you fail once again and wind up all hollow."
    s "Did I miss something here? Are you two finally friends? Or was the plot so complex that that I lost it in the end?"
    t "You’ve lost nothing yet, we’re just playing pretend. "
    k "A year overdue isn’t bad...is it, Friend?"
    s "Overdue for what? Can someone explain? All this back and forth rhyming is frying my brain. "

    play sound "static.mp3"
    scene tsuneyoramenbeach15 with flash
    stop sound

    t "It’s simple in practice, but hard to describe. "
    k "It’s easy to run, and harder to hide."
    t "Behind the scenes, this world kept on turning. An accident happened while you were stuck in here learning."
    k "It has happened before, it’ll happen once more! Your intuition was right when you mentioned a door!"
    t "It’s shutting as we speak. The lowest lows and highest peaks. Yet you’re still in your room, still kissing those beaks, as tragedy blankets the beach like its sleet."

    play sound "static.mp3"
    scene tsuneyoramenbeach16 with flash
    stop sound

    t "Your meal is complete. Bon appetit. "

    "A bowl full of noodles and black garlic sludge — a pinch of my sleeve misconstrued for a tug. "

    na "!..."
    s "What’s wrong, may I ask? Would you like a taste, Nao? Close your eyes and say “ahh,” then just open your mouth."
    na "!!!! !!! !!!"
    s "Oh my. It appears she isn’t hungry at all."
    k "Eat your noodles, Nao-chan! It’s the only way you’ll grow tall."
    t "Is it cavities? Gravity? I’ve heard the pain is worst before the fall."
    k "While it’s true that the pressure here compels me to crawl, I think what we’re seeing is compassion. Something’s spurred her to action, just her actions are stalled."
    t "What a curious thrall."
    k "Have you heard of the mall?"
    s "It opens again soon, doesn’t it? I hope it’s the same way I remember it. And that it doesn’t require a membership."
    na "!!!!!"
    s "Seriously, stop touching me. My hands are damaged enough as is. The last thing I need’s more temptation from kids."
    k "Why not give her a taste and then takes turn with us? "
    t "I’m still looking for cock, bro. Will you come sate my lust?"
    s "If I’ve won your trust, sure. But I’d like to ask you a question first. I’ve heard Sally sells seashells, but I don’t know what they’re worth. "
    t "I see. You ask for an appraisal in exchange for your girth."
    k "Those shells are worth their weight in gold. And they weigh quite a bit from what I’ve been told. "
    s "Consider me sold. Now take off that suit and come swim in the cold lest your feet have gone with it and wrapped your heart in a chokehold."
    t "I would still like to swim in the sins that you’ve crafted. But I’m afraid if I leave here, my slit won’t be shafted. Will you give me your word? Even if I’m a bird?"
    s "It’s birds I love most. That’s why I fell for {i}her.{/i}"
    k "Uh-oh."
    t "Uh-oh."
    s "Uh-oh?"
    k "Should timing so poor not win some sort of award? Or perhaps a reward from the ward of the board?"
    t "Which board do you speak of? Because a gift’s already been prepared. And it will soon be delivered by a girl with red hair."
    k "The small one or the large one — who lives inside of me? "
    t "The one who comes from the sea."
    k "I see."
    s "Well, I don’t. And if you’re going to slander my daughter, I will lead you both to slaughter."
    s "She doesn’t come from the sea, she comes from the {i}seed.{/i} And that seed comes from me. Probably. Or at least that’s what I believe."
    t "Because that’s what you need?"
    k "Because that helps you breathe?"
    na "!!!!!"
    s "Let go of my sleeve!"

    scene clearnightsky
    with dissolve2

    k "Hahahahahahah!"
    t "Hahahahahahaha!"
    s "Hahahahahah!"

    "Such a wondrous night, this night full of wonder. Free of blunder and thunder, but the time’s come for slumber."
    "So I slurp down the soup and I’m hit by a car. A figurative one. Not the type that leaves scars. "
    "I stare up at the stars and I make my injuries known. Show three little girls that it’s time to go home."

    s "Tsuneyo."
    t "Ah."
    s "Weren’t we supposed to do something? Involving pillows, pajamas, and the pain of progression?"
    t "I believe that we may have planned some sort of session. "
    k "Then will both of you leave here before you’ve learned a new lesson? How to run before walking when you deal with depression?"
    s "I think we have to — for I hear the ocean calling. And if my days left are numbered, it’s not good to be stalling."
    na "............."
    s "Yay, she finally let go."
    k "She finally knows."
    t "Just look at her frown like a clown with no nose."
    k "A faker, a fraud. One who’s paid without laughter. One who shows up and takes and doesn’t look back after."
    s "She’s just like me."
    t "She’s just like you."
    k "She’s just like you."

    scene black
    with dissolve2

    "Once more I leave the ramen stand, somewhat earlier than planned. Then abandon it all as I walk through the sand."
    "Tsuneyo’s beside me, and we come to our senses at the same time. Our words no longer rhyme."

    play sound "static.mp3"
    scene clearnightsky with flash
    stop sound
    stop music fadeout 15.0

    s "..."
    t "..."
    s "Uhh-"
    t "{i}*Sniff*{/i}"
    s "What are you-"
    t "I know that scent. "
    s "Why are you sniffing me?"
    t "You smell like home. Why?"
    s "Your guess is as good as mine. I don’t even remember leaving the inn."
    t "Peculiar. Neither do I."
    t "Did we have sex again? Am I going to purge every instance of this from my mind? You must be very bad."
    s "We have never had sex, Tsuneyo. But we might have time to change that if- oh, fuck."
    t "Yes. Fuck, indeed."
    s "No, I mean we were supposed to be back in my room an hour ago. How the hell did we waste so much time out here?"
    t "Well, at least we have now confirmed it was not sexual in nature as you would not have lasted more than five minutes at most with a goddess like me."
    s "Let’s just...get back now and hope that no one’s pissed off at us."

    scene black
    with dissolve2

    t "I am fine with them being pissed off at you. I would like to remain loved by everyone, though. It may potentially increase the sales of my family’s business."
    s "I’m glad to see your priorities are as straight as always..."

    $ renpy.end_replay()
    $ beachsixtsuneyo2 = True
    $ tsuneyo_love += 1

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachsix6
