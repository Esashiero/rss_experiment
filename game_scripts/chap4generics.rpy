label yumispringstreetsgen:
    scene yumispringstreetsgen
    with fade
    play music "yumiska.mp3"

    "Like clockwork, I wind up bumping into Yumi after just a few minutes of wandering the streets."
    "And while I’d like to say that I think it’s good that she isn’t intentionally trying to avoid me anymore, I can not. For the second she sees me approaching, she gets up to walk away."
    "Somehow or another, though, I wind up convincing her to stick around and the two of us proceed to make scattered pointless conversation that, to anyone else, would make it seem like we dislike each other."
    "And I think we might."
    "But I also think that's what keeps bringing us together since it makes it easier to forget about the things we hate about ourselves."
    "The truth is that things might stay this way forever. That we not only might never come to rely on each other, but that we might never even {i}want{/i} to see one another."
    "Maybe that's enough. Maybe it's not. I don't know."
    "But what I do know is that if she keeps getting caught in the webs spun by my half-hearted pleas for her to stay, she'll be too exhausted to try and wiggle herself out soon enough."

    scene black
    with dissolve

    "All I have to do is wait until I can devour her."
    "Or, better yet-"
    "Wait for her to {i}want{/i} me to."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label yumispringnightgen:
    scene yumispringnightgen
    with fade
    play music "blueair.mp3"

    "Yumi, for reasons beyond my comprehension, answers my call and agrees to meet up with me in the old district for an hour or two."
    "Considering that I’ll be with her for about the same amount of time as my walk to actually {i}get{/i} there, I don’t see it as a solid investment of time, but it’s not like I have anything else going on tonight."
    "Once I arrive, the two of us do laps around the neighborhood surrounding Chika’s house."
    "But unlike the way things used to be, we don't try to avoid it anymore."
    "At several points, I can even spot her slow down as we pass by the Chosokabes' balcony. I spot the way her eyes dart up to the glass and the way she holds her breath, like she's {i}excited{/i} to be caught."
    "That might just be the way I want to see things, though. How I want them to be."
    "For the only thing more tantalizing than infidelity alone is the prospect of it being unearthed."

    scene black
    with dissolve

    "So I bury myself in the idea of a night inside a Yakuza princess."
    "And she buries {i}herself{/i} in what I can only imagine is a lifetime's worth of internal conflict of whether what {i}she{/i} wants is best for everyone else."
    "It's not."
    "But I will push that reasoning aside for now as, in this moment, my biggest concern is winning over the girl I came here to see."
    "The one who does not yet rely on me."
    "The one who wants to."

    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chikaspringmaidgen:
    scene chikaspringmaidgen
    with fade
    play music "maidcafe.mp3"

    "I make my way over to the maid cafe to hang out with Chika and then probably have sex with her because she essentially lets me do that whenever I want now."
    "I'm not used to her working here yet. And I'm not sure if I'll ever {i}get{/i} used to it as my first instinct when calling her is still to head over toward our old bench at the mall."
    "I have to take a different bus now. It's a shorter ride and, by all means, it should be a welcome change for me."
    "But something just feels wrong about all of it."
    "Something feels wrong about her new job and her new hair and the new bus and the new everything and I just want my old new-life back."
    "I have no reason to go to the mall anymore."

    scene black
    with dissolve

    "Chika lets me use her employee discount because, as she puts it, I'm {i}family.{/i}"
    "I throw up in my mouth at the idea of ever accepting this but the taste doesn't mix with the eggs."
    "And I finish my meal regardless because it's the right thing to do."
    "And because if I make myself sick, I might want to fuck her less."

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label chikaspringnightgen:
    scene chikaspringnightgen
    with fade
    play music "justlights.mp3"

    "I make my way over to Chika’s apartment to spend the night with her while Yumi and Chinami sit in the living room reading manga together."
    "Neither of them pay any attention to me, so I’m free to spend the night out on the balcony with one of my several {i}girlfriends{/i} as tonight's selection locks her eyes on mine."
    "I can't help but wonder what she's thinking, but I neglect to ask because I don't want her answer to penetrate me the same way I do her on a routine basis."
    "It's both interesting and unfortunate how easily I crack now. But I guess it's easier for hairline fractures to form once the first one has already begun to spread."
    "I crumble and ask her anyway. I ask her why she stares at me the way she does. And what she tells me is this-"
    "{i}I just want to.{/i}"
    "She just wants to."
    "What a terrible waste of time."

    scene black
    with dissolve

    "One more crack forms and I remind myself of thoughts I've had on other balconies."
    "Thoughts of when we wanted one another, and when we could do that without really caring about how or why."
    "But now, I think too much."
    "And all those thoughts revolve around self-destructing and what it would do to this makeshift family of ours."
    "Regretfully, I don't think I'd be able to crawl away anymore."

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label ayanespringmorninggen:
    scene ayanespringmorninggen
    with fade
    play music "acoustic.mp3"

    "I call Ayane in an attempt to invite her out and distract myself for a little while and, within an hour, she's here."

    if amiblock == False:
        "Ami's at work right now and neither one of us has eaten yet, so she takes it upon herself to fill the tiny shoes of my niece by making us breakfast."
    else:
        "Ami's dying in bed right now and none of us have eaten yet, so Ayane takes it upon herself to make the three of us breakfast."

    "There isn't much conversation. In fact, there isn't much {i}anything{/i} apart from silence and lingering, unspoken regret."
    "We watch a pot full of water begin to boil."
    "At one point, it almost overflows. But Ayane catches herself drifting and turns the heat off before a mess is made."
    "It's clear that Ami's shoes are not just too small for her, but a different style altogether."
    "She doesn't fit in any way. Yet she tries, albeit sparingly, to make it look as if they do."

    scene black
    with dissolve

    "Then she tries, tries, and tries again until, finally, something edible is laid out before us."
    "We eat in silence, just as we cooked."
    "And while everything tastes perfectly normal, I struggle to stomach any of it."
    "My appetite isn't what it used to be."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label ayanespringnightgen:
    scene ayanespringnightgen
    with fade
    play music "meanttobe.mp3"

    if amiblock == False:
        "I call Ayane and wind up heading over to the dorms to hang out with her since Ami is at the house tonight and doesn’t take kindly to the idea of Ayane getting “Sensei time” without her."
    else:
        "I call Ayane and wind up heading over to the dorms to hang out with her since Ami is..."
        "Yeah."

    "Instead of making plans to do anything, though, we wind up talking outside of the dorm building for what feels like an eternity, but is really only an hour or two."
    "There's been a lot of that with us lately. A lot of conversations that don't amount to anything but feel like they need to happen so we can maintain some sort of status quo."
    "We retreat to a bench and I ask her to tell me about her day, which she does. And she spares no detail at that. But none of the information really sticks."
    "It's funny, actually. I feel like I used to be so good at listening, even if it wasn't in the way people wanted me to."
    "But now, it's like I can barely even remember when I got out of bed in the morning."
    "It's like all of my effort goes to thinking of the next time I'll be able to get some sleep instead."
    "And whether or not I'll see {i}her{/i} there when I do."

    scene black
    with dissolve

    "We retreat to a nearby park bench and Ayane beats me to the punch by falling asleep on my shoulder."
    "As I look down at her, there's a fleeting thought that she reminds of someone else- but I'm not quite sure who."

    s "..."

    "I just know that they're important."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label ayanespringpoolgen:
    scene ayanespringpoolgen
    with fade
    play music "fallishere.mp3"

    "I bump into Ayane when I make my way over to the pool."
    "I guess I use the term {i}bump{/i} lightly though, as I was kind of hoping she'd be here."
    "Talking to anyone else nowadays just feels like I'm forcing myself most of the time."
    "Things aren't perfect with Ayane and me. They haven't been since that night on the roof. But she's closer to understanding than anyone else what I'm going through."
    "And the reason for that's simple. It's because {i}she's{/i} going through it as well. And the fact that she's able to smile in spite of that makes her ten times stronger than I am."
    "I wish I could match her pace and her color and all of the things that make her who she is."
    "But a quick glance at the water and the rippled reflection of a broken man staring back at me tells me it's impossible."
    "And I decide against plaguing her smile with one that would be little more than avian mimicry."

    scene black
    with dissolve

    "She gets back into the water and speaks to me from there."
    "When she goes under, she closes her eyes."
    "And I think something like that might feel okay if I can hold it until the light is gone."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label sanaspringbargen:
    scene sanaspringbargen
    with fade
    play music "calmbar.mp3"

    "When I first started coming here, I wasn't really sure what I was doing apart from the scattered yet frequent desires to fuck a small girl who {s}has{/s} had trouble speaking."
    "Now, I know exactly why I take up residence on the very stool I speak to you from. I am here to forget."
    "It's not a unique reason by any means. In fact, I imagine it's the same reason this girl and her mother remain so dedicated to the business despite its shortcomings."
    "All of us lost someone. But it's that lingering {i}carrot-on-a-stick{/i} that maybe {i}mine{/i} will come back that makes things even worse."
    "This bar and this girl are welcome distractions. The music is soothing, the atmosphere is comforting, and the alcohol is numbing."
    "And it's even better that it's served up by someone who {s}needs{/s} wants me."

    scene black
    with dissolve

    "I used to wonder what type of person this girl would become, but I seldom imagined what I could turn her into."
    "Now, that's the first thing I think of when I look into her eyes."
    "She lets me see both of them now- like she wants me to take in more of her so that she can, in turn, fill herself with me."
    "I want to know the way her brain moves."
    "I want to know the way her blood flows."
    "I want to stain the sheets in her bedroom."

    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label makotospringporngen:
    scene makotospringporngen
    with fade
    play music "citylife.mp3"

    "I make my way over to the porn shop and, despite her new outlook on this endless timeline and the debauchery that enables us to engage in, she isn't happy to see me."
    "But that's fine, because I'm not really happy to see her either. I'm just here because I don't know what else to do with myself."
    "This shop is the perfect distraction- and its infinite sea of semen-siphoning sex tapes is precisely what I need to slip out of this slump."
    "She looks at me and asks me why I continue to torment her like this despite it not being all that tormenting at all. I can sense she's only saying it at this point."
    "I can sense the lack of sincerity in her words and the unspoken desire to reenact the most depraved articles these shelves have to offer."
    "But I feel like what she senses in me erases any possibility of those wants leaking out."

    scene black
    with dissolve

    "Makoto decides once again that it’s best for me to just leave the porn shop since we both need to wake up early and she still has work to do."
    "I don't argue, for the prospect of sleep seems all the more appealing."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label makotospringnoongen:
    scene makotospringnoongen
    with fade
    play music "love.mp3"

    "I call up Makoto and the two of us make plans to meet up in the park for a little while before she has to head back home for work."
    "When I get there, she greets me with a plastic bag full of assorted soft drinks that the two of us proceed to consume while hanging around the fountain."
    "At one point, she pulls a coin from her pocket and tosses it into the water. But when I ask her what she wished for, she just shrugs."
    "She says there isn't anything she wants. Other than for me to stop torturing her, that is. But if that was possible, I would have done it by now."
    "This compulsive behavior of mine to make her life a living hell no longer mirrors the inverse of my feelings for her. I am no child kicking sand into the eyes of another."
    "I am a man who has habitual rough sex with a girl who could go on to do great things if she could only focus on the outside world rather than what I elect to fill her with."
    "But perhaps it's for the best that she doesn't."

    scene black
    with dissolve

    "Perhaps her reluctance to omit me from her daily thought pattern helps make me human- if one could even call me that."
    "I feel like she would. But I also feel like she'd be lying."
    "And even more than that, I feel as if she may be losing touch with what exactly that means."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label mikuspringpoolgen:
    scene mikuspringpoolgen
    with fade
    play music "highspeedprinter.mp3"

    "I miss the soccer team, but I'm not sure if it's because the scent of chlorine is growing more and more sickening by the day or if I just want something to complain about."
    "The weather has been nice enough lately to warrant extended stays beneath the sun, so being trapped within these walls makes me feel as if I'm suffocating."
    "Drowning would be more apt, I suppose. But then again, I'm the one who remains dry while the girl I came to see absentmindedly kicks her legs in the water."
    "It takes her a few minutes to realize I'm here, but I make no attempt to shorten that time as I've already gotten what I came here for."
    "One whiff of chemicals that could melt my brain if I linger long enough-"
    "And an extended glance at another byproduct of my evils."

    scene black
    with dissolve

    "I wind up staring at Miku for long enough to disturb her."
    "But that’s fine, because instead of asking me to {i}stop{/i} looking at her, she just blushes and looks away, pretending to not notice."
    "I’m glad we’ve reached a point in our relationship where she is well aware of the way I look at her."
    "I’m not glad that she’s started seeing me the same."

    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label mikuspringnightgen:
    scene mikuspringnightgen
    with fade
    play music "justbehappy.mp3"

    "I call Miku and the two of us wind up making a trip to a nearby fast food restaurant so she can replenish her energy stores with what is potentially the least healthy thing you can put inside of your body."
    "But hey, if she wants to jeopardize her future self now while she is still young and able-bodied, she’s allowed to do so."
    "It's not like she's going anywhere. In fact, it's not like she {i}can{/i} go anywhere when we're all perpetually trapped in this world where good things can't exist."
    "A year ago, it would have been easy to cherish a moment like this. It would have been easy to look at this girl, only half my age, and breathe a sigh of relief as I dig into the flesh of a slaughtered animal."
    "Perhaps when we're done here, she'll take me back to her room where I can slaughter one myself."

    scene black
    with dissolve

    "We get our food and settle down at a table near the window and wind up talking about how life has changed lately."
    "For her, it’s mostly about being able to regularly cum now."
    "For me, it’s about regularly struggling to."
    "Is that the most substantial change my life has made as of late?"
    "Absolutely fucking not."
    "But it’s easier to admit that than to admit what the real one is."

    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label rinspringcafegen:
    scene rinspringcafegen
    with fade
    play music "cafe.mp3"

    "I head over to the cafe to do the same thing I always do in gulping down whatever is placed in front of me. Just now I'm subconsciously hoping it's laced with cyanide."
    "It won't be, of course. Rin still likes me for reasons beyond my comprehension."
    "But if I had to take a guess as to why, it's probably because I'm the only other flesh golem in all of Kumon-mi who likes girls as much as she does. "
    "And if it weren't for these cancerous feelings that make me want to prevent her from becoming as jaded and lost as I am, I'd probably serve as her guide in that area of impractical love."
    "I’m glad that she's single again. And I'm glad that she's been learning to gradually move on as of late."
    "But I can’t help but wish she'd be smart enough to leave me out of it."

    scene black
    with dissolve

    "A flood of customers all decide to caffeinate at the same time and I seize the opportunity to leave before I get wrapped up in any of it."
    "Rin notices me leaving and stops what she’s doing to say goodbye."
    "I pretend I don't hear her and walk back out of the cafe and into the street without checking for cars."

    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label rinspringnightgen:
    scene rinspringnightgen
    with fade
    play music "ame.mp3"

    "I call Rin and get roped into joining her at the convenience store for a late night snack because I am a pushover who never says no to attention."
    "Thanks to a raise she received following Christmas this year, she's now making a bit more money than she used to and offers to buy me a drink."
    "I think she's only offering because she can sense that something is wrong. Which means that the only course of action for me is to deny her offer and ultimately die of thirst."
    "She has trouble taking no for an answer."
    "I have trouble thinking that without wanting to throw myself at her."

    scene black
    with dissolve

    "But I manage to avoid doing that because she's my friend. Or my surrogate daughter. Or whatever she's supposed to be to me at this point."
    "The lines that draw our relationship have gone so blurry to me that I often forget what I am to her. It's fine, though, because I'm sure she'll remind me soon enough."
    "The two of us will leave this place and we'll spread apart, thinking about each other as we head in different directions."
    "But her thoughts of me will linger for longer than my thoughts of her will."
    "Not because she likes me more-"
    "But because I'm trying to protect her."

    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label futabaspringlibrarygen:
    scene futabaspringlibrarygen
    with fade
    play music "morningmoon.mp3"

    "I head over to the library to see what Futaba is doing and, like always, she’s reading. Because that's what you do in a library."
    "Unless you're me. If you're me, you suck the life force out of everyone you encounter and convert it into sexual energy which you then inject back into someone via penetrative sex."
    "And there is a high likelihood that penetrative sex will occur today because Futaba hates herself even more than I do. Which is awesome because it means I finally get a win."
    "Her attention switches to me as she believes I'm more interesting than any sort of book she could ever pick up, but she quickly finds out that I have the depth of a half-written synopsis."
    "Frankly, I'm not sure how it took her this long to realize that. So I'll just go ahead and assume she was distracted by my dick in her mouth."

    scene black
    with dissolve

    "I wind up asking Futaba about how her journey as a writer is going because it {i}is{/i} something I'm genuinely interested in. And I hope she makes it further than I ever did."
    "I just hope she understands that proceeding down this path means she'll have to spend more time with her feelings. And if her feelings are anything like mine, that's dangerous."
    "It might be why I stopped writing in the first place. But that memory is buried so far beneath mountains of shit and meat that I doubt I'll ever be able to confirm it."
    "Regardless, I'm glad she has a few new avenues to use when it comes to expressing herself."
    "I just hope they aren't all dead ends."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label futabaspringnoongen:
    scene futabaspringnoongen
    with fade
    play music "kimitoakinobouken.mp3"

    "I call Futaba and the two of us make plans to head back to that bookstore we visited during our date full of offscreen sex."
    "The man working at the shop remembered us immediately and proceeded to go on an extensive rant about the importance of silence in places like this. He did not understand the irony in that."
    "The store seems bigger. Like it's an organic being adding new floors in the form of limbs. And I wonder for a moment if it can feel us moving through it."
    "Maybe I'm a bookstore too."
    "Maybe all those things I feel moving around inside of me are age-gapped couples with destructive power dynamics and the infantile tendencies to shit all over ourselves because we deserve it."
    "Or maybe I'm just a human. That's the more logical answer, of course."
    "It just seldom feels like that word accurately describes me anymore."

    scene black
    with dissolve

    "The trip back home isn’t as quiet as I'd like to be as Futaba fills the radio silence with positive dialogue about how glad she is to have met me."
    "I've been complaining a lot lately, so I won't say anything self-dismissive in response to that. But I will vehemently disagree in terms of my existence somehow benefitting her."
    "Her happiness is temporary because one day, I'll be gone. And she'll be left with nothing but memories of a relationship that will make her vomit when she's older and smarter."
    "But for now, I'll just open my mouth and let her vomit inside of {i}that{/i} instead."
    "My heart says to call that another infantile tendency, but my brain knows even infants aren't that stupid."
    "Unfortunately, there is another organ attached to my body that knows far more than both of those ones- so we end the afternoon in a love hotel covered in fluids."
    "The end."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label amispringmaidgen:
    scene amispringmaidgen
    with fade
    play music "amiamiami.mp3"

    "I find myself heading over to the maid cafe because Ami is cute."
    "I spend the next hour thinking about how cute Ami is."
    "When she brings me her famous omurice, the first thing I think is “Wow, she is so cute.”"
    "After that, she sits down at the table with me and is cute again."
    "Sometimes I think I'm going insane. But then I realize I'm not insane at all. It's just that Ami is so cute and my brain can not comprehend it."
    "When I am looking at Ami, I feel safe and happy because of how cute she is."
    "She really is so cute."

    scene black
    with dissolve

    "Ami is the only girl I will ever need."
    "Ami is the cutest girl in the whole wide world."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami is so cute!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label amispringnoongen:
    scene amispringnoongen
    with fade
    play music "normalday.mp3"

    "I give Ami a call and, feeling generous today, decide to take her to the mall."
    "The only problem is, the mall is closed for renovations. And there is no indication of when it will open back up."
    "Ami and I stare at the doors for a few minutes, wondering whether or not we should set up a tent and wait an indeterminate amount of time until we're allowed to enter."
    "But we stop thinking that when we smell something weird leaking through the glass."

    stop music
    scene squishsquosh
    play music "sound.mp3"

    "We press our ears up to the doors and hear something that sounds a lot like bioorganic matter churning and pulsating and throbbing and oozing."
    "It's pretty strange and we're not sure what it is. But I can immediately tell that renovations are going to take longer than expected."
    "We give up the idea of setting up a tent and attempt to investigate what the noise could be instead."
    "When I try to stare through the glass, I'm not able to see anything. And after several seconds, it feels like a pair of wet arms are wrapped around my waist."
    "The arms aren't long. And they're rather frail, I think. But I'm unable to see them as I've been blinded by the doors and can't currently confirm anything."
    "Ami starts to cry, and I have to reassure her that the arms will take us home."
    "The squishing and squoshing continues but this language of flesh is not one that I learned during my time beneath the Spindle Rock."
    "Something splashes onto my cheek and angers the arms."
    "They reach down and unbutton my pants and try to do evil things to my penis as punishment."
    "They ultimately succeed in doing so because the arms have been my arms all along and they're not even wet. All the moisture was a lie."
    "The arms are dry. Like centipedes in salt fields."

    scene black
    stop music

    "The mall is closed."
    "It's something else now."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label amispringnightgen:
    scene amispringnightgen
    with fade
    play music "love.mp3"

    "I call Ami to find out that she’s in bed, so I decide to join her there because that's what good uncles do."
    "She welcomes me with a smile that could light up a room and an ancient hymn about a Godling called the Gossamer."
    "I listen attentively as she overpronounces her　は's and make sure to correct her speaking patterns so she doesn't disturb the village elders in the future."
    "When the hymn ends, we watch one of her favorite movies — a DVD she found on the side of the road containing three and a half hours of POV hiking footage."
    "We hold hands for so long that they merge together and it takes another hour to untangle our arteries, but it's a heartwarming bonding experience."

    scene black
    with dissolve

    "Eventually, the two of us become tired and we remove her DVD from the disc tray, electing to watch Netflix instead."
    "Ami crawls into my arms like a legless cat and purrs as the light from her laptop makes contact with her sensitive skin."
    "I pop the bubbles forming on her legs with a pencil so she doesn't float away and I gain an extra point of affection for every single one I manage to destroy."
    "I discovered the bonus round."

    $ ami_love += 17
    stop music fadeout 5.0

    "{i}Ami’s affection has increased by 17!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label mayaspringshrinegen:
    stop music
    scene mayaspringshrinegen
    play sound "broken.mp3"
    $ renpy.pause(9, hard=True)
    scene black
    stop sound

    "74 68 69 73 20 69 73 20 6e 6f 74 20 68 65 72"
    "........."
    "......"
    "..."

    jump nightch4

label mollyspringmorninggen:
    scene mollyspringmorninggen
    with fade
    play music "molly.mp3"

    "I call Molly early in the morning, expecting her to not pick up so I can say “at least I tried” and then give myself an excuse to sulk for the rest of the day."
    "Unfortunately, she {i}does{/i} answer. And now I'm here on a park bench beside her, once again not understanding anything and wishing I called someone else instead."
    "Which isn't to say I dislike her. That's not true at all. I've gotten weirdly close to Molly over my time here. But I also know it won't ever go anywhere."
    "She and I aren't “compatible.” Just look at us. The best we can do for one another is soak up each other's fleeting lust so it doesn't ooze out of our bodies and drown the city."
    "But you know- maybe drowning the city would be good."

    scene black
    with dissolve

    "It often feels like I'm underwater anyway. Like I'm trying to move, but my body's so weighed down that it won't cooperate."
    "I wonder how often everyone feels that way. And I wonder if any of those feelings would change if we had gills."
    "I think about fish being all fish-like. I stop thinking about Molly."
    "But she doesn't stop thinking about me."
    "I can tell because I can still hear her from a hundred feet below sea level."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label mollyspringcafegen:
    scene mollyspringcafegen
    with fade
    play music "breeze.mp3"

    "I make my way to the cafe and walk through the doors with my mouth open in hope of being purified one final time before moving onto whichever definition of the afterlife is most accurate."
    "Unfortunately, I just wind up looking like an idiot because Molly is actually working tonight and the cafe is decently busy."
    "It seems as if the city as a whole has been getting busier lately. Even the amount of men around appears to be increasing. But I imagine it's just due to the weather."
    "There's not much of a reason to hide inside anymore now that the temperature has become somewhat bearable."
    "It's only the pungent, sickening scent of cherry blossoms that compels me to stay inside at this point. I imagine that's just a {i}me{/i} problem, though."

    scene black
    with dissolve

    "Molly eventually finds the time to acknowledge my existence and bestows the rest of her responsibility onto another unlucky part-timer so she can come talk to me."
    "And surprisingly, she doesn't talk about anything annoying. She just asks me how I'm doing. But that is annoying in its own way."
    "If she had only noticed my thirst for cleaning fluid when I first came in, she'd know the answer to that question."
    "I don't hold it against her, though. She has never been perfect and I can relate to that."
    "And if she continues to misunderstand the level in which I desire to be here, I think the two of us can stay friends."
    "I leave the cafe. Molly does not."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label tsuneyospringarcherygen:
    scene tsuneyospringarcherygen
    with fade
    play music "summerwind.mp3"

    "I head over to the archery range to find Tsuneyo just...standing there and looking up at the sky."
    "She immediately notices my presence and asks me how I feel about clouds. But I don't feel much at all about anything anymore."
    "According to her, they look familiar. But not in a way that indicates she's seen them before. It's more like they remind her of something from her past."
    "But, from what I understand, her past is confined to just one building in a seedy party of town. And I can't imagine something as free as a cloud could parallel that life in the slightest."
    "We talk a little bit about archery and how she has a knack for it. She thinks it's because of her body and her self-discipline."
    "But all I can think in response to that is when she'll trust {i}me{/i} enough to discipline her instead so she can have more time to herself."
    "There are so many things I can teach her."

    scene black
    with dissolve

    "Tsuneyo hands me her bow and asks me if I’d like to try taking a shot. But when she hands me the arrow, my first instinct is to point the weapon at her."
    "She does not flinch."
    "She does not do anything."
    "And in doing or not doing that, I realize I've {i}already{/i} gained her trust when I've done nothing but show her that she should keep it as far away from me as possible."
    "I lower the bow and hand it back to her."
    "She draws back the string and fires an arrow straight through the bullseye."
    "She should have chosen a different target."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label tsuneyospringramengen:
    scene tsuneyospringramengen
    with fade
    play music "kashiwagi.mp3"

    "I make my way over to Tojo Ramen with a specific menu item in mind, but neglect to order it once I arrive there. But I can't tell you why until I figure out something to tell myself first."
    "I've been thinking a lot about ramen lately- the kind you make in cups. Not the kind served to you in half-cracked bowls by mechanical hands."
    "There is a leak in my water cup. Tsuneyo replaces it with a mason jar and demands that I fend for myself, but she knows nothing of the things I have gone through."
    "The power stays on throughout the night, which is good because I am afraid of the dark now."
    "I'm afraid of almost everything."

    scene black
    with dissolve

    "I've been thinking a lot about ramen lately."
    "I've been thinking of what's upstairs."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label iospringmorninggen:
    scene iospringmorninggen
    with fade
    play music "lifeismostlygood.mp3"

    "I call Io as she's on her way over to the bathhouse and the two of us make plans to meet near the convenience store over there."
    "She offers to buy me breakfast as there's a sale on meatbuns, but I refuse due to a lack of appetite. This, of course, leads to her eating four of them on her own."
    "I'm concerned for a moment that she might have some sort of degenerative disease if she's still so thin despite eating things like this for breakfast every morning."
    "But then I remember she's on roughly ten thousand medications that I'm sure take some sort of toll on her weight."

    scene black
    stop music

    "And then I remember someone else who also used to eat like that."
    "I don't want to, but I do."
    "So I black the rest of the morning out to protect myself."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label iospringbathhousegen:
    scene iospringbathhousegen
    with fade
    play music "io.mp3"

    "I head to the bathhouse to spend some time with Io and, instead, get coerced into taking off all of my clothes."

    if iosex == False and iospring2 == True:
        "And while the temptation to pull her into the water with me threatens to derail this monologue, I've already told both myself and {i}her{/i} that I would be better than this."
        "At least for Io...Because I know where Io comes from. And I know that forcing anyone to do {i}anything{/i} isn't as justifiable as I may want it to be."
        "With so many chips already present in her porcelain skin, I could shatter her with one touch."
        "So my hands remain at my sides while my mind drowns in the gutter."
        "It's a compromise I'm willing to make."
    else:
        "I hope to one day be able to coerce her into taking hers off as well. But she's broken in a way dissimilar to me, so I'm not sure how long that will take."
        "I suppose that, if worse comes to worst, I can always {i}assist{/i} her. She's no stranger to overmedicating, of course."
        "And out of all the medicinal cocktails out there, I'm sure there's bound to be {i}one{/i} that will heighten her libido."
        "If there is, she probably knows it. But something about the way her eyes move when I talk about sex tells me she'd rather just be unconscious instead."
        "Sometimes, I feel the same."

    scene black
    with dissolve

    "I close my eyes and begin to doze off as Io starts explaining the rules of baseball to me. But what I discover is not rest."
    "It's that baseball has a lot of fucking rules and most of them don't make any sense."
    "Eventually, I manage to drown out her voice with unfinished dreams of a life in which she's in here with me."
    "And I finally reach nirvana when I dream of a life in which I'm in her."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label iospringnightgen:
    scene iospringnightgen
    with fade
    play music "justlights.mp3"

    "There's something about hands that makes me uncomfortable, but I can't explain exactly what or why."
    "Upon closer inspection, it might be the way each tendril can move on its own. How there are five creatures pushing themselves out of a center point that sends blood and nutrients to them."
    "That might not be the most accurate description in terms of anatomical function, but it's the one that makes the most sense to me and distracts me from what's actually happening right now."
    "Io inspects my hands. She focuses on the tendrils that have longed to penetrate her in ways that would make her vomit- and she does so with a smile."
    "She sees not their evil as they are divine in nature and easily camouflaged, but their mistaken beauty and a connection between us that is both fabricated and false."

    scene black
    with dissolve

    "Her hands are soft and only half the size of mine. I could crush them if I wanted to."
    "But I don't want anything."
    "I stay still and act as her voodoo doll, hoping the soft tracing of her tendrils upon my center point will send a signal to my brain that reminds me it's okay to love."
    "But all I feel is the warmth of her skin and an immediate desire to go home and lie down."
    "So that is what I do."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label utaspringarcherygen:
    scene utaspringarcherygen
    with fade
    play music "fallishere.mp3"

    "I find Uta at the archery range first thing in the morning and she wastes no time in subtly reminding me that this is one of the two things she's exceptional at."
    "I don't think that's saying much though as the {i}other{/i} thing really just involves conning people into giving her money based on fake affection."
    "Her affection for me is real, though. It's unwarranted, sure. But it's {i}real.{/i} And even though it {i}shouldn't{/i} be, I accept it. Just as I accept everyone else's."
    "You see, there's no point in denying anyone's love for me anymore. Because even if I can't return it, I can still benefit from it. And with Uta, there's one thing I've always wanted."
    "I should be thankful she gets so easily attached."

    scene black
    with dissolve

    "I should be thankful she thinks of me when she's in bed at night and not one of her classmates. I should be thankful I beat all of them out."
    "And I should be thankful that she can remove her eyes from the target long enough to wink at me before letting her arrow fly."
    "..."
    "So why am I not?"
    "Why do I want to {i}hold{/i} her?"

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label utaspringmaidgen:
    scene utaspringmaidgen
    with fade
    play music "maidcafe.mp3"

    "I head over to the maid cafe because there's nothing that distracts me from the pain of simply existing like cute girls who want me to fuck their brains out."
    "Thankfully, there are three of those girls here tonight. But Uta-chan, being the head maid, takes it upon herself to serve me in their place. And I wouldn't have it any other way."
    "You see, {i}this{/i} is the Uta that makes me the most comfortable. It's the one I've known the longest and, even if it's not entirely authentic, it's always been here."
    "Things have been going away lately. But Uta-chan isn't going anywhere. And I can rely on her to treat me the same way every time I take my wallet out."
    "Plus, I'm her most loyal customer. She probably relies on my money to pay for her Internet streaming subscriptions. There's no way I can leave her alone."
    "I couldn’t possibly do that to Uta-chan."
    "If I ever made her sad, I would have to kill myself."

    scene black
    with dissolve2

    "Then all three of these girls would have to fight over who gets to fuck my corpse before it goes cold."
    "And I feel like there's no way Uta would ever win that battle."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label utaspringnightgen:
    scene utaspringnightgen
    with fade
    play music "love.mp3"

    "I meet up with Uta after she gets out of work."
    "It's late now. And it's gotten cold."
    "I feel tempted to wrap my arm around her to keep her warm, and I know that's what she wants, but I abstain because I know where it would lead."
    "My inhibitions frequently get the better of me most nights now. And I often find myself thinking things like “fuck it” or “who cares?” much more than I used to."
    "But..."
    "There are moments where that's not the case. And almost all of those moments are as silent as this one."

    scene black
    with dissolve2

    "Uta has become rather protective of me, but she clings to my side like a cyst in total contradiction of this."
    "You see, she doesn't understand that she's making things worse by simply being here. That the temptation is increasing and my walls are caving in on her."
    "Soon, she too will be consumed."
    "And that's why I let her stay cold."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label otohaspringparkgen:
    scene otohaspringparkgen
    with fade
    play music "brighterdays.mp3"

    "I make my way over to the park to see what Otoha’s up to and, as always, I...I don't know. I...hang out with her, I guess?"
    "She's one of the few teenagers around here that I don't have some sort of {i}connection{/i} with yet. So, all things considered, good for her."
    "But {i}more{/i} things considered, I wonder why I keep going out of my way to be around her despite our current status as “good acquaintances.”"
    "I mean, it's not as if I want that to {i}change{/i} at this point, right? So what sense is there in raising one more chicken if I'm just going to have to slaughter it?"
    "I'll be the first to admit that I still want to fuck that princely aura right out of her, so maybe it's something as simple as that."
    "Or maybe I'm just getting high on the fact that there's someone around here who doesn't see me as her god."

    scene black
    with dissolve

    "I join her on the bench and remain silent as she talks about her morning, sparing no details in describing her strange encounters here."
    "With the increase in foot traffic brought on by this infinite spring, she's been making more money off her music."
    "She offers to use some of it to buy me lunch, but I politely decline and ask her if she'd rather have sex with me instead because it's cheaper."
    "She politely declines and says she would rather sew her vagina shut."
    "She's smarter than her friends. I'm glad she gets to live forever."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label nodokaspringlibrarygen:
    scene nodokaspringlibrarygen
    with fade
    play music "icantseeher.mp3"

    "I find Nodoka in the library because I {i}want{/i} to find Nodoka in the library. But also because that's where she elects to spend most of her time."
    "She accepts me with open arms, and quite literally at that as she stretches them out and beseeches me to cry into her bosom so she can absorb my pain."
    "I want to think that it's because she wants me to feel better, but I know that it's because it's the only chance she'll ever have to actually feel."
    "I would do it if I could. {i}Cry.{/i} But such a thing is a lot easier when I'm alone in the dark and not surrounded by textbooks and fliers for school events."
    "As such, she never gets to experience hurt for the first time. And I never get to experience the seductive manipulation of a girl who could rule the world if she'd only apply herself."

    scene black
    with dissolve

    "I say that, but she {i}does{/i} apply herself. She just applies it to the wrong things."
    "She tells me about research she's been doing lately. About how she thinks the world is broken. But I don't have the heart to tell her she's right."
    "Beneath the table, I place my hand on her thigh and slide up her skirt. She does not react. And it makes me question whether or not she's immune to physical sensations as well."
    "But given how depressing and unfortunate that truth would be, I decide instead that she's content with being my many-stringed puppet. Where I can play with her as much as I want, but never correctly."
    "She's just a little too hard to manipulate. And more often than not, it feels as if {i}she's{/i} the one playing with me."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label nodokaspringnightgen:
    scene nodokaspringnightgen
    with fade
    play music "icantseeher.mp3"

    "I call Nodoka and wind up getting roped into visiting a nearby night market with her."
    "Or at least she pretends it's nearby. In all actuality, I'm forced to join her on the subway as we travel twenty minutes away to an area I'm not familiar with."
    "Sometimes, it feels like this town is alive. Like it's growing. This is one of those times."
    "The market is heavily populated, and I keep feeling as if I'm being watched. Nodoka says I'm not, but I know she feels it too. I can tell by the way she smiles."
    "Thankfully, the paranoia is eventually numbed by the thought that she could pass as my daughter. Unthankfully, this leads to even darker thoughts."

    scene black
    with dissolve

    "I find myself wondering how my life would be if she took the place of Ami."
    "I wonder how different things would be if I was relentlessly and incestuously pursued by someone so much smarter and more intentionally sinister than I am."
    "For some reason, I'm inclined to believe I never would have started teaching at all. And I'm not just saying that because I'm demoralized by knowing I'd never be able to teach {i}her.{/i}"
    "I just mean that I feel like I'd be doing something else. And instead of my desires and dreams being {i}supported,{/i} they'd have been fabricated instead."
    "I think that might be nice. And as Nodoka browses through a dusty selection of old novels, I think about fully surrendering myself to her."
    "It's a fleeting thought, though."
    "And it's replaced by an unwanted mix of fear and comfort the second she looks my way again."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label toukaspringarcherygen:
    scene toukaspringarcherygen
    with fade
    play music "marshmallow.mp3"

    "Touka's been steadily getting better at archery, which is great because it means she's one step closer to being able to put me out of my misery in {i}one{/i} shot instead of four."
    "I didn't come here to complain, though. That's what literally every other location is for. And if I'm going to go out of my way to visit the school on a day off, I should try to be positive."
    "My mind navigates away from the cruel and hurtful things and hones in on the way Touka makes me feel instead. But in an unexpected turn of events, that winds up being even crueler."
    "As comedically {i}good{/i} and...intimately matriarchal as she is, there's something about her presence that confuses me. And now, I'm always confused whenever she's around."
    "I wonder how she interprets this, as I know she's smart enough to realize the changes in my behavior. But I can never bring myself to ask."

    scene black
    with dissolve

    "She smiles at me. And for a moment, there's a bout of silence laced with what I {i}want{/i} to be understanding so I never need to open my mouth again."
    "But all the things that I have learned tell me it's admiration instead, and I pray to the clouds above our heads that I am wrong this time."
    "The silence is killed off when she evades my oddly comfortable unease like a rabbit dodging predators, and I breathe a sigh of relief in knowing I won't have to face this past this morning."
    "I just have to face her."
    "And that's both the easiest and the hardest thing at the same exact time."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label toukaspringnoongen:
    scene toukaspringnoongen
    with fade
    play music "tsukiokamanor.mp3"

    "I call Touka to find that she's busy this afternoon as she has important rich-girl business to tend to at the Tsukioka Manor."
    "And while I'm more than happy (for lack of a better word) to just hang up when I hear that, she invites me over to wander around one of their many gardens with her. So I agree."
    "She sends a car to pick me up and, after another uncomfortable ride, I pull up at the manor and am escorted in by her attendants."
    "The first thing I think when I see her is how infrequently she wears that fancy dress now. And I applaud her for how she's managed to sort of...blend in with all of us commoners in a sense."
    "She'll never be one of us, though."

    scene black
    with dissolve

    "She's even more of an outlier than I am- and I would break her immediately if she exposed her weaknesses to me."
    "It would not be intentional, of course. I'd never jump a fence just to trample a flower garden."
    "But if that fence does not exist, there's a high likelihood of me being too absentminded to care at all. And she'd be ruined in the process."
    "Spring is the season for flowers. And the pungent scent of sakura from an everblooming tree hunts me from what I can only imagine is a mile away."
    "It makes me want to jump a fence."
    "It makes me want to blame her."
    "It makes me want to hurt her."
    "So I leave."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label kirinspringnoongen:
    scene kirinspringnoongen
    with fade
    play music "behindabathroom.mp3"

    "I call Kirin and wind up getting roped into joining her by the riverside that separates the first half of town from the second. And in a way, it's kind of beautiful."
    "Not the scenery or the girl herself, but the fact that she's found a place so apt when it comes to emphasizing the type of person she is at her core."
    "That fine line between the dark and the light- where the former is creeping and closing in and ready to swallow her whole...but she's still dangling from its mouth."
    "You can tell there's some sort of desire to break free and live another day, but she's so desperate to be loved that she'd rather be consumed than save {i}herself.{/i}"
    "What she wants is for me to pull her out. Or perhaps it's for {i}anyone{/i} to pull her out and I'm just what she has."
    "But I can't do that."
    "And it makes accepting the food she holds up to my mouth impossible to take a bite out of as I feel like I'd be biting her."

    scene black
    with dissolve

    "She'd probably like that. She's the type of girl who'd be willing to give up a chunk or two of her flesh in exchange for a mouth full of semen, but I'm not a carnivore just yet."
    "Sure, I partake in the taste of organic meat when the need arises to sate my appetite, but there are other things I enjoy as well."
    "I like the way the light reflects off of the water. And the shadows nearby buildings cast on her freshly shaven legs. I like her. And she likes me."
    "We like each other."
    "I finger her by the riverside and hope someone snipes from the windows."

    $ kirin_love += 1
    $ kirin_lust += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label kirinspringnightgen:
    scene kirinspringnightgen
    with fade
    play music "thesleepingcity.mp3"

    "I give Kirin a call and, while she offers to come visit me so I don't have to leave the house, I go to see her instead."
    "She takes me to an overpass not far from the urban district where we spend the night chatting and watching cars pass beneath us."
    "She seems different tonight. Like she'd purr instead of growl if I decided to bed her in a nearby love hotel. And it's attractive in a way she seldom is."
    "But it gets me thinking about cats. About how I'm so verbally averse to owning them, yet my biggest hobby is feeding them from my palm until they're no longer inclined to bite or scratch."
    "Some cats have trouble shedding their feral nature, though. And I think Kirin might be one of them."
    "No matter how much milk I give her, she'll always want to scratch. And I'm okay with that, because the sensation of her claws digging into my flesh makes me feel alive."

    scene black
    with dissolve

    "I don't tell her I'm thinking these things as she's smiling tonight in way she doesn't normally smile. And if I step on her tail while her guard is down, it might subconsciously scar her."
    "And as delighted I would be to have her rip my throat out with her teeth, I feel bad for whoever would need to clean my blood off of the pavement."
    "We continue staring down at the cars beneath us."
    "But I stop thinking about Kirin and start thinking about jumping."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label norikospringconveniencegen:
    scene norikospringconveniencegen
    with fade
    play music "noriko.mp3"

    "I venture into the worst part of town to hang out with a girl who's way too good for me and find her eating dinner in the dining section of the convenience store."
    "I question whether or not it's okay for her to do this seeing as she's the only person who's ever working, but then I remember just how infrequently people come in here and stop caring."
    "After all, if I can go my entire life without working, I shouldn't fault Noriko for following my footsteps just because she knows better."
    "She makes room for me at the table and I pull up a chair so I can drown my infinite numbness in the ecstasy my sheer existence provides her."
    "And while she likely spends the next two hours waiting for me to make out with her, I spend the next two hours looking at her as a sister."

    scene black
    with dissolve

    "I imagine that's just a side effect of having viewed her that way in what I can only imagine as the better half of my life at this point."
    "Though, it's likely that's not the case at all as this is apparently my second seemingly permanent bout of childish sorrow."
    "But that's just the thing. It's only {i}seemingly{/i} permanent. And what better way to question permanence than by expelling my energy on the rival of the one I lost?"
    "I hope she's looking down on or up at me from wherever she is or isn't and that the jealousy this would cause her forces her back into existence."
    "But of course it doesn't. And the girl who's too good for me continues to be tainted by my presence up to the moment I go home to one I deserve."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label norikospringmorninggen:
    scene norikospringmorninggen
    with fade
    play music "love.mp3"

    "Noriko volunteers to come over to my place the moment I call her, and I reluctantly accept despite the existence of Ami and how that's sure to make her feel."
    "She hates it, of course. And she tries to prevent me from leaving by wrapping her entire body around my legs, which I just kick her off before apologizing and walking through the door."
    "I meet up with Noriko a few blocks away from the house, and we decide it's best to stay in this area so that Ami's body will still be warm when we find it dead a little while from now."
    "I think that would make Noriko happy. She's been put off by Ami's existence lately- which I don't blame her for after what she's witnessed and gone through."
    "In fact, I don't blame anyone for the way they look at my niece now. But I feel especially bad for Noriko as, from her point of view, it's probably like I don't see her at all."

    scene black
    with dissolve

    "And that's true to a certain extent, but not {i}entirely{/i} true. I mean, parts of me have entered parts of her. And that has to count for something."
    "But between Niki and Ami, it's like I'm always closer to someone than I am to her. And I'll never stop being impressed by the way she can persevere despite that."
    "I hope to be as strong as her one day. But considering I've made it 31 years into life without achieving that, I can't imagine I ever will."
    "Which means I'll just have to live vicariously through her. And while that comes with many downsides, I can take solace in the fact that I'm already used to hurting myself."
    "So that part won't be hard at all."

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label yasuspringchurchgen:
    scene yasuspringchurchgen
    with fade
    play music "newhope.mp3"

    "There are living shadows beneath New Hope Cathedral."
    "It is said they walk with extra limbs, assisted by metal rods jutting out of their joints- with white lights at their tips that blink every nine seconds."
    "Like the spinning of this rock called Earth, they carry on in perpetuity- illuminating the basement where the rabbits die, but never long enough to bring them back to life."
    "I watch and listen as Yasu reads passages from her bible. And while all of them are vague and left up to the reader's interpretation, I am unable to interpret anything."
    "I watch the way her fingers move- those tiny, spiderlike appendages jutting out of her hand like metal rods in the knees of shadows, and I begin to feel aroused."
    "There is so much happening beneath our skin that I can't help but fall in love with the idea of swimming through her veins and chewing on her muscle mass."

    scene black
    with dissolve

    "There are living shadows beneath New Hope Cathedral."
    "Three of them visit me on my way to the basement."
    "They carry my body back up the stairs and tell me I'll be interrupting his sleep."
    "I ask them when he will wake up, and then they fade away."
    "There are living shadows beneath New Hope Cathedral."
    "Yasu Yasui has seen them."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label saraspringnoongen:
    scene saraspringnoongen
    with fade
    play music "sidecharacter.mp3"

    "I call Sara and wind up getting talked into meeting her at some cafe that I really don't want to go to. But I guess it's fine since there isn't anywhere else I'd want to be either."
    "Beggars can't be choosers, after all. And if I'm going to funnel my misery down the throats of unsuspecting friends, I should at least let them choose where to open up their mouths."
    "As such, Sara's mouth (As well as the rest of her) keeps me company within the confines of a building that smells like bread. So much so that I have a headache within minutes."
    "To avoid the pain, I retreat to the bathroom and make myself throw up. This only makes the pain worse. But when I come back into the lobby, things go back to normal."
    "My mask is secured tight enough so as to not alert Sara that I'm anything less than perfect right now."
    "Either that, or there's no amount of convincing that could get her to change her mind about me in the first place."

    scene black
    with dissolve

    "Her feet keep bumping into mine beneath the table. I think she's trying to tell me something."
    "But I already know what that something is, and it's something I don't want to hear. So I kick her back in a way that's meant to tell her I'd rather be left alone."
    "Of course it doesn't work."
    "She kicks me again. And again. And again. Until my feet are swollen and no longer fit in my shoes."
    "I might have made that part up. But it changes nothing."
    "I still want to chop them off."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label saraspringbargen:
    scene saraspringbargen
    with fade
    play music "calmbar.mp3"

    "I'm finally starting to understand just how effective Sara's methods are when it comes to dealing with grief."
    "Because, while drinking won't ever make the things I don't want to think about go {i}away,{/i} it {i}does{/i} confuse me after I spend enough time doing it."
    "And hey, I'll take what I can get at this point. Especially when I'm getting it from someone who would probably let me fuck her daughter if I asked her nicely."
    "Not like I'd need to, though. Both Sakakibaras want me as the centerpiece of their world, and it's making me question just how dark those worlds must be if {i}I{/i} can somehow light them up."
    "There's a point during the night where Sara stares at me for an extended period of time."
    "I can tell she wants to say something. But she never does."

    scene black
    with dissolve

    "She just smiles and walks away, grabbing me another beer out of the cooler before taking a break to tend to a few other customers."
    "I observe her while she does this. And I confirm that I'm the only person she smiles like that for."
    "But strangely enough, in complete contrast to the way things used to be, it's not a smile I want to protect. It's one I want to decimate."
    "Because I know that destroying the happiness she's able to get from me now will let her smile for someone else one day."
    "But I am selfish."
    "So I drink. And I wind up confusing myself."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label harukaspringcafegen:
    scene harukaspringcafegen
    with fade
    play music "cafe.mp3"

    "I drop by the cafe to hang out with Haruka but, when I arrive, she’s surprised to see that I approach {i}her{/i} instead of her much younger and much more lesbian employee."
    "I can't blame her, though. Especially when I know she probably wants to fuck her even more than I do. But I draw no attention to this as that would be rude."
    "Instead, I listen to the two of them argue about some inventory-related issues that I can't be bothered to care about when my mind is already flooded with sex and squalor."
    "Eventually, I'm able to order a drink. Hooray. And I spend the next few minutes mandatorily involving myself in Haruka's affairs while Rin makes it."
    "She asks me if I'll be taking it for here or to go. And I instinctively say “here” but I immediately regret it as I take a seat at a nearby table."

    scene black
    with dissolve

    "You see, I've never felt {i}comfortable{/i} in crowds. I don't like being the center of attention and I'm always worried that someone is going to talk to me."
    "Which means I must be a masochist as I keep throwing myself headfirst into situations where that's bound to happen."
    "And today, it does."
    "Someone asks me for the time. But I don't know the time. It's just {i}now.{/i} So I tell them it's {i}now{/i} and they get mad."
    "Haruka comes to drop off my drink, but brings the actual answer to the person's question along with her."
    "She scolds me for messing with her customers. But what she doesn't know is I'm being more genuine now than ever before."
    "I'm scared of eye contact."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label harukaspringnightgen:
    scene harukaspringnightgen
    with fade
    play music "thesleepingcity.mp3"

    "I give Haruka a call and tell her I don't want to be alone tonight, so she comes to pick me up so we can watch a movie together."
    "After buckling my seatbelt, it becomes apparent that she isn't headed toward her house- she's headed to a nearby theatre. So I ask her to turn around as I'd rather be with her and no one else."
    "She smiles when she hears this. I think she likes feeling important to someone. But the thing is, I don't think she {i}is{/i} important to me. She's just who I chose tonight."
    "There's no real reason for it. And the honest truth is that removing her from my life wouldn't do much at all apart from elevating the price I have to pay for coffee in the morning."
    "When she changes into her pajamas, she decides to omit her bra. And I decide to stare because I gain nothing from abstaining."

    scene black
    with dissolve

    if harukapredator == True:
        "She notices me noticing her. And she takes her top off completely to appease me since that's her job now."
        "I tell her to fuck herself with the TV remote while I watch."
        "She's confused by the request, but she obliges and proceeds to struggle fitting it inside her pussy. I'm surprised by this as I assumed I'd stretched it out as far as it will go by now."
        "She asks me if I'm going to talk dirty to her, but I'm not. I've grown bored of the movie, so all I'm doing now is watching {i}her{/i} instead."
        "And I guess it's good that I got bored. Because, for the next ten minutes, the volume and channel change repeatedly."
        "Haruka reaches orgasm with assistance from my fingers. As it turns out, TV remotes don't feel very good when inserted inside of a person."
        "I reward her for her attempt with a mouth full of cum and my immediate departure."
        "I don't get a ride this time."

        $ haruka_lust += 1
        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
    else:
        "She notices me noticing her. And then I notice that she pretends to never notice at all."
        "We might just be {i}friends,{/i} but I know she still longs for my touch. And I think about throwing myself at her in response to this because I know she wouldn't refuse."
        "Throughout the night, she positions herself in ways that are meant to attract me. And I realize she's lacking underwear as well when she bends over to grab the remote off of the floor."
        "She puts on a movie with multiple sex scenes. But she disappears halfway through it to take care of herself when she realizes I won't."
        "Unfortunately for her, I'm too busy torturing myself to pleasure her tonight."
        "And so we'll remain {i}friends{/i} for at least a little while longer."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label kaorispringmorninggen:
    scene kaorispringmorninggen
    with fade
    play music "justbehappy.mp3"

    "Despite how confusing it is simply being around her, I can always count on Kaori to never make me feel any {i}worse{/i} when I go to see her. So I guess that's a good thing."

    if halloweenfive17 == False:
        "Of course, this also means that the likelihood of her making me any happier is just as likely as me having sex with her in the near future, so I'm kind of shit out of luck in that department too."
        "I guess there was that one time she almost raped me, though. So who knows? Maybe that will happen again and she'll be carrying my spawn before the next blue moon rises."
    else:
        "Maybe sometime in the future, I'll be able to visit her for more than just food though. Especially now that I know she has a taste for {i}me.{/i} So maybe I can be the one to feed her for once."
        "It beats giving her {i}kittens.{/i} At least in terms of the result. But hey, maybe being next to her would actually make me feel like a {i}good{/i} parent."

    "Either way, I spend my morning at her newest job. Or at least what I assume is her newest job as I've yet to bump into her in an even more recent location."

    scene black
    with dissolve

    "She creams me in front of a crowd of people who are also patiently waiting to be creamed. And I can't help but imagine that happening in the more visually appealing way. Just with roles reversed."
    "Basically, I imagine her getting gangbanged by a group of random passersby and all of the ridiculous things she'd likely say in her fit of expected ecstasy."
    "Kaori notices a sudden increase in my body temperature and asks me if it's mating season. I tell her it is and that I'm looking for a mate."
    "She blushes and runs away. I must not have used the proper mating dance."
    "Eventually, I pay my bill and jerk off in a nearby public restroom while a spider sits on my thigh and watches."
    "I hope it lays its eggs inside of me. That way, it will be egg time forever."

    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label kaorispringnightgen:
    stop music
    play sound "static.mp3"
    scene kaorispringnightgen with flash
    stop sound
    play music "firstsecondmall.mp3"

    "I make my way into Kaori's apartment after she doesn't answer the door so I can make sure she's alive. And she is. She's just watching TV."

    s "Hello."
    k "..."
    na "..."

    "I decide to watch TV with them."
    "There is a commercial for improvements being made to the mall, but it seems there's no estimated completion date as of yet."
    "I guess it's good Chika got a second job then. It would suck for Chinami if her sister got trapped inside of the mall and wasn't allowed to leave until construction was complete."
    "Kaori, Nao, and I sit by the TV in silent excitement. And while I can't read their minds, I can tell they're looking forward to what the future will bring."
    "I wish I could do that too."
    "I'm excited, sure. But I know that any joy material goods can bring me will only be temporary. And I'm not as easily swayed as a pair of strange girls who want to buy strange objects."

    s "are you going to finish your egg"
    k "..."
    na "..."

    scene black
    with dissolve

    s "bone apple teeth"

    play sound "eggcrack.mp3"

    "I bite into the egg and swallow John's child."
    "It tastes just like a waiting room."

    $ kaori_love += 1
    $ nao_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "{i}Nao’s affection has increased to [nao_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chinamispringmorninggen:
    scene chinamispringmorninggen
    with fade
    play music "gentle.mp3"

    "I make my way over to the Chosokabe apartment to hang out with Chinami because I'm a fucking mess and this is what I do now."
    "When I get there, she's eating cereal and watching TV. So I decide to join her because what the fuck else am I going to do with a girl her age?"
    "Don't answer that question. If you answer that question, you'll be damning me. And I won't be damned. Not like this. Not while incessant laughter bleeds through this flatscreen's speakers."
    "We watch commercials. Just commercials. No actual TV. Chinami says it's always like this in the morning. Chinami says she doesn't mind."
    "But I mind. I need to be distracted before a part of me breaks even more and I wind up perpetuating a cycle that I, too, was- no."
    "Think better things. Think of what {i}she{/i} would say if {i}she{/i} saw you here. Think, you fucking idiot. {i}Remember.{/i} How would {i}she{/i} feel?"

    scene black
    with dissolve

    "How {i}did{/i} she feel?"
    "Was it worth it? Did you watch commercials with her too, AKIRA?"
    "Did she sit on your FUCKING lap and QUESTION what was POKING her, you fucking FREAK?"
    "YOU CAN'T RUN FOREVER, SENSEI."
    "JUST BECAUSE SUMMER'S OVER DOESN'T MEAN YOU SHAN'T {i}TAKE{/i}"

    ch "Papa? Is something-"
    s "I have to go."

    play sound "doorslam.mp3"

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label chinamispringnoongen:
    scene chinamispringnoongen
    with fade
    play music "blueair.mp3"

    ch "Papa?"
    s "Stop calling me that."
    ch "Can Chinami ask you a question?"
    s "Sure. Go for it."
    ch "What do you think is behind the wall?"
    s "I'm not really sure."
    s "I try not to think about it."
    ch "Do you think it's scary? Like...a monster?"
    s "I think it's possible. But don't tell your sister I said that."
    ch "Will Papa get in trouble for revealing the secrets of the universe to Chinami?"
    s "It's not a secret if it's something I'm guessing. I just don't want Chika to think I'm scaring you for no reason."
    ch "Chinami has other things she's afraid of before monsters. And those things are all {i}inside{/i} the wall."
    s "..."

    scene black
    with dissolve2

    ch "Can Chinami ask you another question?"
    s "Sure..."
    ch "What do you think is {i}behind{/i} behind the wall?"
    s "Like-"
    ch "The furthest place you can think of. Somewhere none of us will reach until we're ready to leave Kumon-mi behind."
    s "..."
    s "Maybe a monster."
    s "Maybe something worse."
    ch "Worse than a monster?"
    s "Maybe it's nothing."

    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label nikispringnightgen:
    scene nikispringnightgen
    with fade
    play music "wewereangels.mp3"

    "I decide to spend the night with one of the only people who really {i}gets{/i} me. But the problem with that is that she is one of the only people who {i}really gets me.{/i}"
    "And with the state I've been in lately, I'm not sure if that's a good thing or not. Because if someone spends their night reciting my flaws, what am {i}I{/i} supposed to do?"
    "Granted, any time Niki does that, it's out of love. And I know she means no harm by it."
    "But I see reflections of my mistakes in everything already. I don't need someone to point at them and remind me that they're there when what I want to do is ignore them."
    "Regardless, we tuck ourselves into the corner of some bar near Niki's studio, where she assures me that her identity won't cause any problems."
    "But I kind of wish it would."
    "Because at least then I know everyone wouldn't be looking at me."

    scene black
    with dissolve

    "I spend too much time thinking about myself and I'm unable to have any fun. But, lets face it, I've never been good at that to begin with."
    "We chat about the past and whether or not it has a chance of ever becoming the present again."
    "To a certain extent, Niki thinks it already has."
    "But to a greater extent, I just want to spoon my eyes out and dissolve them in a chemical solution."

    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label osakospringdojogen:
    if osakospring4 == False:
        scene osakospringdojogen
        with fade
    else:
        scene osakospringdojogen2
        with fade

    play music "sakuya4.mp3"

    "I head over to the dojo because I have a good feeling I can get Osako to accidentally kill me if I say the right things. But Ayane is there when I arrive, so I decide against it to save her the agony."
    "I've read in books (When I used to do that) that there are people who manage to overcome their mental rainy seasons through intense physical exertion and things like {i}going to the gym.{/i}"
    "But I quickly discern that I am not one of those people as just being here beneath these lights makes me want to lean into kicks rather than deflect them."
    "Osako proceeds to give the two of us karate lessons, but cuts those lessons short when she realizes I'm not {i}feeling{/i} it."
    "She talks to me alone and tries to hype me up, but I do nothing but stare back at her and silently wish she would have kicked me out of here years ago."
    "Because maybe then, I wouldn't get my hopes up. And I could forget all those things I read."

    scene black
    with dissolve

    "Ayane left without saying goodbye today, but I don't think there was any malicious intent behind it."
    "She knows I'm fucked. And so does Osako to a certain extent, but I'm not sure if she'll ever really {i}get{/i} it since she's never going to fall for me and has no reason to care any more than she already does."
    "I like that about her. I don't have to worry that this will ever turn into anything more than it actually is. And I can slip into physical stasis when I'm with her, so my mind can wander elsewhere."
    "I just wish it would stop wandering in the space between my lust for death and the circumstances that would allow me to seek reprieve inside of her."
    "Interpret that however you want."

    $ osako_love += 1
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label osakospringdivegen:
    if osakospring4 == False:
        scene osakospringdivegen
        with fade
    else:
        scene osakospringdivegen2
        with fade
    play music "10c.mp3"

    "Somehow or another, I wind up spending most of the night at the dive bar talking to Osako after getting my ass handed to me at pool. Or {i}billiards{/i} if I want to sound pretentious."
    "And what I learn from this is that she has a knack for teaching, which is good considering that she's hanging out with a bunch of teachers right now. And Rika, who is a human that exists."
    "But between her instructions when it comes to pool and what she's given me at the dojo (When she's not kicking my ass), I can tell that she really loves sharing what she knows with other people."
    "I just question why she wants to share that knowledge with {i}me{/i} as I've done nothing but cause problems for her during the brief time we've known one another."

    scene black
    with dissolve

    "And I have no intention of putting an end to that as it would mean falling in line and acting the way I {i}should.{/i}"
    "Don't get me wrong, the idea of complacency sounds lovely. And I want nothing more than to peacefully coexist with all of the misery that inhabits this world."
    "But outliers like me can't just {i}fall in line.{/i} There are no lines that suit us. And this conversation alone has been very helpful in making me reaffirm that."
    "I stick out like a sore thumb. My flaws glow bright beneath the neon."
    "And I spend less time learning pool and more time trying to figure out what the looks I'm getting from my friends mean."

    $ osako_love += 3
    $ wakana_love += 1
    $ imani_love += 1
    $ rika_love += 1

    "{i}Osako's affection has increased by 3!{/i}"
    "{i}Imani's affection has increased by 1!{/i}"
    "{i}Wakana's affection has increased by 1!{/i}"
    "{i}Rika's affection has increased by 1!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label wakanaspringdivegen:
    if osakospring4 == False:
        scene wakanaspringdivegen
        with fade
    else:
        scene wakanaspringdivegen2
        with fade

    play music "10c.mp3"

    "It's another normal night at the dive bar. And I spend this one focusing on Wakana as she's hands down the easiest person for me to talk to here."
    "Or maybe I'm just a masochist in constant search of the poison that drips off her tongue when she speaks of how much easier her life is without me in it as much."
    "Even with that being said, though, there's a level of calmness I get when I'm with her that stands leagues above what I'd get from people like Imani and Rika."
    "They're great, don't get me wrong, but this low-maintenance brand of friendship is the kind that I'm most suited to. And I'm {i}happy{/i} just sitting here, watching her drink."
    "Which is great, since I'm confident that she can outdrink virtually everyone in this city. So I'll always have something to watch."

    scene black
    with dissolve

    "Osako comes back over to our table when she realizes I'm alone with her girlfriend, and spares no time at all when it comes to snatching her arm and reclaiming what is hers."
    "Wakana jests and reassures her that she'll never see me as anything more than a flesh-eating parasite, and I'm inclined to agree. In fact, I think that's the most accurate description of me yet."
    "Imani and Rika return as well and, within a matter of seconds, our peaceful intermission comes to an end and another lively night of drunken conversation ensues."
    "It's fine."
    "But I can't help but wish right now that it was only Wakana."

    $ osako_love += 1
    $ wakana_love += 3
    $ imani_love += 1
    $ rika_love += 1

    "{i}Wakana's affection has increased by 3!{/i}"
    "{i}Osako's affection has increased by 1!{/i}"
    "{i}Imani's affection has increased by 1!{/i}"
    "{i}Rika's affection has increased by 1!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label wakanaspringmorninggen:
    scene wakanaspringmorninggen
    with fade
    play music "comfort.mp3"

    "I call up Wakana shortly after waking up to find that she has nothing going on today. And I'm surprised to hear her invite me over just a few seconds later."
    "Unsure of whether or not I'll have to keep this visit a secret from her girlfriend, I make my way over to her apartment and find her still dressed in her pajamas once I get there."
    "I don't know when she decided to start letting her guard down around me, and I can't figure out if it's a good thing or a bad thing."
    "I know she still sees me as a {i}threat.{/i} She reminds me all the time. And it feels like just the other day that I was cornering her in the library."
    "All that's changed since then is how openly miserable I am, so maybe {i}that's{/i} what pushed her over the edge and gave the go-ahead to stop giving a shit when I'm around."
    "She probably thinks I'm too weak to pounce. That I'm a malnourished coyote and she's a well-fed and elusive rabbit."
    "I could probably catch her if I truly want to."
    "I just don't know if it's worth the effort."

    scene black
    with dissolve

    "We wind up ordering breakfast from some local restaurant and I'm not surprised to find that Kaori is the delivery girl."
    "I am surprised to find Wakana address her by name once she arrives, though. But I guess that makes sense considering the two of them are neighbors."
    "We spend the morning coexisting. Wakana tells me stories of what's happening in school and I feign interest while I attempt to forget school altogether."
    "She asks me when I'll be coming back. {i}If{/i} I'll be coming back. And I don't have an answer for her."
    "She smiles in a way that only {i}she{/i} can smile and tells me to take my time, but I know she wants me to hurry."
    "She misses me."
    "She just won't say it out loud."

    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label wakanaspringnoongen:
    scene wakanaspringnoongen
    with fade
    play music "fallishere.mp3"

    "I don't come to school much anymore. I'm too vulnerable when I'm here and, more often than not, all it does is evoke bad memories. But I made an exception today."
    "After calling Wakana and finding out that she's alone in her office, I swallowed my pride and decided to join her there and keep her company while she grades papers."
    "She doesn't demand that I help her this time, as she'd always done in the past. Instead, she makes small talk with me and tells me to help myself to one of the many poetry collections on her shelves."
    "I try not to read anymore unless I absolutely have to as that, too, evokes bad memories."
    "But when the vast majority of my memories are {i}bad{/i} to begin with, I have to learn to accept that, sometimes, wading through them is inevitable."
    "As such, I grab a book off of her shelf and begin to flip through it."

    scene black
    stop music

    "Never mind."
    "I'm going home."
    "I picked up the wrong book."

    $ wakana_love += 1

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label imanispringnoongen:
    scene imanispringnoongen
    with fade
    play music "cafe.mp3"

    "I call Imani to find that her plans for the afternoon are to basically just grade papers until she gets a migraine. And, sensing that she could use a break, I invite her out for coffee."
    "What I did not know at the time of me doing this was that she would take it as an invitation to just grade papers {i}beside{/i} me."
    "And, after I take a few seconds to remind myself that this is simply what {i}responsible{/i} teachers [[probably] do, I don't bother voicing any complaints."
    "I mean, how {i}could{/i} I when the only reason she's working this hard to begin with is to make up for {i}my{/i} absence?"
    "I buy her a drink and a few pastries and keep quiet when she needs me to keep quiet, occasionally voicing an opinion on a topic she...requires an opinion in regard to."
    "But overall, it's just a relatively calm afternoon."

    scene black
    with dissolve

    "Eventually, she puts her notes and papers down and is able to start focusing on me."
    "She apologizes and tells me about how crazy things have been lately. And how it's getting harder to hide the fact that I haven't been showing up."
    "And while she never directly {i}asks{/i} me to come back, it's easy to tell that she wants me to. And that's reinforced by several consecutive stories of how some of the girls are faring without me."
    "She knows I still see them around sometimes. She hears about it while she's trying to teach."
    "But it's not the same....and no one thinks it is."
    "If only they knew how {i}I{/i} felt."

    $ imani_love += 1
    stop music fadeout 5.0

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label imanispringnightgen:
    scene imanispringnightgen
    with fade
    play music "love.mp3"

    "I head over to Imani's apartment to find her taking some much needed time off and lounging around, watching videos from some sort of social media thing on her phone."
    "She makes some room on her mattress, which can hardly be called a {i}bed{/i} as it's haphazardly thrown onto the floor, and I take my place beside her."
    "She comes closer, but I neglect to tell her I'd rather have some space as I see little point in denying any form of company anymore."
    "Our shoulders touch as she begins to include me in her marathon of something she calls {i}doom scrolling.{/i} And I quickly find that it effectively kills a lot of time."
    "So much time, in fact, that it's midnight before I know it. And I'm left with the option to either go home, or spend the night here with her."

    scene black
    with dissolve

    "So of course I go home. Because, while I tell myself I'm against denying company, there's still a part of me that's a coward. Or a part of me that wants her to be happy."
    "And she's been kind and good and useful enough to deserve more than just the shell I can provide her as the person I am now."
    "I would kill to be able to give her more, because a {i}friend{/i} alone will not sustain this frantically beating heart and these hands that keep grasping at straws but coming up empty."
    "{s}I want to put another me inside of her.{/s}"
    "I want to bite off her tongue."

    $ imani_love += 1
    stop music fadeout 5.0

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label imanispringdivegen:
    scene imanispringdivegen
    with fade
    play music "10c.mp3"

    "Imani and I show up at the bar before anyone else does, but I can't confirm whether or not that's a calculated effort on their behalves this time."
    "I'm going to assume it's not as I think my friends are better than taking advantage of me at my lowest but, at the same time, I kind of hope it {i}is{/i} because I don't deserve to be friends with nice people."
    "The two of us waste no time at all in getting the ball rolling as we order the first round of drinks to reward ourselves for our punctuality."
    "Imani then proceeds to poke and prod at my crumbling exterior in an effort to {i}pick me up,{/i} but I think it does more harm than good as it kind of just makes me want to strangle her."
    "I guess it's possible that's what she wants, though. There are weirder and less acceptable fetishes after all. And at least she can't get arrested for hers."

    scene black
    with dissolve

    "Eventually, the rest of the group shows up and apologizes for being late."
    "As it turns out, another sinkhole opened up on the opposite end of town and delayed their arrival as they'd been out shopping together and had to take an alternate route here."
    "They order drinks and we raise our glasses to sinkholes. I don't really get it since they've done nothing but cause problems for them so far, but I go along with it regardless."
    "Because {i}my{/i} experience with sinkholes is a little bit better."
    "And in a roundabout way, I think that's what brought all of us together."
    "So I toast to the hope that, some day, one won't tear us apart."

    $ osako_love += 1
    $ wakana_love += 1
    $ imani_love += 3
    $ rika_love += 1

    "{i}Imani's affection has increased by 3!{/i}"
    "{i}Wakana's affection has increased by 1!{/i}"
    "{i}Osako's affection has increased by 1!{/i}"
    "{i}Rika's affection has increased by 1!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label karinspringmorninggen:
    scene karinspringmorninggen
    with fade
    play music "retrospect.mp3"

    "I call Karin and wind up getting summoned over to the park to join her for her morning jog."
    "Or to join her for what would have been her morning jog if my sheer existence didn't cause everyone and everything around me to stop the moment I show up."
    "My presence is all it takes for Karin to stop caring about her health, and we spend the next ten years on that bench, slowly fusing with it until our blood has turned to sap."
    "My legs are the first to go. They're removed by maintenance workers as they were beginning to terrify children. But Karin's legs are nice, so they get to stay a little while longer."
    "Anyway, what I'm trying to say is nothing of substance occurs."
    "We just talk and waste away along with the morning sun."

    scene black
    with dissolve

    "At least I can take solace in the fact she isn't broken yet."
    "These utterly untainted moments I get to spend with someone who reminds me there is still purity in this world do not go unnoticed."
    "But noticing them alone is not enough to change anything."
    "And just because I am temporarily sated does not mean I'm comfortable or happy."
    "I still want to sleep inside her."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label karinspringpoolgen:
    scene karinspringpoolgen
    with fade
    play music "lifeismostlygood.mp3"

    "I make my way over to the pool because it might be the only opportunity I ever get to see Karin wet."
    "Unfortunately, it seems like today won't be the day for that either as she feels weird about swimming so long as I'm present."
    "As such, the two of us retreat to a bench where she tells me all about the wholesome things she's been doing as a whole, while peppering in comments about how I should return to school."
    "I'm not sure what she would gain from that even if I did given that she's never been a student of mine. But I humor her regardless because it's easier than telling the truth."
    "And I'm not about to sit here and explain to a girl that probably doesn't even know what a penis looks like that I fucked one of her underclassmen out of existence."

    scene black
    with dissolve

    "It would have been nice if I was the one to have disappeared instead. But hey, maybe that's how it will turn out if I ever truly {i}fall{/i} for someone else."
    "Imagine that person winds up being Karin. Imagine what sort of toll would be taken on {i}her{/i} mind if she lost her virginity only to find herself alone and quivering on some cold rooftop."
    "I bet she'd never want to have sex again."
    "Sometimes, I feel like I don't either."
    "But I tell myself I'm wrong so I can keep coming to places like this- where I can convince myself it isn't over yet."
    "But I know that, deep down, it is."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label tsubasaspringnightgen:
    scene tsubasaspringnightgen
    with fade
    play music "tsukiokamanor.mp3"

    "There's something special about Tsukioka Manor. But if you asked me to tell you what it is, I'd probably just point my finger at the creature in front of me."
    "Which isn't to say Tsubasa's daughters aren't just as {i}special{/i} as she is, but they possess only a fraction of the terrifying yet arousing aura I'm experiencing right now."
    "In terms of what makes this place what it is, though, I see no reason to look any further than the opposite side of this desk."
    "Tsubasa isn't what I thought she was at first. She's no stereotypical lord's wife, nor a woman who's simply skating by due to what she's acquired since birth."
    "She's a puppeteer."
    "And any time I'm with her, I need to pay extra attention to my strings."

    scene black
    with dissolve

    "I'm not quite sure why I came here tonight apart from the fact that she wanted me to. And I'm not quite sure what I've gained from doing so."
    "But I feel closer to God than I did the night before. And the reason for that is simple."
    "There's something special about Tsukioka Manor."
    "And you can hear it for yourself if you stop focusing on all of the other sounds."

    $ tsubasa_love += 1
    stop music fadeout 5.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label yukispringbargen:
    scene yukispringbargen
    with fade
    play music "calmbar.mp3"

    "Sakaki-bar-a has been pretty busy as of late, but that never stops me from spending time with my favorite recovering addict."
    "It does, however, stop me from communicating with anyone else when I arrive tonight as both Sana {i}and{/i} Sara are busy serving other customers."
    "After finishing up with one of her other tables, Yuki makes her way over to me and the two of us spend the next thirty minutes or so {i}shooting the shit{/i} as she would call it."
    "And what I've learned is that must mean “Listening to some early-thirties adult male complain about his problems.” Which, let's face it, is {i}kind of{/i} what bars are for in the first place."
    "It feels like just the other day that that was {i}all{/i} I could do in here, though. And I never imagined this place being even a fraction of as popular as it's become lately."
    "And weirdly enough, I think a lot of that is due to Yuki."

    scene black
    with dissolve

    "She's the catalyst that helped turn this place around whether it makes sense or not."
    "And sure, a lot of that could just be convenient timing. But when I'm talking to her, I can't help but think otherwise."
    "She's a surprisingly good listener. And even if her advice isn't always worded eloquently, it always seems to make sense."
    "I don't need eloquence- just someone to be there."
    "And tonight, that person is her."

    $ yuki_love += 1
    stop music fadeout 5.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label yukispringnoongen:
    scene yukispringnoongen
    with fade
    play music "calmbar.mp3"

    "After calling Yuki, I wind up getting talked into visiting her at her apartment so she doesn't have to venture elsewhere just to head off to work later."
    "And while I'm not to keen on the idea of exerting any sort of energy either now that everything hurts all the time, I go to her regardless because it's either that or just standing here."
    "When I make it to her part of town, I'm reminded of how good I have it to own a piece of real estate in what most would call a nicer area."
    "But it's strange to me that this feels more like a home than that does."
    "Perhaps it's just because of what's happening there right now. Or what has happened in the past."
    "But whatever it is, I'm glad to be here."

    scene black
    with dissolve

    "As glad as I {i}can{/i} be, of course. Which still isn't that great, all things considered."
    "But Yuki manages to alleviate some of that pain by making fun of me and poking at my inadequacies in a way that would be sure to make me smile if my facial muscles hadn't all rotted by now."
    "I do the same and poke fun at her while joining her on the couch."
    "I can smell smoke lingering on her breath each time I try to move closer just to immediately remember {i}decisions{/i} I've made in the past and second guess myself."
    "I wonder what would happen if I knew how to say no to myself. I wonder if she'd let me."
    "..."
    "I wonder what I'm doing here."

    $ yuki_love += 1
    stop music fadeout 5.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "........."
    "......"
    "..."

    jump nightch4

label makispringmorninggen:
    scene makispringmorninggen
    with fade
    play music "normalday.mp3"

    "Worried that I will turn to dust if I do not leave the house soon, I make plans to meet up with Maki at the cafe and remind my body that, despite everything, it is still alive."
    "Thankfully, she's in a much better mood than I am. So she takes the lead when it comes to conversation and even winds up buying my coffee for me."
    "I try to tell her I don't mind paying, but she insists that this one is on her so she can {i}express her gratitude{/i} for me or whatever."
    "I'm sure that's just pity, though. I'd probably do the same for her if {i}she{/i} disappeared for two months."
    "But, at the same time, I don't think I offered to pay for her after her husband died. So that tells you basically everything you need to know about my character."

    scene black
    with dissolve

    "The morning passes by without any issues and, eventually, Maki has to leave to start getting ready for work."
    "I question what exactly she needs to {i}get ready{/i} for as a porn salesman and, as you may have guessed, that spiraled into a long-winded tangent about the importance of her job in society."
    "And I agree. If it wasn't for porn, I doubt a lot of us would even exist."
    "So, for a brief moment, I curse the fact that porn exists before remembering that I need to consume it at least once per day in order to keep breathing."
    "It's a terrible curse, but one that I have grown to accept."
    "I just wish I could see it the way she does."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label makispringporngen:
    scene makispringporngen
    with fade
    play music "citylife.mp3"

    "I find myself once again at the only place I really belong- the Miyamura family porn shop."
    "I have experienced many things here since being re(?)-birthed into Kumon-mi, but a thing I seldom experience within these walls is a normal, non-sexual conversation."
    "I mean, how is one supposed to speak normally when surrounded by rubber penises, exposed breasts, and the sounds of violent orgasms bleeding through the speakers in the corners of the room?"
    "Regardless of how impossible that sounds, we manage to find a way. And Maki and I spend the next hour or two just talking about life."
    "As it turns out, and don't tell her this as she's one of the few people I know verbally opposed to me fucking teenagers, we have a lot more in common now that my somewhat-significant other is gone too."
    "And while it's true we were never married, it does not stop me from believing we kind of were inside my head."

    scene black
    with dissolve

    "That's enough miserable reflecting for one night, though. I'll have plenty of time for plenty more of that tomorrow."
    "For now, I should focus on returning Maki's kindness by listening to her vent about...whatever's on her mind this time."
    "But of course it's Makoto."
    "And of course that makes me spiral."
    "So I phone it in for another thirty minutes or so before going home and jerking off to the thought of them touching one another instead of touching me."

    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label rikaspringdivegen:
    scene rikaspringdivegen
    with fade
    play music "10c.mp3"

    "It's pub-trivia night again, which means that Rika is ten times more animated than her already highly-animated self. Which also means that we all have to suffer."
    "She winds up selecting me as a partner, leaving Imani to fend for herself while she pretends not to care. And surely enough, Rika smashes the competition."
    "I still don't understand where this strange bank of useless knowledge comes from. But considering how far behind she is in terms of common sense, I guess she needed to excel at {i}something.{/i}"
    "And you know what? I'm glad it's this. Because it's refreshing sitting beside someone who knows more about ancient pyramids than the evils that men do."
    "And as an evil man who will receive no golden sarcophagus nor tomb of any sort, that puts me at ease."
    "Just not enough {i}ease{/i} to discount the fact that I am, once again, unintentionally the center of attention."

    scene black
    with dissolve

    "Once the trivia game comes to an end, the rest of the girls head outside while Rika and I elect to stay in."
    "She congratulates me on a job well done despite me having done no job at all, and I congratulate her for the impressive defeat of several intellectuals in a battle of...intellect."
    "She gets confused when I word it that way, but I don't care."
    "Because regardless of what she knows or how she came to know it, she's a good person. And at the end of the day, that's more than most of us can say about ourselves."

    $ wakana_love += 1
    $ imani_love += 1
    $ rika_love += 3
    $ osako_love += 1

    "{i}Rika's affection has increased by 3!{/i}"
    "{i}Osako's affection has increased by 1!{/i}"
    "{i}Imani's affection has increased by 1!{/i}"
    "{i}Wakana's affection has increased by 1!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label rikaspringmorninggen:
    scene rikaspringmorninggen
    with fade
    play music "cafe.mp3"

    "I give Rika a call to find that she's in the mood to “do something” this morning. But, not being well-versed in “doing things,” I struggle to think of anything but getting coffee."
    "She jumps at the chance for this because it gives her the rare opportunity to visit Rin at work without being yelled at since it “wasn't her idea.”"
    "Of course, Rika wastes no time in rushing the counter and pointing out Rin to me as if I had no idea she worked here before then proceeding to talk about how great she is."
    "Rin does nothing apart from standing there like a verbal punching bag, absorbing her mother's kind words like jabs from the fists of Mike Tyson."
    "But instead of being knocked out, she just..."

    scene black
    with dissolve

    "She walks away. Meaning that Rika and I now have to wait for someone else to come to the counter if we actually want coffee today."
    "Thankfully, Haruka shows up shortly after and serves us. But not after providing a brief reminder that we are not allowed to torment her employees at work."
    "Rika apologizes, but I do not because I am innocent."
    "Then, after receiving our drinks, we make our way over to a table near the window and spend the rest of the morning discussing the right and wrong times to embarrass your children."
    "And as we exit the store, I silently hope that this discussion will never become relevant to me."

    $ rika_love += 1

    "{i}Rika's affection has increased to [rika_love]!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    jump noonch4

label alexisevent:
    if _in_replay:
        play music "secondmall.mp3"

    scene alexis1 with dissolve2

    amy "I hope you’re hungry, Akira!  Because I plan on buying a {i}bunch{/i} of tacos today!"
    s "Are you finally going to ring the bell? I know how much you’ve been looking forward to it."
    amy "I hope so! I’ll probably need your help though since my hands are gone. You don’t mind, do you?"
    s "Not at all. I’m actually really curious about the giant frog you mentioned."
    amy "Me too! I know he’s real, but he’s kind of also an urban legend at this point. Like, did you know that-"
    q "Amy! I’ve been looking all over for you!"

    "An unfamiliar voice calls out from afar."

    amy "Oh no."
    s "Amy? Who was that?"

    scene alexis2 with hpunch

    amy "No one! It’s time to go, Akira. I’m suddenly not hungry anymore! And I don’t even like frogs that much now that I think about it."

    play sound "footsteps.mp3"

    "The unfamiliar figure moves closer as Amy begins to handlessly fidget with the place her hands should be."

    amy "Akira, come on! There’s a bunch more exciting stuff I haven’t been able to show you yet! You want to see it, don’t you?"
    s "Of course I do. But-"

    scene alexis3 with dissolve2

    q "Finally! I managed to catch up to you."
    amy "{i}Hah...{/i}"

    scene alexis4
    with dissolve

    amy "{i}Hi, Alexis...{/i}"
    s "Alexis?"
    ale "Oooh, is that Akira?! He’s even more handsome than you described him!"
    amy "Alexis, why are you here? Can’t you tell I’m on a date right now? You’re not even supposed to be in the mall anymore now that you’ve joined the Environmental Cleanup Crew."
    s "What’s that? I haven’t heard of any cleanup crew yet. And this mall could really use one."
    ale "I’m part of a group that’s trying to make the outside air breathable again! It’s a dirty job, but somebody’s gotta do it."
    s "And you’re friends with Amy?"
    amy "{i}Ex-{/i}friends. Alexis isn’t even supposed to be here anymore. I have no idea how she got back inside."
    ale "I found a crack in the wall when I was picking up trash outside and walked nearly thirteen miles through a super narrow alley before I saw lights again. I was starting to worry that I would be lost forever!"
    amy "{i}Ahem.{/i}"
    ale "What’s wrong, Amy? Do you have a cough? It’s not another oral infection, is it?"
    amy "{i}No,{/i} Alexis! I just want you to leave so I can carry on with my date! You know how long I’ve been waiting for this!"
    ale "Okay, okay! Can I at least borrow him for an hour or two, though? It was really hard squeezing myself out of that narrow hall and I just {i}know{/i} I’m going to need somebody to push me back in."
    amy "Absolutely not. I know you. Which means I know you’re just going to try to recruit Akira for the cleanup crew and that’s far too dangerous for him. I’d never be able to sleep again knowing he’s out there."
    ale "But you’re able to sleep just fine knowing {i}I’m{/i} out there?"
    amy "Yes. You never belonged in here anyway. All you’ve ever done is get in the way, and there’s no room in the mall for people who don’t want to follow the rules."
    amy "Life would be so much better if you just swallowed a rat."
    ale "That’s really harsh, Amy! Especially after I came all this way just to see you again."
    ale "You’re not the only one who gets lonely, you know. It’s so dark on the outside too. The weeds have grown so tall that I can’t even see the stars most days."
    amy "{i}No,{/i} Alexis. You can’t see the stars because they’re {i}gone.{/i} The old sky has been replaced by the subtle blue tint of an analog television. Remember?"
    ale "Ohhh, right. I forgot we found out the stars were bad. Wow, I really {i}have{/i} been out of it for a long time, haven’t I?"
    amy "Yes. And the mall will be better when you are gone again. Now, Akira-"
    s "Just let me help her out for a minute, Amy. It’ll be okay. I’ll come right back."
    s "Besides, you were really looking forward to ringing the bell and seeing the frog, weren’t you?"
    amy "I mean...{i}yeah...{/i}"
    amy "But I’m..."
    s "..."
    amy "..."
    ale "I’ll go wait outside for a minute. You can come see me when you’re ready to push me through a crack in the wall, Akira!"

    scene alexis5
    with dissolve2

    amy "{i}Hah...{/i}"
    s "If there’s something you want to say, it’s okay to just say it."
    amy "I’m just worried, okay? That you’ll like Alexis more than me."
    amy "I know I’m not perfect. And I don’t want being around other girls to make you think that I’m not worth your time when I’ve {i}already{/i} waited so long to see you."
    s "I think you should be a little more kind to Alexis, Amy. She clearly likes you a lot."
    amy "If she liked me {i}that{/i} much, she wouldn’t have given me a yeast infection."
    s "That’s just one more thing the two of you can share."
    amy "I guess..."
    amy "..."
    s "..."
    amy "You promise you’ll come right back once you’re done killing her?"
    s "I’m just going to help her find her way back."
    amy "You’re not going to kill her?"
    s "I wasn’t planning on it?"
    amy "Are you sure?"
    s "I think so."
    amy "I’m pretty sure you said you were going to kill her."

    scene alexis6
    with dissolve

    s "I’m pretty sure I didn’t. I’m also pretty sure your tacos are here now."
    amy "Please come back, Akira..."
    s "I will. But only under one condition..."
    amy "Really? What is it? I’ll do anything. I’ll even lick your feet if that’s what you want!"
    s "What? No. I just want you to save me a taco."
    amy "Okay. I’ll save you a taco {i}and{/i} lick your feet."
    s "But you don’t-"
    ale "{i}Hey! Are you two almost done being cute in there?! A circle of cockroaches has surrounded me again and I don’t know if I can survive this time!{/i}"
    s "What do the roaches want with Alexis?"
    amy "Probably her baby. I think the nutrients in newborns are easier for them to break down than processed beef."
    ale "{i}I sure wish there was a big, strong man to come and rescue me!{/i}"

    scene black
    with dissolve

    s "I’m coming, I’m coming."
    s "Bye for now, Amy. I’ll be back as soon as possible."
    amy "..."
    amy "Yeah..."
    amy "Bye, Akira..."

    scene alexis7 with dissolve2
    $ renpy.pause(2, hard=True)
    scene alexis8 with dissolve2

    ale "Thanks a lot for saving me back there, Akira. Those cockroaches really had it out for me this time!"
    s "They really did, huh? Amy said it was because of your baby."
    ale "My baby? But my baby isn’t even born yet. They weren’t planning on chewing through my belly to get to her, were they?"
    s "I’m not really sure. I’ve never been good at understanding what bugs want."
    ale "Jeez. Guess I’ll just have to be more careful then from now on, won’t I?"

    scene alexis9
    with dissolve

    ale "So! Where do you want to go first?"
    s "Huh? Am I not escorting you back to the crack in the wall you snuck in through?"
    ale "You are! But there’s plenty to do along the way. And it’s been {i}years{/i} since I’ve last laid eyes on a boy! So I’d like to enjoy my time with you even if Amy will get angry with me for it."
    s "How are you pregnant if you haven’t seen a boy in years?"
    ale "Hm? I’ve always been this way."
    ale "I mean, if you {i}really{/i} get technical about it, I guess I’m not actually {i}pregnant{/i} at all. There’s just kind of a baby stuck inside of me. Just saying I’m pregnant is easier than explaining that, though."
    s "Is it...stillborn?"
    ale "Oh, no! She’s alive. She can speak too! But I’m the only one who’s able to hear her, obviously. And since she stopped growing ages ago, I don’t ever have to worry about her overstaying her welcome."
    s "Wow. I guess that’s kind of nice, actually. You’ll never {i}really{/i} be alone so long as you have something like that inside of you."
    ale "Exactly! I wonder if that’s how the mall feels about the frog?..."
    s "You think the mall has feelings?"
    ale "Of course! I don’t think it would keep growing if it didn’t. Plus, there’s that one wing made entirely of organic matter. I think I saw hair growing in there last time."
    s "Does...a place like that exist in here?"
    ale "Oh yeah! It’s super far away, but we can make a detour if you want to see it?"
    s "Absolutely not."

    scene black
    with dissolve

    s "Let’s just head toward wherever that crack was and figure out if I’ll be able to push you into it..."
    ale "Okay! I think it was...oh! This way! This way!"

    scene gpmc1 with dissolve2
    $ renpy.pause(2, hard=True)
    scene alexis10 with dissolve2

    ale "Have you and Amy come this way yet?"
    s "Yeah. I think she mentioned something about this wing being focused on...luxury shopping or something like that?"
    ale "Yup! There are tons of super nice stores to pick up super nice things, so I used to come here all the time when I was still hanging around the mall."
    ale "She told you I’m rich, right? My dad invented the worm."
    s "Like the insect thing or the dance move?"
    ale "Neither! The one businesses can license out to consume the decaying bodies of shoplifters the proprietors justifiably took the lives of."
    s "Oh."
    s "Well, no. She hasn’t told me about that."
    s "In fact, she hasn’t told me about you at all."
    ale "Really?"
    s "Yeah."
    s "I mean, she {i}did{/i} mention something about how she used to have friends and how it’s basically just pigeons now. But I’m not sure why she would have said that if you’re clearly still around."
    ale "It’s probably just because I don’t come around that much anymore."
    ale "I still love her, though."
    ale "I’ve just always been a little bit better at being alone than she is."

    scene black
    with dissolve

    ale "This way next, Akira! I’ll show you my favorite pillar!"

    "........."
    "......"
    "..."

    scene gpmf1 with dissolve2
    $ renpy.pause(2, hard=True)
    scene alexis11 with dissolve2

    ale "See that one to my right? That’s the best pillar in the whole mall. There’s a hole in it roughly three inches off the ground I used to hide succulents in."
    ale "I had to stop eventually when security caught wind of it, though. Succulents aren’t allowed in the mall. I think their somewhat suspended state of being confuses it?"
    s "I’m not really sure what you mean by that, but that’s sad."
    ale "Just that succulents kind of exist in a form that makes them {i}technically{/i} alive. But they grow at such a slow rate and, sometimes, not at all! They just kind of...{i}live.{/i} It’s almost like my baby!"
    s "Maybe it’s not a baby growing inside of you at all, but a succulent?"
    ale "Hahah! Maybe if succulents could talk."
    s "Maybe they can and we just don’t speak their language?"
    ale "Ooooh, how philosophical of you! I can see why Amy likes you so much now."
    s "Really? Because I can’t."
    s "And she says all this stuff about how we’ve met in the past before, but I really don’t remember any of it."
    ale "That’s not {i}your{/i} fault though, Akira. Tons of people experience similar phenomena when entering the mall. I’ve all but built up an immunity to it after coming and going so many times from my job."
    s "Do you like your job, Alexis?"
    ale "I didn’t at first, but I’ve come to really appreciate it lately. And while I don’t think we’ll ever be able to live on the outside again, I do like the idea of keeping it clean."
    ale "This world has so much history! It’s such a shame that most people only experience it through books or TV when hands-on experience is just so much more impactful in terms of teaching."
    s "It’s dangerous out there, though. Right?"
    ale "Oh yeah. You’d be a goner if you so much as set foot out there, which is why I don’t think we’ll ever return. It’s just a little sad to see."
    s "How do {i}you{/i} go out there then? Don’t your lungs fill up with weird stuff?"
    ale "They do, yeah. But it’s not really an issue when you’re using a mask and an oxygen tank. And we’ve got tons of stations where we can rest and refill our equipment."
    s "Oh, wow. How many of you are there?"
    ale "Hmm...I’m not really sure? I’ve never seen anybody else out there. That might just have to do with us being invisible from certain angles, though."
    ale "Either way, so long as someone is refilling the oxygen tanks and ration boxes, I’ll keep doing my best to make the outside world a better place!"

    scene black
    with dissolve2

    ale "I just wish my daughter was able to see it."

    "........."
    "......"
    "..."

    scene gpmr1 with dissolve2
    $ renpy.pause(2, hard=True)
    scene alexis12 with dissolve2

    ale "..."
    s "..."
    s "Is something wrong, Alexis?"
    ale "Hm? Oh, sorry! I came here without even realizing it. Must’ve been the whole “daughter” thing I said a few minutes ago."
    s "Yeah...It must be tough hearing her and knowing she’s there, but never being able to actually {i}see{/i} her."
    ale "I can picture it in my head — the way she looks. The color of her hair...the clothes that she wears..."
    ale "And you know, it’s weird. She’s been a baby for so long that, when I visualize her, that’s not even what I see anymore."
    ale "In my imagination, she’s not much younger than me. She’d probably look more like a friend than my child to anyone who saw us together."
    ale "But of course, that’s just my imagination. And she’ll probably make fun of me later for verbalizing it."
    s "I don’t think she will."
    ale "No, she already is. And I feel very silly now. But hey, at least I got it out there."
    s "Can I...talk to her?"
    ale "Do you actually {i}want{/i} to? Or are you just saying that because people always feel obligated to acknowledge one another’s children for whatever reason?"
    s "I want to. I’m just not really sure what I’d say. I’ve never been good with kids."
    ale "Well, if it’s any consolation, she’s not much of a kid anymore! She has just as much to say as you and me."
    ale "She’s never spoken to anyone else, though. So she’s a little bit nervous at the idea of it."
    s "Does she have a name?"
    ale "Yes! It’s- wait."
    ale "Sorry, Akira. She doesn’t want me to tell you that."
    s "What? How come? Have I offended her in some way?"
    ale "No. I think she’s just a little embarrassed that she can’t come out and greet you herself."
    ale "She thinks you’re very nice, though! And she, and I quote, “respects the heck outta ya for not mackin’ on another girl in the middle of a date.”"
    s "Oh shit, right. I’ve been having so much fun with you that I forgot I’m supposed to be spending time with Amy."
    ale "Hahah! I’m having fun too, Akira."
    ale "More fun than I’ve had in a...really long time..."
    s "..."
    ale "..."
    ale "Do you..."

    scene alexis13
    with dissolve

    ale "Do you think Amy would get mad if we...kissed?"
    ale "J-Just like a goodbye kiss, though! Like...on the cheek. Which...I guess it would kind of {i}have{/i} to be since I don’t really have a mouth. My whole lower face is basically just one big cheek. And-"
    s "I shouldn’t, Alexis. It’d feel weird with your daughter watching."

    scene alexis14
    with hpunch

    ale "R-Right! What was I even thinking?! Hahahaha!"
    s "I also don’t want to do anything that might lead to me catching a yeast infection."

    with hpunch

    ale "Amy told you about that?! That’s an intensely personal detail! And I promise it’s not how it sounds!"
    ale "I just got really hungry and ate a bag of spoiled yeast one day. Like, I’ve never even {i}touched{/i} a boy. And I’ve never {i}wanted{/i} to until right now and-"

    with hpunch

    ale "Ah! I shouldn’t have said that! Now you know I want to touch you!"
    s "Asking to kiss me also gave that away."
    ale "Hahah...hahahahah! Sorry, Akira! I just-"

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis15 with flash
    scene gpmr1 with flash
    scene alexis14 with flash
    stop sound

    ale "Huh? I..."
    ale "That’s funny..."

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis16 with flash
    scene gpmr1 with flash
    scene alexis16 with flash
    stop sound

    ale "I feel kind of...{i}weird{/i} all of a sudden..."
    s "Is everything okay? You look...grainier than you did a second ago."
    ale "Y-Yeah! I’m totally fine! I-"

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis17 with flash
    scene gpmr1 with flash
    scene alexis17 with flash
    stop sound

    ale "Oh no...No, not like this!"
    s "Alexis? What’s going on? Do you need to sit down? Should I call someone?"

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis17 with flash
    scene gpmr1 with flash
    scene alexis18 with flash
    stop sound

    ale "{b}{size=+20}I/////////REMEMBER/////////NOW!{/b}{/size}"

    play sound "static.mp3"
    scene alexis19 with flash
    stop sound

    ale "{b}{size=+20}THIS/////////YOUR//////[[REDACTED]{/b}{/size}"

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis21 with flash
    scene alexis22 with flash
    scene gpmr1 with flash
    scene alexis18 with flash
    scene alexis22 with flash
    scene alexis21 with flash
    scene alexis20 with flash
    stop sound

    ale "{b}{size=+20}WE/////////EXIST//////OUTSIDE{/b}{/size}"

    play sound "static.mp3"
    scene gpmr1 with flash
    scene alexis24 with flash
    scene alexis23 with flash
    scene gpmr1 with flash
    scene alexis18 with flash
    scene alexis22 with flash
    scene alexis21 with flash
    scene alexis22 with flash
    scene alexis25 with flash
    stop sound

    ale "{b}{size=+20}I//////////LOVE//////////YOU{/b}{/size}"

    play sound "static.mp3"
    scene alexis8 with flash
    scene alexis24 with flash
    scene alexis1 with flash
    scene alexis22 with flash
    scene alexis21 with flash
    scene alexis10 with flash
    scene alexis19 with flash
    scene alexis23 with flash
    scene alexis18 with flash
    scene alexis22 with flash
    scene alexis25 with flash
    scene alexis9 with flash
    scene alexis25 with flash
    scene gpmr1 with flash
    stop sound
    $ renpy.pause(10, hard=True)
    scene black
    with dissolve2

    ".........."
    "......"
    "..."

    scene alexis2
    with dissolve2

    amy "Ahh...yeah. That sounds like a classic case of lungrot."
    s "What?"
    amy "It’s what happens when you accidentally breathe in too much of the outside air."
    amy "Alexis probably forgot to tighten her mask all the way the last time she went outside to clean."
    amy "There’s nothing we can do for her now. She’s just one more casualty and one more example of why you should stay here forever, Akira."
    s "..."
    amy "Now! What do you say we go back to our date?"
    amy "I wasn’t able to finish all of the tacos, so I didn’t get to ring the bell this time. But maybe if I keep working hard and expanding my stomach, we’ll get to see the frog together one day!"

    $ persistent.alexisisreal = False
    $ persistent.alexisevent = True
    $ renpy.end_replay()

    menu:
        "go right":
            jump gpmi
        "go left":
            jump gpmh
        "go back":
            jump gpmq
