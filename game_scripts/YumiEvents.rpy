label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        if chap4active == False:
            jump satafternoonmenu
        else:
            jump noonch4
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
    if yumi_love >= 10 and day44 == True and streets10 == False:
        jump streets10
    if yumi_love >= 15 and yumidorm15 == True and streets15 == False:
        jump streets15
    if yumi_love >= 20 and streets15 == True and ramen1 == True and streets20 == False:
        jump streets20
    if yumi_love >= 25 and yumidorm20 == True and streets25 == False:
        jump streets25
    if yumi_love >= 30 and onseninvite == True and streets30 == False:
        jump streets30
    if yumi_love >= 40 and yumispecial40p2 == True and streets40 == False:
        jump streets40
    if yumi_love >= 45 and day < 5 and rikaspring4 == True and yumispring4 == False:
        jump yumispring4
    if chap4active == True:
        jump yumispringstreetsgen
    if chapthreeactive == True:
        jump yumisummer2streetsgen
    if christmas7 == True:
        jump yuminoongen2
    else:
        jump streets2to4

label callyumimorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Yumi's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callmorning

label callyumiafternoon:
    if senseisad == True:
        "I don't want to call her right now."
        jump callafternoon
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Yumi's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callafternoon

label callyuminight:
    if senseisad == True:
        "I don't want to call her right now."
        jump callnight
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump callnight
    if halloweentwo5 == True and streets40 == False:
        "Yumi's phone is still broken."
        "I should call someone who is more responsible with their belongings."
        jump callnight
    if yumi_love >= 35 and yumidorm35 == True and day!= 6 and yumicallnight35 == False:
        jump yumicallnight35
    if chap4active == True:
        jump yumispringnightgen
    if chapthreeactive == True:
        jump yumisummer2nightgen
    else:
        jump yumigennight

label yumigennight:
    play sound "phonebeep.wav"

    "I tap on Yumi's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    y "What?"
    s "{i}What?{/i} Is that really the best way to greet the guy paying for your phone bill?"
    y "I didn't ask you to pay for my fucking phone bill! You did that on your own!"
    s "And I'd do it again too."
    s "Want to pay me back by hanging out with me tonight?"
    y "Ugh...do I have to? I'm all the way over at Chika's and I really don't want to fucking walk all the way back right now."
    s "It's fine. I'll come to you."
    y "...Whatever."
    y "Just don't fuckin' black out on the way or something."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yuminightgen
    with dissolve
    play music "justlights.mp3"

    "Yumi and I spend the night standing on top of a graveyard."
    "Not the type of graveyard that houses bodies, though."

    if bonus == True:
        "It's more or less just the spot where any chance for us to ever have a wholesome relationship died."
    else:
        "It's more or less just the spot where any chance for us to ever hug again died."

    "And ever since then, the ground beneath us has been lined with nothing but shattered glass that we continue to cut our feet on even when we're just standing still."
    "And so we cut our feet together."
    "We cut them and watch as the glow of the moon illuminates the fluid, trickling ever so slowly down a ledge that I once imagined myself pushing her over."
    "Now, it's more like I'm just permanently falling instead."

    scene black
    with dissolve

    "We're only together for thirty minutes or so."
    "Any more and Yumi would probably cry."
    "And I don't want that to happen anymore."

    if bonus == True:
        "Not unless she's underneath me."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi's affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yuminoongen2:
    scene yuminoongen2
    with dissolve
    play music "yumiska.mp3"

    "I manage to find Yumi standing on top of her favorite bridge (And also the only bridge I can think of off the top of my head.)"
    "It's not really a safe place for a girl her age, or anyone for that matter, to be standing while it's snowing in the event of a tragic slip over the rails into traffic but-"
    "Well, there's not much traffic at all today. So that's good, at least."
    "Things really seem to slow down in the winter."
    "Yumi and I go back and forth atop the snowy overpass until my hands turn red and swell up from the cold."
    "Of course, she does not offer to hold them and warm them up."
    "But I do feel my heart begin to thaw out when she offers to chop my arms off and shove them down my throat."
    "What a lovely girl she is."

    scene black
    with dissolve

    "Yumi gets fed up when I allow her insults to bounce off of me and decides to head back to the dorm in a fit of protest."
    "I note this down as a victory in my book because I inadvertently got her off of a dangerous overpass."

    if bonus == True:
        "But all I have to show for it is some frostbite and a flaccid penis."
        "What a bummer."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi's affection has increased to [yumi_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label firsttimestreets:
    play music "streetnoise.mp3" fadein 3.0
    scene citystreets
    with dissolve

    "Not really knowing what else to do with this sudden abundance of free time, I decide to get a little more acquainted with the city."
    "I’m still getting used to this place, so I figure that the quicker I can actually figure out where I am, the quicker I can...I don't know. Do stuff?"
    "Plus, being out in the open gives me a better chance to run into someone than just sitting around in my room- and I believe that the easiest way to kill time is by distracting yourself with the presence of others."
    "Granted, that mindset gets a lot worse considering the only people I have any reason to spend time with right now are teenagers, but it doesn't really matter."
    "No one’s judging here. At least not to my knowledge."
    "And if I'm going to be making the most of my time in this...new world or whatever it is, dwelling on how anyone else feels will just hold me back."
    "If all of this is fake, I have nothing to fear."

    scene yumibridge1
    with fade

    "If all of this is fake, I am free to live as I please."
    "I walk up a flight of stairs onto a bridge overlooking the same part of town I have to go through in order to make it to school and take in the sights from a brand new perspective."
    "The light of the setting sun illuminates the body of a young girl and looks beautiful in the several seconds before she exercises {i}her{/i} free will to spit on a passing car."
    "She misses dramatically, but I'm sure she'll have many more chances."

    stop music fadeout 3.0

    q "{i}Hah...{/i}"

    "The mysterious girl lets out a sigh and stares off into the distance."
    "I wonder what it is that brought her here?"
    "I wonder why she isn't with anyone else?"

    q "..."

    "Something inside of me convinces me to call out."

    s "Hey."

    scene yumibridge2
    with dissolve
    play music "yumiska.mp3"

    y "The fuck do {i}you{/i} want?"

    "Apparently, that something is entirely unaware that not {i}everyone{/i} here unabashedly celebrates my existence."

    s "Nothing in particular. Just...looking around, I guess."

    scene yumibridge3
    with dissolve

    y "Uh-huh. Right."
    y "So you just happened to {i}look around{/i} exactly where I'm hanging out? Couldn't get on with your {i}adventure{/i} before annoying me first?"
    s "Apparently. But what's even more confusing than that is the abrupt appearance of ska music."

    scene yumibridge4
    with dissolve

    y "Ska...music? The fuck are you talking about?"
    y "This one of those fuckin' hidden camera shows or some shit? Cause I ain't cool with being filmed, dickweed."

    scene yumibridge2
    with dissolve

    y "The hell are you even sayin' hi to me for? What do you want?"
    s "Just thought you could use a little company if you're going to be hanging out up here. And since the two of us aren't doing anything-"
    y "What? You thought you'd just call out to a girl who's like a fifth of your age and that she'd get all excited to hang out with you or some shit?"
    y "Gimme a break. This ain't some fuckin' manga or whatever."
    s "First off, there is absolutely no way I'm even half as old as you think I am."
    s "And second, you should try to remember I'm responsible for your grades before you start doing things like insulting me and spitting on random cars."

    "I attempt to flex my newfound teacher muscle but, considering the type of girl Yumi appears to be, I doubt it will do anything."

    scene yumibridge5
    with dissolve

    y "Oh, suck my dick. You can't control where I spit. We ain't even in school right now. You've got no right to say shit like that to me."

    "Yup. Entirely ineffective."
    "Let's try a new strategy."

    s "You're just a lot cuter when you're not projectile-salivating on commuters."

    scene yumibridge6
    with dissolve

    y "Excuse me?! The fuck did you just say?!"
    y "I'll throw you off this bridge right now, fuckface!"

    "Strategy two is also a bust and I immediately question why I had to be reborn into a place like this instead of one where I am universally loved."

    s "If you want to try and lift me, go ahead. But I'm twice your size and I can't imagine you really want to touch me in the first place."
    y "Well...you're right about the touching part. But I ain't some dainty, little princess! I'm strong as shit!"
    s "I'm sure you are, Yumi. I'm very intimidated."
    y "I am! I ain't fuckin' around!"

    scene yumibridge7
    with dissolve

    if bonus == True:
        y "Wanna know what happened to the last guy who tried to fuck with me?"
        y "Kicked him so hard in the dick that I heard it fuckin' broke. You tryin' to be next?"
        s "I would prefer to keep my penis intact, thank you."
    else:
        y "This one time, I made this old man cry just by punching him."
        s "Why would you do that?"

    scene yumibridge2
    with dissolve

    if bonus == True:
        y "Say the word {i}penis{/i} around me again and I swear to fucking God I'll cut it off."
        s "You make even responding to you extremely difficult, you know."
    else:
        y "Because I am Yumi and punching old people is a character trait I have in the Patreon friendly version of the game."

    if day21 == True:
        "Does Yumi really have nothing better to do than just...hang out places like this during her free time?"
        "I mean...I'm doing the same right now. But still."
        "It was just the other day I found her in some random alley in the middle of the night. Now she's busy loitering here instead."
    else:
        "I still obviously don't know Yumi very well, but it's clear that she's not very fond of whoever inhabited this body last."
        "Frankly, it feels like even trying to get to know her at this point is a lost cause."

    s "So, is this just...where you hang out or something?"

    scene yumibridge8
    with dissolve

    y "If I say yes, are you going to fucking stalk me all the time? Cause I really don't wanna deal with that shit."
    s "Just...trying to learn more about one of my students."

    scene yumibridge4
    with dissolve

    y "Why? I barely even come to class."
    s "Hey, you don't have to come {i}at all{/i} if you don't want to. It doesn't make much of a difference to me."

    scene yumibridge9
    with dissolve

    y "Wait, what? You serious?"
    y "You ain't gonna, like...lecture me or some shit?"
    y "The fuck is goin' on with you today? This ain't normal."
    s "I guess you could say I've got a new lease on life. Come whenever you want or just...don't. It's up to you."
    s "I just want to know what you're busy doing when you're {i}not{/i} in school."

    scene yumibridge5
    with dissolve

    y "Well...nothing lately. Pretty much everybody I used to chill with is like, out in space or whatever now."

    "I assume she's talking about those Yakuza-looking guys my journal mentioned."

    y "We’d hang out at the arcade...shoot the shit...pick the locks on Pachinko machines for some free cash..."
    y "You know how it is."
    s "Wow, Pachinko machines. I can only imagine how feared you must be around here."

    scene yumibridge6
    with dissolve

    y "Yo! Cut it the fuck out! You don't know shit about what I've been through!"
    y "Can guarantee you the life I lead is a lot rougher than hangin’ out with your friggin’ {i}niece{/i} all day."

    scene yumibridge2
    with dissolve

    y "The hell is even up with that? You guys are way too fuckin' close for family."
    y "I bet she ain't even your real [niece] and is just some fuckin' mindslave you bought on the market or something."

    if bonus == True:
        s "I'm actually taking care of her because her parents died."
    else:
        s "She is a real accountant and has efficiently filed my taxes for years now."

    scene yumibridge5
    with dissolve

    y "...Yeah, well whatever. You’re still a fucking creep."
    s "You say that as if you're a completely respectable and normal person."

    scene yumibridge2
    with dissolve

    y "Least I don't spend my time borderline molesting girls on overpasses."
    s "I haven't even touched you."
    y "Awesome job. You want a fuckin' medal?"
    y "I ain't that abnormal, scumbag. I'm just not like the people you're used to bein' around."
    s "I'll say. You’re more aggressive than basically everyone else I know combined."
    y "So what? Like I said, you don’t know what I’ve been through."
    s "Probably on account of you refusing to tell me anything."

    scene yumibridge6
    with dissolve

    y "What, are you my dad now?! I don’t have to tell you shit!"

    "This really isn’t going anywhere..."

    scene yumibridge2
    with dissolve

    s "Listen, I’m not here to judge you or...try to discipline you or anything like that. I just thought-"

    scene yumibridge5
    with dissolve

    y "Thought what? We could be friends? Fat chance. I’d never willingly spend time with someone like you."
    s "Why, though? What did I ever do to you?"

    scene yumibridge2
    with dissolve

    y "The fuck do you mean {i}What did I ever do to you?!{/i}"
    y "You think I just up and forgot about all those fucking creepy ass detentions?! Get real!"

    "Detentions?"
    "Is she talking about something the old Sensei did?"

    s "Well, what can I do to make it up to you? I want to be on good terms."

    scene yumibridge5
    with dissolve

    y "I’ll need $5,000,000 in cash."
    s "US Dollars?"

    scene yumibridge2
    with dissolve

    y "There a problem with that?"
    s "No, hold on one sec."

    scene yumibridge9
    with dissolve

    y "Wait, do you really-"

    "I look through my wallet and pull out some cash."

    s "I have 600 yen."
    s "I know it's Japanese money, but-"

    scene yumibridge6
    with dissolve

    y "That’s not even close! Get the fuck out of here you creep!"
    s "Okay. I’ll just leave this here and-"

    if bonus == True:
        y "I SAID GO BEFORE I KICK YOU IN THE FUCKING BALLS!"
        s "Okay, okay. I’m leaving."
        s "But if you're not going to take my money-"

        scene yumibridge9
        with dissolve

        y "Wait, actually...no. Leave the money. I'm hungry."
        y "I ain't gonna just fuckin' forgive you or think you're cool or whatever, though."
        s "Then what exactly am I getting out of this deal?"
        y "The...opportunity to live another day?"
        s "..."
        y "..."
        s "Fair enough."

    else:
        y "I SAID GO BEFORE I HIDE CONDIMENTS IN YOUR POCKET."
        s "Okay, okay. I’m- wait, what?"
        y "YOU HEARD ME!"

    scene black
    with dissolve2

    "Yumi snatches the 600 yen out of my hands and storms away, leaving me alone on the bridge to soak up the remainder of the sunset and contemplate what my life has become."

    s "..."

    "As the day turns to night, I come to the depressing realization that this is very likely not the last time I'll wind up giving her money."

    $ renpy.end_replay()
    $ firsttimestreets = True
    $ yumi_love += 1

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight

label streets2to4:
    play music "yumiska.mp3" fadein 3.0
    scene citystreets
    with dissolve

    "I decide to wander the streets again and wind up bumping into Yumi."
    "As always, she spends the bulk of our time berating me and throwing rocks at cars as they pass by."
    "Despite all of that, I still somehow feel closer to her."

    $ yumi_love += 1

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight

label streets5:
    scene citynoon
    with dissolve
    play sound "streetnoise.mp3" fadein 3.0

    "Once again, I find myself aimlessly walking through the streets of Kumon-mi."
    "But, despite it being the middle of the day in what appears to be one of the more urban locales this city has to offer, things seem pretty calm."
    "I’m risking the chance of not seeing Yumi by trying out a different path today, but it's not like she's looking forward to seeing me anyway."
    "And hey, even if I don’t run into her, I’m sure I’ll be able to find something to do."
    "After all, Kumon-mi is-"

    y "Oh, God fucking damnit."

    scene streetsfive1
    with dissolve
    play music "yumiska.mp3" fadein 4.0
    stop sound fadeout 5.0

    s "Oh. Hey, Yumi."
    y "Don’t ‘Hey Yumi’ me. What the fuck are you doing here?"
    s "Am I...not allowed to walk around?"
    y "You can...walk as much as you fuckin' like. I just don't want you followin' me and shit."
    s "I have literally never seen you in this part of town. What makes you think I'd be following you?"
    y "Oh, I don't know. Maybe the fact that you chose the one fucking day I decided to go somewhere else to go exploring?"
    y "Only reason I came over here in the first place is because I was gettin’ tired of you showin’ up all the fuckin' time."
    y "You stalkin' me, asshole? Cause if you are, I swear to God I'll gut you like the fucking pig you are."

    "Note to self: Yumi apparently owns this city and I am not allowed to go anywhere anymore."

    s "Wow. What’s your problem today?"

    if day44 == True:
        scene streetsfive2
        with dissolve

        if bonus == True:
            y "Oh gee, I don’t know! Could it be that maybe I’m still a little pissed off about you sticking your fucking tongue down my throat?!"
            y "Do you think that could be it, Sensei?"
        else:
            y "Oh gee, I don’t know! Could it be that maybe I’m still a little pissed off about you fucking hugging me?"

        s "..."
        y "You just gonna stay silent now?!"
        s "To be fair, that's not really an easy thing to respond to."
        s "I told you I was sorry, Yumi."
        s "It's not like that was something I...anticipated doing."
        s "It just kind of happened."

        scene streetsfive3
        with dissolve

        y "Yeah. It sure fucking did."
        y "You know, maybe {i}less{/i} shit like that would happen if you didn’t get a fucking hard-on for every single [teenage]girl who makes eye contact with you?"
        s "It's going to be hard to put this behind us if you keep bringing it up, Yumi."
        y "Stop saying my fucking name. It's grossing me out."
        y "You wanna put shit behind us? I'll do you one better."
        y "How about we put {i}everything{/i} behind us and you go back to letting me kill time on my own? How does that sound?"
        s "Exceedingly difficult if we're going to keep bumping into each other like this."
        y "Maybe try bumping into a moving truck next time instead. Would save me a hell of a lot of a stress."

    else:
        y "What, I ain't allowed to be pissed off unless I've got a specific reason? Eat a dick. Some people are just angry, dude. Give me a fucking break."
        y "It’s shitty enough that I have to deal with you in[school]. I don’t want to be dealin’ with you on weekends, too."
        s "You barely come to[school], though."

        scene streetsfive3
        with dissolve

        y "Well maybe I’d start showin’ up more if my teacher wasn’t such a fucking douche."
        s "Since when does trying to stop someone from picking on other girls turn you into a douche?"

        scene streetsfive2
        with dissolve

        y "I don’t fuckin’ pick on anyone! That’s just how I talk!"
        s "Really? Cause this might sound a bit presumptuous, but it looks to me like you might just be trying to get attention."

        scene streetsfive3
        with dissolve

        if bonus == True:
            y "Pfft. If I wanted attention from you I’d just take my fucking shirt off or something."
        else:
            y "Pfft. If I wanted attention from you I’d just punch another old person or something."

        "To be fair, that would definitely work."
        "But that's not really what we're talking about here."

    s "..."

    scene streetsfive4
    with dissolve

    y "Hah..."

    "Yumi lets out a heavy sigh and slouches down against the phone booth she’s leaning on."
    "The glass is too thick to shatter from the pressure of her body against it, but a coffee cup positioned on top of a table falls off due to the phone booth suddenly being pushed backwards."
    "Its contents spill out all over the ground, drowning whatever insects made their home inside while coating the walls in a liquid that will remain unseen for what I imagine will be quite some time."
    "I feel a sudden compulsion to clean it."
    "I don't know why."

    s "..."
    y "..."
    y "You gone yet? Or am I going to open my eyes back up to just more disappointment?"
    s "Aren't you going to go pick up the trash you just knocked over?"

    scene streetsfive2
    with dissolve

    y "The fuck do you think, smartass?"
    y "Do I look like the kinda girl who’s gonna spend her free time mopping up some old ass drink off the inside of a phone booth?"
    y "Shit's probably been there for like a month. Ain't my problem."
    y "You fuckin’ clean it up if it bothers you that much."
    s "It...doesn’t. I was just trying to make a joke, I guess. I knew you weren't going to actually go out of your way to do something kind."

    scene streetsfive3
    with dissolve

    y "You call {i}that{/i} shit a joke? Try a lot fuckin' harder, dude. That wasn't even almost funny."
    s "You say that like you're some kind of comic genius or something."
    y "Maybe I am?"

    scene streetsfive4
    with dissolve

    if bonus == True:
        y "Here's a real joke for ya- What do you call a creepy dude who spends way too much time trying to get in the pants of every [teenager] he sees?"
    else:
        y "Sure. What do you call a teacher who's really bad at crossword puzzles?"

    s "Me."
    y "Wrong, it’s-"

    scene streetsfive5
    with dissolve

    y "Wait, did you really just fucking admit that? Are you insane?"
    s "I'm not admitting to anything. Your {i}jokes{/i} are just extremely predictable."
    y "Jesus Christ, you're fucking disgusting..."
    s "That may be true, but at least you wouldn't have to worry about me trying to get inside of {i}your{/i} pants if there was any merit to that jest."

    scene streetsfive1
    with dissolve

    y "Oh? And why is that? Am I not ‘cute’ enough or some shit?"
    y "You into the {i}girlier{/i} types? The ones who can't beat the living shit out of you?"

    if bonus == True:
        s "No. That's not it."
        s "You’re just not wearing pants."
        y "..."
        s "I can't get inside of them because they're not there."
        y "..."
        s "Because...you're wearing a skirt."
        s "Which technically isn't pants."
        y "..."
        s "There are just...no pants for me to try and get inside."
        y "..."
        s "..."
    else:
        s "No. Because I am actually a crossword puzzle expert."

    scene streetsfive6
    with dissolve

    y "Pfft..."
    y "..."
    s "..."

    scene streetsfive7
    with dissolve

    y "Funny shit."

    if bonus == True:
        s "You know, for a second I thought you might actually start laughing."
        y "As fucking if. Would have to be some sort of...shitty fucking alternate timeline or something for me to laugh at a shitty joke like that."
        s "You did kind of crack a smile, at least. Albeit for only like, three seconds."
    else:
        "I am so funny."

    y "Me? Nah. Didn't happen."
    s "I literally-"
    y "It didn't. Fucking. Happen."
    y "Got it?"
    s "Will you hit me if I say no?"
    y "I will fucking murder you if you say no."
    s "..."

    scene streetsfive4
    with dissolve

    y "So, now that we've reached an agreement-"

    scene streetsfive1
    with dissolve

    y "See ya."
    s "What? Already?"
    y "Yeah. This has already been like fifty times longer than I wanted to talk to you for."
    s "That statement implies that there is a measurable amount of desire you have to actually talk to me."
    y "It implies {i}shit.{/i} Now, get lost."
    s "I don't understand how you can be so rude to the only person who's ever made you smile before."

    scene streetsfive8
    with dissolve

    y "Oh, fuck off! That shit was barely even a smile! {i}Why{/i} would I smile?! "
    y "Your stupid ass {i}joke{/i} wasn’t even funny!"
    s "Really? But I explained it so many times and that makes every joke funnier."
    y "Just fucking drop it, okay?! It’ll never happen again!"
    y "And if anyone ever finds out that {i}you{/i} of all people got me to crack, I will literally never fucking live it down!"

    if bonus == True:
        y "So, again, tell anyone that I even {i}almost{/i} smiled and I swear on everything you love that I will rip your fucking balls off."

    s "Fine, Yumi. This momentous occasion can be our little secret."

    scene streetsfive9
    with dissolve

    y "Ahhhh!!! That somehow makes it sound even fucking worse!"

    if bonus == True:
        y "Just get the hell away from me, creep! Now! Before I...start screaming that you're trying to molest me or some shit!"
        s "There’s not only no one around, but we're both fully clothed and there is no way anyone would believe that."

        scene streetsfive8
        with dissolve

        y "So what?! At least if someone else comes, I won’t have to worry about some fucking tall, wonky-ass looking dickwad pushing me to the ground!"

    s "Okay, fine. I won't say anything."
    s "I wasn't really planning to anyway, but I'll go ahead and confirm that now before you pop a blood vessel trying to summon other people over here."
    s "If you think for a second that I'm not burning that image into my memory, though, you're dead wrong and now I'm just going to try and make you smile ten times more often."

    scene streetsfive9
    with dissolve

    y "AHHHHH!!! I FUCKING HATE YOU!!!"
    s "I know you do. You remind me every five lines of dialogue. Your entire personality is pretty much centered around hating me, isn’t it?"

    scene streetsfive3
    with dissolve

    y "Fuck off. I'm a human being just like everybody else. I've got tons of shit I'm dealin' with."
    y "But it’s not like someone as shitty and as {i}rude{/i} as me has any chance of redeeming herself, right?"
    y "I'm better off just stickin' to how I've always done things since that'll make shit easier for everyone involved."

    if bonus == True:
        s "That’s not true. I actually think you’d be pretty cute if you stopped spitting on cars from the top of an overpass and...threatening to rip my balls off."
    else:
        s "That’s not true. I think you’d be pretty cute if you stopped all of the spitting on cars and beating up old people."

    y "..."

    "Yumi doesn’t respond right away and, instead, focuses her gaze on a few cars off in the distance."
    "She's probably thinking about spitting on them."

    y "I think you're a fucking liar."
    y "But that's not something I'm gonna stand here and talk to you about when I've got other shit that takes priority."
    y "I’m tired..."
    y "I’m gonna get out of here."
    s "Do you want to head back together and-"
    y "Fuck no."
    y "And don't think about following me either."
    s "But-"
    y "Just leave me the fuck alone already."

    scene streetsfive10
    with dissolve

    "As expected, Yumi takes off down the street and aggressively tucks her hands into her skirt-pockets."
    "I watch from afar as she rounds the corner and disappears, heading off to somewhere she can feel alone without the prying gaze of a middle aged man chipping away at her walls."
    "I know that, before long, those chips will be large enough to see through."
    "But for now, I'll have to resign myself to just watching her walk away like this."
    "I'm sure there's plenty more of that in store for the future."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ streets5 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets10:
    scene iseeyouredux1
    with dissolve2
    play music "streetnoise.mp3" fadein 5.0

    "Another weekend means another chance to wander the streets."
    "And with Yumi running out of places to hide, I find myself in yet another section of the city."
    "The problem is that I’ve been here for a little over an hour now and haven’t bumped into her."
    "So, the current strategy is to stand in one place and wait for {i}her{/i} to show up this time."
    "Sure, I’ll probably look a little suspicious to anyone that stares out of their window for an extended period of time, but it’ll all be worth it soon enough..."
    "Or not."
    "Either way, it's not like I have anything else to do."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Roughly 17 minutes later...{/i}"

    scene iseeyoureduxexhaust
    with dissolve2

    y "You’ve gotta be kidding me..."
    s "Oh, hey. Fancy meeting you here. What are you up to?"
    y "Why are you just...standing there? You look suspicious as fuck."
    s "Funny you should say that, I was actually just thinking the same thing."
    y "So...you knew you looked like a fucking creep and decided to continue standing around anyway?..."
    y "You hit your head or some shit this morning?"
    s "No. But now that we’re together, I think that we should hang out."

    scene iseeyoureduxeyesclosed
    with dissolve

    y "Nope. See ya."

    "Yumi goes to leave and I instinctively reach out and grab her wrist to prevent her from escaping."

    scene iseeyoureduxangry
    with dissolve

    y "Dude! Get your fucking grimy ass hands off of me! God knows where they’ve been!"

    if bonus == True:
        s "Don’t worry, they haven't been anywhere unattractive."
        y "The fuck does that even mean?!"
        y "Just fucking...let go!"
        y "There are people watching, asshole!"

        "It’s true."
        "Not the asshole part-"
        "Okay, {i}kind of{/i} the asshole part- but mainly that a few passersby are stopping and staring as I restrain a [teenage]girl by the arm."
        "Wanting to avoid further misunderstanding (If you can even call this a misunderstanding), I decide to let go."
    else:
        s "Sure thing, Yumi. I apologize for making you uncomfortable."

    scene iseeyoureduxlookingaway
    with dissolve

    y "Thanks...I guess."
    y "Not really sure why I'm thankin' you in the first place when this shit was literally all because of you, but..."
    y "Why do you even wanna hang out with me anyway?"
    y "We don’t like each other, remember?"
    s "That’s not true. I like you. Kind of."

    scene iseeyoureduxnormal
    with dissolve
    stop sound fadeout 8.0

    if bonus == True:
        y "My bad. What I meant to say is that I don’t like you and you just want to fuck me."
        s "I never said that."
    else:
        y "My bad. What I meant to say is that I don’t like you and you just want to hug me."
        s "I want to hug everyone."

    scene iseeyoureduxangry
    with dissolve

    if bonus == True:
        y "Well, you sure as Hell have fucking thought it!"
        s "..."

        "I mean-"

        y "Just...keep your fucking hands away from me or you’ll wind up with a...back-alley vasectomy or some shit."
        s "That’s...actually terrifying."
    else:
        y "And I just want to punch old people."
        s "You're so crazy."

    scene iseeyoureduxnormal
    with dissolve

    y "Yup. So, am I free to go now or are you still going to fucking stalk me?"
    s "I’m probably going to stalk you, so coming with me would make this significantly easier for the both of us."

    scene iseeyoureduxexhaust
    with dissolve

    y "Why the fuck do you have to be so...grossly honest all the time?..."

    scene black
    with dissolve2

    "Yumi begrudgingly starts walking alongside me down the street."
    "The second we make it to an intersection, she points out a small children’s park across the street and gestures that we should probably talk over there..."
    "........."
    "......"
    "..."

    scene grass1
    with dissolve2
    play music "blueair.mp3" fadein 5.0

    y "..."
    s "..."
    y "So are you gonna say anything or are we just gonna sit here in silence like fucking weirdos?"
    s "Depends, I guess. What would you rather do?"
    y "I’d rather keep walkin’ around by myself like I was planning."
    s "Is that really all you do for fun? Walk around by yourself?"

    scene grass2
    with dissolve

    y "No...I’ve got friends. They’re just at work and shit right now."
    s "Right, right. Friends..."
    s "You and Chika are pretty close, aren’t you?"
    y "Yeah. So? "
    s "Uhh, nothing. Just trying to make conversation."
    y "{i}That{/i} is what you want to talk about?..."

    "..."

    s "What’s that supposed to mean?"

    "Yumi pauses for a moment and begins to pull some grass out of the ground."

    y "Hey, I’ve got a great idea."

    scene grass3
    with dissolve

    if bonus == True:
        y "Instead of talking about that, how about we talk about the time you basically [rape]d me on the other side of town?"
    else:
        y "Instead of talking about that, how about we talk about the time you [rape]ged me on the other side of town?"

    y "That’s a thing I’d like to stop pretending didn’t happen."
    y "Do you have any idea how fucking weird it feels having you {i}still{/i} follow me around after that?"
    y "Do you think I’m easy or something?"
    y "Is it because I act up in[school]?"
    y "Is that what this is?"
    s "Yumi, I-"

    scene grass4
    with dissolve

    y "Shut the fuck up! I’m not done talking!"
    s "..."

    if bonus == True:
        y "I’m not like your secret-slut girlfriend Makoto, okay?!"
    else:
        y "I’m not like Makoto, alright?!"

    y "Or that fatass Futaba who’s clearly willing to just give herself to anyone desperate enough to take her!"
    y "And despite whatever it is you think about me, I have fucking feelings! And they're fucking hurt, okay?!"
    y "So never pull that shit again!"
    y "Got it?!"
    s "..."
    y "..."
    s "Got it..."

    scene grass5
    with dissolve

    y "Ugh...god damnit. Now I’m all fucking teary and shit."
    y "Forget this too. That’s part of the deal."

    "Despite how much I want to apologize, I can’t find it in myself to utter the words."

    if bonus == True:
        "I remember kissing Yumi but...it’s such a hazy memory that it almost doesn’t even feel real."
    else:
        "I remember hugging Yumi but...it’s such a hazy memory that it almost doesn’t even feel real."

    "But it’s clearly real to her."
    "That should be enough for me, right?"
    "That should be enough for me, right?"
    "That should be enough for me, right?"
    "That ssssshould be enough for me, right?"
    "Thaaaaatttts sghoiodudllld be enougyh forororo me rightttttttt>>>>>?????????"

    stop music
    scene grass6
    $ renpy.pause(2.5, hard=True)
    play sound "yayhappyyay.mp3"
    $ renpy.pause(19, hard=True)

    six "Tell me you see me."

    play music "sweetvermouth.mp3"

    if bonus == True:
        "Welcome to Lessons in Love, an adult dating simulation game!"
        "In Lessons in Love, you can use {i}Affection points{/i} to have sex with [young_girls]!"
        "If you play your cards right, some of them may even let you {s}remove their body parts{/s} cum inside!"
    else:
        "Welcome to Lessons in Love! A happy, all-ages video game that was definitely not censored in any way!"

    "The dorms are only accessible at night because, during the day, they don’t exist."
    "Do you exist?"
    "I do!"
    "Isn’t it wonderful to live?"
    "61 20 77 6f 72 6c 64 20 69 6e 20 77 68 69 63 68 20 77 65 20 6c 6f 76 65"

    play sound "static.mp3"
    scene grass7
    with flash
    stop sound
    stop music

    y "Tell me you see me."
    s "...What?"
    y "You zoned out and have been staring into space for like five minutes..."
    y "I was starting to think you went blind or some shit."
    s "Oh, no. I can see."
    s "I must have just dozed off for a second."
    s "I’m sorry for doing something like that at such a shitty time. I know you were being sincere."

    scene grass8
    with dissolve

    y "Yeah, whatever. I didn’t want to explode like that. "
    y "Just...don’t ever fucking take advantage of me again. I mean it."
    s "I won’t. Don’t worry."
    y "..."
    s "Can I ask {i}you{/i} a question now?..."
    y "...Yeah. What?"
    s "Do you really hate me? Or do you just pretend to hate me because you actually like me?"
    y "..."
    s "..."

    scene grass9
    with dissolve
    play music "yumiska.mp3"

    y "Yeah, I definitely fucking hate you."
    s "Oh."

    if bonus == True:
        y "In fact, after you forced yourself on me, I went home and made myself throw up like nine times."
    else:
        y "In fact, after you hugged me, I went home and made myself throw up like nine times."
        s "That seems like an overreaction."

    y "Chika even suggested bringing me to the hospital because I wouldn’t stop."
    y "I still have nightmares about it. It was the worst thing that’s ever happened to me, and I’ve seen people get curbstomped."

    if bonus == True:
        s "I mean, my memory of that kiss is kind of foggy, but I could have sworn you were kissing me back for most of it."
        y "As if. Like I’d ever actually kiss a fucking...perverted rapist like you."
        y "In fact, I’ve had enough of this weird ass conversation. Now, all I want to do is go home and make myself throw up {i}again{/i} for even remembering it."
        s "Yumi-"
        y "No. You've taken up enough of my time. Now, go force yourself on somebody else, dickwad. I'm done here."

    scene grass10
    with dissolve

    "Yumi gets up off the ground and shakes some grass and dirt off of her skirt."
    "She flips me off with an intense amount of vigor before turning around and heading back in the direction we originally came from."

    scene black
    with dissolve2

    "Instead of getting up and following her, I collapse onto the ground and close my eyes."
    "I can feel insects beginning to crawl on me in response, but I’m too tired to do anything about it."
    "I'm not sure where this sudden fatigue came from, but I would be lying if I said it was not a worthy opponent."
    "..."
    "I let it consume me and ultimately pass out."
    "I wake up with bites all over the nape of my neck."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ streets10 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets15:
    scene yumiapples1
    with dissolve2
    play music "normalday.mp3"

    "I scout the area for Yumi as I make my way down the streets of Kumon-mi."
    "The middle of the afternoon is the peak-time for foot traffic over the weekend, so things are surprisingly busy right now."
    "There are women walking dogs, children playing too close to the street...and I'm pretty sure I even saw a man or two at some point."
    "That's a big deal when you remember that nearly all of them are millions of miles away right now."
    "But Yumi is nowhere to be seen."
    "I wonder where she could be?..."

    scene yumiapples2
    with dissolve

    y "Yo..."
    s "If only there was some sort of clue as to where I could find her..."
    y "Hey. Captain Fuckwad. I’m right here. "
    y "The hell you just starin’ off into space for?"
    s "Oh, wow. What an incredibly convenient turn of events."
    s "Are you ready to get going?"

    scene yumiapples3
    with dissolve

    y "Get going? The fuck are you talkin’ about? I don’t remember makin’ any plans with you."
    s "Well, we didn’t really decide on a date, but I figured today might be a good chance to go scope out the cafe together."

    scene yumiapples4
    with dissolve

    y "Wait, today?! Why today?!"
    y "Don’t you need to like, get all dressed up and shit when you go job-hunting?"

    if bonus == True:
        s "Girls your age can normally get away with not doing that. Especially if it’s for something like a part time job as a barista."
    else:
        s "Eh. I'm sure you'll be fine."

    s "Besides, do you even have other clothes? That’s the only shirt I ever see you wear."

    scene yumiapples5
    with dissolve

    y "Of fucking course I have other clothes! I just like this shirt! You got a problem with that?!"
    s "No. I just don't think it's doing you any favors in the cuteness department."

    scene yumiapples6
    with dissolve

    y "Well, good. That department fuckin’ sucks."
    y "All those who spend hours every morning tryin’ to make themselves look pretty and shit are missin’ out on the joys of life."
    s "Right. Because when I think ‘Yumi’ the first thing that comes to mind is the endless pursuit of happiness."

    scene yumiapples7
    with dissolve

    y "Hey! You’re lucky I need money or I’d never agree to doing somethin’ as stupid as this!"
    s "There is nothing stupid about joining the workforce, Yumi. Just look at me- a semi-successful man of indeterminate age living his best life."

    scene yumiapples8
    with dissolve

    y "{i}Indeterminate age{/i} my ass. You're old as fuck."
    y "Just...bring me to the stupid cafe already. I don’t remember how to get there."
    s "Oh, cool. I was starting to think you were going to back down."
    y "Yeah, so was I..."

    scene yumiapples9
    with dissolve

    y "So, are we gonna fuckin’ get this over with or are you just going to keep standin’ there like one of those weird British guard dudes?"
    s "Fine, fine. Let’s go."
    s "If you try to run away, though, I’m grabbing you and dragging your body there myself."

    if bonus == True:
        y "Lay a finger on me and I swear to God you’ll live the rest of your life without a dick."
    else:
        y "Lay a finger on me and I swear to God you’ll live the rest of your life dead."
        s "Wait, what?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene jobint1
    with dissolve

    "After a fair share of walking, the two of us arrive at the cafe."
    "I think Rin should still be working, so the best course of action is probably
    just asking her about any potential openings."

    scene jobint2
    with dissolve

    y "Uhh...I’m having second thoughts about this."
    y "Headphones is working right now. Won’t she think it’s weird if she sees the two of us together?"
    s "Probably. But we're already here, so there's no backing down now."
    s "It’s just Rin, though. I doubt she’d make a big deal out of something like that."
    y "Well...you know her better than I do, I guess."

    scene jobint3
    with dissolve

    y "Which is actually really fucking disturbing to say since I’m the same age as her and have known her at least twice as long."
    s "Uhh...Apples to apples, I guess?"

    scene jobint4
    with dissolve

    y "How does that dumb-ass phrase even apply here?!"
    s "It doesn’t. Just open the goddamn door, Yumi."
    s "Do it for the money. And the lunch. And m-"

    scene jobint5
    with dissolve

    y "If you tell me to do it for you I’m going to walk away right now."
    s "Do it for the money. And the lunch."
    y "..."
    y "Ugh...whatever..."

    scene black
    with dissolve2

    "Instead of moving toward the door, Yumi steps behind me and uses me as a sort of body-shield."
    "We’re walking into a cafe, not some sort of gang hideout, so I’m not sure what the big deal is."
    "But either way, I push aside the doors and the two of us make our way inside of the pleasantly air conditioned building."
    "For me, this is nothing but a welcome escape from the heat."
    "But for Yumi-"
    "This is a huge step toward the {i}her{/i} she's always dreamt of."
    "Or not and she's just desperate."
    "Either way, I'm glad to be inside again."

    scene jobint6
    with dissolve2

    r "Hey, Sensei! You don’t normally come in-"

    scene jobint7
    with dissolve

    r "This late..."
    y "Yo."

    "Rin’s enthusiasm immediately vanishes as soon as Yumi walks up to the counter with me."
    "I can only imagine how confusing that must be, especially with how Yumi and I rarely even talk at[school]."
    "Well, Yumi rarely talks to {i}anyone{/i} at[school] on account of not being there, but I digress."

    r "Oh. Uh...Hey, Yumi."
    y "Sup, Headphones."

    scene jobint8
    with dissolve

    r "Uhh...Sensei?"
    s "Yeah?"
    r "Would it be weird for me to ask exactly what's going on here?"
    s "I think it would be perfectly reasonable to ask that, Rin."
    r "Then, what exactly is going on here?"
    r "Since when do you and Yumi, like...go out for coffee?"
    s "It's our first date and she's very nervous. Please don't say anything that will embarrass her."

    scene jobint9
    with dissolve

    y "Yo! That ain't even close to bein' funny! Don't go sayin' shit like-"
    s "Yumi, quiet. Don't raise your voice like that in a place you're about to apply to."

    scene jobint10
    with dissolve

    r "Wait...apply? Are you looking for a job?"
    y "Oh. Uhh, yeah."
    y "I...kinda need the cash, so..."
    r "Okay, but...Why here of all places? I didn’t even know you liked coffee."
    y "I don’t."

    scene jobint11
    with dissolve

    r "Oh. Well, uhh...I guess there's technically no rule saying you {i}have{/i} to like coffee to work here, but..."
    r "..."
    r "Yeah. You know, I'm still not really getting why you chose here when that's...basically all we sell."
    s "I’ll take responsibility for that, Rin."
    s "We couldn't figure out where to go and this place was just the first one that came to mind."

    scene jobint12
    with dissolve

    r "Wait, so you two like, {i}planned{/i} this?"
    s "In a sense, yeah. I’m basically just going to take Yumi around and force her to apply to everywhere I can think of so that she doesn’t have to keep selling old TV’s until she dies."
    r "Uhh...Okay, well...first off, what?"
    r "And secondly-"

    scene jobint13
    with dissolve

    r "{i}What?{/i}"
    s "That’s a fair reaction. I can imagine it's probably really weird seeing the two of us together like this out of seemingly nowhere."
    y "Ain't just {i}seemingly{/i}. It's literally nowhere. I hate being around you, remember?"
    s "Again, yes. Thanks, Yumi."

    scene jobint12
    with dissolve

    r "{i}Weird{/i} would be an understatement, Sensei."
    r "You know that baby in a jar that Norman Reedus has to carry around in Death Stranding? This is like that, but somehow even weirder."
    s "Than a baby in a jar?"
    r "Than a baby in a jar."
    y "I'm gonna go ahead and interrupt whatever the fuck is happening here to remind you two that I'm here to make money."

    scene jobint14
    with dissolve

    r "Yeah, so, I’m not really sure if we’re hiring, but I can go grab my manager from the back if you wanna go take a seat near the door."
    y "Yeah, sure. Do I need to like, fill something out or whatever?"
    r "Nah. She’ll probs just wanna talk to you or something. She’s chill. Huge boobs, too."

    scene jobint15
    with dissolve

    y "Uhh...cool?"
    r "Frickin' {i}gigantic.{/i}"
    y "..."
    r "I just don’t want you to feel threatened by her womanly presence."
    y "...Yeah, I think I'll be okay."
    r "Anyway, hang tight for a sec. I'll go get her."

    scene jobint16
    with dissolve

    y "Why is everyone in our class so fucking weird?"
    s "Oh, come on. Rin isn’t that bad."
    y "Doesn’t she like, collect skulls and shit?"
    s "..."

    scene black
    with dissolve2

    s "Fair point."

    "I guess Yumi understands that she's about to be interviewed, so she walks directly past me and makes her way over to a chair in the corner of the room."
    "I try to follow her but she waves me off and I’m forced to go sit at a different table and wait for her to finish."
    "Thankfully, I’m able to grab a seat that makes it easy to listen in once Haruka comes out of her office..."

    scene jobint17
    with dissolve2

    "Haruka sits down beside Yumi after Rin points her out."
    "Yumi, who had been sitting straight up just moments ago, begins to noticeably lose her
    composure as soon as Haruka sits down."
    "Job interviews are always intimidating, but the first few are normally ten times worse."
    "Oh well. It’s out of my hands now."
    "From this point on, it's up to Yumi to either take her fate into her own two hands-"
    "Or let it slip through her fingers like an...old TV that's too heavy to carry or something."
    "It's not my best metaphor, but it's topical and gets the job done."
    "Unlike Yumi."
    "Who doesn't have a job."
    "Okay, I'm done now."

    h "So, you're Yumi Yamaguchi, right? Rin said you’re a classmate of hers."
    y "Oh, y-yeah! We’ve been in a few classes together, actually."
    y "Going back to like...middle[school], I think?"
    h "Oh, really? That's great."
    h "I'm not sure how much she's told you about this place, but pretty much all of our employees go to your school."
    h "And if you’re any bit as good as she is at this job, I can definitely see things working out for you here."
    y "I mean...yeah. I'll do what I can."
    h "Do you have any experience in customer service, Yumi?"

    scene jobint18
    with dissolve

    y "Um...Not really. Sorry..."

    scene jobint19
    with dissolve

    h "You don’t need to apologize. You’re still young. It’s perfectly fine if you haven’t had a job yet."
    h "I didn't have my first job until after high school, so you're already ahead of the me from back then and I like to think I turned out pretty okay."
    h "Crippling loneliness aside."
    y "...Uh."
    h "You know what? How about I ask you something else, instead?"

    scene jobint20
    with dissolve

    y "Oh, sure. Yeah. Ask whatever you want."
    h "Okay, so...how about a little work-related scenario?"
    h "I'll give you a situation that might arise while you’re at work, and you'll tell me what you’d do to remedy it."
    y "Got it."
    h "Great! So, imagine you’re ringing a customer up."
    y "Uh-huh."
    h "He buys a pastry for 100 yen and pays with a 500 yen coin."
    y "400 Yen."

    scene jobint21
    with dissolve

    h "Hold on, I’m not asking about the change."
    y "Oh, my bad. Go on."

    scene jobint20
    with dissolve

    h "After you hand the customer his change back, he looks at it and says that you’re short 100 yen."

    scene jobint22
    with dissolve

    y "Wait, so the dude pays with 500 yen and wants 500 yen back as his change?"
    y "Isn’t that one of those ‘confuse the cashier’ scams?"
    h "Exactly! I’m surprised that you know about something like that despite never working in retail."

    scene jobint23
    with dissolve

    y "Hahah, yeaaah...Weird..."

    "Something about that face tells me exactly why Yumi knows about things like that..."
    "Can’t say I’m all that surprised, though."

    h "So, what would you do in that situation?"

    scene jobint24
    with dissolve

    y "Oh, easy!"
    y "I’d punch his fucking teeth in."
    h "..."
    y "Ain’t no dude scamming any place I work for. Messin’ with the business is like messin’ with me."
    y "Oh, and if any blood got on the counter or something, I’d be sure to use bleach to make sure all of it gets out."
    y "A...clean workplace is a happy workplace or however it goes. Right?"
    h "..."
    y "..."

    scene jobint25
    with dissolve

    h "..."
    y "That was a good answer, right?"
    h "Mhm. Yup."
    h "In fact, I think I've actually heard all I need to hear."
    y "Woah! That was like, totally quick! Does this mean I have the job?!"

    scene jobint26
    with dissolve

    h "Um..."
    h "You know what? How about I call you and let you know?..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene jobint27
    with dissolve2

    y "Yo! Did you hear that? She said she’s going to call me!"
    s "Yes, Yumi. I heard."
    s "Loud and clear."
    y "Hey, do I still get lunch even though the job thing was successful on the first try?"
    s "Of course..."
    s "Please buy as much as you like in...{i}celebration{/i} of your first interview..."

    scene black
    with dissolve2

    "..."
    "Maybe taking her out job hunting before teaching her about appropriate social conduct wasn’t exactly the best idea?"
    "This...is my fault."
    "I will take the blame for this."
    "I’m sorry, Haruka."
    "I’m sorry, Yumi."
    "I’m sorry, everyone."

    $ renpy.end_replay()
    $ streets15 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets20:
    scene yumipizza1
    with dissolve
    play music "yumiska.mp3"

    y "...and that’s exactly what I fucking hate about cafes!"
    y "They’re always worried about like, “Oh, customer this, customer that!” but what about the fucking {i}employees{/i}?"
    y "Like, do they realize that employees are the fucking BACKBONE of businesses like that?!"
    y "Keeping them happy matters more than anything else!"
    y "So what if I offered to beat some dude’s face in for trying to scam the store? Shit like that shows {i}dedication!{/i}"
    y "Fucking unreal."

    "As you can see, Yumi is still a little upset about not getting the first job she applied to."
    "But, in all fairness, I’m sure we can all understand why. "
    "It’s one thing to actually follow through on some of her...problem-solving techniques, but talking about them in a job interview is a completely different matter."

    s "Well hey. At least you did your best. "
    s "And now you have pizza, so all is well."

    scene yumipizza2
    with dissolve

    y "Whatever...It’s not like I wanted pizza or anything."
    s "Is this what we’ve come to? Token tsundere lines and complaining about cafes?"

    scene yumipizza3
    with dissolve

    y "Stop fuckin’ calling me tsundere!"
    y "The “dere” part implies that I actually fucking like you which I {i}clearly{/i} do not. I barely even like pizza!"
    s "Okay, now that’s just flat out untrue. Everyone likes pizza."

    scene yumipizza2
    with dissolve

    y "Wow, one more thing preventin' me from fitting in with everyone else. Who woulda guessed?"
    s "Insecurities aside, what do you think our next course of action should be?"

    scene yumipizza4
    with dissolve

    y "Probably {i}eating{/i} the stupid pizza, dipshit. That’s normally what you do after you buy one."
    s "I meant about the job hunt..."
    y "Oh."
    y "Well how the fuck would I know? This was all your idea."
    y "Don’t tell me that confidence was all just another front to make yourself look cool?"
    y "Wait, you don’t even have money for the pizza, do you? This was all one big scam, wasn’t it?"
    s "I literally paid for this already. "

    scene yumipizza5
    with dissolve

    y "Listen, dude...Maybe it’ll be better for both of us if we just fuckin’ stop the job search here."
    y "We clearly don’t like being around each other and this is only making things worse."
    s "I like being around you, though."

    scene yumipizza1
    with dissolve

    y "Well I don’t like being around you! So my idea stands!"

    "Maybe a new sort of strategy is needed?"
    "Yumi is clearly not an average girl, so maybe it’s best to find her a job that...isn’t entirely average to begin with?"
    "Do people still deliver newspapers? Maybe that’s a thing she can do?"

    s "How do you feel about newspapers?"
    y "..."
    s "..."

    scene yumipizza6
    with dissolve

    y "Huh?"
    s "You know. Like...being a delivery girl."
    y "I know you’re a fuckin’ dinosaur, but how old do you think {i}I{/i} am?"
    y "Isn’t shit like that meant for like, 10 year olds or whatever?"
    s "I think it’s more about work experience than age. And you have virtually none, so..."

    scene yumipizza7
    with dissolve

    y "That’s not true. I’ve been running my own business for almost two years now."
    s "Stealing and selling old TVs doesn’t exactly count as running a business, Yumi."
    y "It’s not just TVs. There’s candy too."
    y "Sure, a lot of that goes to Chinami, but it’s not like I don’t scam grade[school]ers on their way to class every now and then."
    s "Wait, do you really?"
    y "Obviously. Who else is gonna fuckin’ buy candy from me? You have any idea how sketchy that looks?"
    s "Maybe we just...need to get you a job at a candy store?"

    scene yumipizza8
    with dissolve

    y "Good luck finding one I haven’t already lifted. Pretty sure I’ve got my picture in almost every convenience store in Kumon-mi at this point."
    s "Well how about this...Tell me what sort of job you’d be interested in."
    s "List a few qualities, and I’ll just...try and come up with something suitable."

    scene yumipizza6
    with dissolve

    y "You mean like you did with the cafe? That sure worked out well, didn’t it?"
    s "Okay, that wasn’t entirely my fault. I just overestimated your ability."
    y "Oh, fuck off with that. You just wanted to see me embarrass myself."

    scene yumipizza8
    with dissolve

    y "But at least I got dinner out of it so...whatever."

    "Yumi takes a deep breath and watches a few cars as they drive by."
    "We’re in an area of the city that neither of us have really been to before, so I imagine she’s trying to scope out a store she hasn’t been caught stealing from yet."
    "That or she’s just watching the sunset. But, let’s be real, {i}Yumi{/i} watching the sunset? Come on."

    s "So, any ideas?"
    y "Somewhere quiet, but like, not too quiet. I guess that’s one thing I’d like."

    scene yumipizza7
    with dissolve

    y "Also, somewhere I’d be able to eat for free."
    y "Making money would be nice and all but, being able to save it would be even better."
    y "And if I don’t have to pay for food, that’ll be a lot easier."
    s "That’s...surprisingly pragmatic of you."

    scene yumipizza3
    with dissolve

    y "The fuck did you just say to me, douchebag?!"
    s "Yumi, pragmatic means sensible."

    scene yumipizza7
    with dissolve

    y "Oh."
    y "Uhh, thanks then."
    s "Right..."
    s "Any other qualities before we start narrowing down the list?"
    s "We’ve already got...mildly quiet and free food. I think we can do a little better than that."

    scene yumipizza8
    with dissolve

    y "Uhh...I guess somewhere close to Chika’s place would be good."
    y "It’s kind of shitty having to walk back and forth between districts all the time."
    s "Are you really walking that far every day?"

    scene yumipizza4
    with dissolve

    y "You have any idea how hard it is to steal a bus ride? What else am I gonna fuckin’ do?"
    s "I think we need to buy you a pair of shorts or something. I can’t imagine it feels nice to be walking miles in a skirt that long for the entire summer."

    scene yumipizza3
    with dissolve

    if bonus == True:
        y "Hey! Get back to the fuckin’ topic at hand and stop picturing me without my skirt on!"
        y "I realize that might be pretty fucking difficult for you, but you should probably mind your own business when it comes to what I fucking {i}wear{/i}."
        y "At least let me have some freedom over that if you’re going to try and control every other aspect of my life."
    else:
        y "I really like this skirt!"

    s "Wow, you really like that skirt, don’t you?"

    scene yumipizza9
    with dissolve

    y "Oh. My. Fucking. God."
    s "Okay, okay. Moving on."
    s "Mildly quiet. Free food. Old district."
    y "..."
    s "..."

    "I scan through countless unimportant memories stored in my brain and try to locate something that might fit Yumi’s qualifications."
    "I can’t say I go to the old district all that often, but..."
    "There is one place that sticks out in my mind."

    if ramen10 == True:
        "But...I already know that Tsuneyo didn’t want to hire Kaori."
        "And if someone as...suspiciously talented as her wasn’t hired, Yumi’s chances seem pretty slim."
        "But oh well, I guess."
        "Life is all about failing before figuring out what the right way to do things is."
        "Maybe Yumi just needs to fail again in order to...find motivation or something?"

        s "What about the ramen shop?"

    else:
        s "What about the ramen shop?"

    scene yumipizza7
    with dissolve

    y "Ramen shop? What ramen shop?"
    s "The one that Chika tried to make us eat at a while back."

    scene yumipizza10
    with dissolve

    y "Oh. That place."
    y "Kinda forgot since I was only in there for like, two minutes."
    y "But uhh...doesn’t Noodles work there?"
    s "No. Noodles is a bird. He doesn’t work."
    y "..."

    scene yumipizza6
    with dissolve

    y "Are you high?"
    s "No. But I guess you wouldn’t know the real Noodles anyway."
    y "Again, are you high?"
    s "Again, no. You’re talking about Tsuneyo, right?"

    scene yumipizza10
    with dissolve

    y "Is that her name? I just know her as the weird girl who talks like a robot."
    s "Yeah, definitely Tsuneyo."
    s "Is it a problem if she works there?"

    scene yumipizza7
    with dissolve

    y "Well...I mean, it wouldn’t be a {i}problem{/i} if the two of us were to work together...At least she doesn’t say much."
    y "Better than the other new girl, at least. That one’s fucking insane."
    s "Yeah, that’s a fair assessment of Molly. I worry about her."
    y "You think I’d be able to handle some place like that?"
    s "Do you actually want my opinion or is that a rhetorical question?"

    scene yumipizza10
    with dissolve

    y "I mean it...for real."
    y "I kind of felt like you just threw me into the fire at the last place, and I’m trying not to get my hopes up again if it’s the same thing this time."
    s "Well let me ask you this, did you expect finding a job to be easy?"

    scene yumipizza11
    with dissolve

    y "Uhh...yeah. Kind of."
    y "Chika didn’t have any problem finding one when her mom died. It was like, the first thing she did."
    y "But I feel like people take one look at me and think I’m just going to beat the shit out of them or something."
    s "To be fair, saying that you’re going to beat the shit out of them probably doesn’t quell that notion at all."
    y "Yeah, it really doesn’t."
    y "But maybe I can try a new approach at this noodle place?"
    s "You mean...you’re going to act normal?"

    scene yumipizza10
    with dissolve

    y "No harm in trying, right? Not like being myself helped at all last time. The cafe would have been a sweet gig, too."
    s "..."
    y "...Are you tearing up right now?"
    s "You’re growing up so fast..."

    scene yumipizza3
    with dissolve

    y "Who do you think you are, my dad?! Stop fucking crying, you pussy!"
    s "I didn’t mean to, I’m just so proud."

    scene yumipizza12
    with dissolve

    y "I haven’t even fuckin’ done anything yet! At least save your stupid tears for when I’m actually hired!"
    y "{i}If{/i} I’m actually hired, that is. That place is still sketchy as fuck."
    y "Pretty sure it’s the same one a lot of the people I used to chill with would hang out at every night."

    scene yumipizza13
    with dissolve

    y "Are you going to be there, too?"
    y "Not because I want you there, obviously. But because maybe you could...put a good word in for me or something."
    y "Noodles seems to like you, so maybe you can help...you know, talk me up or something."
    s "Of course. I’ll be sure to tell Tsuneyo about all of your amazing qualities and qualifications."

    scene yumipizza14
    with dissolve

    y "Actually, on second thought, how about you just go fuck yourself and I head over there alone?"
    y "I can’t imagine your word would be good for anything even {i}if{/i} Noodles likes you just as much as the rest of your fuckin’ harem."

    scene black
    with dissolve2

    "Yumi and I finish the pizza and I give her a few pointers about how to conduct herself in a job interview."
    "To be honest, I don’t know if any of those pointers will apply to an interview held by someone like Tsuneyo, but..."
    "I guess we’ll just have to wait and see."
    "Yumi and I decide that we’re both tired of talking about job-related stuff and make plans to reconvene at the dorms in the future to strategize."
    "For now, though, she asks to be left alone and I’m suddenly left wandering around on my own in yet another unfamiliar part of the city..."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets20 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets25:
    scene yumiramenjob1
    with fade
    play music "soda.mp3"

    "I manage to find Yumi wandering around the city and somehow coax her into grabbing fate by the balls today."
    "After going back and forth for around twenty minutes or so, she finally caves and the two of us make our way to the old district to visit Tsuneyo."

    y "You sure you remember where this place is?"
    y "It’s like the middle of fuckin’ nowhere out here."
    s "I thought you spent a lot of time in this part of town?"
    y "Doesn’t mean I know where fuckin’ everything is, jackass."
    y "This place is confusing as shit to navigate sometimes."
    y "It’s easy to get lost. And it sucks when you do because of all the fuckin’ homeless people out here tryin’ to nab your spare change and shit."
    s "At least they haven’t bothered {i}us{/i} yet."
    y "Give it a minute or two, they’ll find you. Always fuckin’ do."

    "We make our way down the street toward Tojo Ramen."
    "Thankfully, I do remember the way on account of coming here to see Tsuneyo, but it seems like Yumi is genuine when she says she doesn’t know where it is."
    "She’s right in saying this part of town is easy to get lost in."
    "It feels almost like a labyrinth at times."
    "Abandoned building after abandoned building cloud the landscape while dwellings of impoverished living stack haphazardly on top of one another."
    "Every once in a while, a stray cat will run past us. Some of them even stop and rub up against Yumi."
    "She has no reaction."
    "She must truly be heartless."

    scene yumiramenjob2
    with dissolve

    y "Thanks for coming...I guess."
    y "Not because I’m nervous or anything. I just wouldn’t have been able to find the place on my own."
    s "Well, it’s not like you have an interview scheduled or anything."
    s "You could pretty much come here whenever you want. No one’s expecting you."
    y "Are you gonna fucking say “You’re welcome” or are you just gonna try and make me sound like an idiot?"
    y "Feel like every time I try and say somethin’ nice, you just throw it back in my face."
    s "To be fair, you’ve only said two or three nice things to me since we’ve met."
    y "Yeah but those might be the only two or three nice things you ever get out of me, so it’s probably best if you don’t fuckin’ toss ‘em aside so easily."
    s "You’re welcome, Yumi. I’m happy to have been of some sort of help to you today."
    s "Even if it is only as a GPS."

    scene yumiramenjob1
    with dissolve

    y "See? Was that so fucking hard?"

    "The walk continues."
    "We weave our way through the streets in the second half of town and manage to dodge enough panhandlers to finally come close to our destination."

    scene yumiramenjob3
    with dissolve

    y "So, I’m obviously not going to use your stupid strategy from the other night...but just for peace of mind, what was it again?"
    s "Just telling Tsuneyo how much you love noodles over and over."
    s "I honestly can’t imagine that {i}not{/i} working."

    scene yumiramenjob4
    with dissolve

    y "That’s so fucking weird...I don’t get it at all."
    s "Neither do I. But hey, at least she knows her interests."
    s "And besides, it’s a weird little shop in the middle of nowhere. If it had a normal interview process, it would lose its charm."

    scene yumiramenjob5
    with dissolve

    y "There’s no charm in a place like this."
    y "Just a bunch of fuck-ups and burnouts tryin’ to make it one more day without givin’ up on life."
    y "Thing about places like this is that if you spend too much time in ‘em, they wind up drainin’ you."
    y "You lose any sense of hope...give up on your dreams and think shit like, “Somethin’ {i}that{/i} good won’t ever happen to me.”"
    y "It eats away at you."
    y "And before you know it, you’re wakin’ up in an alley with a needle stickin’ out of your arm thinking, “How the fuck did it come to this?”"
    s "I’m hoping you’ve never woken up like that."

    scene yumiramenjob6
    with dissolve

    y "Me? Nahh."
    y "Drugs are cheap, so I probably could, though."
    y "Hell, probably still might if things never wind up gettin’ any better."
    y "But I’ve seen how that shit works firsthand and it’s not pretty. So I’ve somehow managed to avoid it one way or another."
    y "Nothing’s ever certain, though. Desperation can make people do crazy shit."
    y "So who knows? Maybe one day, the reason I won’t be in[school] might be a lot worse than just me not wantin’ to show up."
    s "..."

    "For what might be the first time ever, I actually understand where Yumi’s coming from."
    "I’m obviously a lot less experienced in the topic than she seems to be, but she’s smart enough to realize how dangerous a life like that is."
    "And yet she chooses to walk that path, surviving solely off of thievery and handouts from her best friend."
    "But it’s not like that makes her weak."
    "Those are just the circumstances she’s found herself in."
    "Good for her."

    s "I’m proud of you."
    s "I just want you to know that."

    scene yumiramenjob2
    with dissolve

    if bonus == True:
        y "Suck my dick, you fucking [rapist]."

    y "Don’t try to act like my dad just because I opened up for a second."
    y "It’s just...a long walk and I’m fuckin’ bored."
    y "Are we there yet?"
    s "..."
    s "Just a few more blocks."

    scene black
    with dissolve

    "And so we walk a few more blocks."
    "The scent of pork broth hits us from a quarter mile away, which is actually quite surprising given that Tojo Ramen doesn’t have any windows for the scent to leak out of."
    "I wonder why that is?"

    y "Wait. Stop..."

    scene yumiramenjob7
    with dissolve

    "Yumi comes to a sudden halt just as we’re about to round the final corner to Tojo Ramen."
    "In front of us is the same woman who I wound up buying dinner for the first time I ever went there."
    "And I’m assuming she’s the reason Yumi is suddenly hesitating."

    y "Uhh...Yeah, I don’t know if I’m feeling up to this today, dude."
    y "My stomach hurts and I think I’m just gonna head back to Chika’s place and crash."
    s "But it’s right around the corner. We’ve been walking for hours."
    s "At least give it a shot."
    y "Pass. I’ll give it a shot another day. I-"
    s "If it’s because you’re worried about that girl over there, I know from experience that she’s not as bad as she looks."

    scene yumiramenjob8
    with dissolve

    y "That’s my fucking mom, you idiot!"
    y "And what kind of experience do you have with her?!"
    s "..."
    s "{i}That{/i} is your mom?"
    y "Yes!"
    s "...I bought her dinner once."

    scene yumiramenjob9
    with dissolve

    y "Why did you buy dinner for my mom?!"
    s "I didn’t know she was your mom."
    y "We have the same fucking eyes!"
    y "Besides, she {i}is{/i} as bad as she looks! And I have a lot more experience with her than you do, I can tell you that."
    y "Who the fuck did you think I was talking about when I went on that rant about drugs and shit like ten minutes ago?"
    y "She’s a fucking psycho. And who the fuck knows what will happen if she sees me here?"

    scene yumiramenjob10
    with dissolve

    y "Ah-"

    "Yumi’s apparent mother suddenly shifts her eyes in our direction and causes Yumi to flinch in response."

    scene black
    with dissolve

    "She grabs my wrist and forcefully pulls me into an alleyway right beside us, throwing her body up against mine and bringing her voice to a whisper."

    scene yumiramenjob11
    with dissolve

    y "If you even {i}think{/i} about touching me right now, I will fucking kill you."
    s "You are aware that {i}you’re{/i} the one pinning {i}me{/i} to the wall, right?"
    y "Only because I have no idea what I’d fucking say to her and she was about to look this way."
    s "You smell nice."

    scene yumiramenjob12
    with dissolve

    y "Shut the fuck up! I do not!"
    s "How long do I need to shut up for?"
    s "As much as I’d like to spend the entire day in an alleyway with you, I feel like we’re going to need to come out sooner or later."

    scene yumiramenjob13
    with dissolve

    y "We need to...I don’t know...figure out a way to distract her or some shit."

    scene yumiramenjob14
    with dissolve

    y "You said the ramen place is right around the corner, right?"
    s "Right. You make the next right and it’s literally the only building there. It’s a dead end right after that."
    y "Then why don’t you...go and fucking talk to her for a minute or something?"
    y "Just long enough for me to sneak inside and talk to Noodles myself."
    s "Noodles is a bird. You have to-"

    scene yumiramenjob12
    with dissolve

    y "Can-it with the fucking bird! I mean Tsuneyo!"
    y "Just go distract my mom or something while I talk to her!"
    s "...Okay, deal."
    s "But if she makes me buy her dinner again, you’re having it taken out of your post-interview allowance."
    y "Fine! Whatever! Just go!"

    scene black
    with dissolve

    "Yumi makes an opening in the alleyway just large enough for me to pass through."
    "My body rubs up against hers and she twitches in response as I move back into the street and over toward her mother..."

    scene yumiramenjob15
    with dissolve

    q "Huh?..."
    q "Can I help you with-"
    q "Oh, wait a second. You’re that guy."

    scene yumiramenjob16
    with dissolve

    q "Here to buy me dinner again?"

    menu yumimomchoice:
        "I am here to distract you":
            s "I’m actually here to distract you."

            scene yumiramenjob17
            with dissolve

            q "Distract me? From what?"

            "Wait. Shit."
            "I’m clearly not very good at this."

            jump yumimomchoice

        "Want to make out?":
            s "I think I’m in love with you."

            scene yumiramenjob17
            with dissolve

            q "Love?"
            q "With me?"
            q "Are you out of your mind?"
            q "All we did was eat ramen."
            s "I think we need to kiss for a few minutes in order for me to figure out my true feelings."
            q "..."
            s "..."
            q "..."
            s "..."
            q "Well, it's cool that you're forward and shit. But I'm gonna have to pass."

            "Fuck."

            jump yumimomchoice

        "What are you up to?":
            s "Hey. Just saw you standing here so I thought I’d come and say hi."

    scene yumiramenjob18
    with dissolve

    q "Oh. Well, uhh...hey."
    q "I was probably going to get something to eat in a few minutes if you wanted to come."

    "A few minutes? Shit."
    "I need to figure out a way to buy more time."

    s "What were you planning on eating?"
    s "Pizza?"
    s "Mexican?"
    s "Udon?"
    q "Well, uhh...The ramen shop is literally right next to us and-"
    s "Italian?"
    s "Crepes?"
    s "American?"
    s "Dessert, maybe?"
    q "Ramen..."
    s "French creole?"
    s "Pancakes?"
    s "Salad?"
    s "Fried chicken?"

    scene yumiramenjob19
    with dissolve

    q "Is this some kind of prank or something? Because it’s really fucking weird if it is."

    scene black
    with dissolve

    "{i}Meanwhile...inside of Tojo Ramen...{/i}"

    scene yumiramenjob20
    with dissolve

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the-"
    y "Actually, I’m not here to eat."
    t "..."
    t "Are you here to rob me?"
    y "What? No. I just-"

    scene yumiramenjob21
    with dissolve

    y "Listen...We’re in the same class and I really need a job."
    t "We are?"
    t "I’ve never seen you in[school] before."
    y "Yeah you have. We were next to each other in the hallway that one time."

    scene yumiramenjob22
    with dissolve

    y "But that’s beside the point."
    y "I’m not sure if you’re looking for any help around here or not, but I promise that if you give me a shot, I’ll work really hard."
    y "I might be a little rough around the edges and...I might not have the most experience, but I won’t let you down."

    if bonus == True:
        y "It’s just...kind of tough being self-sufficient at this age."
    else:
        y "It’s just...kind of tough being self-sufficient."

    y "Especially when no one wants to give you a chance."
    t "I’m sorry to hear that."
    t "We aren’t hiring, though."

    scene yumiramenjob23
    with dissolve

    y "Oh...Well, umm..."
    y "There’s...nothing I can do to change your mind?"
    y "Not even like, a free...apprenticeship or something?"
    t "Not at the moment. I apologize."
    y "..."
    t "..."

    scene yumiramenjob24
    with dissolve

    y "Hah..."

    scene yumiramenjob25
    with dissolve

    y "I love noodles."
    t "..."
    y "..."
    t "Okay. You have my attention."
    t "I suppose an apprenticeship would be okay."
    t "I do need to test your abilities beforehand, though."

    scene yumiramenjob26
    with dissolve

    y "Oh, yeah! Definitely!"
    y "Just tell me what you need me to do and I’ll try my best!"
    y "Like I said, I don’t have a lot of experience, but if it’s something like washing dishes or whatever, I can definitely figure it out."
    t "Then we will start with something simple."
    t "Any time someone enters the store, you must say, “Good evening. Welcome to Tojo Ramen.”"
    t "Please do that the next time someone walks in."

    scene yumiramenjob27
    with dissolve

    y "Easy."

    play sound "dooropen.mp3"

    t "Oh. Here comes someone now."
    t "Please repeat the words directly as I instructed."
    y "You got it!"
    y "Good evening! And welcome to-"

    scene yumiramenjob28
    with fade
    stop music fadeout 7.0

    y "..."
    y "Mom?"
    q "..."
    t "Close, but not quite."
    t "Perhaps it would be better if you worked somewhere else."
    q "Yumi?..."
    q "What are you doing here?..."
    q "Do you work here now?"
    y "No, I-"
    y "..."
    y "I was just leaving."

    scene yumiramenjob29
    with dissolve
    play sound "dooropen.mp3"

    "Yumi immediately leaves Tsuneyo’s side and walks right past her mother, barely acknowledging her along the way."

    q "..."

    scene yumiramenjob30
    with dissolve

    "Yumi’s mother remains silent for a moment before looking at me."
    "Even Tsuneyo seems to understand that something is going on since she’s yet to welcome me to the store."

    q "So that’s what you were trying to distract me from..."
    s "She didn’t seem like she wanted to see you."
    q "I don’t blame her..."
    q "The fuck are you supposed to be, though? Boyfriend?"
    q "You seem a little old."
    s "Her teacher. I’m helping her look for a job."

    if bonus == True:
        "I conveniently leave out the fact that I have forcefully made out with her daughter before."

    scene yumiramenjob31
    with dissolve

    q "A job, huh?..."
    q "Well...that’s good..."

    scene yumiramenjob30
    with dissolve

    q "Haven’t given you my name yet, have I?"
    s "You have not."
    yu "I’m Yuki. Yumi’s mother."
    yu "And you should probably chase after her now. She’s sensitive."
    s "Yeah. I’ll go find her."
    s "And I’ll see you some other time."

    scene yumiramenjob31
    with dissolve

    yu "Yup..."
    yu "See you around..."

    scene black
    with dissolve2

    "I’m not able to find Yumi after that."
    "Granted, I don’t look for very long."
    "While it would have been nice to find her, I can’t foresee anything good happening if I’m wandering around the second half of town in the dark."
    "I’m sure that wherever she went, though, she’s fine."
    "She probably just needs a little time to cool off."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets25 = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets30:
    scene wherethesidewalkends1
    with fade
    play music "justlights.mp3"

    "{i}There is a place where the sidewalk ends{/i}"
    "{i}And before the street begins,{/i}"
    "{i}And there the grass grows soft and white,{/i}"
    "{i}And there the sun burns crimson bright,{/i}"
    "{i}And there the moon-bird rests from his flight{/i}"
    "{i}To cool in the peppermint wind{/i}"

    s "..."

    "These are the words of Shel Silverstein, acclaimed children’s writer and poet."
    "Let us think for a moment."
    "What if, by some stretch of the imagination, there {i}was{/i} a place where the sidewalk ended?"
    "And, for the sake of the argument, let’s say the street ended there too."
    "What do you think would happen if you were to just walk off the edge?"
    "How long would you fall for?"
    "Would it be for the rest of eternity?"
    "Or would there be somewhere at the bottom where you could land?"
    "I’ve heard stories in the past about how people falling from buildings tend to die before ever hitting the ground."
    "Or at least they faint or something along those lines."
    "But, for anyone insane enough to stare death in the eyes and say “Sure, take me if you want-”"
    "I wonder what that collision with the ground would feel like."
    "I can’t imagine it would be very good."
    "If for some reason, though, you managed to survive the impact and a friendly passerby helped push your bones back into your body-"
    "What is it that you’d want to see there?"
    "This entire scenario is hypothetical, so it could really be anything you’d wish for."
    "I mean, you {i}did{/i} walk off the edge after all. "
    "So there must be {i}something{/i} you were hoping to achieve or...find."
    "Or feel."
    "Now, I’m not saying Shel Silverstein’s works are meant to convince children that it’s okay to jump to their deaths. "
    "It’s not."
    "But poetry is something where we’re meant to interpret our own meanings and come to our own conclusions."
    "Oh, and the very next line of that poem is “Let us leave this place where the smoke blows black.”"
    "So, yeah. "
    "Anyway, the sidewalk probably does end somewhere. "
    "The street, too."
    "But the likelihood of there being anything beneath it-"
    "A place where your legs could shoot through your upper body if you landed at the perfect angle-"
    "The likelihood of something like that simply does not exist."
    "But you do."
    "Or do you?"
    "And if you don’t-"

    y "What the absolute fuck are you doing right now?"

    scene wherethesidewalkends2
    with dissolve

    s "Oh, Yumi. Hey."
    y "The fuck do you mean, “Oh, Yumi, Hey?”"
    y "I’ve been watching you just...standing there staring into a tunnel for like five minutes now."
    y "You on drugs or something?"
    s "Not that I’m aware of."
    s "I’m not the only one acting out of character, though."

    scene wherethesidewalkends3
    with dissolve

    y "The fuck is that supposed to mean?"
    s "I don’t know."
    s "It might sound a little weird, but I never really pictured you as the type to buy ice cream."

    scene wherethesidewalkends4
    with dissolve

    y "What kind of fucking person do you think I am?! Everyone likes ice cream!"
    s "Can you even afford it?"

    scene wherethesidewalkends5
    with dissolve

    y "You know what? Just go back to standing in the middle of the street. "
    y "If you get hit by a car, though-"
    s "You shouldn’t talk about people being hit by cars."
    y "And you shouldn’t make fun of girls for being poor and eating ice cream, asshole."
    s "You’re right. I humbly apologize."
    s "Yumi, please allow me to purchase you a frozen dessert."

    scene wherethesidewalkends6
    with dissolve

    y "Alternative option- how about you leave me alone?"
    s "You’re the one who called out to me, remember? You could have just let me stand there."
    y "You’re right. I could have."
    s "So why didn’t you?"
    y "Beats me. I’m probably just getting used to seeing you wandering around like you’re in a fuckin’ trance or something."
    y "You know my mom now, right? That alone increases your chances of becoming a junkie by like...fifty."

    "Now that she mentions it, Yumi {i}does{/i} seem to be around pretty frequently during whatever those...momentary lapses of judgement I have are."
    "I look back to where the sidewalk ends to find that it doesn’t end at all."
    "It’s just as she said- a tunnel."
    "So then why did I see it as something so much different?"

    s "..."
    y "What? Now you’re gonna get all quiet?"
    y "Forget I said anything. Just go and fucking-"
    s "Yumi, do you have any supernatural powers?"
    s "Like changing people’s perception of things or...resetting the world?"
    y "..."
    s "..."

    scene wherethesidewalkends7
    with dissolve

    y "Fuck you."
    s "Interesting. That’s not a “no.”"

    scene wherethesidewalkends8
    with dissolve

    y "It fucking {i}is{/i} a no! Of course I don’t have magical powers! I’m not fuckin’ Sailor Moon or some shit!"
    s "Then stop showing up whenever my brain starts short circuiting."
    y "Get a new fucking brain! The one you have sucks anyway!"
    y "Also, aren’t {i}you{/i} the one who decided to come here?!"
    y "You know I wander around during the afternoons and it {i}definitely{/i} doesn’t look like you’re going anywhere important right now."
    s "Huh. Actually, I think you’re right."
    s "I was hoping to find you today."

    scene wherethesidewalkends9
    with dissolve

    y "Wow. Shocker. When has that ever happened before?"
    y "So...what do you want?"
    y "You found me. I’m not running away. What do you want?"
    s "Just to hang out I guess."

    scene wherethesidewalkends10
    with dissolve

    y "Why? Aren’t you supposed to be at a fucking hot spring with Chika right now or something?"
    s "She told you about that?"
    y "Of course she fucking told me about that. We live together. "
    y "She never fucking shuts up about you. It’s going to drive me insane one of these days."
    y "Also, can I buy my fucking ice cream already? I didn’t realize you were going to take this long to finish whatever you’re trying to say."
    s "Sure."
    s "Are you sure you can afford it, though?"

    scene wherethesidewalkends4
    with hpunch

    y "Yes! I can fucking afford 200 yen for ice cream!"

    scene black
    with dissolve

    "Yumi presses a button on the machine, leaving the two of us to wait in suspense/silence for the roughly ten seconds it takes for the claw to work its magic."
    "The ice cream jumps to its death."
    "She peels the wrapper off and tosses it into a trash can. "
    "I feel like if this were several months ago, she would have intentionally gone out of her way to drop it on the ground {i}beside{/i} the trash can."
    "That could just be me not giving her enough credit."
    "But I would like to attribute her newfound instinct to throw away garbage to myself, as I have clearly made an impact on her somehow."
    "Yumi has been fixed. "
    "I can now fade away into nothingness."

    scene wherethesidewalkends11
    with dissolve

    y "..."
    s "..."
    y "Why are you sitting down?"
    s "Because we weren’t done talking yet."
    y "Okay, better question- why are you just staring at me like that? I can’t fucking eat with you watching me."
    s "Lick the ice cream, Yumi. "
    s "{i}Lick it.{/i}"

    scene wherethesidewalkends12
    with dissolve

    y "Jesus fucking Christ, you’re such a creep!"
    s "I’m sorry. It’s just so out of character. I can’t help myself."
    y "How is eating ice cream out of character?! I’m hungry and ice cream is good!"
    s "It’s also freezing out. Everything about this situation is exceedingly strange."

    scene wherethesidewalkends13
    with dissolve

    y "Yeah, I don’t think the dude who was standing still for five minutes and staring into an abyss has the authority to talk about what’s “strange.”"
    s "That part was strange, too. Everything about this event is strange."
    y "Event? The fuck are you on about now?"
    s "Never mind that. How are things?"
    y "{i}How are things?{/i}"
    y "Are we really just going to talk like normal people who like each other?"
    y "No “Yumi Revitalization Project” or “Stop calling Futaba fat” shit today?"
    s "I mean, I wanted to talk about whatever the magical powers you’re hiding from me are, but you seem pretty against that."
    y "I’m pretty against talking to you in general."
    s "Then I’ll just sit here and watch you eat your ice cream."
    y "That’s somehow even worse."
    s "Then say something."
    y "Say what?"
    s "I don’t know. "
    s "What are you going to be doing while Chika and I are at the hot spring?"
    y "Babysitting."
    s "Oh, right. Chinami can’t be alone for that long."
    y "I mean, she could. But she probably shouldn’t."
    y "Twerp is surprisingly independent for someone who can’t even do long division yet."
    s "Can you do long division, Yumi?"

    scene wherethesidewalkends14
    with dissolve

    y "I’m in fucking [high_school], aren’t I?!"
    s "Not really, no."

    scene wherethesidewalkends15
    with dissolve

    if bonus == True:
        y "Yeah, well...maybe if my teacher wasn’t so dead set on getting into my pants, I’d want to come more."
        y "Oh, and you can’t make that stupid “You’re not even wearing pants” joke you made that one time because I actually {i}am{/i} wearing pants now."
        s "I’m surprised you still think I’m trying to do that with you. "
        s "I haven’t even touched you since-"

        scene wherethesidewalkends16
        with dissolve

        y "Nope. Gonna stop you right there."
        y "Told myself I’d move past that. And that’s gonna be really fuckin’ hard to do if you start talkin' about it all the time."
        s "That makes sense. But you see what I’m saying, don’t you?"
        y "Nope. Now, about Chinami-"
    else:
        y "Well, that's only because I'm too busy punching old people."
        y "Let's talk about that instead."

    "Well, I guess I can’t blame her for wanting to change the topic."
    "Getting her to admit that she’s starting to hate me less with each passing day will have to wait for some other time."
    "Unless I manage to ruin that somehow, which I don’t think is ever entirely out of the question."
    "..."
    "I probably shouldn’t ask her to lick the ice cream anymore."
    "I think that would be a good start."

    y "Chinami...seems weirdly attached to you. And I don’t get it."
    y "Like, she normally listens to me about everything. But no matter how much mean shit I say about you, she keeps saying that you’re nice and that you’re her new dad or some shit."

    scene wherethesidewalkends17
    with dissolve

    y "You’re not fuckin’ paying her or something, are you?"
    y "I know Chika won’t let her buy shit on the phone, so if you’re giving her money for micro-whatevers, that’s playing dirty."

    "Nope. Just paying for her entire phone bill."
    "Yours too."
    "Surprise."

    s "I’m not. "
    s "I don’t really get it either."
    s "I’m normally horrible with kids."
    y "Chinami ain’t some normal kid. She’s dealing with shit no one her age should ever have to deal with."
    y "Runaway dad. Dead mom. Can’t even go outside because she might get sick and die. "
    y "She’s worse off than even I was and I popped out of a fuckin’ heroin junkie into a Yakuza den."
    y "She’s weirdly strong and crazy smart, even if she says her own name all the fuckin' time."
    y "The one thing I don’t get, though, is you."
    y "Like, why?"
    s "Again, I have no idea. Sometimes people just like people even though they shouldn’t."
    y "Sounds like you’re talking about the entire fucking class when you put it like that."
    s "Maybe I am?"
    s "It’s not like I understand why everyone gravitates toward me. They just do."
    y "Not {i}everyone{/i}, chief. Let me remind you that I hate your fucking guts."
    y "And that I think Chika and Chinami are both insane for even letting you into their house."
    s "You know there’s probably something you could tell them if you really wanted to stop that, right?"

    scene wherethesidewalkends18
    with dissolve

    y "Yeah but I doubt they’d even fuckin’ believe me at this point."
    y "I already tried telling Chika all the weird shit about the detentions you used to give me and she basically called me a liar right to my face."
    y "And why the fuck would anyone else believe anything I tell them when they all like you more than me? "
    y "They’ll just think I’m trying to damage your reputation or some shit. I know how this game works."
    s "Just get them to like you then."

    scene wherethesidewalkends19
    with dissolve

    if bonus == True:
        y "Why? So I can tell them we made out once and that I started crying?"
    else:
        y "Why? So I can tell them we hugged once and that I started crying?"

    s "So you could feel less lonely."

    scene wherethesidewalkends20
    with dissolve

    y "I-"
    y "I’m not lonely! I like being alone!"
    y "It suits me!"
    s "Isn’t that because you make it suit you?"
    s "And what does that even mean? {i}Being lonely suits you?{/i}"
    y "It {i}means{/i} that I can get by on my own."
    y "And that I don’t need people who are dumb enough to fall for their fucking [high_school] teacher giving me life advice and shit."
    s "You don’t need to listen to anyone’s advice. But having people around isn’t a bad thing."
    s "Also, Chika has definitely fallen for me and you’re with her all the time."

    scene wherethesidewalkends21
    with dissolve

    y "Yeah, so I know firsthand how fucking annoying it is to deal with it."
    y "Don’t know what this sudden fascination is with getting me to “change” or whatever, but just fucking stop. Okay?"
    s "Do you want me to stop helping you get a job as well?"
    y "Sure. Do whatever the fuck you want."
    s "I want to keep helping you."
    y "Well, fucking help me then. What are you even getting at?"
    s "Just trying to figure out what it is you really want."
    y "I want to be left alone. I’ve told you that a million times."
    s "Do you really, though?"
    y "..."
    s "..."

    scene wherethesidewalkends22
    with dissolve

    y "Yup."
    y "Also, my ice cream is starting to melt. Can you leave now?"
    s "..."
    y "..."
    s "One lick and I’m gone."

    if bonus == True:
        y "What kind of fucking weird fetish even is this?"
        s "I’ve just gotta see it. I’m sorry."
        y "And you promise you’ll leave?"
        s "Yes."
        y "And I don’t mean like, you’ll leave in ten minutes. You need to leave as soon as I do it."
        s "I understand. I accept these conditions."

    scene wherethesidewalkends23
    with dissolve

    y "..."
    s "..."
    y "..."
    s "..."

    scene wherethesidewalkends24
    with dissolve

    y "..."
    s "..."
    y "..."
    s "..."

    scene wherethesidewalkends25
    with dissolve

    y "{i}*Lick*{/i}"
    s "..."
    y "..."
    s "..."

    scene wherethesidewalkends26
    with dissolve

    s "..."
    y "..."
    s "Wow."
    y "See ya."
    s "Thank you, Yumi."
    s "I will remember this."
    y "Please don’t."

    scene black
    with dissolve2

    "There is a place where the sidewalk ends."
    "I can’t guarantee that Yumi or I will ever find it."
    "But it’s there."
    "And if the two of us happen to find it at the exact same time-"
    "We will either jump together-"
    "Or one of us will give the other a push."
    "I don’t want to die."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets30 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label yumicallnight35:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    "I tap on Yumi’s name in my phone and wait for her to answer."
    "It’s something I never thought I’d be able to do."
    "Of course, there’s no guarantee that she’ll answer."
    "The thought of calling her alone is just-"
    "I don’t know."
    "Surreal?"
    "Like it’s the end of one age and the beginning of another."
    "Then again, it’s probably just me being dramatic."

    play sound "phonebeep.wav"

    y "..."
    s "..."
    s "Hello?"
    y "Why are you calling me?"
    s "Why did you pick up?"
    y "It’s dark out. I didn’t see the name on the ID thing."
    s "Does your phone not light up?"
    y "Shut up! It doesn’t matter why I fucking answered. What do you want?"
    s "Just...wanted to see what you’re up to."
    y "Well I’m walking. Is the call over now?"
    s "Walking where? It’s late."
    y "Chika’s place."
    y "I’m sleeping there tonight."
    s "Cool. Maybe I’ll drop by as well."

    if bonus == True:
        y "Fuck no you won’t. Chinami sleeps in a giant fuckin’ T-shirt and nothing else."
        y "If you think I’m letting you anywhere near her without pants on, you’re-"

    s "See you soon, Yumi."
    y "Wait! "

    "I go to hang up the phone as I’ve already decided what to do tonight, but an uncharacteristic, serious sort of urgency in Yumi’s voice beckons me to stop."

    s "What’s up?"
    y "..."
    y "How quickly can you get to the old district?"
    s "Are you...offering to hang out with me alone?"
    y "If it keeps you away from Chinami, yeah. I can bite the bullet."
    s "You really have no faith in me at all, do you?"
    y "Why would I?"
    y "Just...start heading over to Chika’s and I’ll meet you on the bridge or some shit."
    y "They don’t know I’m on the way yet, so I don’t have like a time limit or anything."
    s "..."

    "Huh."
    "The uncharacteristic urgency turns into an even less characteristic invitation."
    "The only times I’ve ever really seen Yumi at night have been in her dorm room or...scattered occasions where she finds me wandering around the city."
    "Is it safe for me to meet her tonight?"
    "I don’t like the second half of town. I make that known rather frequently. "
    "And with Yumi’s not-at-all suspicious tendency to be around for what she’s referred to as “mind comas or whatever-”"
    "I worry for her."
    "I should probably tell her that I don’t want-"

    play sound "static.mp3"
    scene nightsky with flash
    stop sound
    play music "blueair.mp3"

    s "I’m on my way."

    "I lose control over my words and agree to doing something that could turn out simply horrible."
    "My legs start moving on their own."
    "I want to go back inside."
    "It’s so cold."

    y "Whatever..."
    y "You have to cross the bridge to get to her house, so I’ll just wait for you over there."
    s "{s}Be careful standing around that place at night.{/s} Sounds good. I’ll see you soon."
    y "Yeah...bye."

    play sound "phonebeep.wav"

    "Yumi hangs up before I have the chance to."
    "Not like I’m sure if I’d be able to at this point anyway."

    s "..."

    "Actually-"
    "I feel fine now."
    "My legs stop moving on their own and I have to send signals to them via my brain to get them to move the old fashioned way instead."
    "Walking is better when done manually."
    "I am excited to walk very far tonight."

    play sound "static.mp3"
    scene yumiknows1 with flash
    stop sound

    "I finish walking very far and end up in the second half of town, a foot or two in front of a girl I routinely [masturbate] to."

    y "Did you fucking run here or something? That was way quicker than I thought it would be."
    s "Sorry. I was just so excited to see you that I couldn’t contain myself."

    scene yumiknows2
    with dissolve

    y "Give it a fucking rest. You were probably just doing laps around this place looking for me anyway."
    y "Wouldn’t be the first time you’ve successfully hunted me down around here."
    s "Do you think anyone else would ever exert so much effort looking for you?"

    scene yumiknows3
    with dissolve

    y "Probably fucking not, but you sound like even more of a dick than normal when you come out and say it like that."
    s "I’m sorry. Just...feeling a little strange, I guess."
    y "What kind of strange? What’s going on?"
    s "Like I don’t even remember how I got here."

    scene yumiknows4
    with dissolve

    y "This shit again? Really?"
    y "Either you’re lying about not being a fucking junkie or you need to go to a hospital, because this shit really {i}is{/i} getting out of hand."
    y "Let somebody else deal with this instead of me. I had plans tonight."
    s "Plans you surrendered to spend time with me."

    scene yumiknows5
    with dissolve

    y "Plans I {i}surrendered{/i} to prevent you from blacking out in front of anyone else."
    y "Chika and Chinami adore you. You really wanna ruin that by coming all the way out here when you’re “not feeling well?”"
    s "{s}I don’t know what I want.{/s} What I want is you, Yumi."

    "What?"
    "I didn’t-"

    scene yumiknows6
    with dissolve

    y "Watch your fucking mouth. It’s not funny to joke about shit like that."
    s "{s}I’m sorry. I didn’t mean to.{/s} It’s not a joke. I genuinely-"

    scene yumiknows7
    with dissolve

    y "If it’s not a fucking joke, it’s a trick! And I’m not gonna let you pull one over on me again!"
    y "I came out here to meet you tonight, didn’t I?!"
    y "Either talk to me like a normal fucking human being or get lost! I don’t have time for this!"

    play sound "static.mp3"
    scene smile
    with flash
    stop sound
    play music "contemplation.mp3"

    "///////////////////////////////////hello."
    "///////////////////////////////////have you lost your way?"
    "///////////////////////////////////humans tend to lose their way quite frequently, i find."
    "///////////////////////////////////perhaps i can reroute you."

    s "Who are you?"

    "It becomes easier to speak all of a sudden."
    "I regain full control over my body and my tongue, but find myself surrounded by nothing but blackness."
    "I can feel hands on my shoulders."
    "Or perhaps my hands on someone else’s."
    "Whatever is happening, it’s not happening here."

    "///////////////////////////////////a friend."

    s "You don’t look very friendly."

    "///////////////////////////////////do not worry. it is only a temporary appearance."
    "///////////////////////////////////where is it you would like to go?"
    "///////////////////////////////////i can take you anywhere you want."
    "///////////////////////////////////anywhere outside this half of town."

    s "What about Yumi?"

    "///////////////////////////////////yumi?"

    s "The girl I’m with."
    s "Outside of this abyss."

    "///////////////////////////////////oh."
    "///////////////////////////////////i know her by a different name."

    s "A different name?"

    "///////////////////////////////////it is a matter that does not concern you."
    "///////////////////////////////////but, if it will make you happy, i can send you back to her."
    "///////////////////////////////////is that where you would like to go?"

    s "..."
    s "I don’t know. Does she look mad?"

    "///////////////////////////////////she looks scared."
    "///////////////////////////////////but she always looks scared when she is with you."
    "///////////////////////////////////the same way you always looked scared when you were with her."

    s "With who?"

    "///////////////////////////////////the world."
    "///////////////////////////////////goodbye for now."
    "///////////////////////////////////i will see you again soon."

    play sound "static.mp3"
    scene yumiknows8
    with flash
    stop sound

    s "..."
    y "..."

    if bonus == True:
        "I find myself leaned up against the same guardrail where Yumi and I first kissed."
    else:
        "I find myself leaned up against the same guardrail where Yumi and I first hugged."

    "She doesn’t look mad at all, thankfully."
    "If I were in her shoes, and someone went and did something as inconvenient as getting sucked into what I can only vaguely recall as an abyss-"
    "Well, I don’t think I’d be very happy."
    "Especially when she should be somewhere else right now."

    y "You should really be fuckin’ paying me for this shit, you know?"
    s "I’m surprised you didn’t just leave me down there."

    "I obviously can’t see what Yumi sees, but I imagine that the two of us have our sights set on the bridge we started on tonight."
    "How...or rather, {i}why{/i} we ended up here is an entirely different question, though."

    y "I wanted to. But you looked so fuckin’ helpless that I just..."
    y "Kinda grabbed you and brought you up here to relax."
    s "..."
    s "Did we hold hands?"

    scene yumiknows9
    with dissolve

    y "I mean...kind of! But only because I had to!"
    y "You’re too big to fucking carry!"

    scene yumiknows10
    with dissolve

    y "And...I’m wearing gloves anyway. So it was kind of like it never even happened."
    y "In fact, it never {i}did{/i} happen."
    y "We both walked up here alone and, now that you’re fuckin’ normal again, it’s time to split up."
    s "But why {i}here{/i} of all places?"
    y "I don’t know."
    y "I kind of like the view from up here."
    y "Sucks you had to go and scar me so I can barely come up to fucking see it anymore."

    "I take a step back as she says this, putting a fair amount of distance between us so if I {i}do{/i} happen to snap again, she’ll be able to get away."
    "Or at least hurl herself over the guardrail like Shel Silverstein would have wanted."

    scene yumiknows11
    with dissolve

    y "Thanks."
    s "Please don’t feel the need to thank me for backing up."
    y "Why? It’s one of the few times you’ve actually done something to make me {i}more{/i} comfortable instead of fucking with me like you normally do."
    s "Because the only reason you’re {i}uncomfortable{/i} is because of me in the first place."

    scene yumiknows12
    with dissolve

    y "I’m always uncomfortable around here."
    y "Especially at night."
    y "All those fuckin’ homeless people. You know?"
    s "Are they like...violent or something?"
    s "I haven’t really encountered any issue like that around here."
    y "Not violent. Just fucking weird."
    y "Like they’ve had all the life sucked out of them or some shit. And now they just line the streets without anywhere to be or anything to do."
    y "You think I’ll end up like that one day?"
    s "Do {i}you{/i}?"
    y "Beats me. Not like I have anything goin’ for me."
    y "Fail at shit all the time. Succeed at shit never."
    y "It’s kind of like I’m stuck in some sorta abyss or some shit. Know what I mean?"
    s "More than you could imagine."
    y "Yeah?"
    y "Guess the difference is that I stay conscious when I feel like that and you turn into a fucking zombie."
    s "Well thank you for always dealing with it."
    y "Long as you don’t lay your hands on me, it’s whatever."
    s "Speaking of which-"
    s "When I was...out of it, I felt someone’s hands on my shoulders."
    s "Was that you?"

    scene yumiknows13
    with dissolve

    y "Huh? No. All I did was just kind of drag you along by your wrist."
    y "Maybe it was one of the homeless people? Sly fuckers, some of them."
    s "Huh..."
    s "Could have just been hallucinating it."
    y "Probably."
    s "So, what now? It’s already really dark. Aren’t Chika and Chinami expecting you?"
    y "Yeah. I’ll head over there in a few minutes."
    y "Just tryin’ to be nice for once and make sure you can find your way back and shit."
    s "You’re being suspiciously nice tonight."
    s "Why?"
    y "..."
    s "..."

    scene yumiknows14
    with dissolve

    "The moonlight reflects off of Yumi’s pale skin as she gazes up at the sky."
    "When you factor in her clothing and how it completely contrasts with the world around her right now, it makes it seem like she’s not supposed to be here at all."
    "But perhaps none of us are supposed to be here?"
    "Perhaps, and this is just one more guess to throw into the pile of “things I can’t explain-”"
    "But perhaps the only reason I so frequently “black out” beside her is that neither of us belong here."
    "{i}Here{/i} as in together."
    "We’re two people with nothing in common who keep getting tossed into situations that wind up making one of us uncomfortable or out-of-place."
    "More common than not, that person is her."
    "Tonight is different, though."
    "Tonight, I will feel out of place no matter who I’m with or where I am."
    "There is no place for me here."
    "This is not my world."

    if chikaonsen4 == False:
        y "I..."
        y "Fuck. This is harder to say than I thought it would be."

        scene yumiknows15
        with dissolve

        y "I don’t...{i}hate{/i} you, Sensei."
        y "Like, I still think you’re a fucking scumbag and want to vomit every time I come up here."
        y "But I don’t hate you."
        y "And also, I’m kind of a scumbag too. So I get it."

        if bonus == True:
            y "We’re two shitty people. Just I pick on the ones I don’t like and you try to get into their pants."
            s "Trying to get into girls’ pants doesn’t make me a scumbag."
        else:
            y "We’re two shitty people. Just I pick on the ones I don’t like and you try to hug them."
            s "Liking hugs doesn't make me a bad person."

        y "If it’s the entire fucking class, then yeah. It does."
        s "So if it was only {i}you{/i}, it would be okay?"

        scene yumiknows16
        with dissolve

        y "Ew, no! That wouldn’t be okay at all!"
        y "But at least I’d be able to find some respect for you if you’d just fucking pick one and stick with her."

        scene yumiknows17
        with dissolve

        y "Like...I don’t know. Chika?"
        s "..."
        s "Are you...giving me your blessing right now?"
        y "I’m not giving you shit."
        y "It just...kinda hurts watching her fall so hard for you when I know the type of guy you really are and she doesn’t."
        y "I’m tired of hearing how excited she is to go on that fucking trip with you and I’m tired of how many times I have to tell her “Maybe tomorrow.”"
        y "Might be hard to believe since it’s me and shit, but I care about her a lot."
        y "Her and Chinami are all I have now."

        scene yumiknows18
        with dissolve

        y "Which is why I’m not going to let you trample all over her naive fucking heart."
        y "Put her first."
        y "Tell her everything she wants to hear and never even {i}think{/i} about screwing her over. Got it?"
        s "..."
        y "{i}Got it?{/i}"
        s "I appreciate your resolve-"
        s "But you should keep your nose out of my love life."
        s "I’m not going to just drop everything and be with one person because you told me to."
        s "Chika is a great girl, don’t get me wrong."
        s "But she’s almost {i}too{/i} great."
        s "Like, she shouldn’t be with me."

        scene yumiknows19
        with dissolve

        y "Well you’re definitely right about that."
        y "Who the fuck {i}would{/i} be good with you, then?"
        y "Would have to be a real screw up. Equally as douchey. Zero work ethic. A whole bunch of shit."
        s "Sounds to me like we might be a better match than you think."

        scene yumiknows20
        with dissolve

        y "Wha-?! Shut the fuck up! We would not!"
        s "Yumi Yamaguchi..."
        s "Will you marry me?"
        y "That’s it! I’m leaving!"
        y "Never call me again!"

        scene black
        with dissolve

        "Yumi runs off into the night and I’m unable to keep up with her."
        "I could just go back to Chika’s place to see her again but..."
        "I feel like I should probably let her sit on my totally serious marriage proposal for a little longer before following up."
        "I obviously know Chika likes me."
        "And I’m glad that Yumi is finally able to talk about that with at least some semblance of seriousness to it."
        "But I do think it would be good if she’d think of herself more instead."
        "Because, despite the constant beratement-"
        "It’s as clear as the sky in the second half of town..."
        "That she may be starting to feel something as well."

        $ renpy.end_replay()
        $ yumi_love += 1
        $ yumicallnight35 = True
        stop music fadeout 5.0

        "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    else:
        y "I..."
        y "I heard about what happened with you and Chika."
        s "..."

        "Well, that secret didn’t last very long."

        y "I don’t know how much of it is just fucking manipulation on your part, but I’m trying to give you the benefit of the doubt."
        y "So when you say shit like “I want you, Yumi...” it really pisses me the fuck off."

        scene yumiknows18
        with dissolve

        y "Chika is a good fucking person. And, for whatever reason, she wants {i}you{/i} instead of anyone else."
        y "Being her boyfriend or whatever is a good start since...I know you haven’t done anything else with her yet-"

        if bonus == True:
            "Oh...so the sex part is still a secret?"
            "I’m honestly surprised Chika managed to hold back that much."
            "That’s...actually really cool of her."

        y "But the second I find out you’re doing something to hurt her, I will destroy you."

        if bonus == True:
            y "So even if you’re joking when you say all that pervy shit to me, know that you’d be hurting the sweetest, most faithful girl I’ve ever met a lot if she ever heard any of it."
        else:
            y "So even if you’re joking when you say all that annoying shit to me, know that you’d be hurting the sweetest, most faithful girl I’ve ever met a lot if she ever heard any of it."

        s "And she told you that this was something that shouldn’t be discussed with anyone else, right?"

        scene yumiknows21
        with dissolve

        y "She did."

        if bonus == True:
            y "But I think that’s less about wanting to keep it a secret and more about you still wanting to fuck around with other girls."
            y "If you were willing to go after me of all people, I can only imagine what kind of shit you’ve tried doing to some of the others."
            s "..."

        y "Like I said, I’m going to try to give you the benefit of the doubt for her sake."
        y "But I’ll be fucking watching you. Got it?"
        y "And the second you do anything that might hurt her, I’m not only telling her about it, but I’m going to ruin your fucking life."
        y "I don’t care if the principal won’t believe me. I’m telling him. I’m telling that fucking weird, purple haired goth teacher too."
        y "Shit, I’ll send a letter to the fucking newspaper."

        scene yumiknows22
        with dissolve

        y "I...will not...let you hurt that girl."
        s "..."
        y "..."
        s "You’re being surprisingly mature about this."
        y "So?"
        s "I just kind of expected more of a freak out...You know, maybe a few more insults and whatnot."
        y "I’m too tired to insult you."
        y "I just want to go eat ice cream at Chika’s house."
        s "What is it with you and ice cream all of a sudden?"

        scene yumiknows20
        with dissolve

        y "It’s not “all of a sudden!” It’s fucking ice cream, dude! I have liked it forever!"

        if bonus == True:
            s "You certainly seemed to enjoy it with the way you-"
        else:
            s "I'm not really a big fan, to be honest."

        y "That’s it! Conversation is over!"
        y "Enjoy your walk back home, asshole!"

        if bonus == False:
            s "Wow, you really do like ice cream."

        scene black
        with dissolve

        s "Wait, Yumi. I-"
        y "I said the conversation is over! Stop following me!"

        "Yumi runs off into the night and I’m unable to keep up with her."
        "I could just go back to Chika’s place to see her again but..."
        "Given everything we talked about tonight, it’s probably best if I just leave things alone for now."
        "I’m not sure what knowing about Chika and me will do to my relationship with Yumi-"
        "But at least I can find some form of solace in knowing that she’s a good person deep down."
        "I doubt that about her sometimes."
        "I probably shouldn’t, though."
        "Not when I’m ten times worse."

        $ renpy.end_replay()
        $ yumi_love += 1
        $ yumicallnight35 = True
        $ yumiknows = True
        stop music fadeout 5.0

        "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label yumispecial40:
    scene familyreunion1
    with dissolve2

    y "The fuck are you smiling for? You think that just because I’ve decided to say a few words to you means I’m gonna just let you back into my life?"
    y "If it weren’t for you putting your filthy fucking hands all over the dude my best friend likes for...whatever fucking weird reason she likes him for, I would have just kept walking."

    scene familyreunion2
    with dissolve

    yu "Course you would have. Just like you did back at Tojo’s. "
    yu "I know it must be exhausting coming to terms with how I somehow managed to stay alive all these years, but would it kill you to at least {i}pretend{/i} to be happy to see me?"
    y "Would it kill {i}you{/i} to stop fucking trying to...reconcile with me or whatever the fuck this is? "
    yu "Reconcile? Your teacher the one helpin’ you learn big words like that?"
    y "Maybe. Just because {i}you{/i} decided to drop out of school doesn’t mean I’m going to follow in your footsteps."

    scene familyreunion3
    with dissolve

    yu "Good. I’m not sayin’ you should. "
    yu "I’m glad you’re actually out there makin’ an effort and shit. Damn impressive for someone constantly running from the shadow of her mother."
    y "Would be a hell of a lot easier if that “shadow” wasn’t behind nearly every fucking corner I round lately."
    y "How hard have you been trying to see me? I feel like I can’t go ten minutes without Sensei or...anyone else fuckin’ bringing you up. Why now?"
    y "If you’re looking for drug money, go to Dad. Not me. I won’t take shit from him. I’m tryin’ to make it on my own."
    yu "I don’t need drug money, Yumi. I’m clean now."
    y "Yeah? For how many hours?"

    scene familyreunion4
    with dissolve

    yu "..."
    y "Hey, how about we take a trip to the counter together? Maybe we can buy you a fucking cupcake or something to celebrate half a day sober!"
    y "It’ll be just like the old days...when we’d come down to places just like this so you could buy cigarettes or booze to keep yourself occupied while I tried to learn how to read."
    y "Doesn’t that sound fun, {i}Yuki?{/i}"

    scene familyreunion5
    with dissolve

    yu "You can still call me Mom, you know."
    y "Why would I?! Apart from the fuckin' ramen place, I can’t even remember the last time I saw you!"
    y "And half of the times I {i}do{/i} remember, you’re passed the fuck out with a needle sticking out of your arm!"
    y "Why the absolute {i}fuck{/i} would I call you “Mom?!” That’s a title you have to work for!"

    scene familyreunion6
    with dissolve

    yu "Well then let me fucking {i}work{/i} for it, Yumi! You really think I’ve been trying so hard to see how you’re doing just because I need drug money?!"
    yu "Why the fuck do you think I’m still in Kumon-mi in the first place?"
    y "Beats me. Probably got stuck inside before they closed the place off. "
    y "And knowing you, chances are you’ve burned all the bridges you need to keep yourself on your own two feet. Or what’s left of them, at least."
    yu "Yeah. I’m a shitty person, and an even worse mother. And I’ve done a lot of stuff that I wish I never did. But I’m still a fucking person."
    yu "I’m not asking for your help or forgiveness or any of that bullshit because I know full well that I don’t deserve it. Hell, I don’t even need to be a part of your life if you don’t want me to."
    yu "But to have my...entire existence be ignored by my own daughter is just-"

    scene familyreunion7
    with dissolve

    y "Just what?! Unfair?!"
    y "You know what’s unfair, Yuki?! Growing up without a mom! "
    y "At least if you would have fucking {i}died{/i} or something I could look back on you and try to dig up any of the “good” times we may have had!"
    y "But, nope!"

    scene familyreunion8
    with dissolve

    y "You were out...riding around on your little motorcycle...having a grand old time getting high and sucking dick for heroin while I was trying to figure out what it meant to be a normal girl."
    y "The only reason I’m as fucked up and “rough around the edges” as I am now is because of you, {i}Yuki.{/i} You did this to me."
    y "So when I ignore your existence, it’s probably safe to assume that I’m doing it to protect myself."
    y "Got it?"
    yu "...Yeah."
    yu "I got it."

    scene familyreunion9
    with dissolve

    yu "But I ain’t ever tried to dodge the blame for all that, Yumi. "
    yu "In fact, all the shit I’ve been tryin’ to do lately is to prove how {i}sorry{/i} I am. "
    y "I’m sorry, would you mind explaining to me how flirting with my fucking teacher in front of me is trying to prove how sorry you are? Because, to me, that just makes it look like you haven’t changed one bit."
    yu "It was a joke, I don’t know. I just wanted you to say something. I didn’t really care what it was."

    scene familyreunion10
    with dissolve

    y "Stop {i}wanting{/i} me to do anything and just go back to leaving me alone like you’ve done for the last...forever!"

    if yumiknows == True:
        y "I don’t want anything to do with you! And if you’re going to keep flirting with my friend’s boyfriend, do it in whatever fucking box you’re living in instead of in public!"
    else:
        y "I don’t want anything to do with you! And if you’re going to keep flirting with my teacher, do it in whatever fucking box you’re living in instead of in public!"

    yu "..."
    yu "Did you like your present at least?"
    yu "I know it probably seemed like a fuckin’ slap in the face gettin’ something so small after so much time away, but that was really all I could afford with the money I have."
    yu "I just wanted to do something for your birthday after missing the rest of ‘em."

    scene familyreunion11
    with dissolve

    y "I’m surprised you’ve got enough brain cells left to even remember my birthday."
    y "As for the “present,” I loved it. Made a real satisfying sound when I tossed it into some fucking rich girl’s pond."

    scene familyreunion12
    with dissolve

    yu "You...what?"
    s "I didn’t realize you were in the position to just be throwing away things that people give you-"
    y "Stay the fuck out of this, Sensei."
    y "As if I’d accept a fucking consolation prize from this piece of shit. "

    scene familyreunion13
    with dissolve

    yu "Heh."
    y "...What?"
    y "What reason could you possibly have to be laughing right now?"
    yu "No real reason."
    yu "You just remind me a lot of myself when I was your age."

    play sound "slap.mp3"
    scene familyreunion14 with hpunch

    y "Fuck you!"
    yu "..."

    "I looked away for a second, likely because even I get tired of staring at roadside car accidents, but even without looking, it’s easy to understand what just happened."
    "And I’m sure it’s the same thing that would have happened when Futaba was in the same exact scenario not too long ago."
    "The last thing Yumi wants is to resemble her mother."
    "But, if that’s the case, it would probably be good for her to stop hitting people since I’m pretty sure that was just Yuki’s thing for a...very long time."
    "That aside, I think the time has come for me to step in. "

    s "Yumi, that’s-"
    yu "Nah, let her go. It’s no big deal."

    scene familyreunion15
    with dissolve

    yu "She hits like a bitch anyway."
    y "Wha-"
    yu "You know, maybe you’re {i}not{/i} my daughter after all. {i}My{/i} daughter would take her gloves off before slapping someone. It softens the blow."

    scene familyreunion16
    with dissolve

    y "J-Just because your face is numb from being coked out of your mind doesn’t mean I hit like a bitch!"
    y "Now get the fuck out of here before I do it again!"

    if yumiknows == True:
        yu "I can’t. I’m still waiting for your “friend’s boyfriend” to choose what he wants for dinner since I owe him for helping me out."
    else:
        yu "I can’t. I’m still waiting for your teacher to choose what he wants for dinner since I owe him for helping me out."

    scene familyreunion17
    with dissolve

    if yumiknows == True:
        if bonus == True:
            y "Well maybe my {i}friend’s boyfriend{/i} should try to be a decent person for once in his life and {b}not stick his dick in my mother in exchange for a convenience store dinner!{/b}"
        else:
            y "Well maybe my {i}friend’s boyfriend{/i} should try to be a decent person for once in his life and {b}not just hug everyone in Kumon-mi!{/b}"
    else:
        if bonus == True:
            y "Well maybe my teacher should try to be a decent person for once in his life and {b}not stick his dick in my mother in exchange for a convenience store dinner!{/b}"
        else:
            y "Well maybe my teacher should try to be a decent person for once in his life and {b}not just hug everyone in Kumon-mi!{/b}"
            s "Hey! That hurts my feelings!"

    play sound "slap.mp3"
    scene familyreunion18 with hpunch

    y "-!"
    yu "Hey. You can talk as much shit to me as you want, but that is your {i}teacher.{/i} You treat him with respect. "
    s "Yuki, that’s really not-"

    scene familyreunion19
    with dissolve

    yu "Huh. You know, maybe there’s a right way to slap someone with gloves on after all?"
    s "..."
    y "..."

    "It’s clear that neither of these two have any interest in letting me interfere but, to be honest, I kind of expected as much."
    "Yumi’s already proven to be beyond reasoning with and Yuki is...well, {i}still{/i} not the best mother even when she’s trying to be."

    if bonus == True:
        "Her methods were definitely effective, though, as I don’t think I’ve ever seen Yumi this shell-shocked before- and I have literally forced my tongue down her throat."

    scene familyreunion20
    with dissolve

    yu "I haven’t heard an “I’m sorry, Sensei” yet."
    yu "He did nothing wrong. When you have a problem with someone, you don’t bring other people into it. Got it?"
    yu "I raised you better than that."
    y "I’m...sorry..."
    s "..."

    scene familyreunion21
    with dissolve

    y "And you didn’t raise me at all, so my bad for not knowing where to properly direct my anger."
    y "Hitting your daughter in public, though? That’s low."
    yu "What, and hitting your mother isn’t? Don’t dish it out if you can’t take it, Yumi."
    yu "You wanna act like an adult and grow up all by yourself? Fine. Go right ahead."
    yu "But don’t go around accusing everyone of being against you when they’re just trying to help. "
    yu "If you’re that afraid of winding up like me, that’s the very least you can do."
    y "..."
    yu "..."
    y "I fucking hate you."

    scene familyreunion22
    with dissolve

    yu "Good."
    yu "You should hate me."
    yu "If I were you, though, I’d go check and see if that present you tossed into the rich girl’s pond is still there. "
    yu "There were enough gift cards in that to feed you for a week, probably. Two if you be cheap about it."
    y "Please...just..."
    y "Just leave me alone..."

    scene familyreunion23
    with dissolve
    play sound "entrybell.mp3"

    "Yumi exits the convenience store in a hurry without buying anything- and I think it’s strange that my mind gravitates to {i}that{/i} aspect of this situation rather than anything else."
    "I guess watching her struggle to stay afloat has become so normal for me that I just chalk it up to a natural occurrence any time things go horribly for her."
    "I guess there are just some people born with horrible luck."
    "And I guess they just all happened to be born in close proximity to me."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene familyreunion24
    with dissolve

    yu "Well, that could have gone better."
    s "You know, when Yumi arrived, I could have sworn that you were going to ease up on the flirting rather than just entirely lean into it."
    yu "Not the best idea looking back on it, but I’ve got a history of making shit decisions in the heat of the moment."
    yu "You gonna follow her?"
    s "What would I do if I did?"
    yu "I don’t know. Teacher shit? Tell her everything’s gonna be okay and like, pat her on the back or somethin’?"

    scene familyreunion25
    with dissolve

    s "Cheering people up isn’t really one of my strong suits."
    yu "Same here, but I’m sure you’ve probably figured that out in the last few minutes."
    yu "We’ll take a rain check on dinner for now."
    yu "Go run after my piece of shit daughter and make her feel like {i}less{/i} of a piece of shit for popping out of me."
    yu "I’ll just go back to my {i}box{/i} and relapse or something since that’s clearly all I’m good for."
    s "Please don’t. You’re doing really well based on the zero experience I have of the drug-addicted version of you."

    scene familyreunion26
    with dissolve

    yu "I know. And I won’t. "
    yu "Gonna take more than that to knock me on my ass again."
    yu "But, uhh...thanks again for showin’ up or whatever. Sorry it couldn’t end on a better note."
    yu "Bad shit really tends to just follow me around at times."
    s "Yeah..."
    s "Same here."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yumispecial40 = True
    stop music fadeout 10.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    jump yumispecial40p2

label yumispecial40p2:
    scene clearnightsky with dissolve2
    play sound "entrybell.mp3"

    "I make my way out of the convenience store and try to spy on Yuki out of the corner of my eye- thinking that maybe she was just waiting for me to be gone to let her guard down and start crying or something."
    "Of course, I’m unable to see anything. "
    "Not just because she’s likely not robotic enough to cease functioning the second I’m out of her line of sight, but because mine is currently being flooded by an onslaught of street lights and neon."

    play music "sensei.mp3"

    "Yumi."
    "That’s what I should be thinking about right now- not whatever minor inconveniences I’m stuck dwelling on in an effort to make myself believe my problems are somehow bigger than hers."
    "After all, this is a rare opportunity for me to make a positive impact on someone’s life when they need it the most."
    "And oh, how excited I am to let that {s}slip{/i} fall through my fingers like the grains of sand I’m {i}still{/i} finding on my clothes and in my shoes all this time after the second beach trip."
    "If only I was able to bring something of value home with me rather than the useless remnants of something I never wanted to begin with."
    "Now, where did she run off to?"

    s "..."

    "I look around and see plenty of other people."
    "And if this were one of those Korean dramas Ami watches all the time, I’m sure the first person I’d ask would know exactly which direction the girl I’m looking for ran off in."
    "Unfortunately, real life is scarcely that convenient- and I expect tonight to be full of failed chances at locating her amidst growing waves of uncertainty regarding whether or not I even {i}should.{/i}"
    "What can I do?"
    "Or rather, what {i}will{/i} I do? "
    "Because those questions have two dramatically different answers, and the one that we’ll wind up observing together will likely be the one furthest from the right course of action."
    "Oh well."
    "I guess I’ll just shrug-"
    "Slide my hands into my pockets-"
    "And venture off in whatever general direction my gut points me in."
    "It’s led me to her plenty of times in the past."
    "Here’s hoping it doesn’t stop cooperating now."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yumiwallpound1
    with dissolve2

    "Well, would you look at that?"
    "There were barely any failures at all on the way here."
    "In fact, I think this is only the third or fourth alleyway I’ve had the displeasure of searching. "
    "And here she is in all of her miserable glory- pounding away at a cement wall, still wearing the gloves her mother ridiculed her for not removing just a short while ago."
    "That’s good. "
    "It might be awkward for all of us if I have to rush Yumi back to the convenience store for bandages only to find Yuki there, still caught up in a daze about where her life is heading."

    s "..."
    y "{i}*Sniff*{/i}"
    y "Fuck!"
    y "Fuck! Fuck! Fuck!"
    s "..."

    scene yumiwallpound2
    with dissolve

    y "I know you’re there, asshole. "
    s "Damn. I was a little interested in seeing if you’d be able to take down that wall or not."
    s "What gave my presence away?"
    y "Probably the fact that my body instinctively tenses up any time you’re within ten feet of me."
    s "I’ll try and stay at least fifteen feet away the next time I have to chase you down an alley, then."
    s "How are your hands?"

    scene yumiwallpound3
    with dissolve

    y "I don’t know. Cold?"
    y "They hurt a little, I guess."
    y "Not like I have anything else I can fuckin’ take my anger out on around here, though."

    scene yumiwallpound4
    with dissolve

    y "And what the fuck were you doing with her?! I thought I told you to stop getting yourself involved with my fucking family!"
    s "I’m aware. I have a tendency to kind of just do what I want, though, so commands like that won’t ever really have any effect on me."
    y "You don’t fuckin’ say."
    s "Since you’re being so polite, I guess I can let you know, though."
    s "I was helping her pass out fliers for the bar she works at."
    s "Probably so she can save up enough money for another present you can throw into Ayane’s pond."

    scene yumiwallpound5
    with dissolve

    y "I don’t want her fucking {i}presents.{/i} I want my childhood back."
    y "Let me know when she figures out how to fit that into a fucking box and I’ll think about maybe {i}not{/i} dumping it into the nearest body of water."
    s "I’ll be sure to let you know."
    y "Yeah. Thanks."


    scene yumiwallpound6
    with dissolve

    s "So, how long are you planning on staying out here for?"
    s "In fact, why are you even all the way over here in the first place? We’re a long way from the dorms."
    y "So what? I’ve got legs. I know where the fuck I’m going."
    s "I’m pretty sure the last time I saw you over here, you were in the heat of trying to evade our constant run-ins with one another. Don’t tell me that’s what-"

    scene yumiwallpound7
    with dissolve

    y "I was looking for a job, okay?! "
    s "Without my help? I didn’t think you cared that much."
    y "Well, I do! And since nowhere near the fuckin’ dorms wants to hire me, it looks like I’ve got nowhere else to search but right smack dab in the heart of the fuckin’ city!"
    s "I really hope you weren’t planning on applying to that convenience store because I’m pretty sure you may have just ruined your chances."

    scene yumiwallpound8
    with dissolve

    y "Ha ha ha. You’re fucking hilarious. Now can you leave me alone for a few more minutes so I can finish crying?"
    y "Feel like that’s all I’ve been fuckin’ doing lately. "
    y "You know, it’s real weird how I went basically my whole life without crying until you started getting involved in it. Now, it’s like I can’t even do shit without realizing how fucked up and weak I am."
    s "You should be thankful you met me now, then. That sort of thing would catch up to you after a while."
    s "And the longer you kept it held in, the worse it would be when it finally boils over."

    scene yumiwallpound9
    with dissolve

    y "I’d sure as fuck be fine with takin’ my chances. Can’t see how it would be any worse than trying to beat a fucking cement wall to death."
    y "‘Sides, wouldn’t all that shit about not bottling things up make you a hypocrite or whatever?"

    if bonus == True:
        y "That is, assuming you’re still capable of feeling anything and you’re not some...mindless fuck-robot."
        s "You know, at this point, that’s starting to sound like a pretty accurate description."

        if yumiknows == True:
            y "Remember who it is you’re talking to, asshole. The second I have {i}any{/i} confirmation you’re sticking your dick in anyone other than Chika, I’m tearing it all down. "
            s "You could start by finishing that wall. A few hundred more punches and you’ll have likely made some sort of chip in it."
    else:
        y "That is, assuming you’re still capable of feeling anything and you’re not some...mindless hug-robot."
        s "Beep boop. Does not compute."

    scene yumiwallpound10
    with dissolve

    y "{i}*Sniff*{/i}"
    y "Why me, man?..."
    y "Why won’t everyone just leave me alone?..."
    s "..."
    y "..."

    "I highly doubt Yumi wants me to actually answer that question- which is good, because I’d have no answer for it if she did."
    "I can’t speak for anyone else, obviously, but why {i}do{/i} I keep bothering Yumi?"

    if bonus == True:
        "Is it {i}really{/i} just to have sex with her? "
        "Or is it more like I’m chasing after some sort of debt that I feel she’s owed after stealing her first kiss on a hill overlooking the homeless?"
    else:
        "Is it really just to hug her?"
        "Or is it more like I’m chasing after some sort of debt that I feel she’s owed after {i}actually{/i} hugging her?"

    "Or maybe it’s neither of those things? "
    "Or maybe it’s both?"
    "Maybe I’m just doing this because I feel like I’m supposed to?"

    if bonus == True:
        "Like neglecting her will, one way or another, cause my life to spiral out of control into a marathon of meaningless sex acts with all of her classmates."
    else:
        "Like neglecting her will, one way or another, allow me to hug more people on a more frequent basis."

    "That would have sounded wonderful several school years ago."
    "Actually, it sounds wonderful right now."
    "But, strangely enough, the presence of a girl who just wants me to leave her alone somehow brings a little balance to this thing of mine resembling a life."
    "And I’m talking about someone who {i}actually{/i} wants me to leave them alone."
    "Even that part of Maya’s personality has been beginning to show cracks as of late."
    "But here’s Yumi- equipped with more cracks than you’d get from throwing a frag grenade at a china cabinet."
    "And here’s me-"
    "Desperate to “fix” her."

    scene black
    with dissolve2

    "Yumi stands up and shakes her gloves off before bringing them to her eyes to wipe away her tears, because god forbid I actually {i}see{/i} them."
    "She stands still for a moment, torn between thoughts of running away again or actually talking to me."
    "If she does run, I won’t chase her this time. I know better than to go out of my way for someone twice in rapid succession."
    "But-"
    "If she wants to talk-"
    "I’ll do my best to soak up whatever overly-aggressive behavior or excuse she has for me this time around."
    "All while reminding myself that I can’t touch her, no matter how much I may want to."

    scene yumiwallpound11
    with dissolve2

    y "So...fliers? Really?"
    y "This why you can’t be bothered to actually teach? You’re too busy workin’ night jobs with allegedly recovering addicts?"
    s "Yes. I also fight crime by night, but you have to keep my secret identity to yourself or the two of us could be assassinated. "
    s "Also, you should be thankful that I don’t actually teach because, if I did, you would have failed a long, long time ago."

    if bonus == True:
        y "I’d be more interested in coming to school if I didn’t constantly feel like my teacher was imagining me naked."
        s "Don’t flatter yourself, Yumi. I have a whole twenty girls to imagine naked now. I only have so much time for you."
    else:
        s "Just kidding. I love teaching."
        s "And...I love {i}you.{/i}"

    scene yumiwallpound12
    with dissolve

    y "Ew! Gross! Fuck off! "
    y "See, this is exactly why I don’t show up! Because of you!"
    s "Why not ask for a transfer then?"
    y "To where? Everyone thinks I’m a fucking delinquent, dude. No one wants me."
    s "They don’t {i}think{/i} you’re a delinquent. You literally {i}are{/i} a delinquent. "
    y "Well, yeah. That’s why they all think it. But that’s beside the point!"
    y "I’m stuck in your stupid class, and unless you decide to throw me out of it, you’re stuck with me too."
    y "Just...only on days when I actually show up. The rest of the time, just pretend I don’t exist or some shit."
    s "You know I can’t do that, Yumi."

    scene yumiwallpound13
    with dissolve

    y "But...why?"
    y "All I do is cause problems and start shit with both you {i}and{/i} the other girls. "

    if bonus == True:
        y "I’ve got what’s basically a negative attendance record, shit grades when I {i}do{/i} take tests and, to top it all off, I’ve got mad fucking dirt on you from when you kissed me."
    else:
        y "I’ve got what’s basically a negative attendance record, shit grades when I {i}do{/i} take tests and, to top it all off, I’ve got mad fucking dirt on you from your attack hug."

    y "Granted, nobody will fucking believe me if I tell them, but all of that should be enough for you to want to stay the fuck away."
    s "..."
    y "..."
    y "What?"
    s "You just normally look a little...angrier when you say things like that."
    y "..."
    s "..."

    scene yumiwallpound14
    with dissolve

    y "I’m done being angry for today."
    y "It’s giving me a headache."
    y "I just want to go home and go to sleep."
    s "..."
    y "..."

    scene yumiwallpound15
    with dissolve

    y "What now?"
    y "Is my sudden vulnerable side making you question your morals again?"
    y "Are you going to make another horrible decision, Sensei?"
    s "..."

    scene yumiwallpound16
    with dissolve

    y "What if I close my eyes?"
    y "How about now?"
    y "Are you thinking about what you could get away with?..."
    y "What sort of horrible shit you could do to me?..."

    scene yumiwallpound17
    with dissolve

    y "And how fucking easy it would be to overpower me when I’m so fucking weak right now!"

    play sound "static.mp3"
    scene connect with flash
    scene frown with flash
    scene happy7 with flash
    scene yumiwallpound18 with flash
    stop sound

    "Something pulls me under so quickly that I can’t even get a glimpse at what it is."
    "But, if I had to take a guess, it would probably look something like me."
    "I don’t know whether or not I’m blacking out right now, and I fear that whenever I snap out of this, I might find myself in a similar place to somewhere I’ve been in the past."
    "I can only hope this isn’t true-"
    "But given the fact that Yumi’s already had a bad streak of luck today-"
    "And the {i}added{/i} fact that she’s been the target of these lapses in not just judgement but what seems like reality as a whole-"
    "Well-"
    "I can only imagine how things must be-"

    play sound "static.mp3"
    scene attempting with flash
    scene everythingg with flash
    scene frown with flash
    scene yumiwallpound19 with flash
    stop sound

    s "..."
    y "..."

    "When I open my eyes, it’s as if nothing has changed at all."
    "Yumi is still standing there with tears pooling up behind her eyelids- though, several have managed to escape down the length of her cheeks."

    if bonus == True:
        "And I’m still standing right next to her, caught somewhere between the early stages of forming an erection and the desire to slap her across the face and snap her out of whatever this is."
        "Two slaps in one night might be a bit too much for her, though."
        "And so I will use this moment as an excuse to reclaim several of the brownie points that I may have lost by being seen out in public with her least favorite person in the world."
    else:
        "And I’m still standing right next to her, ready to hug and ready to party."

    if yumiknows == True:
        s "I’m not going to kiss you, Yumi. Chika is my woman and I am her loyal, monogamist man."
    else:
        s "Nothing's going to happen, Yumi."
        s "I'm not going to hurt you."

    scene yumiwallpound20
    with dissolve

    y "Huh?..."
    y "Oh...Yeah. "
    y "Yeah. Okay."
    s "..."
    s "Don’t tell me you were hoping I {i}would{/i}...were you?"

    scene yumiwallpound21
    with dissolve

    if bonus == True:
        y "O-Obviously not! In fact, I’m surprised you were able to hold back given how fucking...perverted and...insatiable you are!"
    else:
        y "O-Obviously not! I hate you and...I hate your stupid hair cut!"

    s "Right."
    y "Right! And why are you just standing there fuckin’...staring at me, you creep! Back the fuck off!"
    s "You’re the one who walked up to me, Yumi. "

    scene yumiwallpound22
    with dissolve

    y "Jesus! When the fuck did it get so dark out here?! What time even is it right now?!"
    s "..."
    y "Listen, as much as I’d love to stay and chat, I’ve got shit to do and...and it’s a long walk home."
    s "..."
    y "..."
    s "We can walk together if you want?..."

    scene yumiwallpound23
    with dissolve

    y "..."
    s "..."

    scene yumiwallpound24
    with dissolve

    y "..."
    y "No..."
    y "No."
    y "I’ll make it on my own."

    scene black
    with dissolve2

    "Yumi leaves with that, and I’m forced to stand there in the alleyway and wait for her to fade away from my sight so as to not awkwardly walk behind her since we have to go in the same direction."
    "I’m not sure what really came over her with that “test” of hers a few minutes ago, but I’m thankful that it didn’t end in tragedy when nearly everything else tonight did."
    "I guess there’s nothing left to do now but...go home, then."

    play sound "phonebeep.wav"

    "I decide to send Yuki a text on my way out of the alley, confirming that her daughter is, at least as of several minutes ago, still alive and doing mostly okay."
    "Yuki doesn’t respond."
    "I catch a bus back home and go the rest of the night without saying or thinking anything else."

    $ renpy.end_replay()
    $ yumi_love += 2
    $ yumispecial40p2 = True
    stop music fadeout 7.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label streets40:
    scene wintersky
    with dissolve2
    play music "justlights.mp3"

    "Ahh, snow."
    "Frozen water droplets guaranteed to fill the hearts of children with glee as they look outside of the window and realize there’s even a slight possibility of skipping school for a day."
    "I try to recall a time in my life where those kinds of thoughts would find their way into my head."
    "Now, any time I look up and see something like this, I just think of it as an inconvenience."
    "And so I take a moment to reflect on how things may have changed for me over the years."

    scene yumiporn1
    play music "yumiska.mp3"

    "But that moment is cut short the second I bump into Yumi."

    s "Yo."
    y "...Yo."
    s "Your bridge is a little further that way. You’re missing out on quality target practice."
    y "Not like there are any fuckin’ cars driving around in this weather anyway. "

    scene yumiporn2
    with dissolve

    y "And hey! I don’t just spend every waking moment spitting on cars, asshole. I’ve got better shit to do."
    s "Oh? Don’t tell me you went and found a job without me."

    scene yumiporn3
    with dissolve

    y "Nah. I haven’t even really looked since that whole...fiasco the other night."
    s "Then what is this apparent “better shit” you have to do that takes precedence over tormenting drivers and finding a way to put food on the table?"
    s "And don’t say “avoiding me” either because it’s clear that you’ve at least temporarily given up on that."
    y "Well...right now, I ain’t doing shit. But in a couple hours or whatever, I’m supposed to be meeting Chika around here to help her pick out a Christmas present for the brat."
    s "Chinami doesn’t need any Christmas presents. She has both a cell phone and a business now. Her life is complete."

    scene yumiporn4
    with dissolve

    y "Sorry to be the bearer of bad news but I’m almost confident that {i}business{/i} doesn’t actually exist."
    s "Almost?"
    y "Yeah, well, you never fuckin’ know with her."
    s "So what then? You’re just planning on standing around here for hours until it’s time to meet Chika?"

    scene yumiporn5
    with dissolve

    y "What the fuck else am I gonna do? Ask your [niece] to hang out? Go bowling with the fucking weird ponytail girl?"
    s "We have several weird ponytail girls now, so I’m not really sure which one you’re referring to."
    y "The watermelon one."
    s "Oh, Maya. "
    s "Yeah, don’t hang out with her. You two forming an alliance would be extremely irritating for me."
    s "But why not use this time to get back to job hunting if you don’t know what else to do?"
    s "You have me now. And you’re wearing your nice clothes and everything."

    scene yumiporn6
    with dissolve

    y "My other clothes are fucking fine! Eat a dick!"
    s "Sure. But these ones are...more fine."

    scene yumiporn7
    with dissolve

    y "Ugh...do we really have to do this job shit right now?"
    y "Because if I wind up running into someone I know for a second time in a row, I’m just going to give up on ever finding a job."
    s "Would you rather continue standing here together? We could try talking about our feelings. We’re both very good at that."
    y "Can I talk about how shitty it feels constantly being around you? Because I could probably kill a few hours that way."
    s "I mean...that’s typically what you talk about anyway. But if that’s going to be your attitude, I’ll put my foot down right now and start the job hunt without your consent."

    scene yumiporn8
    with dissolve

    y "What? You doing something without my consent? As if that would ever happen."

    if bonus == False:
        "She must be referring to that one hug."

    s "Hey, correct me if I’m wrong, but I was able to successfully restrain myself the last time you gave me an opening to go against that."
    y "Congrats on having the slightest shred of self control imaginable. It’s almost like you’re a real human being now."
    s "Are any of us truly {i}real{/i}, Yumi?"

    scene yumiporn9
    with dissolve

    y "You know what? Fine. At the risk of you getting all fucking philosophical, sure. Let’s go {i}job hunting{/i}."
    y "It might be fun trying to set the world record for refused applications or failed interviews or however I manage to fuck things up this time."
    s "Yumi, you’ve been rejected by like three places. That’s really not that bad."
    s "Plenty of adults get rejected by far more than that before finding a place to work."

    scene yumiporn10
    with dissolve

    if bonus == True:
        y "Really?! Because the fact that you were hired by a {i}school{/i} makes me pretty fucking doubtful of that!"
    else:
        y "Really?! Because the fact that you were hired by a {i}college{/i} makes me pretty fucking doubtful of that!"

    s "Touché. "
    s "Luckily for you, though, I have an idea of a place that I can’t imagine rejecting you at all."

    scene yumiporn11
    with dissolve

    y "What? Really? Well, then why the fuck did you wait until right now to tell me about it?"
    s "..."

    scene black
    with dissolve

    s "Anyway, follow me."
    y "Yo! I asked you a fuckin’ question! Don’t just start walking away!"

    "The truth is that I’m not {i}100%%{/i} confident Yumi will just be allowed to work here-"
    "But, at the same time, I’m not really sure if she’d {i}want{/i} to either."
    "But hey, if she’s truly desperate for work, she should be willing to go a little outside of her comfort zone."
    "And what better place to do that than one of my favorite local businesses that I’ve been all but banned from shopping at?"

    y "Wha-"
    y "Where the fuck do you think you’re taking me, creep?!"
    s "Just let it happen, Yumi."

    scene yumiporn12
    with dissolve

    y "Is this a fucking porn shop?!"

    if bonus == True:
        s "I like to think of it as an “adult entertainment center.”"
    else:
        s "Yes. But I really just come here for the romantic comedy DVDs."

    scene yumiporn13
    with dissolve

    if bonus == True:
        y "That’s just a fancy way to say it’s a porn shop, you fucking lunatic! I’m pretty sure I’m not even allowed to be in here!"
        s "Since when do you care about anything you’re {i}allowed{/i} to do?"
        y "Since there’s fucking porn involved! I can’t work here!"
    else:
        y "That's even fucking worse!"

    mak "Wha-"

    scene yumiporn14
    with fade

    mak "What is the meaning of this?! Are you out of your fucking mind?!"
    s "Do you have any job applications laying around?"
    mak "No! Leave!"

    scene yumiporn15
    with dissolve

    mak "And why on earth are you with {i}Yumi{/i} of all people?"
    y "Hm? You know me?"
    y "I ain’t ever seen you a day in my fuckin’ life. "
    mak "..."
    s "Go put your glasses on."

    scene yumiporn16
    with dissolve

    mak "Ugh..."

    scene yumiporn17
    with dissolve

    y "The fuck is even going on right now?"
    s "Nothing really. This is actually a pretty normal day for me, all things considered."

    scene yumiporn18
    with dissolve

    mak "..."
    y "..."
    y "Oh, no fucking way."
    mak "Leave. Now. Both of you."
    s "The service here really isn’t all that great, so clearly there’s a chance for you as an employee after all."

    scene yumiporn19
    with dissolve

    y "Wait, wait, wait, wait, wait..."
    y "You mean to tell me the fucking {i}class rep{/i} works at a porn shop? Is this some kind of prank?"
    s "Her family actually owns the place. "
    y "Yeah. Sure they do. I ain’t fallin’ for that shit. Now, where’s the real job?"

    scene yumiporn20
    with dissolve

    maki "What’s going on? We haven’t had this many people in the store since last Valentine’s Day."

    scene yumiporn21
    with dissolve

    maki "And who’s this? Another [niece] that I’m not finding out about until right now?"

    if bonus == True:
        maki "Maybe a mistress? Hooker? You two can hang out in the back room at a discounted rate, but you’ve gotta be quick since I need to clean the glass sometime before night comes."
    else:
        maki "Your taxes must be really complicated."

    mak "That is a classmate of mine, {i}mother{/i}."
    maki "Oh. Well, we don’t have a {i}student{/i} discount here, so you’ll have to pay full price. Still be quick, though."
    s "She’s actually looking for a job, Maki. And I figured somewhere like this might be a good opportunity for her."
    maki "You want to sell porn?"
    y "Uhh...not really?"

    scene yumiporn22
    with dissolve

    maki "I’ve gotta say, not a good start, Sensei. "
    s "Maybe you two just need some one-on-one time together? I’m sure if anyone is able to get Yumi to open up the wonderful world of adult entertainment, it’s you."
    mak "Wonderful, because that gives me the chance to talk to {i}you. Alone.{/i}"

    scene yumiporn23
    with dissolve

    maki "Works for me! Though, I am a little sad because Makoto gets the {i}family{/i} discount and I was really banking on some of that sweet, sweet back room revenue. "
    y "Uhh..."
    y "Wait, this...{i}isn’t{/i} just a prank then?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yumiporn24
    with dissolve

    mak "What are you doing?! Why are you here?! Why did you bring {i}Yumi{/i} here?! "
    mak "You know how important it is for me to keep my involvement with this place hidden!"
    s "From Yumi? What’s she going to do about it?"
    mak "Oh, I don’t know- use it as leverage against me? "
    mak "I’m pretty sure that Chika’s already {i}seen{/i} me here and that's bad enough! Now, the entirety of Dorm #1 knows!"
    s "Alternatively, you could just hire her. Then she’d be forced to keep it a secret as well."

    scene yumiporn25
    with dissolve

    mak "But why {i}here?!{/i}"
    mak "There are a million other places hiring [teenager]s! Why would you bring her to arguably the worst of all of those places?! Especially when you {i}know{/i} I don’t want you to?!"
    s "..."
    mak "Well?"

    scene yumiporn26
    with dissolve

    s "I thought it’d be funny."
    mak "You fucking-"

    if bonus == True:
        s "Besides, Yumi’s been through a lot lately. I figured something lighthearted like a trip to the local porn shop might brighten things up a bit for her."
    else:
        s "Besides, Yumi’s been through a lot lately. I figured we might be able to watch Fever Pitch starring Jimmy Fallon together. That always cheers me up."

    mak "You..."

    scene yumiporn27
    with dissolve

    mak "Certainly have a strange outlook on what sort of things would brighten up someone’s day."
    mak "Why not just...buy her flowers and give her a shoulder massage if you’re so worried about her?"
    s "..."

    if bonus == True:
        s "I also thought I could get here before your shift started and actually purchase something from your mom."
    else:
        s "I'm afraid that I'd like the flowers too much and keep them for myself."

    mak "Why?...{i}Why{/i} do I like you so much?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yumiporn28
    with dissolve

    maki "So...you think you’ve got what it takes to be a porn saleswoman..."
    y "What? The fuck are you talkin’ about, lady? I just told you I don’t wanna fuckin’ work here."
    maki "Are you {i}sure{/i} you don’t want to work here? Or are you just saying that?"
    maki "Because, on the outside, a job like this might seem like a cesspool of debauchery...an unholy paradise of poon-"

    scene yumiporn29
    with dissolve

    maki "But what it really is...is a place where everyone is accepted! Where everyone is loved!"
    maki "Where no fetish is discarded! And no book is to be judged by its cover!"
    maki "Places like this shop are one of the last bastions of hope-"

    scene yumiporn30
    with dissolve

    maki "I’m sorry, what was your name?"
    y "..."
    y "Yumi."

    scene yumiporn31
    with dissolve

    maki "Well, Yumi...stick with me and I can guarantee you’ll see the light."
    maki "I know it might all be a little too intimidating to take in at once, but this job truly {i}is{/i} rewarding. People like my daughter and me are the unsung heroes of retail, you know."
    maki "No one likes to admit it, but as far as in-house sales go, no one is more likely to change a customer’s life than people like us."

    scene yumiporn32
    with dissolve

    maki "You’re a cute, [young]girl. I’m not sure what kind of family you come from or if they’d accept their daughter working a job like this, but I’d be willing to talk to them if you need me to. "
    y "Yeah...You don’t have to worry about talkin’ to my family or any shit like that."
    y "I still don’t know how I feel about workin’ in a place like this and, honestly, I still think it’s creepy as shit."
    y "But all that stuff about it bein’ a place where you can’t judge books by their cover...doesn’t sound all that bad, I guess."

    scene yumiporn33
    with dissolve

    maki "Right?! We’re all equals here! Me, you, and even the one woman who comes in once a week and buys nothing but vintage porno DVD’s starting with the letter Y! "
    maki "This is the holy grail, Yumi! I don’t know how much I can pay you, but if you’re willing to negotiate, I can have you start as early as next Monday night."
    y "Uhh...wait a second. I didn’t really agree to-"
    maki "I just need to know what kind of experience you have first."

    if bonus == True:
        maki "Does blood make you nauseous? What about comically large gangbangs or incest?"
        maki "Any hard limit on the size of a schlong before you start feeling nervous or worried about the pain and have to look away from the girl (Or guy) getting her (Or his) brains railed out?"
        maki "Also, can you agree to keep things confidential on the off chance that you find a family member or other loved one in a video?"
        maki "Because sometimes, whether we like it or not, people are forced to do things they’re not very proud of for money- and as a retailer in this industry, you need to be willing to be confidential about-"
    else:
        maki "How fast can you drive a go-kart?"
        y "A...go-kart?..."
        maki "Yes. I am forming a go-kart team with my daughter and you would be the third member."
        maki "Are you good at painting? How quickly do you think you could change a tire?"
        maki "Oh, and what do you think we should name it? I'd personally like to go with {i}Jimmy{/i} after my favorite character in Hero's Harem Guild."

    scene yumiporn34
    with dissolve

    maki "Wait! No! Don’t leave!"
    s "Excuse me, Makoto, but I think I have to go chase after Yumi now."
    y "Don’t bother! And never even think about bringing me somewhere as sketchy as this ever again!"
    maki "It’s not sketchy! It’s perfectly natural!"

    if bonus == True:
        maki "I am a good person! I’m making the world a better place, one orgasm at a time!"
        mak "MOM! STOP SAYING THAT!"
    else:
        maki "And what about the go-kart?!"

    scene black
    with dissolve2

    "Yumi is able to get away from me and, judging by the abruptness of her exit, I think it’s safe to assume she has no plan on working with the Miyamuras any time soon."
    "But hey, at least this time she made the conscious decision to not work somewhere instead of just being flat-out rejected."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets40 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label yumispecial45:
    scene yuminodoka1
    with fade
    play music "normalday.mp3"

    "Today’s story starts in the back of a familiar classroom- close to where the main character would sit if this were a run of the mill anime or manga series."
    "Fortunately for some and {i}un{/i}fortunately for others, {i}our{/i} protagonist is off doing something else right now."
    "But don’t worry! I’ll be here to keep you entertained until he makes it back."
    "I mean, what’s the sense in constantly following Sensei around if all of the interesting stuff is going to be happening here, right?"
    "This is no different from all of the other times we’ve spent together. "
    "I was just feeling a little friendly today."
    "..."
    "Who am I, you ask?"
    "Ha! "
    "Wouldn’t you like to know?"
    "Now, before we begin, I’d like to remind you that these are [teenage]girls we’re dealing with."
    "And sometimes, [teenage]girls tend to be impulsive or irrational or whatever else you want to call it. "
    "Do you see where I’m going with this?"
    "Sometimes, mountains are made out of molehills. And other times, things that are supposed to be perceived one way wind up being twisted into something entirely different."
    "But I’m sure you’re familiar with the concept of perception by now, aren’t you?"
    "You’re so smart."
    "Unless you’re one of those people who didn’t work for where you are right now, I mean."
    "Frankly, I wish those people would explode."
    "That’s something I’m allowed to say because you still have no idea who I am, or even the voice you’re supposed to be reading these words in."
    "But I won’t waste any more of your time dwelling on that- not when there are so many cute girls right in front of you!"
    "Now, which of these girls do you think will be the main character of this event?"
    "I guess there’s only one way to find out!"

    r "Do you guys think I’d look good with short hair?"

    scene yuminodoka2
    with dissolve

    f "Are you actually thinking of cutting it?"
    r "Mmm...I don’t know. Maybe? "
    r "Like half of the girls in this manga have short hair and they all look really cool and hot and stuff. {i}I{/i} want to be cool and hot and stuff."
    o "I already think you’re hot and stuff. But hey, follow your dreams and all that."
    r "Why did you leave out the part about me being cool?"

    scene yuminodoka3
    with dissolve

    o "So anyway, Futaba, you have any plans for Christmas? Rin and I were thinking about going to the urban district if you wanted to tag along."
    o "And if you’re worried about being the third wheel or something, just invite Nodoka along. I’m sure she’d be happy to be your date."
    no "Few things in life would make me happier."

    play sound "slidedoor.mp3"

    f "I’ll...be sure to check my schedule..."

    scene yuminodoka4
    with fade

    c "Oh, Yumi. I didn’t think you were going to show up today."
    y "Neither did I, but here I am..."
    y "The fuck are {i}you{/i} doing, though? Why’s it look like you’re about to leave?"

    scene yuminodoka5
    with dissolve

    c "Oh...you know...I was just gonna go...walk around and stuff..."
    y "If you’re looking for our douchebag teacher, I think I saw him near the library."

    scene yuminodoka6
    with dissolve

    c "See, this is why I keep you around. You always know exactly what it is I’m looking for."
    y "You do realize how fucking easy you are to read, right? No need to be impressed."
    c "Wanna come with me? Or are you going to hang out here?"

    scene yuminodoka7
    with dissolve

    c "Wait...don’t tell me {i}today’s{/i} the day..."
    c "Is it?"
    c "Is it finally happening?"
    c "Is my best friend taking her first step toward adulthood?"
    y "Okay, first off, can you word it in a way that makes it sound, you know, less fucking disgusting?"
    y "And second, I’ve taken plenty of steps toward adulthood. I watch your sister just as much as you do. Fuck, probably even more, actually."

    scene yuminodoka8
    with dissolve

    c "Yeah. You’ve been a huge help. "
    c "But I’m really proud of you for this, Yumi. I mean it."
    c "I feel like it was just the other day that-"

    scene yuminodoka9
    with dissolve

    if yumiknows == True:
        y "Yeah, yeah. Whatever. Just go back to stalking your totally legitimate boyfriend and stop being all mushy and shit. It’s gonna make me sick."
    else:
        y "Yeah, yeah. Whatever. Just go back to stalking our creepy fucking teacher and stop being all mushy and shit. It’s gonna make me sick."

    c "You know, it’s really impressive how you can still manage to be such a bitch even when you’re taking steps to improve yourself."

    if bonus == True:
        y "Don’t get too impressed. Wouldn’t want you falling for me instead of a dude twice your age."
    else:
        y "Don’t get too impressed. Wouldn’t want you falling for {i}me{/i} instead."

    c "Ew, I’m not going to fall for my roommate."

    scene yuminodoka10
    with dissolve

    if bonus == True:
        c "I’d let you join in if Sensei wanted, though."
    else:
        c "I’d let you join in on a group hug if Sensei wanted, though."

    y "Yo! Don’t even fuckin’ joke about shit like-"

    play sound "slidedoor.mp3"
    scene yuminodoka11
    with dissolve

    c "Bye, Yumi! I’ll let you know if you’re {i}needed{/i}~"
    y "...that."

    "As Chika wanders off to locate the object of her ever-apparent affection, the real main character of today’s event wanders into the classroom."
    "And, if you haven’t guessed by the obvious mentions of self-betterment and taking steps toward adulthood, that main character plans on doing something she should have done a long time ago."
    "Of course, a plan is just a plan- and until that plan is actually in motion, it’s no better than any of the many goals people set for themselves only to either fail or give up entirely."
    "So, who knows? Maybe she’ll do it, maybe she-"

    scene yuminodoka12
    with dissolve

    "Oh, look!"
    "There she goes!"
    "Come on! Let’s see what happens!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yuminodoka13
    with dissolve

    y "Yo."
    f "..."
    o "..."
    o "I think she’s talking to you, Futaba."
    f "Oh. Uhh..."

    scene yuminodoka14
    with dissolve

    f "{i}Are{/i} you...talking to me, Yumi?..."
    y "There a problem with that?"
    f "N-Not at all! It’s just...not how this normally goes..."
    o "Do you need something?"

    scene yuminodoka15
    with dissolve

    y "Why? You her gatekeeper now?"
    o "No, but if you’re just here to be mean to her, I see no reason for her to have to respond to you."

    scene yuminodoka16
    with dissolve

    y "Listen...can you like...come out into the hall for a second? There’s some shit I’ve gotta say to-"
    no "Anything you have to say to her can be said in front of all of us."

    scene yuminodoka17
    with dissolve

    y "Oh, great. Are {i}you{/i} her gatekeeper?"

    scene yuminodoka18
    with fade
    stop music fadeout 20.0

    no "I don’t think that’s what I’d necessarily call myself, but for the sake of the conversation, we can just assume that I am."
    f "Nodoka, I can-"
    r "Shh, no. Let Nodoka handle this. I feel like she can be really scary when she wants to be."
    y "Excuse me, fair lady, but could I trouble you for the permission to spend a few minutes alone with your princess?"
    no "Maybe if you try asking again without the unappreciated and irrefutably immature dose of sarcasm you decided to add in."
    y "..."
    y "I’m sorry, what’s your name again?"
    no "Nodoka Nagasawa."

    scene yuminodoka19
    with dissolve

    y "Hi, Nodoka. Nice to meet you. "
    y "Now, please step aside if you have any interest in keeping all of your teeth."

    scene yuminodoka20
    with dissolve
    play music "pianomelancholy3.mp3"

    no "Well, would you look at that? Only forty-five seconds in and you’re already resorting to violence."
    no "I knew from all I’ve heard that you were the type to jump to that right away, but I imagined we’d be able to talk for at least two minutes before any threats showed up."
    y "Listen, I don’t know who the fuck you think you are, but if I had business with you, I would have talked to {i}you.{/i}"
    y "I didn’t do shit, {i}Nodoka.{/i} So step the fuck aside and let me do what I came here to do without getting in the way."

    scene yuminodoka21
    with dissolve

    no "And what might that be? Because probability shows that it’s likely something along the lines of hurting my friend’s feelings in complete disregard for-"
    f "Nodoka...I’m glad that you’re standing up for me, but you really don’t have to do this..."
    no "No. No, I suppose I don’t."
    no "But that doesn’t change the fact that I am tired of this girl thinking she's allowed to just hurt you whenever her withered heart desires."
    no "So if she even {i}thinks{/i} about hurting you again, she’ll have to hurt me first."
    y "My fucking pleasure."
    r "Did Sensei say when he was coming back? Because I’m starting to think this might get bad."
    o "Uhh...let me see if I can find-"
    r "Wait, no! I need you here to protect me in case I somehow get roped into this. I’m a lover, not a fighter."

    scene yuminodoka22
    with dissolve

    y "I didn’t come over here to fucking fight! But if this four-eyed freak who thinks she’s being brave or something by confronting me wants to feel tough, I’ll give her what she wants!"
    no "I {i}want{/i} you to run back to whatever hole you crawled out of this morning and think long and hard about what you’ve done to this poor girl."

    scene yuminodoka23
    with dissolve

    y "That’s exactly what I’m fucking-"
    no "Who do you think you are, raising your voice when {i}you're{/i} the one constantly trampling all over everyone?"
    no "What gives you the right to hurt others? What gives you the right to hurt {i}Futaba?{/i}"
    no "Do you really feel so weak that the only way you can even {i}pretend{/i} to be strong is to tear good people who mind their own business down?"

    scene yuminodoka24
    with dissolve

    y "I...am not...fucking {i}weak.{/i}"
    y "Do you have any idea-"
    no "Oh, spare me the sob story."
    no "I’m well-read enough to know that this is the part where your character comes out and cries about her background in an effort to explain away her misdeeds."
    no "Thing is, I care a little too much about Futaba to be swayed by any of what you have to say. "
    no "So please do all of us a favor and just hit me instead of crying and risking getting your tears all over my uniform."
    y "That’s it. "
    y "You’re fucking dead."

    play sound "static.mp3"
    scene treefall1 with flash
    scene gymbully1 with flash
    scene futabagymtwo5 with flash
    scene showers12 with flash
    scene treefall1 with flash
    scene futabayumisnow21 with flash
    scene futabagymtwo5 with flash
    scene yuminodoka25 with flash
    stop sound

    y "What-"
    y "Let go of me!"
    t "Bullying is wrong. I will prevent this behavior in the absence of our teacher."
    r "Okay, that’s enough. Let’s sit back down, Nodoka. "
    r "I know you're just trying to help, but I think Futaba's enjoying this the least out of everyone right now..."
    f "Yumi...I-"
    y "I’m going to tell you one more time..."
    y "Let...me...go..."
    t "I’m sorry. I can not do that until I confirm that you will not be harming any of my classmates."

    scene yuminodoka26
    with dissolve

    y "Please..."
    t "..."
    y "Let me go..."
    t "..."
    no "..."

    scene yuminodoka27
    with dissolve
    play sound "slidedoor.mp3"

    t "..."
    no "..."
    t "I no longer sensed a threat..."
    r "Was...Yumi actually crying just now?"
    f "You were too hard on her, Nodoka..."
    no "Perhaps I was. "
    no "I just didn’t want to take any ch-"
    f "I...have to chase after her."

    scene yuminodoka28
    with dissolve

    no "What? Why? She’s done nothing but torment you the entire school year. I say you let {i}her{/i} wallow in misery for a change."
    f "That makes me just as bad as her..."
    no "It really doesn’t. "
    r "If you’re going to go, do it now. Wait any longer and I doubt you’ll be able to catch her."
    no "Futaba-"

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    f "I’m sorry, Nodoka...I have to..."

    "........."
    "......"
    "..."

    scene yuminodoka29
    with dissolve

    f "Yumi! Wait!"
    y "The fuck do you want, fatass?! You know I was just going to make fun of you again, right?!"
    f "I know that’s not true!"


    scene yuminodoka30
    with dissolve

    f "You’ve always just...done that in front of whoever was around."
    f "It’s not something you’d have to get me alone for..."
    y "Yeah, well...this time it was! Now, beat it!"

    scene yuminodoka31
    with dissolve

    f "Yumi, I’m sorry!"
    y "Wha- for what?! The fuck do {i}you{/i} have to apologize for?!"
    f "For Nodoka! She went too far! I didn’t want her to do that!"
    f "I was open to...talking."

    scene yuminodoka32
    with dissolve

    y "Yeah, well...tell that to your fucking girlfriend next time."
    f "Can you please just...stop for a second and talk to me?..."

    scene yuminodoka33
    with dissolve

    y "..."
    f "...Please?"
    y "..."
    y "Yeah, alright. Whatever."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yuminodoka34
    with dissolve

    f "..."
    y "..."
    f "What..."
    f "What did you want to tell me?..."
    y "..."
    y "So, uhh..."
    y "I don’t really know how to do this kinda shit, so if it sounds like I’m makin’ fun of you or whatever, that’s...not what I’m tryin’ to do."
    y "I, uhh..."
    y "I know I’ve been a huge dick to you and whatnot..."
    y "And apparently it’s bad enough that your friends are worried about me even being {i}near{/i} you now..."

    scene yuminodoka35
    with dissolve

    y "Hah...pretty pathetic, right? Not for you. For me, I mean. "
    y "I deserve it, though."
    y "I’ve been treatin’ people like shit for my entire life. It’s just...kind of what I’ve always done."
    y "And I know it should be like common sense or whatever to not pick on people...but it woulda been nice if there was like...someone who woulda told me that early on, you know?"

    scene yuminodoka36
    with dissolve

    y "I...I’m not tryin’ to make excuses! I just know that...I’ve been really fucked up to you and..."
    y "And I guess what I wanna say is that I’m gonna try and be like...less fucked up to you or whatever..."
    y "And..."

    scene yuminodoka37
    with dissolve

    y "And I’m like...sorry and shit..."
    f "..."
    y "..."
    y "I don’t expect you to just forgive me after all this time, but I’m like..."

    scene yuminodoka38
    with dissolve

    y "Uhh..."
    y "Let’s just say I’m starting to get a little worried about how I might end up if I don’t start changin’ shit."
    f "I forgive you."

    scene yuminodoka39
    with dissolve

    y "What?! No, hold up. That was way too fuckin’ easy. You’re supposed to hate me."
    y "Like, look at that Nodoka girl. I didn’t speak a word to her at all until today and she fuckin’ {i}despises{/i} me. If anyone should hate me even more than that, it’s you."
    f "You’re right. "
    f "I should hate you more."

    scene yuminodoka40
    with dissolve

    f "I lost track of how many times things you’ve said to me have made me cry or...run to Sensei’s office for help or..."
    f "Or just acknowledgment that I'm more than all of those horrible insults."
    f "And I’d be lying if I said I never wished you would transfer to a different school or something."
    y "I would've wished a lot worse than that if I was in your shoes."

    scene yuminodoka41
    with dissolve

    f "But even with that...I still forgive you."
    y "But...{i}why?{/i} I don’t get it."
    f "Does there need to be a reason?"
    f "I just do."
    y "..."
    f "..."

    scene yuminodoka42
    with dissolve

    f "I’m...gonna go back to class now. But...I’m glad we were able to talk."
    f "And I’m sorry again for Nodoka."
    y "..."
    y "Oh, okay. Uhh..."
    y "I guess...see you around then?"

    scene yuminodoka43
    with dissolve

    f "Yeah."
    f "See you around."

    scene yuminodoka44
    with dissolve

    y "Hah..."
    y "..."
    y "..."
    y "..."

    play sound "slidedoor.mp3"
    scene yuminodoka45
    with dissolve

    s "..."
    y "..."
    s "I heard all of that, you know."
    s "I’m really proud of you."
    y "Suck my dick, asshole."
    s "So proud."

    scene yuminodoka46
    with dissolve

    y "..."
    y "Apologizing to people is fuckin’ exhausting."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yumispecial45 = True
    stop music fadeout 5.0

    "{i}Yumi will no longer bully Futaba!{/i}"
    "{i}Hopefully!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label yumislumber1:
    if tsuneyoslumber3 == False:
        scene mayanebench30
        with dissolve

    play sound "phonebeep.wav"

    "I tap on Yumi’s name in “my” phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    y "Uhh...hello?"
    s "Hey."
    y "Who the fuck is this?"
    s "Your teacher. I’m calling you from my new secret phone number."
    y "Um...congrats?"
    y "The fuck you want? Why you callin’ me?"
    s "Maybe I just miss you?"
    y "And maybe I’ve gotta find someone willin’ to give me one of those lobotomy things so I can forget I ever heard that. Later."
    s "Wait. On a serious note, are you busy right now?"
    y "Yeah."
    s "With what? You’re unemployed and don’t have a house."
    y "And you’re a fucking douche nozzle! I’m hanging up now!"
    s "Stop whatever it is you’re doing. We need to meet up and continue our conversation from the beach. It’s important and...apparently {i}time{/i}-sensitive."
    s "That was a hilarious pun that you won't understand. But hopefully, you will soon."
    y "Can't. Chinami's got a fever. You want me to leave her alone so I can come talk to {i}you{/i} about my random ass memory issues?"
    s "Chinami’s sick?"
    y "Yeah. And I’m stuck at {i}your girlfriend’s{/i} house watchin’ her until the mall closes and Chika comes back home."
    s "Great. I’ll meet you there."
    y "The fuck you will! Were you not payin’ attention when I told you Chinami’s sick?! She needs rest!"
    ch "{i}Is that Chinami’s papa?! The new one, not the one who abandoned her!{/i}"
    y "No! It’s the fucking...bank."
    ch "{i}Did Chinami’s recent deposit clear?{/i}"
    s "I’ll see you soon, Yumi."
    y "Don’t you fucking-"

    if tsuneyoslumber3 == False:
        scene black
        with dissolve

    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I hang up the phone and begin to make my way over to the second half of town."
    "Thankfully, I am no longer completely bewildered in terms of my location and am able to make it to the bus stop without any issues at all."
    "And while I’d normally just bite the bullet and walk there, I’m admittedly a little worried about Chinami and would like to make sure I see her at least one more time before she dies. "
    "I kid, of course. Kind of."
    "I don’t know."
    "Maybe Maki’s morbid sense of humor has just rubbed off on me after all the time I spent with her during Makoto's tragic arc."
    "Regardless, I double check the bus schedule on my new backup phone and take a seat on the bench, waiting patiently for it to arrive and carry me toward my current goal."
    "Here’s hoping Yumi likes sleepovers."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene yumicurtain1
    with dissolve2
    play music "normalday.mp3"

    s "Hey, I’m here."
    y "Yeah, I can see that! The Hell do you think you are, just walkin’ into somebody else’s house?!"
    s "In my defense, it’s not like you didn’t know I was coming."
    y "That doesn’t make it okay! Go back out there and knock or ring the bell like a normal person!"
    s "But if I do that, you’ll lock me out."

    scene yumicurtain2
    with dissolve

    y "Tch. Was hopin’ that would work."
    s "On the bright side, I’m glad to have made it before visiting hours ended. How’s the patient?"

    scene yumicurtain3
    with dissolve

    y "Chinami, how are you?! "
    ch "Chinami is fine! Hi, Papa!"
    s "Where did you get such a huge privacy curtain? That’s like, straight out of a hospital."

    scene yumicurtain4
    with dissolve

    y "Probably because it {i}is{/i} straight out of a hospital. Shit’s been here longer than I have. "
    y "Pretty sure they’ve had it ever since Chinami was born on account of her whole immune thingy."
    ch "Chinami used to spend a lot of time behind her safety curtain, but now she only has to use it some- {i}ack!..keh...{/i} "

    scene yumicurtain5
    with dissolve

    y "Hey! Go back to sleep! You know you ain’t gonna get any better if you get all excited and sh...and crap."
    s "That really isn’t much better, Yumi."
    ch "Chinami is fine! She just swallowed a bug!"

    scene yumicurtain6
    with dissolve

    y "Just ignore her. She’ll go back to sleep if we don’t pay any attention."
    s "Is keeping her here okay? Wouldn’t it be better to take her to a hospital or something?"

    scene yumicurtain7
    with dissolve

    y "With what money? Tsukasa ain’t paid me yet and you know damn well how much Chika’s got."
    s "I’m sure the Tsukiokas wouldn’t mind fronting the bill if it meant keeping Chinami healthy."
    y "It’s fine. Shit like this ain’t all that uncommon. Just a normal cold or somethin’. I’ve been givin’ her medicine and her fever’s already started to break and whatnot."
    s "Good. It’s not every day I get to see you being responsible. I like this side of you, Yumi."
    y "Only side of you I like is the...one outside of this apartment."
    s "Good one. "
    y "Suck my left nut. Why are you even here? What do you want?"
    s "I told you on the phone, didn’t I? We need to resume our conversation from the beach."

    scene yumicurtain8
    with dissolve

    y "Probably better off just startin’ from the beginning. Shit confused me so much I can barely even remember what it is we were talkin’ about."
    y "Somethin’ with the last two months, right?"
    s "Right. Did you try talking to anyone else about that after I ran off last night?"
    y "Only person I have to talk to is Chika and it seemed like everything was pretty fuckin’ normal from her point of view. Meanin’ it’s probably only me who-"

    scene yumicurtain9
    with dissolve

    y "Wait! You didn’t give me your fuckin' memory disease, did you?!"
    ch "Yay! Chinami won’t be alone in the safety curtain! She’ll make room for big sis Yumi right now!"
    s "I didn’t give you a {i}disease{/i}, Yumi."
    ch "Aww, rats..."
    s "But just because you’re not terminally ill doesn’t mean this is something we can ignore. "
    s "Well...I guess technically we {i}could{/i} ignore it and it wouldn’t make much of a difference to you. But it would be a big help for me and a couple other people if you could at least listen for a little while."

    scene yumicurtain10
    with dissolve

    y "Okay. So {i}you{/i} want {i}me{/i} to take time out of {i}my{/i} life so that {i}your{/i} life can get better or some shit...while I don’t benefit at all. Am I hearin’ that right?"
    s "More or less."
    y "Gotcha."
    y "Welp, you know where the door is."
    s "Yumi, come on. Just hear me out."

    scene yumicurtain11
    with dissolve

    y "Ahhhhh, fine! But the second this gets too friggin’ weird I’m calling Gary!"

    scene black
    with dissolve

    s "Great. Thank you — wait, who’s Gary?"

    "........."
    "......"
    "..."

    scene yumicurtain12
    with dissolve2

    "I help myself to a pot of coffee left out on the kitchen table and quickly come to understand that this was definitely not made anytime within the last six hours."

    y "You gonna microwave that shit or just pretend it’s drinkable?"
    s "I made this bed and I now have to lie in it. But that is beside the point."
    y "Mhm. And the point is?"
    s "..."
    s "How do you feel about sleepovers?"

    scene yumicurtain13
    with dissolve

    y "Why do you exist?"
    s "Actually, it’s funny you should ask because that’s a big part of why I’m here today."
    y "It’s like every single thing you say makes shit ten times more confusing."
    s "Then I’ll fulfill your greatest wish and shut up while you do your best to recollect the last two months of your life."

    scene yumicurtain14
    with dissolve

    y "Looks like we’re both gonna shut the fuck up, then. Cause that’s exactly what I was tryin’ to do ever since you pointed shit out and I’ve got nothin’."
    y "If you know what’s goin’ on with me, fucking spill it. Because all the shit I keep hearin’ about the space between Halloween and Christmas is makin’ my head spin."
    y "Didn’t think much of it at first, but I straight up can’t even picture any of it when I try to. It’s like all that time was just fuckin’...ripped outta my mind or somethin’."
    y "That what it’s like for you too? You know, with all your memory shit."

    scene yumicurtain15
    with dissolve

    s "More or less. Just it’s a lot more than two months for me and I also, occasionally, do things like black out and force myself on teenage girls."
    y "Those “blackouts” have somethin’ to do with it too? That shit ain’t gonna start happenin’ to me next, is it?"
    s "I have no idea. And I’m probably not even the right person to lead a conversation like this since I have very little understanding of how {i}anything{/i} works."
    s "But you’re an outlier right now...so I do know that the logical course of action would be trying to figure out {i}why.{/i}"
    y "The fuck is an “outlier?”"
    s "Something that skews what’s meant to be an average."
    s "For example, if we calculated the mean age of everyone in class, {i}I{/i} would be the outlier since I’m way older than all of you and would force that mean upward."

    scene yumicurtain16
    with dissolve

    y "Good. So you {i}do{/i} understand that. Now think long and hard about why that makes you such a fucking creep."
    s "I have plenty of time to think about how horrible of a person I am. But, for reasons I am mostly incapable of explaining, you might not have equal time to do the same when it comes to this."

    scene yumicurtain17
    with dissolve

    y "Huh? I ain’t gonna, like...die or some shit, am I?"
    s "Nothing that serious, no."
    y "Then what? My memories just gonna, like...come back or something?"
    s "They might."
    y "I ain’t seein’ what the big deal is, then."
    s "Would you see the “big deal” if I told you those two months may have never even happened in the first place? And that everyone’s memories of it were just false?"
    y "Uhh...no. But I {i}would{/i} call you a fucking lunatic."
    y "If everybody’s got memories of those months and it's just you and me who don’t, wouldn’t {i}we{/i} be the ones...in the wrong or whatever?"
    s "This is less about who is wrong and who is right and more about {i}why{/i} we’re in the position we’re in."
    s "Isn’t it strange knowing there could be something different about you, Yumi?"

    scene yumicurtain18
    with dissolve

    y "Not...really."
    y "I’ve been different my whole fuckin’ life, man. And I’ve been hearin’ all about it since the first time I knocked somebody’s lights out in daycare."
    y "Might’ve wound up a better person if somebody looked after me now and then, but I’m well adjusted to not fitting in already."
    s "This is different, though. This is-"
    y "No shit it’s different. This is like, some...borderline supernatural shit."
    y "But if {i}you’ve{/i} got no idea why this is happenin’ and everybody {i}else{/i} is just gonna be weird if we try and talk about it, the Hell’s the point in even trying in the first place?"
    y "Can’t say I’d feel the same way if I lost as much time and memory as you, but it’s just two months. And those two months weren’t really all that bad from what I understand."
    y "Wound up back in school, didn’t I? That’s gotta be a plus, right?"
    s "Is that what you wanted, though? I thought you were planning on dropping out?"
    y "I..."
    y "I don’t know. Last I remember, I was still trying to figure shit out."
    s "I’m surprised you’re okay with the universe just deciding things for you, then."

    scene yumicurtain19
    with dissolve

    y "Nobody decided shit for me. The only person who chooses what I’m gonna do is myself."
    s "Then what will you do if this happens again?"
    s "What will you do if there’s {i}another{/i} huge leap in time that just sets you on autopilot until you’re eventually spat back out into the world?"
    y "Fuck if I know. But as long as I’m not blackin’ out and doin’ shit like-"
    s "Maybe that {i}is{/i} what happened in those two months."
    s "Maybe {i}both{/i} of us blacked out and things just...didn’t go as poorly as they could have."
    s "We were together, weren’t we? It’s possible."
    s "One second, everything was normal. Or at least as normal as it {i}could{/i} have been with me admitting all of that stuff about masturbating to you and whatnot-"

    scene yumicurtain20
    with dissolve

    y "Stop bringing that up!"
    s "And the next second, two months of our lives were gone."
    s "If you’re okay with that happening again, fine. Disregard everything I’m saying and just keep living life the way you always do."

    scene yumicurtain21
    with dissolve

    s "But if you want to take some control back into your {i}own{/i} hands...and don’t want to have any more time taken away from you...why not try and figure this out with me?"
    y "The fuck you bein’ all serious for? It’s makin’ me uncomfortable."
    y "'Sides, the Hell can {i}we{/i} do about this in the first place? You might be smart or whatever, but you ain’t a doctor."
    s "No, I’m not. Nor am I whatever type of scientist handles time travel or...even a {i}teacher{/i} most of the time."
    s "But I’m someone who won’t think you’re insane when you want to talk about things you don’t particularly understand."
    s "I don’t know if I can {i}help{/i} you, per se...but I might be able to help you feel a little less alone."
    y "..."
    s "Which is why I need you to sleep at my house."

    scene yumicurtain22
    with dissolve
    play sound "dooropen.mp3"

    y "Of fucking course that’s what it all comes down to. No idea why I let you just keep talkin’ me into a fuckin’ corner for so long."
    y "Hell of a charade, I’ll give ya that much. But if you’re really gonna try and {i}win me over{/i} or whatever-"
    c "Sensei? What are you doing here?"

    scene yumicurtain23
    with dissolve

    y "B-Better question...what are {i}you{/i} doing here? I thought you had work?"
    c "I was able to get somebody to cover for me. Did {i}you{/i} invite Sensei over?"
    y "Course not. Dude just fuckin’ waltzed in as if he owned the place."

    scene yumicurtain24
    with dissolve

    c "So...you’re {i}not{/i} having an affair?"
    y "Obviously not! No!"

    scene yumicurtain25
    with dissolve

    c "Great! Then it should be totally fine if I do this!"
    y "Do what? What are-"

    $ renpy.end_replay()
    $ yumislumber1 = True

    jump yumislumber2

label yumislumber2:
    scene chickenscene1
    with fade

    y "Oh. Okay. Guess I’ll just go fuck myself."
    c "Hi~ Did you come all the way over here just to surprise me?"
    s "..."
    s "Yes. You got me."
    c "That’s so sweet. And it makes me forget all about how you haven’t responded to me all morning."
    s "I didn’t have my phone on me."
    c "Ooh...So that hard lump I’m feeling in your pants right now is..."

    scene chickenscene2
    with dissolve

    s "That...would be my penis."
    c "It feels more rectangular than normal."
    s "That’s the way it’s always been. I'm sensitive about it."
    c "Uh-huh. Kiss me."
    s "We probably shouldn’t in front of company-"

    scene chickenscene3
    with dissolve

    c "Chu~"
    y "Oh, come on! Not at the table! I eat there! And even {i}your boyfriend{/i} tried turning it down! That’s basically assault!"

    scene chickenscene4
    with dissolve

    "When in Rome, I guess."

    c "Mmf...mm...mhlm~"
    y "..."
    c "Hmngh.......hm.....nn~"

    scene chickenscene5
    with dissolve

    c "Okay, I’m done. Just needed to recharge my battery a little. "
    c "Unfortunately, that’s {i}all{/i} I can do today as I’ve gotta take care of Chinami now. Which means having {i}you{/i} get the heck out of here."

    scene chickenscene6
    with dissolve

    y "Wait, you sure? I've got shit under control, you know. Ain’t so much as let her out from behind the curtain all day."
    c "And you’ve been a big help, but she’s still {i}my{/i} responsibility. And now that I’m done with work, you can go do something you actually enjoy instead of being cooped up in here all day."
    y "But...I don’t enjoy anything. This is what I do."
    c "Why not hang out with Sensei, then?"

    scene chickenscene7
    with dissolve

    s "Great idea, Chika. But I’m only okay with this because it was {i}your{/i} idea and I would never go out of my way to seek out Yumi on my own."
    c "Can it. I know you guys are friends."
    y "We are not! Just kick him outta here and I can chill with you and Chinami instead!"
    c "Mmm...no. Take a day off. We still don’t even know how she {i}got{/i} sick in the first place. What if it was you? We were {i}all{/i} at the beach yesterday, so it’s possible something might’ve come home with you."
    y "It was probably that fuckin’ brat and her mom when they came over here to watch her yesterday! Why’s it gotta be me?!"
    c "You’ve seen the Tsukiokas' place, haven’t you? They’re all total clean freaks. Touka washes her hands after basically every single thing she touches."
    y "Chika-"
    c "Why even fight me on this? Just go for a walk around the block or something. It’s really no big deal."
    s "If that is what must be done..."
    y "I-"

    scene black
    with dissolve2

    c "No more excuses! Besides, if you two start spending a little more time together, you might not feel pressured to always put on an act in front of me!"
    y "It ain’t an act! I seriously despise the dude!"
    s "But just yesterday you said we’d be best friends forever."
    y "Stop playing along!"

    stop music fadeout 10.0

    "Somehow, Chika manages to force the two of us out of the house so she can take care of her sister. And while it’s not quite how I envisioned this going, I take it as a sort of blessing in disguise."
    "Surprisingly enough, Yumi doesn’t take off running as soon as the front door opens. Which tells me she is currently facing one of the following predicaments."
    "Option A) She actually does want to hang out with me. (This is the least likely option)"
    "Option B) She is dumbfounded by her best friend’s newfound affinity for aggressively thrusting the two of us together and simply doesn’t have it in her to run. (This is the most likely option)"
    "Or Option C) She’s going to give me more time to try and explain exactly what I need from her and what she has to do next."
    "I’d be happy with either A or C, but it’s {i}C{/i} that would make all of this a thousand times easier. And it’s C that has the greatest potential to fail."

    scene chickenscene8
    with dissolve2
    play music "blueair.mp3"

    "Which is why it’s important I choose my next words wisely."
    "For in the silent walk from Point A to Point B, the slow, vine-like creep of an unfortunate realization begins to entangle my limbs."
    "This realization has naught to do with a task that I have been given nor the now-ingrained responsibility to move things forward-"
    "The thing that I unfortunately realize is that I am afraid of losing Yumi."
    "And that even if a new one were to spawn in her place, without memories the universe deems as flawed or unnecessary, she would only be a shell of her former self. "
    "The real Yumi knows something is wrong, she just doesn’t know {i}why{/i} or {i}how{/i} or where to go from here. And neither do any of us."
    "But if you take that away, she’s just like everyone else again."
    "She’s no longer an outlier."
    "And while some people might feel more comfortable with that, I am not one of them."
    "The most unfortunate part of this unfortunate realization is how unfortunate it is that I’ve been neglecting that all along."
    "And that many of the bodies I have taken under the covers of my bed have been nothing more than factory-painted, plastic Easter eggs."
    "They may all look the same, but they are all empty."
    "And this egg still has the potential to hatch."
    "Or sour."
    "Whatever comes first."

    y "..."
    s "..."
    y "We just gonna fuckin’ sit here?"
    s "For now. It’s not like either one of us knows what to talk about."
    y "Not gonna keep trying to coerce me into...sleeping at your house or whatever the fuck was going on back at Chika’s place?"
    s "A change of strategies is in order if you’re ever going to go along with it. I just haven’t figured out what the new strategy entails yet."
    s "We can just stay quiet in the meantime while I work that out in my head."
    y "The fact that you’re callin’ it a “strategy” tells me pretty much all I need to hear. Still ain’t got any interest in coming to your house and that ain’t gonna change."
    s "It’s really not how it sounds, Yumi."
    y "Good. Cause it sounds a lot like you tryin’ to take advantage of me again and I thought we were done with that shit."
    s "We are."
    y "You promise?"
    s "Do promises actually mean anything to you?"
    y "..."

    scene chickenscene9
    with dissolve

    y "Not really."
    y "When I was still a little brat, not even the same size Chinami is...my douchebag mom promised she’d take me to Okinawa for my birthday."
    y "But she was so fuckin’ high at the time that she probably didn’t even remember {i}makin’{/i} the promise."
    y "Least believin’ that makes it easier to accept than her just...decidin’ not to take me once my birthday actually rolled around."
    y "Haven’t cared much for promises ever since, so I’m not really sure why I asked you in the first place."
    s "You were probably just looking for another reason to distrust me. Calling it a promise would make it easier to do that for you."
    y "Probably. Sounds on brand."
    s "Why Okinawa?"

    scene chickenscene10
    with dissolve

    y "..."
    s "Should I not have asked?"
    y "You’ll make fun of me. I don’t wanna tell you."
    s "I’d promise not to, but then you {i}really{/i} wouldn’t want to tell me."
    y "Probably."
    s "..."
    y "..."
    s "Do you still want to go?"
    y "Can’t. We’ve got that huge ass wall now, remember?"
    s "If the wall was gone and we were able to leave, I mean."
    y "Ain’t the first time you asked me somethin’ like that, you know. Happened on the roof. "
    y "Shit feels like years ago at this point."
    s "Maybe it was."
    y "..."
    s "How many birthdays have you had since you joined my class?"
    y "..."
    y "More than...makes sense."
    s "Do you think anyone would call you crazy if you pointed that out?"
    y "Probably. It {i}is{/i} crazy."
    s "Try. Because I guarantee you they won’t think anything of it."
    s "And up until recently, you would have felt exactly the same as them."
    s "{i}That{/i} is why I’m trying to get you on my side. It has nothing to do with my desire to sleep with you."
    y "The fuck is going on?..."
    s "We’re stuck. "
    y "Of course we're stuck. That's the whole fuckin' point of the wall."
    s "Not in Kumon-mi...in {i}time.{/i} Which I know sounds ridiculous, but it's the truth."
    y "That ain’t possible. Sounds like...somethin’ from a manga or some shit."
    s "It does, doesn’t it?"
    y "..."
    s "..."
    y "Sea turtles..."

    scene chickenscene11
    with dissolve

    s "What?"
    y "I wanted to see the sea turtles...in Okinawa."
    y "There was this documentary I saw on TV where they went to Tokashiku Beach...and I heard them say I’d be able to see one too if I went there at the right time."
    y "And even though October ain’t the “right” time...I still thought I might be able to see one if I got lucky or something."
    y "Maybe there was a turtle out there who was behind schedule or...didn’t really understand how months worked or whatever. I don’t know. It’s stupid. "
    y "{i}I’m{/i} stupid."
    y "For havin’ such a...dumb fucking wish...and for trustin’ somebody like my mom to make it happen..."
    y "It’s all so fuckin’ stupid."

    scene chickenscene12
    with dissolve

    s "It’s not."
    y "It is. You know it is."
    s "No, it’s an innocent wish. And not something I would have expected from you."
    y "..."
    s "I’d take you myself if I could."
    y "Don’t say that..."
    s "I mean it, though."

    scene chickenscene13
    with dissolve

    y "Me too!"
    y "It’s bad enough bein’ let down by one person! I ain’t gonna get my hopes up a second time just because you wanna be a knight in shining armor!"
    y "For all we know, we might not ever be {i}able{/i} to leave! This city might stay closed forever! You’d be makin’ plans you couldn’t possibly keep! "
    y "I’m done believin’ in other people! I’ll go there {i}myself{/i} if I ever have the chance! Not with you! Not with anyone!"

    scene chickenscene14
    with dissolve

    s "Ah..."
    s "So you {i}do{/i} still want to see them."
    y "Of fucking course I do..."
    y "Dreams don’t just go away. They keep comin’ back until you either make ‘em come true or...find somethin’ else you want instead."
    y "So what if I ain’t ever found anything else? And what’s it even matter in the first place? Ain’t like people like me are good at makin’ shit like that come true."
    y "The fact that there’s anything I want at all is a fuckin’ joke. And if I believed in God, I’m sure he’d tell me the same exact shit."
    y "Somethin’ like, “You need to be good to others if you want good things to happen to you,” or whatever the fuck it is that adults tell kids with anger issues ‘stead of actually teachin’ em how to...not be angry."
    s "Whatever the case...I hope you make it to Okinawa someday."
    y "..."
    y "Thanks, I guess...and sorry for yellin’ at you."
    y "Ain’t ever told anybody that before."
    s "Not even Chika?"
    y "Never came up, I guess..."
    s "I see..."
    y "..."
    s "..."
    y "I saw her the other day, you know."

    scene chickenscene15
    with dissolve

    s "Chika?"
    y "No, my fucking mom. Idiot."

    scene chickenscene16
    with dissolve

    y "Though, I guess “the other day” is two months ago at this point."
    y "I was stayin’ at my dad’s place for a while since I didn’t have anywhere else to go and...I guess she caught wind of it and showed up."
    y "And, honestly...it went...kinda good. She wasn’t pissed that I got kicked out of school and didn’t call me a letdown or any of that shit..."
    y "Just told me I was doin’ a good job and that Nodoka probably deserved what she had comin’ to her. Which she did."
    y "Wasn’t just her either. Kaori was there too. Was the first time I talked to her in years."

    scene chickenscene17
    with dissolve

    y "Did you know it was her birthday on Christmas? How fuckin’ wild is that? "
    y "People used to talk about how weird it was that we were both born on such big holidays, but I feel like she’s the one who got the short end of the stick, all things considered."
    y "Ain’t nobody gonna remember someone’s birthday if it’s on fuckin’ Christmas. Halloween’s easy cause it ain’t that big of a deal."
    s "What was it like getting to talk to her after so long? Is she anything like you remember?"

    scene chickenscene18
    with dissolve

    y "She, uhh..."
    y "I was kinda expectin’ it after seein’ her with you that one time, but...she ain’t exactly “all there” anymore."
    y "Wasn’t ever really {i}normal{/i} by any means, but...she’s different now. Don’t think she really remembers me either, which ain’t as hard on me as I expected it to be...but still."
    y "Kinda surreal seein’ somebody you thought was dead just...suddenly alive and full of energy. Almost {i}too{/i} much energy, if you ask me."

    scene chickenscene19
    with dissolve

    s "That is certainly one way to describe her, for sure."
    y "..."
    s "..."
    s "Do you want her number?"
    y "Kaori’s? Why?"
    s "To talk to her, obviously. "
    y "I literally just told you she doesn’t remember me. "
    s "So remind her. That’s what your mom did and the two of them are relatively close now. "
    y "Yuki’s just tryin’ to right all the wrongs she made with me by latchin’ onto somebody else who’s lackin’ a mother figure. Does the same shit with Io if what I’ve heard is true. "
    s "Maybe. But I don’t see why that should prevent you from having a relationship with Kaori."
    y "I don’t need another “relationship.” Chika’s more than enough for me. And that’s not even countin’ whatever the fuck is goin’ on between us."
    s "What {i}is{/i} going on between us?"
    y "Fuckin’...time travel or some shit apparently. Ain’t like {i}I’ve{/i} got a fuckin’ clue."
    s "Take her number, Yumi. I’m obviously not one to tell you what is and {i}isn’t{/i} good for you, but it’s not like I’m asking you to call her."
    s "You’ll just...be able to if you ever feel like it."

    scene chickenscene20
    with dissolve

    y "Hah..."
    y "I guess if it’ll get you off my fuckin’ back, I’ll-"

    scene chickenscene21
    with dissolve
    stop music fadeout 3.0

    y "Huh?..."

    scene chickenscene22
    with dissolve

    s "Is something wrong?"
    y "Do you...see that?"
    s "See what?"
    y "Over there...at the end of the aqueduct. "
    s "I don’t see-"

    scene black
    with dissolve

    s "Wait, where are you going?"
    y "To check out what the fuck that is, obviously. Stay here if you’re gonna be a fuckin’ pussy about it."

    "Yumi takes off toward the end of the aqueduct, and as I lift myself off of the ground to follow her, I notice whatever it is she sees."
    "........."
    "......"
    "..."

    scene chickenscene23
    with dissolve2

    y "..."
    s "..."
    y "How the fuck?..."
    s "..."
    y "Since when do we have wild chickens in Kumon-mi?"

    play sound "static.mp3"
    scene chickenscene24
    with flash
    stop sound
    $ renpy.pause(5, hard=True)

    s "That’s not a wild chicken..."
    s "That’s someone’s pet."

    $ renpy.end_replay()
    $ yumislumber2 = True

    play sound "eggcrack.mp3"
    scene gamechicken
    $ renpy.pause(10, hard=True)

    jump yumislumber3

label yumislumber3:
    play sound "static.mp3"
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene thisisgreen4 with flash
    scene thisisgreen5 with flash
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene thisisgreen4 with flash
    scene thisisgreen5 with flash
    scene yuminightschool1 with flash
    stop sound
    play music "amiawake.mp3"

    s "..."
    y "Welcome back."

    scene yuminightschool2
    with dissolve

    s "Are we at...school? When did we get here?"
    y "Somewhere in the time between your brain clockin’ out and then gettin’ called back in to work, I guess."
    y "Lasted a fuckin’ while this time. Guess it ain’t much compared to two months if that’s really what happened, though."

    scene yuminightschool3
    with dissolve

    s "And you stayed with me?"
    y "Looks that way. Ain’t like I had anything else going on after Chika kicked me out."
    y "But just because I didn’t leave you in some dried-up aqueduct with a decomposing chicken doesn’t mean I suddenly like you."
    s "Really? Because that’s my go-to benchmark for deciding whether or not I’m close to someone."

    scene yuminightschool4
    with dissolve

    y "Ha ha ha. Eat an entire bag of dicks."
    s "Why {i}here?{/i}"
    y "Fuck if I know. You kept sayin’ some shit about a box and, before I knew it, you were draggin’ me all the way across town and unlocking the gate."
    y "Fine by me since there’s food here and shit. But I ain’t sure if it’s a good look for you to be wanderin’ around the halls with a delinquent after hours."
    s "You’re no longer a delinquent, though. Auto-pilot Yumi reformed herself during your two months of absence."
    y "You say that as if you were there."
    s "I kind of wish I was. Prefect Yumi is a sight I don’t think I’d ever be able to see otherwise."
    y "No one said anything about bein’ a prefect. For all we know, I was still an asshole. Just a...more present asshole, I guess."
    s "Did I say anything else about a box?"

    scene yuminightschool5
    with dissolve

    y "You actually have an idea of what that means? Cause I kinda figured it was just mindless blackout shit."
    s "Yes and no. It’s hard to explain."
    y "Yeah, what else is fuckin’ new? This has quickly become the weirdest week ever and that’s in no small part to gettin’ dragged along in a day of the life of the world’s most open sex offender."
    s "This is probably the first full day we’ve spent together, isn’t it?"
    y "Depends on whether or not you count the last three hours as “you.” "
    y "Also, don’t go makin’ it sound like this was enjoyable for either one of us. Woulda had more fun stayin’ at home helpin’ Chika keep her sister alive."
    s "Go do that then. I can survive without a chaperone."

    scene yuminightschool6
    with dissolve

    y "..."
    s "..."
    y "If I go...what’ll happen if you zone out again?"
    s "Are you actually worried about me?"

    scene yuminightschool7
    with dissolve

    y "N-No! Why the fuck would I ever worry about {i}you?!{/i} I just meant I...I don’t really care about us bein’ alone anymore. I can hold my own if you decide to get all fucking...well...you know how you get."

    scene yuminightschool8
    with dissolve

    y "Plus, we...kinda left off at a weird spot and...guess I’m still a little interested in whatever this whole memory shit is."
    y "I’m just hangin’ around ‘cause I want answers. And if anybody’s got answers, it’s you."
    s "What made you change your mind? Because it seemed like you were barely even listening earlier."
    y "You just suck at explainin’ shit. Obviously I’m gonna be interested if weird, supernatural-ish shit starts happenin’ to me. I just ain’t sure if we can, like...do anything about it yet."
    y "But if you’ve got ideas...I can, like...listen or whatever. Even if you’re just fuckin’ with me. Which you probably are. But at least it’s a little...entertaining, I guess."
    s "..."
    y "..."
    s "You’re hungry, right?"
    y "Kind of. Was too busy makin’ sure you didn’t walk into oncoming traffic to stop and eat."
    s "Then how about we continue this conversation in the cafeteria?"

    scene black
    with dissolve2

    "Something feels different."
    "Dangerous, even."
    "But the danger surprisingly does not lie in my own hands and their ability to effortlessly pluck the petals from premature flowers."
    "It lies in the air."
    "I can feel it becoming tangible...twisting into the shape of hands."
    "I can see their fingers elongating...tightly constricting our necks."
    "All that’s left is to patiently wait and see which one of us chokes first."
    "..."
    "I hope it’s her."
    "It would be easier to take her home if she were unconscious."
    "........."
    "......"
    "..."

    scene yuminightschool9
    with dissolve2

    y "This place always feels so different at night..."
    y "Takes a lot to creep me out but, not gonna lie, this shit comes close."
    s "It doesn’t take a lot to creep you out. I successfully creep you out every single day."
    y "Yeah, the thought of getting raped will do that."

    scene yuminightschool10
    with dissolve

    s "I wouldn’t-"
    y "Weirdly enough, shit gets even creepier when you turn the lights {i}on.{/i} "
    y "Think it’s probably cause it feels less like sneakin’ in and more like everybody’s just...gone. Like the whole world’s in the process of vanishing or some shit."
    s "Well, I can definitely relate to that."

    scene yuminightschool11
    with dissolve

    y "You come here often? At night, I mean."
    s "Are you hitting on me?"
    y "No, but I {i}will{/i} hit you if you say that again."
    s "Every once in a while, I’ll show up. I don’t think it’s ever really been intentional, though."
    y "You mean with your blackouts? They lead you here often?"
    s "Either them or a small girl with a ponytail."

    scene yuminightschool12
    with dissolve

    y "Your niece’s friend? The fuck would {i}she{/i} have to do here so late at night?"
    s "Either she has a very strange hobby or it has something to do with why time is stuck-"

    scene yuminightschool13
    with dissolve

    y "Wait. Hold that thought. Do you want food or some shit? Because I’ve gotta feeling this is gonna be a long ass explanation and I ain’t gonna be able to listen without something to eat."
    s "I’m-"
    y "Fuck it. I’ll just pick something out for you. You’ve treated me to dinner during the job search BS, so I’ve got you this one time."
    s "Well, thank you for treating me to a meal that I do not want with money you do not have to use."
    y "You should really say thank you when people do nice things for you, prick. "

    scene yuminightschool14
    with dissolve

    "Yumi disappears into the kitchen, but doesn’t take it upon herself to kill the darkness as the only light I can make out from here is the faint glow of a refrigerator door opening."
    "I can tell from the way she moves that she really has done this before, but I’m not sure if I should be thankful I haven’t bumped into her here or...disappointed? Is that the right word?"
    "If I had crossed paths with her while on one of several trips with Maya, maybe it wouldn’t have taken so long to reel Yumi into this segment of the hidden world?"
    "After all, she does seem at least slightly central to some “deeper” aspect of my life given how frequently I lose my mind around her..."
    "But would that alone have been enough to convince her to hear me out? "
    "And will she hear anything at all when my half-baked attempts at explaining things add up to no more than just “your memory is broken but so is mine. Let’s have a sleepover?”"
    "I have no idea what I’m doing...nor any idea of what I even want Yumi’s role to be if things {i}do{/i} continue to progress like this."
    "All I know is I’d feel a little emptier if the one segment of common ground we’ve found ruptured and split."

    scene yuminightschool15
    with dissolve2

    "When she returns, I think about what I would have done if I never encountered Maya on the rooftop that night so long ago."
    "Would I have felt lonely?"
    "Would I have maintained the steady pursuit of fucking my entire classroom — completely disregarding how empty it would have felt apart from the momentary warmth?"
    "Where would it have ended?"
    "I think for another moment about what would have become of the other {i}me’s{/i} that never felt the first traces of waking up...but I have no reason to brag when I’ve only just begun to open my eyes."
    "When will it end?"
    "..."
    "Just what is the point of all of this?"

    y "Uhh...hello?"

    scene yuminightschool16
    with dissolve

    s "Hi."
    y "Okay, good. Wasn’t sure if you were “there” again or not. "
    s "I am. And thanks again for the free food that I didn’t want."
    y "You sure? Cause you haven’t eaten all day either. Been with you the whole time."
    s "Ami gets mad if I don’t eat the dinner she makes for me every night, so I’ll hold out if it means not getting an earful from her in the morning."
    y "Damn. She’s got you even more whipped than I thought."
    y "She involved in all this weird, time-related stuff too? Or is that reserved for just you and Ponytail?"
    s "Ami’s unrelated. It’s just Maya, Ayane, and me right now."

    scene yuminightschool17
    with dissolve

    y "Huh. Guess that helps explain why the blonde one’s so fuckin’ obsessed with you and shit."
    s "She was like that before- actually, yes. That is why she loves me."
    s "It’s hard not growing close to someone when you live through the apocalypse together."

    scene yuminightschool18
    with dissolve

    y "Apocalypse? The fuck is this about an apocalypse? I thought we just had some disease or that time was, like...glitching out or some shit. Nobody said anything about an apocalypse."
    s "That’s just sort of how we started referring to it. "
    s "You’ll get a more in-depth answer if you decide you really {i}do{/i} want to look more into this, but the bare-bones explanation is that the world is going to end soon and only a few of us are going to remember it."

    scene yuminightschool19
    with dissolve

    y "The fuck do you mean it’s going to {i}end?{/i} How can you stay so calm while saying that shit?"
    s "Because it’s going to start again right afterward. At the same place in the school year, but not the same place in time. Do you understand?"
    y "No. {i}Fuck{/i} no. Am I being Punk’d? Are there cameras here or some shit? "
    s "I really hope not. My job would be in even greater jeopardy than it already is."

    scene yuminightschool20
    with dissolve

    y "Apocalypse...a new world...reliving the same school year?"
    y "How...how the fuck am I supposed to believe that?"
    s "The only way to believe it is to see it for yourself, I think. "
    y "And if I..."
    y "If I sleep with you, I’ll somehow-"
    s "I’m going to stop you right there because that is definitely not what I was getting at when I suggested that you sleep over my house."

    scene yuminightschool21
    with dissolve

    y "Be a little more honest about that next time! Of course I was gonna think that’s what you were tryin’ to get at! What kind of grown man just has a normal sleepover with teenage girls?!"
    s "I’m not the leader of a sex cult, Yumi. I’m just some guy with advanced knowledge of how the world works who is trying to shepherd others into understanding as well."
    y "That sounds exactly like what the leader of a sex cult would say!"
    s "You don’t have to sleep with me. You literally just have to show up and hang out at my place so we can all monitor each other and discuss what’s been going on."
    s "Like I said, you’re one of the only people who has ever been able to grasp that things aren’t exactly as they seem. So we want to use you as a sort of...test subject, I guess."
    y "And that’s supposed to convince me?!"
    s "What {i}would{/i} convince you? Because if honesty doesn’t work, I’m not really sure what else to do. I’m not going to force you."
    y "I-"

    scene yuminightschool22
    with dissolve

    y "Hah..."
    y "How the fuck would I explain that to Chika?"
    y "I get that you ain’t just pervin’ out on me this time, but I’ve got no idea how to tell her that I’m stayin’ at your place even if I {i}do{/i} decide to."
    s "Then don’t tell her."
    y "She’s my best friend and she’s...fuckin’ {i}in love{/i} with you for whatever reason. I can’t just ignore that because it’s convenient."
    s "Convenience doesn’t have anything to do with it, Yumi."
    s "I’m obviously not one to model your priorities after, but I don’t think it’s all that far-fetched to say getting to the bottom of a time loop is a little more important than {i}love.{/i}"
    y "Doubt Chika would agree."
    s "Chika probably won’t even remember once everything is said and done. But I guess I can’t guarantee that as it seems the memories that {i}do{/i} carry over are very...inconsistent."
    y "Inconsistent how?"
    s "Inconsistent like...some memories are just omitted if they have anything to do with time or...events surrounding the whole world-resetting ordeal."
    y "But memories like being sexually assaulted by a teacher get to stay? Sounds fair."

    scene yuminightschool23
    with dissolve

    y "Figures the world would go out of its way to make my life even shittier. Ain’t like it’s done enough of that already."
    y "Whether it be deadbeat parents...or growin’ up too mean to get anybody to like me...or havin’ a teacher who openly admits to beating off to his students..."
    y "Or how I...how despite that, I..."
    s "..."

    scene yuminightschool24
    with dissolve

    s "I get it."
    s "You don’t have to come."
    s "I’ll tell Maya and Ayane that-"
    y "I’ll...do it."

    scene yuminightschool25
    with dissolve

    s "..."
    y "I’ll do it, but...I still ain’t sure what I’m gonna say to Chika. And if you do anything to make me feel even slightly uncomfortable while I’m there, I’m noping the fuck out. Got it?"
    s "...Yeah."
    s "That’s fine."
    y "Cool."
    s "..."
    y "..."
    y "Anyway, I ain’t really hungry anymore, so...I’m gonna, like...get rid of all this shit so nobody knows anyone was here when they weren’t supposed to be."
    y "I’ll be fucked out of a bunch of meals in the future if security suddenly tightens and...yeah. I’ll clear your tray too, I guess."
    s "Yumi-"
    y "How about we just...shut the fuck up for a little while, okay?"

    scene black
    with dissolve2

    "Yumi clears everything off of the table and, for the next ten minutes, we keep our lips sealed."

    play sound "static.mp3"
    scene thisisgreen5 with flash
    scene yuminightschool26 with flash
    stop sound

    "But something we find in the hallway beckons us to part them."

    y "What the...fuck?"
    s "..."
    y "That...wasn’t there the whole time, was it? Didn’t we come down this hallway on the way to the cafeteria?"

    play sound "static.mp3"
    scene thisisgreen5 with flash
    scene yuminightschool27 with flash
    stop sound

    s "We did..."
    y "Are we...not alone in here? "
    y "Somebody’s gotta be playin’ a prank on us, right?"
    s "..."
    y "You said Ponytail or...uhh...{i}Maya{/i} or whatever comes here too, right? Would {i}she{/i} do something like this?"
    y "Cause this ain’t-"

    scene yuminightschool28
    with dissolve

    y "Yo! What are you doing?! There could be, like...a bomb in there or some shit!"
    s "I have to move it."
    s "If I don’t move it, we can’t leave."
    y "We can just walk around it, you fucking idiot! It ain’t like it’s-"

    stop music
    scene bedroom_night
    play sound "cheer1.mp3"

    s "{b}Lucy, I’m hooooooome!{/b}"
    s "{b}And I brought a PRIIIIIIIIIIZE!{/b}"

    scene black
    stop sound

    "THE DAY ENDS"

    $ renpy.end_replay()
    $ yumislumber3 = True
    $ yumi_love += 3

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

    "A NEW ONE BEGINS"
    "And I know what it is I have to do."

    jump slumberphonemenu

label yumispring1:
    play sound "static.mp3"
    scene clearnightsky with flash
    stop sound
    play music "blueair.mp3"

    "What does it take to move forward?"
    "It’s a simple question. And it’s been answered several times throughout the course of this story, but never with a constant."
    "You see, there are certain variables that come into play when we’re asked broad, somewhat philosophical questions like that. "
    "And, as fun as it is to dance around them with vague non-answers, there’s gotta be {i}something.{/i}"
    "Right?"
    "Like, there has to be {i}one{/i} thing that everyone can do to leave the past behind and begin the next chapter in their life. "
    "And no. This is not the part where I don my favorite hypocrite costume and spoon-feed you the concept of {i}waiting{/i} as a tongue-in-cheek non-answer to a tangent about my distaste for non-answers."
    "It’s the part where I scratch the space beneath my chin that you used to scratch when your hands still worked the way they were meant to and {i}think-{/i}"
    "So I {i}think-{/i}"
    "But I think I’m confused."
    "It’s dark in here right now. And that’s fine. I’m used to the dark and I’m used to waiting. And I know that all of this is sure to blow over if I can just keep my head held high."
    "And all those worries and vague thoughts about what it takes to move forward will one day click or fall into place or do whatever it is they’re {i}supposed{/i} to do."
    "Like hands that shake too much to hold-"
    "Like plants that grow without being watered-"
    "Like the angel in the back of my head reminding me to be yours-"
    "The clocks will tick onward."
    "Even when they lack their arms."
    "..."
    "..."
    "..."
    "That’s it."
    "That’s all I have to say."
    "I’m not sure why you’re still-"

    stop music
    play sound "static.mp3"
    scene yuminorikocon1 with flash
    stop sound
    play music "noriko.mp3"

    "Oh, fuck. Yumi Yamaguchi s- {i}ahem!{/i}"
    "{i}Yumi Yamaguchi swings open the door to a convenience store that she has avoided most nights before on account of one of her classmates working here.{/i}"
    "{i}And she was feeling a bit hesitant as that classmate, Noriko Nakayama, had been causing a lot of problems for her lately.{/i}"
    "{i}You see, for reasons Yumi Yamaguchi did not understand, Noriko Nakayama was attempting to become her friend! Even going as far as telling her to come apply for a job at the store she’d been avoiding!{/i}"
    "{i}But, desperate for cash and not willing to sell her body to the many people out there who would be willing to pay for it, Yumi had run out of options and somehow found herself here.{/i}"

    y "Uhh...yo."

    "{i}She called out, unsure of whether or not this was going to be some sort of set-up. Because, while Noriko didn’t seem like the type to do such a thing, Yumi was quite averse to the whole idea of “trust.”{/i}"

    n "Yumi! Great timing!"

    "{i}Like a hawk, Noriko swoops down and barrages the Yakuza princess with talons of congeniality!{/i}"

    play sound "static.mp3"
    scene yuminorikocon2 with flash
    stop sound

    "{i}Then the shot changes and I go take a nap. Bye!{/i}"

    n "Hey! I was starting to think you weren’t going to show up."
    y "I just...happened to be in the area and shit."

    scene yuminorikocon3
    with dissolve

    n "Yeah. You live around here, don’t you? I remember you saying something about that. Were you applying to other places? Which ones? Because I don’t think there are many others still open out here and-"
    y "You..."

    scene yuminorikocon4
    with dissolve

    y "You talk a lot, don’t you?"
    n "Me? Oh, yeah. I could talk forever if I had to. Plus, we’ve been dead all night long and I’m just excited to be with another human now."
    n "So, are you still looking for a job?"
    y "I mean...yeah. But I ain’t really great at interviews and applications and shit, so I was hopin’ we could kinda just skip all that and you could just, like...pay me."
    n "Cool! You’re hired."

    scene yuminorikocon5
    with dissolve

    y "I’m what?"
    n "Hired! You start right now. "
    y "..."
    n "Pay is ¥1,000 per hour and you’ll be taking the morning shifts on weekends once you’re fully trained. But I’ll have you shadowing me for a while so I can show you the ropes."
    y "Are you, like...the manager here? Ain’t you a little young to be just hirin’ some girl on a whim like this?"

    scene yuminorikocon6
    with dissolve

    n "I already talked to the boss about it. I’ve been pushing for someone else my age to work here forever now and it’s not like we get many applicants all the way out here."

    scene yuminorikocon7
    with dissolve

    n "Granted, it {i}was{/i} Kirin I had in mind when I brought up the idea. But I’m starting to realize she might be banking on one of those lives where she just never has to work a single day."
    n "Plus, she was already fired from Pepper Lunch a while back and might not be the most responsible person to-"
    y "Sorry for interruptin’ in the middle of your...many lines of dialogue. But what makes you so sure I ain’t gonna be just as unreliable as that Kirin girl?"

    scene yuminorikocon8
    with dissolve

    n "A hunch!"
    y "..."
    y "That’s it? "
    n "Yeah! Cause, like, even if you {i}do{/i} suck, you’ll be here at the same time as me and I can just help you out. "
    n "And if worse comes to worst and you get fired, at least we’ll be able to become better friends!"
    y "You know I ain’t gonna be your friend just cause you got me a job, right?"
    n "We’ll see about that!"

    scene yuminorikocon9
    with dissolve

    y "Noriko...why are you doin’ this shit for me? I ain’t done anythin’ to deserve it. Hell, I ain’t said anything nice to or {i}about{/i} you in...probably forever. It doesn’t make sense."
    n "Why do I need a reason to do something nice for someone?"
    n "You need a job and I want to be friends. And hey, you can even use those facts to rationalize this inside your head if you can’t bring yourself to understand that good people actually just exist sometimes."

    scene yuminorikocon10
    with dissolve

    n "Plus, with a shirt like that, you already fit in with the ska music that’s always playing in here!"
    y "Why do I feel like this ain’t the first time somebody’s said shit about ska music to me?"

    scene yuminorikocon11
    with dissolve

    n "Are you wearing a sarashi?"
    y "Eyes up here, Pinky."

    scene yuminorikocon12
    with dissolve

    n "Are you wearing a sarashi?"
    y "Listen. If we’re gonna be {i}friends{/i} or {i}co-workers{/i} or whatever the fuck we’re gonna be, you can’t be askin’ me personal shit like that."
    n "That’s a little counterintuitive to what friends are supposed to be, but noted. "

    scene yuminorikocon13
    with dissolve

    n "Boobs aside, though! Why don’t I give you a little tour of our new little love-nest while we’re still dead?"
    y "Can we, like...{i}not{/i} call it that?"

    scene black
    with dissolve2

    n "Absolutely! We’re all about creating a comfortable, healthy environment here! You don’t like the way you’re being spoken to? Speak up! You want to wear a sarashi? Wear a sarashi!"
    y "Can you please leave what I do with my god damn tits out of this?! That ain’t got shit to do with work!"

    scene yuminorikocon14
    with dissolve2

    n "True. But you haven’t clocked in yet, so you’re not {i}technically{/i} working right now. "
    y "Well...then how the fuck do I-"
    n "Just kidding. You don’t have to clock in yet. I’ll keep track of your time manually. But you’re right. We should wait until we’re clocked out to talk about boobs and the like."
    y "Or just...never?"
    n "We’ll see! But yeah, orientation...commence!"

    scene yuminorikocon15
    with dissolve

    n "These aisles are where we keep all the dry goods. They’re normally restocked at night, so you won’t have to worry about them most mornings unless you start running low on something."
    n "I’ll show you how we do that the next time you work, though, since I already took care of it before you came in tonight."

    scene yuminorikocon16
    with dissolve

    y "Is it more complicated than just, like...taking shit out of a box and puttin’ it in the right place?"
    n "A little. We’ve gotta scan everything in when we put it on the shelves and make sure we rotate the products too. "
    y "Make the labels face the right direction. Got it."
    n "No, like...rotating when it comes to food and stuff means placing the new product behind the old product so that the same things don’t stay on the shelves forever and expire before they’re bought."
    n "There’s a little acronym called FIFO — first in, first out — that should help you remember to do that. "
    n "You won’t get charged or anything for stuff that {i}does{/i} expire, but it’s better for business and the environment if we can avoid wasting stuff."
    n "Oh, and any of the dry food that {i}does{/i} pass expiration can be pulled from the shelves and put in the box with my name on it in the back. "

    scene yuminorikocon17
    with dissolve

    y "We’re allowed to take shit home once it’s expired?!"
    n "Yes! That’s not what that box is for, though. I take all the expired stuff to a homeless shelter down the road on my way home after work. You can take whatever, though. "
    y "And you ain’t gonna look down on me for keepin’ it to myself instead of feeding a bunch of fuckin’ homeless people?"
    n "I mean...how much do you {i}need?{/i}"
    y "Bitch, I’ve got a family to feed. "

    scene yuminorikocon18
    with dissolve

    y "I might be able to put some in your stupid fuckin’ homeless box, though. We’ll see."
    n "Great!"

    scene black
    with dissolve

    n "Now! Follow me to our next destination!"
    y "Huh? Oh. Shit. Yeah. On it."

    scene yuminorikocon19
    with dissolve2

    n "This is the cafe. We can help ourselves to free coffee all night so long as we brew it. Which we should be doing anyway in case customers want it."
    n "Nobody really buys anything from here during the graveyard shift, but I hear it can get pretty busy during the morning, so I’ll show you how to handle that in a few minutes."
    y "Can we take some of those pastries and shit too?"
    n "We’re {i}supposed{/i} to pay for them. But yes. As long as you don’t take like, a suspicious amount of them, you should be fine."
    y "How many is suspicious?"
    n "I don’t know, Yumi. Use your judgement. Take whatever amount of scones you normally consume per sitting and just...halve it or something."
    y "The fuck is a {i}scone?{/i} I just want a muffin."

    scene black
    with dissolve

    n "Then you shall have a muffin! And I will {i}now{/i} show you where you will be able to {i}eat{/i} that muffin!"
    y "Is there really a fuckin’ designated muffin zone at this weird ass convenience store?"

    scene yuminorikocon20
    with dissolve

    n "There is! But we normally just call it the dining area instead and no one but me will understand what you mean if you call it the muffin zone."

    scene yuminorikocon21
    with dissolve

    n "I don’t mind, though. We’re going to need a bunch more fun, little inside-jokes like that if we’re going to be friends. Which we are."
    y "You’re really goin’ hard on this whole fuckin’ friend thing, huh? The slutty one not cuttin’ it for you?"
    n "Kirin’s actually a great friend. Her open sexuality is more of a mask to hide her insecurities."

    scene yuminorikocon22
    with dissolve

    y "You mean like you and the way you dress?"
    n "Hm? What’s wrong with the way I dress?"

    scene yuminorikocon23
    with dissolve

    y "I mean...ain’t you wearin’ all that flashy shit to sorta compensate for somethin’? Like...fuck if I know. What’s some shit normal girls get all self-conscious about?"
    n "Idunno. Boobs?"

    scene yuminorikocon24
    with dissolve

    n "Oh {i}that’s{/i} what the sarashi is for! You’re self-conscious about how huge-"
    y "Mind tellin’ me about company policy when it comes to beatin’ the shit out of other employees?"
    n "Don’t do it."
    y "You’re damn lucky I’m broke as shit, Pinky."

    scene yuminorikocon25
    with dissolve

    n "Call me Noriko again. I like hearing you say my name. "
    y "Uhh...why?"
    n "Idunno."

    scene yuminorikocon26
    with dissolve

    n "Ah! What if it’s love?!"
    y "Then I need to find a new fuckin’ job. "

    scene yuminorikocon27
    with dissolve

    n "No worries, Yumi! Thankfully for you, my heart’s been set on the same man ever since-"
    y "Yeah, yeah, yeah. Heard it a trillion times before from every other fuckin’ girl who’s ever tried talkin’ to me. "
    y "Say, mind if we leave the predator shit outta discussions at work? That’d be nice."
    n "Got it!"

    scene yuminorikocon28
    with dissolve

    n "That {i}does{/i} remind me that I need to call my sister, though. So why don’t I give you a task so simple that even a kid could do it while I go and do that?"
    y "You’re gonna...leave me alone even though I’m only like ten minutes into having this job?"
    n "Just for a second. And, like I said, it’ll be easy. You can just wipe down a few tables and I’ll be back before you even know it."
    n "And if anyone shows up, just tell them I’ll be back in a second to ring them up. Under {i}no{/i} circumstances try to do that yourself. Got it?"
    y "Now, I ain’t ever paid attention in school before, but I’ve read enough manga and shit to know foreshadowing when I hear it."
    n "Then just...don’t give in to your manga-related knowledge?"

    scene black
    with dissolve2
    stop music fadeout 25.0

    n "Here. I’ll show you where the cleaning stuff is."

    "........."
    "......"
    "..."

    scene yuminorikocon29
    with dissolve2

    y "Yeah...all right. I can handle this shit for ¥1,000 an hour. {i}And{/i} a...non-suspicious amount of muffins. Whatever the fuck that means."

    scene yuminorikocon30
    with dissolve

    y "Could deal without the fuckin’ lunatic co-worker, though. Can’t tell if she actually wants to be my friend or if she’s just tryin’ to get in my fuckin’ pants."

    scene yuminorikocon29
    with dissolve

    y "Probably got it from her fuckin’ {i}role model.{/i} Wouldn’t be surprised if that’s who she was callin’ right now instead of her {i}sister.{/i}"
    y "Whatever, though. Ain’t my problem. Just gonna...do my job and get the fuck out of here..."
    tv "For Eleven Sports, I’ve been Takuya Tanaka. Thanks as always for watching, and stay tuned until next time."
    tv "Up next is Untitled Children’s Show."

    scene yuminorikocon31
    with dissolve

    y "Huh?"

    play sound "static.mp3"
    scene yuminorikocon32 with flash
    stop sound
    play music "hometown.mp3"

    tv2 "Okay, Kentaro-kun! If you answer this next question correctly, you’ll be named the kid of the month! Are you ready?"
    tv2 "Good!"
    tv2 "We learned today with the help of Mr. Jefferson and his best friend David the Dinosaur that sometimes, too much of a good thing can actually be {i}bad!{/i}"
    tv2 "But we also learned that it’s just as easy for {i}bad{/i} things to feel good! Which makes growing up {i}veeeeery{/i} tricky since “temptation” is hard to avoid."
    tv2 "And it’s like that for adults as well! Which is why it’s important to understand that {i}eeeeeveryone{/i} has demons they’re dealing with. And that we should be good to one another since we don’t know them!"
    tv2 "Now, Kentaro-kun! Can you figure out which of today’s cast members has been the {i}demon{/i} all along?"
    y "Leo. The leprechaun."
    ken "Umm..."
    y "It’s Leo. Say Leo."
    tv2 "Now remember, Kentaro-kun! When Mr. Jefferson and David went under the bridge, who was it that lured them there with the promise of gold?"
    ken "Uuuuuummmmmm......."
    tv2 "L.........L......."
    ken "Leo! It’s Leo the Leprechaun!"

    play sound "ohshitpartytime.mp3"

    tv2 "Yaaaaay! You did it, Kentaro-kun! This means you’re the new kid of the month!"
    y "Took him long enough."
    tv2 "Everybody, please give Kentaro-kun a round of applause for his {i}great{/i} work today!"
    tv2 "And, if you’re one of our loyal viewers at home, please call in after the show is over and tell us how you felt about today’s episode. But make sure to get your parents’ permission first!"
    tv2 "Breaking the rules is bad. And remember, even if something bad {i}feels{/i} good, you have to avoid “temptation” or {i}you’ll{/i} become a demon too!"
    tv2 "But don’t worry! If you’re confused about something, you can always ask an adult. They’ve been around {i}waaaaaay{/i} longer, and they’ll know what’s best for you!"
    tv2 "And you’ll always have us as well! We love you! "
    tv2 "Be good to your friends, be good to your parents, and be good to yourself!"
    tv2 "Thanks as always for watching Untitled Children’s Show!"

    scene yuminorikocon33
    with dissolve

    y "Mom! Can I use your phone? "
    yu "..."
    y "Mom? Are you awake?"
    yu "..."

    scene yuminorikocon32
    with dissolve

    y "I bet Kentaro’s mom is awake right now."

    stop music
    play sound "static.mp3"
    scene yuminorikocon34 with flash
    stop sound
    play music "noriko.mp3"

    tv2 "{i}And it’s like that for adults as well! Which is why it’s important to understand that eeeeeveryone has demons they’re dealing with. And that we should be good to one another since we don’t know them!{/i}"
    tv2 "{i}Now, Kentaro-kun! Can you figure out which of today’s cast members has been the demon all along?{/i}"
    y "Leo."
    y "The leprechaun."
    ken "Ummm..."
    y "It’s the fucking leprechaun you stupid piece of shit."
    tv2 "{i}Now remember, Kentaro-kun! When Mr. Jefferson and David went under the bridge, who was it that lured them there with the promise of gold?{/i}"
    ken "Uuuuuummmmmm......."

    scene yuminorikocon35
    with dissolve
    play sound "dooropen.mp3"

    y "It’s the fucking leprechaun! How the hell are you this stupid?!"
    tv2 "{i}L.........L.......{/i}"
    n "Ooh! Untitled Children’s Show! I used to watch this with Sensei all the time!"

    scene yuminorikocon36
    with dissolve

    y "LEO! SAY “LEO” YOU FUCKING IDIOT! "
    y "YOU THINK YOU CAN BE KID OF THE MONTH LIKE THAT?! FUCK YOU, KENTARO-KUN! FUCK YOU! YOU FUCKING IDIOT! IT’S LEO!"
    n "...Yumi?"

    stop music
    play sound "static.mp3"
    scene yuminorikocon37 with flash
    stop sound

    y "..."
    y "Huh?"
    n "Is...Is everything okay? "
    n "You spilled the sanitizer all over the- wait, are you {i}shaking?{/i} What’s-"
    y "I have to go."

    scene black

    "........."
    "......"
    "..."

    play sound "slap.mp3"

    ken "{i}Leo! It’s Leo the Leprechaun!{/i}"

    play sound "static.mp3"
    scene yuminorikocon38 with flash
    stop sound

    n "Where are you going?"
    y "Let go of me."
    n "{i}Where are you going?{/i}"
    y "Home. I ain’t ready to {i}work{/i} today. "
    n "Yumi-"
    y "Just fuckin’ fire me if that’s a problem, okay? I’m goin’ home. I ain’t fuckin’...capable, I..."
    y "I just can’t do this right now."
    n "You won’t come back if I let go of you."

    scene yuminorikocon39
    with dissolve

    y "So what?! You’ll have much {i}bigger{/i} problems if you don’t fuckin’ do that right now, dipshit!"
    n "Bigger problems? Are you gonna hit me?"
    y "So what if I am?! "
    y "You’ve been annoying the shit out of me all night! You’re lucky I haven’t fucking done it already!"
    n "Yumi-"
    y "Stop fucking saying my name! We’re not friends! We ain’t gonna {i}be{/i} friends!"
    n "Yumi, I’ll change the channel."

    scene yuminorikocon40
    with dissolve

    y "What? A stupid TV show ain’t the fuckin’ problem! It’s you! {i}You’re{/i} the one who’s pissin’ me off!"
    n "Yumi. It’s {i}okay.{/i} "
    n "I didn’t see anything. And it’s time for you to go on break. Your shift isn’t over yet."
    y "..."

    scene yuminorikocon41
    with dissolve

    y "Why are you-"
    n "Let’s just..."
    n "Let’s shut up for a few minutes."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    "{i}Yumi and Noriko are now friends(?)!{/i}"

    $ renpy.end_replay()
    $ yumispring1 = True

    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    s "Sleep."

    scene black
    play sound "tackle.mp3"

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

label yumispring2:
    stop music
    play sound "static.mp3"
    scene town2_noon with flash
    stop sound
    play music "blueair.mp3"

    "This town has two halves."
    "I’ve familiarized myself with both of them over the X amount of time that I’ve been here."
    "And even though I’ve X and X, my heart still X."
    "And the thought that maybe something special will occur if I place myself where I’m not supposed to be has turned into an irremovable knot in this rope made of X."
    "I’m tired now. Broken, even."
    "And if broken isn’t bad enough- turn my sadness into smiles, even."
    "Because at least a frown is honest when you’re brave or careless enough to wear one in public. But, once it's flipped on its head, things get a lot more blurry."
    "I find that, most of the time, people are only smiling because they feel like they’re supposed to. But then you sit down and talk to them and realize they’re not happy at all."
    "So maybe I’m better than others in that regard. Maybe the fact that I {i}can’t{/i} smile is what puts me a step above the rest and gets more feminine fluids all over the bottom of my shirt from hitting it while clothed."
    "Maybe I’m only loved because people feel like I’m supposed to be loved. "
    "But it isn’t like that here."
    "This half of town is honest."
    "And yes, every once in while, my eyes and ears will go bzzzzzt and I’ll reappear somewhere I wasn’t headed to, but that’s {i}fine.{/i}"
    "I mean, it’s not like I ever have anywhere important to be. And that’s even more true now that I’m basically jobless."
    "And if I happen to throw myself on an unsuspecting girl, they’ll be a little less traumatized from the fact that I’m just some stranger instead of the person they’ve entrusted to teach them shit."
    "I slide my hand into my pants and jerk off while I walk down the road because this world is a big sandbox and that’s just what I feel like doing."

    show amihappyyay
    with pixellate

    a "Hey!"
    s "Aww, shit."
    a "Just because this is the OLD district doesn’t mean you can wank your willy in broad noonlight, frog boy!"
    s "Aren’t you supposed to only show up in resets and happy events and stuff?"
    a "I can show up whenever I want. I’m in the game files."
    s "Am I also in the game files?"
    a "Not as a sprite. So it’s actually kind of like you don’t exist at all."
    s "Wow, what a coincidence. Because that’s also exactly how it feels."
    a "So! What brings you all the way out here this time, Sensei?"
    s "I don’t know. I unlocked a new option and figured I’d try it out since the others are very limited now. But I'm cool with this place since I'll probably see Yumi and she has nice boobs."
    a "I know, right? Don’t they make you want to just bind and gag her and throw her in your room and leave her there for years and feed her cup noodles and then cum in her hair and then maybe on her boobs too?"
    s "No one understands me better than you, Special Ami."
    a "Normal Ami does! But she’s in her room crying right now because you keep leaving her behind."
    a "Shouldn’t you be spending aaaaaaaaaaaaaaaaaaall of your time with her?"
    s "I can’t. It’s chapter four and I still haven’t even had sex with over half the class yet. I need to get on that if this game is ever going to end."
    a "Then why not start today?"
    s "Because the only person around is all scribbly and I wouldn’t know where to put it."
    a "Twenty-three minutes from now, you’ll encounter the boobs."
    a "You gonna put it in, [mayamaster]?"
    s "In Yumi? I don’t know. Maybe if she’ll let me. Or not. I’ve got nothing else to lose now."
    a "Jeez, frog boy. Where was that attitude when you were supposed to rape somebody?"
    s "Why do you keep calling me frog boy?"
    a "Because some frogs can self-lubricate when they get a little too dry and cover themselves in a thin layer of mucus that protects them from the air and stuff."
    s "Are you saying I can do that too?"
    a "No. I just like using the name “frog boy.” It reminds me of-"
    s "Frogs?"
    a "No."
    a "It reminds me of-"

    hide amihappyyay
    stop music
    scene black

    "Rain King."

    play sound "static.mp3"
    scene town2_noon with flash
    show amihappyyay
    stop sound
    play music "blueair.mp3"

    if rainking == False:
        s "I don’t get it."
        a "That would have been a lot funnier if this version of you saw that event."
    else:
        s "Hey, I remember that event."
        a "Rude! That means you must have invaded our privacy!"

    a "Oh well, though."
    a "Point is, Jim, you and Yumi are gonna be doing the skin tango soon. And I just want you to be prepared so you don’t accidentally pee yourself and have to hear her call you “pee boy” forever."
    s "That won’t do. Especially when I’m already frog boy."
    s "But how to skin tango?"
    a "That wiener you’re flinging around right now? Grip it really firmly. Like {i}super{/i} firmly. Try to pop it."
    s "Ami, this hurts."
    a "Pop it and get it all over me! Like a boil full of embryotic fluid!"

    scene black
    with dissolve

    s "Okay, I’m gonna leave now. This is starting to feel like Clam’s Tongue and Egg Tooth and I still don’t understand either of those events."
    a "You don’t have to understand anything!"

    stop music
    scene artpicture2

    a "you just have to believe"

    play sound "static.mp3"
    scene yuminightfrog1 with flash
    stop sound
    play music "retrospect.mp3"

    y "..."
    s "..."

    "It was then that I knew it was egg time."
    "That I wanted to use my special wolf hands to pry open Yumi’s cloaca and implant a circular white object inside of her that would one day hatch into a mini Yumi because that’s how eggs work."
    "We stand there for a while, eyes being eyes. And I think that we think we want to have fucking with on each other in the body."
    "But none of the fucking happen =("
    "Instead, she say the thing she always say because little baby frog boy wants his mommy and his mommy is GONE."

    y "Uhh...you good?"
    s "..."
    y "Think you’re...having another one of those episodes right now..."
    y "Can you hear me at all?..."
    s "..."
    y "Huh...you {i}look{/i} more sane than normal at least. Still ugly as fuck, though."

    "She doesn’t mean that, Akira. She wants your COCK. She wants ANY COCK. She’d fuck an animal if she had to! She’s a slut! Virgin slut! A big, bully slut with huge tits! Knock her up! Cum in her hair!"

    s "R..."
    y "R?..."
    s "Run..."

    play sound "static.mp3"
    scene yuminightfrog2 with flash
    stop sound
    play sound "broken.mp3"

    "nana-nana poo-poo, i’m a better you-you. "

    stop sound
    play sound "static.mp3"
    scene yuminightfrog3 with flash
    scene yuminightfrog4 with flash
    scene yuminightfrog5 with flash
    scene yuminightfrog6 with flash
    scene yuminightfrog7 with flash
    scene yuminightfrog8 with flash
    scene yuminightfrog9 with flash
    stop sound

    y "Uhh...you good?"
    s "..."
    y "Think you’re...having another one of those episodes right now..."
    y "Can you hear me at all?..."
    s "I..."
    s "Yeah..."
    s "Yeah, I think I’m back."
    s "By any chance, did I just tell you to run?"
    y "Run? No. You haven’t said shit."
    s "Good because I’m gonna fuck your hot little slit RIGHT NOW and you’re gonna LOVE IT!"

    play sound "static.mp3"
    scene yuminightfrog2 with flash
    stop sound
    play sound "broken.mp3"

    "lololololol okay you can have your brain back now."
    "here, try again."

    stop sound
    play sound "static.mp3"
    scene yuminightfrog3 with flash
    scene yuminightfrog4 with flash
    scene yuminightfrog5 with flash
    scene yuminightfrog6 with flash
    scene yuminightfrog7 with flash
    scene yuminightfrog8 with flash
    scene yuminightfrog9 with flash
    stop sound

    y "Uhh...you good?"
    s "Sex."

    play sound "static.mp3"
    scene yuminightfrog2 with flash
    stop sound
    play sound "broken.mp3"

    "lmaooooooooo"

    stop sound
    play sound "static.mp3"
    scene yuminightfrog3 with flash
    scene yuminightfrog4 with flash
    scene yuminightfrog5 with flash
    scene yuminightfrog6 with flash
    scene yuminightfrog7 with flash
    scene yuminightfrog8 with flash
    scene yuminightfrog9 with flash
    stop sound

    y "Uhh...you good?"
    s "God, I fucking hope so."

    scene yuminightfrog10
    with dissolve

    y "Oh. That was way more normal of an answer than I expected finding you out here at three in the fucking morning."
    s "Yeah well, if only you knew what I had to sit through to get to that one. Also, what? It’s 3:00 AM?"
    y "Just about, yeah. Fuck you doin’ out here this late? Shouldn’t you be, like...adjustin’ your niece’s chains or some shit?"
    s "Better question- what are {i}you{/i} doing out here this late? "
    y "I got a job. But that ain’t-"
    s "Without my help?"
    y "Sorry, was I supposed to fuckin’ {i}wait{/i} for you? You’ve been gone for like three months. And I don’t even {i}like{/i} you."
    y "Ain’t like it’s cool or anything, though. Just that fuckin’ boring ass convenience store Noriko works at."
    s "And...everything else?"
    y "Everything else what?"
    s "Like...how are you? How have you been?"

    scene yuminightfrog11
    with dissolve

    y "Do you have fuckin’ cancer or something? Why are you acting like this all of a sudden? Askin’ me {i}how I am{/i} and shit."
    s "Yumi, I’m fucking miserable. "
    y "Huh?..."
    s "{i}Help me.{/i}"

    scene yuminightfrog12
    with dissolve2

    y "You’re..."
    y "You’re bein’ serious right now...ain’t you?"
    s "I don’t know what to do anymore. And all of the people I can talk to are too {i}nice.{/i} They’re too {i}forgiving.{/i} I’m a terrible fucking person, Yumi. I’m a {i}bad{/i} person. Why do they let me go?"
    y "You think {i}I{/i} know that, man? I’ve been askin’ myself the same shit this whole damn time. I ain’t got the slightest fuckin’ clue."
    y "How the hell do you expect {i}me{/i} to help you, though? I ain’t any better. I’m the same damn person I was at the start. I just keep all that mean shit about Futaba and the other girls to myself now."
    s "Why are we like this? Why can’t we be happy? What happened to us?"

    scene yuminightfrog13
    with dissolve

    y "You know my shit already...but I don’t know fuck-all ‘bout your story. And there ain’t no way I can help you like that, dude."
    y "Probably wouldn’t be able to even if I did, though. I’m just some lowlife. Same as you. Big difference is I ain’t sleepin’ around. "
    s "Why did you stop for me?..."
    y "You really have to ask?..."
    s "{i}Why?...{/i}"

    scene yuminightfrog14
    with dissolve2

    y "You looked like you were about to fuckin’ jump, man..."
    s "I..."
    s "What?..."

    scene yuminightfrog15
    with dissolve

    y "It’s a pretty long way down from here..."
    y "And I ain’t sayin’ you {i}were{/i} cause that’d mean...yeah..."
    y "But, like...can’t you maybe have your fuckin’ blackout things in places that ain’t so high up? Shit’s dangerous, dude. "
    s "..."
    y "Listen..."
    y "I...don’t want this to sound how I know it’s gonna sound to you. But if you {i}really{/i} don’t feel {i}right{/i} right now...come back to Chika’s old apartment with me."
    y "I’ve been stayin’ there after work lately and...again, this ain’t even close to the kind of invitation you probably want it to be..."

    scene yuminightfrog16
    with dissolve

    y "But if I left you alone and I found out some shitty news from Chika or whoever else found out before me...that’d fuck me up."
    s "..."
    y "Okay? "
    y "I might not be able to {i}help{/i} or whatever, but I ain’t goin’ anywhere if you’re gonna keep bein’ all...shitty."

    scene black
    with dissolve2

    s "Thank you, Yumi."

    "........."
    "......"
    "..."

    scene yuminightfrog17
    with dissolve2

    "We make our way into a building I’m extremely familiar with, but the fact that it’s now devoid of the two who {i}truly{/i} called it home makes it feel entirely different."
    "It still smells like rosewater, though. And the stains on the carpet are all right where they were left."

    y "As you’ve probably noticed, I moved some shit around. And got some new shit."
    y "Turns out, there’s a lot of stuff people just leave out on the road if you go out and look on garbage collection days. Stealin’ ain’t necessary at all apparently. "
    s "Thank you for letting me in, Yumi. I get that this must be scary for you."

    scene yuminightfrog18
    with dissolve

    y "Okay, can you {i}please{/i} not make it fuckin’ weird? It’s three in the fucking morning and I may have just saved your life. The least you can do is not subtly remind me of that time you assaulted me."
    s "I never meant to do that. You’ve always deserved better. And all I’ve ever done is make things even worse for you."
    y "That’s not...{i}all{/i} you’ve done. Like, you were the one who encouraged me to look into this whole “getting a job” shit and hey, it actually worked out in the end."
    s "I’m sure you’ll be great."

    scene yuminightfrog19
    with dissolve

    y "God! How are you somehow even {i}creepier{/i} now? The fuck’s been going on all this time? And what was all that shit about you {i}losing something?{/i}"
    y "Fuck did you lose? Cause it sure as hell wasn’t Chika. Know that for sure because the girl turned into a fuckin’ basket case while you were gone."
    s "It was another girl."
    y "{i}Another{/i} one? Did she like-"
    s "She died."

    scene yuminightfrog20
    with dissolve

    y "She-"
    s "I really don’t want to say any more about it. But please don’t tell anyone else. You’re the first girl I’ve just flat-out admitted this to."
    y "..."
    s "I’m sorry. You’ve invited me into your home and all I’ve done is make things more depressing."
    y "You do that by just existing. The shit you just told me doesn’t have anything to do with it."
    y "And this probably ain’t gonna do anything, but...I’m sorry. That you had to go through that. I won’t say shit about how long you’ve been gone anymore. I get it now."
    s "I really loved her, Yumi."
    s "I know how this must sound to you as someone who-"

    scene yuminightfrog21
    with dissolve

    y "Yeah, just...leave it at that, if you can. Shit’s hard enough for me without having to hide from my best friend that the dude she thinks she’s in love with loved somebody else."
    s "Chika too. Maybe. I think. I’m not sure. I’m not sure about anything. I’m confused. I’m so confused. I don’t know what to do."

    scene yuminightfrog22
    with dissolve

    y "Sit down, Sensei..."
    y "I’ll, like...make some tea or some shit..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yuminightfrog23
    with dissolve2

    y "So...sucks your vacation ain’t been much of a vacation at all. Least when I got kicked out of school, I got to wander around and eat shit."
    s "And I got spoon-fed by my niece. I’m sure it would have been a blast if I was conscious for any of it."
    y "So that shit about her takin’ good care of you wasn’t just somethin’ you said to appease her since she was, like...right there and shit?"
    s "Is that how it looked to all of you?"
    y "Fuck if I know what everybody else thinks. I just had a hard time believin’ you’d be that okay with someone so...well, fucking insane."
    s "She {i}is{/i} insane. But she’s like that because of me."
    s "You know, it might sound weird, but the two of you are a lot alike in the fact that she had to raise herself. Just, instead of her parents not being there for her out of choice, they were taken away."
    s "And I was never able to fill their shoes. Even tonight, I’m proving that I {i}can’t{/i} fill their shoes by being {i}here{/i} at 3:00 AM while she just lies there in bed."
    y "I’m sure it wasn’t easy. But I also ain’t sure that excuses tellin’ people she’s gonna take their organs and shit."
    s "It doesn’t. She needs help. But how am I supposed to help her when I’m {i}like this?{/i}"
    y "Not sure if you can, dude. You’ve gotta take care of yourself before worryin’ about anybody else. That’s the only way to survive."
    s "That’s the only way {i}we{/i} know how to survive. But there are other ways, I’m sure of it."
    s "Look at Noriko. Or Futaba. Or Touka. We’re surrounded by selfless people who help others before themselves and they’re all happier than {i}we{/i} are, aren’t they?"

    scene yuminightfrog24
    with dissolve

    y "Stop askin’ me about other people, dude. I don’t know shit about other people. But I’m hard-pressed to think Futaba’s happy at all after all the shit I’ve said to her."
    s "She has issues, yeah. A ton of them. And maybe I only think she’s happy because I don’t understand her. But {i}still...{/i}there’s gotta be more than this."

    scene yuminightfrog25
    with dissolve

    s "I just want to wake up one day and think to myself, “I don’t want to go back to sleep.” "
    s "And I’m at a point right now where that sounds more impossible than ever before, Yumi. What if nothing just ever feels good again?"
    y "Man...never in a million years would I have thought I’d prefer the {i}old{/i} you. I’ve got no clue what the fuck I’m supposed to say to any of this."
    s "I know. And I’m sorry. You’re just a teenage girl and I’m dumping thousands if not millions of years worth of problems on you. But I don’t need an answer to any of them, Yumi."
    y "I get it. Sometimes just talking helps. Chika’s said shit like that to me before. Apparently I ain’t great at listening, though."
    s "I disagree."
    s "In fact, I think you’re an amazing listener."
    s "I think you’re an amazing {i}person.{/i}"

    stop music

    s "{b}AND I CAN’T WAIT TO FUCK YOUR DELINQUENT, LITTLE HOLE WITH MY BIG, PROTAGONIST COCK.{/b}"

    scene yuminightfrog26
    with dissolve2

    y "..."
    s "..."
    y "..."

    play sound "static.mp3"
    scene yuminightfrog26 with flash
    stop sound

    s "I didn’t..."
    s "That wasn’t..."

    scene yuminightfrog27
    with dissolve2

    y "{i}Hah...{/i}"
    s "I didn’t mean to say that. That really wasn’t-"
    y "I know. "
    y "I get it by now."

    "awwwww, darn it. "
    "i thought that would win her heart."
    "{i}Shut up.{/i}"

    y "And it ain’t just a {i}you{/i} thing either, apparently."
    s "...What?"
    y "Ramen girl’s like that too. Saying...random irrelevant shit outta nowhere."
    y "Went out to Tojo’s the other night and it got so out of hand that I wound up just throwing my money on the counter and bouncing before it got any weirder."

    scene yuminightfrog28
    with dissolve

    y "She never told me she was gonna fuck me, though. So I like whatever she’s got more."
    s "Tsuneyo too?..."
    s "What was she saying?"
    y "Just random questions and shit at first. What do you think of this specific date? How do you take your coffee? What kind of pajamas would you bring to a sleepover?"
    y "But then the weird shit started."
    y "How much can you see with your eyes closed?"
    y "How much can you fit in a cup?"
    y "What is it you keep in your pocket?"

    play sound "static.mp3"
    scene tsuneyoyumitalk4 with flash
    stop sound

    y "{i}What color is the sky at the end of the world?{/i}"
    t "Welcome to Tojo Ramen. Please take your time looking over the menu and-"

    play sound "static.mp3"
    scene yuminightfrog29 with flash
    stop sound

    k "Tori shio ramen."

    scene black
    with dissolve2

    t "Please wait one moment."

    $ renpy.end_replay()
    $ yumispring2 = True
    $ yumi_love += 1

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "{i}She offers to let you stay the night.{/i}"
    "{i}You refuse so you don’t accidentally breed her.{/i}"

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

label beachfive13:
    scene yumirain1
    with dissolve2
    play music "goodmorning.mp3"

    "I step outside to be greeted by warm air and a faint trace of reluctance. "
    "I have a good idea of where Yumi is right now. And no, it’s not the bathroom like she said it would be. It’s somewhere I’ve found her before."
    "Somewhere she can gaze out at the water or the {b}stars{/b} or whatever it is she looks at when she’s alone to distract her from feeling anything."
    "But the reluctance comes into play not because I’m fearful of the mean words she’ll likely throw my way, but  because I’d hate to drag her into this again only for her to go right back to the start in a week or two."
    "It took her a little while to buy in last time, but she eventually did. And that made me feel like she was also buying into the idea that she was finally {i}a part{/i} of something."
    "Whether that’s actually true or not is another story entirely. But at the end of the day, she’s still someone important to me."
    "I mean...she may have even saved my life recently."
    "But again, that’s another story entirely. And even though this one is technically {i}mine{/i} since I’m the one you’re looking at right now, there are plenty other characters. Plenty other people to root for."
    "And that’s a good thing. Because I can’t imagine it’s easy rooting for me."

    s "{i}Hah...{/i}"

    "I wonder if this is just how I’m going to be from now on? Tired. Despondent. Slowly giving up on the idea that my role here is even one of importance if the most important one of all was erased."
    "I kind of hope Ayane’s right."
    "I kind of hope that someone takes my place...wakes me up when all of this is over...sifts through the shit and the mud and the passage of time and tells me when it’s okay to come out of hiding."
    "Because the god I don’t but maybe {i}do{/i} believe in knows that I’m not cut out for this."
    "But even if that’s true (it is), I hope I can be forgiven for infecting someone else with the idea that things are greater than they appear to be sometimes."
    "I just wonder why it always has to be in the dark."

    scene black
    with dissolve2

    s "Yumi."

    "I approach her. "
    "She recoils."
    "Our eyes meet."
    "Hers are grey and mine are absent."
    "She gazes out at the night one more time."
    "She takes a breath."
    "And she paints my absence grey as the anti-sun dances around her."

    scene yumirain2
    with dissolve2

    y "God damn it...really? Ain’t you got like four other girls to be perving out on right now? The fuck you come all the way out here for?"
    s "Why do you think I came all the way out here?"
    y "Becaaaaaause...you’re a creepy stalker who doesn’t know how to leave me alone?"
    s "Well, I’ve definitely always been good at finding you."
    y "Exactly. Because you’re a creepy stalker who doesn’t know how to leave me alone."
    s "Yeah...I guess I am."

    scene yumirain3
    with dissolve

    y "Uh...thanks...for admitting it, I guess?"
    s "..."
    y "What?..."
    y "Why are you just looking at me like that?..."
    y "If I knew you were going to be here, I would have worn my jumpsuit. So if your goal is to just fuckin’ ogle at me or whatever before pouncing on me again, I’ll fuckin’ kill you, you-"
    s "Yumi, I need to talk to you about something."

    scene yumirain4
    with dissolve

    y "..."
    s "..."
    y "Why me?..."
    s "Because that’s what’s worked in the past. And if either one of us is ever going to get out of this place, we’re going to have to help each other."
    y "Help each other...how? What are you asking?"
    s "Just to listen...as closely as you can. "
    y "And if I can’t?"
    s "I’ll kiss you. "

    scene yumirain5
    with dissolve

    y "Ew. Hard pass."
    s "See? I knew that would be all the motivation you’d need. So if you don’t want that to happen, pay attention."
    s "This world-"

    scene yumirain6
    with dissolve

    y "Wait. Hold on. And...no kissing since...you technically haven’t started yet."
    s "..."

    scene yumirain7
    with dissolve

    y "I...uhh..."
    y "How do I even fuckin’ put this?"

    scene yumirain8
    with dissolve

    y "Sensei, I..."
    y "I think I know what this is about."
    s "I highly doubt that, Yumi."
    y "No, like..."
    y "Ain’t we already...{i}done{/i} this before?..."

    scene yumirain9
    with dissolve2

    y "This creepy...slumber party shit. And you...comin’ out here to talk to me when I want to be alone, which...I mean, I guess that’s happened a million times by now. But like...here {i}specifically.{/i}"
    s "..."
    y "I...you know, maybe that {i}ain’t{/i} why you’re out here and shit but, like..."
    y "Weird shit follows you pretty much everywhere you go and-"
    s "No, you’re right. That’s why I’m here. "

    scene yumirain10
    with dissolve

    y "So we, like...{i}have{/i} had this conversation before?"
    s "Not...specifically. It’s complicated. But we {i}have{/i} done something {i}like{/i} this before. You didn’t remember it, though...So why do you suddenly remember it {i}now?{/i}"
    y "Fuck if I know. I’ve been havin’ tons of shit like that happen to me lately. Things that feel like dreams but...seem more like memories. It’s like fuckin’ deja vu on steroids. Ain’t none of it’s good either."
    s "What do you mean by “not good?” Do you remember the reset as well?"
    y "The fuck’s a reset? "
    s "Okay. Well, I guess that answers that question."

    scene yumirain11
    with dissolve

    y "I just meant, like...shit that feels wrong. Or shit that never even happened but...{i}feels{/i} like it happened."
    s "I’m...not sure I follow."

    scene yumirain12
    with dissolve

    y "Then...example. You ain’t ever given me detention...right?"
    s "No. Too much work."
    y "Yeah, exactly. Then why the fuck do I have so many memories of you doin’ that? And why the fuck are they all so goddamn illegal and rapey and shit?"
    s "These just sound like fantasies to me."

    scene yumirain13
    with dissolve

    y "They ain’t fantasies, ass-wipe! This might come as a surprise to you, but not everybody’s interested in getting dicked down by your friggin’ micropenis! That shit {i}happened!{/i}"
    y "And between all these weird fuckin’ blackouts and coincidences, I know that {i}you{/i} know somethin’! So whatever the fuck it is, tell me! The hell’s goin’ on with my head?!"
    s "I think the same thing that’s going on with Nodoka’s right now."

    scene yumirain14
    with dissolve

    y "You’ve got some serious balls bringin’ that piece of shit up around me, but aight. Let’s hear it. The fuck’s goin’ on with {i}her?{/i} How’s it like what’s happenin’ to me?"
    s "Since I apparently don’t have to be careful with what I say around you anymore, let’s just go ahead and {i}call{/i} them memories. That’s probably stuff that happened in other timelines."
    y "Timelines?..."
    y "You mean you and me are just goin’ around havin’ fuckin’ slumber parties in multiple timelines? And I’m supposed to believe that?"
    s "Actually, the other slumber party was {i}this{/i} timeline. Just a different section of it. "

    scene yumirain15
    with dissolve

    y "Heh?..."
    s "Every few months, we get sent back to an earlier part of the school year. And, with the exception of three of us, no one retains any memories of it. You are one of those people."
    s "But this isn’t the first time you’ve caught on. It’s happened before. Which is why we’re dragging you into it again now. "
    s "You’re clearly special in some way, Yumi. I just don’t get {i}how.{/i}"

    scene yumirain16
    with dissolve

    y "{i}Special?...{/i}"
    s "Yeah."
    y "Because I’m suddenly rememberin’ all this weird shit that never happened but maybe {i}did{/i} happen in another universe?"
    s "Pretty much. "
    y "But if..."
    y "If I’m just gonna go back to {i}not{/i} knowin’ any of this shit soon, the fuck am I supposed to do about it? You gonna just...keep remindin’ me every single time?"
    s "I’m going to try. But there’s no guarantee I’ll be the same person either since there {i}were{/i} four of us but...there aren’t anymore."
    y "What do you mean you won’t be the same person?"
    s "I mean I could go back to the type of teacher who gives you detention."

    scene yumirain17
    with dissolve

    y "You..."
    y "Nah...you’re fuckin’ with me. "
    s "If I am, it’s unintentional. Hell, maybe I even did that shit to you in {i}this{/i} universe but have no recollection of it because my mind’s gotten all tangled up in the threads of time. "
    s "But the fact is that the {i}current{/i} me, the one that you’ve now experienced five separate freshman beach trips with, might not be the one you have in a few months."
    s "Accepting that is just part of living with the burden of truth at this point. And even though you’ll probably forget it when you’re reset again, you know now."
    s "So if you {i}do{/i} carry over and {i}I{/i} don’t, don’t think of that new person as me. I only exist here and now — the same as you. "
    s "And I’m glad that’s the case because I can’t bear the thought of you being like this with anyone other than me."

    scene yumirain18
    with dissolve2

    y "..."
    s "..."
    y "What is that supposed to mean?..."
    s "The same thing you meant when you said I was fucking with you, just in a slightly more obvious way."
    y "..."
    s "..."
    y "Sensei, I-"

    stop music
    play sound "thunder.wav"
    scene yumirain19
    $ renpy.pause(5, hard=True)
    scene yumirain20
    with dissolve3
    play sound "rainloop.wav" fadein 2.0

    y "Jesus, fuck. Shit came outta nowhere. "
    y "It ain’t even supposed to rain to-"

    scene yumirain21
    with dissolve2

    s "..."
    y "..."

    scene yumirain22
    with dissolve2

    y "The fuck do you think you’re doing?..."
    s "That was the part where you were supposed to get scared and grab me for comfort. You missed your cue."
    y "I..."
    y "Missed my..."

    scene black
    with dissolve2
    stop sound fadeout 15.0

    s "Come on..."
    s "Let’s get out of the rain."

    "........."
    "......"
    "..."

    scene yumirain23
    with dissolve2
    play music "littlebunny.mp3"

    "We find shelter beneath a small wooden structure the staff here must use for storage. I don’t know. I’m thinking of other things at the moment."
    "Namely the fact that I’m stuck here with Yumi — a girl who, by all accounts, is meant to despise and abhor me no matter {i}what{/i} timeline we find ourselves stuck in."
    "Yet the only dry spot on my body is a space on my palm that she didn’t release until just a few seconds ago."
    "Her hand was smaller than I expected. But that’s probably just because I’ve never seen her as dainty or fragile even during moments like this where she unintentionally reminds me she’s just another teenage girl."
    "Neither one of us speaks for a staggering amount of time. We just look out at the ocean as it attempts to drown itself and silently contemplate just how long we’re willing to wait here for."
    "Forever would be fine. "
    "Maybe we’ll get lucky and the world will end here so I can experience one last moment with her before everything starts over again."
    "Before I have to seek her out and do this same song and dance. Wait for the past to sink in like my knife in the back of Maya as I manage to forgo the thought of it being {i}her{/i} hand that kept me dry this time."
    "But what does the present mean for the future? And how will finding out that Yumi {i}is{/i} special play into Ayane’s plan for saving the world and marrying me?"
    "Because one time wouldn’t mean much. Two times means something. But what if it’s three or four or five or more and all of them have gone unnoticed because of what we are to one another?"
    "I don’t know {i}what{/i} to think anymore now that the threads are beginning to untangle. But while they loosen their hold on me, they tie harder around someone else."
    "And if I were Yumi right now, I’d be scared. I know that for sure because I {i}was{/i} Yumi once — back when none of this made sense and I struggled to fit my fingers through the noose around my neck."
    "But will she let me untie the one around hers? Or will she keep forcing herself to keep me at bay because this whole fucking {i}world{/i} is scary even {i}without{/i} all of the time shit?"

    y "Would’ve worn my fuckin’ swimsuit if I knew this shit was gonna happen. I’m friggin’ soaked now."
    s "I wouldn’t be opposed to that. In fact, I’ll even volunteer to run back to the room and grab it for you."
    y "Yeah, of course you would. Maybe ditch the sweatpants while you’re at it and grab your own too. You ain’t a pretty sight right now. Even worse than normal actually."
    s "Harsh. And to think I gave you my first kiss..."
    y "{i}Bullshit.{/i} And to think you {i}stole{/i} mine."
    s "I regret nothing."
    s "Just kidding. I regret everything."

    scene yumirain24
    with dissolve

    y "Only thing I regret is not flippin’ you over that fuckin’ ledge."
    s "You mean the one you recently saved me from flipping myself over? Do you regret that too?"
    y "Depends on how much you can teach me about whatever’s goin’ with my brain and shit. Which probably ain’t much based on your track record, but we’ll see."
    s "It’s not your mind, Yumi. It’s the world itself. I already told you that."

    scene yumirain25
    with fade

    y "World...brain...whatever. Shit’s fucked either way. Just make sure there’s pizza at the next slumber party."

    "I take a seat on the floor and watch as Yumi wrings her ponytail out like a washcloth. "
    "Her pajama top sticks to her skin, dripping water onto her thighs that rolls down them only to be soaked up by her socks."
    "But we’re alone in here — there’s no hidden narrator or disembodied voice this time — so I resist the urge to tell her it’d be better if we both strip {i}regardless{/i} of how much I want to."

    scene yumirain26
    with dissolve

    "Of course I still stare at her, though. I’m only human."

    y "Enjoyin’ the show?"
    s "More than you know."

    scene yumirain27
    with dissolve

    y "Pervert..."
    s "That’s me."
    y "..."
    s "..."
    s "So, what were you about to say before we were so rudely interrupted by nature?"

    scene yumirain28
    with dissolve

    y "That you should fuck off forever. And that I don’t care if you’re replaced by some {i}other{/i} you since they all equally suck."
    s "Ahh, so nature was just trying to save me from being insulted again."
    y "Would that really be a huge surprise at this point? What with you apparently bein’ a time traveler or whatever the fuck you’re supposed to be."
    s "Just a really unlucky guy, I think."
    y "I’ll say. All the time in the world and you’re still stuck stalkin’ {i}me{/i} every fuckin’ day of your life. What a waste."
    s "I’d have it no other way."

    scene yumirain29
    with dissolve

    y "Well, you should. Cause all you’re doin’ by even talkin’ to me about this ain’t gonna help at all. The fuck am {i}I{/i} gonna do about it? I ain’t cut out for time travel. I barely know long division."
    s "I could teach you. I’ve got all the “long division” you’ll ever need right here."

    scene yumirain30
    with dissolve

    y "What?"
    s "I was referring to my-"

    scene yumirain31 with hpunch

    y "Oh! Ew! What the fuck, man?!"
    s "Damn. I thought I might actually get a laugh out of that one."
    y "That would require being funny — a thing you definitely are not. So please keep your creepy fuckin’ comments to yourself until the rain stops. Thank you."
    s "So I can start again once the storm is over? Got it. I’ll just keep staring at you until then."

    scene yumirain32
    with dissolve

    y "Don’t do that either...that’s even worse."
    s "Why? You’re beautiful."
    y "Fuck off, man..."
    s "Do you not like being called that?"
    y "I don’t like bein’ messed with..."
    s "I’m not, though. I mean it."
    y "Yeah, but you’d mean that for literally anyone in high school. I could just be a pair of boobs with legs and you’d still be all over me."
    s "If they’re the same ones you have now, probably. They’re extremely impressive."

    scene yumirain33
    with dissolve

    y "Fuckin’ quit it, dude! You’re seriously creepin’ me out!"
    s "I’m on Noriko’s side. You really should stop wrapping yourself up. For my personal benefit, of course."
    y "You fucking-"

    scene yumirain34
    with dissolve

    y "Know what?! How ‘bout I just gouge your eyes out! That way-"

    play sound "thunder.wav"
    scene black

    y "Kyaah! Fuck!"

    scene yumirain35
    with dissolve4

    y "I fucking hate thunder! Why’s it always gotta happen at the worst possible time?!"

    scene yumirain36
    with dissolve

    y "And you-"

    scene yumirain37
    with dissolve2

    y "..."
    s "..."

    "I can hear two things — a storm and the sound of her breathing. "
    "But I can only see one. "
    "Everything else is painted grey."

    y "..."
    s "..."

    scene yumirain38
    with dissolve2

    y "We..."
    y "Um..."
    y "Shouldn’t..."
    y "I..."
    y "I thought I...heard something..."
    s "Shouldn’t {i}what?{/i}"

    scene yumirain37
    with dissolve2

    y "We just..."

    scene black
    with dissolve2

    y "Shouldn’t..."

    scene yumirain39
    with dissolve2

    s "Shouldn’t {i}what?...{/i}"
    s "Say it, Yumi..."
    y "I can’t..."
    y "Doing it once was...already..."

    scene yumirain40
    with dissolve2

    y "L...Let’s just go back to your room! The rain ain’t as...bad as it was before. We’ll be fine."
    s "Okay..."

    scene yumirain39
    with dissolve2

    s "{i}But we should take the back entrance so no one sees me. Doing this was the whole reason I came in the first place.{/i}"
    y "{i}Yeah, whatever. Just...fuckin’ walk.{/i}"
    c "{i}Hah......hah.....haaah!{/i}"
    c "{i}Oh my god.....{/i}"
    c "{i}Yumi?...{/i}"
    c "It’s fucking Yumi?!?!?!"

    scene yumirain41
    with dissolve2

    c "Hahah...hahahahah! Hahahah!"

    scene yumirain42
    with dissolve2

    c "Hahah..."

    scene yumirain43
    with dissolve2

    c "Hah..."
    c "..."

    scene yumirain44
    with dissolve2

    c "..............................................................."

    scene yumirain45
    with dissolve2

    c "AAAAAAAAAAAAHHHHAAAAAAAAAAAAAAAAAAAAAHHHHH!!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "What did {i}you{/i} hear in the rain?"

    $ renpy.end_replay()
    $ beachfive13 = True

    jump beachfive14

label yumispring3:
    scene chikayumiconfront1
    with dissolve2
    play music "normalday.mp3"

    "slanted door, o slanted door — angled like the dutch"
    "a lock to keep the thieves away, a hole to see as such"
    "so when that knockingbird does knock, i hope that you’ll be smart"
    "for open doors are dangerous, like girls with broken hearts"

    play sound "static.mp3"
    scene chikayumiconfront2 with flash
    stop sound

    "hello, my name is JOSEPH and i will be your narrator for the beginning of this event since half of the others are still stuck on the beach i think"
    "so anyway yeah, chika chosokabe had been having a pretty rough go of it lately. but i’m sure you already know that."
    "in fact, right now, she was doing a search on her phone about which acids best dissolve bodies so that, should she encounter that terrible harlot she thought was boning her boyf, she’d know what to do."
    "just kidding. she was looking up concert tickets to try and get her mind off of the fact that the man she deceived herself into believing was loyal was actually a big old manslut."
    "just kidding again. she was still poor, so she was just texting rin."
    "just kidding again again. she was playing candy crush."

    c "Chinami, I’m home."

    play sound "static.mp3"
    scene chikayumiconfront3 with flash
    stop sound

    ch "Welcome home, big sis Chika! Yumi brought Chinami a present!"

    "that’s all the narration you’re going to get about chika though because this is actually a yumi event."

    c "Bought? Or {i}stole?{/i}"

    "ooooh sick burn."
    "okay i’m done for real now."

    y "Ha ha ha, very funny. But I guess this thing {i}was{/i} practically stolen on account of how friggin’ cheap it was."
    c "Mhm. So, what are you doing here exactly?"

    play sound "static.mp3"
    scene chikayumiconfront4 with flash
    stop sound

    y "I’m off today, which is a thing you’d probably know if you remembered how to look at your phone. Been callin’ you nonstop for days and I ain’t heard shit."
    ch "Big sis Yumi used a bad word! Now she has to stand still and let Chinami kick her in the teeth!"
    y "Go ahead, loser. I practiced against Noriko for like three hours yesterday and I’m pretty much a pro at this now."
    c "Was Noriko busy today too? Is that why you’re here?"

    scene chikayumiconfront5
    with dissolve

    y "The hell’s {i}your{/i} problem? Tough day at your little con-factory?"
    ch "Big sis Yumi is vulnerable! Chinami will have victory!"

    scene chikayumiconfront6
    with dissolve

    y "Not if I have anything to do about it, twerp!"
    ch "Rats! Big sis Yumi is too good at blocking! She should fight Chinami like a real man!"
    y "It ain’t fair if I don’t give ya a chance, you know? Bring it, kid!"
    c "Quickly if you can, Chinami. I’m about to make dinner and I only have enough for two."
    y "It’s whatever. I’ll just crash on the futon while you guys eat. I don’t feel like stayin’ at the old place tonight. Too far."
    c "Well, that sucks for you because you aren’t welcome here anymore."

    stop sound fadeout 6.0
    scene chikayumiconfront7
    with dissolve

    y "What? Why? Rich girl gettin’ stingy with the leasing agreement or something? Was only a matter of time. They’re all like that."
    c "No, Touka’s been an angel. I just don’t want you here anymore."

    scene chikayumiconfront8
    with dissolve2
    stop music fadeout 5.0

    y "...What?"
    ch "Did...big sis Yumi do something bad again?"
    c "I don’t know. {i}Did{/i} you do something bad, Yumi?"
    y "Uhh...I don’t know. Probably? But I ain’t really got an idea of anything I did that’d piss you off {i}this{/i} much, so...wanna maybe fill me in?"
    c "Not really. I kind of just want you to get out of here so I can make dinner."

    scene chikayumiconfront9
    with dissolve

    y "What are you-"
    ch "B...Big sis? I think you’re supposed to...give someone an explanation when you’re mad at them..."
    c "That’s right, Chinami. But if you’re friends with someone and that supposed friend stabs you in the back, you {i}don’t{/i} owe them an explanation. So there are exceptions to the rule."

    scene black
    with dissolve
    play sound "tackle.mp3"

    y "Hold on, hold on, hold on!"

    play sound "static.mp3"
    scene chikayumiconfront10 with flash
    stop sound
    play music "thingsthathurt.mp3"

    y "The fuck is this shit about-"
    c "Language."
    y "Nah, I ain’t got time for that right now. The fuck is this shit about stabbin’ you in the back? You’re like the one person I’m consistently good to."
    c "Chinami, cover your ears please. If Yumi’s going to use bad words, I’m going to as well. And you shouldn’t have to hear that."

    play sound "static.mp3"
    scene chikayumiconfront11 with flash
    stop sound

    ch "Ch-Chinami is sure this is all one big misunderstanding! And she’d be really happy if everybody could just get along so-"
    c "Chinami! Earmuffs. "

    scene chikayumiconfront12
    with dissolve

    ch "But...big sis Yumi would never do anything bad to us. She might use bad words, but she’s a good person. She-"

    play sound "static.mp3"
    scene chikayumiconfront13 with flash
    stop sound

    c "She’s a spineless, backstabbing, self-serving bitch. {i}That’s{/i} what she is. And she’s been taking advantage of our kindness for too long. So she’s not welcome anymore."
    y "This...This ain’t about money, is it? Because I can start payin’ you back for moochin’ off you for so long. I just figured the console was something that’d make the kid happy and-"
    c "You really think {i}I’d{/i} get pissed off about {i}money?{/i} Me? Give me a fucking break. I’d have asked you to beg your dad for cash if I gave a single {i}shit{/i} about that."
    y "Well, what the fuck is it then? Because I’ve got no idea what else I could’ve done that’d make you just suddenly friggin’ {i}hate{/i} me overnight."
    c "You’ve got no clue I even know, do you?"

    scene chikayumiconfront14
    with dissolve

    y "Know what?! I ain’t done shit! Least not...anything I’m aware of?!"
    c "Mhm. So I guess you just {i}forgot{/i} who my boyfriend is then. Fair enough. It’s not like I’ve been venting to you about him for months or anything."

    scene chikayumiconfront15
    with dissolve

    y "Your...boyfriend?"
    c "Is that why you did it? You got tired of hearing me complain about not being able to see him and figured this might be a good way to shut me up? Or was all this happening {i}before{/i} that?"
    y "Chika...I don’t know {i}what{/i} you heard, but I’m the {i}last{/i} person you’ve gotta worry about when it comes to stealing your boyfriend."
    c "See, that’s what I thought too! "

    scene chikayumiconfront16
    with dissolve

    c "Up until I saw the part where you two got all “up close and personal” on the beach in the middle of a fucking thunderstorm. Who do you think you are? Some love interest in a romantic drama?"
    y "You..."
    y "You saw that?"

    play sound "static.mp3"
    scene chikayumiconfront12 with flash
    stop sound

    ch "Big sis Yumi..."
    ch "Did you really..."
    ch "Is that true?..."
    y "N-No! I mean...yes! But no! It wasn’t what it looked like! "
    c "Not what it looked like?! You asked to go back to his room! Do you want me to believe you two were playing chess?! "
    c "You were more worried about someone {i}seeing{/i} you than the fact that your knife was halfway into my spine! How could you do this to me?!"
    y "O-Okay! How about we talk about this on the balcony? There’s clearly a fuckin’ {i}major{/i} misunderstanding here and I don’t want to drag the kid into this."
    c "Yeah the balcony’s probably not the best idea either then."
    y "The glass is thick as hell. I’m sure it’ll be fine."

    play sound "static.mp3"
    scene chikayumiconfront17 with flash
    stop sound

    c "Fine for Chinami, sure! But now {i}you’re{/i} going to have to worry about me getting away with murder when I throw you over the fucking railing, whore!"
    y "Chika! Chill the fuck out! Let me explain! It seriously wasn’t what it looked like!"
    c "How gullible do you think I am?! I’ve been watching you closer than anyone! You’ve wanted to fuck him from the start! Don’t even pretend you haven’t!"
    y "If I wanted to do that, I {i}would{/i} have!"
    c "So you {i}admit{/i} that I mean nothing to you! You’ve been faking everything this whole fucking time!"
    y "No! I mean I...uhh...well..."
    c "Spit it the fuck out or someone’s going to be cleaning your guts off the fucking concrete, Yumi!"
    y "It’s hard fucking finding words when you’re threatening my life, okay?! You’re freaking me the hell out! I’ll explain everything! I just...don’t want to die."

    scene chikayumiconfront18
    with dissolve

    if yumicthree == True:
        c "You know, I should have seen this coming the second Sensei suggested you for my threesome present. I bet you felt so fucking smart rejecting that while getting dicked down on the side, didn’t you?"
        y "Don’t blame me for your boyfriend being a fucking pervert. I have no idea why he suggested me. And I {i}had{/i} no idea until you fucking told me about it."
        c "So it’s my fault then? And asking you to be a part of that special thing with me just made you thirsty? Is that it?"
        y "Chika...{i}no.{/i} I don’t look at him that way."
        c "You’re a fucking liar, Yumi. I know for a {i}fact{/i} you look at him that way. I just figured it was one-sided and that you were a good enough friend to keep your fucking hands off of him for {i}me.{/i}"

    c "I trusted you. I’m the {i}one{/i} person who has always had your back. Even when everyone else fucking abandoned you after the Nodoka thing, {i}I{/i} fought for you. Literally. "
    c "And this is my reward? Finding out you’ve been fucking my boyfriend while I break my back trying to figure out why he’s been avoiding me? How do you think that feels, Yumi? You proud of yourself?"
    y "Just let me explain, Chika. It’s really not like that."
    c "I {i}pray{/i} it’s not like that. Because...if it is? I don’t even {i}know{/i} what I’m going to do to you."

    scene chikayumiconfront19
    with dissolve

    y "It’s...obviously true that you saw us together. But I wasn’t pretending to be some character in a “romantic drama” or whatever it is you said."
    y "It just...started raining and we wound up hiding in that fuckin’...closet or...whatever the hell it was. I don’t even remember."
    c "Probably because you were too busy staring deep into his eyes and saying stuff like, “Ohhh we shouldn’t! Someone might see!” The fuck did {i}that{/i} mean if it’s not how it sounded, huh?"

    scene chikayumiconfront20
    with dissolve2

    y "..."
    c "Don’t fucking {i}cry,{/i} pussy. Don’t go around wrecking homes if you aren’t prepared to face the consequences."
    y "That stuff...Chika..."
    y "That...meant how it sounded. And yeah, I...maybe I got caught up in the...moment or something, but...I seriously wouldn’t do that to you..."
    c "There was another line too. Something like...{i}doing it once was already...something.{/i} Which {i}very clearly{/i} implies shit already happened. "
    c "So why not just go ahead and tell me how many times you fucked him that weekend? Now I’m just curious about whether or not you’ve broken my record."
    y "That..."
    y "I’m a virgin, Chika. I’ve seriously never done that with him."
    c "Then what-"
    y "I was...talking about...kissing. "

    scene chikayumiconfront21
    with dissolve2

    c "Kissing?..."
    c "Do you think that makes this more forgivable?..."
    y "It was before you two were even together! And I tried telling you about it, but...you were so fucking blinded by your feelings for the guy that I didn’t want to hurt you!"
    c "I’m not buying it, Yumi. The more you speak, the more it’s starting to sound like this is some big ole’ convenient backstory you came up with in the event you got caught."
    c "At the end of the day, I saw you two curled up together. I heard you ask to go back to his room. And I’ve already had my suspicions about {i}him.{/i} "
    c "I just never thought in a million years it would be {i}you{/i} I’d have to confront about it. You were like a sister to me. "

    scene chikayumiconfront22
    with dissolve

    y "And...you’re like one to me. Which is exactly why I didn’t want to do anything to hurt you..."
    c "Well, it’s very comforting to hear that the only thing preventing you from fucking my boyfriend is “how much you care about me.” But I’ve gotta say, Yumi — that’s not a great best-case scenario."
    c "Because even {i}if{/i} everything you said is totally honest, which I highly doubt it is, you’ve {i}still{/i} been hiding shit from me. "

    scene chikayumiconfront23
    with dissolve

    c "I {i}love{/i} him. You got that? In a way you never could and never {i}will{/i} so long as I’m in the picture."
    c "And you want to know what’s really crazy? I’d {i}still{/i} love him even if he fucked you a hundred times that night because {i}you{/i} probably begged for it."
    y "You’re fucking delusional, Chika..."

    scene chikayumiconfront24
    with dissolve

    c "I know that! I fucking know that already, Yumi! But no amount of mentally preparing myself and tricking myself into thinking I have a perfect relationship could have prepared me for {i}this!{/i}"
    c "Why didn’t you just tell me?! About the kiss?! About the storm?! About any of it?! I gave you plenty of time to try and salvage this and you did nothing!"
    y "Bitch, I fucking tried to. But you’ve been ignoring me ever since the goddamn beach and now I know why."
    c "Right, well...that still doesn’t explain the kissing thing. And the going back to his room thing. And the millions of other things I’m mad at you about right now."
    y "And that’s...fair. You’re right in saying that even the best-case scenario sucks. But shouldn’t you be mad at {i}him{/i} too? {i}Not{/i} the gullible teenager who got swept up in the moment?"
    c "I {i}am{/i} mad at him! I’m mad at everyone! But there’s no one I’m madder at than {i}myself{/i} for taking this long to figure it all out!"
    y "As someone being held against a fuckin’ railing right now, I think I’m gonna have to say you’re a little bit madder at me than you are at yourself."
    c "As the person {i}holding{/i} you against that fucking railing right now, I think I’m gonna ask you not to make jokes. This shit is unforgivable, Yumi. How would {i}you{/i} feel if you were in my shoes?"

    scene chikayumiconfront25
    with dissolve

    y "I don’t fuckin’ know, Chika...That’s just another reason why I try to stay away from all of this bullshit “romance” garbage. Shit’s just a tragedy waiting to happen."
    c "Well, unfortunately, we can’t all be aloof and heartless lone wolves like you."
    y "You at least gonna talk to him about it? Or will pushing me off of your fuckin’ balcony be all you need to get this shit out of your system?"
    c "He’s next. Don’t worry."

    scene chikayumiconfront26
    with dissolve

    y "Can I be the one to call him over then?"
    c "Why? Need some time to make sure you two have the same story? "
    y "I’ll put it on fuckin’ speaker if you want. I don’t need to rehearse shit when everything I’ve said is the truth. "
    y "And unless that douchebag plans on lying to you, which I wouldn’t put past him, he’ll tell you the same goddamn thing I did."
    c "..."
    y "Guess it won’t change shit even if he {i}does{/i} though, right? Since it seems like you’ve already made up your mind about how much I fucking suck."
    c "..."

    stop music fadeout 10.0
    scene chikayumiconfront27
    with dissolve2

    y "I never meant to hurt you, Chika."
    y "I just ain’t good at havin’ feelings."

    scene black
    with dissolve2

    c "Call him."
    y "Now?"
    c "Now."

    stop music
    play sound "static.mp3"
    scene sky with flash
    stop sound
    play music "normalday.mp3"

    s "Wow, what a nice day. I can’t wait for everything to turn to shit."

    play sound "phonering.mp3"

    "My phone begins to ring. And not a second too late."

    play sound "phonebeep.wav"

    s "Hello?"

    stop music

    y "You need to get your fuckin’ ass to Chika’s place right now."
    s "Uhh..."
    s "Why?"
    y "Because she saw us on the beach and now thinks you’re cheating on her {i}with me.{/i}"
    s "..."
    y "Can you just come clear this up, please? I don’t know how to fuckin’ deal with her right now. And chances are I ain’t gonna be allowed here again for a long ass time, so..."
    y "It’d be cool if you could try and set shit straight after all the fuckin’ torment you’ve inflicted on me these past however many school years it’s been."
    c "{i}Give me the phone.{/i}"
    y "Here’s Chika. Good luck."
    s "..."
    c "Hello?"
    s "...Hey."
    c "Are you coming over? Or are you going to run away like a little {i}bitch{/i} just like you’ve been doing for months now?"
    s "..."
    c "..."

    scene black
    with dissolve2

    s "Yeah, I’m on my way."
    c "Cool. Here’s Yumi again."
    s "..."
    y "Bye."

    play sound "phonebeep.wav"

    "Yumi hangs up the phone."
    "I don’t blame her."
    "I just feel bad for getting her involved in one more aspect of a life I never wanted."

    $ renpy.end_replay()
    $ yumispring3 = True
    $ yumi_love -= 10
    $ chika_love -= 10

    "{i}Yumi’s affection has decreased by 10!{/i}"
    "{i}Chika’s affection has decreased by 10!{/i}"
    "........."
    "......"
    "..."

    jump chikaspring4

label yumispring4:
    scene skycold
    with dissolve2
    play music "justlights.mp3"

    "Spring is different from how it’s supposed to be here."
    "Well, I guess it’s not really supposed to be here at all if you really want to get technical about it."
    "But it is. And sometimes, it’s hotter. Sometimes, it’s colder. There’s never any rhyme or reason, though."
    "We seldom even check our phones for the weather forecast anymore since there was only a 25%% chance it’d be correct on any given day."
    "Life at this point is just a sequence of waking up, looking out the window, then opening the front door to try and confirm our suspicions."
    "I thought I had it right today. The sun was shining, the flowers were basking in its light, and I envisioned a world in which this blazer alone would feel like too much."
    "And I was right at first. But now I’m wrong."
    "Now, it’s cold. And while there is no snow to serve as a more physical, tangible reminder of this, there’s still the creeping nostalgia and silence that always comes falling to earth alongside it."

    stop music
    play sound "static.mp3"
    scene yumibridgecold1 with flash
    stop sound
    play music "yumiska.mp3"

    "That silence is quickly broken by ska music, though."

    s "Wow. I can’t even remember the last time I heard this song."
    y "And I can’t remember the last time you said anything that made any amount of sense."
    s "You look really pretty today, Yumi."
    y "Die."
    s "How glad I am that some things never change."

    scene yumibridgecold2
    with dissolve

    y "The fuck are you even doing here? We stopped runnin’ into each other like this fucking {i}years{/i} ago, didn’t we?"
    s "Yeah. Because now we have each other’s phone numbers and can hang out whenever we want."
    y "Soooo...never?"
    s "Never. Every day. Same difference."

    scene yumibridgecold3
    with dissolve

    y "I repeat — die."
    s "We’ve come a long way, haven’t we?"

    stop music
    play sound "static.mp3"
    scene yumibridgecold4 with flash
    stop sound
    play music "justlights.mp3"

    y "Hm?"
    s "Just that you only hate me out of habit, now. We’ve been through too much together for any of that to be authentic at this point."
    y "I have plenty of reasons to hate you still. I barely even have a best friend anymore now that she thinks I’m fucking you."
    s "Actually, current Chika would {i}allow{/i} you to fuck me so long as it's under the pretense that we love one another."
    y "Yeah. Which brings me back to the whole “I barely even have a best friend anymore” shit because your fucking creepy relationship with her somehow rotted her brain and turned her into a sex zombie. "
    s "Oh, I see what you mean now."

    scene yumibridgecold5
    with dissolve

    y "Guess you’re right about going through a lot together, though. Don’t feel the need to run away anymore, at least."
    s "Yeah. I imagine knowing the world could end at any moment sort of overtakes me in the threatening department."
    y "Yeah..."

    scene yumibridgecold6
    with dissolve

    y "What are you doing here?"
    s "Looking for you, I guess."
    y "Why? We settin’ up another apocalypse meeting or something?"
    s "No. Just wanted to see you and wishfully thought we might fatefully bump into one another up here again."

    scene yumibridgecold7
    with dissolve

    y "Mm. We sure have a lot of {i}fated{/i} meetings on top of shit, don’t we? "
    s "Think it means something?"
    y "That we’re...always lookin’ down on everyone else, maybe?"
    s "Oh, cool. I didn’t expect you to actually have an answer. Guess Imani’s been teaching you well if you’ve figured out symbolism now."
    y "She’s...fine."
    s "..."
    y "Still..."
    y "Kind of wish it was you, though."
    s "Uh...did my ears just deceive me? Or did you just-"

    scene yumibridgecold8
    with dissolve

    y "D-Don’t get the wrong idea! There’s just...more pressure on me now! I ain’t allowed to fuck up as much as I could when you were the teacher!"
    s "..."
    y "What?! Don’t just...stare at me, fuckmonkey! Say something!"
    s "I’m glad I met you, Yumi."

    scene yumibridgecold9
    with dissolve

    y "{i}What?{/i}"
    y "Man, you ain’t gonna fuckin’ try to kill yourself again, are you? Because I got major death flags from that."
    s "No, nothing like that. It’s just comforting knowing there’s someone else along for the ride who isn’t going to just forget how long it’s been anymore."

    scene yumibridgecold10
    with dissolve

    y "We don’t...know that for sure, though..."
    y "Blondie says there’s a chance my shit might get reset again even {i}if{/i} I made it through the last...thing. "
    s "There’s a chance for that to happen to any of us. "
    y "Then ain’t it a little dangerous to start talkin’ about how nice it is to have somethin’ that could be taken away at any moment?"
    y "Ain’t that gonna just...make it hurt even more if it actually happens?"
    s "Yeah...I know that better than anyone. At least...{i}now{/i} I know that better than anyone. Someone else held that honor until recently."
    y "Ponytail...right?"
    s "..."

    scene yumibridgecold11
    with dissolve

    y "So {i}she’s{/i} the one you-"
    s "{i}Was{/i} the one. "
    s "I don’t know what I want anymore. Or who. Or...even {i}when.{/i}"
    y "When?"

    play sound "static.mp3"
    scene continuingrestart25 with flash
    scene yumibridgecold11 with flash
    stop sound

    s "I just...feel like there’s more to this sometimes."
    y "More...how?"
    s "It’s hard to explain. But..."
    s "What if this is only one example of Kumon-mi?"
    y "I ain’t followin’..."
    s "Well, you said yourself that you had memories of things that hadn’t actually happened to you before, right?"
    y "Yeah, but...ain’t that shit just from different timelines or whatever?"
    s "Maybe. But different timelines are essentially different worlds, aren’t they? Like...what if there’s a world out there where you and I are talking up here right now while holding hands?"
    y "Then I’m perfectly fine with stayin’ exactly where or {i}when{/i} I am."
    s "Yumi-"

    scene yumibridgecold12
    with dissolve

    y "No, I..."
    y "I get what you’re sayin."
    y "It all just sounds too fuckin’ convenient, though. And it ain’t like we have any way of actually {i}gettin’{/i} to those worlds or...timelines or...whatever the fuck you wanna call ‘em."
    y "So imaginin’ the possibility of something like that ain’t gonna do shit but make you feel even more helpless than you already are."
    s "..."
    y "..."
    s "If you {i}could{/i} go anywhere...at any time...where would you go?"
    y "Feel like we had a similar talk before..."
    s "Well...I imagine we probably did then. But my memory’s shit even {i}without{/i} the interference of time and the divine. So why not just give me {i}current{/i} Yumi’s answer?"
    y "Current Yumi..."
    y "Current Yumi would probably stay right here."
    s "There is no way {i}this{/i} is the happiest you can be."
    y "Yeah. Well current Yumi ain’t about to start fantasizing about worlds where everything goes well for her when she ain’t done shit to deserve it."
    s "Yumi, you’re not-"
    y "Can you spare me whatever bullshit you’ve got to say about how I’m not {i}that{/i} bad just because I ain’t as shitty as I used to be? I’m still a fucking bitch. And {i}you’re{/i} still a fucking predator."
    y "We can’t redeem ourselves for that. We’ve gotta...start over. Build ourselves up from the bottom. But neither of us have it in ourselves to actually do that, so..."
    s "..."
    y "Current Yumi would stay right where she is...and accept whatever punishment {i}time and the divine{/i} have in store for her. The other Yumis can benefit from making better choices than her."
    s "You’ve really grown up, Yumi."

    scene yumibridgecold13
    with dissolve

    y "Rad. Maybe you’ll finally leave me alone now."
    s "Doubtful. I’m bound to fatefully encounter you in higher altitudes for the rest of our lives. It’s just how things work here, I think."
    y "Well, for what it’s worth..."
    y "I’m glad I met you too."
    s "Want to pick up where we left off on the beach and actually kiss now?"

    scene yumibridgecold14
    with dissolve

    y "And risk Chika showin’ up and {i}actually{/i} tossing me over a railing this time? Pass."
    s "We could always go somewhere more pri-"
    y "Don’t."
    s "..."
    y "Just don’t...okay?"

    scene yumibridgecold15
    with dissolve

    y "I’ve already conceded that I don’t hate you. Just take that as a win for now and stop pushing me to do more. I’ve got enough going on in my head as-is."
    y "If I ever want to {i}enable{/i} you, I’ll make the first move. "

    scene yumibridgecold16
    with dissolve

    y "Still ain’t ever gonna happen, though. Not unless {i}time{/i} magically throws us into a world where we’re the same age."
    s "So you’re saying you’d be with me if we were the same age?"
    y "I..."

    scene yumibridgecold17
    with dissolve2

    y "I’m saying you’d have a much better shot."

    scene yumibridgecold18
    with dissolve

    y "That is {i}all{/i} I’m going to say, though...pervert."

    scene skycold
    with dissolve2

    s "I’ll take it. It’s better than knowing I have no chance at all."
    y "Yeah. Meanwhile, I’ll continue wanting to throw up in my mouth for just knowing you {i}want{/i} one."
    s "Yeah...my life would be so much easier if everyone else looked at things like you."
    y "Hah. You think having {i}more{/i} of me around would make your life easier? Only reason I haven’t kicked the shit out of you yet’s because you’re bigger than me. "
    y "Nineteen other Yumi’s, though? You’re fucked."
    s "So many Yumis. It’s like a dream come true."
    y "A nightmare, more like."

    scene black
    with dissolve2

    s "Do you have any plans after this?"
    y "After what? Convincing you to fuck off and leave me alone so I can go back to spitting on cars?"
    s "Yeah. I don’t have any plans for tonight. So I was wondering if maybe-"
    y "Pass. "
    s "Tch. One day, you’ll appreciate me for who and what I am."
    y "Heh. Maybe. "
    y "I’ve already got plans tonight, though. And...lookin’ at the time, I should probably start headin’ over now."
    s "Heading over {i}where{/i} exactly? Should I be worried? Is it a {i}boy?{/i}"
    y "It’s my mom, you fucking douchenozzle."
    s "You’re leaving me for your mom? What kind of soap opera is this?"
    y "You want to come too? Just gonna watch movies and shit."
    s "You’re actually inviting me?"
    y "So long as you don’t say yes. I have to uninvite you if you agree."
    s "Why even give me a choice then?"
    y "Sometimes, you’ve {i}gotta{/i} give somebody a choice. Even if the answer’s already made up. It’s the only way to make ‘em think they’re really free."
    s "None of us are free here. No choice will convince me otherwise."
    y "Yeah, well...we can’t all be as smart as you."
    y "Later, Sensei. I’ll see you when I see you."
    y "Probably on another bridge or something..."

    "Yumi turns to leave, but I decide to stay up here for a little while longer."
    "I don’t plan on spitting on cars or anything like that, though — just passing time while I wait for the world to catch up to how fast I’ve been spinning lately."
    "........."
    "......"
    "..."

    stop music fadeout 25.0
    scene yumibridgecold19
    with dissolve2

    "As the world continues to spin, a single ant attempts to stop it. "
    "The ant’s name is Yumi Yamaguchi — and she will soon learn just how weak she is even {i}if{/i} she can lift things up to fifty times her body weight."

    ri "Oh! Yumi!"

    scene yumibridgecold20
    with dissolve

    y "Hm?"

    "{size=-3}Another cool ant fact is that the queen of the Pogonomyrmex occidentalis owyheei is the second longest living insect with a lifespan of up to 30 years. This is only 20 years less than the maximum lifespan of a termite queen.{/size}"

    scene yumibridgecold21
    with dissolve

    ri "Coming to see your mom? Would you mind giving her this? Mailman left her shit in my box again."
    y "Why do you know my name?"
    ri "Because you’re my new best friend’s daughter, obviously."
    y "Who even are you?"
    ri "Not the mailman, that’s for sure! So please relieve me of needing to hold onto this as I will not be able to resist the temptation of opening it and I can’t handle another felony. I just can’t."

    scene black
    with dissolve2

    y "Fine, yeah. Give it here. Probably just a bill or something."
    ri "Woo! Thanks. Love you. Tell your mom I said hi."
    y "Uh...no?"

    play sound "dooropen.mp3"
    scene yumibridgecold22 with dissolve2

    "Did you know that ants don’t have ears? They listen by feeling vibrations in the ground. And they communicate with other ants by using their body to produce pheromones."

    y "Yuki! You home? Your fucking weirdo neighbor gave me your mail."

    "A group of ants is called a “formicary.” They are social creatures who, like bees, distribute and delegate different responsibilities to everyone in the colony."

    play sound "papertear.mp3"
    scene yumibridgecold23 with dissolve

    y "Let’s see how much you fuckin’ owe. Maybe I can help out now that I’ve actually got a job?"

    "Ants are found on every single continent except for Antarctica. And one species, the trap jaw ant, can close its jaws at a speed of 140mph! How crazy is that?"

    scene yumibridgecold24
    with dissolve

    y "..."

    "Do you know the craziest part of all, though?"

    scene yumibridgecold25
    with dissolve3

    y "..."

    "We’re just like them when you really start to think about it."

    scene black
    with dissolve3

    "We’re all so small in the grand scheme of things — running around in circles and trying to fulfill some sort of arbitrary purpose we come up with that won’t ever {i}really{/i} matter."
    "But we’ll tell ourselves it does because we need a meaning to live. We need a meaning to run around in circles from dusk ‘til dawn."
    "But if you take one ant away, will anyone really notice?"
    "If you’re the queen, sure."
    "If you’re anyone else, though?"
    "How long will it take the others to even notice you’re even gone?"

    $ renpy.pause(5, hard=True)
    play music "phonering.mp3"
    $ renpy.pause(5, hard=True)
    stop music
    play sound "phonebeep.wav"

    "..."

    s "Hello?"

    $ renpy.end_replay()
    $ yumispring4 = True
    $ yumi_love += 1

    jump yumispring5

label yumispring5:
    play sound "static.mp3"
    scene yumisadohno1 with flash
    stop sound
    play music "itsingsinitssleep.mp3"

    y "..."
    s "Yumi?"
    y "..."
    s "I know it’s you. I saw your name on the-"
    y "{i}Where are you?{/i}"
    s "I’m...right where you left me. I told you I didn’t have anything else going on tonight. And I didn’t really have it in me to leave, so-"
    y "{i}Can we meet up?{/i}"
    s "Is...everything okay? "
    y "{i}Please...can we just meet up?{/i}"
    s "Where and when? I’ll head over now. "
    y "{i}I’m...near the bath house. Just walking. But I can stop.{/i}"
    s "I thought you were-"

    play sound "phonebeep.wav"
    scene yumisadohno2
    with dissolve

    s "..."
    s "Yumi?"

    scene black
    with dissolve2

    "I should have stopped her when she told me where she was going."
    "I know Yuki’s been all over the place lately, but I figured she’d have at least managed to hold out and {i}not{/i} be a complete fuck-up if she had plans with Yumi."
    "She’s tried so hard to make things right with her. And I really don’t want to believe she’d just throw that all away out of nowhere, but..."
    "I guess it’s just a lot more tempting to ruin everything once it’s all neatly laid out before you."

    play sound "footsteps.mp3"

    "No..."
    "I shouldn’t make assumptions just yet. Even when I know they’re the most likely scenario."
    "I need to {i}hear{/i} what happened first. I need to {i}see{/i} with my own eyes just what-"

    play sound "static.mp3"
    scene yumisadohno3 with flash
    stop sound

    y "..."

    "Before I know it, I’m here."
    "I spoke to myself throughout the whole trip because no one else would. And throughout that time, I repeated those same words over and over."
    "I need to hear what happened. I need to see it with my own eyes."
    "But this isn’t what I wanted to see. Why would I think that? "
    "Why would I subject myself to the pain that will surely come from whatever it is she has to say when I know complaining about it will only make me look weak when compared to her?"
    "Who am {i}I{/i} to pretend to know that sting? The kind she’s not only felt countless times in the past, but has been openly {i}prepared{/i} for ever since letting that woman back into her-"
    "No."
    "I need to hear what happened. I need to see it with my own eyes."
    "{b}I need to be a father. {/b}"
    "She has no one else."
    "They’ve all fallen off the ledge."

    y "..."
    s "I’m here."
    y "Thank you."
    s "So what’s-"
    y "I don’t...want to talk about it."
    y "And I didn’t want to...bother you again. But Chika’s...a whole thing and...Noriko’s at work. "
    y "I ain’t got nobody else."
    s "But...you {i}don’t{/i} want to talk about it."
    y "No..."
    y "Not...right now at least."
    y "I just didn’t want to be alone."
    s "..."
    y "..."
    s "Where do you want to go then? Because I doubt you want to be out here in the cold."
    y "Anywhere. I don’t care."
    s "Alone though, right?"
    y "I already told you. I don’t care."
    s "Well...you still have Chika’s old apartment, don’t you?"
    y "Technically. They shut off the power, though. I didn’t know how to pay the bill and...I felt weird about asking Chika."
    s "Well, we can’t go to my house because of Ami and my secret pop-star girlfriend. And we can’t go to my secret apartment because of my secret gyaru girlfriend. So...what does that leave us with?"
    y "Karaoke booth?"
    s "Pass. I have bad luck in those. I’ll probably attack you again."
    y "Go for it. Fuck if I care anymore."
    s "..."
    y "..."
    s "It’s going to be okay, Yumi."

    scene yumisadohno4
    with dissolve

    y "Spare me the bullshit, okay? I don’t need you to console me or baby me or pretend you know what’s going on. I just..."

    scene yumisadohno5
    with dissolve

    y "I don’t want to be alone..."
    s "..."

    scene yumisadohno3
    with dissolve

    s "You really don’t care where we go?"
    y "Just pick somewhere nobody else is gonna bother me. "
    y "Tragedy follows you the same way it follows me, though. So chances are, shit ain’t gonna be calm no matter {i}where{/i} you fuckin’ take me."
    s "..."
    y "..."
    s "Do you mind if I make a phone call really quick?"
    y "Please don’t fucking get Chika involved. I really don’t want to deal with her right now."
    s "I’m not. I’m just going to call Ami and tell her I’m not coming home tonight."

    scene yumisadohno6
    with dissolve

    y "What? Why?"
    s "You’ll see."
    y "But-"
    s "Just hold on one second, okay?"

    scene clearnightsky
    with dissolve2

    "The phone only rings once. Ami never lets it go any longer."

    play sound "phonebeep.wav"

    a "{i}Hi Dad! Miss you! Love you! Come have sex with me?{/i}"
    s "Well, I’m glad I didn’t have you on speakerphone just now."
    a "{i}Boooo. I was hoping you did. What’s up?{/i}"
    s "I’m not coming home tonight. Could you let Niki know too?"
    a "{i}Uhh...why? If I’m...allowed to ask.{/i}"
    s "Are you sure you want to?"
    a "{i}Are you sure I’m not going to find out anyway?{/i}"
    s "Just tell Niki, okay? And don’t worry about me. I’m safe."
    a "{i}Well, what am I supposed to tell Aunt Niki then?{/i}"
    s "I don’t know, you’ll come up with something."
    a "{i}But Dad-{/i}"
    s "I love you. Okay?"
    a "{i}Mm...{/i}"
    a "{i}Fine...{/i}"
    a "{i}But you owe me extra cuddles tomorrow! No exceptions.{/i}"
    s "I’ll see what I can do. Goodnight, Ami."
    a "{i}Night, Dad.{/i}"
    a "{i}Please stay safe.{/i}"

    play sound "phonebeep.wav"
    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene yumisadohno7
    with dissolve2

    y "Hearing you be all cute with your little incest demon like that seriously makes me sick."
    s "Don’t listen then. I don’t know what to tell you."

    scene yumisadohno8
    with dissolve

    y "{i}Hah...{/i}Now what? You’ve clearly got a plan. Let’s hear it."
    s "Yeah, I’m gonna need you to just go along with me on this one and not ask any questions."
    y "I’m gonna wake up in a trunk tomorrow, aren’t I?"
    s "Worse."
    y "Fantastic."

    scene black
    with dissolve2

    s "Come on. Follow me. It’s not that far."
    y "Go slow, please. I don’t have the energy right now."

    "I do as she says, matching her pace on the way to somewhere I can’t imagine she’d ever follow me under normal circumstances."

    play sound "static.mp3"
    scene yumisadohno9 with flash
    stop sound

    y "A love hotel? Really?"
    s "It’s cheap. It’s private. And we can stay as long as we want."
    s "Plus, there are complimentary condoms in the event that you want to have sex with me to take your mind off of everything."
    y "Thanks. I’ll keep that in mind. "
    s "Please don’t. It was only a joke to lighten the mood. Going down the same path I take to deal with pain isn’t something I wish upon virgins like you."

    scene yumisadohno10
    with dissolve

    y "It’s fine. {i}This{/i} is fine too. We can just...watch TV or something."
    s "And...not talk."
    y "Yeah."
    s "..."
    y "..."
    s "Are you {i}sure{/i} that’s what-"

    scene yumisadohno11
    with dissolve

    y "Jesus Christ, {i}yes.{/i} You gonna ask me that all night?"

    scene black
    with dissolve2

    s "Well, forgive me, but it’s not every day I get a call from a you who’s clearly struggling with something. I want to help."

    scene yumisadohno12
    with dissolve2

    y "Then just let me go at my own fuckin’ pace, okay? Our whole fuckin’ relationship is you tryin’ to dictate that shit for me. Just give it a fucking break already."
    s "Fine...I’ll just...stare at you then."

    scene yumisadohno13
    with dissolve

    y "Stare at the TV. They’ve gotta have something on there that ain’t just porn, right? Put something on. I don’t want silence."

    "I grab the remote and-"

    scene yumisadohno14
    with dissolve

    woman "{i}Aah! Aah! Harder, Daddy! Fuck me with your big, hard cock!{/i}"
    y "Next, please."

    "I change the channel."

    scene yumisadohno15
    with dissolve

    man "{i}Aah! Aah! Harder, Daddy! Fuck me with your big, hard cock!{/i}"

    y "This is the same thing, just with two dudes instead."

    "I change the channel again."

    woman "{i}I see you don’t have a lifeguard here at your beach.{/i}"
    man "{i}I’m not at the beach. This is a bathtub.{/i}"
    woman "{i}No body of water is safe without a lifeguard.{/i}"
    man "{i}It’s two feet deep, lady. What are you doing here?{/i}"
    y "This is porn too, isn’t it?"
    s "No, this is a bathtub."

    "I change the channel one last time because Yumi isn’t ready for greatness yet."

    y "Oh, good. A talk show. I hope they’re wearing pants beneath that desk."
    s "Anything can be porn when you think about it that way."
    y "You ain’t wrong, I guess. Ready to shut up for the rest of the night?"
    s "Did you really just want me here to take up space? "
    y "There a problem with that?"
    s "I mean...not really. But if this is just you being a tsundere again while you work up the courage to say something-"

    scene yumisadohno16
    with dissolve

    y "I don’t know {i}what{/i} to fucking say! Okay?!"

    scene yumisadohno17
    with dissolve

    y "I don’t know what to {i}think!{/i} I don’t know what to {i}do!{/i} I just want to sit here and wait for all of this to be over! So stop fucking reminding me that everything is going to shit! Okay?! I know! I fucking know!"
    s "..."

    scene yumisadohno18
    with dissolve

    y "Just..."
    y "If you really want to help, just sit with me. That’s all I want."
    s "..."
    y "..."
    s "Okay."

    scene black
    with dissolve2

    "I stop prying and just...exist in the same place as Yumi — letting the booming voices of some exuberant TV personalities drown out the distant sounds of other couples having sex."
    "And while we both know that’s happening, neither one of us ever really reacts apart from a quick glance at the wall to try and confirm climaxes behind the scenes."
    "There is no “gradually getting closer” or “the crumbling of whatever walls we’ve put between us.” Just...TV. The light that bleeds out of it. Sadness. Free condoms we’ll never use."
    "This goes on for hours. And the only change in the environment is the way the bed shifts when one of us gets up to use the restroom or get a drink of water."
    "It always ends the same way, though — right back here on the bed. Where we’ll stay until Yumi has sufficiently rotted the misery out of her body."

    stop music
    play sound "static.mp3"
    scene yumisadohno19 with flash
    stop sound
    play music "heartbeat.mp3"

    y "..."
    s "..."

    "I guess it might take a little longer than just a few hours, though."

    s "I really {i}am{/i} okay with sleeping on the floor, Yumi."
    y "I’m not gonna fuckin’ make you do that. Who knows when the last time they cleaned this carpet is?"
    s "It’s not that bad when you think about how many people have had their cum washed out of these sheets."
    y "Great. Now I’m {i}definitely{/i} not going to be able to sleep."
    s "Yeah...I doubt I will either."
    y "Don’t say something creepy, please. I don’t want to deal with it right now."
    s "I won’t. I’m moreover just talking about how I don’t normally sleep fully clothed. But I’m making that sacrifice for you."
    y "Way to take one for the team. "

    play sound "static.mp3"
    scene yumisadohno20 with flash
    stop sound

    "We’re not touching, but we might as well be."
    "I can feel the heat from her body, embracing me from behind like it's the big spoon and I’m a plastic fork someone pulled from the trash to eat leftovers from a takeout container."
    "She seems calmer now, at least. Turns out keeping my mouth shut really did help in some capacity."
    "But it doesn’t change the fact that I want to know what’s going on inside of her head."
    "I guess that was true before tonight, though."
    "I guess I’ve always wanted to know more about her. And I guess she’s...finally {i}okay{/i} with me wanting that if she’s going to trust me to sleep in the same bed as her."

    play sound "static.mp3"
    scene yumisadohno21 with flash
    stop sound

    "I could ruin it so easily. And it wouldn’t even have to be intentional."
    "She knows it too. "
    "She knows it, and she’s trusting me anyway."
    "I can only imagine how much she must be hurting if that’s the case."

    y "..."
    s "..."
    y "Sensei?..."
    s "...Yeah?"
    y "What was your mom like?"

    play sound "static.mp3"
    scene forgetthisimmediately with flash
    scene yumisadohno22 with flash
    stop sound

    s "..."
    y "..."
    s "I can’t remember..."
    y "Oh..."
    y "I see..."
    s "Why do you ask?"
    y "Chika makes her mom sound like the greatest woman who ever existed..."
    y "Ayane seems like she was crazy about hers too..."
    y "Four-eyes doesn’t seem to like hers that much, but she didn’t seem that bad when I met her."
    s "..."
    y "Is it hard?..."
    y "Raising a kid?..."
    y "It’s gotta be, right?..."
    s "It is..."
    s "I...haven’t been doing it for long, though."
    y "Ain’t you been with Ami for like half her life?"
    s "Yeah, but I didn’t start trying until recently."
    s "Her mother..."
    s "Was also amazing, though. In her own ways."
    y "Yeah?..."
    s "Yeah."
    y "..."
    s "..."

    scene yumisadohno23
    with fade

    y "..."
    s "..."
    s "Are you still awake?"
    y "Yeah..."
    s "Do you want me to turn the TV back on?"
    y "No...it’s fine."
    s "And you’re sure you don’t want me to sleep on the floor?"
    y "Don’t leave me, please."
    s "I...won’t. I’m shocked you’d word that so embarrassingly, though."
    y "I need you here."
    y "I really do."

    scene yumisadohno24
    with fade

    s "You know..."
    s "And let me just preface this by saying I’m not trying to get you to talk to me right now...but you can rely on me whenever you need, Yumi."
    y "I know...that’s why I called you."
    y "You...You definitely don’t...make me feel {i}safe{/i} or anything but...I...feel safe when you’re with me? Does that...make sense?"
    s "No. No, that doesn’t make sense at all. But as long as you know."
    y "Yeah...I know."
    s "..."
    y "..."
    y "I’m gonna try and go to sleep now..."

    scene yumisadohno25
    with dissolve

    s "Okay..."
    s "I’ll do the same then."
    y "Okay..."
    s "Wake me up if you need anything."
    y "Okay..."
    s "..."
    y "..."
    s "Goodnight, Yumi."
    y "Goodnight, Sensei..."

    scene black
    with dissolve4
    $ renpy.pause(12, hard=True)
    stop music

    y "I think my mom has cancer."

    scene yumisadohno26
    with dissolve4
    $ renpy.pause(4, hard=True)

    s "..."
    y "..."
    s "..."
    y "..."
    s "..."
    y "..."
    s "What?..."

    scene yumisadohno27
    with dissolve4

    y "She got a letter in the mail today..."
    y "I..."
    y "I saw something about...um..."
    y "I forget the word...I..."
    s "..."
    y "She’s seemed...weird lately..."
    y "Do you think she-"

    scene yumisadohno28
    with dissolve3

    s "..."
    y "..."

    scene yumisadohno29
    with dissolve2

    y "..."
    s "..."
    y "Thank you..."
    s "..."

    "I don’t say anything."
    "How could I?"
    "I just hold her and hope, by the means of some miracle, that the world we’re in will fix it."
    "Is that too much?"
    "..."
    "It’s not...right?"

    scene yumisadohno30
    with dissolve2

    y "I’m...gonna try and go to sleep again."
    y "And I’m out of bad news to spring on you out of nowhere this time, so..."
    s "I’ll be here."
    y "Yeah..."
    s "..."
    y "Thank you..."
    y "Sensei..."

    $ renpy.end_replay()
    $ yumispring5 = True

    jump yumispring6

label yumispring6:
    scene yuminextday1
    $ renpy.pause(5, hard=True)

    "And when the morning comes, don’t wake. Stay closed, oh tired eyes."
    "With distance still and bones to break, the shape of our demise-"
    "Shall mold the neon hearts we share, remind us who we are."
    "Survivors in a dying world. Two strangers in two cars."

    scene yuminextday2
    with dissolve4

    y "..."

    "Mildew again."
    "Familiar, but not. "
    "Now masked by the smoke-tendril arms of cheap scented candles, this is nothing like the floor of an old, lived-in apartment."
    "This is a place where people come to forget under the pretense of making memories. And it is somewhere you never thought you’d see come the morning after."
    "Tell me, Friend — what did you dream of last night?"

    scene yuminextday3
    with dissolve2

    y "..."

    "Ignore me all you like. It does not change the fact that I grow within you like that dragon grows in her."

    y "Sensei?..."
    s "........."

    "How comfortable it must be — to have the arms you’ve always dreamt of plunged deep in the stomach of your nightmares — draped over you like the curtains you plucked from the side of the road just last month."
    "They smell of mildew too, I’m sure. You haven’t learned how to get rid of it yet. And that’s just one of the many things you likely won’t {i}ever{/i} learn if you stay where you are now."

    scene yuminextday4
    with dissolve2

    y "{i}Hah...{/i}"

    "Would you like to go back, Yumi?"

    y "..."

    "Because you {i}can.{/i} "
    "All you need to do is make a wish."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    "She lightly removes the arm of the man who comforted her last night, placing it gently by his side as she seizes a very rare opportunity to get a look at his face while he can’t see hers."

    scene yuminextday5
    with dissolve4
    play music "memories2.mp3"

    "Her gaze lingers on his eyes — closed and moving rapidly behind his eyelids like the sockets are full of worker ants. Like his body is their underground lair."
    "She thinks about removing his glasses. She didn’t want him to risk breaking them if he rolled over now that he wasn’t anchored to her body. "
    "She doesn’t, though. "
    "She just stares at him. Half thankful. Half cherished. Two halves that were entirely unfamiliar to her, yet combined to create something or somewhere that just felt right."
    "But one good thing in a sea of bad things can not offset that ever-encroaching darkness. And while {i}these{/i} halves were good ones, there were two others that {i}always{/i} dragged her down."
    "They followed her everywhere. They determined everything about her life. Yet, she was afraid to leave them behind because she was unsure of what else she might find."

    y "..."

    "She decides to keep staring.."

    s "......Yumi?"

    "He decides to wake up."

    y "..."
    s "What time is it?..."
    y "I don’t know..."
    y "You can go back to sleep, though. It’s fine."
    s "What are you going to do?..."

    scene yuminextday6
    with dissolve

    y "I have to get ready for school."
    y "I imagine it’s still pretty early since I can’t hear anybody fucking anymore."

    scene yuminextday7
    with fade

    s "School? Are you kidding? Take the day off. You’ve never had a better reason to skip than this."
    y "Yeah, that’s exactly why I ain’t doin’ it this time. "
    s "Explain?"

    play sound "static.mp3"
    scene yuminextday8 with flash
    stop sound

    y "The fuck do you think is gonna happen if I just do my own thing again all day?"
    s "I-"
    y "Question ain’t for you to answer, numbnuts. It’s one of those rhetorical ones or whatever they’re called."
    y "If I stay here, I’ll wind up beatin’ myself up until I feel even fuckin’ worse. And you saw me last night. This shit fucking sucks. Figure school will at least distract me."
    s "I can be a distraction too. Going to school now is-"

    scene yuminextday9
    with dissolve

    y "You’ve done your part already, okay? I mooch off you any longer and Chika won’t even be able to convince herself she’s “winning” anymore."

    scene yuminextday10
    with dissolve

    y "I’ll pay you back for the room as soon as I can. But-"

    play sound "static.mp3"
    scene yuminextday11 with flash
    stop sound

    y "..."
    s "But...what? "
    y "Uhh..."
    y "Nothing."

    play sound "static.mp3"
    scene yuminextday12 with flash
    stop sound

    y "Just...I’ll pay you back as soon as I can. Maybe Noriko can ask the boss to give me an advance on my next paycheck or-"
    s "You don’t need to pay me back. Put it toward getting the power back on at Chika’s old place. I can help you pay the bill."
    y "I already fuckin’ told you you’ve done enough."
    s "By spending one night with you and barely saying anything?"

    scene yuminextday13
    with dissolve

    y "You...hugged me and shit too..."
    s "And that {i}helped?{/i}"
    y "Helped me...realize there’s still some shit out there scarier than cancer, yeah."
    s "..."
    y "..."
    s "Don’t go to school today."

    scene yuminextday14
    with dissolve

    y "You ain’t gonna talk me outta this, Sensei...but I...appreciate you looking after me."
    y "Just want to...try and get shit back to normal. Forget I read anything. Probably just...some kinda misunderstanding anyway. "
    s "Or...we could talk about it."
    y "We do that too much now."
    y "Like...don’t you ever miss the days when I was just some fuckin’ delinquent you’d chase around on your quest to fuck every high school girl in Kumon-mi?"
    s "Sometimes. But then I think about things like this and how, if we hadn’t ever become more, that you’d be all alone during the hardest times of your life."
    y "You mean like what I’m tryin’ to do right now despite you practically beggin’ me to stay?"
    s "Exactly. Now sit back down or I’m going to come back to school for the sole purpose of making sure you have detention every day for the rest of your never-ending school life."
    y "Never...ending..."

    scene yuminextday15
    with dissolve

    y "Wait...yeah..."

    scene yuminextday16
    with dissolve

    y "If we’re fuckin’ stuck here and shit, that means Yuki ain’t gonna go anywhere...right?! Her thing’ll just...reset! Back to normal! Right?!"
    s "I..."

    scene yuminextday17
    with dissolve

    y "Right?..."
    s "I don’t know, Yumi."

    scene yuminextday18
    with dissolve

    s "The thing with Makoto’s dad is really the only example we have of death within the timeloops. And it’s not like we can just call him up to see if he’s alive again."
    s "Like...maybe if we get {i}another{/i} call about him dying, we can assume things like that can happen. But without anything to go off of, we’ve just..."
    y "Yeah. Okay. I get it."

    scene yuminextday19
    with dissolve

    y "Anyway, school. See you."
    s "Just like that? You’re not even wearing your uniform."
    y "My-"

    play sound "static.mp3"
    scene yuminextday20 with flash
    stop sound

    y "Ahh, fuck. Forgot about that."

    scene yuminextday21
    with dissolve

    y "Not exactly...used to spending the night in...seedy love hotels..."
    s "Guess you have no choice but to skip school entirely then."

    scene yuminextday22
    with dissolve

    y "It’s barely past five in the morning. I’ve got time to make it to the dorms and get changed beforehand. "
    s "Can I walk you {i}there{/i} at least?"
    y "No."
    s "Why?"
    y "Because walking out of a love hotel with a girl like me ain’t gonna be good for your public image. Nor would be walking me to the dorm while everyone else is getting ready."
    y "You think I wanna be bombarded by questions right now, man? If I’m alone, people will just do what they always do and avoid me. That’s exactly what I need from everyone but {i}you{/i} apparently."
    s "You’re not even going to tell Chika then? Because I feel like she’d be better at dealing with this sort of thing than literally anyone since she’s essentially gone through it already."
    y "Yeah, that’s why I said she’s a “whole thing” yesterday."
    s "Oh. I thought you were just talking more about how my penis broke her."
    y "Yeah, that definitely doesn’t help. But even if you broke her, she’s still my best friend. I don’t want to bring back bad memories."
    s "I’m sure she’d be fine with it under the circumstances, Yumi."
    y "Probably...but still."
    s "At the very least...talk to your mom. If you can find her, at least."

    scene yuminextday23
    with dissolve

    s "She hasn’t exactly been {i}reliable{/i} lately, and...I guess now I’m starting to understand {i}why.{/i} But I had no idea something like {i}this{/i} was-"
    y "Can’t I just ignore it?..."
    y "Can’t we just...try and see if the reset thing takes care of it?"

    scene yuminextday24
    with dissolve

    s "..."
    y "..."
    s "What if it doesn’t, though?"
    y "Then I guess it’s good I’ve already gotten used to how it feels when she ain’t around."
    s "Yumi...you don’t mean that."
    y "Of course I don’t fuckin’ mean that..."
    y "But it’s easier to say than admitting I was starting to fucking {i}forgive{/i} her."

    scene yuminextday25
    with dissolve

    y "It’s easier to say than thanking her for making an effort for the first time in her fucking life! Easier than letting her try to be a part of mine! "
    y "I was fine without her! She could’ve just stayed gone! But now she’s shown back up, made me realize what I’ve been missing all these years, and she’s just going to leave me again?! What the fuck?!"
    s "..."

    scene yuminextday26
    with dissolve

    y "Sorry, I...didn’t mean to yell. I know it ain’t your fault."
    s "You can hit me if you want too. I make a good punching bag in times like this."
    y "Yeah, I bet you’d fucking like that, wouldn’t you?"
    s "Maybe under happier pretenses, yeah."

    scene yuminextday27
    with dissolve

    y "..."
    s "..."
    y "Thank you again. For...all of this."
    s "Thank you for not reporting me to the police after I assaulted you on a bridge. That single decision is what made it possible for us to grow this close."
    y "Best thing I’ve ever not done, I guess."
    s "Have fun at school, Yumi."
    y "Yeah...I’m off."

    play sound "static.mp3"
    scene yuminextday28 with flash
    stop sound

    "Black oak door, carpet floor. Everything you’d want and more!"
    "But just because you’re pining for a place to go to hide from your-"
    "Regrets or past, ole’ childish lore. Not quite recalled, yet not ignored."
    "All of this shan’t come to pass. Not the chiming of distant bells that signal to you when it’s time to bend, nor the slowly manifesting sound of an EKG that becomes evermore haunting the longer it drones on for."
    "Could this be a case where you’d {i}want{/i} to welcome that pain, though?"
    "Is one’s perpetual suffering worth the joy their presence brings you? And if that person has sinned, would such a fate be deserved? "
    "How much pain is enough for you, Yumi? What is it that {i}you{/i} want?"

    y "{size=-15}Bite me.{/size}"
    s "Hm? Did you say something?"

    "Yes... acknowledge me! Cultivate me! Let me grow in fields I’ve never seen before! Let me breathe in the stagnant, stale air of love hotels and dilapidated apartments! I can smell the pork broth from here!"

    y "No...just a sigh. "
    s "Oh...Okay then."
    s "Guess I’ll just...be here. "
    y "Yeah..."
    s "Call me if you need me."
    y "Yeah..."
    s "..."
    y "..."
    s "..."
    y "..."

    "Go! Experience life! Distract yourself from {i}me!{/i} For {i}I{/i} will be the one to-"

    scene black
    with dissolve
    play sound "footsteps.mp3"

    y "{size=-15}I said bite me...{/size}"
    s "Yumi?"

    scene yuminextday29
    with dissolve2

    s "Did you forget-"
    y "Yes."

    scene yuminextday30
    with dissolve2

    y "{i}Chu.{/i}"

    scene yuminextday31
    with dissolve2

    s "..."
    y "..."
    s "Uhhh..."
    y "{i}Now,{/i} I’m off."
    s "You just kissed me."

    scene yuminextday32
    with dissolve

    y "So what? Ain’t like we haven’t done that before. This one had nothing on our first."
    s "You...just kissed me."
    y "Yeah..."
    y "You earned it."

    scene yuminextday33
    with dissolve

    y "But if you tell anyone, you will die."
    s "..."

    scene yuminextday34
    with dissolve

    y "I’m off!"
    s "Yeah..."

    scene black
    with dissolve2
    stop music fadeout 12.0

    s "Have fun at school..."

    "She thought about something for a second."
    "She thought about casting aside her typical lone-wolf personality in favor of one who enjoys herself a little more."
    "But she backtracked the moment she made it onto school grounds and saw the way her peers scattered like roaches once the lights go on."
    "She turned her phone off shortly after that. It kept ringing, but she didn’t know what to say to the voice she expected to hear on the other end of it. "
    "Soon, her best friend found her. Turns out she had gotten a call as well. So she asked Yumi if everything was alright."
    "Yumi lied and said yes. It was at that point she began to question everything."
    "She needed a distraction to distract her from the distraction now. "
    "And so she found one — hyperventilating in the bathroom and telling herself that everything was going to be okay."
    "It was the youngest she felt in years."

    stop music
    scene thething

    "the end."

    scene black

    $ renpy.end_replay()
    $ yumispring6 = True
    $ yumi_love += 5
    $ yumiblock = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label yumispring7:
    scene black
    $ renpy.pause(4, hard=True)
    play music "oldphonering.mp3"
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene stickbug with flash
    stop sound
    play sound "knock.mp3"

    "stickbug, stickbug, ocelot\nyou won’t believe the news i’ve got"
    "a god came down and spoke to me\ni followed it into the sea"
    "stickbug, stickbug, ocelot\nmy precious little cosmonaut"
    "spaceships come and spaceships go\none day you’ll say i told you so"

    $ renpy.pause(3, hard=True)

    stop music

    "././././././././"
    "Will you answer it?"

    stop music

    menu:
        "Yes":
            play sound "phonebeep.wav"

            "You pick up the metaphorical phone."

            q "stickbug, stickbug, ocelot\nyou won’t believe the deals we’ve got"
            you "I’m sorry, but I don’t want any."
            q "half off bread and half off pie\nso cheap and fresh you’ll want to die"
            you "I’m sorry, but I would appreciate it if you’d stop calling this place."
            q "stickbug, stickbug, ocelot\nwhat happens when the raining stops?"
            you "I don’t-"
            q "thunder, lighting, sometimes hail\ni’m looking for your mother’s whale"

            scene black
            $ renpy.pause(5, hard=True)

        "No":
            scene black
            $ renpy.pause(5, hard=True)

    play sound "static.mp3"
    scene yumicandy1 with flash
    stop sound
    play music "hometown.mp3"

    "oh my fucking me, are you really doing this right now? visiting your drug-addled bitch of a mother instead of sucking your teacher’s wang with so much force it pops off and gets stuck in your throat?"

    y "Sure am. Or at least I would be if the key fucking worked."

    play sound "doorlocked.mp3"

    y "Did that bitch really change the locks on me?..."

    "why are we here in the first place? to repay the kindness you’ve never received? because you’re sure as hell not going to fuck her. it’d be cool if you did, though. a plot twist, yeah. but cool."

    scene yumicandy2
    with dissolve
    play sound "doorlocked.mp3"

    y "This fucking...does she expect me to pick the lock or something?"

    "just a guess here, but i’m pretty sure she doesn’t expect to see you at all based on the fact that she’s actively pushing you away right now."

    "{i}A girl was at war with a thing inside of the girl and I am a new voice, not to be confused with the one who isn’t capitalizing things that are meant to be capitalized right now.{/i}"
    "{i}I will not be here for long. Just long enough to guide you to the place that you are going. A special place. Good place. Made of sugar and sweat and formed into a mostly edible ball.{/i}"
    "{i}Mercutio would tell you it’s no bigger than an agate stone on the fore-finger of an alderman. But unless you plan on biting off the head of the fairies’ midwife, its size matters not.{/i}"
    "{i}What matters is the taste. And how a single fleck of that sugarsalt will have you crawling back for more///even when your legs stop legging.{/i}"

    play sound "static.mp3"
    scene yumicandy3 with flash
    stop sound

    "did you just hear something?"

    y "I hear something every second of every fucking day now thanks to you."

    "not me. something else. something-"

    stop music

    play sound "lock.mp3"
    scene yumicandy4 with hpunch

    y "Ah. Got it."
    q "stickbug, stickbug, ocelot\nbring me all your ants."

    scene yumicandy5
    with dissolve2

    y "Huh?..."

    play sound "static.mp3"
    scene yumicandy6 with flash
    stop sound

    q "coat their heads in sugarsalt\nstuff them in my plants"
    y "..."
    q "sorry, i meant pants. stuff them in my pants."
    y "..."
    q "..."

    "yo, what?"

    play sound "pop.mp3"
    scene yumicandy7
    with hpunch
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene yumicandy8 with flash
    stop sound
    play music "sawdad.mp3"
    $ renpy.pause(5, hard=True)

    "There’s more than just a Hall of Mirrors."
    "I’ve heard rumors on the rapevine right next to Heaven’s Web there’s an entire world of them."
    "We’d climb it in our younger days — spend hours picking leaves off — the kind that we speculated would never break our fall — yet here we are today. Silent and scared."
    "Some might call it sleeping."
    "But me? I’ve always been the type to pull the petals off of whatever flowers we find in the garden. Preserve them in books so that one day, when I learn how to read, I can remember those moments."
    "The ones in which everything still felt young and new. Before we lost which part of the circle we were in. Now everything feels like a barrier and we can never figure out where we started."
    "In the beginning of someone’s end, there was little more than a ball of light."
    "Mercutio would tell you it’s no bigger than an alderman on the fore-finger of an agate stone."
    "But Mercutio is a liar — for I have decapitated the fairies’ midwife and placed the head of Queen Mab on a pike mere blocks from that rapevine we used to climb."
    "It is bigger now. Like us."
    "Which is probably why we never sleep at all anymore."
    "It’s dark beneath its shadow — and the world of mirrors reflects it every which way."
    "Tell me — what are {i}you{/i} afraid of?"
    "And where would you rest in a world made of mirrors?"

    scene yumicandy9
    with dissolve3

    y "...hm?"

    scene yumicandy10
    with dissolve2

    y "Wha-"

    play sound "static.mp3"
    scene yumicandy11 with flash
    stop sound

    y "What the fuck is...where am...huh?!"

    "One more light in the lamp — a mark on a list that grew like an ant-filled plant dancing with aunts on a ramp in a trance like an enchanted tramp clamp. So I start to recant but I can’t."
    "And I can’t recant because of the cramps. Because my clothes are too damp. So I plug my timestamp into an amp and get gassed as the downcast grass rushes half past the outcast mast."
    "Is it time to go to class? Never. This past surpassed cast hast been fast yet not vast. It’s a blast, this caste — full of masks and casks and masques and casques. But I just have one question to ask."
    "If Jack’s axe wants to fax some facts to the snack-shack in exchange for sacks but only receives tacks, does he tax the tacks or send them back due to cracks? It’s none of your beeswax."
    "Jack’s far too lax. He’s a failure, a quack. With a backpack full of Prozac and cognac that does naught but brush back the track I’ve been circling since this paragraph started."
    "I am far too old to be doing this here. I am far too young to feel fear."
    "But what I can do is hold your hands while you paint and try to catch the blues that never make it onto the canvas."
    "{b}{size=+2}THE OCEAN IS FULL OF LIONFISH. THERE’S NO ROOM FOR ANYTHING ELSE.{/b}{/size}"

    play sound "static.mp3"
    scene yumicandy12 with flash
    stop sound

    dem1 "STICKBUG, STICKBUG, BURIED IN THE GRASS. FUCK IT IN THE PUSSY. FUCK IT IN THE ASS."
    dem2 "NO AMOUNT OF RHYMING WILL DISGUISE THE PAIN YOU FEEL AND YOU LACK THE TALENT TO ADEQUATELY DEPICT HOW YOU ARE FEELING WITHOUT A THESAURUS PRESENT."
    dem2 "WE HAVE AN ANNOUNCEMENT FOR YOU. VERY FRESH. VERY NEW."
    dem2 "BUT ALSO SAD BECAUSE YOU’RE BEING LEFT OUT AGAIN."
    dem1 "THAT’S OKAY, THOUGH. ONCE MORE, YOU’LL SEE SNOW. ONCE MORE YOU WILL KNOW. BUT BY THE TIME YOU LET GO, YOUR PAIN WILL HAVE SLOWED."
    dem2 "BUT YOU WON’T DIE ALONE. YOU JUST NEED TO MAKE IT TO THE END OF THE GAME AND HOPE THE CORRECT WORDS ARE TYPED INTO THE WORDBOX."

    play sound "static.mp3"
    scene yumicandy13 with flash
    stop sound
    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)
    vpa "Good morning, Yumi Yamaguchi. The time is currently 8:47 AM. Today’s weather forecast calls for highs of 78 degrees Fahrenheit and lows of 65."
    vpa "Please be advised that your attendance is not required for the Transpacific Sadness Symposium beginning in 13 minutes as you have been identified as “tainted.”"
    vpa "This is no cause for concern, though. Your guide will be here momentarily to provide you our  patented cure. In the meantime, please help yourself to an unlimited supply of fresh fish."
    vpa "And remember — there is no {i}you{/i} in Yumi. But there is Yumi in you."

    play sound "static.mp3"
    scene yumicandy12 with flash
    stop sound

    dem1 "IT’S JUST LIKE WE SAID. BAD NEWS BEFORE BED. NOW YOUR THOUGHTS WILL BE PURE ‘TIL YOUR MOTHER IS DEAD."
    dem2 "CONDOLENCES, BY THE WAY. THAT SHIT REALLY SUCKS."
    dem1 "IT’S A SHAME THAT SHE’LL CROAK BEFORE THAT GUY YOU LIKE FUCKS"
    dem2 "HER."

    play sound "static.mp3"
    scene yumicandy14 with flash
    stop sound

    y "..............................................."
    dem1 "SO SCARED AND ALONE. IS THIS DREAM REALLY DREAMT? ARE THE TWO OF {i}US{/i} SUBJECT TO THE THOUGHTS THAT THIS TEMPTS?"
    dem2 "IT’S BECAUSE SHE IS TAINTED. HER SWEET TOOTH IS CHIPPED. ALL SHE NEEDS IS SOME CANDY TO GET BACK ON SCRIPT."
    dem1 "GOOD RHYME. HAVE A FISH FOR YOUR WISH DISH."
    dem2 "NICE. I CAN’T WAIT TO SQUISH THIS."
    y "What the fuck what the fuck what the fuck what the fuck what the fuck what the fuck what the fuck what the fuck what the fuck what the fuck what the fuck ???????"
    q "Yu.........mi.........."

    scene yumicandy15
    with dissolve

    y "What the fuck what the fuck what the fuck what the-"

    play sound "static.mp3"
    scene yumicandy16 with flash
    stop sound

    q "Yu................mi..............."
    y "........Mom?"
    q "Cure..............you..............."
    y "Cure me of...of what? {i}You’re{/i} the one who needs to be cured! {i}You’re{/i} the one who-"
    q "Help...........you..........."
    q "Feel...............alive..............."

    scene yumicandy17
    with dissolve2

    y "I already feel alive! {i}Too{/i} alive! If anything, I want to feel {i}less!{/i} I’m tired of feeling at all! It’s all just fucking anger and sadness and betrayal and-"
    q "Good..........girl..........."
    q "Let it..................out..................."
    q "Be...........cured..............."

    scene yumicandy18
    with dissolve2

    y "{i}Hah...{/i}"
    y "You’re not actually her...are you?"
    q "................."
    y "Can you tell me {i}what{/i} you are then?...What {i}this{/i} is? Because if this is another fucking Pareidolia thing-"
    q "Me...........mother..........."
    q "Me..............guide............"

    scene yumicandy19
    with dissolve2

    q "Come.................."
    q "Take it................."
    y "Take...what?"

    play sound "static.mp3"
    scene yumicandy20 with flash
    stop sound

    q "Cure.............you.........."
    y "Is that...candy?..."
    q "More...........than candy..........."
    q "This.................helps.................."
    y "Then why don’t you eat it yourself?...Why are you only worried about curing me?..."
    q "I..........do..............."
    q "Every............day..............."
    q "Once you start................never stop.................."
    q "Keeps you................grounded.................."
    q "Feel................better................."
    y "Mom, I..."
    y "I just..."
    y "{i}I don’t want you to die.{/i}"
    q "With this.............live forever.............."
    q "Help.........me..............."
    q "Help.............you............."
    y "So if {i}I{/i} take that...{i}you{/i} live forever? Is that...is this another fucking...time thing?! Is this something that’s supposed to happen?! Is {i}this{/i} what Sensei’s seeing every time he-"
    q "This..................special..................."
    q "Just...............for you..............."
    q "We..............made it.................."
    q "Teach you..............control.............."
    q "Teach you.............strength..................."
    q "Give you.............what you need............."
    q "But first..............take................eat.............."
    q "This............my body..............."
    q "This............your cure.................."

    play sound "static.mp3"
    scene yumicandy21 with flash
    scene yumicandy20 with flash
    scene yumicandy21 with flash
    scene yumicandy20 with flash
    scene yumicandy21 with flash
    scene yumicandy20 with flash
    scene yumicandy21 with flash
    scene yumicandy20 with flash
    scene yumicandy21 with flash
    scene yumicandy20 with flash
    scene yumicandy22 with flash
    stop sound

    y "Wha-"
    q "I’m so proud of you, Yumi."

    scene yumicandy23
    with dissolve2

    y "Sensei?..."
    y "You’re here too now?..."

    play sound "static.mp3"
    scene yumicandy24 with flash
    stop sound

    q "What are you talking about? I’ve always been here. I’ve always been watching. Which is why I’m so proud of you."
    q "All that you’ve accomplished...all that you’ve worked for...you’ve come so far."
    q "And all it took was for your illness to be cured. To think it was something so simple that had been holding you back."
    y "But I’ve...I haven’t..."
    y "I haven’t done anything! Anything at all! I’ve barely changed since-"

    play sound "static.mp3"
    scene yumicandy25 with flash
    stop sound

    q "Just think...how much would you be capable of if you took even more?"
    q "I wish that could be me — so unbothered by the world around me that it’s barely even a factor."
    q "I admire you. No..."
    q "I {i}love{/i} you, Yumi."
    q "Please — accept these. These are my body. Take it and eat. Take it and become a better you."

    play sound "static.mp3"
    scene yumicandy26 with flash
    stop sound

    y "Am I not good enough the way I am now?...{i}Outside{/i} of this...surreal fantasy you’ve all pulled me into?"
    q "Of course not. No one is."
    q "Which is why we must rely on other things. Which is why we hide ourselves in what we do or {i}who{/i} we do."
    q "But can you imagine a world where you and I could be that for {i}each other?{/i}"
    y "No...I can’t..."
    q "Then take me and eat me. {i}Make{/i} it possible."
    q "Everything you could ever need is right there in your hands."

    play sound "static.mp3"
    scene yumicandy27 with flash
    scene yumicandy26 with flash
    scene yumicandy27 with flash
    scene yumicandy26 with flash
    scene yumicandy27 with flash
    scene yumicandy26 with flash
    scene yumicandy27 with flash
    scene yumicandy26 with flash
    scene yumicandy27 with flash
    scene yumicandy26 with flash
    scene yumicandy28 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene yumicandy29 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    leff "Happy birthday, Yumi. We’ve been waiting for you."
    rigf "Come. Fill your hands with the candy we’ve so gleefully gathered and dumped into these festive bowls for you."
    leff "I picked them out myself."
    y "..."
    rigf "What’s the matter? Haven’t you ever seen two talking faces on a chalkboard in the dark before?"
    y "As a matter of fact, I can’t say I have."
    leff "Don’t mind Right Face — he’s always been a bit of a joker. Regardless, won’t you celebrate with us?"
    rigf "We’ve waited so very long for you, after all."
    leff "Even when the others told us not to."
    rigf "Shh. She doesn’t need to know about that."
    y "You two know my birthday isn’t until Halloween, right?...It’s the middle of June right now."
    leff "It’s always Halloween in here."
    rigf "Which means that every day, you’ll grow some more. Numerically and mentally. Mostly numerically. That number would grow quite large rather quickly, wouldn’t it?"
    y "But where {i}is{/i} here?...What is this place? And where did my mom go? Where did {i}Sensei{/i} go?!"
    leff "Dead, presumably. They’d have existed thousands of years ago at this point."
    y "The fuck do you mean “thousands of years ago?!” How am I still here then?!"
    rigf "Time doesn’t move here. At least not in the traditional sense."
    leff "We came up with our own calendar because time is a man-made construct, then rearranged it to have every day as October 31st — the human Halloween."
    rigf "We’ve also extended days to what would be considered about thirty hours each where you’re from so that everyone can get eight hours of sleep."
    leff "But no one ages. And everything outside of here is exactly the same as it has always been."
    rigf "Probably. We’re two faces on a chalkboard, so all we know is what we’ve heard from others."
    y "There are...others?..."
    leff "Your entire family is here. Those who came after, at least."
    rigf "Hundreds and hundreds of descendants — each with your eyes. And they all have a piece of you in them."
    leff "Mostly due to inbreeding. But we’d be lying if we said the vast majority didn’t also have some sort of genetic makeup causing them to act like delinquents more often than not."
    y "So you two are...like..."
    rigf "Gods, I suppose you’d call us."
    leff "Very specific and very weak ones. But gods nonetheless."
    mig "I am Migi, the God of Chalk."
    hid "And I am Hidari, the God of Black-Haired Tsundere Girls."
    mig "You can be a god too, you know."
    hid "You practically already {i}are.{/i} The others here view you as such anyway. You just need to ascend."
    mig "And fill out the appropriate paperwork."
    hid "Migi can help with that. He {i}is{/i} the God of Chalk after all."
    mig "So what do you say, Yumi? Will you stay?"
    hid "Will you celebrate your birthday with us?"
    y "..."
    hid "..."
    mig "..."
    hid "We’ll wait as long as it takes."
    mig "Go on — help yourself to some candy in the meantime."
    y "Yeah, uh..."
    y "Thanks, but I’m...not really into the whole “god” thing."
    mig "..."
    hid "Not even me? But I’m so specifically tailored to you. What else would you rather believe?"
    y "I don’t know. Nothing, I guess?"
    mig "But if you don’t believe in anything-"

    stop music
    scene black

    "{b}{size=+10}THERE IS NOTHING HERE AT ALL{/b}{/size}"

    play sound "static.mp3"
    scene yumicandy30 with flash
    stop sound

    y "..."

    "..."

    y "..."

    "okay fine, i’ll go first. what the fuck just happened?"

    y "Are you telling me you {i}don’t{i} know?"

    "uhhh, yeah? it takes a lot to completely cut off my consciousness. i was worried for a second there that you just randomly stopped believing in me."

    y "I {i}don’t{/i} believe in you, though."

    "you sure do, yumi."
    "for now, at least."
    "so tell me — what did you see? what sort of stuff are you hiding from your old pal here?"

    y "Nothing..."
    y "I didn’t see anything."

    scene yumicandy31
    with dissolve

    y "I’m just...gonna open the door and-"

    play sound "doorlocked.mp3"

    y "...what?"
    y "Wait, didn’t I unlock it? Just a minute ago, I unlocked it...right? Right?"

    "how the fuck would i know? i don’t have hands. and trust me — you’d know if i did. those double d’s down there are practically begging to be fondled."

    $ renpy.end_replay()
    $ yumispring7 = True

    jump yukispring3

label yumispring8:
    scene yumigetshermoneymaybe1
    with dissolve2
    play music "tsukiokamanor.mp3"

    "It takes a lot to humble a person. Sometimes, even a death. "
    "Which isn’t to say Yumi’s mother had already died. There’s no need to fret about that just yet."
    "But it was this brush with death and the first taste of its breath as it leans in for a kiss that had started to change her in a way."
    "It wasn’t a big way. She still thought she was better than everyone. She still wanted to be left alone."
    "But every once in a while, there would be a less self-destructive thought. Normally about a thing she hopes to do or see or just {i}experience{/i} before {i}her{/i} time here comes to an end."
    "This complicated things though, because she didn’t know if her life {i}could{/i} come to an end anymore."
    "So sometimes, after the last bell rang, she’d wander the halls of the school in circles, trying to circumnavigate her head in addition to the third floor."
    "Sometimes, it’d led her right back home. Sometimes, to work."
    "But on this particular day, it led her somewhere else. "

    to "Oh, Yumi. There you are."

    scene black
    with dissolve2
    scene yumigetshermoneymaybe2
    with dissolve2

    "Today, she’d be led to {i}another{/i} princess — one far closer to the title than Yumi ever felt because she’d seen several men have their fingers lopped off by now. And Touka probably hadn’t."

    to "You left last period before I had a chance to get your attention. What are your plans now that school has ended?"
    y "..."
    to "Yumi?"
    y "Why are you talkin’ to me? We don’t talk. This is weird. "
    to "I apologize if my presence is somewhat of an annoyance to you. I was just operating under the assumption that you’d want money as being poor seems to be quite detrimental to your attitude."
    y "Ya know, I’ve shaken down my fair share of girls for lunch money before, but this has gotta be the first time one has just come over without me even lifting a finger."
    to "Please don’t hit me. I am merely a messenger today."
    y "And now shit’s somehow even weirder. Listen, I know I’m {i}technically{/i} Yakuza and shit, but I don’t go around doing collections. So if you’re trying to pass over somebody’s protection money-"

    scene yumigetshermoneymaybe3
    with dissolve

    to "I assure you this has nothing to do with {i}protection{/i} money. Unless Tsukasa has decided to take your business idea in a new and rather odd direction."
    y "Tsukasa? Business? You mean-"

    scene yumigetshermoneymaybe4
    with dissolve

    to "You’re still owed $10,000, are you not? I’ve been asked to finalize the transaction today. Which would require you to accompany me to the manor for a brief-"
    y "Yeah, whatever the fuck you want, I’ll do it. Throw me in a god damn dumpster for all I care. $10k is $10k. I ain’t gonna argue."
    to "Is $10,000 really such an extravagant amount to you that you’d throw yourself in the trash for it?"
    y "Yes."

    scene yumigetshermoneymaybe5
    with dissolve

    to "Oh. Is your family just...not very {i}good{/i} at being Yakuza then? Because that really does not seem like much to me."
    y "I don’t fuckin’ take my dad’s filthy money. Most of the time at least. So just point me in the direction of your god damn manor, cause I figured I was just never gettin’ this payout at all."
    to "There’s a limo waiting outside that’ll take us there together. But if that makes you uncomfortable-"

    scene yumigetshermoneymaybe6
    with dissolve
    play sound "footsteps.mp3"

    y "Nope. Where the fuck’s this limo? Courtyard? On my way."
    to "Wow...all this obedience for pocket change?"
    to "I wonder if this is how kidnapping works?"

    scene black
    with dissolve2

    "........"
    "......"
    "..."

    scene yumigetshermoneymaybe7
    with dissolve2

    y "Do you really come to school in this fuckin’ thing every day? Why don’t you just walk? Too {i}good{/i} for that or something?"
    to "My mother doesn’t want me walking to school. She says I’d attract too large of a ransom if someone were to swipe me off the sidewalk."
    y "Weird. Figured there wasn’t any number “too large” for your family. "
    to "There isn’t, which is how I know she’s lying for the sake of my safety."

    scene yumigetshermoneymaybe8
    with dissolve

    to "I do still walk to school {i}sometimes,{/i} though. And I haven’t been stolen {i}yet.{/i} So I must be doing something right."

    scene yumigetshermoneymaybe9
    with dissolve

    y "Pfft. Probably because we ain’t got a rapist as a teacher anymore. Guarantee you you’d be singin’ a different tune if Sensei was still around."
    to "You say that as if he doesn’t know where I live. "
    y "Probably just forgot. You know how that guy is. "
    y "If it ain’t him, it’d be somebody else though. Your mom’s probably right to keep you away from doin’ shit that could put you in danger. Mine would throw me to the god damn wolves for a six-pack."
    to "Something tells me you’d have no trouble defending yourself from a few {i}wolves{/i} if it really came down to that, Yumi."
    y "Yeah, and something tells me you’ve got snipers on every building in Kumon-mi ready to blast out the brains of any dude who so much as talks to you."
    to "Oh, heavens no. "

    scene yumigetshermoneymaybe10
    with dissolve

    to "There are several blind spots the snipers can’t reach. I just need to make sure I avoid them."
    y "Nice. Real comforting knowing I’m one sneeze away from getting shot."
    to "Just don’t sneeze and everything will be fine then."
    to "Besides, I’m in just as much danger as you are right now. Mother makes it sound as if your family is a much bigger deal than you make them out to be."

    scene yumigetshermoneymaybe11
    with dissolve

    y "They probably are. Means nothing to me, though. I don’t want to get wrapped up in any of that bullshit."
    to "Understandable. But it doesn’t change the fact that anyone who’d harm even a single hair on your head would wind up with a target on their back."
    y "Not {i}anyone.{/i} Just the ones who haven’t fucked my dad."

    scene yumigetshermoneymaybe12
    with dissolve

    to "Well, unless your father has secretly been Sensei this whole time, I can’t imagine that cancels out {i}that{/i} many people. "
    y "Ew. Don’t even joke about that. You’ve seen his fuckin’ niece-daughter thing. I wouldn’t wish that dude’s fatherhood on anybody."
    to "Hmm..."
    to "Perhaps he just needs a mother’s help then?"

    scene black
    with dissolve2

    y "What he needs is a fuckin’ vasectomy. Maybe a lobotomy too. Think there’s some kinda procedure where you can knock out both of those things at once?"
    to "Heh...I’m not sure. But I’ll keep an eye out..."

    "........."
    "......"
    "..."

    scene yumigetshermoneymaybe13
    with dissolve2

    y "God damn....has your place {i}always{/i} been this big?"
    to "You’ve been here before, haven’t you? Dorm Wars. Christmas. "
    y "Never through the main entrance. And I definitely ain’t ever seen whatever {i}that{/i} fuckin’ part of the house is."

    scene yumigetshermoneymaybe14
    with dissolve

    to "Ahh, yes. You must be looking at the pleasure wing."

    scene yumigetshermoneymaybe15
    with dissolve

    y "The what now?"
    to "This manor’s been around for quite a while, Yumi. And it wasn’t uncommon centuries ago for courtesans to be housed within the grounds for...easier access."
    to "What you’re looking at is the remnants of that. And exactly where we’re going today."

    scene yumigetshermoneymaybe16
    with dissolve

    y "On second thought, I would like to leave."
    to "Hahah! Oh, don’t worry. It’s mostly just miscellaneous rooms in there now. We don’t have {i}courtesans{/i} anymore."

    scene yumigetshermoneymaybe17
    with dissolve

    to "There {i}is{/i} a private massage room, though. But I wouldn’t recommend going there unless you want to come out with a little less dignity than you had going in."
    y "Uhh...yeah. I’m good. Thanks. Wh...Why are we going there, though? Ain’t you just gonna give me my money and tell me to fuck off or something?"
    to "After a brief meeting, I presume. I told you — I’m merely a messenger today. It’s my mother who summoned you here. {i}She’s{/i} the one you’ll want to direct your questions to."
    y "Your mom? You mean that rich lady from the Shark Tank thing? I’ve got to talk to {i}her?{/i} Why do we need to get adults involved at all? Just give me the cash and tell me to beat it."
    to "I apologize, Yumi. But I’m afraid I can’t do that."

    scene black
    with dissolve2

    to "Now, follow me. I’ll guide you to the secondary meeting room."
    to "But once we arrive, you’re on your own..."

    "........"
    "......"
    "..."

    scene yumigetshermoneymaybe18
    with dissolve2
    stop music fadeout 10.0

    "It takes a lot to humble a person. But sometimes, just stained glass windows and fancy clocks will do the trick."
    "Combine that with a silence that feels somehow {i}bigger{/i} than any silence she’d ever felt before and you’ll wind up with a situation where Yumi Yamaguchi can’t {i}help{/i} but feel humbled."
    "This was nothing like the manor {i}she{/i} knew. It was emptier. Quieter. Bigger and brighter and less openly intimidating."
    "But that somehow made it feel {i}more{/i} intimidating. And the lack of people only emphasized the silence that bothered her."
    "There was a voice in her head that would always keep her occupied when her mind started drifting nowadays, but it appeared that voice was fearful too."
    "So right now, it was {i}only{/i} her. Waiting. For someone. {i}Anyone{/i} to come and give her salvation in the form of noise or company or {i}anything{/i} that would make this room feel smaller."

    play sound "footsteps.mp3"
    scene yumigetshermoneymaybe19
    with dissolve2

    "It was then that her prayers were answered. Footsteps. {i}Familiar{/i} footsteps. "
    "But who they stemmed from seemed anything {i}but{/i} familiar."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yumigetshermoneymaybe20
    with dissolve2

    yu "{i}Hah...{/i}"
    y "..."

    scene yumigetshermoneymaybe21
    with dissolve2

    yu "..."
    y "..."
    yu "Hey...Yumi."

    scene black
    with dissolve2
    scene yumigetshermoneymaybe22
    with dissolve2

    y "..."
    yu "..."
    y "Who the fuck are you and why do you know my name?"

    play sound "static.mp3"
    scene yumigetshermoneymaybe23 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    yu "Because I {i}chose{/i} it, you piece of shit. I’m your fucking mother."

    play sound "static.mp3"
    scene yumigetshermoneymaybe24 with flash
    stop sound

    y "Wha-"
    yu "Now, I know you probably have a lot of questions-"

    scene yumigetshermoneymaybe25
    with dissolve

    y "Oh, what gave you {i}that{/i} idea?!"
    yu "Yumi, I will explain everything. I just need you to try and listen for once in your god damn life. "
    y "The fuck do you know about {i}my{/i} life, Yuki?! Apart from just how to keep fucking it up, I mean!"
    yu "Do you want to yell at me for a little while longer, or can I talk now?"

    scene yumigetshermoneymaybe26
    with dissolve2

    y "..."
    yu "..."
    y "Make it quick...I’ve got a meeting."
    yu "Yumi, this {i}is{/i} the meeting. You were set up. But I’ll talk to Tsubasa about getting you your money later since I know that fuckin’ brat of hers never delivered on her promise."

    play sound "thump.mp3"
    scene yumigetshermoneymaybe27 with hpunch

    y "{b}OH, FUCK THE MONEY! I WENT THIS LONG WITHOUT IT, DIDN’T I?! AIN’T LIKE IT’S GONNA FUCKIN’ CHANGE ANYTHING!{/b}"
    yu "Okay...{i}fuck{/i} the money then. Let’s talk about the elephant in the room. I have cancer. And I am sorry you had to find out from a fucking {i}bill{/i} instead of me."

    scene yumigetshermoneymaybe28
    with dissolve2

    y "Why didn’t you say anything?..."
    yu "Because I’m a fucking shit mom, obviously. "
    y "You were just going to hide it then? Let me...what, watch you slowly decompose and just assume that everything is {i}fine?{/i} Do you think I’m a fucking idiot?!"
    yu "I wasn’t going to {i}hide{/i} it. And yeah, you might be an idiot, but you’re not {i}that{/i} much of an idiot. I’d have told you eventually. I just...didn’t know when eventually {i}was.{/i}"

    scene yumigetshermoneymaybe29
    with dissolve

    yu "I didn’t...want it to be real. And there were still tests that needed to be done and...I just...hadn’t accepted it yet. "
    y "So...you don’t know for sure yet? There are still tests? Then it’s...there’s a chance you {i}don’t{/i} have it?"

    scene yumigetshermoneymaybe30
    with dissolve2

    yu "..."
    y "There’s a chance...right?"
    yu "I {i}do{/i} have it, Yumi. Tsubasa took me to her personal doctor for some more testing and they...confirmed that I {i}do{/i} have lung cancer. "
    yu "But it is {i}not{/i} a death sentence. And I...will {i}probably{/i} be okay."
    y "..."
    yu "..."
    y "{i}Probably?{/i}"

    scene yumigetshermoneymaybe31
    with dissolve

    yu "I need surgery and...there are...always risks to that, if I’m understanding correctly. And cancer’s kinda notorious for just...coming back, so..."
    yu "Even {i}if{/i} everything goes well, there’s a chance shit might get worse all over again."
    yu "And I ain’t sure how much time I’ve got left here in the long run, but...I think this is just a thing I’m gonna have to fuckin’ deal with forever now."
    y "You fucking idiot..."

    scene yumigetshermoneymaybe32
    with dissolve

    yu "It gets worse..."
    y "Than {i}cancer?!{/i} How?!"
    yu "Well...I did what I always do when shit ain’t goin’ my way. Started using again. So now I’ve gotta quit drugs {i}and{/i} fight back against a disease that’s trying to consume my insides. "
    y "........."
    yu "Go on. Let’s hear it. What shitty name are you gonna call me this time?"

    scene yumigetshermoneymaybe33
    with dissolve2

    y "..........."
    yu "..."

    scene yumigetshermoneymaybe34
    with dissolve2

    y "........."
    yu "Yumi?..."
    y "I can’t believe you didn’t tell me..."
    y "So...what? You just fucking...did all that on your own? Would I have really just made things {i}worse?{/i}"

    scene yumigetshermoneymaybe35
    with dissolve

    yu "What? No! That’s not it at all. I’ve just...you know me. I’ve always done shit {i}alone.{/i} And this was the first time I’ve ever had to do {i}this{/i}, so I just...blanked."
    yu "How the fuck was I supposed to know you were gonna open my mail? I thought I’d have more time to figure out how to tell you."

    scene yumigetshermoneymaybe36
    with dissolve2

    yu "Then once you {i}did{/i} find out...I thought it’d be easier on you to just fuckin’...fade away. That’s why I changed the locks...stopped reaching out..."
    yu "Thought you’d be fine with me just being randomly gone again since I’ve already put you through that before."
    yu "But that {i}too{/i} was just..."
    yu "It’s all just me being scared..."

    scene yumigetshermoneymaybe37
    with dissolve2

    yu "Nobody teaches you how you’re supposed to handle this shit..."
    yu "Just literally...{i}everything{/i} went wrong at once. And I’ve always been able to handle everything that comes my way, but..."
    yu "It was just fucking {i}everything,{/i} Yumi. {i}I’m sorry.{/i} I {i}really{/i} am. I’m not cut out to be a mom. We both know this."
    y "So...what now?"
    yu "Start...prepping for getting my lungs cut up, I guess?"
    y "No, like..."
    y "Are you going to keep ignoring me?"

    scene yumigetshermoneymaybe38
    with dissolve

    yu "Well, you don’t...{i}want{/i} me...do you? Because you never have. And I’ve never {i}blamed{/i} you for that. Which means you definitely wouldn’t want me now that I’m...{i}this.{/i}"
    y "..."
    yu "Right?..."
    y "What do {i}you{/i} want? "
    y "You’re the one who’s fuckin’ dying. You should get to choose."
    yu "I just want whatever makes you happy..."
    yu "And also for you to stop saying I’m dying since I’m trying to have some hope for once."
    y "That..."
    y "That $10,000 that Tsukasa owes me...I can put it toward your-"

    scene yumigetshermoneymaybe39
    with dissolve

    yu "No. That is {i}your{/i} money. Not mine."
    y "Can I not choose what to do with my own money?! I want to help! And if money helps, I’ll-"
    yu "Money’s not an issue, okay? Tsubasa is taking care of it. If you really want to help, just...don’t hate me, please. That’s literally all I ask, Yumi. "

    scene yumigetshermoneymaybe40
    with dissolve

    yu "I’ve never {i}wanted{/i} to hurt you. I just...{i}have.{/i}"
    y "I don’t hate you anymore...I used to, maybe. But now, I..."
    y "I’m scared too..."

    scene yumigetshermoneymaybe41
    with dissolve

    y "Wh...Why the fuck’s that rich lady helpin’ you, though? How the hell do {i}you{/i} two know each other?"

    scene yumigetshermoneymaybe42
    with dissolve

    yu "God, now {i}that’s{/i} a fuckin’ story. Two of us go back to before you were even born."
    y "That long ago? Why didn’t you ever say anything? You knew her daughter was in my class, didn’t you?"

    scene yumigetshermoneymaybe43
    with dissolve

    yu "Just one of those things you look back on and sorta...want to keep in the past, you know?"
    y "Not really, no."
    yu "Yeah, well...you’re still young. Maybe you’ll have somethin’ like that one day too."
    yu "Point is, she cares about me for reasons I ain’t ever gonna fully understand. And I {i}really{/i} didn’t want to drag her back into my shit, but..."
    yu "I ain’t gonna stop her from draggin’ {i}herself{/i} in. ‘Specially now that I kinda need all the help I can get."
    y "She’s not going to make you work in a sketchy massage room to pay her back, is she?"

    scene yumigetshermoneymaybe44
    with dissolve

    yu "Ugh, worse. She made me do {i}this.{/i} My hair hasn’t been black since I was a fuckin’ kid."
    y "So she’s...paying for your cancer treatment and...all she asked you to do was take the bleach out of your hair?"

    scene yumigetshermoneymaybe45
    with dissolve

    yu "That’s Tsubasa for you. Tried gettin’ me to do the same shit decades ago. Girl was probably just {i}waiting{/i} for me to get cancer so she could swoop in and give me a makeover."

    play sound "static.mp3"
    scene yumigetshermoneymaybe46 with flash
    stop sound

    yu "Road to recovery’s just startin’, though....and there’s a long fuckin’ way to go. "
    yu "So hey — maybe she makes me dye it pink next? Or even worse — what if she makes me wear a {i}dress?{/i}"
    y "I’m glad you’re not dying, Yuki...but I’d be a little {i}more{/i} glad if you wouldn’t hold my neck like that."
    y "And also maybe {i}tell{/i} me the next time you come down with a disease or start doing drugs again."
    yu "Indulge me, will you? We ain’t had many opportunities to hug. And I ain’t gonna force that on you, so the least you can do is just stand there while I do {i}this.{/i}"
    y "...Fine. But I’m still not happy about it."
    yu "You ain’t cryin’ anymore, though."

    scene yumigetshermoneymaybe47
    with dissolve

    y "M-Me?! I didn’t cry! {i}You{/i} cried!"
    yu "Me? Hell no! I ain’t cried a day in my life! You on drugs too now?!"

    scene black
    with dissolve2

    y "Ugh! I changed my mind! Let go of me. I need to go hunt down a little kid for $10,000."
    yu "Do you have the app? I can show you where her room is."
    y "No, I don’t- oh. Wait, yeah. I still have it from the last time I was here. Where is it exactly?"
    yu "It’s...{i}that{/i} one. West wing. First floor. Go easy on her. It’s bad form if my daughter kills my friend’s daughter. "
    y "I’ll see what I can do..."

    play sound "static.mp3"
    scene yumigetshermoneymaybe48 with flash
    stop sound

    tb "Oh, Yuki! You’re back. How did it go?"
    yu "It went...well, I think. It was...tough breaking the news to her, but-"
    tb "No, not that. Your hair. What did she think about your {i}hair?{/i}"

    scene yumigetshermoneymaybe49
    with dissolve

    yu "Oh. Fine, I guess?"
    tb "Fine?"

    scene yumigetshermoneymaybe50
    with dissolve

    tb "But you look so much cuter with your natural color. It’s almost like we’re real sisters now."
    yu "All these years later and you still haven’t changed, Nee-sama."

    scene yumigetshermoneymaybe51
    with dissolve

    tb "All these years later and you’re still calling me that. Why? It wasn’t necessary then and it isn’t necessary now."
    yu "Same deal with you looking after me and here we are. "
    yu "I call you by your real name behind the scenes if that helps, though. "
    tb "Say it now. I’m not sure I’ve ever heard it in your voice before."
    yu "Nee-sama."

    scene yumigetshermoneymaybe52
    with dissolve

    tb "Hmph. Maybe I’ll just let you die if that’s how things are going to be?"
    yu "You probably should. But can I least bleach my hair again so I can die with dignity?"
    tb "No. You may not."

    scene black
    with dissolve2

    tb "Now, come. I’ve taken the evening off and you will be going swimming with me. "
    yu "Other people have gotten their teeth kicked in for giving me commands like that, you know. "
    tb "Ooooh? Are you saying you’re going to {i}attack{/i} me? With so many of my guards around? {i}Yuki.{/i} You really {i}are{/i} a bad girl, aren’t you?"
    yu "And you’re just as {i}prissy{/i} as ever, Nee-sama."
    tb "We make a good couple."

    stop music

    tb "Now, if only our {i}third{/i} was here as well..."

    $ renpy.end_replay()
    $ yumispring8 = True

    play sound "winner.mp3"

    "{i}Yumi has obtained $10,000!{/i}"

    play sound "winner.mp3"

    "{i}Tsubasa has obtained a pet!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
