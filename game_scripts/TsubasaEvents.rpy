label calltsubasamorning:
    if tsubasa_love >= 0 and toukaspecial15p3 == True and tsubasadate1 == False:
        jump tsubasadate1
    else:
        play sound "phonebeep.wav"

        "I tap on Tsubasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callmorning

label calltsubasaafternoon:
    if tsubasa_love >= 20 and tsubasadate20 == True and chikadorm45 == True and otohadate20 == True and norikoinvite3 == True and tsubasaspecial20 == False:
        jump tsubasaspecial20
    if tsubasa_love >= 20 and chinamispring6 == True and yumispring8 == True and tsubasaspring4 == False:
        jump tsubasaspring4
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Tsubasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callafternoon
    if chapthreeactive == True:
        jump tsubasasummer2noongen
    else:
        play sound "phonebeep.wav"

        "I tap on Tsubasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callafternoon

label calltsubasanight:
    if chap4active == True:
        jump tsubasaspringnightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Tsubasa's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callnight

label tsubasadate1:
    play sound "phonebeep.wav"

    "I tap on Tsubasa’s name in my phone and wait for her to answer."
    "Is it weird for me to be casually phoning the wealthiest woman in all of Kumon-mi first thing in the morning? Yes."
    "But after many phone calls with Ayane, who I believe is in second place after the entirety of the Tsukioka family’s women, I think I’m prepared."
    "Especially after hearing how Tsubasa’s been itching to start sneaking away from her normal life again."
    "Well, {i}itching{/i} probably isn’t the most accurate description of her feelings- but it makes me feel a little more like she’s doing this to see me and not just to feel...un-rich for a short burst of time."
    "Oh well. I guess we’ll just have to see how things play out. "
    "Here’s hoping that I can provide her a bit more entertainment than her husband can."
    "Interpret that however you want."

    play sound "phonebeep.wav"

    tb "Well, hello. I can’t say I was expecting you to call so soon after exchanging numbers."
    s "Just deciding to switch things up a bit. Are you doing anything today?"
    tb "I’m afraid I am. Well, at least in some sense. "
    tb "I’m mostly free so long as I remain at home. But I must remain nearby in the event that I’m needed for anything involving the acquisition of another hotel for the brand."
    s "Expanding your empire this early in the morning?"
    tb "Yes, well, Tsukasa was so smitten with the red-ish light district the other day that she insisted we move into that part of the city as quickly as possible."
    s "I guess I should call back some other time, then?"
    tb "I suppose. Unless you’d be willing to make the trip here, of course."
    s "I don’t think I own any clothes nice enough to really look the part."
    tb "Oh, I wouldn’t worry about that at all. It wouldn’t be the first time we’ve opened up parts of the manor for a tour. "
    tb "And seeing as I’m here, I could serve as your personal guide. It would be my thanks for your recent assistance in what is soon to be the next section of a corporate takeover."

    "Is it really okay for me to go to Touka’s house without receiving her blessing?"
    "Probably not. But I’m going to do it anyway because I want to make her life harder and Tsubasa and I are technically friends or something now."

    s "Send me the address and I’ll head over, I guess."
    tb "Splendid! I’ll have someone pick you up at the gate once you arrive."
    tb "See you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "So, I guess I’m going to have to meet up with some random person first if I’m going to make my way into the Tsukioka manor."
    "With my extremely limited knowledge of rich people, however, I assume that’s just par for the course."
    "All I can really do at this point is hope that A) Touka doesn’t find out. And B) That Touka’s {i}father{/i} doesn’t find out."
    "From what I understand, their relationship isn’t really as strong as it once was, but I would imagine it’s at least strong enough to not want his wife inviting other men over just yet."
    "Yet again, though, I’m wrong just as often as I’m right."
    "He could very well be into that sort of thing."
    "Or I could very well be walking into a death trap."
    "There’s only one way to find out."

    play sound "phonebeep.wav"

    "I receive a text from Tsubasa with her address and, after doing a quick search online to figure out exactly where she lives, I begin to make my way over."
    "........."
    "......"
    "..."

    scene tsubasatour1
    with dissolve2
    play music "tsukiokamanor.mp3" fadein 3.0

    "Upon arriving at the Tsukioka residence, I’m escorted through several different gardens, ultimately leading to one much {i}bigger{/i} garden where Tsubasa is hanging out."
    "She diverts her attention away from the crystal clear waters of a manmade pond I will never be able to afford and sets her sights on me- a man so clearly out of place that it must be comical to her."
    "It was certainly comical for me the other day, so I see no reason to disbelieve things wouldn’t be the same when flipped on their head."

    tb "Welcome. I take it you found the manor okay?"
    s "Why do you have so many gardens?"

    scene tsubasatour2
    with dissolve

    tb "In case one breaks down, of course."
    s "..."

    scene tsubasatour3
    with dissolve

    tb "I’m sorry- was that not funny? My husband always laughs at that joke."
    s "Always? Meaning you have told it more than once?"
    tb "When you’re married and spend nine tenths of your life in one place, you tend to run out of material."
    s "Well, either your husband has a horrible sense of humor or he’s just trying to make you feel funny."

    scene tsubasatour4
    with dissolve

    tb "It’s likely the former, to be quite honest."
    s "On a related note, does he know I’m here?"

    scene tsubasatour5
    with dissolve

    tb "Why do you ask?"
    s "I’d just feel a little weird personally if my wife invited some guy to my house without telling me."
    tb "You’re married? I had no idea."
    s "What? No. That was rhetorical."
    tb "You’re not married?"
    s "Do I really look like the married type to you?"

    scene tsubasatour2
    with dissolve

    tb "No. Which I suppose would make my darling Chika very happy for the time being."
    s "Was that supposed to be a joke as well? Because, if so, you’re zero-for-two so far."
    tb "Less of a joke and more of a...wistful observation."
    tb "And, to answer your question from earlier, my husband does not know you’re here."
    tb "He’s very busy and, with a house this large, I doubt we’d be able to find him even if we tried."
    s "What a wonderful problem to have."
    tb "Apologies again for not being able to step away, but I’m sure you’ll come to find that there’s plenty to do on these grounds. And I’m not just talking about gardening, of course."

    scene tsubasatour1
    with dissolve

    tb "What I would suggest, seeing as this is your first time here and all, is a brief tour of the premises. We should be able to cover at least half of it today if we begin now."
    s "I was kind of figuring this would be more of a “You and I just hang out and talk” type of thing."
    tb "Can we not do both?"
    tb "I see this is as an...introduction to my world. And if my world isn’t interesting to you, who’s to say the two of us would find any joy in talking at all?"
    tb "To understand each other, we must first know where the other comes from. And it would bring me a great deal of joy knowing you’d at least humor me in indulging this thought of mine."
    s "So instead of sneaking away today, you’re deciding to turn around and run head first into the thing you’re interested in getting away from?"
    tb "“Sneaking” is only exciting if it’s on occasion, Sensei. If I were to entirely abandon this life, it would be more akin to simply {i}running{/i} away."
    s "Well, it doesn’t seem like I really have any say in this to begin with, so I’ll accept your tour of wealth and try my best to look impressed as you show me all of the nice things you have."

    scene tsubasatour6
    with dissolve

    tb "Fantastic."
    tb "Oh, and if we bump into Touka, just pretend you do not see her. She’d be very embarrassed knowing you’d come to visit her home without her knowledge. "
    s "She’s here?"
    tb "Perhaps. She {i}does{/i} live here, after all. "
    tb "She may be getting more accommodated to life in her dorm room, but that can’t compare at all to what we’ve built over the years."

    scene tsubasatour1
    with dissolve

    tb "But I’m sure you’ll understand by the end of the tour."
    tb "Now, shall we go?"

    scene black
    with dissolve2

    "Tsubasa peels herself away from a bridge I’m sure she spends hours a week looking out over in a mix of admiration and longing."
    "She takes a place beside me, one that I imagine was filled much more frequently by the man she fell in love with at a younger age, only to have it go vacant in years subsequent. "
    "I can not tell if she’s comfortable or not, but it wouldn’t change my position either way if she isn’t."
    "I exist to fill the holes others can not fill on their own- whether they want them there or not."
    "Whether they want me there or not."
    "Whether I want to be there or not."

    scene tsubasatour7
    with dissolve2

    tb "Tell me, do you notice anything different about {i}this{/i} garden compared to the several others you’d passed on your way to me?"
    s "Not really, no."
    tb "{i}Well,{/i} the key difference between this and the others is that {i}this{/i} particular rock garden has been around since the Edo period. "
    tb "The Tsukioka family is one dating back to the origins of Kumon-mi, and this garden has been {i}mostly{/i} untouched for all of its history. "
    tb "And despite not being born into this family, I’ve taken quite a liking to it. There’s something very special about history, whether it be familial or personal."
    tb "And I remember the first time I ever saw this garden as if it’s the back of my hand."
    s "You wear gloves like 90%% of the time, Tsubasa."

    scene tsubasatour8
    with dissolve

    tb "Well...yes. But that doesn’t mean I don’t remember what my own hands look like, Sensei."

    scene tsubasatour9
    with dissolve

    tb "The first time I ever saw this garden was on a trip to meet my husband for the first time."
    tb "Arranged marriages are still very common in our world, you see. And before I was even introduced to Tomonori, I fell in love."
    tb "Even being from an almost equally affluent family, I’d never seen something like this in one’s own residence before."
    tb "And I suppose it may make me sound a bit materialistic, but I had no intention of abandoning a place like this from the moment I laid eyes on it."
    s "So what you’re telling me is you married your husband for an old rock garden?"
    tb "What I’m telling you is that I married into a family I wanted to be a part of. That I wanted to continue carving out a name for. And I likely would have done that even if my husband wasn’t a good man."

    scene tsubasatour10
    with dissolve

    tb "But I got lucky. He {i}was{/i} a good man. And we made two beautiful daughters together. Daughters who will, one day, walk through this rock garden with their prospective husbands."
    tb "Who will ultimately bring more people into our world. More people to fall in love with the history."
    tb "What makes this particular garden so different is that it’s a physical reminder of all of that, Sensei. "
    tb "It’s something I can look out on while pondering what the other women who married into the family felt about it."
    tb "Generations of people, all witnessing the same thing at different points in time..."
    tb "If that doesn’t sound magical to you, I don’t know what will."
    s "..."

    scene tsubasatour11
    with dissolve

    tb "Just kidding. I know {i}exactly{/i} what will."
    tb "Now, if you’ll follow me-"

    scene black
    with dissolve2

    "Tsubasa leads me through the rest of the garden and over to a large building resembling a shrine."
    "She removes an old, rusted key from somewhere inside of her sleeve, sliding it into the door and slowly pushing it open."
    "The doors creak as if they haven’t been opened in centuries, but upon stepping inside and seeing how clean and well-kept everything is, I know that can’t be true."
    "And she was right."
    "This does seem magical."

    scene tsubasatour12
    with dissolve2

    "Magic isn’t real, though. "
    "And I know that, behind whatever history {i}this{/i} room holds, it’s just another room at the end of the day."
    "It doesn’t matter who died here or who {i}will{/i} die here- it’s an empty box filled with pretty things that exist for no real purpose."
    "Much like most of the world, but with a fresher coat of paint on it."
    "It’s only magic for a moment."

    tb "Would you care to take a guess at what this room is?"
    s "I can’t imagine anything I say would come even remotely close."
    tb "This is the Tsukioka family ceremony room. It’s where I married my husband and where my daughters will marry theirs."
    tb "Assuming anyone will ever take Tsukasa, that is."

    scene tsubasatour13
    with fade

    s "You {i}all{/i} get married in here?"
    tb "As per tradition, yes. It’s the sole purpose of this room. "
    s "I’m having a very hard time picturing Touka getting married."
    tb "I imagine that’s because you’ve only seen her as a student."
    tb "Touka’s been just as invested in the history of our family as me ever since she was a little girl."
    tb "She’s likely too embarrassed to say anything about it to you, but she’s been dreaming of the day she gets to stand here beside her lover for years."
    s "Yeah, still not really able to picture it."

    scene tsubasatour14
    with dissolve

    tb "Has she told you that we were planning on arranging her marriage as well?"
    tb "We had several suitors picked out, but I could always tell she was never really comfortable with the idea."
    tb "They all wound up in space anyway, though, so it’s not like the plan would have come to fruition even if we hadn’t decided to...rethink things."
    s "Well, I’m sure she was really happy with that decision. I can’t imagine her doing {i}anything{/i} that’s commanded of her, let alone marrying someone."
    tb "I think you’d be very surprised at what Touka would be willing to do for her family. "
    tb "Or anyone, for that matter."
    tb "I often think that the reason my youngest daughter is so devilish is because my oldest wound up being such an angel."
    tb "But, I suppose that basically sums up what {i}this{/i} particular room is used for."
    tb "Come. I’ll show you around some of the others. "
    tb "You’ll soon find that all things serve some sort of purpose."

    scene black
    with dissolve2

    "Tsubasa continues our tour of the Tsukioka manor for what feels like an eternity."
    "Every corner we round is doused in history and, I don’t know if it’s just due to spending so much time around them or if it really {i}is{/i} an innate interest in all things Tsukioka-"
    "But she knows every single story. And she tells them as if she were there for the origins."
    "I wonder what it’s like having so much pride in something."
    "The only pride I have is that of the sinful sort. There’s nothing that I can look at or hold and think, “This is a part of me.”"
    "But even if that was something I {i}could{/i} do, I imagine I’d be more focused on just figuring out where that part belongs so I can start putting myself back together."
    "Maybe one day when time is no longer limitless."
    "Maybe one day when I actually want to."

    scene tsubasatour15
    with dissolve2

    tb "We’ll cap off today’s portion of the tour with our indoor arboretum- another family relic that’s been an important part of our history for centuries."
    tb "A long time ago, before industrialization took up its scythe and laid waste to our lands, Kumon-mi was covered in trees and filled with wildlife."
    tb "You’d never be able to tell with how things look today, but that doesn’t mean all traces of the past are gone."
    tb "This “arboretum” holds but one tree- an everblooming sakura, kept alive by extremely specific climate controlling, imported soil, and a fair bit of willpower."
    s "I didn’t realize trees had “willpower.”"
    tb "Why wouldn’t they? They’re alive, after all. Just like you and I."
    tb "In fact, I’d wager they’re even {i}more{/i} alive than us. "
    tb "Just think of how much this tree has seen. All of those stories I recounted for you today would be actual {i}memories{/i} for something that’s been alive as long as our sakura."

    scene tsubasatour16
    with dissolve

    s "I don’t want to be the bearer of bad news, but I’m pretty sure trees can’t retain memories."
    tb "Of course I know that. But if they {i}could{/i}, imagine just how many of them there would be."
    tb "I suppose the importance of this particular transplanted piece of nature isn’t in what it {i}could{/i} hold, however, and rather what it stands for. "
    s "Which is?"
    tb "Perseverance. "
    tb "To be the only remaining trace of what was once an important part of the world...I believe there is something special about that."
    tb "Every other aspect of this tree’s world has been, and forgive the pun, cut down. "
    tb "All that remains is the ground itself, and even that ground would not suffice in keeping it alive anymore."
    tb "In here, though..."
    tb "In this world created for the sole purpose of sustaining it..."
    tb "It can live."
    tb "And I think that’s beautiful."
    s "..."
    tb "Has my explanation floored you to the point of speechlessness? "
    s "Not particularly. "
    s "I just think it’s interesting how you can speak so highly of things other people would see as boring or unimportant at surface level."
    tb "As I said earlier, this is my world. It’s one that I chose and one that I {i}would{/i} choose if the chance to do so repeated itself."
    tb "Of course I’ll be able to find the right berries to pick when I know where all of them grow."
    s "If that’s a figure of speech, I’m not really following."
    tb "I’m saying that I know why everything here is so special because I have had the time to learn. "
    tb "I’m sure it’s not far off from how your family feels about...arcade machines or...what were those silly things we ate called again? Toucans? "
    s "Tacos...and those aren’t really a thing that carry some sort of emotional weight for people who don’t grow up with arboretums or marriage-rooms. "
    tb "Well, whatever it is you find special, then. "
    tb "I believe that there is beauty in all things. And even if {i}you{/i} do not, that’s something I wanted to show you."
    tb "As a friend who wants to be a part of your world and who wants to share hers with you."

    scene tsubasatour17
    with dissolve

    tb "I suppose there is one more place we can stop before our day comes to a close, though. Something I’m sure {i}all{/i} people can appreciate and not just those with an affinity for history. "
    s "Am I finally getting to see the animatronic band I’ve heard so much about?"
    tb "Heavens, no. That’s at one of our vacation homes."
    tb "You’ll see what I’m referring to in no time at all."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ tsubasadate1 = True
    $ tsubasa_love += 1

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump tsubasadate1p2

label tsubasadate1p2:
    if _in_replay:
        play music "tsukiokamanor.mp3"

    "Tsubasa leads me away from the everblooming sakura into a hall full of old Japanese paintings I should probably know the names of but don’t."
    "I wouldn’t doubt if some of them are originals that I’m meant to be impressed by, but I refuse to be impressed by anything that’s so easily duplicated."
    "My untrained eye wanders from canvas to canvas, hoping to pick up even a fragment of what makes this dimension so palatable for someone like Tsubasa, but I get caught up on her instead."
    "Beauty is supposed to be in the eye of the beholder anyway. And despite how frequently these eyes deceive me, I know what it is that I would prefer to waste away my days observing."
    "There are no paintings that can bring me joy."
    "Maybe once upon a time there were-"
    "But there aren’t any left now."
    "And if there are, I imagine they’re locked behind more doors in this palace than I’ll ever be able to open."
    "Tsubasa says some things as she leads me down the hall, but none of them attach to whatever part of my brain is meant to process them."
    "It isn’t until she leads me into a wide open, half-misty room that I remember what we’re doing or how to listen."

    scene tsubasapool1
    with dissolve2

    tb "This is one of Touka’s favorite additions to the manor and one that most people we bring here tend to enjoy very much."
    tb "It’s nothing extravagant or historical like a special tree or a ceremonial room, but it houses a borderline-olympic sized heated pool."
    tb "I used to spend a lot of time here when I was younger. I’m afraid I can seldom make the room in my schedule at this point, though."

    scene tsubasapool2
    with dissolve

    s "If there's anything I've learned today, it's that you’re a lot busier than I ever really imagined you were."
    tb "Did you assume I was just some woman living off of her husband’s money without making an effort to actually accomplish anything?"
    s "I don’t know if my thoughts were {i}that{/i} specific."
    tb "It’s that sort of perception that comes with the territory when you marry into the most influential family in a city."
    tb "I can guarantee you I’ve heard it all before."

    scene tsubasapool3
    with dissolve

    tb "Of course, though, that’s not even remotely true."
    tb "I suppose it’s just in my nature to always be doing {i}something{/i}. I have a hard time pulling myself away from anything that could be called “productive” in some form."
    tb "Which is why you’ll see me...offering to give tours. Or offering to babysit. Or offering to check in on remote onsens for the sake of the family business."
    tb "I suppose that last one was a tad relaxing, though. "
    tb "Even with all of the noise."

    scene tsubasapool4
    with dissolve

    s "I have no idea what you’re talking about. Chika and I were just watching TV."
    tb "You’ll have to tell me what program. I can’t remember the last time I enjoyed {i}watching TV{/i} that much."

    play sound "water1.mp3"

    to "Wha-"
    to "Sensei?"

    scene tsubasapool5
    with fade

    to "What are you doing here?..."
    s "Being shocked at how you’re still in [high_school]."
    to "Yes, but {i}what are you doing here?{/i}"
    tb "I invited him over to give him a tour of the manor, dear. I figured it was the least I could do to offer him thanks for his time at the arcade and...surrounding areas the other day."
    to "I see..."
    s "Have you been in there this whole time?"

    scene tsubasapool6
    with dissolve

    to "I’ve been in here for at least an hour. If I’d known you were coming, I would have put on something more presentable."
    s "No worries. What you’re wearing is totally fine. "

    scene tsubasapool7
    with dissolve

    to "Are you enjoying the tour, at least? I’m assuming Mother already told you about the rock garden? She always likes to open up with that."
    tb "I also showed him the golden room and told him all about how you’ve been dreaming of getting married there one day."

    scene tsubasapool8
    with dissolve

    to "Wha- Mother?! "
    to "Sensei has no interest in that! And those were just silly, girlish dreams!"
    tb "Oh? So you {i}don’t{/i} want to be married in the golden room anymore?"
    to "I...well..."
    tb "Touka darling, come out of the pool if you’re going to hold a conversation with us. It’s bad manners staying in there."

    scene tsubasapool9
    with dissolve

    to "Hah...yes, Mother..."

    scene black
    with dissolve2

    "Touka exits the pool and wrings her hair back out into the water."

    if bonus == True:
        "If her mother wasn’t standing beside me, I’d use this opportunity to make some perverted comment about the angle of her body as she does this."
        "But, at the risk of forming an erection in the process of mentally describing that, I will elect to abstain."
    else:
        "The environment thanks her."

    scene tsubasapool10
    with dissolve

    tb "Oh my. Are you {i}still{/i} growing, dear? You may even surpass me at this rate."

    if bonus == True:
        "Nevermind. Some things just can’t be contained."

    to "Mother, stop! Weren’t you {i}just{/i} speaking of bad manners?!"

    scene tsubasapool11
    with dissolve

    tb "Oh, yes. Silly me. I was so impressed with your...progress, that I’d forgotten your teacher was even here."
    s "I completely understand. I forgot as well for a second."
    to "If you two are done objectifying me for now, I would like to go get dressed into something more suitable for the remainder of Sensei’s tour."

    scene tsubasapool12
    with dissolve

    tb "Oh, his tour is just about over for the day. I’ve been dragging him around all morning. Though, I suppose he {i}was{/i} willingly following me, so perhaps he enjoyed it?"
    s "I just didn’t want to get lost in the entire mini-city you’ve built for yourselves."
    to "Have you really been here for that long? Why wasn’t I informed of this?"
    s "I honestly didn’t even think you’d be okay with me coming."
    to "I’m...mostly indifferent to you coming. But if you’re {i}here{/i}, I believe I should be involved in some way."

    scene tsubasapool13
    with dissolve

    tb "I apologize for not telling you, dear. I’d just assumed you wanted the rest."
    to "{i}My{/i} rest aside, I thought you had meetings today? "
    tb "I was on call for meetings regarding some of the properties we saw the other day- but it appears that none of them ever happened."
    tb "Or at least no one’s been able to find me to inform me about them. You know our manor staff, though, so that doesn’t seem very probable."
    to "Well...regardless, I’m going to go get changed."

    scene tsubasapool12
    with dissolve

    to "Please inform me if you’re ever going to come here again. It’s one thing to appear casual at the dorms, but as the heiress of the Tsukioka Foundation, I can’t afford to be seen like this here. "
    to "I have a reputation within the manor to uphold. "
    tb "I won’t tell anyone if you don’t, dear. Now, go get dressed. We’ll stay here until you return."
    to "Okay..."
    to "Don’t go anywhere."

    scene tsubasapool14
    with dissolve

    "Touka grabs a towel off of a nearby rack and dries herself off before disappearing into the hall of a thousand paintings."
    "That’s not an accurate number- just an estimation."

    tb "My lord. It feels like just the other day I was purchasing her luxury training bras. "
    s "That’s an item that probably shouldn’t exist."

    scene tsubasapool15
    with dissolve

    tb "But it does, and so she had them. Not for very long, though, as you can probably assume."
    s "So I guess we’re talking about your daughter’s breasts now. Not really how I imagined this tour ending after 90%% of it was a history lesson."

    scene tsubasapool16
    with dissolve

    tb "Just some passing commentary. That wasn't a topic I intended to remain on any longer- at least not without her present for it."
    s "I feel like having her present for it would make things even weirder. "
    tb "Perhaps it would."
    tb "Though, I wouldn’t say the same about what I feel we must discuss next."
    s "Which is?"

    scene tsubasapool15
    with dissolve

    tb "Would you find it rude if I took my shoes off? I don’t want to get in the pool, but I’d like to dip my feet in for a moment while we await my daughter’s return."
    s "Do whatever you want, it’s your house."
    tb "Excellent. Then, don’t mind me."

    scene black
    with dissolve2

    "Tsubasa sits down on a fancy looking beach chair and unstraps whatever the elegant looking sandal things she’s wearing are called."
    "She catches me looking at her for a moment and kindly waves me off so she can remove her stockings as well and, reluctantly, I oblige."
    "Once she’s done, she returns to me and sits down in front of the pool, hiking her dress up and dipping her toes into the water."
    "I sit beside her, mostly certain and even more uncomfortable about what I believe she wants to discuss next."

    scene tsubasapool17
    with dissolve2

    tb "..."
    s "..."
    tb "Do you know what it is I want to talk about, Sensei?"
    s "Probably, but I’d prefer to not guess and just have you get it over with so I don’t have to risk guessing incorrectly."
    tb "Then I suppose I’ll “get it over with” and save us the difficulty of prodding at one another until it’s out in the open."
    tb "A young lady who I’ve grown rather fond of lately seems to believe that the two of you are involved in an exclusive relationship with one another."

    if bonus == True:
        tb "But that young lady is just that. {i}Young.{/i}"
        tb "And while I’m no stranger to the prospect of marrying someone older given that women have been traded between affluent families like cattle for centuries-"
        tb "I can’t help but get a little caught up when it comes to wrapping my mind around your situation."

        "You know, when I first told Tsubasa that I’d be okay with spending more time with her, I worried that something like this might come up."
        "She’s one of the only people Chika trusts enough to talk about our “relationship” with, which is kind of odd considering Tsubasa was, at one point, just some random woman at an onsen."
        "But she’s much more than that now. To Chika, at least."
        "And to Tsubasa, Chika is important as well."
        "So it only makes sense that she’d ask me about this now that she finally has an opportunity to."
        "The only issue is that I don’t know what the right thing or the wrong thing to say is."
        "Tsubasa seems like a rational and understanding person but, at the same time, she’s someone I’ve only known for a little while."
        "And I’m less important to her than a surrogate daughter."
        "In fact, I doubt I bear any sort of importance in Tsubasa’s life at all."
        "So, I should probably tread carefully here."
    else:
        "Oh no. She knows about the hugs."

    s "What are you asking me?"

    scene tsubasapool18
    with dissolve

    tb "Oh? Is that a trace of attitude I’m hearing?"
    s "Not intentionally. I’m just not sure how to answer a question that hasn’t been asked yet."
    tb "And I’m not quite sure what I want to hear. "
    tb "On one hand, I want the young lady I care about to be happy. But when you really think about what it is that’s {i}making{/i} her happy, the waters get a little muddy."
    s "I don’t-"

    if bonus == True:
        tb "You are a grown man sleeping with a girl in [high_school]. Sleeping with your {i}student.{/i}"
    else:
        tb "I know about the hugs."
        s "Oh no."

    tb "Aren’t you even a little worried about what could happen to you if that information were to get out?"
    s "..."
    tb "..."
    s "Are you grilling me as a friend or a parent right now?"
    tb "Can it not be both?"
    s "Not when my answer would change based on yours."
    tb "Then I suppose we can say I’m asking you as a friend."
    s "I see."

    scene tsubasapool19
    with dissolve

    s "Of course I’m worried about what would happen if that information were to get out."
    s "And yet, I don’t really do anything to try and stop it apart from just...asking her to keep quieter."
    tb "Do you love her?"
    s "..."
    tb "..."
    s "Not the way I’m supposed to."
    tb "And how is it you are {i}supposed{/i} to love someone?"
    s "The same way she loves me, I guess."
    tb "Hm."

    scene tsubasapool18
    with dissolve

    s "You know, you can be pretty intimidating when you want to be."
    tb "Women in power are good at that sort of thing."
    tb "But if you want the truth, I’m not really appalled by what you do."
    tb "Like I said, that sort of thing doesn’t mean much to me when I’ve gone my whole life hearing stories of other women from {i}my{/i} family being shipped off to men twice their age."
    tb "It loses its impact after a while."
    tb "What I’m worried about is whether or not you’re going to hurt that young girl- whether it be intentional or unintentional. Because I don’t know if she’d be able to handle it."
    s "..."
    tb "..."
    tb "Just going to stay silent forever?"
    s "Sometimes, silence is the best answer."
    tb "And you think this is one of those times?"

    scene tsubasapool20
    with dissolve

    s "I’m not sure what this is."
    s "But if I had to guess, I’d wager that I {i}am{/i} going to hurt her."
    s "Life isn’t even half as convenient as it would need to be in order for me to avoid that."
    s "But I don’t intend to leave her side either. "
    s "I don’t really think I could."
    s "Even if she winds up hating me for something I’ve done or...{i}will{/i} do in the future, I’ll be there for her."
    s "So at least she won’t have to hurt alone."
    s "Granted, I’m not sure how much help my presence will be- especially when I’m worse at cheering people up or even just talking than anyone else I’ve ever met."
    s "But I’ll be there."
    s "She doesn’t have to be alone anymore."
    tb "..."
    s "..."

    "I think about how the water would feel against my skin."
    "I shrug it off."
    "That’s all I ever do."

    tb "That was a good answer."
    tb "We can’t prevent ourselves from hurting the people we care about. All we can do is pray it doesn’t happen and be prepared to suture the wounds if it does."
    tb "As long as you’re not just using the girl, I can accept the nature of your relationship."
    s "At first, that’s exactly what it was."
    tb "But it’s not anymore, is it?"
    s "..."
    tb "..."
    tb "Ah."
    tb "Silence."
    s "It’s the best answer sometimes."

    scene tsubasapool21
    with dissolve

    tb "I certainly picked an interesting class to enroll my daughter in, didn’t I?"
    s "Probably the worst one possible. And I’ve always been a little curious about why."
    s "You’ve known about Chika and me since the beginning. I figured that would be all you need to know to keep Touka away."

    scene tsubasapool22
    with dissolve

    tb "Tell me...How deep do you think this pool is, Sensei?"
    s "What?"
    tb "When Touka was a little girl, she really wanted to learn how to swim."
    tb "We hired an entire team of renowned instructors to teach her. People from all over the globe, since they were still allowed in back then. "
    tb "We spent {i}so much{/i} money trying to help that little girl swim."
    tb "But none of it worked."
    tb "No matter who we hired or what their methods were, she just couldn’t learn."
    tb "But one day, while the two of us were lounging near the poolside, I recalled a story one of my girlfriends told me about how {i}she{/i} learned to swim when she was younger."
    tb "Her mother pushed her into the pool."
    tb "Terrified and wanting nothing more than to stay alive, her instincts kicked in and she managed to swim back to the ledge and pull herself out."
    s "You...pushed your daughter into the pool knowing full well she didn’t know how to swim?"

    scene tsubasapool23
    with dissolve

    tb "And now you’re her teacher."
    tb "Sometimes, forcing people to do things they’re not comfortable with is the best way to move them forward."
    tb "I’ve known from the beginning that you were the exact opposite of what Touka needs."
    tb "And I think that’s exactly what makes her need you the most."
    s "..."
    tb "..."

    if bonus == True:
        s "Okay. But you have literally heard me have sex with a girl the same age as your daughter."
        tb "Lots of it."
    else:
        s "Okay. But you know about the hugs. I am evil."
        tb "(Airplane noises)"
        s "Well said."

    s "..."
    tb "..."
    tb "Are we ending the conversation here?"
    s "Yeah, I think we probably should."

    scene black
    with dissolve2

    "Tsubasa and I sit in silence until Touka returns wearing the same white dress she had on when I first met her."
    "Everything goes back to normal. "
    "And I, once again, manage to slip through the cracks of morality as I find that my newest acquaintance might also be a little broken as well."
    "Just in a much more beautiful way than I am."

    $ renpy.end_replay()
    $ tsubasa_love += 1
    $ tsubasadate1p2 = True
    stop music fadeout 5.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"

    jump saturdaynight

label tsubasaspecial15:
    if _in_replay:
        play music "comfort.mp3"

    scene tsubasalimo1
    with dissolve2

    "That was a metaphor, in case you still haven’t picked up on my affinity for those yet."
    "Today, it isn’t raining at all. "
    "To splash is to exist. And the puddles are air-pockets I don’t belong in as my true home is the ocean."
    "This amphibious shell makes breathing on land possible, but I know where it is I really belong."
    "Somewhere far away from here — filled with people I can relate to about things I care about. "
    "But instead, my air-pocket today is the backseat of a car I’ve found myself in before. "
    "The two girls joining me here, while they may look similar to the last one, are not the same."
    "And I cannot relate to either of them at all, for they were not born with skin as permeable as mine."
    "They can not survive in the water, and puddles like this are seen as nothing more than things to play in."
    "So as this external lung unsuccessfully siphons the bad out of the good and takes it all in as one singular dose of half-tainted oxygen, I wish I was born with fur."
    "That way, I wouldn’t have to deal with any of this."
    "And I could touch anything I wanted without fear of contamination."

    tk "You look kind of weird, Jeeves. Weirder than normal, I mean- since you look pretty weird in general."
    tb "Tsukasa is right. You seem a tad bit “out of your element” right now. Could it be that Chika’s nostalgic tales have cast a shadow on you the same way they did me?"
    s "Yeah, that has to be it. There’s no way being in the back of a car with two girls from the wealthiest family in all of Kumon-mi would take me “out of my element.” This is clearly where I belong."
    tk "Is commoner sarcasm always so snarky and unfunny? Or are you just bad at making jokes?"

    scene tsubasalimo2
    with dissolve

    tb "Tsukasa, be nice. We may not be at the manor, but Sensei is still our guest. And we must treat him with the same level of respect we’d treat anyone else."
    tk "Yes, Mother. Can I ask a question, though?"
    tb "Of course, dear."
    tk "Why do we have to drive him home when he said he was okay with walking? Isn’t doing that just unnecessarily flaunting how rich we are?"

    scene tsubasalimo3
    with dissolve

    tb "There is a difference between doing something to flaunt one’s wealth and doing something out of the kindness of one’s heart."
    tb "If you’d like a better explanation, look no further than your older sister as the two of you seem to approach this matter in completely different ways."
    tk "My way is better. People are always taking advantage of Onee-sama because she has a heart. Do you think Jeff Bezos or Elon Musk have hearts, Mother? Because I don’t. And {i}they{/i} rule the world."
    tb "Well, until {i}you{/i} rule the world, please try and be more like your sister."
    s "Tsukasa’s right, though. "

    scene tsubasalimo4
    with dissolve

    tk "I am?"
    s "Not about the wealth thing — though, I will agree you’re not entirely {i}wrong{/i} in that regard. But I was talking more about the “driving me home” part."
    s "You didn’t have to go this far out of your way for me, even if it {i}was{/i} out of the kindness of your heart."
    tb "Nonsense. It’s no trouble at all. In fact, I’m glad things worked out this way as it gives me a rare opportunity to capitalize on something I’ve been particularly interested in."

    scene tsubasalimo5
    with dissolve

    tk "{i}There’s{/i} my mother. I knew you wouldn’t have gone through this much trouble if you didn’t have something to gain from it."
    s "So, what I’m hearing is that this is less “giving me a ride home” and more “kidnapping me to get something you want.”"
    tb "Well, if you’d like to make me sound like some sort of villain, I suppose there would be a bit of truth to that."
    s "Well, what can I give you that your money can’t? "
    s "Oh, and if it’s something you can’t say in front of Tsukasa for {i}reasons,{/i} just wink at me. I will understand."

    scene tsubasalimo6
    with dissolve

    tk "Mother, what did that mean? Jeeves is trying to speak cryptically, but isn’t smart enough to do it properly so it didn’t make much sense to me."
    tb "Nothing, Tsukasa. And that is most assuredly not what I have “kidnapped” Sensei for."
    tb "I simply wanted to see the property my oldest daughter invested in. That’s all."

    scene tsubasalimo7
    with dissolve

    tb "Joining the world of real estate is a very respectable decision to make at Touka’s age. Even {i}if{/i} that decision was only partially made with {i}her{/i} future in mind and not {i}someone else’s.{/i}"
    s "Well, ignoring the fact that I thought we were on the way to my {i}actual{/i} home, it’s not like I pressured Touka into that or anything. I straight up told her I wouldn’t accept it."

    scene tsubasalimo8
    with dissolve

    tb "And yet you {i}did{/i} accept it. Curious. "
    s "She wouldn’t take no for an answer."
    tb "Touka rarely takes no for an answer. Do you cave to {i}all{/i} of these assertions, or just the ones that greatly benefit you?"
    s "..."
    tb "Why do you look so threatened? Did I hit the nail on the head?"
    s "Kind of. But if I look threatened, it’s probably more due to the fact that I know you could murder me and cover it up without any trouble at all."

    scene tsubasalimo9
    with dissolve

    tb "Nonsense. There would be a {i}little{/i} bit of trouble. But I can promise you that you’re in good hands. "
    tb "Touka would be {i}quite{/i} disappointed if her favorite teacher mysteriously vanished, of course."
    s "So, what then? You just want to see my apartment and then you’ll release me from your villainous clutches? "

    scene tsubasalimo10
    with dissolve

    tb "You think you can break free from my grasp that easily? "
    s "No. And I also think I probably look slightly more threatened right now."
    tb "I think you {i}should{/i} look slightly more threatened right now. I’m a very powerful woman, Sensei."
    tk "Mother, is this what “flirting” is?"

    scene tsubasalimo11
    with dissolve

    tb "What? Where did you learn that?"
    tk "Jeeves, there are easier ways of getting inside Tsukioka Manor than engaging in an affair with my mother. You don’t have to try that hard. The butler offer is still on the table."
    tb "Tsukasa, that is absolutely not what is going on right now. It was playful bantering. Right, Sensei?"
    s "It kind of felt like flirting near the end there. I won’t lie."

    scene tsubasalimo12
    with dissolve

    tb "Ugh, fantastic. Now, Tsukasa’s curiosity is going to be piqued and we’ll need to start her on “those” slideshows even earlier than anticipated. And she was already ahead of schedule."
    tk "Do I have to watch those? Onee-sama didn’t leave her wing of the manor for a full week after she watched them and that makes me kind of worried."
    tb "I will not argue if you also wind up staying in your wing for a week after all is said and done. Or longer."
    s "You two can look around the apartment. I doubt it will be any fun, though. I haven’t really changed anything yet. "

    scene tsubasalimo13
    with dissolve

    tb "Oh, Tsukasa won’t be joining us. It will just be you and me. "
    tk "What?! Why?! I want to see Onee-sama’s low-income housing too! You know I love low-income housing!"
    tb "What I {i}know{/i} is that you need to go to sleep or you’ll be grumpy for your classes in the morning."
    tk "I already know everything in those classes! I want to learn more about real estate so I can help you and Onee-sama next year!"
    tb "No means no, Tsukasa."
    tk "But Mother-"
    tb "No talking back. Responsibility first, leisure second. If you do well tomorrow, {i}then{/i} we can return to your sister’s building. Tonight, you will go to sleep."

    scene tsubasalimo14
    with dissolve

    tk "...Fine. But only because I’m extremely mature and goal-oriented."
    tb "This all works for you, correct? "
    s "Does it even matter? You’re just going to talk me into it if I say no. "

    scene tsubasalimo15
    with dissolve

    tb "See? I told you it was impossible to escape my grasp."

    scene black
    with dissolve2

    "The driver stops by Tsukioka Manor and drops Tsukasa off, who is then promptly escorted inside by an unnecessarily large amount of bodyguards and staff members."
    "I’m not sure what would have happened within the thirty seconds it took for them to make it down the walkway, but I guess that doesn’t matter as it's now fading from my vision anyway."

    scene tsubasalimo16
    with dissolve2

    "When we eventually make it to my apartment, Tsubasa takes it upon herself to start traipsing around as if she owns the place. Which...I guess she kind of does."
    "But that doesn’t make it any less weird."
    "In fact, this whole situation is weird. "
    "I get wanting to check out the building her daughter invested in, but that could have been done without me."
    "There are plenty of other rooms {i}without{/i} tenants here. So either there’s more to this than she’s letting on or-"

    tb "I assume you’ve caught on by now that this is a little more than a quick walkthrough to inspect the property."
    s "...Yeah. "
    s "I should have figured that out when you wouldn’t let Tsukasa come. "

    scene tsubasalimo17
    with dissolve

    tb "Oh?"
    tb "Then, since you appear to have slipped into detective-mode, tell me...what do you think I was trying to gain by coming here {i}alone{/i} with you in the middle of the night?"
    s "..."
    tb "Well?"
    s "I mean...common sense would probably say sex."

    scene tsubasalimo18
    with dissolve

    tb "Is that your final answer?"
    s "It would make the most sense. "
    s "You’re a seemingly...dissatisfied married woman with enough power and money to ensure I wouldn’t talk about it. Which I wouldn’t do anyway, but still."
    s "And you’re certainly calculating enough to ensure we wouldn’t get caught. "
    tb "But?"
    s "But...I feel like that’s not it."
    tb "Then what is?"
    s "Something...with Chika? Or Touka? "
    tb "Are you just guessing at this point?"
    s "Kind of, yeah."
    tb "Hmm..."
    tb "Do you have any champagne? Or wine?"
    s "I...do not."

    scene tsubasalimo19
    with dissolve

    tb "I suppose I’ll have to get you some as a housewarming present, then. It’s bad manners to keep your house-guests thirsty, you know."
    s "I mean...it’s not like I was expecting-"
    tb "It’s bad manners to not offer them a seat as well."
    s "..."
    s "Would you...like to sit?"
    tb "I thought you’d never ask."

    scene black
    with dissolve2

    "Tsubasa steps forward and...takes a seat on the bed?"
    "Is she actually here for sex after all?"

    scene tsubasalimo20
    with dissolve2

    tb "Hmm...the decor is a bit bland for my tastes. But overall, I’d say this is an acceptable staging for Touka’s first property."
    tb "You really lucked out getting this for free, didn’t you?"
    s "Like I said, I wasn’t asking for this."
    tb "How many people know about this place?"

    scene tsubasalimo21
    with dissolve

    s "Counting you? About...a handful."

    "There could have been more, but the world took them away."

    tb "So...three others apart from my daughter and me."
    tb "I see."
    tb "Is your niece one of them?"
    s "She’s not."
    tb "Is {i}Chika{/i} one of them?"
    s "She’s...not."
    tb "Interesting."
    tb "May I ask what you intend to use it for? You already have a house of your own. And, from what I understand, it’s your niece who takes care of you, so..."
    tb "You’re likely not intending to {i}live{/i} here, correct?"
    s "I don’t really have any idea what I’m going to use this place for just yet."

    scene tsubasalimo22
    with dissolve

    tb "Are you open to suggestions?"
    s "I...guess?"
    s "Do you have something in mind?"

    if chikalust25 == True:
        tb "To begin, I think this would be an acceptable substitution for Touka’s bedroom the next time you engage in violent sex with a teenage girl."

        scene tsubasalimo23
        with dissolve

        s "Yeah...that’s a pretty reasonable suggestion. I’ll keep it in mind."
        tb "Was the barking your idea or hers?"
        s "Are you actually interested or are you just winding up to something?"
        tb "Can it not be both?"

        scene tsubasalimo24
        with dissolve

        s "I take it that means it’s both."
        tb "I am a woman of questionable morals at times. "
        tb "Would I act as you do and go out of my way to engage in illicit relations with high schoolers? No. More than likely, not."
        tb "But would I leave the door cracked and peer through as {i}you{/i} do that for several minutes while questioning my sanity? Perhaps."
        s "Did you enjoy the show?"
        tb "I enjoyed that {i}you two{/i} enjoyed it. You seemed just as enthralled with one another as the day I first met you."

        scene tsubasalimo25
        with dissolve

        tb "Whether it be her body alone, the taboo nature of taking something you’re not allowed to have, or genuine love...I know not. But we’ve already discussed this once before and I don’t mean to do it again."
        s "Then...what do you intend to-"

    scene tsubasalimo26
    with dissolve

    tb "Why not share in this newfound convenience with someone who needs it more?"
    tb "Why not ask Chika and her sister if they’d like to move in?"
    s "That’s a lot more wholesome of a suggestion than I expected based on your...demeanor ever since we left her apartment."
    tb "If I don’t keep you on your toes, you might wind up getting the better of me someday. And we can’t have that, can we?"

    scene tsubasalimo27
    with dissolve

    s "Doesn’t matter. Chika already said no to your hospitality. And sure, you were inviting her to come live {i}in your mansion,{/i} but I doubt she would have accepted this either. "
    tb "As do I. Her will is far stronger than it should be for a girl her age. And her experience growing up with close to nothing has skewed her perception of just how meaningless material goods are."
    s "Says the woman with more “material goods” than anyone."
    tb "It’s because I have everything that I know just how little any of it matters."

    scene tsubasalimo28
    with dissolve

    tb "I’ll never actually replace her mother. Nor do I intend to. And even if Chika appreciates the role I’ve somehow wound up with in her life, I think she feels a little guilty. "
    tb "If I were her and the last connection I had with my mother apart from some jewelry and makeup were the memories of a home...and some other woman tried to whisk me away from that-"
    tb "I’d almost surely say no as well."
    tb "But that’s different from a person she’s in love with asking her. You wouldn’t be “replacing” anyone. "

    scene tsubasalimo29
    with dissolve

    tb "You’d be the next step in her life...or a chance for her to grow without convincing herself she’s abandoned what little she has left."
    s "But it wouldn’t be the right step."
    tb "Not even if it would make her safe?"
    s "You know very well she’s not safe with me."
    tb "Because you’re having consensual sex with her slightly before you’re {i}supposed{/i} to be? That’s silly. "
    tb "She’ll be safer because she’ll have stability...and she won’t have to worry about living in an area where people are defecating on the streets."
    tb "I’d never force her to walk away from important memories...that would be insensitive and it is just not the type of person I am."
    tb "The type of person I {i}actually{/i} am would subtly convince her that what she wants isn’t what she needs...all while slowly guiding her from the shadows into a safer, healthier life."
    tb "It’s manipulation in the {i}good{/i} way. It’s stripping away the things that could potentially hurt her, all while setting her up for success."
    tb "As the new matriarch in her life, it’s my duty to keep an eye on things like that. And, apologies if this dehumanizes you, but you’re a tool I need in order to get that done."
    s "Kind of like how I was a tool to start moving Touka forward as well?"
    tb "Exactly. "

    scene tsubasalimo30
    with dissolve

    tb "I look out for my girls. "
    tb "And we both know she’d be better off if she could free herself from that cage of responsibility she was locked in when her mother died."
    tb "She can’t do it alone...and she won’t accept help from someone who {i}can{/i} help her because it will make her feel like she’s failed."
    tb "But she’ll accept it from someone who can’t."

    scene tsubasalimo31
    with dissolve

    s "..."
    tb "At this rate, she won’t accept my aid until her sister falls ill. And by then, it may already be too late."
    tb "We can change that if we work together."
    tb "I can handle the financials and the motherly bonding-"
    tb "And you can be the curtain maintaining the illusion that she’s doing it all on her own."
    s "This would be way easier if she’d just accept how shitty her life is."
    tb "I don’t know if she’d have ever made it this far to begin with if she’d done that."
    tb "Sometimes, those less fortunate than us need to refute reality entirely to create a world that feels like it’s worth living in."
    tb "They trick themselves into seeing a light at the end of a tunnel even when everything is dark...and it’s that false chase that keeps them occupied enough to never give up or turn around."
    tb "When you have nothing, you’re forced to create something."
    s "What happens when you have everything?"

    scene tsubasalimo32
    with dissolve

    tb "You share it."
    s "Tell that to Jeff Bezos or Elon Musk. "
    tb "The only thing I’d tell them is to shove it. "
    tb "Talk to Chika. Convince her that coming here is the right move."
    s "I can’t just ask her to move in with me, though. If she finds out Touka gave me this place, it’ll open a whole can of worms and spiral into...terrified jealousy or something. I know her."
    tb "Then just tell her you bought it yourself. Or-"

    scene tsubasalimo33
    with dissolve

    tb "Ah! "
    tb "I’m a genius!"
    s "I’m already aware of that. You don’t have to brag about it."
    tb "The key is quite literally {i}making her think she’s done this on her own.{/i} "
    tb "So if we frame it as a new, affordable apartment complex with a rate that wouldn't immediately dissuade her, she’ll be able to get out of that god-forsaken section of Kumon-mi once and for all."
    s "Maybe, but that still doesn’t change the fact that she’s got an extreme emotional attachment to her current place."
    tb "But she has an extreme emotional attachment to {i}you{/i} as well. That’s what I’ve been trying to explain all along."
    s "I don’t know, Tsubasa...we can try, but-"

    scene tsubasalimo34
    with dissolve

    tb "I’m going to call my daughter. The more bearable one. But think more about what I said."
    s "You said a lot of things tonight, so if you could give me like one major theme or idea to ponder over while you’re gone, that would be nice."
    tb "Hmm...I suppose I can pose a question. Does that work?"
    s "Sure."
    tb "Then..."
    tb "What matters more — the livelihood of those you care about...or a life of unparalleled convenience?"
    tb "Ooh, and here’s another one — how much work are you willing to put in to help someone resistant to change?"
    tb "Oh! And also-"
    s "That’s enough. I’m good with just those two questions. Thanks."
    tb "One more. That’s all."
    s "Ugh...fine."
    tb "Can you still love someone if they’re always right beside you?"

    scene black
    with dissolve2

    "Tsubasa leaves before I can tell her I already have an answer to that last question."
    "It was just someone else who helped me figure it out."

    $ renpy.end_replay()
    $ tsubasaspecial15 = True
    $ tsubasa_love += 1
    stop music fadeout 7.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label tsubasadate20:
    scene tsubasakyudo1
    with dissolve2
    play music "summerwind.mp3"

    "Another weekend morning is another chance to hang out with Touka. "
    "Or, since Touka doesn’t seem to be around right now, a chance to hang out with her mom and a dejected lesbian. "
    "Weekends are awesome."

    s "Morning. Where’s everyone else?"

    scene tsubasakyudo2
    with dissolve

    tb "Oh, Sensei. Good day to you. Were you intending to sit in on practice this morning?"
    w "Yeah, I’m sure that’s exactly why he’s here."
    s "I guess that’s one way to put it. How about you, though? I don’t bump into you over here very often."
    w "Just how frequently are you trespassing in my kyudojo, Arakawa? You know you’re not supposed to be here."
    s "I’m sorry, I just missed you so much."
    w "And I miss sleep, but you don’t see me spending day after day in bed."
    s "You know, I really wish I did. You need it. "
    tb "I was just dropping by to check in on my daughter. But I know she doesn’t like it when I watch her participate in sports, so I wasn’t planning on staying very long."
    w "Unfortunately, Tsubasa picked the worst day to do this on account of the girls spending today’s morning practice tending to and maintaining their equipment."
    s "Tsubasa? Since when are you two on a first-name basis? I didn’t even realize you knew each other."

    scene tsubasakyudo3
    with dissolve

    tb "We didn’t until just moments ago. And I’m the one who proposed we address each other by our first names as I see no reason to be so formal with a fellow alumna of Higashigaoka Girls’ Academy."

    scene tsubasakyudo4
    with dissolve

    s "Fellow alumna? But didn’t you go to some super-rich girl school for, like...you know, really rich people? With good manners and all of that stuff?"
    tb "I did attend such an academy, yes."
    s "And...you’re saying Wakana did too?"
    tb "Unless I’ve been deceived, that is what I am saying. Yes."
    s "You’re a {i}private school{/i} girl?"

    scene tsubasakyudo5
    with dissolve

    w "Why do you sound so surprised?"
    s "You know, if anything, I think this actually helps me understand you even better. "
    w "Meanwhile, I’d be shocked to discover you had any sort of formal education whatsoever. "
    s "You two didn’t go to school together, did you?"

    scene tsubasakyudo6
    with dissolve

    tb "Oh, heavens no. I’m much, much older than Wakana. She hasn’t even finished her twenties yet."
    s "Oh, right. She’s so lifeless that I forget she’s younger than me sometimes."
    w "This guy..."
    s "How old are you, Tsubasa? I don’t think I’ve asked."

    scene tsubasakyudo7
    with dissolve

    tb "And for good reason. It’s incredibly impolite to ask a woman her age. "
    w "It’s also incredibly impolite to add several years to it."
    tb "If you don’t mind, Sensei, I’d prefer to keep that information confidential. You don’t see me asking you for {i}your{/i} age, do you?"
    s "Don’t need to. I’m 31. Now you know and I get to find out how old you are as well. It's only fair."

    scene tsubasakyudo8
    with dissolve

    tb "Oh my. No wonder you’re still so full of life. You’re so young. And with Wakana only several years your junior, the two of you would make excellent-"
    w "Enemies."

    scene tsubasakyudo9
    with dissolve

    tb "...Enemies, indeed. "
    s "We’re the good kind of enemies, though. The ones who secretly really care about one another deep down."
    w "The only thing I care about is regaining control of the archery range. Get out of here, Arakawa. Go crawl back into your hole."
    s "What she really means to say is, “I can’t wait until I see you again.” To which I would agree."
    w "No, what I really mean to say is “Go crawl back into your hole.” Which is exactly what I said because, unlike you, I can get by {i}without{/i} sucking the life force out of everyone around me."
    s "Are you sure? Because apart from you being out in the sun right now, being a vampire would kind of explain a lot."
    w "I want you to fucking die."

    scene tsubasakyudo10
    with dissolve

    tb "Now, now — I understand there’s a bit of hostility between you two, but if you truly do care for one another as you say, you’ll refrain from turning this archery range into a crime scene."
    tb "Sensei, seeing as I’ll be unable to watch my daughter’s practice today, would you care to spend the afternoon with me instead? A nice walk around the grounds seems refreshing, yes?"
    w "Are you sure you want to spend your time with {i}him?{/i} Would you not be better off snapping a twig off of a bush and conversing with that instead?"
    tb "Of course not. I wouldn’t want to dirty my gloves."
    s "You know what? I’ll take it. A victory over a twig might not sound like much to most people, but for me it’s a pretty big deal. "

    scene tsubasakyudo11
    with dissolve

    tb "Would you be so obliged as to join us, Wakana? It isn’t very often I bump into alumnae and I’d greatly enjoy the company of someone with a similar background. No offense to Sensei, of course."
    s "None taken. I wouldn’t have fit in somewhere like that anyway."
    w "You weren’t even the right sex to be admitted, Arakawa. And no, I’ll respectfully decline your invitation and leave you with your twig. I should be checking on my students anyway."
    tb "Perhaps the next time I drop by, then. It was nice speaking with you, Wakana."
    w "It was nice speaking with you as well."

    scene tsubasakyudo12
    with dissolve

    w "Not you, though."

    scene tsubasakyudo13
    with dissolve

    s "..."
    tb "..."
    s "We’re friends, I swear. "
    tb "Close ones, at that. The way she told you to “crawl back into your hole” was absolutely dripping with positive sentiment."
    tb "Now then, shall we go? I, regretfully, don’t have much time to spare today. And I’d like to make the most of what I {i}do{/i} have that I possibly can. "
    tb "Does a stroll around the range fit your schedule, {i}Arakawa-{/i}Sensei?"
    s "Oh, have I graduated from just “Sensei?” I get to have a two-part name now?"
    tb "That didn’t come across as disrespectful, did it?"
    s "Not at all. But I was also just called a twig moments ago and didn’t mind, so titles clearly don’t mean much to me."
    tb "In that case, I suppose I’ll start using your last name more often. We are business partners now, after all."
    s "We...are?"

    scene tsubasakyudo14
    with dissolve

    tb "Walk with me. There’s something we need to discuss."
    s "Oh god, what is it now?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene tsubasakyudo15
    with dissolve2

    tb "After discussing the Chosokabe matter with my daughter, it appears we’re ready to move forward."
    s "Okay...and “moving forward” means?"
    tb "Waiting for you to trigger the magnetic reaction that will pull Chika closer to safety, of course."
    tb "Touka has agreed to listing several of the additional rooms in your complex at a rate well beneath what they’re actually worth. "
    tb "After all, the goal in investing in the property was never to generate income, but moreso to give her an understanding of how the system and property management work as a whole."
    s "Is...generating revenue not a part of the “system and property management?”"
    tb "It is. Of course it is. But this is closer to a small project for her than something she’s meant to live off of. Everything she needs and wants is already supplied by the Tsukioka Foundation."
    s "Wouldn’t it make more sense to...let Chika keep her old apartment and just toss her the key to a new one in the event she changes her mind and wants to move?"
    tb "That’s essentially what we’re doing, Arakawa-Sensei. Just instead of {i}tossing{/i} her the key, we’re leaving it on the ground for her to pick up."

    scene tsubasakyudo16
    with dissolve

    tb "Unless you don’t want her closer to you for some reason. And that’s certainly not the case, is it?"
    s "I mean...it could definitely cause some problems."
    tb "Ohh?"
    tb "You weren’t intending to use my daughter’s generous gift as a secret love nest, were you? Does having your {i}girlfriend{/i} in the same building throw a wrench into things?"

    scene tsubasakyudo17
    with dissolve

    s "It’s a little more complicated than that. I’ve barely even spent any time in that apartment..."
    s "But it feels weird to just uproot someone’s life under the guise of “this is better for them” when that shouldn’t be our choice to make."
    tb "A well-thought out answer and impressive deflection away from my “love nest” accusation. Though, I wouldn’t say it’s one I agree with."

    scene tsubasakyudo18
    with dissolve

    s "And why’s that? "
    tb "Isn’t it obvious?"
    tb "Most people aren’t smart enough to make their own decisions."
    tb "The world would crash and burn if it weren’t for those of us who can bend it to our will...and shape it back into its proper form."
    tb "Chika’s an amazing girl and I care for her and empathize with her — but she isn’t smart."
    s "She {i}is{/i} though. You don’t know her like I do."
    tb "I know that she has a sexual relationship with an adult male. And that she’s turning down free aid that would make both her {i}and{/i} her sister’s lives easier."
    tb "The first of which can be justified under the pretense of you providing some sort of benefit — emotional, physical or financial — but the second?"
    tb "The second is pure negligence and stubbornness and will only force her down the same road her mother had to walk before her."

    scene tsubasakyudo19
    with dissolve

    tb "If I need to reshape things one more time to prevent her from enduring such tragedy, so be it. I do it out of the kindness of my heart and ask for nothing in return."
    s "But doing things your way just seems like it’s providing an illusion of free will. It’s not giving Chika or...anyone else you deem “not smart enough” the chance to burn out or fail on their own."
    s "Sometimes, people need that if they’re going to improve."
    tb "I agree. But this isn’t a score on a test or a poorly-made resume- it is a life. {i}Two{/i} lives, even."

    scene tsubasakyudo20
    with dissolve

    tb "What’s wrong with playing God when the one we dreamt up never wants to come outside?"
    tb "As long as nothing crashes and burns, we’ll have succeeded. So you can keep playing the “good cop” all you want while believing the girls you know so well are capable of making their own decisions-"
    tb "Or you can leave it to the “bad cop” who just-so-happens to have good intentions. "
    s "You really are “manipulative in the good way,” aren’t you?"

    scene tsubasakyudo21
    with dissolve

    tb "I really am."
    s "I respect your speech and all. It’s nice hearing from someone with a mindset like that. But it’s making me a little confused about your stance on Touka. "
    tb "How so?"
    s "Do you not think her life is at stake by throwing her into my class at such an impressionable part of her life? "
    s "She might have a healthy, albeit extremely obnoxious, little sister...but this is her education we’re talking about and you’ve figured out by now that’s, like...the last thing on my list of priorities."
    s "I guess what I’m asking is...why is she allowed to make her own decisions, but Chika can’t? Is it really just the sister thing that changes all of this?"

    scene tsubasakyudo22
    with dissolve

    tb "Not at all. In fact, my repeated presence at this school should be the only hint you need in regard to her autonomy."
    tb "There are several mistakes I {i}want{/i} her to make- and she is well on her way to making them. "
    tb "But it all circles back around to what {i}I{/i} want for her as I would never put her into a position where that outcome would be unachievable."
    s "You really are just a well-endowed puppeteer, aren’t you?"

    scene tsubasakyudo23
    with dissolve

    tb "Perhaps I am!"

    scene tsubasakyudo24
    with fade

    tb "Does that make you my puppet?"
    s "I guess that depends on whether or not you think I’m “smart enough” to make my own decisions."
    tb "Surely you’re not making me out to be some sort of {i}villain,{/i} are you, Arakawa-Sensei?"
    tb "I’m sure a man of your position can understand my point of view, no?"
    tb "I possess both the intellect and influence to make anything I want a reality. Why would I {i}not{/i} do that?"
    s "Again, you’ve got a point. I’d probably do the same thing in your position."
    tb "Which is why I like you. But that’s enough about me and my points of view — why don’t you tell me a little about {i}yourself?{/i}"
    tb "What do you believe in?"
    tb "What’s your favorite food?"
    tb "What kind of music do you like?"
    tb "I have so many questions for you."
    s "This might come as a surprise given my outstanding charisma and boisterous attitude, but I don’t really like talking about myself."
    tb "But you’ve learned so much about me so far. And you’ve been addressing me as “Tsubasa” this whole time. Do you not want to be my friend after all?"
    s "That’s not it. I’m just not that exciting. That’s really all it is."

    scene tsubasakyudo25
    with dissolve

    tb "Ohh? "
    tb "Perhaps I’ll look into you on my own, then? I can’t have my daughters, biological or not, spending so much time around a man with a shady background, can I?"
    s "You’re not trying to intimidate me right now, are you? Because the smirk and the fact that I have to look up at you were more than enough to do that without the vague threat."

    scene tsubasakyudo26
    with dissolve

    tb "That’s not what I want."
    tb "I’ve spent so much time looking down on others that being up here is just more comfortable for me. That’s all."
    tb "You’re an interesting person, Arakawa-Sensei. And I really do want to learn more about you as I assume you’ll be growing {i}quite familiar{/i} with my family in the years to come."
    s "That “quite familiar” emphasis was a little suggestive, don’t you think?"
    tb "You’ll have to forgive me if my...{i}sincerest{/i} thoughts managed to leak out. I just meant that I don’t intend to let you walk away from us is all."
    tb "We’ve all taken quite the interest in you."

    scene tsubasakyudo27
    with dissolve

    tb "But, with you unwilling to tell me any more about yourself, it appears that I’ll have to look further into you on my own after all."

    scene black
    with dissolve2

    tb "Come now. You can escort me to the car. "

    "Tsubasa gestures as if she’s pulling on puppet strings, but I follow her up the stairs out of my own free will. "
    "Or...what I {i}think{/i} is my own free will but is actually just her masterminding my every move like she was alluding to earlier."
    "She reminds me of someone else in a way."

    play sound "static.mp3"
    scene nodokacrazy1 with flash
    scene black with flash
    stop sound

    "But the two of them are completely different."
    "I can understand what Tsubasa wants...and it really does seem like she just wants this world to be a better place."
    "But “better” is subjective...and she likely hasn’t failed enough in life to know that what “she” wants isn’t what’s best for everyone."
    "Is she like me — so self-centered that she’ll never be able to look past that? "
    "Can she keep believing what she’s done is right even when it’s wrong in every other sense of the word?"
    "Or is she someone who can change the way she thinks...and reshape {i}herself{/i} along with the world she treats as a globe, spinning infinitely beneath her finger?"
    "I don’t know."
    "I’m not close enough to her yet."
    "But..."
    "I don’t mind having her yank my strings a little longer if it changes that."

    $ renpy.end_replay()
    $ tsubasadate20 = True
    $ tsubasa_love += 1
    stop music fadeout 7.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label tsubasaspecial20:
    play sound "phonebeep.wav"

    "I tap on Tsubasa’s name in my phone with a bit more optimism than normal- but it’s not because I understand her any better now."
    "And it’s {i}also{/i} not because I foresee any sort of progression in regard to our (but mostly {i}her{/i}) super secret plan to relocate a gyaru."
    "That still hinges upon me to some extent and, with no further movement from Chika on top of my customary lack of action, things will likely stay the same for at least a {i}little{/i} while longer."
    "But as these last few sentences have pulled me from the beaten path we were walking together just moments ago, I’d like to now confess {i}why{/i} I’ve been stricken with optimism."

    scene noonsky
    with dissolve2
    play music "tsukiokamanor.mp3"

    "You see, last night, I had another dream — and in it, the paint peeled from off of the walls in my home, but it was only the first layer."
    "The layer {i}beneath{/i} told me a secret."
    "It said “The past will catch up to me” before that layer peeled off as well."
    "Then suddenly, my house was gone and I was all alone in a field full of sunflowers."
    "I plucked one from the ground and pressed it to my tongue."
    "And I remembered why I’ve always loved them."

    play sound "phonebeep.wav"

    tb "Ahh, Arakawa-Sensei. Excellent timing. I was just about to call you."
    s "Really? You never call me."
    tb "Well, today is a special exception as you are being cordially invited to join me in my office for a bit of a meeting."
    s "Does this involve Chika again? Because I still haven’t-"
    tb "It does not. This is a matter regarding my family and yours."
    s "If this is a joint marriage proposal, I’d like to remind you I have basically nothing to offer."
    tb "Why, that’s not true at all. But you can take solace in the fact that it’s something completely different."
    s "Can...you tell me what that something is?"
    tb "I will! But I would like you to actually {i}be{/i} here first. "
    s "I guess I’ll...start walking then."
    tb "Oh, that won’t be necessary. Someone should-"
    limo "Arakawa-sama, please get into the vehicle."
    s "What the fuck? Where did you come from?"
    tb "Oh, splendid! It sounds as if your car has already arrived! "
    tb "You’ll be escorted directly to me upon arrival. I’m looking forward to it."
    limo "Arakawa-sama, the mistress is waiting. Please get into the vehicle."
    s "Fine, okay. But I’m not wearing another blindfold."

    scene black
    with dissolve2

    "I get into the back of the car and am quickly whisked off to Tsukioka Manor for an impromptu meeting with someone I am now tempted to refer to as “the mistress.”"
    "The main problem here is that I’d likely be unable to say this without a sarcastic undertone that would make it sound as if I’m mocking her. And I would prefer not being assassinated today."
    "As such, I will respect Tsubasa as much as I possibly can."
    "And I will only try to have sex with her if I think she {i}really{/i} wants it."
    "Anything else is just too risky."
    "........."
    "......"
    "..."

    scene tsubasameeting1
    with dissolve2

    tb "Welcome to yet another brand new room — and a rare one at that. You join the ranks of the lucky few who have been able to sit with me at this table. It’s something you should be very proud of."
    s "And all I had to do to get here was make your daughter want to bone me."
    tb "..."
    s "..."
    s "My bad. I’m not very good at formal meetings like this."

    scene tsubasameeting2
    with dissolve

    tb "It’s fine. It’s not as if anyone is listening in on us. I just can’t help but be taken aback by your...casual brazenness. "
    tb "No one’s ever had the courage to say such a thing to my face before."

    scene tsubasameeting3
    with dissolve

    tb "But that’s just one more thing that makes you all the more interesting."
    s "Am I allowed to flirt back or does that go against manor policy?"
    tb "Go ahead. This isn’t me accepting your advances, but I’m curious to see what you’d say."
    s "Uhh..."
    tb "..."
    s "..."
    tb "Nothing? Are you not attracted to me after all?"
    s "It’s just...kind of hard when you’re directly challenging me."
    tb "Then let’s just say you said something flattering and that I laughed. And that we left it at that before moving onto other things."
    s "Ahh, so it’s {i}not{/i} just a meeting where you flirt with me. I was beginning to think the arranged marriage was for {i}us.{/i}"

    scene tsubasameeting4
    with dissolve

    tb "Oh, look! You managed to flirt after all. That was actually rather cute. Good job, Sensei."
    s "And now it’s weird again since you’re complimenting me."

    scene tsubasameeting5
    with dissolve

    tb "Does this feel awkward for you? Would we have been better off in the garden? "
    tb "I know it might seem as if I’m trying to put myself in a position of power here, but the truth is I just had a lot of work to get done and all of that work is in {i}here.{/i}"
    s "It does...but it would feel less awkward if you’d just tell me why I’m here already."

    scene tsubasameeting6
    with dissolve

    tb "Then, to save {i}both{/i} of us the discomfort, I’ll get right to it."
    tb "When we last left off on the stairs of your school’s archery range, you made it apparent that you weren’t interested in divulging any of your...personal details to me."
    tb "To which I responded that I would look into them on my own."
    s "And...I’m assuming this meeting is in response to you doing just that."

    scene tsubasameeting7
    with dissolve

    tb "And in that assumption, you would be correct...{i}Akira.{/i}"

    "Welp, make it four people who now know that name."

    tb "Is it okay if I call you that? It seems only fair, what with me just being “Tsubasa” to you and all."
    s "Is “the mistress” preferable? Because that’s how the driver earlier referred to you and I was thinking it might be fun to try that."
    tb "If you’re planning on working {i}for{/i} me instead of {i}with{/i} me, such a title would be fine. But I’d prefer to keep things a bit more amiable between us."
    s "So...what do you want?"
    tb "Why do you think I want something?"
    s "The look into my background...the raised eyebrow...the way your hands are folded together...all signs point to you wanting something."
    s "What did you find out? Why did it warrant calling me to your home?"

    scene tsubasameeting8
    with dissolve

    tb "What I {i}found out{/i} is that you’re a much more...{i}legitimate{/i} teacher than you present yourself to be."
    tb "Your grades in school were exceptional...among the top of your class even. And every single career assessment survey you ever filled out all had the same exact aspiration listed on them. {i}Teacher.{/i}"
    s "You read my...career assessment surveys?"

    scene tsubasameeting1
    with dissolve

    tb "If it’s something you’ve written on paper and handed over to someone, chances are I have access to it. "
    tb "You were quite the poet as well. Do you still write?"
    s "..."
    tb "Ara- {i}Ahem...{/i}Akira-san?"
    s "No. I don’t write anymore."
    tb "Did something happen?"
    s "..."
    tb "Is that a troubling question?"
    s "I don’t want to talk about it."
    tb "So much for not being very interesting. "
    s "Is that all, {i}mistress?{/i}"

    scene tsubasameeting9
    with dissolve

    tb "Oh my. I didn’t mean to anger you. I was simply curious about how you became the way you are today."
    tb "No amount of records or poetry can properly retell the story of the life you’ve lived. So I was hoping you would share a piece or two of that with me."
    s "And I was hoping my private life would stay a little more, you know, {i}private.{/i}"
    tb "In my defense, you didn’t try to stop me when I explicitly told you this was coming. I’d not have pried if I’d only known you were against it."
    s "It’s...fine. "
    s "To be honest, the past is a bit of a touchy subject for me as there’s still a lot of it I don’t remember."
    tb "That you don’t...remember?"
    s "Just call it amnesia. That’s the simplest way to explain it."

    scene tsubasameeting10
    with dissolve

    tb "Your medical records mention nothing about amnesia. Could I be missing documents? I’m normally so good at this."
    s "It’s not something that would be {i}documented.{/i} And yeah, there was a thing that happened. "
    s "But I’m nowhere even close to being able to talk about it with anyone yet...let alone someone who’s only probing me to satisfy her own curiosity."

    scene tsubasameeting11
    with dissolve

    tb "You say that as if I don’t care about you. That hurts."
    s "{i}Do you, though?{/i}"
    tb "Of course."
    s "But it’s only because of the role I play in your scheme, right? It’s only because Touka needs me in order to...move forward and adhere to the plan you have for her or whatever."
    tb "..."
    s "Am I wrong?"
    tb "..."

    scene tsubasameeting12
    with dissolve

    tb "{i}Hah...{/i}"
    tb "I sincerely apologize, Akira-san. "
    tb "I must have let my guard down at the archery range as it’s very clear now that I didn’t properly think my words through."
    tb "If I had, you wouldn’t think this way at all."

    scene tsubasameeting13
    with dissolve

    tb "It’s true that I fancy pulling the strings...and that there is nothing more important to me than ensuring my daughters’ futures play out just as smoothly as mine."
    tb "But that doesn’t mean I see you as nothing more than a hunk of meat...ready to be thrown on the grill so they can go to sleep sated and satisfied."
    tb "I see you as an equal."
    s "You don’t see anyone as an equal."
    tb "That is simply not true. And if I’ve come across that way, it means I must have improperly conveyed {i}other{/i} words of mine as well."
    s "Consistent poor-wording aside...what does that have to do with {i}our{/i} families? What was so important that you went out of your way to borderline kidnap me?"
    tb "I would like to ask you for a favor."
    s "Big surprise. Who do you want me to reel in now?"
    tb "My daughter."
    s "Touka’s too perceptive to-"
    tb "My {i}other{/i} daughter."
    s "...What?"

    scene tsubasameeting14
    with dissolve

    tb "Tsukasa-darling! Could you come in here?"

    play sound "dooropen.mp3"
    scene tsubasameeting15
    with dissolve

    tk "Yes, Mother?"
    tb "Tsukasa, how are you faring in your studies?"
    tk "Exceptionally, Mother. There are no problems at all."
    tb "But are you enjoying yourself?"
    tk "Yes, Mother."
    tb "It’s okay to be honest right now, dear. This isn’t a formal meeting."

    scene tsubasameeting16
    with dissolve

    tk "But-"

    scene tsubasameeting17
    with dissolve

    tk "Oh. It’s just Jeeves. What is he doing here?"
    tb "Tsukasa, how would you feel about Arakawa-sensei taking over your lessons?"

    scene tsubasameeting18
    with dissolve

    tk "Really?! Can he?! That’s okay?!"
    s "Uhh..."
    tb "Is there a problem, Arakawa-sensei? It’s not as if you don’t already have experience tutoring girls her age, correct?"

    play sound "static.mp3"
    scene imissyou12 with flash
    scene tsubasameeting18 with flash
    stop sound

    s "I..."
    s "Tsukasa is on another level. I can’t keep up with whatever she’s being taught right now."

    scene tsubasameeting19
    with dissolve

    tb "The same goes for Touka and she’s been exceptional under your guidance. I assume you’ll have no trouble replicating that same success with someone younger."
    tk "Don’t worry, Jeeves! If I’m too smart for you to tutor, I’ll just teach you instead! It’ll be fun!"
    s "I don’t have the time to come here every day, Tsubasa. I’m already teaching at school and there’s no way they’d admit Tsukasa at her age."
    tb "The school will do whatever I tell them to. But that’s not what I had in mind."
    s "Then what-"
    tb "I was planning on having my daughters move into your new building as well."

    scene tsubasameeting20
    with dissolve

    tk "What?"
    tb "Is something wrong, dear?"
    tk "I’m...going to live with Onee-sama? "
    tb "There are some preparations that still need to be made. But that is the plan as of right now, yes."
    tk "And...what...what did Onee-sama say?"
    tb "That she’ll uphold her duty as the heir to the foundation and do exactly as I ask. Just as I expect you to do as well."

    scene tsubasameeting21
    with dissolve

    tk "But...that means I’ll spend even less time with you and Papa than I do now! And I barely ever get to spend time with you in the first place!"
    tb "What are you saying, dear? You’re with me almost every waking hour of the day."

    scene tsubasameeting22
    with dissolve

    tk "That’s not what I mean! You’re always working and Papa never wants to see me and I’m tired of you always trying to get rid of me! I didn’t do anything wrong!"
    tb "Tsukasa?..."
    tk "I want to stay here with you! I don’t want to leave yet!"
    tb "Tsu-"

    scene tsubasameeting23
    with dissolve

    tk "I’m going to my room!"
    tb "Tsukasa! Wait!"

    play sound "doorslam.mp3"
    with hpunch

    tb "..."
    s "..."
    s "You know, if I knew that’s what you were ramping up to, I probably could have prevented this."

    scene tsubasameeting24
    with dissolve

    tb "What? How? I don’t even understand what just happened."
    s "She’s lonely. I’ve known that since National Tsukasa Day."
    tb "How is she lonely? She’s surrounded by either attendants or me for nearly twenty-four hours every day. She gets everything she wants and {i}does{/i} everything she wants. How is that lonely?"
    s "All of that might be true, but when was the last time the two of you did something {i}fun{/i} together? Where you weren’t just being dragged along as a babysitter."
    tb "I..."
    tb "I’m not..."
    s "It’s the same with Touka too, but to a much lesser extent since you still make time to drop by her dorm room every now and then."
    s "Plus she’s also mature enough to shelve those feelings and hide them from you. Tsukasa can’t do that."

    scene tsubasameeting25
    with dissolve

    tb "{i}Hah...{/i}"
    tb "You’re right..."
    tb "You’re absolutely right."
    tb "I don’t know how I didn’t realize that earlier."
    s "Just...too busy focusing on other things, I guess."

    scene tsubasameeting26
    with dissolve

    tb "All other {i}things{/i} are now on hold — and that includes this meeting. It’s clear that I need to have a talk with {i}both{/i} of my daughters."
    s "Does that mean I can stop teaching Touka things? She keeps trying to learn while she’s in school and I’m not sure how to handle it."
    tb "You’ll continue on with Touka exactly as you’ve done thus far. And Tsukasa will follow shortly after things are remedied between the two of us."
    s "Why do you even want me to teach her? I don’t get it. "
    tb "You don’t need to."

    scene black
    with dissolve2

    "Tsubasa stands up from her desk, prompting me to do the same as I’m sure I’ll be escorted out of the manor momentarily."

    scene tsubasameeting27
    with dissolve

    "I get that her methods in growing her daughters can be a little...{i}unorthodox,{/i} but sending a girl Tsukasa’s age to live in the same building as me is something I didn’t even think she’d consider."
    "I mean...why would she? Chika makes sense. Touka {i}kind of{/i} makes sense...But what could Tsukasa gain from that?"
    "Is it the risk that would help her grow?"
    "Have I fallen so far that there’s any risk at all?"
    "I just don’t understand."

    tb "That look on your face tells me I should clarify something."
    s "Why were you...sending her to live with me? "
    tb "It was just the same building. It’s not as if I was asking her to sleep in your bed."
    tb "Besides, when {i}I{/i} was her age, I had an apartment as well. I just never had any use for it."
    s "And she does?"
    tb "I thought so. But that was {i}before{/i} the screaming and the revelation of her loneliness. Now, I know I was wrong. That happens sometimes, you know."
    tb "Just because I’m powerful doesn’t mean I don’t make mistakes. I’m as flawed and vulnerable as everyone else. "
    tb "I’m the same as you. "
    tb "That’s what I meant by {i}equal.{/i}"
    tb "And, Akira-sensei..."
    tb "I’m not trying to {i}insinuate{/i} anything here...but my decision to send her to Touka’s new apartment complex was {i}not{/i} for the reasons you may think."
    s "And...what do you assume I thought?"
    tb "Let’s just say that there are different stages of development my daughters need to go through before I will fully acknowledge them as women."
    tb "Touka is in the {i}final{/i} phase of development...and I trust that she’s mature enough to make decisions in regard to how and {i}when{/i} she uses her body."
    tb "You could lay as many fingers as you want on her and I’d think nothing of it."
    tb "But if you believe for even a moment that I’d apply that same ideology to Tsukasa...we’d have a bit of a problem on our hands. "
    tb "I would like to avoid that. Wouldn’t you?"
    s "Definitely. I wouldn’t have even thought about that."
    tb "Are you telling me you don’t find Tsukasa pretty?"
    s "I..."
    s "That..."

    scene tsubasameeting28
    with dissolve

    tb "Just a joke to lighten the mood. There was no right answer there."
    tb "Plus, once Chika moves in, I doubt you’ll have time to even {i}think{/i} of doing such things with other girls. "

    scene tsubasameeting29
    with dissolve

    tb "But in the event that both she {i}and{/i} my oldest daughter can not satisfy your...{i}urges...{/i}"
    tb "All you need to do is let me know and...{i}arrangements{/i} can be made."
    s "..."
    tb "..."
    s "That...was a joke too, right?"
    tb "I wonder."

    scene black
    with dissolve2

    "I exit the manor both terrified and aroused."
    "And after spending a lot more time with her recently, I think that’s...just the sort of effect Tsubasa is going to have on me."
    "I understand her, but I don’t."
    "I’m afraid of her, but I’m not."
    "I can’t explain it."
    "But there is one thing I know for sure."
    "And it’s that I need to keep her close."
    "Because I know that if I don’t, I’ll be peering over my shoulder for the rest of my life."
    "..."

    s "..."
    s "What the fuck are {i}arrangements?{/i}"

    $ renpy.end_replay()
    $ tsubasaspecial20 = True
    $ tsubasa_love += 1
    stop music fadeout 7.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label tsubasaspring1:
    play sound "vibrate.mp3"

    s "..."

    "Awoken by the sound of my phone, I fight back against the desire to keep my eyes closed and continue my dream."

    play sound "vibrate.mp3"

    "You see, as “wonderful” as those have been lately, I’ve developed a bit of an issue when it comes to staying trapped inside of them for too long."

    play sound "vibrate.mp3"

    "And what I mean by this is rather personal — but seeing as you’ve watched me penetrate countless teens by now, I suppose that you knowing one more intimate detail isn’t the end of the world."

    play sound "vibrate.mp3"

    "You see, I’ve become so invested and immersed in my dreams lately, that I’ve been cumming in my sleep."

    play sound "vibrate.mp3"

    "It’s particularly obnoxious on nights where it happens early on as it gives the cum time to dry and creates an extremely unpleasant sensation that never ceases to shock and surprise me."

    play sound "vibrate.mp3"

    "But I suck it up (not literally of course) because the things I’ve been experiencing in the world where she exists are far better than anything I’ve experienced here."

    play sound "vibrate.mp3"

    "I had sex with the God of Torment last night."

    play sound "vibrate.mp3"

    "And the reason I’ve decided to wake up is not just because I wanted to save myself a morning-shower, but because I feared for my dream-penis and what her scissor wings would do to it."

    scene bedroom_day
    play sound "phonebeep.wav"

    s "Hello?"

    play music "tsukiokamanor.mp3"

    tb "Oh! Good morning, {i}Akira.{/i} I’m not calling too early, am I?"
    s "Why are you calling at all?"
    tb "Oh my. Judging by {i}that{/i} attitude, perhaps it {i}is{/i} too early after all. Would you prefer if I called back at a later time?"
    s "I didn’t mean to give you an attitude. I’m just not sure why you couldn’t wait until-"

    "I take a look at the clock to find it’s even earlier than I thought."

    s "Tsubasa, it’s only 6:30."
    tb "Well, what time do people in your tax bracket typically get themselves out of bed?"
    s "Any day where I have to get out of bed before 7:00 winds up being terrible. But hey, every day has been terrible lately. So I guess I’ll just...go get the worm or something."
    tb "The worm?"
    s "You know...like...the early bird gets the worm. "
    tb "I’m confused. You own a bird?"
    s "Never mind. Just tell me what you want."
    tb "What kind of bird is it?"
    s "Tsubasa, I don’t have a bird."
    tb "Why, it’s very impolite to trick people over the phone, Akira. You should know by now how gullible and easy to deceive I am."
    s "You? No. Touka, maybe. But I refuse to believe you’re not aware of everything ever at all times."
    tb "Hahah! Stop, stop. You give me too much credit, Akira."
    s "Why do you keep saying my name?"
    tb "Well, because it’s a beautiful name, of course! {i}Akira.{/i} I’m sure you don’t mind me using your given name, correct? We {i}are{/i} friends after all, aren’t we?"
    s "Is that what we are?"
    tb "I believe so. Unless you’re looking to get something {i}else{/i} out of this relationship."
    s "Sorry, are you {i}flirting{/i} with me right now? Is this a booty call? "
    tb "Oh, I’ve heard of those in pop culture! That’s when two people arrange a meet-up with the intention of having sexual intercourse, correct?"
    s "Uhh...yeah. Yeah, that’s what that means."
    tb "Hilarious! But no, that’s not what this is. And I can’t quite tell if I’m flattered or offended that you’d assume such a thing."
    tb "I {i}would{/i} like to see you, though. "
    tb "For purposes unrelated to sex as I’m a faithful {size=-15} albeit extremely unsatisfied{/size} married woman with a heart of gold and pockets of...well...I suppose there’s gold in those as well. Hahah! I’m so funny."
    s "You got quiet in the middle of that last-"
    tb "I’m afraid I don’t know what you’re talking about. Regardless, are you free right now? I’ve opened up a slot in anticipation of your arrival."
    s "Now? I have to check on my niece first."
    tb "Ahh...yes. I’ve heard from Touka that things seem rather...complicated in that regard. But don’t worry. You may take your time."
    tb "And whenever you’re ready, there will be a car outside of your house."
    s "Like...Like it’s there right now?"
    tb "Yes. But it’s fine to keep them waiting. They’re very well-trained and understand that commoners don’t prioritize punctuality the way my family does."
    s "Tsubasa, I didn’t even know we were meeting until a few minutes ago. I don’t think punctuality matters here."
    tb "Akira, while I do love the sound of your voice, I do hope you know that every second you spend talking to me is one second between you and your beloved Ami. And then subsequently me again. "
    s "Can I at least know what you want to talk about so I can prime myself for another uncomfortable discussion with a woman who could have me killed at any moment?"
    tb "Hahah! No, actually. I quite like the idea of keeping you on {i}edge.{/i}"
    s "Tsubasa-"
    tb "Ciao! "

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "I hang up the phone and...accept that this is happening again."
    "But even though Tsubasa’s affinity for keeping me on my toes is shining brighter than ever, I do have to note that she hasn’t {i}yet{/i} blinded me in any capacity. So maybe this...instinctual distrust is wrong."
    "She {i}is{/i} on my side, right?"
    "And if she trusts me enough to be alone with her daughters, then-"

    stop music
    play sound "static.mp3"
    scene tsukasaarrives2 with flash
    stop sound
    scene specialsky

    "{b}THEN SHE IS A FOOLISH BITCH IN NEED OF SOME THICK COCK.{/i}"

    play sound "static.mp3"
    scene tsubasatalks1 with flash
    stop sound
    play music "tsukiokamanor.mp3"

    tb "Thank you very much for coming, Akira. Please allow me to extend my sincerest apologies in regard to tearing you away from your niece."
    s "It’s fine. She can be alone for a little while. "
    tb "Forgive me for asking, but would you mind sharing exactly what’s wrong with her? Because, if there’s something I could do-"

    scene tsubasatalks2
    with dissolve

    s "Can you bring the dead back to life?"
    tb "..."
    s "That was a joke. "
    tb "Oh, good. I couldn’t quite tell."
    s "Yeah. But Tsubasa, before you talk about whatever you’re going to talk about, I want to make something extremely clear to you."
    tb "Please do."
    s "Do {i}not,{/i} under {i}any{/i} circumstances, get yourself involved with my niece. "
    s "I get that you’re a {i}curious{/i} woman who {i}wants to use her powers for good{/i} or whatever it was that pushed you into uprooting Chika’s entire life and planting your daughter in my class."
    s "But this is different. This is my family. And I will not let you get involved with Ami."
    tb "Forgive me for being blunt here- but who do you think you are, speaking to me that way?"
    s "I’m not kidding. This-"

    scene tsubasatalks3
    with dissolve

    tb "Hahah! Forgive me! I just couldn’t help but try to sound threatening there. "

    scene tsubasatalks4
    with dissolve

    tb "I can assure you that if you do not want me to get involved, that I will keep my nose out of it. I know a thing or two about the situation and can acknowledge how {i}sticky{/i} it must be."
    s "I’m...not surprised to hear you know “a thing or two.” But...thanks. "
    tb "Were you scared, though? Of my “don’t talk to me like that” voice? Did I sound intimidating?"
    s "You pretty much always sound intimidating. "
    s "How was I, though? I don’t get all serious that often so I have no idea how it must have sounded."
    tb "I quite liked it, actually. It isn’t every day that someone speaks to me like that."

    scene tsubasatalks5
    with dissolve

    tb "But I suppose our time would be better spent discussing matters {i}apart{/i} from the things we like about one another. After all, you never know when my husband might be listening in."

    scene tsubasatalks6
    with dissolve

    tb "And I can’t imagine he’s the type of person you want to make {i}jealous.{/i} Right, Akira?"
    s "..."

    scene tsubasatalks5
    with dissolve

    tb "The reason I called you is simple, really. And it’s a call you’d be right to expect at...somewhat regular intervals in the future."
    tb "I understand that you’ve decided to take a leave of absence from your job as a teacher, correct?"
    s "Yeah, but...if this is about me going back-"
    tb "It’s nothing of the sort. I’d never {i}force{/i} you to do anything, even if it {i}does{/i} seem as if I’m pushing you in certain directions from time to time."
    s "I know. Because you’re the type who will manipulate me into thinking that {i}I’m{/i} making my own decisions instead. When, in all actuality, you’re the one pulling my strings. "

    scene tsubasatalks7
    with dissolve

    tb "Ooooh...you’re {i}feisty{/i} today."
    s "Only because I know you like being talked down to now."
    tb "Don’t push it, though. You’re not quite sure what my limits are yet, Akira. "
    s "You’re right. So please, do me the favor of telling me what you’re going to manipulate me into doing this time so I can go back home and take a nap."

    scene tsubasatalks8
    with dissolve

    tb "Status reports."
    s "{i}Status reports?{/i}"
    tb "On all {i}four{/i} of my daughters since the Chosokabe girls are under my wing now as well."
    s "Can’t you just...ask them yourself? There’s no sense in hearing about their education from me when A) I’m no longer a teacher. And B) I could just lie and make myself sound better than I actually am."
    tb "It’s not their {i}education{/i} I’m interested in, Akira. I can evaluate that myself. And frankly, I imagine I’m more adept at such a thing than you to begin with."
    tb "What I {i}want{/i} is your opinion on the type of women they’re becoming. If they’re sticking to the right path or-"
    s "If they’re following me down the one {i}I’m{/i} on..."

    scene tsubasatalks9
    with dissolve

    tb "Now, now, Akira. There’s no need to belittle yourself like that. "
    s "I’m just not sure what else you could mean. Without beating around the bush, we both know you’re smart enough to realize that nothing good will come from any of them being around me."
    tb "Again, you seem to misunderstand the way I view your relationships with all of my girls. So I’ll remind you now that {i}my{/i} moral code is somewhat askew as well due to my background."
    s "Is this the part where you slap a bell around your daughter’s neck and see how much I’m willing to bid for her? "
    tb "The wealthiest among us are typically the most frugal, Akira. As such, there’s no need for a bell at all. Touka’s already grazing in your pasture and you’ll always be able to find her there if you just step outside."

    scene tsubasatalks10
    with dissolve

    s "I’m...out of cow-based knowledge and unsure of how to proceed with this dialogue."
    tb "Then I’ll ask you plain and simple."

    scene black
    with dissolve2

    "Tsubasa moves further down an aisle lined with marble and satin and emphasizes the distance between us in every sense of the word."
    "And even though I know I’ll never catch her, I can’t help but chase her down."

    scene tsubasatalks11
    with dissolve2

    "She turns to face me. And despite her inarguable beauty and the passing thought that simply touching her would be akin to fucking the God of Torment once more, I feel stuck."
    "I want to reach out and feel her, but I’m content with the space between us and the way the sunlight reflects off of the manor’s tiled floors. And I don’t want to ruin it."
    "I want to stay here forever, dangling from the strings she holds above my head because I know she can choose better for me than {i}I{/i} ever could."
    "I’ll just never understand why {i}my{/i} strings were the ones she reached for."

    tb "Touka’s seemed a bit...different lately. Would you agree with that, Akira?"
    s "I...haven’t seen her much. I’ve been unconscious for two months, remember?"
    tb "Right, right. And, within that time, she grew rather...{i}grumpy,{/i} to say the least. Why, she’s even raised her voice at me a few times. It was quite shocking. "
    tb "Where do you think that attitude comes from, Akira?"
    s "..."
    tb "My eldest daughter truly {i}has{/i} fallen head over heels for you, hasn't she?"
    s "Nothing’s happened between us, Tsubasa."
    tb "Yes, but is that {i}your{/i} choosing or hers?"
    s "I don’t...see her that way."
    tb "Nonsense. Every man in Kumon-mi would jump at the chance to bed my daughter regardless of her age. Denying your own feelings on the matter would actually be quite offensive."
    s "I mean...yeah. She’s hot. But I’ve found...something else in her."

    scene tsubasatalks12
    with dissolve

    tb "Something else?"
    s "Something...I don’t know. It’s going to sound stupid."
    tb "No, I’m intrigued. Do tell."
    s "Something...comforting. "
    tb "Comforting..."
    tb "As in...matriarchal?"
    s "Yeah...That. "

    scene tsubasatalks13
    with dissolve2

    tb "{i}Hah...{/i}I see."
    s "Does that...disappoint you?"

    scene tsubasatalks14
    with dissolve

    tb "It doesn’t disappoint me. And I can understand where you’re coming from. I’m just surprised to see a man your age admit it. Isn’t your type typically a bit more...{i}proud?{/i}"
    s "Probably. But I’ve reached a point where everything hurts so much that I find little purpose in continuing to hide feelings like that."
    tb "How do you think Touka would feel if she heard you say such a thing?"
    s "Sad. Angry. Compassionate? I don’t know. Touka’s a lot of things and literally all of them are good."
    tb "And Tsukasa?"
    s "What about her?"
    tb "You had your first session with her the other day, didn’t you? {i}Tutoring.{/i}"
    s "Not intentionally. She kind of just showed up and then everything went to shit."

    scene tsubasatalks15
    with dissolve

    tb "{i}Hah...{/i}I was worried about that."
    tb "In fact, I didn’t even know you two had run into one another until Chika informed me. And when I confronted Tsukasa about it, she was unwilling to say anything at all. Likely out of shame, I imagine."
    s "No, Tsukasa didn’t do anything wrong. I was just...not in the right frame of mind that day. It wasn’t her fault."

    scene tsubasatalks16
    with dissolve

    tb "Is...Is that so? You’re not just saying that to keep her out of trouble?"
    s "No. Tsukasa..."
    s "Forgive me for saying this, but Tsukasa’s a brat."
    tb "Oh, I’m well aware."
    s "But she’s very smart. And I can tell she’s been raised well."
    s "And if I was in the position {i}to{/i} be tutoring again, she’d be great. She seems willing to learn and...and easy to teach so long as she doesn’t fire me for looking at her wrong."
    tb "And the reason you’re not in the “position” to tutor is because of your...mental health?"
    s "Right."
    tb "As in...you believe it would be dangerous for my daughter to be in your care? Or you believe {i}you{/i} would be in danger due to caring for my daughter?"
    s "I..."
    s "Uh..."
    s "Both?..."

    scene tsubasatalks17
    with dissolve

    tb "I see."
    tb "I must have scared you when we first spoke about this in my office."
    s "Yeah, well..."
    s "Not as much as I scare myself sometimes."
    tb "Hm..."
    s "..."
    tb "..."
    s "Are...you thinking about something?"
    tb "A few things. But each one seems rather...destructive?"
    s "That’s...not a good word."
    tb "The gist is that I’m not sure how I’m supposed to look at you now."
    s "Meaning?"
    tb "Meaning that it sounds rather {i}fishy{/i} to hear you talk about not wanting to bed my eldest daughter, but not trusting yourself around my youngest."
    s "Can we just...not talk about this anymore?"
    tb "I think we {i}have{/i} to now, don’t we?"
    s "We definitely don’t. And I should probably head home before-"
    tb "Akira."
    s "..."
    tb "..."
    s "What?"
    tb "Oh, nothing."
    tb "I just wanted to say your name again."
    s "..."

    scene tsubasatalks18
    with dissolve

    tb "Akira, Akira, Akira...What an {i}interesting{/i} man you are."
    tb "I wonder how you got here? Apart from the limo, I mean."
    s "It’s probably better if we avoid that topic too."

    scene tsubasatalks19
    with dissolve

    tb "Oh?"
    s "It’s just...bringing up the past isn’t exactly one of my fondest hobbies. And it doesn’t help that most of it is still pretty hazy."
    tb "Yes...age will do that to us, won’t it?"
    s "And misery."
    tb "Are you unhappy, Akira?"
    s "I don’t know how much longer I can do this, Tsubasa."

    scene tsubasatalks20
    with dissolve

    tb "Mm."
    s "I’m glad you’re happy, though. You have an amazing life and two amazing daughters."
    tb "Do you think having such things is enough to make a person happy?"
    s "Is it not?"

    scene tsubasatalks21
    with dissolve

    tb "Sometimes I wonder."
    tb "It takes more than just {i}having{/i} things to make life worth living. But I guess we can leave it at that as I don’t want to make you feel any worse than I’m sure you already do."
    s "Then...I guess this concludes our status report?"

    scene tsubasatalks22
    with dissolve
    stop music fadeout 5.0

    tb "I guess so."
    tb "Please hand me your cell phone."
    s "What?"
    tb "Immediately."
    tb "Or I will have it seized by security."
    s "I don’t-"
    tb "Now, please."
    tb "I don’t have all day."
    s "Tsubasa-"

    scene tsubasatalks23
    with dissolve
    play sound "phonebeep.wav"

    tb "Yoink."
    s "What?..."
    s "Why are you-"
    tb "Shh..."
    tb "Everything will be over soon."
    s "..."
    tb "Oooh. Cute wallpaper."
    tb "You must really love your niece."
    s "What are you doing?..."
    tb "Calling the police, of course."
    tb "I left {i}my{/i} phone in the other room. And you’ve said some very {i}suspicious{/i} things in regard to my darling Tsukasa that I’m not willing to ignore."
    s "But...nothing’s happened..."
    tb "Then you won’t mind your house being searched."
    s "Tsubasa-"

    scene tsubasatalks24
    with dissolve

    tb "I’m {i}kidding.{/i}"
    tb "Here."

    scene tsubasatalks25
    with dissolve

    "Tsubasa hands the phone back to me and-"

    s "..."
    tb "..."

    play sound "winner.mp3"
    $ tsukasanumber = True

    "{i}You have obtained Tsukasa’s phone number!{/i}"

    s "Why?..."
    tb "Who knows? Maybe I’m a bad person after all?"
    s "..."
    tb "What’s wrong? Cat got your tongue?"
    s "I just...I’m so confused..."
    tb "Me too. We’ll see if I regret this later."

    scene tsubasatalks26
    with dissolve

    tb "I read in a self-help book recently that doing {i}impulsive{/i} things like this can lead to an increase in serotonin. Maybe this was a bit {i}too{/i} impulsive, though?"
    s "{i}You think?{/i}"

    scene tsubasatalks27
    with dissolve

    tb "Well, look at it this way — you’ve been hanging around Chinami for how long now? And you’ve never done anything {i}impure{/i} to her, have you?"
    s "Well...no. But-"
    tb "Then there’s clearly a part of you that knows how wrong it is and that part of you is {i}winning.{/i} Just look at this as a...test."
    s "This isn’t a test I want to take, Tsubasa."
    tb "We all have to do things we don’t want sometimes, Akira."
    s "You don’t. Touka doesn’t. Tsukasa doesn’t."
    tb "All {i}I’m{/i} hearing is that your life would be smooth sailing if you married one of my daughters and joined the family. And look, I’ve now made it easier than ever for you to do that."
    s "You’re putting way too much trust in me."
    tb "Who says I’m putting {i}any{/i} trust in you at all? Maybe I’m just...cutting off a few of your strings so you don’t confuse yourself as my puppet anymore."
    s "..."

    scene tsubasatalks28
    with dissolve

    tb "Aaaaanyway, I need to review some recent acquisitions before a call this afternoon. But you’re free to continue exploring the grounds if you like."

    scene tsubasatalks29
    with dissolve

    tb "There’s a good chance you might find Touka in the pool. But I’m worried her poor, maidenly heart wouldn’t be able to take another instance of her beloved Sensei seeing her as a {i}matriarch.{/i}"
    s "..."
    tb "Until next time, Akira."

    scene black
    with dissolve2

    tb "I’m hoping for a very interesting status report."

    "I leave the manor."

    scene bedroom_night
    with dissolve2

    "I turn my phone off."

    scene black
    play sound "tackle.mp3"

    $ renpy.end_replay()
    $ tsubasaspring1 = True
    $ tsubasa_love += 1

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
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

label tsubasaspring2:
    if _in_replay:
        play music "calmbar.mp3"

    scene tsubasaentersbar1
    with fade

    tb "Hmm...am I in the right place? There don’t be appear to be any customers."
    sar "{i}Mmph!!?! Wrclsd!!!{/i}"
    s "{i}Be quiet. We haven’t been caught-{/i}"

    scene tsubasaentersbar2
    with dissolve

    tb "Oh, Akira. What are you doing here?"

    play sound "static.mp3"
    scene tsubasaentersbar3 with flash
    stop sound

    sar "{i}Aghkrrra?! Isstyrnmm?!{/i}"

    play sound "static.mp3"
    scene tsubasaentersbar4 with flash
    stop sound

    s "I work here now."
    tb "Oh, is that so? I’d assumed your leave from teaching at Kumon-mi High would only be temporary, but perhaps I was wrong if you’ve already sought new employment."
    s "Yup. I’ve always wanted to be a bartender."

    play sound "static.mp3"
    scene tsubasaentersbar5 with flash
    stop sound

    sar "{i}Who is that?! Is that the rich lady?! What’s she doing here?! What do I do?!{/i}"
    s "{i}Stop asking questions you already know the answer to.{/i}"
    sar "{i}I figured out the first answer on my own! It’s the second one I’m struggling with!{/i}"
    s "{i}I don’t care what you do, just stop making noise.{/i}"
    tb "Are you...talking to yourself?"

    play sound "static.mp3"
    scene tsubasaentersbar6 with flash
    stop sound

    s "Life has been hard. I’m experiencing daily mental lapses due to recent traumatic events. Some of which involve talking to myself."
    tb "Oh dear. Perhaps you should see a doctor, then? I wouldn’t mind referring you to my family’s psychologist. I actually have a meeting with her and that Yasu girl next week."
    tb "If you’re okay with it, I could put in a good word for-"
    s "Nope. I have a therapist already."
    tb "You do? Who is it?"
    s "I believe that’s confidential, Tsubasa."
    tb "I was under the impression that was merely on the doctor’s behalf?"
    s "Normally, yes. But mine is-"
    sar "{i}Ahmf~{/i}"

    scene tsubasaentersbar7
    with dissolve

    s "Gh..."
    tb "Gh?..."
    s "...Great at his job. And not accepting new patients at the moment."

    "Sara, instead of remaining still, goes back to sucking me off because of course she does."
    "Which isn’t to say I oppose it. I had a feeling this was going to happen the moment I told her to stop making noise instead of keeping her mouth shut. But hey, challenge is my middle name."

    tb "Are you sure it’s just a mental issue? Because, I’m no medical professional, but you appear to be showing signs of physical distress as well."
    s "Inner battle. Hard to fight. What can I get you?"
    tb "Just a glass of wine, please. "

    scene tsubasaentersbar8
    with dissolve

    sar "{i}Ahn...ahm...mlm...{/i}"
    s "..."
    tb "Is there...a step I’m missing when it comes to ordering? I don’t typically patronize establishments such as this and am used to simply being given what I ask for."
    s "We’re all out of alcohol. "
    tb "Then, is there a dinner menu I could peruse?"
    s "No. We’re out of everything. And also we are closed."

    play sound "static.mp3"
    scene tsubasaentersbar9 with flash
    stop sound

    sar "{i}Nngh! Nlgh! Mmlgh! Mmfh!{/i}"
    tb "Oh, I’m terribly sorry. I had no idea. I never would have come if I had known."
    s "It’s fine. Guess that means you’ll be leaving now, though. Goodnight, Tsubasa. Thanks for stopping by."

    play sound "static.mp3"
    scene tsubasaentersbar10 with flash
    stop sound

    tb "Now, don’t get so hasty. The bar may be closed, but that doesn’t mean you and I can’t still spend some quality time together, does it?"
    s "It kind of does. Sorry."
    tb "Why is that? Is there someone else working right now? Or is this more of you just being {i}intimidated{/i} by the prospect of being alone with me?"
    s "In my defense...you are a very intimidating woman."

    scene tsubasaentersbar11
    with dissolve

    tb "I suppose I can be. But I was hoping to be able to...turn that aspect of my personality off tonight with a quiet night at the bar as I’ve been meaning to revisit this place for what seems like {i}aeons{/i} now."
    tb "Tell me- are they still hosting those silly school events here? The ones where all of the girls get together to fight over you?"
    s "They- {i}we{/i} host a lot of things here. It’s a good way to...drive sales."
    sar "{i}Mm...mnngh.....mmm~!{/i}"

    scene tsubasaentersbar12
    with dissolve

    tb "As a {i}man,{/i} though — do you not mind being treated as a...prize of sorts? Especially when there are girls like Chika who are {i}more{/i} than willing to-"
    s "Let’s...not talk about Chika tonight."
    tb "Have your feelings for her dwindled now that my daughter is-"
    s "Actually, let’s not talk about anyone. I got a job here to escape all of my...school-based relationships. If I wanted to get further involved in them, I’d just go back to teaching."

    scene tsubasaentersbar13
    with dissolve

    tb "..."
    sar "{i}Ahm...ahmm...aaahm~{/i}"
    s "{i}Ahem...{/i}So...what’s new?"
    tb "What’s new is you’re acting rather strange tonight, Akira. It’s uncommon for one to {i}not{/i} want to talk about their...{i}hobbies.{/i}"

    play sound "static.mp3"
    scene tsubasaentersbar14 with flash
    stop sound

    s "No it’s not. I need to keep a level head at work or I’ll be let go."
    tb "Oh, darling. I doubt that’s true at all. In fact, I’m hard-pressed to believe you’d be hired as anything other than eye candy to begin with as you have little to no experience in customer service."
    s "I was hired...to tend the bar...I am a bartender..."

    play sound "static.mp3"
    scene tsubasaentersbar9 with flash
    stop sound

    tb "Who just {i}happens{/i} to be a handsome man in a city full of {i}unsatisfied{/i} women. This is clearly a marketing move, Akira. And {i}I{/i} know marketing, so you can trust me."
    tb "I’ll admit, it’s an excellent business decision on behalf of the manager here. I can’t say I wouldn’t do the same if I had my hands in such a field."
    sar "{i}Mm! Mm! Mhhm!{/i}"
    tb "I suppose it’s only a matter of time, though. I- wait. Did you hear that just now?"

    play sound "static.mp3"
    scene tsubasaentersbar15 with flash
    stop sound

    tb "There aren’t any...mice in this bar, are there? I’ve heard that such creatures exist in...{i}dirtier{/i} places. But all I know about them is their high-pitched noises and-"
    s "Nope. No mice. No anything. Just me and you. And- ngh!"

    scene tsubasaentersbar16
    with dissolve

    tb "There it is again, Akira. You should {i}really{/i} see someone if you’re experiencing such constant, agonizing pain."

    play sound "static.mp3"
    scene tsubasaentersbar14 with flash
    stop sound

    s "Mhm...I’ll get right on that."
    sar "{i}Aaaahn....aaahn...aaahn!~{/i}"
    tb "There it is again! It sounds as if it’s coming from behind the bar. Are you sure you don’t see anything?"
    s "Nope. Nothing at all."

    play sound "static.mp3"
    scene tsubasaentersbar17 with flash
    stop sound

    tb "You’re hiding something from me."
    s "That’s impossible and you know it. You have access to an endless library of information on anyone you want and-"
    tb "I appreciate the flattery and acknowledgment of my vast network of connections and knowledge, but I’m going to have to ask you to step away from the bar, Akira. Now."

    play sound "static.mp3"
    scene tsubasaentersbar4 with flash
    stop sound

    s "No."

    play sound "static.mp3"
    scene tsubasaentersbar18 with flash
    stop sound

    sar "{i}Mlggh?!?{/i}"
    tb "No?"

    play sound "static.mp3"
    scene tsubasaentersbar4 with flash
    stop sound

    s "Okay, I’ll tell you the truth. I don’t actually work here. I have a condition that prevents me from letting go of the counter for the rest of my life or I will immediately-"
    tb "Alright, I’ve heard enough. Step aside."
    s "Tsubasa, wait-"

    play sound "static.mp3"
    scene tsubasaentersbar19 with flash
    stop sound

    tb "Oh, dear God!"
    sar "Uhh...h...hey! Welcome to Sakaki-bar-a!"
    tb "Have you been...down there the entire time?"
    sar "M...Maybe?"
    s "This is also part of my condition. Sara is simply alleviating the chronic pain brought on by-"

    scene tsubasaentersbar20
    with dissolve

    tb "Akira — do you have {i}any{/i} idea how disrespectful it is to hold a conversation with someone while having {i}fellatio{/i} performed on you by some {i}peasant?{/i}"
    s "Uhh...very?"

    scene tsubasaentersbar21
    with dissolve

    tb "Not really, to be honest. It’s actually a relatively common demonstration of power and status. "
    sar "Peasant?"

    scene tsubasaentersbar22
    with dissolve

    tb "But still!"
    s "I thought the door was locked, okay? You would have been suspicious if Sara just popped out from behind the counter while you were looking at me."
    tb "You could have simply said she was restocking items or something of the like!"

    scene tsubasaentersbar23
    with dissolve

    s "Oh, shit. You’re right. I guess I just didn’t think of that."
    tb "Well, let this be a lesson for next time then. Not all customers would be as...forgiving as I am."

    if harukaspring2 == True:
        "Sorry, Haruka."

    sar "I guess...we’ve all learned a valuable lesson today, then! No more blowjobs behind the bar! "

    scene tsubasaentersbar24
    with dissolve

    tb "Well, {i}surely{/i} you’re not just going to {i}leave{/i} him like that, are you?"
    sar "Uhh...what?"
    tb "Go on. Pick up where you left off. Leaving a job like this incomplete is unbecoming in numerous ways. Which isn’t even mentioning the negative effects it could have on his health."
    sar "You want me to...keep going?"
    tb "For {i}his{/i} sake, of course. Not mine."
    sar "And...you’re just going to...stand there and watch?"

    scene tsubasaentersbar25
    with dissolve

    tb "Well...we just happen to be in the same place, so...I suppose it wouldn’t hurt."
    sar "..."
    s "..."

    scene tsubasaentersbar24
    with dissolve

    tb "I {i}would{/i} appreciate a glass of wine, though. If you’re not truly sold out, that is."

    scene black
    with dissolve2

    sar "Um..."
    sar "C...Coming right up?..."

    "........."
    "......"
    "..."

    scene tsubasaentersbar26
    with dissolve2

    tb "...and so I say to the gardener, “Not the macrophyllas, the {i}sargentianas!{/i}” I swear, good help is so hard to come across these days."
    sar "Whssasrgntna???"

    scene tsubasaentersbar27
    with dissolve

    tb "Oh, apologies. It’s a strain of hydrangeaceae native to China, while macrophylla is native to Japan. I always forgot I’m supposed to explain my jokes to people like you."
    sar "Ppllkme?"
    s "Would it kill you to not look down on “peasants” directly to their faces, Tsubasa?"
    tb "Why, I wouldn’t be able to see her if I didn’t do that. How would I be able to tell that she’s doing a good job?"

    scene tsubasaentersbar28
    with dissolve

    s "Would my word not suffice?"
    tb "Of course not, darling. Actions speak louder than words ever can. And from what I’ve seen, she’s yet to...{i}finish the job{/i} even once. Perhaps I should direct her?"
    s "You’re doing fine, Sara. Keep it up."
    sar "Shsrghtyknow...Yrllyhvntcmyet...Hwcm?? Dyyuntacshlklylkoldrgrls??"
    s "The only reason I haven’t finished yet is because Tsubasa scares me."
    tb "I already told you, Akira — I don’t {i}want{/i} to be intimidating tonight. There’s a time and a place for that and- well. Actually...now {i}would{/i} be a good time for that."

    scene tsubasaentersbar29
    with dissolve

    tb "But I can be nice too! Look, I’ll even pet her."
    sar "Mm! Thnkyou rchldy!"
    s "You’re actually enjoying this, Sara?"
    sar "Mhm! Cminmymth!"
    tb "Good girl!"
    tb "{i}See?{/i} If she’s not intimidated, why should {i}you{/i} be? Just do your job and let it all out, Akira. You wouldn’t want all of her hard work to go to waste, would you?"
    sar "Mmh! Mmngh! Mlmh!"
    tb "{i}Deeper.{/i}"

    scene tsubasaentersbar30
    with fade

    sar "Mmh! Mmnglkl!"
    tb "Yes...just like that. I bet he {i}loves{/i} it when you push past your limits. Don’t you, Akira?"

    "Tsubasa tenderly runs her fingers through Sara’s hair, gently pushing her forward and adding another inch or two of my cock into her mouth."

    tb "{i}Don’t you,{/i} Akira?..."

    "Okay. I was planning on narrating more, but Tsubasa seems to want my attention."

    s "I...do...yeah..."
    tb "Mm...how nice it must be to...{i}feel{/i} one another in such a way. I’m sooo...{i}jealous.{/i}"
    sar "Mm! Mmhm....mlmlm....[saramaster]..."

    scene tsubasaentersbar31
    with dissolve

    tb "Is this a cabernet sauvignon or a petite sirah? Perhaps a...cabernet franc? I can’t quite tell by the color, and the taste is barely palatable so I’m not sure the vintner would know either. "
    tb "Perhaps it’s just a bad batch? Surely even you people wouldn’t stand for something of {i}this{/i} quality, would you?"
    sar "Mm! Mmlgh! Cmfrme...cmfrme!"
    tb "I believe she would like you to ejaculate now, Akira."
    s "Wow, what gave you that idea?"

    scene tsubasaentersbar32
    with dissolve

    tb "Ooh, how {i}saucy{/i} of you. Does having your cock down the throat of a beautiful woman restore the confidence you lack every {i}other{/i} minute of every day?"
    s "Does talking down on her while she’s sucking me off turn you on?"
    tb "Would I have stuck around and watched if it didn’t?"
    s "Why not get on the ground and help her then?"
    sar "Mm?"
    tb "And risk dirtying my stockings? I’m afraid I’ll have to pass."
    s "Guess being married isn’t the barrier I thought it was if that’s the first thing you can come up with."

    scene tsubasaentersbar33
    with dissolve

    tb "Saucy again. I could make a habit of this. How generous of you to provide me with {i}so many{/i} opportunities to do just that."
    sar "Mm?...Whsstsppsdtmnn?"

    scene tsubasaentersbar30
    with dissolve

    tb "Nothing, dear. Now be a good little girl and focus, okay? You want your reward, don’t you? You want this big, strong man to cum in your little mouth?"
    sar "Mm! Mmhm! Mmm!~"
    tb "Yes, darling..."
    tb "Just.....{i}like.....{/i}that......"

    scene tsubasaentersbar34
    with fade

    sar "Mm! Mm! Mm! [saramaster]! Mmm!"

    "Sara works harder at the behest of Tsubasa, and {i}Tsubasa{/i} goes right back to petting Sara on the head like she’s some sort of domesticated animal."
    "And I’m sure that to a certain extent, she is. It’s probably easy to see everyone as playthings when the world is your sandbox. "
    "But just because you own the playground doesn’t mean you won’t get jealous if someone who {i}doesn’t{/i} starts playing with your toys."

    scene tsubasaentersbar35
    with dissolve

    tb "Cum."
    s "I get that it’s probably been a while for you, but that’s not really how it works."
    tb "Well, make it work. Because for every minute you take from here on out, I’ll reveal one of your {i}deepest...{/i}darkest secrets..."
    sar "Mm! Mm! Mmmmmh!"
    s "Tsubasa..."
    tb "{i}Akira...{/i}"
    sar "S...Sn...sei!..."

    with sexfade
    with sexfade
    scene tsubasaentersbar36 with cumflash
    with hpunch

    sar "Mmnghrlrlr?!?!"
    tb "Ah! Excellent work. He just needed to be threatened first."

    scene black
    with dissolve2
    stop music fadeout 13.0

    sar "{i}Paah...{/i}whew...my jaw hurts."
    s "That...threatening thing was just a coincidence."
    tb "The most wonderful things normally are, Akira..."
    s "What do you-"
    tb "Sorry, {i}Sara{/i} was it? Could you point me in the direction of the wine cellar? I’d like to take a look around while the two of you...{i}clean up.{/i}"
    sar "Uhh...well, it’s not really a cellar. It’s kind of just a basement. And there are a lot of spiders down there right now, so-"
    tb "Ah. That explains everything. "
    tb "No worries, then. I’ll just wait on the couch. Could I offer the two of you a ride home once you’re done? My driver should still be waiting outside."
    sar "Oh, I actually live here. My apartment’s upstairs, so I don’t need a ride."
    tb "Ahh. {i}That explains even more.{/i} Akira?"
    s "I’m good, Tsubasa."
    tb "No, no. I insist. Please, allow me to give you a ride. It’s the least I can do in exchange for the show you two put on tonight."
    sar "Come back next week for more of the same thing! Just lock the door behind you next time."
    s "No, what? Tsubasa-"
    tb "{i}I insist.{/i}"
    s "..."
    sar "Just go, I can clean up here. It’s getting late anyway."
    s "But-"
    sar "{i}Go! And try to get her to invest in the bar while you’re at it!{/i}"
    tb "Ah- you two are whispering again. "
    tb "It better not be about {i}me...{/i}"

    $ renpy.end_replay()
    $ tsubasaspring2 = True
    $ tsubasa_love += 1
    $ sara_love += 1
    $ sara_lust += 1

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "{i}Sara’s lust has increased to [sara_lust]!{/i}"
    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump tsubasaspring3

label tsubasaspring3:
    scene clearnightsky
    with dissolve2
    play music "contemplation.mp3"

    "A familiar man opens the door to a familiar limousine and I crawl into the back next to Tsubasa."
    "And while I’m no stranger to immediately departing the residence of a woman after ejaculating into her mouth, it’s not exactly common for the red carpet to be rolled out for my walk of shame."
    "This, combined with the fact that I’m now quite literally trapped in the back of a moving vehicle with the closest thing I know to a super-villain, is a bit disconcerting to say the least."
    "I doubt this car will be driving off a cliff anytime soon, though. Not with precious cargo tucked safely into the backseat."
    "But should that precious cargo need to lighten the load, I’m sure I’ll be the first to go. "
    "I just hope these hands of stone will be enough to protect the wooden heart I hide behind my glass ribs once I’m forced to dance with the pavement at roughly fifty miles per hour."

    tb "You’re not always this {i}nervous{/i} in moving cars...are you, Akira? Can I assume that you’re once again seeing me as something far more {i}scary{/i} than I truly am?"

    scene tsubasalimo1x
    with dissolve2

    s "I’m always this nervous. So I’m sorry, but you won’t be able to take the credit for my mannerisms this time. "
    s "At least not all of it. You’re definitely adding to everything, though."
    tb "If it helps to dispel your worries, I can assure you Ishimoto is an excellent driver. He’s been chauffeuring me for many years now. You’re in the best of hands, I promise."
    s "I believe you. The present can’t change the past, though."
    tb "It can change the way you perceive it. "
    tb "We all look differently when we’re hit by the light in certain ways. "
    tb "For example, you look much more handsome now than you did under that drab bar’s red glow. I suppose it helps that you’re not currently being fellated, though."
    s "You literally watched the entire time."
    tb "I looked away on several occasions. Never for long. But I won’t sit here and let you blame me for being once more entranced by just how many women you’re willing to conquer."
    s "Aren’t you the same girl who told me she’s {i}used{/i} to watching women being sold off like cattle?"
    tb "I am. But I can’t say I have much experience with...{i}farmers,{/i} so to speak."
    s "I wasn’t just {i}conquering{/i} Sara. I genuinely care about her. "
    tb "Do you genuinely care about me?"
    s "Not really."

    scene tsubasalimo2x
    with dissolve

    tb "Hahah! Not {i}yet,{/i} you mean."

    scene tsubasalimo3x
    with dissolve2

    tb "We simply just haven’t had enough time to get to know one another yet."
    s "{i}You’re{/i} the mystery here. I’m convinced you know practically all there is to know about me now that you have my full name."
    tb "Have I not already told you a great deal about myself? We’ve gone over my family’s history...how I came to be involved with the Tsukioka family...you even know where I went to high school."
    tb "What more would you like to inquire about?"
    s "What you want with me."
    tb "I’ve told you that on several occasions as well. You’re an...{i}asset.{/i} But you’re also a {i}friend.{/i}"
    s "It doesn’t always feel that way, though."

    scene tsubasalimo4x
    with dissolve

    tb "Yes, well..."
    tb "I have to maintain a certain...{i}distance,{/i} you see. "
    tb "If we become {i}too{/i} friendly, someone may notice. And I have a reputation to uphold."
    s "I believed that right up until you started stroking Sara’s hair while she was {i}fellating{/i} me."
    tb "I’m speaking primarily about what goes on within the manor. You know that the vast majority of my time is spent within its grounds, Akira."
    tb "The world outside of my walls is hardly even {i}real{/i} as far as I’m concerned."
    s "Yeah, I kind of figured that’s why you showed no qualms when it came to subtly belittling Sara in her own business."

    scene tsubasalimo5x
    with dissolve

    tb "You really {i}do{/i} care about her, don’t you? You seem awfully offended by some of my dialogue choices tonight."
    s "She has feelings, Tsubasa."
    tb "And you think a few measly jabs at her status put her in greater jeopardy than the fact that you’re on the brink of leading {i}two{/i} teenage girls into a debauched life of sex disguised as love?"
    tb "If it {i}is{/i} only two, of course. You could be involved with your entire class for all I know."
    s "I imagine you already {i}would{/i} know."
    tb "Perhaps I do and I’m just keeping it a secret until I encounter you with {i}them{/i} next. Regardless, you stand to hurt her far more than {i}I{/i} ever could. "
    tb "So maybe it would be wise to not treat {i}me{/i} like the bad guy when you’re the one traipsing all over Kumon-mi, sowing seeds of destruction in every single place you roam."
    s "..."
    tb "What’s wrong, Aki-kun? {i}Cat got your tongue?{/i}"
    s "Never call me that again. Do you understand?"
    tb "No. Could you say it a little louder, please? Maybe grab my shoulders and shake me around a bit?"
    s "And have your driver pull over and beat me to death? Pass. Just...don’t call me that. Please."

    scene tsubasalimo1x
    with dissolve

    tb "You really are interesting, Akira. You remind me a lot of an old friend when you get {i}passionate{/i} like that."
    s "It’s not passion. It’s anger and resentment and fear and sadness and-"
    tb "And all of those things can combine to form {i}passion{/i} under the right circumstances. It’s like I said before. Everything changes with the light. Neither you nor I are exceptions to that."

    "Tsubasa reaches forward, tracing circles around my knee with the tip of her index finger. But there doesn’t seem to be any...{i}intent{/i} to it."
    "In fact, I’m not even sure if she’s {i}aware{/i} she’s doing it. I imagine she is as it’s hard for me to think {i}anything{/i} she does isn’t cleverly calculated, but still."
    "It makes me comfortable and scared at the same time. But I can’t figure out how to make those things combine. Which makes what she said just seconds ago even harder to understand."

    s "Tsubasa...what do you think you’d be doing right now if you never met me?"
    tb "Why, sipping some of the poorest wine that’s ever touched my tongue, of course. "
    s "Not just tonight, but...in general."
    s "Both of your daughters were struggling to learn how the “outside world” functioned or whatever. And {i}you{/i} didn’t have anyone’s backstory to start prying open as your newest hobby."
    s "If we never crossed paths at that onsen however many years ago it was, everything would be different right now."

    scene tsubasalimo6x
    with dissolve

    tb "Is that really what you believe?"
    s "I mean...yeah. That was the catalyst that ultimately brought Touka into my life. And without Touka, we’d have no reason to see each other {i}at all.{/i}"
    tb "I suppose we wouldn’t, would we?"
    tb "But I’m not sure it would even matter, if you’d like my honest opinion."
    tb "Fate has a funny way of forcing things together. And I truly believe that our paths were meant to cross one way or the other."
    s "And why is that? Because you’re not important to me and {i}I’m{/i} not important to you. What would fate have to do with any of this?"
    tb "..."
    s "...Tsubasa?"
    tb "Forgive me, Akira. I’ve said too much. So I’m going to go ahead and drop this subject now."
    s "...What?"

    scene tsubasalimo7x
    with dissolve

    tb "But as a consolation prize, I’ll allow {i}you{/i} to choose our next conversation topic."
    s "I’d like to talk more about fate please."
    tb "Ha ha. Very funny. But no. I was thinking something more...fun. Personal, even."
    s "Sure. But be aware that you’ll have to do all of the heavy lifting since I’m not good at talking about that kind of stuff."
    tb "That’s fine. I probably know it all already anyway."
    s "Ha ha. Very funny."

    scene tsubasalimo5x
    with dissolve

    tb "Any suggestions? Things you’ve been {i}dying{/i} to know more about? My three sizes? My...{i}ideal{/i} partner?"
    s "Careful, Tsubasa. Ishimoto might relay anything you say about your {i}ideal partner{/i} to your husband."

    scene tsubasalimo8x
    with dissolve

    tb "Ishimoto will do nothing of the sort as he understands he’d be castrated for it. Isn’t that correct, Ishimoto?"
    limo "Of course, madam. Your word is law."
    tb "Ahh, how I love being rich."
    s "Well, at the risk of finding out your ideal partner would be anything or anyone other than me, how about this-"

    scene tsubasalimo9x
    with dissolve

    s "What’s the craziest thing you’ve ever done?"
    tb "The craziest thing I’ve ever done?"
    tb "I suppose it would have to be giving you my youngest daughter’s phone number. That could have gone south in many ways. But you’ve yet to disappoint me in response, Akira. I’m proud."
    s "I meant sexually."
    tb "{i}Sexually?{/i}"
    s "If you’re going to encroach on my sex life and watch my friends go down on me, the least you can do is give me something to hold over you as well."
    tb "I don’t intend to {i}hold anything over{/i} you, Akira. I was merely enjoying a little show. Besides, isn’t it rather {i}daring{/i} to ask a woman of my caliber about her sexual history?"
    s "You said I could choose. This is what I’m choosing. It’s either this or we go back to talking about fate and how you’re, once again, weirdly hiding seemingly relevant information from me."

    scene tsubasalimo10x
    with dissolve

    tb "The craziest thing I’ve ever done?"
    tb "Has there even been anything like that?"
    s "I hope. A life of nothing but consensual sex in the missionary position with your husband sounds extremely boring and unfulfilling."
    tb "And I can confirm that it is."

    play sound "static.mp3"
    scene tsubasalimo11x with flash
    stop sound

    tb "Though, there was that one time when I had intercourse with four members of the massage staff at once."

    play sound "static.mp3"
    scene tsubasalimo10x with flash
    stop sound

    s "Sorry. Did I hear that correctly just now?"

    scene tsubasalimo9x
    with dissolve

    tb "I’m not sure. What did you hear?"
    s "That you had sex with four guys at once?"
    tb "Oh, yes. The night before I was married. It’s a family tradition."
    s "To get fucked by four guys at once the night before your wedding???"
    tb "Why do you sound so perplexed by this extremely common ritual?"
    s "Because that’s not a common ritual at all?? And it paints you in a completely different light now that I know you’re getting gang-banged by masseurs."
    tb "Well, how many men do lower and middle class women typically bed before the night of their wedding?"
    s "Probably none? Maybe their fiancée?"
    tb "Well, {i}that{/i} sounds rather boring too, doesn’t it?"

    scene tsubasalimo12x
    with dissolve

    tb "Besides, I’m not being {i}gang-banged{/i} by anyone. At least not on a consistent basis. That was decades ago. "
    tb "And while there’s still a full staff of therapists on call at Tsukioka Manor, none of them would {i}dare{/i} touch me in such a way even if I {i}commanded{/i} them to. Trust me, I’ve tried."
    s "Then how are you-"

    scene tsubasalimo13x
    with dissolve

    tb "I’m not. It’s as simple as that."
    tb "I have little time for such {i}pleasures{/i} anymore in the first place. So please forgive me if I...{i}crossed any lines{/i} tonight."
    tb "It was nice living vicariously through someone else for a change. I don’t often want to do that."

    if chikalust25 == True:
        tb "I’ll admit that watching you dominate Chika was far more pleasurable, though. The taboo factor added a layer of depravity that, while initially shameful, was quite invigorating in hindsight."

    s "So you and your husband just..."

    scene tsubasalimo14x
    with dissolve

    tb "I see {i}you{/i} more than him at this point. He and I don’t even sleep in the same room anymore."
    s "Why not?"
    tb "That’s just the way things worked out, I suppose."
    tb "And apart from him and the massage staff, I barely have {i}any{/i} experience with anyone at all."

    play sound "static.mp3"
    scene tsubasalimo15x with flash
    stop sound

    tb "Though, there was that one time when my friends and I ran off to the urban district and I had intercourse with four men I’d met at a party."

    play sound "static.mp3"
    scene tsubasalimo16x with flash
    stop sound

    s "Jesus Christ, Tsubasa."
    tb "No, I don’t think he was there. I may be old, but I’m not {i}that{/i} old."
    s "Why is it always four?"
    tb "Because once you start adding more than that, no one knows what to do."
    s "So what I’m learning is you have a {i}ton{/i} of experience and you’re just once again tricking me into looking at you in a certain light."
    tb "Perhaps. But by that logic, wouldn’t you say it’s possible neither of those...what do you call them — orgies — happened at all, is it not?"
    s "I...guess? But why would you {i}want{/i} me to think you’re experienced when you’re not?"

    scene tsubasalimo3x
    with dissolve

    tb "Why indeed?"
    s "I really hate when you answer questions by just...questioning the question. It’s impossible to learn anything that way."
    tb "That’s the point, Akira."
    limo "Madam, we’ll be arriving at Master Arakawa’s residence in approximately one minute. If you have yet to finish conversing, I can circle the area or-"
    tb "No, you may proceed to the destination. {i}Master Arakawa{/i} and I are done here."
    s "We are? Because it sounded like things were finally getting good. I’m actually not intimidated for once."
    tb "Are you coming onto me, Akira?"

    "Her fingers stops tracing circles on my knee. It slides further up my leg instead."

    tb "I’m a married woman, you know...and based on the girls I’ve seen you with, I think it’s safe to say I’m...{i}not your type.{/i}"

    "I grab her wrist. She doesn’t flinch."

    stop music fadeout 15.0

    s "I’m not afraid of you, Tsubasa."
    tb "Not {i}anymore,{/i} you’re not..."
    tb "But that’s because I spoon-fed you certain details that shattered the illusion."
    s "That...wait, what?"
    tb "It’s rather funny how quickly a powerful woman can be seen as {i}weak{/i} once certain...details come out."
    tb "All it took for you to change the way you look at me was a little bit of lust and some seductive whispers — tall tales of times that I’ve been vulnerable. "
    tb "Why is it that being swallowed up by the pleasures of the flesh make {i}you{/i} seem stronger — but {i}me{/i} seem weak?"
    s "..."
    tb "I’m as scary as I’ve always been. You’re just easy to manipulate."
    s "Uhh...so, wait. None of that ever happened? I’m confused."
    tb "It all changes with the light, Akira."

    scene black
    with dissolve2

    tb "Sometimes, the things you see aren’t really there."
    tb "And other times, there’s something you can’t help but miss."
    limo "Madam, we’ve arrived."
    tb "Maybe it’s because you’re distracted...maybe you just don’t {i}want{/i} to see it..."
    tb "But you can never know what’s real until you {i}experience{/i} it."

    play sound "slap.mp3"

    "She swats my hand away and leans back in her seat."

    tb "And some things are harder to experience than they look."

    "The driver opens my door and steps to the side."

    tb "Goodnight, Akira."
    tb "It’s been a...{i}pleasure.{/i}"

    "She winks at me once more."
    "The door to the limo closes."

    scene bedroom_night
    with dissolve2

    "And I go back to my room."

    s "..."
    s "..."
    s "..."

    scene black
    play sound "tackle.mp3"

    "I don’t think I’ll ever understand her."

    $ renpy.end_replay()
    $ tsubasaspring3 = True
    $ tsubasa_love += 1

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
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

label christmastsubasa1:
    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick1 with flash
    stop sound

    mo "Ah..."
    s "Tsubasa? When did you-"

    scene tsubasadoesntwantxmasdick2
    with dissolve

    tb "You, out."

    scene tsubasadoesntwantxmasdick3
    with dissolve

    tb "You, stay."

    scene tsubasadoesntwantxmasdick4
    with dissolve

    mo "F...For the record! I consented to everything! In fact, it was {i}my{/i} idea to-"
    tb "I said {i}out.{/i} Now. Or your father will be hearing about this."

    scene tsubasadoesntwantxmasdick5
    with dissolve

    mo "Mm..."
    mo "I’m sorry, Sir..."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    "Molly picks herself up off of whatever the fancy rich-person name for the dresser thing is and leaves."

    play sound "lock.mp3"

    "Tsubasa locks the door again."
    "Not like it ever matters."

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick6 with flash
    stop sound

    $ renpy.pause(3, hard=True)
    scene tsubasadoesntwantxmasdick7
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene tsubasadoesntwantxmasdick6
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene tsubasadoesntwantxmasdick8
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene tsubasadoesntwantxmasdick6
    with dissolve2
    $ renpy.pause(3, hard=True)
    play music "chopmonk.mp3"
    scene tsubasadoesntwantxmasdick9
    with dissolve

    tb "{i}Hah...{/i}"
    tb "Akira, Akira, Akira..."
    tb "I’m beginning to think you have a problem."
    s "I do. I can’t have sex {i}at all{/i} without someone interrupting me anymore. It’s becoming extremely inconvenient."

    scene tsubasadoesntwantxmasdick10
    with dissolve

    tb "Oh, {i}I’m{/i} sorry. Do you think you’re in the position to be making jokes right now?"
    s "Am...Am I actually in trouble this time?"
    tb "Of course you’re in trouble. This is my serious face. Can you not tell?"
    s "It looks just like all of your other faces."
    tb "Maybe that’s because I’m always being serious?"
    s "I’ll, uhh..."
    s "I guess I’ll be going now."
    tb "No you won’t."
    s "But-"
    tb "Do you know what day it is, Akira?"
    s "Uhh...C...Christmas?"
    tb "That is correct. And do you remember what I told you I was doing on Christmas?"
    s "H...Having a meeting?"

    scene tsubasadoesntwantxmasdick11
    with dissolve

    tb "Right! I’m having a meeting."
    tb "Or at least I’m {i}supposed{/i} to be having a meeting. But {i}instead,{/i} I have to go out of my way to make sure an adult man knows to not {i}fuck high schoolers in my bathroom.{/i}"
    tb "Do you think I am happy about that, Akira?"

    scene tsubasadoesntwantxmasdick12
    with dissolve

    s "Probably...not..."
    tb "{i}Very{/i} good! But I’m a little confused. Didn’t I give you a {i}job{/i} to do today?"
    s "I was supposed to watch Tsukasa..."
    tb "But {i}of course{/i} you didn’t want to force her to watch you having sex with a young girl, so you left her behind. Correct?"
    s "Uhh...she kind of just...left on her own."
    tb "So you {i}would{/i} have forced her to watch then."
    s "No, just-"
    tb "The fact of the matter is, Akira- she is not here right now. And she needs to {i}be{/i} here right now, because {i}I{/i} have very important things to do."
    tb "Things that Tsukasa will only {i}get in the way of.{/i} Because {i}that{/i} is what she does. And {i}now,{/i} she’s probably wandering around, getting into trouble and putting {i}everything{/i} at risk."
    tb "All because {i}you{/i} can not keep it in your pants for, excuse the language, one {i}fucking{/i} second."
    s "Well, uhh...I think a good place to start would be putting my pants on {i}now,{/i} so-"

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick13 with flash
    stop sound

    tb "No."
    s "...No?"
    tb "That’s right. You’re going to stand there and think about what you’ve done. "
    s "And what are {i}you{/i} going to do?"
    tb "Why, I’m going to stand here too. I’m sure my associates won’t mind the fact that I had to go take care of a 31-year old {i}issue{/i} at all. "
    s "How did you even know? This house goes on forever and I figured you were busy-"
    tb "Because, {i}Akira,{/i}  I know everything that goes on in this house. Which is why I {i}also{/i} know you had your way with Chika in one of Touka’s bedrooms earlier today."

    if chikalust25 == True:
        tb "{i}Again.{/i}"
        tb "What animal was she dressed up as this time?"
        s "A...regular girl..."
        tb "A {i}regular girl.{/i} How funny. My, I can’t help but laugh."

    else:
        s "In my defense, I tried to have sex with some {i}other{/i} girl. Chika just intercepted my penis."
        tb "Again with the jokes. Unbelievable."

    tb "You really don’t understand how furious I am, do you?"

    scene tsubasadoesntwantxmasdick14
    with dissolve

    s "I think I’ve made it plenty clear that I never understand anything that’s going through your head by now."
    s "Like, who schedules a meeting on Christmas that is not only apparently super fucking important, but needs to be kept a secret from one of your own daughters?"
    tb "Perhaps the meeting {i}concerns{/i} said daughter? Perhaps Christmas is the only day we could feasibly arrange it? Perhaps you shouldn’t be asking questions at all? Perhaps you should be begging for forgiveness?"
    s "Do you {i}want{/i} me to beg for forgiveness?"
    tb "Sure. Let’s hear it."
    s "Oh, powerful Tsubasa. I apologize for being the scum of the earth. Please show me mercy and don’t tell Molly’s father that I fingered the life force out of his daughter on Jesus’ birthday."
    tb "You’re rather large even when you’re not erect, aren’t you?"
    s "Are we pivoting to talking about my penis now?"
    tb "I’m sorry. Would you rather talk about the monks instead?"

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick15 with flash
    stop sound

    mal "Shit! She’s on to us, man!"
    dia "Everyone, beat it!"
    s "You know about the monks?"
    tb "I already told you. I know everything that goes on in this house. And with how much you’ve been ranting about them, I’d be surprised if there’s anyone who {i}doesn’t{/i} know at this point."
    s "They won’t leave me alone, Tsubasa. I just want to enjoy Christmas. And they want me to think they’re my friends, but they’re not. They hate me. You hate me. Everyone hates me."
    tb "I don’t {i}hate{/i} you, Akira."

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick16 with flash
    stop sound

    tb "I just think you’re rather pathetic. That’s all. Hating you would be a waste of energy."
    s "Are {i}we{/i} not actually friends either?"
    tb "Of course we’re friends. If we weren’t, I’d have castrated you myself by now."
    s "You probably should, to be honest."
    tb "Nonsense. How would I ever explain that to Touka? She’s quite excited to have you put that thing inside of her one day. And I’m excited {i}for{/i} her."
    tb "But alas — you see her as your {i}mother.{/i} And surely you wouldn’t-"

    scene tsubasadoesntwantxmasdick17
    with dissolve2

    tb "..."
    s "I...uhh..."

    scene tsubasadoesntwantxmasdick18
    with dissolve

    tb "Heh."

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick19 with flash
    stop sound

    mal "Fuck! She’s on to {i}you{/i} too now, Akira! We’re {i}all{/i} fucked! Quick! Convince her you don’t have a thing for moms!"
    s "It’s just a...coincidence that...it got hard right now..."
    tb "Why, there’s no need to be embarrassed, Akira. You’re merely a boy. These things {i}happen.{/i}"
    s "I’m a man...not a boy."
    tb "Mmm...no. Right now, you’re a little boy. A {i}man{/i} wouldn’t make such terrible decisions. A {i}man{/i} wouldn’t jeopardize a meeting ten years in the making just to finger some white girl. Would he?"
    s "No, but...I’m still not a-"
    tb "Stroke it."

    scene tsubasadoesntwantxmasdick20
    with dissolve

    s "Huh?"
    tb "Take your hand, wrap it around your penis, and carefully stroke it until it feels like you’re going to burst. It’s called masturbation."
    tb "It’s what growing boys like you do to relieve all those pent up feelings they have for their mother or...{i}mother figure.{/i}"
    s "Tsubasa-"
    tb "Now."

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick21 with flash
    stop sound

    tb "{i}There you go.{/i} Doesn’t that feel good?"
    s "You’re just...going to watch?"
    tb "I need to make sure you do it correctly since Touka’s not here to be your mother right now. Don’t worry, though. I’m a suitable stand-in."
    s "It’s just...embarrassing...that’s all..."
    tb "And it wasn’t embarrassing being caught with your pants off while your fingers were stuffed inside of some teenager?"
    s "Somehow...not as embarrassing as this."
    tb "I imagine that’s just because you’re not used to being the one {i}without{/i} power. It’s just like our dynamic when we’re talking."
    tb "The only difference is this time, I get to watch you touch yourself while begging for my forgiveness."
    s "Tsu-"
    tb "Say, “I’m sorry, Mother. I’ve been a very bad boy.”"
    s "I...can’t say that..."
    tb "You’ll say it and you’ll like it. Or I’ll parade you around the manor for {i}all{/i} to bear witness to your shame."
    s "..."
    tb "I’m {i}waiting.{/i}"
    s "I’m sorry, Mother...I’ve been a very bad boy."

    scene tsubasadoesntwantxmasdick22
    with dissolve

    tb "PFFFFT! Hahahahaha! You actually did it! Oh, dear lord! I didn’t think you’d go along with it {i}that{/i} easily! You barely even put up a fight!"
    s "I...uh..."

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick23 with flash
    stop sound

    tb "Now that I know you’re willing to do as I say, though — how about we keep going?"
    s "What...do you want next?..."
    tb "Tell me about the first time you ever fucked an older woman."
    s "No..."
    tb "Why? Would you feel more comfortable telling me about the first time you ever fucked a younger girl?"

    scene tsubasadoesntwantxmasdick24
    with dissolve

    s "That’s...also..."
    tb "Well, I can’t ask you to tell me about the first time you ever fucked a girl your own age. {i}That{/i} would be a very short conversation, wouldn’t it?"
    s "Tsu...basa..."
    tb "Does having me so close heighten your arousal, Akira? Do you want me to...{i}help{/i} you?"

    scene tsubasadoesntwantxmasdick25
    with dissolve

    s "Yes..."
    tb "Then ask politely."
    s "Will you please...help me?..."
    tb "With what? I’m going to need you to be specific."
    s "Please...help me cum..."
    tb "Please help me cum...what?"
    s "Please...help me cum...{i}Mother.{/i}"
    tb "Aww..."
    tb "Well, when you put it that way..."

    scene tsubasadoesntwantxmasdick26
    with dissolve

    tb "No."
    s "Seriously?..."
    tb "Well, what kind of mother would I be if I helped my little boy relieve himself? He needs to learn how to do it on his own or he’ll wind up ruining meetings for someone very important one day."
    s "I said I was sorry, already..."
    tb "Say it again. But swap “Mother” with “Mommy” this time. I’ve always wondered how it’d feel to be addressed so...{i}casually.{/i}"
    s "I’m sorry...{i}Mommy...{/i}"
    tb "For what?"
    s "For...getting in the way of your meeting..."
    tb "Just say, “for not doing as I was told.” I like that more."

    scene tsubasadoesntwantxmasdick27
    with dissolve

    s "I’m sorry...for not doing as I was told..."
    tb "Are you going to listen to Mommy when she gives you a job from now on?"
    s "Yes..."
    tb "Reaaaaally? Because I’ll be very disappointed if you let me down again. But I’ll be so, {i}so{/i} proud of you if you manage to do everything correctly."
    s "What do you want me to do?..."
    tb "Right now, I want you to keep stroking yourself until you cum all over the floor."
    s "Can I touch you?..."
    tb "Sure. If you actually {i}want{/i} to be castrated."
    s "I just...I’ve already done it...so many times today..."
    tb "Oooooh? Are you telling me you’ve picked {i}Christmas day{/i} to be as naughty as you possibly can? What’ll happen if Santa finds out?"
    s "Hah...hah...aaah..."
    tb "Yes...just like that...nice and slow..."
    tb "Show Mommy how you play with that {i}biiiiig{/i} cock of yours."
    s "Please...{i}help...{/i}me..."
    tb "Would a substitute work instead?"
    s "What?...I-"

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick28 with flash
    stop sound
    play sound "knock.mp3"

    to "Mother? Are you in there? Father is trying to stall the best he can, but-"
    tb "Touka, darling — could you come in here and help me with something for a moment?"
    s "Don’t...let her in..."
    s "I don’t want her to...see me like this..."
    to "In...in the restroom? What...exactly do you need help with?"

    scene tsubasadoesntwantxmasdick29
    with dissolve

    tb "There’s a pesky rodent in here that I simply {i}can’t{/i} figure out how to squash!"
    to "A r-rodent?! In the manor?! How is that even possible?!"
    tb "What a {i}great{/i} question, Touka! I have no idea!"
    s "Tsubasa..."

    scene tsubasadoesntwantxmasdick30
    with dissolve

    tb "{i}Harder...{/i}"

    scene tsubasadoesntwantxmasdick31
    with dissolve

    s "Hah...hah...haah..."
    to "I...uhh...is...is this an acceptable situation to call 119? I’ve never had to...I haven’t learned about...rodents at all..."
    tb "I think it’d  be best if you just came inside for some...hands-on experience, darling."
    to "You...want me to touch it?!"
    tb "She’s right outside, Akira. {i}She’ll{/i} give you a hand, I’m sure."
    s "Not like this...not...like this..."
    tb "Or perhaps you’d like her mouth instead? Just imagine how carefully and {i}passionately{/i} she’d suck that...{i}big{/i} dick of yours..."
    to "Are...Are you talking to the rodent? I thought I heard-"
    tb "Just come on in, dear! See for yourself!"
    s "No...don’t..."

    play sound "doorlocked.mp3"

    to "I...can’t. The door is locked."
    tb "You should have a key on you somewhere, dear."
    to "I do. I just...have to find it. We have so many doors and...they all have their own locks."

    scene tsubasadoesntwantxmasdick32
    with dissolve

    tb "Are you excited? Touka’s {i}full{/i} of energy. And quite experienced when it comes to...{i}riding.{/i}"
    s "Tell her...to leave..."

    if tsukasaspring3 == True:
        tb "Would you rather I track down Tsukasa instead?"
        s "No..."
        tb "Are you sure? If you don’t act soon, someone else might...{i}take her away.{/i} And that’d be a real shame, wouldn’t it?"
        s "She’s...just a girl..."
        tb "Yes...and you {i}like{/i} that, don’t you? Admit it. Admit you want to grab her and {i}fuck{/i} that little attitude right out of her. Admit it, you sick fucking pervert. Admit it."
        s "I...won’t-"

        scene tsubasadoesntwantxmasdick33
        with dissolve

        tb "Stop slowing down. Mommy wants you to stroke it harder, so you’re going to fucking stroke it harder. Do you understand me?"
        s "Hah...haah...haah...yes...Mommy..."
        to "Oh! I’ve found it. I-"

        play sound "doorlocked.mp3"

        to "Ah. No. That’s not it."
        tb "I can make it happen, you know. I can get her in here. She’ll do {i}anything{/i} for attention. Especially when it involves you, {i}Sensei.{/i}"
        tb "Both of my little girls want you. One just doesn’t realize it yet. But I can push her in the right direction. Or perhaps it’s the {i}wrong{/i} one."
        tb "The line is rather blurry for people like us, isn’t it?"
        s "You’re a...horrible mother..."
        tb "Yes..."
        tb "Just how you like it."

    else:
        scene tsubasadoesntwantxmasdick33
        with dissolve

        tb "Or what? What are you going to do about it? {i}Fuck{/i} me?"
        tb "Ooooh no! What a terrible fate you’d have me suffer! Assuming you’d last more than three seconds, that is. Which, given your affinity for matriarchs, seems rather unlikely. Don’t you think?"
        to "Oh! I’ve found it. I-"

        play sound "doorlocked.mp3"

        to "Ah. No. That’s not it."

        s "Better you than...her...right now..."
        tb "Why not both? I don’t bond with my daughters nearly as much as I should. Think you’d be able to handle {i}two{/i} mothers, big boy? Or does merely the thought of that make you want to-"

    play sound "static.mp3"
    scene tsubasadoesntwantxmasdick34 with flash
    stop sound

    s "NMMFFGHH!!!!"
    tb "Ah! Oh my."

    "I do my best to stifle whatever noise I’m in the process of making, but I’m not sure if it works."

    scene tsubasadoesntwantxmasdick35
    with dissolve2

    "My semen rockets onto the ground, entirely covering the body of Spork — a glutton, he is."
    "It barely misses Tsubasa’s shoe. Which I imagine is great news as I’m sure I’d need to save up for years to be able to afford them."

    tb "How...{i}violent{/i} that ejaculation was. You poor thing. You must have been {i}incredibly{/i} turned on."

    to "Oh! This one {i}must{/i} be it! I-"

    play sound "doorlocked.mp3"
    stop music fadeout 12.0

    to "Ugh! Mother! I’m not sure how soon I’ll be able to-"

    scene black
    with dissolve2

    tb "Don’t worry, darling! I managed to take care of it on my own."
    tb "Would you be a dear and inform our guests that I’ll be back in one moment? And perhaps summon a maid to tidy up the restroom as well?"
    to "Of course, mother. I’ll see to it right now."

    play sound "footsteps.mp3"

    "One last time, as Touka’s footsteps fade away, I notice how deafeningly silent this room is."
    "But before I have time to drown myself in pity and shame, Tsubasa leans forward and whispers into my ear."

    tb "Never...and I mean {i}never...{/i}cum for anyone other than a Tsukioka in this manor {i}ever{/i} again. Do you understand me?"
    s "Yes..."
    tb "Yes, {i}what?{/i}"
    s "Yes..."
    s "Mother..."

    "O world-"
    "Look what you have done to me."

    $ renpy.end_replay()
    $ christmastsubasa1 = True
    $ tsubasa_love += 1

    "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
    "{i}Molly’s lust has increased to [molly_lust]!{/i}"
    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmasfive6

label tsubasaspring4:
    scene noonsky
    with dissolve2

    play sound "phonebeep.wav"

    "I hesitantly tap on Tsubasa’s name in my phone...knowing that, if she answers, I’ll have a hard time coming out of the conversation unscathed."
    "Because she’s talked to me before about what’s typically done with girls in rich families — how they’re traded like cattle. "
    "I’ve just never expected it would happen to the ones that I know. Let alone the ones she’s raised."
    "And as always, I just can’t understand why she’d do this."

    play sound "phonebeep.wav"

    tb "{i}Hello? Akira?{/i}"

    play music "tsukiokamanor.mp3" fadein 3.0

    "If she even {i}is{/i} doing it at all and Chinami wasn’t just...dramatically misunderstanding something."

    s "Hey, Tsubasa...By any chance, are you free right now?"
    tb "{i}{size=-1}Hmm...That’s a difficult question to answer as the freedom I typically have is almost always inhibited by the constant possibility that I may need to stop what I’m doing to address some sort of conflict or trade. {/size}{/i}"
    tb "{i}But I suppose I can find the time to fit you in should you need something from me. And I assume that you do as you wouldn’t call otherwise.{/i}"
    s "So I can’t call you just to hang out?"
    tb "{i}Of course you can. I’d just likely refuse since your time is better spent with my daughters instead of me.{/i}"
    s "Yeah, so that’s kind of why I want to talk to you. It’s about them."
    tb "{i}Oh my. Touka isn’t pregnant, is she? Because I simply just don’t have the time to deal with that right now.{/i}"
    s "If she is, it’s a miracle as I’ve yet to even lay a finger on her. "
    tb "{i}I’m both delighted and offended at the same time. How odd.{/i}"
    s "Tsubasa, it’s your other daughter I want to talk to you about."
    tb "{i}Oh dear. You got that one pregnant instead? That sounds quite painful for both of you, but welcome to the family regardless.{/i}"
    s "Again, haven’t laid a finger on her. I just...heard something recently that-"
    tb "{i}Let me guess — Tsukasa mentioned something about an arranged marriage to Chinami, who subsequently relayed the message to you out of fear for her friend’s well-being.{/i}"
    tb "{i}And now you’re upset because it means someone else is going to get to her before you do. Is that correct?{/i}"
    s "No. That’s not correct. I’m just worried about how Tsukasa feels in regard to this."
    tb "{i}With all due respect, Akira — Tsukasa is not your daughter to worry about. Perhaps that energy would be best spent on Ami instead?{/i}"
    s "Ami...hasn’t come home in a while. "
    tb "{i}Ahh, then I take it this is parenting withdrawal? Tsukasa’s home now if you would like to come over and pamper her. I’m sure she’d be delighted.{/i}"
    s "Can I just come talk to you instead? This is difficult over the phone since I can’t fall back on how much bigger I am than you when you make me feel weak and powerless."
    tb "{i}Is this flirting again? What should I say back?{/i}"
    s "Just tell me I can come over."
    tb "{i}You can come wherever you like, Akira. It makes no difference to me.{/i}"
    s "Uhh...cool. Then I guess I’m-"

    play sound "cardoor.mp3"

    limo "Master Arakawa — right this way, please."
    tb "{i}Oh, excellent! That was even quicker than normal. Do tell Daigo I said hello.{/i}"
    s "You sent a-"
    tb "{i}See you soon, Akira. Oh — and I have a surprise waiting. Ciao!{/i}"
    s "Tsuba-"

    play sound "phonebeep.wav"

    s "..."
    limo "Master Arakawa-"
    s "Tsubasa says hello."

    scene black
    with dissolve2

    "I hop in the back of the limo and prepare myself for what is already shaping up to be another eventful talk with Tsubasa. And one that comes with a “surprise” at that."
    "I just hope that whatever this surprise is doesn’t end up with me chained to a wall or forced into indentured servitude."

    play sound "static.mp3"
    scene tsubasayukioffice1 with flash
    stop sound

    "But I...suddenly realize that isn’t what she was referring to at all."

    yu "..."
    s "..."
    tb "So quick again! Daigo’s rapidly becoming my favorite driver out of all of them. I might have to give him a raise at this rate."
    tb "Anyway — you already know Yuki, yes? What do you think of her hair? Isn’t this much better than that ugly, faded blonde?"
    s "Her hair is the last thing I’m concerned about. I haven’t seen her since-"

    scene tsubasayukioffice2
    with dissolve

    yu "Since I nearly fuckin’ died in front of you, yeah. What the hell is he doing here? You didn’t tell me he was coming."
    tb "It was a surprise for both of you! Now, you no longer have to mope around all upset that you haven’t seen him in so long."

    scene tsubasayukioffice3
    with dissolve

    yu "What?! I never-"
    tb "She simply {i}won’t{/i} stop talking about you. It’s actually made me quite jealous!"

    scene tsubasayukioffice4
    with dissolve

    yu "That’s a lie! I haven’t-"

    play sound "static.mp3"
    scene tsubasayukioffice5 with flash
    stop sound

    yu "Wha-?! Dude! The fuck are you doing?!"
    s "Just let it happen. I’m glad to see you’re okay."

    scene tsubasayukioffice6
    with dissolve

    yu "Even after I...was a huge fuckin’ asshole to you? And tried to take your money and shit? {i}Why?{/i} Thought that bridge was as good as torched."
    s "You also asked me to come over and fuck you, so it’s not like it was {i}all{/i} evil."

    scene tsubasayukioffice7
    with dissolve

    yu "I...don’t remember doin’ that. But yeah, still alive. Just...{i}here{/i} now."

    scene tsubasayukioffice8
    with dissolve

    yu "And it’s all thanks to Nee-sama that I-"

    play sound "static.mp3"
    scene tsubasayukioffice9 with flash
    stop sound

    yu "N...Nee-sama?"
    tb "Hmph! You’ve never hugged {i}me{/i} like that..."
    yu "I ain’t even doin’ all the huggin’! He just grabbed me outta nowhere!"
    s "Nee-sama? Wait, you two aren’t-"
    yu "We ain’t actually related, no. I’ve just always called her that."
    s "So are you, like...her {i}bodyguard{/i} now? Or..."
    yu "I think I’m more like a pet than anything at this point."
    tb "Bad dog! Heel!"

    play sound "static.mp3"
    scene tsubasayukioffice10 with flash
    stop sound

    yu "See what I mean?"
    s "Yeah, but...I can ask more about that later. Are you doing okay? How long do you-"

    scene tsubasayukioffice11
    with dissolve

    tb "Yuki’s health is no immediate concern and the Tsukioka Foundation is fully covering any and all treatment she may need. It’s the least I can do."
    yu "Callin’ it the “least” you can do when you’re savin’ my life is the fuckin’ understatement of the century. I’d be dying without you, Nee-sama."

    scene tsubasayukioffice12
    with dissolve

    tb "In that case! May {i}I{/i} be hugged next?"
    yu "Sure. Go get her, Akira."

    scene tsubasayukioffice13
    with dissolve

    tb "Tch! Why is it that I can have everything in life besides the one thing I want?"
    s "This is...an interesting side of you, Tsubasa."

    scene tsubasayukioffice14
    with dissolve

    tb "Is it? How so?"
    s "You just seem more...relaxed, I guess? There’s no guard up when you talk to Yuki like there is when you talk to me."
    tb "Nonsense. Why on earth would I have my guard up around you, Akira? You’re among the least intimidating men I’ve ever encountered."
    yu "She just likes fuckin’ with me. Kinda like a big sister pickin’ on the little sister sorta thing."
    s "So Tsubasa’s the {i}older{/i} sister in this relationship?"

    scene tsubasayukioffice15
    with dissolve

    yu "Well, yeah. She’s older than me."
    s "Wait, so how old is-"
    tb "Yuki — didn’t you have some matters to attend to tonight? I practically had to beg just to have you wait around for the surprise."

    scene tsubasayukioffice16
    with dissolve

    yu "Oh, shit! You’re right. I totally forgot."

    scene tsubasayukioffice17
    with dissolve

    yu "I’m goin’ back to the bar to talk to Sara and shit. Ain’t sure if she’ll give me my job back, but I at least want to apologize for bein’ an asshole to her after she went out of her way for me."
    yu "Plus, she doesn’t even know about the cancer thing yet and...yeah."
    yu "But anyway — I’m gonna be here for a little while. And...I’m sorry to you too. I’m just...you know...kind of a terrible person. So shit like that might happen sometimes."
    s "As an equally terrible person, I understand."
    s "It was nice seeing you, Yuki. I’m glad you’re okay."

    scene tsubasayukioffice18
    with dissolve

    yu "Yeah! Uhh..."
    yu "Bye."

    play sound "static.mp3"
    scene tsubasayukioffice19 with flash
    stop sound
    play sound "doorclose.mp3"

    "Yuki leaves the room and...wait, why am I here again?"

    tb "So —you wanted to talk to me about Tsukasa?"

    scene tsubasayukioffice20
    with dissolve

    s "Oh, right. You’re not, like...{i}actually{/i} considering marrying her off to some random guy, are you?"
    tb "He’d be no {i}random{/i} guy, Akira. None of her potential suitors fit that pairing of words. They’re valuable assets from upstanding families who, more than likely, would treat her well."
    s "She’s a kid..."

    play sound "static.mp3"
    scene tsubasayukioffice21 with flash
    stop sound

    tb "Which is probably one more reason {i}why{/i} she has so many suitors. Men in power really seem to jump at that sort of thing, don’t they?"
    s "And you’re just going to endorse it? You don’t care at all about what this would mean for her as a person?"

    scene tsubasayukioffice22
    with dissolve

    tb "What would it mean for her as a person, Akira? Because, from what I understand, you haven’t talked to Tsukasa about this at all. Just one of her friends."
    s "But that friend knows her well and can tell that she’s scared."
    tb "You’re scared right now and no harm has befallen {i}you{/i} yet. Who’s to say the same won’t happen to Tsukasa as well?"
    s "You {i}want{/i} this then? To just...offload her on someone else?"
    tb "Not at all. As I said — there are valuable assets all over this city willing to merge into the Tsukioka Foundation for the right price. And there will always be things money can’t buy."
    s "So you intend to just buy them with your daughter’s hand in marriage?"
    tb "{i}I{/i} don’t. My husband does. And this company is even more his child than the girls are. I imagine Touka would be in the same boat if she were not the heir apparent."
    tb "What I’m doing is mediating the facilitation of his desires as that is my role in both the company and this family."
    s "But isn’t it your role as a {i}mother{/i} to make sure your children are happy and {i}safe?{/i}"
    tb "Indeed it is. Which is why I’d not hesitate to call this off should Tsukasa verbalize her hesitancy. Even mere {i}unease{/i} would do the trick."
    s "It’s...that simple? Really? You don’t have anything else up your sleeve?"

    scene tsubasayukioffice23
    with dissolve

    tb "I always have something up my sleeve, Akira. You have to in this line of work."
    tb "Tomonori may be the family head, but do you really think {i}I’m{/i} the type to gleefully allow someone else to pull my strings?"
    s "When you say shit about “facilitating his desires” then yeah, I’m sort of forced to think that."
    tb "I say what I need to say to protect the things I love. But sometimes, it’s the opposite."
    tb "Sometimes, the things I {i}don’t{/i} say are the ones that ring the loudest...or make the biggest differences. Which is why I’m sure you’ll understand what I’m doing in time."

    scene tsubasayukioffice24
    with dissolve

    tb "But for now — I imagine I must look pretty evil, don’t I?"
    s "You’d look a lot worse if I didn’t find out five minutes ago that you saved my friend’s life."
    tb "I’ve done no such thing. It takes far more than just money to defeat cancer."
    tb "I’m just giving Yuki the tools she needs to fight the battle. But she’s the one who will ultimately need to save her own life."
    s "You’re helping her either way."
    tb "As I’ve said — I protect the things I love. So why do you imagine that what I’m doing with Tsukasa is any different?"
    s "It’s just...a confusing situation for me to hear from one of Tsukasa’s friends that she’s so scared of such a mature thing at her age."
    tb "Confusing because you feel bad for her? Or because you’re attracted to her?"
    s "I’m not-"
    tb "I saw what you did in her room, Akira."

    if christmastsubasa1 == True:
        tb "And almost {i}right{/i} after I told you to never cum for anyone other than a Tsukioka in my house again."
        tb "It’s like you disobeyed me on purpose. The {i}audacity.{/i}"
        s "..."
        tb "Though, I suppose you may have found a loophole. And I suppose that you may have been cumming {i}for{/i} Tsukasa despite being so...{i}deep{/i} inside of your subordinate."

    tb "You’ve been a very, very bad boy."
    s "That was...not a good night for me."
    tb "Oh, I’m not looking for an excuse. You’re not in any {i}trouble.{/i}"
    tb "As far as I’m concerned, what you did in there was no different from a live demonstration of the same brand of sexual intercourse she’d see if she looked it up online."
    tb "Which she’s been doing quite frequently as of late. The poor girl doesn’t realize I can see her browsing history right from my telephone. Isn’t technology so fascinating now?"
    s "I’m not...attracted to her, though. That was just a mistake I made in the heat of the moment."
    tb "Bullshit. You know I have eyes everywhere and you knew you’d be caught. You dragged that woman to Tsukasa’s room for one reason and one reason only. You wanted to plant a seed."

    scene tsubasayukioffice25
    with dissolve

    tb "And no — I’m not talking about the type you planted in {i}her.{/i} I’m talking about the type that wakes a curious little girl up."
    tb "And in that regard — bravo, Akira. You’ve done it. But what will you do {i}next?{/i} What’s the next phase of your plan? Because you need to hurry now, don’t you? The clock is ticking."
    tb "If you don’t act quickly, you might never {i}get{/i} another chance to fuck some woman in front of my youngest daughter. And that’s far more boring for me too, so I’m rooting for you."
    s "You’re...rooting for me."
    tb "I kind of {i}have{/i} to. I don’t have much of a choice when all is said and done."

    scene tsubasayukioffice26
    with dissolve

    tb "I wouldn’t be too worried if I were you, though. Even if the video {i}does{/i} get out, the audio is barely audible and the footage is rather grainy."
    s "You...have it on video?"

    scene tsubasayukioffice27
    with dissolve

    tb "Either that or I’m lying. Which one is it, do you think?"
    s "Tsubasa...what do you want from me? Just tell me instead of trying to blackmail me all the time."

    scene tsubasayukioffice28
    with dissolve

    tb "Well, where’s the fun in that?"
    s "There isn’t any. There doesn’t have to be. Because this might be fun for you, but it’s terrible for me. And the fact that I’m being constantly pushed into making the worst possible decisions is-"
    tb "Blah, blah, blah. Sometimes you have to force someone to do certain things or blah, blah, blah. I can’t remember how it goes."
    s "Can’t...remember how {i}what{/i} goes?"
    tb "The thing. I’m sure you’ve heard it before, no?"
    s "I...don’t really know. But either way, I can’t just...{i}do{/i} that to Tsukasa if that’s what you’re trying to push me to do."
    s "Because I’m sure it sounds weird, but...I kind of {i}care{/i} about her. And I don’t want to hurt her like that because I’ve seen what it turns other girls into."
    tb "Do {i}what?{/i} I’m oblivious and stupid. I don’t know what you’re alluding to."
    s "You know exactly what I’m alluding to. And if you somehow honestly don’t, all you need to do is look up Tsukasa’s search history again for a reminder."

    scene tsubasayukioffice29
    with dissolve

    tb "Hah! Now, now, Akira — we need to give her {i}some{/i} privacy, don’t we?"

    scene tsubasayukioffice30
    with dissolve

    tb "But we also need to make sure she’s not {i}too{/i} ill-prepared for her pending and potentially {i}very scary{/i} future...assuming nothing {i}gets in the way{/i} of that."
    tb "So I’m proposing that you add a {i}new{/i} subject to whatever sort of...{i}curriculum{/i} you’re using for her tutoring."
    tb "And I’m sure you know what that subject is as it won’t be the first time you’ve {i}tutored{/i} a girl her age in it. Do you understand what I mean?"
    s "I...know what you mean. I just don’t know how you {i}know.{/i}"
    tb "You don’t need to. Just play {i}your{/i} part and I’ll play mine."

    scene tsubasayukioffice31
    with dissolve

    tb "One thing to note, though — us Tsukiokas are “hands-on” learners. Do with that information what you will."
    s "What are you reaching for-"

    play sound "buzzer.mp3"

    tb "Tsukasa? Can you come to my office for a moment, dear?"
    s "Tsubasa...what are you-"

    scene tsubasayukioffice32
    with dissolve

    tb "You don’t have any plans tonight, do you? I figure I should be here for at least the {i}first{/i} session if Tsukasa is going to learn sexual education from a man as {i}unpredictable{/i} as you."
    s "{i}Now?{/i} Seriously? I haven’t even agreed yet. This isn’t-"
    tb "Oh, Akira. You don’t have a choice! And neither do I — so let’s just make the most of this, shall we?"

    $ renpy.end_replay()
    $ tsubasaspring4 = True
    $ tsubasa_love += 15

    jump tsukasaspring6

label tsubasaspring5:
    play sound "slidedoor.mp3"

    "{i}One hour later...{/i}"

    to "Mother — I apologize for the intrusion..."

    scene tsubasabathagain1
    with dissolve2
    play music "merrychristmasmrlawrence.mp3"

    to "But I would like to talk about what transpired here today if you have a moment or two to spare."
    tb "Hm...Well at least it’s actually {i}you{/i} this time. So how could I refuse if my oldest daughter is asking?"
    to "You’ve refused me many times before, Mother. "
    to "In fact, you were refusing me quite unabashedly just an hour ago when I was attempting to drag my teacher out of the devious scenario you forced him into this time."
    tb "You seemed quite happy to be involved in that {i}scenario{/i} until your sister tried to steal your man from under your nose, dear."

    scene tsubasabathagain2
    with dissolve

    tb "I swear — I’m always so surprised by how reluctant you are to take the things you’re entitled to."
    to "No one is {i}entitled{/i} to Sensei, Mother. Not me. Not you. And most {i}definitely{/i} not Tsukasa."

    scene tsubasabathagain3
    with dissolve

    tb "No wonder he sees you as a mother if you’re going to defend him like {i}that.{/i} But you seem to be misunderstanding something, dear. "
    tb "What happened in my office was not an attempt to {i}force{/i} your beloved Akira into anything at all. I’m just trying to do what’s best for our family."
    to "Well, I struggle to understand just what you believe you are doing for this family by asking the man I’ve grown a fondness for to teach both my sister and me about...sex."
    tb "You don’t need to hesitate when using that word around me, Touka. You’re at the age now where I’m surprised you can think about anything else {i}at all.{/i}"
    to "I tend to keep my family out of such fantasies, thank you very much. And even {i}if{/i} I am of that age, Tsukasa isn’t."
    tb "She is, though. And do you want to know {i}why{/i} she is, Touka?"
    to "Not particularly...but if I had to wager a guess, I assume it may have something to do with the fact that you’re moving forward with this archaic tradition of marrying her off. "
    to "Which, with all due respect, I am very disappointed to hear. For I had assumed that-"

    play sound "static.mp3"
    scene tsubasabathagain4 with flash
    stop sound

    tb "Did you or did you not create an opportunity for your teacher and his subordinate to venture off for some “alone time” during the Christmas party, Touka?"
    to "I...that-"
    tb "Why? Because I understand kindness, but not the type that involves sending my man off to bed another woman in my own home. "
    to "It...is not up to me who Sensei-"
    tb "Do you know where he {i}went{/i} with her, Touka? Would you like to wager a guess in regard to that as well?"
    to "I...assume one of the guest rooms or a...restroom, perhaps? But does the room really-"
    tb "He went to your {i}sister’s{/i} room. "
    to "Then...Then he likely didn’t know it was-"
    tb "He’s been there before for her studies. And he went there on purpose that night."
    tb "So it wouldn’t be a stretch to believe that she may have witnessed something that sparked this sudden curiosity that night, do you?"

    scene tsubasabathagain5
    with fade

    to "R...Regardless of how such curiosity is {i}founded,{/i} the fact remains that your actions today have done nothing but exaggerate it."
    to "Tsukasa is likely just confused by the idea that she may soon need to marry a man she hasn’t met. "
    to "And I have to say, Mother, I’m surprised she knows at all. You’re typically better at keeping secrets than that."
    tb "I am, aren’t I? Yet both of you have managed to figure it out on your own. So either the two of you are very smart, or I’m just getting sloppy."
    to "Or you’re sowing the seeds of chaos for your own amusement out of jealousy that {i}I{/i} have managed to find something that {i}you{/i} never could. "
    tb "Which is?"
    to "Love for someone that was not {i}chosen{/i} for me."

    scene tsubasabathagain6
    with fade

    tb "..."
    to "And I imagine that’s why you’re going to ship Tsukasa off as well...so that {i}she{/i} can’t find the same thing."
    tb "Is that really what you think of me, Touka? "
    tb "That I’m just jealous? "
    tb "That I’ve never found love of my own before?"
    to "I am saying that is how it appears...And with how secretive essentially {i}all{/i} of your decision-making is, I can’t say I should be blamed for coming to such a conclusion."
    to "If I am to take over for this family, isn’t it time that you stop keeping me in the dark? Have I not proven to you that I am mature enough to hear the {i}truth{/i} yet? "
    to "Just speak to me! Stop making me guess!"
    tb "{i}Mature.{/i} You won’t even fuck the man you {i}love{/i} because you’re nervous about it and you want to talk about being “mature.” Give me a break."

    play sound "static.mp3"
    scene tsubasabathagain7 with flash
    stop sound

    to "If it were just me in that room, I may take this bait...But Tsukasa was there as well. "
    to "And there is simply {i}no{/i} way that someone as smart as you would ever think that such a thing is a “good” idea. So you need to be doing it on purpose. "
    to "{i}You{/i} are the one creating an opportunity this time. Not me. And in your very own house too."

    scene tsubasabathagain8
    with fade

    tb "You make me very proud sometimes, Touka. You really do."
    to "How unfortunate that {i}this{/i} is one of those times. "
    tb "Yes...how unfortunate, indeed. I can’t imagine there’s anything I could say right now that would make you want to join me for a bath, is there?"
    to "Not at the moment, no. I came here for the express purpose of asking you to leave Sensei alone — and to sever {i}all{/i} of his ties with Tsukasa immediately. "

    scene tsubasabathagain9
    with dissolve

    tb "Oh?..."
    tb "Is that for {i}his{/i} sake? Or hers?"
    to "..."
    tb "You seem quite interested in your sister all of a sudden, Touka. You’ve never expressed this much concern for her before. At least not to me. So perhaps {i}you’re{/i} the jealous one?"

    scene tsubasabathagain10
    with dissolve

    tb "Or perhaps all three of us are jealous of one another? It isn’t often we have such a handsome young man roaming around the manor. Of course we’d {i}think{/i} things. {i}Want{/i} things."
    tb "But what if this goes a little deeper than that? What if there’s another possibility for what’s really going on here that I simply...{i}can’t{/i} tell you regardless of how much I may want to?"
    tb "What if what I’m doing right now is the ultimate sign of love?"
    to "I’m hard pressed to believe that Tsukasa’s sexual education plays any part in that at all."
    tb "It does if he fucks her, dear."

    play sound "static.mp3"
    scene tsubasabathagain11 with flash
    stop sound

    to "Mother?!!!?!?"

    play sound "static.mp3"
    scene tsubasabathagain12 with flash
    stop sound

    tb "Tsukasa figured things out without being told and has {i}yet{/i} to speak to me about it. She’s accepted her duty as a member of the family and is inclined to let things play out without interfering."
    tb "I swear, she’s such a good girl when she isn’t tormenting the staff. Which is precisely why we both know she isn’t going to just {i}ask{/i} to go against the family’s wishes."
    tb "That’s not enough, though. If I call the wedding off without reason, that reflects negatively upon us and threatens to disrupt the ecosystem this family has fought so hard to build."
    tb "It won’t just be {i}her{/i} in jeopardy, it will be all of us. "
    tb "But if a third party interferes...and she falls for someone outside of our direct sphere of influence, perhaps we won’t need to call off a wedding at all?"
    tb "Perhaps no one will want one in the first place."
    to "Then you intend to...give her to {i}Sensei{/i} so you don’t have to give her to someone else?! {i}That’s{/i} your master plan?!"
    tb "Maybe. Or maybe it’s just one more lie that’s far easier for you to understand than an even harsher truth."
    to "I just...I understand what you mean and...{i}I{/i} don’t want her married off at this age either. But surely there must be a way that doesn’t involve her sleeping with my teacher?"
    tb "The two of {i}them{/i} could be married, I suppose. Lord knows being married doesn’t mean a couple is having sex. But if they wanted to, it wouldn’t be our place to stop them."
    to "Could she not just...marry one of the staff instead? Why does it have to be {i}him?{/i} That’s the part I’m not understanding."
    tb "You understand, Touka. You just don’t {i}want{/i} to. "
    tb "The two of you want the same thing. So what’s a mother to do when that happens? Especially a mother who’s already promised to protect {i}him{/i} as well. "
    tb "There’s only one way to save all of you. And I imagine we’ll {i}all{/i} wind up sleeping with him eventually, so what’s the point in holding back now?"

    play sound "static.mp3"
    scene tsubasabathagain13 with flash
    stop sound

    to "What do you mean you made a promise to “protect him?” Because, last I checked, you’re the one constantly putting him in danger."
    tb "So you get upset when your sister speaks of fucking him, but not me. Our bond really is a special one, isn’t it?"
    to "Who {i}is{/i} Sensei to you? Why must he be so intrinsically involved in {i}everything?{/i} "
    tb "Just a friend, of course. Any other connection is purely coincidental. "
    to "And I’m just supposed to believe that?"
    tb "No. But you’re supposed to {i}accept{/i} it. Such is the life of a Tsukioka."
    to "If I had known this would be the life I’m meant to lead, I’d have offered myself up instead of Tsukasa and tried my luck elsewhere. I’m not exactly fond of treating people like pieces on a chess board."
    tb "Chess is an acquired taste — like wine. No one starts off liking it, but you grow to appreciate its complexities in time. And eventually, it’s hard to live without it."
    to "Then perhaps you’ve drunk a bit too much as your movements are suddenly sloppy and unfitting of the woman I am modeled after."
    tb "If you think you can handle this better than I can, feel free. I have no qualms with handing over the reins if you’ve come up with your own idea on how to preserve this family."
    tb "That said, however, I imagine that you’ll ultimately arrive at the same place as me. "
    tb "And soon, you’ll understand just how much easier it would be to keep an eye on him if he was just {i}here.{/i}"
    to "If he is here, it will be because he {i}wants{/i} to be. Not because one of us has forced his hand."
    tb "I don’t disagree with that at all. I’m just tired of everyone I know {i}wanting{/i} things and never taking them. It’s all far too nostalgic."
    to "Then let me say this — I {i}will{/i} find a way to make him mine. And {i}when{/i} I do, this type of behavior will not be tolerated {i}regardless{/i} of whether or not you are my mother."
    tb "Aww...you really won’t share? After all I’ve given to you?"

    scene tsubasabathagain14
    with dissolve

    to "Listen to yourself! You are a {i}married{/i} woman! I can’t even {i}begin{/i} to think of what Father would say if he heard any of this right now!"
    tb "You’re right. I {i}am{/i} married."

    play sound "static.mp3"
    scene tsubasabathagain15 with flash
    stop sound

    tb "But we have a {i}long{/i} history of concubines in this family..."
    tb "And if you don’t hurry up, I might be tempted to take one. "
    to "..."
    tb "How would that make you feel, Touka?..."
    tb "Losing your man to your mother?..."
    tb "Better or worse than losing him to Tsukasa?..."
    tb "I wonder which one of us he’d prefer? "
    to "..."

    scene tsubasabathagain16
    with dissolve2

    tb "{i}I’m surprised a righteous {i}fool{/i} like you can love him at all when you already know the answer.{/i}"
    to "Mother-"
    tb "Hurry up. "
    tb "I don’t want {i}you{/i} becoming an obstacle as well."

    play sound "static.mp3"
    scene tsubasabathagain17 with flash
    stop sound

    "Touka Tsukioka was pissed!"
    "It wasn’t every day that someone wanted to fuck the man she- well, actually, it was. But it wasn’t every day that her {i}mother{/i} wanted to fuck him! And that was bad!"
    "Or at least she thought it was bad? But similar to Akira, she left every serious conversation with Tsubasa wondering whether or not she’d just been played."
    "And maybe she had!"

    stop music
    play sound "static.mp3"
    scene tsubasabathagain18 with flash
    stop sound

    "Or maybe she hadn’t. Because Tsubasa wasn’t feeling very ecstatic right now either."
    "And as she stood there in her towel for a solid five minutes, fingers massaging her eyelids as she came to terms with always being seen as the bad guy, she believed for a moment that maybe she {i}was.{/i}"
    "And maybe it was a {i}bad{/i} idea to have a man who wore his impurest proclivities on his sleeves like cuff-links be the one to teach her youngest daughter about the birds and the bees."
    "It was pretty safe to say she was going through it. But that was a side of her that needed to stay concealed at the risk of destroying everything."

    scene tsubasabathagain19
    with dissolve2

    "For if it didn’t, something told her that something else would be destroyed. And that something was far closer to her than that other something. Or something."
    "Neither one of us can tell you what it is because neither one of us knows."
    "We just know {i}it’s{/i} bad and {i}this{/i} is good. But it {i}can’t{/i} be {u}good{/u} if {b}bad{/b} things don’t happen. Which makes the {u}bad{/u} things less {i}bad{/i} and more {u}good.{/u}"

    scene black
    with dissolve4

    "Tsubasa Tsukioka was an excellent babysitter — and an even better business partner."
    "She’s doing a great job! "
    "Her job just sucks."

    $ renpy.end_replay()
    $ tsubasaspring5 = True
    $ tsubasa_love += 1

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label tsubasaspring6:
    scene nightsky
    with dissolve3
    play music "blueair.mp3"

    "Something was happening inside of the Kumon-mi Mall. "
    "They say it’s “renovations.” But if you check online, they don’t ever tell you what they’re {i}renovating.{/i} And that makes me immensely distrustful. "
    "Other things that make me immensely distrustful are the virality of fake animal rescue videos, pricing that ends with .99, and the unfortunate fact that I am always being lied to."
    "I want to see what’s being built inside of those walls. I want to know what’s happening above and below. Where that massive hole leads to. How the town still breathes."
    "And something tells me that soon, I will."

    stop music
    play sound "static.mp3"
    scene tsubasamall1 with flash
    stop sound
    play music "mall.mp3"

    "Because Tsubasa Tsukioka has special privileges and is allowed inside during the construction for some reason."
    "How convenient that I get to stick to her today!"

    yu "{i}This was a fuckin’ horrible idea, Nee-sama!{/i} "

    "Oh, it looks like she’s allowed to bring a friend too."

    tb "Because of the price tag, I assume? You needn’t worry about that. Whatever you want is on me."
    yu "{i}Not because of the fuckin’ price tag! Because I look like a god damn Barbie and the only experience I have with those is rippin’ their heads off and setting ‘em on fire!{/i}"

    scene tsubasamall2
    with dissolve

    tb "Why do all poor people seem to have the most {i}morbid{/i} ideas of how to have fun? I don’t even want to think of what you’d have done to that poor doll’s dream house."
    yu "{i}That shit was for rich kids. But I’d have probably set that on fire too.{/i}"
    tb "I’m sure you look fine, Yuki. Just open the curtain if you’re unsure and I’ll gladly weigh in. No one else is here if you’re worried about being seen."
    yu "{i}I am worried about being seen, but only cause I ain’t ever gonna be able to live this down.{/i}"
    tb "You’re only saying that because you have no confidence, darling. I’m sure you’re stunning. Now, go on — peel back the curtain. Show me the dress."
    yu "{i}Ugh. Fine.{/i}"

    scene black
    with dissolve
    scene tsubasamall3
    with dissolve2

    tb "..."
    yu "I fucking hate you."

    scene tsubasamall4
    with fade

    tb "..."
    yu "..."

    scene tsubasamall5
    with dissolve

    tb "{b}{size=+20}HA!{/b}{/size}"
    yu "Okay. Fun’s over. I’m puttin’ real clothes back on."
    tb "You look like a failed makeover scene from a John Hughes film! Or like you fell into the bargain bin of a Beverly Hills Goodwill! I love it! Come back! I need to take photos!"
    yu "{i}You’re lucky I’m dying! I’d never let anybody fuck with me like this under normal circumstances!{/i}"

    scene tsubasamall6
    with dissolve

    tb "Oh, can it. If I wanted to “fuck” with you, I’d parade you around town wearing that. If anything, {i}you’re{/i} lucky that I want this moment all to myself."
    yu "{i}Yeah. Real lucky you get to burn that image into your mind while I try to figure out how to take this damn thing off. Look like a goddamn bride right now.{/i}"
    tb "Savor it while you can, then. It’s not like {i}you’ll{/i} ever get married, so you may want to burn this image into your memory as well."
    yu "I AM married!"
    tb "I meant to a real man — not one who sits idly by while his wife is violated by a group of cronies who I may or may not have had subsequently castrated."
    yu "{i}You did what?{/i}"
    tb "Hm? I didn’t say anything."

    scene tsubasamall7
    with dissolve

    yu "The fuck were you doin’ over there anyway? Thought you hated the Yakuza. Some kinda business thing?"
    tb "Something like that. Can we not just say I was searching for a damsel in distress?"
    yu "You can, I guess. Just it’d make you look bad since you took your sweet ass time finding me."
    tb "Mmm, and whose fault is it that I needed to {i}find{/i} you in the first place? Hmm?"

    scene black
    with dissolve2

    yu "I don’t know what you’re talkin’ about. We done here?"
    tb "Already? But we haven’t gotten our nails done yet."
    yu "By {i}who?{/i} You took me to a fuckin’ mall without any people in it. I don’t know how to paint my own nails."
    tb "Even better! I’ll do them for you! Here-"
    yu "N-Nee-sama! Leave my fuckin’ hands alone-"
    tb "Oh my. Do you always bite them like this? They look absolutely horrendous."
    yu "Get your fuckin’ hands off of me!"

    play sound "static.mp3"
    scene tsubasamall8 with flash
    stop sound

    tb "I swear, Yuki — you put up a stronger fight against me than you do when you’re being gang-raped."
    yu "I am in much better shape now. {i}You{/i} try puttin’ up a fight when the only things you’ve put in your body for a week straight are drugs and alcohol. "
    tb "Impossible. I know better than to treat my body in such a way. And you would too if you were not such a brat all the time."
    yu "Ain’t nobody ever called me that and lived to tell the tale, you know."

    scene tsubasamall9
    with dissolve

    yu "In fact, ain’t nobody ever called me that in general, I don’t think."
    tb "Good. Only {i}I{/i} should be able to say mean things to you without being punished. This is my privilege as the most powerful woman in Kumon-mi."

    scene tsubasamall10
    with dissolve

    yu "Oh, fuck off. Same shit was true before you even {i}were{/i} the most powerful woman in Kumon-mi. You just enjoy makin’ my life difficult."
    tb "Yes, but now I can make it even {i}more{/i} difficult because I currently {i}am{/i} the most powerful woman in Kumon-mi. "
    tb "Do you have any idea how easy it would be for me to have you locked up and forced to play dress-up with me {i}forever?{/i} "

    scene tsubasamall11
    with dissolve2
    stop music fadeout 12.0

    yu "Why don’t you then if you get so much fuckin’ enjoyment out of it?"
    tb "The same reason as last time. A forest bird never wants a cage."
    yu "What, you gonna get all {i}poetic{/i} on me now? You know I ain’t good at that shit."
    tb "I’m just saying — it’s your freedom that’s always made you so beautiful. Taking that away would be a sin that not even God can forgive."
    yu "You know I ain’t about that {i}God{/i} shit either, Nee-sama."
    tb "Mm."

    scene black
    with dissolve2

    tb "And perhaps that’s for the best."

    "........."
    "......"
    "..."

    scene tsubasamall12
    with dissolve2
    play music "thesleepingcity.mp3"

    "The two girls — or women as they were now — found their way to the parking lot where Yuki’s bike was left."
    "And before long they were off, bathed in the glow of the moon to the point where it felt as if there was a third person right there with them."

    scene tsubasamall13
    with dissolve2

    "But there wasn’t. And there never would be again because that’s just how life works sometimes."
    "But even in those moments of sad acceptance, it’s always possible to find joy. "
    "This was a very rare moment in which both of these girls — or women as they were forced to be — could feel that at once."

    yu "You sure you want to ride with me instead of takin’ one of your fancy limos back? Just as reckless now as I was when we were kids, you know."
    tb "I do hope you aren’t going to ask me that every single time. You did the same thing on the way here."
    yu "Feel obligated to. Ain’t used to carryin’ precious cargo anymore. Might make me a little jumpy."
    tb "How far do you think my old house is from here?"
    yu "You serious? Been stuck in that mansion for so long you can’t even remember where you’re from?"
    tb "I’m not {i}stuck{/i} there. I’m a willing participant of my own seclusion. It makes moments like this all the more special."
    yu "You sure you ain’t just brainwashed? I’ve heard money {i}changes{/i} people, you know."

    scene tsubasamall14
    with dissolve

    tb "Does it? Do I seem all that {i}different{/i} to you then, Yuki?"
    yu "Nah. Still a pain in the ass. Still holdin’ on just as tight as ever. "
    tb "Only because I feel like you’ll leave me behind if I don’t."
    yu "Don’t worry. It’s common courtesy to stop the bike if your passenger falls off."

    scene tsubasamall15
    with dissolve

    tb "Right..."
    tb "That’s what I meant."

    play sound "static.mp3"
    scene tsubasamall16 with flash
    stop sound

    tb "Wait! The beach is the other way! You told me you were taking me swimming! I bought a new bikini for this and everything!"
    yu "Sorry, Nee-sama! New plan! Gonna have to deal with it!"

    scene tsubasamall17
    with dissolve

    tb "I knew it! I {i}always{/i} knew you’d hold me ransom one day! Whatever you’re being offered, I’ll pay you double! Or...how...how much are you being offered exactly?"
    yu "Nadda."
    tb "You’re doing it for free?! You delinquents are so {i}dumb{/i} sometimes! You could make so much money off of me!"
    yu "Sounds kinda like you’re tryin’ to talk me into it."

    scene tsubasamall18
    with dissolve

    tb "I’m just saying — if you’re going to kidnap someone, the least you can do is try to profit off of it. This is why {i}I’m{/i} rich and {i}you’re{/i} not."
    yu "If I wanted to kidnap you, I’d have done it already. We’re just goin’ to the lake instead. Fewer people. Less of a chance that we’ll be caught. Figured you’d like that."

    scene tsubasamall19
    with dissolve

    tb "The lake? You can swim in those? Aren’t they full of fish and bugs and trash and just...generally disgusting, small bodies of water?"
    yu "You know it. So you might want to leave that fancy new swimsuit in your bag and just jump in naked with the rest of us."

    scene tsubasamall20
    with dissolve

    tb "You’re joking."
    yu "Or you could stay on land. Makes no difference to me."
    tb "You’d really have me sit there and watch a bunch of delinquents skinny-dip in a garbage-infested lake?"
    yu "Course not. {i}I’d{/i} have you {i}join{/i} us in that garbage-infested lake. {i}You’re{/i} the one who’s being a priss about it."
    tb "But what happens if something gross touches my leg? "
    yu "Then something gross touches your leg. The fuck you want {i}me{/i} to do about it?"

    scene tsubasamall21
    with dissolve

    tb "Protect me, obviously! You know I don’t like gross things!"
    yu "That shit’s just part of life, Nee-sama. You’re gonna miss out on all of the fun if you’re constantly worried like that."

    scene tsubasamall22
    with dissolve

    tb "Can you at least call me by name if you’re going to indoctrinate me into this filthy way of living? I’m tired of hearing you say “Nee-sama” all the time. It’s so uncharacteristic. "
    yu "Nah."

    scene tsubasamall23
    with dissolve

    tb "You shot me down so easily!"
    yu "Just bein’ respectful, you know? You’re on a level I can’t ever even hope to reach."

    scene tsubasamall24
    with dissolve

    tb "Huh? Why not?"
    yu "Just ain’t how shit works in the real world. Least not most of the time. You were born to eat from silver spoons and shit and I was born to polish ‘em. "
    yu "Ain’t really a bad thing, though. I like livin’ this way. Havin’ nobody who expects anything from me and nobody who feels like they’ve gotta {i}look{/i} for me when I go missing."
    yu "Just different worlds we’ve got. And if you really wanna see mine, you’re gonna have to be a little more open. Capiche?"
    tb "Va bene."

    scene tsubasamall25
    with dissolve

    yu "What?"
    tb "Oh. Sorry. I assumed you spoke Italian."
    yu "Why?"
    tb "Because...you said “capiche.” That’s Italian."
    yu "Oh, no shit? Had no clue. The fuck’s “va bene” then?"

    scene tsubasamall26
    with dissolve

    tb "It means, like...{i}fine.{/i} Or {i}okay.{/i} I was submitting to your demands and agreeing to get naked and jump into a lake with you and all of your delinquent friends."

    scene tsubasamall27
    with dissolve

    yu "Atta girl. Proud of you, Nee-sama."
    tb "I don’t want them staring at me, though. I’ve never been nude in front of anyone before. Let alone in a garbage-infested lake."
    yu "Roger that. I’ll make sure everyone but you spends the entire day with their eyes closed. This is a completely reasonable demand."
    tb "..."
    tb "{size=-10}I don’t mind if {i}you{/i} see me.{/size}"

    scene tsubasamall28
    with dissolve

    yu "You say something back there? Couldn’t hear you over the-"
    tb "Nope. Nothing at all."

    play sound "static.mp3"
    scene tsubasamall29 with flash
    stop sound

    tb "{size=-10}Just as warm as I remember...{/size}"
    yu "You say something back there? Couldn’t hear you over the-"

    scene tsubasamall30
    with dissolve

    tb "Hey, it’s not too late to stop by the lake, is it?"
    yu "Which lake? The fuck you wanna do that for?"
    tb "Just a spontaneous decision. No reason for it, really. "

    scene tsubasamall31
    with dissolve

    yu "Mind if we take a rain check then? Told Sara I’d clean the bar for her tomorrow morning. "
    tb "I can just hire someone to clean it for you instead. A whole team, perhaps. She wouldn’t need to pay a dime and it’d be much faster."
    yu "No can do, Nee-sama. This ain’t about money. It’s about tryin’ to get back to where I was before everything went to hell. Means I’ve gotta be “responsible” and shit."
    tb "Of course...If that’s what you feel you need to do, I have no right to try and hold you back."

    scene tsubasamall32
    with dissolve

    yu "You good back there? Seem a little...{i}quieter{/i} all of a sudden."
    tb "Just a little nostalgic is all. I missed this."

    scene tsubasamall33
    with dissolve

    yu "Yeah — cause gettin’ dragged around by some delinquent on a bike was {i}way{/i} better than whatever the fuck you were doin’ in your ivory tower."
    tb "Would {i}you{/i} have been happy if you were stuck in that tower with me, Yuki?"
    yu "I am {i}now.{/i} And it ain’t been that bad so far. Not a fan of that fancy shit you keep making me eat, though. Not sure how you do it."
    tb "Then why don’t we stop somewhere {i}cheap{/i} for dinner so you’re not {i}forced{/i} to eat anything fancy again?"
    yu "Now you’re speakin’ my language. Have anythin’ in mind?"
    tb "Hmm..."

    scene clearnightsky
    with dissolve2

    tb "Have you ever heard of “tacos?”"
    yu "What?"
    tb "They’re a Mexican dish that-"
    yu "I know what a fuckin’ {i}taco{/i} is, Nee-sama. Just wasn’t expectin’ to hear that from a princess like you."
    tb "Oh, splendid! Then, take us to the subway. I know a place where we can get them."
    yu "Subway tacos. This has gotta be the least boujee thing you’ve ever suggested."
    tb "It’s the least I can do after making you wear that dress."
    yu "Heh. It’s always gotta be a fuckin’ trade with you. Hold on tight, okay?"
    tb "This is why {i}I’m{/i} rich and {i}you’re-{/i} ahh! Yuki?!?! This speed...can’t be legal!"
    yu "It’s not! But it’s fun as hell, ain’t it?!"

    scene black
    with dissolve2

    "Perhaps it was a good thing that the only one who could see them was the moon, for Tsubasa Tsukioka had a difficult time being herself in front of anyone else."
    "And for a while, it felt to her as if she’d never get to be that again."
    "It came with a tinge of guilt, though — for she’d opened the door of a cage she bought in hopes that a forest bird would fly into it on its own."

    stop music fadeout 10.0

    "That she’d be content watching it grow fat under her supervision and thrive in false captivity."
    "But she was the one who filled that cage with berries and seeds, so it all still felt a little forced. Like it was only there to eat."
    "But perhaps if she kept waiting, it would one day land on her shoulder."
    "The thought of that alone was enough to keep her going when all else began to crumble."

    $ renpy.end_replay()
    $ tsubasaspring6 = True

    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    "You've received a picture message from Maya Makinami!"

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
