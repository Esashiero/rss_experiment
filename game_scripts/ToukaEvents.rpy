label toukastreets:
    if touka_love >= 0 and toukastreets1 == False:
        jump toukastreets1
    if touka_love >= 5 and ramen20 == True and convenience5 == True and toukadorm1 == True and toukastreets5 == False:
        jump toukastreets5
    if touka_love >= 15 and toukadorm10 == True and toukaspecial15 == False:
        jump toukaspecial15
    else:
        jump toukastreetsgen

label toukaarchery:
    if tsubasa_love >= 20 and tsubasaspecial15 == True and tsubasadate20 == False:
        jump tsubasadate20
    if touka_love >= 20 and tsubasaspecial20 == True and toukaarchery20 == False:
        jump toukaarchery20
    if chap4active == True:
        jump toukaspringarcherygen
    if chapthreeactive == True:
        jump toukasummer2archerygen

label toukastreetsgen:
    scene toukastreetsgen
    with dissolve
    play music "marshmallow.mp3"

    "I spend the morning walking around town with Touka, pointing out and explaining various things that she has never before seen."

    if bonus == True:
        "It's a bit like hanging out with a child, except this particular child is old enough to reproduce and push out an {i}actual{/i} child that will emerge with a silver spoon in hand."

    "But even though each and every one of her actions is tinged with a hint of naivete, there's an overwhelming feeling of her desire to learn and to understand."
    "To cultivate her knowledge of the outside world and grow into a human being that is both financially blessed and socially adored."
    "And while I still think it may be too soon to cite that desire as selflessness, I can't help but feel as if her good sides are forcing back her bad ones."
    "And that, one day, she will become everything she wants to be."

    scene black
    with dissolve

    "Or die in the process, because living isn't that easy."
    "I wonder what will happen?"

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label calltoukamorning:
    play sound "phonebeep.wav"

    "I tap on Touka's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    "There's no answer. I guess she's busy right now."
    jump callmorning

label calltoukaafternoon:
    if chap4active == True:
        jump toukaspringnoongen
    else:
        play sound "phonebeep.wav"

        "I tap on Touka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

label calltoukanight:
    play sound "phonebeep.wav"

    "I tap on Touka's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    "There's no answer. I guess she's busy right now."
    jump callnight

label toukastreets1:
    scene sky
    with dissolve
    play music "marshmallow.mp3"

    "I decide to mix things up for a change and start aimlessly walking around the city as soon as I wake up."
    "Now, I’m sure you’re thinking that aimlessly walking around is kind of just my thing. "
    "But the whole “mixing it up” part lies in the fact that I normally can’t do that until I’ve at least let the day’s misery sink in."
    "But here I am, on a surprisingly sunny morning in the middle of winter, successfully avoiding that exact misery."
    "And hey, I don’t even think I’ll wind up running into Yumi this time around since I’m pretty sure she’s incapable of waking up this early."
    "I have absolutely nothing to base that on other than that she’s just Yumi."
    "But I’m pretty sure that alone is enough."

    to "Accept my money, blasted peasant drink dispenser!"

    scene toukavending1
    with dissolve

    "Oh, it appears I’ve run into the exact opposite of Yumi."
    "Not so much in attitude since both of them seem to vehemently dislike me on at least a surface level-"
    "And also not so much in terms of adaptability or socializing with their peers..."
    "Actually, now that I think about it, Touka and Yumi might have more in common than they realize."
    "Just one of them is poor and one of them is rich. So yeah."
    "But despite being rich, Touka seems to be fighting with a “peasant drink dispenser” or, as you and I would call it, a vending machine."
    "I should probably call out to her and see what the issue is..."

    s "Having trouble there?"

    scene toukavending2
    with dissolve

    to "Back away, heathen! This is my battle!"
    s "Well okay then. See you later."

    scene toukavending3
    with dissolve

    to "Wait! Stay."
    to "I need your help and I did not realize it was you who was approaching."
    to "What are you doing out and about so early?"
    s "I’d ask you the same thing."
    s "Actually, why are you walking around in general? Don’t you have a chauffeur to bring you to...random vending machines or whatever?"

    scene toukavending4
    with dissolve

    to "I do...but in an attempt to become one with society, Mother has asked that I explore the area and attempt to blend in."
    s "Well you’re doing a great job by yelling at a large appliance. Keep it up."

    scene toukavending5
    with dissolve

    to "How do I make it like my money?! It seems fundamentally simple, but it’s actually very confusing!"
    s "It’s really not. It’s probably just a bad bill or-"

    "Wait."
    "Touka is extremely out of touch with modern society."
    "This obviously means that I must take advantage of her."

    s "Did you say the chant?"

    scene toukavending6
    with dissolve

    to "I’m sorry, the what?"
    s "The chant. "
    s "These vending machines are voice activated and you need to talk to them or they won’t accept your money."
    to "Voice activated? But they look so outdated compared to the high-tech ones we have in our game room."
    s "I guess they’re a little- wait, you have vending machines in your house?"
    to "There are machines at the dorm as well. Are they not a standard appliance in commoner households?"
    s "They-"

    scene toukavending7
    with dissolve

    to "Wait! Before you answer that, please teach me the chant!"
    to "This is the furthest I’ve walked since my family's last vacation to Kyoto and I am beginning to become dehydrated!"
    s "Hmm...I wonder how it went again."
    s "Perhaps there’s something that could jog my memory."

    scene toukavending8
    with dissolve

    to "Are you...attempting to have me bribe you?"
    to "I may be extremely well off, but even I’m not willing to just hand out money if that’s what you’re implying."
    s "I also accept personal favors."

    scene toukavending2
    with dissolve

    to "Just tell me the chant, Sensei!"
    s "Fine, fine."
    s "First, you need to raise your right hand in the air as if you’re about to cast a spell on the machine."

    scene toukavending6
    with dissolve

    to "There is a visual element to this as well?"
    s "Yeah. These machines also double as security cameras, so they can see everything you do."
    to "How utterly terrifying. But I suppose if that is what must be done..."

    "I don’t know if I’m more impressed by Touka’s gullibility or my own ability to come up with such a fluid lie without even thinking."
    "Either way, this is awesome."

    scene toukavending9
    with dissolve

    to "Okay! I am now in position!"
    to "Will this do?"
    s "Yup. Perfect. "
    s "Now all you need to do is politely ask the machine to accept your money."
    s "If you want, you can just repeat after me."
    to "If you’d be so inclined, I would very much appreciate it."
    s "Then-"
    s "Hear my call, peasant drink dispenser."
    to "Hear my call, peasant drink dispenser!"
    s "I, Touma Tsukiyama of the Tsukiyama family-"
    to "I, {b}Touka Tsukioka{/b} of the Tsukioka family-"
    s "Ask for nourishment-"
    to "Ask for nourishment-"

    if bonus == True:
        s "And surrender my rights and my body to the man beside me."
        to "And surrender my-"
    else:
        s "And promise to call my teacher every night before he goes to sleep and tell him he is a good boy."
        to "And promise to-"

    scene toukavending10
    with hpunch

    to "WHAT DO YOU THINK YOU’RE MAKING ME SAY?!"

    "So close."

    scene toukavending11
    with dissolve

    to "Mmm..."
    s "Wait, are you crying?"
    to "I trusted you and you took advantage of me."
    s "I was just messing with you. There’s no reason to cry."
    s "Here, give me the money."

    scene toukavending12
    with hpunch

    to "AND NOW I AM BEING ROBBED! "
    to "MOTHER! HELP!"
    s "I’m not robbing you...I just want to see if there’s a problem with your money."

    scene toukavending13
    with dissolve

    to "Do you promise not to take it and run away?"
    to "On most days, my above average athletic ability would allow me to catch up with you, but my dehydration has made me very weak and I do not think I would be able to today."
    s "I’m not going to run away with one bill. I am not that poor, Touka."
    s "Also, what would it even matter if I did? You’re made of money."
    to "It’s the principle of it. I refuse to fail even during times like this. Tsukiokas always come out on top."
    s "Just give me the note, Touka."

    scene toukavending12
    with dissolve

    to "Fine! But only because you used the right name this time!"

    scene toukavending14
    with dissolve

    "Touka hands me the note she’s trying to use and, just as I suspected, it’s in too bad of shape for the machine to take it."
    "It’s actually so bad that I’m a little surprised someone of her status would even be carrying it."

    to "Is my money broken?"
    s "Where did you get this?"
    to "The tiny, yet surprisingly endowed girl in our class gave it to me when I bumped into her and asked her where I could purchase a drink just moments ago."
    s "Uta? I mean, it makes sense that her money would be in this condition, but why not just use your own?"
    to "I left my coin purse in my room out of fear that I may be attacked during my first ever walk among “the people.”"
    s "Why even leave your room if you’re so afraid of things like that?"

    scene toukavending15
    with dissolve

    to "The constant pressure to blend in and the strive for both your and my mother’s approval as a normal girl!"
    s "Wow. That was a surprisingly honest answer."

    scene toukavending16
    with dissolve

    to "I utterly despise lying and found no reason to in this situation."
    to "Just tell me my money is expired and I will be on my way. "
    s "..."
    to "..."
    s "{i}Hah...{/i}"
    s "Move over."

    scene toukavending17
    with dissolve

    to "I beg your pardon? Why should I have to give up my spot when I arrived first and-"

    scene black
    with dissolve

    to "Hey! What do you think you’re doing!"
    to "Help! I am being attacked!"

    "I move Touka aside and slip some of the coins in my pocket into the machine."

    s "What do you want?"
    to "Wait...are you-"
    to "..."
    to "Just a water is-"
    s "Green tea? Got it."
    to "Why even ask me if you’re just going to do whatever you please?!"

    "........."
    "......"
    "..."

    scene toukavending18
    with dissolve

    s "..."
    to "{i}Sip...{/i}"
    s "This is normally the part where you say “Thank you.”"
    to "..."
    to "{i}Sip...{/i}"
    s "Well fuck you then."

    scene toukavending19
    with dissolve

    to "Oh, stop. There’s no need for such hostility. I’m extremely thankful."
    to "I just believed that there may have been some sort of ulterior motive for a moment, so I was protecting myself."
    to "Without you, I would be significantly less hydrated. You have affected me greatly."
    to "Even if you directly ignored my plea for water in place of this...boxed tea beverage."
    s "Have you never had boxed tea before?"

    scene toukavending20
    with dissolve

    to "I have not. Our family has a tea master who lives at the manor, and he would abhor the idea of me drinking something like this."
    to "It is not nearly as bad as it looks, though. So I would like to thank you once more for making a choice that only appeared bad at first."
    s "You’re...welcome?"

    scene toukavending21
    with dissolve

    to "I...would not reject the idea of you coming to the manor to experience a proper tea ceremony, if that would at all repay you for your graciousness today."
    s "Well thank you for not rejecting it."
    s "That’s not really an invitation, though."
    to "R-Right! It is not."
    s "..."
    to "..."
    s "..."
    to "..."

    scene toukavending22
    with dissolve

    to "{i}Sip...{/i}"
    s "You feel pretty awkward right now, don’t you?"

    scene toukavending23
    with dissolve

    to "Do you not?"
    to "I’ve received plenty of private lessons from teachers in the past, but I have never sat with any of them so casually in public."
    to "Being seen out here makes me feel as if I’m...exposed. And having a...man beside me-"
    to "It feels rather immoral, does it not?"
    s "Not really. I spend most of my days surrounded by [teenage]girls, so I’m pretty used to it."
    to "Yes, but that’s on[school] grounds. It’s entirely different."
    s "Not always. You’ve literally seen me at the dojo with Ayane before."

    scene toukavending24
    with dissolve

    if bonus == True:
        to "Well...yes! But after hearing the things she has said about her...feelings for you, I have come to terms with your relationship being...different."
    else:
        to "Well...yes! But...she appears to like you as more than just a sparring partner..."

    s "..."
    s "I don’t know what she told you, but you’d probably be better off not believing it."

    scene toukavending25
    with dissolve

    to "I will do just that, but...it does not exactly remedy my discomfort."
    to "I realize that I’m likely just being reserved based on my own personal experiences and stigmas, but I can not exactly help it just yet."
    to "With your help, though...I can see myself getting at least partially better."
    s "I wouldn’t count on me too much. "
    s "Just keep being a weird rich girl and I’ll probably keep bumping into you out of a mix of coincidence and curiosity."

    scene toukavending26
    with dissolve

    to "Forgive me if I am misunderstanding, but the latter half of that made it sound as if you are interested in me."
    s "I am. "

    scene toukavending27
    with dissolve

    to "You are?"
    s "Sure. "
    s "You’re weird. It’s funny."
    to "I’m...funny?"
    s "That’s not exactly what I said, but okay. "
    to "I...I see."
    to "Well then...if we happen to bump into each other again on our respective morning walks...I wouldn’t mind doing more things like this."
    to "Since we are both curious about each others’ lifestyles, of course. Not because we’re interested in each other as {i}people{/i}."
    s "I don’t really need to know much about your lifestyle, but I wouldn’t mind showing you a little more about how “commoners” live."
    s "You should be aware that I’m probably going to mess with you a lot, though."

    scene toukavending28
    with dissolve

    to "Why?! What have I done to deserve this?!"
    s "Nothing in particular, but that’s just how things are going to be for a while."
    s "I show you the ropes. You say something unintentionally funny. I tease you about it."
    s "Everyone wins."
    to "This really doesn’t sound like an ideal student-teacher relationship to me..."
    s "The “ideal” part comes later. We’re still in the beginning phase."

    scene toukavending29
    with dissolve

    to "So...you are only acting this way toward me for the time being and will eventually become more of a traditional role model? "
    s "Sure. That’s one way to put it."

    "An incredibly wrong way to put it, but still one way."

    to "I see. So this would be what you would call a...trial period?"
    s "Call it whatever makes you comfortable. "

    scene toukavending30
    with dissolve

    to "A trial period it is, then..."
    to "Though, I have a lot more to learn than just figuring out how to operate various drink machines."
    to "So, if you’re willing to continue guiding me when it is convenient for you to do so...I’d be inclined to accept."
    to "I can’t say I’ll be particularly {i}happy{/i} about it since your methods are still rather confusing to me..."
    to "But I suppose that nothing has gotten {i}dramatically{/i} worse since I’ve started learning under you just yet."
    s "I’m sure it will. That’s normally how things go."
    s "But life without problems is no life at all."

    scene toukavending31
    with dissolve

    to "I suppose that much I’d have to agree with."
    to "The true hardships have yet to come. And I must be prepared for them when they do."
    to "Right now, I’m nothing more than a girl with a fortunate background. A background I must learn to live up to."
    to "And to do that...I require your assistance."

    scene toukavending32
    with dissolve

    to "Not right now, though, since I have plans with my mother and my sister to play shuffleboard on the yacht this afternoon."
    s "I don’t think that’s really something I can assist with, so that’s fair."
    s "I should probably be heading out anyway. I didn’t really expect to spend the entire morning re-educating a princess."

    scene toukavending33
    with dissolve

    to "Would it be too much to ask for you to not call me that?..."
    to "That word bothers me even more than your compulsion to keep addressing me by different names."
    s "Uhh...sure. I didn’t really mean it as an insult."
    to "Well, thank you for understanding then..."

    scene black
    with dissolve2

    "I get off the bench and move away from Touka."
    "I turn back after a few seconds to see if she’s leaving as well, but she remains still-"
    "Sipping on her box of peasant liquid (Which I’m sure is what she’s calling it in her head) and staring off into the distance..."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukastreets1 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label toukastreets5:
    scene toukaolddis1
    with dissolve
    play music "wewereangels.mp3"

    "I make my way over to the same area between my house and the[school] where I last found Touka battling a vending machine."
    "Today, there is no battle. Just a girl standing in the middle of the sidewalk, curiously surveilling her surroundings and probably assigning new rich-person names to everyday commoner objects."
    "Or...trying to figure out how they work and-"
    "I don’t know. But she’s clearly confused to some extent because why else would anyone just stand around in the middle of a mild snowstorm?"
    "I make my way over soon after spotting her, letting the crunch of the ground beneath my feet signal my arrival."

    scene toukaolddis2
    with dissolve

    to "Oh, Sensei. Good morning."
    to "If you had not shown up soon, I would have continued exploring on my own. Needless to say, I am very happy you did."
    s "So you {i}weren’t{/i} just standing around trying to figure out how commoner objects work? You were waiting for me?"

    scene toukaolddis3
    with dissolve

    to "I may be inexperienced, but I am not an imbecile. I know how all of these things function."
    s "So it’s just vending machines you have a problem with, then?"

    scene toukaolddis4
    with dissolve

    to "In my defense, I do have experience with those types of machines. I had just never encountered one that wouldn’t accept my money before..."
    to "Let alone a voice activated one with an added visual element. But at least it is making the streets of Kumon-mi a safer place."

    "Wait, does she still think I wasn’t joking about that part?"
    "Please let me be around whenever she tries to use one again."

    scene toukaolddis5
    with dissolve

    to "So, can I assume that you are here to work as my guide and that you are not simply passing by?"
    s "Just passing by, actually. See you later."
    to "Ha ha ha. That was a rhetorical question, Sensei. I know you are here to see me. "
    to "You do not need to be embarrassed."
    to "I’m sure that being out and about with me may make you look significantly worse by comparison, but there is barely anyone outside today."
    s "Yeah, that tends to happen when it snows. This area is a lot busier in the summer."
    s "Also, being seen with you will not make me look worse. "
    s "If anything, since most of the people out here are just like me, they’d probably just think {i}you{/i} look nice and not think anything of me at all."
    to "I don’t see how that invalidates any of what I said, but as long as you will still be my tour guide, I can look past it."
    to "So, where would you have me go today?"
    s "Oh, it’s up to me?"

    scene toukaolddis2
    with dissolve

    to "Well...yes."
    to "I know absolutely nothing about this area and you seem to know quite a bit."
    to "Should I be researching places I would like to go and informing you of them beforehand? "
    to "I really don’t know the best way to approach things like this, nor where I should start for the authentic commoner experience."
    s "Weren’t you supposed to stop using that word?"

    scene toukaolddis6
    with dissolve

    to "Yes, but...{i}lower middle class{/i} is so much harder to say. And it does not seem like you mind very much."
    s "I don’t, really. Especially since I’ve called you a spoiled rich girl on several occasions now. "

    scene toukaolddis7
    with dissolve

    to "Spoiled?! Me?!"
    s "...Yes."

    scene toukaolddis8
    with dissolve

    to "Yes, I suppose that {i}is{/i} right now that I think about it."
    to "I apologize for my reaction. I’m just not used to being so accurately insulted. "

    scene toukaolddis5
    with dissolve

    to "But, that all ends today! Because I am going on a wholesome adventure with my teacher who is going to be very patient and encouraging with me!"
    s "Patient, maybe. Encouraging, probably not."
    to "Oh, stop. What could possibly go wrong? "
    to "I’m sure that wherever you take me will be somewhere I can ease into and experience at my own pace."
    to "Only a {i}truly{/i} horrible man would toss me into the deep end. And you are only partially horrible based on what I’ve seen thus far."
    s "..."
    to "..."

    scene black
    with dissolve

    s "You know, I think I've got just the place. "
    s "It’s kind of a long walk, though."
    to "That’s fine! I’ve packed plenty of snacks and beverages for the two of us and slept surprisingly well last night!"
    s "What if I didn’t show up today?"
    to "Well...I suppose I would have had to find something else to do with all of the items I brought."
    to "Regardless! I am refreshed and raring to go! "
    to "Lead the way, Sensei! I’m sure you will take me somewhere nice!"
    s "Yeah..."
    s "We’ll see about that."

    scene wintersky
    with dissolve

    "Now, “nice” is a subjective term a lot of the time."
    "There are things certain people find interesting or endearing that others can’t seem to grasp even after prolonged exposure or being forced to consume or experience them."
    "Basically, there are things that you can “train” yourself to like."
    "And right now, essentially everything Touka can and will experience falls into that exact boat."
    "Of course she’d never view any of what us “normal people” see as nice when she’s been conditioned to accept nothing less than the best of what life has to offer."
    "So, with that in mind, the best course of action right now isn’t to slowly ease her into the life that everyone else leads."
    "It’s to do exactly as she {i}doesn’t{/i} want me to do and toss her into the deep end."
    "But that’s okay, because I’m sure her exceedingly rich family has paid for years worth of swimming lessons."
    "And I’m sure that if they didn’t and she winds up drowning, they’ll throw a lavish funeral to celebrate her depressingly short life."
    "Either way, I know where I’m taking her."
    "And it’s somewhere that no amount of snacks or beverages can possibly prepare her for."
    "........."
    "......"
    "..."

    scene toukaolddis9
    with dissolve2

    to "..."
    s "..."
    to "Where...are we?..."
    s "This is the second half of town. Or the old district, if you’d rather call it that instead."
    to "Is this...some sort of theme park? What am I looking at here?"
    s "Not a theme park. Just a low income area where people even worse off than me live."
    s "I figured it might help to show you the polar opposite of your life rather than something boring like a bowling alley or an ice skating rink."

    scene toukaolddis10
    with dissolve

    to "I love ice skating, actually. Would you like to accompany me some day?"
    s "Not particularly. "
    to "How sad. "

    scene toukaolddis11
    with dissolve

    to "This place, though..."
    to "You said that people...{i}live{/i} here?"
    s "{i}Die{/i} here is probably more accurate."
    s "Most of the people in the old district are either...well, {i}old{/i} or homeless. Or a mixture of both of those two things."
    s "But that doesn’t mean there aren’t outliers."

    scene toukaolddis12
    with dissolve

    to "You don’t mean to tell me that there are students in our[school] who call a place like this home, do you?"
    s "There are a few in our class, actually."
    s "Tsuneyo...Chika...That one girl you find more intimidating than me who I can’t remember the name of."

    scene toukaolddis13
    with dissolve

    to "I...suppose I do see how someone like Yumi could live here. She needed to learn her...intimidation tactics somewhere."
    to "But you say that Chika lives here as well? The one who my mother is familiar with?"
    s "Yeah. Her and Yumi live in an apartment over here together."
    s "They’re taking care of a little girl with an immunodeficiency disorder as well. "
    s "It’s pretty impressive, to tell you the truth."

    scene toukaolddis14
    with dissolve

    to "This isn’t another one of your pranks, is it?"
    to "Because I can be depressingly compassionate at times, and it would be very mean for you to make me feel bad about things that simply aren’t true."
    s "It’s true. I’d take you there, but Chika doesn’t let just anyone near her sister since it could get her sick."

    scene toukaolddis15
    with dissolve

    to "I see..."
    to "So she really does live here after all. "
    s "You're not crying again, are you?"
    to "I am. But can I truly be blamed for that? "
    to "This news comes as a bit of a shock to me, Sensei."
    to "My initial reaction was asking if this place was a theme park. "
    to "I didn’t think for a moment that there were people, let alone ones as kind as that girl, {i}living{/i} in a place like this."

    scene toukaolddis16
    with dissolve

    to "And taking care of a sick little girl as well..."
    s "..."
    s "I guess taking you here was a bad idea after all, huh?"
    to "No. In fact, hiding this from me would have made me feel even worse. "
    to "At least now I can try to wrap my head around how things could have possibly gotten to this point."
    to "We’ve only been here for several minutes and I already can’t fathom the idea of calling this area “home.”"

    scene toukaolddis17
    with dissolve

    to "There are people slumped up against walls...tucked into alleyways and trying to keep themselves warm."
    to "It’s snowing, Sensei. They’re going to get sick. Perhaps even worse."
    s "Probably. But that’s just the hand these people were dealt."
    s "We’re lucky to be where we are with that in mind."
    to "Lucky is an absolute understatement. This is abhorrent and I will not stand for it."

    scene toukaolddis18
    with dissolve

    to "Excuse me! Can you tell me your name?"

    "Touka wanders away from me for a moment and crouches down beside an old man half-asleep near the side of a rundown house."
    "I can’t make out the look on his face from where I stand, but I notice a distinct lack of teeth as he opens his mouth to try and respond to Touka."
    "She proceeds to reach into her bag and pull out a handful of snacks for the man, placing them neatly beside him."
    "His eyes light up and, for a brief moment in time, things are less horrible."

    to "Hi there...My name is Touka."
    to "Are you cold?"
    om "..."
    to "You poor thing..."
    to "You can’t even talk, can you?"
    to "I don’t have much on me at the moment, but please take all of this. You need it much more than I do."
    om "..."
    to "Don’t worry about thanking me. Just eat and try to stay warm, okay? The snow will only last so-"

    stop music
    play sound "static.mp3"
    scene ayhh2 with flash
    scene ayhh4 with flash
    scene ayhh10 with flash
    scene ayhh7 with flash
    scene ayhh8 with flash
    scene toukaolddis19 with flash
    stop sound
    play music "noriko.mp3"

    "73 75 64 64 65 6e"

    n "Uhhhhhh..."
    to "Sensei, what is this place?"
    n "Before that, what is this pairing?"
    n "Since when do the two of you hang out outside of[school]?"

    scene toukaolddis20
    with dissolve

    to "Uhh...let’s see...Noriko, correct?"
    n "Yeah..."
    n "And you’re Touka, right?"
    to "Right! Though our teacher seems to forget that rather frequently."
    to "Sensei was just giving me a tour of the old district as it is my first time here."
    to "Then he suggested something about wanting to come here, but was so taken aback by my generosity moments before that he has been mostly speechless ever since."

    scene toukaolddis21
    with dissolve

    to "Is this a...shop of some sorts?"
    to "Do you mind if I take a quick look around? There are so many interesting things here."
    n "Uhh, yeah. Go ahead."
    to "Splendid!"

    scene toukaolddis22
    with dissolve

    "Touka begins to look around the store and I find myself slightly confused and standing at the counter with Noriko."

    scene toukaolddis23
    with dissolve

    n "Hey...are you okay? You seem kind of out of it right now."
    s "I...think so?"
    s "I remember walking around with Touka, but I don’t really remember anything about coming over here."
    n "Hmm..."

    scene toukaolddis24
    with dissolve

    n "Maybe you just realized that a trip to the old district without coming to see me is no trip at all?!"
    s "Sure, let’s go with that."
    s "Since when do you work mornings, though?"

    scene toukaolddis25
    with dissolve

    n "I don’t really have a set schedule. I just kinda work whenever I want to work and stuff."
    n "Today just happens to be one of those days."
    n "Is it my turn to ask a question now?"
    s "I mean, you’re going to ask it anyway, so sure."
    n "Why are you showing her around the old district?"
    n "I get that you like to hang out with everybody and stuff, but...it seems like kind of a weird place to take {i}her{/i} of all people."
    s "That’s exactly why I brought her here."
    s "She’s been having trouble getting accustomed to the life of a middle class citizen and-"
    to "Sensei! What are these?!"
    s "Hold on one second, Noriko."

    scene toukaolddis26
    with fade

    s "Touka, what-"
    to "Are these candy?! Can we buy some?!"

    if bonus == True:
        n "{i}Oooooooooooooooooooh my god.{/i}"
        s "..."
        to "I’m not normally allowed to eat candy on account of what it can do to my body, but today is a special occasion and-"
        s "Touka, I’m going to need you to listen very carefully for a moment."

        scene toukaolddis27
        with dissolve

        to "Listen to what? Did I do something wrong?"
        to "This isn’t actually a museum, is it? There were price tags, so I assumed I could purchase the items on display and-"
        s "Those are condoms."
        to "Condoms?"
        s "Not candy."
        to "Not candy?"
        s "..."
        to "..."

        play sound "entrybell.mp3"

        n "Welcome in!"
        s "You can’t eat condoms, Touka."
        to "..."
        cust "..."

        play sound "entrybell.mp3"

        n "Bye! Please come again!"

        scene toukaolddis28
        with dissolve

        to "Hmm...condoms..."
        to "I feel as if I’ve heard that word before. But what did it mean again?"
        s "I’m sure your mother or...manor staff must have taught you sexual education, right?"
        to "Yes, but what would-"
    else:
        s "Yes."

    scene toukaolddis29
    with hpunch

    to "Ah!"

    if bonus == True:
        s "You remembered?"

        scene toukaolddis30
        with dissolve

        to "I remembered."
        to "This is extremely embarrassing."
        s "Just think of how it would be if you tried to eat them."
        to "I have sullied your good name by acting so inappropriately in public."
        to "And after you took the time out of your day to show me a true middle class...sex shop?"
        s "Convenience store. They just sell condoms because it’s...convenient, I guess."
        s "But you can also buy snacks and drinks here as well."
        to "Doesn’t it make people feel strange buying food and beverages from a store that sells contraceptives?"
        s "Surprisingly, no."
        to "I see."
        s "..."
        to "..."
    else:
        s "Touka?"
        to "I got so excited about buying the candy that I appear to have dropped it."
        n "You must pay for that! I demand it!"

    s "Are you ready to leave now?"
    to "Yes. I believe I am."

    scene black
    with dissolve2

    if bonus == False:
        n "Come back here, candy destroyers!"

    "Touka and I say goodbye to Noriko without purchasing anything."
    "She proceeds to confusedly wave at us as we depart the store and I receive a flurry of text messages moments later with nothing but question marks."
    "Not knowing how to reply, I slide my phone back into my pocket and slowly escort the richest girl in Kumon-mi back to the safer part of town."
    "I got to see a different side of her today, though."
    "And a side that, while overwhelmingly naive, is still endearing."
    "I just hope she doesn’t wind up trying to get too involved in things she doesn’t understand."
    "I may have taken her there today, but I don’t think a place like that is really fit for a girl like Touka."
    "Eventually, we wind up back near the vending machines where this all started and go our separate ways."
    "Instead of just standing around staring during today’s separation, though, I can hear Touka softly humming something to herself as she gleefully skips away."

    $ renpy.end_replay()
    $ toukastreets5 = True
    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label toukadorm10:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Touka’s door and wait for her to answer. "
    "Immediately upon knocking, however, I am graced by the suspicious sound of laughter."
    "Now, laughter on its own isn’t really something I’d ever call suspicious."
    "But I want to remind you exactly where I am right now, and exactly who it is that resides behind this door."
    "Could it be that Touka and Yasu’s friendship has finally reached a point where they both understand {i}and{/i} leisurely banter with one another?"
    "Is Yasu even capable of such a thing?"
    "Or...is this occasion truly a suspicious one after all?"

    s "..."

    "Seeing as there is no answer, I take it upon myself to enter anyway as this is a matter I must investigate to ensure the safety of both my students and myself."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I’m sure I’m probably just overcomplicating things by thinking something is afoot here, but that sort of thing happens all the time when I’m standing outside of doors."
    "It’s just a habit, I guess- envisioning what’s on the other side."
    "What could go wrong."
    "What could go right."

    scene toukahair1
    with dissolve2

    "But, on most occasions, definitely wrong."

    tb "Oh my. Could it be that you’ve wandered into the incorrect room, Sensei?"
    to "Yes. {i}Could it be that you’ve wandered into the incorrect room, Sensei?{/i}"
    ya "Touka, that hurts."
    to "Shut up and deal with the pain, Yasu. It wouldn’t hurt so much if you would actually brush your hair every once in a while. "
    ya "Okay, Touka. I will do as you say as long as it means I can have beautiful hair like yours one day."
    to "I suppose there is no harm in dreaming. "
    s "Hey, Tsubasa. I didn’t realize you were going to be here."
    tb "The same goes for me. I didn’t believe you were even permitted to enter the girls’ dormitories. But I suppose I’m not very well acquainted with the rules of public schools, so I’m likely wrong."
    s "To be fair, I’m not very well versed in them either and I work for one."

    scene toukahair2
    with dissolve

    to "W-What Sensei means to say is that he’s been coming on occasion to...assist with my studies! "
    tb "Does this have something to do with his inquiry about your bed at the Christmas gathering?"
    to "I’m sure it-"

    scene toukahair3
    with dissolve

    to "Wait, you asked my mother about the bed?! Why?!"
    to "I already informed you that it’s a standard bed with rapid sleep capabilities! What else do you need to know?!"
    tb "I advised him of the same. But now, I’m suddenly intrigued by his need to come all the way over here to aid with your studies. "
    tb "Which subjects is Touka struggling with, exactly?"
    s "Uhh..."

    menu:
        "Physical Education":
            s "She’s been really struggling when it comes to gym class. She just can’t seem to keep up with the other girls."

            scene toukahair4
            with dissolve

            to "Okay, {i}that{/i} is entirely untrue! I would never struggle keeping up with any of the girls in our class!"
            to "Save the small one with the auburn hair, but I’m beginning to believe she may have been raised by wolves. She moves far too quickly for a [young]girl."

            "Is {i}that{/i} why Miku never brings up her past?"
            "Also, this entire scenario is untrue and I don’t know why this particular addition to it is what’s setting Touka off."

            tb "You are...tutoring my daughter in physical education?"
            s "I am."
            to "You’re not! Tell her it’s for...English!"
            s "I am here to teach your daughter about physical education and biology."

            scene toukahair5
            with dissolve

            to "Ugh. Why do I even bother?"
            tb "I was unaware she was struggling. Touka has always seemed very athletic to me, but I suppose I haven’t paid much attention to those outside of our bubble. "
            tb "Is that really something you can tutor her in {i}here,{/i} though? You don’t require some sort of...gymnasium?"

        "Economics":
            s "Touka doesn’t seem to grasp the basic concepts of economics- likely due to her inexposure to the middle class or the true value of money."

            scene toukahair4
            with dissolve

            to "Wha- no! That’s not true at all!"
            to "Even if I lack the same sort of {i}exposure{/i} as the other girls, I completely understand and appreciate the value of money! Probably even more than most!"
            to "As the heir to the Tsukioka family business, it is absolutely essential that I understand something as {i}basic{/i} as economics."
            s "You bought a one million yen painting for Makoto on Christmas."

            scene toukahair6
            with dissolve

            tb "That’s it? I told you it was okay to spend a little more."
            to "Did I go under budget? I will admit that seeing the limit written in USD did confuse me a bit, so I apologize if that is what happened."
            to "In my defense, however, conversion rates are not exactly reliable or even relevant at the moment due to Kumon-mi’s isolation from the rest of the world."
            s "You weren’t under budget. You spent more on that present than Makoto has probably ever even seen before."
            to "Oh."
            to "Well, how is that bad?"
            s "It’s bad because it just shows how little you know about money. "
            tb "Darling, I had no idea this was such an issue for you. Perhaps we should ask your father to hold off on transitioning until you’re more comfortable with-"

        "Animal Husbandry":
            s "Touka has been having a really tough time with our animal husbandry course."

            scene toukahair6
            with dissolve

            tb "Is that true, dear?"
            tb "You’ve always been so good with the horses. I assumed animal husbandry would be a walk in the park for you."
            to "I...was unaware we even had an animal husbandry course."
            s "See what I mean? This is how far behind she is."

            scene toukahair7
            with dissolve

            tb "Well, that won’t do at all. Everyone knows how important and essential animal husbandry is to the average, everyday Japanese citizen."
            s "Yup. That is definitely a thing everyone knows."
            s "But, you know- if Touka would just stop strangling all of the kittens we bring in for educational purposes, I wouldn’t have to go out of my way and come here to teach her more about proper husbandry."

            scene toukahair8
            with dissolve

            tb "Touka! You’ve been strangling defenseless kittens?!"
            to "Absolutely not! And, just as I assumed, we don’t have an animal husbandry class at all!"
            to "Probably!"
            to "At the very least, there have not been any kittens!"

            scene toukahair9
            with dissolve

            tb "Oh dear. Then who is it that’s been strangling them? "
            tb "We have to find out before it’s too late."
            tb "But I suppose I shouldn’t get in the way of your husbandry class so Touka can be prepared for when-"

    scene toukahair10
    with dissolve

    to "Mother, no. He is here to tutor me in English."
    to "{i}Like he always does at this time on this specific day of the week.{/i}"
    ya "I have never seen Sensei-"
    to "{i}Like he always does at this time on this specific day of the week.{/i}"
    ya "..."
    tb "Touka, you know I’m fluent in English, don’t you? Why haven’t you asked me for assistance?"
    tb "The entire kitchen staff can speak it as well. It’s becoming an essential language."
    to "The kitchen staff changes monthly, mother. They are not a reliable source of information."
    tb "Yes, I agree. I don’t know where your sister picked up that hobby, but your father really needs to do something about it."

    scene toukahair11
    with dissolve

    to "R-Regardless! Sensei is {i}definitely{/i} here to teach me, seeing as there is no other reason for him to ever come to this room!"
    tb "Well, let me say now that I admire his dedication."
    tb "It takes a special type of person to do something like this out of the kindness of his heart."
    s "What can I say? I’m a pretty great guy."
    tb "And here I was beginning to think that you hadn’t been taking my daughter’s education seriously."
    to "Oh, {i}what a shame that would be.{/i}"

    scene black
    with dissolve2

    "Touka finishes messing around with Yasu’s hair and sends her back over to her side of the room, where she takes a seat and begins staring at the wall in typical Yasu fashion."
    "Tsubasa proceeds to down the rest of her wine in one gulp without so much as batting an eye- a skill I believe she may have acquired after years of dealing with her youngest daughter."
    "She then gestures for me to take a seat on the completely normal bed between her and Touka- who suddenly appears very exhausted for some unknown reason that definitely doesn’t have to do with me."

    scene toukahair12
    with dissolve2

    to "Hah..."
    tb "Oh, darling. Needing a little extra help when it comes to your education is nothing to be ashamed about."
    tb "Just blame it on your upbringing. It is both accurate {i}and{/i} a reasonable excuse when it comes to explaining your perceived inadequacies."
    to "I am not ashamed, Mother. I just wish I had {i}remembered my lessons were going to be tonight{/i}."
    to "Because not only does this interrupt the rare chance for the two of us to spend time together, I look...entirely unprepared to learn."

    scene toukahair13
    with dissolve

    tb "Oh my- you’re right. How incredibly informal of us."
    tb "If I had known you were going to come tonight, I would have postponed our monthly slumber party."
    s "And if I had known this was something you two had been planning, I would have rescheduled Touka’s totally-legitimate English tutoring session."
    to "My, what a lovely offer. I do suppose we’ll take you up on that. Right now."
    tb "Oh, don’t be silly, Touka. As much as I care about our relationship, I also care about you becoming the best person you can be."
    tb "And that person just happens to be fluent in English the same way her mother is."

    scene toukahair14
    with dissolve

    to "Hah..."
    s "..."

    "Touka shoots me a glance that I can immediately tell means that I’m going to owe her a favor in the future, but I guess that’s fine."
    "I’m sure that a large part of why she’s helping disguise one of my many casual visits to her dorm room is to just make {i}herself{/i} look good-"
    "But, as a self-centered man who is also made to look good in the process, I can’t help but thank her for that."
    "Being indebted to someone isn’t exactly a thing I like, though."
    "So if I can prevent having her attempt to cash in her hook on me before she has an actual opportunity to, I probably should."

    s "We can have our totally legitimate tutoring session another time, Touka. It’s fine."

    scene toukahair15
    with dissolve

    to "Pardon my asking, but...what exactly is the catch?"
    s "No catch. Just don’t want to get in the way of something that’s important to you."
    to "Okay, but..."
    to "What is the catch?"
    s "Am I not allowed to do nice things?"
    to "Not really, no. Or at least you don’t seem to possess the capability to actually enact any without something in return."
    tb "Touka, that is no way to speak to your teacher."
    to "Apologies, Mother."

    scene toukahair16
    with dissolve

    tb "Thank you very much for offering to do that, Sensei. My daughter and I don’t get to spend as much time together as either one of us would like."
    tb "Well, {i}this{/i} daughter. My other daughter and I spend almost {i}too{/i} much time together. But she is a...special case."
    s "Why not spend more than one night per month together if that’s the case? I can’t imagine that’s really enough."
    s "Especially with Yasu...existing."
    tb "I quite like Touka’s roommate actually. Her reaction to seeing the manor for the first time was adorable."

    scene toukahair17
    with dissolve

    s "Why has Yasu gotten to see your house but I haven’t?"
    to "Because I don’t believe you’d be able to conduct yourself appropriately if you were to come."
    s "..."
    s "But you think Yasu-"
    to "I said what I said, Sensei."
    to "The fact of the matter is, Mother and I {i}can’t{/i} spend more time together. We’re far too busy for that sort of thing."
    s "Are you? Because all you have is school and Tsubasa has been just...I don’t know. Watching your sister, maybe?"

    scene toukahair18
    with dissolve

    tb "Oh, I do much more than that."
    tb "I spend most of my time overseeing the Tsukioka Foundation's hospitality and real estate branches."
    tb "I’m sure it sounds boring to you, but I’m actually quite good at it."
    s "I don’t think I’ll ever understand how your family transitioned from bubble wrap to basically owning the city."
    tb "Yes, well...the last few years have certainly been very kind to us."
    to "When I was younger, Mother and I had much more time to spend together. But with the family becoming a more prominent figure in the city, it’s just not possible anymore."

    scene toukahair19
    with dissolve

    tb "Ahh, how lovely it would be to go back, though."
    tb "All of those summers spent at our vacation homes...the laughs we shared...the joyous ruckus caused by an expensive band of animatronic animals..."
    s "..."
    s "The what?"
    to "Maybe this summer will be a little different, though?"
    to "Perhaps the small break in the school year would give me the time to see how you handle your end of the family business, Mother?"

    "If there {i}is{/i} a break, that is."
    "If I remember correctly, there was a small one for Christmas just before our first party...but I have no idea how summer vacation works or...if that’s even a thing we get."

    scene toukahair20
    with dissolve

    tb "I think that sounds wonderful, dear. But don’t you think your time might be better used experiencing a {i}real{/i} summer vacation for the first time?"
    tb "You finally have the opportunity to do so- and it’s one that neither your father nor myself ever had. I wouldn’t risk losing that if I were in your position."

    scene toukahair21
    with dissolve

    to "But...I don’t really understand what that entails."
    to "I have a hard enough time following what it is the common folk do during normal parts of the year. The idea of a vacation with them is just...not one that I think I’m fully prepared for yet."
    s "I mean, you did go on the beach trip with everyone recently. Just think of it like that except...the right weather."
    tb "If you don’t understand how it works, just {i}ask{/i}, dear. There’s no harm in that."
    tb "I’m sure your teacher would love to show you how everyone else spends their summer vacations."

    scene toukahair22
    with dissolve

    s "I would?"
    to "Is that...something you’d actually consider, Sensei?"
    to "You {i}have{/i} shown me the ropes of other aspects of the outside world- as frayed as they may have been."
    to "If you’d be willing to show me how a standard, commoner summer would look like as well...I’d consider myself greatly indebted to you."

    scene toukahair23
    with dissolve

    s "Well, that {i}does{/i} sound a lot better than me being indebted to you."
    s "It would just probably make a little more sense to ask one of your other-"
    to "I’m going to stop you right there in order to save both my heart and my pride, Sensei."
    s "Good call. Wouldn’t want your mother knowing you don’t have any-"
    to "Again, I am going to stop you right there."
    tb "Don’t have any what, Touka? Is it something we can provide you?"
    to "Sadly, no. It is not, Mother."

    scene black
    with dissolve2

    if bonus == True:
        "Sensing that it’s time for me to leave, I get off the bed only to be followed up by the Tsukiokas who, when combined, surpass everyone else on this floor put together in terms of breast volume."
    else:
        "Sensing that it’s time for me to leave, I get off the bed only to be followed up by the Tsukiokas who, when combined, surpass everyone else on this floor in terms of awesomeness and hugability."

    "Does that have anything to do with the matter at hand? No."
    "But when the two of them stand next to one another, it’s something I can’t help but notice and appreciate."

    scene toukahair24
    with dissolve2

    if bonus == True:
        "You know, on closer inspection, I think they might win out the combined-floor {i}ass{/i} category as well."
        "This family is rich in far too many ways."
    else:
        "Wow they are so cool."

    tb "Thank you again for allowing Touka and I to spend the rest of the night together. We truly do appreciate it."
    tb "It’s a shame about your lesson, but I’m sure the two of you will make up for it soon enough."
    tb "Especially with you agreeing to teach her about middle class summers and all."
    s "Did I agree to that yet? Because I still don’t really think I’m the right person to-"
    tb "Oh, nonsense. I’m sure you’ll do perfectly fine. Perhaps you can make a field trip out of it?"
    s "Right. Because nothing says {i}vacation{/i} like a planned, school-funded educational trip."
    tb "I wouldn’t mind funding it if money is the issue, of course."
    s "Not really what I was getting at."
    to "Things have been a bit warmer as of late, Sensei. Perhaps you can show me a few things the next time we meet up outside?"
    s "Oh, I’ll show you some things alright."
    to "Splendid. Thank you so much."
    tb "What a generous man you are, going to such lengths for my daughter."

    if bonus == True:
        s "I’m pretty good at all things involving length, so to speak."
    else:
        s "Anything for her education."

    scene toukahair25
    with dissolve

    tb "We {i}are{/i} still talking about education, yes?"

    if bonus == False:
        s "That is what I just said, yes."

    to "Mother! Ew! Don’t say things like that while winking at my teacher!"
    to "In fact, don’t wink at him to begin with! It is strange and unpleasant!"

    scene toukahair26
    with dissolve

    tb "Touka, dear. If there’s anything you need in order to make the most of your summer vacation training course, don’t hesitate to let me know."
    to "I won’t, but...I think it’s less of a training course and more of an...orientation?"
    s "I don’t think I’d call it either of those two things."

    "Especially when I still have no idea what I can even show Touka when her biggest summer memories involve an...animatronic animal band?"

    scene toukahair27
    with dissolve

    tb "I suppose we’ll be seeing you around, then? If there won’t be any lecturing done tonight, we should probably be getting back to Yasu’s hair."
    tb "It is...quite unkempt."
    s "Sure. But if she converts either one of you two, I don’t know how much time I’ll be able to spend with you anymore."
    to "Oh, don’t worry about that. I’ve taught my mother the “boop” technique and we’ve come up with a rule where we poke Yasu every time she begins to rant."
    tb "I’m very excited to try this on my youngest daughter as well. Though I can’t imagine it being nearly as effective."
    s "Well, have fun poking Yasu and being related or something. I’ll get out of your way now."
    to "Thank you again for postponing our totally legitimate English lesson, Sensei. It was a very nice thing to-"
    tb "You know I don’t actually buy that. Right, dear?"
    to "..."
    s "..."
    to "{i}Run.{/i}"

    scene black
    with dissolve2

    "I quickly exit Touka’s bedroom and force myself back into the state of mind where Tsubasa doesn’t believe I just show up to her daughter’s room for no reason whatsoever."
    "That aside, though, I’ll have to start thinking about summer-related activities to teach Touka about soon."
    "That might sound easy to you, but I’d like to use this opportunity to remind you that I only visit a select few locations every week- and I’m sure she’s already seen at least most of them."
    "Either way, I should be thankful that unknowingly interrupting another rare mother-daughter get together did not end in tragedy or suspicion."
    "At least...not any suspicion that was outwardly revealed to me."
    "I have no idea what Tsubasa will choose to believe in her own mind, but..."
    "I guess I can wishfully think it works out in my favor."
    "Especially since that’s all I ever really do anyway."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm10 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukaspecial15:
    scene sky
    with fade
    play music "marshmallow.mp3"

    "I begin my voyage to...wherever the wind takes me bright and early. "
    "In fact, it’s so early that the wind hasn’t even woken up yet, so I’m kind of just going in a straight line and not being {i}taken{/i} anywhere."
    "I guess that’s fine, though, considering that the area I normally meet up with Touka in is a {i}mostly{/i} straight shot from my home."
    "I {i}also{/i} guess that since I just mentioned Touka, there’s a high likelihood that I’ll bump into her and take her on the makeshift commoner’s tour of summer that she wants."
    "It’s a good thing I’ve spent so long looking up and preparing different activities I think she’ll thoroughly enjoy."
    "That was sarcasm if you couldn’t tell."
    "I have absolutely no idea what the two of us are going to do today when we inevitably meet."
    "But at least we’ll get to be alone."

    to "Oh. Good morning, Sensei."

    scene toukatrain1
    with dissolve

    "Or not."

    s "Good morning, entire Tsukioka family."
    to "Well, it’s...not the {i}entire{/i} family without my father."
    s "Yeah, but he doesn’t really matter to me."
    tk "Good morning, commoner teacher man! We are ready to walk among you and your people! We come in peace!"
    s "Good morning, mini Touka. I like your shirt and I’m sure there won’t be anyone around today who is offended by it."

    scene toukatrain2
    with dissolve

    tb "I tried very hard to get her to wear something else, but she was insistent on trying to look like “As much of a commoner as possible.”"
    tk "Of course I was! Talking to Chinami has made me realize how important it is to make time for those smaller and less significant than me!"
    tb "I understand that, but...I don’t really think your shirt will accomplish that, dear."
    s "Honestly, though, if “looking normal” is what you were all going for, Tsukasa is, weirdly enough, the closest out of everyone."

    scene toukatrain3
    with dissolve

    to "With a shirt as...{i}direct{/i} as that? How is that possible?"
    s "I don’t know. You two just sort of...exude wealth. Tsukasa just looks like a weird kid."

    scene toukatrain4
    with dissolve

    tk "Wha- weird?! Who do you think you are belittling, peasant?! I am Tsukasa Tsukioka! I am royalty! I am-"
    s "A weird kid."

    scene toukatrain5
    with dissolve

    tk "You told me he was nice."
    to "Is “nice” the word I used? Because I specifically recall using the word “fine” to describe him in place of that."
    s "That’s a lot closer, but still a bit off."
    tb "I hope you don’t mind that Tsukasa and I decided to tag along for your summer tour today. She just wouldn’t take no for an answer when she heard about it and..."
    tb "Well, let’s just say it’s been quite a while since I’ve really ventured off for the sole purpose of leisure as well."
    s "It’s fine, but I still think you guys are making a much bigger deal out of this than it really is."
    s "Like, I still have no idea what to even do today."
    s "I tried telling you before, but I’m not really the best person to ask about “fun” stuff like this."

    scene toukatrain6
    with dissolve

    to "You don’t have {i}any{/i} ideas? At all?"
    s "I mean, you’ve already been to the beach. That about sums up my knowledge of summer."
    s "I guess there are public pools too, but those are somehow even less fun and probably underwhelming for people of your...status."
    to "Our “status” is precisely what we are attempting to leave behind today, Sensei. Why else would we have dressed so casually?"
    s "Sorry, is that dress supposed to be casual? Because it really just looks like you’re trying to impress someone."

    scene toukatrain7
    with dissolve

    tb "How funny. That’s exactly what I told her before we left the manor this morning."
    to "Mother! Please!"
    s "The same goes for you as well, Tsubasa."

    scene toukatrain8
    with dissolve

    tb "Hm? I beg your pardon?"
    s "Just a little overdressed for the occasion is all. Us “commoners” don’t normally wear our family crests on our necks."

    if bonus == True:
        "We also don’t wear shirts that look like they’re going to come unbuttoned at any moment for the most part, but I guess that ones a sort of case by case basis."

    tb "But I...can’t simply leave the crest at home like Touka and Tsukasa do. Not as the wife of the Tsukioka Foundation’s chairman. It must remain on my person at all times."
    to "Father wouldn’t know if you took it off for a day out on the town, Mother."

    scene toukatrain9
    with dissolve

    tb "Touka, please. This isn’t like a wedding ring. I can’t just...take it off whenever I want."
    to "Do you...really not have anything planned, Sensei? Because I’d feel rather embarrassed to have brought my family along for...absolutely nothing."
    to "Not to mention getting dressed for the occasion- even if it’s not quite up to par with what you’d expect someone closer to your...level of income to be wearing."
    s "I really don’t. So if the three of you want to go back home and-"
    tk "I have an idea!"

    scene toukatrain10
    with dissolve

    tb "Tsukasa, {i}please{/i} tell me it doesn’t involve a kitchen."
    tk "It...probably doesn’t?! I don’t know!"
    s "What’s your idea, Tsurumi?"
    tk "My name isn’t-"
    to "He has a memory problem, Tsukasa. Just accept it."
    tk "Fine! Okay!"
    tk "I, Tsurumi Tsukioka, demand that you take us to the thing called a “subway!”"
    to "You don’t have to accept the name, Tsukasa."
    tk "Why is adult life so confusing?!"
    tb "Tsukasa, dear. Why do you want to see the subway exactly? This was supposed to be a tour of...various summer related activities."

    scene toukatrain11
    with dissolve

    tk "Because it’s the first thing that comes to mind when I think of people who have less money than us!"
    tk "What screams “poor people” louder than a bunch of sweaty commoners paying money to get  crammed into a rectangular metal box underground?"
    tb "I...suppose that is a fair point?"
    s "Is it?"
    to "Is the subway...you know...{i}safe,{/i} Sensei? Because it’s come up in several of the instructional videos I’ve watched at home about safety."

    scene toukatrain12
    with dissolve

    tb "Touka raises a good question- {i}is{/i} the subway safe? Because I remember gropers being a bit of a problem when I was Touka’s age."
    tk "What’s a groper?"
    s "A thing that very likely doesn’t exist around here anymore on account of the severe drought in testosterone."
    tk "What is testosterone? A food?"
    s "The subway should be fine. I just don’t ever really ride it since there’s not much of a need, though."
    s "I also don’t think it will be very fun, but who am I to tell anyone how to have a good time when one of Touka’s key interests is horses?"

    scene toukatrain13
    with dissolve

    to "I’m sorry, do you have an issue with {i}horses{/i} now? Because, last I checked, they were majestic, smart creatures who have been serving us longer than nearly any other animal for nothing in return."
    s "Yeah, hearing all that gives me hope that you guys might like the subway after all."
    to "I don’t...ugh."
    to "Forget it."
    tb "Well...I suppose it’s better than nothing. Seeing how the layman moves from place to place could be a wonderful, educational experience for my daughters."
    tb "I suppose there’s just the matter of figuring out where to ride the subway {i}to.{/i}"
    s "We’d have to figure that out when we go down to the station. Like I said, I don’t ride it very often, so I have no idea where it even leads."

    scene toukatrain14
    with dissolve

    tk "Never fear, teacher man! I used my {i}smartphone{/i} this morning to memorize the route map for each individual train!"
    tk "Do you know what a smartphone is? Or are you too poor to-"
    s "I have a smartphone, Tsurumi. They’re accessible to {i}my people{/i} now."
    s "Also, there is no way you memorized the route map for every train."
    tb "Oh, I wouldn’t put that past her. Tsukasa might be a handful, but she’s actually quite the little genius for her age. Her memory is near photographic as well."
    to "If you’ve wanted to ride the subway that badly, why haven’t you asked Father to simply build us one under the manor? He’s talked about it in the past as a means for staff members to get around."

    scene toukatrain15
    with dissolve

    tk "It wouldn’t be the same! There are no poor people at our house! And everyone is constantly speaking in different languages that only Mother understands!"
    to "Well...as long as Sensei is okay with it..."

    scene toukatrain16
    with dissolve

    to "But if you get lost, we’re not coming back for you. You’re going to have to find a new family."
    tk "Mother! Touka is being mean to me!"
    tb "Is the station far from here, Sensei? Should I wave down a taxi or summon us a limo?"
    s "Have you really been cooped up in that manor for so long that you think taxis are just driving around suburban areas looking for passengers?"
    tb "Yes."
    s "Oh."
    s "Well, they’re not."
    s "The station is literally right behind you, though. We can be there in less than five minutes if we want."

    scene toukatrain17
    with dissolve

    tk "That’s it?!"
    tk "What are we waiting for then?!"
    tk "Take us to the peasant version of a sardine can already, Mr. Teacher!"

    scene black
    with dissolve2

    if bonus == True:
        "I gesture toward the station behind the Tsukiokas and begin to make my way over, only to be followed closely behind by them like they’re a pack of high class escorts."
        "Well, two of them at least."
        "Or one."
        "I’m followed closely behind by three girls who look nothing like me."
        "Which is...probably nowhere even close to my initial perception of what the sight appears to be."
        "Anyway. Subway station."
    else:
        s "I can't wait to get my groove on in the subway."

    scene toukatrain18
    with dissolve

    tk "This way, Mother! Follow the scent of standing water and processed meats!"
    tb "Tsukasa, dear, are you sure this is the right way? It’s been a long time, but I think we may have to visit a ticket kiosk of some sort first."
    to "I’m...sorry I dragged them along, Sensei."
    to "Well, I suppose it was less of me {i}dragging{/i} them and more of them simply latching onto my dress and seeing where it leads."
    s "It’s a nice dress."
    to "Is that how you really feel? Or are you just saying that because it’s currently a three-for-one deal?"
    s "That’s how I really feel. It fits you well."
    to "Well...thank you, Sensei. I appreciate that."
    s "Like, {i}really{/i} well."
    to "And there you go, ruining yet another moment where I believed you to be a good man for a fraction of a second."

    scene black
    with dissolve2

    "Tsukasa, who somehow managed to get in front of all of us (Likely due to her difference in size), leads the way to a random train that, at least I {i}hope{/i} she’s actually memorized the path of."
    "All things considered, there are a few areas of this city I don’t really see fit for the Tsukioka family just yet."
    "Sure, Touka was able to survive a trip to the Old District, but if anything like what happened with Yumi and I were to happen in front of an entire family- let alone one as influential as this..."
    "Well, let’s just say Ami might never see me again."
    "Or anyone for that matter."
    "So...yeah."
    "Here’s hoping the train stops somewhere other than impending doom and tragedy."
    "........."
    "......"
    "..."

    scene toukatrain19
    with dissolve

    "We make our way into a subway car and, contrary to Tsukasa’s description from earlier, it’s not like we’re being packed in at all."
    "I’m sure that roughly half of the population no longer being around has something to do with that, but I’m not about to complain about an actual convenience when I understand how bad it could have been."

    to "Does it always smell this...{i}horrible{/i} in here?"
    s "Probably."
    tk "Hi. I’m Tsurumi Tsukioka, a poor person just like you. But you can probably tell on account of my shirt."
    tb "Tsuka- ahem."
    tb "Tsurumi dear, please don’t pester the other passengers."
    tk "What is your favorite commoner activity? Mine is watching the news."
    tb "{i}Tsurumi,{/i} that woman is asleep. Please do not wake her up."

    scene toukatrain20
    with dissolve

    to "So, what do we do now? Are there any...private compartments for groups of three or more?"
    tb "I don’t believe that sort of thing is available on subways, dear. From what I understand, this is a form of local transport used to get from one place to another in a quick, uncomplicated manner."
    to "So...we all just...stand in this small space together until we get to our destination? Is there a...gift shop? Or a...restroom, even?"
    s "Nope. Just other duplicates of this exact subway car, all chained together in typical poor person fashion."

    scene toukatrain21
    with dissolve

    tk "Okay, Mother. I’m over this. It looked more fun on the Internet and all of these people look really sad."
    tb "Well, I assume that’s because they are."
    tb "Also, we can’t leave just yet dear. The train has just started moving."

    scene toukatrain22
    with dissolve

    tk "Well, then ask them to stop! This is boring!"
    tb "It doesn’t work that way, dear. I think. I’m not really sure."
    s "You’re right. It doesn’t."
    tb "Exactly. It doesn’t work that way, dear."
    to "Tsukasa, this was {i}your{/i} idea. And, pardon the pun, but...you have to ride it out to the end."
    s "Nice pun."
    to "I said pardon it, Sensei."
    tk "I don’t have to do anything! {i}We{/i} don’t have to do anything! We’re rich! We probably own this stupid subway car!"
    tb "Not yet. But give it a few years, sweetie. Who knows what your father’s next big plan will be?"

    scene toukatrain23
    with dissolve

    to "Are we allowed to sit down on this subway thing? Or do we need to pay extra for that?"
    s "You need to pay extra. There are doors connecting the cars. Take the ones on your left all the way to the end and ask the person in the room at the head of the train for permission and a seating ticket."

    scene toukatrain24
    with dissolve

    to "Oh! I believe I’ve heard of that person before. The...conductor, I think?"
    s "Sure."
    tb "Was that always a rule?..."
    to "As a special thanks for your assistance, I’ll be sure to purchase you a seat as well, Sensei."
    s "Thanks, Touka. If you could also get me a drink from the cooler in the conductor’s room, it would be greatly appreciated as well. They’re complimentary, so you won’t have to pay."
    to "Of course. Does green tea sound okay?"
    s "Perfect, actually. Thanks, Touka."
    to "My pleasure."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Five minutes later...{/i}"

    scene toukatrain25
    with dissolve

    to "Oh {i}good.{/i} You managed to sit down without your {i}seating ticket.{/i}"
    s "Yeah. I forgot they aren’t needed on the weekends. My bad."
    to "Does tormenting me truly cause you enough joy to warrant continuously doing it? Do you not get bored of having me make a fool of myself?"
    s "It does and not really."

    scene toukatrain26
    with dissolve

    to "Hah...Well, I suppose it’s over now. All there is left to do is ride this train until Tsukasa decides it’s time to get off."
    s "Pretty sure that will be the next station. She doesn’t seem as thrilled as she expected to be among her beloved poor people."
    to "Yes, but did you truly expect her to be? She’s even more spoiled than I am and I have a helicopter with my name painted on it."
    s "{i}Why?{/i}"
    to "It was a present for my tenth birthday."
    s "{i}Why?{/i}"

    scene toukatrain27
    with dissolve

    to "Why do you think, Sensei? Because I’m lucky...and happened to be born into a family that had already carved out a sizable part of this world."
    to "I have many things that others could only dream of due to no hard work or...work {i}at all{/i} on my own."

    scene toukatrain28
    with dissolve

    if bonus == True:
        to "I’m a [teenage]girl on the cusp of becoming a woman and I don’t even know how to ride the subway or...what the other girls in my class do to celebrate their summer vacations."
        to "I’m entirely hopeless when torn out of my element."
        to "And yet all you do is toy with me."
    else:
        to "I just wish I had more than five years left to live..."

    s "..."
    to "..."
    s "Sorry. Did you say something? I wasn’t paying attention."

    scene toukatrain29
    with dissolve

    to "Rude. I was attempting to have a moment with you."
    s "I don’t normally “have moments” with girls when their mothers are sitting directly beside them."
    to "Well I apologize for being the bearer of bad news, but my mother is a very big part of my life."
    to "And if you and I are going to continue spending time with one another, I can only hope that {i}she’ll{/i} have the time to be there for some of it."
    to "It’s just something you’ll have to accept. Like how {i}I’ve{/i} accepted you’re a tasteless hack who couldn’t tell a salad fork from a soup spoon."
    s "Is the spoon the pointy one? My small, proletarian brain can’t quite remember."

    scene toukatrain30
    with dissolve

    to "Mhm! So the next time the maître d’ asks you if you’re missing anything and you notice a distinct lack of pointed utensils, make sure to ask for a new spoon."
    s "You have a long way to go if you’re trying to trick me into doing the same sorts of things I trick {i}you{/i} into."
    to "Maybe for now."
    to "But that’s just because I’m still out of my element."
    to "You just wait until I drag you into {i}my{/i} lifestyle. We’ll see who truly struggles to adapt then."
    s "I didn’t really think you intended on dragging me into your lifestyle anytime soon, Touka."
    to "Neither did I. But the thought of seeing you suffer sounds a little too good to overlook anymore."

    scene toukatrain31
    with dissolve

    s "Well, it’s a weird sentence to say, but I guess I’m looking a little forward to whatever suffering you have in store for me."
    to "As am I..."
    s "..."
    to "..."
    to "You called me Touka again."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukaspecial15 = True
    stop music fadeout 15.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"

    "We ride the subway to the end of the line after Tsukasa takes Touka’s earlier comment of “riding things out” to heart and wind up at a station that looks significantly different from the one we boarded from."
    "Wanting to stretch their legs and observe wherever it is we’ve wound up, the female members of the Tsukioka family exit the subway car and, after awkwardly looking around the station, head for a nearby staircase."
    "Once we get to the top, however, and a flood of multicolored light overtakes us- they realize just how out of place they are in this world."
    "........."
    "......"
    "..."

    jump toukaspecial15p2

label toukaspecial15p2:
    scene tsukiokaarcade1
    with dissolve2
    play music "justbehappy.mp3"

    tk "What?! Where are we?! This doesn’t look like a place that’s made for poor people at all!"
    tb "Did we perhaps go...{i}under{/i} the outer barrier instead of through it? Have we accidentally discovered a loophole in the isolation policy?"
    to "No, Mother. I believe we’re still in Kumon-mi. I’ve overheard several of my classmates speaking about a place like this, but I had no idea it was so...large. And colorful."
    to "Why, this is actually quite impressive."
    tk "Mother! Mother! There is a sign for something called a “Maid cafe!” Poor people {i}can{/i} have maids after all!"

    "As much as I’d like to say that Kumon-mi keeps getting larger, I actually know where we are now."
    "Well, vaguely. "
    "I’m pretty sure this place isn’t far off from the arcade I visited with Rin a while ago. The...architecture looks the same, at the very least. "
    "I’m pretty sure I’ve heard Ami and company talk about this area as well, but those conversations have always been riddled with terminology I don’t understand, so I never paid much attention."
    "Either way, as you can see, the Tsukioka family is currently struggling to come to terms with the expansion of their world and has gone into a bit of a collective state of shock."

    scene tsukiokaarcade2
    with dissolve

    to "Sensei...we {i}are{/i} still in Kumon-mi, correct? Do you have any idea what this part of the city is called?"
    s "We are and no. I have no idea what this place is called. Just keep an eye out for a sign if you’re that curious."
    to "Well aren’t you as unhelpful as ever."
    s "I’d like to take this opportunity to remind you that you’re technically the one who brought {i}me{/i} here. Well, your sister at least."
    tk "This place is crazy! Super crazy! "
    tk "Why’s that man over there dressed like a woman?! And why is that woman dressed like a cat?! And why is that cat- wait, no. That’s just a normal cat."
    tk "Mother! Put Father on Facetime! He must see this!"
    tb "This isn’t one of those “Red light districts” I’ve heard about, is it? "
    to "The lights {i}do{/i} seem rather red-{i}ish.{/i}"
    s "I’m sure there’s nothing you have to worry about during the day. Things might be a little different at night, though."

    if bonus == True:
        "I’ll have to make sure I stop by and check some time. In the interest of keeping my students out of harm’s way, of course. There are absolutely no “personal” reasons for my sudden desire to spend more time here."

    scene tsukiokaarcade3
    with dissolve

    tk "Mother! Do you think the reason commoners are able to tolerate the subway as effectively as they do is because they know where it is taking them?"
    tb "No, dear. I think they just have a completely different standard of living than we’re used to. But I’m sure a place like this {i}would{/i} provide some sort of...incentive."
    to "Tsukasa, will you be choosing where we head from here as well? You know, since our tour guide would rather {i}tour{/i} than {i}guide.{/i}"
    s "I’ll have you know that there is actually one building over here that I have been inside and that is infinitely more than any of you have exposure to."

    scene tsukiokaarcade4
    with dissolve

    to "Is that true? What in the world brought you over to this part of town, Sensei? All that I’ve heard about it involves otaku culture, scantily clad women and-"

    scene tsukiokaarcade5
    with dissolve

    to "Oh. I believe I understand now."
    tb "You’re absolutely sure there’s nothing...you know, {i}inappropriate{/i} around here, Sensei? "
    tb "Touka is one thing, but I shouldn’t be exposing Tsukasa to such...aspects of the world at her age. Especially with her inherent curiosity about everything."
    tk "Nonsense, Mother. I’m just as much of an adult as Touka."
    tb "You’re really not, dear."
    s "I have no idea what is or isn’t inappropriate about this part of town. The building I alluded to a minute ago should be fine, though."
    s "It’s just some arcade thing I’ve been to with another girl from class."

    scene tsukiokaarcade6
    with dissolve

    tb "Well aren’t you the most popular man around?"
    s "Strangely enough, I kind of am."
    to "Who did you come here with, Sensei?"
    to "Was it the Irish girl? Molly? This seems like the sort of place she’d enjoy. "
    tb "I bet {i}I{/i} know who it was."
    s "It was Rin."

    scene tsukiokaarcade7
    with dissolve

    tb "Nevermind. This is what I get for thinking I’m “in the loop.”"
    to "I suppose you two are rather friendly with one another, so that makes sense. "
    to "What would we do at an arcade, though? Tsukasa and I have very little exposure to video games since they’re known to rot away at the brain. "
    s "I think that’s just a thing parents say to keep their children away from having fun for whatever reason. There’s not really any truth to it."

    scene tsukiokaarcade8
    with dissolve

    tb "You know, dear, your mother used to be rather excellent at pinball when she was your age. "
    tb "I’m not sure if I’d call that a {i}video{/i} game per se, but I’m not opposed to reliving some of the old days with my two favorite girls by my side."
    to "Is that true, Mother? I had no idea. I’d assumed those old pinball machines in our seventh basement were just valuable antiques of some sort."

    scene tsukiokaarcade9
    with dissolve

    tb "What? No! Don’t call them antiques! That makes me feel old!"
    tk "Mr. Teacher Man, does this “arcade” have the pig-killing game that my new friend Chinami has been telling me about? "
    tk "She has been raving quite a bit about it and I must train in order to knock her off her shoddy, immunocompromised pedestal and show her who the true champion of the world is."
    s "Probably not, but there’s only one way to find out."

    scene tsukiokaarcade10
    with dissolve

    tk "I vote for the commoner arcade! I see enough maids at home! A cafe full of them does not interest me!"
    tb "I also think that might be fun. I’m not sure I’m as good with my hands as I used to be, but I’d certainly like to give them a bit of a workout if you catch my drift. "
    s "I...don’t know if I do? Because that sounded a lot like-"
    to "With Mother’s blessing, I’d be delighted to go as well."
    to "It might not be a public pool or a beach vacation, but this {i}does{/i} seem like a summer activity of sorts. So it’s almost like the purpose of our visit here is actually being fulfilled!"
    to "Congratulations, Sensei! You have achieved a very rare success!"
    s "Who is it that’s been teaching you sarcasm? Because I really don’t like this side of you."
    to "What side are you speaking of? I am but a naive, young woman- ignorant to the harshness of a commoner summer and all of the activities that accompany it."
    tb "And I’m her mother: An ex-pinball expert who is definitely not “old.”"
    tk "And I’m bored! Arcade! Now! Go!"

    scene black
    with dissolve2

    "I search for the word “arcade” on my GPS app only to be flooded with a list of at least twenty of them that I must now cycle through until I find the one I’m actually familiar with."
    "After a fair bit of navigation, the name “Couch Potato” jumps out at me and I confirm that it’s the correct one."
    "The arcade is about a mile away, so I’m sure it’s more walking than any of the Tsukiokas have ever done while not on some sort of...rich person hike or something."
    "If that’s even a thing rich people do."
    "Huh."
    "I guess I really would be lost if I were to enter Touka’s world."
    "But for now, she and her family are a part of mine."
    "Just...one that I don’t often explore. "
    "Either way, I coerce them into following me without the assistance of a limo and, after a short while, we arrive at the arcade."
    "........."
    "......"
    "..."

    scene tsukiokaarcade11
    with dissolve2

    tb "You know, I was a little worried about where you were leading us once we started moving further and further away from the nice looking buildings, but I will admit that this is nicer than I was expecting."
    s "Thanks? Maybe?"
    to "It’s just an interesting choice. That’s all. I’m sure this arcade has just as much to offer as all of the ones we passed that were ten times the size of it."
    s "Really. Who taught you this?"
    to "There are certain things a person just...picks up after spending enough time with you. "
    s "Anyway, {i}I’m{/i} not the one who actively {i}chose{/i} this arcade. It’s just the only one that I’ve physically been to."
    s "Take it up with Rin if you have a problem with it. This is just the one where cool people hang out at according to her."

    scene tsukiokaarcade12
    with dissolve

    to "What? Cool people? I would like to be “cool.”"
    s "Then go play a game or something. I don’t know. "
    s "Enjoy your pretend summer vacation while it’s technically still winter."
    tb "What are you going to do, though?"
    s "Me? Probably zone out for a few minutes and then choose which one of you to spend time with."
    tb "Well {i}I{/i} am going to get a drink. I was not expecting there to be a bar here. "
    tb "I was also expecting there to be maybe {i}one{/i} pinball machine, but...alas."

    scene tsukiokaarcade11
    with dissolve

    to "And I suppose I will make my way over to a random machine and pretend to know what I am doing. "
    to "Feel free to come teach me if you’d be so obliged, Sensei. Since that {i}is{/i} your job and all, I mean."
    s "Uh-huh. We’ll see."

    scene black
    with dissolve2

    "The Tsukiokas disperse and, after a moment of self-reflection and mild confusion about yet another situation I’ve found myself in, the time comes to make a choice."
    "Who do I want to spend time with first?"

    menu tsukiokaarcade:
        "Touka" if toukaarcade == False:
            scene tsukiokaarcade13
            with dissolve2

            to "Oh, good. You’re here. "
            to "Can you tell me what the purpose of this game is exactly? I can’t seem to make it past the first level."
            s "Touka, that’s the start menu. "
            to "Does it not count as a level? I’m very confused. "
            s "You just have to hit the start button."

            scene tsukiokaarcade14
            with dissolve

            to "The...oh. Okay. I see it. Can I not just use this knobby thing to control the video game? Using multiple buttons {i}and{/i} a knobby thing sounds very hard for a beginner like me."
            s "I’m pretty sure this is one of the easiest games to control here. You’ve just got two buttons and a joystick."
            s "Most of the modern games Ami and her friends play require all sorts of buttons and multiple joysticks, so if you’re going to learn, this is probably the place to do it."

            scene tsukiokaarcade15
            with dissolve

            to "Do you also play games like this in your spare time, Sensei? Or is all of it spent wandering into the rooms of unsuspecting [teenager]s?"
            s "I don’t really do anything like this, no. Knowing how arcade machines work is kind of just ingrained into the lower middle class, I guess."
            to "I see. "
            to "If only they could find that same level of ingrained passion for exercising or eating anything other than junk food."
            s "Yeah, if only."
            s "Anyway, do you want to give this a try? It’s a fighting game, so you can just mash a bunch of those buttons and hopefully hit me or something."

            scene tsukiokaarcade16
            with dissolve

            to "Yes! That sounds wonderful."
            to "Let’s see...um...start!"

            "Touka slams down on the start button and finally makes it past the opening menu."
            "A fit of paid applause rings out in the distance as she conquers what is probably the biggest challenge she has faced to date."

            to "Please go easy on me, Sensei. It is my first time and I don’t know what I’m doing."
            s "Can you say that again, but with direct eye contact and a slightly redder face?"

            scene tsukiokaarcade17
            with dissolve

            to "Ha ha ha. Sexual harassment is no joke, Sensei. "
            s "Then why did you just laugh?"
            to "Because that...wasn’t a real..."

            scene tsukiokaarcade18
            with dissolve

            to "You know what?! I do not need to defeat you with words! I will defeat you in combat instead!"
            to "Engarde!"
            s "You haven’t selected a fighter yet."
            to "How do I do that?"
            s "Just move your joystick until the character you want to play as is highlighted. Then hit one of the two buttons you’re hovering over."
            to "Okay. But if this is a trick and your method causes me to lose before the game even begins, I will be incredibly upset with you."
            s "This is one of the rare times I’m actually being honest. "

            "Touka cycles through all of the characters for a moment while I just select the “Random” option since I have no idea how any of them work and don’t really care."
            "Eventually, she makes up her mind and slams down on the button with way too much vigor, prompting the round to start."

            to "{i}Now{/i} engarde!"
            to "How do I attack? Which of these two buttons inflicts the most pain upon my enemy?"
            s "Well, you’re going to want to walk over to my character first."
            to "Which one is your character?"
            s "Literally the only other character on the screen besides yours."
            to "I see. Do not move. I am coming to eliminate you."
            s "..."

            "Touka eventually manages to move her character over to mine and stops him dead in his tracks before actually attacking."

            scene tsukiokaarcade19
            with dissolve

            to "Do you have any last words, Sensei?"
            s "Yes. Are we actually fighting? Or am I supposed to stand here and let you kill me?"
            to "Do you think you can defeat {i}me?{/i} Touka Tsukioka of the esteemed Tsukioka family?"
            to "I have practiced a bit of Judo, you know. I was never very good, but I do believe it will give me a bit of an advantage when it comes to-"

            scene tsukiokaarcade20
            with dissolve

            to "Wait! What was that noise?! What happened to my little green bar at the top of the screen?!"
            s "I punched you while you weren’t looking. "
            to "The {i}audacity!{/i} How dare you!"

            scene tsukiokaarcade21
            with dissolve

            to "Hi-yah!"

            "Touka presses one of her buttons and manages to punch my character as well."
            "This means war."

            to "Hi-yah! Hi-yah! Hi-"
            to "Wait. No. Stop it. Let me hit you. My flurry of blows is not yet complete."
            s "I’m good. I don’t really like losing."

            scene tsukiokaarcade22
            with dissolve

            to "And you think {i}I{/i} do?! Absolutely not! I will not be defeated by my-"
            s "You just lost."

            scene tsukiokaarcade23
            with dissolve

            to "Already?!"
            to "You liar! You heathen! You’re an expert at video games, aren’t you?! Is this what it means to be hustled?!"
            s "No. This is what it means to stop paying attention when you’re competing against someone."
            s "You let your guard down and I just took advantage of that."

            scene tsukiokaarcade24
            with dissolve

            to "But my character was so much larger than yours. He should have been able to live for much longer than that."
            to "This game is entirely unrealistic. "
            s "You know, I think you’re going to find that that’s a recurring aspect of video games. The vast majority of them don’t really pride themselves on their realism."

            scene tsukiokaarcade25
            with dissolve

            to "I demand a rematch immediately. I refuse to leave this machine until I defeat you. "
            s "But we could be here for years."
            to "Nonsense. I just need several more rounds to familiarize myself with the form of martial arts my character uses."
            to "I will be mopping the floor with you in no time at all, good Sir."
            s "Sure thing, Touka. Whatever you say."

            scene black
            with dissolve2

            "Touka and I proceed to play several more rounds of the fighting game. "
            "Then several more."
            "Then...several more."
            "She is very, very bad. Even by beginner standards."
            "Eventually, I get so tired of winning that I put on an act to make it seem like she defeats me fair and square, freeing me once and for all from my prison of incessant victory."
            "And while it does hurt my pride a bit losing to Touka (Even if it’s on purpose), that pride is quickly healed by the sight of her literally jumping for joy."

            if bonus == True:
                "I curse whatever innovations in fashion manage to keep her dress secured to her chest before sighing to myself and returning to the center of the arcade."
            else:
                "I am so glad that I was able to make her happy."

            "........."
            "......"
            "..."

            $ toukaarcade = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

        "Tsubasa" if tsubasaarcade == False:
            scene tsukiokaarcade26
            with dissolve2

            "I make my way over to Tsubasa at the bar and feel very proud of myself for once again actively seeking out someone closer to my age group."
            "Honestly, though, Tsubasa isn’t really that different from Touka in...any way whatsoever. So it’s kind of just like hanging out with Touka 2.0. "
            "Or...1.0 depending on your preferences, I guess."
            "Either way, I take my place beside her at the bar and order a beer that, hopefully, Tsubasa will pay for on account of both her immense wealth and the invasion of what was supposed to be a thing for Touka and me."

            tb "Well, hello there."

            if toukaarcade == True:
                tb "Does this mean you and Touka are done {i}combating{/i} one another?"
                s "Yes. Though, I did have to take a dive in order to get away."
                s "She refused to leave the machine until she beat me and she is incredibly bad at video games."
                tb "Look at you, taking a fall to please a young girl. How noble."
            else:
                tb "I’m a little surprised to see you come over to me before Touka. What with me intruding on your little “field trip” and whatnot."
                s "It is what it is. I don’t really care one way or the other."

            s "I’m honestly kind of surprised you even wanted to tag along for this. It doesn’t really seem like a thing you’d be into."
            tb "Well it’s not as if I {i}knew{/i} what I’d be getting into. But I doubt I would have refused even if I’d known where we were going from the start."

            scene tsukiokaarcade27
            with dissolve

            tb "This may come as a bit of a surprise to you, but I don’t particularly “get out” often."
            s "{i}What? No.{/i}"
            tb "Okay. So it might be {i}overwhelmingly apparent{/i} that I don’t get out often. "

            scene tsukiokaarcade26
            with dissolve

            tb "But that doesn’t mean I’ve always been this way."
            tb "I used to do a fair bit of “sneaking away” when I was Touka’s age, you know. And that led to all sorts of wild experiences."
            s "How wild are we talking here?"

            scene tsukiokaarcade28
            with dissolve

            tb "Hahah~ Maybe {i}wild{/i} wasn’t the right word, exactly. I’m sure it was really nothing compared to what [teenage]girls are doing nowadays."

            scene tsukiokaarcade26
            with dissolve

            tb "But for my girlfriends and I, it was wonderful. And I often wish those experiences weren’t so few and far between when looking back on them."
            tb "It oftentimes feels that I may have...wasted away my youth to some extent."
            tb "Coming from a wealthy family is certainly an advantage in life, but that doesn’t mean it’s without its setbacks."
            s "Well, at least you’re getting to experience more of {i}this{/i} life now."

            scene tsukiokaarcade29
            with dissolve

            tb "True. But {i}this{/i} is only happening because I followed my daughter out. It’s not really a thing I’d be able to do on my own with my lack of knowledge or...connections outside of the business world."
            s "Well, you’ve got me. I’m outside of the business world."

            scene tsukiokaarcade30
            with dissolve

            tb "Careful, Sensei. Saying it that way makes it sound like we might be {i}friends.{/i}"
            s "I mean...we {i}can{/i} be?"

            scene tsukiokaarcade31
            with dissolve

            tb "We...can? You and me? But we have virtually nothing in common."
            tb "And Touka’s already advised you that I don’t have much time to really do things with her- let alone someone outside of the family."
            s "Sure. And I’m not really expecting that to change. Just letting you know that there is {i}someone{/i} outside your circle of insanely rich people who wouldn’t mind spending time with you."

            scene tsukiokaarcade32
            with dissolve

            tb "That’s very kind of you. And..."
            tb "And perhaps I {i}will{/i} take you up on that sometime."
            tb "It’s been years since I’ve “snuck away” for anything. Just thinking about doing something like that again is actually getting me quite excited."
            tb "Perhaps we should share contact information?"
            s "Sure. But only as long as you can promise me your husband isn’t going to use his citywide influence to spy on us or tap your phone."

            scene tsukiokaarcade27
            with dissolve

            tb "Or perhaps it would be best if we didn’t share that information with one another at all."
            s "..."

            scene black
            with dissolve2

            "I realize soon after that Tsubasa is [[probably] just kidding and the two of us swap numbers."
            "I chug down my beer as soon as it arrives and, just like I wished, Tsubasa offers to pay for it."
            "Here’s hoping that whatever sorts of things the two of us do when she manages to sneak out are worth the price of that."
            "And, if they’re not, I’m even more boring than I thought."
            "Either way, I make my way back to the center of the arcade and begin to look around and see if there’s anything else I’ve missed..."
            "........."
            "......"
            "..."

            $ tsubasaarcade = True
            $ tsubasanumber = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

        "Tsukasa" if tsukasaarcade == False:
            scene tsukiokaarcade33
            with dissolve2

            "For some reason that I don’t fully understand, I make my way over to Tsukasa at some tabletop arcade machine."
            "She stops fiddling with a joystick in a compartment underneath the table long enough to look up and lock eyes with me."
            "Through the harsh judgement and pity and disgust and a bunch of other things I can tell she is feeling regarding my existence as a human, however, I can tell she needs help."

            tk "I need help."

            "This is subsequently confirmed."

            s "What do you need help with?"
            tk "Everything."
            s "That’s too many things."
            tk "I don’t know how to get this game to work. Or what the pig killing game even looks like."
            tk "Or where we are or what the song on the radio is or who I need to talk to for a glass of water."
            tk "So, yeah. Everything."
            s "Sucks to be you, I guess."
            tk "Hey. Do you wanna be my new butler? The one I have right now knows nothing about peasant life, so our interests really aren’t aligning at this current point in time."
            s "I don’t think I’d make a very good butler."
            tk "Why not?"
            s "Because I am bad with children and you seem...extremely high maintenance."

            scene tsukiokaarcade34
            with dissolve

            tk "I probably am. But wouldn’t living in a giant mansion and getting your own swimming pool and pretty much anything else you want make up for that?"
            s "This offer suddenly sounds a lot more interesting."
            tk "Is that a yes?"
            s "I’ll have to consult with my business partner. Who also happens to be my [niece]. If I move out, she’ll probably die."

            scene tsukiokaarcade35
            with dissolve

            tk "Oh well. One less mouth to feed."
            s "Tsukasa, why are you...the way you are?"

            scene tsukiokaarcade36
            with dissolve

            tk "You mean awesome?"
            s "I mean awful."

            scene tsukiokaarcade37
            with dissolve

            tk "That’s not a very butlery thing to say, Jeeves."
            s "My name isn’t Jeeves."
            tk "It is now. All of my butlers are named Jeeves. It’s the most butlery name. You have to fit the role."
            s "I haven’t even agreed yet."
            tk "What do you mean you haven’t agreed? I’m Tsurumikasa Tsukioka. You have to listen to me or I’ll hire a team of assassins to...well, assassinate you."
            s "I suppose that is a bridge I’ll cross when I come to it."
            tk "Hm..."
            s "What do you mean “Hm?”"
            tk "I’m just trying to figure out why my sister likes you so much. You seem pretty boring and lame to me if you don’t even want to come live in a fancy mansion."
            s "Has Touka really told you she likes me?"
            tk "Mhm. She says you’re the best teacher she’s ever had. But she’s never really liked any of her other teachers, so I guess that’s not saying much."
            tk "Either way, I don’t see it. If you were {i}my{/i} teacher, I would have fired you by now. But I fire all of my teachers so, again, that’s not saying much."
            tk "Can you teach me how to play this game now?"
            s "Immediately after insulting me?"
            tk "Well, who else is gonna teach me? {i}Someone{/i} has to."
            s "Just figure it out on your own like you did with the subway. It’s really not that hard."
            tk "I don’t want to figure it out on my own. I want you to teach me."
            s "But I’m an annoying, boring commoner."
            tk "You are. But it’s no fun doing things on my own. And Papa won’t teach me things like this because of how they’re bad for me."
            tk "In fact, he doesn’t really have time to teach me anything anymore."
            tk "So that’s why I want you to do it."
            tk "It would be better if you were my butler, but I have to take what I can get at this point. Good help is hard to come by around here."
            s "..."
            tk "..."

            scene tsukiokaarcade38
            with dissolve

            tk "Jeez! Hasn’t anybody ever told you that time is money?"
            tk "No wonder you’re so poor if you’re just going silent in the middle of conversations like that."
            s "If I teach you how to play this game, you’re going to owe me a favor in the future."

            scene tsukiokaarcade39
            with dissolve

            tk "A trade offer? I can do that."
            tk "What are you after? A luxury car? One of Touka’s horses? Name it and it will be yours."
            s "I don’t know what I want yet. I just think it will be useful for a person of your status to owe me a favor that I can call upon when I need it most."
            tk "Like if you have to bury a body?"
            s "What? No. I-"

            scene tsukiokaarcade40
            with dissolve

            tk "Say no more. I agree to these terms and will help find you an experienced burial crew the moment you need it."
            s "Tsukasa-"
            tk "Silence. The terms have been accepted. The deal is complete."

            scene tsukiokaarcade41
            with dissolve

            tk "Now, let’s play, Jeeves!"

            scene black
            with dissolve2

            "I spend a few minutes learning how to play the tabletop game so I can teach Tsukasa, and it’s easy enough that we’re both able to pick it up without any issue."
            "It’s multiplayer as well, so I’m able to stay on the opposite side of the table and play against her once we have things figured out."
            "Surprisingly, she’s actually pretty good at it. But I guess reflexes are better when you’re young and...well, she {i}is{/i} allegedly some sort of gifted kid."
            "I get tired of playing eventually, though, and decide to head back to the center of the arcade."
            "As I leave, I spot Tsukasa frowning out of the corner of my eye."
            "........."
            "......"
            "..."

            $ tsukasaarcade = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

label endoftoukaarcade:
    $ renpy.end_replay()
    $ toukaspecial15p2 = True
    $ touka_love += 1
    $ tsubasa_love += 1
    $ tsukasa_love += 1

    "{i}Your affection with the entire Tsukioka family has increased by 1!{/i}"

    jump toukaspecial15p3

label toukaspecial15p3:
    if _in_replay:
        scene black
        play music "justbehappy.mp3"

    "The next half hour or so goes by without much of a change to anything. "
    "Touka continues training her virtual combat skills against AI opponents, Tsukasa sits by herself at some table likely thinking about poor people, and Tsubasa downs probably an entire bottle of wine."
    "As for me, I repeatedly cycle around the arcade, spending short bursts of time with each one of them until things devolve into what I would call a mild amount of chaos."

    if bonus == True:
        tk "Mother! Mother! Can I have permission to rail Touka’s teacher?"
        tb "Of course dear. Just don’t get hurt. That thing looks like it’s meant for big girls and you’re still so young."
        to "Tsukasa, no! He’s {i}my{/i} teacher and I get to rail him first!"
        to "Mother! Tell Tsukasa to not rail Sensei before me!"
        tb "Perhaps I should be the one to rail him if you two are just going to fight over it?"
        s "Am I really the only person finding something odd about this conversation?"
    else:
        tk "Mwahahah! The time has come for me to activate the many bombs I have placed in this building!"

    "As you can see- a mild amount of chaos."

    if bonus == True:
        "Anyway, the Tsukiokas take turns railing me and, after they tire themselves out, the time comes for us to leave the arcade."

    scene noonsky
    with dissolve2

    "We spent enough time inside that the sun has already begun to set, taking a bit of the pre-summer warmth back behind the clouds as it disappears."
    "And, in other news, I wish it also took Tsukasa along with it since she has been doing nothing but annoying me ever since leaving the arcade."

    tk "Mr. Teacher Man, have you played the same game with my sister that you played with the hot spring peasant girl?"
    tb "I certainly hope not~"
    to "Hot spring peasant girl? Are you speaking of Io, Tsukasa?"
    tk "Does Io look like she fell asleep in a tanning bed?"
    tb "Tsukasa! Chika is part Filipino, her skin color has nothing to do with tanning."
    to "What sort of game were you playing with Chika at a hot spring? Is it one that I can play as well?"
    s "Sure."
    tb "{i}Ahem.{/i}"
    s "I mean no."
    to "Well, that doesn’t seem very fair at all..."

    scene black
    with dissolve2

    "The four of us continue to walk around what I am now going to refer to as the “Entertainment District” for lack of a better term."
    "I think it’s technically part of the urban one given the size and scope of everything but, at the same time, I don’t really think it makes much of a difference."
    "All I know is that I haven’t blacked out and forced myself on anyone here, so it’s likely not part of the old district."
    "Regardless, we decide to make our way back to the station for some budget commoner food before venturing back to the area of Kumon-mi we’re all more familiar with."
    "Here’s hoping that the Tsukiokas have any amount of exposure to Mexican street food- which is, very strangely, the only thing this subway station seems to have."

    scene toukataco1
    with dissolve2

    to "If I ask you how I am supposed to order, will you assist me? Or will you just make me look like a nuisance again?"
    s "Of course I’ll help you, Touka. I’d do anything for you."
    to "You intend to make me look like a nuisance after all, don’t you?"
    s "Why would I ever {i}not{/i} do that?"

    scene toukataco2
    with dissolve

    taco "Hi. How can I help you?"

    scene toukataco3
    with dissolve

    to "Oh, good afternoon. My name is Touka Tsukioka of the Tsukioka family, and this man behind me is my [high_school] teacher."
    taco "I am the taco man. Behind me is a sink."
    to "Say hello, Sensei. You don’t want to be rude to the taco man, do you?"

    "Well, this is already going better than I expected."

    to "May I trouble you for a recommendation, taco man? I am not well-versed in the art of Mexican cuisine, so I’m not quite sure what to order."
    taco "All we have are tacos. I recommend those."
    s "Really living up to your name, aren’t you?"
    taco "I don’t get it."

    "Sometimes, I feel like I’m the only normal person in this city."

    to "I suppose I will take the tacos, then! How many would you say a three person family would consume on average?"
    taco "I have no idea, Touka Tsukioka of the Tsukioka family."
    to "There’s no need to worry, taco man. I’m sure Sensei knows the answer to a question as simple as this."
    s "One thousand tacos."
    to "Or not. "
    taco "How about I just give you a random amount of tacos and you come back if you need more?"
    to "Splendid! Thank you very much for your assistance, taco man. Have you ever considered teaching [high_school]? We could use more people like you."
    taco "My brother used to work at Kumon-mi High. I heard nice things."
    to "Used to? Did he retire?"
    taco "He died after some girl hit him with a dodgeball."
    taco "No one came to the funeral but me."
    s "Well that’s certainly a part of the plot I didn’t expect to ever show up again."
    to "Oh my! I’m so very sorry to hear that. I hope the purchasing of your tacos will, in some way, help to numb the pain."
    taco "It really will. "
    taco "Thank you, Taco Tsukioka of the Tsukioka family. "
    to "And thank {i}you{/i}, Touka man!"
    to "Wait-"

    scene black
    with dissolve2

    s "Nope. We’re done here. No one said anything weird and it’s time to eat."
    to "But...I could have sworn I just-"
    s "Nope."

    "Touka and I wait patiently as the taco man does what he does best and, before long, we’re carrying several trays worth of tacos over to a nearby picnic table."
    "........."
    "......"
    "..."

    scene toukataco4
    with dissolve2

    to "So...{i}these{/i} are tacos."
    tk "..."
    s "..."
    tb "How exactly are we supposed to eat them?"

    scene toukataco5
    with dissolve

    s "You start by grabbing them. Then you finish by biting them. "
    s "It’s really just a two step process."
    tb "We grab them...with our hands?"
    s "I mean...I guess you could use your feet if you’re agile enough?"
    tb "Is there no option for chopsticks? Or perhaps a fork or knife? All of us were taught to never eat with our hands."
    s "That is very unfortunate because I can’t imagine these being consumable any other way."
    tk "What’s the yellow thing holding all of the stuff inside called?"
    to "I believe that is the...taco bone?"

    scene toukataco6
    with dissolve

    s "The taco bone?..."
    to "I-I don’t know! It just appears to be the bone of the taco!"
    to "Are we supposed to remove the innards? Or is the bone edible?"
    s "Touka, it’s a shell."
    to "Then say that before I call it a bone, Sensei! Stop allowing me to appear uncivilized in front of my family."
    tk "How come I got more than everybody else? I’m the smallest one here."
    tb "Probably because you’re the most special, dear. Now, eat your tacos before they get cold."
    tb "Unless they...already are cold? I’m not quite sure."

    scene toukataco7
    with dissolve

    s "I understand that you’re all very sheltered and don’t understand how most things in the outside world work, but I really feel like you’re making this harder than it has to be."
    tk "Mother. You go first. I need to know they are safe."
    tb "No, dear. I’m not expendable the way you are. I have a business to run."
    tk "I’m telling Father you called me expendable. "
    to "I...I will do it."
    to "I will be..."

    scene toukataco8
    with dissolve

    to "The sacrifice!"
    tb "Be careful, dear. Have you washed your hands? "
    to "Of course, Mother. I’m no heathen. "
    tk "Mother, if Touka dies from taco poisoning, can I get {i}all{/i} of her bedrooms?"
    tb "We’ll see, Tsukasa. Now, pay close attention to your sister. These could very well be her final moments."
    s "..."
    to "Here I go..."

    scene black
    with dissolve2

    "Being around rich people is exhausting."

    stop music fadeout 20.0

    "Eventually, the Tsukiokas {i}do{/i} eat their tacos. But, unfortunately for the taco man and his deceased brother, I don’t think they particularly enjoy them."
    "I guess that’s to be expected, though."
    "If you spend your life consuming the best of the best, you’ll be nothing but underwhelmed or let down the moment you try something less...refined."
    "Which I guess allows me to segue into this thought that I’ve been having ever since Tsukasa mentioned Touka openly admitting she likes me as a teacher."
    "Why?"
    "I don’t work with her schedule. I don’t do what she asks or wants me to do. Hell, I’m not even {i}nice{/i} to her the vast majority of the time. "
    "So why am I preferred over all of the people who were handpicked for the sole purpose of educating her?"
    "A small part of me thinks that it might be because Touka isn’t really what her family and upbringing have turned her into."
    "That part of me is wrong, though."
    "Touka is who she is and doesn’t seem to inherently {i}dislike{/i} that."
    "But, somehow, having everything she could ever want served to her on a silver platter just...isn’t enough for some strange reason."
    "I’m not sure why."

    scene nightsky
    with dissolve2
    play music "thesleepingcity.mp3"

    "But I’m also not sure why she asks me to walk her back to the dorm instead of just taking a cab or limo, and here I am- "

    if bonus == True:
        "Fighting off the return of the cold alongside the desire to defile one of the closest things to perfection this horrible world has ever spit out."
        "I won’t, of course."
        "Not unless she wants me to."
        "But, you know what? Maybe she {i}does{/i} want me to."
        "Maybe {i}that’s{/i} why she apparently “likes” me so much. "
        "It has nothing to do with my skills as a teacher or the way I can make her flustered by simply calling her the wrong name a few times in a row."
        "It’s the power I possess- and how she knows that her livelihood outside of the bubble she’s grown up in is entirely within my hands."
        "I’m likely the first person she’s ever felt powerless against."
        "Maybe that powerlessness excites her."
    else:
        "Super chilly and mildly sad =/"

    scene toukataco9
    with dissolve2

    "Or maybe that’s just what I’m telling myself to fill the several inches of space between us with something less lonely."

    to "Thank you again for putting up with my family and me today. I’m sure it was awfully stressful having to deal with a group of women so much-"
    s "Better than me?"
    to "{i}Different{/i} from you."
    to "If we were to grade our respective performances at the arcade, I’m sure you would have emerged as the “best.” Would you not?"
    s "If only who we are as people could be quantified by something as simple as that."
    to "Yes, if only. Imagine how many hours I could have saved if all of my lessons were replaced by leisurely activities growing up."
    s "Do you ever feel like you sort of wasted your childhood, Touka?"

    scene toukataco10
    with dissolve

    to "That’s certainly a strange question to ask out of the blue."
    s "Your mom said something like that earlier. I was wondering if you felt that way as well."

    scene toukataco11
    with dissolve

    to "Hm."
    s "..."
    to "..."
    to "No."
    to "I wouldn’t say any of my childhood was wasted."
    to "Sure, I do wish there was a little more of {i}me{/i} choosing things rather than just allowing myself to be pushed in the directions my family {i}thought{/i} I wanted to be pushed in."
    to "But to say that any of that was a waste would be akin to saying that I’m not comfortable with the result of all of those years and all of that hard work."

    scene toukataco12
    with dissolve

    to "Do you think I’m a good person, Sensei?"
    s "I do."
    s "Annoyingly good, sometimes."
    to "I think I’m a good person as well."
    to "That’s why I don’t consider any of my early years wasted."
    to "Seeing as those years are over, though, there’s not much purpose in dwelling on them."
    to "And there’s not much purpose dwelling on the current years either."
    to "Only a small portion of my life will be spent in this state, you know. "
    to "I’ll be an adult for the vast majority of my time on this planet. So why would I not look toward the future instead of getting so hung up on the me of the past or the present?"
    to "As long as I can remain a good person, anything I endure will be worth it."

    scene toukataco13
    with dissolve

    to "And I assume there will be a fair bit I have to endure, what with you suddenly turning my existence into some form of entertainment for yourself and all."
    s "You’ve been spending far too much time with Yasu if you think you can just poke me into changing."
    to "I’m spending far too much time with Yasu regardless of whether I want you to change or not."
    s "You absolutely want me to change."
    to "A little change would be nice, yes."

    scene toukataco14
    with dissolve

    to "But I will accept you for who you are now as well. Because I know, deep down in this...{i}suspiciously hard{/i} chest of yours, there is a heart. "
    to "It is not as big as mine, nor is there as much room inside for love, but it exists. "
    to "And {i}I{/i} think you should stop pretending it doesn’t."
    s "..."
    to "Goodnight, Sensei."
    to "I had a nice time today."
    to "In fact, it was {i}so{/i} nice that I may even consider leaving my family behind for our next outing."
    s "At the very least, let me know in advance if they’re going to be there so I can mentally prepare to deal with more than one rich person."
    to "I’ll see what I can do."

    scene toukataco15
    with dissolve

    to "Goodnight! "
    s "What, you’re not going to invite me up?"
    to "Hahah..."
    to "Now {i}why{/i} would I do that?"
    s "..."
    to "{i}Goodnight,{/i} Sensei."
    to "Thank you again for a wonderful day."

    s "..."
    s "..."
    s "..."

    scene black
    with dissolve2

    "I go home."

    $ renpy.end_replay()
    $ touka_love += 3
    $ toukaspecial15p3 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukaarchery20:
    scene toukatsuneyoarchery1
    with fade
    play music "marshmallow.mp3"

    "I, once again, take it upon myself to intrude on Wakana’s domain in an effort to get closer to a girl who may one day own this entire city. "
    "She is joined, of course, by a girl who will likely never own anything apart from the most popular ramen shop in the entire old district (Out of what I can only assume is one.)"
    "And while they are certainly an odd pairing, they’re not without their similarities as well."
    "They both grew up sheltered. Neither one of them is good at socializing. {i}And{/i} they could probably kill me within a matter of minutes if they wanted to."

    scene toukatsuneyoarchery2
    with hpunch
    play sound "tsurune.mp3"

    t "Ha!"

    "Or seconds in Tsuneyo’s case. Touka’s team of assassins (That I definitely know she has) would probably take a little longer to properly coordinate."

    to "Almost there, Tsuneyo! Though, I can’t help but wonder if your shots would be any more accurate if you’d put less power behind them."

    scene toukatsuneyoarchery3
    with dissolve

    t "Weapons were made for inflicting harm. Normally upon other people with weapons."
    t "But in this case, my enemy is a circle. And so I will attack with every last bit of power I have."

    scene toukatsuneyoarchery4
    with dissolve

    t "I am Tsuneyo Tojo, slayer of shapes!"
    t "Ha!"

    scene toukatsuneyoarchery5
    with hpunch
    play sound "tsurune.mp3"

    t "Mm..."
    to "Oh my. That one managed to pierce straight through the wall."
    t "The wall is my enemy as well."
    s "Please don’t go destroying school property in front of me. I think I’m supposed to report it or something."

    scene toukatsuneyoarchery6
    with dissolve

    to "Oh, Sensei. Good morning. I was unaware you’d be joining us today."
    to "But I suppose I should have expected it on account of your newfound affinity for stalking me at my morning practices. "
    s "What?"
    to "I apologize. Did you {i}not{/i} recently come here to watch me, only to subsequently spend the day with my mother and then proceed to forget about me entirely?"
    s "I did. But why do you sound so bitter about this?"

    scene toukatsuneyoarchery7
    with dissolve

    t "The heart of a woman is a complicated thing. But the heart of a warrior is easy to understand. Shoot. Kill. Repeat. "
    t "Take aim at the shape before you...then steel your resolve and turn it into a tree."

    scene toukatsuneyoarchery8
    with hpunch
    play sound "tsurune.mp3"

    t "Ha!"
    to "It hit the wall again, didn’t it?"

    scene toukatsuneyoarchery9
    with dissolve

    t "Perhaps it is time for me to review the basics once more."
    to "Excellent idea, Tsuneyo. Why don’t you go have Miss Watabe teach you once more so I can spend the morning reminding our dear teacher to stop getting involved in my mother’s affairs?"
    t "Yes, Master. "
    to "And please stop calling me “Master.” Even if I {i}do{/i} enjoy the sound of it."

    scene toukatsuneyoarchery10
    with dissolve

    "Tsuneyo scans her surroundings to make sure the coast is clear before collecting her arrows (Or at least the few that didn't break) at the opposite end of the archery range."
    "Back on this side, however, it appears that I am in trouble?"

    to "Well? Do you have anything to say to me?"
    s "You...look very pretty today?"

    scene toukatsuneyoarchery11
    with dissolve

    to "Something I am {i}not{/i} already aware of?"
    s "Are you...looking for an apology or something? What’s going on here?"

    scene toukatsuneyoarchery12
    with dissolve

    to "That’s what I would like to know. Why are you suddenly so...gung-ho in terms of watching my morning practices? You hardly seem like the type to enjoy this sport."
    s "Are you only saying that because I'm a commoner?"

    scene toukatsuneyoarchery13
    with dissolve

    to "Yes. "
    to "But also because, at least from my perspective, it appears that your key interests are limited to flirting with the girls in class. And surely you wouldn’t flirt with {i}me{/i} while there are sharp objects around."

    "On second thought, maybe Touka’s team of assassins is closer than I previously believed."

    to "It would be one thing if you were to take an interest in kyudo, but any woman in my position would be reasonably put off by someone coming to just {i}watch{/i} for no reason at all."
    s "It seems unfair that your mom is allowed to but I’m not."
    to "My mother carried me inside of her body for nine months and then proceeded to nurture me afterward. Comparing yourself to her is just silly. "
    s "Fine. I guess I’ll just have to carry you around for nine months to make up for lost time. Come here, I’ll give you a ride back to the main building."

    scene toukatsuneyoarchery14
    with dissolve

    to "What do you want, Sensei? And why can’t it wait until I’m {i}not{/i} in the middle of morning practice? Disrupting one’s schedule for your own personal gain is exceptionally rude."
    s "I’m glad you asked, Tsuneyo. Because there’s something I’ve been wanting to talk to you about and now is the best time for me."
    to "Sorry, are you talking to me? Because Tsuneyo is still collecting her arrows and my name is {i}Touka.{/i} To-u-ka. Say it with me. To-"
    s "Come on, Tsuneyo. Let’s talk in the shade."

    scene toukatsuneyoarchery15
    with dissolve

    to "...Yes. Let’s do that."

    scene black
    with dissolve2

    "I convince Tsuneyo 2 to follow me behind the archery building so the two of us can talk without worrying about any rogue arrows or the possibility of being spotted with one another."
    "Not because I think anyone would assume something, but because there actually {i}is{/i} something I want to talk to Touka about and I don’t want to risk being interrupted."

    scene toukatsuneyoarchery16
    with dissolve2

    "But before that, I should try and clear up whatever misunderstanding she very obviously has about her mother and me."

    s "Just so you know, I haven’t boned your mom."

    scene toukatsuneyoarchery17
    with dissolve

    "There. That should take care of it. Now I can move on to-"

    to "{i}Why{/i} would you open the conversation like that? That was perhaps the worst possible way to get me to pay any attention to whatever it is you want to discuss today — which is apparently my mother."
    s "It’s not. Well, it is. Kind of. But I only opened like that because you’re clearly upset about me hanging out with her here and that is unfair to me — a man who came to here to see {i}you.{/i}"

    scene toukatsuneyoarchery18
    with dissolve

    to "I believe you. But that doesn’t change the fact that she is now caught up and interested in both your personal affairs {i}and{/i} mine."
    s "I thought you wanted her to be more interested in your “personal affairs” though? What with the two of you barely ever seeing each other and everything."

    scene toukatsuneyoarchery19
    with dissolve

    to "Yes, but not like {i}this.{/i} The ordeal with the apartment complex was meant to be something I handle on my own to show her I’m capable of taking on additional responsibilities. "
    to "Now, I’m being slowly pushed out of my own purchase all because she’s incapable of keeping her hands clean from anything that interests her. Which just so happens to be real estate and project management."
    s "No offense to you or your mom, but those are some pretty boring interests. "

    scene toukatsuneyoarchery20
    with dissolve

    to "To you, I’m sure. But people love what they love. And my mother has a hard time letting things go once she becomes absorbed in them."
    to "I’m not sure {i}how{/i} it happened this time, exactly- "
    to "But seeing as you just so happen to be the only resident of my complex and have been spending time with my mother recently, you can’t blame me for assuming you have something to do with this."

    scene toukatsuneyoarchery21
    with dissolve

    s "I mean...I won’t say I don’t have {i}anything{/i} to do with it. But I wish she’d stay out of this just as much as you do."

    scene toukatsuneyoarchery22
    with dissolve

    to "You do? Why? I was under the impression the two of you were working together to some extent. Did I misunderstand? "
    s "Probably. In fact, the only reason she’s “working” with me at all is because I can do something she can’t."
    to "Well, yes. That’s the only reason partnerships exist in the first place. There’d be no reason to work together on something one could accomplish on their own."
    to "But, and I apologize for how offensive this may sound, I highly doubt there is anything {i}you{/i} can do that my mother can not."
    s "It’s something that involves Chika."

    scene toukatsuneyoarchery23
    with dissolve

    to "Chika? How did she get wrapped up in all of this? I was unaware you were even telling anyone about the building."
    s "Has Tsubasa really not told you anything?"
    to "Not really, no. She did mention something about a plan for leasing the remaining rooms out, but I’m not privy to the specifics. "
    to "And seeing as the complex is technically owned by the Tsukioka Foundation and not specifically {i}me,{/i} my hands are tied. She can do whatever she wants with this listing and I can’t stop her."
    to "I actually don’t even have to be {i}informed.{/i} So, unless she goes out of her way to specifically advise me of her plans, I’ll remain in the dark altogether."
    s "Can {i}I{/i} advise you of her plans? Or will you go and tell her that I came clean right away and destroy the rapport I have with her?"
    to "Is there any particular reason you need to continue building a rapport with her?"
    s "Yes. But I can’t tell you what it is until you’re older."
    to "..."
    s "..."

    scene toukatsuneyoarchery24
    with dissolve

    to "You’re a disgusting man. You do know this, right?"

    scene toukatsuneyoarchery25
    with dissolve

    s "Yeah. Just wait until you hear the rest, though."
    s "Like I said, the reason Tsubasa is suddenly so interested in this building isn’t because of me at all. It’s because of Chika and her sister."
    s "Your mom is unhappy with the condition of the building they’re living in-"
    to "And for good reason. That apartment is held together by duct tape and Elmer’s glue. "
    s "But Chika doesn’t want to leave it since all of her childhood memories are there."

    scene toukatsuneyoarchery26
    with dissolve

    to "I see..."
    s "So now, there’s this huge plan where {i}I’m{/i} supposed to convince Chika to move into the building. But it came out of nowhere and I feel like I can’t even get {i}out{/i} of it because Tsubasa’s too...commanding."
    to "May I ask why you {i}want{/i} to get out of it? "

    scene toukatsuneyoarchery27
    with dissolve

    to "There’s more than enough room in that building for Chika. And I’d allow them to stay free of charge as I’m aware of Chinami’s condition and know that tragedy could strike at any moment."
    to "The closer she is to adequate care, the safer she’ll-"
    s "Chika...kind of thinks that we’re dating."

    scene toukatsuneyoarchery28
    with dissolve

    to "..."
    s "..."
    to "And...{i}why{/i} does she think that, exactly?"
    s "..."
    to "..."
    to "I see."
    s "If I ask her to come live in the same building as me, it’ll turn into a whole thing. Like, yeah, I could probably make it happen under the guise of it all being real, but-"
    to "How long has she thought this, exactly?"
    s "..."
    to "Long?"

    scene toukatsuneyoarchery29
    with dissolve

    s "...Yeah."
    to "And you never bothered clearing things up with her?"
    s "No...and it’s kind of too late at this point, so..."
    s "I’ve sort of just...accepted it."
    to "Hm..."
    to "I suddenly understand your resistance."
    s "..."
    to "If Chika remains distant from you, it will be easier to continue shying away from the true nature of your relationship and what that means to {i}you{/i} as opposed to what it means to {i}her.{/i}"
    to "And...just based on what I’ve seen and heard...would likely prevent her from questioning you in the event that {i}others{/i} who may think the same thing {i}she{/i} does wind up in that building as well."
    to "People like Maya. Or Makoto."
    s "Did Makoto tell you?"
    to "Not directly. But it wasn’t hard to pick up on once the two of us started growing closer."
    s "Gotcha....that’s basically the situation, then. And I feel weird talking to you about it like this, but I really just don’t know what else I’m supposed to do."

    scene toukatsuneyoarchery30
    with dissolve

    to "Do you at least understand how {i}I{/i} feel having to be the one to talk about this with you?"
    s "Not really, no."
    to "Of course you don’t. Because it is more convenient for you to {i}not{/i} understand that. Plus, you are an idiot."
    to "But instead of spelling it out for you, I’ll play my part and offer you a piece of advice instead."
    to "If that is okay with you, of course. I could just keep my mouth closed and let you sort this out with my mother. But good luck trying to get her to cease fire in {i}any{/i} regard whatsoever."
    s "What do you think I should do?"
    to "You’re not going to like it. I will warn you right now. Do you still want to hear it regardless?"
    s "It’s not like I’ve got any other ideas. And, like you said, the chances of me getting Tsubasa to back down are slim to none."

    scene toukatsuneyoarchery31
    with dissolve

    to "I see."
    to "Then, I think you need to grow up."
    to "There are far greater problems in this world than whether or not you break the heart of a girl in the springtime of her youth. "
    to "You’re an adult and you should act like one. Which means having a backbone and making your own decisions instead of waiting for everyone else to change and mold every given situation to fit your needs."
    to "The fact of the matter is, Chika and her sister will be safer in a new housing complex."
    to "Will that make your life harder and a bit less convenient? Yes. But I ask you to think of how much better it will make {i}their{/i} lives since you apparently haven’t done that of your own volition just yet."
    s "I’m not sure I follow. Getting Chika to move in wouldn’t require breaking her heart. It would be the exact opposite. Asking her to come live there would make her extremely happy."

    scene toukatsuneyoarchery32
    with dissolve

    to "At first, yes. "
    to "But how would she feel the moment she sees someone else leaving your room? {i}That’s{/i} what you’re afraid of, isn’t it?"
    to "No matter how secretive you be, she’ll always be right down the hall. And she could catch you at any moment. "
    s "I haven’t even...done anything like that in the apartment, though."

    scene toukatsuneyoarchery33
    with dissolve

    to "Then gaining a few new neighbors wouldn’t disrupt your habits at all. It would just prevent new ones from forming. Which, in this context, sounds like it could be a good thing."
    s "..."
    to "I told you you wouldn’t like what I had to say. Every last bit of it makes {i}your{/i} life worse and everyone {i}else’s{/i} life better. That is essentially a narcissist’s Kryptonite. "
    to "Did I say that correctly? {i}Kryptonite?{/i} That’s the superhero gem, right? "
    s "You know, you really do take after your mom. "
    to "Because I’m beautiful and smart?"
    s "Sure, there are those things. But it’s mostly because you’ve both found a way to put yourself on a pedestal miles above everyone else without seeming entirely pompous about it."
    to "Generosity goes a long way in bringing people over to one’s side. You should try it some time."

    scene toukatsuneyoarchery34
    with dissolve

    s "Sounds exhausting."
    to "Oh...you don’t know the half of it..."

    scene black
    with dissolve2

    "As I leave the archery range, I feel a little bad about emptying my problems out all over Touka. "
    "But, for the sake of creating another fun new comparison that may or may not be symbolic in some sort of way, I will now do several things."
    "The first of which is having you imagine that my problems are a liquid."
    "The second is recalling what I said moments ago about how similar Touka and her mother are."
    "The third is forgetting that."
    "And the fourth is wrapping back around to my liquid problems and finalizing the comparison by telling you Tsubasa’s skin is hydrophobic."
    "Her daughter’s is not."

    $ renpy.end_replay()
    $ toukaarchery20 = True
    $ touka_love += 1
    stop music fadeout 7.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label toukadorm25p1:
    play sound "knock.mp3"

    "I knock on Touka’s door and don’t have anything creative to say about it."

    to "C-"

    play sound "knock.mp3"

    "So I decide to knock a second time just to make things slightly more interesting."

    to "..."
    to "Come in?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I save my third knock for when my creativity fully dies and Touka will no longer let me into her room."
    "At this rate, something like that could happen any day."

    scene toukawalk1
    with dissolve2

    "Because, while the two of us can have serious conversations on occasion (Normally while I’m interrupting her morning practices), she’s still {i}Touka{/i} at the end of the day."
    "She’s not on the same level as everyone else and, even if she {i}does{/i} like (or tolerate) me now, that could change at any given moment."
    "Her family will always come first because that’s just...the type of family she’s from."
    "And no matter what I do (or want to do) to her, nothing will change that."
    "Probably."

    to "I believe this is the part where I’m supposed to act surprised by your arrival, but your impatience reared its head at the door and I was able to realize it was you a bit earlier than normal today."
    s "Good day to you as well, madam."
    s "Why are you all dressed up? It’s been a while since I’ve seen you in that outfit."

    scene toukawalk2
    with dissolve

    to "I abstain from wearing it around the city as I’ve come to realize it’s a bit too {i}lavish{/i} to be perceived as “normal.” Plus, dressing in commoner-attire prevents me from being attacked."
    to "This dress is worth more than your home and I’d prefer it remains both {i}on{/i} my body and {i}out{/i} of the wrong person’s hands."
    s "So what I’m hearing is the “right” person would be able to get their hands on said body so long as you remain clothed."
    to "Of course that’s what you’re hearing. You are a pervert. And to that I say- please back away. I am carrying mace."
    s "Will do. But you still haven’t told me what the occasion is."

    scene toukawalk3
    with dissolve

    to "I must not have received the memo advising me that I must inform you of my every action. Please forgive me."
    s "It’s okay, you’re forgiven. What’s going on?"
    to "..."
    s "Do I need to send a second memo?"

    scene toukawalk4
    with dissolve

    to "I’m on my way to the manor to take care of some business with my mother. And I {i}intended{/i} to go there alone, but I now feel pressured to invite you on account of how “clingy” you are tonight."
    s "I’m not clingy. I just miss you and appreciate all you do for both the class and me."

    scene toukawalk5
    with dissolve

    to "You absolutely do not. But I will allow you to come regardless. I do ask that you remain on your best behavior, though. From what I understand, this is going to be a serious meeting."
    s "Serious? You don’t think it’s about the apartment complex, do you?"

    scene toukawalk6
    with dissolve

    to "I do not. Because, and brace yourself for this, Sensei- the world does not revolve around you. The Tsukioka Foundation has much more to worry about than some trivial side project I took up."
    s "The world doesn’t revolve around your family either. Which is why you should all surrender your wealth to me and let me take up the mantle as the new Tsukioka figurehead."

    scene toukawalk5
    with dissolve

    to "If you’re going to propose, at least do it in a proper, less self-absorbed way. Of course I won’t say yes to that."
    s "You’re sure it’s cool if I come with you? I don’t want to interrupt whatever “important business” you have going on. Especially now that I know it’s business that doesn’t directly pertain to me."

    scene toukawalk2
    with dissolve

    to "I’m sure it will be fine. The worst case scenario is that you’ll be forced to wait out the night in a private room while I take care of whatever it is that needs to be done."
    to "But it would be less like “solitary confinement” and more like being sequestered in a three-star Holiday Inn Express."

    scene toukawalk7
    with dissolve2

    "This message has been brought to you in part by Holiday Inn Express."
    "At Holiday Inn Express hotels, we keep it simple...and smart."
    "Book your stay today."

    scene toukawalk2
    with dissolve2
    stop music fadeout 20.0

    s "That doesn’t sound so bad. I’ve always wanted to stay in a Holiday Inn Express."
    to "Why?"
    s "Because they keep it simple and smart."
    to "Oh. Well, okay. I suppose this works out quite well then."

    scene black
    with dissolve2

    to "We mustn’t delay any further, though. My limousine is already waiting outside."
    to "If you’d please follow me, Sensei..."

    "Touka reaches out her hand to guide me but, when I attempt to grab it, she takes it back and makes me look like an idiot."
    "I have no idea who taught her this, but my newest goal in life is to find them and eliminate them."
    "Or, if it is someone I am actively having sex with (Which is very possible from a sheer mathematic point of view), to eliminate them in a {i}different{/i} way."
    "With my penis."
    "What I mean is that I’m going to have really violent sex with them."
    "But anyway, Touka and I hop into the limo and, after a smooth and quiet ride over to the manor, we begin to make our way through an area that is becoming rather familiar to me."

    scene toukawalk8
    with dissolve2
    play music "tsukiokamanor.mp3" fadein 3.0

    "How that happened is still a little strange but, then again, what isn’t nowadays?"
    "If you told me two years ago that I’d one day be memorizing the layout of a rich girl’s mansion, I probably would have assumed your name was Ayane and then asked you to stop speaking with my dick in your mouth."
    "But that’s not the case at all. In fact, my dick rarely finds its way into Ayane’s mouth at all anymore because we’re either too busy having real sex like human beings or learning things about the end of the world."
    "I wonder for a moment how long it will be before Touka makes it to that point."
    "Not the sex part — the latter. But of course, I wholeheartedly welcome the idea of having sex with her prior to that."
    "And with the way she smiles at me sometimes, I feel as if that’s not all that far away."
    "I know it’s just politeness, though."
    "I know this is how she was raised."
    "I know there must have been countless men and women before me who were shown this same exact smile in this same exact dress."
    "And I know it always went nowhere."
    "But that doesn’t stop me from wanting to be an outlier."
    "And it can not quell the incessant fantasies of tearing that dress off of her."

    to "You’re thinking something inappropriate, aren’t you?"
    s "Me? Never."

    scene toukawalk9
    with dissolve

    to "Perhaps I should just sequester you now and save myself the mace?"
    s "Yeah...that would probably be best for everyone."
    to "You really are like a child sometimes, Sensei."

    scene toukawalk10
    with dissolve

    s "Meanwhile, I have a hard time believing you {i}ever{/i} acted like a child. At least not in this setting. The real world is another story entirely."
    to "I’m getting there. But you’re not far off in your assumption of how I was at home."

    scene toukawalk11
    with dissolve

    to "For as long as I can remember, I’ve been showered with praise. For my behavior...My talent...My understanding of the role that I was born into."
    to "But of course, such praise was not simply gifted to me. Everything I {i}was{/i} and everything I {i}am{/i} was earned."
    to "I lost count of how many different lessons I’ve taken over the years. And for things that won’t even matter, no less."
    to "How to hold a fork. How to play piano. The {i}names{/i} of different {i}types{/i} of forks. French. The {i}position{/i} forks need to be placed in."

    scene toukawalk12
    with dissolve

    to "There were so many lessons about forks! Why?!"
    s "Being rich sounds weird."

    scene toukawalk13
    with dissolve

    to "It is so incredibly strange at times. Especially in hindsight. And I sometimes find myself envying my sister as her schedule is significantly less packed than mine was at her age."

    scene toukawalk11
    with dissolve

    to "But again, this was the role that I was born into. And as the eldest daughter of Tomonori and Tsubasa Tsukioka, there are certain things expected of me."
    to "I suppose you could even say I lack the freedom to discover who I am on my own as it was already predetermined the moment I entered this world."
    to "And yet...I do not hate it."
    s "You don’t?"
    to "I don’t."

    scene toukawalk14
    with dissolve

    to "Perhaps it’s due to my future being figuratively beaten into me since I was young, but I never fancied or even...I suppose {i}comprehended{/i} any other sort of life."
    to "Without any idea of what I {i}could{/i} want, I was left to only want {i}one{/i} thing. And that thing is plastered to a slowly rising sun that will one day shine for me and no one else."
    s "As if it doesn’t shine for you already."

    scene toukawalk15
    with dissolve

    to "I understand why you’d say that. To you and many others, it must seem that I already have everything I could ever want."
    to "But what can not be seen is my want for {i}wanting{/i} something."
    to "What can not be seen is the cage that keeps me from taking flight."
    to "The most depressing part is that the door of that cage has been open this entire time. And I’ve been perfectly capable of leaving it."
    to "But among a ruthless regime of fork-based lessons and lectures on etiquette, I was also taught that I {i}wanted{/i} to stay inside of that cage...so there was never a reason to leave at all."
    to "And now, it’s so ingrained into the way I think that it’s as if I’ve inherited every last bit of my mother. And my father. And those who lived before me."
    to "Decades and decades of customs and expectations and {i}rules{/i} flow through my blood like crocodiles in the Nile."
    to "They’re simply a part of me now. They can not be removed, nor do I {i}want{/i} them to be. But I know their existence was not of my own choosing, which makes it all feel a bit false at times."

    scene toukawalk14
    with dissolve

    to "Nothing against crocodiles, of course. I’m sure they love their home just as much as I do."
    s "Isn’t it...boring, though? Already knowing your future?"

    scene toukawalk15
    with dissolve

    to "It can be."
    to "But my life is not entirely devoid of excitement now that you and the others have nestled into it."

    scene black
    with dissolve2

    "Touka stops walking and I don’t notice right away."
    "But when I turn around, she isn’t gazing up at the moon or...wistfully watching the stars and correlating them to some grand idea of how expansive the universe is."
    "She’s looking at me."

    scene toukawalk16
    with dissolve2

    "She’s looking at something that stood beneath her cage and shouted catcalls at her until she was forced to leave it."
    "And it wasn’t until she was outside that she realized just how expansive that universe really is."
    "It wasn’t the stars at all."
    "It was all of us."

    to "..."
    s "..."
    s "What? Why are you looking at me like that?"
    to "Like what?"
    s "Like {i}that.{/i} Like you’re-"
    to "My mother?"
    s "..."

    scene toukawalk17
    with dissolve

    to "Ahh...you really have been spending more time with her lately, haven’t you?"

    scene toukawalk18
    with dissolve

    to "Should I be worried?"
    s "What would you have to worry about?"
    to "That you’ll see just how...{i}unoriginal{/i} I am."
    s "I mean...don’t get me wrong. You two clearly have a lot in common. But there’s plenty I’ve seen in you that I’ve yet to see in her."
    to "I’m assuming those sample sizes are rather skewed in my favor, though. And I wonder if you’ll say the same when you come to know her just as well."
    s "I doubt Tsubasa is the type to {i}let{/i} anyone know her that well."
    to "And I am?"
    s "So far. You might also be capable of sly, behind-the-scenes manipulation- but you’ll need way more practice if you’re ever going to get to her level."

    scene toukawalk19
    with dissolve

    to "You know her better than I thought."
    to "Her intentions are good, though. And I trust her judgement entirely."
    s "It {i}does{/i} seem that way most of the time. The way she goes about things just makes me feel a little weird. Like I’m the sidekick to the world’s most lawfully good vigilante or something."
    to "Hmm...I’m not sure if you’re fit to be her “sidekick” just yet."
    to "But I wouldn’t mind you being mine."
    s "Oh yeah? And what would my duties include? Making sure you don’t have any sort of original thought? Filtering all your opinions through your mother and trying to get them approved?"
    to "Ha ha ha. Clever. But I’ll have you know that sharing the same values and ideals as her does not make me a complete clone. I’m still Touka Tsukioka when all is said and done."
    s "Until your corporate robo-family asks you to be something else."
    to "They will not ask. They will {i}expect.{/i} And I will likely do as they want as that is how I was grown."
    s "With the one exception being an arranged marriage?"

    scene toukawalk20
    with dissolve

    to "I...beg your pardon?"
    s "Your mom told me a while ago that they had several “suitors” picked out for you, but that you never seemed comfortable with the idea."

    scene toukawalk21
    with dissolve

    to "Why on earth would she tell you that? How did that topic even come up?"
    s "No clue. But if you’re so dead set on playing the role, why was that an issue?"

    scene toukawalk22
    with dissolve

    to "Hah..."
    to "It wasn’t."
    s "What do you mean?"

    scene toukawalk23
    with dissolve

    to "I mean that I would have followed through with it if it needed to be done."
    to "As the family’s heir, it is my responsibility that we maintain our status once my parents pass away. And if joining families with another influential house would secure such a status, I would comply."
    s "Then why-"
    to "Because you do not always have to be “comfortable” with something to know that it must be done. That is especially true for people in power."
    to "If my family had always taken the “comfortable” path, we’d be nowhere near where we are today."
    s "So...what? You’d just let some random guy from another family knock you up for {i}status?{/i}"
    to "Would you rather it be you?"
    s "That...wait. No. That’s not what I was-"

    scene toukawalk24
    with dissolve

    to "As much as I appreciate my mother’s kindness and consideration, I would do whatever I believed to be best for my family."

    scene toukawalk25
    with dissolve

    to "But...thankfully...I don’t {i}have{/i} to."
    to "You see, there’s no one here who could elevate our family any further. At least not with the city closed-off. So I’m free to marry someone I love instead."
    to "I just wonder if I can ever find it in myself to do that."

    scene toukawalk26
    with dissolve

    to "To be completely honest, I’m not sure I’d make a very good wife in the first place. A mother, perhaps. But I’m not sure if I could tolerate someone like you pestering me all day, every day."
    s "It sounds fun, though. Right?"

    scene toukawalk27
    with dissolve

    to "{i}Fun?{/i} Please. That sounds like the single most exhausting thing I’ve ever heard of."
    s "And that’s not even counting what we’d get up to at {i}night.{/i}"

    scene toukawalk28
    with dissolve

    to "Are you sure I’m not a bit too {i}womanly{/i} for your tastes? What, with you fancying girls of {i}Maya’s{/i} stature and all."
    s "That was...not a thing you were supposed to see."

    scene toukawalk29
    with dissolve

    to "But I did. And now I know, so ha."
    s "Touka..."
    to "Sensei, if you’re {i}that{/i} desperate to marry into the family, perhaps Tsukasa would be more in line with your...{i}tastes?{/i}"
    s "Tsukasa? Just what kind of person do you think I am?"
    to "Someone who should not be allowed within five miles of a school."
    s "Touka, I am not going to {i}marry{/i} Tsukasa. And I really wish you and your mom would stop trying to-"
    tk "Peasant!"

    $ renpy.end_replay()
    $ toukadorm25p1 = True
    $ touka_love += 1

    jump toukadorm25p2

label toukadorm25p2:
    if _in_replay:
        play music "tsukiokamanor.mp3"

    scene toukawalktwo1
    with fade

    tk "You would be {i}foolish{/i} not to marry me! Only an imbecile would deny such a once-in-a-lifetime opportunity!"
    to "Tsukasa?! What are you doing out here so late?! And...what are you wearing?!"

    scene toukawalktwo2
    with dissolve

    tk "And you! Heir or not, I will not allow you to ridicule me just because you’re older than I am! I’m just as fit to lead this family as you are!"
    to "That’s not what I was-"
    tk "Silence!"

    scene toukawalktwo3
    with dissolve

    tk "It’s just as Jeeves said. You and Mother are always looking down on me and treating me like some sort of...pawn! "
    s "Technically, that is not what I said at all. It does involve the same people, though."
    tk "Silence, Jeeves. I heard all I needed to hear from across the stream. And I do not know who this “Maya” person is, but if I fit your “tastes,” I would be happy to marry you."

    scene toukawalktwo4
    with dissolve

    to "Tsukasa! That was a joke!"
    tk "Mm...Maybe “happy” isn’t the right word to describe how I’d feel about marrying you. But if it would get Onee-sama and Mother to begin taking me seriously, so be it."
    s "I feel like marrying me is the worst possible way to get {i}anyone{/i} to take you seriously. Also, you are a child."
    tk "In the days of old, it was common practice for men of your age to take girls like me as a bride! Because, while I may not be capable of bearing children now, those days are not far away!"
    s "Okay. Time to leave."

    scene toukawalktwo1
    with dissolve

    tk "You are going nowhere!"

    scene black
    with dissolve2

    "Tsukasa marches forward and pushes me aside so she can stand near her sister. "
    "Just to clarify, though, she is not strong enough to physically move me on her own. I just decide to do the right thing and step out of the way. I swear I’m not actually weak."

    scene toukawalktwo5
    with dissolve2

    to "Tsukasa, what on earth are you doing wandering around dressed like that? "
    tk "{i}I{/i} am getting engaged."
    s "{i}No,{/i} you are not."
    tk "And {i}also,{/i} I am on my way to meet Mother in the pool area. Which, according to the schedule, {i}you{/i} should be doing as well. So it appears that {i}you{/i} are the one not properly dressed, dear sister."

    scene toukawalktwo6
    with dissolve

    to "The...{i}pool{/i} area? But Mother informed me this was an important family meeting that could take up the rest of the night."
    tk "Is bonding with your family not “important” to you, Onee-sama? Or are you just too busy flirting with my fiance to care?"
    s "I really don’t like how this is a thing now."

    scene toukawalktwo7
    with dissolve

    to "Stop calling Sensei your fiance! It’s incredibly disrespectful and inconsiderate of his feelings!"
    tk "But it was {i}your{/i} idea. And you never make mistakes because you’re the apple of Mother’s eye and {i}I{/i} am just the butt of all of your jokes."
    to "Tsukasa!"
    tk "I demand an apology. If I receive one, I will rescind my offer to marry your teacher and will return to simply campaigning for him to become my butler instead."
    tk "And of course, you will need to apologize to Jeeves as well for breaking his poor, peasant heart."

    scene toukawalktwo8
    with dissolve

    to "Weren’t you ever taught to abstain from eavesdropping on the conversations of close family members?"
    tk "{i}No.{/i} I was too busy learning about forks."

    scene toukawalktwo9
    with dissolve

    to "Hah...I am sorry for including you in a conversation that was not, and I reiterate, meant to be a joke at {i}your{/i} expense, but Sensei’s."
    tk "Apology not accepted. Stating that it would be a joke at {i}his{/i} expense implies that you do not believe I am the exceptional marriage candidate we all know I am."
    to "{i}No...{/i}it implies that his taste in women is even {i}less{/i} acceptable than it already is."

    scene toukawalktwo10
    with dissolve

    tk "Is Jeeves a lolicon?"
    to "Tsukasa. Mind your manners. He’s still your elder."
    tk "Barely. Like I said, in the days of old, it wasn’t uncommon for men of his age to-"

    scene toukawalktwo11
    with hpunch

    to "Enough!"
    tk "Onee...sama?"

    scene toukawalktwo12
    with dissolve

    to "I apologize for raising my voice, but this discussion is over. It has already carried on far longer than it was meant to and now {i}I{/i} am beginning to get uncomfortable."
    to "And Tsukasa, even {i}if{/i} you are on your way to meet Mother, you must not dress in such attire {i}prior{/i} to entering the pool room. It is inappropriate and unladylike. "

    scene toukawalktwo13
    with dissolve

    tk "But she said it was okay!"
    to "You are likely misremembering. But seeing as I must meet with her as well, I can find out myself."

    scene toukawalktwo14
    with dissolve

    to "Come. Both of you. "
    tk "Jeeves too?! But he isn’t even a part of the family yet!"

    scene toukawalktwo15
    with dissolve

    s "..."
    s "Was the “yet” really necessary?"

    scene black
    with dissolve2
    stop music fadeout 8.0

    "I follow the girls down a familiar path and several subsequent {i}un{/i}familiar passageways that I’m sure will ultimately lead to somewhere else I’ve been before."
    "Unless the Tsukiokas have multiple pool rooms of course which, honestly, wouldn’t be all that surprising."
    "What {i}is{/i} surprising, though, is Touka’s sudden shift in demeanor. "
    "I doubt it’s jealousy or fear that I would {i}actually{/i} take her sister’s uncallused hand in marriage, but it’s definitely {i}something.{/i}"
    "But whatever that {i}something{/i} is dissipates the moment chlorine meets our nostrils."
    "And she slinks back into the perfect girl she always is...for she never figured out how to survive as anything else."

    scene toukawalktwo16
    with dissolve2
    play music "marshmallow.mp3"

    tb "Oh! Girls. And Ak- {i}ahem.{/i} And Sensei is here as well. What a pleasant surprise."
    s "Nice save."
    tk "Mother! Tell Onee-sama it’s okay for me to walk around in my bathing suit! She didn’t believe me!"
    to "Um...Mother? What exactly is going on here? I was under the assumption we had important matters to take care of tonight."
    tb "Is spending time with your family not important to you, dear?"

    scene toukawalktwo17
    with dissolve

    tk "Ha. It’s just as I said. {i}You’re{/i} the only one here who doesn’t understand the situation, Onee-sama. And you call yourself a Tsukioka. "
    to "It’s not that! I adore the brief moments we spend together!"
    to "But as Tsukasa says, there’s something I’m not understanding about this. Why would you make it sound like there was a formal meeting tonight?"
    to "Did an esteemed guest...cancel? Was it something along those lines? I apologize for questioning you so directly, I just can’t seem to wrap my head around any of this."
    to "Also, I do hope it’s okay that I brought Sensei along as well. I have already warned him that he may need to be locked away for the duration of our talk tonight."
    tb "Locked away?"

    scene toukawalktwo18
    with fade

    tb "Now, why would we go and do something like that to such a valued visitor?"
    s "I apologize in advance for staring. I can’t help it."
    tb "And I apologize for making things {i}difficult{/i} for you. If I had known beforehand that you were coming, I would have worn something a bit less...revealing. "
    to "The reason I expect he’ll need to be secluded is that, despite the...attire required for tonight’s discussion, I’m sure we’ll still be going over matters that those on the outside must not-"

    scene toukawalktwo19
    with dissolve

    tb "There is no “discussion,” dear. I lied to you because I wanted this to be a surprise."
    to "You...what?"

    scene toukawalktwo20
    with dissolve

    tb "It was recently pointed out to me that my responsibilities with the foundation may have been...getting in the way of our relationship, so to speak."
    tb "So I took it upon myself to arrange a night for the three of us to bond for several hours — free from the worries of what may happen to the company in the meantime. "
    tb "But I see now that, in doing so, I may have unintentionally gotten in the way of {i}another{/i} relationship of yours."

    scene toukawalktwo21
    with fade

    to "In the way? Of course not. You’ve given me so much that you could never possibly be in the way of-"
    tb "Touka, darling, I believe that dress might be cutting off your circulation as I thought I made it {i}pretty{/i} clear just now that there is no such need for formalities tonight. "
    tb "Instead of taking up our normal places on the ladder, let us simply be mother, daughters, and...I’m sorry, what should we refer to Sensei as here?"

    scene toukawalktwo22
    with dissolve

    to "Unneeded."
    tk "Cannonball!"
    tb "No “cannonballs,” Tsukasa. You’ll hurt yourself."

    play sound "water1.mp3"

    tk "Tch. What use is Japan’s greatest medical staff if we’re unable to reap the benefits of it?"
    s "Should I go lock myself in your Holiday Inn Express?"
    to "You are aware it is not an actual Holiday Inn Express, aren’t you?"
    tb "Instead of that, why doesn’t he just join us in the water? Seeing as your father was unable to attend, he might be an adequate stand-in."

    scene toukawalktwo23
    with dissolve

    s "That won’t be necessary. I’m not-"
    to "..."
    s "..."

    scene toukawalktwo24
    with hpunch

    s "I’m not all that fond of swimming in the first place."
    to "Can you at least make your staring less glaringly obvious? Pun somewhat intended."
    tb "Well, I’d feel horrible just having him sit around and {i}watch{/i} so..."
    tb "Oh! Here’s an idea. How about I spend some time alone with Tsukasa now and you and I can reconvene once Sensei heads home for the night?"
    tb "Assuming he is not staying in our “Holiday Inn” of course."

    scene toukawalktwo25
    with dissolve

    to "But I can’t just walk away from you after you went through the hassle of rearranging your entire schedule for our sake. "
    tb "It won’t be walking away, darling. Why not show Sensei the sauna? Or perhaps stop by the buffet on the way to one of our many terraces?"
    s "I don’t mean to spoil the mood, but this is starting to sound more and more like a Holiday Inn as time goes by."
    to "Will that not offend you after extending such a gesture? Because, as much as I appreciate the opportunity-"
    tb "Touka, go have fun. You and I will see each other later tonight. I’ll stay with Tsukasa for now."
    tk "Hooray! I get Mother all to myself while Onee-sama spends time with a commoner! "

    scene toukawalktwo26
    with dissolve

    to "It’s beginning to sound as if we don’t have much of a say in the matter."
    s "Oh no. Whatever shall we do in a giant mansion filled with everything we could ever possibly want?"

    scene toukawalktwo27
    with dissolve

    to "Good question. Well...the sauna is a no from me as I’d have to leave my mace behind. And I’ve seen the terraces a good thousand times already, so..."

    scene toukawalktwo28
    with dissolve

    to "Perhaps we could go have a little fun somewhere {i}private?{/i}"
    s "..."
    to "..."
    s "There is absolutely no way that means what I want it to mean."
    to "Oh, we’ll see about that..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    stop music
    play sound "static.mp3"
    scene toukawalktwo29 with flash
    stop sound
    play music "rapid.mp3"

    "I was right."

    to "At long last, Sensei...I can show you the true power of the Tsukioka family that has been handed down from generation to generation."

    scene toukawalktwo30
    with dissolve

    s "Something, something bloodlines and hidden power. "
    s "I’m not afraid of you, Touka. "

    scene toukawalktwo29
    with dissolve

    to "But you should be. For I have not only replicated the dojo we had our first encounter in, but I have grown so familiar with it over time that it is now like a second home to me."
    s "You can’t have a second home inside of your home. That’s not how homes work."
    to "What I mean to say is that I will be able to use the environment to my advantage...while you, a man who has seen it but never {i}felt{/i} it, can do nothing to gain the upper hand."

    scene toukawalktwo31
    with fade

    s "That’s just what you think, {i}bitch.{/i}"

    scene toukawalktwo32
    with dissolve

    to "Well, that was unnecessarily rude. I was just trying to have a little fun in the same way Ayane’s told me the two of you have before."
    to "But if you are going to be that unpleasant and offensive, I’ll have you locked up right now."
    s "You and what army?"

    scene toukawalktwo33
    with dissolve

    to "Oh, yay! More roleplay."

    scene toukawalktwo34
    with dissolve

    to "Me and my own personal army of assassins, trained in a form of ninjutsu so ancient and so forgotten that they’re the only clan left in existence who knows it."
    s "Or at least that’s what {i}you{/i} think."

    scene toukawalktwo35
    with dissolve

    to "Ah! Are you saying {i}you{/i} know it as well?"
    s "That’s exactly what I’m..."
    to "..."
    to "Sensei?"

    scene toukawalktwo36
    with dissolve
    stop music fadeout 10.0

    s "Hah..."
    s "This just feels weird without Ayane. No offense, Touka."
    to "None taken. I didn’t want it to seem like I was trying to interfere in any memories you may have of her. I just believed it would help put you at ease in such an intimidating environment."

    scene toukawalktwo37
    with dissolve

    s "Thanks, Touka. But that really wasn’t necessary. I’m already starting to familiarize myself with this place. "
    s "Or at least I thought I was until I discovered several minutes ago that you’re now replicating locations from our daily lives inside of your mansion. "
    to "How else am I meant to practice interacting with others in such locations? This is the simplest method I could think of."
    s "You have issues."
    to "I do. But you’re not without issues as well, Sensei."
    s "Name one."
    to "Well, to start-"

    scene toukawalktwo38
    with dissolve

    to "You’ve let your guard down."
    s "I’ve what-"

    scene toukawalktwo39
    with hpunch

    to "HA!"

    scene black
    with hpunch
    play sound "thump.mp3"

    "........."
    "........"
    "......."
    "......"
    "....."
    "...."
    "..."
    ".."
    "."

    scene toukawalktwo40
    with dissolve2
    play music "kimitoakinobouken.mp3"

    "When I open my eyes, it’s as if I’m waking up from a dream."
    "My head is rested on the lap of a beautiful girl- who’s gently stroking my hair and completely ignoring the fact that she knocked me unconscious with a single kick just moments ago."
    "As my eyes lock onto hers, there is a moment of intense intimacy that can’t really compare to anything else."
    "But just as I think about summoning what little strength I have left to lift this aching head and kiss her, my world comes crashing down."

    play music "justbehappy.mp3"
    scene toukawalktwo41
    with hpunch
    play sound "slidedoor.mp3"

    "And what I mean by that is her family shows up."
    "But that’s okay because I was just making up all of that other stuff anyway."
    "To be honest, my head hurts way too much to even lift right now in the first place."
    "But I guess we can see how those two managed to misunderstand the situation before we dwell any further on that."

    tb "Oh my. Were we interrupting something?"
    tk "Onee-sama! What are you doing with my husband?! Wench!"

    scene toukawalktwo42
    with dissolve

    to "He is not your husband! He is my teacher! And I may or may not have unleashed my secret technique on him!"
    tb "Secret...technique?"
    tk "She’s been spending too much time with poor people. All they have is their imagination."
    s "Before anyone misunderstands, it was a {i}fighting{/i} technique. Nothing else went on in here. At least not while I was conscious."

    scene toukawalktwo43
    with dissolve

    to "{i}What do you think you’re insinuating?! Do I look like the type to do something so heinous to a sleeping person?!{/i}"
    s "Hey, I don’t know what kind of weird stuff you’re into."
    tb "Tsukasa, why don’t you go take a bath and get ready for bed? I’d like to make good on my promise and spend some time with your sister alone."
    tk "Okay, Mother. But can we do this again soon? I had fun."
    tb "We’ll see, dear. There’s a lot more work I need to catch up on first."

    scene toukawalktwo44
    with dissolve
    play sound "slidedoor.mp3"

    tb "Will you be much longer? I don’t want to intrude more than I already have."
    to "You haven’t intruded on anything! It really isn’t what it looks like! I just misjudged my own strength and knocked Sensei unconscious while sparring with him!"
    s "How long was I even out for?"

    scene toukawalktwo45
    with dissolve
    stop music fadeout 20.0

    to "An hour."
    s "And you didn’t...think of taking me to the hospital? Or getting me any sort of medical care apart from a lap pillow?"
    to "I did not. And stop whining."
    tb "Well, whenever you’re done, I’ll be waiting in my room — where I expect to hear a full explanation of why Tsukasa suddenly believes she is married."

    scene black
    with dissolve2

    to "Yes, Mother...And I apologize for having you walk in on-"

    if chikalust25 == True:
        tb "Don’t. "
        tb "I can assure you I have walked in on much worse."
    else:
        tb "There’s nothing to apologize for, dear. "
        tb "Just be glad it was {i}me{/i} and no one else."

    play sound "slidedoor.mp3"

    "Tsubasa leaves the room and Touka assists me in pulling my head off of her lap."
    "It’s a premature departure I really wish I could have avoided for a bit longer but, seeing as I’ve already interfered in at least two hours of mother-daughter time, I should probably get going."

    $ renpy.end_replay()
    $ toukadorm25p2 = True
    $ touka_love += 1

    jump toukadorm25p3

label toukadorm25p3:
    scene clearnightsky
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "And so another night ends with me only getting {i}slightly{/i} closer to her — but that’s par for the course when her entire life is built around a world that I have no part in."
    "I stare back at her mansion from the backseat of a ride that I am forced to take and remember just how far apart we are in almost every single way."
    "And how even in those few moments of feigned intimacy, where our bodies move closer together than they should ever be...that I am an outsider. "
    "I have been one from the start- and there is no way someone like me, who can’t stop plucking his feathers, could ever take a fledgling bird like her under my wing."
    "For even if I could fly, there is nothing I could show her that she can’t already see from the cage she was brought up in. "
    "After all, it’s miles higher than any of {i}us{/i} will ever reach."
    "You can look up as much you want — but I will hearken back to another recent metaphor involving a hole and reiterate the fact that ascension is far more difficult than its antonym."
    "She’s the one who will need to come down to us."
    "But she needs to {i}want{/i} it."
    "And I’m not quite sure if she ever will."

    limo "Arakawa-sama, if you’d be so kind as to inform me of your destination, I would be very grateful. The mistress did not tell me where you were headed tonight."
    s "I don’t really care, to be honest. You can drop me off wherever."
    limo "I can’t-"
    s "It’s fine, really. I’m not a big fan of cars in the first place."
    limo "I apologize for the inconvenience. "
    limo "You may exit the vehicle at your leisure."

    "The car screeches to a halt in the middle of nowhere and I remove myself from its metal stomach, half-digested from the acid that’s been dripping from my mind as it runs wild once more. "
    "Just, this time, the world alone remains in view."
    "There is no blackout nor subsequent confusion from an abrupt change in locale. "
    "I can feel my limbs and move my body. I can hear the sounds of the gravel beneath my feet as I walk off in a direction I only half-expect to be the right one."
    "And all the while, I wish that I was still in her lap."
    "I wish we could have looked at each other for more than a handful of seconds."
    "But it’s better that we didn’t."

    scene black
    with dissolve2

    "And it’s better that she’s now with someone who understands her instead of someone who simply {i}wants{/i} to."
    "For a moment, I envision these empty streets as the halls of a lavish manor. "
    "The streetlights are suits of armor. The stars, a chandelier. "
    "And the moon is the face of someone I wish to see — tragically gazing down from a perspective far more interesting than my own."
    "I’m sure it all looks small to her."

    scene toukabath1
    with dissolve2

    "And I’m sure that’s just the way she likes it."

    to "Hah...I needed this..."
    tb "Did you have a long day, dear?"
    to "“Long” doesn’t even begin to describe it. Every second with that man feels like an hour. And the sudden appearance of Tsukasa did not help very much either."

    scene toukabath2
    with dissolve

    to "I’m glad we wound up here instead of the pool. I likely would have drowned from exhaustion if I were to get in there right now."
    tb "I might not be a perfect mother, but even I wouldn’t let my eldest daughter drown right before my very eyes."

    scene toukabath3
    with dissolve

    to "But you would your youngest?"
    tb "Oh, stop. You know that’s not what I meant."
    to "Of course I do."

    scene toukabath4
    with dissolve

    to "But if you just {i}happened{/i} to look away for a moment or two, I can’t say I’d blame you."
    tb "Be nice. Tsukasa may be a handful, but she’s dealing with a lot right now."

    scene toukabath5
    with dissolve

    to "Is she? How so?"
    tb "It’s no fault of her own. It’s because of me."
    to "That can’t be true. You haven’t done anything at all."
    tb "I believe that’s...exactly the issue. Tsukasa’s been feeling...left out, I suppose. She isn’t as inherently accepting of my absence as you were at her age."
    to "Did she...tell you this? That seems rather mature for her."

    scene toukabath6
    with dissolve

    tb "Yes and no. There were some...words she shouted at me in the middle of a meeting. But it was Sensei who pointed out the meaning behind all of them as I struggled to wrap my head around it."
    to "Sensei? You mean...{i}my{/i} Sensei? He did that?"
    tb "Oh? You’re calling him {i}yours{/i} now? Perhaps I {i}was{/i} interrupting before, then."

    scene toukabath7
    with dissolve

    to "D...Don’t be ridiculous! It’s excruciatingly obvious that’s not what I meant. I just didn’t think he paid much attention to her at all."
    to "To think he’d notice something neither of us did despite his limited time with her is..."
    tb "Kind of impressive, right? "
    tb "I suppose an outsider’s perspective really helps sometimes. I can see now why your sister decided to marry him."

    scene toukabath8
    with dissolve

    to "Guh."
    tb "Would you mind explaining how that came about?"
    to "That...is the unfortunate result of a joke I made in poor taste earlier. Which is precisely why I normally abstain from comedy altogether. It is very much a weakness of mine."
    tb "Did it make you jealous hearing her say that?"

    scene toukabath9
    with dissolve

    to "What? Of course not. I just think she should behave around her elders and it irritates me that she’s able to be so...crass. It's as if she doesn’t have a care in the world."
    tb "So you’d accept if she {i}did{/i} become his betrothed?"

    scene toukabath10
    with dissolve

    to "Mother, just what exactly are you getting at? Why even joke about such a thing? "
    tb "Hahah! I suppose I’m just as weak when it comes to comedy as you are. "

    scene toukabath11
    with dissolve

    tb "I suppose we should just stick to what we do best and let those with less on their plates be the ones to provide the entertainment."
    tb "That said, your teacher really {i}is{/i} quite the character, isn’t he?"
    to "Well...yes. But how much time have you been spending with him exactly? Because there are certain...{i}things{/i} about him that I can’t imagine you’d brush off as...quirkiness."
    tb "Quite a lot, actually. We’re...{i}partners{/i} of sorts. Though, I doubt he’d say the same if you were to ask him."

    scene toukabath12
    with dissolve

    to "I didn’t need to. He came to {i}me{/i}."
    tb "Oh?"
    to "I know all about your little scheme to turn my apartment complex into a...re-homing site for the Chosokabe sisters. And I know about Sensei’s involvement in it as well."
    to "What I {i}wish{/i} I knew is why you neglected to provide me the specific details. "
    to "Unless this is just another of your {i}lies{/i}. I wouldn’t put it past you, given what you pulled tonight."
    tb "Are you...{i}upset{/i} with me?"

    scene toukabath13
    with dissolve

    to "No...it’s not that. I agree with everything you’ve done and I understand how...absorbed you become in certain things. I just feel as if I was robbed of a chance to impress you myself."
    tb "Touka, you don’t need to do something like that to impress me. Just...speaking your mind the way you’re doing right now is impressive."
    tb "I think that may be the first time you’ve ever spoken to me like that."

    scene toukabath14
    with dissolve

    to "Ah! Please excuse my temperament! It was not my intention to talk down on you, I just-"
    tb "It’s fine. You needn’t apologize. In fact, I wish you’d be honest like that more often."

    scene toukabath15
    with dissolve

    tb "It wasn’t my goal to raise you into a woman who just kneels before anyone with more {i}power{/i} than her. In fact, the most powerful of all are the ones who fight for what they believe in."
    tb "{i}That{/i} is what I want you to be — not a second Tsubasa Tsukioka. Though, I must say, I am quite flattered by just how much of myself I see in you."

    scene toukabath16
    with dissolve

    tb "You’re a beautiful young woman, Touka. And I’m sure you’ll be an even more beautiful figurehead one day."
    tb "And while we’re at it, I suppose I should also apologize for sticking my hands where they don’t belong. I simply wanted a better life for Chika and her sister."

    scene toukabath17
    with dissolve

    to "I know...which is why I said I agree with you. "
    to "Additionally, the reason I don’t speak to you in such an...uncouth way more often is that I simply admire everything you do and seldom hear anything I disagree with."
    to "It just felt a little bit like you didn’t trust me this time. That’s all. "
    tb "That’s not it at all, dear. I tried to involve you as much as I could. There are just certain aspects of Sensei’s involvement that would best be kept under wraps."
    to "I likely know about those as well."

    scene toukabath18
    with dissolve

    tb "You...do?"
    to "Sensei explained the whole situation to me. How his relationship with Chika is not...of the normal student-teacher variety."

    scene toukabath19
    with dissolve

    tb "He openly told you that?! Are you sure you didn’t just...discern this information on your own?"
    to "He omitted {i}some{/i} of the details, but...it was quite obvious what he was trying to say."

    scene toukabath20
    with dissolve

    tb "Ugh. Just when I was beginning to believe I understood him. What a confusing man he is."
    tb "The bright side to all of this, though, is that it means he trusts you. And that’s something that can be leveraged."

    scene toukabath21
    with dissolve

    to "Leveraged?..."
    tb "Not for anything improper, of course. It’s just information you can use to plot out your next action. "
    to "My next...what? I’m not sure what you mean by that. "
    to "Am I to take over the responsibilities of relocating the Chosokabe family in your stead?"
    tb "Of course not. I’m not trying to create more work for you when your schedule is already busy enough."
    tb "I simply mean that knowing he trusts you will make it easier for the two of you to sleep together. "
    to "..."
    tb "..."
    to "Can you please repeat that? I think there may be water in my ears."
    tb "You {i}do{/i} want to sleep with him, don’t you?"

    scene toukabath22
    with hpunch

    to "What?! Why?!....What?!"
    tb "There’s no need to yell, dear. You’re at the age where it’s completely natural to be thinking about things like that. "
    tb "Plus, it was written all over your face earlier. In fact, it’s written on there now as well."
    to "Have you gone mad?! What is happening right now?!"

    scene toukabath23
    with dissolve

    tb "We’re bonding! Oh, it’s been so long since I’ve been able to engage in “girl talk” with anyone. And seeing as I’m your mother, there's no need to shy away from touchy subjects like intercourse. "
    tb "Do you have any questions for me? I’d be happy to help."
    to "Only about a million or so."
    tb "Well, let’s start with one and see how things go from there. Shoot."
    to "..."
    tb "{i}Shoot.{/i}"
    to "..."

    scene toukabath24
    with dissolve

    tb "Touka, there’s absolutely nothing wrong with feeling the way you feel. Well, at least not from your perspective. "
    tb "Your body is going through changes and-"
    to "I have seen more than enough “instructional videos” to know precisely what “changes” my body is going through, Mother."
    to "What I do {i}not{/i} see is why you’d insinuate and seemingly {i}endorse{/i} me doing something like that with my teacher when I’m still this...young."

    scene toukabath25
    with dissolve

    tb "Because we’re in a position fortunate enough to do anything we want whenever it is we want to do it. "
    tb "And if there is something {i}you{/i} want, even if you are not supposed to {i}have{/i} it, I don’t mind if you try to reach out and grab it."
    tb "“It” in this case, of course, being your teacher. Will you at least admit that the thought has crossed your mind?"
    to "..."
    tb "Touka, it’s fine. I will understand."

    scene toukabath26
    with dissolve

    to "Of...course it’s crossed my mind. As you said, thinking about such things at my age is completely normal. I am aware of that."
    tb "Then what is it that’s preventing you from moving forward? The consequences? The...risk? What is it?"
    to "The...{i}everything.{/i}"
    to "I won’t deny that I...often find myself gravitating toward him in many more ways than I ever expected to, but I don’t believe we’re anywhere near the level required to do something like {i}that{/i} yet."
    tb "Level?"

    scene toukabath27
    with dissolve

    to "What I mean is...we’re not in love. "
    to "I’ve seen the way he acts with some of the other girls in class, and you can {i}feel{/i} a connection between those pairs that he and I distinctly lack."
    to "Who am I to take what {i}I{/i} want when I haven’t worked nearly as hard for it as they have?"
    tb "Touka, a key benefit to being who we are is not {i}having{/i} to work as hard as others. "
    tb "Besides, there’s no need for a connection of that level when you can simply just use him to satisfy the...{i}cravings{/i} you may have. Any man in their right mind would jump for joy at a deal like that."

    scene toukabath28
    with dissolve

    to "Who are you and what have you done with my perfect mother?!"
    tb "Perfection is just a mask we put on to impress those around us. When that mask comes off, we’re all the same, Touka."
    tb "I’m not endorsing the idea of you going around and sleeping with all of the remaining men in Kumon-mi. I’m just saying I trust your judgement and wouldn’t blame you for indulging those desires of yours."

    scene toukabath29
    with dissolve

    tb "It doesn’t even have to be Sensei if you’re dead set on being “in love” with him first. We have an entire massage staff who would be more than happy to {i}assist{/i} you."
    tb "How do you think {i}I{/i} stayed sane when I was your age?"

    scene toukabath30
    with dissolve

    to "Mother!"
    tb "Ahh...how I miss those days. Things are no fun anymore now that I’m unable to let my guard down."

    scene toukabath31
    with dissolve

    tb "But it doesn’t have to be that way for you. You can-"
    to "Oh, no. Don’t you go admitting something like that and then giving me a motivational speech about why it’s okay to abuse the massage staff."

    scene toukabath32
    with dissolve

    tb "{i}Abuse?{/i} I’d never make them do anything they didn’t already want to. And if it weren’t for my mother, I never would have known about those services in the first place. "
    tb "This goes back generations and generations, Touka. It’s not a new thing."
    to "This tradition...ends with me."

    scene toukabath33
    with dissolve

    tb "{i}Why?{/i} It’s completely natural and {i}really{/i} helps take the edge off. If you think this bath is relaxing, just imagine how-"
    to "Mother."
    tb "...yes?"
    to "I do not want to talk to you right now."

    scene toukabath34
    with dissolve

    tb "Fine. Two can play at that game. But don’t come crying to me when your urges become too much for you to bear."
    to "As my mother, you would be the last person I’d ever come to for that in the first place."
    tb "Hmph!"
    to "Hmph!"
    tb "..."
    to "..."
    tb "..."
    to "..."

    scene toukabath35
    with dissolve

    tb "This was fun. We should spend time together like this more often."
    to "I agree. Looking past the many things I learned about you tonight, it was very nice getting to speak to you in a way much...different than normal."
    to "And I mean {i}much{/i} different. I wasn’t even aware this side of you existed."

    scene toukabath36
    with dissolve

    tb "What do you say to having our next get-together in the massage lounge?"
    to "I say that I am suddenly tired and have decided to retire for the night. "
    to "Goodnight, Mother. If that is {i}really{/i} who you are."

    scene black
    with dissolve2
    play sound "water1.mp3"

    tb "It’s who I’ve always been, dear. I just think you’re mature enough to hear about it now."
    to "I’m barely a freshman!"

    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2

    "I peel off my shirt, now drenched with cum from battling loneliness, and toss it across the room into a pile of others that have met the same fate."
    "You’d never guess who I thought of tonight."

    scene black
    with dissolve2

    "I hope she thought the same of me."
    "And I hope her clothes are lying in a pile right now."
    "........."
    "{i}She did.{/i}"
    "{i}And they were.{/i}"

    $ renpy.end_replay()
    $ toukadorm25p3 = True
    $ touka_love += 1
    stop music fadeout 7.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
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

label toukacamp1:
    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I haven’t had much time to think about her lately, but..."
    "Now that I have Touka’s number, I’m sure she wouldn’t mind if I gave her a call. Right?"
    "I know it’s late...and I know I may have ghosted her for months while I was lying in bed mostly unconscious. But things are better now. Kind of."
    "And I think that, with her, they can get even better than that."

    play sound "phonebeep.wav"

    "Or maybe that’s just wishful thinking and my voice will do naught but annoy her now that she isn’t used to it anymore."

    scene toukacampcall1
    with dissolve2
    play music "tsukiokamanor.mp3"

    to "Hello?"
    s "Hey. I’d like to place an order for delivery."
    to "Apologies, I believe you may have the wrong number. This is Touka Tsukioka of the Tsukioka-"
    s "Just one large with pepperoni. Thanks."
    to "One large with-"
    s "Actually, add some garlic knots to that as well. Thanks."
    to "Uh- hold on one moment. Let me find a pen."

    scene toukacampcall2
    with fade

    to "Mother- you don’t happen to be carrying a pen, do you?"
    tb "A pen? For what, dear?"
    to "A delivery order. One large with pepperoni and garlic knots."
    tb "A large {i}what?{/i} "
    to " I’m not sure. Let me confirm."

    scene toukacampcall3
    with dissolve

    to "Sir, are you still there? A large {i}what,{/i} exactly?"
    s "Touka, it’s me. "
    to "Oh, apologies again. I’ve yet to take down your name. Please wait one moment while my manager obtains something for me to write with."
    s "Touka, I’m not actually placing a delivery order. I’m fucking with you."
    to "Fucking?"
    tb "One large fucking with pepperoni and garlic knots. I’ll inform the kitchen staff right away."
    to "Your order will be ready in thirty to forty-five minutes, sir."
    s "Got it. Thanks again, Tina."

    scene toukacampcall4
    with dissolve

    to "Nevermind, Mother. It’s just Sensei. I can tell by his failure to correctly say my name."
    s "Hey, I tried. But you probably didn’t recognize my voice {i}because{/i} I was using the correct name."
    tb "What does Sensei want with a large pepperoni fucking? "
    tb "Are the delivery parlors near his home- "

    scene toukacampcall5
    with dissolve

    tb "Oh! This must be one of those “crank calls” I have heard about on the television. He wasn’t actually ordering anything at all, was he?"
    to "Do you think I have time for your games, Sensei? I’d have gladly answered if your intention was not to toy with my emotions and consume precious business hours."

    scene toukacampcall1
    with fade

    s "My bad. I’ve once again underestimated just how out of the loop you and your mother are."
    to "Yes, well, there are plenty of loops we’re involved in that you could never even {i}hope{/i} to come into contact with. So what do you {i}really{/i} want? There isn’t a problem with your apartment, is there?"
    s "No. I’m actually in the woods right now."
    to "The...woods? Are you in trouble? Do you need me to send someone to-"
    s "I’m just camping."
    to "Camping?"
    s "It’s when you go hang out in the woods and then ultimately go to sleep there."
    to "One moment, Sensei."

    scene toukacampcall6
    with fade

    to "Mother, have you heard of something called “camping” before?"
    tb "Why, yes. I believe that’s when a group of commoners go into a wooded area with the intention of creating some form of recreational shelter and...starting fires?"
    to "Why would they do such a thing?"
    tb "I’m not sure, dear. The poor do all sorts of strange things, but we mustn’t question their customs for that could be one of us one day. "

    scene toukacampcall7
    with dissolve

    to "Sensei? Are you still there?"

    scene toukacampcall8
    with fade

    s "Yes. And I heard all of that."
    to "Oh, splendid. Then, would you mind explaining to me why you’d willingly do something like “camping?” Are you that desperate to get away from everyone that you’d isolate yourself in the woods?"
    s "I’m not isolating myself. I’m here with Ami and some of my other friends."
    to "Since when do you have friends?"
    s "I don’t know. They’ve just kind of always been around. But it doesn’t really matter {i}why{/i} I’m out here. What matters is that I wanted to talk to you."
    to "About what, exactly?"

    scene toukacampcall9
    with dissolve

    s "Does there actually need to be a reason?"
    to "..."
    s "Because I don’t have one."

    scene toukacampcall10
    with fade

    s "I kind of just wanted to hear your voice."
    to "You..."

    scene toukacampcall11
    with dissolve

    to "You’re only saying that to get a rise out of me...just like when you ordered the pepperoni fucking."
    s "Maybe I am, maybe I’m not. Can you talk or not, though? Because I was kind of hoping we could maybe do this {i}without{/i} Tsubasa looming over your shoulder."
    to "Regardless of the reason, you’ve chosen a terrible time to do this. I’m in the middle of-"

    scene toukacampcall12
    with dissolve

    tb "Wow, I sure am tired all of a sudden."
    to "Uhh...please hold again, Sensei. "
    to "Mother, weren’t you just saying a moment ago how much energy you’ve had as of late?"

    scene toukacampcall13
    with dissolve

    tb "Yes. But I must have forgotten to mention how today is the exception to that. "
    to "Um..."
    tb "So, if you’d please excuse me, I believe it’s time that I retire for the evening. "
    to "If...that is what you believe to be best, then-"

    scene toukacampcall14
    with dissolve

    tb "Goodnight, dear. And please don’t stay up too late. We have guests coming in the morning that we must be prepared for. "
    to "Y...Yes, Mother. I understand."

    scene toukacampcall1
    with fade

    to "Sensei? Are you still there?"
    s "Yes. And again, I heard all of that. Phones pick up a lot now, Touka."
    to "Then...I suppose it appears that I {i}do{/i} have time to talk after all. But I’m still not quite sure of what’s going on here. "
    to "From what I understand, one does not typically call another {i}just{/i} to hear their voice. "
    s "People in relationships do."
    to "But the two of us do not have the sort of “relationship” you’re referring to at the moment. "
    s "But we {i}do{/i} have {i}a{/i} relationship. "
    to "If you want to be that vague, I have a relationship with {i}many{/i} people. "
    s "Sure. But do you feel the same way when you’re talking to me that you feel with any of them?"
    to "Are you referring to the innate desire to reach through the telephone and smack the side of your head?"
    s "Yeah. I’m pretty sure they call that “love” in some cultures."
    to "Hah...what have I gotten myself into now?"

    scene black
    with dissolve2

    "I remain on the phone with Touka as she walks through the halls of the manor. And, throughout that time, I fill her in on why I’m out here and what I hope to accomplish with Ami."
    "Or I guess...what I’ve {i}already{/i} somehow accomplished."
    "It feels weird to share any of this with one of her classmates, though. Even if I barely look at Touka as another teenager in the first place when she acts so much more mature than the rest of them."
    "And yes, I know that sort of statement makes me sound deplorable and that it would never hold up in a court of law, but I mean it."
    "I wouldn’t see her as some sort of matriarch if I was getting high off of her hormones. And I certainly wouldn’t be calling her in the middle of the night just to “talk.” "
    "But the fact of the matter {i}is{/i} that I just wanted to hear her voice. And another fact of the matter is that I know she wanted to hear mine. "

    scene toukacampcall15
    with dissolve2

    "But those ways do not run parallel with one another. "
    "They violently intersect, slicing each other in half, and all we can do is wait to feel the after-effects and hope that most of our limbs remain intact. "
    "For right now, this is perfect."
    "But I know it can’t stay this way forever."

    to "You’re on speaker, Sensei. So please do me a favor and keep the inappropriate language to a minimum. You never know just who is listening around here."
    s "You and your mother were literally just talking about “pepperoni fucking” like ten minutes ago."
    to "Yes, but that was when I was under the impression that “fucking” was simply a slang term for a food item I’d never heard before."
    to "You must remember that there’s a great deal I still don’t understand about your world, Sensei."
    s "Oh, I don’t need to remember. You remind me every time I talk to you."

    scene toukacampcall16
    with dissolve

    to "Then you most assuredly {i}do{/i} require a reminder as you had no qualms at all with completely ignoring me for several months."
    s "I completely ignored {i}everyone{/i} for several months, Touka."
    to "Yes. But you and I have a {i}relationship,{/i} don’t we?"
    s "..."
    to "Isn’t that what you said just a short while ago, Sensei?"
    s "I mean...yeah."

    scene toukacampcall17
    with dissolve

    to "So that {i}relationship{/i} only exists when it benefits you?"
    s "That’s not what I’m saying."
    to "Then please explain what you mean a little better. Because your earlier words implied that there was some sort of connection between us and {i}now{/i} you’re making it sound like I’m no different from anyone at all."
    to "Which one is it, Sensei? Do tell. "
    s "I’m sorry for ignoring you, Touka."
    to "As you should be. I’m disappointed in you."

    scene toukacampcall18
    with dissolve

    to "Don’t think I didn’t notice how frequently your eyes landed on me at the Halloween party, Sensei. "
    s "You mean the one where I literally sought you out and asked you to stay with me? Because yeah, that would typically involve a certain amount of eye contact."
    to "And what? You just...stopped desiring such a thing once that night came to an end? Did you think for a moment about how that would make {i}me{/i} feel?"

    scene toukacampcall19
    with dissolve

    to "If one second I’m important to you and the next I’m not, how is that any different than the more {i}playful{/i} ways in which you tug at my strings, Sensei?"
    s "It’s starting to sound like I’m in trouble right now."
    to "Because you are. But I’m kind enough to not make you grovel at my feet and beg for forgiveness. "
    s "Then tell me, kind and wonderful Touka, what must I do to be forgiven?"

    scene toukacampcall1
    with fade

    to "Simply doing what I ask you to do means nothing to me when I have the power to {i}make{/i} you do anything I want, Sensei."
    s "Your mother would be so proud right now."
    to "If you truly want to mend the wound that {i}you{/i} have inflicted upon us, {i}you{/i} will come up with a solution. I will not coddle you 100%% of the way. "
    s "How about 90%%?"
    to "That sounds much more manageable. I accept. "
    to "But I hope you understand that this means {i}you{/i} will be putting in a certain amount of work as well."
    s "I think I can probably manage 10%%."

    scene toukacampcall20
    with fade

    to "I would sure hope so. I can only imagine how destined to fail this {i}relationship{/i} would be if {i}both{/i} of us were incapable of acting our age."
    s "You’re probably even further off than I am, to be honest."
    to "Yes, because I’m a mature and responsible young woman while {i}you’re{/i} a blubbering lunatic who wastes his precious phone time on a girl half his age."

    scene toukacampcall1
    with fade

    s "That’s me alright."
    to "I’m glad you called, Sensei."
    to "I’m always happy to hear your voice."
    to "Even {i}when{/i} it torments me. "
    s "I’m not tormenting you right now, am I?"
    to "You most certainly are- forcing me to have a conversation this intimate over the telephone rather than appearing before me in person."
    s "Is “intimate” the right word here?"
    to "Are we not privately sharing our feelings with one another? Is that not what intimacy is?"
    s "I just typically associate that word with something else."

    play sound "static.mp3"
    scene toukacampcall21 with flash
    stop sound

    to "That’s because {i}you’re{/i} a bastard and {i}I’m{/i} a princess."
    s "At least half of that statement is correct."
    to "Which half?"
    s "The former, obviously. Being a princess requires a little more than just being rich. "
    to "There you go again, squandering a perfect opportunity to mend the wound you’ve inflicted by pouring salt in it."
    s "I formally apologize for knowing the textbook definition of “princess.”"
    to "Apology accepted. Now, apologize for setting my mind ablaze during your two month absence. "
    s "Ablaze? You thought about me that much?"

    scene toukacampcall22
    with dissolve

    to "Considering the last look I had at you was met with a glance that screamed “save me,” yes. I thought about you quite a bit."
    to "I worried almost constantly. But I was also furious with you, Sensei. "

    play sound "static.mp3"
    scene toukacampcall9 with flash
    stop sound

    to "Which is ultimately why I elected to not save you at all when all it would have taken was one phone call."
    to "So...maybe I {i}do{/i} want to see you grovel. Just a little bit."
    s "I’ll make sure to do that the next time I see you."
    to "And when will that be?"
    s "When do you want it to be?"
    to "I want you to start living up to that 10%% and make your {i}own{/i} decisions about what to do with me rather than letting me guide you the whole way. Did I not make that clear enough?"
    s "I can promise you that you do {i}not{/i} want me making the decisions about “what to do with you.” "
    to "Are you being a bastard again? Insinuating such impure things to a lady of my stature?"
    s "I’m pretty much always being a bastard. I thought you knew that about me."

    play sound "static.mp3"
    scene toukacampcall23 with flash
    stop sound

    to "Oh, I do. It’s actually rather pathetic. "
    s "Yeah...I’m well aware."
    to "Are you?"
    s "Yeah. But I’ll make it up to you soon. Does Saturday morning sound okay?"
    to "Okay for what? You haven’t even informed me of what we’ll be doing yet."
    s "I’ll just take you out to eat or something and we can talk more about how much I suck for letting you wallow in worry for several months. "
    to "Sounds wonderful. I’ll mark my calendar in anticipation of your expected groveling."
    s "There will be no groveling involved. Just food and likely depressing dialogue."
    to "Oh, then why don’t I just cancel now? {i}Anyone{/i} can buy me food, Sensei. Such a thing won’t show me you care."
    to "So until you start expressing with both your actions {i}and{/i} words that you regret the way you’ve treated me, I simply won’t believe you."
    s "You like the way I treat you, though."
    to "When it’s just teasing...I suppose I do. But this time was different."
    to "This time, you really hurt me."

    scene toukacampcall24
    with dissolve

    to "So I want you...to make up for it..."

    scene toukacampcall1
    with fade

    s "I guess I’ll practice my dogeza then."
    to "Mm...I’m excited to see it..."
    s "So...Saturday works then?"
    to "Mm..."
    s "Cool."
    to "Mm..."
    s "..."
    to "..."
    s "Are you still there?"
    to "Mm..."
    s "Are you tired or something? You sound different."
    to "Yes...it’s been a long day..."
    to "But you’ve made it a lot better by calling."
    s "Should I just hang up and...let you sleep then?"
    to "Mm..."
    to "No..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    to "Stay on the line a little longer."

    "Touka falls silent several minutes later and I’m left with nothing to do but...continue aimlessly wandering through the woods."
    "I’m not sure what she expects me to do come Saturday, but..."
    "I can almost guarantee it won’t be what she wants."
    "All I can do is just hope it won’t stretch the wound out even further."
    "I want to keep her close. "
    "Just as a different sort of tool than I’m used to."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukacamp1 = True

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    scene clearnightsky
    with dissolve2

    "Now what?"

    jump campmenu2

label toukaspring1:
    scene bedroom_day
    with dissolve2

    play sound "phonebeep.wav"

    "I tap on Touka’s name in my phone as the amount of interpersonal training I have forced myself to endure throughout my time here now somewhat allows me to remember plans I personally made."
    "And today is the day I planned on taking Touka out and “groveling” or whatever it is she’s going to get a high off of making me do."
    "To be honest, I can’t imagine there will be much groveling at all as, like me, I think she’s mostly just talk."
    "She’s far too kind to push me off the pedestal I’ve spent thirty-one (and more) years building and will probably just make me say generic nice things to her or something along those lines. "

    play sound "phonebeep.wav"

    to "Hello? Sensei?"

    play music "marshmallow.mp3"

    "Which means I have to hit her with my greatest pick-up line right now so I can sail smoothly through-out the rest of the day."

    s "Hey."

    "Or at least that’s what I would say if I knew any pick-up lines."

    to "Hay is for horses. And, as today will be your day of groveling, I demand a more formal greeting. One that is at least {i}somewhat{/i} memorable."
    s "Welcome to today, esteemed and beautiful Touka Tsukioka. May fortune continue to favor you and may the gods smile down on your suspicious womanly figure."
    to "Suspicious?"
    s "Yeah. It’s kind of unfair that you’re more physically developed than some women I know in their 30’s."
    to "Well, I shan’t say that was formal. But I suppose you’ve nailed the memorable bit."
    s "Yeah, I have a lot more experience than most when it comes to nailing things."
    to "Is that so? I didn’t take you as a handyman."
    s "I’m not a handyman, but I sure am handy with my hands."
    to "Well, yes. They are hands. They are handy by nature."
    s "..."
    to "..."

    play sound "phonebeep.wav"

    "I hang up so I can completely restart this phone call in a way that is hopefully much less awkward."

    play sound "phonebeep.wav"

    to "Hello again."
    s "I’m sorry you had to hear any of that."
    to "It’s fine. I was just about to do the same thing."
    s "This is why I don’t normally call people first-thing in the morning. Especially lately since it’s been getting way harder to pull myself out of dream-mentality. "
    to "I suppose I can somewhat relate. To what do I owe the pleasure, though?"
    s "I told you I was going to call today, didn’t I? We made plans to do stuff while I was out camping."
    to "I suppose we did. But I was under the impression that you were either going to cancel or just disappear again."
    s "Well, I guess this is me proving you wrong then. When can you meet up?"
    to "Whenever I find out {i}where{/i} we’ll be meeting up. Because, unlike you, I’ve already been awake for several hours- {i}patiently{/i} waiting for your call."
    s "Bullshit. Just three seconds ago you said you expected me to cancel."
    to "Yes, that’s correct. I was just trying my hand at sarcasm, but I feel as if I haven’t quite gotten it down yet. If you want the truth, I just got out of the bath."
    s "I have no response to that that wouldn’t ruin this phone call."
    to "My! Look at you, Sensei — acting so uncharacteristically mature despite having just opened your eyes. I admire the restraint. "
    to "It {i}does{/i} make me feel slightly lonely, though"
    s "Why would that make you-"
    to "One hour. We can meet near the vending machine."
    s "Touka, we live in Japan. There’s a vending machine on every corner."
    to "You know the one I mean, Sensei. "
    to "Ciao."

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "I’m annoyed because she’s right. There’s only one vending machine that holds any sort of significance for us, but even then it’s {i}still{/i} just a machine."
    "Regardless — after getting dressed and preparing for the day, I walk out into the living room to find Ami watching television on the couch. "
    "It’s a simple sight, but one that I’ve forgotten over the last several months. And I’m glad I can finally see it again, as silly as that sounds."
    "But when she asks me where I’m going, I lie. "
    "There’s no need to. I’m sure she wouldn’t stop me if she knew the truth. "
    "But I do it anyway, because there always needs to be {i}something.{/i} And if there’s anything I’m good at (apart from nailing things or tormenting rich girls), it’s building mole hills for someone else to turn into mountains."
    "When I leave the house, I look behind me. But I’m not sure quite why."
    "I don’t think I’m being followed. "
    "But I think I wish I was."

    scene toukadateday1
    with dissolve2

    to "Well, would you look at that? It’s only been forty-five minutes, Sensei. Were you so excited to see me that you left early?"
    s "No, I just didn’t stop for coffee on the way over like I originally decided to."

    scene toukadateday2
    with dissolve

    to "One sentence in and you’ve already ruined our date. Impressive."
    s "Sure. Except that this isn’t really a “date” and more of just a way for me to show you how sorry I am for causing you to worry for so long. I’m doing it for everyone."
    to "Wow, and now you’ve made it even worse. Is there no limit to your undesirableness? "
    s "Not really, no. I just tend to say things like that when I’m worried about getting closer to someone."

    scene toukadateday3
    with dissolve

    to "So you {i}do{/i} see us getting closer...but you also see me the same way as everyone else...while setting up a meeting that only exists because I asked you to do something to prove that you {i}don’t{/i} see me that way."
    to "I’m confused. "

    scene toukadateday4
    with dissolve

    to "So I’m just going to say it’s a date. And if that word does not accurately describe what’s truly happening here, you can internalize it, for doing the opposite will only make me feel unwanted."
    s "Sure. Do whatever you want. Just don’t expect me to take you to some fancy French restaurant like you did for me when {i}you{/i} got to choose the date."

    scene toukadateday5
    with dissolve

    to "Oh, I remember that day. It’s when you chose Chika over me. What a lovely memory."
    s "I barely knew you at the time, Touka."

    scene toukadateday1
    with dissolve

    to "So you’re saying you’d choose differently if that contest took place today?"
    s "Is everything you say today going to be carefully designed to make things as hard as possible?"
    to "Am I making it hard now?"
    s "..."

    scene toukadateday6
    with dissolve

    to "That..."
    to "I believe you interpreted that in a way you were not intended to."
    s "I’d believe you if you were wearing a different outfit."

    scene toukadateday7
    with dissolve

    to "My...outfit has nothing to do with your perversion, Sensei! I should be free to wear what I want without your gaze lingering longer than it’s supposed to."
    s "How long is it supposed to? What’s the max amount of time?"

    scene toukadateday8
    with dissolve

    to "Somewhere between two and five seconds. Long enough to not draw attention to the fact that there is any lingering at all."
    s "I’m kind of surprised to hear that you have an actual number."
    to "Of course I have a number. It’d be irrational to expect everyone to completely ignore my assets. All I ask is that it be done in moderation and never mentioned verbally."
    s "Then I will keep it in mind. Literally."

    scene toukadateday9
    with dissolve

    to "Well done, Sensei. Now, take me away from here before anyone realizes what we’re talking about."

    scene black
    with dissolve2

    s "On it."
    to "Oh, and please inform me of what we’ll be doing as I’ve only brought approximately 500,000 yen with me and have decided it will be best to keep my spending to a minimum as it’s grovel-day. "
    s "Yeah, I think that’ll be more than enough. And I’m not sure what we’re doing yet. But we’ll begin by going to your favorite place in the world."
    to "The Swiss Alps?!"
    s "The subway. "
    to "I hate you."
    s "Yeah, I know."

    scene toukadateday10
    with dissolve2

    "Touka and I arrive in the urban district after a brief subway ride and begin to wander around in search of something that looks interesting to both of us."
    "The thing is, there isn’t much {i}at all{/i} that seems to interest both of us. The only thing I can think of that comes close is the movie theater, and all Touka wants to watch is horror."

    to "We’ve passed several museums, Sensei. Did you not think to take me into any of those?"
    s "Museums don’t interest me."
    to "Yes, but you don’t matter today. "
    s "Well, that was rather blunt."

    scene toukadateday11
    with dissolve

    to "Only because it’s true. If you want me to believe I hold a special place in your heart, you must go out of your way to prove it to me."
    to "I see no purpose in allowing you to lean on me in your time of need if you will not offer the same to me when {i}I{/i} require a shoulder."
    s "I didn’t realize right now was a {i}time of need{/i} for you. "
    to "I suppose it’s less a time of “need” and more a time of “want.” But what I want is not so easily put into words."
    s "I can’t imagine it would be if it requires {i}my{/i} participation in any capacity. You’re sort of like ten leagues above me, Touka."

    scene toukadateday12
    with dissolve

    to "Oh, it’s far more than that. But it doesn’t change the fact that I enjoy your company far more than someone like me ever should. But we all have our flaws, and mine appear to be that I like you."
    s "Not unconditionally, though."
    to "Would you prefer me as a mindless zombie who will love you no matter what?"

    scene toukadateday13
    with dissolve

    s "You’d be easier to hang out with, that’s for sure."
    to "I’m easy right now as well. You’re likely just over-thinking it. {i}Or{/i} not thinking at all, but I’m going to give you the benefit of the doubt since you {i}did{/i} show up today."
    s "Yeah. I kind of can’t afford to have you not liking me anymore. So if I need to put in some work to maintain our relationship every now and then, so be it."
    to "Oh, yay. I’ve always wanted to be someone’s {i}chore.{/i}"

    scene toukadateday14
    with dissolve

    s "That’s not what I meant, Touka. If anything, {i}I’m{/i} the chore here."
    to "You most certainly are. You’ve been a never-ending pain in my behind since the moment we first met. "

    scene toukadateday13
    with dissolve

    s "The first time we met was in Osako’s dojo. I didn’t become a pain until you were one of my students."
    to "I suppose you’re right."

    scene toukadateday15
    with dissolve

    to "But it’s also because of you that I’m beginning to understand what “pain” is at all. And I can’t quite tell if I like it or not."
    s "What’s there to like about pain?"
    to "The parts where it feels good."
    s "..."
    to "Your mind is wandering again, isn’t it?"

    scene black
    with dissolve2

    s "I’m beginning to believe it’s not “wandering” at all and that you’re just leading it into the darkest corners of Kumon-mi on purpose."
    to "On purpose? Now, why would I do that?"
    s "Maybe you’re curious about what will happen there?"
    to "Maybe I am? Then what?"
    s "..."
    to "Is something wrong, Sensei? You’re walking a little...{i}strangely{/i} all of a sudden."
    s "Just keep looking forward, Touka."

    "........."
    "......"
    "..."

    scene toukadateday16
    with dissolve2

    "Eventually, our “date” leads us into a restaurant after we spend an hour or so wandering through a park — a park where Touka decided the best use of her money was lining the pockets of various street performers. "
    "And yes, she’s generous. This is what she does. But there’s a point where generosity becomes dangerous. And she’s just lucky no one has attempted to take advantage of that yet."
    "I could if I wanted to. I {i}know{/i} I could."

    play sound "static.mp3"
    scene toukadateday17 with flash
    scene toukadateday16 with flash
    stop sound

    "But there is something else I want from her instead. "
    "Something that can’t be bought. "
    "Or even understood by most — this endless Oedipal craving and the desire to both consume and {i}be{/i} consumed by a single being that my existence could both start {i}and{/i} end with. "
    "So she looks at me, and I look back at her."
    "But while she sees a fancy jewel or an interesting mechanical toy, I see a blanket and a ball-gag. And I feel the sensation of someone sneaking into bed beside me."

    to "So..."
    s "So..."
    to "I heard you had a conversation with my mother recently."
    s "I’ve had many conversations with your mother. But I’m reluctant to divulge the details of any of them."
    to "And why is that?"
    s "Two reasons. One — you don’t need to know. And two — you probably already do."

    scene toukadateday18
    with dissolve

    to "I can see why you’d think that, but I assure you that my mother has no qualms at all with keeping information she does not wish to share away from me."
    s "So if you know I was there, it would have to mean she {i}wants{/i} you to know I was there, right?"

    scene toukadateday19
    with dissolve

    to "Maybe. "
    to "Or maybe I just have eyes."

    if tsukasaspring1 == True:
        s "The kind you personally see with? Or the kind your sister has that are just stationed around Tsukioka Manor?"
        to "I see you’ve learned of Tsukasa’s henchmen. Interesting. How did that come to be?"
        s "Maybe I have eyes too?"
        to "If you’ve been planting cameras around my home, I do hope you’ve omitted them from my bedrooms. "
        s "I’ll have them removed next week. Scout’s honor."
    else:
        s "You saw us?"
        to "Is that the conclusion you’ve drawn from that?"
        s "It’s what you were implying, is it not?"
        to "All I’m doing is offering up a potential explanation. I never said I actually {i}saw{/i} anything."

    to "Regardless of what {i}I{/i} know, though, I’d like to hear from you. What business do you have with my mother?"
    s "I think a better question is what business Tsubasa has with me. I can never figure out what the hell she’s trying to do. Especially now that the whole Chika situation is under control."
    to "So she asked you for something? "
    s "I didn’t say that."
    to "You didn’t answer the question either. She did, didn’t she?"
    s "Why not just ask her?"
    to "Why not just tell me?"
    s "Because I have no idea what she’s okay with me sharing and acknowledge the fact that she could put me in prison whenever she wants."
    to "True. But then she’d need to find someone else to pique her interest, and that doesn’t happen very often. And besides, I could put you in prison if I wanted to as well."
    s "Sure. But then you’d need to find someone else to pique your interest, and I don’t think that happens very often."
    to "And you’d be right in thinking that. But there’s something I’d like to ask you, Sensei. Or rather...something I’d appreciate your participation in."
    s "Oh good. Here we go again. Your family really has it out for me, don’t they?"

    scene toukadateday20
    with dissolve

    to "Sensei...all I want is for you to stop giving her the time of day."
    s "What?"
    to "She’s gotten too interested in...{i}interfering.{/i} And I’d very much like her to mind her own business when it comes to my personal affairs. But, so long as you keep letting her tug your strings, she has no reason to stop."
    s "Is just knowing {i}you{/i} don’t want her getting involved not enough?"
    to "Not when she knows I can’t and won’t do anything about it."
    s "But why not? You’re the...future heir or whatever, aren’t you? Can’t you leverage that to get her to back off?"

    scene toukadateday21
    with dissolve

    to "Hah...no. That’s my duty, and it’s separate from my personal life. If I begin conflating the two, it’ll blur the lines my ancestors have so meticulously drawn."
    to "These two things must remain separate no matter what. Which means that the only thing I can {i}leverage{/i} is the fact that I’m my mother’s daughter and that I’d like some privacy."

    scene toukadateday22
    with dissolve

    to "But we Tsukiokas aren’t typically great when it comes to “privacy.” And that’s especially true for my mother who suddenly wants to know every explicit detail of my personal life."
    to "But the strangest part is that she rarely expressed any interest in that until I began spending time with {i}you.{/i}"
    s "Well...why do you think that is?"
    to "I have my guesses. But I don’t think I can share any of them inside of a restaurant."

    scene toukadateday23
    with dissolve

    to "If that {i}is{/i} what this place is, I mean. Because I’m not quite sure I’ve ever seen food that looks like this before."
    s "That is fried chicken, Touka."
    to "Then why is it so shiny and round?"
    s "Asset limitations. Just ignore it and look at me."

    scene toukadateday24
    with dissolve
    stop music fadeout 20.0

    to "Apologies. "
    s "Talk to her if you don’t want her interfering. Don’t put that on me."
    to "Do you think I haven’t tried that? It’s as if she refuses to let me have {i}anything{/i} without also sharing it with her. "
    to "It’s quite infuriating, to be honest. But there’s only so much I can do."
    s "You can do way more than I can, Touka. "
    s "Because even though Tsubasa hasn’t really done anything {i}bad{/i} to me yet, she knows enough about me that she definitely {i}could.{/i} "
    s "But I don’t know enough about her yet to know if she actually {i}would.{/i} You know?"
    to "I suppose I understand what you’re saying. I just didn’t take you as the type to let someone like that boss you around."
    s "Then you don’t know me very well yet, I guess."

    scene toukadateday16
    with dissolve

    to "Oh well. I suppose this just means that {i}I{/i} get to boss you around too now that I {i}know things{/i} about you."
    s "In a roundabout way, that’s almost what this date is."
    to "In a roundabout way, I think I’d have to agree."

    scene black
    with dissolve2

    to "But that calls into question just what {i}else{/i} I can get you to do for me..."

    $ renpy.end_replay()
    $ toukaspring1 = True
    $ touka_love += 1

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump toukaspring2

label toukaspring2:
    "I’m not sure why she smirks at me when we both know she isn’t actually going to {i}make{/i} me do anything. That’s just not the type of person she is."
    "And that’s likely part of why she’s cemented herself as such a subtly pivotal figure in this endlessly confused half-life of mine. "

    scene nightsky
    with dissolve2
    play music "tsukiokamanor.mp3" fadein 3.0

    "I’m sure I’m not the only one around here who’s “confused,” though. And I need to stop putting myself into a bubble that prevents me from actually caring about that."
    "Touka Tsukioka is a girl. Not a woman. Not a mother. She’s a girl. Plain and simple."
    "But this causes complications for me because it turns her into something I don’t {i}want{/i} her to be. And accepting that truth brings me closer to making one more mistake and losing one more piece of myself."
    "Maybe it’d be okay if she gave me a piece of her as well, though."
    "I’ve told myself I shouldn’t care. That I’d given up on finding happiness and that I’d settle for reverting to the real me — a man who fucks those he shouldn’t and forgets those he should. "
    "So what am I doing pretending roles like “matriarch” even matter to me at this point?"
    "What am I doing {i}not{/i} trying to fuck her when she fits the criteria of everyone else I’ve corrupted almost perfectly?"
    "Am I just fooling myself? Because my body most certainly wants her. It’s only my mind that doesn’t."
    "But I’ve never trusted that part of myself before. And I definitely don’t think I should {i}start{/i} doing that now that it’s clearly gotten worse.."
    "Is all of this just a clever way of convincing my brain to dwell less on the past and more on the future since I know at least {i}that{/i} will never leave me behind?"
    "Or is she closer to resembling something even {i}more{/i} forbidden than the {i}youngest{/i} fruit that fell from the same tree?"
    "Whatever she is, it scares me...because it makes me doubt myself. And that scares me even more because my first instinct is to wrap myself up in her to find comfort."
    "It’s an endless cycle of fear and love, spearheaded by a girl who doesn’t even know the power she wields."
    "Or maybe she does and she’s just like me — denying it because it’s complicated and conflicts with what her heart craves."

    scene returntothemanor1
    with dissolve2

    "We wind up back at the manor somehow. I don’t know. I spent so much time trying to argue away my erection that I must have blurred out everything that happened after lunch. "
    "I’m sure it went well. And I’m sure Touka enjoyed herself if she was willing to take me back home after it all played out."
    "But I also know that this is typically the part of a “date” where one invites the other up for tea or coffee before clothes start to come off and poor decisions start to be made."
    "It’s the perfect moment to figure out whether she really {i}is{/i} important to me in a way that separates her from the rest. "
    "But I don’t like “perfect” moments. "
    "So I hope that she ruins it."

    to "Is something the matter, Sensei? You’ve been rather quiet since we entered the manor. "
    s "Yeah well, one wrong move here and someone could slit my throat."
    to "I doubt anyone would do that while I’m in such close proximity to you. Dirtying my clothes would be greatly frowned upon."
    s "Then be sure to stay close so I can make it home after this. "
    to "And to which home will you be returning today? The one with your {i}niece{/i} who is in love with you? Or the one with your {i}girlfriend{/i} who is in love with you?"
    to "Or {i}one{/i} of your girlfriends, I suppose. I’m not quite sure how many you have, come to think of it. But I do know that it’s more than I’d personally recommend."

    scene returntothemanor2
    with dissolve

    s "And I’m sure you’d recommend only one, correct? You don’t strike me as a polyamorist."
    to "One would be ideal, yes. But it isn’t uncommon for those in my echelon to take a {i}mistress{/i} as well."

    scene returntothemanor3
    with dissolve

    to "Of course, that only goes for the men. Us women aren’t typically awarded the same level of {i}freedom.{/i} Which isn’t to say I’d do such a thing anyway. I just figured I’d share."
    s "Thanks for the info. But you’re a girl, not a woman."
    to "Some might disagree, Sensei. You’ve noted on many occasions just how much more mature I am than the rest of the girls in our class, have you not?"
    s "Are you trying to tell me something right now, Touka?"
    to "Is there something you’d {i}like{/i} me to tell you?"
    s "No, actually. "
    to "No?"
    s "Right. It’s already wrong of me to have followed you all the way to what I can only imagine is one of thirty bedrooms you have."
    to "Yet here you are. And here I want you to be."
    s "Touka-"
    to "Would you perhaps like to see a tour of-"

    scene returntothemanor4
    with dissolve

    tb "Oh my! If it isn’t my eldest daughter and her “former” teacher."

    scene returntothemanor5
    with dissolve

    to "Aaaand of course my mother is here."

    scene returntothemanor6
    with fade

    tb "How unexpected. I’d known the two of you ran off somewhere, but if I had any idea that you’d be returning together, I’d have had dinner prepared for you. "
    to "We already ate. But thank you, Mother. And thank you for keeping tabs on my every move as well. It’s good to know that I am always being watched."

    scene returntothemanor7
    with dissolve

    tb "Or perhaps your teacher is the one I’m keeping tabs on and you just happened to be there with him?"
    s "Yeah, I wouldn’t put that past you. "

    scene returntothemanor8
    with dissolve

    tb "Hahah! Hilarious as ever! Oh, how I enjoy that blunt sense of humor of yours. "
    to "{i}Ahem.{/i}"

    scene returntothemanor9
    with dissolve

    tb "What’s wrong, dear? You’re not coming down with a cold, are you?"
    to "No, Mother...I was just in the middle of a conversation."

    scene black
    with dissolve

    tb "Oh, good! Then surely you won’t mind if I join you for a few minutes."
    to "But-"
    tb "Don’t worry, darling. I was just on my way to the sauna, so you aren’t interrupting anything."

    scene returntothemanor10
    with dissolve2

    to "That’s...not what I was trying to imply..."
    tb "Oh? Am I perhaps...interrupting something? "
    tb "It {i}is{/i} rather late to be receiving lessons, isn’t it? Let alone lessons from a {i}former{/i} teacher. Unless something has changed, of course."

    scene returntothemanor11
    with dissolve

    to "{i}Hah...{/i}I was just giving Sensei a tour of the central pavilion. I can assure you it was nothing out of the ordinary. "

    scene returntothemanor12
    with dissolve

    tb "Nonsense. What are your intentions with my daughter?"

    scene returntothemanor13
    with hpunch

    to "Mother!"
    tb "Hahah! Oh, I’ve always wanted to say that. I’m so funny."

    scene returntothemanor14
    with dissolve

    to "The funniest, truly..."
    s "Intimidating as ever too."
    tb "What reason is there to be intimidated? You’ve already made it quite clear to me that you have no such intentions with Touka. What with seeing her more as a “mother figure” and all. Correct?"

    scene returntothemanor15
    with dissolve

    to "I’m sorry?"
    s "Hah..."
    to "You must be misunderstanding something, Mother. We’ve had a legitimate competition in regard to that topic, and I {i}lost.{/i} "
    to "Besides, I’m merely half of Sensei’s age. He wouldn’t possibly view me in such a way. Right, Sensei?"

    scene returntothemanor16
    with dissolve

    s "Why do you do this?"
    tb "Do what? All I did was repeat what you told me. "
    s "Yeah, but did you have to do it right in front of her?"

    scene returntothemanor17
    with dissolve

    to "...What?"
    tb "Would it be better for her to {i}not{/i} know your intentions, Sensei? Because the last thing I want is my beloved daughter being “led on.” I believe that phrase is applicable here, correct?"
    to "..."
    s "I’m not “leading her on” because I see her in a different light from the other girls her age. I just-"

    scene returntothemanor18
    with dissolve

    to "So that’s how it really is then."
    s "Touka-"
    to "Good night, Sensei. I apologize for misinterpreting just what sort of {i}relationship{/i} we had. "

    scene returntothemanor19
    with dissolve
    play sound "dooropen.mp3"

    to "I will see you in the morning, Mother."
    tb "Goodnight, dear. "
    s "{i}Why?{/i}"

    play sound "static.mp3"
    scene returntothemanor6 with flash
    stop sound

    tb "Whatever do you mean, Akira?"
    s "You {i}knew{/i} she wouldn’t want to hear something like that. So why would you put {i}both{/i} of us on the spot and just air it out like it was nothing? She was having a great day. She was in a good mood."

    scene returntothemanor9
    with dissolve

    tb "Apologies, but would it have been better for her to throw herself at you only to have you reject her? Because I’d imagine the emotional trauma {i}that{/i} would cause would be significantly worse. "
    tb "And I was under the impression that is what was about to happen."

    scene returntothemanor7
    with dissolve

    tb "So, from my point of view, it’s like I rescued {i}both{/i} of you from a terrible misunderstanding! You should be thanking me."
    s "Not everything has to involve {i}you,{/i} Tsubasa. "

    scene returntothemanor6
    with dissolve

    tb "This isn’t “everything,” Akira. This is my daughter we’re talking about. "
    s "Yeah, but you know you’d be doing the same thing even if it wasn’t."

    scene returntothemanor7
    with dissolve

    tb "Probably! But that’s not what’s happening this time, so it doesn’t apply."
    s "Stop interfering."

    scene returntothemanor20
    with dissolve

    tb "Will there be consequences if I don’t?"
    s "Probably not. But stop anyway."
    tb "Shame. I like consequences."
    s "I’m surprised you know that when you’ve likely never experienced any."
    tb "We can’t all be as {i}experienced{/i} as you, Akira. Which is why it’s your job to {i}teach{/i} people like us."
    s "I don’t think there’s anything I can teach you that you don’t already know, Tsubasa."
    tb "Oh, darling. We {i}both{/i} know that’s not true."
    s "..."
    tb "..."
    tb "Tell me — has Touka shown you where to find our massage parlor yet?"
    s "What?"

    scene returntothemanor21
    with dissolve

    to "{i}AAAAAAAAAAAHHHHHHHHHHHH!{/i}"
    tb "On second thought, maybe that’s a secret that would be best kept until next time."
    tb "Right now, you have a job to do."

    scene black
    with dissolve

    s "Yeah, what else is new?"
    tb "Tons, I’m sure! But I’m just an uninvolved passerby who doesn’t know any of it."
    s "And I’m the king of France. "
    tb "Oooh! Enchanté~ "

    "Tsubasa holds her hand out to me, but I ignore it before she has the chance to pull it away. "

    play sound "dooropen.mp3"
    scene returntothemanor22
    with dissolve2

    "But when I walk into Touka’s room to clear up the not-so-misunderstood misunderstanding, I quickly forget why I even opened the door in the first place."

    s "Okay. Now this is just unnecessary."
    to "Go away. I’m brooding."

    play sound "static.mp3"
    scene returntothemanor23 with flash
    stop sound

    s "Why are you brooding, Touka?"
    to "Because you made me look like a fool in front of my mother! And you made me {i}feel{/i} like a fool in front of me!"
    s "You can’t be in front of yourself. That’s not a thing."
    to "Shut up! And leave me alone!"
    s "Do you want to talk or not?"
    to "No! Go away!"
    s "Okay, well we’re going to talk anyway."
    to "Guards!"
    s "Please don’t call the guards on me. Someone needs to take care of Ami."
    to "Well maybe I can do it since I’m basically her grandmother now!"

    scene black
    with dissolve

    s "I’m coming over there. You have approximately ten minutes to prepare yourself before I make it."
    to "Stay away! I don’t want to see you right now!"

    "I obviously don’t stay away because I {i}do{/i} want to make this right. I’m just not really sure if I’ll be {i}able{/i} to since I’m still sort of figuring out what I want Touka to be."
    "Because {i}yes,{/i} she’s like a mother figure to me. "
    "But I’ve given you enough hints about how little something like that matters."
    "I want it to. Don’t get me wrong."
    "But some things are just beyond fixing and I often feel like I’m one of them."
    "Anyway, Touka recoils and crawls away the second I make it to her bed."

    play sound "static.mp3"
    scene returntothemanor24 with flash
    stop sound

    "Just kidding. She immediately leaps forward, knocking me over and crawling on top of me."

    to "A mother?! Really?!"
    to "I understand that I’m nurturing and comforting and that you’re a misguided pervert who has likely never experienced maternal love, but come on! Seriously?! I’m just a girl! You said it yourself!"
    s "It’s complicated, okay? I don’t really get it either. "
    to "Well, figure it out because that’s not a way I want to be seen! "
    to "I’m happy to comfort you when you need it! And I understand that you need it rather frequently because you’re a misguided pervert who has likely never experienced maternal love-"
    s "Did you really need to say that a second time?"
    to "But that’s just not the way I see us, Sensei!"
    s "Then how do {i}you{/i} see us, Touka?"

    scene returntothemanor25
    with dissolve

    to "That’s not something I can say now that I know you’re picturing me as your parent!"
    s "That’s not the {i}only{/i} way I picture you. And even if it was, it wouldn’t change anything about where this relationship can go."
    to "That is a very disturbing thing to say!"
    s "Yeah. This might come as a surprise to you, but I’m pretty fucked up in a lot of very unfortunate ways."

    scene returntothemanor26
    with dissolve

    to "Hah...I seriously can’t believe you just let me get carried away and...{i}flirt{/i} with you despite the way you’ve been seeing me this whole time. I called it a “date” and everything."

    scene returntothemanor27
    with dissolve

    to "When did this start? Because on the beach-"
    s "It was around Halloween, I think. "
    s "I was feeling lost and scared and you were just...the one I looked for. And it didn’t really dawn on me {i}why{/i} until I really started thinking about it."
    to "Do you know how {i}I{/i} interpreted that, Sensei?"
    s "I have my guesses."
    to "I thought you {i}liked{/i} me. I thought you really {i}did{/i} see me differently than everyone else."
    s "I do."
    to "But not in the right way!"
    to "I want you to see me as a woman."
    s "I-"
    to "The kind that’s not related to you. "
    s "So-"

    scene returntothemanor28
    with dissolve2

    to "I {i}like{/i} you. "
    to "And maybe this is inappropriate for me to say as your student, but that’s not stopping anyone else and it just isn’t fair if I’m the only one keeping it to myself at this point."
    to "If that disgusts you, fine. But it’s something you needed to know."
    s "It doesn’t disgust me at all."
    to "But you see me as a {i}mother.{/i}"
    s "Yeah, but I’ve also been staring at your chest all day."

    scene returntothemanor29
    with dissolve

    to "You’re probably just hungry. "
    s "I’ve also had an erection since the moment we met up pretty much."

    scene returntothemanor30
    with dissolve

    to "You know, I had a feeling that’s what was poking me but it felt wrong to point it out."
    s "Doesn’t all of this just show that you’re not {i}only{/i} like a matriarch, though? Like, there’s very clearly some {i}desire{/i} at play here."

    scene returntothemanor31
    with dissolve

    to "But will it ever {i}go{/i} anywhere? Or will you condemn me to the role of the one who comforts you upon your return home from someone else?"
    to "Because I can only tell you everything will be okay so many times. I can only give you so many lap pillows and so many head rubs."
    s "You can leave out the head rubs. Not really my thing."
    to "There needs to be something for {i}me.{/i} Do you understand what I’m saying?"
    to "I’m happy to give, but not without something in return. "
    to "And what I want in return is far more intimate than a lap pillow."
    s "..."
    to "Do you understand what I’m saying?"
    s "Do I really need to say it?"
    to "Yes."
    s "The thing that’s poking you isn’t giving it away?"
    to "I need to hear you say you understand. "

    "She doesn’t blink."
    "She doesn’t move."
    "She stays perfectly still like one of the many monuments in the room and, in every single way, she’s more beautiful than all of them."
    "To think this creature on top of me, who rivals the output of artisan hands without any effort at all, would want {i}me{/i} is perplexing."
    "She’s not a random girl in a random high school class. She’s a young woman who could have {i}anyone{/i} she wants. And {i}still{/i} it’s me. "
    "I don’t get it."
    "I’ll never get it."

    s "I understand."

    "But I tell her I do because that’s what I’m good for — filling holes in hearts and bodies while ignoring the gaps in myself."

    scene returntothemanor32
    with dissolve

    to "..."
    s "..."
    to "Will you condemn me, Sensei?"
    to "Or will you make me grovel?"
    s "Would you actually grovel for me?"

    scene returntothemanor33
    with dissolve

    to "If it works, maybe. I’ve never tried before."
    s "You like me that much, huh?"

    scene returntothemanor34
    with dissolve

    to "I have very poor taste in men, apparently."
    s "You really do. "
    s "But no..."
    s "I won’t condemn you."

    scene returntothemanor35
    with dissolve

    to "So..."
    s "I can’t change the way I see you. "
    s "But I also can’t deny the fact that I want to fuck your brains out."

    scene returntothemanor36
    with dissolve

    to "Oh my."
    to "That was...forward."
    s "Yeah, well...you asked."

    scene returntothemanor37
    with dissolve

    to "I did, didn’t I?..."
    s "..."
    to "..."
    to "I...um..."
    to "I also..."
    to "Would like for you to do that..."

    scene returntothemanor38
    with dissolve

    to "N-Not right now, though! Eventually!"
    to "This is all...happening really fast and..."
    to "I will admit that I’m still rather turned off by the fact that you’d do such a thing with someone you’re openly admitting to viewing as a mother figure. Even if the figure in question is a teenage girl. "
    s "Yeah. I can’t say I really blame you for that."

    scene returntothemanor34
    with dissolve

    to "So...what do we do now? Mother is bound to ask what transpired in here when I see her in the morning."
    s "If you really want to fuck with her, just tell her we had sex."

    scene returntothemanor39
    with dissolve

    to "Sensei! I couldn’t possibly-"
    s "Stop."

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "Call me Akira from now on."

    $ renpy.end_replay()
    $ toukaspring2 = True
    $ touka_love += 1

    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2

    "Touka and I decided it would be best to keep our conversation confidential from Tsubasa, but I can only guess how well that will work."
    "I’m sure she’ll find out sooner or later."
    "And I’m sure she’ll just try to get herself involved again once she does."
    "So yeah, that could be really problematic given the nature of our relationship and what the future holds."
    "But I’m trying to think of the positives."

    scene black

    "And the positives in this case sound very exciting."

    se "Come to bed, Aki-kun."

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
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

label toukaspring3:
    scene toukabuysporn1
    with dissolve2
    play music "marshmallow.mp3"

    "It was a normal day in the life of Makoto Miyamura."
    "She was sitting behind the desk of her family’s porn shop, reading one of just three or four books sold in Kumon-mi and thinking to herself-"
    "Wait, no. Actually — it was a different book. But they all have the same cover due to asset limitations or something like that. Yeah."
    "But anyway, she was reading it and thinking to herself, “Wow. I’m really fucking bored.” Which you might also be thinking right now as you’re reading this. And you know — fair. "
    "We’re well past due for a reset by now and, without a clear direction to head in order to invoke (or evoke or whichever voke was correct there) one, it sometimes feels like things are dragging on."
    "It sometimes feels like we’re just repeating the same thing over and over again and- oh. I get it. "

    play sound "static.mp3"
    scene toukabuysporn2 with flash
    stop sound

    "In that case, why don’t we shake things up a bit?"

    play sound "static.mp3"
    scene toukabuysporn3 with flash
    stop sound

    "A book was sitting behind the desk of the Miyamura family porn shop and reading one of the Miyamuras. There we go. That should keep you held over until something traumatic happens again."
    "So, as it was sitting there or standing or hovering or whatever it was doing, it was thinking to itself, “Woah, hot girl.” And it was right. "

    play sound "static.mp3"
    scene toukabuysporn4 with flash
    stop sound

    "So it stuffed her into its little book mouth and started chewing on her until the top half was all mushy and gross and the bottom half was still able to be penetrated by anyone with a necrophilia kink. "

    play sound "static.mp3"
    scene toukabuysporn1 with flash
    stop sound

    "There we go. That was fun. Unlike real life — in which Makoto Miyamura was {i}still{/i} just reading a book. "
    "But what makes it even more boring is that she’s been doing this ever since the last beach trip ended while waiting for the newest Touka event to trigger."

    q "{i}Ahem.{/i}"

    scene toukabuysporn5
    with dissolve

    "Oh, look. There it goes now."

    play sound "static.mp3"
    scene toukabuysporn6 with flash
    stop sound

    q "One pornography please."
    mak "..."
    q "..."
    mak "What flavor would you like?"
    q "Uhh..."
    mak "..."
    q "Just the...regular one will do."
    mak "Small, medium, or large?"
    q "Medium, please. And a cup of green tea as well. Thank you."
    mak "Sure. Just show me your membership card and I’ll get that started for you."
    q "M...Membership card?"
    mak "Of course. You can’t buy porn in Japan without a membership card. Is this your first time?"
    q "N-No! Of course not. I just...I left it at home! But surely you’re willing to overlook such a careless mistake and...provide the pornography regardless, correct?"
    mak "Only if you do the pornography dance. I sadly can’t help you without receiving dance moves as collateral in lieu of your porn membership."
    q "..."
    mak "..."

    scene toukabuysporn7
    with dissolve

    q "Pornography-"

    scene toukabuysporn8
    with dissolve

    q "Dance-"

    scene toukabuysporn9
    with dissolve

    q "Provide-"

    scene toukabuysporn10
    with dissolve

    q "Please-"
    mak "What the hell is that supposed to be?"

    scene toukabuysporn11
    with dissolve

    q "I apologize for such a pathetic display. I never learned the dance."

    play sound "static.mp3"
    scene toukabuysporn12 with flash
    stop sound

    "It was no longer a boring day for Makoto Miyamura."

    mak "Why are you here, Touka?"

    play sound "static.mp3"
    scene toukabuysporn13 with flash
    stop sound

    to "H-How did you know it was me?!"
    mak "Because there’s no one else in the entire world that would have fallen for that."

    scene toukabuysporn14
    with dissolve

    to "Wha- I knew that dance must have been a lie!"
    to "You just wait until I receive my pornography membership card! You’ll be sorry to have crossed me then!"
    mak "You know you can just watch porn for free on the Internet, right?"

    scene toukabuysporn15
    with dissolve

    to "Well...y...yes. But..."
    to "I learned recently in a...very embarrassing way that Internet traffic isn’t exactly...{i}private.{/i}"

    scene toukabuysporn16
    with fade

    mak "It sounds to me like you just need NordVPN."
    to "N-NordVPN?"
    mak "Cybersecurity. Built for everyday. "
    mak "Staying safe online is becoming increasingly difficult thanks to malicious hackers and companies who want to sell your information and search history for profit."
    mak "But with NordVPN, you can change your IP address from your very own computer, making you harder to track and securing your privacy."

    scene toukabuysporn17
    with fade

    to "Why thank you, Makoto. I’ll have to look into this product when I get home as it was quite difficult having to explain my search history to my overly-curious mother."
    mak "Don’t mention it. Just be sure to use the code MAKOTO5 at checkout for 20%% off your order."
    mak "This message has not been formally sponsored or endorsed by NordVPN. "
    to "Oh, look. All of the little logos are suddenly fading away."
    mak "Yeah, product placement’s been getting out of hand lately. Why are you {i}really{/i} here, though? Is it seriously {i}just{/i} for porn? Because we have other stuff too, you know."
    to "I know. I’m still waiting on my green tea."
    mak "No, I meant like toys and costumes and all sorts of stuff like that. And I make commission on these things called DildoSabers that-"

    scene toukabuysporn18
    with dissolve

    to "Oh, n...no. My mother has made sure I have all of...{i}those objects{/i} I could...{i}ever{/i} possibly need. They’re just...{i}intimidating.{/i}"
    mak "Yeah. You get used to it."
    mak "Sometimes {i}too{/i} used to it."

    scene toukabuysporn19
    with dissolve

    to "Do you have any...educational materials, perhaps? Secret...resources that only members of the lower class would know about?"

    scene toukabuysporn20
    with fade

    mak "I mean...we have Girls Gone Wild."
    to "What’s that?"
    mak "A series of DVDs featuring mainly American girls."
    to "What do they do, exactly?"
    mak "...Go wild? "
    mak "I’m not really sure what else to tell you."
    to "Ugh...just the green tea then. I suppose I’ll have to figure things out elsewhere."

    scene black
    with dissolve2

    mak "You know...it’s getting close to closing time. Do you want to come up to my room and talk for a little while? That’s where all the tea is anyway."
    to "Well, I...suppose it wouldn’t {i}hurt.{/i} "
    to "But I’ve also been taught to exercise caution when people in what my family refers to as “seedy areas” invite me anywhere. And I believe this establishment meets that criteria."
    mak "Which is something I’d agree with basically every single time except this one since I just happen to live here by a bad stroke of luck and am not sexually attracted to girls."
    to "Oh, excellent. I am also not sexually attracted to girls. I am excited to bond over this shared connection with you over tea."
    mak "Please don’t make it weird."
    to "With all due respect, you are making this just as weird as I am."

    scene toukabuysporn21
    with dissolve2

    "And so the two of them made their way up the stairs and into Makoto’s bedroom."
    "The pictures lining the stairway had all been removed, so this new set of eyes was deprived of the same experience an older set had just a short while ago."
    "It was back when hope had only just begun decaying. But now, its had ample time to decompose, and all that remains is a shell of what once was."
    "But to that shell’s left was a skeleton that still wore fresh meat. Which, of course, had spawned some jealousy. But not the type that would warrant cyanide-laced tea."
    "It was the type that filled her with an indescribable emptiness — and the depressing, untimely realization that she’d given herself up long before she was destined to."

    mak "You don’t have to sit seiza-style, Touka. There’s no expectation of formality once you’re invited into someone’s room."
    to "I actually prefer to sit this way. It feels more comfortable."
    mak "{i}That{/i} feels more comfortable? Really?"
    to "As the heir to the Tsukioka Foundation, I’ve been sitting in on formal presentations and meetings ever since I was a girl. Almost all of which required me to appear as proper as possible."
    to "So yes, I suppose this just feels more natural for me."

    scene toukabuysporn22
    with dissolve

    mak "Weird. The only times we ever had to do that in my family were when we went out to fancy restaurants. And even then, my mom always complained about it."
    to "How interesting. I continue to be intrigued by your people’s ways of life."
    mak "So, tell me — what is it you want to know about sex?"

    scene toukabuysporn23
    with dissolve

    to "Wha- why are we back to that all of a sudden?!"
    mak "That’s what you came here for, right? "
    mak "I doubt we have any sort of “reference materials” that your family wouldn’t already have access to. But if you have any specific questions, I might be able to help."

    scene toukabuysporn24
    with dissolve

    to "And you...wouldn’t mind doing that?"
    mak "Not at all. I’m supposed to be open about that sort of thing given my job and whatnot."

    scene toukabuysporn25
    with dissolve

    to "Oh, thank heavens. Because I tried talking to Chika about this, but she was just so...{i}graphic.{/i}"
    mak "It’s kind of hard {i}not{/i} to be sometimes. Sex is super intimate, and letting someone literally {i}inside{/i} of you is kind of a...{i}graphic{/i} thing."

    scene toukabuysporn26
    with dissolve

    to "Is it truly as...{i}painful{/i} as it sounds?"
    mak "It’s different for everybody. Some people actually enjoy their first time. It’s definitely {i}weird,{/i} though. But, like...a good kind of weird."
    mak "Is it just the pain part you’re worried about? "

    scene toukabuysporn27
    with dissolve

    to "Well...{i}no.{/i} "
    to "If anything, I’d say that’s one of the things I’m least concerned about. I’ve received an...extremely detailed and lengthy explanation about how sexual intercourse works and...what to expect physically."
    to "It’s the emotional aspect of it I’m struggling to understand as that was never covered in any of the presentations I watched."
    mak "Uh...presentations?"
    to "I think my biggest question right now is...when is the right time to engage in that sort of conduct?"

    scene toukabuysporn28
    with dissolve

    to "At what point is such a thing acceptable and...how am I supposed to act when that time {i}does{/i} come? Do I just...remove my clothes and lie there? Am I meant to be the aggressor?"
    to "Who initiates what? How long does it go on for? How frequently does such a thing even occur between partners?"
    mak "{i}That’s{/i} what you’re worried about?"
    to "I have no romantic experience whatsoever, so...all of this just feels strange and...new to me."

    scene toukabuysporn29
    with dissolve

    mak "Yeah...that’ll happen. But I think that’s meant to be part of the fun."
    mak "Meeting someone and learning that you {i}want{/i} to do that stuff with them is, like...the first {i}real{/i} step to growing up, I think. Or at least becoming a “woman.”"
    mak "My mom always says that sex is like a dance, but I think that extends to romance as a whole. And the hardest part of learning any dance with a partner is learning how to not step on their feet. Probably."
    mak "I don’t know. I’ve never danced before."
    to "Technically, you’re not far off. Simply learning to control one’s body as a whole is the most difficult part of dancing. I’m formally trained in five different styles."
    mak "I never would have known based on your porn dance from earlier."

    scene toukabuysporn30
    with dissolve

    to "I once again apologize for such a terrible, inappropriate display. I haven’t felt that embarrassed since I learned how to use a vending machine."
    mak "There’s nothing to be embarrassed about, Touka. This whole situation is one that’s essentially impossible to be comfortable with at first."
    mak "It was the same for me and I legitimately grew up hearing my mom get railed down the hall on a weekly basis."

    scene toukabuysporn31
    with dissolve

    to "Oh, I’ve played that game before!"
    mak "...Game?"
    to "Yes. My whole family played the railing game just before we learned what tacos are."
    mak "...Okay. "

    scene toukabuysporn32
    with dissolve

    mak "Anyway, the point is that it’s fine to not know how any of this stuff {i}works{/i} yet as long as you know how to, like...{i}actually{/i} do it. "
    mak "And even then, you’re probably going to find yourself just letting your partner “do his thing” most of the time since that partner is probably going to be Sensei and he likes to be in control."

    scene toukabuysporn33
    with dissolve

    to "Uhhh wh- what? No. I never said that. Why would you bring him up? That’s crazy. You’re a crazy girl. You say crazy things. What? Sensei? No. That’s ridiculous. What?"
    mak "Touka, it’s fine. I’m not going to tell anyone. Besides, I’m sure {i}he’d{/i} be willing to help you with all of this too if you only asked."
    mak "But I guess the reason you’re asking the girls instead is because you don’t want to embarrass yourself in front of him. Which, hey — fair. I’m no stranger to wanting to impress that guy."

    scene toukabuysporn34
    with dissolve

    to "How...do you know all of this, exactly?"
    mak "Oh, is that not obvious? I’ve been having sex with him for years."

    scene toukabuysporn35
    with dissolve

    to "You what?"
    mak "He’s screwed me so many times by now that I’m pretty sure I could accurately choose his dick out of a line of like...one thousand penises."
    to "{i}That’s so many...what are they all doing there?{/i}"
    mak "His is enormous, though. So picking it out probably wouldn’t be hard even if he only screwed me one time instead of hundreds."

    scene toukabuysporn36
    with dissolve

    to "How..."
    to "How large would you say “enormous” is exactly?..."

    scene toukabuysporn37
    with dissolve

    mak "Mmm...maybe like this?"
    to "Dear lord."
    mak "{i}Yeaaaah.{/i}"

    scene toukabuysporn38
    with dissolve

    mak "{i}He’s good with it too.{/i}"
    to "..."
    mak "Any more questions, Touka?"
    to "Yes. Who are you?"

    scene toukabuysporn39
    with dissolve

    mak "Teacher’s pet, of course. "
    mak "He can do anything he wants to me any time he wants to do it. "

    scene toukabuysporn40
    with dissolve

    mak "Which is why I’m hoping you fail. No offense. "
    mak "You won’t, of course. You’re beautiful. And Sensei would have sex with pretty much anyone to begin with. So if by some stroke of luck you manage to fail, that means more sex for me."
    to "..."
    mak "Now what? Want me to get as {i}graphic{/i} as Chika did? Because I’m sure I have plenty of stories for you if you want to hear them."

    scene black
    with dissolve2

    to "I actually think it’s time for me to go home."
    mak "Wait, Touka. You’ve barely touched your tea. Why not sit back down and finish it up while I tell you about the time he walked in on me masturbating downstairs?"
    to "N-No thank you! It is very late!"
    mak "Or the time he took my virginity at our first Halloween party..."

    play sound "doorslam.mp3"

    to "{i}G-Goodnight, Makoto!{/i}"
    mak "Goodnight!"
    mak "..."
    mak "..."
    mak "..."

    play sound "thump.mp3"

    mak "Ugghhhh! When will it ever end?!"

    "Makoto Miyamura slams her head down onto her table while instinctively reaching toward the same book she was stuck in at the beginning of the event."
    "Touka Tsukioka, on the other hand, elects to walk back to the dorm instead of calling one of her drivers."
    "When she arrives there, she checks to make sure her roommate is asleep before unlocking a secret compartment built into the foot of her bed."
    "Then she slides open a drawer and rummages through a seemingly endless supply of sex toys, hoping to find one that matches the size Makoto showed her roughly one hour ago."

    play sound "vibrate.mp3"
    stop music fadeout 12.0

    to "Ah!"

    "But then she accidentally turns one on and scares herself."

    ya "Mn...Touka?...Is that you?..."

    play sound "doorslam.mp3"

    to "No! I mean...yes! "
    ya "What are you-"

    play sound "tackle.mp3"

    to "Nothing! Goodnight, Yasu! Sweet dreams! "

    "She once again goes to sleep without using any of them. "
    "But it takes her hours this time as her mind has trouble returning from its adventure into the sewers."

    $ renpy.end_replay()
    $ toukaspring3 = True
    $ touka_love += 1
    $ makoto_love += 1

    "{i}Both Touka and Makoto’s affection increased by 1! And you didn’t even have to do anything this time!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label toukaspring4:
    if _in_replay:
        play music "newhope.mp3"

    scene toukadownstairs1
    with dissolve2

    "We’re ushered through a winding hallway toward a set of stairs that seldom sees sentience. Each step feels like a promise. Each promise is immediately broken."
    "I have trouble focusing on what exactly is happening. It all feels surreal. I’d resigned myself to the idea that this place was little more than a shell to house delusions in. Now the shell is gaining a mind of its own."
    "The torches on the walls, rarely ever lit as I can only imagine, lock the eyes they shouldn’t have on me and ask me why I’m going along with this."
    "It’s like they have seen what has transpired in the lower plane and want to silently talk me out of it. But I am unable to respond. I merely look at them and return the silence — asking why they care."
    "All the while, a hand rests on my shoulder and forces me down further, uncaring that the torches talk. And there is nothing I can do to change that as it stems from a mind with its roots already sunken in."
    "The death grip they have on my legs makes it feel as if those arboreal veins have become the laces of my shoes — and they attempt to pull me down only to be met with instant gratification and prophesied success."
    "There is nothing I can do to stop what is coming. That is something I have resigned myself to as well. Long before I knew this place existed. Long before I knew {i}she{/i} existed."
    "This peculiar half-mento. Those blinding blue eyes that can peer through my armor and dissolve my resolve. "
    "I want to break her open to see what’s inside. I can only imagine what colors would spill out."

    ya "Almost there! Almost there!"

    play sound "static.mp3"
    scene toukadownstairs2 with flash
    stop sound

    to "Almost {i}where,{/i} Yasu? Are you escorting us to some sort of...ritualistic room? Where this apparent vow must take place?"
    ya "Yes! Exactly! I heard Him just now, Touka! He told me where to take you! He says my wings are naught more than a whale away!"
    to "He measures things in whales?"
    ya "Whales, tails, the shells of snails! As pale as Michael’s bed of nails!"

    scene toukadownstairs3
    with dissolve

    to "Oh, why didn’t you just say so? I completely understand now."
    ya "Do {i}you{/i} understand as well, little lamb? Before we turn your legs to meat, you must feast on wheat! We beg you, eat!"
    s "........."

    scene toukadownstairs4
    with dissolve

    ya "Silence, violence, noncompliance. How shall I guide who seeks no guidance?"
    to "I believe an effective place to start would be {i}not{/i} mentioning that you want to turn his lamb legs into meat."
    s "Is this really part of the game, Yasu?"
    ya "This {i}is{/i} the game. "

    play sound "static.mp3"
    scene toukadownstairs5 with flash
    stop sound

    ya "{b}YOU ARE GOING TO HAVE SO MUCH FUN!{/b}"

    play sound "static.mp3"
    scene toukadownstairs6 with flash
    stop sound

    to "What...{i}is{/i} this, Yasu?"
    s "I’m pretty sure it’s a jail cell."
    to "I’m aware of what it {i}appears{/i} to be. But I don’t believe that churches typically double as prisons."
    ya "This is no prison. This is salvation."

    play sound "static.mp3"
    scene toukadownstairs7 with flash
    stop sound

    ya "This is a chance to be reborn!"

    play sound "static.mp3"
    scene toukadownstairs8 with flash
    stop sound
    play sound "cellslam.mp3"

    to "Why you- Yasu! What the hell do you think you’re doing?! Unlock this blasted cell at once! You said you were bringing us here to make a vow! Not to keep us as prisoners! "
    ya "You’re {i}not{/i} prisoners, Touka! Prisoners don’t have the luxury of deciding when to leave! {i}You{/i} do!"
    to "Excellent! I would like to leave now!"

    scene toukadownstairs9
    with dissolve

    ya "Okay!"
    to "Oh. Was it...was it really that easy?"
    ya "It will be! You just have to complete the vow."

    scene toukadownstairs10
    with dissolve

    to "Hah...fine."
    to "I, Touka Tsukioka, hereby vow to not change my color and...whatever else I am supposed to vow to complete Yasu’s ritual. The end."
    ya "That’s not how the vow goes."

    scene toukadownstairs11
    with dissolve

    to "I don’t {i}know{/i} how the vow goes! You haven’t told me what I’m supposed to say! "
    ya "You’re not really supposed to {i}say{/i} anything. It’s about what you {i}do.{/i}"
    s "Uh-oh."
    to "Well, what am I supposed to {i}do{/i} then?!"

    scene toukadownstairs12
    with dissolve

    ya "Make a baby!"
    to ".............................."

    scene toukadownstairs13
    with dissolve

    ya "I’ll give you two some privacy! Bye!"

    play sound "static.mp3"
    scene toukadownstairs14 with flash
    stop sound

    to "Privacy, my ass! Get back here you little evangelist! I am {i}not{/i} losing my virginity in a dungeon!"
    s "So, it appears that I may have been wrong when I said that we should just go along with her to see what happens."

    scene toukadownstairs15
    with dissolve

    to "You think?!"
    s "Yeah. At the same time, though, now I finally get a chance to grope you. So that’s cool."
    to "How can you make jokes at a time like this?! We’re trapped in a dungeon and apparently not allowed to leave until I’m pregnant! "
    s "Yeah, but you’re the one who has to carry the child. Not me."
    to "I will murder you!"
    s "Touka, relax. Yasu’s not even here. We can just tell her we had sex and she’ll just...go along with it whenever she gets back, probably. "

    scene toukadownstairs16
    with dissolve

    to "Yes, because hiding the truth from a girl who can see into the future {i}and{/i} past is a thing that can definitely be done."
    s "Use your phone to call for help then. Or try and squeeze through the bars. You’re small enough. You probably can if I give you a push."

    scene toukadownstairs17
    with dissolve

    to "I...suppose that may be possible. This entire situation is just frustrating to me. "
    to "I tried so hard to create an environment in which Yasu can feel {i}normal{/i} again only to be given the harshest possible reminder of {i}why{/i} we decided to medicate her in the first place."
    to "It’s one thing to be impulsive. But to throw people who care about you into situations like this is-"
    s "It’s like it’s not her at all, right?"

    scene toukadownstairs18
    with dissolve

    to "She was fine just hours ago..."
    to "It wasn’t until you were brought into the picture that she started going off the rails again. I just...don’t understand what is going on between you two. How can you affect her so dramatically?"
    s "That’s what I want to know too because there clearly is {i}some{/i} sort of merit to it. I can’t just ignore it and call her crazy anymore."

    scene toukadownstairs19
    with dissolve

    to "So, what’s the plan then? Humor her and just...sit down here, wait until she comes back, then inform her that I’m carrying your child?"
    s "If you really want to sell it, you can make some really loud sex noises. Then she {i}really{/i} wouldn’t be able to deny that we did it."

    scene toukadownstairs20
    with dissolve

    to "Or we can just actually do it."
    s "..."
    to "That was obviously a joke."
    s "It wasn’t that obvious."

    scene toukadownstairs21
    with dissolve

    to "May I offer you a seat? "
    s "May I offer {i}you{/i} one? On my penis?"

    scene black
    with dissolve2

    to "No, I think the mattress will be just fine."

    play sound "tackle.mp3"

    s "You’d be humming a different tune if we were in your oversized bedroom, I bet."

    play sound "static.mp3"
    scene toukadownstairs22 with flash
    stop sound

    to "Probably a lullaby since I’m effectively your mother and whatnot."
    s "Are you really going to sit like that?"
    to "Yes. This is just how I sit. And I will not let the fact that I am in jail influence my dignity and refinement in any way."
    s "Suit yourself. Just think you might actually enjoy it if you try to relax a little."
    to "In a {i}jail cell?{/i} With a man I have {i}feelings{/i} for? Have you gone mad? "
    s "Yeah. Quite a while ago, actually."
    to "At least you’re honest. It’s quite irritating being one of the only people in this god-forsaken city with a level head. "

    play sound "static.mp3"
    scene toukadownstairs23 with flash
    stop sound

    s "How {i}does{/i} this all look to someone with a level head, exactly?"
    to "Like utter nonsense, that’s what. You’d think I’d be used to it by now. But apparently, even constant exposure to the abnormal can’t normalize it. "
    to "It’s chaos every day in the outside world, and I’d be lying if I said I don’t miss my bubble at times. But I suppose there are pros to this sort of {i}exposure{/i} too."
    s "I’m one of them, right?"
    to "Of course. Though, I will say that I like you more when we’re {i}not{/i} trapped in a jail cell together."
    s "We’re not {i}really{/i} trapped at all. We’re just playing charades and humoring your friend. Just like we were when she brought us down here."
    to "...Yes. I suppose that’s right."
    to "But it doesn’t change that it {i}feels{/i} wrong."

    play sound "static.mp3"
    scene toukadownstairs24 with flash
    stop sound

    to "Which is a feeling only exacerbated by the fact that one of her dolls is staring at us from across the hall."
    s "Which one do you think that is?"
    to "Don’t ask me. I’m not the one who remembers their names."
    s "Why do you think it’s down here?"
    to "If I had to take a wild guess, I imagine it’s due to some {i}other{/i} strange ritual or game Yasu’s schizophrenia has induced. "
    s "You don’t actually think she has that, do you?"
    to "I...don’t. Not anymore at least. But when every doctor in Kumon-mi continues to land on that as the diagnosis, I find it easier to just go along with it than to come up with a {i}new{/i} term."
    to "On the bright side, though...the facility Yasu seems to have the most luck with has experienced such a thing before. Which is why I imagine we’ll keep going there from this point on."
    to "So long as they keep allowing me to sit in on her evaluations, that is."
    s "Such a thing as...as Yasu? Really? How?"
    to "Patient confidentiality agreements unfortunately prevent me from knowing any more than the fact that they have seen someone else with her condition before."
    to "And I only know that in the first place because her doctor informed me."
    s "Can’t you just...use your money and influence to extract that information from them if it means coming closer to a potential solution? For Yasu’s sake of course."
    to "Yes, Yasu’s sake. I’m sure your rampant curiosity has nothing to do with it."
    s "Two birds. One stone."
    to "Unfortunately, I’m not sure I could. I had a hard enough time just getting the staff to allow me to {i}watch.{/i} I imagine my mother would, though. She has connections there."
    s "That’s not surprising. She has connections everywhere."

    play sound "static.mp3"
    scene toukadownstairs25 with flash
    stop sound

    to "Being the most powerful woman in the city has its perks."
    s "Think you can get her to pry a little bit for the sake of your friend? {i}And{/i} my curiosity?"
    to "Under normal circumstances, yes. But she’s been busier than normal lately thanks to..."
    to "Thanks to something I...am supposed to keep secret."
    s "Well, now I {i}have{/i} to know."
    to "I’m afraid that telling you wouldn’t accomplish much in the grand scheme of things. If anything, I Imagine it might put all of us at risk, actually."
    s "“All of us” as in-"
    to "My family, of course. This is a personal matter. One that you needn’t-"

    scene toukadownstairs26
    with dissolve2

    to "..."
    s "Do {i}you{/i} want to talk about it?"
    s "Or should I just leave it alone?"
    to "..."
    to "That’s a dirty move — placing your hand on my shoulder like that when you know you’re one of my weaknesses."
    s "One of my only specialties is exploiting those in every one. You’re one of the easiest, surprisingly. You’re too kind."

    scene toukadownstairs27
    with dissolve

    to "Hm."
    to "You sound like my sister."
    s "Yeah, I can see Tsukasa saying something like that. I’m actually the type to capitalize on it, though. She doesn’t have the heart yet."
    to "Oh, she has the heart. She’s extremely capable for her age. Which is..."
    to "Precisely what..."

    scene toukadownstairs28
    with dissolve

    to "This specific issue...entails."

    play sound "static.mp3"
    scene toukadownstairs29 with flash
    stop sound

    s "What do you mean?"
    to "..."
    s "Is something going on with Tsukasa?"
    to "We...should probably...not discuss-"

    play sound "static.mp3"
    scene toukadownstairs30 with flash
    stop sound

    to "Ah-"
    s "Your secret’s safe with me."
    to "Why, that’s not true at all."
    to "You’re the type of man who destroys everything he touches."
    to "There is {i}nothing{/i} that is safe with you."
    s "{i}This{/i} is."
    to "And why should I believe that?"
    s "Because I know that revealing it to anyone will destroy my chances of ever getting you somewhere like this with your consent."
    to "You want me to...consent to being a prisoner?"
    s "Mostly just...in a private room with me."
    to "I see..."
    to "And you’re {i}really{/i} not at all disturbed by the fact that you see me as a matriarch?"
    s "You’re more disturbed by that than I am."
    to "That is true. I {i}am{/i} quite disturbed. But I supposed Oedipal complexes aren’t {i}exactly{/i} unheard of. "
    s "You’re also not my real mother."
    to "What was your real mother like?"

    scene toukadownstairs31
    with dissolve

    s "Don’t change the subject. Tell me what’s going on."
    to "Or what?..."
    s "I’ll have to force it out of you."
    to "How?..."
    s "I..."
    s "Don’t know..."

    scene toukadownstairs32
    with dissolve2

    to "Mm..."
    to "Cute."
    to "So close to making me crumble, just to collapse yourself at the very end."
    to "I like you, Sensei...enough to open a window to my heart. But I’m afraid that I can’t open {i}any{/i} windows to my family until I know how serious you are."
    s "About what?"
    to "What do you think?"
    s "{i}You?{/i}"
    to "{i}Me.{/i}"

    scene toukadownstairs33
    with dissolve2

    to "I’ve already taken Yasu in...I have no qualms at all with...{i}taking you in{/i} too..."
    s "You don’t really want a peasant like me. I’m just the closest you’ve ever had to someone who won’t put up with your shit."

    scene toukadownstairs34
    with dissolve2

    to "You’ll put up with anything I want you to."
    to "You might think you have a hold on me, Sensei...but {i}I’m{/i} the one who pulls the strings here."
    to "If I ask you to jump...you jump."
    to "If I ask you to beg...you beg..."

    scene toukadownstairs35
    with dissolve2

    to "If I ask you to {i}come...{/i}what do you do?"
    s "Come..."

    scene toukadownstairs36
    with dissolve2

    to "Yeah?..."
    s "..."
    to "You’d come for me?..."
    s "Mhm..."
    to "See?..."
    to "I have you wrapped around my finger..."
    to "I’m the...one...who..."

    scene toukadownstairs37
    with dissolve2

    to "Ah..."
    to "I’m suddenly...quite...dizzy..."
    to "Isn’t it rather...hot in here?..."
    s "Tell me what to do...Touka..."

    scene toukadownstairs38
    with dissolve2

    to "Hah...hah...do I really have to spell it out for you?"
    to "Let’s give that fucking {i}god{/i} what he wants..."
    ya "Yay!"

    play sound "static.mp3"
    scene toukadownstairs39 with flash
    stop sound

    to "Wha-"

    play sound "static.mp3"
    scene toukadownstairs40 with flash
    stop sound

    ya "........."
    to "Y...Yasu! Open the door! We’ve been down here long enough!"
    s "Or just go back upstairs for a few minutes. That works too."
    ya "Did you spill your seed inside of her body? Have the roots begun to grow? Is the vow complete?"
    s "No, I need more time."
    to "L-Lies! I...am full of his seed as we speak! Even now, the...presence of light within me moves! I can feel it! It is...spectacular!"

    scene toukadownstairs41
    with dissolve

    ya "I knew it! I knew you’d love it! Now, you can be happy! Now, an angel can be born! You shall name him Pahaliah! Just as He wants! Just as He says! "
    to "Yes, yes! Whatever must be done! Now, release me so I can spread the word! Release me! Release me!"

    scene black
    with dissolve
    play sound "celldoor.mp3"

    ya "Okay, Touka! Here you go! I told you it was easy! I-"

    play sound "static.mp3"
    scene toukadownstairs42 with flash
    stop sound

    to "How {i}dare{/i} you lock me in a cage like some sort of...animal! Even as part of a game, this was entirely unacceptable, Yasu! You know better than this!"
    ya "You..."
    ya "You lied to me?..."

    scene toukadownstairs43
    with dissolve

    ya "Nothing grows inside of you...there is no light to be delivered..."
    to "Yes! I {i}did{/i} lie! Just like {i}you{/i} lied when you said we could choose when to leave!"

    scene toukadownstairs44
    with dissolve

    ya "I...was just repeating what I heard! I don’t know all the rules! The instructions are always different! I-"
    to "I don’t care! I will humor you as often as you want! I will take you here to {i}communicate!{/i} But I will not allow you to take advantage of my kindness and treat me like a toy for your god! Do you understand?!"

    scene toukadownstairs45
    with dissolve2

    ya "......no..."
    ya "I don’t understand anything..."

    scene toukadownstairs46
    with dissolve

    ya "I don’t understand anything! I’m a useless messenger! A broken doll! I don’t deserve your kindness! I don’t deserve your love!"
    to "Wait! No! Don’t cry! I didn’t mean it! It’s just...locking people in cells is {i}wrong,{/i} Yasu! You can’t do that no matter {i}what{/i} you hear! Okay?"
    ya "I just...want...to...save you! I’m sorry, Touka! I’m sorry, Sensei! I’m a failure! I’m a worm! I’m not fit for ascension!"
    s "Yeah...yelling at her probably wasn’t the best move."

    scene toukadownstairs47
    with dissolve

    to "Oh, well you’re just {i}full{/i} of excellent advice today, aren’t you?!"
    ya "AaaAaaAaHHH!! AAAaaAAAAAHHHHH!"

    scene black
    with dissolve2
    stop music fadeout 12.0

    to "Yasu! No crying! Okay? Come with me. Back upstairs. We’ll get you home and into bed. Okay? Okay??"
    ya "Aaahhh...AaaaAAhh...Aaaahhhh...."
    to "Sensei, would you mind-"
    s "I’ll leave, yeah. Being around me is...clearly not healthy for her."
    to "Thank you...and..."
    to "About that...issue I mentioned...could you please not bring it up to my mother? The idea of the two of you communicating behind my back is...well, disturbing enough to me as-is."
    s "Yeah. I understand."
    s "Get Yasu home safe, okay? And Yasu — thanks for showing me the color game. I had fun."
    ya "{i}Sniff...{/i}you did?..."
    ya "Really?..."
    s "Yeah...tell Etinsib Ziwa I’d like to actually speak with him some day. I’d like to learn more about what he knows."
    ya "{i}Sniff...{/i}okay...I’ll tell him..."
    to "Say goodnight, Yasu. We have to get you home."
    ya "Goodnight...Sensei..."
    s "Goodnight...both of you."

    "I leave the cathedral before either of them have the chance to follow me out."
    "The torches ignore me this time. So do the walls. So does everything."
    "But there is a single rabbit doll I pass by on my way out of the building with eyes like stained glass that follow me all the way home."
    "I can feel them even now that I’m lying here in bed — burning holes through the body that sleeps beside me on the way to my chest."
    "I imagine they won’t ever leave."
    "I imagine they can’t."
    "I imagine I’m asleep."
    "I am."

    $ renpy.end_replay()
    $ toukaspring4 = True
    $ touka_love += 1

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
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

label toukaspring5:
    play music "tsukiokamanor.mp3" fadein 3.0
    scene tsukiokasonthecouch1
    with dissolve3

    "Two girls on a couch in a house in a town that won’t stop growing — but they were safe within these walls from the clutches of those ever-expanding tendrils that no one ever sees!"
    "They were both very pretty. They were both very kind! But the heart of one was much brighter than the heart of the other."
    "And while the color of a heart does not dictate the way and speed with which it beats, it {i}does{/i} paint a mostly accurate picture of whether or not someone can be trusted."
    "Would “trust” be an important element to this conversation? Who knows?! For they already trusted each other. But did they {i}really?{/i}"
    "A mother’s relationship with her daughter can be quite difficult to understand, you know? That said, however — there is nothing like it in the world."
    "And the events that transpire upon this couch are sure to show you just that. "

    tb "You wanted to speak with me, Touka?"
    to "Correct, Mother. I had some questions about Sensei that I believe only you will be able to answer."
    tb "Oh? There’s nothing I can tell you that he {i}can’t,{/i} dear."
    to "True. But approaching him about the matter is...difficult, considering our relationship. And I know you to be a woman of great influence {i}and{/i} great knowledge."
    tb "My dearest daughter, there’s no need for such generosity. Please speak with me as if we’re gossiping over mimosas at Le Coin Français."

    scene tsukiokasonthecouch2
    with dissolve

    to "Is that really okay?"
    tb "{i}Of course,{/i} dear. You are my first-born child who I’m sure will one day have a very similar conversation in a very similar position on this very couch. "
    tb "If you are to {i}become{/i} me, you must first stop holding me to such ridiculous standards. I really {i}am{/i} just another one of the girls at the end of the day."

    scene tsukiokasonthecouch3
    with dissolve

    to "I apologize for the unwanted formality, then. Yes — let us speak as two women deep in the throes of brunch at a cozy French cafe."
    tb "How {i}is{/i} your French, by the way? Have you been practicing?"
    to "Let us speak not of language until my questions have been answered or acknowledged, Mother."
    tb "You haven’t been, have you?"

    scene tsukiokasonthecouch4
    with dissolve

    to "I barely have time for anything anymore between my classes here and at school. Which doesn’t even touch upon how much time I’ve needed to spend on the apartment building {i}and{/i} Yasu lately."
    tb "A Tsukioka {i}always{/i} has the time, Touka. You’d be doing yourself a kindness to remember that."
    to "Perhaps you are correct..."

    scene tsukiokasonthecouch5
    with dissolve

    to "But still...that has naught to do with the matter at hand."
    tb "Then ask away, dear. But do so with {i}tact.{/i} I’d {i}hate{/i} to belittle someone I have so much respect for behind his back."
    to "Why {i}do{/i} you have so much respect for him, Mother? Without making him sound like a terrible person...Sensei is, by all accounts, a really {i}terrible{/i} person."
    tb "Ha! I suppose that, by conventional means, that’s true. But we are not a conventional family, Touka. We don’t share the same values as those outside of our walls."
    tb "Which is why, if you are here to expressly ask for permission to sleep with him-"

    scene tsukiokasonthecouch6
    with dissolve

    to "Mother, no!"

    scene tsukiokasonthecouch7
    with fade

    tb "{i}Still{/i} you refuse to believe that’s what you want? I’m so perplexed, dear. If {i}I{/i} were you, I’d be all over that man like Isaac Burns Murphy on Buchanan at the Kentucky Derby."
    to "That...is another matter entirely! It is not what I wish to discuss."

    scene tsukiokasonthecouch8
    with dissolve

    tb "Okaaaay! I’m just saying, dear...wait any longer and someone {i}else{/i} in the family might get to him first."

    play sound "static.mp3"
    scene tsukiokasonthecouch9 with flash
    stop sound

    to "You...wouldn’t."
    tb "How do you know I’m not speaking about your sister?"
    to "But Tsukasa is-"
    tb "To be wed to someone else. I know."
    to "That...is not what I was going to say. But yes, I suppose that much appears to be true as well. "
    to "Regardless, can we {i}not{/i} speak of the potentialities of my teacher’s sex life within Tsukioka Manor and, instead, speak of his existence in this city as a whole?"

    play sound "static.mp3"
    scene tsukiokasonthecouch10 with flash
    stop sound

    tb "And what is that supposed to mean, {i}daughter?{/i}"
    to "Recent events within New Hope Cathedral have just...led me to believe that Sensei may possibly bear the same sort of...{i}divine significance{/i} as Yasu."
    tb "Divine significance...what an interesting choice of words."
    to "Forgive me, but I’m unsure of how else to describe their shared connection to a seemingly forgotten sect of spiritual wisdom."
    tb "{i}Wisdom{/i} implies that there is some amount of truth to it, Touka. It’s all but more fanatical nonsense at the end of the day — the same way it is with {i}all{/i} religion, dear."
    to "Perhaps...but that doesn’t change the fact that there are many things about their respective existences that never cease to perplex me."
    to "And I {i}know{/i} that you’ve gone to the efforts of researching Sensei’s past, so if there’s something of significance that you may have uncovered..."
    to "Something that could help {i}me{/i} cultivate a better...understanding of who he is, I would greatly appreciate if you shared that knowledge with me."
    tb "Touka darling, if you {i}want{/i} to fuck him, just {i}tell{/i} him. All these extra steps you’re taking are making me dizzier than a 1922 Madeira would."

    play sound "static.mp3"
    scene tsukiokasonthecouch11 with flash
    stop sound

    to "This is {i}not{/i} about sex! Why do you keep making everything about {i}sex?!{/i} Can I not show interest in him {i}apart{/i} from carnal desire?! Is that truly so bad?! So wrong?!"
    tb "It’s not {i}wrong...{/i}It’s just boring. You have to admit, the man is attractive. {i}Experienced{/i} too."
    to "I don’t {i}care{/i} about that! I care about knowing why you’re, for lack of a better term, {i}obsessed{/i} with him! He’s a commoner! He’s {i}nothing!{/i} He’s-"
    tb "Important."

    scene tsukiokasonthecouch12
    with dissolve

    to "...how?"
    to "In what way?"
    tb "Would you believe me if I told you I’d known him since before you were born? Or that he is somehow the key to winning the space war? Or {i}maybe{/i} that he is your long lost older brother! Ooh, that’d be fun!"
    to "No! I would not believe any of that. And I ask, no — I {i}beg{/i} that you save jokes like this for a moment where I am {i}not{/i} caught between a rock and a hard place!"
    tb "If only the hard place was his thick, {i}throbbing{/i} member..."

    scene tsukiokasonthecouch13
    with dissolve

    to "What in the {i}world{/i} has gotten into you?! Why are you acting this way?! It’s like you’re barely my mother at all!"

    play sound "static.mp3"
    scene tsukiokasonthecouch14 with flash
    stop sound

    tb "Oh, {i}I’m{/i} the one who isn’t myself? Please."
    to "What is that supposed to-"

    scene tsukiokasonthecouch15
    with dissolve

    tb "Your charade is as flimsy as a wet paper bag, darling. Why not drop the act now and show me who you really are?"

    play sound "static.mp3"
    scene tsukiokasonthecouch16 with flash
    stop sound

    q "..."
    tb "Ooooh, interesting! I recognize those eyes."
    q "How did you know?..."

    play sound "static.mp3"
    scene tsukiokasonthecouch17 with flash
    stop sound

    tb "You think I wouldn’t recognize someone masquerading as my own daughter?"
    tb "There’s nothing more important to me in this entire {i}world{/i} than my girls, dear. Surely {i}your{/i} mother is the same, is she not?"
    q "That’s...um..."
    tb "Let’s cut to the chase — what do you want? What use do you have for Akira? "

    scene tsukiokasonthecouch18
    with dissolve

    q "{i}Hah...{/i}"

    scene tsukiokasonthecouch19
    with dissolve2

    q "What do you think about this place, Miss Tsukioka?"
    q "Are you happy here?"
    tb "Why, I haven’t heard {i}that{/i} question in quite some time. Shows you the type of people I commonly associate with, does it not?"
    q "Just answer the question, please. I’ve already broken the rules by revealing myself. I shouldn’t stay any longer than I need to."
    tb "How can I answer what can {i}not{/i} be answered at all? Just tell me what you need and I’ll see to it."
    q "Would you believe me if I told you I wanted to save the world?"
    tb "Which one?"

    scene tsukiokasonthecouch20
    with dissolve

    q "Oh, {i}you’re{/i} good. I guess coming here really {i}was{/i} the right idea after all."
    tb "You must be somewhat desperate if that’s the case, though. It’s been decades since the last time I encountered one of you."

    scene tsukiokasonthecouch21
    with dissolve

    q "I am. But please keep it a secret because I’m {i}really{/i} trying to shake things up. "
    tb "Ooh, I love secrets! Do tell."

    scene tsukiokasonthecouch22
    with dissolve

    q "{i}Ahem!{/i} I’ve been practicing this pitch for quite some time, so get ready to have your mind blown."
    tb "A business proposition then?"
    q "{i}Something{/i} like that."

    play sound "static.mp3"
    scene tsukiokasonthecouch23 with flash
    stop sound

    "Blah, blah, blah. Then some stuff happened. Busy now! Gotta go! Bye!"

    to "Do the two of you ever feel as if someone is talking about you behind your back?"

    play sound "static.mp3"
    scene tsukiokasonthecouch24 with flash
    stop sound

    ka "Every time I sneeze."
    ya "Talking about a creature as insignificant as me would be a waste of time and energy! That’s why {i}I{/i} only think about God!"
    ka "Why do you ask, Touka?"
    to "I just...can’t help but feel like I’m having some strange sort of...out of body experience right now. Like I’m in two places at once."
    ka "Is the other place a diner? I hope it’s a diner. I’m really hungry. I want to be there too."

    play sound "static.mp3"
    scene tsukiokasonthecouch25 with flash
    stop sound

    to "It’s certainly not a diner, but...I’m not quite sure {i}where{/i} it is. Or what."
    to "It’s nowhere specific, surely. It’s more of just a...state of being or...{i}not{/i} being, maybe. Like I’m caught between two separate planes of existence at once."
    ka "Uh-oh! I think Yasuyasu might be rubbing off on you! Tickle tickle tickle!"
    ya "Aah! Stop it, Karin! It feels like there are ladybugs beneath my skin!"

    scene tsukiokasonthecouch26
    with dissolve

    to "Whatever the case, I’m sure it will go away shortly. Perhaps it’s just {i}my{/i} turn to start experiencing intermittent possession and this is {i}my{/i} body’s way of warming me up to it."

    scene tsukiokasonthecouch27
    with fade

    ya "One of us! One of us!"
    ka "Possession? What do you mean it’s {i}your{/i} turn to start being possessed? Isn’t that a horror movie thing?"
    to "Yes, but- oh! Perhaps I should be Linda Blair for next year’s Halloween party? Regardless, it both is and {i}isn’t{/i} a “movie thing.”"
    to "And I imagine you’ll bear witness to it soon enough if you continue to spend time with Yasu and me as she experiences bouts of something possession-adjacent quite frequently."

    scene tsukiokasonthecouch28
    with dissolve

    ka "{i}This{/i} little bug?! Getting all scary like that?! Doubt it! She could never even hurt a fly! Could you, Yasu?"
    ya "I could not! For I am but one of them and bringing harm upon myself or my kind would be worth nineteen days in a tub of acid."
    ka "Just say no next time, kay?"
    ya "It’s not just me either! It’s Sensei too! We have a “gift!”"

    scene tsukiokasonthecouch29
    with dissolve

    ka "{i}Sensei?{/i}"
    ya "He’s {i}extra{/i} special! He can {i}see{/i} things! I merely become them and carry words from up above to those undeserving who live closer to the ground than the sky!"
    ka "So he...what?"
    to "You’ve never witnessed something seemingly take him over before?"

    scene tsukiokasonthecouch30
    with dissolve

    ka "...What?"

    play sound "static.mp3"
    scene tsukiokasonthecouch31 with flash
    stop sound

    to "Probably just one more case of you not experiencing what essentially everyone else in our class has due to less exposure to him."
    to "It’s practically common knowledge to all of us at this point that he has bouts of...{i}decreased{/i} identity. Though, the reasons for this remain as elusive to me as ever."
    to "Perhaps I should refer him to Yasu’s doctor as well? Their cases are slightly different, but I’m sure that-"
    ka "You...You’ve {i}seen{/i} this before, Touka? This...possession thing? What’s it like? Can you tell me? I...I’m just curious! It’s not like...{i}I’ve{/i} actually seen it, but...you know, if I {i}had,{/i} I’d obviously want to {i}know!{/i}"

    scene tsukiokasonthecouch32
    with dissolve

    to "You’d be better off asking Ayane than me. He seldom acts that way in my presence. {i}Probably{/i} because he thinks I’m his mother and is comforted by my existence. I hate it."
    ka "Ayane...yeah."
    ka "She...knows stuff about him. I’ll...ask {i}her.{/i}"
    to "You {i}have{/i} witnessed it, haven’t you?"

    play sound "static.mp3"
    scene tsukiokasonthecouch33 with flash
    stop sound

    ka "No!"
    to "..."

    scene tsukiokasonthecouch34
    with dissolve

    ka "...maybe."
    to "Well, on the off chance you {i}haven’t,{/i} you will soon enough. And I do ask that you don’t hold it against him as I imagine there’s no one who hates it more than {i}he{/i} does."
    ka "You...think he’s a good person then?"
    to "Now...I don’t know if I’d go {i}that{/i} far. But I don’t think he means any harm."
    ka "Yeah..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    ka "Maybe...he doesn’t..."

    "Back! Sorry. What did I- oh, darn. Over already? "
    "Guess I’ll just get out of here, then! Later! "
    "Hope you enjoyed being one of the girls!"

    $ renpy.end_replay()
    $ toukaspring5 = True
    $ yasu_love += 1
    $ touka_love += 1
    $ karin_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "{i}Uh-oh.{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
