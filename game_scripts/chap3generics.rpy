label yumisummer2streetsgen:
    scene yumisummer2streetsgen
    with fade
    play music "yumiska.mp3"

    "Like clockwork, I wind up bumping into Yumi after just a few minutes of wandering the streets."
    "And while I’d like to say that I think it’s good that she isn’t intentionally trying to avoid me anymore, I can not. For the second she sees me approaching, she gets up to walk away."
    "Somehow or another, though, I wind up convincing her to stick around and the two of us proceed to make scattered pointless conversation that, to anyone else, would make it seem like we dislike each other."
    "That’s wrong, though. And I don’t just mean from one angle."
    "The truth is that even being able to talk to her without her running off is a monumental improvement from the way things used to be."
    "And while I’d prefer not to jinx myself by saying something like, “We might be on the precipice of some sort of breakthrough...”"
    "I think that we might be on the precipice of some sort of breakthrough."

    scene black
    with dissolve

    "Of course, that remains to be seen."
    "With the way Yumi is, she could start hating me again at any moment."
    "And, with the way I am-"
    "I’m sure it would be the result of something I did."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label yumisummer2nightgen:
    scene yumisummer2nightgen
    with fade
    play music "blueair.mp3"

    "Yumi, for reasons beyond my comprehension, answers my call and agrees to meet up with me in the old district for an hour or two."
    "Considering that I’ll be with her for about the same amount of time as my walk to actually {i}get{/i} there, I don’t see it as a solid investment of time, but it’s not like I have anything else going on tonight."
    "Once I arrive, the two of us do laps around the neighborhood surrounding Chika’s house, being careful to not actually {i}pass{/i} Chika’s house, as Yumi remains adamant about remaining hidden."
    "And even though I can’t imagine anything {i}happening{/i} tonight, or that half of us even {i}want{/i} anything to happen, it’s interesting to me just how important this temporary privacy is to her."

    scene black
    with dissolve

    "Of course, I can only imagine how bad it would be for everyone involved if Chika were to find out her best friend was seeing her “boyfriend” behind her back, platonic or not."
    "And of course I know there’s likely a little more behind Yumi’s reasoning than this alone."
    "But I will push that reasoning aside for now, as in this moment, my greatest concern is the same as the one belonging to the girl I came here to see."
    "The one who does not yet rely on me."
    "The one who wants to."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label chikasummer2morninggen:
    scene chikasummer2morninggen
    with fade
    play music "love.mp3"

    "I head over to Chika’s place first thing in the morning to spend some time with her before she needs to go to work."
    "Seeing as Chinami is already awake once I get there, the three of us spend our morning watching cartoons on her old television that, and this might be a first world complaint, {i}dramatically{/i} requires an upgrade."
    "Considering how I’m already paying for both of their phones, though, I doubt I’ll be splurging on any more electronics any time soon."
    "Unless she’s willing to let me live here, that is. Which...honestly, she probably would."
    "But at this point, I don’t think I’ll be able to live anywhere without taking Ami with me."
    "And I can’t imagine Ami would be very happy with observing the things I would do to her classmate."

    scene black
    with dissolve

    "Eventually, the time comes for me to head out and I walk with Chika to her bus stop, feeling eerily like a man walking his daughter somewhere and not at all like a significant other."
    "Well, apart from the unearthly desire to undress her. But, let’s face it, there are plenty of fathers out there thinking that same thing about {i}their{/i} daughters every day."
    "Just not Chika’s on account of the whole...yeah."
    "Anyway, Chika heads out and I make my way back into town to figure out what else I want to do today."

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chikasummer2mallgen:
    scene chikasummer2mallgen
    with fade
    play music "mall.mp3"

    "Chika isn’t on break when I make it to the mall, so I head over to her store (Which I still can not pronounce the name of) and decide to spend the afternoon with her there."
    "It’s busy, but not so much that it takes away any of our time together as even when she’s helping customers, she still seems very focused on what I’m doing."
    "I guess that sort of thing is to be expected given just how big a part of her life I’ve become, though."
    "She also seems to pick on cues pretty well as every time someone sees the two of us together and attacks us with a gaze of skepticism, she starts slinging customer service dialogue at me like it's second nature."

    scene black
    with dissolve

    "And might I add that the customer service here is exceptional since the two of us wind up making out in the dressing room shortly after that."
    "Things don’t progress any further as Chika still seems a little hesitant about going all the way in public after our talk some time ago."
    "Just...not hesitant enough to hold herself back from kissing me, I guess. Which is fair."
    "I could talk my way out of that if someone saw the two of us. "
    "What I {i}don’t{/i} think I could talk my way out of is someone finding me secretly fucking a teenager while she’s on the clock."
    "But hey, maybe if I start thinking up excuses now, I’ll be able to some day."
    "Until then...I’ll just have to keep making out with her, I guess."
    "Woe is me."

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chikasummer2nightgen:
    scene chikasummer2nightgen
    with fade
    play music "justlights.mp3"

    if yumiblock == False:
        "I make my way over to Chika’s apartment to spend the night with her while Yumi and Chinami sit in the living room reading manga together."
        "Neither of them pay any attention to me (Likely because a certain someone asked them not to), so I’m free to spend a wholesome night out on the balcony with my fake girlfriend while she longingly gazes up at the sky."
    else:
        "I make my way over to Chika’s apartment to spend the night with her while Chinami sits in the living room watching TV."
        "She doesn't pay any attention to us, so I'm free to spend a wholesome night out on the balcony with my fake girlfriend while she longingly gazes up at the sky."

    "It feels a little odd spending time together when I know that we’re being secretly spectated at all times, but I guess that sort of family dynamic is exactly what Chika wants in the first place."
    "She’s not the type to mind the ones close to her knowing her feelings. "
    "She’s the exact opposite of me."
    "But as long as she keeps those feelings away from everyone else...I think that’s okay."

    scene black
    with dissolve

    "We don’t need to be the same to want each other. We can just...do it."
    "And if and when things self-destruct, less people will get caught in the blast. "
    "We’ll crawl away with some skin still left on our bones and pick ourselves up as if nothing ever happened."
    "But for now, we’ll remain like this- two bodies on a balcony under a sky full of stars."
    "We head back inside and I leave when they all fall asleep."

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanesummer2morninggen:
    scene ayanesummer2morninggen
    with fade
    play music "acoustic.mp3"

    "I call Ayane in an attempt to invite her out for breakfast, but am immediately met with the insistence that {i}she{/i} come over to cook breakfast for me instead."
    "The gesture is fine and all, but seeing as there is already someone who lives here and cooks breakfast for me pretty much every single morning, the novelty of home cooked meals is beginning to wear thin."
    "Not to mention that I purposely {i}did not{/i} eat the breakfast prepared for me this morning specifically because of that."
    "But hey, if it makes Ayane happy, that’s fine."
    "I’m sure the sudden understanding of how the world is on an infinite loop must be weighing down on her in some way, so she deserves every win she can get right now-"
    "And I will gladly stomach yet another home cooked meal to support that."

    scene black
    with dissolve

    "Or at least that’s how I thought I’d feel before she made me something healthy in an effort to “Save my cholesterol levels from exploding.”"
    "It is at this moment that I understand she is only here to torment me and that her insistence of personally cooking for me is just one part of a very detailed plan to adjust my diet."
    "Of course, she denies this accusation and forces me to eat her food. Which, while certainly {i}good,{/i} is not what I wanted."
    "And I will never forgive her for this."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label ayanesummer2dojogen:
    scene ayanesummer2dojogen
    with fade
    play music "sakuya4.mp3"

    "I wind up deciding to spend yet another afternoon at the dojo- a place that, very surprisingly, I have not yet been banned from due to lack of participation."
    "I’m sure that a large part of that is due to Ayane putting in extra work to make up for me or, at the bare minimum, paying double whatever the membership cost is to ensure that I can return whenever I want."
    "That said, it seems that even Osako is warming up to me around here."
    "I can tell because she no longer interjects when Ayane gets too close to me every five minutes and instead, just accepts it as a part of our relationship."
    "Feeling a sudden burst of energy and the desire to make these two girls who still manage to put up with me mildly happier, I actually begin to make an effort and do some warm-ups."

    scene black
    with dissolve

    "My “warming up” stops there, however, as I never intended to move past that phase- even with Ayane’s incessant encouragement and compulsion to drag me toward the sparring circle."
    "But I am doing this for her. Because even if she {i}does{/i} practice and understand the fundamentals of karate, I am a man twice her size and could destroy her at any given moment."
    "I allow Ayane to continue living as she is an ideal vessel for the release of my sexual energy, and the afternoon ends without much of a change at all."
    "But at least I managed to make it one more day without being kicked out of here."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label ayanesummer2nightgen:
    scene ayanesummer2nightgen
    with fade
    play music "meanttobe.mp3"

    "I call Ayane and wind up heading over to the dorms to hang out with her since Ami is at the house tonight and doesn’t take kindly to the idea of Ayane getting “Sensei time” without her."
    "Instead of making plans to do anything, though, we wind up talking outside of the dorm building for what feels like an eternity, but is really only an hour or two."
    "Among the topics discussed are: how much she loves me, her new role as an official swim club member, how much she loves me, something about getting Sana to eat better-"
    "And, most importantly, how much she loves me."
    "Needless to say, despite talking for what {i}is{/i} but {i}isn’t{/i} an eternity, I’m unable to really contribute much."
    "But I guess all she really asks for in the first place is someone to be there and listen."
    "And, believe it or not, I’m good at that."
    "I just don’t always listen the way people {i}want{/i} me to."

    scene black
    with dissolve

    "We retreat to a nearby park bench and Ayane falls asleep on my shoulder."
    "Waiting for her to wake up does no good, so I’m forced to carry her back upstairs and bring her to bed."
    "I realize halfway to her room that she’s either been faking it the whole time or woke up somewhere along the way, but I don’t say anything about it."
    "Even now, with nothing to listen to, I still find myself struggling when it comes to talking."
    "Thankfully, she says nothing. Even as I lay her down and pull her blanket over her."
    "I leave as if I was never here at all and return home as if I had never left."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sanasummer2bargen:
    scene sanasummer2bargen
    with fade
    play music "calmbar.mp3"

    "I somehow find myself returning to the least popular spot in all of Kumon-mi which, coincidentally, also happens to be the business with the single worst name in all of Kumon-mi."
    "Despite that, though, I am quite fond of the family who runs it and elect to spend the night with the younger of the two of them."
    "Sana’s come a long way in what, at least to {i}her{/i} is a remarkably short amount of time."
    "For me, it’s probably close to around a...year at this point? Maybe a year and half? I’m not really sure. But, as is customary, it makes me question the passage of time and its effect on those it changes."
    "It makes me question just what type of person this girl will become."
    "Whether or not she’ll be anything like her mother."
    "Whether or not it would be good for her if she did."
    "But the thing I find myself questioning the most-"
    "Is exactly what I {i}am{/i} to her."

    scene black
    with dissolve

    "Sana is one of the few girls I find myself questioning rather often at this point."
    "I don’t know how much of it has to do with the things she’s gone through or...the people she surrounds herself with-"
    "But what I do know is that I want it to change."
    "I want to know the way her brain moves."
    "I want to know the way her blood flows."
    "I want to know her."
    "And I will never know that if I can not get her to open up and let me crawl in."

    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label makotosummer2morninggen:
    scene makotosummer2morninggen
    with fade
    play music "love.mp3"

    "I call up Makoto and the two of us make plans to meet up for coffee, which quickly evolves into “Meet up for coffee and walk around the park” as if I didn’t just walk several miles to meet her."
    "Regardless, she pays for my drink with her dirty, porn money so everything works out in the end except for the one small fact that I am still not allowed to actually contribute to her porn money fund."
    "I’m sure that will change sooner or later given that we’re now sexually involved and going on what could only be described as “dates” this early in the morning."
    "But for now, I will keep my head held high and remain as hopeful as a man in my position could possibly be."
    "We do a few laps around the park and wind up passing by Otoha several times, who’s busy playing her guitar in the usual spot."
    "It becomes awkward after the third time we pass her and we all make a silent agreement to ignore each other’s presence for the rest of the morning."

    scene black
    with dissolve

    "Makoto seems embarrassed at first to be seen together, but quickly gets over this by amping herself up and repeatedly mentioning how normal it is for a teacher and his assistant to get coffee together."
    "She gets more embarrassed when I mention how {i}abnormal{/i} it is for those two people to have sex."
    "And then she gets very mad when I suggest that we go do that instead of continuing our walk."
    "I feel like it’s a strange thing to get mad {i}about{/i} as it is in stark contrast to the way I treated sex with her in the early stages of our relationship, but I suppose this is just something we won’t see eye to eye on."
    "Regardless, we do a few more laps (No sex involved) before heading our separate ways and getting on with our respective days."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label makotosummer2poolgen:
    scene makotosummer2poolgen
    with fade
    play music "notabluearchivesong.mp3"

    "I call Makoto to find that she is spending her free time at school today, which seems like an incredibly {i}Makoto{/i} thing to do."
    "But it is {i}then{/i} that I find she’s actually all by herself in the school swimming pool, so I decide to go and meet up with her so I can see her in her swimsuit- which is an incredibly {i}me{/i} thing to do."
    "As you may have guessed, I regret nothing and the trip is worth it from the moment I arrive."
    "As it turns out, Makoto is not only happy to finally be a part of an {i}actual{/i} club and not just the student council, but that it’s done wonders for her overwhelming lack of relaxation as of late."
    "And while I’d be happy to help her out with that whenever she wants, I do think it’s good that she finally has an outlet she can enjoy."
    "Especially since I can vicariously enjoy it {i}through{/i} her by visiting her when she’s here."

    scene black
    with dissolve

    "Eventually, watching Makoto float directly in front of me begins to get a little awkward and I feel as if I should leave so she can actually...you know...{i}swim.{/i}"
    "So, being the generous guy that I am, I let her get back to it and leave the school with the image of her ingrained into my head for use at a later time."
    "And by “a later time” I likely mean tonight."

    s "..."

    "I am suddenly filled with many regrets for leaving in the first place."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label makotosummer2porngen:
    scene makotosummer2porngen
    with fade
    play music "citylife.mp3"

    "I spend my night tormenting Makoto by taking various sex toys out of their boxes and then asking her about how they’re meant to be used."
    "As you may have guessed, she does not appreciate this {i}at all{/i} and claims that I, an adult male, should be more aware of these things than she is."
    "I explain to her that is not something someone in her line of work should be admitting."
    "She does not appreciate that comment as well."
    "In fact, Makoto appreciates essentially nothing I do from the moment I walk in to the moment I think about leaving, but instead grab another sex toy to-"

    mak "Can you please not? Putting these back inside of their boxes isn’t as easy a task as you might think."
    s "Is it because you’re too tempted to use them?"
    mak "Do I look like the type of girl who would use an anal vibrator?"
    s "You-"
    mak "Don’t answer that."
    mak "In fact, just get out. Cleaning up after your “fun” is going to take long enough as is."
    s "You should know full well how long cleaning up after my “fun” takes when-"
    mak "Out. Now."

    scene black
    with dissolve

    "Makoto and I decide it’s best for me to just leave the porn shop since we both need to wake up early in the morning and she still has work to do."
    "And while I’m not happy to be, once again, leaving empty-handed...I am leaving knowing that Makoto is {i}exactly{/i} the type of girl to use an anal vibrator whether she believes it or not."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mikusummer2poolgen:
    scene mikusummer2poolgen
    with fade
    play music "highspeedprinter.mp3"

    "I head over to the school, finally free from my duty as the coach of the soccer team- a position I was forced into by the very girl I am here to see right now."
    "But, and I’m sorry to Miku for thinking this, I kind of prefer things this way."
    "Sure, there are {i}fewer{/i} girls around seeing as the swim club has barely enough members to stay afloat (Pun not intended)-"
    "But there are more girls I {i}know{/i} here, which greatly increases my chances of ultimately getting to sleep with them in their school swimsuit."
    "Regardless of my inability to keep my mind out of the gutter after seeing Miku’s surprisingly toned yet alluringly slender body, I’m happy she was able to fit in here as quickly as she did."
    "I’m sure it was difficult giving up the one thing she really loved doing, but athletes will be athletes no matter what sport they’re thrown into."
    "And as long as it involves intense physical activity and an overabundance of energy, I’m sure Miku will be fine."

    scene black
    with dissolve

    "In thinking that, my mind quickly falls back into the gutter and I wind up staring at Miku for long enough to disturb her."
    "But that’s fine, because instead of asking me to {i}stop{/i} looking at her, she just blushes and looks away, pretending to not notice."
    "It may have taken several cycles of the world to get here, but I’m glad we’ve reached a point where she is well aware of the way I look at her."
    "But I’m even gladder that we’ve reached a point where I can capitalize on that."

    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label mikusummer2nightgen:
    scene mikusummer2nightgen
    with fade
    play music "justbehappy.mp3"

    "I call Miku and the two of us wind up making a trip to a nearby fast food restaurant so she can replenish her energy stores with what is potentially the least healthy thing you can put inside of your body."
    "But hey, if she wants to jeopardize her future self now while she is still young and able-bodied, she’s allowed to do so."
    "And I say this as a young-ish and mostly able-bodied male who is about to put the same things into {i}his{/i} body."
    "Either way, it feels nice and...surprisingly natural to come to places like this with Miku."
    "If she wasn’t half my age, I might even say something along the lines of how she feels a bit like some sort of childhood friend."
    "Which, honestly, doesn’t sound so bad because the only childhood friend I do have yells at me all the time and the only times I’ve heard Miku yell have been extremely depressing and not at all personal."

    scene black
    with dissolve

    "We get our food and settle down at a table near the window and wind up talking about how life has changed lately."
    "For her, it’s mostly about the swim club and how she’s in the process of trying to convince some of the girls from the disbanded soccer team to swap clubs."
    "For me, it’s about the direction our relationship has headed in."
    "Is that the most substantial change my life has made as of late?"
    "Not at all."
    "But it’s the one that makes her blush, so it is the one that I will use."

    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rinsummer2cafegen:
    scene rinsummer2cafegen
    with fade
    play music "cafe.mp3"

    "I head over to the cafe to drink a random combination of syrups and espresso and hang out with a girl who would rather sleep with {i}another{/i} girl than me."
    "Why I have decided to be so unabashedly confrontational about that via inner monologue, I don’t know. Especially since I, too, would rather sleep with a girl than myself."
    "But I digress."
    "The morning proceeds normally and Rin fills me in on all of the latest happenings of her life that I may have missed over the last 24 hours."
    "As you may have guessed, all of them involve either Otoha or music. Or both of those things."
    "And while I’m happy that she’s getting to dive face first into the things she loves as of late, I can’t help but wish there was some piece of me in there."

    if rinbetrayed == True:
        "I understand why there’s not, though."
        "And at this point, I honestly doubt there ever will be."

    else:
        "It doesn’t have to be a big piece. Even a sliver would be fine."
        "I just feel like we’re moving backwards all of a sudden."
        "And the idea of that hits me harder than it should."

    scene black
    with dissolve

    "A flood of customers all decide to caffeinate at the same time and I seize the opportunity to bail out before I get wrapped up in the mess."
    "Rin notices me leaving and stops what she’s doing to say goodbye, causing the customer she’s currently helping to get pissed off-"
    "But allowing {i}me{/i} to leave the building knowing I haven’t been completely forgotten yet."
    "And that the thought of me may just cross her mind while her tongue is in her girlfriend’s mouth."

    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label rinsummer2nightgen:
    scene rinsummer2nightgen
    with fade
    play music "lifeismostlygood.mp3"

    "I call Rin and am immediately roped into a late night trip to the convenience store because 9:00 PM is apparently the most ideal time for sushi."
    "I figure that both Futaba and Otoha are unable to go (Probably because 9:00 PM sushi adventures are frowned upon by most people), but I’m not put off by the fact that I might be slightly more insane than them."
    "In fact, it’s for that exact reason that I actually enjoy spending time with Rin."
    "Sure, she’s light years above me in terms of innate insanity and not the type that just causes a person to black out and force himself on girls in the old district, but we’re {i}both{/i} still a little “out there,” I guess."
    "Plus, this convenience store is {i}not{/i} in the old district, which means the chances of me sexually assaulting Rin are statistically lower."

    scene black
    with dissolve

    "Rin goes to pay for her sushi as well as a varied assortment of energy drinks but, lo and behold, conveniently managed to leave her wallet behind at the dorm."
    "I try to get out of the idea of having to pay for her, but then I remember that I’m paying for her ex-crush’s phone bill and figure that Rin deserves at least {i}some{/i} form of compensation."
    "I guess I also see it as a way of paying her back for all of the free drinks she’s given me. But hey, it’s not like I’ve ever actually {i}ordered{/i} any of those things."
    "Regardless, Rin gets her sushi and I get an empty promise that she’ll pay me back when I know she won’t."
    "After that, I am abandoned and left with slightly less money in my pockets while she returns to the dorm and eats away my hard work."

    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabasummer2librarygen:
    scene futabasummer2librarygen
    with fade
    play music "morningmoon.mp3"

    "I head over to the library to see what Futaba is doing and, hold onto the edge of your seat for this, she’s {i}reading.{/i}"
    "Or {i}was{/i} reading."
    "Her attention immediately switches to me as I’m more interesting than any sort of book she could possibly pick up, and likely packed with significantly more secrets as well."
    "Unfortunately for her (And even less fortunately for me), those secrets are pressed so far into the back of my mind that it would take the world’s most seasoned psychological spelunker to uncover them."
    "Seeing as Futaba is not at all qualified for that job, the two of us make idle chit chat about things that will {i}not{/i} cause my mind to melt into a puddle of Jell-O."

    scene black
    with dissolve

    "I wind up asking her about how her journey as a writer is going, but it seems she hasn’t had much time to write at all as of late."
    "I can’t tell if that’s the truth or just some sort of excuse she’s coming up with to avoid disappointing me, but it’s not as if I’d be majorly disappointed to begin with."
    "The whole reason I pushed her so hard down that path in the beginning was to help give her an outlet to express herself and distract her from the depressing and untrue thoughts that plagued her mind."
    "But she has several different avenues to express herself now, and an even larger roster of people willing to listen."
    "She doesn’t need to write anymore."
    "She doesn’t need me anymore."
    "I leave the library before my mind moves any further away from her."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label futabasummer2noongen:
    scene futabasummer2noongen
    with fade
    play music "kimitoakinobouken.mp3"

    "I call Futaba and the two of us make plans to revisit the bookstore she likes."
    "It seems that things have gotten a lot livelier here since the first time we came."
    "Several more floors have been added on, each with their own distinct theme or specialty."
    "But, seeing as neither of us want to climb any more stairs, we surrender ourselves to the second floor and spend the afternoon there, discussing different writers and remembering how far apart our tastes are."
    "It’s funny...the way that, despite having not read a single book since waking up in the classroom all that time ago, I still remember what I do and do not like."
    "But I guess that we all have parts of ourselves that can’t be destroyed by anything. And that we don’t need to actively attempt to remember our past as it’ll wind up crawling back on its own."
    "Futaba must catch onto my slip into existential territory as she switches herself into shopping mode, grabbing a few things off the shelves before announcing that she’s ready to leave."

    scene black
    with dissolve

    "The trip back home isn’t as quiet as the tail end of our bookshop “date,” with Futaba utilizing the time to discuss the latest happenings in the lives of her two closest friends."
    "When I ask her why she doesn’t talk more about {i}her{/i} life, she takes a look around, as if to shield herself from the embarrassment of anyone but me hearing her, and says-"
    "“This is my life.”"
    "It’s a little corny, but the dying light of the sun reflecting off of her skin makes it seem like the end of a movie."
    "It isn’t, though...as I’m unable to think up a proper response and give her back nothing more than, “I see...”"
    "When, in all actuality, I don’t."
    "Everything has already faded to black."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label amisummer2maidgen:
    scene amisummer2maidgen
    with fade
    play music "maidcafe.mp3"

    "I find myself heading over to the maid cafe before I even know it to spend some time with one of my niece’s many forms."
    "This form, however, might actually be my favorite."
    "Because not only does she treat me with the same amount of love and affection she does everywhere else, {i}but she is dressed as a maid,{/i} which immediately makes every girl at least two points better."
    "That is a factual statement, for maid cafes would not exist if it was not true."
    "Anyway, the morning shift is dead, so the two of us wind up hanging out on the couch as Ami hams up her role as my servant and hangs on my every word."
    "But, being a man of few words, it’s more like she’s hanging on by a thread."
    "What little conversation I’m able to muster comes to a halt when she stops and stares into my eyes for an uncomfortable amount of time."

    scene black
    with dissolve

    "Nothing happens after that. Not even a word. It’s just ten or twenty seconds of her looking at me with a mix of appreciation, admiration, and something much darker."
    "Something that, without any words at all, tells me that I am what keeps her grounded."
    "And that without me, she’d simply fly away."
    "I could just be projecting, though...as some days, I feel that way about her."
    "But of course, I won’t let her know that."
    "Her string is tied tightly enough around my neck as is."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label amisummer2noongen:
    scene amisummer2noongen
    with fade
    play music "amiamiami.mp3"

    "I give Ami a call and, feeling generous today, decide to take her to the mall so she can complain about how I never buy her anything and get too close to me in public."
    "In hindsight, I was probably just bored- as I can not envision any version of myself generous enough to endure such niecely activities."
    "The two of us move from store to store, but it’s more like I’m being {i}dragged{/i} from store to store than anything else."
    "I think all of the maid cafe money must be going to Ami’s head as she winds up picking up at least one item from basically every business we step into."
    "Well, every business beside Chika’s...which she still made a conscious effort to go into, likely to rub the fact that the two of us were hanging out in Chika’s face."

    scene black
    with dissolve

    "Thankfully (And surprisingly), Chika trusts me enough to believe that there’s nothing more to this and locks herself into the preconceived notion that Ami is just...very clingy."
    "Which, to be fair, she is."
    "But her feelings are obviously much greater than that."
    "If they weren’t, she wouldn’t keep insisting to every employee in every store that I need to accompany her into the dressing room- a thing that not a single person has bought so far."
    "It’s gotten to the point where I just walk away whenever she says that now."
    "Eventually, we run out of stores to shop from and dressing rooms to {i}not{/i} enter and have to leave the mall before Ami spends the remainder of her paycheck on pointless accessories."
    "And, even though it’s a little annoying, the two of us grow a little closer in the process."
    "But, it is at that moment that I begin to wonder just how much closer we can possibly get."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label amisummer2nightgen:
    scene amisummer2nightgen
    with fade
    play music "love.mp3"

    "I call Ami to find out that she’s just lounging around at home, so I decide to call it an early night and join her there."
    "I’m {s}forced{/s} asked to stop at the convenience store for what she describes as “a disgusting amount of ice cream” but get confused once I arrive as there is no amount of ice cream that I would find disgusting."
    "As such, I pick up as much as I’m willing to carry and make it back home to a fresh plate of dinner that I devour almost instantaneously."
    "Dinner is succeeded by a trip to Ami’s bedroom where the two of us sit on her couch as she shows me what {i}I{/i} would describe as “a disgusting amount of cat videos.”"
    "This goes on for almost one hour before I toss her phone across the room and drag her back out into the living room so we can watch a movie."
    "Preferably one without cats."

    scene black
    with dissolve

    "I put on the first thing I find on Netflix and try to get myself absorbed in it, but fail spectacularly as whatever I chose in my anti-feline stupor is somehow even worse."
    "Of course, Ami seems to like whatever it is because that is just how my night is going to go, I guess."
    "Thankfully, she doesn’t mind me talking throughout the entire thing and the two of us discuss scattered topics like her work and how she’s starting to hate the heat a little less."
    "I have no idea {i}how{/i} given that this summer has been so hot that even our air conditioner is struggling to keep up with it, but I guess she’s free to like whatever she wants."
    "We fall asleep together on the couch and I wake up about an hour later to find that the TV has already turned off."
    "Not wanting to carry her, I grab a blanket off of Ami’s bed and toss it over her before heading back to my room and allowing myself to fall asleep on something more comfortable."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mayasummer2shrinegen:
    scene mayasummer2shrinegen
    with fade
    play music "shrinesong.mp3"

    "I bear the heat just long enough to ascend the stairs to the shrine and find Maya all alone in the shade from the temple, fixing her ponytail and pretending not to notice me."
    "I think about shooting her some snide remark about how she should be hiding or something along those lines, but decide against it and just take my place beside her in the shade."
    "My silence must get to her as she breaks character and speaks before I’m able to."
    "What she says doesn’t matter, but it’s the fact that she says {i}anything{/i} that makes me realize how far we’ve come despite the absence of changes in our {i}physical{/i} relationship."
    "Of course that’s how it would work with her, though."
    "Even though I’ve come to understand just what sorts of feelings she’s kept locked away all this time, I understand even more just how stubborn she is."
    "And all things considered, I’m the same way."
    "That’s why I’m still able to bear the heat and ascend the stairs."

    scene black
    with dissolve

    "The sun chases away the shade and we wind up having to relocate to prevent ourselves from getting sunburnt."
    "It is at this time, however, that Maya suggests I relocate to somewhere completely different as she is “tired of my presence.”"
    "Not feeling the need or desire to fight back this time, I oblige and immediately turn around to leave."
    "My actions shock her for the second time today as I’m able to hear a slight gasp escape her lips, but she does not chase after me."
    "She’s just too stubborn to do so."

    $ maya_love += 1
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label mollysummer2cafegen:
    scene mollysummer2cafegen
    with fade
    play music "breeze.mp3"

    "I make my way to the cafe to hang out with Molly and immediately regret my decision as she sprays me with cleaning fluid and tells me that I have been purified."
    "Whatever strange sort of purification ritual this is, I doubt it works as my thoughts are just as cynical and self-serving as ever."
    "I am reminded of this when she sprays me {i}a second time{/i} because one purification simply wouldn’t be enough."
    "Thankfully, I am a large and powerful man who is able to snatch the bottle out of her hands and spray her back with it."
    "{i}Not{/i} so thankfully, I spray her directly in the face and have to spend the next five minutes washing her eyes out so she doesn’t go blind."
    "But, if you ask me if I regret anything, I’ll tell you I don’t."
    "In fact, I’d double down and say that she had this coming."
    "But that’s okay-"
    "Because now-"
    "She, too, has been purified."

    scene black
    with dissolve

    "Molly regains her vision, but not her bottle as I have hidden it in a location that someone her size would never be able to reach."
    "Feeling slightly bad about being the [[deserved] cause of her current ocular anguish, I accompany Molly back to the table and sit with her as her purification wears off."
    "I even take it upon myself to clean off a few tables in the process. Just...without the cleaning juice as I don’t want her to find out where I hid it."
    "Eventually, Molly returns to normal and attempts to cast some sort of Gaelic spell on me or something with a magic wand that she had tucked into her back pocket for some reason."
    "I take this as my cue to leave and do so without the effects of the spell ever reaching me."
    "But if I randomly drop dead one day due to unknown causes, you’ll know why."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label tsuneyosummer2archerygen:
    scene tsuneyosummer2archerygen
    with fade
    play music "summerwind.mp3"

    "I head over to the archery range to find Tsuneyo practicing her form without the use of any actual arrows as she is afraid she may accidentally shoot a bird in transit."
    "Why she is worried about this when countless fowls have died at her hand, I do not know. But this is Tsuneyo we’re talking about, so I’m not going to ask any questions."
    "Especially because I feel like she wouldn’t hesitate to shoot {i}me,{/i} transit or not."
    "We talk a little bit about how she’s enjoying this club and how it's her first experience with anything like it since kendo."
    "Apparently, the only contact she had with other girls during her kendo career was during competitions, so this is still a lot different and, to her, much more fun."
    "I question exactly how she became so {i}good{/i} at kendo without practicing against people her age but, as expected, she tells me it was all her father and that he is the one who trained her to be all she is today."

    scene black
    with dissolve

    "Tsuneyo hands me her bow and asks me if I’d like to try taking a shot but, seeing as there are still no arrows to be found, I just...hold it and pull the string back a little bit."
    "It’s a satisfying feeling- one that’s hard to describe or compare to anything else. But what strikes me most is how heavy it feels and how she’s able to do this with no effort at all."
    "I’m sure there’s a lot more to it than just strength alone but, if she’s anywhere as good at this as she was at her last sport, I’m excited to see more out of her one day."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label tsuneyosummer2ramengen:
    scene tsuneyosummer2ramengen
    with fade
    play music "kashiwagi.mp3"

    "I make my way over to one of the few sanctuaries in the seediest part of town to be greeted by the same expressionless, mechanical greeting as always."
    "Tsuneyo stands before me like some sort of omnipresent being who can do anything she wants, but all she {i}wants{/i} is to feed me noodles."
    "That works, though, because I...probably wouldn’t have come here if I wasn’t hungry."
    "And I say that as someone who consistently comes here despite not being hungry, which is...a little strange, now that I think about it."
    "I don’t want to say that I don’t {i}like{/i} talking to Tsuneyo. It’s just...well...you know."
    "There’s never really much {i}to{/i} talk about with her when everything I say goes over her head and everything {i}she{/i} says slips well under mine."
    "But regardless, I find myself here yet again- empty stomach and empty mind. Ready to fill up on ramen and whatever strange form of “wisdom” she is willing to bestow on me this time around."

    scene black
    with dissolve

    "We talk at length about darkness and how it has always made her feel uneasy."
    "She used to keep a night light in every corner of her room to chase away the evil."
    "Those lights are in her father’s room now."
    "She says he needs them more."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iosummer2morninggen:
    scene iosummer2morninggen
    with fade
    play music "lifeismostlygood.mp3"

    "I call Io and the two of us make plans to meet at the dorms and then...immediately leave that location because, as Io puts it, “there is far too much estrogen there.”"
    "And while I admire her ability to feel hormones in the air, I don’t think I admire it enough to understand why we can’t just talk there instead."
    "Either way, I play along and follow her to the nearby strip of small shops and restaurants I’ve visited with Ami and some of the others before."
    "Io takes a seat on the ground in the middle of what is currently an empty lot-slash-indie venue type thing despite there being benches literally all around us and I am forced to sit on the floor as well."
    "She says a bunch of stuff about how happy she is that I would “waste my time on someone like her,” and, like always, I’m not really sure what I’m supposed to do about that."
    "Io feels like the one person I’ve met so far who just...hasn’t really changed at all."
    "And I’m not sure if she’s just too far gone to be reached at this point, but I know that it’ll be dangerous for her and the few people she loves if she keeps it up."

    scene black
    with dissolve

    "Once the town wakes up and more people start passing by, the two of us pick ourselves off the ground and start heading back to the estrogen minefield known as “the dorms.”"
    "Io isn’t happy about this, of course, and talks about how she wishes she could spend the entire day with me instead."
    "For a moment, I think about inviting her to do just that."
    "But as I open my mouth, another self-loathing comment spills out of hers and makes me question my decision."
    "In the end, she heads back inside to be miserable without me and I head off in the opposite direction to be complacent without her."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label iosummer2bathgen:
    scene iosummer2bathgen
    with fade
    play music "io.mp3"

    "I head to the bathhouse to spend some time with Io and, instead, get coerced into taking off all of my clothes."
    "The first part of my mission is still completed, however, as Io (With all of her clothes unfortunately still on) sits behind me the way she’s done before and kills the silence with the sound of her voice."
    "She tells me more about the bathhouse and how she’s thankful that her aunt allows her to live here so long as she helps out from time to time."
    "The thing is “from time to time” seems more like “all the time” as I have never once met Io’s aunt while Io always happens to be here."
    "I guess that she’s never had much reason to leave until recently, though."
    "And given that both Uta and I are the only people she willingly associates with, somewhere like this actually seems pretty good for her."
    "It’s quiet, but not too quiet. And sure, there are plenty of girls who come and go, but all of them are off in a private room while Io is free to..."
    "Well, creepily sit behind her naked, adult male teacher and talk to him about the history of the bathhouse."

    scene black
    with dissolve

    "Wanting the conversation to move in a more interesting direction, I begin dropping scattered innuendos about how Io should join me in the water."
    "They either go unnoticed or ignored, though...as she deflects every single one of them with the thick side of another bathhouse fact, leaving me alone and bored in the water until I have no choice but to get out."
    "Without looking at me, Io gets up as well to find me a towel and tosses it my way before retreating back to the lobby."
    "I get dressed, feeling unfulfilled and mildly confused, before exiting the changing room and finding her back in her usual spot behind the counter."
    "She tries to strike up another conversation, but when I notice the time on the clock behind her, I realize exactly how long I must have spent in the bath and have to cut her off."
    "She’s noticeably upset, but seems to understand as I turn my back to her and leave the bathhouse."
    "But at least I’m leaving knowing much more about it."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label iosummer2nightgen:
    scene iosummer2nightgen
    with fade
    play music "justlights.mp3"

    "I give Io a call right as she’s about to leave work and the two of us make plans to meet up at the bathhouse and walk around the city for a little while before she heads back to the dorms."
    "I let her lead the way seeing as she appears to know this area like the back of her hand, but this ultimately gives her the opportunity to wander into every single store that’s still open and buy food from all of them."
    "Why she can’t just decide on one, I have no idea. But it seems like this isn’t the first time something like this has happened as most shopkeepers seem to recognize her right away."
    "I’m not sure if it’s because she works right around the corner or because there aren’t many green-haired girls with twintails running around Kumon-mi, but I find it a little surprising nonetheless."
    "Not because she’s recognized, though...but because even though every single shopkeeper is female, Io doesn’t seem averse to any."

    scene black
    with dissolve

    "It gets me to thinking that maybe the problem isn’t someone’s sex at all...and that specific genitalia just...gives certain people a disadvantage when it comes to her or something."
    "Honestly, I have no clue. Io’s very vocal about {i}who{/i} she is, but not at all vocal about {i}why{/i} she’s like that or what may have happened to make her that way."
    "I guess she’s just the type that needs to warm up to people...and I guess she has a harder time warming up to people that give off certain auras."
    "Not that I believe in “auras” or anything. I’ve just heard of animals that can identify a human’s sex by their scent alone."
    "Maybe Io is just an animal?"
    "..."
    "Maybe Io just likes my scent?"

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utasummer2archerygen:
    scene utasummer2archerygen
    with fade
    play music "summerwind.mp3"

    "I visit the archery range to find that Uta is not only awake early today, but that she’s already taken it upon herself to head over to the school’s archery range to practice her technique."
    "I find it a little shocking that someone who I know for a fact isn’t a morning person would be able to summon the resolve to actually {i}do{/i} something this early-"
    "But what I find even more shocking is how focused she is."
    "There’s a certain elegance in the way she draws her bow that not only screams that she has done this before, but that it’s something she {i}loves.{/i}"
    "Apart from karaoke, flirty banter, and getting me to empty my wallet, I don’t think I realized that there was {i}anything{/i} Uta loved until now."
    "I watch in awe as she repeatedly strikes the target, taking in the sound of the string snapping each time she releases it."
    "The snap carries across the archery range like a gunshot, waking birds and causing them abandon their nests or homes as she remains unmoving and unwavering in her stance."

    scene black
    with dissolve

    "I don’t attempt to break her out of her trance, as it brings her a level of refined beauty that...I just wouldn’t expect out of someone like Uta."
    "Eventually, she breaks {i}herself{/i} out of the trance and directs her attention to me before apologizing for taking so long."
    "She tells me about how things like this are calming for her and that she didn’t realize how much she missed it."
    "She tells me she’d like to return to Nara one day and practice alongside her brother again."
    "The morning ends with a hushed reassurance from yours truly about how, one day, she’ll be able to."
    "But I know that’s not true."
    "Not unless something changes."
    "Not unless something big changes."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label utasummer2maidgen:
    scene utasummer2maidgen
    with fade
    play music "maidcafe.mp3"

    "Once again, I subject myself to the financial Hell that is the maid cafe while Uta is working."
    "Thankfully, I think she’s beginning to feel bad for me after how much money I have spent on her, as I’ve noticed an increasing amount of complimentary items and discounts as of late."
    "She doesn’t even charge extra for the flavor beam anymore, and I think that might actually be the best part of all."
    "There are people who would kill for this if they had to."
    "I am one of them."
    "The good thing, though, is that this is a power that can only be harnessed by one person...and that even though there are other maids who work here, none of them are ready for it yet."
    "Which...is good. Because if Ami gained this power and began using it at home, I wouldn’t have a reason to leave the house anymore."
    "I couldn’t possibly do that to Uta-chan."
    "If I ever made her sad, I would have to kill myself."

    scene black
    with dissolve

    "Uta-chan disappears into the back room and I wonder for a moment about why life is so unfair and why she can’t just stay in maid form for the rest of eternity."
    "I’m sure that if I asked her, she’d respond with something along the lines of how Uta-chan is only special because she exists only when she needs to."
    "But what she doesn’t understand is that I need her to exist at all times if I am ever going to understand my place in this world."
    "Uta-chan is the key to everything."
    "Uta-chan is the light that guides me home."
    "And I will make her mine, whether she wants to be or not."

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

label otohasummer2streetsgen:
    if otohaspecial15p2 == True:
        scene otohasummer2streetsgenhair
        with fade
    else:
        scene otohasummer2streetsgen
        with fade

    play music "brighterdays.mp3"

    "I make my way over to the park to see what Otoha’s up to and, as always, she’s busy busking and causing any woman who passes by to immediately fall in love with her."
    "I think to myself for a moment about which direction {i}my{/i} life would head in if I were to take up an instrument and spend my days trying to impress women."
    "But then I remember that I’m able to impress them without any notable skills at all, so I discard the idea and make my way over to the bench and wait for Otoha to finish playing."
    "Once the last of her spectators disperse, she packs her guitar up and signals to me that I am cool enough to approach her."
    "I thank her for taking time out of her busy schedule to spend on a nobody like me and then proceed to tease her about more things along those lines because she hates it and making her mad is fun."

    scene black
    with dissolve

    "We do several laps around the park before heading over to the cafe to kill the rest of the morning there."
    "Or, at least that’s the reasoning we verbalize. In all actuality, Otoha probably just wants to hang out with Rin and I am becoming a nuisance."
    "But hey, I’m fine with being a nuisance as long as I can be one around attractive girls, so I decide against pushing her buttons in {i}this{/i} regard as it will soon prove beneficial to me."
    "When we finally make it to Koi Cafe, I’m pleasantly surprised to find that I am not immediately converted into a third wheel and that I am actually able to stay involved in conversations."
    "Unfortunately, that doesn’t really do much for the subconscious feeling that I’m interrupting something by being here."
    "So after hanging around for a short while longer, I grab a coffee to-go and take my leave."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label nodokasummer2librarygen:
    scene nodokasummer2librarygen
    with fade
    play music "morningmoon.mp3"

    "I decide to spend the afternoon at the library because, somewhere in the back of my mind, I’m probably in the mood to discuss the complexities of incest and things of that nature at length."
    "Of course, there is only one person I can share in this with (That I am not already related to), and so I greet Nodoka with whatever my max amount of enthusiasm is and take a seat at the table."
    "The conversation proceeds as you’d expect, with the two of us going in circles and bouncing innuendos off of one another."
    "But, in a weird sort of way, it starts to feel as if we’re developing some sort of code-"
    "Like we understand each other without ever having to divulge any actual details about ourselves which, to me, is pretty great considering I don’t have all that many to divulge to begin with."

    scene black
    with dissolve

    "We reach a point where we run out of steam and convert from constant chatter to silence- but it’s not the sort of awkward silence I’d experience with most people."
    "Nodoka buries her face in a book, kicking her feet up on the table in complete disregard for whether or not I’ll be able to look up her skirt."
    "Unfortunately, she presses her legs together just before I’m able to actually see anything before smugly winking at me and telling me I don’t have enough Nodoka points."
    "I am infuriated by having to redeem currency in order to have my curiosity sated, so I tell her she can keep her points as I make my way to the door, hoping it will make her reconsider."
    "It does not and I am forced to use my imagination as I exit the school and hope that whoever I see next will allow me to see them in some state of undress."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label nodokasummer2nightgen:
    scene nodokasummer2nightgen
    with fade
    play music "icantseeher.mp3"

    "I call Nodoka to find that that she’s taken it upon herself to sneak into the school and spend the night swimming- likely to give herself a break from all of the artistic smut she reads."
    "{i}How{/i} she managed to sneak into school, I’m not going to question. Especially since that is something I have been guilty of on several occasions with several other girls."
    "Regardless, I decide to join her there because the only thing better than a night of discussing the ins and outs of sex (Pun not intended) with an attractive girl is discussing that same exact thing while she is half-naked."
    "Or just having actual sex with her but, given the type of person Nodoka is proving to be and my dramatic lack of Nodoka points, I can’t envision that happening any time soon."
    "When I arrive at the pool, I quickly take notice of a certain level of grace I didn’t really expect to see from her as she swims her way over to me and whips the water out of her hair, soaking my t-shirt in the process."

    scene black
    with dissolve

    "Feeling generous and not wanting to subject me to the {i}torture{/i} that would be watching her swim for the rest of the night, Nodoka joins me along the side of the pool and takes a seat on the tiles."
    "The scent of chlorine is enjoyably pungent as it rolls off of her skin and onto my clothes each time our shoulders touch."
    "She speaks the same way she always does, but the silence brought on by night mixed with the water and a room that only emphasizes each and every noise makes her sound unbelievably powerful."
    "It also makes me feel unbelievably alone...but not in a way that I dislike."
    "Right now, this is the only world that exists to us."
    "And I finally understand why Nodoka may have wanted to spend her time here rather than in a world with everyone else."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukasummer2archerygen:
    scene toukasummer2archerygen
    with fade
    play music "summerwind.mp3"

    "I make my way to the archery range to find Touka wandering around the grounds and...observing the architecture or something."
    "To be honest, she looks a little lost. Though, that could just be me having a hard time linking her ojousama persona to sports, even {i}with{/i} her constant insistence that she’s very athletic."
    "I guess if there was going to be a sport that would fit her, though, this would be it. There’s a certain level of elegance when it comes to archery that, whether or not I can believe it, Touka possesses."
    "Or...{i}would{/i} possess if she would stop wandering around and talking about the craftsmanship of every single wooden structure she encounters."

    scene black
    with dissolve

    "As it turns out, Touka has the same level of appreciation for history that her mother does, and she spends the rest of the morning lecturing me about the origins of kyudo and what early examples of it looked like."
    "It {i}also{/i} turns out that her skills in the art are not as polished as the rest of the girls in the club as of yet, but that she’s working hard to improve and doesn’t plan on giving this up."
    "I admire how headstrong she is and how, even when it comes to things other than kyudo, she never seems to stray from her goals."
    "Before I leave, we take a quick walk around the archery range and she invites me over to her home sometime in the future to see the one her dad built for her."
    "But, knowing that there’s nothing more to the invitation than providing her with another opportunity to give me a history lesson, I don’t accept right away and ask her to let me sleep on it instead."
    "In the end, I leave without making any plans and Touka goes back to wandering around."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label yasusummer2chapelgen:
    scene yasusummer2chapelgen
    with fade
    play music "newhope.mp3"

    "I wind up at the cathedral without any recollection of actually coming here."
    "It feels a lot different inside than it did during Winter, but I imagine it’s due to the fact that this building is likely hundreds of years old and that there haven’t been many upgrades made to it within that time."
    "I approach Yasu and hear her mumbling something to herself, but I’m unable to decipher any of the words."
    "It sounds almost as if she’s speaking backwards."
    "I’m sure it’s just her being weird though."
    "She tends to do that a lot, especially within what’s left of these walls."
    "I attempt to snap her out of her delusions or...visions or...whatever sort of false states of mind someone’s god can force them into, but make no progress at all."

    scene black
    with dissolve

    "It isn’t until she’s finished praying that I’m able to talk to her. But even then, the residual effects of fraudulent divinity contaminate the conversation and make it hard for me to focus."
    "I understand that if I ever want to be with {i}Yasu{/i} and not this shell of a human being possessed by a spirit that I must do so away from this place."
    "And yet I find myself here time and time again, hoping that things will be different when they never are."
    "I leave and incur the wrath of whoever it is she believes in."
    "But her love for me grows because I managed to show up- and that’s more than most people can say."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikosummer2morninggen:
    scene norikosummer2morninggen
    with fade
    play music "noriko.mp3"

    "I call up Noriko first thing in the morning and allow her to talk me into accompanying her to some record store so she can force me to listen to music I don’t like."
    "It’s not the most exciting of plans I have made, but it gives us the opportunity to spend the morning together, and we don’t get to do that very often."
    "Thankfully, the shop she wants to visit isn’t too far away, so the two of us meet up near my house and take a short bus ride over to a shopping plaza she used to visit with her sister all the time."
    "Unfortunately, Niki doesn’t have time for things like that anymore. So the responsibility falls on me as the older brother slash guy she masturbates to to carry the torch and come in her place."
    "And while I might have poked fun at the type of music she’s interested in just seconds ago, I will admit that it is a little fun to watch her get excited about things."
    "Even if those things cause my ears a great deal of both distress and pain."

    scene black
    with dissolve

    "We’re only in the record store for about forty-five minutes or so, so we wind up heading over a nearby brunch place to cap off the morning afterward."
    "Noriko orders a bunch of weird sounding vegetarian food and I just get french toast because I don’t want to hear her talk about how animal cruelty is wrong."
    "Surprisingly enough, the opposite happens when she tells me that I don’t have to worry about appeasing her and that I’m free to eat whatever I want."
    "And so when the waitress returns, I order a side of bacon as well and the morning ends with me getting at least {i}one{/i} thing for myself."
    "Two, counting Noriko. But I’ve apparently already had her for years without even knowing it."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label norikosummer2noongen:
    scene norikosummer2noongen
    with fade
    play music "noriko.mp3"

    "I give Noriko a call to find that she’s using the music room at school to practice playing bass since Kirin kicked her out of the dorm for being too loud."
    "Not having anything else to do, I decide to drop by as well and listen to her play. As it turns out, though, listening to someone play bass isn’t really as exciting as listening to someone play guitar or...piano."
    "Fortunately, Noriko can apparently play all of those things. So she rotates from instrument to instrument, trying to get me to play as well only to fail miserably."
    "I think this is the part where I’d normally say something about how taken aback by her talent I am but, honestly, Noriko seems like some sort of silent prodigy in a lot of different ways."
    "The only thing I can think of that she {i}isn’t{/i} good at is staying away from me, but...let’s face it. There isn’t really {i}anyone{/i} I know who is an expert at that."
    "And, for what it’s worth, Noriko’s actually seemed relatively restrained lately."

    scene black
    with dissolve

    "I’m not sure if it’s because of her sister’s feelings weighing her down or...something {i}else{/i} that I’ve yet to uncover, but..."
    "Well, whatever it is, I hope it doesn’t last long."
    "The truth is that, and don’t tell Maya I said this, I’ve wanted to get “closer” to Noriko since she first walked [[back] into my life."
    "It just seems like every chance we’ve had to make that happen has imploded."
    "It’s almost like fate itself is attempting to keep us apart."
    "I don’t believe that, though. I can’t."
    "Even if she is a relic from my past, she’s one that I deserve to have. And it is within the right of no divine power to keep me from that."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label norikosummer2conveniencegen:
    scene norikosummer2conveniencegen
    with fade
    play music "noriko.mp3"

    "Once again, I find myself tucked deep into the heart of the second half of town, wasting away my night in an old convenience store with a girl who likes me far more than she should."
    "As always, things are pretty calm around here, with an influx of customers so minute that it’s like no one ever shows up at all."
    "Noriko spends the night talking about precious memories from her past and I spend the night wishing I could talk about that too."
    "Instead, I stand there like a sponge, absorbing information that leaked out of me a long time ago and hoping that there will be more memories for her to gleefully look back on in the future."
    "But I know better than most that things like that won’t happen so long as I’m around."

    scene black
    with dissolve

    "If I could strip away her memories and replace them with ones aimed at someone else, I would."
    "If I could rid her of her lingering feelings and years worth of unrequited love, I would."
    "There are many, many things that I would do if only I could find the strength or resolve required to act."
    "And while my acting skills in terms of the masks that I can wear may be among the best, it does not change my inability to fulfill a role I do not understand."
    "And so I continue to stand there and I continue to listen- but I leave with almost nothing."
    "And everything I managed to absorb in those several hours stationary leaks out again once the moonlight hits my skin."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirinsummer2archerygen:
    scene kirinsummer2archerygen
    with fade
    play music "summerwind.mp3"

    "I find Kirin shortly after arriving at the archery range and she immediately stops what she’s doing to come spend time with me."
    "It’s a lot like how things were back when I would visit her at soccer practice in how easily and readily she can drop whatever she’s immersed in and just fall into me instead."
    "The issue with soccer, though, is that she never felt {i}quite{/i} immersed to begin with."
    "I’m not sure if things are the same here. And chances are I {i}won’t{/i} know for quite some time as Kirin isn’t exactly the most emotionally open person I know."
    "Now, if you’re talking physical openness, that’s another story entirely. And one that I’m reminded of quite frequently throughout our time together at the archery range."
    "With each and every gap between the scattered observations thrown our way by the other club members, a small hand finds its way into my lap and reminds me of how filthy it can be."
    "But all I can think of is how fragile it is."

    scene black
    with dissolve

    "Kirin stops reaching for me after I mention something along the lines of how pretty her hands are."
    "I guess it’s harder for her to pretend to be unloved when she hears things like that."
    "It’s good that things end when they do, though, as a flood of attention drifts toward us the moment Uta calls out to Kirin and beckons her to come practice."
    "If this were soccer, Kirin would remain beside me and complain about how she’s tired or doesn’t feel well."
    "But today she gets up."
    "And that might not seem like much of an improvement to you-"
    "But, to me?"
    "To me, it makes her feel like a new person entirely."
    "One who can become immersed without getting lost."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kirinsummer2noongen:
    scene kirinsummer2noongen
    with fade
    play music "love.mp3"

    "I make my way over to Kirin’s house after she informs me that both her parents and her sister aren’t going to be home for the next several hours."
    "And while I interpret that as invitation to come over and fuck her brains out on her parents’ bed, I am informed upon arrival that Kirin just wants to “hang out” today."
    "Yes, I am just as shocked as you are."
    "But, as it turns out, the vaginal insertion of a foreign object the size of her forearm just isn’t something her tiny body is able to handle every single day of the week. Go figure."
    "As such, the two of us sit on her couch and watch crappy reality TV for an hour or two, making idle banter about the people on the television and our thoughts on who they actually are when the cameras aren’t rolling."

    scene black
    with dissolve

    "It reminds me of us in a way, and how we’re just two more people who change based on who is around us and what we need to be at any given moment."
    "The difference is that I make some semblance of an effort while Kirin goes out of her way to act in contradiction to whatever that may be."
    "It’s strange being so similar to someone, yet so different when it comes to the ways in which we present ourselves."
    "Another episode airs and Kirin moves closer to me."
    "I don’t know if it’s a conscious decision or one her mind forces upon her to compensate for how alone she feels."
    "But either way, she ends up beside me."
    "And then on my lap."
    "But never on her sister’s bed."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label kirinsummer2nightgen:
    scene kirinsummer2nightgen
    with fade
    play music "thesleepingcity.mp3"

    "I give Kirin a call, but instead of me coming to meet up with her like things usually go, she takes it upon herself to come visit me instead."
    "I try to stop this considering that a certain redhead also lives in this neighborhood and the idea of her seeing Kirin and me together is relatively alarming, but it does no good as she arrives less than 30 minutes later."
    "What’s even worse is that she winds up directly outside of my door in complete disregard of all of the warnings I gave her beforehand."
    "Thankfully, Ami is in the bath at the time of her arrival, so I’m able to slip outside without being noticed as I take Kirin somewhere more private in an unfortunately platonic way."

    scene black
    with dissolve

    "I’m sure she did all of this on purpose, and I’m sure that she was {i}hoping{/i} Ami would catch her as it would be one more piece of drama she could feed off of to make herself feel good."
    "Or at least {i}attempt{/i} to make herself feel good, but regret it in secret while she cries herself to sleep the following night."
    "No one cries at all tonight, though, as nothing horrible happens."
    "We just take a mostly silent walk through the streets of my neighborhood, clinging to the shadows like they’re handrails, and pretending that we don’t see the world through shit-colored glasses."
    "It’s actually quite nice."
    "But then it ends, and she goes home and cries herself to sleep anyway."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sarasummer2noongen:
    scene sarasummer2noongen
    with fade
    play music "justbehappy.mp3"

    "I call Sara and the two of us make plans to meet at her bar and go for a walk around the neighborhood before her shift begins."
    "What I didn’t realize at the time of making these plans is that “a walk around the neighborhood” was more like being dragged around it while she points out various locations she has fond memories of."
    "I wonder if I’d be like that as well if I could properly recollect my past and where I come from."
    "In fact, I wish I could. Because even if Sara is refusing to let go of my arm and constantly pulling me in a new direction every two minutes, it seems like she’s having a good time."
    "She points to an aqueduct where she broke her leg once and talks about how, in that moment, she believed she was going to die."
    "She tells me all sorts of personal stories, lacing them with grim connotations that sound more like jokes thanks to the way she speaks-"
    "And I never pull away my arm, so she’ll still have something to hang on to when she can’t laugh anymore."

    scene black
    with dissolve

    "She takes me down to the aqueduct and almost slips in the process."
    "I catch her and pull her back to me before she repeats the past and it causes the two of us to fall into the dirt."
    "She lands on top of me like it’s some sort of scene in a romantic comedy."
    "But instead of using the opportunity to either kiss me or blush and apologize for being so clumsy, she just stares into my eyes in silence."
    "For a moment, I think I see something in them."
    "But when a bug crawls across her arm and she gets startled out of her trance, whatever it was disappears."
    "And I walk her home without any idea of whether or not I’ll ever see it again."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label sarasummer2bargen:
    scene sarasummer2bargen
    with fade
    play music "calmbar.mp3"

    "Another night means another chance to drink cheap beer and flirt with an attractive bartender while her daughter cleans glasses in the next room over."
    "Thankfully, Sara is social enough that I don’t have to spend the majority of the night teaching her how to talk to people and, instead, am free to interact the way a normal human being does."
    "One of the things I like most about Sara is how naturally our conversations are able to form and how, despite having not known each other for very long, it feels like we’ve been together forever."
    "I think for a moment about how things would be if I could go back in time and meet her there."
    "About having an upperclassman two grades ahead of me who would pop into my classroom and steal me away from my friends."
    "And about what the rooftop would look like if we were to sit down and eat lunch there."

    scene black
    with dissolve

    "Throughout the night, a stream of customers come into the bar."
    "It isn’t many, but it’s more than before. And it goes to show that Sara is trying her best, even if I don’t always see it."
    "Either that or Yuki is going out and intimidating people into coming here but, at this point, business is business."
    "I accept the moments in which I need to be ignored in favor of furthering Sara’s return to the successful business-owner world and down several more drinks while she tends to other guests."
    "But she always comes back to me once she’s done with them."
    "And that’s far more than I deserve from her."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukasummer2cafegen:
    scene harukasummer2cafegen
    with fade
    play music "cafe.mp3"

    "I drop by the cafe to hang out with Haruka but, when I arrive, she’s surprised to see that I approach {i}her{/i} instead of her much younger and much more lesbian employee."
    "Regardless, she happily accepts the company as she’s been wanting to vent to someone about “adult problems” all week and none of her part-timers really understand them."
    "To be honest, {i}I{/i} don’t really understand them either since the vast majority involve cafe operations and I have never attempted either running or opening a cafe at any point in my life."
    "Probably."
    "I guess there’s a slight chance that I did something like that in the past, but seeing as I am now thinking about it and remaining entirely sentient, it’s probably safe to assume that never happened."
    "I think Haruka catches onto my lack of knowledge about cafes as she takes a seat on the couch and begins asking me about how {i}my{/i} life has been lately."

    scene black
    with dissolve

    "I tell her about how I’m caught in a timeloop with two of my niece’s closest friends and that the secret to the universe might involve me impregnating teenagers."
    "She nods and tells me she knows what it’s like (She doesn’t), and that she’d lend me a hand if there was any way for her to help without being personally impregnated."
    "I shrug off her assistance and move onto other topics as I didn’t really expect her to go along with this one anyway but, honestly, I’m glad she did."
    "I might not be of any help when it comes to hearing {i}her{/i} issues out, but being able to talk about mine to someone who will go along with them rather than ask questions is always a welcome experience."
    "Especially when the person I am talking to sneakily unlatches the top button of her shirt every time I walk into the store."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label harukasummer2nightgen:
    scene harukasummer2nightgen
    with fade
    play music "thesleepingcity.mp3"

    "I give Haruka a call and wind up catching a bus ride over to her neighborhood so the two of us can get dinner at some hole-in-the-wall Chinese restaurant she frequents."
    "I ask her about how long she’s been coming here and she goes silent for a moment, not quite knowing how to respond. Which, in itself, is more of a response than I bargained for in the first place."
    "I’m sure I’m not the first person to take a seat beside her in there."
    "I’m sure I’m not the first person to comment on the sun-bleached menus stuck to the storefront windows and how it looks like the place hasn’t been cleaned in years."
    "But I’m sure I’m the first person who’s done any of those things ever since her husband left."
    "She knows that. And she knows {i}I{/i} know that- which is why she takes it upon herself to come out and assure me that I am not just a replacement."
    "That I am not just someone to block the wind from the rotating fan beside the table we ate at."

    scene black
    with dissolve

    "Haruka disappears into the bathroom for ten minutes and comes back with her eyes slightly swollen and red."
    "She pays the cashier before I have time to comment on them and urges me outside, hoping that the darkness is enough to hide her misery when we all know it’s not."
    "I ignore it, though. That’s just the type of person I am."
    "For if she wants to pretend to be happy, I will too."
    "And I will accompany her into any hole in any wall that she’s afraid to enter alone."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kaorisummer2morninggen:
    scene kaorisummer2morninggen
    with fade
    play music "justbehappy.mp3"

    "I wind up getting talked into coming to the diner after calling Kaori and finding out that they’re having some sort of special today."
    "I am informed upon arrival that {i}I{/i} am special because I am Kaori’s friend and that is what she was actually referring to over the phone."
    "Both flattered and thankful that I am not being added to the menu, I figure that I might as well stick around and hang out with her in between her light-speed trips to the kitchen and back to help other customers."
    "On her eighth trip back, I finally decide what I want to eat. Well, kind of."
    "What I decide is that, in lieu of an actual special that doesn’t fuck teenagers, I want Kaori to make me something herself."
    "She advises me that that is not how a kitchen staff works and that she is not allowed to use the cooking equipment, but then I respond with how the customer is always right and so she is forced to oblige."

    scene black
    with dissolve

    "Feeling determined to make me something truly special and prove to her boss that she is ready to cook, Kaori declares that she will make me the most special thing I have ever eaten before."
    "She uses a lot more words to say that, but fifty percent of them were irrelevant, so I decided to leave them out for your sake."
    "She disappears into the kitchen once again, this time for much longer than the several seconds it normally takes for her to reemerge, but what she has in her hands when she does is not special at all."
    "It’s a peanut butter and jelly sandwich with a side of raw broccoli."

    k "Consume the tiny trees, Friend! They will help you walk longer distances!"
    s "..."

    "I ask for a to-go box and decide to just...eat this later."

    $ kaori_love += 1
    $ pbj += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "{i}You have obtained a peanut butter and jelly sandwich and broccoli!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kaorisummer2noongen:
    scene kaorisummer2noongen
    with fade
    play music "maidcafe.mp3"

    "I give Kaori a call to find out that she has a rare afternoon off, so the two of us make plans to go out to eat at what she describes as “her new favorite restaurant.”"
    "As soon as she sends me the address and I realize where I am going, I’m overcome with an intense feeling of pride that is hard to put into words."
    "I walk into the maid cafe to applaud her for her newfound impeccable taste only to find that she’s decided to bring along John as well."
    "Now, I don’t have a problem with chickens. I just don’t really think this is the right place for them as they’re unable to grasp the concept of-"

    john "Yooooooo why these bitches so cute???"

    "I accept that I will be dining with John as well today and take my place at the table opposite Kaori."
    "I ask her why she thought it was okay to continue coming here without me and she replies with something along the lines of a need to remove clouds."
    "I then ask if she has tried the uniform on again and she informs me that she is saving up money to buy her own, but that she does not want to work here as she can’t “act the way maids do.”"

    scene black
    with dissolve

    "To be honest, that’s probably for the best."
    "Kaori should probably avoid taking on any job that hinges on communication skills because...yeah."
    "Frankly, I think it’s miraculous that she’s been able to survive as a waitress for as long as she has. But hey, if it works, it works. And she is very good at her job in terms of everything except the talking part."
    "Osako, who still works here for some reason, eventually arrives to take our order."
    "Kaori asks for two chicken sandwiches. One for herself and one for John."
    "It arrives shortly afterward and he partakes in the consumption of his own kind."
    "I just get a dessert."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chinamisummer2morninggen:
    scene chinamisummer2morninggen
    with fade
    play music "gentle.mp3"

    "I call up Chinami to find that Chika just left for work a few minutes ago and that she is now lonely and needs someone tall enough to retrieve the box of cereal on top of her fridge."
    "I can’t say I called her with any intention of showing up to perform tasks that she is unable to but, then again, I don’t really have any idea what my intentions were in the first place."
    "Knowing full well how strange and socially unacceptable this is, I head over to Chika’s apartment without her knowledge and then proceed to feed her sister sugary food before letting her out on the balcony."
    "It’s still cool this early in the morning, and Chinami wastes no time exclaiming about how pretty the sky looks and how much nicer it is without all of the glass in the way."
    "It is at that moment that I remember she is not supposed to be out here without supervision, and I can say with absolute certainty that anyone I watch is assuredly not being “supervised.”"

    scene black
    with dissolve

    "As such, I force Chinami back inside and cheer her up with another bowl of cereal before finally deciding that I should tell Chika about this."
    "Not because I feel weird about hanging out with her little sister, though. Because I feel bad that there is now no cereal left and Chika is extremely poor."
    "But if cereal and the exploitation of poverty is what it takes to make Chinami happy and keep her from falling to her death, so be it."
    "I can always replace cereal, but I can not replace her."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chinamisummer2noongen:
    scene chinamisummer2noongen
    with fade
    play music "happyandplotting.mp3"

    "I call Chinami and am immediately yelled at for disturbing her in the middle of what she calls a “very important business meeting.”"
    "I find out soon after that her “meeting” was just a Facetime conversation with Touka’s extremely bratty little sister about a whole bunch of animals they plan on distributing in the coming quarter."
    "And while I think it’s nice that Chinami suddenly has a friend, I do wish she had one that was a little better of an influence."
    "Which probably means nothing from me seeing as I am an adult male who is now en route to her house in the middle of the day, but still."
    "When I arrive, Chinami is busy playing games on her phone and will only speak to me in between rounds of pig-slaughter."
    "I spend the rest of the time questioning my life and the decisions that may have led me here."

    scene black
    with dissolve

    "Chinami stops playing games after her phone suddenly dies and, as I help her look around for her charger, I’m glad that she’s getting so much use out of it."
    "I can only imagine how boring it is having to spend day after day in one room."
    "Maybe {i}that’s{/i} why I’m coming here?"
    "Maybe it’s something as simple as me feeling bad for her because she’s unable to go out and live a normal life."

    s "..."

    "I decide that’s exactly what it is."
    "The only alternative would be much worse."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label karinsummer2morninggen:
    scene karinsummer2morninggen
    with fade
    play music "lifeismostlygood.mp3"

    "I have to call Karin three separate times in order to make plans with her after she accidentally got nervous and hung up on the first two attempts."
    "But once she remembers how to speak and that I am not just an evil penis-bearing entity, the two of us make plans to meet up at a diner near her house for coffee and breakfast."
    "What she did not inform me at the time of making these plans is that she already {i}ate{/i} breakfast and that she wanted to suggest something else, but didn’t want to disappoint me."
    "She orders food regardless so she can take it home to Kirin and I awkwardly sit there and eat while she just...watches me."
    "But hey, at least she’s watching me in admiration and not hesitance or suspicion like she used to."
    "Even {i}if{/i} she’s still struggling to talk normally around me, I know that she’s gotten a lot better and that {i}we{/i} have gotten a lot closer."

    scene black
    with dissolve

    "There’s still much room to go, though."
    "Just being the only man in her life apart from her father is not enough to sate my appetite."
    "I don’t care how many breakfasts I must eat alone or how many rice balls she’ll stuff into to-go boxes."
    "I will take what I want for-"

    ka "Um...S-Sensei?"
    ka "You look...I don’t know...different?"
    ka "Is everything okay?"
    s "..."

    "I stare down at a plate still full of food and a half-empty cup of coffee-"
    "And suddenly feel full."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label karinsummer2poolgen:
    scene karinsummer2poolgen
    with fade
    play music "retrospect.mp3"

    "I call up Karin to find that she’s spending the afternoon teaching little kids how to swim at the school pool, which might just be the most {i}Karin{/i} thing I have heard her do since I met her."
    "She nervously asks if I’d like to join and I obviously respond with the fact that I do not enjoy children, but am then assured that they’ll be leaving soon anyway."
    "Sensing a fantastic opportunity to see Karin in significantly less clothing than normally, I head over to school as quickly as I can and find her sitting on a bench off to the side of the pool."
    "I take a seat beside her, leaving about a foot of distance between us so she doesn’t burst into flames, and she begins to tell me about how she’s loving it here so far."
    "Karin feels bad about how quickly she’s gotten over the departure from soccer given how upset Miku was and still {i}is{/i} over it, but being the captain makes her feel really good about herself."

    scene black
    with dissolve

    "Karin doesn’t know if there’s a career for her in swimming and, frankly, it seems like she doesn’t really {i}care{/i} if there is."
    "She’s just enjoying herself while she still can and helping others in the process."
    "She’s also doing wonders for her already ridiculously athletic body since swimming is one of the best full-body exercises out there."
    "Sensing her desire to get back into the water, I tell her that she doesn’t have to mind me and that she can get back in whenever she wants, but she abstains."
    "She says there’s something else she’d rather do right now instead."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label makisummer2morninggen:
    scene makisummer2morninggen
    with fade
    play music "cafe.mp3"

    "I give Maki a call and the two of us make plans to meet up at the cafe for breakfast."
    "I guess she must consider it a special occasion or something as, when I get there, she’s not in her usual “casual pajama” look that she is somehow always okay with wearing out in public."
    "But hey, maybe those days are gone forever as she turns over a new leaf and joins the world of working adults who wear normal clothes when they’re not at home."
    "I suppose that she and I may have different definitions of “working adults” though seeing as her line of work involves a much greater deal of semen than mine."
    "Sometimes."
    "Either way, the two of us grab some coffee and take a seat in the back of the room to talk about sex or something away from the prying ears of Haruka as she is dramatically deprived of it."

    scene black
    with dissolve

    "Upon sitting down, Maki becomes unusually sentimental and thanks me for both spending time with her and “taking care” of her daughter on a daily basis."
    "I breathe a sigh of relief in knowing that she doesn’t quite understand exactly {i}how{/i} I am taking care of her daughter."
    "But in terms of spending time with Maki, I don’t really understand why I need to be thanked at all. I’m the one who called her. It’s not as if someone is paying me to do this or anything."
    "The fact of the matter is that when you look past the waterfall of euphemisms that creates the bulk of her personality, she really is just a normal girl who wants and tries to relate in her own sort of way."
    "The only problem is that she’s likely grown accustomed to {i}her{/i} way pushing others back. But I’m not one of those people."
    "So I thank her in return for spending time with {i}me-{/i} another person who just can’t seem to relate."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label makisummer2porngen:
    scene makisummer2porngen
    with fade
    play music "citylife.mp3"

    "I make my way over to the porn shop to find Maki restocking the shelves after some woman came in and purchased nearly her entire inventory of giant rubber penises."
    "It was probably Sara. That seems like something she would do."
    "Maki quickly misunderstands my presence in her store as a call to be lectured about the history of sex toys and their evolution over the past hundreds of years- a thing I don’t really care about knowing."
    "But it is her immense education on the topic that helps me realize where her daughter gets {i}her{/i} diligence from."
    "The only thing is that Makoto’s diligence extends to things beyond sex toys and Maki has now been discussing them for a good fifteen minutes without showing any signs of stopping."
    "I take it upon myself to remind her that my interest in dildos is very limited, which she misinterprets as a desire to learn more about the history of male sex toys."

    scene black
    with dissolve

    "I must wait {i}another{/i} fifteen minutes for her to stop talking about those until I finally have an opportunity to tell her that I’m just here to hang out and don’t want to be educated."
    "She’s visibly upset by this but understands and ultimately decides to put down the oversized dildo she’d been waving around for the entire conversation and take her place behind the counter instead."
    "The rest of the night proceeds with limited mention of penises (Or as limited as that can be with Maki) while the two of us talk more about her background and how she got to where she is today."
    "Of course, that comes to a screeching halt once she asks about mine."
    "Two whole hours manage to pass by without either of us noticing and eventually the time comes for me to head back home and inform my niece that I was not murdered."
    "Maki escorts me to the door and locks up shop in turn, but not before giving me one final (Albeit very brief) history lesson on the origin of the rubber vagina."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nikisummer2morninggen:
    scene nikisummer2morninggen
    with fade
    play music "remember.mp3"

    "I give Niki a call to see if she wants to go out for breakfast but, being tired of the sausage fest (Which I didn't realize was possible), she decides to come over to my neighborhood instead."
    "Of course, she refuses to part with her disguise as the two of us walk around in public."
    "But, honestly, I’m surprised that disguise does {i}anything{/i} at all considering there aren’t many young, pink-haired bombshells just casually wandering the streets of Kumon-mi."
    "I make sure to notify her of this, which she does not appreciate at all and, in typical tsundere fashion, she proceeds to berate me for the next thirty minutes over it."
    "It’s fine, though. It’s not like I wanted her praise anyway."

    scene black
    with dissolve

    "The two of us continue to walk around the area for about half an hour or so and Niki’s beratement turns into a lengthy comparison of my current neighborhood to the one we grew up in."
    "Having no recollection of such a thing, I listen closer than I typically would and come to find that, in one way or another, things have improved a lot for me."
    "I’m not sure if I’d call being periodically subjected to the apocalypse an improvement in {i}every{/i} regard, but it’s still nice to hear that things somehow worked out well for the two of us."
    "Sure, I might not be a famous idol or anything like that-"
    "But I get to have sex with as many attractive teenagers as I want. Which, by my standards, is a hell of a lot better."

    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label nikisummer2nightgen:
    scene nikisummer2nightgen
    with fade
    play music "love.mp3"

    "I call Niki a little bit later than normal to find that she’s holed up in some fancy hotel in the urban district."
    "Her mild inebriation at the time of my calling somehow converts into full on drunkenness by the time I get there and the two of us spend the night relaxing on the bed and talking about life."
    "Of course, being that the two of us are on a mattress and my libido is ten times greater than that of an average male, I attempt to turn our conversation into something more."
    "Unfortunately, Niki becomes an even bigger bitch when she is intoxicated and spends the rest of the night teasing me and blocking me from making any sort of move."
    "I continue to press on in hopes of changing that and eventually come extremely close, only to have her pass out minutes later."

    scene black
    with dissolve

    "While my mission to hook up with an idol may have failed tonight, I am sure there will be many victories to come in the foreseeable future."
    "I’m just not sure if any of them will come while Niki is under the influence."
    "I guess that’s kind of a good thing, though, as it makes my moral compass appear a lot stronger than it actually is- and prevents {i}her{/i} from doing something she may potentially regret."
    "Not that I think she’d regret anything happening between the two of us when tons of things have {i}already{/i} happened."
    "What I think she’d regret is not remembering it."
    "Either way, seeing as she is now unconscious and I have nothing else to do, I take it upon myself to summon a ride back home and hope silently along the way that my next trip to a hotel will have a happy ending."

    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukisummer2bargen:
    scene yukisummer2bargen
    with fade
    play music "calmbar.mp3"

    "I make my way over to the bar to find that Yuki is handling tonight’s shift on her own."
    "And while I’d like to applaud her for the improvements she must have shown in order to be given a responsibility like that, I understand that it’s likely just due to a lack of customers."
    "Either way, the fact that she’s been able to successfully hold down a job despite never having one before is something to be proud of."
    "And, with me being a hard-working member of society, you can take my word for it."
    "Yuki and I spend the majority of the night discussing how her life has been changing lately and the intense turnaround she was able to make."
    "We also discuss a certain black-haired tsundere that is still out there hoping to turn the early stages of {i}her{/i} life around."

    scene black
    with dissolve

    "Despite their distance, it’s clear that Yuki still cares deeply about her daughter."
    "And even though Yumi’s nowhere near ready to forgive her mother for her absence and negligence all those years ago, I think it’s clear that the widest part of the rift is beginning to close."
    "At this rate, there’s no knowing if it will ever be repaired. But the fact that Yuki is able to start moving forward regardless of that is a huge testament to her power as a person."
    "The night concludes with one of her token wise-man style bouts of unsolicited advice in which she reminds me to hang on to the things I love most."
    "But she doesn’t tell me what to hang onto in the event that I can’t find anything."

    $ yuki_love += 1
    stop music fadeout 5.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label tsubasasummer2noongen:
    scene tsubasasummer2noongen
    with fade
    play music "tsukiokamanor.mp3"

    "I give Tsubasa a call and get talked into coming over to her manor as she’s unable to leave the premises today for rich person reasons."
    "I guess that’s fine, though. I’m comfortable enough with my commoner lifestyle to not be put off by the overwhelming success of others- even if those people are born into it."
    "Do I think it’s a little unfair? Sure. But Tsubasa, at least so far, seems like a good person. So even if she wasn’t born into a wealthy family, I’m sure she would have figured it out so far."
    "Once I arrive, I’m escorted through the gates by a group of servants and taken to meet Tsubasa in her usual water garden."
    "As always, her husband is nowhere to be found and I wind up hanging out with her while he’s off being inattentive and unintentionally abstinent."

    scene black
    with dissolve

    "Tsubasa takes me inside and gives me another tour of her endless abode, once again packed with history of the Tsukioka family and where all of their various treasures have been imported from."
    "Along the way, she prods me for information about her daughter and how she’s doing in school."
    "She {i}then{/i} tries to pawn her other daughter off on me. But I’m pretty sure that’s only because Tsubasa is a step or two away from making her disappear forever at this point."
    "Eventually, she takes me into the dining hall for a full-on buffet prepared by a team of world class chefs that will likely all be fired by a certain someone before nightfall."
    "Not really knowing how to approach this (Or even what the majority of the food {i}is{/i}), I take a seat at the table and allow Tsubasa to choose my lunch for me."
    "Before I know it, I have gorged myself to the point of being unable to walk anymore and need to be driven back home by her personal driver- but not before packing another box of rich person food for Ami to try."

    $ tsubasa_love += 1
    stop music fadeout 5.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label wakanasummer2morninggen:
    scene wakanasummer2morninggen
    with fade
    play music "phantomthief.mp3"

    "I call up Wakana to find that she’s spending the morning in her office to grade papers and keep her plants company."
    "Why plants need company, I don’t know. But I decide to join her anyway seeing as I have nothing else to do and feel the need to be reminded of how miserable and pointless life is every few minutes."
    "Wakana does not disappoint in that regard, bashing me over the head with her catchphrase immediately upon my arrival before asking me to do all of her work for her so she can take a nap."
    "I’m surprised that she’s even {i}okay{/i} with the prospect of taking a nap in the same room as me, but...I guess there’s a lot about our dynamic that I’m being constantly surprised about."
    "Anyway, surprise or not, I refuse Wakana’s task as I can’t even be bothered with grading my {i}own{/i} papers, let alone hers."
    "She goes back to watering her plants with a sigh and mentions that she’ll just grade everything from home later on tonight."
    "This, of course, calls into question why she even bothered coming here in the first place if she was just going to shrug it off since...I don’t think plants need to be watered every day."
    "I’m no botanist, though. So I may very well be completely off the mark with that."

    scene black
    with dissolve

    "Wakana finishes up providing [[potentially] needed water for her foliage friends and collapses onto the couch seconds later before, you guessed it, once again complaining about how painful it is to be alive."
    "I join her in an attempt to complain as well only to be berated and told that I don’t understand, which is fair since my life is pretty great."
    "But, without knowing too much about Wakana, hers seems like it’s not that bad either."
    "I guess you can never really know for sure, though."
    "Minutes later, I am told to get lost so Wakana can go {i}tend to something-{/i} whatever that means."
    "I oblige and, before I know it, I’m back outside of the school and looking for something to do."

    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label wakanasummer2nightgen:
    scene wakanasummer2nightgen
    with fade
    play music "love.mp3"

    "I somehow find myself going over to Wakana’s apartment after calling her and finding out that Osako is going to be working late tonight."
    "And while that may potentially make it sound as if the two of us are doing something inappropriate behind her back, I can assure you that it is anything but."
    "Instead, the two of us sit on separate couches in her incense-filled living room slash bedroom and watch some televised documentary about the occult in Japan."
    "And while that’s not something I’d typically find myself getting interested in, the fact that I am very much currently living in a scenario that many would describe as “occult” makes me reevaluate that."
    "Unfortunately, the series on the television is primarily focused on aliens and I have a hard time believing they have any part in the manipulation of time and our world as a whole."
    "But, then again, we’re also apparently in the middle of a space war- so I guess anything is possible."

    scene black
    with dissolve

    "Osako comes home to find the two of us watching television and quickly needs to force herself into pretending that she’s not jealous that I’m spending time with her girlfriend."
    "Wakana takes notice of this and teases her about it. But, in doing so, makes it sound like she would never be interested in me that way, which I take great offense to."
    "I guess just being friends is fine for now, though. It’s not like I want to fuck {i}every{/i} girl in Kumon-mi. Just-"
    "Actually...no. I’d definitely still have sex with her if given the opportunity."
    "But I don’t {i}have{/i} to do that and can probably live with the idea of it just...not happening."
    "I just hope that it does."
    "..."
    "I really hope that it does."
    "Anyway, it quickly becomes apparent that the reason for me being here has vanished, and so I bid the two of them goodbye and make my way out of the apartment."
    "As I do, I notice John outside of Kaori’s apartment- staring off into space, entirely unaware of my presence."
    "I leave before he notices me and manage to make it home without interacting with any animals."

    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label osakosummer2dojogen:
    scene osakosummer2dojogen
    with fade
    play music "rapid.mp3"

    "I show up at the dojo and reluctantly agree to spar with Osako, a decision I immediately regret."
    "It was only a matter of time until something like this happened again, though. There are only so many days I can go without participating in any of her lessons without getting my ass kicked."
    "But hey, if that’s the price I need to pay for slacking off 99%% of the time, it’s fine."
    "To be completely honest, getting beaten up by someone like her is light years better than getting beat up by some hairy dude in an alleyway somewhere."
    "And while the prospect of that ever happening to me is extremely low considering the near-complete lack of men in Kumon-mi, it’s moments like this where I need to look at the bright side of life."
    "And so, if this flying kick connects with one of my ribs and goes on to puncture one of my lungs, I want you to know that I died with no regrets."
    "Well, no regrets apart from the fact that I never got to have a threesome with Osako and her girlfriend."
    "Goodbye, world."

    scene black
    with dissolve

    "The kick connects, but my ribs and lungs emerge unscathed and the idea of an eventual threesome is still slightly possible."
    "I thank the god I don’t believe in for the precious gift of life as Osako reaches down to help me up and apologize for going a little too hard."
    "As it turns out, though, I am apparently an excellent target when it comes to letting her rage out as this sort of kick would probably kill at least 80%% of her students."
    "I’m not sure whether or not that is a good thing as it means I will likely continue to incur attacks like this in the future, but at least I’m alive."
    "Either way, I wind up sticking around after the rest of the class goes home and talking to Osako for a bit before she needs to get ready for her second job."
    "Once she does, I throw back on my normal clothes and head back into the street."
    "I just...have to do it a little slower than normal as I am still very much in pain."

    $ osako_love += 1
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label imanimorninggen:
    scene imanimorninggen
    with fade
    play music "love.mp3"

    "I give Imani a call and somehow wind up going over to her place first thing in the morning."
    "Is making a trek across town something I {i}wanted{/i} to do as soon as I woke up? Absolutely not. But for some reason, I just have a hard time saying no to her."
    "Maybe it's due to the fact that I'm well aware she's doing my job {i}for{/i} me at this point and that I feel...indebted to her for that."
    "Or maybe it's because I just like being around her for some strange, borderline masochistic reason. I wouldn't put something like that past me at this point."
    "I'm sure I have a tipping point when it comes to incessant teasing without any payoff but, if I'm able to survive Uta, I'm positive I can handle Imani."
    "I also don't think Imani would have to make any phone calls before taking her pants off and, to me, that is a major plus."

    scene black
    with dissolve

    "The two of us spend the morning sitting on her bed (Which is actually just a mattress on the floor) and talking about school (Which is really just her regurgitating gossip)."
    "Why she wants to be so involved in school drama, I have no clue. But she {i}does{/i} feel like a teenager trapped in an adult's body at times, so I guess it makes sense."
    "I'm not about to tell her how to live her life. And, to be honest, she seems so focused most of the time that I doubt she'd even listen to me if I did."
    "Instead, I just let her do her thing...because I know that chances are, one day, I'm not going to have her around anymore...or at least not as much as I want."
    "Unless the world has something to say about it, I guess."
    "But for her sake..."
    "I kind of hope it doesn't."

    $ imani_love += 1
    stop music fadeout 5.0

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label mayanightgen:
    scene mayanightcallgen
    with fade
    play music "love.mp3"

    "I give Maya a call and ask her to come over to my secret apartment so the two of us can {i}not{/i} have sex with each other."
    "Boring, I know. But given that she actually cares about me and doesn't want my brain to melt, this is really all we can do."
    "Am I willing to risk that for what I have come to personally refer to as “The forbidden vagina?” Probably. But alas, I remain unwillingly abstinent in the face of greater peril."
    "Incessant innuendo aside, this is fine. It's {i}good{/i} that we can be together now without the constant bickering and references to how disgusting I am."
    "Which isn't to say we {i}are{/i} together without those things. They still happen."
    "But they don't have to."
    "And they only {i}do{/i} because that's what “normal” is for us."

    scene black
    with dissolve

    "We spend the night out on the balcony, looking up at the stars and the moon."
    "And every time I try to touch her, my hand is slapped away."
    "It stings, but not due to the sensation."
    "It stings because she's the one thing I want that I'm not allowed to have."

    $ maya_love += 1
    stop music fadeout 5.0

    "{i}Maya's affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label amyevent:
    play sound "static.mp3"
    scene gpmx1 with flash
    stop sound
    play music "firstsecondmall.mp3"

    "I make my way over to the mall to hang out with Chika, but take a wrong turn somewhere and get stuck in an alternate reality instead."

    scene gpmx2
    with dissolve4

    s "..."
    q "..."

    scene gpmx1 with hpunch

    "A mysterious creature shows up and immediately scurries away as it may be the first time she’s seen a human being in hundreds of years."
    "She looks like someone I can’t remember, so I clap my hands to show her I’m not a threat and coax her into returning."

    scene gpmx2 with dissolve2

    q "..."
    s "..."
    q "Um..."
    q "By any chance...are you..."
    s "Looking for a good time? Sorry lady, but I’m {i}not that kind of guy.{/i}"
    q "No! U...Um...What I meant was...are you...by any chance..."
    q "Named...Akira?..."
    s "How do you know my name, mysterious creature?"
    q "Oh my God! It really {i}is{/i} you, isn’t it?! It’s been so long! "
    s "Sorry, but...have we met before?"
    q "Only once. You helped rip number 17 out of my mouth after my gums became infected and I’ve been searching for you to say thanks ever since."
    q "But, as you can see, I haven't really had any success until now."
    q "God, it's been so long."
    s "Do you have a name? "
    q "Oh! Right! Silly me."
    amy "I’m Amy. "
    amy "Do you...Do you come here often?"
    s "Yeah, but I’m normally on the other side."
    amy "The other side?..."
    amy "Do you mean the west wing?"
    s "No, I mean the side where the colors are brighter and there aren’t any character sprites."
    amy "I’m a little confused...but if you’re not familiar with the mall, I wouldn’t mind showing you around!"
    s "No thanks. I’m just gonna head back to where I came from and go hang out with Chika instead. But it was nice seeing you and I’m glad to hear your gums are doing okay."
    amy "But...you can’t leave."
    s "Why not?"

    play sound "jackpot.mp3"
    scene gpmx3

    amy "Because this is a special bonus mission. Nobody is allowed to leave until they’ve had enough fun at the mall. And even then, it's really difficult and there’s no reason to leave in the first place."
    amy "The world outside these walls is contaminated. Breathing in the air for longer than three minutes will fill your lungs with some weird stuff and then you’ll die."
    s "So, all I have to do is have fun at the mall and I can leave?"
    amy "I mean...{i}technically{/i} yes. But...did you not just hear the part about how you’ll die?"
    s "Don’t worry. If I die, everything will just start over. It’ll be totally fine."
    amy "Then...in that case, maybe you and me could walk around for a little while? "
    s "You mean like a date?"

    scene gpmx2
    with hpunch

    amy "D-Date?!?!?!"
    amy "You’d really...consider going on a date with someone like me?..."
    s "Do you have any STDs?"
    amy "Not any of the bad ones. "
    s "Then sure. I don’t see any harm in that."
    s "Plus, it’ll help me get acquainted with your side of the mall better. So if you have any tips or recommendations, please let me know."
    s "I’m very excited to get going!"
    amy "Me too! But, be warned — it’s really easy to get lost in there. So easy that even {i}I{/i} get lost sometimes, and I’ve been here for thousands of years!"
    s "You look so young for someone in their thousands."
    amy "Teehee! You should have seen me when I still had hands."

    scene gpmx1
    with dissolve

    amy "Come on! Let’s get started!"
    amy "I’m sure it’ll be a load of fun!"

    scene black
    with dissolve2

    "........."

    jump gpmaintro

label gpmaintro:
    stop music
    play sound "static.mp3"
    scene gpma1 with flash
    stop sound
    play music "secondmall.mp3"
    $ renpy.pause(7, hard=True)
    $ gpma = True

    scene gpma2
    with dissolve2

    amy "Hey! Sorry about that. I slipped through a crack in reality and wound up somewhere in Halo 3. But I’m back now!"
    s "Great! Because I have absolutely no idea where we are."
    amy "I already told you, silly! We’re at the mall."
    amy "Before this, you were in the waiting room. That’s the room that you’re supposed to wait in before you’re admitted to the mall."
    s "Sounds like a pretty serious mall if you need to wait just to get in."
    amy "It’s the most serious mall! Everything you could ever want is here. It’s a little sad though since not many people know about it yet."
    amy "But I’m sure it will be swimming with customers in another year or two! You’ve gotta keep your hopes up, you know?"
    s "So, where should we start?"
    amy "Anywhere you want!"

    scene gpma3
    with dissolve

    amy "It’d be no fun if I were to just take control of the date, you know? Gender roles dictate that the man is supposed to decide things like this and I’m just supposed to be good and listen to whatever he wants!"

    scene gpma5
    with dissolve

    amy "I’m sure any decision you make will be fine! Like I said, everything you could ever want is here. And even if there’s {i}nothing{/i} you want, we have that too!"
    amy "There’s a hole in the wall of the white room you can throw yourself into that will send you falling for the rest of eternity. That’s where my last boyfriend went, but I didn’t have anything to do with it."
    s "Cool. Then-"
    amy "I promise I didn’t have anything to do with it."
    s "..."
    amy "I didn’t throw him into the hole."
    s "Okay Amy."

    scene gpma4
    with dissolve

    amy "Seriously, it wasn’t me. He did it himself."
    s "I-"
    amy "I didn’t put him in the hole."
    s "..."
    amy "..."

    scene gpma2
    with dissolve

    amy "A-Anyway! I’ll shut up about the hole now..."
    amy "Just choose a direction and we’ll go from there!"

    "Oh jeez."
    "I sure hope I don’t get lost."

    $ renpy.block_rollback()

    menu:
        "go left":
            jump gpmb
        "go right":
            jump gpmc

    $ renpy.block_rollback()

label gpma:
    scene gpma1 with dissolve
    s "Hmm..."

    scene gpma2 with dissolve

    amy "What’s wrong, Akira? We’ve already been over here."
    amy "Is there something else you wanted to see?"

    if gpma and gpmb and gpmc and gpmd and gpme and gpmf and gpmg and gpmh and gpmi and gpmj and gpmk and gpml and gpmm and gpmn and gpmo and gpmp and gpmq and gpmr and gpms and gpmt:
        jump gpmending
    else:
        s "Nothing in particular. Just trying to figure out what I want to do."
        amy "Well, I’m ready whenever you are!"

        $ renpy.block_rollback()

        menu:
            "go left":
                jump gpmb
            "go right":
                jump gpmc

        $ renpy.block_rollback()

label gpmb:
    if gpmb == True:
        scene gpmb1 with dissolve
        s "Hmm..."

        scene gpmb2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmb1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmb2 with dissolve2

        amy "Watch your feet, Akira. The foundation of this hall hasn't fully grown in yet and it’s caused the whole wing to get a little uneven."
        amy "It’s kind of annoying to walk in sometimes, but I bet it would be really fun with a skateboard."
        s "Do you have a skateboard, Amy?"
        amy "Me? I could never. I have a degenerative bone disease and my doctor says extreme sports aren’t good for me. But I do know of a shop here that sells them if you want to try!"
        s "Do you think I’d look cool as a...skateboard person?"
        amy "Of course! I think you’ll look cool no matter what you do."
        amy "You've got a bit of a...cool {i}aura{/i} to you that's hard to describe."
        amy "Like that feeling you get when you spin around really fast and start to see those white specks everywhere. Just, instead of white specks, it's like...I don't know. Cooler."
        s "Well, for what it's worth, I think you're pretty cool too. Even {i}with{/i} your faulty bones."
        amy "Aww...Thanks, Akira. That means a lot to me."
        amy "I try to keep a positive attitude, but it's hard not getting down on myself sometimes when I look in the mirror, you know?"
        amy "Like, I'll think to myself...Amy! No one is ever going to love you and the world would be better off without you in it!"
        s "Wow. That's extremely depressing and very likely untrue."
        s "Take me, for example. Without you, I'd be totally lost."
        amy "Hahah! Thanks, Akira. It's the same for me whenever I'm not with you."
        amy "Just...a little differently."

        $ gpmb = True

    $ renpy.block_rollback()

    menu:
        "go left":
            jump gpmt
        "go forward":
            jump gpmm
        "go back":
            jump gpma

    $ renpy.block_rollback()

label gpmc:
    if gpmc == True:
        scene gpmc1 with dissolve
        s "Hmm..."

        scene gpmc2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmc1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmc2 with dissolve2

        amy "..."
        s "Hey, Amy?"
        amy "Yeah? What’s up?"
        s "What are those blurry spaces behind you?"
        amy "Temporal rifts! Nobody knows what happens if you go inside of them. But I definitely wouldn’t recommend it since I threw a plastic bottle in one time and it came back out full of pee."
        s "Oh, okay. We should probably avoid the temporal rifts then."
        amy "Exactly! Always avoid the temporal rifts."
        s "Can you tell me anything else about this wing?"
        amy "Of course! This is where we keep foliage. That’s the fancy word for “leaves and plants and stuff.”"
        amy "And while they might just look like normal plants, they have a really important job!"
        amy "Since no air from the outside can get in without putting all of us in danger, the foliage generates oxygen and helps us breathe! I think. I never paid much attention in science class."
        amy "I just know that damaging any of the plants is punishable by-"
        s "Being thrown into the same hole your last boyfriend was thrown into?"
        amy "Ugh! Akira! Don’t tease me about that! You’re gonna make me mad!"

        $ gpmc = True

    $ renpy.block_rollback()

    menu:
        "go forward":
            jump gpmd
        "go right":
            jump gpme
        "go back":
            jump gpma

    $ renpy.block_rollback()

label gpmd:
    if gpmd == True:
        scene gpmd1 with dissolve
        s "Hmm..."

        scene gpmd2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmd1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmd2 with dissolve2

        amy "Over here is where we gather to eat our meals and drink coffee and stuff!"
        amy "You can get all sorts of food in the mall, but my favorite is the garlic bread from Shiawase Group. I know it sounds boring, but they do this thing where-"
        s "I have no interest in bread, Amy."
        amy "How come? Bread is good for you. The carbohydrates suck away the excess moisture in your intestines and make it so any living creature you accidentally ingest has a harder time moving around."
        s "Is that a thing you actively worry about?"
        amy "Absolutely! If you’ve ever had a tapeworm, you’d understand."
        amy "Thankfully, there have been no recorded cases of anyone contracting tapeworms from Shiawase Group! Or {i}anywhere{/i} at the mall!"
        amy "So if there’s somewhere you’d like to stop and grab a bite to eat, just let me know. We’ve got a lot more walking ahead of us after all."
        amy "You’re going to need all the energy you can get."

        $ gpmd = True

    $ renpy.block_rollback()

    menu:
        "go left":
            jump gpmf
        "go right":
            jump gpmg
        "go forward":
            jump gpmh
        "go back":
            jump gpmc

    $ renpy.block_rollback()

label gpme:
    if gpme == True:
        scene gpme1 with dissolve
        s "Hmm..."

        scene gpme2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpme1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpme2 with dissolve2

        amy "Oh! I know exactly where we are! Even more so than normal!"
        s "Is this what they call a “power spot?”"
        amy "What? No. What even is that?"
        amy "What I was going to say is that I used to ride that little helicopter thingy over there when I was little."
        amy "It plays this song my mom used to sing to me. It’s called, like...Daisy Bell, I think? Or Bicycle Built For Two? I don’t know. It’s one of those."
        amy "Wow, this brings back so many memories."
        s "Are you still in touch with your mom?"
        amy "I am! We meet up on Wednesdays to go water the plants and have our retinal fluid refilled over in the medical ward."
        amy "My vision is fine, but hers is starting to get a little worse as the years go by. So I still get the shots myself so she doesn’t have to feel bad about going blind."
        s "You’re such a good daughter."
        amy "Oh, stop! You’re gonna make me blush..."
        s "..."
        amy "..."
        amy "Um..."
        amy "Hey...Akira?"
        s "Yeah?"
        amy "Do you really not remember the first time we met?"
        s "I’m sorry, but...no. I really don’t."
        amy "I see..."
        s "..."
        amy "..."
        s "Are you okay?"
        amy "Y-Yeah! I just..."
        amy "It’s nothing. Don’t even worry about it."

        $ gpme = True

    $ renpy.block_rollback()

    menu:
        "spin":
            jump gpmi
        "do a flip":
            jump gpmn

    $ renpy.block_rollback()

label gpmf:
    if gpmf == True:
        scene gpmf1 with dissolve
        s "Hmm..."

        scene gpmf2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmf1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmf2 with dissolve2

        amy "Guh. This part of the mall always creeps me out."
        s "Why is it so dark?"
        amy "Rumor has it that a long time ago, when the mall was first coming into existence, a small group of some...weird kind of entity or something snuck in and started nesting around here."
        amy "I think I heard a thing about how they’d burrow into the ground and then pull the tiles back over the holes they dug to make it look like everything is normal."
        amy "It reminds me a lot of some story my dad read to me when I was little. About these weird monster thingies retreating into the earth to suck up energy from the soil."
        amy "I also heard that if they suck up enough, they can manipulate their bodies into appearing human! Meaning some of them could be here right now and we’d have no idea!"
        s "I’m having second thoughts about exploring this part of the mall now."
        amy "I’m sure it’ll be okay. We have each other, after all!"
        amy "And..."
        amy "I feel..."
        amy "I feel really safe when I’m with you..."

        $ gpmf = True

    $ renpy.block_rollback()

    menu:
        "go in the diagonal direction":
            jump gpmk
        "go left":
            jump gpmo
        "go back":
            jump gpmd

    $ renpy.block_rollback()

label gpmg:
    if gpmg == True:
        scene gpmg1 with dissolve
        s "Hmm..."

        scene gpmg2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmg1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmg2 with dissolve2

        amy "Hey, Akira. See that hole in the ceiling?"
        s "Yeah, why?"
        amy "{i}I dare you to go inside.{/i}"
        s "How would I even get in there? I’m not nearly tall enough and my jumping skills are subpar at best."
        amy "I can give you a boost! I’m stronger than I look, you know."
        s "How about I just give {i}you{/i} a boost instead?"
        amy "So you can peek up my skirt? No way, Jose. That’s third date territory right there."
        s "I feel like we’ve been here long enough at this point to count it as multiple dates."
        amy "Nuh-uh! You haven’t seen anything yet!"
        amy "Actually, come to think of it, we’re not far from the official mall mascot’s cage."
        s "There’s an official mall mascot?"
        amy "Yup! It’s a naked homeless man who showed up here on accident one day."
        amy "He kept screaming about wanting to get out, but mall policy dictates that all complaints must be sent directly to the main office, so he was tied up and thrown into a cage."
        s "That doesn’t sound very legal."
        amy "The craziest part of all of it is that his face has been slowly disappearing day by day. All that’s left now is his right nostril and a tiny skin-gap where his mouth used to be."
        amy "I wonder how he eats?"
        s "I don’t think I want to see the homeless man."
        amy "Are you sure? I have a handful of pennies we can throw at him to make him do a dance."
        s "I’m good, Ami."
        amy "Amy."
        amy "It’s {i}Amy.{/i}"
        amy "There is no Ami here."

        $ gpmg = True

    $ renpy.block_rollback()

    menu:
        "go forward":
            jump gpmi
        "go sideways":
            jump gpmp
        "go back":
            jump gpma

    $ renpy.block_rollback()

label gpmh:
    if gpmh == True:
        scene gpmh1 with dissolve
        s "Hmm..."

        scene gpmh2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmh1 with dissolve2
        $ renpy.pause(2, hard=True)

        s "..."
        s "..."
        s "..."
        s "Amy? Where did you go?"

        scene gpmh2 with dissolve2

        amy "Up here!"
        s "Woah, how did you do that?"
        amy "Heheh! Cool, right?"
        amy "There are a few rooms in the mall where gravity works a little differently. This is one of them!"
        amy "Unfortunately, I’m the only of us with a membership. So you won’t be able to see everything upside down until you decide to register."
        s "How much does registration cost?"
        amy "It’s totally free! You just need to pledge to live here and donate your blood once a year. But you get juice and cookies and stuff so it’s not really any trouble at all."
        amy "Oh, and you see that pool behind me?"
        s "It’s kind of hard not to. It's taking up the majority of the room."
        amy "It’s {i}heated.{/i}"
        s "Woooooow."
        amy "Yeah. They keep it at the same temperature of a Starbucks kids’ hot chocolate. It’s perfect for swimming, but it {i}does{/i} get a little crowded on weekends."
        amy "Next time we’re here, you should totally bring a bathing suit!"
        s "That sounds nice and all, but I’m not sure if I’m going to be coming back after today."
        amy "Really?..."
        amy "Are you...not having a good time? Because I thought this date was going really well and-"
        s "It’s not like that, Amy."
        amy "And I don’t want you to hate me! I’ve been waiting so long to see you and if you don’t enjoy this, it means all those years of looking for you must have meant nothing! It means it was all for nothing!"
        s "Amy-"
        amy "Nothing! There is nothing! There is nothing! Nothing! Nothing!"
        amy "Why don’t you love me?!"
        s "Uhhhhhh..."
        amy "..."
        amy "I’m sorry."
        amy "I forgot to eat breakfast this morning."

        $ gpmh = True

    $ renpy.block_rollback()

    menu:
        "go up":
            jump gpmj
        "go right":
            jump gpmn
        "go back":
            jump gpmd

    $ renpy.block_rollback()

label gpmi:
    if gpmi == True:
        scene gpmi1 with dissolve
        s "Hmm..."

        scene gpmi2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmi1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmi2 with dissolve2

        amy "..."
        s "..."
        amy "..."
        s "Amy? Is everything okay?"
        amy "Yeah! I just..."
        amy "I can’t help but feel a little embarrassed around you. That’s all."
        s "There’s nothing to be embarrassed about. I’m the same as you — made of meat and full of blood."

        scene gpmi3
        with dissolve

        amy "I know, I know...But you’re just so cool."
        amy "I’ve always wanted to go on a date with somebody like you. And being able to walk around my favorite place in the world with you like this is..."
        amy "Well..."

        scene gpmi4
        with dissolve

        amy "It makes me really happy."
        amy "So happy that the tiny hairs on my arms are starting to stand up and cut through this shirt I got from the H&M in the north wing."
        amy "So happy that, for the first time in thousands of years, I can feel things...{i}happening{/i} to me that haven’t happened in..."
        amy "Well, a really long time. And I just don’t want this day to ever come to an end."
        s "Well, at this rate, you might be in luck. I have no idea where I’m going and feel like I’ve been in here forever."

        scene gpmi3
        with dissolve

        amy "The saddest part is that, for me...it only feels like it’s been a few minutes."
        s "..."
        amy "..."
        amy "Please stay, Akira."
        amy "We can be happy here."
        amy "If nowhere else will let that happen for us, why not take a chance and...start over {i}now?{/i}"
        amy "Why not stay in this mall with me for the rest of forever?"
        s "I can’t, Ami."

        scene gpmi4
        with dissolve

        amy "{i}Amy.{/i} And you {i}can.{/i}"
        amy "Just save the game."
        amy "Save the game and stay here so the world will stop moving and we can be together forever."
        amy "I know that we’ve only just met, but I feel like I’ve known you forever and...and I can’t let this chance get away!"
        amy "Save the game, Akira! Save the game and come visit me every single night! I’ll look forward to it! I’ll never stop looking forward to it!"
        amy "And if we run out of things to say, I’ll...I’ll think up new ones! I’ll keep adding new places for us to explore and things to talk about because I..."
        amy "I love you."
        amy "And I am finally happy."
        s "..."
        amy "..."
        amy "I will always be here."

        $ gpmi = True

    $ renpy.block_rollback()

    menu:
        "go right":
            jump gpmf
        "go left":
            jump gpmq
        "go back":
            jump gpmg

    $ renpy.block_rollback()

label gpmj:
    if gpmj == True:
        scene gpmj1 with dissolve
        s "Hmm..."

        scene gpmj2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmj1 with dissolve2
        $ renpy.pause(2, hard=True)

        s "Where are we now?"

        scene gpmj2 with dissolve2

        amy "Hmm...I think this is the entrance to the subway."
        s "I know Subway. Eat fresh."
        amy "Not {i}that{/i} Subway, silly. I mean an actual subway. You know, like with trains and stuff."
        s "In the mall? Why is there a subway in the mall?"
        amy "This isn’t just any mall! It’s the greatest mall in the world! Like, if what I’ve heard is correct, it’s even bigger than the state of Rhode Island. And I’m pretty sure that’s kind of impressive."
        amy "Having a subway to move between different wings is essential to all of the people who live here since most of the housing is over in the south wing."
        amy "Personally, I don’t have much use for it since I enjoy walking through the mall so much. And everybody here knows me, so nobody will get mad if I take a nap on a bench or something."
        s "You really love this mall, huh?"
        amy "It’s the only place where I’ve ever felt like I belong."
        amy "Before I came here, the world I was stuck in was so..."
        amy "Well, let’s just say I didn’t really fit in with anybody. And my idea of what a happy life should be was way different from what anyone {i}else{/i} thought."
        amy "I’m glad things ended up like this, though. Because even if most of my memories from those days are gone, the ones that are still kinda stuck in my head help me realize that..."
        amy "Well, something like this is what’s best for me."
        s "..."
        amy "And having you here only makes that better."
        s "..."
        amy "..."
        amy "A-Anyway! Sorry for saying all that embarrassing stuff. We can..."
        amy "We can go now. There’s not much else over here."

        $ gpmj = True

    $ renpy.block_rollback()

    menu:
        "go sideways":
            jump gpmd
        "go diagonally":
            jump gpms
        "go back":
            jump gpmh

    $ renpy.block_rollback()

label gpmk:
    if gpmk == True:
        scene gpmk1 with dissolve
        s "Hmm..."

        scene gpmk2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmk1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmk2 with dissolve2

        amy "Shh...You have to be really quiet over here."
        s "Really? How come?"
        amy "Well...you don’t {i}have{/i} to, technically. I just have some reeeeeeaaaaally overdue VHS tapes from the rental store over there and I don’t want them to see me."
        s "Why not just return them?"
        amy "Obviously because I’m still using them. Do you have any idea how hard it is to get a copy of “Endless White Noise” nowadays? If I return {i}my{/i} copy and it ends up in the wrong hands?...Ugh. Don’t even."
        s "What is “Endless White Noise?”"
        amy "It’s a tape of endless white noise. It helps me fall asleep and makes my stomach stop hurting whenever it gets upset."
        s "Well, it’s not {i}endless,{/i} right? If it’s on a VHS tape, it would need to be, like...rewound and stuff."
        amy "You’d think so, but this tape is special."
        amy "The film is made from the stomach lining of a beluga whale. And the guy at the store told me that it’s the whale's memories that are making the noise and not any actual, like...filmmaking or whatever."
        s "Why would a whale’s memories be stored in its stomach?"
        amy "Because whales consume the memories of all the fish they swallow."
        s "What?"
        amy "Yeah. You didn’t know that? There’s a library around the corner if you want to research it. I just can’t go in there either since I have a few overdue picture books."
        s "Do you just not understand the concept of renting or something?"
        amy "Teehee! I guess not!"

        $ gpmk = True

    $ renpy.block_rollback()

    menu:
        "go left":
            jump gpme
        "jump":
            jump gpml
        "go back":
            jump gpmf

    $ renpy.block_rollback()

label gpml:
    if gpml == True:
        scene gpml1 with dissolve
        s "Hmm..."

        scene gpml2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpml1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpml2 with dissolve2

        amy "Watch your step. If you cut your feet on broken glass, they could get infected. Then, you’ll have to go all the way over to the medical ward. And they pretty much always have really long lines."
        s "Thanks for looking out for me, Amy. I don’t know how to do that thing you’re doing, though. So I’ll just stand still for now."
        amy "Hahah! I was like that once upon a time as well."
        amy "Wall-walking is a skill only those who fully devote themselves to the mall can learn."
        s "Well, I’m very impressed by your unwavering devotion."
        amy "Thanks!"
        amy "You know, you should devote yourself to the mall as well, Akira. There really aren’t any downsides to it."
        amy "Plus, if there’s something in particular you’re looking for, it’ll only be a hop, skip, and a jump away!"
        s "That sounds nice and all, I’m just not sure if this place is for me just yet."
        amy "Hmm...Well, what do you think would make it better?"
        s "If all my friends were here..."
        amy "Yeah...I can see how not being able to communicate with the people you love could be a real bummer."
        amy "But, on the bright side, you have me! And I won’t leave your side {i}at all{/i} while you’re here!"
        s "Not even when I go to the bathroom?"
        amy "Not even when you go to the bathroom."
        amy "But it’s for your own good. Because I don’t want you getting lost and stuff."
        s "You’re lying to me, aren’t you?"
        amy "I might be lying to you."

        $ gpml = True

    $ renpy.block_rollback()

    menu:
        "spin":
            jump gpmr
        "go forward":
            jump gpmm
        "go back":
            jump gpmk

    $ renpy.block_rollback()

label gpmm:
    if persistent.alexisisreal == True and not _in_replay:
        jump alexisevent

    if gpmm == True:
        scene gpmm1 with dissolve
        s "Hmm..."

        scene gpmm2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmm1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmm2 with dissolve2

        amy "Oooh! Great idea, Akira! I was just getting hungry too."
        s "Where are we now?"
        amy "Taco Bell."
        s "Oh."
        s "Oh, okay."

        scene gpmm3
        with dissolve

        amy "Oh man. I’m so excited. I heard that if you eat enough tacos, they’ll let you ring the bell. And if you ring it loud enough, you’ll wake up the giant frog in the center of the mall!"
        s "The {i}what?{/i}"
        amy "The giant frog in the center of the mall. Do they not have one where you come from?"
        s "No?..."
        amy "Oh!"

        scene gpmm4
        with dissolve

        amy "Well, I guess that probably sounds pretty worrying then, huh?"
        amy "There’s nothing to fear, though. He’s harmless. And even when he wakes up, he kind of just looks around for a little while before spitting out an egg and then going back to sleep."
        amy "You know, just normal frog stuff."
        s "I suddenly don’t think I’m in the mood for tacos anymore."
        amy "Don’t be such a baby, Sensei! You’ll be fine!"
        s "..."
        amy "..."
        s "What did you just-"

        scene gpmm3
        with dissolve

        amy "C-Can you just sit down already so we can eat our tacos?!"

        $ gpmm = True

    $ renpy.block_rollback()

    menu:
        "go forward":
            jump gpma
        "spin":
            jump gpmt
        "go back":
            jump gpml

    $ renpy.block_rollback()

label gpmn:
    if gpmn == True:
        scene gpmn1 with dissolve
        s "Hmm..."

        scene gpmn2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmn1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmn2 with dissolve2

        amy "Akira, Akira! Let’s play!"
        s "I think we’re a little too old to play in that weird rectangle, Amy."
        amy "You’re never too old for rectangles! That’s what my mom always says."
        s "Wow, your mom sounds like a real {i}square.{/i}"
        amy "..."
        s "..."
        amy "..."
        s "..."
        amy "..."
        s "..."
        amy "..."
        s "..."

        scene gpmn3 with dissolve

        amy "Come on! Over here! We can do stuff on this...bridge thingy!"
        s "What kind of {i}stuff{/i} can we possibly do on that “bridge thingy?” It can barely even fit you and you’re only half my size."
        amy "We can pretend we’re hermit crabs on the hunt for new shells! Or sing the hot dog song together!"
        s "What is the hot dog song?"
        amy "{i}Hot dogs, not dogs ~ not made of dogs! Piping ~ hot and ~  not made of dogs!{/i}"
        s "Not gonna lie, the insistence that they’re not made of dogs is making me very suspicious."
        amy "Just come over and play with me already!"
        s "No. In fact, I think you should come down before you get hurt. You’re going to fall."
        amy "I’m not going to fall! I do this all the time!"
        s "Amy, I am {i}telling{/i} you — you are going to fall."
        amy "Lies and slander! Just look at how nimble I am!"

        play sound "tackle.mp3"
        scene gpmn4 with hpunch

        amy "Ouch."
        amy "I fell."
        s "This is what you get for trying to play without legs."

        $ gpmn = True

    $ renpy.block_rollback()

    menu:
        "go left":
            jump gpmc
        "go right":
            jump gpmo
        "go back":
            jump gpmm

    $ renpy.block_rollback()

label gpmo:
    if gpmo == True:
        scene gpmo1 with dissolve
        s "Hmm..."

        scene gpmo2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmo1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmo2 with dissolve2

        amy "Hey, Akira...what kind of girls do you like?"
        s "Is that even something you’re supposed to be asking on a date?"
        amy "Sure! I need to know which ones to avoid and when I should grab your arm and run in the opposite direction."
        s "You’re starting to sound a lot like some other girl I know."
        amy "Oh yeah? Is {i}she{/i} your type?"
        s "She is...definitely {i}a{/i} type."
        amy "{i}A{/i} type? What does that mean?"
        s "Just that she’s very unique."
        amy "Well, uniqueness is a great quality in a girl! It’s great in guys too! And a huge part of why I like you so much!"
        s "What makes me so different from everyone else you know?"
        amy "Well, to begin with, all of the people here are invisible from behind."
        s "What?"
        amy "Yeah. You can only see us head-on since that’s all that was designed."
        amy "I’m not sure how it is where you’re from, but that’s just par for the course here."
        s "That makes certain...{i}positions{/i} sound actively unfun."

        scene gpmo3 with hpunch

        amy "Ewwww, gross! Don’t be such a perv while we’re in the east wing! That’s what the north side is for."
        s "What’s this side for then? What’s there to do where we are now?"
        amy "Luxury shopping mostly. If you’re in the market for a Rolex or something like that, you can head over to the left. And the Tesla shop is over to the right, but that’s full of hipsters and it makes me feel weird."
        s "And what if I’m not in the market for either?"
        amy "Then you have no other choice but to simply enjoy your time with me!"
        s "Ooooooh, I wonder what’s over there."
        amy "Hey! Akira! Get back here!"

        $ gpmo = True

    $ renpy.block_rollback()

    menu:
        "go forward":
            jump gpmk
        "jump":
            jump gpmb
        "go back":
            jump gpmn

    $ renpy.block_rollback()

label gpmp:
    if gpmp == True:
        scene gpmp1 with dissolve
        s "Hmm..."

        scene gpmp2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmp1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmp2 with dissolve2

        amy "Echo!...Echo!...Echo!..."
        s "It’s not an echo if you just keep yelling “echo” you know."
        amy "I know...I just always expect the acoustics to be a little better in here with how empty this part of the mall is."
        s "And...what part is that exactly?"
        amy "This is how you get to the parking garage. And it’s obviously empty since nobody is able to leave and there’s no reason to {i}go{/i} to the garage."
        s "Doesn’t the existence of parking garages imply people {i}were{/i} able to leave at some point, though?"
        amy "Yes, because they were. It was only after the air became contaminated that we were forced to keep ourselves in here. But this mall was made with the possibility of that in mind to begin with."
        s "The people who built the mall knew something like that would happen?"
        amy "Yes! But you’re wrong about one thing — it wasn’t people who built the mall. It was the mall itself."
        s "What?"
        amy "Mhm! Crazy, right? This mall is technically a living thing. It’s still growing and expanding and sucking in people like you who aren’t {i}supposed{/i} to be here, but {i}want{/i} to be here."
        amy "All of us are simply living inside of it. And for that, we must pay our thanks as we wander through what would probably be its organs! Kinda gross when you think about it like that though, huh?"
        s "A little bit, yeah..."

        $ gpmp = True

    $ renpy.block_rollback()

    menu:
        "go forward":
            jump gpmq
        "go right":
            jump gpms
        "go back":
            jump gpmc

    $ renpy.block_rollback()

label gpmq:
    if gpmq == True:
        scene gpmq1 with dissolve
        s "Hmm..."

        scene gpmq2 with dissolve

        amy "What’s wrong, Akira? Are you finally ready to go to Toys “R” Us?"
        s "No. I just made a wrong turn."
        amy "Ugh. Darn it."

    else:
        scene gpmq1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmq2 with dissolve2

        amy "AAAAAAHHHHHHHH!!!!!!!!!"
        s "What? What’s wrong? Why are you yelling?"
        amy "Look, Akira! A Toys “R” Us!"
        amy "I thought they were all gone!"
        s "Why do they put the “R” in quotation marks? I don’t get it."
        amy "They also put it backwards, but...is that really what you’re concerned about? You should be freaking out just as much as me right now! We might have stumbled upon something amazing!"
        s "You really didn’t know it was here? I thought you knew this place like the back of your hand."
        amy "I don’t have hands. We already went over this."
        s "Oh, right. Sorry."
        amy "Hahah! It’s fine, don’t worry about it."
        amy "And yes, I do know this place very well. But that doesn’t mean there aren’t still new things popping up every now and then! So whenever I find a place I haven’t seen before, I can’t help but get excited."
        s "I know what you mean. My town is a little like that too."
        amy "Really?"
        s "Yeah. I’m not sure if we have one of...whatever this place is, though."
        amy "How about I {i}show{/i} you what it is?!"

        scene gpmq3 with dissolve

        amy "Come on, Akira! Let’s go play!"
        s "Maybe a little later, Amy. I still want to look around."

        scene gpmq2 with dissolve

        amy "Grr...fine. But you’re definitely taking me soon, okay?"

        $ gpmq = True

    $ renpy.block_rollback()

    menu:
        "gyrate":
            jump gpmj
        "go left":
            jump gpmr
        "go back":
            jump gpmm

    $ renpy.block_rollback()

label gpmr:
    if gpmr == True:
        scene gpmr1 with dissolve
        s "Hmm..."

        scene gpmr2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmr1 with dissolve2
        $ renpy.pause(5, hard=True)
        scene gpmr2 with hpunch

        amy "Boo!"
        s "Jesus. Why would you do that?"

        scene gpmr3
        with dissolve

        amy "Hahahahah! You should have seen the look on your face!"
        s "Do you scare all of your dates? Or just me?"
        amy "You make it sound like I go on a lot of dates when that’s not the case at all."
        amy "This is actually the first one I’ve been on since you ripped number 17 out of my mouth."
        s "Really?"
        amy "Mhm! I’ve been so focused on finding you that I kind of lost interest in dating altogether. It’s not a big deal, though. It’s not like I’m totally alone here or anything."
        s "Do you have friends?"
        amy "I used to. Now, my only real companions are a group of pigeons that gather near the food court looking for scraps. I think they’re starting to believe I’m one of them."
        amy "Do I give off pigeon vibes, Akira? Because I didn’t think I did, but it’s hard to ever really tell what you’re looking at when you glance into the mirror. It’s better to rely on others for that sort of thing."
        s "You give off normal girl vibes to me. But I’m not very experienced when it comes to vibes, so take that with a grain of salt."
        amy "Hahah! Will do. You wanna know what kind of vibes {i}you{/i} give off, though?"
        s "Sure. Hit me."
        amy "{i}Dad{/i} vibes."
        s "I can’t tell if that’s an insult or a compliment."
        amy "Mmm...both!"
        amy "I like being with you."
        amy "And...umm..."
        amy "I’m not really...{i}opposed{/i} to this leading to something more one day..."

        $ gpmr = True

    $ renpy.block_rollback()

    menu:
        "go right":
            jump gpmi
        "go left":
            jump gpmh
        "go back":
            jump gpmq

    $ renpy.block_rollback()

label gpms:
    if gpms == True:
        scene gpms1 with dissolve
        s "Hmm..."

        scene gpms2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpms1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpms3 with dissolve2

        amy "Why’d you wanna come down here? All the fun stuff is back upstairs."
        s "I didn’t mean to. It just kind of happened on account of me having literally no idea where I am."

        scene gpms2 with dissolve

        amy "Well, {i}I{/i} say we head back upstairs because we’re not supposed to be in here. Plus, it creeps me the heck out."
        amy "Like, you know that weird feeling you get in your stomach when you go somewhere you’re not supposed to be? That’s pretty much all I feel right now."

        scene gpms4 with dissolve

        amy "And it’s definitely not because I’m hiding what’s in here from you. Got it?"
        s "Got it. But what is this place? The...basement or something?"

        scene gpms5
        with dissolve

        amy "It’s nothing! Don’t worry about it!"
        s "Amy-"
        amy "I’m going upstairs now! Bye!"

        scene gpms1
        with dissolve

        s "Amy, wait-"
        s "..."
        s "..."
        s "..."

        $ gpms = True

    $ renpy.block_rollback()

    menu:
        "jump":
            jump gpmg
        "backflip":
            jump gpmt
        "go forward":
            jump gpmp
        "go back":
            jump gpmr

    $ renpy.block_rollback()

label gpmt:
    if gpmt == True:
        scene gpmt1 with dissolve
        s "Hmm..."

        scene gpmt2 with dissolve

        amy "What’s wrong, Akira? We’ve already been over here."
        amy "You’re not lost already, are you?"
        s "Of course not. I know exactly what I’m doing."

    else:
        scene gpmt1 with dissolve2
        $ renpy.pause(2, hard=True)
        scene gpmt2 with dissolve2

        amy "Wow...it’s so colorful in here. I wonder if it’s like a daycare or something?"
        s "Did you ever have to go to daycare, Amy?"
        amy "Mmm...I can’t really remember."
        amy "Some weird stuff happened to my memories before I wound up in the mall, so there’s a lot of just, uhh...I guess you could call it blank space in there?"
        amy "Basically, it feels like everything is only half complete. And there’s stuff that makes me {i}feel{/i} like I’m remembering sometimes-"
        amy "But then something fun or interesting or dramatic happens and I just go back to being complacently oblivious!"
        s "I know how you feel. Just without the “complacent” part, I guess."
        amy "Are you not happy with where you’re from, Akira? Because if not, you should just stay here with me! I’m very happy! Just imagine how happy I’d be with {i}you!{/i}"
        s "It’s not that I’m unhappy. It’s more that I’m just...nothing."
        amy "Well you’re something to {i}me,{/i} Akira. And even if the rest of the world stops caring about you, {i}that{/i} won’t change."

        scene gpmt3 with dissolve

        amy "What I’ve learned through my time here is that life is what you make of it — so it’s best to make it fun!"
        amy "Whether that means indulging in your hobbies or interests...or even just teaching yourself not to care what other people say about you! There’s always {i}something{/i} you can do!"
        s "Thanks, Amy. That means a lot."
        amy "Don’t mention it. A bit of helpful advice is the least I can do after all you’ve done for me."
        s "Are you talking about your teeth again?"
        amy "No."
        s "Then what-"

        scene gpmt2 with dissolve

        amy "Come on! Let’s see what we can find next!"

        $ gpmt = True

    $ renpy.block_rollback()

    menu:
        "spin":
            jump gpmn
        "go left":
            jump gpmo
        "go sideways":
            jump gpmh
        "go back":
            jump gpma

    $ renpy.block_rollback()

label gpmending:
    s "..."
    amy "..."
    amy "Akira?"
    s "I think I’ve seen enough, Amy."
    amy "Enough?..."
    amy "No..."
    amy "No! No, you’ve barely seen anything! We still have lots left to explore!"
    amy "You...You can’t leave yet! You can’t leave at all! You haven’t had enough fun! You have to stay until you’ve done everything there is to do! You need to have more fun!"
    s "I’ve had tons of fun with you. I just can’t stay here. There’s somewhere I need to get back to."
    amy "Somewhere better than this?! Because nowhere is better than this! We have everything and more! And...And {i}I’m{/i} here!"
    amy "Are you just going to keep me waiting again?! For how long?! When is the next time I’ll see you?! Will I {i}ever{/i} see you?! Am I just supposed to move on?!"
    amy "This world is for us! Not {i}me!{/i} This isn’t right! None of it is right!"
    s "Then...maybe I’ll find my way back somehow. I don’t know. But I didn’t mean to end up here today, so who’s to say the same thing won’t happen again?"
    amy "..."
    s "Is that not a satisfying answer?"
    amy "I..."
    amy "I don’t think there can be a satisfying answer."
    amy "I thought you’d want to stay after seeing how much there is to love here, but..."
    amy "I guess it’s not enough."
    amy "And I guess..."
    amy "I guess {i}I’m{/i} not enough..."
    s "..."
    amy "..."
    s "..."
    amy "..."
    amy "Akira..."
    s "Yeah?"
    amy "If..."
    amy "If you’re not going to stay here...and live in the world that {i}I{/i} love..."
    amy "Will you promise me you’ll do your best to love {i}yours?{/i}"
    amy "Because if...if I know you’re trying to be happy over there..."
    amy "I think I can try to be a little happier over here."
    s "..."
    amy "..."
    s "Okay."
    amy "Thank you..."
    amy "And please...{i}please{/i} come visit me again. Even if it’s only for a little while."
    s "How about this...{i}you{/i} show me the way out and {i}I’ll{/i} try to come back as soon as possible. Does that work?"
    amy "But there is no way out."
    s "There has to be a way out."

    scene gpma4 with dissolve

    amy "There really isn’t. All of the old exits are impossible to get through and you wouldn’t be able to survive outside anyway."
    s "I’m not trying to go {i}out{/i}side. I’m trying to go back to {i}my{/i} side."
    amy "But I have no idea where that side {i}is.{/i} So how am I supposed to help you?"
    s "You really don’t know of {i}any{/i} way to leave the mall? Any at all?"
    amy "Just those temporal rifts, but...I don’t want you to get covered in pee."
    s "I don’t want that either."
    amy "..."
    s "..."
    amy "There’s...the hole?"
    s "You mean the one you didn’t push your ex-boyfriend into?"
    amy "Right. The one I didn’t push my ex-boyfriend into."
    s "That might-"
    amy "Seriously. It wasn’t me."
    s "..."
    s "That might be our best course of action then."
    amy "How is falling for the rest of forever the best course of action?"
    s "Well...it could be like one of those dreams, right? Where you’re just falling and...then you wake up?"
    amy "Sure. Or it could be like, you know, just literally falling. And then you don’t wake up. You just fall."
    s "Trust me. I’ve got a good feeling about this."
    amy "Well I sure as heck don’t, but...you know. Gender roles and all. I have to listen to you."
    s "Then please show me the way because there is absolutely no chance I’m getting there on my own."
    amy "Heheh...yeah. This place takes a little getting used to, doesn’t it?"
    amy "To get to the abyss, we need to head back to 01110100."
    amy "I can take you there...I just have one more thing to ask in exchange for it."
    s "And what’s that?"
    amy "That you hold my hand along the way..."
    s "..."
    amy "..."
    s "..."
    amy "..."
    s "Amy, you don’t have hands."
    amy "Crap."
    amy "You’re right."
    amy "I totally forgot."

    scene black
    with dissolve2
    stop music fadeout 10.0

    amy "I guess just follow me then. It’s not like I can ask for a high five or anything either."
    s "Maybe a hug or something?"
    amy "Please don’t hug me"
    amy "All that will do is make me even more upset that you’re leaving me behind."

    "........."
    "......"
    "..."

    scene gpms1 with dissolve2

    amy "Akira...are you sure you want to do this? Because it still sounds really risky to me."
    s "If it’s the only way for me to actually get out of this mall...yeah. I’m sure."
    amy "Okay, but...the room it’s in is kind of weird."
    s "This whole place is kind of weird. I’m sure that whatever is in there won’t be much different."
    amy "Uhhhhh...okay. I’ll trust your judgement on this, I guess."
    amy "It’s through the second door on your right. But again, it’s weird."

    scene black
    with dissolve

    s "Thanks, Amy. I appreciate-"

    scene gpmend with dissolve
    play music "firstsecondmall.mp3"

    s "Oh."
    amy "Yeah."
    s "..."
    amy "..."
    s "You know, maybe getting covered in piss isn’t the worst-"

    scene black
    play sound "tackle.mp3"

    s "Ah."
    amy "{i}It wasn’t me!{/i}"

    "The voice of a new friend fades away as I descend."

    amy "{size=-15}{i}Seriously! I didn’t do it!{/i}{/size}"
    stop music fadeout 5.0
    "........."
    "........"
    "......."
    "......"
    "....."
    "...."
    "..."
    ".."
    "."
    play sound "pop.mp3"
    play music "mall.mp3"
    scene amy1

    a "Sensei. Hey. Snap out of it."
    a "What’s going on? I came here to buy new pajamas and the first thing I see is you just standing in the middle  of the mall with your eyes glossed over."
    a "Are you okay? Do you need me to take you home? Do you-"

    stop music
    scene black
    play sound "tackle.mp3"

    a "Ah-"

    scene amy2
    with dissolve3

    a "..."
    s "..."

    scene amy3
    with dissolve2

    a "..."
    s "..."
    a "Let’s get you home."

    scene black
    with dissolve2

    $ renpy.suspend_rollback(False)
    $ renpy.end_replay()
    $ letsgoexploring = False
    $ amyevent = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label tsuneyocallmorninggen:
    scene tsuneyomorningcallgen
    with dissolve
    play music "summerwind.mp3"

    "I give Tsuneyo a call just before she sets out for morning practice and wind up heading all the way across town to meet up with her so she doesn't have to walk alone."
    "It's utterly horrible time management as her house is extremely far from me and she is now very likely going to be late, but hey. At least we're together."
    "The morning proceeds as normal, with cryptic dialogue and endless references to noodles, but the weather is nice enough to distract me from how {i}mostly{/i} unwanted I am."
    "There are several moments that make me think the opposite, but they're gone so quickly that I'm never able to latch on to them."

    scene black
    with dissolve

    "I think back on our trip to the amusement park and how that day was so much different from every other one we've shared."
    "I'm not sure how we'll ever reach that level again if she's going to remain as aloof and dismissive as this, but it doesn't mean I can't hope."
    "Deep down in the sodium-packed shell of hers, I know there is a girl who is dying to be both understood and accepted."
    "And while I can't make any promises in regard to that first part...the second is something I can't imagine I'll ever have a problem with."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo's affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label tsuneyocallafternoongen:
    scene tsuneyonooncallgen
    with dissolve
    play music "summerwind.mp3"

    "I decide to spend the afternoon with Tsuneyo in the second half of town after she tells me she has time to kill before the restaurant opens for dinner."
    "Well, to be honest, it was less like she was telling me she had time to kill and more like {i}me{/i} telling {i}her{/i} that she doesn't need to open so early."
    "It's for this exact reason, however, that I'm so surprised when she agrees when I was fully prepared to just sit inside of a ramen shop for an hour or two."
    "Thankfully, that's not the case and the two of us take a walk through her neighborhood, finally coming to a stop along the riverbank so we can watch the sunset."

    scene black
    with dissolve

    "The only thing is, neither one of us seems to care much about the sunset and we're only looking up at it due to aesthetic obligation."
    "The next ten minutes are silent, interrupted only by the sounds of cicadas as they remind us whose domain this is."
    "I think to myself that no matter how strong or how large we become, we will always be outnumbered- and this fills me a sense of emptiness I have a hard time replicating through text."
    "What I'm trying to say is I am alone."
    "We both are."
    "And so we head our separate ways as whatever this was just...didn't work."

    stop music fadeout 5.0

    "{i}Tsuneyo's affection does not increase!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight
