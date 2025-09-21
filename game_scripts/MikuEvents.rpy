label mikupool:
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        if chap4active == False:
            jump satmorningmenu
        else:
            jump ch4morningmenu
    if chap4active == True:
        jump mikuspringpoolgen
    if chapthreeactive == True:
        jump mikusummer2poolgen

label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
    if miku_love >= 5 and soccer5 == False:
        jump soccer5
    if miku_love >= 10 and soccer10 == False:
        jump soccer10
    if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
        scene soccerfield
        with dissolve
        "I show up at the soccer field to try and talk to Miku but she immediately runs off and starts talking to one of the other girls."
        "Am I...being avoided?"
        "I should probably try visiting her dorm sometime to figure out what's going on with her..."
        jump saturdayafternoon
    if miku_love >= 15 and day83 == True and mikudorm10 == True and soccer15 == False:
        jump soccer15
    if miku_love >= 20 and soccer15 == True and soccer20 == False:
        jump soccer20
    if miku_love >= 25 and mikudorm15 == True and halloween14 == True and soccer25 == False:
        jump soccer25
    if miku_love >= 30 and mikudorm25 == True and soccer30 == False:
        jump soccer30
    if miku_love >= 35 and mikudorm30 == True and day271 == True and soccer35 == False:
        jump soccer35
    elif christmas7 == True:
        jump mikusoccergen2
    else:
        jump soccer2to4

label callmikumorning:
    if miku_love >= 40 and day > 5 and makotospring1 == True and chinamispring3 == True and mikuspring4 == False:
        jump mikuspring4
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        jump callmorning
    if chapthreeactive == True:
        "Miku should be at the pool right now. I should go there if I want to see her."
        jump callmorning
    else:
        "Miku should be at the soccer field right now. I should go there if I want to see her."
        jump callmorning

label callmikuafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        jump callafternoon
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    if miku_love >= 50 and christmastwo20 == True and mikudorm45p2 == True and mikuspecial50 == False:
        jump mikuspecial50
    else:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        play sound "phonebeep.wav"

        mi "Heya!"
        mi "Need something, Sensei?"
        mi "I was just about to head over to the park to do some laps. Wanna join me?"
        s "Didn't you literally just finish soccer practice?"
        mi "Yup! Which means it's time for practice round two! You comin' or not?"
        s "I'll come, but there is no way I am going to do any actual running."
        mi "That's fine! Just be a creeper and sit on the bench while ya watch my bag or somethin'!"
        mi "I'm going to the one near the[school], so just come there whenever ya can! Bye bye!"

        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene mikugennoon
        with dissolve
        play music "highspeedprinter.mp3"

        "I show up at the park to find Miku waiting for me on the ledge of a fountain."
        "She must have come directly from practice since she still has her bag with all of her stuff in it."
        "I have absolutely no idea how she's filled with so much energy that she needs to wash down practice with {i}more{/i} practice-"
        "But I guess there's still a lot I don't really understand about Miku in the first place."
        "After spending a few minutes talking to me, it becomes clear that she's getting anxious and needs to get the rest of her energy out."
        "I agree to watching her things and then subsequently watch {i}her{/i} as she takes off down the walking trail, carefully avoiding several women out walking their dogs or their children."
        "Well, I guess you don't technically {i}walk{/i} children. But you might as well considering they're essentially useless."
        "More people should just get dogs."

        scene black with dissolve

        "Miku only winds up running for ten minutes or so before deciding to call it for the day and spend more time with me."
        "But, with the sun already starting to set and daylight beginning to die out, I decide it's best to just walk her back to the dorm and get on with the rest of my night..."

        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku's affection has increased to [miku_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label callmikunight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        jump callnight
    if chap4active == True:
        jump mikuspringnightgen
    if chapthreeactive == True:
        jump mikusummer2nightgen
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        play sound "phonebeep.wav"

        mi "Heya Sensei! How're ya doin'?"
        mi "You realize what time it is, right? Why call so late?"
        s "I require immediate assistance, Miku. It is urgent."
        mi "Urgent?! What the heck happened?! Is everything okay?!"
        s "Yes. Everything is fine."
        s "However, everything would be {i}more{/i} fine if you were to accompany me to a fast food restaurant right now."
        mi "The heck, Sensei?! Ya had me worried sick!"
        mi "But okay! I'll hang out with ya. I already ate dinner though, so..."
        mi "Actually, I can eat fries. Yeah, I'll eat fries. Fries are always good."
        mi "Just gotta make sure I burn 'em off in the morning and-"
        s "We are missing out on precious burger time."
        mi "Say no more! Miku Maruyama, out!"

        play sound "phonebeep.wav"

        "Miku hangs up without the two of us ever deciding on a meeting place."

        scene black
        with dissolve

        "I wind up texting her an address to a restaurant between my house and the dorm and start making my way over."
        "........."
        "......"
        "..."

        scene mikugennight
        with dissolve
        play music "soda.mp3"

        "Miku winds up ordering a ton of food without realizing that she had made a promise to herself just moments earlier to only eat fries."
        "In her defense, though, she {i}did{/i} wind up purchasing two large orders of them, so it's not like they completely slipped her mind."
        "If anything, I can just help her finish them so she doesn't wind up with cholesterol issues that destroy her future as an athlete."
        "Or...I can simply use that as an {i}excuse{/i} to eat them considering she has no future as an athlete."
        "None of us have any future as anything other than what we are now."
        "Time is what pushes all humans to improve and grow. And with that cut out of the mixture, Miku has no reason to ever do more than she's currently doing right now."
        "Continue to grow and cherish your youth, Miku."
        "You only have X years left of it."

        mi "Sensei? You doin' okay?"
        mi "Want some of my fries?"
        s "..."

        scene black with dissolve

        s "Yes."
        s "I want all of them."

        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku's affection has increased to [miku_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mikuinvite:
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        jump callnight
    if mikuinvite1 == False:
        jump mikuinvite1
    if mikuinvite1 == True and mikuinvite2 == False:
        jump mikuinvite2
    else:
        jump mikuinvitegen

label mikuinvitegen:
    play sound "phonebeep.wav"

    "I tap on Miku's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    mi "Miku reporting in! To what do I owe the pleasure, Sensei?"
    s "Hey. I was just wondering if you were up to anything tonight."
    mi "Is that your wiener wondering? Or your heart?"
    s "Uhh-"
    mi "Say no more cause Miku Maruyama ain't got nothin' else to do and'll take up the job!"
    mi "Oh, but if Makoto asks, I never saw ya. Don't even know where you live."
    s "You two have literally come here together on multiple occasions."
    mi "Weird. Musta caught whatever your memory disease is when you splooged all over my face."
    s "Please don't say that ever again."
    mi "Aye aye, sir! Now, buckle your seatbelt and scotch-guard the corners cause I'll be there quicker than ya can say David Beckham!"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene mikuinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    mi "Thanks for the invite, Sensei. Was startin' to wonder when I'd get to be alone with ya again."

    "How should I spend my time with Miku?"
    menu mikuinvmenu:
        "Hang Out (Raise Affection)":
            jump mikuinviteaff
        "Licking (Raise Lust)":
            jump mikuinvitelicking
        "Fingering (Raise Lust)":
            jump mikuinvitefingering
        "Headpat":
            jump mikuheadpat

label mikuinviteaff:
    scene mikuinvitegen
    with fade

    "Somehow, I get talked into playing video games with Miku again. And while it's not my favorite (Or anywhere remotely close to a favorite) activity, it is nice getting to be this close to her."
    "I've come to find recently that the Miku outside of my bedroom is worlds apart from the person she is {i}inside{/i} of here."
    "Of course, it's extremely plausible that this is due to her newfound affinity for orgasms...but I'd like to think that it's a little more than that."
    "I'd like to think that in here, despite what anyone with all of their brain cells intact would say- she feels safe."
    "She knows that if things were to go wrong and she were to have yet another panic attack...that she would have someone to protect her."

    scene black
    with dissolve

    "But instead, she just has me."
    "Someone who has failed to do that time and time again- and will continue to fail so long as there is a shallow crevice to sink my cock into."
    "Miku is important to me. That much is inarguable. But she's also just one more naive soul unfortunate enough to cross the path of someone who can never return her innocent, heartwarming gaze."
    "As her eyes peer into the twisted vines of my own, falsely illuminated by the light of a television and made into something less disgusting, she gets wrapped up in all she thinks I am."
    "And I beat her in a game that she should have won."
    "But it's not because I am better than her."
    "It's because she'd already lost everything the moment she walked in."

    $ miku_love += 3
    stop music fadeout 5.0

    "{i}Miku's affection has increased to [miku_love]!{/i}"

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mikusoccergen2:
    scene mikusoccergen2
    with dissolve
    play music "highspeedprinter.mp3"

    "Miku and the others are holding practice inside of the gym today on account of the cold, which I am incredibly thankful for."
    "I mean, I don't think soccer would really go over well in the snow anyway-"
    "But I'm just glad I don't have to deal with standing around freezing to death while everyone else runs in circles and keeps themselves warm."
    "I've gotta admit, I admire the team's dedication."
    "I've been coaching them for months now (You could even say I've been coaching them since the summer) and they've yet to even play a game."
    "And I doubt anything like that would be possible if it weren't for this girl right here."
    "Even though all of these outdoor-loving people are trapped inside, Miku is able to keep spirits high with her never-ending abundance of energy."
    "But what I like most about her is that she's still able to find time for me in the midst of all of that."

    scene black
    with dissolve

    "And of course, as soon as I think that, she tells me she needs to go back to focusing on practice and that I should pay attention as the coach."
    "The thing is, I don't even get paid for this."
    "So of course, I decide to leave before I'm roped into doing anything coach-like and simply move on with my day."

    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku's affection has increased to [miku_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label firsttimesoccer:
    scene sky
    with dissolve2
    play music "highspeedprinter.mp3"

    "You know, after being reborn into a world where I’m suddenly expected to fulfill the role of a teacher, I didn’t really expect to be using my {i}free time{/i} to hang out at school as well."
    "But here I am, drenched in sunlight and making my way over to the soccer field for reasons unbeknownst to even me."
    "I’m not sure what I expect to get out of this exactly, but I do know that at least one of my students is a member of the soccer team, so I'm {i}really{/i} hoping she’s there."
    "Otherwise, I’ll just wind up looking like some creepy older guy wandering around the premises."
    "Which, in all fairness I kind of am. "
    "It’s just significantly {i}less{/i} creepy if I know someone and can fall back on them."
    "Even if...the person I’d be falling on is a foot shorter than me and would likely snap in half from the pressure."

    scene mikunewsoccer1
    with fade

    "I manage to spot Miku gathering up some rogue soccer balls and shouting things to a group of girls who appear to be heading back to the gym."
    "Not knowing what else to do and still mildly worried about appearing as a stalker, I make my way over to her."

    s "Hey, Miku. Good morning."

    scene mikunewsoccer2
    with dissolve

    mi "Heya! Mornin’, Sensei!"

    scene mikunewsoccer3
    with dissolve

    mi "Wait, Sensei?! What are you doin’ over here?! You some kinda stalker now or somethin’?"

    "Damn it."

    s "No. In fact, I only approached you so I {i}wouldn’t{/i} look like some kind of stalker."
    mi "So...you’re stalkin’ me to...{i}not{/i} look like a stalker? I don’t get it."
    s "I’m not stalking anyone. I just happened to be in the area and thought I’d come say hi or something."

    scene mikunewsoccer4
    with dissolve

    mi "Works for me! I hereby grant you one Miku Maruyama “Daytime Stalking Pass!”"
    mi "In fact, take a whole box of ‘em! I give you permission to show up whenever ya want from this point on!"

    scene mikunewsoccer5
    with dissolve

    mi "How come ya gotta be at school on the weekend, though? Thought all you teachers were out doin’ math problems with each other or somethin’ on those days."
    s "Teachers have lives too, you know. "
    mi "Sure don’t look like it if you’re-"
    s "I’m just very good at my job. Can we stop talking about teaching now?"

    scene mikunewsoccer4
    with dissolve

    mi "Heck yeah we can! That kinda stuff always puts me to sleep anyway."
    mi "So, you lookin’ to learn about soccer or somethin’? Haven’t really seen ya drop by the field at all and I ain’t buyin’ that you’re just here to say hi."

    scene mikunewsoccer6
    with dissolve

    mi "Wait a sec! You ain’t here to become the new coach, are you?!"
    s "Coach? Absolutely not. I have zero interest in soccer and I {i}really{/i} am only here to say hi."

    scene mikunewsoccer7
    with dissolve

    mi "Guh."
    s "Guh?"

    scene mikunewsoccer8
    with dissolve

    mi "God! Can’t a girl say “Guh” around here without a teacher jumpin’ down her pants?!"
    s "I think you mean “throat” but please proceed."

    scene mikunewsoccer9
    with dissolve

    mi "Sorry for snappin’ at ya, Sensei. It’s just been all downhill since our last coach got knocked up and had to get put on baby-watch or whatever they call it."
    s "I believe that would be “maternity leave.”"
    mi "I don’t care what it’s called. All I know is that we’re startin’ to fall behind and we were {i}already{/i} havin’ a tough time trainin’ for nationals."
    s "Nationals? Are you guys really that good?"

    scene mikunewsoccer10
    with dissolve

    mi "Good? No way. "
    mi "A few of us are pretty awesome- me being one of ‘em of course. But a lot of the girls are like headless chickens out there, Sensei. It’s pure chaos."
    mi "I was kinda hopin’ this was gonna be like a sports anime and you were gonna show up and be all like “I used to play soccer before I stepped on a landmine” and then drop knowledge bombs on us."

    scene mikunewsoccer3
    with dissolve

    mi "Oh, crud! Sorry for wordin’ it like that. I’m sure it ain’t easy hearin’ the word “bomb” used so casually after the whole thing with your leg."
    s "Again, I know absolutely nothing about soccer and I am mostly confident that I have never stepped on a landmine."

    scene mikunewsoccer11
    with dissolve

    mi "Today just keeps gettin’ worse..."

    scene mikunewsoccer12
    with dissolve

    mi "Guess it wouldn’t change much even if I did get my sports anime wish, though. "
    mi "With the whole space war thing goin’ on, none of us are allowed outside of the barrier anyway."
    mi "With no teams from other prefectures to play, it’s kinda like the entire soccer team is just one giant, headless chicken."
    s "Do you know any other analogies or is that the only one?"

    scene mikunewsoccer10
    with dissolve

    mi "I don’t even know what an “analogy” is so that’s probably the only one."

    "I guess the journal thing in my room was right about Miku not being the brightest girl out there."
    "It wouldn’t be fair if she was gifted in both sports {i}and{/i} studies, though. It’s normally just one or the other for people."
    "Or neither, if you’re really unlucky."
    "But hey, at least Miku’s got {i}something.{/i}"

    s "I guess definitions aren’t really important as long as you’re not failing all of your tests. "
    mi "..."
    s "You’re failing all of your tests, aren’t you?"

    scene mikunewsoccer13
    with dissolve

    mi "You’re my teacher! Shouldn’t you know?! "
    mi "Makoto’s doin’ all she can to help me, but there’s only so much room in my brain for all that smart person stuff!"
    mi "I swear, I really don’t get why she wants to stay friends with me sometimes when I’ve got pretty much nothin’ I can do for her."
    s "You and Makoto are friends?"

    scene mikunewsoccer4
    with dissolve

    mi "Best friends, actually! Roommates too. We’re like two peas in a pod if the...pod only had two peas in it? How many peas are normally in a pod? "
    s "I have no idea, Miku."
    mi "Some kinda teacher you are. Not knowin’ about peas and showin’ up to soccer practice to stalk the star player."
    s "Hey, I have unlimited daytime stalking passes. I am allowed to be here."
    mi "Didn’t say ya weren’t. I think it’s great that ya wanna spend so much time around young girls. Means you’re still in touch with your youthful side."
    s "Yup. That is exactly what that means."
    mi "You like any kinda sports at all, Sensei? Baseball? Tennis? Hermit crab racing?"
    s "Not really. I’ve always- wait, what was that last one?"
    mi "Hm? Tennis?"
    s "No, the...actually, forget it. I don’t like any sports. "
    s "In fact...I don’t really like anything now that I actually think about it."

    scene mikunewsoccer3
    with dissolve

    mi "Well then how the heck do ya look all muscley and stuff? If ya didn’t just tell me you’re some kinda couch potato, I’d think you were workin’ out all day every day!"
    s "This is just how I am, I guess. I’m sure your looks wouldn’t change much either if you just...dropped out of the team or something."

    scene mikunewsoccer14
    with dissolve

    mi "Miku Maruyama droppin’ out of the soccer team? No way. There’s a better chance of you findin’ the guy responsible for blowin’ off your leg."
    mi "I love soccer. I love the rush. Runnin’ around with my friends...goin’ out to family restaurants after practice..."
    mi "Even cleanin’ up all the balls is kinda fun when ya get to do it with people ya like bein’ around."
    s "Well, I am very sorry for standing between you and your affinity for balls."

    scene mikunewsoccer15
    with dissolve

    mi "You ain’t standin’ between anythin’, Sensei! I like bein’ around you too!"
    mi "If I didn’t, I woulda asked you to leave a while ago."
    mi "Besides, the fact that you’re still here makes me confident that I can get ya to agree to bein’ our new coach!"
    s "No."

    scene mikunewsoccer13
    with dissolve

    mi "At least think about it, would ya?! If we don’t get a new coach by the end of the season, the school is gonna disband us!"
    s "Are they really?"
    mi "Well...they haven’t come out and said that! But that’s what would happen if this was a sports anime!"
    s "You really need to stop equating your real life sports club to the clubs in cartoons, Miku."
    s "Though...I definitely wouldn’t be surprised if your club {i}was{/i} disbanded for the reasons you mentioned."
    s "I’m sure there are like...health hazards or something if all of you are here over the weekend unsupervised."

    scene mikunewsoccer12
    with dissolve

    mi "It ain’t like we need supervision. Heck, it ain’t even like we need {i}coaching{/i} on account of the lack of teams for us to play against. "
    mi "We just need somebody who doesn’t mind occasionally bein’ around a bunch of girls in tight shorts to sign their name on a sheet of paper so we can keep doin’ what we love doin’."
    s "That really should have been your pitch from the get go. That sounds a lot more enticing."

    scene mikunewsoccer16
    with dissolve

    mi "Just wait ‘til ya see my vice captain. She’s got thighs so crazy they’ll give ya nightmares. Abs so hard they’ll...give ya nightmares too!"
    mi "What I’m gettin’ at is that you’re gonna have a bunch of nightmares, Sensei! So you better be prepared!"

    "As much as I like the idea of surrounding myself with other versions of Miku...I really don’t know if I’ll have the time to do this whole coaching thing."
    "There’s no way it will be as easy as just signing my name on a sheet of paper and staring at thighs."
    "Especially not when even keeping up with this conversation has been harder than normal for me."

    s "I...don’t know, Miku."

    scene mikunewsoccer4
    with dissolve

    mi "Then I’ll just have to keep botherin’ ya!"
    mi "You do plan on comin’ back, right? I’m sure I ain’t alone in thinkin’ that a boy bein’ around might help some of the girls kick it into overdrive, if you know what I’m sayin’."
    s "I want that to be a compliment, but I’m pretty sure it’s because almost all of the other men around here are gone."
    mi "That just means you’ve got more options to choose from! Tons of young, spunky soccer players- ripe for the pickin’!"
    s "For someone who loves being around her friends so much, you sure don’t seem to have a problem with handing them off to someone twice their age."

    scene mikunewsoccer17
    with dissolve

    mi "Think of ‘em as bargaining chips, Sensei. If you start dependin’ on ‘em and then I cut off your supply...you’ll {i}have{/i} to be our coach."
    mi "And that’s the bottom line, cause Miku Maruyama said so."
    s "Miku."

    scene mikunewsoccer7
    with dissolve

    mi "Guh. Don’t say it. It’s hard enough to stay motivated when all ya can do is run around in circles like some kinda-"
    s "If you mention headless chickens again, I am going to deflate every soccer ball on this field."

    scene mikunewsoccer13
    with dissolve

    mi "Hold on there, Bill Belichick! You think you can just walk onto {i}my{/i} soccer field and start touchin’ {i}my{/i} balls?! You ain’t earned the right!"
    s "That’s fine, because hearing you word it that way killed any desire I would have possibly had to do it anyway."

    scene mikunewsoccer17
    with dissolve

    mi "Mwahahah! Miku Maruyama wins again! A true champion of justice and soccer!"
    s "But not Nationals."
    mi "..."
    s "You know. Since you’ll never be able to make it, I mean."
    mi "..."
    s "..."

    scene mikunewsoccer18
    with dissolve

    mi "Gimme back that friggin’ day pass."

    scene black
    with dissolve2

    "Miku revokes my box of imaginary day passes, but that’s okay."
    "Because even if I have no intention of becoming the coach of this team, I still plan on showing up again."
    "Just like how I plan to learn more about Miku and ultimately use that as leverage to find my way into her extremely tight shorts."
    "That still seems miles away at this point, of course."
    "But something about seeing her sprint toward her goals makes me want to sprint toward mine..."
    "Even if they’re on the opposite side of the world."
    "As I turn around to leave the field, a ball crashes into my back with so much force that it almost knocks me over."
    "I think about glancing behind me to see whether or not this was intentional-"
    "But the sudden addition of Miku’s childish laughter blending in with the pre-existing medley of vigorous youth answers that question better than any glance possibly could."

    $ renpy.end_replay()
    $ firsttimesoccerfield = True
    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label soccer2to4:
    play music "highspeedprinter.mp3" fadein 2.0
    scene soccerfield
    with dissolve

    "I walk over to the soccer field to see how Miku and the rest of the team are doing."
    "She notices me right away and runs up to me with the same level of excitement as always."

    if soccer20 == True:
        "I thought her enthusiasm might have died down a bit after I became the coach, but it's become easily apparent that this is not the case."
        "Regardless, I take a seat on the sidelines and watch as a group of attractive and fit [teenage]girls kick a ball around."
        "It's something I wouldn't mind watching all day, but eventually practice comes to an end and I need to find something else to do..."

    else:
        "Just like she does every time I'm here, Miku tries coaxing me into being the new coach."
        "Knowing absolutely nothing about soccer, I decline and Miku goes back to yelling
        at the rest of the girls to speed up."
        "I stay and watch for a little while before realizing that I probably
        look like a creep and decide to get on with the rest of my day..."

    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label soccer5:
    scene sky
    with dissolve2
    play music "highspeedprinter.mp3" fadein 3.0

    "I kick some dirt up as I make my way across the soccer field first thing in the morning."
    "Why I've decided to take my chances on conversing with the most energetic creature I have ever encountered less than an hour after waking up? I have no idea."
    "But I'm here now, so...I guess that means I should be making the best of it."
    "That aside, I'm here relatively early today. So chances are I'll have some time to kill before Miku and the others shows up."
    "I'm not exactly excited to spend this surplus of time alone, but I guess it will give me some time to think over whether I want to actually {i}coach{/i} this team or not."
    "On one hand, doing that would probably mean waking up earlier a lot more often...and that doesn't sound fun at all."
    "But on the other hand, it may enable me to seduce a congregation of tomboys- and that sounds significantly more interesting."

    s "..."

    "You know, maybe it's good that I came a little early? At least now I can-"

    mi "Heya! Sensei! Over here!"

    "At least now I can forget I ever thought that and get locked into a conversation with Miku."

    scene soccerfive1
    with dissolve

    mi "Mornin', Sensei! Come to watch me practice again?"
    s "Looks that way. And for a second, I thought I may have beaten you here."

    scene soccerfive2
    with dissolve

    mi "Ha! You're gonna need a lot of practice if you ever expect to beat me here. Not even rain or snow can stop Miku Maruyama from bein' the first one to practice every morning."
    s "Well I'm glad that it's always sunny in Kumon-mi because I'm beginning to believe you might freeze to death if it wasn't."

    scene soccerfive3
    with dissolve

    mi "Hey, yeah. That is kinda weird, isn't it?"
    s "You tell me. I've only been here for [totaldays] days so it's not like it's {i}that{/i} weird for me just yet."
    mi "The heck is that supposed to mean? You some kinda alien or robot the government sent over?"
    mi "Oh! Or maybe you're not the real Sensei at all and this is one of those body swap thingies! Like in that one movie with all the lens flares!"
    s "I have absolutely no idea what you're talking about, but I feel like that second one has a chance to be true."

    scene soccerfive1
    with dissolve

    mi "Just don't let Makoto know. She likes the normal Sensei a lot and I don't know how she'd handle some country girl bein' the one inside of you all of a sudden."
    s "I'd much prefer to be inside of the country girl in that scenario."
    mi "You would be! That's how body swaps work. You'd be inside of her and she'd be inside of you."
    s "Well, that just sounds difficult and painful. But anyway, where is everybody else right now?"
    mi "Idunno. Probably still wakin' up or somethin'."
    s "You’re the captain, aren’t you? Shouldn’t they get here whenever you show up?"
    mi "I mean...I guess so? I ain't holdin' it against anybody if they don't wanna be as early as me, though."
    s "Here's hoping that doesn't come around to bite you in the ass one day."

    scene soccerfive4
    with dissolve

    mi "Ain't much to bite in the first place."
    s "..."
    mi "..."
    s "I can't tell if that silence means you want me to compliment your ass or not."

    scene soccerfive2
    with dissolve

    mi "Sensei, if there's anything I've learned from Netflix documentaries, is that it's probably best to never compliment a schoolgirl's butt."
    s "What an extremely specific thing to be the {i}one{/i} piece of information you leeched from documentaries."

    scene soccerfive5
    with dissolve

    mi "I kinda only pay attention for the first ten minutes or so anyway, so it ain't like that info has anywhere to go."
    mi "'Sides, my brain's filled to the brim with soccer stuff so there ain't even room for all that smart person mumbo jumbo."
    s "I'm sure you could be plenty smart if you applied yourself, Miku."

    scene soccerfive6
    with dissolve

    mi "Applied where?"
    s "Okay, nevermind."
    mi "I’m confused."
    s "You know what? Why don't we talk about something you do understand. Like...soccer."
    s "Why exactly do you want me to be your coach again?"
    mi "Because the last one got knocked up and we're gonna get disbanded if we don't find a new one."
    s "So...it doesn't have to be me. It can be anyone?"
    mi "Pretty much, yeah."
    s "You're not very good at selling things, Miku."

    scene soccerfive7
    with dissolve

    mi "Selling?! I gotta {i}pay{/i} you now?!"
    s "That...That would be {i}buying,{/i} wouldn't it?"
    mi "I don't friggin' know! I've been lost since you started talkin' about butts!"
    s "I will do my best to resist bringing them up in the future, but I will also inform you now that I will likely fail."
    mi "So...wait, are you gonna be the coach or not?"
    s "I'm still not sure. I don't know the first thing about soccer. Hell, I barely even remember all the names of my students. There's no way I can memorize the entire team."

    scene soccerfive1
    with dissolve

    mi "Really? I thought learnin’ names that quick was like a special ability all teachers were just born with."
    s "Well, first off, we aren’t born as-"
    s "Well...{i}most{/i} people aren't born as teachers."
    s "But even the ones that {i}are{/i} still have to practice memorizing names."
    mi "Really? Then...do you have any special talents at all, Sensei? It doesn't have to just be boring teaching stuff. Could be anything."

    if bonus == True:
        s "I...guess I'm good with my hands?"
    else:
        s "I am exceptional when it comes to braiding hair."

    scene soccerfive7
    with dissolve

    if bonus == True:
        mi "What do you mean? Like givin' massages or somethin’?"
        s "Sure. Why not?"
    else:
        mi "Woah! Ya must be really good with your hands, then!"
        s "I am okay, I suppose. I just like how hair feels against my skin."

    scene soccerfive8
    with dissolve

    mi "Well, that’s just one more reason for you to be coach, then!"

    if bonus == True:
        mi "Never underestimate the value of a good massage on an athlete’s muscles!"
        mi "Plus, think of all the girls you’d get to rub without ever seemin' like a weirdo!"
        s "There is no possible way things would work out that easily."
        mi "Sure it would! Silence 'em all with those magic hands of yours!"
        s "Can I just...give the massages without doing the coaching thing?"
    else:
        s "It is?"
        mi "Yeah! Lots'a girls on the team would love gettin' their hair braided!"
        s "But I am a human male and you are all human females. Someone could get the wrong idea."
        mi "Hmmmm..."

    scene soccerfive7
    with dissolve

    mi "That might be kinda hard explainin’ to everybody..."
    mi "Especially on account of most of ‘em not havin’ any experience with boys and stuff."
    s "Are you implying that you {i}do{/i} have experience with boys, Miku?"

    scene soccerfive9
    with dissolve

    mi "Huh?"
    mi "Me?"
    mi "The heck are you talkin’ about?"

    if bonus == True:
        mi "Have you {i}seen{/i} me? I’m built like a ten year old boy. "
        mi "Goin’ on a date with Miku Maruyama would be like...askin’ out your little brother."

        scene soccerfive1
        with dissolve

        mi "I don't care, though! I don’t really have time for stuff like that anyways. Gotta focus on soccer and stuff."
    else:
        mi "I don't got time for that kinda stuff when I'm so determined to become the best soccer player in all of Kumon-mi!"

    scene soccerfive2
    with dissolve

    if bonus == True:
        mi "Plus! My growth spurt should be comin’ any day now! Don’t be surprised if I wind up even bustier than Futaba this time next year!"

        "I am trying to picture that and I...can't really see how it would work."

        s "Maybe...aim for someone closer to Rin's size if you're going to have goals like that. I don't know if Futaba is at a level you'll ever be able to reach."
        s "She’s honestly kind of unreal for someone your age."

        scene soccerfive6r
        with dissolve

        mi "Right?! You could knock over an ice cream truck with those puppies!"
        s "But...why would you-"
    else:
        mi "Plus! I've still gotta get ripped so that if anyone ever pulls a sword out on the field, I'll be able to deflect it with my abs!"

    scene soccerfive1
    with dissolve

    mi "You just could, okay? And hey, why are you even here so early?"
    mi "We started talkin’ about body swaps and stuff right away so I never found out. You have some kinda...teacher meeting or something?"
    s "Maybe I was just really excited to see you?"
    mi "Yeah, I ain't buyin' that. What's the real reason?"
    s "No real reason, I guess. Thought about heading over to the cafe beforehand, but that...never happened."
    mi "The one Rin works at? Makoto loves that place."
    mi "She always gets this weird drink with caramel in the name."
    mi "It’s like a caramel marshmallow or something."
    s "I think that would be a...caramel macchiato?"
    s "I guess that drink fits her, though. Sweet and mildly complicated."

    scene soccerfive2
    with dissolve

    mi "And totally hot, right?"
    s "..."
    mi "{i}Right?{/i}"
    s "Miku, do you have a crush on Makoto?"

    scene soccerfive6r
    with dissolve

    mi "What?! No!"
    mi "She just told me she’d buy me lunch if I said nice stuff about her to you. I didn't mean to make it sound like I was tryin' to score with her!"
    s "Makoto is...paying you to 'talk her up' to me?"

    scene soccerfive2
    with dissolve

    mi "You bet! And for the low, low price of 500 yen, I can deliver a message for you as well!"
    s "Are you some sort of used car salesman now? Because I thought we figured out that selling things wasn't right for you."

    scene soccerfive4
    with dissolve

    mi "With my grades, I might have to be."
    mi "You don’t have to take any sort of fancy test to become a car salesman do you?"
    s "I don’t think so?..."
    s "But is that something you really want to do?"

    scene soccerfive5
    with dissolve

    mi "I don't know. I haven’t really thought about the future like that."
    s "You haven’t? I was under the impression you just wanted to be a soccer player or something."

    scene soccerfive1
    with dissolve

    mi "I mean, that’d be awesome, yeah. But even someone as good as me isn’t a sure shot to make the Olympic team..."
    mi "Or...any sort of professional team, for that matter."
    mi "I always hear people sayin’ stuff like “Miku! You need a backup plan! What if your leg snaps in half or your arm gets bitten off by a shark!”"
    mi "And I’m just over here like, “Sharks aren’t even real!”"
    mi "And then Makoto is all like “What are you talking about?! Of course they are!”"
    mi "And so I’m all like “You’re not my mom, Makoto! Gimme my 500 yen for tellin’ Sensei you’re a caramel marshmallow!”"
    s "Miku, I think you need to sleep more."

    scene soccerfive2
    with dissolve

    mi "Heheh...I’m just pullin’ your leg this time."
    mi "I’m sure I'll be fine with whatever happens to me after high school."

    scene soccerfive9r
    with dissolve

    mi "Yeah, I might not make it as a soccer player or used car salesman or whatever-"
    mi "But as long as I can find somethin’ that makes me happy, that’s all that matters, right?"
    s "..."
    mi "..."

    play sound "whistle.mp3"
    scene soccerfive11
    with dissolve

    mi "Oh! Here come the other girls!"
    mi "Hey! I'm over here with our future coach!"
    mi "Kirin! Make sure you wear your shin guards this time! If your sister kicks you in the leg again, don’t come cryin’ to me!"

    scene soccerfive1
    with dissolve

    mi "Sorry to break up our meeting, but I’ve gotta get to practicin’ for real now, Sensei."

    if bonus == True:
        mi "But it was fun talkin’ to you and stuff! Keep thinkin’ about that coachin’ offer if you ever want to rub some [teenage]legs!"
        mi "Or just drop by whenever you want to hang out! So long as I'm not practicin', I mean."
    else:
        s "I will miss you dearly and wish you the best of luck in your athletic journey."

    scene black
    with dissolve2

    "Miku gets up and sprints over to the rest of her team, jumping into the arms of a taller looking girl before I even have a chance to respond."
    "I wonder what she meant by finding ‘something that makes her happy...’"
    "I'm sure she's not the only person who hasn't been thinking that much about the future...but she should probably have at least {i}some{/i} sort of idea and-"

    s "..."

    "My thoughts of Miku's future are interrupted by a stampede of exposed thighs and form fitting spandex."

    $ renpy.end_replay()
    $ soccer5 = True
    $ miku_love += 1
    stop music fadeout 3.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer10:
    scene soccerfield
    with fade
    play music "highspeedprinter.mp3" fadein 3.0

    "I make my way onto the soccer field in a slightly better mood than normal- probably on account of how many thighs I am going to see today."
    "Perhaps it's a little more than that, though?"
    "Perhaps I actually {i}enjoy{/i} spending time with Miku and...trying to keep up with her bullet-train of thought or something?"
    "Hell, at this rate, I might actually wind up becoming the coach of this team."
    "That is, assuming it doesn't hurl a wrench at my {i}extremely busy{/i} schedule as the world's worst teacher."
    "Does that analogy still work when the wrench is being thrown {i}at{/i} something rather than inserted {i}into{/i} something? I don't know."
    "Besides, how busy can coaching a girls’ soccer team possibly be when they don’t even play any games?"

    mi "Senseiiiiii!!!!!"

    with hpunch

    "I’m suddenly assaulted as Miku crashes into my back at full speed."
    "She does her best to wrap her arms around my abdomen in an alarmingly friendly greeting hug, but doesn’t find much success as her hands can barely touch one another."

    mi "Woah! Your abs are super hard, Sensei. I knew you were muscley, but this makes it seem like you're some kinda bodybuilder or somethin'."
    s "Nope. Not even close. The only exercise I ever really get is just...walking around town."

    scene nightvisionredux1
    with fade

    "Miku releases her death grip on my suspiciously hard abdomen, allowing me to turn around and actually face who I'm speaking to."

    mi "You know, if ya ever wanna get some more exercise, I’m always around!"
    mi "Maybe I could be your personal trainer or somethin'? First three lessons are free."
    s "{i}I{/i} would need to be paid in order to convince me to run with you, Miku. That is not a thing I...ever want to do."
    s "At least not until you learn to calm down a bit."

    scene nightvisionredux2
    with dissolve

    mi "Oh, come on! You think I’m some kinda slave-driver or somethin'?"
    mi "I’m totally fine with just joggin' if your stamina ain't all that great. That's what I have to do with Makoto whenever I can convince her to come with me."
    mi "Heck, I could even give ya a piggyback ride if you get tired!"
    s "I would literally crush you."

    scene nightvisionredux3
    with dissolve

    mi "Nuh-uh! I could totally lift you up!"
    s "Please don't try."
    mi "Well, I kinda have to now."
    s "You really don't."

    scene nightvisionredux4
    with dissolve

    mi "Prepare for liftoff, Sensei!"

    "Miku once again takes position behind me and wraps her arms around my body. Or at least...tries to."
    "She arches her back and bends her knees, attempting to lift me up, but obviously failing due to the fact that I’m more than double her weight."

    mi "Guh...What the heck is this? How are you this heavy? I can lift up Kirin just fine."
    s "I have no idea who Kirin is, but I am going to guess she is not a six foot male with suspiciously hard abs."

    scene nightvisionredux5
    with dissolve

    mi "Maybe I should practice on her sister before I try pickin' you up again?"
    s "Maybe. Or, here's an even better idea, you could just...give up."
    mi "Whatever. I know when to accept defeat. "

    scene nightvisionredux1
    with dissolve

    mi "But yeah! If ya ever wanna run around or anything like that, I promise I won’t blow ya out of the water!"
    mi "Or if you just wanna come grab a snack with me and Makoto, that’s okay too!"
    s "Did Makoto pay you to say this?"

    scene nightvisionredux2
    with dissolve

    mi "Hahaha! Not this time, I promise! This invitation is 100%% Miku-approved!"

    scene nightvisionredux1
    with dissolve

    mi "It's only a matter of time 'til you become our coach, so we should probably start gettin’ to know each other better anyway, right?"
    s "You sound pretty confident that this is a thing I’m going to eventually do."
    mi "I am confident! Why else would ya keep showin’ up here?"
    s "You do realize I'm a teacher right? Being at school is kind of my job."
    mi "Mhm! But have you ever seen any other teachers around here over the weekend?"
    s "Actually...no. I haven’t."
    mi "Yeah, that's what I thought! Take a friggin' day off sometime, Sensei!"

    "Huh...I can't tell if it's weird that I've yet to bump into any other teachers around here yet."
    "I've obviously seen some other staff members around, but...none on the weekend."
    "Which...I guess makes sense if there aren’t any other clubs with weekend practice."

    scene nightvisionredux6
    with dissolve

    mi "All jokin' aside, we kinda need you, Sensei!"
    mi "The other teachers don’t really care about our team now that the normal coach is havin’ her baby and stuff."
    mi "I've heard from some of the other girls that they're calling our club pointless without any real opponents."
    s "I mean...isn't it?"
    mi "Heck no! That ain't it at all! We're all here for one reason and one reason only! To be a part of a team and to have fun playin' soccer."
    s "That would be two-"
    mi "Bein’ part of a team means hangin’ out and practicin’ every day...and helpin’ each other through tough times!"
    mi "We're like a big family over here!"

    "A family, huh? I guess I can see that."
    "That reminds me, I don’t really know anything about Miku’s family yet."
    "I wonder what they’re like?"

    s "Hey Miku, I was wondering-"

    play sound "whistle.mp3"
    scene nightvisionredux7
    with hpunch

    mi "GUH! Can't we invest in a...quieter whistle or something?"
    sg "Miku! We still need those extra cones for our drills! Can you get them or should I just send Kirin instead?!"
    s "Oh, good. A chance to find out if Kirin is actually a six foot male."
    mi "Shoot. I totally forgot I was supposed to be doin’ stuff."
    s "Aren’t you the captain? Why’s that tall girl bossing you around like that?"
    mi "I’ll get em in one sec! Sorry about that!"

    scene nightvisionredux6
    with dissolve

    mi "That tall girl is Karin Kanda. She’s the vice-captain of the team and ain't really tryin' to boss me around."
    mi "She’s been wantin’ to try more of that ‘bein’ in charge stuff’ lately, so I figured I’d let her take the reins today."

    scene nightvisionredux1
    with dissolve

    mi "Oh! Here's an idea! Wanna help me carry all the cones out so we can get back to talkin' faster?"
    mi "Your arms are a lot bigger than mine so we can probably do it all in one trip with the two of us!"
    s "Sure. I don't see any problem following a teenage girl into a dark storage room with tons of other girls watching."

    scene nightvisionredux6
    with dissolve

    mi "Problems? Whatcha mean? "
    s "..."
    s "Nothing at all, Miku. Just lead the way."

    scene black
    with dissolve2

    "Miku starts sprinting over to a storage room attached to what I believe is the school gym and I am forced to jog just to keep up with her."
    "I think about looking behind me to see if anyone is watching but, after realizing that might make me look even {i}more{/i} suspicious, I elect to keep my head down instead..."
    "........."
    "......"
    "..."

    scene painisreal1
    with dissolve2

    mi "So! Here we are! Home sweet home!"
    s "Would you mind explaining to me why we just stepped over a mattress?"
    mi "Doesn't every storage room need a mattress?"
    s "...No?"
    mi "I obviously know that, Sensei. The mattress is just a thing Kirin set up so she could slack off during practice."
    mi "Pretty sure she dragged it here by herself and none of us wanna get rid of it, so...I guess we've just got a mattress now?"
    mi "Kinda works out, though, since the storage room doubles as our medical tent thingy for now."
    s "Isn’t the actual nurse’s office connected to the soccer field?"
    mi "Yeah, but she doesn’t come in on weekends."
    s "Huh..."

    scene painisreal2
    with dissolve

    mi "You got some kinda problem with mattresses, Sensei? Yer actin' all weird all of a sudden."
    s "Nope. If anything, I'm glad to have such a convenient mattress stashed away in such a discreet location."
    mi "For what? You gonna sneak in here to take naps during school or something?"
    s "Close. I'm sure you’ll find out eventually."

    scene painisreal3
    with dissolve

    mi "Well, Idunno what the heck you’re talkin’ about, but I’m gonna start grabbin’ some cones."
    mi "If we’re in here for too long, the girls might get the wrong idea or somethin’."

    scene painisreal1
    with dissolve

    mi "You start grabbin’ all the ones in the corner near the door and I’ll get the ones over here in the back, got it?"
    s "Got it."

    scene painisreal4
    with fade

    "I turn around and begin searching my side of the room for any cones we might be able to use for the girls’ drills."
    "I can make out one tucked away behind a-"

    stop music
    play sound "imscared.mp3"
    with hpunch

    s "...!"
    s "Jesus...what the fuck was that?"
    sg2 "Sorry, sorry! Rogue soccer ball! Everything's okay!"

    "I can hear a set of footsteps outside of the door as one of the girls comes over to retrieve the apparently {i}rogue{/i} soccer ball."
    "I guess someone must have kicked it a little too hard or...too far or something and it wound up bouncing off of the door."

    s "Shouldn't they be playing a little more...I don't know, carefully?"
    s "You guys might wind up breaking something at this rate."
    mi "..."
    s "..."
    s "Miku?"

    play sound "static.mp3"
    scene help
    with flash
    stop sound

    "67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20
    67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20
    67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 "
    play sound "static.mp3"
    scene help2
    with flash
    scene painisreal5
    with flash
    stop sound
    play music "painisreal.mp3"

    mi "{i}Hah...hah...hah...hah...hah...hah...ahhhhh...{/i}"
    s "..."

    play sound "static.mp3"
    scene help3
    with flash
    scene painisreal6
    with flash
    stop sound

    mi "{i}Hahhhh...Ahhh...ahhhhh...hahhhhh...AHHHhhh..AHHH...HAHHHHHH...{/i}"
    s "..."

    play sound "static.mp3"
    scene help4
    with flash
    scene painisreal7
    with flash
    stop sound

    mi "{s}AHHHH!!!!AHHHHAHHHHAH!!!HAHHAHHH!!!h{/I}"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal8
    with flash
    stop sound

    mi "{b}AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!{/i}"

    "I’m frozen in place as I watch Miku begin to claw at her scalp with her fingernails."

    mi "{i}Ahhhh.....hah...hah......AHHHHH!!{/i}"

    "She won’t stop screaming."

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy9
    with flash
    stop sound
    scene painisreal8

    s "Miku...what’s going-"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal9
    with flash
    stop sound

    mi "{b}DON’T COME NEAR ME!{/b}"

    play sound "static.mp3"
    scene painisreal8
    with flash
    stop sound

    mi "GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY"
    mi "GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY"

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy9
    with flash
    stop sound
    scene painisreal10

    "A world without light, where nightvision plays messiah."
    "Where good little boys and good little girls are gifted with forgiveness."
    "Come with me!"
    "To a better place!"
    "Let us {s}GET AWAY{/s} escape this hell together!"
    "Do your eyes play tricks on you?"
    "If so, close them!"
    "Relinquish yourself to me and the two of us can spend our lives together!"
    "Time matters not!"
    "Fear matters not!"
    "All that matters is us!"

    scene painisreal11

    "Pain is real!"
    "Happiness is real!"
    "Everything is real!"
    "A whole new world awaits us!"
    "信じて！"
    "信じて！"
    "信じて！"
    "信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal8
    with flash
    stop sound
    play sound "slidedoor.mp3"

    sg "What’s going on in here?!"

    "Two girls from the team run into the storage room and surround Miku."

    scene painnew1
    with dissolve

    mi "{b}NO! GET AWAY FROM ME! LEAVE ME ALONE! GET AWAY GET AWAY GET AWAY!{/b}"
    sg "Oh my god...but...how?..."
    sg "What happened?"
    sg2 "I...I kicked a ball and...and it hit the door...The noise must have-"
    sg "Miku. Miku, it's me. Karin. Everything is okay. You're fine."

    scene painnew2
    with dissolve

    sg2 "We...we were just playing...I didn’t mean to-"
    ka "Kirin, let me handle this."
    ka "Miku, listen to me. You're safe. We're here for you. "
    mi "{i}Hah...hah...hah...hahhh...ahhhhh...{/i}"
    ka "Good girl...Just like that...Deep breaths...In and out...In and out..."

    "The girl to my left begins to coach Miku through some breathing exercises as I stand here absolutely useless."
    "What...could have caused this?"
    "What happened to her?"

    scene painnew3
    with dissolve

    ka "Sensei...I’m sorry, but could you please leave us alone for now?"
    ka "She’ll be okay."
    ka "She’s just a little scared, that’s all."
    s "Oh, uhh...yeah."
    s "I’ll go."
    s "Are you sure you’ve got this under control?"
    ka "I am. It's not the first time something like this has happened."
    ka "Kirin will come with you. It would be best if I did this alone."
    ki "But I...I can..."

    scene painnew4
    with dissolve

    ki "Okay..."
    ki "I..."
    ki "I really didn’t mean to-"
    ka "Just go. We’ll talk about it later."

    scene black
    with dissolve2

    "I exit the storage room alongside Kirin, enveloping myself in the sounds of urgent consolation bleeding through the large metal doors."
    "Something is wrong."
    "Something is very wrong."

    stop music
    scene ohno

    "{i}Oh no! It looks like Miku may have ripped out some of her hair!{/i}"
    "{i}Will you still think she’s pretty when it's all gone?{/i}"

    $ renpy.end_replay()
    $ soccer10 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer15:
    scene sky
    with dissolve
    play music "highspeedprinter.mp3"

    "I show up at the soccer field to see how Miku’s practice is going."
    "It's another early day, so I wouldn’t be surprised if it was just her here right now."
    "I slowly make my way across the school grounds, listening close for the sound of a whistle or...anything to signify that practice is in session-"

    mi "Sensei! Over here!"

    "But the noise I hear before anything is Miku's voice, calling out to me before I even know where she is."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikukarin1
    with dissolve2

    mi "Heya! Come to watch us kick some balls around again?"
    s "As long as they’re not mine."
    ka "...............ah."
    s "Good morning to you as well, Karin."
    s "Is Miku making you carry her around the field as training or something?"
    ka "That...That wasn’t the plan, but..."
    mi "We’re just helpin’ each other stretch so that we’re all loosened up when it comes time for the main event later!"
    s "Is what you're doing really going to loosen Karin up? Shouldn't you...maybe switch positions every thirty seconds or something?"

    scene mikukarin2
    with dissolve

    ka "I think I might be a little too heavy for Miku to carry like this..."
    mi "Karin’s gettin’ plenty loose by bendin' over like this, Sensei!"
    s "Can you say that again, but in a more seductive voice?"
    mi "I've never tried a seductive voice before, so I'm gonna say no!"
    mi "I guess this is more like strength training for her, though. But hey, if I get a chance to ride a friend, I'm gonna ride a friend."
    ka "I'm also not sure if this...even counts as strength training since Miku is by far the lightest girl on the team..."

    scene mikukarin3
    with dissolve

    mi "Hey! Less talkin’ and more stretchin’! If you lose focus, you’re gonna drop me and I’m gonna break my ankles!"
    mi "I need my ankles to do...ankle stuff! Like running and...jumping! And..."
    mi "Ankle stuff!"
    ka "I'm going to try and stay quiet so...Miku can keep doing ankle stuff..."
    s "Miku, you should be nicer to the girl who’s keeping you suspended in mid-air right now."

    scene mikukarin4
    with dissolve

    mi "Hey! Who do ya think you’re talkin’ to?! I’m the captain of this ship and if I say starboard you better do whatever the heck that means!"
    s "Isn’t that just a part of the ship?"
    mi "That's it! You're walkin' the plank!"
    ka "Sorry, S...Sensei...Miku is unusually fired up today..."
    s "Any reason why?"

    scene mikukarin5
    with dissolve

    mi "Oh! That’s right! I totally forgot to tell ya, but we’re havin’ a full-on practice game between the girls later on."
    mi "We’re probably gonna be here all day so if you wanna stick around and watch, you totally should!"
    s "Maybe. We'll see how I feel once the afternoon rolls around."
    s "You really have enough players for a practice game, though?"
    mi "Well, normally we wouldn’t. But Karin’s on the softball team too, so she pulled some strings and got a few of them to agree to play!"
    s "You’re on two teams at once, Karin? Isn’t that a little tiring?"

    scene mikukarin6
    with dissolve

    ka "Oh, no! Not at all!"
    ka "I love pretty much all sports, so I figure out how to make it work."
    ka "Sure, it can be a little tiring at times...but it's not like there's really anything else I have to do other than studying."
    ka "Plus, my body was...kind of built for stuff like this, so it’s a lot easier on me than it would be on someone like my sister."
    mi "Where is Kirin, by the way? I thought she was gonna show up early too?"

    scene mikukarin7
    with dissolve

    ka "Who even knows? That girl is always doing her own thing."
    ka "It’s going to get her into trouble one day, I just know it..."
    s "Karin, are you really okay just...continuously balancing Miku like that? You’ve barely moved since I got here."

    scene mikukarin8
    with dissolve

    ka "Oh, right. Miku is on my back. I totally forgot."
    mi "Am I..."
    mi "Am I really that light?..."

    scene black
    with dissolve2

    "Karin arches her back and forces Miku to dismount."
    "Fortunately, Miku does not fall and her ankles remain intact, ensuring that she will still be able to do {i}ankle stuff{/i} in the near future."
    "Whatever that means."

    scene mikukarin9
    with dissolve

    mi "Sorry Karin, I’d offer to lift you up and stuff, but I’m pretty sure you’d crush me."
    ka "I don't weigh {i}that{/i} much...And you can't just {i}only{/i} train cardio, Miku. You need to be training your entire body."

    scene mikukarin10
    with dissolve

    mi "I know, but...You’re just so muscley that there’s no way I’d be able to even get you off the ground! It'd be a lost cause!"
    s "Didn’t you try to pick me up the other day? I’m bigger than Karin."

    scene mikukarin11
    with dissolve

    mi "Yeah and how well did that work out? It was more like a backwards bear hug than anything else."

    scene mikukarin12
    with dissolve

    mi "I’m sure Karin could do it, though! She’s probably even stronger than you, Sensei!"
    mi "You should look at her abs!"
    mi "Karin! Lift up your shirt and show Sensei what you’re working with!"

    scene mikukarin13
    with dissolve

    if bonus == True:
        ka "W-w-what?!? N-n-no way!"
        ka "There’s...There's no way I could ever do something like that! Not in a gazillion years! Is gazillion even a number?!"
        ka "Would Sensei even {i}want{/i} to see something like that?! Because I sure as heck wouldn't if I was him! No way! Nuh-uh!"
        s "Not gonna lie, I kind of want to see."
    else:
        ka "Whssashshshahshashahshshshshshshabbbbabbbbbbbbbba!!!!!"
        s "Bless you."

    scene mikukarin14
    with dissolve

    ka "Why?!"
    ka "Also, is it just me or am I really loud right now?!"
    mi "Hehehe..."
    mi "This...{i}This{/i}, children...is the scent of love."

    scene mikukarin15
    with dissolve

    ka "L-L-L-L-L-LOVE?!?!?"
    ka "Miku! W-What are you talking about?!"
    mi "Sensei, as ya can see, Karin ain't very good with boys. She has this thing where whenever she tries to talk to one, she gets all...broken."
    ka "Miku! What do you think you’re telling him?! H-H-He doesn’t want to hear-"
    s "Not gonna lie, I kind of want to hear."

    scene mikukarin16
    with dissolve

    ka "Why are you doing this to me?!"
    ka "Do you like watching me suffer?!"
    s "Of course not. I just think you’re really cute when you get flustered and I’d like to see a little more of that side of you."

    scene mikukarin17
    with dissolve

    ka "C..."
    ka "..."
    ka "Huh?"
    ka "..."
    ka "C..."
    ka "What?"
    ka "What did you say?"
    ka "What’s-"
    ka "Where am I?"

    if bonus == True:
        mi "Ahh, youth..."
        mi "Sunburn...sweat...hormones running wild..."
        mi "What a time to be alive."
    else:
        s "Kumon-mi."

    ka "C..."
    ka "C...C...C...C..."
    s "Wow, she really {i}is{/i} bad with boys."

    scene mikukarin18
    with dissolve

    mi "Duh! Ya think your old pal Miku would lie to ya about something as silly as that?!"
    mi "We’re brothers in arms, Sensei! We’re gonna take on the world!"
    s "What does that have to do with the way Karin handles men?"

    scene mikukarin19
    with dissolve

    mi "Idunno. But it’s fun, right? Just look at how her eyes get all squinty whenever she doesn’t know what to say."
    ka "C...C...C...C..."
    s "Cute."

    scene mikukarin20
    with dissolve

    ka "MMMMMMMMMMMMM!!!!!!!"
    s "Wow. This {i}is{/i} actually kind of fun."

    if bonus == True:
        s "What do you think would happen if I touched her?"
        mi "Like I’ve been sayin’! If you become our coach, you could probs even rub those monster-thighs whenever ya want! Doesn’t that get your blood pumpin’?!"
        s "Yes. Though, not in a way that is exactly safe or acceptable in the middle of a soccer field."
        mi "Hm? Whatcha talkin' about?"
        s "Nothing. Just don't look down."

        scene mikukarin20r
        with dissolve

        mi "Well, of course I'm gonna look down if ya-"

        scene mikukarin21
        with dissolve

        mi "WOAH! WHAT THE HECK IS GOIN' ON DOWNSTAIRS?!"
        s "Something that will very likely kill Karin if she breaks out of her trance state."

    else:
        s "If I was not dedicated to educating women like you two, I may even contemplate asking her on a date to see if her behavior toward me adjusts in any form."

    scene mikukarin22
    with dissolve

    ka "C...C...C...C..."
    mi "I..."
    mi "I suddenly feel...kinda dizzy..."
    s "Want me to take you to the nurse's office?"

    scene mikukarin23
    with dissolve

    mi "To do what?! I ain't goin' anywhere with ya 'til you take the friggin' rocket launcher out of your pants!"
    s "I can assure you that the last thing you want right now is for me to remove {i}anything{/i} from my pants."
    s "Or the first. I don't really know with you yet."

    scene mikukarin24
    with dissolve

    mi "Somehow...gettin' even...dizzier..."
    ka "C...C...C...C..."

    "Well, then. This has certainly turned into a strange situation."

    if bonus == True:
        mi "Sensei...will I ever be able to see again?..."
        mi "We've got the...practice game today and...I've gotta..."
        ka "G-game?..."
        ka "Oh...right...we have a game..."
        ka "We need to...practice...for the..."
        ka "For the game..."
        s "Karin, open your eyes."
        ka "I can't...I closed them too tightly and now they are shut forever."
        mi "Aren't guns...illegal in Japan, Sensei? Where'd ya...get your hands on one that size?..."
        s "You know what? I think maybe you two need a little time to recharge."
        ka "To...recharge..."
        ka "Y...Yeah..."
        ka "Miku...let's go...recharge..."
        mi "Yeah...Yeah, we've...we've gotta...do the thing..."
        s "That's right. Go do the thing and I'll..."
    else:
        mi "I think we are under attack!"
        s "It must be a part of the space war. They are dropping chemicals on the soccer field causing the two of you to act strange."
        s "I will now go and defeat the aliens."
        s "If I do not return, please tell my accountant I appreciate her."
        mi "Good luck, Sensei! You'll need it!"

    scene black
    with dissolve2

    "I'll go do something about the cause of all of your problems..."

    if bonus == True:
        "I leave the two incredibly hormonal soccer team members to their own malfunctioning devices and attempt to get on with my day."
        "I just...wind up taking a quick trip to the nearest restroom first."
    else:
        "I activate my super legs and jump into space."
        "I land on a space ship and destroy ten aliens before having to jump back down."
        "I can only hold my breath for so long."

    $ renpy.end_replay()
    $ soccer15 = True
    $ miku_love += 1
    stop music fadeout 4.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer20:
    scene soccergirls0
    with dissolve
    play music "highspeedprinter.mp3"

    "I decide to spend yet another morning at the soccer field."
    "I feel like I’ve been doing that a lot lately."
    "It’s a little taxing coming all the way to[school] first thing in the morning, especially on the
    weekend, but I’ve managed to somehow get used to it on account of that whole ‘teaching’ thing I do."
    "Combine that with the fact that my trips here are normally pretty exhausting to begin with and it’s surprising that I’m still even showing up."
    "Who would have thought I’d get so hooked on hanging around a girls’ soccer team?"

    if bonus == True:
        "Sure, there are the skin tight shorts...the thigh-highs...the toned and developing muscles..."
        "..."
        "Actually, it does make sense that I keep coming here when I look at it that way."
    else:
        "It's just so rewarding seeing all of their hard work pay off."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene soccergirls1
    with dissolve

    "I spot the three girls I know the names of on a nearby...whatever this
    thing is and come to a full stop several feet away without them noticing."
    "I wait a moment to find out if they are talking about me (They aren’t) before
    deciding to call out and get myself involved in the conversation..."

    menu:
        "Hey, Karin":
            $ karin_love += 1
            $ hikarin = True

            s "Hey, Karin. What are you three up to today?"

            scene soccergirls2
            with dissolve

            ka "Ah-! W-W-What?! Who’s there?!"
            s "Open your eyes and find out..."

            scene soccergirls3
            with dissolve

            ka "Oh...Umm...Hey?..."
            ka "You kind of surprised me. I didn’t even hear you coming."
            mi "Heya, Sensei. Why’d ya call out to Karin? You know she has a heart attack whenever a boy shows up."
            s "That’s precisely why I called out to her instead of you or Kirin. I
            figured it would be funnier if Karin were to get all surprised and whatnot."
            s "And, of course, I was right."

            scene soccergirls4
            with dissolve

            ka "Am I...a plaything to you?! You can’t just toy with my condition like that!"
            s "It seems a little off to call it a condition, but I’ll try to keep that in mind
            the next time I sneak up on you."
            ka "There will be more times?!"
            s "Of course. I’ll have you warm up to me if it’s the last thing I do."

            scene soccergirls5
            with dissolve

            ka "Um...well..."
            ka "I guess if you're okay with waiting...I-"
            mi "Aaaaaanyway...I’m gonna interrupt this special moment to bring you an important announcement."
            s "Wait, what?"

        "Hey, Miku":
            $ miku_love += 1
            $ himiku = True

            s "Hey, Miku. What are you guys up to?"

            scene soccergirls6
            with dissolve

            mi "Oh, Sensei! We’re just hangin’ around on the giant blue step thingy, talkin’ about life and whatnot."
            s "Why is the soccer team having a discussion about life so early in the morning?"
            s "Shouldn’t you three be practicing for whatever fake-game you have coming up next?"

            scene soccergirls7
            with dissolve

            mi "Um...It sounds kinda rude when you call ‘em fake."
            s "Well, they are, aren’t they? They don’t count for anything."
            ka "We tend to use the word unofficial, Sensei..."

            scene soccergirls8
            with dissolve

            mi "Yeah, what Karin said. And besides, all games have a purpose! Even the fa- Erm, even the unofficial ones!"
            mi "If we don’t keep practicin’ we’ll be S-O-L when it comes time to actually play a real team."
            s "Just of out of curiosity, Miku, do you know what S-O-L stands for?"

            scene soccergirls9
            with dissolve

            mi "Uh..."
            mi "Of course I do~ Hahaha..."
            s "It stands for-"

        "Hey, Kirin":
            $ kirin_love += 1
            $ hikirin = True

            s "Hey, Kirin. What’s up?"

            scene soccergirls10
            with dissolve

            ki "Huh? What?"
            ki "Oh...Uhh, hey."
            ki "I saw you coming but I didn’t really think you were going to call out to {i}me{/i} over those two."
            mi "Yeah, what gives? Did you and Kirin become secret friends behind our backs or somethin’?"
            s "No. But we do have a sort of contract together now."

            scene soccergirls11
            with dissolve

            ki "Yeaaahhhh...I forgot about that...hahaha..."
            mi "A contract? What kind of contract?"
            ka "Are you two working on some sort of...new training regimen or something?"
            s "Well, that is {i}one{/i} way to put it."

            scene soccergirls12
            with dissolve

            ki "Dude."
            s "Sorry. Couldn’t help it."
            ka "I’m confused. What other sort of contract is there?"
            mi "Yeah, now I’m kinda curious too."

            scene soccergirls13
            with dissolve

            ki "Hey! Uhh, let’s just leave it alone for now, okay? Hahahah~"
            mi "You’re actin’ kinda weird today..."
            ki "Shut up. Besides, didn’t you have something you wanted to ask him?"
            mi "Something to ask- Oh!"

    scene soccergirls14
    with dissolve

    mi "Sensei! I hereby proclaim you the new coach of the soccer team!"
    s "Wait, what?"
    s "What just happened?"
    ka "Miku decided that if you showed up today, she was just
    going to make you the coach instead of waiting for you to agree to it."
    s "Can she do that?"

    scene soccergirls15
    with dissolve

    mi "There is no limit to my power! Mwahahahaha!"
    ki "She technically can’t, but are you really gonna say no to that face, Sensei?"
    s "What face? The one she has on now?"
    mi "Tremble before me, mortal!"
    s "Kirin, are you sure this is the face you’re talking about?"
    ki "What’s wrong? I think she’s cute when she turns into a supervillain."

    scene soccergirls16
    with dissolve

    mi "Jokin’ aside, I’m puttin’ my foot down, Sensei. You’ve kept me waitin’ for far too long."
    mi "We’ve all got achin’ muscles just beggin’ to be massaged by those magic hands of yours!"
    ka "..."

    scene soccergirls17
    with dissolve

    ka "Wait, what?!"

    scene soccergirls18
    with dissolve

    mi "Yeah! Haven’t you heard? Sensei is apparently a super good moose!"
    s "Masseuse, Miku. It’s masseuse. "
    s "Also, I’m just okay. I never said I was a god."
    ka "Wait, Miku! I know you said it would be good to have him around, but I’m pretty sure he’s not allowed to like, {i}touch{/i} us..."
    ki "I don’t mind~ My legs have been suuuuuper sore lately. I’m sure some {i}physical{/i} therapy will get all of those knots out in a jiff."

    if bonus == False:
        "She must be talking about a hug."

    mi "Why wouldn’t Sensei be allowed to touch us? The last coach did it all the time and you always talked about how great ya felt after."

    scene soccergirls19
    with dissolve

    ka "The last coach was a girl, though...She didn’t have any...{i}ulterior motives...{/i}"

    if bonus == True:
        s "I can hear you, you know..."
        mi "Hmm..."

        scene soccergirls20
        with dissolve

        "Miku pauses for a moment and stares deep into my soul."
        "She doesn’t believe the whole ‘ulterior motives’ thing, does she?"
        "..."
        "Wait a second. I {i}do{/i} have ulterior motives. Why am I getting so up in arms about this accusation?"

        mi "*Ahem* Sensei. Or shall I say...Coach!"
        s "Sensei is fine."
        mi "Coach! Do you have any ulterior motives when it comes to the [young]women of the soccer team?"

        scene soccergirls21
        with dissolve

        ki "Yeah, Sensei~ You weren’t planning on doing anything {i}naughty{/i} to us, were you?"

        "Kirin, I’m really going to need you to keep it together right now..."

        s "Of course not. I won’t touch anyone how they don’t want to be touched."
    else:
        s "Neither am I. I just want you all to become better at soccer."

    scene soccergirls22
    with dissolve

    ka "Hold on a second...I’m not entirely satisfied with that answer."

    if bonus == True:
        ka "What do you mean by how they want to be-"
    else:
        s "I'm being super duper serious, though."

    mi "Sounds good to me! You’re the moose here. You know what’ll work best."

    scene soccergirls23
    with dissolve

    ka "Miku! Don’t I get any sort of say in this? I’m second in command and a year older than you."

    scene soccergirls24
    with dissolve

    ki "You're also a year older than me and I’m still like three times more mature than you~"

    scene soccergirls25
    with dissolve

    ka "You still sleep with a teddy bear, Kirin! I don’t want to hear it!"
    ka "And if you’re more mature than me, how come your curfew is an hour earlier than mine?"

    scene soccergirls26
    with dissolve

    ki "Who cares about a stupid curfew? At least I don’t start crying any time a boy looks at me."
    mi "So, Sensei-Coach-Master-"
    s "Master has been added on now as well?"
    mi "As you can see, things can get a little dysfunctional around these here parts."
    mi "So what that means is, as our new coach, you’re gonna have to keep these two in check so they stop frickin’ fightin’ all the time."
    s "Are they really always like this?"
    mi "Well...not {i}all{/i} the time. But yeah, pretty often."

    if bonus == True:
        mi "I try to step in when I can but it’s not like a pipsqueak who’s just barely outgrown her trainin' bra can really do much to someone Karin’s size."
        mi "And Kirin’s kinda scary in her own way too. Like one of those feisty types that’ll pull ‘yer hair if ya mess with her."

        "Yeah, I definitely get that vibe from Kirin as well."
    else:
        s "That is sad. Sisters should love each other as often as they can because you never know when something bad might happen to one."
        s "Death comes far too soon for far too many people."
        mi "Got that right, Sensei!"

    s "And you’re really sure about me being the coach? I think I’ve told you before, but I really can’t be here every day."

    scene soccergirls27
    with dissolve

    mi "That’s totally fine! We can always do stuff later on if ya can’t make it to the field. "

    scene soccergirls26
    with dissolve

    mi "None of us really have anythin’ to do besides soccer and trainin’ and whatnot anyway. "
    mi "So if ya ever want to just do laps around the park or somethin’ like that, you can always let
    your good pal Miku know."

    scene soccergirls28
    with dissolve

    mi "Oh, actually! I’ve got an even better idea!"
    mi "How about you take down our phone numbers?!"

    scene soccergirls29
    with dissolve

    ki "I second that! Take mine first, Sensei!"

    scene soccergirls30
    with dissolve

    "Kirin pulls a smartphone out from the inside of her shirt and types out her contact info on it before holding it up for me to see."
    "I type the numbers down in my phone and click ‘save,’ still awaiting the next two numbers."

    "{i}Congratulations! You now have Kirin’s cell phone number!{/i}"

    mi "I can’t remember...do ya already have my number, Sensei?"
    mi "We’ve been together a lot and I’m kinda forgetful, so sorry if ya
    already have it and I’m bein’ weird. Hahahaha~"
    s "Nope, don’t think so. Here, you can type it in yourself."
    mi "Coolio!"

    scene soccergirls31
    with dissolve

    "Miku runs over and rapidly types her number into my phone."
    "I’m surprised she’s able to do it so quickly. I know she’s full of energy but I
    kind of figured that would all be saved for the field, not technology."

    "{i}Congratulations! You now have Miku’s cell phone number as well!{/i}"

    mi "Kirin and I are gonna go ahead!"
    mi "Good luck tryin’ to get Karin’s number, Sensei! She’s never given it to a boy before!"

    "Miku and Kirin start jogging toward where all of the other
    girls are playing and I’m suddenly left alone with Karin..."

    scene soccergirls32
    with dissolve

    ka "Mmh..."
    s "..."
    ka "Umm...I-"
    s "You don’t have to give me your number if you don’t want to, Karin."

    scene soccergirls33
    with dissolve

    ka "Huh?"

    if bonus == True:
        s "I don’t blame you for feeling weird around guys. Especially older ones like me."
        s "If anything, I think that most of the other girls are surprisingly forward."
        ka "Um-"
        s "Besides, even if you don’t want me to be your coach, I’ll do what I can to
        make sure it doesn’t bother you or anything like that."
        ka "Uhh-"
        s "I know you’ve been on the team for a while and I obviously wouldn’t want to be stepping on your toes, but-"
    else:
        s "I don't have unlimited texting anyway, so I'll barely ever be able to talk to you."

    scene soccergirls34
    with hpunch

    ka "T-T-T-Take my number too!"
    s "..."

    scene soccergirls35
    with dissolve

    ka "Mmmnnn..."
    s "Are you sure?"
    ka "..."

    "Karin quickly nods her head up and down in place of responding."
    "I hand her my cell and, with trembling fingers, she types her phone number in. "
    "Sure, she needs to backspace some of the digits a few times, but she gets it done in the end."

    "{i}Congratulations! You now have Karin’s cell phone number too!{/i}"

    if bonus == True:
        "{i}Wow! Three phone numbers in one day! It’s almost like you’re the protagonist of a porn game!{/i}"

    ka "..."
    s "..."
    ka "..."
    s "..."

    scene soccergirls34
    with dissolve

    ka "Okay bye!"

    scene soccergirls36
    with dissolve

    "With borderline-frightening speed, Karin joins the rest of her teammates and
    absolutely demolishes them in terms of speed as they make their way around the track."
    "Somehow, I don’t even think Miku would be able to keep up with her right now..."

    scene black
    with dissolve

    if hikarin == True:
        "{i}Karin’s affection has increased to [karin_love]!{/i}"

    if hikirin == True:
        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"

    if himiku == True:
        "{i}Miku’s affection has increased to [miku_love]!{/i}"

    $ renpy.end_replay()
    $ soccer20 = True
    $ mikunumber = True
    $ karinnumber = True
    $ kirinnumber = True
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer25:
    scene black
    with dissolve

    "........."
    "......"
    play sound "slidedoor.mp3"
    "..."

    scene mikushed1
    with dissolve2
    play music "retrospect.mp3"

    "Somehow or another, Miku and I find ourselves in the storage shed once again."
    "And when I say “Somehow or another,” what I really mean is that we’re in here on clean-up duty."
    "Being miles ahead of the rest of the team (With the one other exception being Karin), it’s okay for Miku to miss out on practice every once in a while."
    "The only issue is that the atmosphere is a little strange given exactly what went down the last time Miku and I were here together."

    mi "So, uhh, good thing we got the goalie to step in and protect the storage shed from any rogue balls this time, right? Hahahaha..."
    s "Are you going to be okay?"
    s "I have literally no idea what I’m doing as a soccer coach but maybe it would be better for Karin and I to swap places until the clean-up is done?"
    mi "Naaaah...It’s totally fine. I mean, it’s not like there’s even much to clean up or anything."
    mi "We’ve just gotta collect all the spare balls and bring ‘em out for...kicking practice and stuff."
    s "Isn’t all of soccer practice just...kicking practice?"

    scene mikushed2
    with dissolve

    mi "‘Course not! We’ve also got runnin’ practice and defensive drills and all of that other stuff you should be figurin’ out since you’re our coach now."

    if bonus == True:
        s "I’m really only here for the thighs."
    else:
        s "I’m really only here for the bump in my salary."

    scene mikushed3
    with dissolve

    if bonus == True:
        mi "Yes, yes. All because Master Miku tapped into ‘yer real feelings and brought the true Sensei outta hidin’ to come touch a bunch of girls."
        s "Right. Even though I haven’t technically done any touching yet."
        mi "That sounds like a you-problem, Sensei. Pretty sure ya can just walk up to anybody and start rubbin’ em and they’ll be all like “Wow, thanks! I needed that!”"
        s "I’m pretty sure I’d get in a lot of trouble if I actually did that."
    else:
        mi "And the cute girls!"
        s "Yes, you are all cute. But I am a teacher and a coach first and foremost. I express no interest in or desire to pursue anything else with any of you."

    mi "Nuh-uh. You-"

    scene mikushed4
    with dissolve

    "I go to take a step forward to prove my point and Miku’s eyes immediately grow about six sizes larger."

    mi "Stay back, heathen! My thighs are fine! I haven’t even run yet!"
    s "See what I mean? If {i}you're{/i} reacting like this, how do you expect the other girls to react?"

    scene mikushed5
    with dissolve

    if bonus == True:
        mi "The other girls probably have experience in the sexy-department and the only experience {i}I{/i} have are those pop-ups that show up when ya illegally stream anime."
    else:
        mi "Badly! Like when I ask them torrent anime for me cause the connection in my room sucks!"

    s "Illegally streaming things is bad, Miku. You should know this."
    mi "I know, I know."
    mi "Illegally piratin’ anything is bad and should be punishable by death. "
    mi "Just kill me now, why don’t ya?"
    s "Especially when it’s something you can get for the price of a coffee."
    mi "You’re really makin’ me feel like crap, Sensei."
    mi "I just can’t stop thinkin’ about how hard the people who made all that stuff work only to have it stolen by someone as impatient and immature as me. "
    mi "I hereby promise to never pirate anything again. "

    if bonus == True:
        s "Good. Now, back to thighs."

        scene mikushed6
        with dissolve

        mi "Oh, right. That’s what we were talkin’ about."
        s "Are you sure you don’t want to seize this rare opportunity of us being alone in the shed to get a massage, Miku?"
        mi "A massage sounds pretty good but I’ve been feelin’ kinda weird around you ever since the whole dry-humpin’ incident."
        s "Makoto has brainwashed you. No humping was involved at all."

        scene mikushed7
        with dissolve

        mi "I...became a woman that day..."
        s "You really didn’t."

        scene mikushed8
        with dissolve

        mi "Anyway, we can save all that thigh-touchin’ stuff for some other time. We’ve gotta job to do and that job involves balls."
        s "Please go on."
        mi "Just gotta reach around and grab some until I can’t hold anymore."
        s "You’re making this a euphemism on purpose, aren’t you?"
        mi "Hm? Euphe...UFO?"
        mi "Ya’ hear something out there, Sensei? Should we go check?"
        mi "Space war is ragin’ on and on and we never know when the aliens might come down and enslave us."
        s "Yeah, I’m pretty sure we don’t need to worry about something like that."
        s "Let’s just focus on cleaning this place up before Karin comes in and yells at us."
    else:
        s "I am glad that we have reached that understand. Now, in order to maintain a healthy, clean environment, I propose that we commense cleaning this room immediately."

    scene mikushed9
    with dissolve

    mi "Roger that!"
    mi "Cleaning-rangers...go!"

    scene black
    with dissolve

    "Miku and I proceed to tidy up the storage shed, setting aside any spare soccer balls we can find to bring out to the field."
    "I’m not sure how all of these balls wound up in such strange places, and I’m beginning to think that someone might be intentionally placing them in weird locations to get a rise out of us."
    "What a weird prank that would be if it were true."
    "There’s even a ball inside of a bucket."
    "Why?"
    "Who puts a soccer ball in a bucket?"

    mi "Sensei! Can ya try reachin’ up on top of this shelf and grabbin’ those for me, please?"
    s "Huh? How did those even get up there?"
    mi "Beats me but it’s our duty to get ‘em!"
    s "There’s no way I can reach those. You’re going to have to get on my shoulders."
    mi "Guhh, fine! Kneel down and let me get on top of ya."

    "........."
    "......"
    "..."

    scene mikushed10
    with dissolve

    mi "Holy heck! Is this what it feels like bein’ a tall person?!"
    mi "This is friggin’ awesome! I could finally kick Karin’s butt!"
    s "Can you reach the soccer balls, Miku?"
    mi "Probably, but I’m kinda just enjoyin’ bein’ up this high. "

    scene mikushed11
    with dissolve

    mi "Lemme stay up here for a little while longer and soak-in the fact that I’ll never actually be this tall."

    if bonus == True:
        s "Have you given up on your growth spurt?"
        s "What happened to getting boobs as big as Futaba’s?"

        "Miku squeezes my head with her thighs in order to stabilize herself."
        "It’s awesome."
        "That’s all I have to say about the matter."

        scene mikushed12
        with dissolve

        mi "Stupid gigantic monster-boobs. Just who does that girl think she is? "
        mi "Imagine if I had bazongas like that? You probably wouldn’t even be able to hold me up here."
        mi "They’re probably like six thousand pounds. "
        s "Having fun up there?"

        scene mikushed13
        with dissolve

        mi "I think so. I’m not squeezin’ ya too hard, am I? "

        "{i}You’re not squeezing me hard enough.{/i}"

        s "I’m fine. "
        s "In fact, I’m surprised you’re even okay with staying up there given how hesitant you were to have me touch your thighs like five minutes ago."
        s "Why is something like this okay but that wasn't?"

        scene mikushed14
        with dissolve

        mi "Because this was necessary! We've got a job to do!"
        mi "And it’s not like I’m gonna pop a boner and stab the back of your head with it or somethin’!"

        scene mikushed15
        with dissolve

        mi "And...ngh...Watch how hard you’re grabbin’ onto my legs! That feels...really weird!"
        s "I thought your thighs were fine? They feel pretty tight to me. Maybe we should loosen them up?"

        "I dig my fingers deeper into Miku’s thighs and need to reposition my legs to ensure that we don’t topple over."
        "Granted, there’s a mattress right behind us so, if we do fall, it will probably be fine."
        "But I’d like to avoid the low chance that I actually crack her skull open and cause her to bleed out in front of me."
        "That would be a huge bummer."

        scene mikushed16
        with dissolve

        mi "S-Sensei! Stop it!"
        mi "I might look strong but I’m delicate! Super fragile! Gonna die if ‘ya keep touchin’ me like that!"
        s "You’re the one that’s taking forever to grab the balls."
        mi "I’m not ready to grab your stupid balls! I’ve been tryin’ to tell you that!"
        s "The soccer balls, Miku."

        scene mikushed17
        with dissolve

        mi "Uhh...Oh."
        mi "Well that’s your fault for sayin’ somethin’ so easy to misunderstand."

        scene mikushed18
        with dissolve

        "I can feel Miku lean forward to try and grab the balls on top of the shelf."
        "The tightness of her legs around my face eases up a bit and is replaced with the feeling of her stomach pressing against the back of my head."
        "When she’s unable to reach even then, she inches her body forward until she’s basically grinding against my neck."
    else:
        s "Sure, Miku. I understand your desire to be tall and will respect your decision to stay atop my shoulder for a slightly extended amount of time."

    scene mikushed19
    with dissolve

    mi "For real, though...who the heck puts soccer balls in such hard-to-reach places? This is madness."
    s "Just grab them unless you want me to start gripping you harder again. "

    scene mikushed20
    with dissolve

    mi "Y-Yes sir!"

    scene black
    with dissolve2

    "Miku manages to finally get the balls off of the shelf and quickly hops off of me the second I begin to lower my knees."

    scene mikushed21
    with dissolve

    mi "Well that was an...interesting sensation."
    mi "I had no idea just ridin’ on somebody’s shoulders could give me so many butterflies."

    if bonus == True:
        s "Did you not get butterflies when riding on my waist before the Halloween party?"

        scene mikushed22
        with dissolve

        mi "Not like this! This was way different for some reason!"
        s "Sounds to me like you’re becoming aware of your womanly desires, Miku."
    else:
        s "Is this your first time experiencing altitude sickness?"

    scene mikushed23
    with dissolve

    mi "Nuh-uh. I’m the same as always."
    mi "How do your shoulders feel, though? I was kinda up there for a while."
    s "They’re fine. You’re even lighter than you look, which is already pretty light to begin with."

    if bonus == True:
        mi "You sure you don’t want me to rub ‘em for a little bit or somethin’?"
        mi "I don’t mind. I give Kirin shoulder massages all the time. I’m pretty good from what I hear, too."
        s "So I’m not allowed to massage you but you’re allowed to massage me?"

        scene mikushed24
        with dissolve

        mi "Of course ‘yer allowed! Just not...today! "
        mi "Besides, ya already got a good enough feel while I was up on your shoulders, didn’t ya?"

        scene mikushed25
        with dissolve

        mi "Let ‘yer old pal Miku pay ya back for all of the weird ways you made her body feel today!"
        mi "Even the coach needs to relax every now and then, ya know?"
        s "..."
        mi "..."
        s "Sure, Miku."
        s "Do what you must."
    else:
        mi "Nonsense! Prepare yourself for a platonic shoulder massage!"
        s "But I do not want-"
        mi "I hope you are prepared!"
        s "I am not."

    scene black
    with dissolve

    "The two of us walk over to a stack of mats in the corner of the room and Miku literally pushes me onto them."
    "This is not an exaggeration. "
    "I need to use my hands to catch myself in order to prevent landing on my face and she laughs almost maniacally as she gets behind me and starts massaging my shoulders..."

    scene mikushed26
    with dissolve

    if bonus == False:
        s "Someone help."

    mi "Yes, yes! Surrender to my above-average shoulder massage skills!"
    mi "Feel the burn, Sensei! Feel the burn!"
    s "I can’t tell if you’re going for a supervillain vibe or an 80’s exercise video vibe."

    scene mikushed27
    with dissolve

    mi "Me neither. But it feels good, right?"

    if bonus == True:
        mi "Your shoulders are super stiff. When was the last time anyone helped ya relieve some tension?"

        "I’m going to go out on a limb here and assume she only means shoulder-related tension."
        "I’ve definitely had tension released in other ways on several occasions."

        s "Probably never, to be honest."
    else:
        s "I have never felt this scared in my life."

    scene mikushed28
    with dissolve

    mi "Never?! No wonder why ya feel like a friggin’ brick wall up here."

    "Miku’s fingers dig into the gaps in my shoulder blades and begin to work out what feels like aeons worth of knots."

    if bonus == True:
        "She actually {i}is{/i} surprisingly good at this."
        "I guess small hands don’t really matter much when you subject yourself to hours of athletic training every day."

    scene mikushed29
    with dissolve

    mi "Sorry for sittin’ on top of ya before, Sensei. Had no idea your muscles were so...bleh."
    mi "Even if I’m little-boy sized, it probably put more unnecessary strain on your body."
    mi "You’ve gotta take care of yourself, ya know? What good will you do any of us if ‘ya wind up gettin’ paralyzed and can’t leave the house anymore?"
    s "I’m not sure how going without shoulder massages could cause paralysis, but I’ll try to keep that in mind."
    mi "Good!"
    mi "Also, please don’t tell Makoto about this cause I’m pretty sure she’ll chop my head off even if this is just a wholesome shoulder rub."
    mi "I think she likes you, Sensei. Like, {i}likes you{/i} likes you."
    s "Wow, I wonder what gave you that idea."

    scene mikushed30
    with dissolve

    mi "Did you know she keeps a picture of you in her wallet?"
    mi "I saw it the other day when I was goin’ through her bag lookin’ for some spare change to buy a drink with."
    s "You shouldn’t be snooping through other peoples’ things, Miku."
    mi "Probs shouldn’t be giving my teacher a massage either but here I am."
    s "Yup. Here you are."

    if bonus == True:
        s "I’ll remember this when it comes time for me to cash in on the thigh-rubbing I was promised when I agreed to fill the coaching job."

        scene mikushed31
        with dissolve

        mi "Go rub one of the Kanda girls if you want thighs on-demand. I’m fine with just doin’ things like this for now."
        mi "I can’t be lettin’ things get any weirder between us when my best friend is literally walkin’ around with a mini-Sensei in her wallet."

    scene black
    with dissolve2

    "The pressure Miku applies to my shoulders eases up just seconds after she says that."
    "One minute later, the massage comes to an end and she proceeds to sit there with her hands on my back until we both get up at exactly the same time and start tossing all of the balls we collected into a bin."
    "The sunlight singes my eyes when we step outside after being trapped in the dark for so long."
    "And then, just as always, I watch Miku go on to completely dominate the other girls on the field before I step away from practice and get on with my day."

    $ renpy.end_replay()
    $ miku_love += 1
    $ soccer25 = True
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer30:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene mikudayrun1
    with dissolve
    play music "highspeedprinter.mp3"

    "I show up at the[school] much earlier than normal after deciding to skip my morning coffee."
    "Now that I’m here, however, I’m definitely regretting the decision."
    "Not only is this particular morning much colder than it should be for what is {i}technically{/i} still summer, but there’s no one anywhere to be found."
    "I guess it’s too early for even someone like Miku to show up and start...running around in circles or whatever it is she does when she’s the only one here."

    s "..."

    "A thought suddenly crosses my mind along with a strong gust of wind as I stand before an empty bench, too afraid to sit down and feel how cold it would be against me."
    "If winter is truly right around the corner, what is going to happen to soccer practice?"
    "Are all of the girls still going to show up every day when it starts dropping to freezing temperatures?"
    "Does Kumon-mi even get that cold?"

    scene mikudayrun2
    with dissolve

    mi "...?"

    "Out of nowhere, Miku comes running toward me from around the corner."
    "Her eyes widen when she realizes I’m here already, and I’m a bit curious as to why she’s wearing pants when she has practice this morning."
    "The hoodie I can understand, but I’m pretty sure pants aren’t the best for a sport that so-heavily involves lower body movement."

    scene mikudayrun3
    with dissolve

    mi "M-Morning, Sensei! "
    mi "What brings ya here so early? Also, isn’t it a little too cold to be wearin’ that same ole’ blazer?"
    mi "Where’s your winter jacket? Your scarf? Your gloves?"
    mi "Ya gotta be prepared or you’ll wind up catchin’ a cold and we’ll get a substitute teacher who actually {i}teaches{/i} us stuff."
    s "That sounds horrible."

    scene mikudayrun4
    with dissolve

    mi "It would be! I don’t even know if I remember how to write my own name."
    s "Please tell me you’re exaggerating."
    s "That seems like too much even for you."

    scene mikudayrun5
    with dissolve

    mi "Course I am. I practiced writin’ my name a bunch of times when I was little since I thought I’d be signin’ autographs and stuff once I got to college."

    if bonus == True:
        s "Still think you have a chance to make it there?"
        mi "Make it where? College or autographs?"
        s "Both?..."
        mi "Probably not, but I try not to think too much about that anymore."
        mi "Besides, now that it’s gettin’ all cold and stuff, I'm havin' a hard time focusin' anyway."
        s "I was actually just thinking, is anything about soccer practice going to change when winter rolls around?"

        scene mikudayrun6
        with dissolve

        mi "Mm...I don’t really know."
        mi "I’m a first-year so I haven’t ever seen how this[school] handles that sorta thing before."
        mi "But if it’s anythin’ like my middle[school] was, I don’t think much should change. Some girls will probably just bring hoodies or somethin’."
        s "Are they going to be bringing pants, too? "

        scene mikudayrun7
        with dissolve

        mi "Why do ya ask, Sensei? Afraid of missin’ out on some of that good ole exposed [teenager] skin?"
        s "That and the fact that you’re wearing pants right now. "
    else:
        s "Ahh, yes. College. The place we are at right now."
        s "Also, why are you wearing pants? They are going to hinder your athletic ability."

    scene mikudayrun8
    with dissolve

    mi "Oh. Well, ya see, there’s actually a good reason for that."

    if bonus == True:
        s "That reason wouldn’t happen to involve what went down in your dorm room recently, would it?"
        s "Are those pants your anti-Sensei barrier?"

        scene mikudayrun9
        with dissolve

        mi "What? Nononono. It’s nothin’ like that. "
        mi "Besides, there are much easier ways to prevent ya from gettin’ all handsy with me if I don’t want ya to."
        s "Sounds ominous. You don’t carry any weapons around, do you?"
    else:
        s "Is the reason because you are concealing a firearm?"

    scene mikudayrun10
    with dissolve

    mi "No weapons here, just the heart of a warrior! "
    mi "The real reason I’m not dressed in my jersey today is that we’re skippin’ practice on account of everybody bein' sick."
    mi "A bunch of the girls went out to some yakiniku place last night and all wound up with food poisoning. "
    s "So you’re here all by yourself? Why not just sleep in?"

    scene mikudayrun11
    with dissolve

    mi "I can’t sleep in or I’ll miss out on the exercise I need to prevent my body from going all wibbly-wobbly whenever I’m playin’ soccer."

    scene mikudayrun12
    with dissolve

    mi "And also I...thought I might run into ya here and stuff."
    s "So you woke up extra early on the weekend and came all the way to[school] in your normal clothes because you thought you might see me?"
    mi "Don’t forget about the exercise part. It’s not {i}just{/i} because of you. That’s just a little bonus I guess."

    "Adorable."

    s "Well, I’m glad I wound up coming here then. It will give the two of us a chance to talk about stuff."

    scene mikudayrun13
    with dissolve

    if bonus == True:
        mi "This isn’t gonna be one of those adult talks about the dangers of babymakin’, is it? Cause we got real close recently and I definitely ain’t ready for that."
        s "Okay well first, we did not come anywhere close to “babymaking.”"
    else:
        mi "Does it have somethin' to do with how Makoto's family still hasn't changed the name of their business to somethin' other than {i}DVD Store{/i} yet?"
        s "Firstly, yes. That is something they should do."

    s "Secondly, I mean more about just...discussing normal stuff."
    s "You said you wanted to get to know me better, and I don’t really know anything about you either other than that you play soccer and don’t like loud noises."

    scene mikudayrun14
    with dissolve

    mi "That’s pretty much all I’ve got. If you’re lookin’ for someone more unique, you’re probably better off with somebody like Kirin."

    if kirindate10 == True or ayanelust10 == True:
        "Well, she’s definitely right about Kirin being...unique."
        "I’m not quite sure if that’s a good thing yet, though."

    s "Well then it shouldn’t be a difficult conversation since I don’t have much interesting to say either."

    scene mikudayrun15
    with dissolve

    mi "Really? No crazy stories about what it’s like lookin’ after Ami?"
    s "I think it’s closer to Ami looking after me, to tell you the truth."

    "In all fairness, though, it’s not like I know anything about how things were beforehand."
    "That’s probably something I’ll need to hear from Ami or Ayane directly before I jump to any conclusions about how difficult things were."

    s "Do you want to go sit down somewhere, maybe?"
    s "I’m starting to feel a little odd just standing on this pathway talking about...whatever we’re talking about."
    mi "A whole lotta nothin’, if ya ask me. But yeah, we can go sit."

    scene mikudayrun16
    with dissolve

    mi "There’s a spot I ran past earlier that the sunlight can reach. We probably won’t freeze our butts off like we would on one of the benches either."
    mi "Nothin’ worse than a cold bench, ya know?"
    s "I mean, there are definitely worse things. But yeah, take me to your secret sunspot."
    mi "Heheh...it’s not a secret. It’s just a corner of the[school] building. "
    mi "Come with me and you’ll see!"

    scene black
    with dissolve2

    "Miku begins to walk alongside me and it feels rather...odd."
    "It’s never occurred to me before but I don’t normally see her walking. Like, ever."
    "Even on the rare occasions where we’ve gone out at night during one of my dorm-visits, it’s always centered around jogging."
    "It’s good knowing that Miku has a lower setting as well."
    "I like the high-velocity version, but a cold morning like this is definitely not ideal for the standard version of Miku, as far as I’m concerned."

    scene mikudayrun17
    with dissolve

    "The light filters through the clouds and spills onto us as we step into a sun-soaked sanctuary on the side of the[school]."
    "Miku leans up against the wall and I decide to take my place in front of her instead of off to her side."
    "Sure, my section is a little closer to the shade, but if we’re actually going to be {i}talking{/i} to each other for once, it might be helpful to see her face."
    "Not to mention, I like her face quite a bit. It’s a good face."

    mi "Sooooo...what did you want to talk about?"
    mi "I can go on and on about most stuff, but when it comes to this openin’ up kinda thing, I just sorta freeze up."
    s "Is that like, a confidence issue or something?"

    scene mikudayrun18
    with dissolve

    mi "Uhh...no. No, that’s not it at all."
    mi "Just that there’s some stuff that’s happened to me in the past that’s not really fun to talk about."
    mi "I told you that in my dorm a while ago, didn't I? After the first time ya saw me actin' all weird."
    mi "I don’t like feelin’ weak, so I try to push it away as much as I can. But there’s only so much I can push, ya know?"
    mi "I’m strong, but I’ve got tiny arms. Pushin’ stuff can be hard."

    "Oh, this is a good opportunity to be deep."

    s "You know Miku, I can-"

    scene mikudayrun19
    with dissolve

    mi "You can help me push things that are too heavy for me to push on my own. I know."
    s "What the hell? You stole my moment."

    scene mikudayrun20
    with dissolve

    mi "Yup! Makoto said the same thing when I brought up the arm thing before. And you’re really just the boy version of her."
    mi "Err, actually no. I {i}used{/i} to think you were like the boy version of her. But now you’re like...just a boy."
    mi "But you two still have glasses and talk the same so I guess you’re kinda still similar."
    s "Well it’s good knowing that I remind you of your best friend."
    mi "Yup!"

    scene mikudayrun21
    with dissolve

    if bonus == True:
        mi "Can’t say Makoto’s ever tried to put her fingers in me before, though, so that’s a thing we’ve gotta take into account now."
        s "So really, the only things Makoto and I have in common in your head are...glasses and the way we talk."
        mi "I coulda sworn there was more but I guess not."
    else:
        mi "Can’t say Makoto’s ever tried to hug me before, though...."
        s "That is so sad."

    scene mikudayrun22
    with dissolve

    mi "Do you have any cool stuff you want to tell me about {i}your{/i} past since I don’t wanna talk about mine, Sensei?"
    mi "Like I said the other day, I don’t know anything about you. Tell me some stuff."

    if bonus == True:
        mi "Like, when did ya realize you liked thighs so much?"
    else:
        mi "Like, when did ya realize you liked pretzel rods so much?"
        s "How did you know about that?"
        mi "Just tell me, idiot."

    s "Probably the first time I saw them but that’s not really something I can talk about at length."

    "At least not with Miku. I’m not trying to scare her off when we’re finally becoming closer."

    mi "That’s like me and soccer! "
    mi "The first time I ever saw a game, I was totally hooked!"

    if bonus == True:
        mi "Sure, soccer is a lot more innocent to get hooked on than a girl’s legs, but I can kinda understand more about your interests now."
    else:
        mi "Sure, soccer is a lot more normal to get hooked on than pretzel rods, but I can kinda understand more about your interests now."

    s "Can you really, though?"

    scene mikudayrun23
    with dissolve

    mi "Course I can! A hobby is a hobby is a hobby is a hobby!"
    s "I think you said “hobby” a few too many times there."

    scene mikudayrun24
    with dissolve

    mi "I don’t think so. Hobbies are important."
    mi "Ya never know when ya need somethin’ like that to help you get yer mind off of stuff."
    mi "One of the big reasons I’m as into soccer as I am is that it helps me push away all of that sad stuff I was hinting at earlier. "
    mi "Soccer makes it so I don’t need to ask people like you and Makoto for an extra set of arms when things get tough."
    mi "Just like in sports, sometimes you just need to push through."

    "Miku begins spewing out a bunch of positivity despite hiding something so big from me that she breaks down whenever she hears a loud noise."
    "Thankfully, there are no loud noises around in this quiet pre-winter morning, so she is able to maintain the illusion of happiness for the time being."
    "Of course, that illusion is bound to come crashing down at any minute and she’ll need to think up a brand new justification for why she’s disguising her past."
    "What the hell happened to her and why is it worth putting on airs to tuck away?"

    scene mikudayrun25
    with dissolve

    mi "Woah! Where’d that angry face come from?"
    mi "If I knew ya hated positive outlooks so much I would have just started cryin’ and punchin’ the wall or somethin’."
    s "Don’t punch the wall. It’s made of stone and you’ll hurt your hand."
    mi "Then snap the heck out of it and look at me normally again! "

    scene mikudayrun26
    with dissolve

    mi "If we’re gonna be spendin’ the mornin’ together, I wanna do it with smiles on our faces. None of that “I’m a bad-guy teacher! Rawr!” mumbo-jumbo."
    s "I have never once {i}rawr’ed{/i} at you, Miku."
    mi "Not yet! But you look like you’re about to! "

    scene mikudayrun27
    with dissolve

    mi "Oh! I know! Let’s talk about anime! Lemme tell ya all about this tournament arc thingy I watched with Makoto last night!"
    s "Makoto watches anime?"
    mi "Of course! Now, listen up-"

    scene black
    with dissolve

    "Miku goes on to talk about a bunch of things I have to pretend to be interested in in order to avoid bringing her down any more than my face from several minutes ago did."
    "The rest of the morning flies by and, before we know it, the sunspot consumes all of Kumon-mi and converts a temporary, cool sanctuary into another scorching nightmare."
    "But at least it’s a nightmare Miku is able to smile in."

    $ renpy.end_replay()
    $ soccer30 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label mikuwinterbeach1:
    play sound "slidedoor.mp3"

    "Makoto and I make it back to the inn to find the entire room dark and devoid of sound."
    "It’s a little disappointing knowing how quickly the day came to an end..."
    "But on the bright side, at least it means that I won’t have to figure out how to correctly answer any more of Makoto’s questions."
    "Frankly, it’s mildly miraculous that I was able to make it through the night without really pissing her off."
    "Especially since she brought up one of my least favorite topics in the idea of me fully devoting myself to one person."
    "Still, though-"
    "We wind up in the same place at the end of the day. "
    "We take our clothes off in separate rooms and reconvene in front of a mutual acquaintance of ours."

    scene mikusleeping1
    with dissolve
    play music "asobeatsex8.mp3" fadein 4.0

    mak "See? I told you she’d be out cold."
    s "Congratulations. What would you like as your reward?"

    if bonus == True:
        jump mikubeachdryx
    else:
        scene black
        with dissolve

        mak "A night of peace and quiet in separate rooms because sleeping in the same bed is unnecessary and weird."
        s "I agree. Goodnight, Makoto."

        "Makoto and I go to sleep in separate rooms, but Miku wakes up in the middle of the night to come and hug me before going back to sleep."
        "It's weird and she feels bad about it."
        "Oh well."

        $ renpy.end_replay()
        $ mikuwinterbeach1 = True
        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku’s affection has increased to [miku_love]!{/i}"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date

        jump makotowinterbeach4

label soccer35:
    scene gym
    with fade
    play music "highspeedprinter.mp3"

    "I make my way to the gym first thing in the morning to see what the girls are up to for soccer practice."
    "I immediately notice Karin leading a bunch of shorter girls in some drill that I should probably know the name of by now but can honestly just not be bothered to learn."
    "Well, to be more precise, I immediately notice Karin's thighs."

    if bonus == True:
        "Everything else comes after."
        "There’s no Miku anywhere in sight, though."
        "In fact, I don’t see Kirin anywhere either, but I guess that’s a lot more normal than having the team captain absent."
        "I begin to make my way over to Karin to ask about-"
    else:
        "But then I immediately look away because even if she is a grown woman, looking at her without her approval or consent would be rude."

    ki "Sensei! Come quick! Miku is in trouble!"

    if bonus == True:
        mi "I told ya I’m fine, Kirin! Sensei, you can go back to walkin’ around the gym lookin’ at butts and stuff!"
        ki "No, no! Come over here! This is where the best butts are!"
    else:
        mi "Help! She is trying to make me watch the third season of Seinfeld!"
        ki "Do it."

    scene black
    with dissolve

    if bonus == True:
        "Being swayed by the prospect of the alleged best butts on the soccer team, I follow Kirin’s voice and wind up in front of the stage..."
    else:
        s "I will save you, Miku."

    scene mikuankle1
    with dissolve

    ki "Sensei, quick! Miku needs mouth to mouth!"

    if bonus == True:
        mi "I don’t need friggin’ mouth to mouth for a twisted ankle..."
        s "Are you sure? Because I’ll do it."
    else:
        s "Ew, kissing."

    ki "You should do it. Just to be safe."

    if bonus == True:
        s "That’s a good idea, Kirin. Please step aside."
    else:
        s "I'd have to ask my accountant first."

    scene mikuankle2
    with dissolve

    mi "Jeez! When the heck did you two get as close as peanut butter and jelly?!"

    if kirin_virgin == False:
        scene mikuankle3
        with dissolve

        ki "..."
        s "..."
        ki "Do you want to tell her or should I do it?"
        mi "Tell me what? What are you talkin’ about?"
        s "I don’t think either of us should tell her."
        ki "Booooooring. I wanna do it."
        s "Kirin..."
        ki "Sensei~"
        mi "...Miku?"

    else:
        scene mikuankle3
        with dissolve

        ki "I don’t know if I’d go as far as peanut butter and jelly...but Sensei and I have definitely been spending a decent amount of time together."
        mi "What, for like...soccer coaching and stuff?"
        mi "You tryin’ to whip yourself into shape, Kirin?"

        scene mikuankle4
        with dissolve

        if bonus == True:
            ki "Yup. He’s working me {i}really{/i} hard too. It’s a good thing I like it a little rough."
            s "Okay, I’m going to cut this conversation off before it has any...adverse effects on me."
            mi "What...kinda routine does he have you on exactly?"
        else:
            ki "No. I just like his scent."

    scene mikuankle5
    with dissolve

    s "Okay, moving right along- what happened to your ankle? You said you twisted it?"
    mi "Yeah. Playin’ inside is a lot different from playin’ on the grass and I came down kinda hard on it since I ain’t totally used to things in here yet."
    ki "And yours truly swooped in to temporarily rescue her, knowing full well that our dearest coach would soon show up to carry her to safety."
    s "How did you know I was coming today?"
    ki "Because you always show up as soon as something interesting happens. It’s like clockwork or however the thing goes."
    mi "Yeah, it is kinda weird now that Kirin mentions it."

    scene mikuankle6
    with dissolve

    mi "I’ll be totally okay, though! I just need to run to the nurse’s office for some painkillers."
    mi "Except...I can’t really run because of my ankle and..."
    mi "You know what? Maybe I’m just doomed."
    ki "Sensei, maybe you should princess carry her to the nurse’s office?"

    scene mikuankle7
    with dissolve

    mi "No way! I watched him do that when Ayane hurt her ankle and when she came back, she was all red and...panting and stuff!"
    ki "Oh?"
    mi "Yeah! Not sure how just carryin’ somebody can make em get all sweaty and heated, but I’ll be totally fine on my own."
    s "I can assure you that the state Ayane returned in had nothing to do with the way I carried her."

    scene mikuankle8
    with dissolve

    mi "Well it sure as heck wasn’t like any ankle injury I’ve ever seen before, so explain that!"

    if bonus == True:
        ki "Yeah. Explain that, Sensei. We’re all dying to hear what went on with you and Ayane in the nurse’s office."
        mi "Yeah!"
        s "To be honest, that was so long ago now that I can’t even remember."

        "Lies. We made out behind a curtain. It was awesome."

        s "Anyway, talking about what happened back then won’t fix your ankle, Miku."
        mi "I ain’t lettin ya carry me like a heckin’ princess, Sensei!"
    else:
        s "You are right. It was horrible and unlike anything I've ever seen as well."
        s "But my time in the medical field prepared me for it and, today, Ayane can walk with only a tiny bit of shooting pain."

    scene mikuankle9
    with dissolve

    ki "You could always just give her a piggyback ride instead. That sounds a lot less romantic, doesn’t it? Pretty sure that’s the issue here."
    s "Miku, is that fine with you?"
    mi "I mean...yeah. I guess that’s okay."
    mi "I had to ride on your shoulders that one time in the shed so it’s not like I’m unfamiliar with the vehicle."
    s "I’m a vehicle now?"

    scene mikuankle10
    with dissolve

    mi "Yup! The cheapest, fastest one around!"
    ki "I want to take a ride when Miku is done."
    mi "Hop right on, Kirin! The Sensei express has enough room for everyone!"
    s "Yup. Hop right on Kirin. The real ride starts when we get to the nurse’s office."
    ki "Mmmmmmmmm...as much as I want to, I think I’ve gotta give this one up to Miku."
    ki "She could really use some of those good ole’ Sensei healing powers right about now."
    mi "You’ve got healing powers, Sensei?! You shoulda said somethin’! Now we don’t even have to go to the-"
    s "I don’t have healing powers, Miku."
    s "Now hurry up and get on my back before your ankle heals on its own."

    scene black
    with dissolve

    "I lean down to let Miku jump onto my back but she wraps her legs around my neck and decides to ride my shoulders again instead."
    "There will be no complaints from me regarding this situation."

    scene mikuankle11
    with dissolve

    mi "This is fine, right?"
    mi "I realize it’s not a piggyback ride but I feel little bit better holdin’ onto your head than wrappin’ my arms around those big ole shoulders of yours."
    s "I also feel better this way."
    ki "Have fun, you two."
    ki "I’ll cover for you if Karin asks where you went, which she probably will because she’s a buzzkill and she sucks."
    mi "No worries, Kirin! We won’t be gone long!"
    mi "Cause even though Ayane came back all red and sweaty that one time, her ankle was totally fine!"
    mi "And I’m a lot more fit than she is so I’m sure Sensei can do the same thing for me."
    s "Yup. Definitely can."
    ki "...Right."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Having Miku on my shoulders makes it rather complicated walking through the halls of the[school]."
    "Doors are a completely separate ordeal, and Miku seems entirely unwilling to help from atop her throne, so I need to bend down and nearly break my back just to get through some of them."
    "But, after a few minutes of pain that will likely force me into taking some of whatever Miku plans on taking to fix her ankle, we wind up at the nurse's office."
    "Unfortunately, Miku hops off right away, so I don’t have a chance to drop her on the bed like I did with Ayane."
    "I guess today is going to be a bad day after all."

    scene mikuankle12
    with dissolve2
    play music "love.mp3"

    "Miku slowly limps her way over to a table holding a bunch of different bottles on the far side of the room as if she’s done it a million times before."
    "It would probably make sense for the soccer team to have their own stash of this stuff, but I guess there might be some issues that arise by providing full pharmaceutical access to a bunch of [teens]."

    mi "Sorry to make ya carry me all the way here, Sensei."
    mi "I normally bring some weaker stuff with me but I forgot to refill my bottle before comin’ to practice this morning."

    "Oh. Well I guess Miku normally {i}does{/i} have full pharmaceutical access and I was wrong."

    s "Do you...have an addiction you want to talk about, Miku?"

    scene mikuankle13
    with dissolve

    mi "What? Course not. It’s not anythin’ like that."
    mi "I rarely ever get hurt during practice. I normally just keep ‘em around in case of headaches or if one of the other girls gets hurt."
    s "Is that normal?"
    mi "Course it is. Ya think those bags that girls are always carryin’ around are just filled with rainbows and sunshine or somethin’?"
    s "Well that would certainly be more exciting than Loxonin or Eve."
    mi "Yeah but a rainbow’s not gonna make your head stop hurtin’ so you should be proud of me for bein’ so prepared."
    s "If you were prepared, you would have remembered to refill your personal bottle."

    scene mikuankle14
    with dissolve

    mi "Uh...well...yeah. I guess you’re right."

    scene mikuankle15
    with dissolve

    mi "So...uhh...I guess that’s all we needed to come here for."
    mi "We can probably...get goin’ now."
    s "You sure you don’t want me to use my miracle cure on you?"

    if bonus == True:
        mi "Do you...actually have one or...is that just a thing you’re sayin’ to try and get all touchy with me again?"
        s "Woah. Since when are you this perceptive?"

        scene mikuankle16
        with dissolve

        mi "I’m a woman now, Sensei! I’ve seen the light!"
        mi "Well...felt the light when I sat on your lap that one time!"
        mi "But I’m not allowed to talk about that!"
        mi "And a woman knows when she’s about to be duped!"
        s "And yet that “woman” willingly rode my shoulders all the way here."
        mi "I did what I had to do to fix my ankle! Gotta be crafty to survive sometimes!"
        mi "That’s what Kirin always tells me at least!"
        s "Kirin probably isn’t the best role model for you, Miku."
    else:
        mi "Yes. Please use it."
        s "I just need to capture a turtle first."
        s "I will enlist the help of Kirin. She hates turtles."

    scene mikuankle17
    with dissolve

    mi "I keep hearin’ people say stuff like that about her, but I’ve never felt that way at all."
    mi "I don’t get it. She’s always so nice to me."
    s "Well that’s probably just because you’re her friend."
    mi "She’s got lots of friends, though. Like everybody in the class is friends with her."
    s "Friends or “friends?”"
    mi "What? The heck is that supposed to mean?"
    s "Aren’t there people who you call your friend despite never really spending time with them?"
    mi "I guess so, but they’re still my friends."
    mi "I’d never call somebody that if I don’t feel that way. Friendship’s a big thing, Sensei. It’s a dog-eating world out there."
    s "I...think you meant to say “dog eat dog,” but I don’t want to sidetrack this conversation."
    s "I’m sure Kirin has a lot of “friends,” but you seem to be one of the few she genuinely cares about."
    s "So you probably don’t understand what people say about her because it’s never applied to you."

    scene mikuankle18
    with dissolve

    mi "Yeah, Makoto said somethin’ similar. Just kinda hurts to hear when I know that deep down she ain’t all that bad."
    s "Well, on the bright side, her being in the class now will give her plenty of time to show that side of herself to everyone."

    "Which I can almost guarantee she will {i}not{/i} do based on my experience with her."

    scene mikuankle19
    with dissolve

    mi "Yeah..."
    mi "It’s still kinda crazy she wound up in our class, huh?"
    s "Not really. The way she talked about it made it seem like she was going to make that happen no matter what."
    mi "Class in general has just been...all sorts of crazy lately."
    mi "Specially with that roommate of hers showin’ up."
    s "Noriko?"
    mi "Yeah, that one."
    mi "You...uhh..."
    mi "You’re...really popular with all sorts of girls, aren’t you?"
    s "If you’re worried about Noriko stealing me away from the rest of you, don’t be."
    s "I wouldn’t be me if I didn’t equally distribute my incredibly valuable time among all of you girls."

    scene mikuankle20
    with dissolve

    mi "It’s not really me I’m worried about..."
    mi "Makoto’s been gettin’ all sorts of down about stuff lately and I...don’t want more girls showin’ up to stress her out even more, ya know?"
    mi "She works suuuuuper hard. And she’s really beautiful and so smart and-"
    s "Did she pay you to talk her up again?"
    mi "..."

    "I’ve gotta hand it to Makoto. She’s definitely determined, if not anything else."

    s "Listen, if Makoto wants to talk about things like that, she can talk to me herself."
    s "And if {i}you{/i} want to talk to me about things like that, the same goes for you."
    s "But I’m not going to let you act like a middleman who's out to gauge my relationships with some of the new girls for profit."

    scene mikuankle21
    with dissolve

    mi "It’s...it’s not just for profit! I’m curious too!"
    mi "We got a maid, a green haired girl who won’t talk to anybody, and a punk lookin’ girl who wants to have your babies! It’s weird!"
    mi "Course I’m gonna wanna ask about them when you’re treatin’ em the same way ya treat all of us!"
    mi "More girls means less time for you and me to go runnin’ and stuff like that!"
    mi "And less time for you to consider buyin’ a ring and tellin’ Makoto to be your-"
    s "Miku..."

    scene mikuankle22
    with dissolve

    mi "Darn it!"
    mi "How’s a girl supposed to make any cash when she can’t even hype up her BFF?"
    s "Just tell her you followed through, it’s fine."
    mi "I can’t heckin’ lie to Makoto, Sensei! She’s Makoto!"
    mi "She’ll see through me like a friggin’ window!"
    s "Well then I suppose it’s time for you to start looking for a real job."
    mi "The heck kinda job is someone like me gonna do?"
    s "I don’t know. What are you good at besides soccer?"
    mi "..."
    s "...?"
    mi "You...have any messages that need to be delivered?"


    scene black
    with dissolve2

    "I leave a message with Miku to give to Makoto, but quickly retract it once I remember that I’m supposed to pay her."
    "Miku lives the rest of her life unemployed and dies alone and poor."
    "The end."

    $ renpy.end_replay()
    $ miku_love += 1
    $ soccer35 = True
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label mikudorm45:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Miku’s door and wait for her to answer."
    "It’s the first instance of me coming here to spend time with her since the Christmas party, and while I {i}should{/i} be of the mindset that maybe things might {i}go somewhere{/i} this time-"
    "I can’t help but worry that Makoto might somehow get involved again."

    if bonus == True:
        "I was able to miraculously survive one topless Miku run-in with her (Albeit with a surprisingly painful slap) but I really don’t know if I’d be able to emerge from a second alive."
        "Considering that I haven’t heard anything from Makoto yet, though, I doubt that Miku has told her anything."
        "Which is good, because I have no idea how I’d react if I were to be suddenly confronted by the two of them at once regarding our respective relationships."
    else:
        "Every time Makoto is involved in anything, my tummy starts hurting."

    s "..."

    "Oh no."

    if bonus == False:
        "It is happening again."

    mi "Ah! One more second, Sensei! I’m...not done gettin' ready yet!"
    s "What exactly are you getting ready {i}for{/i}, Miku?"
    mi "I...can’t tell you that!"
    s "Well, that’s not suspicious at all."
    mi "Just...give me another minute! I made a mistake!"
    s "What kind of mistake would-"
    mi "Just give me a friggin’ minute, okay?! Jeez!"
    s "..."

    "You know, maybe I should just quietly back out of the hall and go find something else to do?"
    "This is likely one of those times where my inner monologue mysteriously predicts what is going to happen next, and I’m not really in the mood for a confrontation right now."
    "Or...ever, for that matter."
    "Let alone one that potentially involves someone as good at slapping as Makoto."

    mi "Okay! You can come in now, Sensei!"
    s "Before I do, can you confirm whether or not Makoto is in there?"
    mi "Makoto? No, she’s at work right now."

    "Oh."
    "I guess...Miku wasn’t getting ready for an intervention then?"
    "What else would she be getting ready for, though?"

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "I open the door to greet Miku and-"

    scene intervention1
    with dissolve2

    mi "Why don’t you take a seat, Sensei?"
    s "You know, I was really hoping I wouldn’t ever have to hear those words."
    mi "Also, Makoto is here after all. Surprise."
    s "You fucking liar."
    mak "We’re here precisely because Miku {i}isn’t{/i} a liar, Sensei."
    mak "Or rather- that she’d prefer to not keep things hidden from her best friend, despite how desperately you may want her to."
    s "Why is it okay to lie to me and not to you? That doesn’t seem fair at all."

    scene intervention2
    with dissolve

    mak "Oh, fantastic! Since we’re now on topic of what constitutes “fair,” how about you-"
    mi "{i}Ahem.{/i}"
    mi "I believe I told Sensei to take a seat, Makoto. ‘Yer gonna ruin the innervention."

    scene intervention3
    with dissolve

    mak "Ugh. Fine. Sensei, please sit down so we can proceed with this {i}intervention.{/i}"
    s "I really don’t want to."
    mi "You’ve gotta, Sensei. You’ve got two ladies wrapped around ‘yer finger and the time’s come to untangle ‘em."
    mak "There are a lot more than just two, Miku. Frankly, there are so many at this point that I doubt Sensei will ever be able to untangle all of them."
    s "Yeah, thanks for the reminder."

    scene black
    with dissolve

    "I take a seat in a third chair that Miku and Makoto set up on the side of the room and wonder why they went to the trouble of doing that instead of just letting me sit on the couch."
    "But I guess comfort is probably the least of their concerns right now, when-"

    mak "Oh, no. Don’t go getting lost in thought right now, Sensei..."

    scene intervention4
    with dissolve

    s "I should have just stayed at home."
    mi "This was gonna happen whether ya liked it or not, Sensei. It’s the only way we can settle matters once and for all."
    s "Fine. Then I pick Makoto since at least she doesn’t lie to me. Meeting adjourned."

    scene intervention5
    with dissolve

    if day > 5:
        mak "Excellent. See you in school on Monday, Sensei."
    else:
        mak "Excellent. See you in school tomorrow, Sensei."

    mi "Wait, no! The choice ain’t supposed to be as easy as that! In fact, there ain’t supposed to be a choice at all! Neither one of us expects ya to just-"
    mak "Sensei’s clearly made his decision already, Miku. I believe the only thing left for us to do is accept it."

    scene intervention6
    with dissolve

    mi "Well...yeah. I guess that would be the easiest thing to do. Definitely a heck of a lot easier for me. But I kinda figured we were gonna at least talk about it a little."
    mi "I ain’t ever liked somebody before, and I don’t want all these weird feelings cloggin’ up my brain when it’s already givin’ Usain Bolt a run for his money."
    mak "I know, I know. I was only being half serious. I’m just...not sure how to do this, though. Organizing an intervention for a love triangle is not exactly “normal.”"
    s "You know an organized meeting is bad when even Makoto isn’t into it."

    scene intervention7
    with dissolve

    mi "I’m doin’ my best, okay?! "
    mak "Let’s just...let Miku take charge of this. She’s proven to be quite effective at making the first move as of late."

    scene intervention8
    with dissolve

    s "You seem less mad at me than I expected you to be."
    mak "Oh, don’t get me wrong. I {i}want{/i} to be angrier with you. I just know that, in this case, Miku was the one who pounced on you."
    mak "All you did was buy her a present she really liked."
    mak "Granted, I’m sure there was much more that happened beforehand that ultimately {i}culminated{/i} in this all happening, but the fault isn’t yours alone."
    mak "Miku’s obviously had feelings for you for quite some time. {i}Obviously{/i} not as long as I have, but it’s not as if we can ignore those feelings when they’re just as real as anyone else’s."
    s "So much for letting Miku take charge of the meeting."

    scene intervention9
    with dissolve

    mak "I can’t believe you kissed her before me!"
    mi "Didn’t ya just admit {i}I{/i} was the one who kissed {i}him,{/i} Makoto? "
    mak "Yes, but still! "
    s "Do you want me to kiss you right now and even the playing field?"

    scene intervention10
    with dissolve

    mak "Yes, actually. I would very much appreciate that."
    mi "Wait, wait, wait! Hold on a sec! Nobody’s kissin’ anyone!"
    mak "Maybe not right now. But who knows what the fuck you two would do if I were to leave the room."
    mi "Just cause I kinda attacked Sensei doesn’t mean I think I’m at the front of the race or anythin’ like that! "
    mi "I just didn’t want us keepin’ secrets from each other anymore! ‘Specially if I’ve got the green light to go ahead and try and make sense of all these butterflies!"
    s "Green light? What are you talking about? "

    scene intervention11
    with dissolve

    mak "Did you really think I was going to stop Miku from following her heart just because it’s trailing my own?"
    mak "I’ll admit that I was hoping things would never come to this but, now that they have, what else are we supposed to do other than simply deal with them?"
    mak "Frankly, I’m {i}more{/i} comfortable with the idea of you romantically pursuing Miku than any of the other girls."
    mak "Not that I’d ever expect you to romantically pursue {i}anyone{/i} when romance is the furthest thing from your mind...but still."
    s "So what, then? I’m free to just mess around with both of you? Because if that’s the case, this meeting could have been solved with a single text message."

    scene intervention12
    with dissolve

    mi "Sensei...you know we’re not just tryin’ to “mess around,” right? Me and Makoto actually {i}like{/i} like you."
    mak "Makoto and I."
    s "What am I supposed to do about that, though?"
    mi "I don’t know...maybe just...{i}consider{/i} it when we’re all doin’ stuff together?"
    mi "The whole reason I wanted to do somethin’ like this is so we wouldn’t hurt each other’s feelings in the long run."
    mi "Both of you guys are crazy important to me, and I don’t wanna risk hidin’ anything if I think it could make stuff worse."

    "That’s a surprisingly mature outlook from one of the least mature girls I know."
    "But it’s...respectable in its own twisted sort of way."
    "How much exactly does Miku intend to share, though? Because there’s certainly one thing I can think of that I can’t really imagine Makoto just brushing off."

    s "I just feel like this is more of a thing for the two of you rather than me."
    s "If I’m not being forced to pick between you, I can’t imagine this meeting making any sort of impact on things to come."

    scene intervention13
    with dissolve

    mi "It {i}is{/i} mostly for just me and Makoto-"
    mak "Makoto and me, in this case."
    mi "But you {i}are{/i} Makoto. "
    mak "..."
    mi "Oh, I get it."
    mi "But yeah. It is mostly for us two, I guess. I just think that if everybody’s gonna be involved in this weird triangle thingy...that we should all know about it."
    mi "And that even if none of us are tryin’ to hold the other ones back...that we’re okay with whatever happens."
    s "Are you really {i}okay{/i} with whatever happens, though, Miku?"

    scene intervention14
    with dissolve

    mi "Whaddya mean?..."
    mi "Like if you decide to just go full-Makoto and ignore how I feel? Course I wouldn’t be {i}okay{/i} with it...so maybe that ain’t the best word."
    mi "I’d understand, though. "
    mi "I don’t really know how you make decisions and stuff, Sensei, but if I were in your shoes, I’d be tryin’ to hurt the least amount’a people possible."
    mi "One of us is obviously gonna get hurt. Maybe even all three. But I feel like just knowin’ that is enough to make it all hurt a little less."
    s "..."
    mak "..."
    mak "I want to give you a hug, but I hardly think this is the right time."

    scene intervention15
    with dissolve

    mi "Huggin’ your rival’s just as good as admitting defeat! We can hug when all of this is said and done."
    mak "{i}If{/i} things are ever said and done. Sensei here is so helpless when it comes to making decisions that, more often than not, I find myself making them for him."
    s "Can you do me a favor and decide that this meeting is over, then? Because if nobody has any questions-"

    scene intervention16
    with dissolve

    mi "Oh, I’ve got a question. How come ya ain’t kissed my roommate yet? "
    mak "I don’t like the bluntness with which that question was asked, but I definitely {i}would{/i} like to know the answer to that as well."
    s "Just hasn’t come up yet."
    mi "But, like..."

    scene intervention17
    with dissolve

    if bonus == True:
        mi "Ain’t you two already doin’ more...adult stuff?"
    else:
        mi "Ain’t you two already in the secret hug club?"

    mak "..."
    s "You know, I kind of assumed that when you said you two share everything that you didn’t literally mean {i}everything.{/i}"
    mi "Isn’t...goin’ straight to the major stuff like that kinda like cheating?"
    mak "Is this something we really have to discuss right now?"
    mi "Does it have somethin’ to do with how Makoto’s always surrounded by those videos? You like...doin’ her a favor to prevent her from goin’ crazy or somethin’?"

    scene intervention18
    with dissolve

    mak "Obviously n-"
    s "Yes."

    scene intervention19
    with dissolve

    mak "That is absolutely {i}not{/i} why we have been doing those things!"
    s "So if you ever find yourself going crazy as well, Miku-"

    scene intervention20
    with dissolve

    mak "Don’t listen to him. This is how he traps you into a relationship where he doesn’t {i}have{/i} to kiss you because you’ve already skipped that step. "
    mak "Run while you still can. Don’t turn into another me."
    mi "Two Makotos does sound like a little too much now that ya mention it..."
    mi "Why don’t ya just kiss him yourself, though? It ain’t that hard. Ya just kinda...go for it."
    s "Yeah, Makoto. This is all your fault and you should try and be more like Miku."

    scene intervention21
    with dissolve

    mak "Maybe {i}you{/i} should try and be more like Miku! I have done more than enough for you and deserve a reward every once in a while!"
    mi "She {i}does{/i} deserve it, Sensei. "
    s "Correct me if I’m wrong, but...aren’t you supposed to be rooting for yourself right now? "
    s "I figured the whole “Team Makoto” thing would be over with after today and that you’d try a little harder to keep me to yourself."

    scene intervention22
    with dissolve

    mi "Why would I try and keep ya to myself when Makoto likes you too? That ain’t fair at all."
    mi "I don’t see any reason why I can’t stay on Team Makoto {i}and{/i} like you. There some kinda rule against that?"
    mak "I mean...I don’t think there’s a {i}rulebook{/i} we can consult...but that’s not normally how love triangles go..."

    scene intervention23
    with dissolve

    mi "Well, maybe it ain’t really a triangle then?"
    mi "Aren’t you kinda rootin’ for me too, Makoto?"
    mak "Uhh..."
    mak "Not really?"
    mak "I obviously don’t want to hold you back from pursuing the person you admire, but if you’re asking if I’m hoping you and Sensei get closer...absolutely not."
    mi "Oh. "
    mi "Huh."

    scene intervention24
    with dissolve

    mi "Guess I’m the weird one, then."
    s "No surprise there."
    mak "Do {i}you{/i} have any questions, Sensei?"
    s "Just one. Was this really necessary?"
    mak "Probably not. But I’m sure it made Miku feel a little more comfortable and, strangely enough, I think I feel that way as well."
    s "Well, I don’t. This was weird and I’d prefer that we don’t ever do anything like this again in the future."
    mak "If you honestly think you’ll be able to avoid a similar conflict in the future, you’re out of your mind."
    mak "It’s only a matter of time until you’re having this exact conversation with every pair of friends who fall hopelessly in love or...{i}like{/i} with you."
    mak "All things considered, I think Miku and me handled this extremely well."
    s "Miku and I."
    mak "..."
    s "..."

    scene intervention25
    with dissolve

    mak "I changed my mind. You can have him."

    scene black
    with dissolve2

    "The intervention comes to a close as Makoto needs to start getting ready for work."
    "It definitely feels a little later than normal for her to start heading over there, so I initially dismiss it as an excuse to give Miku and me some time alone. "
    "But that notion is immediately quelled when Makoto says this."

    if bonus == True:
        mak "Oh, and you two are going to be walking there with me. I refuse to leave this room knowing that her shirt would immediately come off as soon as the door closes."
        mi "That happened one time! "
        mi "I do kinda wanna walk, though. So I’ll come."
        mak "And you, Sensei?"
        s "..."
        s "Ugh, fine."
    else:
        mak "Yahtzee!"
        s "Congratulations, Makoto."

    scene intervention26
    with dissolve

    mak "Oh, for fuck’s sake! Who keeps turning the number on our door upside down?! It’s getting very tiring!"
    mi "Do you really think it’s weird that I wanna be on Team Makoto {i}and{/i} Team Miku? Cause I just don’t really get why."
    s "That’s something you’ll have to talk to Makoto about. I’m perfectly fine with it."
    s "I do stand to benefit the most, though, so I’m probably biased."

    scene intervention27
    with dissolve

    mak "Why are we talking about that again?! The intervention is over and it’s time to return to reality!"
    mi "Oh, and sorry for lyin’ about Makoto not bein’ around. I figured ya would’ve ran if I told ya she was with me."
    s "It’s whatever. That honestly went a lot better than I was expecting. "
    mi "Yeah, nobody cried at all. And Makoto only got a tiny bit flustered when I brought up her {i}relationship{/i} with “little” Sensei."

    if bonus == True:
        s "Please don’t call it that, Miku."
        mak "Please don’t talk about that at all! And {i}definitely{/i} not in the halls!"
    else:
        s "Who told you about my miniature clone? That was supposed to be a secret."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mikudorm45 = True
    $ makoto_love += 1
    $ miku_love += 1
    stop music fadeout 8.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm45p2

label mikudorm45p2:
    scene mikuwalksatnight1
    with dissolve2
    play music "retrospect.mp3"

    if bonus == True:
        "Eventually, we {i}do{/i} stop talking about my penis. "
        "Depressing, I know."
        "But seeing as it’s dangerous enough to discuss that in the dorms, it would be even more dangerous to walk the streets of Kumon-mi without trying to move onto other topics."
        "Things that will not ultimately serve as yet another common ground for the two of these girls to sprawl out on."
        "I guess one of them hasn’t done much sprawling yet, though."
        "But it’s only a matter of time- and I’m sure Makoto knows that too."
        "Miku’s grown up in a world filled with competition- she lives for it. And not just to win either. "
        "There are a lot of people out there who will tell you the whole idea of playing sports is to have fun, and there are those who would vehemently disagree."
        "I’d probably be one of those people."
        "And I’m sure that in the right shade of light, Miku would be too. "
        "But I think this is just one of those times where she’s excited to be playing."
        "Especially since it’s a game she’s just learning to play now."
        "But maybe her best friend will be able to help her."
        "And maybe one day, I can have them both sprawled out over that common ground at once."
    else:
        "(Insert SFW monologue here)"

    mi "Oh, Makoto. What’d ya wind up doin’ with that fancy painting Touka gave ya?"
    mak "I wound up giving it to my mother to either hang up at home or sell but, knowing her, I doubt she still has it."
    mi "Yeah, Maki doesn’t really seem like the kind of girl who would be into stuff like that."
    mak "It’s less that she doesn’t care for things like that and {i}more{/i} that she’s just really into...one very specific hobby."
    mak "But that’s not really something I want to discuss right now since I’m going to be surrounded by it in a matter of minutes."
    mak "I’d much prefer to hear about Sensei’s present. "

    scene mikuwalksatnight2
    with dissolve

    s "Oh, I’m involved now?"
    mi "Yeah. Didn’t Molly make somethin’ for ya, Sensei? I remember hearin’ somethin’ about that."
    mi "You two talkin’ again? Cause she seemed really beat up for a while over whatever happened with you two."
    s "We’re on good enough terms for her to make me clothing, at least."
    mak "Are we finally saying goodbye to your trusty thick t-shirt?"
    s "Well, it’s not like I was going to be able to wear it forever. "
    s "Once summer comes, I’ll need something thinner. And I guess Molly just figured that out before I could."

    scene mikuwalksatnight3
    with dissolve

    mak "I suppose we’ll get to see it soon then. The weather’s been rather nice these last few days."
    mi "Fine by me. I’m tired of wearin’ this oversized jacket. Summer Miku’s been rarin’ to go for months."
    s "You wore a hoodie all last summer too, so I was just under the impression you liked being overheated."

    scene mikuwalksatnight4
    with dissolve

    mi "Nah...it ain’t really like that. I just don’t really change up my look that often and that’s what I had lyin’ around."
    mi "But...I’ve been thinkin’ it might be time to maybe try out a few new things and see if any of ‘em stick. You know?"
    mak "Want me to help with your hair again? I’ve noticed that it’s starting to get longer and I actually quite enjoy doing it when the circumstances aren’t utterly horrible."

    scene mikuwalksatnight5
    with dissolve

    mi "Yeah! Just don’t use the scissors to kill me or somethin’. I know how you can be when you get competitive and we {i}are{/i} kinda like rivals now."

    scene mikuwalksatnight6
    with dissolve

    mak "I’m not going to murder you, Miku."
    mi "Sounds like somethin' a murderer would say. "
    mak "God, I really hope this isn’t just how you are now. It’s difficult enough having to use virtually all of my free time teaching you the things Sensei doesn’t."
    s "Don’t worry, Makoto. I’ll make sure to teach Miku everything I know."

    scene mikuwalksatnight7
    with dissolve

    mak "Like hell you will!"
    mi "I think only I’m allowed to joke about stuff like that, Sensei. Makoto’s gonna get mad if you start doin’ it."
    mak "Start?! Our entire relationship is based around him using me however he wants."

    scene mikuwalksatnight8
    with dissolve

    mi "That ain’t true, Makoto. Sensei likes you and doesn’t do that stuff to hurt you on purpose."
    mi "And I ain’t sayin’ I know a lot about all of that adult stuff you and your mom watch together but, from what I’ve heard, it sounds to me like Sensei has done plenty to please you and not just-"

    scene mikuwalksatnight9
    with dissolve

    mak "Oh, look! My family’s store! What an inconvenient moment for this conversation to end. "

    if bonus == True:
        s "The porn shop is still like three blocks-"
    else:
        s "I can smell the DVDs from here."

    scene mikuwalksatnight10
    with dissolve

    mak "Right! Which means it’s the perfect place for us to part ways and not further discuss the horrible things we do {i}with{/i} and {i}to{/i} each other."

    if bonus == True:
        mi "If they’re so horrible, how come you keep-"
    else:
        s "What is so wrong about hugging?"

    mak "CAN’T HEAR YOU! HAVE TO WORK! BYE!"
    s "..."
    mi "..."

    scene mikuwalksatnight11
    with dissolve

    s "I think that Makoto probably would have kept a few more secrets from you if she had known you were going to just bring them up in casual conversation."
    mi "I just don’t get why she’s so embarrassed about it."
    s "I think the easiest way to put it is to just say that Makoto is kind of a different person when she’s doing that kind of stuff."
    mi "Different how?"
    s "..."
    mi "..."
    s "Is that a real question? Because that seems like a weird thing to ask about your best friend."

    scene mikuwalksatnight12
    with dissolve

    mi "Man! I’ve got no idea what’s okay to talk about and what’s {i}not{/i} okay to talk about when it comes to this stuff."
    mi "How come playin’ for two teams is like...twice as hard as playin’ for one?"
    s "Miku, I know you’re not very good at math, but I think that you can handle this problem if you just believe in yourself."

    scene black
    with dissolve2

    "Miku and I walk for a little while longer, and I’m pretty sure it’s aimless as well since it’s in a direction I’ve never gone before."
    "I doubt that either of us care much right now about where we’re headed or what we’re going to do when we get there."
    "We’re just kind of...moving from one place to the next and hoping that existing beside one another isn’t enough to tire the other out."
    "With someone like Miku beside me, that much is always a little uncertain."
    "But it’s been getting better lately."
    "Well, maybe “better” isn’t the right word."
    "But she doesn’t tire me out even half as much as she used to...and that is absolutely a good thing."
    "On the other side of things, though-"
    "It’s clear that she’s the one beginning to get a little exhausted."

    scene mikuwalksatnight13
    with dissolve2

    s "..."
    mi "..."
    s "Everything okay?"
    mi "Yeah, yeah. Everything’s good. Really good, actually."
    mi "I’m just still tryin’ to wrap my head around everything."
    mi "I’m used to stuff movin’ fast since that’s pretty much all I’ve ever known, but...this is a completely different kinda fast."
    mi "My blood’s pumpin’ and my heart is racin’, but my legs are all noodley and I can’t really hold my hands straight."
    mi "They’ve got this thing in sports called “The zone” where an athlete just gets like, mega focused for a little while and it kinda, like...enhances all of their abilities and stuff."
    mi "But I don’t know if this whole...liking you thing has a “zone.”"
    mi "I don’t know when I’m gonna stop being nervous and stuff. Which means I have no idea when I’m gonna be able to go back to {i}normal.{/i}"

    scene mikuwalksatnight14
    with dissolve

    mi "Wait! What if it’s not that?! What if I actually am sick?!"
    s "I’m no doctor, but I’m pretty sure your initial take on the situation is the one you’re looking for."
    s "Besides, there’s no need to go back to normal. Especially when normal with you has always been kind of abnormal to begin with."

    scene mikuwalksatnight15
    with dissolve

    mi "Ya think so? Cause we’ve got some pretty abnormal girls in our class and I was under the assumption that I was kinda one of the more normal ones."
    s "Sometimes, sure. "
    s "You have your moments, though."
    s "Like, I can’t think of anyone else who would have immediately gone against what I asked them to do and told their friend instead of just continuing to make out with me in private."

    scene mikuwalksatnight16
    with dissolve

    mi "You mad about that, Sensei? Cause I understand if you are. "
    mi "Ya gotta remember that you didn’t do anything, though. It was all me. We’d be playin’ a completely different ball game if you made the first move and kissed me instead of me kissin’ you."
    s "That’s true, I guess. I’ve made the first move on several occasions with you before and you never told Makoto about any of those."
    s "Well, until now, I guess."

    scene mikuwalksatnight17
    with dissolve

    mi "That’s not...completely true...and it might be why I still feel like somethin’s kinda...not right."
    mi "Makoto still doesn’t know about what happened at the beach and I kinda...don’t really wanna admit it to her."

    if bonus == True:
        mi "But that makes me feel really bad cause she told me {i}all about{/i} you two goin’ at it. "
        mi "I just don’t get why I’d wanna confess one thing but not confess another if they all fit into the same box, ya know?"
        s "Kissing and dry humping someone to the point of orgasm aren’t really things that fit into the same box, Miku."
        s "You don’t need a reason to not want to tell a person something. You can just...{i}not{/i} want to tell a person something. And that’s completely okay."
        mi "But is it still okay when you’re pretendin’ that everything is out in the open even when there’s still somethin’ buried beneath it all?"
    else:
        mi "But that makes me feel really bad cause she told me {i}all about{/i} how you guys are in the secret hug club. "

    s "Well, let me ask you this- do you think Makoto has really shared {i}everything{/i} with you?"

    scene mikuwalksatnight18
    with dissolve

    mi "I’m pretty friggin’ sure she has because I have no idea what else two people can even do to each other that she didn’t already tell me about."
    mi "Felt like any moment she was gonna start breakin’ out reference material. Certainly knows where to get it."
    s "Oh. Well...I don’t know, then."
    s "I’ve never had a best friend to talk to about things like that, so I’m not really sure what someone would be compelled to share or not."
    s "But I do know that there are things I’d want kept a secret from everyone- and I don’t think you should beat yourself up about it for being in the same boat."

    scene mikuwalksatnight19
    with dissolve

    mi "Yeah...probably not..."
    mi "Everythin’ just seems a little too good to be true right now, I guess. "
    mi "The guy I like’s hangin’ out with me on a bench in some park and my best friend who likes the same person doesn’t seem to mind at all."
    s "I think it’s less that she doesn’t mind and more that she’s just good at dealing with it."
    mi "Then she’s friggin’ stronger than I’ll ever be cause, if I was in her place, I’d be pissed the heck off."
    s "And what place is that? Because you two don’t seem too far off from where I’m standing."
    mi "I mean, she’s basically kinda your girlfriend already, just without the title and...without the kissing. "

    if bonus == True:
        mi "You two see each other all the time...she’s super loyal...you’ve {i}done it{/i} more times than I can even keep track of..."

    mi "What else is missing?"
    s "Love."
    s "On my end, at least."
    mi "Well, I hope you change your mind one day. "
    mi "She deserves it."
    s "And you don’t?"
    mi "Not really. "
    mi "I ain’t a bad person, but I ain’t really a good one either."
    s "I think you’re a good person, Miku."
    mi "Sure don’t feel that way, Sensei. Not while I’m pretendin’ to have a totally clean slate when all I did was use my hand to wipe off the dirt."
    mi "And, you know what? I don’t really want it to be completely clean either. When stuff like that’s clean, ya gotta take more time to look after it and make sure it doesn’t get all messed up."
    mi "But when somethin’s already a little dirty, you don’t have to be as careful. You can be a little reckless from time to time and just hope that nothin’ goes wrong."
    mi "Somethin’ always can, though."
    mi "Somethin’ always does."
    s "..."
    mi "..."
    s "This isn’t just about Makoto, is it?"

    scene mikuwalksatnight20
    with dissolve

    "Miku looks up at me, but doesn’t reply."
    "If she did, she’d be opening herself up. Exposing a weakness."
    "And in true athletic fashion, she’s swapped over to defense in order to weather my attack. "
    "I’m not much of an athlete, though-"
    "So it will be a half-hearted attack that I already know she’ll be able to deflect."
    "And one that won’t break through until she’s been worn down to near nothingness."

    if kirinkill == False:
        s "I know what happened to your parents."

        scene mikuwalksatnight23
        with dissolve

        mi "Don’t..."
        s "I can't tell you who told me, but-"
        mi "No..."
        mi "Not yet..."
        mi "I...ain’t ready..."
        s "Do you think you ever will be?"
        mi "Sensei..."
        mi "I really can’t..."
        s "I won’t force you to."
        s "I implore you to take your own advice sometime, though."
        s "Be a little reckless. Hope that nothing goes wrong."
        s "Maybe even rely on a teammate to make up for the areas you lack in."
        s "I’m not good at sports, but I can listen to whatever it is that happened and give you some half-hearted advice on the matter that’ll likely devolve into some sort of existential monologue."
        mi "..."
        s "I might be getting ahead of myself in saying this, but I think calling me just another average person in your life is a little outdated at this point."
        s "If you want to get closer, get closer. You’re good at that."
        s "And remember that simply talking about things that have happened in the past is perhaps the best way to get over them."

        "Something gets stuck in my throat during that last sentence."
        "Probably the irony."

        mi "..."
        s "..."

    else:
        s "I still don’t know anything about your past."

        scene mikuwalksatnight21
        with dissolve

        mi "My...past?..."
        mi "But...why would you..."
        s "It just might help me understand a little more about why you think the way you do."
        s "It’s a bit of a hobby of mine- staring into the depths of people and trying to attach motives to their actions. Particularly the ones that make the least amount of sense to them."
        s "But that’s hard to do when I can’t see even a single quadrant of the big picture."

        scene mikuwalksatnight22
        with dissolve

        mi "I...uh..."
        mi "It’s...hard..."
        mi "Like...I...."
        mi "I...start freezing up..."
        mi "Whenever I...go back there..."
        s "That bad?"

        scene mikuwalksatnight23
        with dissolve

        mi "I can..."
        mi "Still hear it..."
        mi "See it..."
        mi "I don’t..."
        mi "I...I can’t..."
        s "That’s enough."
        mi "..."

    s "You’ll tell me when you’re able to tell me, I guess."
    s "I just figured that whatever happened back then is probably something I’d know about {i}before{/i} we started taking our relationship in a more exciting direction."
    mi "I just..."
    mi "I want to forget..."
    s "Do you?"
    mi "..."
    s "..."

    "As expected, Miku cocoons herself inside a blanket of fear and waits to metamorphosize into something a little less defenseless."
    "Something more beautiful."
    "But her wings fuse to her chrysalis and she gets stuck inside."
    "As such, it falls on me to free her."
    "Or rather-"
    "I just want to."

    s "Let’s just talk about something else."

    scene mikuwalksatnight24
    with dissolve

    mi "..."
    s "..."
    mi "Yeah."
    mi "Yeah, that sounds good."
    mi "Sorry for-"
    s "Don’t apologize. Just move on."
    s "I’d prefer to not have to drag your screaming, nubile body all the way over to Makoto’s porn sanctuary and have her nurse you back to health."

    scene mikuwalksatnight25
    with dissolve

    mi "I think there were a bunch’a nicer ways to say that, but...yeah. I don’t really want ya doin’ that either."
    mi "‘Sides, bein’ round all those videos makes me feel kinda weird anyway. I’ve got no idea what’s goin’ on in like 90%% of them."

    if bonus == True:
        s "Want to find out?"
    else:
        s "Do you want to braid each other's hair?"

    mi "Jeez, Sensei. At least take me on a date-"

    scene mikuwalksatnight26
    with dissolve

    mi "Ooh! Right! I was gonna ask ya earlier when we were still with Makoto, but..."
    mi "Do you...maybe wanna come to the mall and help me pick out some clothes? I ain’t really sure if that counts as a date or not, but we can call it one if ya want."
    s "I don’t really care what we call it, but I {i}am{/i} interested in helping you find an outfit since that is an area I can now safely say I am slightly experienced in."

    scene mikuwalksatnight27
    with dissolve

    mi "Yeah...I remember you comin’ along with us when we got new swimsuits before the beach trip."
    mi "I guess this’ll be kinda like that, just...with only us two instead of a group of girls."
    s "Did you have an idea of when you’d want to go?"

    scene mikuwalksatnight28
    with dissolve

    mi "Idunno. Just call me after soccer practice on the weekend and we can meet up at the mall or somethin’."
    mi "We can make a whole thing out of it. Somethin’ that’ll get Makoto real jealous when I recap it for her."
    s "For my own personal curiosity, is {i}everything{/i} we do outside the bedroom in a beach inn something that’s going to be immediately forwarded to Makoto?"
    s "Because that would make my life exponentially harder."
    mi "I can probably make some more exceptions if they’re good enough."
    mi "Like ya said, I shouldn’t feel inclined to share {i}everything{/i} all the time."
    mi "You haven’t failed me so far, Sensei. So maybe you’re right about that too."
    s "Good enough for me."
    s "I’ll call you sometime over the weekend, then."
    mi "Sounds good."
    mi "I’m..."
    mi "Really lookin’ forward to it."

    scene black
    with dissolve2

    "Seeing as it’s already late and this park is as close to a halfway point as we're going to get, the two of us decide to split up and head back to our respective residences."
    "There’s no hug or kiss marking the end of the night in a way any different than it would normally be."
    "There’s no anything, really."
    "Just more lingering curiosity about what it is that made Miku {i}Miku{/i}-"

    if bonus == True:
        "And a higher likelihood of her sneaking into my thoughts when I go home to rub one out before bed."
    else:
        "And a really neat bird that lands right next to us on a tree branch."

    $ renpy.end_replay()
    $ mikudorm45p2 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikuspecial50:
    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I tap on Miku’s name in my phone and wait for her to answer."

    if bonus == True:
        "I figure that since soccer practice is over, now is the best time to invite her to the mall and take all of her clothes off."
        "Are there going to be other steps in between those two things? Of course. But I’m a lot less interested in those than I am in the end goal here."
        "Even if that goal will likely be obscured by a curtain since I doubt Miku’s level of aggression has moved far past spur of the moment makeout sessions."
        "Guess there’s only one way to find out, though."

    play sound "phonebeep.wav"

    mi "..."
    s "..."
    s "Miku?"

    play music "lifeismostlygood.mp3" fadein 3.0

    mi "Heeeeeeeeeeeeeeeeeey..."
    s "..."
    mi "..."
    s "If you’ve been kidnapped and can’t talk about it, cough and I will call the police."
    mi "I ain’t locked in somebody’s trunk right now, Sensei. I’m friggin’ nervous, okay?"
    s "About what?"
    mi "Well...aren’t ya callin’ me to go on that date thingy we talked about?"
    s "I guess, but I don’t really see why you’d be nervous about that when we’re together all the time."
    mi "It’s less the whole “spendin’ time together” part and more the “I’m gonna look like an idiot” part."
    s "Then just...don’t try on idiotic looking clothes? Is that good moral support?"
    mi "Not really, no. "
    s "Well, do you want to meet up or not? Because if you’re going to back out-"
    mi "No! We can still meet up! I’ve just gotta get ready!"
    s "Fine. But if you show up with another handwritten intervention sign, I am leaving you stranded at the mall."
    mi "Okay, good. Cause I was wonderin’ how I was gonna carry it all the way over there in the first place."
    mi "But anyway! I’ll see you there!"
    mi "And please don’t make fun of me when ya see me! "
    s "But why-"

    play sound "phonebeep.wav"

    s "..."

    "Miku hangs up the phone and I’m suddenly left wondering what exactly I would be making fun of her {i}for.{/i}"
    "The only thing I can think of is that stuff Makoto said the other night about doing her hair. But it’s been way too short of a time for it to finish growing and-"

    play sound "static.mp3"
    scene amisepiathing with flash
    stop sound

    a "The same way Maya can eat more than her body weight in food and Ayane can materialize guns and giant bananas out of thin air."
    a "Cute girl magic!"

    play sound "static.mp3"
    scene noonsky with flash
    stop sound

    s "No...there’s no way."

    scene black
    with dissolve2

    "I’m sure I’ll figure out whatever it is Miku is concerned about as soon as I make it to the mall."
    "........."
    "......"
    "..."

    scene mikugirly1
    with dissolve2

    "Miku somehow manages to make it there before me and sends me a text about where to meet up with her."
    "However, when I approach the meeting spot, I only see a tree."
    "I wonder if that means anything."

    s "{i}Ahem.{/i}"

    scene mikugirly2
    with dissolve

    mi "Ah!"
    s "..."
    mi "..."
    s "Miku, stop pretending to be a tree and look at me."
    mi "I don’t wanna. I look weird."
    s "I can neither confirm nor deny that on account of your face being shielded, but I can assure you that you probably look fine."
    mi "Sayin’ “probably” kinda makes it sound like ya ain’t so sure, Sensei."
    mi "I know you’re supposed to dress a little better than normal for stuff like this, but I barely even feel like Miku right now."
    s "I feel like that should technically make things easier."
    s "If you don’t feel like Miku, you can act like whoever it is you {i}do{/i} feel like and come out from behind the tree since there would be nothing to be embarrassed about."
    mi "The heck are you even talkin’ about right now? That didn’t make any sense at all."
    s "Just come out from behind the fucking tree, Miku."
    mi "..."
    s "..."

    scene mikugirly3
    with dissolve

    mi "Did ya really have to curse at me?"
    s "Is that...really you?"

    scene mikugirly4
    with dissolve

    mi "I told ya it was weird! This kinda look doesn’t suit me at all! And my hair hasn’t been this long in years! It keeps gettin’ in my eyes!"
    s "Where did you even get that outfit? I thought the whole purpose of us coming here was to buy you summer clothes?"

    scene mikugirly5
    with dissolve

    mi "Makoto got it for me as a present to celebrate my first time going out with a boy."
    s "Well, that explains why it fits you so well. There isn’t really anyone who knows you better than she does."

    scene mikugirly6
    with dissolve

    mi "Fits me well? You kiddin’ right now? My arms feel so exposed that I can barely even remember I’m wearin’ a shirt."
    mi "Or a...blouse, I think? What am I supposed to call this thing, Sensei? I have no friggin’ clue."
    s "Let’s just call it “cute” and get on with our date, then."

    scene mikugirly7
    with dissolve

    mi "Cute?! Oh God- is this how Karin always feels when ya tell her she looks like that?! I think I’m finally startin’ to get it!"
    s "Miku, step away from the tree."

    scene black
    with dissolve2

    mi "Fine! I’m goin’! But if you start laughing, I’m runnin’ the heck outta here!"

    "........."
    "......"
    "..."

    scene mikugirly8
    with dissolve2

    s "Wow."
    s "What a turnaround."
    mi "That’s what I’m sayin’. S’like I’m a completely different person right now. Nearly jumped outta my socks when I looked in the mirror before leavin’."
    s "Don’t get me wrong, I thought the whole “tomboyish charm” thing was adorable most of the time, but I think this works just as well."
    mi "Even if it ain’t really normal Miku anymore?"
    s "I don’t see why there can’t be two normal Mikus. All that should really matter is whether or not {i}you{/i} like it."
    mi "How am I supposed to know that, though? I don’t really have any idea how I feel right now."
    mi "It’s harder to move around in this...my arms and legs are cold...and I keep feelin’ like people are starin’ at me cause they think I’m some crossdressin’ [teenage]boy."
    mi "But I guess...it doesn’t look as bad as I expected it to when I first saw the outfit."
    mi "I still think it’d look better on somebody like Makoto, though. Sure, she’d have to shrink a few sizes to get it on, but I think she’d make me look like the friggin’ poser I am if she were to wear this."
    s "I don’t know. I think it fits you really well."
    mi "You also thought a stuffed bear fit me well, so you’re probably just confusin’ me for a normal girl or somethin’."
    s "Nah. I know full well that despite everything you say, you’re just as “girly” as everyone else."

    scene mikugirly9
    with dissolve

    mi "Am not!"
    s "Is that really something you want to be arguing?"
    mi "I don’t know! Maybe?! I feel...weird! And now {i}you’re{/i} lookin’ at me too and it’s really makin’ me wanna change back into somethin’ more comfortable!"
    s "I wouldn’t be staring so much if I wasn’t so attracted to you, so this is kind of your fault."

    scene mikugirly10
    with dissolve

    mi "Not sure how you can feel that way about somebody like me, but...thanks."
    mi "I still don’t really think it works, but...I guess I could maybe wear this again in the future if ya actually {i}do{/i} like it as much as ya say."
    mi "Right now, though...I don’t really think I’m comfortable in this, Sensei..."
    mi "And I kinda wanna just go put somethin’ else on."
    mi "Havin’ to focus on lookin’ pretty {i}and{/i} bein’ on a date is like...some advanced level technique. I ain’t ready to multitask like that just yet."
    s "Fortunately, I don’t think you need to focus at all in order to be pretty."

    scene mikugirly11
    with dissolve

    mi "Stop bein’ so cool! Can’t ya see I’m goin’ through a crisis right now?!"

    if bonus == True:
        s "What do you want to do then? Go find an outfit that makes you feel more like “normal” Miku and less like the Miku that is presently giving me an erection?"
        mi "Don’t go gettin’ one of those in public! People are already lookin’ over here because of the crossdressin’ boy you’re hangin’ out with!"
        s "Stop calling yourself a boy and go take your clothes off."
        mi "Now?! This is goin’ way too fast!"
    else:
        s "What do you want to do then? Go find an outfit that makes you feel more like “normal” Miku and less like the Miku that I presently want to hug?"
        mi "Yes! But I am having a difficult time choosing a store! Whatever will we do?!"

    s "Just choose a store, Miku. Preferably sometime before summer."

    scene mikugirly12
    with dissolve

    mi "Uhh...maybe that place Chika works at, then? They looked like they had a pretty decent variety when we went there that one time."
    s "Choose literally any other store."

    scene mikugirly13
    with dissolve

    mi "You avoidin’ Chika now? How come?"
    mi "This another one of those girls Makoto’s suspicious of you spendin’ too much time with?"
    s "Perhaps. I just know she’d get a little jealous if she saw me with you."

    scene mikugirly14
    with dissolve

    mi "Chika? Jealous of me? You kiddin’?"
    mi "She’s like...superstar pretty. And I’m just some weirdo walkin’ around in clothes clearly made for someone else."
    mi "She’d probably laugh me outta the store before gettin’ jealous about something like that."
    s "I think you’re gravely misunderstanding how cute you are, Miku."
    mi "And I think you’re just gravely...wrong. But if it makes ya feel better, we can go somewhere else."

    scene mikugirly15
    with dissolve

    mi "After that, though...we’re gettin’ ice cream whether ya like it or not."
    s "Do I...seem like the type of person who is anti-ice cream?"
    mi "You seem a little anti-everything, Sensei. But if we’re gonna be goin’ out on dates, you’re gonna be buyin’ me ice cream. Those are just the rules."
    s "If that is what must be done..."

    scene black
    with dissolve2

    if bonus == True:
        "Despite being far more comfortable with the idea of {i}dating{/i} than I assumed she’d be, Miku still can’t seem to let go of the idea that she just doesn’t belong in feminine clothing."
        "And, as excited as I am to get her out of said clothing, I do wish she’d maybe try and look at herself a little harder."
        "I guess feeling a little discomfort is to be expected though when you’ve finally got the opportunity to move around in someone else’s skin."
        "She just needs to grow into it."
        "Don’t share that thought with her, though. She’ll think it’s a shot at her breasts."
        "Or...lack thereof, I suppose."
        "Either way, the two of us walk through the mall together, mostly ignoring the fact that Miku is wearing a dress, and wind up at another familiar store."

    "........."
    "......"
    "..."

    scene mikugirly16
    with dissolve2

    mi "What do you think, Sensei? Are high waisted shorts a little too girly, too? Should I try and get somethin’ a little...lower-waisted? Or would that just be called “normal?”"
    mi "This is exactly why I hate shoppin’ for stuff. I’ve got no idea how any of this fashion mumbo-jumbo works."
    s "Why does it matter if they’re girly or not? Who cares?"
    s "No one is expecting you to keep up the same appearance forever and I have no idea why you’re so dead set on it."

    scene mikugirly17
    with dissolve

    mi "I don’t wanna hear that from somebody who’s been wearing the same heckin’ blazer for as long as I’ve known him."
    s "I’m only wearing this because it reminds me of the first time we kissed."

    if bonus == True:
        mi "Ya think I’m actually gonna fall for that? You’re just smooth talkin’ me cause ya think it’ll get me to put out in the dressing room. I know your games, Sensei."
        s "Makoto should have never told you anything. That line would have worked out better if you didn’t know I was routinely having sex with your best friend."
    else:
        mi "Ya think I’m actually gonna fall for that?"

    scene mikugirly18
    with dissolve

    mi "What about this one? Is {i}this{/i} one too girly?"
    s "..."

    "Wow. I guess Miku really {i}is{/i} unfazed by the whole thing between Makoto and me, then."
    "I...don’t know how I feel about that."
    "But I guess she does hang out with Kirin a fair bit, so maybe she’s just been negatively influenced in some way."
    "If you can even call the acceptance of relationships existing outside of your own personal bubble “negative” to begin with."
    "Which you can’t, because that’s just how life works."
    "But it would still be nice for her to get a {i}little{/i} bit jealous."

    scene black
    with dissolve2

    mi "Okay...I..."
    mi "I think I’ve got somethin’."
    mi "Yeah...Yeah, this’ll work."
    s "Need me to come in there with you?"
    mi "I know how to dress myself, ya friggin’ horn dog! Just wait out here and I’ll be done in a sec!"

    "Maybe one day..."
    "........."
    "......"
    "..."

    scene mikugirly19
    with dissolve2

    mi "..."
    s "..."
    mi "Good? Bad? What’s the verdict?"
    s "You look nice. I think I prefer the dress, though."
    mi "I like the dress too, but...I just ain’t ready yet, Sensei. Stuff like this is what I’m more comfortable in."
    mi "I’m fine with tryin’ to go a little more outside of my comfort zone, but...I’ve gotta take baby steps."
    mi "Ain’t always right to expect yourself on the starting roster if it’s your rookie season, ya know?"
    s "Not really, but I’ll trust your judgement."
    s "What you wear or the way you choose to style your hair doesn’t really make any difference to me. So as long as you’re happy, I’m fine with it."

    scene mikugirly20
    with dissolve

    mi "Guess it’s settled, then! Summer Miku’s makin’ her debut appearance before summer even begins!"
    mi "She’s also about to actually spend money on clothes for the first time in forever! So that’s a big step in...some sorta direction as well! Thanks for the help, Sensei!"
    s "What help? All I did was stand here and say you look cute a few times."

    scene mikugirly21
    with dissolve

    mi "Exactly! That was all ya needed to do."
    mi "Sometimes, girls just need moral support. We say a bunch of stuff that’s been squirmin’ around our minds cause we want ya to disagree with us."
    mi "You not doin' that means you passed the test!"
    s "Test?"

    scene mikugirly22
    with dissolve

    mi "The test to prove that I actually {i}do{/i} like ya after all!"
    mi "Sorry Makoto, but Miku Maruyama ain’t backin’ down any time soon!"

    scene black
    with dissolve2

    "Miku goes back into the dressing room to gather the dress her {s}best friend{/s} rival bought for her and decides that she’s just going to keep wearing her {i}new{/i} new outfit for the rest of the “date.”"
    "While we’re waiting in line to pay, it becomes increasingly apparent that mostly all of her nerves have departed with the addition of new clothing or, to harken back to an earlier metaphor-"
    "A different set of skin."
    "We leave the store in a hurry as Miku returns to her normal self and, within a matter of minutes, she has the {i}other{/i} thing she came here for as well..."
    "........."
    "......"
    "..."

    scene mikugirly23
    with dissolve2

    mi "Here! I went ahead and got you vanilla since you seem so boring and normal all the time."
    s "That’s a very offensive thing to say to someone who just bought you ice cream."

    scene mikugirly24
    with dissolve

    mi "I’m obviously just kiddin’, Sensei. I don’t think you’re normal at all."

    if bonus == True:
        mi "Ain’t nothin’ even remotely normal about gettin’ locked inside of a love triangle with two students. Let alone ones as young as-"
        s "Yes, thank you for acknowledging how inappropriate and abnormal our situation is. I would never have recognized it otherwise and I thank you for setting me down the right path."
        mi "Well, wherever that path is headed, I hope I can walk it with ya."
        mi "I might not be as smart or feminine as the other girls, but I’ve got tons of energy and I can’t think of anybody I’d rather spend it on than you."
        mi "Now eat your friggin’ ice cream before it starts to melt!"
        mi "We’ve got lots more hangin’ out to do!"
    else:
        s "Are you bullying me right now?"
        mi "Gimme all your lunch money, punk!"
        s "But I just bought you ice cream D="

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ miku_love += 3
    $ mikuspecial50 = True
    stop music fadeout 20.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm50

label mikudorm50:
    "We manage to spend at least another hour at the mall and, miraculously, don’t bump into anyone we know. "
    "Feeling victorious due to this once in a lifetime, genuinely fortunate happening, Miku and I decide to head back home after grabbing a quick bite to eat at some fast food place she likes."
    "And while she manages to stay bright and cheerful for the bulk of our “date” today, she gets noticeably quieter on the bus ride back."
    "The silence snowballs to the point where she stops speaking altogether and the air between us thickens."
    "And while I want to say that she’s just upset that the two of us are going to have to part ways, I’m sure there’s more to it than that."
    "There’s always more to it than that."
    "Unfortunately-"
    "It’s hard to ever find out {i}what{/i} without doing a little pushing."

    scene mikudormfivezero1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    mi "..."
    s "..."

    if bonus == True:
        jump mikudorm50x
    else:
        scene black

        mi "Sensei no what are you doing"
        s "Pushing you!"
        s "Be vanquished, Miku!"
        mi "Sensei no we were supposed to do the thing"
        s "Only if that THING is PUSHING!"
        mi "Ahhhhhhhhhhhhh"

        "I defeat Miku, but it takes a long time and all of my abilities go on cooldown."

        $ renpy.end_replay()
        $ mikudorm50 = True
        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku’s affection has increased to [miku_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mikuinvite1:
    play sound "phonebeep.wav"

    "I tap on Miku’s name in my phone and wait for her to answer."
    "Now that things have calmed down for the time being, I feel that it’s finally safe for me to invite her over so we continue progressing our...{i}relationship{/i} in a much more private manner."

    if kirinlust30 == False:
        "Hopefully in a way that leads to me receiving some form of satisfaction this time as all I’ve really done thus far is finger her until she cries."
    else:
        "Hopefully in a way that leads to me receiving some form of {i}fully-conscious{/i} satisfaction this time. Or, at the bare minimum, something more exciting than fingering her until she cries again."

    "And while that’s cool and all, it would be nice to shake things up in a manner more intimate than letting her dry hump me in bed next to her friend."
    "If she {i}wants{/i} to do that again, I’m not opposed. I should just probably get permission from Makoto first so I don’t have to go through another intervention."

    play sound "phonebeep.wav"
    play music "acoustic.mp3"

    mi "Hiyo, Sensei! What’cha up to?"
    s "Oh, you know. Just letting my imagination run wild. You?"
    mi "Just hangin’ with Makoto. Wanna say hi?"
    s "Yeah. Put her on for a second."
    mi "Roger that! Please hold. {i}Makoto! Your boyfriend wants to talk!{/i}"
    mak "{i}To me? Really? Why?{/i}"
    mi "{i}Maybe to confess his undying love? Come find out!{/i}"
    mak "Uhh...hello?"
    s "Hey. I was just wondering if I could have permission to bone your roommate."
    mak "{i}Here, Miku. You can have the phone back.{/i}"
    mi "{i}Huh? Already? That was quick.{/i}"
    mi "Sensei? Makoto looks friggin’ pissed. What did you say to her?"
    s "Just something that needed to be said. Don’t worry about it. Anyway, do you want to come over?"
    mi "Sure! When?"
    s "Now."
    mi "Like...{i}now{/i} now? "
    s "Does that work for you?"
    mi "I mean...I’ve gotta bring Makoto. We had plans and stuff."
    s "Gotcha. Can you put her on again?"
    mi "{i}Makoto! Round two!{/i}"
    mak "{i}Ugh! What now?{/i}"
    mak "Hello?"
    s "How do you feel about threesomes?"

    if makotofutabafuntimelustevent == False:
        mak "Aren’t you supposed to be nicer to me? Isn’t that a thing we talked about?"
        s "How do you feel about threesomes...{i}please?{/i}"
    else:
        mak "..."
        s "..."
        mak "Are you seriously asking me that right now? Have you not already done enough?"
        s "I just want to know more about you."
        mak "I think you know more than enough by now, thank you."
        s "It would sure be swell if you were into them as much as I am."

    mak "{i}Take it back. I can’t handle this today.{/i}"
    mi "Jeez, Sensei. You’re really strikin’ out today, aren’t ya?"
    s "It unfortunately appears that way. I’ll get her to come around, though."
    mi "Oh she’s come plenty of rounds if you know what I’m sayin’. "
    s "..."
    mi "Get it? Cause you give her orgasms and stuff. "
    s "Have I unlocked a new side of you?"
    mi "Probably! I’ll start gettin’ ready and the two of us’ll drop by your house in like...an hour? That work?"
    s "Sure. I hope Makoto is prepared. She seems a little confrontational today."
    mak "{i}Go to Hell! I can hear you!{/i}"
    s "See?"
    mi "Hahah! I’m sure she’ll be fine once we get there. But I’m gonna go shower and stuff, so...bye! See you soon!"

    scene black
    with dissolve2
    play sound "phonebeep.wav"

    "Miku hangs up the phone and..."
    "And I am left on my own to prepare for a threesome that will almost definitely not happen."
    "........."
    "......"
    "..."

    scene mikumakotoinv1
    with dissolve2

    mi "Heeeey. Haven’t been here in a hot minute. "
    mi "You still lettin’ girls sneak into your room to ride your junk while you’re asleep?"
    s "On occasion. Interesting choice of ice breaker, Miku."
    mi "Yeah...I ain’t really used to this whole “boy house” thing after my sexual awakening. Not gonna lie. Feels kinda lewd."
    mak "I hate you."
    s "So that’s a no to the threesome, huh?"
    mak "I hate you a lot."

    scene mikumakotoinv2
    with dissolve

    mi "What’s this about a threesome?"
    mak "Miku. Don’t."
    mi "I mean, I guess if I’m gonna have one, doin’ it with you would probably be best. I still don’t really know what I’m doin’, though. Ya might have to show me the ropes."

    scene mikumakotoinv3
    with dissolve

    mak "Look at what you’ve done to my sweet, innocent friend! She’s turning into my mom and I would literally die if I suddenly had two of them!"
    s "There goes my secret dream of her ending up with Haruka."
    s "Besides, I doubt it was {i}me{/i} who did this to her. This side of Miku has probably been buried deep down her entire life. Right, Miku?"
    mi "Hm? Oh, no. This is your fault. I have seen the light."
    mak "Sensei!"
    s "I did not mean for this to happen...but I am glad it did."
    mak "Yeah, until she starts running her mouth about it to everyone else! "
    mak "You know Miku’s attention span is...inadequate! It’s only a matter of time until she forgets this is something that’s meant to be kept {i}secret!{/i}"
    s "That’s fair. Ami could have been home and listening in on this entire conversation. You’re lucky she’s not."
    mi "If Ami was home, she woulda popped out of her room the second I talked about ridin’ your junk."

    scene mikumakotoinv4
    with dissolve

    mi "Also, you guys ain’t givin’ me enough credit! I ain’t gonna go around blabbin’ about this to everybody! I‘m too young to die! "
    mak "Just..."
    mak "Listen, I get that you’re excited to be, umm...{i}learning about your body-{/i}"

    scene mikumakotoinv5
    with dissolve

    mi "Oh, come on! Please don’t go into teacher mode in front of my friend-with-benefits. You’re gonna take all the benefits away."
    mak "...but, you need to be careful. This man is relentless. He will use you and cast you aside for someone else before you even know it."
    s "Hi. Still here."
    mi "Ain’t that a little hyper-critical? "
    mak "A little...{i}what?{/i}"

    scene mikumakotoinv6
    with dissolve

    mi "Uhh..."
    mi "Hippo...criminal?"
    mi "No...I’m pretty sure “critical” is in there somewhere and..."

    scene mikumakotoinv7
    with dissolve

    mi "A-hah! It’s hippie-critical, ain’t it?! Cause they were always sayin’ stuff that didn’t make much sense! See! I ain’t dumb!"
    mak "Is this really a creature you think you should be making sexual contact with?"
    s "I may be currently rethinking my decision. That much I will admit."

    scene mikumakotoinv8
    with dissolve

    mak "{i}Regardless,{/i} the reason I accompanied Miku here instead of letting her run off alone was precisely so something like that would {i}not{/i} happen."
    s "So, in other words, you were jealous."
    mak "That...may have played some role as well, I will admit. "
    mak "But the gist is that nothing like that will be happening today because we are {i}both{/i} here and singling out {i}one{/i} of us for...things...would be unfair."
    s "So if I wanted to single out {i}you{/i} instead..."

    scene mikumakotoinv9
    with dissolve

    mak "Obviously, Miku would never agree to such-"
    mi "I can wait out here. Feels like you need it more than me. Knock ‘im dead, Makoto. "
    mak "..."

    scene mikumakotoinv10
    with dissolve

    mak "I...suppose letting you get it out of your system may be of {i}some{/i} benefit to us."
    mi "I’m telling ya, Sensei. You’ve got a magic wiener. It’s the only explanation."
    s "Listen, we don’t {i}need{/i} to do anything like that today if it will exclude one of you. I called Miku because I wanted to invite her over. Making her wait out here would be flat out rude."
    mak "As if being rude was ever an actual concern of yours..."
    mi "If we ain’t gonna bump uglies, whaddya wanna do instead? Jump on Ami’s bed? Microwave stuff we ain’t supposed to microwave? Oooh, you got any games we could play?"
    s "I have the 1999 PC classic, Rollercoaster Tycoon."

    scene mikumakotoinv11
    with dissolve

    mi "I {i}love{/i} the 1999 PC classic, Rollercoaster Tycoon!"
    mak "Why are you guys saying it like that?"
    mi "Where’d you get a copy? That’s a piece of vintage memorabilia, ya know."
    s "Io found the time to drop it off between pretending to be a pharmacist and slinging you pills. "

    scene mikumakotoinv12
    with dissolve

    mak "Between {i}what?{/i}"
    mi "{i}Shh!{/i}"

    scene mikumakotoinv13
    with dissolve

    mak "Miku, what-"
    mi "Oh, Sensei! That’s a funny joke you just made! Anyway, time to go into your room and see what kind of stuff you’re hiding from us!"

    scene mikumakotoinv14
    with dissolve
    play sound "dooropen.mp3"

    mi "It’s this one, right? Hope you don’t mind me looking through your stuff!"
    mak "..."

    scene mikumakotoinv15
    with dissolve

    mak "I’m sorry, I think I misheard you. Something about...pills? And...Io pretending to be a pharmacist?"
    s "..."
    mak "Sensei, if you know something-"
    s "It was just a tasteless joke. It didn’t actually mean anything."
    mak "That just seems like such a random and uncalled for-"

    scene black
    with dissolve

    s "Come on. Let’s go make sure Miku doesn’t find my secret porn stash and unlock an even dirtier section of her brain."
    mak "...Yeah."
    mak "Okay..."

    "I wanted to tell Makoto."
    "And in hindsight, I probably should have."
    "But sometimes the “right” thing to do isn’t as easy as the other options. "
    "And sometimes, in order to save someone, you must sacrifice something else."

    if kirinlust30 == True:
        "Not only would giving away Miku’s newest secret put our new {i}relationship{/i} in jeopardy, but it could potentially expose {i}me{/i} as well."
        "She’s not the only one who’s hiding something. And by all means, what I’m hiding is a lot more sinister."

    "Besides, it’s quite possible she doesn’t need saving in the first place."
    "It’s quite possible that whatever Io is doing will work for Miku...and that there’s no real risk involved at all."
    "But..."
    "If that were the case, Makoto would know."
    "And the fact that she doesn’t tells me Miku’s hiding it from her on purpose."

    scene mikumakotoinv16
    with dissolve2

    "At what point is it okay to begin distributing information that doesn’t belong to you? And how can you package it up to make it seem like you’re doing it with good intentions?"
    "In all actuality, it’s not about wanting to save anyone at all. It’s about wanting to maintain the status quo — where everything is peaceful and you can stick your dick inside of as many teenagers as you want."
    "The disruption of that pattern would shake my world to the core when my world was built upon that principle. "
    "It is not my place to put Miku in hers, and it is not Makoto’s place to raze both of them in an endless pursuit of what is right."
    "The three of us will stay like this so we may one day stay as something else."
    "Something close to what the real me wants."
    "Not whoever I’m becoming."

    mi "Sensei, why the heck do you even own Mario Kart if you’re so friggin’ bad at it?"
    s "I didn’t even realize I had this."
    mak "I fucking hate Waluigi. Get out of my way, you piece of shit. I hope the fishing line snaps the next time they reel you up. Asshole."

    scene mikumakotoinv17
    with dissolve

    mi "Need some help figurin’ out the controls? I’ve heard it can be pretty tough for people your age to just start playin’ games this late in life."
    s "I’m only 31, Miku. I’m still well below the median age in the country."
    mi "Yeah, but Japan’s got a bazillion old people. You’re still kinda prehistoric by our standards, ya know."
    mi "Even if half the class is apparently into that sort of thing."
    mak "It isn’t half the class. It’s the entire class. Everyone is fighting for Sensei’s affection- even the ones who deny it."

    scene mikumakotoinv18
    with dissolve

    mak "WALUIGI, YOU LANKY CUCK! I WILL FUCKING MURDER YOU!"
    s "I’ll be fine figuring out the controls. Just promise not to laugh at me when I come in last place."
    mi "I ain’t gonna laugh at ya, Sensei. It’s still just a game at the end of the day and havin’ fun will always be the most important thing."
    mak "FUCK! YOU!"
    mi "Even if we’ve got people like Makoto who have trouble turning the competitive part of their brain off."
    s "You’d think Kumon-mi High’s greatest athlete would be the {i}more{/i} competitive one, wouldn’t you?"

    scene mikumakotoinv19
    with dissolve

    mi "I ain’t that special. 'Specially now that soccer’s gone."
    mi "Swimming’s fun, I guess. Just doesn’t feel the same, though. Ain’t no crazy adrenaline rush that comes from a breakaway or anythin’ like that."
    s "It...could come back one day. Right?"
    mi "Soccer? Doubt it. We ain’t got the numbers for it and there ain’t any reason to form the team back up without anybody to play."
    mi "It’s fine, though. Just gives me more time to focus on other things. "
    s "Other things...like what?"
    mi "I wonder."

    scene mikumakotoinv20
    with dissolve

    mak "Hey. What do you think you’re doing? Public displays of affection are rude even {i}if{/i} you’re only displaying said affection in front of your best friend."
    mi "Guess I’m rude, then. Cause I ain’t got any intention of movin’ any time soon."
    mi "You know he’s got a second shoulder open, don’t ya? Why don’t you rest your head a little too? "
    mi "Ain’t a threesome like Sensei wanted but it still lets all of us be close together. "

    scene mikumakotoinv21
    with dissolve

    mak "You’re going to lose the race with that sort of mindset, Miku."
    mi "You sure it ain’t you who’s gonna run out of gas first? Always keepin’ the pedal to the metal and whatnot. Just stay steady and keep your eyes on the prize, Makoto."
    mak "Nice try, but there is no gas in Mario Kart."
    mi "Who says I’m still talkin’ about Mario Kart?"
    s "What are those boxes? Do they slow you down if you hit them?"

    scene mikumakotoinv22
    with dissolve

    mi "They’ve got power-ups and stuff inside. You smash ‘em and use whatever you get to mess with the other people on the track. "
    s "I see..."
    mi "Do ya? Cause it seems to me like you’re just starin’ at Makoto now."
    s "That’s a new dress, isn’t it?"
    mak "Took you long enough."
    s "It looks great. You’re beautiful."

    scene mikumakotoinv23
    with dissolve

    mak "Wha- huh?! Me?! You...really think so?! "
    mak "I got a little jealous that Miku had one and I didn’t so-"
    s "That was Makoto I just hit, wasn’t it?"
    mi "Yuuuup. Great strategy, Sensei."
    mi "Takin’ somebody out IRL so you can hit ‘em in-game is a real power move."

    scene mikumakotoinv24
    with dissolve

    mak "You...fucking asshole! You distracted me! I’ll get you back for this!"
    mi "Not if I have anything to do with it."

    scene mikumakotoinv25
    with dissolve

    mak "Wha- you too?! {i}Both{/i} of you are ganging up on me now?! What did I do to deserve this?!"
    mi "Drive, Sensei! Drive! Show us how much all those years of wisdom are really worth!"
    s "I think I just fell off."
    mi "Baby steps, Sensei. Baby steps."

    scene black
    with dissolve2

    "The three of us sit in my room playing the same game for the next two hours."
    "Makoto eventually falls asleep on my arm, prompting Miku to take it upon herself to talk more about how “cute” the two of us look together."
    "It’s strange to me how she can still say something like that with a smile on her face."
    "I find it cute how genuine the love she has for her best friend is. And while something like that {i}should{/i} feel ideal for me as Miku doesn’t intend to pose any sort of threat..."
    "All I can think of is that I really wish she would."
    "And that she’d look better in my eyes if she would just pull me a little closer to her."

    $ renpy.end_replay()
    $ mikuinvite1 = True
    $ miku_love += 1
    $ makoto_love += 1
    stop music fadeout 6.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mikuinvite2:
    play sound "phonebeep.wav"

    "I tap on Miku’s name in my phone and wait for her to answer."
    "And if there is any justice in this world, I will soon find out that she is alone and capable of coming over without the sentient purity ring that is Makoto Miyamura wrapped around her finger."
    "Unless Makoto has flipped stances in regard to her feelings on threesomes overnight. If that is the case, I will gladly welcome the two of them once again."
    "The thing is, the chemistry brewing between Miku and me is still a little volatile. It’s new and different...and so I can’t be condemned for my desire to experiment a little more."
    "And experimentation is never fun when it’s being supervised."
    "I am an adult, and if I want to prey upon the naiveté of a young girl in the comfort of my own home, I should be allowed to- actually, no. Makoto is right."
    "But that changes nothing because Makoto is almost always right and I’ve dodged most major consequences thus far. Further debauchery will not slow me down."

    play sound "phonebeep.wav"

    mi "Heeeeeeeeeeeeeey..."
    s "That’s a weird way to say hello."
    mi "Too many e’s?"
    s "A few. What are you doing right now?"
    mi "Uhh..."
    mi "Would it be weird to say I’ve been waiting for you to invite me over?"
    s "As in...you’re just sitting in your dorm room and waiting for me to give you the go ahead to come to my house?"
    mi "I was also watchin’ TV and stuff, but yeah. "
    s "That is kind of weird, I won’t lie."
    mi "Well I’m kinda...you know. And Makoto’s at work right now, so..."
    s "You realize you can call me as well, right? You don’t have to wait for me to give you the signal if there is sex involved."
    mi "Ain’t that...exactly {i}when{/i} I’m supposed to wait for the signal? Don’t think it’s safe to just show up at your door and ask you to take my skirt off."
    s "It is. Just make sure Ami’s not home."
    mi "You’re playin’ a dangerous game, Sensei. I might wind up movin’ in if you go and tell me stuff like that."
    s "I take it that means you’re coming over?"
    mi "Heh. Coming."
    s "Okay, if you really {i}are{/i} turning into Maki, you should try and suppress it so we can keep Makoto alive."
    mi "The only thing {i}I’ll{/i} be suppressing is your giant boner."
    s "I don’t think you understand what the meaning of “suppressing” is."
    mi "Yeah, there’s a lot I don’t understand. But what I {i}do{/i} understand is that I’m feelin’ some kinda way and you’re the only person who knows how to do anything about it!"
    s "I guess I’ll...see you soon then. "
    mi "I guess you will..."

    scene black
    with dissolve2
    stop music fadeout 5.0
    play sound "phonebeep.wav"

    "I hang up the phone and marvel at the fact that Miku has gone from a girl with almost no sexual feelings whatsoever to one who sits around her dorm room and waits for me to invite her over."
    "I guess that’s just the process for these girls, though. "
    "And while I can paraphrase that to make it sound like I’m just helping them {i}learn more about themselves{/i} or whatever way you want to spin it that could justify what’s about to happen...I won’t."
    "Right now, a high school freshman is on her way to my house because I am going to do things to her. And {i}she{/i} is going to do things to me."
    "This is happening because I let it."
    "And there is no way you can word it that makes it okay."
    "Please."
    "Stop watching me."

    play sound "static.mp3"
    scene 1 with flash
    scene 5 with flash
    scene mikuhjinv1 with flash
    stop sound
    play sound "dooropen.mp3"
    play music "asobeatsex2.mp3"

    mi "Heeeeeeeeeey..."
    s "Too many e’s again."
    mi "Sorry if I took a little longer than you expected. I wanted to run but I didn’t wanna get all sweaty if we were gonna...you know. "
    s "You know, I’ve turned a lot of girls on during my time here in Kumon-mi, but I think this might be the first time any of them have thought about literally running to me because of it."

    scene mikuhjinv2
    with dissolve

    mi "Something something...new Miku...something?"
    s "You have such a way with words sometimes."
    mi "And you’ve got such a way with...your...fingers?..."
    s "..."
    mi "Can you do the thing again?"
    s "You literally just got here. We’re not even in the bedroom yet."

    scene mikuhjinv3
    with dissolve

    mi "We’re doing it in the bedroom?!"
    s "Did you expect me to finger you on my kitchen table?"

    scene mikuhjinv4
    with dissolve

    mi "I...wouldn’t be against it."
    s "Is there something wrong with my bedroom, Miku?"
    mi "No! It’s just...you know. It feels more serious that way. And I still ain’t ready to, like...go all the way just yet. So I didn’t wanna make it feel like that’s what I was bankin’ on."
    s "So you’re horny enough to almost run to my house to get fingered, but not horny enough to have sex with me?"

    scene mikuhjinv5
    with dissolve

    mi "I don’t think the horny part’s the problem. The problem’s that I’m half your size and kinda sensitive down there. I ain’t really interested in gettin’ split in half just yet."
    s "That’s fine. I won’t rush you if that’s what you’re worried about. It’d be nice to have {i}something{/i} done for me eventually, though."
    mi "Like what?"
    mi "You want me to try puttin’ my fingers inside of you next?"
    s "Don’t even joke about that."
    mi "I ain’t jokin’. I’ve heard Maki say that kinda thing’s totally normal."
    s "That is not the scene I want to happen right now."
    mi "Well, what {i}do{/i} you want? Cause I might be horny as heck, but I still know that fair is fair and I’m the only one who’s gotten some so far."

    if kirinlust30 == True:
        "Well, that’s not {i}entirely{/i} true given what happened in my hotel room last Halloween, but...thankfully, it doesn’t seem like Miku remembers that."

    s "Do you want to talk more about that in my bedroom?"

    scene mikuhjinv6
    with dissolve

    mi "You and that heckin’ bedroom, man. Whaddya got against the kitchen table?"
    s "For starters, the fact that I eat off of it."
    mi "And I eat off of my bed but ya don’t see me makin’ ya finger me on the floor."
    s "Why are you eating off of your bed?"
    mi "It just happens sometimes, okay? But I ain’t here to talk about food- I’m here to do sexy stuff with my teacher. And if that kinda stuff {i}has{/i} to happen in your room, then...fine."
    mi "But I really ain’t ready to go all the way yet. For real. I need more...practice first."

    scene black
    with dissolve2

    s "I’m sure we can figure something out..."

    "........."
    "......"
    "..."

    scene mikuhjinv7
    with dissolve2

    "Miku entangles her arm with mine and I wind up walking her into my room like I’m some sort of escort. Or...{i}she’s{/i} some kind of escort. "
    "I don’t know. I’ve never needed to resort to that before. But I’m sure this is how things would look if one of us was an escort."
    "Despite her clear nervousness, she puts on a smile — likely because she still thinks she’s about to be fingered until my bedsheets are a soaking mess. But that is not the case."
    "Or...at least it’s not the case {i}yet.{/i} "
    "We’ll get there later, I’m sure. But for now, I really would like to capitalize on her ability to recognize when {i}fair is fair.{/i}"

    s "So..."
    mi "Soooo..."
    s "You ready to try something a little different?"

    scene mikuhjinv8
    with dissolve

    mi "Mhm..."
    mi "You’ll take it easy on me, right? I obviously wanna do somethin’ for {i}you{/i} when you’ve helped me a bunch of times, but I still ain’t really sure what’s goin’ on just yet."
    s "Thankfully, we’re in a good environment for me to teach you."

    scene mikuhjinv9
    with dissolve

    mi "Teach?! Was this just a trap all along?! Did Makoto put you up to this?!"
    s "Wow. You don’t even understand context, do you?"

    scene mikuhjinv10
    with dissolve

    mi "Oh. You mean {i}sex-{/i}teach. My bad. My brain sucks even more when I’m nervous and it gets harder for me to understand stuff right away."
    mi "But yes. Please teach me. I can’t promise I’ll be any good at what you want, but I’ll do my best."
    s "Good. Because there’s a reward in store for you when you succeed."
    mi "Thank friggin’ God because I’ve been tryin’ to do it myself all day and it just ain’t the same."
    mi "So, what’s on the menu? What can your old pal Miku do for ya this fine evening?"
    s "You can start by not referring to yourself as my “old pal” right before we make sexual contact."
    mi "Are we not friends anymore? I ain’t your girlfriend, am I?"
    s "That’s not what I- you know what? Forget it. Kneel down by the foot of the bed. "
    mi "Should I take my clothes off? "
    s "Stay the way you are now, actually..."
    s "I like that dress."
    s "I want to ruin it."

    scene mikuhjinv11
    with dissolve

    mi "Whaaat? No! I like this dress. It’s the only thing that makes me feel girly."
    s "That’s precisely why I want you to keep it on. "
    s "You’re cute dressed like that. Well, you’re cute always. But there’s something particularly alluring about the prospect of you sucking me off while you’re dressed that way."

    scene mikuhjinv12
    with dissolve

    mi "...Okay."
    mi "Just...remember. Take it easy on me, please. "
    mi "I’m still really nervous..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikuhjinv13
    with dissolve2

    "Miku crouches down at the foot of the bed like I asked and waits patiently as I get into position in front of her."
    "I gesture her to slide forward, gently grabbing the back of her head and angling her closer to my dick, hoping she’ll take the initiative required to remove it from the fleeting residence that is my pants."
    "Instead of doing anything, however, she simply looks up at me with a sense of...childish innocence in her eyes that does nothing but make me want to paint her face white with my seed."
    "Keep looking at me like that."
    "Your purity gets me harder than anything."

    mi "So...do I take it out? Or do you do it? I ain’t all that familiar with blowjob etiquette."
    s "You can do it. I want to pay close attention to how you look after seeing it for the first time."

    if kirinlust30 == True:
        "“First” being a word I use lightly as, again...Valium."

    mi "Yeah...I guess I {i}haven’t{/i} seen it yet, have I? Closest I came was that one Halloween that landed the two of us in hot water."
    s "Do you still have that costume?"

    scene mikuhjinv14
    with dissolve

    mi "Why do you ask?..."
    s "You might suck at context, but I’m pretty sure that even you can understand that."
    mi "Remind me to bring it the next time I come over..."
    mi "But, for now..."

    play sound "zipper.mp3"
    scene mikuhjinv15
    with dissolve

    mi "Hoooooooly shit, it looks even bigger than it felt. And it felt like I was ridin’ a fallen redwood. "
    s "Your fear about being split in half is perfectly reasonable and I will not hold that against you."
    mi "Sensei, this is bigger than my head. How do you even stay conscious when this thing gets hard?"
    s "Probably willpower."
    mi "How the utter heck did Makoto and Kirin ever get this thing inside them? They ain’t even that much bigger than me."
    s "What? Since when do you know about Kirin?"

    scene mikuhjinv16
    with dissolve

    mi "I haven’t known for long. She told me during beachmas."
    s "{i}Why{/i} did she tell you during “beachmas?”"
    mi "Because...I may have accidentally spilled the beans that you finger me sometimes?"
    s "Miku-"

    scene mikuhjinv17
    with dissolve

    mi "I’ll be more careful in the future, I swear! I was just excited to talk about it since I like you so much!"
    s "Ugh, great. I obviously can’t stay mad when you go and say things like that."

    scene mikuhjinv18
    with dissolve

    mi "I totally get it, Sensei. All the worries in the world start goin’ away the second you get to spend time with somebody like this, right?"
    mi "And it only gets better once they start touchin’ you."
    mi "Feels kinda like the world is gettin’ flipped on its head, doesn’t it?"
    mi "And even if I ain’t ready to go as far as Makoto and Kirin did, I still wanna help you feel good after all the times you helped {i}me.{/i}"
    mi "Just...maybe don’t compare me to either of them until I have a little more experience, okay? "
    s "You’ll need a lot of practice...they have a pretty big lead, you know."

    scene mikuhjinv19
    with dissolve

    mi "Oh, we can practice whenever you want..."
    mi "Itadakimasu."

    scene mikuhjinv20
    with dissolve

    mi "Mm......mnch........mn~"

    "Miku drags the tip of her tongue across the head of my cock, stimulating the most sensitive area on my body with a surprising amount of delicacy and care."
    "Given the type of person she is, I figured she’d approach this a little more...relentlessly. But she starts off extremely slow and sensual and...honestly, it’s insanely hot."

    mi "Hmn...mmngh......hmnm..."

    scene mikuhjinv21
    with dissolve

    mi "Mngh...mm...am I doing okay so far?...Are you close to finishing?..."
    s "We’ve only been doing this for like five seconds."
    mi "That’s all it takes for me sometimes. I don’t know how penises work. This is my first time ever handling one."
    s "It’ll take a little while longer. Bear with me, please."

    scene mikuhjinv22
    with dissolve

    mi "Don’t say stuff like “Bear with me, please.” It makes it sound like I’m just putting up with this because I {i}have{/i} to, not because I {i}want{/i} to."
    mi "I like this part of you, Sensei...I want to make it feel good."

    "Miku...begins rubbing her cheek against my cock?"
    "She’s like a cat brushing up against its owner to try and coax it into petting her and, while that might not {i}sound{/i} very sexual, it’s that exact brand of innocence that drives me insane at times."

    mi "It’s really warm...is it always like that?"
    s "Your face is just as warm, I’m sure..."

    scene mikuhjinv23
    with dissolve

    mi "Sensei...can I tell you a secret?"
    s "Now?"
    mi "It’s not a random one. It’s related to what we’re doing."
    s "Sure...Go ahead."
    mi "It kind of...{i}excites{/i} me...how this has been in some of my friends."
    s "It...does? I feel like most people would have the opposite reaction to information like that."

    scene mikuhjinv24
    with dissolve

    mi "Amf...guess I’m just...special?..."
    s "Do you...like girls as well or something?"
    mi "Mmf...mm...no...it’s not that..."
    mi "It just...mmf...feels kinda like I’m...amf...winning right now..."
    mi "It’s fun...beating out the competition...makes me feel like...mnngh...I’m doing somethin’ right..."
    s "You’re...definitely doing something right. I’ll admit that much."

    scene mikuhjinv25
    with dissolve

    mi "Yeah?..."
    mi "You like it when I lick you like this?..."
    mi "You don’t mind me goin' really slow?..."
    s "You can do whatever you want so long as you keep looking like that..."
    mi "Like what?..."
    s "I don’t know...adorable?..."

    scene mikuhjinv24
    with dissolve

    mi "Girly?..."
    s "That too..."
    mi "Mmf...mmm...is it just...the dress making you say that?..."
    s "It’s a lot of things...but, for one, I didn’t imagine you’d be this delicate."
    mi "And I...amf...didn’t imagine your wiener would be the size of my head..."
    mi "I’ve gotta move like this or I’ll wind up suffocatin’."
    s "Can I make a request? Please don’t call it a “wiener” when we’re doing things like this?"

    scene mikuhjinv25
    with dissolve

    mi "Roger..."
    mi "Your “not old pal” Miku will take real good care of your huge cock...don’t you worry..."
    s "That’s no better than just saying “old pal...”"
    mi "Champion of Justice and Soccer, Miku Maruyama, will take good care of your huge cock...don’t you worry..."
    s "Maybe...less talking in general would be-"

    scene mikuhjinv26
    with dissolve

    mi "Chu~"
    mi "Chu....chu.....chu..."

    "Miku gives up on licking me for a moment and begins to shower me in soft kisses, each lasting no more than half a second. "
    "And despite these motions not being all that conventional in terms of bringing me to climax given that she’s no longer stroking me as well, I shouldn’t be feeling even {i}half{/i} as good as I actually am right now."
    "Yet...each time her lips connect with my cock, I feel like I’m holding myself back from pulling her forward and cumming down the back of her throat."

    scene mikuhjinv27
    with dissolve

    mi "Chu.....chu......you look really cute right now..."
    s "Me? You’re the one who looks cute..."
    mi "Mm-mm...you look cute too..."
    mi "Can I tell you another secret?"
    s "Only if it’s as good as the last one..."
    mi "I’m not wearing underwear today......chu~"
    s "So you’re an exhibitionist now?"
    mi "Chu.......a what?"
    s "Don’t worry about it. Just keep doing what you’re doing."
    mi "Can I tell you one more?..."
    s "..."
    mi "I can’t wait until you finger me...I’m kind of in Hell right now.......chu~"
    s "Yeah, well...you won’t be there for much longer at this rate..."

    scene mikuhjinv28
    with dissolve

    mi "Mmf...mmmngh...this ain’t as...hard as I thought it’d be..."
    mi "Is Miku Maruyama...actually a blowjob champion?..."
    s "Not without actually putting it in your mouth first..."
    mi "I don’t think I even have to...my original gameplan seems to be goin’ pretty well..."
    s "It wouldn’t hurt..."

    scene mikuhjinv29
    with dissolve

    mi "But if it’s in my mouth, I can’t keep kissing you."
    s "Miku..."
    mi "The tip’s the most sensitive part, right? Won’t you still cum if I just continue like this?"
    s "That’s not the-"
    mi "Sensei...can I tell you another secret?"
    s "...Go ahead."

    scene mikuhjinv30
    with dissolve

    mi "Then..."
    mi "I want you to cum on my face..."
    s "Wow. That’s a line I didn’t think I’d ever hear from you."
    mi "I think I’m a slut now."
    s "I don’t think that’s how being a slut works, Miku."
    mi "I don’t know. Kirin’s a slut and the only boy she’s ever done anything with is you."
    s "I don’t think it’s fair to put yourself on the level of Kirin just yet."
    mi "Does she do this too?"

    if kirinlust30 == True:
        "{i}You’ve literally done it together...{/i}"

    s "She might..."
    mi "Is she good?"
    s "Do you want the honest answer or the one that will make you happy?"

    scene mikuhjinv31
    with dissolve

    mi "Aw, man...she’s {i}really{/i} good, isn’t she? "
    s "Probably the best I’ve ever had since honesty seems to be the route you want to go down."
    mi "Darn it. And here I was thinkin’ I could beat her at this too. Gettin’ too cocky on my first time, I guess."

    scene mikuhjinv32
    with dissolve

    mi "Heh. C-"
    s "Don’t do it, Maki. Remember Makoto."
    mi "How good is {i}Makoto{/i} at this stuff? "
    s "Focus less on your friends and more on me. I was about to finish just a few seconds ago and am now beginning to-"

    scene mikuhjinv33
    with dissolve

    mi "Amf...mm...mngh...mnch...hngh...mmm!"
    s "Well, that was easy..."
    mi "The sooner you...finish...the sooner...{i}I{/i} get to feel good...and I...mmf...can’t wait any longer..."
    mi "I’ve been going crazy all day...I want you to play with me...I want you...I want you..."
    s "Look at me..."
    s "And keep saying that..."

    scene mikuhjinv34
    with dissolve

    mi "I want you..."
    mi "I {i}want{/i} you..."
    mi "{i}I want you...{/i}"

    with sexfade
    with sexfade
    scene mikuhjinv35
    with cumflash
    with hpunch

    mi "Mmm!"

    "The steady pace of Miku’s handjob-slash-licking combo meshed with a three word sentence that does {i}not{/i} pain me to hear winds up forcing an aggressive orgasm out of me."

    scene mikuhjinv36
    with dissolve

    "She stares down at my cock as she carefully empties it out, squeezing every last drop onto her face and tongue, clearly unsure of how long this typically goes on for."

    scene mikuhjinv37
    with dissolve

    "Fortunately for her, the duration of the male orgasm is not particularly long and her wish of having me ejaculate on her face is granted just a minute or two after its initial proclamation."
    "There’s no fanfare or immature Miku-esque commentary to accompany it either — just a smug smile from a girl who knows she did a good job."

    scene black
    with dissolve2
    stop music fadeout 10.0

    mi "Senseiiiii..."

    "And a girl who desperately wants me to finger her."

    s "Lie down."
    mi "Do ya have a towel or somethin’? Shouldn’t I wipe my face off first?"
    s "I told you to lie down."
    mi "I get that, but- ahh! What are you doin’?!"

    "I lift Miku up myself and toss her onto the bed."
    "I hike up her skirt."
    "And I finger her so violently that she destroys my mattress. "

    $ renpy.end_replay()
    $ mikuinvite2 = True
    $ miku_lust += 3

    "{i}Miku’s lust has increased to [miku_lust]!{/i}"
    "{i}You can now invite her over whenever you want!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mikupool55:
    scene mikupoolscene1
    with dissolve2
    play music "merrychristmasmrlawrence.mp3"

    ka "Hey, Miku. Are you okay? Are you feeling sick or something?"
    ay "Is she even awake?"
    ka "She is. Her eyes are open. Just barely, though. "
    ka "Do you guys know if she’s been sleeping well lately? Or anything that might be fatiguing her?"
    ka "If this was anyone else, I’d say she just needs a day to recharge or something. But Miku’s a different story and I feel like she recharges {i}by{/i} being active."
    ay "You mean like a car battery?"
    ka "Sure, if the car battery is a prodigious athlete. Miku, hey. Focus."
    mi "..."

    "Karin begins to snap her fingers, trying to drag Miku back to reality, but whatever is happening to her right now puts up too strong of a forcefield to let something like a mere {i}sound{/i} drag her out of it."
    "It’s a little ironic when you think about it."
    "Well, maybe not {i}ironic{/i} as tying any sort of expectation to any sort of mental illness is just asking to be proven wrong in one way or another."
    "But the only reason she got into this mess in the first place was to {i}prevent{/i} sound from reaching her."
    "And now that it can’t, look at what we’re left with."
    "Maybe there’s more to it than that. In fact, there {i}has{/i} to be more to it than that. "
    "The voice of vibration and its incessant mockery of this poor girl is just what {i}we{/i} can bear witness to."
    "Who knows what must lurk inside of her? Who knows what it is that {i}we{/i} can’t see?"
    "And who knows how close I may have come to grazing it with the tips of my fingers during my new and exciting venture into her most private depths."
    "If I could pull it out, I would."
    "If I could reach all the way to her heart and swipe away the fog with a quick flick of the wrist, she wouldn’t need to rely on someone else who’s broken to try and fix her."
    "That sort of thing will never work."

    s "..."

    "Ah."
    "{i}There’s{/i} the irony."

    ka "Do you need to go to the nurse’s office? Do you want us to call Maki?"
    mi "..."
    ka "Do you need {i}anything?{/i} Can you even hear me right now?"
    mi "..."

    scene mikupoolscene2
    with dissolve

    ka "What the heck? Where did this even come from? She was fine earlier."
    ay "Should I go get Makoto? She should still be in the class or Sensei’s office or something. Maybe she’ll know what to do?"
    ka "You can try. But if it really is fatigue, I don’t think there’s anything we {i}can{/i} do but let her rest. And the pool isn’t exactly the best place for that."

    scene mikupoolscene3
    with dissolve

    ka "Sensei, I’m sorry to ask such a big favor of you- but would you mind bringing Miku to the nurse’s office? I’d do it myself, but I promised Miss Imai I’d take care of everything here in her absence."
    s "..."
    ka "Sensei?..."

    "That’s the wrong idea."
    "As the one person here who knows this isn’t just “fatigue,” taking Miku to the nurse’s office won’t do anything but make what’s likely wrong with her even more apparent."
    "And that will incriminate me. Or {i}could{/i} incriminate me if either Miku or Io accidentally mention to someone that this is something I’ve known about."
    "But they wouldn’t do that, right? Even if they talk too much, they wouldn’t do that. They like me. And nobody else-"
    "Makoto. Makoto would figure it out. She’d figure out that this is something I’ve been aware of. I’ve given her so many hints."
    "And it would not only ruin my relationship with her if this is serious, but open me up to further consequences as well if she made my involvement publicly known. Which she {i}might.{/i}"
    "Because even if {i}she{/i} likes me, this is an area she won’t budge on. Even if {i}she{/i} likes me, she likes {i}Miku{/i} more. And she’ll know that I’ve been letting this happen."
    "Taking Miku to the nurse will ignite a spark that could burn down my entire life. I can’t have that. I can’t risk losing anything over taking her to the wrong place."
    "I should take her somewhere quieter. Safer. But not so quiet and safe that no one would ever find her. Besides, she’ll be okay. Right? She probably just took too much of something and needs to come down."
    "Everything will be fine. I should hide this. If I hide it, I can talk to her when she’s more conscious and make her stop."
    "There’s no need to risk destroying anything over this. I can just take her somewhere else. It’s that easy. I’m such a genius."

    s "What if I just took her back to the dorm?"

    scene mikupoolscene4
    with dissolve

    ka "The dorm? But that’s like a mile away. And I highly doubt Miku will be able to walk in this condition if she’s not even waking up for me."
    s "Then I’ll carry her. It’s fine."
    ka "You’re going to...carry her all the way back there?"
    s "It’s fine. Look at her. She can’t weigh any more than like 80lbs max."
    ka "I mean...you’re the teacher. And I know better than to talk back if you think you know what’s best. So if that’s your decision, okay. But I’d appreciate if you’d text me when you get to her room."
    ka "Just let me take her back to the locker room and change her clothes before-"
    s "I’ll just carry her like that. Stripping a girl while she’s unconscious isn’t really a thing we’re supposed to do."
    s "Besides, putting her normal clothes back on might overheat her. She needs to get some rest as soon as possible. She can get dressed when she wakes back up."

    scene mikupoolscene5
    with dissolve

    ka "A...Again...if that’s what you think is best..."
    s "It is. I’ve thought a lot about this. "
    s "Come on, Miku. We’re going now."
    mi "..."

    scene black
    with dissolve2

    "I make my way over to Miku and lift her off of the bench."
    "It’s clear that Karin is worried about what’s going on here and what I’ve decided to do, but that worry will only be temporary."
    "Once Miku goes back to normal and regains control of her limbs, this will all fade and there will never be anything to worry about again."
    "She’ll be good as new in no time at all. And it’ll all be because of me and how I avoided revealing to everyone that she’s casually overdosing on medication that wasn’t prescribed to her."
    "You’re welcome, Miku. And Io. And everyone else that I am saving and/or protecting by deciding to do this."
    "This is the right choice. I am making the right choice."

    play sound "static.mp3"
    scene mikupoolscene6
    with flash
    stop sound

    "I am making the right choice."
    "And if anything happens to her, it won’t be my fault. "
    "Except it will. "
    "But it won’t."
    "It will be Io’s fault. "
    "I told her to stop this. "
    "I did my part."
    "And there’s nothing I could have done to avoid this."
    "Which is why I will fix it now."
    "Which is why I will take her home."
    "And it is there she will recover and we’ll laugh all about this the next time we talk."
    "I am making the right choice."

    ka "Sensei?...Is she a little heavy after all? If you really need help, I can-"

    scene mikupoolscene7
    with dissolve

    s "No. I’m fine. I’m making the right choice."
    ka "I...I trust your judgement. But again, please let me know as soon as-"

    scene black
    with dissolve

    s "Come on, Miku. It’s time to go home."
    ka "As soon as..."
    ka "...you get to her room."

    scene noonsky
    with dissolve2

    "This isn’t so bad."
    "She really {i}is{/i} light."
    "And she doesn’t even smell like chlorine since she never made it into the pool today."
    "All things considered, this could have gone a lot worse."
    "People could be looking at me."
    "But no one seems to care that I’m carrying a partially conscious teenage girl wearing nothing but skintight latex to {b}GOD{/b} knows where in broad daylight."
    "This is a totally normal thing and I’m totally normal for doing it and Miku is going to be totally fine and it’ll be totally awesome."

    play sound "static.mp3"
    scene mikupoolscene8
    with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    "Oh, okay. I guess we’re here now. That’s good. I saved the day."

    s "..."
    mi "..."

    "I wonder when her eyes closed."
    "She’s still breathing. I can see the air exiting and entering her body. Just not the literal air. What I mean is that her body is moving. But only the part that air goes into. Which I guess also isn’t accurate but-"
    "Anyway, we’re here. I did my job. Time to put Miku into her bed and then leave because what she needs is rest and not medical attention. You know what they say about time being the best medicine and all."

    play sound "static.mp3"
    scene mikupoolscene9 with flash
    stop sound
    play sound "tackle.mp3"
    with hpunch

    "Okay. She’s in bed now. Job done."
    "But is it okay if she stays like this? Should I take her clothes off? Is she too hot? Is she too cold? Does she need another blanket or no blanket at all?"
    "Wait. There was something else I was supposed to do, wasn’t there?"
    "I have to call someone."
    "But who-"

    play sound "phonebeep.wav"

    "Nevermind. I remember."

    s "..."
    s "..."
    s "..."

    play sound "phonebeep.wav"

    "They answer."

    a "Hello?"

    play sound "phonebeep.wav"

    "Fuck. No. Not her. Someone else."
    "Uhh..."
    "Screw it. They’ll contact me if it’s really that important and I can just say I don’t remember anything."

    mi "...nh."

    "A sound slithers through the slight gap in Miku’s lips then grows legs, sprints across the mattress, and throws a grappling hook over my shoulder before climbing up and entering me through my left nostril. "
    "A small man that was living inside of Miku spends the rest of his life building a home inside of my cranium and we all live happily ever after. Isn’t symbolism just the coolest?"

    scene mikupoolscene10
    with dissolve2

    mi "Ah..."
    s "..."
    mi "..."
    s "..."

    "Just like I said — I did my job and now everything is good."
    "I have saved Miku’s life and prevented all of us from suffering or losing a valuable member of the class in one fell swoop."
    "Ami would be so proud of me if she could see me right now."

    play sound "phonebeep.wav"

    "But I’ll call her again just to make sure."

    s "..."

    play sound "phonebeep.wav"

    "Here she is."

    scene mikupoolscene11
    with dissolve

    a "Hey! What’s going on? I kinda figured the first call was just an accident since you hung up right away. Do you actually need something?"
    s "No. I just wanted to tell you I did a good job today."
    a "You...do a good job every day, Sensei. Did something happen, though?"
    s "No. Nothing happened except for the good deed I did."
    a "..."
    s "..."
    a "Where are you?"
    s "Everywhere and nowhere, all at once."
    a "Do you need me to come get you?"

    play sound "phonebeep.wav"

    "I hang up the phone because Ami doesn’t understand and redirect my attention to Miku, whose eyes are now open because I did a thing."

    mi "Sensei?..."
    s "That’s my name. Just it isn’t. My real name is Akira. Hello."
    mi "Wass...goin’ on?..."
    mi "Feel like I was just at school a minute ago...How’d I get here?..."
    s "I carried you here because I’m awesome and responsible and was protecting you from the nurse so we can keep spending time together in the future and I don’t have to leave."
    mi "You carried me here...all the way from school?...Why?..."
    s "Because you’re a fucking idiot and have been taking random pills that Io gives you for an indeterminate amount of time now."
    mi "Huh?..."
    mi "But I didn’t even take any of those today..."
    s "What?..."

    scene mikupoolscene12
    with dissolve

    mi "Or maybe I did...I don’t remember..."
    s "Well, you’re not anymore. You’re done. No more medication without seeing a doctor first."
    mi "Io says doctors are the worst..."
    s "Io says everyone is the worst."
    mi "Not me...Io likes me..."
    s "No, Io likes playing pharmacist — which you go along with because you have the IQ of a rhinoceros beetle and don’t understand the potential consequences of your actions."
    mi "Maybe...{i}you’re{/i} the one who doesn’t understand?..."
    s "That’s exactly what she told me. But you’re both wrong. How much did you take today?"
    mi "I already told you, I don’t remember. But I won’t take that much again. Promise."
    s "You can’t keep that promise if you don’t even know how much it was, Miku."
    mi "Heheh...you got me..."
    mi "Thanks for carryin’ me, though...That was real nice of ya..."
    s "The alternative was taking you to someone who would have understood what was happening and it would have spiraled into something horrible."
    mi "How come understanding what’s happening has to be bad?..."
    s "That part isn’t bad. The bad part is how I wouldn’t have been able to keep my mouth shut and how Io could get in trouble for it and how Makoto would stop having sex with me."
    mi "That’s fine...You can just have sex with me instead..."
    mi "I probably don’t know the same sex moves as her, though..."
    s "..."
    mi "Come on..."
    mi "What’re ya waitin’ for?..."
    mi "Do it already..."
    mi "That was your invitation, Sensei..."
    mi "Ya gonna make me spell it out?..."
    s "Miku...are you out of your mind?"

    scene mikupoolscene13
    with dissolve

    mi "Yeah."
    mi "I kinda am."
    mi "That’s kinda why I started seein’ Dr. Io in the first place. And it’s been workin’ out real well."
    mi "Just look how long my hair’s gettin’. I ain’t pulled any out in months. And I ain’t scared of anything anymore."
    mi "Worst thing that’s happened is you havin’ to carry me home. But even that ain’t bad since ya get to stick it in me now."
    s "Absolutely not. "
    mi "Really? Is that thing about boys wantin’ sex all the time just a rumor after all? I fall for those pretty easily, so it wouldn’t be weird if I was wrong."
    s "I’m not going to have sex with someone coming down from a minor overdose."
    mi "How long do we gotta wait? Cause I can’t really feel anythin’ right now and figured this would be a good chance to give you my v-card without gettin’ hurt."
    s "If you’re okay, I’m going to leave now."
    mi "Without even fingering me? But we’re all alone. Ya gotta give me somethin’ here."
    s "I don’t have to give you anything. And, to be honest, I kind of don’t even want to look at you right now."

    scene mikupoolscene14
    with dissolve

    mi "You...bein’ serious?..."
    mi "I can’t really tell..."
    s "I am. This isn’t like you, Miku. You’re not the type of person to do things like this."
    mi "S’cuse me for puttin’ it bluntly, but...the heck do you know about who I {i}really{/i} am?"
    mi "You ain’t got the first idea of what I’m dealin’ with. You don’t get it at all, Sensei."
    s "It’s hard to get something when you’d rather knock yourself out than open up to me."
    mi "You’re the same friggin’ way."
    mi "I don’t know anythin’ about {i}you{/i} and I still squeeze the cum outta ya because I’m a good friend and we don’t {i}need{/i} to know that kinda stuff about each other."
    s "And that’s fair. But your way of avoiding difficult confrontation is slowly killing you. "

    scene mikupoolscene15
    with dissolve

    mi "So is yours...only difference is that ain’t nobody strong enough to carry you home..."
    s "That’s not the same thing, Miku. This is-"
    mi "Listen, Sensei — my head is kinda poundin’ and my throat is really dry, so if you’re not gonna stick your wiener in me, could ya maybe let me take a nap or somethin’? Thanks."
    s "I don’t like this side of you, Miku. This isn’t the person I know."
    mi "Cry me a friggin’ river. Night, Sensei."
    s "..."
    mi "..."
    s "..."
    mi "..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "There will be no river, nor tears at all-"
    "For it hurts the most {i}before{/i} the fall."
    "Then afterwards, with broken bones-"
    "And flesh untucked from dermal homes-"
    "The sky is where we find salvation."
    "Our final sight and last sensation."
    "As eyes roll back, and respiration-"
    "Contorts our lungs in expiration-"
    "We’ll rely on half-unpacked narration"
    "And take shelter in these new vibrations."

    s "..."

    "This one was me."
    "But I wish that it wasn’t."
    "So I’ll forget it immediately."

    s "..."

    "There is no narrator I can ever rely on."
    "Everyone just wants to break me."
    "But no one can finish the job."

    $ renpy.end_replay()
    $ mikupool55 = True
    $ mikublock = True
    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love] for the remainder of the night, but it goes back down the morning after when she has trouble remembering what happened.{/i}"
    "{i}You hurt yourself when you got home, but only you will know what that means.{/i}"

    jump advancetothurs

label mikudorm55p1:
    stop music
    play sound "static.mp3"
    scene mikudoortime with flash
    stop sound
    play sound "knock.mp3"
    play music "sweetervermouth.mp3"

    "I knock on Miku’s door a little too hard and wind up shattering the fabric of reality."
    "And while doing such a thing will make it relatively more difficult for me to look back on today in a moment of quiet contemplation once I get home, it’ll at least take up a few minutes as I try to fix stuff."
    "Normally, when the world breaks, I wind up breaking along with it."
    "But as I grow older and less desirable, that seems to stop being the case."
    "Now, any time the ground starts to shake and my hands begin to expand to seven times their original size, I can shove them in the pockets of my make-believe pants and start to think-"
    "Why are we here?"
    "Why am I here?"
    "Life is more than just knocking on doors and knocking up girls, isn’t it?"
    "Life is a bucket of fish heads, and each one of those fish has an extra eye to compensate for their inherent stupidity that you often seem to forget whenever you look at them."
    "In the moving of their mouths, you become unsettled. Quieted. And as you gaze back into the gaping darkness molded together by improper jaws, you remember we’re supposed to be in first person."

    play sound "static.mp3"
    scene mikudoortime2 with flash
    stop sound

    "Then I pick a peck of pickled peppers and wind up walking in on the Temptation of Saint Anthony."
    "{i}A rumbling approaches.{/i}"
    "{i}You can feel the ground begin to swallow you whole.{/i}"

    play sound "pop.mp3"
    scene mikudoortime3 with flash
    stop sound

    "{i}Then out pops renowned painter, Salvador Dali.{/i}"

    salvykun "Hola. Gracias por venir a mi casa. Soy Salvador Dalí."
    salvykun "¿Estás buscando la puesta de sol? "
    s "Sí. La puesta de sol es mi cosa favorita. Quiero tirarle cacahuetes y gritarle a los niños."
    salvykun "¿Niños?"
    s "Si niños."
    salvykun "Esa es una razón diferente a la que esperaba. Pero te ayudaré."
    salvykun "Pero primero, debes saludar a mi gato, Frankie."
    s "Hola, Frankie."
    salvykun "Has pasado mi prueba. Ahora, escucha mis instrucciones."
    salvykun "Primero, debes quitarte la lengua. Debes utilizar una cuchilla caliente. Eso evitará que mueras."
    salvykun "Después de que tu lengua se haya ido, debes correr en círculos. Haz esto siete veces. Cuando termines, mira al cielo."
    salvykun "Verás una cara. Será una cara especial. No será Frankie."
    salvykun "Dile a la cara, “tu salsa picante es deliciosa.” Luego, gira una vez. Después de eso, te dará una taza."
    salvykun "En la copa estará la sangre de un niño. Bébela. Saboreala. Sabrás cuándo parar."
    s "¿Hacer esto me ayudará a encontrar la puesta de sol?"
    salvykun "Sí. Esta es la única manera de hacer tus sueños realidad."
    salvykun "Pero ningún sueño se hace realidad sin sacrificar algo. Debes recordar eso. Puede que no valga la pena."
    s "Entiendo. Seguiré tus instrucciones para poder ver el atardecer. Acepto el sacrificio."
    salvykun "¿Tienes alguna otra pregunta para mí?"
    s "Sí. Tengo una pregunta más. ¿Dónde está Miku?"
    salvykun "¿Miku?"
    s "Sí. La chica de la vagina bonita y las piernas bonitas. "
    salvykun "Para llegar a la chica, debes ver el mundo a través de sus ojos."
    s "¿Cómo puedo hacer eso?"
    salvykun "Comienza mirando a través de las paredes."

    stop music
    play sound "static.mp3"
    scene mikufinetime1 with flash
    stop sound
    play music "painisreal.mp3"

    "I do what I’m told and peer through the walls, utilizing a special ability I’ve been hiding from you that allows me to see everything at all times even when I’m not there."
    "It’s something I’m only able to do because I’m the protagonist, but it really comes in handy when there are girls having mental breakdowns so I can watch them without getting in the way."
    "After all, every time I try to help Miku out of anything, I only make things worse."
    "I should have had sex with her when she was high on drugs the other day because it’s possible my semen has magical powers that would take away her post-traumatic stress disorder."
    "But instead, I’ll have to stay here on the other side of the wall, slowly thrusting my waist up against the operable part of it known as “DOOR” to create the illusion that I am humping her muscular nubile body. "
    "She doesn’t know I’m doing this. She’s too lost in her own world."
    "And oh how I wish to know what is happening inside of that world."
    "But alas — despite being able to see everything, I can not see into her head. For that is a wall I am incapable of penetrating. Much like this door."
    "One day, I will have a quirky, energetic tomboy to penetrate in the door’s stead. And it is at that point where all will be well and the world will be cured of its cancer."
    "I recall the Temptation of Saint Anthony and wonder what it was that tempted him in the first place."
    "I wonder if he was anything like me."
    "I wonder if he ever dry-humped a door."

    mi "It isn’t real."
    mi "It isn’t real."
    mi "None of it’s real. It isn’t real."
    mi "None of it’s real."
    mi "It isn’t real."
    mi "Nothing is real."
    mi "It isn’t real."

    "{i}A silverfish crawls across Miku’s left foot, but she is too busy dissociating to notice it.{/i}"
    "{i}It crawls inside of an open bottle of iced tea on her desk and waits to be consumed so it can have a shot at laying its eggs inside of her digestive tract.{/i}"

    play sound "static.mp3"
    scene mikufinetime2 with flash
    stop sound

    "{i}Little does it know, no silverfish has ever succeeded in such an endeavor.{/i}"
    "{i}And little does it know, the world beyond itself is far too big to even give a fuck about what a silverfish can do or is or wants or anything because what the fuck even is a silverfish?{/i}"
    "{i}One thing is certain. It’s not an actual fish. Its entire existence is an enigma and a lie and the only reason you’re getting this narration anyway is because I’m bad at symbolism.{/i}"
    "{i}I’m bad at everything. And I am being eaten from the inside out in my attempts to recreate what is or isn’t perfect while you watch from behind a wall with your cock pressed up against the door.{/i}"
    "{i}But the craziest part of all is that there are people even worse than you.{/i}"
    "{i}And you never know what those people are doing with doors.{/i}"

    stop music
    play sound "static.mp3"
    scene black with flash
    stop sound

    "I’m sorry."
    "I keep letting it fester."
    "But I woN’T keep It THat WaY any LOnger."
    "I wilL SHow yoU why I AM the Way i AM."
    "And why the month of July no longer exists for me."

    play sound "static.mp3"
    scene mikudoortime4 with flash
    stop sound
    play sound "likepigstopigwater.wav"

    "The essence of eiderdown lays waste to the room and carries with it the haunting ideology that nothing is real except what {i}we{/i} feel."
    "There is no one but you."
    "Nothing else will ever feel what you can."

    stop sound
    scene black

    "Unless you make them."

    play sound "static.mp3"
    scene mikufinetime3 with flash
    stop sound
    play music "nowhereissafe.mp3"
    $ renpy.pause(7, hard=True)

    "Somewhere, beyond one wall and then another, a lonely girl finds herself in a labyrinth of dislodged memories."
    "They run circles around her, kicking what’s become the purpose of her life into a giant net that blankets a special world she’ll see for one night only."
    "Tomorrow, it will be a new one. It is {i}always{/i} a new one. And at the behest of an of army of pseudo-nostalgic visions, she can now say things like “It’s been that way forever.” But she is wrong."
    "There was a time long ago, before the nets and night terrors, where she’d sleep peacefully in the warm bed of a warm house where a warm family lived."
    "She’d scarf down microwaved dinners as if her life depended on them, and spend weekends nestled between the left thigh of a woman and the right thigh of a man."
    "Every once in a while, the three of them would fall asleep there — and she’d be carried off to that warm bed once one of them woke up."
    "The following day would mark a reset — just not the kind you’re familiar with."
    "School. "
    "Then soccer. "
    "Then another microwaved dinner. "
    "Another late night television show — but only on the weekends. "
    "It was a schedule that she’d have been happy following for the rest of her life. But of course, this was back before she understood the value of life at all."

    play sound "static.mp3"
    scene mikufinetime4 with flash
    stop sound

    "She gets it now. "
    "She pretends not to because that makes it easier to forget, but she knows."
    "Better than anyone perhaps. "
    "In fact, she’s so aware of the fragility of human life that things as simple as loud noises or doors opening too quickly send her spiraling so far down that she winds up {i}here.{/i}"

    play sound "static.mp3"
    scene mikufinetime5 with flash
    stop sound

    "But down here isn’t much safer."
    "You’d think that retreating to the confines of your mind would be a good method when it comes to {i}protecting{/i} yourself from the things you’re afraid of on the outside, but that isn’t always the case."
    "When the inside is just as scary and just as threatening as what you’re hiding from, there’s no way to ever feel safe at all...is there?"
    "So, what happens then?"
    "Do you try to block it all out?"
    "No. You can’t."
    "Do you try to rely on others instead?"
    "No. You can’t do that either. It’s too hard."
    "Do you just {i}accept{/i} the suffering? And pretend that you’re okay even when you’re not?"
    "That’s one way of handling things. And it’s the one you’re most familiar with by now."
    "But there’s an easier method than even that."
    "It’s to let the light and the dark in all at once."

    play sound "static.mp3"
    scene mikufinetime6 with flash
    stop sound

    "It’s to let both of them become a part of you, so that the good blends in with the bad and turns everything into a palatable shade of gray that no one {i}else{/i} will understand, but {i}you{/i} will."
    "But that means you’ll realize it doesn’t fix anything. It just makes everything monotonous and boring. But monotonous and boring is better than being afraid, isn’t it?"
    "But wait. There are still good memories in there somewhere. You can feel them- crawling across your skin like silverfish. Tickling your toes like the essence of eiderdown."
    "Desperate to see more, you try to let the light in."
    "But the dark has become so interchangeable with it at this point that both shades flood your conscience and make you back into the person you became that day."

    play sound "static.mp3"
    scene mikufinetime7 with flash
    stop sound

    "But who {i}is{/i} that person, exactly? And why does it always feel like there’s something else inside of you trying to slither out?"
    "The answer to that is simple. Something {i}is{/i} trying to slither out."
    "But it’s not the need for revenge. It's not anger that you’ve become this mess of a once happy creature."
    "Nor is it fear or uncertainty- or the desire for someone or {i}something{/i} to tie a rope around your waist and pull you out of the hell you’ve fallen into."
    "It’s {i}confusion.{/i}"
    "You want to {i}understand.{/i}"
    "But there are many things in life that just don’t make sense."
    "Like the way light reflects off of floating dust particles."

    stop music
    play sound "static.mp3"
    scene mikufinetime8 with flash
    stop sound

    "Or how quickly everything you love can disappear."
    "Oh, how deeply you wish for it to all become clearer."
    "For the sun to set on your tragic past."
    "But some things are just meant to stay opaque."

    scene black

    "Some things, you will never understand."
    "........."
    "......"
    "..."

    scene dorm
    play music "sweetvermouth.mp3"
    play sound "knock.mp3"

    "I knock on Miku’s door and wait for her to answer."

    stop music
    play sound "static.mp3"
    scene mikufinetime9 with flash
    stop sound
    play music "lastdailysong.mp3"

    "But I wind up entering before she has a chance to."

    mi "...................."
    s "Miku?..."
    mi "..."
    s "Is...everything okay?"
    mi "..."
    s "Uh..."
    mi "You..."
    s "What about me?"
    mi "This is {i}your{/i} fault."
    s "What? "
    s "{i}What’s{/i} my fault? I wasn’t too loud coming into the room, was-"

    play sound "static.mp3"
    scene mikufinetime10 with flash
    stop sound

    mi "You know what you did!"
    s "I...have no idea what I did."

    scene mikufinetime11
    with dissolve

    mi "Liar! {i}LIAR!{/b} You don’t like the new me! So you made Io stop giving me medicine! I know it was you!"
    s "I...I don’t think it was?"

    scene mikufinetime12
    with dissolve

    mi "Liar! Liar liar liar liar liar! Give it back! Make her give it back!"

    "I know I talked to Io about this recently, but...she didn’t actually listen to me, did she?"
    "I could have sworn she was able to silence {i}me{/i} in that talk. I didn’t think she’d actually take any of it to heart after all was said and done."
    "But I guess the reason {i}why{/i} she did this isn’t important now. What matters at the moment is dealing with the fallout."

    s "Miku, I’m not sure if I had anything to do with Io’s decision or not...but you could have seriously hurt yourself just trusting her to-"

    play sound "static.mp3"
    scene mikufinetime13 with flash
    stop sound

    mi "Ngah! Aah!....NGAAAAH!"

    play sound "static.mp3"
    scene mikufinetime14 with flash
    stop sound

    s "Miku, I’m not going to let you tear your hair out right in front of me when you were literally {i}just{/i} talking to me about how long it's getting. "
    mi "Get your hands off of me! Where’s Io?!"
    s "Io’s not here. You can deal with me right now."
    mi "I can’t deal with {i}anything{/i} right now! I need Io! I need my medicine! Why are you keeping it from me?!"
    s "So we can get you an {i}actual{/i} prescription rather than one your classmate just decided to share."
    mi "No! I want what Io has! Give it back! I know you have it!"
    s "I don’t have anything. You need to see a doctor. An {i}actual{/i} doctor."
    mi "No! No, no, no, no!"

    scene mikufinetime15
    with dissolve

    mi "You can’t make me! Let go! I’ll do anything you want! Anything! Just give it back!"
    s "I already told you- I don’t have anything. There is nothing {i}for{/i} me to give back."
    mi "Why do you keep lying to me?! What have I ever done to you?! Why don’t you like the new me?! Why do I have to be sad?!"
    s "Miku, why won’t you just go to the doctor?"

    scene mikufinetime16
    with dissolve

    mi "Because they’ll make me talk!"

    scene mikufinetime17
    with dissolve2

    mi "Because they’ll make me talk..."
    s "..."

    scene mikufinetime18
    with dissolve

    mi "Please..."
    mi "Just give it back..."
    s "..."
    mi "{i}Please...{/i}"
    mi "I need it..."
    s "I don’t have anything, Miku. I mean it."

    scene mikufinetime19
    with dissolve2

    mi "AaAAAAAaaAAAAAah!!!!!!! "
    mi "AAAAhhhAAaaaHhhhh!!!!!!!...Hah....aaaah.....aaaaaahhhhH!!!!!!!"

    "Miku pounds at my chest, drenching my shirt in tears as I pull her closer to try and calm her."

    scene black
    with dissolve2

    "She doesn’t relent, no matter how hard I try. "
    "And it isn’t until Makoto comes home that I get a moment to breathe."
    "This time, there is no misunderstanding. "
    "She simply asks me to go home and I oblige- surrendering a hysterical Miku to her so she can try and make up for what I obviously lacked in."
    "For what I {i}always{/i} lack in."
    "But the problem isn’t that I’m incapable of understanding- it’s that I understand a little {i}too{/i} well. "
    "And I’m sure that all of my advice sounds just as half-hearted as it feels coming out."
    "If I had actually been the one responsible for taking away Miku’s medication, I probably would have caved tonight and given it back to her."
    "And I probably would have {i}kept{/i} doing that until another tragedy occurred."
    "I understand that she’s in pain."
    "I understand that she’s afraid."
    "But more than anything-"
    "I understand what kind of animals we become when we’re cornered."
    "When we feel like we have nowhere else to go."
    "And how dangerous we become to not just everyone, but {i}ourselves{/i} when we instinctively lash out."

    scene bedroom_night
    with dissolve2
    stop music fadeout 10.0

    "When I arrive back at home, most of her tears have already dried. "
    "But there’s a small damp spot on my shirt that makes me think of her."
    "And I lie on my stomach so I can feel it when I fall asleep."

    scene black
    with dissolve2

    "As hard as I try to dream about her, I’m unable to."
    "It’s just dark."
    "The same way it always is."

    $ renpy.end_replay()
    $ mikublock = False
    $ mikudorm55p1 = True
    $ miku_love -= 10

    "{i}Miku’s affection has decreased by 10!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm55p2

label mikudorm55p2:
    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    scene bedroom_day
    with dissolve4

    "When the morning comes, the night prior feels as if it never even happened."
    "Like it was all some sort of dream dreamt in advance before my subsequent slumber and an even more subsequent sea of black."
    "The first thing I think about when I wake up is thanking my organs, though I’m not quite sure why."
    "Though, I know there must be some sort of correlation between the spontaneity of such a nonsensical desire and the much more sensical (Which isn’t actually a word for some reason) need to see Miku again."
    "The second thought I have is that it might be time for a change of color."
    "I could paint my room. Or get a new shirt. Maybe even dye my hair and start my “bad boy” phase."
    "A third and mostly related thought is that something needs to change."
    "A fourth is that something will."
    "And a fifth is that I’m not sure if I’ll like it or not."

    scene black
    with dissolve2

    "My sixth thought involves getting dressed."
    "The seventh, leaving the room."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene mikuvisitafter1
    with dissolve2
    play music "wewereangels.mp3"

    a "Oh, good timing. I was just about to come get you and passive-aggressively ask why Miku is here to see you this early in the morning."
    s "That’s a good question, Ami...I was under the impression I was going to have to go see {i}her.{/i}"
    mi "Hahah...hah..."
    mi "Sorry if I’m gettin’ you in trouble, Sensei. I just...you know...wanted to talk about last night and stuff..."
    a "Well, I didn’t like that sentence one bit."
    s "It’s not like that, Ami. There was just-"

    scene mikuvisitafter2
    with dissolve

    a "You don’t {i}have{/i} to tell me, Sensei. I’m just being difficult because that’s what I’m used to doing."
    a "I’ll leave you two alone. I have to go to work anyway. We just added a bunch of new menu items and Uta wants all of us to remember them by Tuesday."
    s "You’re going to just...leave me alone in the house with another girl?"

    scene mikuvisitafter3
    with dissolve

    a "It’s just Miku. It’s not like I’m leaving you here with Kirin or Noriko. Plus, everyone knows better than to show up for funny business with you while {i}I’m{/i} home. "
    a "The {i}real{/i} risky ones are the girls who do it behind my back. So Miku actually gains points for asking me if she could come inside."
    a "Not like she needs or wants them, though. This is probably just to clear up some sort of misunderstanding, right?"

    scene mikuvisitafter4
    with dissolve

    mi "I’m not really sure if...“misunderstanding” is the right word, but...I ain’t lyin’ when I say I’m not here for any sorta funny business."
    a "Well, all I can really do is take your word for it. So, whatever is going on, I hope you two can figure it out. "
    a "Until then, I have like five soups and a few drinks to memorize."
    s "That doesn’t seem like that many, Ami."

    scene mikuvisitafter5
    with dissolve

    a "Then I’ll be back before there’s even a {i}chance{/i} for any funny business."

    scene mikuvisitafter6
    with dissolve

    a "Breakfast is in the fridge and coffee is already brewed! Have a nice day, Sensei! I love you!"

    play sound "dooropen.mp3"

    "Ami...{i}leaves the house.{/i}"
    "And suddenly, there are two girls I need to bring to the doctor."

    mi "..."
    s "..."
    s "So, how are we tackling this? Because, based on the way you’ve been nervously fidgeting since I came out of my bedroom, I doubt you’re going to be yelling at me again."
    mi "Course I ain’t gonna yell at you, Sensei. Shouldn’t have yelled at ya last night either. That’s kinda the first thing I wanted to talk about."
    s "Well, go ahead. You can take the reins on this one. I’ll just stand here and figure out what I’m supposed to do with you."
    mi "Yeah...yeah, that’s...fair..."

    scene mikuvisitafter7
    with dissolve

    mi "Hahah...this...this feels kind of familiar, right? You remember the first time you found out about my...brain thingy? And how I had to apologize back then too?"
    s "I do. But I also remember that I’m the one who visited {i}you{/i} back then."

    scene mikuvisitafter8
    with dissolve

    mi "And I was surprised you did..."
    mi "Kinda figured you’d want nothin’ to do with me after freakin’ out on ya like that. "
    mi "But...it’s been a long time since then and...it might not seem like it to you, but I think I’ve changed a lot. And you and me are...a lot closer now. Even if it’s just...you know...in a naughty way..."
    s "It’s not {i}just{/i} that, Miku. "
    mi "I know, yeah. Yeah. But, like...what I’m sayin’ is...I’m like..."
    mi "I trust you now...and stuff...and just sittin’ around and waitin’ for {i}you{/i} to come to {i}me{/i} gives me all sorts of...butterflies and...yeah..."
    mi "To tell ya the truth, I’ve actually been wanderin’ around your neighborhood for, like...four or five hours or something."
    s "What? It’s only like 9:00 AM."
    mi "Yeah...I couldn’t really sleep."

    scene mikuvisitafter9
    with dissolve

    mi "But I was nice enough to let {i}you{/i} sleep in, so...I didn’t do anything wrong. Right? I just couldn’t really...you know..."
    mi "Waiting is..."
    s "..."
    mi "..."

    scene mikuvisitafter10
    with dissolve

    mi "Sensei, I’m really sorry. I’m sorry I keep puttin’ you in positions like this because of the kinda girl I am."
    s "This position is a little different from that first one, Miku. This is way more serious."
    mi "I know, I know. That first time, you could’ve given me a pass or somethin’. But {i}this{/i} time, I’ve {i}gotta{/i} apologize because {i}this{/i} time I actually messed up. Like, a lot."
    mi "It ain’t like I’m gettin’ all weird because of my...condition. I blamed you for a thing you didn’t have anythin’ to do with and that was all sortsa messed up in a million different ways."
    mi "I know you were just tryin’ to help. And even if it {i}was{/i} you who took everythin’ away, I shouldn’t have gone off on ya like that."
    s "You’re giving me too much credit, Miku."

    scene mikuvisitafter11
    with dissolve

    mi "What do you mean by “givin’ you too much credit?”"
    s "I mean that saying I was just trying to help is making me sound a lot better than I actually am when I shrugged this off time and time again."
    s "If I really wanted to help, I would have done something sooner."
    mi "That ain’t true. Buttin’ into somebody else’s life ain’t always easy, Sensei. I ain’t gonna blame you for not doin’ somethin’ earlier. I’m sure you had your reasons."
    mi "But the point is...I get how dangerous what I was doin’ was now. And I ain’t gonna do it anymore. "
    mi "Maki’s gonna take me to a real doctor and...I’m gonna figure out where to go from there."
    s "Sounds like a lot has happened in the last twelve hours, huh?"

    scene mikuvisitafter12
    with dissolve

    mi "Friggin’ tell me about it. "
    s "No. You tell {i}me{/i} about it. What {i}did{/i} happen after I left last night?"

    scene black
    with dissolve2

    "Miku agrees to open up about what happened when Makoto came home, and the two of us make our way over to the couch..."

    scene mikuvisitafter13
    with dissolve2

    "There’s a moment of silence when we get there, but it’s no different from the hundreds of other moments of silence I’ve had before hundreds of other difficult conversations."
    "And while Miku’s managed to avoid most of those, she does have her moments every now and then. It’s just hard for her to have more substantial ones when she’s still so secretive about everything."
    "I don’t blame her for that. How could I? I’m just noting that it makes things harder."
    "But no one said this would be easy. No one said {i}any{/i} of this would be easy, and I’m learning more and more of exactly what that means every single day."
    "There’s likely nothing I can do to help her. But I can {i}listen.{/i}"
    "And sometimes, that’s all a person needs."

    mi "Without beatin’ around the bush, nobody took anythin’ from me at all. I just...kinda forgot where I put the bag Io gave me."
    mi "I had a bad episode before school that day, so I took a little too much to try and calm myself down and...must’ve put what was left somewhere I wasn’t exactly used to or somethin’."
    mi "But...that ain’t gonna be a problem anymore since Makoto found it before I was able to and gave me the lecture of a friggin’ lifetime."

    "Ah...so it wasn’t a change of heart for Io after all. "
    "I should have known."

    s "So Makoto knows now?"

    scene mikuvisitafter14
    with dissolve

    mi "I told her everythin’ except where I was gettin’ ‘em."
    mi "I didn’t wanna throw Io under the bus like that when she’s got enough goin’ on."
    s "And how did Makoto take that?"
    mi "She was shocked. Cried a lot. Asked me a bunch of questions I had a hard time answerin’ since I was panickin’ the whole time."
    mi "Seein’ her like that started to calm me down, though. Felt like I was bein’ a...huge disappointment after all she’s done for me. So I just started spillin’ out my guts all rapid-fire like."
    mi "She flushed the leftover medicine down the toilet and called Maki to make an appointment thingy for me. Didn’t even care that I didn’t wanna talk to them. Just didn’t want me to get hurt."

    scene mikuvisitafter15
    with dissolve

    mi "I left you out of it too, ya know. Far as Makoto’s concerned, you were just in the wrong place at the wrong time."
    s "I doubt she’s going to buy that I wasn’t at least partially involved in this. She’s too smart for that."
    mi "You really weren’t, though. All ya did was try and talk me out of it. You tried talkin’ Io out of it too, didn’t ya? So why do you keep blamin’ yourself for this?"
    s "Because I’m an adult. It’s my responsibility to do something about stuff like this if I’m made aware of it."
    mi "The heck’s bein’ an adult have to do with anythin’? People are people and talkin’ to {i}other{/i} people can get pretty hard. You ain’t responsible for me."
    s "I literally {i}am.{/i} I’m your teacher. "
    mi "But you’re also my friend, ain’t ya? And that’s the sorta thing most friends who aren’t named Makoto would have a tough time dealin’ with."
    mi "Only one to blame here is me. I’m an idiot and didn’t realize what I was gettin’ myself into. But thanks to you guys, I’m gonna try and be better from now on. Promise."
    s "Is there anything you need from {i}me?{/i}"

    scene mikuvisitafter16
    with dissolve

    mi "..."
    s "If there’s any way I can help, just tell me. I’m obviously no doctor- and if you want to absolve me of my partial responsibility for what happened, fine. But if there’s {i}anything{/i} I can do-"
    mi "There..."
    s "..."
    mi "Um..."
    s "..."

    scene mikuvisitafter17
    with dissolve

    mi "Okay, so..."
    mi "Remember how I was talkin’ about how far we’ve come and how much I’ve changed and...and how much I trust you and all that?"
    s "That wasn’t all that long ago, so...yeah. I remember."
    mi "Well...um..."
    mi "I’m..."
    mi "Uhh..."

    scene mikuvisitafter18
    with dissolve

    mi "There...there ain’t a lot of people who know about...{i}why{/i} I’m like this...and why I ain’t good at talkin’ about it or...how I kinda {i}can’t{/i} talk about it..."
    mi "But if I’m gonna be ruinin’ your life all the time like I {i}have{/i} been, I think I owe it to you to at least {i}try{/i}...especially if they’re gonna make me tell this story to doctors and stuff soon..."
    s "Are you {i}sure{/i} you want to tell me?"
    mi "No. But if you keep askin’ me questions like that, chances are I’m never {i}gonna.{/i} I can’t have an option when it comes to this. I’ve gotta just...I’ve gotta do it. I’ve gotta tell you."

    scene mikuvisitafter19
    with dissolve

    mi "When I..."
    mi "Umm..."
    s "..."
    mi "Uhh..."
    mi "Sorry...it’s been years since I’ve had to...I don’t even know how to..."
    s "Take your time. It’s fine."

    scene mikuvisitafter20
    with dissolve

    mi "Hah..."

    scene black
    with dissolve2

    mi "When I was little..."
    mi "Two men broke into my house."

    play sound "static.mp3"
    scene mikuvisitafter21 with flash
    stop sound

    int1 "{i}I don’t know about this...maybe we should leave?{/i}"
    mi "I got out of bed to get a drink of water or..."
    mi "Or maybe it was milk or..."
    mi "No. No, the drink doesn’t matter. But I got out of bed, walked down the hallway and..."
    mi "And there they were."
    int2 "{i}And do what? Go back home and go to sleep like we didn’t break into someone’s fucking house? Just be quiet and take as much as you can.{/i}"
    mi "Since I had just woken up, I wasn’t able to see really well, but...I could tell something was wrong."
    int1 "{i}They’ve got a kid...{/i}"
    mi "My dad...had friends over a lot. So at first I thought it might just be some of them, but..."
    int2 "{i}So do I. But if I don’t come up with enough money by the end of the week, that could change.{/i}"
    int2 "{i}We don’t have time for questions and observations. Just take anything that might be valuable. Now.{/i}"

    play sound "static.mp3"
    scene mikuvisitafter22 with flash
    stop sound

    mi "I...I think I heard one of them say something about...about taking our stuff, so..."
    mi "So I tried to be quiet and go tell my...my parents, but..."
    mi "I think...I think they might have heard me...or..."
    int1 "{i}Did you hear something just now?{/i}"
    int2 "{i}...{/i}"
    int1 "{i}...{/i}"
    int2 "{i}I...{/i}"
    int2 "{i}Whatever it was is gone now. So put the fucking frame down and start going through their drawers.{/i}"

    play sound "static.mp3"
    scene mikuvisitafter23 with flash
    stop sound

    mi "When I made it into their room, I shook them awake...I told them...I told them there were people in our house..."
    mi "And at first, they didn’t believe me. We...weren’t rich or anything, so...why would anyone...uh..."
    mi "Anyway...uhh...umm..."
    mi "When...when they finally heard something in the...living room or...maybe it was the kitchen? Or..."
    mi "Uh..."

    play sound "static.mp3"
    scene mikuvisitafter24 with flash
    stop sound

    mi "My dad...he...uhh..."
    mi "When the sounds...happened, he..."
    mi "The door and..."
    mi "And there was yelling and..."
    mi "And my mom had me hide under the bed and..."
    mi "There was more yelling and...then a bang..."
    mi "Then another and..."
    mi "And the yelling got quieter...and quieter..."
    mi "And quieter..."
    mi "And...and then it stopped..."
    mi "So I...from under the bed...I..."
    mi "Then...the living room and..."
    mi "And they were..."
    mi "Both of them were..."
    mi "I was...I couldn’t..."
    mi "I kept trying to wake them up..."
    mi "I didn’t believe it...I still don’t...I don’t understand..."
    mi "Why us?...What did we do wrong?..."

    scene mikuvisitafter25
    with dissolve

    mi "Was it my fault?..."
    mi "If I never woke up...If I never got thirsty...If I was quieter..."
    mi "Then maybe...maybe they would..."
    s "It’s not your fault, Miku..."
    mi "But...because of me...all of this happened...because of me..."
    s "There is no “because of” anyone. Some things just happen without a reason."
    mi "My mom...and dad..."
    mi "For no reason?..."
    mi "None?..."
    s "I don’t know. There’s nothing I can say here to make you feel any better."
    s "All I can do here is listen. "
    s "But I’m glad you finally told me."

    scene mikuvisitafter26
    with dissolve

    mi "That’s why...any time I hear a loud noise, I..."
    mi "It’s like I’m {i}back{/i} there..."
    mi "In my old house..."
    mi "Trying to wake them up..."
    mi "But..."
    mi "But they never do..."
    s "..."
    mi "..."
    mi "I just want it to stop."
    mi "I want to stop going back there."
    mi "I need help."
    s "You’ll get help if you’re willing to admit that. Maki will make sure of it. Makoto too."
    mi "I’m a burden to them. They’ve done so much for me and all I am is a burden to them."
    s "Don’t feel too bad about that. I’m a burden to everyone around me and I’m able to live with myself just fine."
    mi "Can I use your bathroom please?"
    s "Only if you promise you’re not going to pull your hair out in there."
    mi "Then can I use your bed?"
    s "Yes, Miku..."

    scene black
    with dissolve2

    s "You can use my bed."

    "I sit on the floor as Miku sobs herself to sleep for the first time in over twenty-four hours."
    "And I silently applaud her for being much stronger than I am at less than half my age."
    "The mystery’s been solved. And even though some of the details are still a little fuzzy, that’s okay."
    "I don’t need to know everything."
    "Because what I {i}do{/i} know now is more than I deserve."
    "But it’s enough to make me want to stand by her every step of the way."
    "Even if I have to walk on glass."

    $ renpy.end_replay()
    $ mikudorm55p2 = True
    $ miku_love += 10
    stop music fadeout 10.0

    "{i}Miku’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2

    "When Ami comes home, I thank her for leaving Miku and me alone today."
    "She returns the favor with samples of five different types of soup and a hug that lasts the rest of the night."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    jump advancetomon

label mikuspring1:
    scene bedroom_day
    with dissolve2

    "Another day means another chance to fall into an uncovered manhole and be eaten by the secret alligators in the catacombs of Kumon-mi."
    "That probably isn’t the most constructive thought I’ve had first thing in the morning lately, but at least it’s an interesting one."
    "Being eaten by an animal would be a good way to go. And no one would be able to get mad at me for it since the animal would be too easy to blame."
    "And also, it would give those I care the most about a fun story when they’re recollecting their youth fifty years from now to grandchildren who will have escaped the shade of my family tree."
    "I’ve been talking to myself a lot lately."
    "I don’t mean to, but it’s a thing I keep doing and I don’t understand why."
    "It’s never anything interesting. Mostly just quick utterances of vague fatalisms like “I want to die” or “I fucking hate myself,” but they always make me feel off because I’m the only one around to hear them."
    "And I already know those things. I gain nothing from watching them fall from the horse’s mouth. I {i}am{/i} the horse. Complete with oversized penis and everything."
    "I don’t know."
    "I hope something interesting happens today."
    "I hope I get to see an alligator."

    play sound "phonering.mp3"

    s "..."

    "My phone rings."

    play sound "phonebeep.wav"

    "I press the button that bridges the gap between where I am and where I’m never meant to be."

    s "H-"

    play music "notabluearchivesong.mp3"
    with hpunch

    mi "Good friggin’ mornin’, Sensei! Or, as they say in the states, “Good friggin’ mornin’!”"
    s "Well that’s certainly a joke that doesn’t translate very well."
    mi "I don’t get it. But there’s tons’a stuff I don’t get, so I’m willin’ to overlook that in favor of gettin’ the talk-ball rollin’!"
    s "The...what?"
    mi "Idunno, I’m just sayin’ stuff at this point. How ya been lately? Wiener still floppin’ around all floppy-like and stuff?"
    s "I...guess so?"
    mi "Great! Cause that means you can bring it on over here for a day of action and adventure, Miku-style!"
    s "New Miku style? Or old Miku style? Because those are very different things and require very different levels of participation on my end."
    mi "Mmm...old Miku style? I ain’t tryin’ to put it in my mouth today. Just wanna see your face and stuff."
    mi "It’s been a while, hasn’t it?"
    s "Yeah. Life is kind of terrible. Sorry I haven’t been keeping in touch."
    mi "Nah, I get it. I’ve got too much energy for even Makoto sometimes and she’s been dealin’ with me forever. But a little dose every now and then ain’t all that bad, right?"
    mi "Oh, and before ya go misunderstandin’ that last part — that ain’t, uhh...whaddy’a call them things again? Metal...forks?"
    s "...Metaphors?"
    mi "Yeah! That “dose” thing ain’t a metal fork for medicine. I’ll have ya know I’m still goin’ strong without that stuff! Therapy’s been okay, though. Talkin’s still hard. And I haven’t even gotten to the tough stuff yet."
    mi "Oh! And my grade’s are doin’ kinda okay now! And...let’s see...what else is goin’ on...hmm..."
    mi "Swimming! Yeah! The club’s been-"
    s "Are you just...going to recap me on everything that’s been happening in your life the last couple months? Right now?"
    mi "Is now a bad time? Should I call back later?"
    s "I mean...if it’s going to be long, I can just come see you."
    mi "You’re actually okay with that? Kinda figured you were gonna shoot me down."
    mi "We ain’t hung out in months and you ain’t been in any rush tryin’ to put an end to that. Which is perfectly fine! I know things are tough right now."
    s "We can meet. It’s not like I’ve been avoiding you on purpose or anything. That’s just...sort of a side-effect of all of this."
    mi "Awesome! Can ya come to the park, then? I’m havin’ a picnic thingy with Io and Uta and I’m sure they’d be happy to see you too! "
    mi "Three girls at once ain’t too much, is it?"
    s "Three girls at once is actually a major fantasy of mine. "
    mi "That a sex joke?"
    s "Yeah, that was a sex joke."
    mi "Heck yeah! I understand those now. Ain’t sure how well that’s gonna work in public, though. Think there are laws against that kinda thing."
    mi "Either way! Get your butt over here ASAP! I’ll let the others know you’re comin’."
    s "Sure. It’s the park near the school, right?"
    mi "Yeah, the one where Otoha’s always playin’ guitar and stuff."
    s "Is she there right now?"
    mi "Mmm...no. Don’t see her. Just some old guy with a weird coat and- oh. {i}Oh.{/i} "
    mi "Ya know, maybe that public stuff is legal after all?"
    s "I’m on my way. Stay away from the old guy, please."
    mi "Yeah, I’m just gonna...I’m gonna jog around the track while waitin’ for the others to show up."
    mi "Bye, Sensei! See ya soon!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and pull myself out of bed. But while I’m getting dressed, my mind strays from alligators and catacombs and lands on something brighter."
    "Maybe Miku is precisely the type of girl who can share some of her light with me — in the good way. Not the Yasu way."
    "Or the Yasu way if she thinks she’s ready. But...not in public."
    "There are laws against that sort of thing."

    scene sky
    with dissolve2

    "When I make it to the park, it finally dawns on me how beautiful the weather is today."
    "I was so distracted on the way here by the idea that I might be biting off more than I can chew that I wound up forgetting how nice it is to be rid of the summer."
    "That is until a familiar scent makes me yearn for the snow."
    "But I forget that again when my heart is thawed by a surprisingly wholesome sight."

    scene mikupark1
    with dissolve2

    mi "Well, if it ain’t Captain Sorrow in the flesh!"
    i "Hi, Sensei! Long time no see! If you’re not counting the part where Uta and I broke into your house and tried to kidnap you."
    u "Hahah...yeaaah...That’s a thing that happened, alright..."
    s "I can’t say I’m fond of my new nickname, but hey. To all three of you. Sorry for turning into a hermit."
    mi "Ain’t nothin’ to apologize for, Sensei. I’d probably be go into hidin’ too if {i}my{/i} niece started sayin’ stuff that made her sound like a serial killer. "
    mi "‘Specially cause I ain’t got a niece and that would make stuff extra scary. But I get it."
    s "Ami is not a {i}serial killer.{/i} She’s just...kind of-"

    scene mikupark2
    with dissolve

    i "Yeah, yeah, yeah. Let’s not talk about weird nieces right now. Let’s shoot for something different instead! Like the best way to cook steak. Or weird pictures we might keep in our phones!"

    scene mikupark3
    with dissolve

    u "{i}Io! Shh! No!{/i}"
    mi "Weird pictures? You tryin’ to confess to somethin’ right now, Io? What’choo keepin’ in there?"
    i "Oh, you know. The same kind of stuff everybody else does. I just figured this might be a good chance to clear up any misunderstandings before our imaginations start to fester and kill us from the inside out."
    s "Yeah, I’d rather not talk about what I keep in my phone."

    scene mikupark4
    with dissolve

    i "You don’t say. "
    mi "Does everybody keep weird stuff in their phone but me? This another one of those adult things I ain’t learned about yet?"
    s "Everything okay, Uta? You look upset."
    u "I’m...uhh...confused. That’s all."
    i "Sensei, do you maybe want to talk to Uta for a minute while Miku and I...go over...uhh..."

    scene mikupark5
    with dissolve

    i "...there?"
    u "{i}Hah...{/i}"
    mi "Now wait just one second, Io. I didn’t ask Sensei if he wanted to come all the way over here just so he could have some alone time with your roomie. "
    mi "And I know that for sure ‘cause I got my {i}own{/i} roomie who {i}always{/i} wants alone time with Sensei and that’s just rude when we’ve got a whole group of people doin’...group stuff."

    scene mikupark6
    with dissolve

    u "I agree! Group stuff it is! Talking about what we have in our phones is super personal and private anyway! What we don’t know won’t hurt us! Right, Sensei?!"
    s "Uhh...right. Exactly."
    mi "Well, now that all that weird stuff is outta the way, how we gonna do this? Under the table? On top of the table? I gotta know where to put the pizza."

    scene mikupark7
    with dissolve

    i "Wait, what are we talking about now?"
    s "Another misunderstanding. Please ignore everything Miku says that sounds even remotely suggestive and just continue to be your normal, cynical self."

    scene mikupark8
    with dissolve

    i "Now {i}that{/i} is a task I can handle."
    mi "Well, if we’re gonna be law abidin’ citizens and all that, what {i}can{/i} we do? Cause Sensei ain’t the type to enjoy any kinda socially acceptable physical activities."
    i "Boy am I glad I was just told to ignore everything even remotely suggestive."
    s "Miku, why don’t you continue filling me in on everything else that’s been going on? You know, in a way that can’t possibly lead to anyone hearing anything they don’t want to hear?"

    scene mikupark9
    with dissolve

    mi "How the heck am I supposed to be keepin’ track of what other people wanna hear when I don’t even know what I wanna hear?! I ain’t some kinda event organizer! "
    mi "Heck, I didn’t even know I was supposed to bring anything to this picnic and I’m the one who kinda organized it! I clearly ain’t cut out for this!"
    i "It’s cool, Miku. Uta and I brought more than enough for all of us. Plus, we had a big breakfast earlier, so neither one of us is that hungry."
    u "I ate three bowls of cereal. I am not proud of myself. But I also didn’t know we were even having a picnic until we were on the way here, so..."
    i "She probably doesn’t remember that we’re going to the movies tonight either. Uta and I both have mid-shifts, though, so we can’t stay for super long."
    mi "She’s right. Totally forgot about that until right now."
    i "See?"
    mi "I’m what most people like to call a “lost cause.”"
    s "Why put together a picnic in the first place? That’s far too passive of an activity for someone like you who seems to exist for the sole purpose of just...running around and yelling."
    mi "I gotta eat too, Sensei. All that runnin’ and screaming requires some serious fuel and my battery ain’t gonna recharge itself."
    mi "Plus, everybody’s been lookin’ so darn sad lately that I felt like I {i}needed{/i} to do somethin’. And gettin’ you outta the house as well was a crazy bonus that even I didn’t expect."

    scene mikupark10
    with dissolve

    i "Yeah. Not gonna lie, after you gave us that speech in school, I was pretty confident you were going to go right back home and allow yourself to be chained up or something."
    u "We were all worried about that. Which is probably why we’ve all seemed so “down” lately."
    i "Uta in particular has taken your absence really harshly. I haven’t seen her this miserable since they stopped selling the umeboshi onigiri at Lawson’s — the place where I work."
    s "Halloween is over, Io. You don’t have to pretend to work at Lawson’s anymore."
    i "Once a Lawson, always a Lawson. That’s what Mr. Lawson always says. "
    s "Miku- and you two as well, I’m {i}sorry.{/i} Okay? It’s not like I {i}wanted{/i} to make any of you upset. And while I’m flattered that you’re all this down because of me, you need to snap out of it."
    s "Like, look at what’s become of Miku. She’s trying to organize events now and is clearly horrible at it. Her words, not mine. But also my words. Even {i}I{/i} know everyone is supposed to bring something to a picnic."
    i "And yet you have shown up empty-handed. Curious."
    mi "It ain’t just that, though, Sensei. I’ve been kinda messed up too. I’ve really missed you. "
    mi "You’ve been more than just a teacher for a long darn time. And havin’ you stuck in your house is kinda like havin’ a friend move away. So I’m tryin’ to bring some of the fun back into life."
    mi "You have any idea how many times I’ve wanted to call ya since you disappeared? Your name in my phone’s like, the last thing I look at every night. "
    mi "Been dreamin’ about you too, but I don’t think I can talk about those with my other friends present."

    scene mikupark11
    with dissolve

    i "Come to think of it, I’m pretty sure Uta has as well. Because I’ve definitely been hearing “{i}Sensei...Sensei!{/i}” in the middle of the night a lot lately. "
    u "Hahaha! Not me! I don’t have any dreams at all! Ever!"
    s "How are you not embarrassed saying things like that out loud, Miku? I’m not even talking to Uta right now and I can already tell she’s internally screaming."
    u "{i}(Fuck!){/i}"

    scene mikupark12
    with dissolve

    mi "What’s there to be embarrassed about? If somebody’s gonna shame me for lovin’ my friends, they ain’t somebody I wanna hang out with in the first place."
    mi "The thing I want the most right now is for you to get back to normal. So if I’ve gotta start organizin’ picnics to do that, I’m gonna."
    s "Sure. Except for the part where we’ve never had a picnic before and this isn’t really normal either."
    mi "The picnic ain’t the important part, it’s bein’ together that is. So I’ve been tryin’ to spend time with everybody lately to remind ‘em all that this is just temporary."
    mi "You’re gonna get better, Sensei. And maybe it won’t ever be “normal” again if whatever ya lost was really that important to ya. But still...we’ve gotta do {i}somethin’.{/i} "
    mi "And that somethin’ may as well be fun."

    scene black
    with dissolve2

    "I take a seat at the picnic table with all three of the girls and force myself to eat a slice of pizza despite barely having an appetite for over a month."
    "And while the conversation that picks up once the introductory phase of our rendezvous comes to an end is simpler, something still feels off."
    "It could very well be the fact that I just haven’t spent much time with any of these girls since before the incident, but that’s probably just wishful thinking."
    "It only makes sense that there are some things happening behind the scenes that I don’t know about. Miku’s living proof of that."
    "But it seems that finding out what’s going on with Uta and Io will have to wait as the two of them bid Miku and me farewell once the sun begins to set, leaving us alone once more."

    play sound "static.mp3"
    scene mikupark13 with flash
    stop sound

    "For the first time in a while."

    mi "Did you know that some people do it in the butt? Crazy, right?"
    s "And it’s like no time has passed at all..."

    scene mikupark14
    with dissolve

    mi "Huh? What do you mean?"
    s "Nothing. Just narrating my thoughts again."
    mi "You do that often?"
    s "Not really. But I’ve been talking to myself a lot more than normal lately, so I guess that’s a thing."
    mi "Weird. Makoto’s been doin’ that too. Figured it was just stress or somethin’."
    s "It might be. There’s certainly been no shortage of that since my sadness-coma."

    scene mikupark15
    with dissolve

    mi "Wanna talk about it? I’ve learned a thing or two about therapy lately. And if that kinda thing works for somebody like me-"
    s "Maybe some other time, but not because I don’t trust you. It’s because I don’t want to put an end to this...haphazardly organized soiree meant to serve as a re-introduction to a less sorrowful reality."
    mi "I’ve got no frickin’ clue what any of that just meant, but okay. Long as you’re happy."
    s "I’m not."

    scene mikupark16
    with dissolve

    mi "Then what the heck were all of those big words for?!"
    s "I’m just commending you for trying. It’s really nice of you to go to all this effort just to try and pick up the slack I’ve created by...semi-vanishing."

    scene mikupark17
    with dissolve

    mi "Oh...yeah."
    mi "It’s been hard. All of this stuff. And I ain’t just sayin’ that cause I’ve had to go back to usin’ my own fingers. "
    mi "The thing is...I really like you. Lots of us do. But since I haven’t been able to {i}get{/i} to you, I’ve just been tryin’ to pick everybody else up instead."
    mi "Makoto’s...fine, I think? Which is weird. But she also just had some crazy trauma with her dad recently that might’a helped her deal with stuff like people vanishin’ a little better, though."
    mi "Sana’s been weird, though. Io’s been worse than normal. Uta’s cryin’ a lot. Futaba seems stressed. Kirin’s kinda...I don’t know. Let’s just say she’s weird too. But Ayane’s got it the worst."
    mi "She cries in the shower after swim club so nobody will notice, but I do. I {i}always{/i} do."
    s "You...watch Ayane shower often?"

    scene mikupark18
    with dissolve

    mi "Body goals, Sensei. Body goals."
    mi "Ayane’s got the kinda figure girls like me can only dream of. Had no idea I’d stumble upon her havin’ a secret breakdown in there. But she won’t even talk to me about it since we ain’t close."
    s "Ayane doesn’t like talking about things like that with {i}anyone.{/i} She’s like me. More of a...{i}bottle it up{/i} type of person."

    scene mikupark19
    with dissolve

    mi "I get it. You know I do. But we’re {i}all{/i} gonna wind up miserable if we keep doin’ that to ourselves. Which is why I just want us all to...get back to where we were at the start of the year."
    mi "Back when..."

    scene mikupark20
    with dissolve

    mi "When..."
    mi "Wait...what? Weren’t you absent at the start of the year? How does that...nah, I’ve gotta be....."

    scene mikupark21
    with dissolve

    mi "A-Anyway! If things are ever gonna be fun again, me and {i}you{/i} are-"
    s "You and I."
    mi "You and {i}I{/i} are gonna have to cross this...bridge or somethin’ together! Which means continuin’ to explore and continuin’ to enjoy each other’s company! Both sexually and {i}not{/i} sexually! "
    s "And...which one of those things do you want most right now, Miku?"
    mi "Both! I am very conflicted and very excited to see you again!"

    scene mikupark22
    with dissolve

    mi "Which means..."
    s "Which means?"
    mi "Which means there is only {i}one{/i} place the two of us can go...to kill both birds with a rock."
    s "Not how that phrase goes, Miku."
    mi "Things have changed here on the outside while you’ve been gone, Sensei. You don’t know how we talk anymore."
    s "Miku, just tell me where we’re going."
    mi "To the {i}promised land,{/i} Sensei."

    $ renpy.end_replay()
    $ miku_love += 1
    $ mikuspring1 = True

    jump mikuspring2

label mikuspring2:
    stop music
    play sound "static.mp3"
    scene mikupornshop1 with flash
    stop sound
    play music "citylife.mp3"

    mi "To the promised land!"

    "So, apparently the promised land is the Miyamura family porn shop — a development I should have expected given recent developments in Miku as a person."
    "And while the majority of those developments probably entered her attached to my fingertips, it is my responsibility as an adult to make sure that she experiences this brave new world as responsibly as possible."

    s "They keep the hardcore stuff in the back. That’s the place you want to be."

    scene mikupornshop2
    with dissolve

    mi "Whaddya mean by “hardcore stuff?” This about that butt thing I was mentionin’ earlier? Cause I ain’t gotta see that. Just thought it was neat."
    s "I think that, when it comes to porn, it’s best to just experience things yourself so that you don’t go in jaded by expectations placed on you by others."

    if brony == True:
        s "Take me, for example. I habitually masturbate to images of cartoon ponies. And I probably never would have done that if someone told me it was wrong beforehand."
        mi "Sorry, did I hear that right? Cartoon ponies?"
        s "Yeah. You heard that correctly. "
        s "I’ve been on a bit of an Applejack kick lately. "
        mi "Like the cereal? You and Uta eatin’ breakfast together now?"
        s "No. Like the horse, Applejack — the most dependable pony this side of Ponyville. A proud farm pony who ain’t afraid to get her hooves dirty."
        mi "Now, I learned from Maki that it ain’t right to bash what other people are into, but I ain’t so sure about this one, Sensei."
        s "It’s fine. I’ll show you the light eventually. You’ll understand one day."
    else:
        mi "Oh, I get it. It’s like choosin’ a favorite sports team. It’s better to pick for yourself instead of just doin’ what ‘yer folks want ya to do, right?"
        s "I don’t know. You should be very aware by now that I’m not a sports person. But I {i}am{/i} a porn person, which means you should take everything I say very seriously while we’re here."
        mi "Roger that, Sensei. My fate is in your hands."

    scene mikupornshop3
    with dissolve

    s "Right now, our main goal is to think of an objective. Why are we here? What is it we seek within these walls today? Knowledge? Pleasure? Or perhaps...Student Council Punishment Games Volume 9?"

    scene mikupornshop4
    with dissolve

    mi "Wait, volume 9? Do I gotta watch the other ones first?"
    s "No, but you probably should. The storyline is actually extremely gripping and dramatic. And the main character looks and acts a lot like Makoto. "
    mi "So she’s like, one of them straight-laced, smartypants types with a secret freaky side?"
    s "That’s right. And she won’t stop until she’s been punished by everyone in town."
    mi "Won’t stop what?"

    scene mikupornshop5
    with dissolve

    s "You know...just...she won’t. Don’t ask questions."
    mi "How the heck am I supposed to learn about sex and porn and stuff if I can’t ask questions? Ain’t you supposed to be my tour-guide on the way to Bonerville?"
    s "I’m not allowed in Bonerville anymore. Everyone else was getting jealous."
    mi "That’s fine. You just gotta get me to the gate. I can figure out the rest. "
    s "I’m not going to drop you off at Bonerville, Miku. You’re not ready yet."

    scene mikupornshop6
    with dissolve

    mi "Damn it, Sensei! Enough with your games! I’m finally ready to start consumin’ adult media and I ain’t gonna be held back by a man who ain’t allowed in Bonerville!"
    maki "Hm? Bonerville?"

    scene mikupornshop7
    with fade

    maki "Are you two planning a vacation to my favorite place on earth without me? That’s so mean."

    scene mikupornshop8
    with dissolve

    mi "Maki! Sensei won’t-"

    scene mikupornshop9
    with dissolve

    mi "Whaaaaaaaaa..."
    maki "Big, right? "
    s "Maki, what is that?"

    scene mikupornshop10
    with dissolve

    maki "Horse cock!"

    if brony == True:
        s "I could finally please Applejack..."
        maki "You sure could! Because we all know she likes ‘em big."
        s "Maki...{i}you too?{/i} You’re one of us?"
        maki "I appreciate all porn equally! That’s my job, after all!"
    else:
        s "{i}Why?{/i}"
        maki "Because some people are into that sort of thing. I don’t know."
        s "You’re one of those people, aren’t you?"
        maki "Maybe I am. Maybe I’m not. What difference does it make? A dildo’s a dildo’s a dildo! And if somebody wants to put something inside of them, it’s my job to help."
        maki "Just not physically. That’s a different profession. And it costs extra. And I’m going to make you sign a waiver."

    mi "I’m scared."

    scene mikupornshop11
    with dissolve

    maki "That’s just because you’re not ready yet! But one day, when the time is right, and your curiosity has advanced far past normal human penises, you’ll know where to come for something different."
    maki "I have demons and ogres and stuff in stock too. Any dick you could ever imagine, I’ve pulled out of a box. That’s right, Miku. Whether it be Bad Dragon or the Official Dildo Saber, I’ve got anything you-"
    s "Maki, I understand that you’re a salesman at heart, but you might want to remember who you’re selling things {i}to.{/i}"

    scene mikupornshop12
    with dissolve

    maki "Oh, good point. You should walk away so I can teach her about all of this girl-to-girl. There’s no need for your kind here, penis-haver."
    mi "I think I’m just gonna see what Makoto’s doin’ instead..."

    scene mikupornshop13
    with dissolve

    mi "You two have fun with...your {i}horse...{/i}"
    maki "Darn it. Nobody ever wants to have the horse cock talk."
    s "Can you really blame them? And also, why are you holding it like a rifle?"

    scene mikupornshop14
    with dissolve

    maki "Better question — where the hell have you been lately?"
    s "Is that really a better question? Because I think mine is-"
    maki "I’m being serious right now, Akira. I heard from Sara that you were back, but I sure didn’t expect you to come wandering into my shop like nothing ever happened."
    maki "Are you okay? Do you need anything? Free horse cock?"
    s "There’s no way you’d give that to me for free."

    scene mikupornshop15
    with dissolve

    maki "Yeah, this baby’s like 60,000 yen. But still. "

    scene mikupornshop16
    with dissolve

    maki "If there’s anything you need-"
    s "Just time. That’s all. I’ve barely talked to anyone lately, so please don’t take it personally that I haven’t really dropped by."

    scene mikupornshop17
    with dissolve

    maki "That little factoid makes it even stranger that you’re showing up with Miku. But I guess if you two are just here looking for Makoto-"
    s "Oh, no. Miku said she was taking me to the promised land and, next thing I knew, we were here."

    scene mikupornshop18
    with dissolve

    maki "Ah! I’ve never been this proud in my life!"
    s "You know you have an actual daughter, right?"
    maki "Yes, but she simply doesn’t understand."

    scene mikupornshop19
    with dissolve

    maki "Miku, though...she’s been all sorts of {i}curious{/i} lately, hasn’t she?"
    s "Not like I’d know. This is the first time I’ve really hung out with her since Halloween."
    maki "Well, without getting into any of the graphic details, I think her {i}time{/i} has finally come. And without anybody else to show her the ropes, she and I might really have to talk soon."

    scene mikupornshop20
    with dissolve

    maki "But hey! On the bright side, it seems like whatever Makoto had going on with her mystery-boyfriend has either fizzled out or she’s just gotten really good at hiding it! So either way, yay!"
    s "Yeah...that’s great news."

    scene mikupornshop21
    with dissolve

    mi "We have to leave."
    maki "Everything okay, dear?"
    mi "I’ve seen things I can never unsee."
    maki "..."
    s "..."

    scene mikupornshop22
    with dissolve

    maki "Oh...She wasn’t studying in there, was she?"
    mi "I don’t wanna talk about it."
    s "But what about the promised land? Don’t you want Maki to help you start exploring the world of-"
    mi "Nope."

    scene mikupornshop23
    with dissolve

    mi "I don’t want anything ever again."
    maki "{i}Hah.{/i} I told her to stop doing that in there. But {i}girls will be girls,{/i} I guess."
    s "Yeah...Anyway, I’m going to follow Miku. But it was nice seeing you again, Maki. I’ll...be around."

    scene mikupornshop24
    with dissolve

    maki "You know where to find me."
    maki "Hang in there, Akira."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikupornshop25
    with dissolve2

    mi "Welp, I’m sure glad that’s over."
    s "Part of me wants to ask exactly what you saw, but the other part of me thinks it might be better if I just never find out."
    mi "Yeah, I’m gonna say you’re better off without this forbidden knowledge, Sensei."
    s "Well...now what, then? Are we just going home? "

    scene mikupornshop26
    with dissolve

    mi "Idunno. I kinda wanna keep hangin’ out if you’re okay with it. Don’t get many chances to see ya anymore since you stopped comin’ to school and the dorms."
    s "I’ll be back eventually. I just need to stop wanting to die first. "

    scene mikupornshop27
    with dissolve

    mi "Please don’t die. I ain’t ready for even more tragedy yet. And, ya know what? I probably never will be. So just stay alive for the rest of forever, okay?"
    s "I’ll...see what I can do, Miku."

    scene mikupornshop28
    with dissolve

    mi "Thanks, I...guess..."
    s "..."
    mi "..."
    s "Uhh..."

    scene mikupornshop29
    with dissolve

    s "Is everything-"

    scene mikupornshop30
    with hpunch

    mi "Mm!"
    s "Oh. You wanted to hold hands."
    mi "It’s dark..."
    mi "And nobody else is around, so you ain’t gotta worry about us bein’ seen or anything..."
    s "..."
    mi "And maybe I just kinda...you know...wanted to..."

    scene mikupornshop31
    with dissolve

    s "It’s fine. I don’t mind. In fact, I find it really cute when you act like this."
    mi "Shut up. I know you’re only sayin’ that to mess with me. I ain’t cute at all. "
    s "I’m not, though. "
    s "You don’t need to wear dresses and stuff to be {i}cute,{/i} Miku. You’ve always been cute. And whenever you let your guard down around me, it really shows."

    scene mikupornshop32
    with dissolve

    mi "It’s only {i}because{/i} it’s you that I can-"
    q "Miku? Is that you over there?"

    scene mikupornshop33
    with hpunch

    mi "Ah! What?! Maybe?! Yes!"

    scene mikupornshop34
    with fade

    ka "Oh! Sensei, you’re here too. "
    ka "It’s really funny. In the dark, it kind of looked like you two were holding hands."

    scene mikupornshop35
    with dissolve

    mi "Hahahah! That Karin! Always such a friggin’ kidder! Me and Sensei holdin’ hands! Hahaha! What is this?! Some kinda rom-com?! Hahahah!"
    ka "Miku, are you okay? Your face is beet-red."

    scene mikupornshop36
    with dissolve

    mi "Oh! Hahah! Yeah!"
    mi "That’s just from all the porn."

    scene mikupornshop37
    with dissolve

    ka "The...p..."
    mi "Running! I don’t know why I said that other thing! We were running! Right, Sensei?"
    s "Yes, but only because it’s Karin and she’s the last bit of purity I have in this world now that Sana’s been taken from me."

    scene mikupornshop38
    with dissolve

    mi "Huh? What happened with Sana?"
    ka "Yeah, what happened with Sana?"
    ka "Wait, who is Sana again?"
    mi "Short girl. Black hair. Used to have one eye, now she has two."

    scene mikupornshop39
    with dissolve

    ka "Aww. I love stories of people overcoming obstacles. Good for her."
    s "Nothing happened with Sana. I’m just talking out of my ass again."
    mi "Better than doin’ that other thing with it at least. "

    scene mikupornshop40
    with dissolve

    mi "What’re {i}you{/i} doin’ out here this late, though? Ain’t you normally home around this time?"
    ka "I was out with some of my friends from the softball club and decided to take the long way home today. And I’m glad I did since I got to run into you guys."
    ka "How come you’re walking around in the dark, though? Isn’t that a little dangerous?"
    mi "Shouldn’t we be the ones sayin’ that to you? ‘Least I’ve got an escort. You’re out here by yourself. And with bazongas like that, you’re way more of a target than I’d ever be."
    ka "What’s a “bazonga?”"
    s "It’s slang for your kind and gentle demeanor."
    mi "Yeah. And your boobs are huge too."

    scene mikupornshop41
    with dissolve

    ka "M-Miku?! You can’t say things like that in front of a teacher! You’re going to get in trouble!"
    mi "There are a lotta things I shouldn’t be doin’, Karin. But ya girl’s headin’ down a long and lonely road full of sausage and sweat and she ain’t got no more time for censorship."

    scene mikupornshop42
    with dissolve

    ka "Nonsense. There is always time for censorship as we are far too young to be exposed to material that could begin to shape the world in a negative-"
    mi "Blah, blah, blah. Sensei, what are your thoughts on censorship?"

    play sound "static.mp3"
    scene mikupornshop43 with flash
    stop sound

    a "{i}I am your accountant after all. And some would say that's like having no hair whatsoever.{/i}"

    play sound "static.mp3"
    scene mikupornshop44 with flash
    stop sound

    ay "{i}I don't actually like the third season of Seinfeld.{/i}"

    play sound "static.mp3"
    scene mikupornshop45 with flash
    stop sound

    ya "{i}(Airplane noises){/i}"

    play sound "static.mp3"
    scene mikupornshop42 with flash
    stop sound

    s "Pass."
    mi "{i}Pass?{/i}"
    ka "Sensei just knows that censorship makes everything better and that the world would be a happier, sunnier place if we would all just watch daytime television."

    scene mikupornshop46
    with dissolve

    mi "Okay, forget the censorship thing since it’s clear all three of us ain’t gonna get on the same wavelength for it. But that don’t mean we can’t still find a way to have fun."
    ka "Miku, it’s almost 9:00. How am I supposed to have fun after 9:00? That’s pajama-time. If I don’t get the recommended eight hours of sleep, how am I supposed to function tomorrow?"
    mi "Idunno. Sleep later?"

    scene mikupornshop47
    with dissolve

    ka "How {i}dare{/i} you..."
    ka "I taught you better than this."
    mi "Sensei, you on board for some pajama-time fun-time? "
    s "Probably not the kind Karin would be interested in."

    scene mikupornshop48
    with dissolve

    mi "Well, {i}I’ve{/i} got the perfect idea. And it’s one I’m sure nobody sees comin’."
    s "I’m not taking Karin to the promised land. "
    ka "And I’m still not convinced it’s okay to walk away from pajama-time."
    mi "The three of us...are doin’ karaoke!"

    play sound "static.mp3"
    scene mayakaraoke29 with flash
    scene karaoketime12 with flash
    scene theendoftheworld32 with flash
    scene theendoftheworld46 with flash
    scene mikupornshop49 with flash
    stop sound

    s "Uhh-"
    ka "Oh, I love karaoke! But I thought the noises would-"

    play sound "static.mp3"
    scene mayakaraoke29 with flash
    scene karaoketime12 with flash
    scene theendoftheworld32 with flash
    scene theendoftheworld46 with flash
    scene mikupornshop49 with flash
    stop sound

    mi "Don’t worry! I’ve been practicin’ with stuff like that and I think I’ll be okay! Maybe! I don’t know! It’s kind of a test!"
    s "Guys-"
    ka "If it’s just for a little while, I don’t mind. I didn’t bring any money with me, though."

    play sound "static.mp3"
    scene mayakaraoke29 with flash
    scene karaoketime12 with flash
    scene theendoftheworld32 with flash
    scene theendoftheworld46 with flash
    scene mikupornshop49 with flash
    stop sound

    mi "That’s fine! Sensei’s an adult! He can pay!"
    s "I don’t really want to-"

    stop music
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop50
    $ renpy.pause(0.2, hard=True)
    scene mikupornshop51
    $ renpy.pause(0.2, hard=True)
    scene black
    $ renpy.pause(2, hard=True)

    $ renpy.end_replay()
    $ mikuspring2 = True
    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump karinspring2

label mikuspring3:
    scene mikugymtalk1
    with dissolve2
    play music "10c.mp3"

    mi "Alright, ladies! Listen up!"
    mi "I know y’all look at me like some kinda loser that knowns nothin’ ‘bout anythin’, but I’m here today to tell ya that I {i}do{/i} know somethin’! And that somethin’ is sports!"
    mak "Apologies for interrupting, but I don’t think any of us need reminding that your expertise lies in-"

    scene mikugymtalk2
    with dissolve

    mi "Personal foul — roughing the speaker! Number six! Fifteen-yard penalty! First down, Miku!"
    mak "...What?"
    mi "It means shut the heck up while I’m tryin’ to give my motivational speech! I don’t care if ‘yer my roommate or not! I got trainin’ to do!"
    ay "Just let her continue, Makoto. We all showed up because we trust Miku to lead us to victory in this year's sports-day-slash-dorm-wars contest."

    scene mikugymtalk3
    with dissolve

    mak "The full title is actually: Super Mega Ultimate Sports-Day Dorm Wars: No Boys Allowed ~ The Extremely Awesome and Only Kind of Sad Special Event for Bonding and Battling."
    f "Was the “No Boys Allowed” part really necessary to add? Because I really don’t think Sensei was planning on showing up this year even {i}if{/i} he were invited."
    sa "I think that’s...why we added the “kind of sad” part...but I agree that...we should make the title a little shorter..."

    scene mikugymtalk4
    with dissolve

    mi "The title ain’t important right now! All that matters is preparin’ for the SMUS-DDW:NBA ~ TEAaOKoSSEfBaB so we ain’t blindsided by any plannin’ those second floor gals are doin’!"
    f "Is it just me or does the acronym make it even harder to remember?"
    ay "It’s just you. I can remember SMUS-DDW:NBA ~ TEAaOKoSSEfBaB just fine."
    mi "Thank you, Ayane! But again, the name ain’t important right now! "

    scene mikugymtalk5
    with fade

    mi "The unfortunate truth is we’ve always had an advantage when it comes to these Dorm Wars thingies since ours is the floor that loves Sensei the most!"
    mi "Now that he’s stripped outta the competition entirely, we’ve gotta figure out a way to compensate! And that ain’t gonna be easy when they’ve got girls like Touka and Noriko up there!"
    mak "Are either of those two athletic? Because I’ve never seen either one of them do anything to prove that at any point."

    scene mikugymtalk6
    with dissolve

    mi "Touka’s always talkin’ about how she wants to show us her skills when it comes to that stuff. And if there’s anythin’ I know about vegans like Noriko, it’s that they’ve got super powers and can fly and stuff."
    ay "Noriko’s a vegetarian, actually. She’s not vegan."

    scene mikugymtalk7
    with dissolve

    mi "Damn. So she probably just has super-speed instead."
    f "If anything, I think Tsuneyo is the one we’re going to have to worry about. She’s kind of...comically strong."
    sa "Doesn’t...Kirin have experience with sports too?..."
    ay "I wouldn’t be surprised if dorm seven was above-average in that field as well. Uta’s great when it comes to archery and I’m pretty sure Io is into baseball."

    scene mikugymtalk8
    with dissolve

    mi "And all that’s exactly why we’ve gotta practice!"
    mi "We’ve still got no clue what sortsa contests we’ll be havin’ and what kinda games we’ll be playin’, so we’ve gotta prepare for anythin’ and everythin’ so we can have strategies in place and not look bad!"
    mak "I’m surprised to see your competitive spirit this ignited, Miku. Normally, that’s my thing. And we don’t even know this year’s prize yet, so there’s no way {i}that’s{/i} what lit this fire. "
    mi "It ain’t the prize that matters, Makoto. It’s the glory of the braggin’ rights. And I ain’t just sayin’ that since only like one instance of the Dorm Wars has actually had a real prize."
    ay "Shh...I thought we agreed that we were going to stop bringing that up?"

    scene mikugymtalk9
    with fade

    mi "We are! So instead of focusin’ on the past, let’s start figurin’ out where to go in the future!"
    mi "Futaba! Tell me some of ‘yer strengths! "
    f "Me?"
    mi "Yes, you! There’s gotta be somethin’ you’re good at when it comes to sports!"
    f "Can I pass? I’ve never really been an {i}athletic{/i} person."
    mi "Part’a bein’ an athlete is mental too! Just think’a baseball! That game’s like 90%% mental and 5%% physical, with the other 10%% bein’ luck!"

    scene mikugymtalk10
    with dissolve

    sa "Five...ten..."
    f "Then...I guess...I’m okay when it comes to problem-solving? Maybe? So long as the problem...isn’t about me...I think..."
    f "Like, I don’t want to say I’m {i}creative,{/i} but-"
    mi "Yeah, yeah, yeah! Good enough! "

    scene mikugymtalk11
    with dissolve

    mi "If you’re good at problem solving, you might make a good coach! And you like reading, don’t ya?! Which means ya could get familiar with the rules of stuff super quick! Maybe!"
    mi "So, since we ain’t got any idea what we’ll be playin’ yet, why don’t ya head on over to the library after our meeting today and take out a book on every sport ever?! That’ll be sure to give us an advantage."
    f "E...Every sport?...."
    mak "I don’t think Miku understands how quickly the average person reads, Futaba. I’ll help you look for relevant materials once we’re done here."
    mi "Sana! You next! What are you good at?"
    sa "I..."
    mi "No need to answer! I already know you’re gonna say video games! Which means your hand-eye coordination is probably better than a lot of the other girls!"

    scene mikugymtalk12
    with dissolve

    sa "I...I mean...um...maybe? But I...get tired really easily and..."
    mi "Drink a Monster! Maybe two! Do whatever ya gotta do to amp those energy levels up, cause you’ll be our secret weapon once sports day rolls around! Got it?!"

    scene mikugymtalk13
    with dissolve

    sa "N-No?!?! Why do I have to be the secret weapon?! I couldn’t even answer my own question!"
    f "Maybe we’ll get lucky and there will be some sort of...video-game based competition? "
    mi "For {i}sports day?!{/i} I doubt it, coach! We’ve gotta prepare for a full day’s worth of sweatin’ and...well, sports! And anythin’ else that starts with an S! Spaghetti maybe?"

    play sound "thump.mp3"
    scene mikugymtalk14
    with hpunch

    ay "What about me, Miku? I’m good at all sorts of stuff. "
    mi "Which means you’ll be our ringer! Same as me. And if we’re able to compete in more than one thing, me and you’ll be the ones to make the second floor’s life a living hell. Understood?!"
    ay "Got it! But also, please reconsider making Sana the secret weapon. I really don’t think she’s built for things like this."

    scene mikugymtalk15
    with fade

    mi "I ain’t reconsiderin’ nothin’, Ayane! This ain’t ‘yer grandma’s sports-day! This is the contest to end all contests! And by George, we’re gonna win this one for the boys back home!"
    mak "As much as I agree, I thought your whole thing was that sports are great for reasons {i}outside{/i} of the winning part?"
    mi "That was before the boys came back home, Makoto! Now, we’ve gotta win this for them!"
    mak "What boys? All the boys are still in space. Apart from my dad, at least. "

    scene mikugymtalk16
    with dissolve

    mi "You know...the boys! The ones back home!"
    mak "..."
    mi "The boys on the docks! The boys are back in town! You know! {i}The boys!{/i}"
    mak "..."

    scene mikugymtalk15
    with dissolve

    mi "Forget Makoto! The point is, we’ve all got a role to play! "
    mi "Tom Brady says that the {i}true{/i} competitors are the ones who always play to win. And the last thing we need is those people livin’ above us thinkin’ they’re higher up the ladder than we are!"
    f "That’s- oh, it’s not even worth it."
    mi "You’ve got that right, boobzilla! Now, everybody stand up tall and pay attention while I give ya the rundown of every single sport we might be playin’ for sports-day! You too, Sana!"
    sa "Huh?...What?...Where am I?..."
    mi "The first sport we’re gonna talk about is curling. Ya see, it all starts with a broom-"

    scene mikugymtalk17
    with dissolve

    mak "Okay. Hit the showers, everybody. And thank you for being the ones who actually showed up. Futaba, you can have a head start so Miku can’t prey upon you again."
    mi "Hey! That’s a deleted scene now, damn it! And don’t go puttin’ an end to my meeting without askin’ me first!"

    scene mikugymtalk18
    with dissolve

    mak "Then, would {i}you{/i} like to do the honors? Because class is already done for the day and you told everyone this would only take ten minutes."
    mi "Ten minutes...ten hours...what’s the difference? "
    mak "That would be 590 minutes."
    mi "You think you’re so damn smart, don’t ya?"
    mak "Do you want the honors or not? Because we can’t keep them here all day."
    mi "As a matter of fact, I {i}would.{/i} Thank you."

    scene mikugymtalk19
    with dissolve

    mi "Let this be a lesson to all of ya! If ‘yer gonna give a speech, make sure ya don’t bring Makoto along to listen to it!"
    mi "Meeting adjourned! But don’t forget we’ve got another-"

    scene mikugymtalk20
    with dissolve

    mi "Heh?"
    mi "The heck you tryin’ to hold my hand for? We both like boys."
    mak "Miku, you have phonophobia. Do you really think I’m going to let you blow a whistle and send yourself into shock?"

    scene mikugymtalk21
    with dissolve

    mi "Oh, right. Good call."

    scene black
    with dissolve2

    mi "Anyway! Hit the showers, girls! Me and Makoto’ll be there once we clean up our balls!"
    mak "She means our sports balls. "
    ay "We’ll support you no matter what kind of balls you have, Makoto. "
    mak "Why do I feel like I’ve had this conversation before?"

    "........."
    "......"
    "..."

    play sound "shower.mp3" fadein 5.0
    scene mikugymtalk22
    with dissolve2

    mak "So...you’re really into the Dorm Wars this year, aren’t you?"
    mi "Huh? Course I am. We’re combinin’ two of my favorite things — sports and war. Just kinda sucks that Sensei won’t be involved this time."

    scene mikugymtalk23
    with dissolve

    mak "I’m sure he’ll be back next year. Or the year after. There’s only so much time he can spend moping around now that life is a constantly repeating-"
    mi "Wonder what he’s up to right now? Haven’t seen him since karaoke the other night."

    scene mikugymtalk24
    with dissolve

    mak "Karaoke?"
    mi "Yeah. Remember when I-"

    scene mikugymtalk25
    with dissolve

    mi "Oh god, I just remembered what happened right before that."
    mak "Shhh...no you don’t. That was all in your head, Miku. You never saw anything at all. And if you did, it definitely wasn’t me you saw doing it. Now, what’s this about karaoke?"

    scene mikugymtalk26
    with dissolve

    mi "Oh, sorry. Me and Sensei bumped into Karin when we were walkin’ around and the three of us wound up goin’ to that karaoke place near the school."
    mak "Since when are you into karaoke? You haven’t expressed any interest in that for as long as I’ve known you."
    mi "Iduno, figured I’d try somethin’ new for once. Didn’t amount to much though since I forgot I already made plans with Io and Uta and had to bail before even tryin’ to sing a song."

    scene mikugymtalk27
    with dissolve

    mak "Huh..."
    mi "Somethin’ felt kinda off, though. Sensei started bein’ weird as soon as I brought up the idea. Didn’t realize he was that self-conscious."
    mak "I...see..."
    mi "Guess I don’t know as much about him as you, though. For all I know, you two have been knockin’ boots in that same place for the past-"

    scene mikugymtalk28
    with dissolve

    mi "Wait! That’s it, ain’t it! He felt weird ‘cause I was bringin’ him to-"
    mak "Shh. Keep your voice down."

    scene mikugymtalk29
    with dissolve

    mi "He felt weird ‘cause I was bringin’ him to your secret sex lounge and he ain’t done that with me and Karin yet."
    mak "Uhh...no. I don’t think that’s it. I’ve only been there with him on one occasion and I can promise you it was definitely not sexual. Just weird."
    mi "Picturin’ you two singin’ together is definitely weird, so yeah. I can see that."

    scene mikugymtalk30
    with dissolve

    mak "No, I just mean there might be {i}other{/i} reasons why he’s...uncomfortable there. It just doesn’t make much sense to me yet, so I’m not sure if I can explain it well enough for you to understand."
    mak "But regardless, I’m sure he’ll get over his hump sure enough."

    scene mikugymtalk31
    with dissolve

    mi "Well, that’s good. ‘Cause I know we’ve got some humpin’ we wanna do as well."
    mak "I really don’t like this openly sexual side of you. You’re starting to remind me of my mom."
    mi "Ain’t nothin’ wrong with that. Maki’s great. And thanks to her, I aint back-alley medicated no more. Plus, I’m learnin’ to actually talk about stuff, too. And you’ve wanted me to do that forever."
    mak "How’s that going, by the way? We haven’t really talked about it lately."
    mi "Fine, I guess. Haven’t really gotten to the tough parts yet. But you said it took a little while for you to get there too, didn’t it?"

    scene mikugymtalk32
    with dissolve

    mak "It did, yeah...but I’m also a lot more open as a person than you’ve ever been."
    mi "Are ya? Cause apart from this one thing, I sure don’t think so. You’ve been keepin’ your sadness a secret for as long as I’ve known ya."

    scene mikugymtalk33
    with dissolve

    mi "I’m glad, though. Cause lately, you’ve felt a lot...different. Happier, maybe?"
    mak "..."
    mi "I don’t really know. Maybe I’m wrong and ya ain’t happy at all. But, at the very least, I’m glad we’re both gettin’ help now. If we waited any longer, we might’a ended up like Sensei."
    mi "And I don’t know about you, Makoto, but I ain’t all that interested in a world where Ami needs to wipe drool off of my chin."

    scene mikugymtalk34
    with dissolve

    mak "I see..."
    mi "..."
    mak "I am."
    mak "Happier now, I mean."
    mak "Or...at least, more {i}free.{/i}"
    mak "It’s kind of crazy, actually. Like all of the weight I’ve been carrying my whole life has somehow just {i}vanished.{/i} And I can be me {i}now{/i} without worrying about how I’ll be in the {i}future.{/i}"
    mi "Ain’t that kinda dangerous, though? You’ve always been worried about the future. ‘Bout where you’ll “end up” and stuff like that."
    mak "And, now that I’m not, I can finally breathe."
    mi "I get it, I think. Just don’t want ya losin’ sight of all that and endin’ up in a place you never wanted."

    scene mikugymtalk35
    with dissolve

    mi "Your situation’s different than somethin’ like that happenin’ to somebody like me who’s never really {i}had{/i} a place they’ve wanted to go. You’ve got more to lose."
    mak "..."
    mi "But hey, if ‘yer happy...’yer happy. And I ain’t gonna tell ya how to live your life. Just wanted to know everythin’s okay."
    mak "Yeah...thanks."
    mi "..."
    mi "Can I...ask you something, Makoto? "
    mak "Of course. Unless it’s about what you saw at the porn shop."
    mi "It’s just..."
    mi "Are you really okay with Sensei not bein’ back yet? It really ain’t botherin’ you?"
    mak "Of course it bothers me, Miku."

    scene black
    with dissolve2
    stop music fadeout 10.0
    stop sound fadeout 10.0

    mak "There’s just...no rush anymore."
    mi "Better be careful, then. Not rushin’ means that somebody else might beat you to the punch."
    mak "..."
    mi "If that person’s me, we’ll stay friends...won’t we?"
    mak "Of course."
    mi "That’s good..."
    mi "Cause I’ve been learnin’ more about threesomes lately and, I’ve gotta say-"
    mak "Okay, I’d like to shower in silence for the rest of the afternoon. Thanks. "

    "{i}One more day without you passes by.{/i}"
    "{i}The cogs continue to move.{/i}"

    $ renpy.end_replay()
    $ mikuspring3 = True

    jump nightch4

label mikuspring4:
    scene sky
    with dissolve2
    play sound "phonebeep.wav"
    play music "fallishere.mp3"

    "I tap on Miku’s name in my phone and wait for her to answer."
    "And, guess what? I’m going to do something kind today."
    "Now, you may be asking {i}why{/i} I’m going to do something kind. And to that, I say-"
    "I have no idea."
    "I just know that Miku’s never really done anything {i}wrong,{/i} so she deserves to be rewarded for being an entirely neutral force in my life who also lets me touch her inappropriately at times."

    play sound "phonebeep.wav"

    mi "Hiya, Sensei! Good morning! "

    "But just {i}how{/i} will I reward her, you ask?"

    mi "What’s up? Want to come over and put your wiener in my mouth?"

    "With some good old-fashioned {i}physical activity.{/i}"

    s "I was actually wondering if you wanted to go for a jog or something."

    "Just not the kind you were expecting."
    "I’m just full of surprises, aren’t I?"

    mi "Hm? What was that? Any chance ya can speak up, Sensei? Think I might be hearin’ things again."
    s "I said I was wondering if you- wait, what do you mean “again?”"
    mi "Oh, you know. Just that never-ending screaming people get in their heads. Sounds kinda like a demon crossed with some kinda tiger or somethin’."
    s "...What?"
    mi "Yeah, you know how it is."
    s "I...don’t. But again, I was wondering if you wanted to go for a jog. Maybe we could meet up in the park?"
    mi "..."
    s "Miku?"
    mi "Who the heck are you and what have ya done with Sensei?! Cause I ain’t got any money for his ransom, but there are these two rich girls I know who’ll flat out buy the dude if ya let ‘em!"
    s "Are you really that shocked by this? We used to run together all the time, didn’t we?"
    mi "“All the time” is a little generous, don’t ya think? We only did that a couple times and it seemed like you hated every friggin’ minute of it."
    s "Not {i}every{/i} minute. Just the ones when we were running."
    mi "Exactly! So why bother doin’ somethin’ if it’s just gonna make ya-"
    s "To make you happy."
    mi "Ah...huh?"
    s "It’s fine to do things for you every once in a while. And it’s not like jogging will {i}hurt{/i} me. At least...not long term. "
    s "Plus, I could probably use the workout since I’m still recovering from those two months in bed."
    mi "Ya mean that sleepover bangathon you had with my roommate the other day wasn’t enough of a workout for you?"
    s "It’s good to see you two are still sharing every detail about your sex lives with each other."
    mi "Makoto just likes braggin’. Any time I try to say anythin’, she just gets mad at me."
    mi "But Sensei...you really sure about this? Cause I’m fine just...comin’ over to your place and stuff. We ain’t gotta make it about me."
    s "Then just think of it as you helping me get back into shape."
    mi "There are other-"
    s "Non-sexually."
    mi "You bored of my little boy physique now? I ain’t enough woman for ya? That what’s goin’ on here?"
    s "Miku, are we doing this or not?"
    mi "HECK YEAH WE’RE DOIN’ IT, ARE YOU KIDDING?! I ain’t been this excited to hang out since I learned what an orgasm feels like!"
    mi "I’m just...a little surprised. That’s all."
    mi "But...I’ll get dressed right now! Meet me at the park in five minutes!"
    s "That’s...way too soon."
    mi "Then ten minutes! Bye, Sensei!"

    play sound "phonebeep.wav"

    "Miku hangs up the phone and I need to quickly throw on whatever clothes I can find that are suitable for running."

    play sound "static.mp3"
    scene mikuparkjog1 with flash
    stop sound

    "But, as it turns out, I don’t have {i}any{/i} clothes that are suitable for running so I just wind up sticking with my normal outfit."
    "Maybe I should go shopping soon?"

    mi "Hey! I got here early and couldn’t sit still, so I’ve already done a few laps around the place. That’s okay, right? I can still keep going! Don’t worry! Or {i}do{/i} if it means you care about me! Anyway, hi!"

    "It’s been significantly longer than ten minutes, but placing such an unrealistic expectation on me when she lives closer to this place than I do makes my tardiness {i}her{/i} fault, not mine."

    s "Hey. Sorry for keeping you waiting, Miku."

    "I apologize regardless of none of this being my fault because I have grown as a person and can do that now. "
    "This growth will also be demonstrated several minutes from now when she makes me look like an old man by running circles around me as people look on in secondhand embarrassment."
    "..."
    "Actually, on second thought, maybe we should just go exercise in my {i}usual{/i} way?"

    scene mikuparkjog2
    with dissolve

    mi "The heck are you apologizin’ for? I just told ya I got here early, didn’t I? "
    mi "I was just...excited. That’s all. This is...really cool of you, Sensei. Nobody ever wants to go running with me anymore. Like, even Karin’s been weird about it lately."
    s "Yeah, well...I’m sure she has her reasons."

    scene mikuparkjog3
    with dissolve

    mi "So, like...um...do you just want to get started? Or...maybe take a break first since you just walked all the way {i}here.{/i}"
    s "You gonna put me to shame this time or are you willing to once again try and match my pace?"

    scene mikuparkjog4
    with dissolve

    mi "You ain’t gotta worry about me takin’ off on ya, Sensei! I ain’t gonna mess up this once in a lifetime opportunity! "
    s "Is it really “once in a lifetime” if it’s already happened multiple times?"
    mi "That was with the old Sensei who was still trying to figure out how to get into my pants! New Sensei doesn’t have to try anymore, so things like this might never happen again for all I know!"
    s "That...is both annoyingly perceptive and depressingly accurate."

    scene mikuparkjog5
    with dissolve

    mi "You ain’t the only one who’s gone from one side’a the room to the other, Sensei. I, too, have seen the light. And I now understand just how silly I was to keep my pants on in the first place. Puberty, am I right?"
    s "Sadly, yes."

    scene mikuparkjog4
    with dissolve

    mi "Great! So let’s get this show on the road, then!"

    scene sky
    with dissolve2

    mi "On your mark!"
    mi "Get set-"
    s "Go!"
    mi "Ah- Sensei?! You seriously tryin’ to get a head start on me?!"

    play sound "static.mp3"
    scene mikuparkjog6 with flash
    stop sound

    mi "The heck you think you’re doin’? Ain’t we supposed to be keepin’ up with each other? Or is this just how ya tell me you’ve been secretly trainin’ this whole time and are now ready to defeat me?!"
    s "Just for a second, I wanted everyone else around to think I’m faster than you. It’s something I’ve never experienced before."
    mi "What kinda grown man has “being faster than a teenage girl” on his friggin’ bucket list?"
    s "The kind who’s knocked off pretty much everything else already except “learn how to smile.”"

    scene mikuparkjog7
    with dissolve

    mi "Ya’d think with all those billboards around tellin’ us to remember to do that, you’d have figured it out by now."
    s "Why do you think those are there in the first place? They’re very...1984, aren’t they?"
    mi "Damn, they’ve been there for that long?"
    s "...Yup. That’s what I meant."
    mi "Ain’t you only 30, though? How the heck do you remember stuff from...uhh...{i}more than 30{/i} years ago...I think."
    s "It’s a book, Miku. I’m talking about a book."

    scene mikuparkjog8
    with dissolve

    mi "Then I am no longer interested!"
    s "Also, I’m 31."
    mi "That ain’t no excuse for a lack’a speed, grandpa! Amp it up, would ya?! We’re gonna do a hundred laps today!"

    "I am never being kind again."

    scene sky
    with dissolve2

    "As much as I’d like to brag about how I lasted the full one hundred laps, I began to struggle after just five. "
    "Well, technically, I began to struggle after just one. But I didn’t reveal that I was actually struggling to Miku until the sixth lap since I wanted her to think I was cool."
    "So while my kindness lived fast and died young, it was not wasted. It adopted the same unspoken motto Miku has to make every second worth it because you never know when those seconds will run out."
    "I do hope this isn’t me somehow foreshadowing that she’s going to actually die young, though. If Makoto loses anyone else, I think she’ll probably just lock herself in her room for the rest of her life."
    "But hey, if the afterlife is real, maybe Miku would get to see her parents again. I just hope they’re all in one piece."

    play sound "static.mp3"
    scene mikuparkjog9 with flash
    stop sound

    "Anyway, here’s me being rewarded with a lap pillow just seconds after monologuing about my pillow’s dead parents. "
    "The bounties of this fast-paced life never seem to end."

    mi "You did great today, Sensei. And I can’t even be mad that you’ve got the stamina of an old dog cause you’ve got the heart of one too."
    mi "It means a lot that you were willin’ to do this for me, ya know. It felt great too. In a different way than all those times you get sexy with me."

    scene mikuparkjog10
    with dissolve

    mi "Kinda funny, though. Been so excited by how that stuff feels lately that I almost forgot what things were like {i}before{/i} I started learnin’ all that."
    mi "Things are a little crazy now, ain’t they? What with you bein’ pulled every which way by every single girl ya know. But that’s just...that’s why it makes today even more special."

    scene mikuparkjog11
    with dissolve

    mi "You could’a been with any one of them...doin’ anything you want...and yet you chose to do somethin’ you hate with me."
    mi "Is this what havin’ a boyfriend’s like?"

    scene mikuparkjog12
    with dissolve

    mi "W-Which isn’t me sayin’ I think you’re my boyfriend! I get we’re just really {i}good{/i} friends or...whatever we are! It just kinda {i}feels{/i} like-"

    scene mikuparkjog13
    with dissolve

    mi "Wait, are you even awake?"
    s "..."
    mi "..."

    scene mikuparkjog14
    with dissolve

    mi "I like you {i}so{/i} much, Sensei."
    s "I’m awake, Miku."

    scene mikuparkjog15
    with hpunch

    mi "Gyah!"
    s "Gyah."
    mi "The heck were you stayin’ so quiet for?! How long were you gonna let me ramble on about all that embarrassin’ stuff?!"
    s "Why be embarrassed at all? I like you too."

    scene mikuparkjog16
    with dissolve

    mi "Yeah, but...not in the girlfriend way, right? Ain’t we just, like...friends with benefits or whatever it’s called? That’s what the Internet said."
    mi "But the Internet also told me the earth is flat and I’m pretty sure that ain’t true since globes are all circular and stuff. Why would all those astronauts just lie to us by makin’ fake globes like that?"
    s "Miku, you’re okay with me seeing multiple people, aren’t you?"

    scene mikuparkjog17
    with dissolve

    mi "Huh? Yeah. That doesn’t really bother me."
    s "So then, just out of curiosity, what would be the difference to you if I actually {i}was{/i} your boyfriend? Because for most people, that’s sort of an exclusivity deal."
    mi "Exclusivity?"
    s "Most real couples are just that — couples. But if that’s not how it is for you, I’m not really sure what the difference would be between what we are now and how we would be as an {i}official{/i} pair."

    scene mikuparkjog18
    with dissolve

    mi "Hm..."
    mi "I wanna say it’d be the part where I can talk to other people about it. But Makoto says sometimes that stuff stays secret even {i}when{/i} people are together, so..."
    mi "I don’t...really know?"

    scene mikuparkjog19
    with dissolve

    mi "Maybe it’s like a...promise or somethin’? A way to know ya ain’t just gonna get bored of me and go chase somebody with huge bazongas one day."
    s "That’s not the case either, though. Real relationships also end without warning sometimes. That’s kind of just how it works."
    mi "I ain’t really got an answer for ya, Sensei. Ain’t somethin’ I ever thought much about until recently."

    scene mikuparkjog20
    with dissolve

    mi "There’s just somethin’ that sounds really nice about makin’ somethin’ like what we’ve got {i}official,{/i} ya know? I’d feel a lot more...important."

    scene mikuparkjog21
    with dissolve

    s "I wish everyone looked at it that way. Because I’ve been letting Chika call me her boyfriend for years now and, due to recent events, I’m now worried she’s going to start killing all of you."
    mi "Jesus, Sensei. First Ami, now Chika? I like ya a lot, don’t get me wrong, but they must {i}really{/i} like you if they’re thinkin’ about goin’ that far."
    s "I’m actually {i}more{/i} worried about Chika than Ami if you want my honest opinion. Because I think my outlook is more like yours and, when I tried explaining that to her the other day, she...kind of snapped?"
    mi "Whaddya mean “snapped?”"
    s "Talking to herself. Staring off into space. Saying she understands things that she definitely does not."
    mi "Pretty sure that’s {i}Yasu{/i} you’re talkin’ about, Sensei. She’s the one with white hair. You really been away from school for so long that ya can’t even remember who’s who anymore?"
    s "This was different from the way Yasu does those things, Miku."

    scene mikuparkjog17
    with dissolve

    s "All I’m saying is that I wish more girls were like you. For entirely selfish purposes, of course. Not because I think the world would be better that way as I would certainly {i}not{/i} be willing to share you."
    mi "So if I wanted to hook up with some other guy, that’d be a total no-go?"
    s "Right."
    mi "How come?"
    s "..."
    mi "Come on, Sensei. You asked me to tell ya what I meant. Least ya can do is return the favor."

    scene mikuparkjog22
    with dissolve

    s "Jealousy."
    mi "Makoto says the same thing. Something about not lettin’ other people play with your belongings and stuff?"
    s "..."
    mi "Am I on the right track?"
    s "I used to have feelings for someone who belonged to someone else."

    scene mikuparkjog23
    with dissolve2

    mi "..."
    s "More than just {i}feelings,{/i} actually. But...I’ve probably always been a jealous person. "
    s "When I want someone, I want them to be {i}mine{/i} and mine alone. And I don’t want to share them because I don’t want anyone else to {i}ruin{/i} them. "
    s "But..."
    s "More than that, I think I’m worried that the person I’d be sharing would see how small I am compared to everyone else."

    scene mikuparkjog24
    with dissolve

    mi "That’s a {i}small{/i} one?! How friggin’ big do they get?!"
    s "As a person, Miku. I’m not talking about my penis."

    scene mikuparkjog25
    with dissolve

    s "Do you really not feel that way? Because you’ve joked about it — but what if I really {i}did{/i} just...move on from you one day because you didn’t have something I wanted when someone else did?"

    scene mikuparkjog26
    with dissolve

    mi "..."
    s "Why...are you smiling now? That was a pretty heavy question."
    mi "Cause I get it when ya put it like that."
    mi "I {i}would{/i} be sad if ya left me in the dust. "
    mi "I can’t give ya brains like Makoto or boobs like Futaba. I ain’t as creative as Nodoka, ain’t as stylish as Chika, and I ain’t even half as cute as Ami."
    mi "I ain’t got much, really. Don’t even have a family anymore. All I have to give is myself. So yeah...I get it now. But I don’t look at it the same way you do."
    mi "It’s {i}because{/i} of what I lack that I understand why you’d wanna get all that stuff elsewhere. Ain’t wrong to want more out of life...more out of a partner...and I want ya to be happy."
    mi "Chase after whatever it is ya want, Sensei. I ain’t goin’ anywhere. "
    mi "And I know it ain’t sayin’ much since there’re barely any guys left in Kumon-mi to begin with, but you’re the only one I need right now anyway."
    s "..."
    mi "...What? Why’re you just lookin’ at me like that?"
    s "You’ve really grown up, Miku."
    mi "Not without help, I haven’t."
    mi "You’ve done so much for me, Sensei. Ya helped me figure out who I am and that’s...that’s a thing I ain’t ever been able to do on my own."
    mi "There are other ways you can still help me, though...I’ve got a lot left to learn."
    s "Of course. Whatever it is, just let me know. "
    s "I was actually just thinking earlier about how unproblematic you’ve been so far. So if I can return the favor in any way-"
    mi "Sensei."

    stop music fadeout 7.0

    s "...Miku?"
    mi "{i}I’ve got a lot left to learn.{/i}"
    s "..."
    mi "Are you pickin’ up what I’m puttin’ down right now?"
    s "...Uh."

    scene mikuparkjog27
    with fade

    mi "{i}I wanna do it with you...{/i}"

    scene mikuparkjog28
    with dissolve2

    s "...Seriously?"
    mi "{i}Seriously.{/i}"
    mi "{i}You made me really happy today...and now I wanna make you happy too.{/i}"
    s "..."
    mi "{i}Makoto says I’m supposed to wear a condom, though.{/i}"
    s "..."

    scene black

    mi "{i}But I don’t wanna.{/i}"

    $ renpy.end_replay()
    $ mikuspring4 = True

    jump mikuspring5

label mikuspring5:
    play sound "static.mp3"
    scene mikuvirgin1 with flash
    stop sound
    play music "asobeatsex6.mp3"

    "It’s like a storm the moment we make it back to her room, but not in the sense that it triggers her PTSD and sends her into a state of catatonia."
    "It’s violent and sudden and aggressive, but everything about it screams that we’re making the right choice despite how both logic and morality would disagree with that."
    "She tears off her clothes and I tear off mine. The moment that’s done, I pounce on her like a lion about to sink his fangs into the neck of a gazelle."
    "She might be faster than me — she might be more graceful than me — but I am the king of this world. I will always win. And she knows that, which is why she’s stopped trying to get away."

    mi "Ahn...aahmmf...mmm! Mmngh...mmf...Sensei...{i}Sensei...{/i}"

    "A successful hunt lands my tongue in and out of the mouth of a girl who barely knows what to do with it. And I’m sure it doesn’t surprise you to hear how that excites me."
    "She spreads her legs and welcomes me. But a lion does not swallow its meals whole — it tears them to shreds and meticulously cleans every last bit of meat off of the bones."
    "Which is why I keep just kissing her despite how desperately she’s squirming, trying to readjust her waist so that I slide into her without any fanfare."
    "There {i}will{/i} be fanfare, though. This will be a night to remember. And I have felt her insides before, so I know the challenge that awaits me."

    scene mikuvirgin2
    with dissolve

    mi "Mnch...ahn...Sensei...how long...ahnn...are we going to do this for?..."
    s "Feeling impatient, Miku?"
    mi "Of course I’m...mmnch...feeling impatient..."

    "She shifts her hips again, grinding her slit against the tip of my cock."

    mi "Can’t you feel how badly I want it?..."
    mi "Can’t you?..."

    play sound "static.mp3"
    scene mikuvirgin3 with flash
    stop sound

    mi "Huh? What? Why’d you-"
    s "You’re {i}sure{/i} you’re ready for this?"
    mi "Yeah, why?"
    s "I just want you to be prepared for the pain. It’s not going to feel good, but I’ll do my best to make it comfortable."
    mi "You’ve put your fingers in me a bunch of times. Is it really that much different?"
    s "Yes. It’s very different. "

    scene mikuvirgin4
    with dissolve

    mi "I’ll be okay. I can handle pain. "
    s "Okay. Because-"
    mi "But...uhh...just...hyper-thetically, in the event that I {i}can’t...{/i}then what?"
    s "I stop."
    mi "You ain’t gonna be upset that you don’t get to dump your baby batter inside of me?"
    s "I am suddenly no longer aroused. Thanks."

    scene mikuvirgin5
    with dissolve

    mi "That ain’t true, Sensei. Just look at how-"

    scene mikuvirgin6
    with dissolve2

    mi "Oh...wow."
    mi "That looks...way bigger when it’s...right next to my...uhh..."

    scene mikuvirgin7
    with dissolve

    mi "You know what? I’m just gonna look away. You know what do from here on out, don’t ya Sensei? "
    s "It’s okay to be scared, Miku."
    mi "Scared? Me? Champion of Justice and penis? I mean soccer. I mean swimming? Whatever. I ain’t scared. You’re only like three feet long and I’m just a...girl the size of a young boy...what could...go wrong?"
    s "Hey. Look at me."

    scene mikuvirgin8
    with dissolve2

    mi "..."
    s "We don’t have to go through with this. You can back out."
    mi "After coming this close? No way, Jose. What kinda girl would I be if I let you walk outta here without stickin’ it in me?"
    s "One who’s nervous. Which is totally fine."
    mi "Just friggin’ put in, Sensei. The longer you make me wait, the more scared I’m gonna get. Sometimes, ya gotta just rip the bandaid off. And today, that bandaid is my vagina."
    mi "Maybe...don’t actually rip it off, though. I’m pretty sure I still need it for stuff."
    s "If you want me to stop, just say so. Got it?"

    scene mikuvirgin4
    with dissolve

    mi "Got it..."
    s "Then-"
    mi "Hey, is..."
    mi "Uhh..."
    mi "This ain’t a good time to say I love you, is it?"
    s "..."

    scene mikuvirgin7
    with dissolve

    mi "Nevermind! Just...put it in now. Forget that happened."
    s "Miku-"
    mi "Miku isn’t home right now. Please save any and all questions until the end of class. Thank you!"

    scene black
    with dissolve2

    "I do as she says and forget what happened."
    "Remembering it would only make this harder."

    scene mikuvirgin9
    with dissolve2

    "And given that I’m about to penetrate a hole {i}way{/i} too small for me, I already understand just how difficult this is going to be."

    mi "Hey, I’m not gonna, like...bleed, am I?...Cause I really ain’t good with blood..."
    s "Just don’t look down. "
    mi "But that’s where all the action is. You really think I’m gonna be able to just keep my eyes closed for this?"
    s "Or look into my eyes. And I’ll look back into yours the whole time."

    scene mikuvirgin10
    with dissolve

    mi "Easy for you to say! You ain’t got anythin’ else to look at! This’ll be like doin’ a body pillow to you! And I’m an authority on doin’ body pillows cause you ain’t always free!"
    s "I have everything to look at, Miku."
    s "You’re one of the cutest girls I’ve ever laid eyes on."

    scene mikuvirgin11
    with dissolve

    mi "Sh...Shut up...Just put it in me already...I wanna like...make you feel good and stuff..."
    s "Last chance to back-"
    mi "Please...proceed...good sir..."
    s "..."
    mi "Please..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikuvirgin12
    with dissolve2

    "I angle myself down and press the tip of my cock up against her slit — so tight that it might as well be sewn shut."
    "Miku’s breathing intensifies. Her chest begins moving rapidly as her eyes dart around the room and her fingers grip the blanket for support."
    "She doesn’t gaze into my eyes like I direct her to. She doesn’t know {i}what{/i} to do. And it makes me think once more about the gazelle."
    "About its last thoughts before those fangs pierce its throat and drink its blood."
    "That is likely the most pure form of fear that exists."
    "And I am blessed to be able to witness that right now."

    scene mikuvirgin13
    with dissolve2

    mi "Mm!"

    "I sink my fingers into both sides of her waist and begin to move forward."

    mi "Hah...hah...hah! Okay! I can do this! Don’t look down! Don’t...look down!"
    s "You okay, Miku?"
    mi "Huh? Yeah! Is it...it’s not in yet, is it?"
    s "Almost. So I’m gonna keep going, okay?"
    mi "Okay! I’m good! Whooo boy! Here we go! Time to...oh man. Okay! I’m good!"

    "Once more, I gently move forward..."

    scene mikuvirgin14
    with dissolve2

    mi "Haah! Oh shit! Oh man...Is it in? Is that everything?"

    "She reflexively reaches forward as her body send signals to her brain that an intruder is about to cause her a great deal of harm. And her body is right. I am."
    "Yet...Miku stops herself. Her hand simply hovers there as I submerge half of my head in her shallow depths, holding it there for a moment to allow her twitching to subside."

    s "Not yet, Miku..."
    s "You’re not looking down anymore?"

    scene mikuvirgin15
    with fade

    mi "Mm-mm! I can’t!"
    s "Can’t continue? Or can’t look down?"
    mi "Second one! Please proceed, good sir!"
    s "Why do you keep calling me that?"
    mi "Because I’m friggin’ scared, okay?! I’m startin’ to panic from how long this is taking! Just shove it in there already and be done with it!"
    s "How about this — count down from ten. Once you get to zero, I’ll put you out of your misery, okay?"
    mi "Okay! Okay! Ten!"
    mi "Nine!"

    "Like a doctor anesthetizing a patient, I pull out my trump card and begin to slide myself deeper into her the moment she starts counting down."
    "And while this works like a charm when you’re dealing with a patient who has an IV pumping drugs into their veins, it’s significantly {i}less{/i} effective when you’re deflowering a small girl."
    "Which is why I still haven’t managed to break through despite her now being at “eight.”"

    mi "Seven!"
    mi "Six!"
    s "Actually...can you start from ten again?"

    scene mikuvirgin16
    with dissolve

    mi "Again?! But-"

    scene mikuvirgin17
    with dissolve

    mi "Aah! Nope! Looked down on accident! Why are you makin’ me start over?!"
    s "I just...need a little more time. That’s all."

    scene mikuvirgin15
    with dissolve

    mi "Nghhh! Fine! Ten!"

    "I try moving forward again only to be met by the same resistance I’d encountered last time — something unlike anything I’ve experienced in the past. "
    "And it begins to make {i}me{/i} worry that I’m going to harm her even more than I thought I was."

    mi "Mmmngh nine!"
    mi "Eight!"

    "It’s now or never. I can’t stall any longer."
    "It’s {s}un{/s}safe to continue."

    mi "Seven!"

    "I lunge forward, breaking through her resistance in one fell swoop."

    mi "Si-"

    stop music
    play sound "stab.mp3"
    scene mikuvirgin18 with hpunch

    mi "Ngheh!?!?"

    "I’m in."

    play sound "static.mp3"
    scene mikuvirgin19 with flash
    stop sound

    mi "Ten! Nine! Eight! Seven! Six! Five! Four! Three! Two! One! Ten! Nine! Eight! Seven! Six! Five! Four! Three! Two! One! "

    "She begins repeating her countdown, but it’s easy to tell by the look on her face that she’s doing it for different reasons this time."

    s "Are you okay? Do you need to-"
    mi "Shhh! Ten! Nine! Eight! Seven! Six! Five! Four! Three! Two! One!"
    s "... "
    mi "Ten! Nine! Eight! Seven! Six! Five! Four! Three! Two! One!"

    "I stay still for a moment, not wanting to make the initial pain any worse. But Miku gets caught in a loop and it would feel wrong to just...stop when she’s clearly trying so hard."

    scene mikuvirgin20
    with hpunch

    mi "Nghhehghhg?!?!"

    "So I elect to keep going."
    "I thrust into something that very {i}clearly{/i} doesn’t want me there — something that’s not even pleasurable for {i}me{/i} as it squeezes me hard enough to cause physical pain."
    "A new resistance then takes the place of the former one. "
    "I have nowhere else to go."

    scene mikuvirgin21
    with dissolve2

    mi "{i}Mnnnnnnngh!!!!! Mmmmf!!!!!{/i}"

    "She covers her mouth to keep herself from screaming as tears begin to well up in her eyes."
    "They flow so heavily that even closing her eyelids as tightly as she can is unsuccessful in staving off the flood."
    "And, as if that was not enough-"
    "I begin to feel a second one."

    play sound "static.mp3"
    scene mikuvirgin22 with flash
    stop sound
    play music "undersea.mp3"

    "There’s a warmth I’m too familiar with that both is and isn’t meant to be there."
    "It sticks to me like glue. And the sound it produces as I continue to move is-"
    "Well, I imagine it’s how the neck of a gazelle would sound as razor-sharp teeth chew through flesh and muscle."

    mi "{i}MMMMMFGHH! HNGH! HNGH!{/i}"
    s "..."

    "Once more, a girl subjects herself to excruciating pain for both my benefit and the mere {i}chance{/i} to hollow out a bigger space in an already empty heart."
    "This time, however, that pain seems worse than ever before."

    play sound "static.mp3"
    scene mikuvirgin23 with flash
    stop sound

    mi "{i}MMMMMMMMMMM!!!!!!!{/i}"

    "This poor girl — writhing in agony when all she wanted was to experience something wonderful. How twisted I am to do that to her. How terrible I-"

    play sound "static.mp3"
    scene mikuvirgin24 with flash
    stop sound

    "{b}hey man, it’s not YOUR fault she’s tight as shit. some girls just ain’t built like the others. it’s nothing some good old fashioned stretching won’t fix.{/b}"

    play sound "static.mp3"
    scene mikuvirgin23 with flash
    stop sound

    "He’s right for once. This {i}isn’t{/i} my fault. She wanted this. We both wanted this. And if her body is not yet prepared, it’s not- wait. No, hold on."

    play sound "static.mp3"
    scene mikuvirgin24 with flash
    stop sound

    "{b}stop thinking, bitch boy. just savor the moment.{/b}"
    "{b}the more time you spend rationalizing, the more regrets you’ll have when you can’t properly recall how her pussy felt when you’re jerking it later{/b}"

    play sound "static.mp3"
    scene mikuvirgin23 with flash
    stop sound

    "Yeah. I should think less."

    mi "{i}Stop...{/i}"

    "I should savor the moment. This is a night to remember. Everything is going according to plan."

    mi "{i}Sensei...stop...I can’t...{/i}"

    "I just need to stretch her out. After that, everything will-"

    play sound "static.mp3"
    scene mikuvirgin25 with flash
    stop sound

    mi "Stop, stop, stop, stop, stop, stop, stop! It hurts too bad! I can’t! I can’t do it! I’m sorry! Please stop!"

    play sound "static.mp3"
    scene mikuvirgin15 with flash
    stop sound

    s "Huh? Yeah! Okay! We’ll stop. We’re done. That’s it."
    mi "I’m so sorry...I’m so sorry! I thought I could do it! I thought I could!"
    s "It’s over. We’re done. You’re fine."

    scene mikuvirgin26
    with dissolve2

    mi "I’m fine? So I’m not-"

    scene mikuvirgin27
    with dissolve2

    mi "{i}Hah...{/i}"
    s "Hey. Miku. Don’t look down. Look up here."
    mi "Is that...normal?..."

    play sound "static.mp3"
    scene mikuvirgin28 with flash
    stop sound

    s "I told you to look up here. Don’t look down. You’re okay."
    mi "So much...{i}blood...{/i}"

    play sound "static.mp3"
    scene mikufinetime8 with flash
    scene mikuvirgin28 with flash
    stop sound

    s "It’ll stop. I promise."
    mi "Sensei...{i}it hurts...{/i}"

    play sound "static.mp3"
    scene mikufinetime8 with flash
    scene mikuvirgin28 with flash
    stop sound

    mi "{i}It hurts...so bad...I’m gonna be sick...oh god, I’m gonna be sick!{/i}"
    s "Miku, you’re okay. I’ve got you."

    play sound "static.mp3"
    scene mikufinetime8 with flash
    scene mikuvirgin29 with flash
    stop sound

    s "{b}EVERYTHING WILL BE FINE{/b}"
    mi "AAAAAAAHHHHH! GET OFF GET OFF GET OFF! GET AWAY FROM ME! STOP!"

    play sound "static.mp3"
    scene mikufinetime8 with flash
    scene mikuvirgin28 with flash
    scene mikuvirgin29 with flash
    scene mikuvirgin28 with flash
    scene mikufinetime8 with flash
    scene mikuvirgin29 with flash
    scene mikuvirgin28 with flash
    scene mikufinetime8 with flash
    scene mikuvirgin30 with flash
    stop sound

    s "Okay! I’m over here now. I’m not touching you. You’re okay."
    mi "Nghhhh! It hurts so bad! Something’s wrong! I can still feel it coming out!"
    s "I’m sure it’s...fine..."
    s "You just...have to...wait for it to..."
    mi "NGAAAHAHAH! MAKE IT STOP! I’M SCARED, SENSEI! IT HURTS! IT REALLY, REALLY HURTS!"

    play sound "static.mp3"
    scene mikuvirgin31 with flash
    stop sound

    mi "Hah! Nghh! Mmmngh! Aaaaaah! Nch!"

    "As she clutches her stomach and wipes the tears from her eyes, I begin to worry too."
    "I know that bleeding is common during times like this, but...that seems like...{i}a lot...{/i}"

    mi "Ngh! Ngh...mmngh! When is it...supposed to stop?!"
    s "..."
    mi "Sensei! When is it supposed to stop?!"

    play sound "static.mp3"
    scene mikuvirgin32 with flash
    stop sound

    s "Uhh..."
    s "Uuuhhhh..."
    s "Maybe we should...call an ambulance if...you’re really sure that something’s wrong. Just...to be safe."

    play sound "static.mp3"
    scene mikuvirgin33 with flash
    stop sound

    "{b}oh yeah, real smart. “hello, 119? my name is akira arakawa. i’m 31 years old and i just finished screwing this teen who is now profusely bleeding from her vagina. whoops!”{/b}"

    play sound "static.mp3"
    scene mikuvirgin34 with flash
    stop sound

    s "Not now! I’m thinking!"
    mi "Aaaaaahahaha! I don’t know what to do! It won’t stop!"

    play sound "tackle.mp3"
    scene black

    s "Makoto! She’ll know what to do. I’ll call her!"
    mi "Please! Just do something!"

    play sound "static.mp3"
    scene mikuvirgin35 with flash
    stop sound
    play sound "phonebeep.wav"

    mak "Hel-"
    s "Where are you?"
    mak "Well, {i}someone{/i} sounds urgent o-"
    s "Where are you, Makoto?!"
    mak "I-I’m on my way back to the dorm! Jeez! Why are you yelling?! What’s going on?!"
    s "I fucked Miku and now she’s bleeding everywhere. I don’t know what to do."
    mak "Wow. You just left {i}me{/i} lying there when you were done taking my virginity. You really {i}were{/i} an asshole back then, huh?"
    s "This isn’t like that! She’s bleeding {i}a lot.{/i}"
    mak "Like...how much?"
    s "A lot, Makoto. I don’t know. I’m not an expert at vaginal bleeding. I just know this has never happened to me before. So should I call an ambulance or-"
    mak "No, hold on. I’ll be back in like five minutes and I can take a look at her. And if she needs an ambulance, {i}I{/i} will call them. You doing that raises so many red flags it’s not even funny."
    s "Okay...thank you."
    mak "You’re welcome. Now, let this be a lesson on the downsides of sticking your dick in anyone who isn’t me."
    s "I’m not in the mood to be joking around right now, Makoto. I really hurt her. And now she’s scared and crying and-"
    mak "Yes, yes. I know. But if I don’t keep you calm, I’ll have {i}two{/i} people to worry about when I get there instead of {i}just{/i} my freshly deflowered roommate. "
    s "If I knew this was going to happen-"
    mak "Sensei, relax..."

    scene black
    with dissolve2

    mak "Everything will be fine..."

    $ renpy.end_replay()
    $ mikuspring5 = True

    jump makotospring2

label mikulust5:
    scene black
    with dissolve2
    scene mikufirstlust1
    with dissolve2
    play music "citylife.mp3"

    "I make my way over to the porn shop to find that, for some reason, Miku is now allowed to man it completely unsupervised."
    "Which, of course, I immediately take advantage of by persuading her to close up shop for the night so we can “further her education” or something along those lines in the back room."
    "I can’t specifically remember what I said because I had an erection at the time of saying it and had to put my brain on pause. "
    "Which is a thing that happens to me since there’s only so much blood in my body and so much penis to fill."
    "But for those who have smaller penises or smaller brains that require less blood to be powered, I imagine they too would have taken advantage of this girl. "
    "Or at least that’s what I will tell myself so I can feel better about wrapping my arm around her while we watch that one video of that girl who looks like Makoto getting railed by ten dudes."

    mi "I’ve gotta say, Sensei. Watchin’ Makoto take all those wieners ain’t really havin’ the same effect on me that it does on you."
    s "You do know that’s not {i}actually{/i} Makoto, right?"
    mi "Can we {i}really{/i} know that for sure, though? Cause Makoto’s an expert at takin’ wieners now, ain’t she? Bet she could handle ten no problem. {i}I{/i} can’t even handle one."
    s "One day, Miku. One day."
    mi "I sure hope so, Sensei. Cause all these porno girls always make it look like it’s the greatest thing in the world. It’s like they ain’t ever even been screwed into a hospital before."
    s "To be fair, I imagine most of them haven’t. You were a very rare case and are now a very rare regret of mine."

    scene mikufirstlust2
    with dissolve

    mi "You regret puttin’ it in me? Ain’t that a little rude to say right to my face?"
    s "I regret {i}hurting{/i} you. I should have been more careful considering our...difference in size."

    if nodokathontwo3 == True:
        mi "But Sana’s even smaller than me and I watched you go crazy on her during the Dorm Wars. "
        mi "Great job, by the way. Was almost like watchin’ a real porno, just with girls who probably ain’t old enough to-"
        s "That was filmed?"
        mi "Oh. You didn’t know?"
        s "Nope."

        scene mikufirstlust3
        with dissolve

        mi "Then, uhh...surprise?"
        s "..."
        mi "..."

    else:
        mi "But I ain’t {i}that{/i} much smaller than some of the other girls you’re doin’ stuff with. "
        mi "How come I ain’t ever hearin’ about {i}them{/i} breakin’ {i}their{/i} vaginas? And trust me, I’ve asked."
        s "{i}Don’t.{/i} This is supposed to be a secret, remember?"
        mi "Sensei, ain’t nobody keepin’ this a secret anymore. And if that’s what ya want, that’s what I’ll do it. But it really ain’t as bad as you’re makin’ it-"

    play sound "static.mp3"
    scene mikufirstlust4 with flash
    stop sound

    s "Anyway, I don’t want it to sound like I regret...{i}going down this path with you.{/i} Or anyone else, really. Just the...outcome of it."
    mi "Thought your whole thing was “regretting” stuff, though. Least that’s how Makoto makes it sound sometimes."

    scene mikufirstlust5
    with dissolve

    s "On a...{i}moral{/i} level, maybe. Like, there’s no way even {i}I{/i} can convince myself that what I’m doing with you girls is justifiable in any sort of way. "
    s "But on a romantic or...interpersonal level, I don’t have any regrets. Or...maybe I do have {i}some{/i} regrets and am just talking myself into a hole right now."
    mi "Yeah, I don’t really get what you’re tryin’ to say. I just know you’ve got a good wiener and I’m sorry it doesn’t fit inside of me."

    scene mikufirstlust6
    with dissolve

    s "Thank you, Miku. I needed to hear that."
    mi "Anything for you, Sensei! "
    s "There’s really no need to apologize for something beyond your control, though. You can’t help how your body develops."
    mi "And {i}you{/i} can’t help that you like porkin’ teenagers. So why’ve you gotta be so sad about it all the time?"
    s "Probably...because I know it’s wrong and I do it anyway. "
    mi "Cause it feels good? Or cause ya like havin’ somethin’ to blame yourself for?"
    s "Yes."
    mi "You get what I’m sayin’ though, right?"
    s "Do {i}you{/i} get what you’re saying? Because this seems to me like more stuff you probably just picked up from Makoto. "
    mi "You sayin’ I ain’t smart enough to have opinions of my own?"
    s "Of course not. I’m just saying you’re not smart enough to have {i}smart{/i} opinions."

    scene mikufirstlust7
    with dissolve

    mi "Hey!"
    s "Or maybe “perceptive” is a better word? Either way, I did not come here tonight to be psychoanalyzed. I get enough of that everywhere else."

    scene mikufirstlust8
    with dissolve

    mi "Well, why {i}did{/i} ya come here then? Cause you said it was for my education when ya showed up, but you ain’t done much educatin’ at all apart from showin’ me Makoto’s sex tape."
    s "Again, {i}not{/i} Makoto."
    mi "Again, we can’t be sure."
    s "Miku — I would like you to harness the power of every last one of your brain cells to come up with the {i}real{/i} reason I am watching porn with you in a room overflowing with sexual energy."

    scene mikufirstlust9
    with dissolve

    mi "Oh! I know this! We’re flirting, ain’t we?!"
    s "You did it, Miku. I’ve never been more proud in my life."

    scene mikufirstlust10
    with dissolve

    mi "Whatcha wanna do, though? Ain’t you gettin’ bored of just usin’ our hands on each other all the time?"
    s "Nope. "
    mi "Not even a little?"
    s "Nope."
    mi "Wow, Maki was right. Men really are easy to please, ain’t they?"
    s "You say that as if being fingered isn’t your actual favorite thing in the world."
    mi "Good point, Sensei. I used to think it was cheeseburgers. Not so much nowadays, though. "

    scene mikufirstlust11
    with dissolve

    mi "Either way, though! I wanna try somethin’ else if we’re gonna do horny stuff! I’ve been learnin’ all sorts’a things lately, Sensei! Time for you to rape the benefits of all my hard work!"
    s "It’s “reap,” Miku. You do not “rape” the benefits of something."
    mi "Not with that attitude, ya don’t!"

    scene black
    with dissolve2

    "Miku hops off the couch and brings herself to her knees in front of me."

    play sound "static.mp3"
    scene mikufirstlust12 with flash
    stop sound

    "That’s it. That’s the narration."

    mi "So! You know about boobs, right?"
    s "I’ve heard of them, yeah."
    mi "Great! So {i}apparently,{/i} they’re for more than just feedin’ babies or makin’ fashion execs a ton of money. You can do sex stuff with ‘em too!"
    s "I...{i}yes.{/i} But Miku-"
    mi "Yeah? What is it?"
    s "..."
    mi "?..."
    s "You know what? Nothing. I’ll just let you do your thing."

    scene mikufirstlust13
    with dissolve

    mi "Yeah, yeah. I know I ain’t workin’ with much here. But turns out there are a lotta flat girls in porn. So I’ve been watchin some’a what {i}they{/i} do and tryin’ to learn from {i}them.{/i}"

    scene mikufirstlust14
    with dissolve

    mi "Which is why I now know that you don’t even {i}need{/i} boobs to give a boob job! Who would’a known dicks are so simple?! Literally {i}anything{/i} makes ‘em feel good!"
    s "Ugh. Don’t remind me."
    mi "Can I try, Sensei? Think they call it a “naizuri” for girls like me. "
    s "Absolutely. I {i}do{/i} have one request before we start, though."

    scene mikufirstlust15
    with dissolve

    mi "You do? What? What is it?"
    s "I want you to call me something else during sex from now on."

    scene mikufirstlust16
    with dissolve

    mi "Frick yeah! I’ve been waitin’ for this moment ever since I found out you did this with Makoto too! "
    mi "Hit me, Sensei. Whatcha got? What cool new sex name should I call ya?"

    "What should I have Miku call me?"

    jump mikunaming

label mikunaming:
    $ mikumaster = renpy.input("Enter a name for Miku to call you...")
    $ mikumaster = mikumaster.strip()

    if mikumaster.lower() in ["sensei"]:
        s "It might be weird, but...I want you to call me Sensei during sex."

        scene mikufirstlust17
        with dissolve

        mi "{i}Hah.{/i}"
        s "Miku? What’s wrong?"
        mi "All that buildup and excitement wonderin’ what you’re gonna make me do, and this is the payoff. Just callin’ you what I’ve always called you."
        s "Oh, have you been calling me that this whole time? I never noticed."
        mi "Yeah, of course ya haven’t. Too busy gettin’ called Captain Wiener by Makoto or something. "
        s "Fine, fine. Instead of Sensei, you can call me..."

        jump mikunaming

    if mikumaster.lower() in ["captain wiener"]:
        s "Captain Wiener. "

        scene mikufirstlust18
        with dissolve

        mi "That ain’t funny, Captain Wiener! Ya think you’re so damn smart, Captain Wiener! Just wait ‘til I make ya call me First Admiral G-Spot! "
        s "You may proceed, First Admiral G-Spot. My life is in your hands."
        mi "Fine! But I’m goin’ back to “Sensei” because Captain Wiener ain’t as hot as it sounded in my head!"
        s "Whatever you need to do, Miku...Whatever you need to do."

        $ mikumaster = "Sensei"

        jump mikupostnaming


    if mikumaster.lower() in ["miku"]:
        s "I would like for you to call me Miku from now on."

        scene mikufirstlust19
        with dissolve

        mi "Okay! Sure!"
        s "Wait, really?"
        mi "Yeah! Why do ya seem so surprised?"
        s "People just...normally put up a fight when I ask them to call me by their name instead of my own?"
        mi "Sounds kinda selfish to me, Miku. There can be more than one of us. Just like {i}you{/i} can have more than one girlfriend and {i}I{/i} can have more than one boyfriend."
        s "No you can’t."

        scene mikufirstlust20
        with dissolve

        mi "I can’t? Why not?"
        s "Because you’re mine, obviously."

        scene mikufirstlust21
        with dissolve

        mi "..."
        s "Is there a problem with that, other Miku?"
        mi "No. That just made me really horny for some reason."
        s "Good. Well, channel that energy into talent as I imagine you will need an abundance of it to pull off your next stunt."

        scene mikufirstlust22
        with dissolve

        mi "You got it, Miku! Miku will give it her all!"

        jump mikupostnaming

    if mikumaster.lower() in ["makoto"]:
        s "I’d like for you to call me Makoto from now on."

        scene mikufirstlust23
        with dissolve

        mi "Really? Does that mean you make Makoto call you Miku?"

        if makotomaster.lower() in ["miku"]:
            s "Yes."
        else:
            s "Ugh...no. But maybe she’ll do that now if I ask nicely? She’s kind of dependent on my penis at this point, I think."

        mi "Why do ya wanna be called that, though? Like I get that it’s a unisex name and stuff, but so is Akira. Why not just keep usin’ that one?"
        s "Oh, easy. Because every time I close my eyes, I also just imagine I’m Makoto. "
        mi "Really?"
        s "Yeah. Big hobby of mine."
        mi "So, when you’re gettin’ naughty with Makoto-"
        s "I close my eyes and it’s two Makotos. And that’s so much better than just the one."
        mi "Huh. Interesting. Wonder if she’s closin’ her eyes and pretendin’ to be you, now."
        s "You know, it really seems that way sometimes."
        s "Regardless, are you okay with this? Or would calling me by your best friend’s name, like...weird you out or something?"
        mi "I don’t really care. I’ll call ya Makoto. Ain’t gonna bother me."
        s "Great. Then I guess we can just...proceed then?"
        mi "Yeah, I’m ready when you are."

        jump mikupostnaming


    if mikumaster.lower() in ["maki"]:
        s "I’d like for you to call me Maki from now on."

        scene mikufirstlust24
        with dissolve

        mi "{i}Maki?{/i} Really? Why that?"
        s "Because Makoto won’t and you’re my only hope."
        mi "I get wantin’ to bang Maki. She’s a hot MILF lady. It’s the wantin’ to {i}be{/i} Maki part I ain’t understandin’. "
        s "She’s just really cool and sex-positive and I feel like imagining I’m her during a sexual encounter will give me the confidence I need to perform better."
        mi "So you’re sayin’ if I call ya Maki, you’ll be better at sex stuff?"
        s "That’s the idea, yeah."

        scene mikufirstlust25
        with dissolve

        mi "Worth a shot then. Ain’t like I’ve got anythin’ to lose except maybe a little pride."
        s "Great. Then I guess we can just...proceed then?"
        mi "Yeah, I’m ready when you are."

        jump mikupostnaming

    if mikumaster.lower() in ["coach"]:
        s "Why not call me “Coach” again? I always liked that when you did it during soccer practice?"

        scene mikufirstlust26
        with dissolve

        mi "D...Did you really? Always kinda worried I might’ve been annoyin’ you since I kinda just...dragged you into it one day."
        s "No, I thought it was cute. And it spawned a great deal of sexual fantasies for me that I’ve now had to abandon since the soccer club disbanded."

        scene mikufirstlust27
        with dissolve

        mi "Well, I mean..."
        mi "It ain’t like the storage room is just {i}gone.{/i} And it ain’t like I threw away my uniform, so..."
        mi "If you maybe wanted to, you know...{i}pretend...{/i}we could probably do that."
        s "You’re okay with calling me Coach, then?"

        scene mikufirstlust28
        with dissolve

        mi "..."
        s "..."
        mi "Can I be honest for a sec?"
        s "Of course."
        mi "There’s probably nothin’ else I’d {i}rather{/i} call ya. And I’m kinda tempted to break my vagina again right now just thinkin’ about this."
        s "This sounds like good news to me."
        mi "Yeah...just glad this fantasy’s hittin’ me now instead of back then since I can’t imagine it would’a been easy to practice this wet. "
        s "Okay. Please continue with your attempt at a boob-job before I tackle you and inflict further damage upon your underdeveloped body. "
        mi "Yes, Coach."

        jump mikupostnaming

    if mikumaster.lower() in ["selebus"]:
        s "I want you to call me Selebus from now on. He’s the creator of-"
        mi "Lessons in Love. I know."
        s "What? How do you know?"

        scene mikufirstlust29
        with dissolve

        mi "We just started sellin’ it at the shop. Maki made me play the first half hour of it to get familiar with the product."
        mi "But then Ami showed up and started tellin’ me to breed her and I had to turn it off because I didn’t get it."
        s "Wait, Ami’s in it?"

        scene mikufirstlust30
        with dissolve

        mi "Yeah, we {i}all{/i} are. How’d ya not know that if you’re askin’ me to call you by the creator’s name?"
        s "I...don’t know. I just feel like this creates some sort of meta paradox thing where we all exist inside of a game that simulates exactly what we’re going through right now."
        mi "So you’re sayin’ that what’s happenin’ now could be happenin’ in the game version too?"
        s "Right. And if the two of us inside of the {i}game{/i} think they’re real and are having this exact conversation-"

        scene mikufirstlust31
        with dissolve

        mi "Holy convolution, Batman!"
        s "I asked you to call me Selebus, not Batman."
        mi "Sorry. I don’t know why I said that."
        s "You know, for the sake of avoiding a paradox, let’s just say you {i}shouldn’t{/i} call me Selebus."
        s "I’ll choose a new name instead."

        jump mikunaming

    if mikumaster.lower() in ["kirin"]:
        s "How about you call me Kirin from now on?"

        scene mikufirstlust32
        with dissolve

        mi "You ain’t gonna tell the {i}real{/i} Kirin about this, are you? Cause she already tries gettin’ into my pants way more than I’m comfortable with."
        s "Just out of curiosity, how much of Kirin trying to get into your pants {i}are{/i} you comfortable with?"
        mi "Anything more than once a week just seems excessive when there’s a perfectly good penis attached to the guy we both like."
        s "Got it. I’ll relay this news to Kirin then."
        mi "Okay. Just again, leave out the part of me callin’ you that from now on."
        s "Oh, so you actually will?"

        scene mikufirstlust23
        with dissolve

        mi "Sure. Can’t see why not. A name’s just a name, you know."
        s "Oh...cool."
        s "I guess...proceed then?"
        mi "Sure, yeah."

        jump mikupostnaming

    if mikumaster.lower() in ["daddy", "dad", "father", "papa"]:
        s "So...you might be a little uncomfortable with this, but I want you to call me [mikumaster]."

        scene mikufirstlust33
        with dissolve2

        mi "..."
        s "Miku?"
        mi "Sorry, I..."
        mi "I know that’s, like...a normal thing boys like to be called for...some reason during stuff like this."
        mi "But I...need some more time. I ain’t ready to...call anybody that in...{i}any{/i} sorta situation yet."
        s "..."
        mi "I’m sorry, Sensei..."
        mi "Maybe in the future when I’m...better. But-"
        s "It’s fine. I’ll just choose something else."
        mi "Thank you...and...sorry again."

        jump mikunaming

    if mikumaster.lower() in ["akira"]:
        s "Just call me Akira."

        scene mikufirstlust23
        with dissolve

        mi "Really? Ain’t that just your regular name?"
        s "Yeah. What’s more romantic than being called by your regular name during the most intimate moments of your life?"
        mi "Good point. Probably why I wanna take your pants off every time you call me Miku."
        s "Miku."
        mi "See? That’s it. They’re comin’ off."

        jump mikupostnaming

    else:
        s "Just call me [mikumaster] if that’s okay."

        scene mikufirstlust34
        with dissolve

        mi "Sure is, [mikumaster]. A name’s just a name after all. And if that’s what turns you on, that’s what it’ll be."
        s "Perfect. Then I guess we can just...proceed then?"
        mi "Yeah, I’m ready when you are."

        jump mikupostnaming

label mikupostnaming:
    scene mikufirstlust35
    with dissolve

    mi "Gotta get this bra up before anything, though. Don’t want you gettin’ any friction burns for my sake."

    scene mikufirstlust36
    with dissolve

    mi "No laughin’, okay? And no teasin’ either. I’m still self-conscious. "

    scene mikufirstlust37
    with dissolve2

    mi "I’m just willin’ to put that aside if it means makin’ you feel good...[mikumaster]."
    s "..."
    mi "What? Whatcha lookin’ at?"
    s "Something too cute to exist, I think. "
    mi "You really think I’m cute, [mikumaster]? You’re not just...saying that to {i}humor{/i} me?"
    s "There’s an easy way to find out if you really want to know, Miku. "
    mi "Not even gonna take it out yourself? Gonna make {i}me{/i} do it?"
    s "I just wouldn’t want to rob you of the chance to open up a present when Christmas is still so far away."
    mi "So kind, [mikumaster]. "
    mi "Please...allow me to show you my gratitude."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "zipper.mp3"
    "..."

    scene mikufirstlust38
    with dissolve2

    "Miku inches closer to the couch, gripping my cock and placing between two budding mounds that I wouldn’t even know were there if not for my eyes."
    "I’m very happy with what I see, though. And even more happy each time she leans forward and presses her cheek against the tip. "
    "I stroke her face as she very slowly and very {i}sensually{/i} begins to move her body, using her hand to press the underside of my shaft against her to absorb her warmth."

    mi "Still think I’m cute when I do this, [mikumaster]?"
    s "Even cuter than you were a few minutes ago."
    mi "Oh yeah? I’m not {i}sexy{/i} now that I’m learnin’ all sorts’a stuff about how to...{i}take care{/i} of my teacher?"
    s "I think you’ve got a little work left to do until you reach the “sexy” category, Miku."
    mi "Work, you say?"

    scene mikufirstlust39
    with dissolve2

    mi "{i}I{/i} can work, [mikumaster]. I’m much more willing to learn when it comes to you than when it comes to math. {i}Math{/i} never makes me cum."
    s "One more difference between you and Makoto, I guess."
    mi "Mhmmm~ But the biggest difference is pressed against you right now, isn’t it? Or maybe it’d make more sense to call it the...{i}smallest{/i} difference in this case."
    mi "You really don’t mind how little they are? How little...{i}all{/i} of me is...[mikumaster]?"
    s "Okay...{i}now{/i} you’re crossing into sexy territory. "
    mi "Did it feel good when you fucked me?...We haven’t gotten to talk much about it since then."
    mi "Boys like them {i}tight,{/i} don’t they? Was I...sufficient?...[mikumaster]?"

    "I rack my mind to try and remember the sensation, but all I can find is something that felt more suffocating than anything else."
    "Of course I can’t say that, though. I don’t want to kill the mood when she’s already trying {i}this{/i} hard. So I’ll find a way to tell her the truth {i}without{/i} hurting her."

    s "I’d break you all over again if I had the chance to..."

    scene mikufirstlust40
    with dissolve

    mi "Oh, you’ll have {i}plenty{/i} of chances...I’m working {i}really{/i} hard to take more of you, [mikumaster]."
    mi "Like some nights, when I’m {i}really{/i} horny, I can almost get a second finger inside."
    mi "How many more fingers do I need to fit, you think? Before I’m ready to try out {i}this{/i} again?"
    s "I don’t know...but I’d love to watch you practice."

    scene mikufirstlust41
    with dissolve

    mi "Yeah?...You’d love to watch me lie there and struggle to make myself feel half as good as {i}you{/i} can make me feel?"
    mi "Between that and splitting me open, I’m startin’ to think you might {i}like{/i} watchin’ me suffer."
    s "I’m starting to think the same with you, Miku. Having my cock so close to your mouth and refusing to even lick it is {i}sinful{/i} behavior."
    mi "I’m not {i}refusing,{/i} [mikumaster]. You just haven’t asked me to."

    scene mikufirstlust42
    with dissolve2

    mi "I’ll do...mlem...anything you want...you just...mlem...might need to give me directions sometimes..."
    mi "I’m still...ahm...new after all...I don’t know what I’m doing..."
    s "Seems to me like you’re...learning rather quickly, though..."
    mi "Mmm...it’s like they say on the field...Practice makes perfect..."
    mi "I wonder if practice will help my boobs grow, though?"
    s "It won’t...and I’m...{i}glad{/i} it won’t...because this feels great in its own way, Miku..."

    scene mikufirstlust43
    with dissolve2

    mi "Mlem...yeah?...That feels good?..."
    s "It does...I just...wish you’d...go a little harder..."
    mi "Mlem...mlem....harder?...What’s that mean?"

    "Her already slow movements somehow get even {i}slower{/i} as she teases me. And if it weren’t for her breathing, I doubt I’d feel her body moving against me at all."

    s "What happened to...doing what I {i}ask?{/i}"
    mi "I’ll gladly do what you ask, [mikumaster]. I just don’t understand how to go “harder” when I have nothing to go harder {i}with.{/i}"
    s "Just...suck it...please..."
    mi "Mlem...mmnh...hnmmm~"

    scene mikufirstlust44
    with dissolve

    mi "Ya know, I {i}want{/i} to. But I feel like you ain’t tellin’ me what it {i}really{/i} is you want. "
    mi "You’re holdin’ back for me, ain’t ya? Why? "
    s "It’s hard not to when what I {i}really{/i} want to do will send you back to the hospital."
    mi "You want to fuck me, [mikumaster]?...Does havin’ your big cock stuck between these little mosquito bites drive you that crazy? "
    s "Mnh..."
    mi "You wanna cum on my face? Will that make you feel better?"
    s "Just...fucking suck it, Miku..."
    s "It’s torturous to just...lick the tip like that and not finish the job..."
    mi "Finish the job, you say? So you {i}do{/i} want to cum? From just a couple minutes of teasing? And you say {i}I’m{/i} the cute one."
    s "Miku-"
    mi "Tell ya what, [mikumaster]. Close your eyes and I’ll {i}finish the job{/i} for ya. There’s somethin’ {i}else{/i} I want to try, though."
    s "And I...can’t know what it is beforehand?..."
    mi "Nope! It’s a {i}surprise...{/i}"

    scene black
    with dissolve2

    s "{i}Hah...{/i}fine."
    s "But nothing goes inside me. Do you understand?"
    mi "Mhm~"

    scene mikufirstlust45
    with dissolve2

    mi "Me neither..."

    play sound "static.mp3"
    scene mikufirstlust46 with flash
    stop sound

    s "Wait, Miku...I don’t think we should-"
    mi "Relax, [mikumaster]...I’m not putting it in...I’m just gonna stroke it for a little while..."
    mi "And if you just {i}happen{/i} to cum while I’m doing that?...{i}Oh well...{/i}"

    "I can feel her grinding lightly against the tip of my cock, almost mechanically stroking me into her pussy as I subconsciously prod at it, praying for her miraculous descent."
    "But knowing that there is forbidden fruit not yet ripe for the taking just {i}begging{/i} to be picked makes me feel as if this is not a sensation that will last for very long."

    scene mikufirstlust47
    with dissolve2

    s "............"
    mi "This is another trick I learned...from watching girls my size play with cocks even bigger than {i}yours,{/i} [mikumaster]."
    mi "You don’t {i}need{/i} to go all the way inside of my pussy to feel good. Boys are so simple that...all they need to do is...{i}touch{/i} it a little bit..."
    mi "Guess that...makes {i}me{/i} simple too, though, cause...this feels {i}really{/i} good."
    mi "Plus, I feel bad that ya didn’t get to bust inside of me last time. Maybe I can make up for it now if I angle it right?"
    s "{i}Hah........hah............{/i}"
    mi "{i}I want you so bad...[mikumaster]...{/i}but I’m sure I don’t have to say that when...you can {i}feel{/i} it."

    "Her grip gets tighter as she leans forward, squeezing and pulling me between her lips as she gyrates just barely enough to prevent me from sliding in."
    "And while the temptation is powerful to thrust upward and break her once more, the constant pressure she applies on my upper body reminds me that I’m not to do that."
    "Which really means that all I {i}can{/i} do is look on in agony as she jerks me off into her slit."

    mi "Much better than my mouth, right?..."
    s "Miku..."
    mi "[mikumaster]..."
    s "I won’t last much longer if you don’t slow down a little..."
    mi "You’re asking {i}me{/i} to slow down?...Who do you think you’re talking to?"

    scene mikufirstlust48
    with dissolve

    s "Ah...wait..."
    mi "{i}Wait?{/i} We’re not just running anymore, [mikumaster]. Not {i}this{/i} time at least. "
    mi "I’ve gotta practice lots and lots if I ever want the real thing..."
    mi "And I {i}do...{/i}I want it so bad...I want you {i}so{/i} bad...and this is the best way to warm me up to your size, isn’t it? "
    s "Miku..."
    mi "Cum for me...[mikumaster]...cum for my tight...{i}schoolgirl{/i} pussy..."

    scene black
    with dissolve2

    "I close my eyes..."
    "And let her escort me to the finish line."

    scene mikufirstlust49
    with dissolve2

    "She pushes back against my cock with the tips of her fingers, preventing me from cumming {i}into{/i} her pussy and instead, just shooting everything onto her ass and her thighs."
    "It is a reasonable compromise as far as I am concerned."

    play sound "static.mp3"
    scene mikufirstlust1 with flash
    stop sound

    "And then we’re right back to sitting on the couch, watching fake-Makoto get fucked by even {i}more{/i} guys this time as if nothing ever happened."
    "I like that about Miku. How the sexual stuff is essentially activated by a toggle switch."
    "But it makes me a little concerned as well — because she really {i}is{/i} more just...like a friend with benefits than anything else."
    "..."
    "Do I want {i}more{/i} than that?"

    mi "Man. I’m really gonna need to ask Makoto how she does it. That’s so many dicks."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "For the last time, that’s not Makoto."
    mi "Hmm..."
    mi "Maybe a younger Maki then?"
    s "{i}Hah...{/i}"

    "The rest of the night carries on like this."
    "And we manage to grow a little bit closer..."

    $ renpy.end_replay()
    $ mikulust5 = True
    $ miku_love += 1
    $ miku_lust += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Miku’s lust has increased to [miku_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
