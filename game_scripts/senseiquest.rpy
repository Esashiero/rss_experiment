label halloweenfive7:
    play sound "static.mp3"
    scene gameworld1 with flash
    stop sound
    play music "8pox.mp3"

    "{i}It’s time to get gamey, but not like the meat! Four orbs of power make mission complete!{/i}"
    "{i}Do you have what it takes to defeat the [[insert generic antagonist]? Test your skills in the Shiawase Group’s latest RPG-{/i}"

    scene gameworld2
    play sound "rpgintro.mp3"
    $ renpy.pause(4, hard=True)

    "{i}Please be advised that Sensei-Quest is still in early access and all assets and aspects are subject to change.{/i}"

    s "Is the main antagonist a pizza?"

    "{i}No. We just liked how the icon looked. It really fit the vibe we were going for. We might change it later.{/i}"

    s "What is it with games and releasing in early access these days? Why can’t you just finish them first?"

    "{i}Because we need your money! Now run along and collect PREMIUM CURRENCY if you want to get to the end of the game!{/i}"
    "{i}There will be an option to buy this later. But you’re a beta-tester right now, so we’ve added PREMIUM CURRENCY as a drop from every standard enemy in the game.{/i}"

    s "But how am I supposed to defeat enemies if I don’t have any gear?"

    "{i}Oh! We took care of that as well!{/i}"

    play sound "winner.mp3"

    "{i}Sensei has received IRON SWORD!{/i}"

    play sound "winner.mp3"

    "{i}Sensei has received MELON HELMET!{/i}"

    play sound "winner.mp3"

    "{i}Sensei has received DEPRESSION!{/i}"

    s "Was that last one really necessary?"

    "{i}What’s wrong? DEPRESSION is a very powerful skill you can use to debuff your enemies by making them feel bad for you!{/i}"
    "{i}Or at least that's what it will be. Right now, it doesn't do anything.{/i}"

    s "I wanna learn how to cast FIRE BALL."

    "{i}Then you better get out there and start earning PREMIUM CURRENCY!{/i}"
    "{i}Oh, look! Here comes the tutorial NPC now!{/i}"

    play sound "static.mp3"
    scene gameworld3 with flash
    stop sound

    q "Oh, good! You’re finally awake!"
    q "What’s that dripping out of your helmet, though?"
    s "I think it’s my DEPRESSION."
    q "That is very interesting! Are you ready to learn how to play Sensei-Quest?"
    s "Do I even have a choice?"
    q "Not if you ever want to see your family again!"
    q "The objective of Sensei-Quest is to track down the {b}Four Elemental Orbs of Power{/b} and combine them into an {b}Ancient Orb{/b} in order to summon the final boss!"
    s "Earth, Wind, Water, Fire. Got it."
    q "What?"
    s "You said they’re elemental orbs, didn’t you?"
    q "Yes, but not {i}those{/i} elements. The elemental orbs {i}you{/i} need to collect are, {b}Plant, Worm, Fist,{/b} and {b}Red.{/b}"
    s "None of those things are elements."
    q "Not with that attitude, they’re not!"
    me "Oh! Also, my name is Meowri! I probably should have told you that earlier."
    s "It’s fine. You look kind of familiar, though. "
    me "That isn’t very surprising! My design is based on the [[IDEAL FEMALE], so of course you’d remember if you ever encountered anyone who looks like me. But that’s not important right now!"
    me "Sensei-Quest is an [[OPEN WORLD RPG], so you are free to explore wherever you like! We’re in the town of {b}Fuckladore{/b} right now, which is the main hub of the game."
    me "Fuckladore is full of vendors and taverns! Or...will be full of vendors and taverns! Right now, there is only one of each."
    s "Fucking early access games."
    me "Yeah, sorry about that. You can still feel free to browse those at your leisure, though!"
    me "The {b}MERCHANT{/b} sells weapons and armor you can use to better take down your enemies, while the {b}TAVERN{/b} sells powerful spells and abilities you can use to...also take down your enemies."
    s "Why does the tavern sell spells? Isn’t that supposed to be the kind of place that I pick up quests from or something like that?"
    me "Is it? None of our developers have ever played a video game before. We’re all just kind of guessing."
    s "This is sounding less fun by the second."
    me "Just wait until you find out the combat mechanics lack any amount of depth and use the same text box system as visual novels!"
    s "Ughhhhhhhh."
    me "The game is super grindy too!"
    s "Can I just exit out of your dialogue and go exploring now? I clearly have a lot of work to do."
    me "Okay! If you want to explore on your own, I’ll let you. "
    me "Just come find me once you’ve collected all of the Orbs of Power and I’ll help you summon the final boss."
    s "Cool. Thanks, Meowri. I can’t wait to unlock the first sex scene."
    me "There aren’t any sex scenes in Sensei-Quest."
    s "UGHHHHHHH!"

    play sound "static.mp3"
    scene gameworld1 with flash
    stop sound

    "{i}Meowri has returned to {b}MEOWRI’S HOUSE.{/b}{/i}"
    "{i}It’s time for you to save the world!{/i}"

    s "I will be the hero this world needs."
    s "But where should I begin my adventure?"

    menu gameworldmainhub:
        "Fields of Despair":
            jump fieldsofdespair
        "Sea of Stairs" if stairmap == True and plantorb == False:
            jump seaofstairs
        "Bedlehem" if bedmap == True and wormorb == False:
            jump bedlehem
        "Palace of the Fist" if fistmap == True and fistorb == False:
            jump palaceofthefist
        "Unholy Cathedral" if clockmap == True and redorb == False:
            jump unholycathedral
        "Developer Island" if ancmap1 == True and ancmap2 == True and fredisdead == False:
            jump developerisland
        "Traveler’s Tavern":
            jump travelerstavern
        "Roadside Merchant":
            jump roadsidemerchant
        "Meowri’s House" if fistorb and redorb and wormorb and plantorb == True:
            "{i}This is the point of no return. Do you still wish to proceed?{/i}"

            s "Wow, an actual helpful tip for once."

            "{i}Do you wish to proceed or not?{/i}"

            menu:
                "Summon the final boss":
                    $ renpy.end_replay()
                    $ halloweenfive7 = True

                    jump endofgameworld
                "Continue exploring":
                    s "I have a few loose ends to tie up first..."

                    jump gameworldmainhub

    ###################
label travelerstavern:
    scene gameworld4
    with fade

    if travbeen == False:
        q "Hey there! Welcome to the Traveler’s Tavern."
        q "I haven’t seen you around here before. Are you new in town?"
        s "Yeah. I just woke up here and now I need to collect a bunch of orbs or I will never see my family again. How is your day?"
        q "Oh, you know. Can’t complain."
        q "Well, actually I can since none of the assets for my tavern have been added into Sensei-Quest yet and I’m kind of just standing around in an empty room waiting for an update."
        q "But I’ve got items! And quests!"
        s "But the tutorial said you didn’t have quests and that you only sold abilities."
        q "Outdated tooltip, I guess. But it’s not like those things are ever helpful in the first place, right?"
        s "Can I have {b}Fire Ball{/b} for free please?"
        q "Nope! But I’d be willing to let it go for only 500 PREMIUM CURRENCY."
        s "That’s the same exact price written on the board. I’m not getting a discount at all."
        q "No discounts here, buddy. A girl’s gotta make a living after all."
        s "Ughhhh this game is so user unfriendly. I hate having to work for things."
        q "Same here, man. You think I want to be spending all of my time just standing around like this? Heck no. I ain’t built for the NPC life. So just tell me what you want or drag your butt on outta here. Capiche?"

        $ travbeen = True

    else:
        q "Hey there! Welcome back."
        q "What can I get for you?"

    "Right now, I have [pcur] PREMIUM CURRENCY."
    "What do I want to buy?"

    menu travmenu:
        "Quest: Sea of Stairs" if stairmap == False:
            if pcur >= 100:
                play sound "winner.mp3"

                "{i}Quest accepted — Sea of Stairs!{/i}"

                $ pcur -= 100
                $ stairmap = True

                q "Rumor has it that some big ole’ douchebag is holed up in the Sea of Stairs. And if my intel is correct, he might have one of those orbs you’re looking for."
                s "How possible is it that your intel is incorrect?"
                q "I’d say it’s about 50/50."
                s "Did you just sell me a quest that only has a 50%% chance of giving me a reward?"
                q "Yup! And there’s nothing you can do about it either since all sales are final."
                s "I would like to speak to the manager."
                q "That’ll cost you another 5000 PREMIUM CURRENCY."
                s "..."
                q "Any questions?"
                s "Yes. Why do you hate me?"
                q "I never hate the player. I hate the game."
                s "..."
                q "Get it? Because we’re in a game right now."
                s "..."
                q "And it sucks."
                s "I think I'll just try my luck without speaking to the manager."
                q "Good call."

                jump travmenu

            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Quest: Bedlehem" if bedmap == False:
            if pcur >= 150:
                play sound "winner.mp3"

                "{i}Quest accepted — Bedlehem!{/i}"

                $ pcur -= 150
                $ bedmap = True

                q "One of my other customers just came in and told me something about an ancient being taking shelter somewhere in Bedlehem."
                s "I didn’t realize you had other customers."
                q "Of course I have other customers. What would the point of a beta test be if only one person was testing the game?"
                s "I’m not sure. How do I get to Bedlehem, though? I’ve never been there before."
                q "Not many people have. It’s a super secret location that only a handful of us know how to reach. But seeing as you’ve purchased the quest, I guess I kind of have to tell you, don’t I?"
                s "That would be greatly appreciated. I have a good feeling I’ll be able to find one of the elemental orbs there."
                q "Maybe! Only one way to find out, buddy!"

                "{i}You’re not sure how, but without any actual dialogue revealing the details of the location, you suddenly know how to get to Bedlehem!{/i}"
                "{i}Video games are awesome!{/i}"

                jump travmenu

            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Quest: Palace of the Fist" if fistmap == False:
            if pcur >= 250:
                play sound "winner.mp3"

                "{i}Quest accepted — Palace of the Fist!{/i}"

                $ pcur -= 250
                $ fistmap = True

                q "There’s this place not far from here where all of the strongest adventurers go to train called the Palace of the Fist."
                q "And right now, the master of the palace is offering an orb of power to anyone who is able to defeat him."
                q "Taking him down will be no easy task, though. And even if you have the right build, you might have to try a bunch of different methods until something works."
                s "If that is the price that must be paid for reuniting with my family, I will do it. I will bring this palace master to his knees."
                q "Go for it, Sensei! I believe in you!"
                s "I will put my wiener is his stupid mouth too."
                q "What?"
                s "Then I’ll wiggle it around and tell him to call me “daddy.”"
                q "You’re being really weird about this, man."
                s "He better be ready for my cummy-wummies."
                q "Okay, I’m gonna have to ask you to leave now."

                scene gameworld1 with fade

                "{i}You got kicked out of the store!{/i}"

                s "That guy will never know what hit him once the penis comes out."

                jump gameworldmainhub

            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Quest: Unholy Cathedral" if clockmap == False:
            if pcur >= 300:
                play sound "winner.mp3"

                "{i}Quest accepted — Unholy Cathedral!{/i}"

                $ pcur -= 300
                $ clockmap = True

                q "I’m sure I don’t have to tell you this, but the {b}Unholy Cathedral{/b} is the most dangerous place east of Fucklador."
                s "What’s the most dangerous place to the west?"
                q "Newark, New Jersey."
                s "Please tell me there isn’t an orb there."
                q "There might be! But yeah, for your sake, I hope there’s not."
                q "But anyway! If you want to try your luck against the {b}Red Twins,{/b} I’d head over there. It won’t be an easy fight, though. Most of my customers try to stay clear of that place by any means possible."
                s "What happens to the ones who don’t?"
                q "Well, I wouldn’t still be selling this quest if any of them completed it, would I?"
                s "Good point. Guess I’ll go see if I can take them down then."
                q "Okay! Just try not to die. I kind of need you to stay alive for reasons."
                s "What kind of reasons?"
                q "You’ll find out in the sequel."

                jump travmenu

            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Venom Spit" if venomspit == False:
            if pcur >= 50:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Venom Spit!{/b}{/i}"

                $ pcur -= 50
                $ venomspit = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Banana Blast" if bananablast == False:
            if pcur >= 100:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Banana Blast!{/b}{/i}"

                $ pcur -= 100
                $ bananablast = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Bubble Beam" if bubblebeam == False:
            if pcur >= 200:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Bubble Beam!{/b}{/i}"

                $ pcur -= 200
                $ bubblebeam = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Sanitize" if sanitize == False:
            if pcur >= 100:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Sanitize!{/b}{/i}"

                $ pcur -= 100
                $ sanitize = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Fertilize" if fertilize == False:
            if pcur >= 150:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Fertilize!{/b}{/i}"

                $ pcur -= 150
                $ fertilize = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Salt Spray" if saltspray == False:
            if pcur >= 50:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Salt Spray!{/b}{/i}"

                $ pcur -= 50
                $ saltspray = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Fire Ball" if fireball == False:
            if pcur >= 500:
                play sound "winner.mp3"

                "{i}Sensei has learned {b}Fire Ball!{/b}{/i}"

                s "Finally."
                q "I’m happy for you, buddy."

                $ pcur -= 500
                $ fireball = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Ancient Map Piece 1" if ancmap1 == False:
            if pcur >= 1000:
                play sound "winner.mp3"

                "{i}Sensei has obtained the first piece of an ancient map!{/i}"

                if ancmap2 == True:
                    s "Hell yeah. Now I can finally go treasure hunting."
                else:
                    s "What am I supposed to do with this?"
                    q "Beats me. I just figured I could make a quick dime off of it."

                    "I should try and find the rest of the map..."

                $ pcur -= 1000
                $ ancmap1 = True

                jump travmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Sex Scene" if travsex == False:
            if pcur >= 1000000:
                play sound "winner.mp3"

                "{i}Sensei has obtained a coupon!{/i}"

                $ pcur -= 1000000
                $ travsex = True

                s "What is this? This is not sex."
                q "Of course it’s not sex. Did you seriously think you were going to be able to just buy your way into my pants?"
                q "The tutorial straight up told you there wasn’t any sex in this game. What the hell were you thinking? How long did you have to grind to even get this much PREMIUM CURRENCY?"
                s "A long time. I am so tired. Please give sex now."
                q "Not that kind of girl, pal. But that coupon will get you 10%% off at Tojo Ramen once you get out of here!"
                s "I’d rather take 10%% of your clothes off."
                q "Do you...want my tie as a consolation prize?"
                s "Can I have your underwear instead?"
                q "..."
                s "????????????"
                q "Please get out of my store."

                scene gameworld1 with fade

                "{i}You got kicked out of the store!{/i}"

                s "Gosh darn it."

                jump gameworldmainhub
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump travmenu

        "Go Back":
            scene gameworld1 with fade
            jump gameworldmainhub

###################
label roadsidemerchant:
    scene gameworld5
    with fade

    if roadbeen == False:
        q "Hey there, nyaa! Welcome to the shop, nyaa! First time in, nyaa?"
        s "Are you going to do that at the end of every sentence?"
        q "Would you like me to stop, nyaa?"
        s "Kind of, yeah."
        q "Praise the lord. If I had to do that one more time, I was probably going to claw my eyes out. So thanks to you, I won’t go blind!"
        s "As the hero who will save the world, I am happy to be of service. Now tell me, merchant — what is it you sell here?"
        q "Can you not read the graphic to my left? Did the developers forget to code it in or something?"
        s "I can read it. I just wasn’t sure if that would be meta-gaming or if you had to verbally tell me before I could conceive those words in-universe."
        q "Nope. Just look at the board, tell me what you want, then fork over the dough."
        s "Why is everything so expensive here?"
        q "Or complain too. That’s fine, I guess."
        s "You’re charging 800 PREMIUM CURRENCY for a bucket."
        q "It’s a good bucket. What do you want from me?"
        s "A cheaper bucket."
        q "For what? What do you even need that for?"
        s "I have no idea. I just got here. Everything is so fresh and new to me."
        q "Well, it’ll all make sense in due time why my prices seem a little high. But even if it doesn’t, I don’t have any competition! And if you’re going to advance, you’re going to {i}have{/i} to buy this stuff sooner or later."
        s "We’ll see about that, roadside merchant."
        q "So! Anything tickle your fancy right now? Or do you want to shop around for a bit? And by “a bit” I mean forever. Because, again, I’m the only girl with wares like these."

        $ roadbeen = True

    else:
        q "Hey there! Welcome back."
        q "What can I get for you?"

    "Right now, I have [pcur] PREMIUM CURRENCY."
    "What do I want to buy?"

    menu roadmenu:
        "Sword of Hope" if swordofhope == False:
            if pcur >= 500:
                play sound "winner.mp3"

                "{i}Sensei has obtained the {b}Sword of Hope!{/b}{/i}"

                $ pcur -= 500
                $ swordofhope = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Shield of Resistance" if shieldofresistance == False:
            if pcur >= 600:
                play sound "winner.mp3"

                "{i}Sensei has obtained the {b}Shield of Resistance!{/b}{/i}"

                $ pcur -= 600
                $ shieldofresistance = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Boots of Forgiveness" if bootsofforgiveness == False:
            if pcur >= 700:
                play sound "winner.mp3"

                "{i}Sensei has obtained the {b}Boots of Forgiveness!{/b}{/i}"

                $ pcur -= 700
                $ bootsofforgiveness = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Steel Bucket" if steelbucket == False:
            if pcur >= 800:
                play sound "winner.mp3"

                "{i}Sensei has obtained a {b}Steel Bucket!{/b}{/i}"

                $ pcur -= 800
                $ steelbucket = True

                q "Not so high and mighty now, are you?"
                s "I can’t believe I just paid 800 PREMIUM CURRENCY for a bucket."
                q "I can. It’s called capitalism, buddy. Supply and demand. There are no other buckets in Fucklador."
                s "I am overflowing with sadness."
                q "Well, at least now you’ve got a bucket to catch some of it!"

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Blowtorch" if blowtorch == False:
            if pcur >= 400:
                play sound "winner.mp3"

                "{i}Sensei has obtained a {b}Blowtorch!{/b}{/i}"

                $ pcur -= 400
                $ blowtorch = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Massage Oil" if massageoil == False:
            if pcur >= 350:
                play sound "winner.mp3"

                "{i}Sensei has obtained some {b}Massage Oil!{/b}{/i}"

                $ pcur -= 350
                $ massageoil = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Ancient Map Piece 2" if ancmap2 == False:
            if pcur >= 3000:
                play sound "winner.mp3"

                "{i}Sensei has obtained the second piece of an ancient map!{/i}"

                if ancmap1 == True:
                    s "Hell yeah. Now I can finally go treasure hunting."
                else:
                    s "What am I supposed to do with this?"
                    q "Beats me. I just figured I could make a quick dime off of it."

                    "I should try and find the rest of the map..."

                $ pcur -= 3000
                $ ancmap2 = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Profile Outfit: Nyaori" if nyaorifit == False:
            if pcur >= 3000:
                play sound "winner.mp3"

                "{i}A new profile outfit for Kaori has been unlocked!{/i}"

                $ pcur -= 3000
                $ nyaorifit = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Profile Outfit: Nyao" if nyaofit == False:
            if pcur >= 3000:
                play sound "winner.mp3"

                "{i}A new profile outfit for Nao-chan has been unlocked!{/i}"

                $ pcur -= 3000
                $ nyaofit = True

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Sex Scene" if roadsex == False:
            if pcur >= 1000000:
                play sound "winner.mp3"

                "{i}Sensei has obtained a stick!{/i}"

                $ pcur -= 1000000
                $ roadsex = True

                s "..."
                q "Is there a problem, dear customer?"
                s "I think there might be a printing error on your menu. This is not what I attempted to purchase."

                "I hold the stick out so she can see that it’s a stick and not sex."

                q "That seems like a quality piece of wood to me! May I ask what you were attempting to buy?"
                s "No. It’s too embarrassing."
                q "Well, how am I supposed to help if I don’t know what the error is?"
                s "Can’t you just look at my receipt?"
                q "Do you have a receipt?"
                s "It never printed."
                q "Then no, I can’t help you."
                q "But if you’re looking to sell that neat stick you’ve got there, I can give you...10 PREMIUM CURRENCY for it!"
                s "..."
                q "..."
                q "Fine. I’ll give you 15. But that’s my final offer."
                s "No..."
                s "I’ll just hang onto it..."

                jump roadmenu
            else:
                play sound "computerboo.mp3"

                "I only have [pcur] PREMIUM CURRENCY..."

                jump roadmenu

        "Go Back":
            scene gameworld1 with fade
            jump gameworldmainhub

    #########################
label fieldsofdespair:
    stop music fadeout 1.0
    scene gameworld6
    with fade
    play music "8aloelite.mp3" fadein 1.0

    if fieldsbeen == False:
        "{i}The Fields of Despair sprawl out for miles before you! Just look at how sad everything is!{/i}"

        s "This doesn’t look sad at all."

        "{i}Yes it does!{/i}"

        s "It’s just slimes."

        "{i}Nuh-uh. There’s some other stuff too. Just look at that guy in the suit back there. And- oh! I see a snail!{/i}"

        s "I guess that guy back there does look kind of sad now that you mention it."

        "{i}Told you! But anyway! The Fields of Despair are where you can grind for PREMIUM CURRENCY!{/i}"
        "{i}Each monster has its own weakness and monetary value!{/i}"
        "{i}In the final version of the game, these monsters will drop SUBPREMIUM CURRENCY which can be exchanged for PREMIUM CURRENCY at an exchange rate of 2:1 or RAINBOW COINS at 4:1!{/i}"
        "{i}SUBPREMIUM CURRENCY can also be purchased with real money.{/i}"

        s "Hold on, what the fuck are RAINBOW COINS?"

        "{i}An higher tier of PREMIUM CURRENCY that can be purchased in special bundles with RAINBOW QUARTZ!{/i}"

        s "Don’t you mean RAINBOW COINS?"

        "{i}No.{/i}"

        s "I hate this game."

        "{i}But we love you! And we definitely mean you! Not just your wallet!{/i}"
        "{i}Now, go! Grind! Earn your PREMIUM CURRENCY!{/i}"

        $ fieldsbeen = True

        jump fieldsmenu

    else:
        "Looks like I’m back here again..."
        "What shall I slay?"

        jump fieldsmenu

    menu fieldsmenu:
        "Pink Dogslime":
            jump pinkdogfight

        "Greenis":
            jump greenisfight

        "Blue Dogslime":
            jump bluedogfight

        "Herbal Slime":
            jump herbalfight

        "Common Snail":
            jump snailfight

        "Lavaslime":
            jump lavafight

        "Metal Dogslime":
            jump metalfight

        "Blobman":
            jump blobmanfight

        "Yogurt":
            jump yogurtfight

        "Suit Guy" if suitguyalive == True:
            scene gameworld8
            with fade

            "{i}You approach the man wearing a suit. His name is Kenji. He does not belong here.{/i}"
            "{i}He gazes out at the mountains, thinking back to the days when he would visit his grandparents in the countryside of Gifu. It all seems so distant now. {/i}"
            "{i}Kenji had been off the clock for several hours but, for some reason, he decided to stop here today instead of returning to his wife.{/i}"
            "{i}They had been fighting lately. Their marriage hadn’t been the same since he’d learned of her affair. But Kenji was spineless and couldn’t find the words to say to try and mend the rift.{/i}"
            "{i}His eyes hone in on a cardinal — his daughter’s favorite bird. She had passed away from a lengthy battle with leukemia just a few years ago. He visited her grave every Wednesday.{/i}"

            s "Why is there so much background information on this enemy mob?"

            scene gameworld9
            with dissolve2

            "{i}Kenji’s favorite number was nine. When he was younger, he had dreams of becoming a figure skater. But it was a dream that would be shattered along with his kneecap senior year of high school.{/i}"

            s "Jesus."

            "{i}He daydreams of the river — of dipping his toes in and feeling like a child again. And he remembers the games he would play with his brothers as the water washed over their feet.{/i}"
            "{i}He hadn’t seen any of them in years now either, but it wasn’t as if his relationship with them was strained. He was just never good at facing the past — and that’s all they were now.{/i}"

            s "Can I fight him now?"
            kenji "Why must we fight at all?"
            s "Oh, god. You gave him voice lines?"
            kenji "No matter how many times I fall, I’ll come right back. I think it’s...some kind of metaphor."
            s "..."
            kenji "Tell me, young man...what do you believe the meaning of life is?"

            scene gameworld10
            with dissolve2

            kenji "Are we put here to find happiness? Or are we only here to die?"
            kenji "Maybe there’s no reason at all now that I think about it. Maybe this is all just the result of some fortunate coincidence. And maybe these experiences and lives we lead will be just as fleeting as our fading youth."
            s "..."
            kenji "You seek the {b}Four Orbs of Power{/b}, don’t you?"
            kenji "Ha...I remember when I set off on my journey as well."
            kenji "I’d just registered at the Adventurer’s Guild...my eyes were still so bright and full of hope back then."
            kenji "But now, I don’t even have eyes."
            kenji "My...time surely does fly, doesn’t it?"
            s "..."
            kenji "Tell me...when you find the {b}Four Orbs of Power...{/b}what do you intend to do? And if your answer is “find my family” or anything along those lines, let me reassure you...they’re safe and sound."
            kenji "They were never in any danger at all. That’s just a lie the game masters tell us to push us forward. To buy more PREMIUM CURRENCY out of fear that they’ll be harmed. But it’s all just manipulation."
            kenji "We exist to line their pockets...they don’t even think of us as human."
            kenji "But you’re different...you still have a chance. {i}You{/i} can be the one to break us out of this cycle."
            kenji "So...what do you say, young man? Do you have what it takes to save us?"
            kenji "Where will your journey lead you from here?"

            menu:
                "Push":
                    scene gameworld11
                    with dissolve
                    with hpunch

                    s "..."

            "{i}Kenji plunges down the cliff! His body collides with jagged rocks along the way and you can see them tear him open in various places.{/i}"
            "{i}Countless memories topple down with him. Visions of his daughter. Conversations at the dinner table with his wife. Family dinners. Soccer games. It’s all gone now. And it’s all your fault.{/i}"
            "{i}You also don’t collect any PREMIUM CURRENCY as you would need to climb to the bottom of the cliff to loot his body.{/i}"

            s "..."

            $ suitguyalive = False

            scene black
            with dissolve2

            s "Guess I’ll just keep grinding then..."

            play sound "static.mp3"
            scene gameworld6 with flash
            stop sound

            s "Oh, look. He’s back now."

            "{i}Please be advised — Sensei-Quest is still in early access! Just pretend his model is gone for now!{/i}"

            s "What should I fight against next?"

            jump fieldsmenu

        "Return to Fucklador":
            stop music fadeout 1.0
            scene black
            with dissolve2
            scene gameworld1
            with dissolve2
            play music "8pox.mp3" fadein 1.0

            jump gameworldmainhub

#########################
label pinkdogfight:
    scene gameworldpink with fade
    play sound "battlestart.mp3"

    "{i}Pink Dogslime has appeared!{/i}"

    menu pinkslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}Now he’s all gooey...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Pink Dogslime is now pregnant...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Why?...{/i}"
                    with hpunch
                    "{i}Pink Dogslime is wandering around aimlessly...{/i}"

                    jump pinkslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Pink Dogslime is wandering around aimlessly...{/i}"

            jump pinkslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label greenisfight:
    scene gameworldgreenis with fade
    play sound "battlestart.mp3"

    "{i}Greenis has appeared!{/i}"

    menu greenisfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    scene black
                    play sound "explosion.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Greenis is getting ready to explode!{/i}"

                    jump greenisfightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Greenis is getting ready to explode!{/i}"

                    jump greenisfightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Greenis is getting ready to explode!{/i}"

                    jump greenisfightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Greenis is getting ready to explode!{/i}"

                    jump greenisfightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"

                    scene black
                    play sound "explosion.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Greenis is getting ready to explode!{/i}"

                    jump greenisfightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 40

                    "{i}Sensei has earned 40 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"

                    scene black
                    play sound "explosion.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Greenis shivers with delight!{/i}"
                    play sound "explosion.mp3"
                    scene gameworld7 with hpunch

                    "{i}And then it explodes?{/i}"

                    play sound "coins.mp3"

                    $ pcur += 40

                    "{i}Sensei has earned 40 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Greenis is getting ready to explode!{/i}"

            jump greenisfightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label bluedogfight:
    scene gameworldblue with fade
    play sound "battlestart.mp3"

    "{i}Blue Dogslime has appeared!{/i}"

    menu blueslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}Now he’s all gooey...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Blue Dogslime is now pregnant...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Why?...{/i}"
                    with hpunch
                    "{i}Blue Dogslime is wandering around aimlessly...{/i}"

                    jump blueslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Blue Dogslime is wandering around aimlessly...{/i}"

            jump blueslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label herbalfight:
    scene gameworldherbal with fade
    play sound "battlestart.mp3"

    "{i}Herbal Slime has appeared!{/i}"

    menu herbalslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Herbal Slime is about to give birth!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It dies before it can!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 15

                    "{i}Sensei has earned 15 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 15

                    "{i}Sensei has earned 15 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 15

                    "{i}Sensei has earned 15 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Why?...{/i}"
                    with hpunch
                    "{i}Herbal Slime lets out a pleasant aroma!{/i}"

                    jump herbalslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Herbal Slime lets out a pleasant aroma!{/i}"

            jump herbalslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label snailfight:
    scene gameworldsnail with fade
    play sound "battlestart.mp3"

    "{i}Common Snail has appeared! Run for your life!{/i}"

    menu snailfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 5

                    "{i}Sensei has earned 5 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail.{/i}"

                    jump snailfightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail.{/i}"

                    jump snailfightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail.{/i}"

                    jump snailfightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail.{/i}"

                    jump snailfightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Common Snail is now pregnant...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail. A pregnant one.{/i}"

                    jump snailfightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 5

                    "{i}Sensei has earned 5 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 1

                    "{i}Sensei has earned 1 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 1

                    "{i}Sensei has earned 1 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Why?...{/i}"
                    with hpunch
                    "{i}Common Snail just...continues being a snail.{/i}"

                    jump snailfightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Common Snail just...continues being a snail.{/i}"

            jump snailfightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label lavafight:
    scene gameworldlava with fade
    play sound "battlestart.mp3"

    "{i}Lavaslime has appeared!{/i}"

    menu lavaslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    scene black
                    play sound "slayed.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 20

                    "{i}Sensei has earned 20 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    scene black
                    play sound "slayed.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}It burned up immediately...{/i}"
                    with hpunch
                    "{i}Lavaslime is getting hot!{/i}"

                    jump lavaslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Lavaslime is getting hot!{/i}"

            jump lavaslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label metalfight:
    scene gameworldmetal with fade
    play sound "battlestart.mp3"

    "{i}Metal Dogslime has appeared!{/i}"

    menu metalslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 100

                    "{i}Sensei has earned 100 PREMIUM CURRENCY! Jackpot!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

                    jump metalslimefightmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Metal Dogslime is so shiny now!{/i}"
                    with hpunch
                    "{i}Metal Dogslime is huge and hard and shiny and ready to fuck!{/i}"

                    jump metalslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Metal Dogslime is huge and hard and ready to fuck!{/i}"

            jump metalslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label blobmanfight:
    scene gameworldblob with fade
    play sound "battlestart.mp3"

    "{i}Blobman has appeared!{/i}"

    menu blobmanfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    scene black
                    play sound "slayed.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED!{/i}"

                    jump blobmanfightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED!{/i}"

                    jump blobmanfightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED!{/i}"

                    jump blobmanfightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED! But slightly cleaner now!{/i}"

                    jump blobmanfightmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED!{/i}"

                    jump blobmanfightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Blobman is PISSED!{/i}"

                    jump blobmanfightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 50

                    "{i}Sensei has earned 50 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 50

                    "{i}Sensei has earned 50 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"

                    scene black
                    play sound "slayed.mp3"

                    "{i}Sensei died...{/i}"

                    scene gameworld1
                    with dissolve2

                    "{i}You somehow manage to respawn in Fucklador.{/i}"
                    "{i}Your hospital bill will be sent to you later.{/i}"

                    jump gameworldmainhub

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"

            scene black
            play sound "slayed.mp3"

            "{i}But it’s not enough! Blobman still wins!{/i}"
            "{i}Sensei dies...{/i}"

            scene gameworld1
            with dissolve2

            "{i}You somehow manage to respawn in Fucklador.{/i}"
            "{i}Your hospital bill will be sent to you later.{/i}"

            jump gameworldmainhub

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

label yogurtfight:
    scene gameworldyogurt with fade
    play sound "battlestart.mp3"

    "{i}Yogurt has appeared!{/i}"

    menu yogurtslimefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}He’s covered in yogurt now! Delicious!{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    play sound "slayed.mp3"
                    scene gameworld7 with hpunch

                    "{i}It was super effective!{/i}"

                    play sound "coins.mp3"

                    $ pcur += 10

                    "{i}Sensei has earned 10 PREMIUM CURRENCY!{/i}"

                    scene gameworld6
                    with fade

                    jump fieldsmenu

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}Nothing happened...{/i}"
                    with hpunch
                    "{i}Yogurt is packed full of probiotics!{/i}"

                    jump yogurtslimefightmenu

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    "{i}Why?...{/i}"
                    with hpunch
                    "{i}Yogurt is confused!{/i}"

                    jump yogurtslimefightmenu

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"
            "{i}Yogurt is packed full of probiotics!{/i}"

            jump yogurtslimefightmenu

        "Run Away":
            play sound "escape.mp3"
            scene gameworld6 with fade

            "{i}Sensei has escaped!{/i}"

            s "That was close! [[INSERT ENEMY NAME HERE] almost got me!"

            jump fieldsmenu

    #########################
label seaofstairs:
    stop music fadeout 3.0
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene gameworld12
    with dissolve2
    play music "8faster.mp3"
    $ renpy.pause(3, hard=True)
    scene gameworld13
    with dissolve2
    $ netkillpts = 0

    "{i}Net With Knife Nose & Melon Mouth appeared!{/i}"

    if knifeseen == True:
        net "This again? Just go away."
        s "No! I must obtain the Four Orbs of Power!"
        net "It would make more sense if there were only {i}three{/i} orbs of power as that number corresponds directly to the amount of frequently recurring gods in Lessons in Love that-"
        s "Silence, Net With Knife Nose & Melon Mouth! Your time ends now!"
    else:
        net "So...we meet again."
        s "Again?"
        net "Yeah."
        s "I don’t remember you."
        net "Really?"
        s "Yeah. Who are you?"
        net "One of the first “curious objects” to ever appear to you. I’m the one who’s really into the lore, remember?"
        s "Oh. Well, are we going to fight or do you just want to hand over your Orb of Power?"
        net "Just as before, I’m acting as a guardian. I can’t let you pass unless you prove yourself worthy."
        net "Please answer the following questions correctly in order to pass."
        net "When Yumi is first seen on the beach-"

        play sound "sword.mp3"
        with hpunch

        s "Yah!"
        net "Woah. What are you doing?"
        s "I have no time for any more quizzes! Taste my blade and all of the abilities I have collected!"
        net "I’ll make you regret ever challenging me, heathen."

        $ knifeseen = True

label netfight:
    $ config.rollback_enabled = False

    if senseidamage > 30:
        stop music fadeout 5.0
        s "Ngh..."
        net "This is the end for you, Akira."
        net "You were never meant for this place."
        s "I can’t...go on..."

        play sound "tackle.mp3"
        scene black
        with hpunch

        "{i}Sensei collapses to the ground!{/i}"
        "{i}He has failed...{/i}"
        "........."
        "......"
        "..."

        scene gameworld1
        with dissolve2
        play music "8pox.mp3"

        $ senseidamage = 0

        "{i}You somehow manage to respawn in Fucklador.{/i}"
        "{i}Your hospital bill will be sent to you later.{/i}"

        $ config.rollback_enabled = True

        jump gameworldmainhub

    else:
        jump netfightmenu

    menu netfightmenu:
        "Attack":
            menu:
                "Tackle":
                    if netkillpts == 3 and swordofhope == True:
                        "{i}Sensei used Tackle!{/i}"
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                        net "Heh. It’s amusing how you still think you can hit me after I’ve dodged so many of your attacks already."
                        s "It {i}would{/i} be amusing..."
                        s "If I didn’t have another trick up my sleeve!"
                        net "What?"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei launches a second attack with the Sword of Hope!{/i}"

                        play sound "stab.mp3"
                        with hpunch

                        net "Ngh!"
                        s "Hmph."
                        net "Of all the...weapons to slay me with..."
                        net "It had to be...that one..."

                        play sound "slayed.mp3"
                        scene gameworld12 with hpunch

                        "{i}Net With Knife Nose & Melon Mouth has fallen!{/i}"

                        play sound "winner.mp3"

                        "{i}Sensei has obtained the {b}Orb of Plant!{/b}{/i}"

                        net "Please...promise me that-"

                        scene black
                        with dissolve
                        stop music fadeout 10.0

                        s "I don’t make promises to my enemies."
                        net "But I have never been your-"
                        s "You stabbed me like a million times, dude."
                        net "..."
                        s "Peace out, man."
                        net "Goodbye...Akira..."

                        scene gameworld1
                        with dissolve2
                        play music "8pox.mp3"

                        $ senseidamage = 0
                        $ plantorb = True
                        $ config.rollback_enabled = True

                        s "I am stronger now than I was before!"

                        "{i}Not really. You just have an extra key item now.{/i}"

                        s "Shut up, secret narrator."

                        jump gameworldmainhub

                    else:
                        "{i}Sensei used Tackle!{/i}"
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                        play sound "sword.mp3"
                        "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                        play sound "stab.mp3"
                        "{i}Sensei has taken 10 Damage!{/i}"

                        $ senseidamage += 10

                        jump netfight

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Fire Ball" if fireball == True:
                    if netkillpts == 2:
                        "{i}Sensei used Fire Ball!{/i}"
                        with hpunch
                        "{i}It’s a direct hit! The enemy is burning!{/i}"
                        net "Tch! I see now..."
                        net "You used the massage oil to cover me in grease that you could set ablaze with Fire Ball. A genius move, Akira."
                        s "Yeah. That’s exactly what I was trying to do. Now, give me your orb!"
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Net With Knife Nose & Melon Mouth extinguishes the fire!{/i}"
                        net "Over my dead melon..."
                        play sound "sword.mp3"
                        "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                        play sound "stab.mp3"
                        "{i}Sensei has taken 10 Damage!{/i}"

                        $ senseidamage += 10

                        $ netkillpts += 1

                        jump netfight

                    else:
                        "{i}Sensei used Fire Ball!{/i}"
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                        play sound "sword.mp3"
                        "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                        play sound "stab.mp3"
                        "{i}Sensei has taken 10 Damage!{/i}"

                        $ senseidamage += 10

                        jump netfight

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                    play sound "sword.mp3"
                    "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                    play sound "stab.mp3"
                    "{i}Sensei has taken 10 Damage!{/i}"

                    $ senseidamage += 10

                    jump netfight

                "Use...Massage Oil?" if massageoil == True:
                    if netkillpts == 1:
                        "{i}Sensei used massage oil!{/i}"
                        with hpunch

                        net "What the-"
                        s "I hope you like massages, because you’re about to be rubbed out!"
                        net "Aren’t we fighting? Why would you just pour oil on me like that? I’m a net. I don’t even have muscles. This accomplishes nothing."
                        s "We’ll see about that, Net With Knife Nose & Melon Mouth!"
                        net "Bruh."
                        play sound "sword.mp3"
                        "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                        play sound "stab.mp3"
                        "{i}Sensei has taken 10 Damage!{/i}"

                        $ senseidamage += 10
                        $ netkillpts += 1

                        jump netfight

                    else:
                        "{i}Sensei used massage oil!{/i}"
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Net With Knife Nose & Melon Mouth manages to dodge the attack!{/i}"
                        play sound "sword.mp3"
                        "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                        play sound "stab.mp3"
                        "{i}Sensei has taken 10 Damage!{/i}"

                        $ senseidamage += 10

                        jump netfight

        "Guard":
            if netkillpts == 0:
                play sound "guard.mp3"
                "{i}Sensei protects himself!{/i}"
                play sound "sword.mp3"
                "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                play sound "dodge.mp3"
                with hpunch
                "{i}Sensei dodges the attack!{/i}"

                $ netkillpts += 1

                net "Not bad. That’s the last time that will work on me, though."
                s "We’ll see about that, Net With Knife Nose & Melon Mouth."
                net "Just call me Net, dude."
                s "Shut up, Net With Knife Nose & Melon Mouth! Taste my blade!"

                jump netfight

            else:
                play sound "guard.mp3"
                "{i}Sensei protects himself!{/i}"
                play sound "sword.mp3"
                "{i}Net With Knife Nose & Melon Mouth attacks with his noseblade!{/i}"
                play sound "stab.mp3"
                "{i}It’s no use! Sensei has taken 10 Damage anyway!{/i}"

                $ senseidamage += 10

                jump netfight

    #########################
label bedlehem:
    stop music fadeout 3.0
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene gameworld14
    with dissolve2
    play music "8faster.mp3"
    $ renpy.pause(3, hard=True)
    scene gameworld15
    with dissolve2
    $ mannykillpts = 0

    "{i}Manny the Unfriendly Maggot appeared!{/i}"

    if mannyseen == True:
        manny "You never learn, do you?"
        s "I’ll surely defeat you this time, former friend."
        manny "Listen man, since we used to be on good terms, why don’t I just let you in on a little hint about what will happen if you miraculously {i}do{/i} manage to kick my ass."
        manny "Nothing’s going to get any better. Even if you collect the Four Orbs of Power, using them to summon the final boss just sets you up for an even {i}worse{/i} death."
        s "But I know I will win, Manfred."
        manny "Don’t call me that. And how do you know you’ll win?"
        s "Because..."

        with hpunch

        s "{b}THIS GAME IS NAMED AFTER ME!{/b}"

        jump mannyfightmenu

    else:
        s "Manny? What are you doing here? And who programmed my bedroom into Sensei-Quest?"
        manny "You’ve been gone a long time, Sensei. Many things have happened. And {i}I{/i} am the ruler of this realm now."
        s "{i}No!{/i}"
        manny "I’ve been fucking your girlfriend too."
        s "Which one?"
        manny "Wait, how many do you have?"
        s "I don’t know, man. I’ve lost count."
        manny "Well, I’m talking about the rubber one with that hole in it that you keep on the top shelf."
        s "Oh, so like none of the human girls?"
        manny "Nah, they’re all dead now. Sensei-Quest takes place in the year 5382."
        s "Jesus."
        manny "I had a threesome with one of the dorms before everyone died, though."
        s "Really? Which one?"
        manny "I’m not really sure. I haven’t grown any eyes yet. Just a bunch of these Bolwig organ things. Which really sucks because it makes me think I’m going to be a maggot forever."
        s "Is that why you’re so unfriendly now?"
        manny "Part of it, yeah."
        s "That makes sense. It’s really good to see you, though. You’ve grown a lot."
        manny "Thanks, man. You look good too."
        s "So, can I have the Orb of Presumably Worm or do I actually have to fight you for it?"
        manny "You’ve gotta fight me for it. Sorry, dude. Honest truth is I’ve had it ever since A Life of Prizes. It’s what gives me the ability to speak. And I’ve got a girlfriend now. I won’t let you steal my voice."
        s "Then...it looks like the time has come..."
        s "For me to be Unfriendly Sensei!"
        manny "That was lame as fuck, dude. Please just go home."
        s "I’M ALREADY HERE!"

        $ mannyseen = True

        jump mannyfightmenu

label mannyfight:
    $ config.rollback_enabled = False

    if senseidamage > 30:
        stop music fadeout 5.0

        s "Ngh!"
        manny "You made me do this, former friend. But hey, on the bright side, at least you get to respawn. So you should use that opportunity to do something more productive with-"
        s "I’ll...be back..."
        manny "Please don’t."

        play sound "tackle.mp3"
        scene black
        with hpunch

        "{i}Sensei collapses to the ground!{/i}"
        "{i}He has failed...{/i}"
        "........."
        "......"
        "..."

        scene gameworld1
        with dissolve2
        play music "8pox.mp3"

        $ senseidamage = 0

        "{i}You somehow manage to respawn in Fucklador.{/i}"
        "{i}Your hospital bill will be sent to you later.{/i}"

        $ config.rollback_enabled = True

        jump gameworldmainhub

    else:
        jump mannyfightmenu

    menu mannyfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"

                    if mannykillpts == 0:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot attempts to deflect the blow, but fails!{/i}"

                        manny "What the fuck? Since when are you venomous?"
                        s "Since that girl at the tavern rewrote my genetic structure for the low cost of 50 PREMIUM CURRENCY."
                        manny "You’re lucky you’re allowed to wander around. And also that you’re able to hold more than one spell at a time. All I know is Bolwig Blast."
                        s "More like Bullshit Blast. You can’t hurt me."
                        manny "I’d actually prefer Bullshit Blast. That hits way harder. I think I need to evolve first, though."

                        play sound "explosion.mp3"
                        with hpunch

                        "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"

                        manny "See? Not that bad, right?"
                        s "Not at all..."

                        "{i}Sensei has taken 10 damage!{/i}"

                        s "It only took a third of my HP away."
                        manny "Jesus, how squishy are you?"

                        $ senseidamage += 10
                        $ mannykillpts += 1

                        jump mannyfight

                    else:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                        play sound "explosion.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        jump mannyfight

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"

                    if mannykillpts == 2:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot attempts to deflect the blow, but the bubbles get into his Bolwig organs!{/i}"

                        manny "Fuck. This is going to make detecting light so much harder."
                        s "Is that a {b}HINT{/b} I hear?"
                        manny "What? No. It’s just literally harder to detect light now. Stop fighting like a bitch and just tackle me or something."
                        s "And risk getting Bolwig Blasted? No thanks. I’ll stick to my bubbles and salt and venom, thank you very much."
                        manny "Tch..."

                        "{i}Your barrage of various chemicals has weakened Manny the Unfriendly Maggot!{/i}"
                        "{i}He is {b}Stunned{/b} until next turn...{/i}"

                        s "Hell yeah."
                        manny "Hell no."

                        $ mannykillpts += 1

                        jump mannyfight

                    else:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                        play sound "explosion.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10

                        jump mannyfight

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the...sex?{/i}"

                    manny "Ew, dude. I never realized you looked at me that way."
                    s "I’m doing it for the sake of battle!"
                    manny "Well, stop."

                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"

                    if mannykillpts == 1:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot is unable to block Sensei’s Salt Spray!{/i}"

                        manny "First venom, now salt? What the hell is this fighting style, man?"
                        s "You know what they say about venom and salt, Manny."
                        manny "........No?"
                        s "They’re highly effective against larvae."
                        manny "Literally no one has ever said that. You’re probably thinking of slugs. But even then, I don’t think venom has any effect on-"

                        "{i}Sensei used Salt Spray again!{/i}"
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot is unable to block Sensei’s Salt Spray!{/i}"

                        manny "Dude, knock it off."
                        s "Hell no. It’s working."
                        manny "Well, it’s not going to work anymore."

                        play sound "computeryay.mp3"
                        with hpunch

                        "{i}Manny the Unfriendly Maggot has developed an immunity to Salt Spray thanks to his {b}Thicc Skin.{/b}"

                        s "You do look pretty thicc."
                        manny "And you look pretty dead."

                        play sound "explosion.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10
                        $ mannykillpts += 1

                        jump mannyfight

                    else:
                        play sound "guard.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                        play sound "explosion.mp3"
                        with hpunch
                        "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10

                        jump mannyfight

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot deflects the blow!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump mannyfight

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    play sound "guard.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot hates massages!{/i}"
                    play sound "explosion.mp3"
                    with hpunch
                    "{i}Manny the Unfriendly Maggot casts Empowered Bolwig Blast!{/i}"
                    "{i}It’s a critical hit!{/i}"
                    "{i}Sensei has taken 20 damage!{/i}"

                    $ senseidamage += 20

                    jump mannyfight

        "Guard":
            if mannykillpts == 3 and shieldofresistance == True:
                play sound "guard.mp3"
                "{i}Sensei protects himself!{/i}"
                play sound "explosion.mp3"
                "{i}Manny the Unfriendly Maggot casts {b}BOTFLY INVASION!{/b}"

                s "Woah! What the fuck is that move? You said you only had one!"
                manny "Racial passive. All maggots have it. Doesn’t count toward my ability total."
                s "Tch!"

                play sound "slap.mp3"
                with hpunch

                "{i}A horde of botflies begin to slap Sensei around!{/i}"

                s "Why do they all have hands?!"
                manny "Dude, ask the developers. I don’t know. I barely ever use this- wait. What’s that glow?"

                play sound "guard.mp3"
                with hpunch

                "{i}Sensei’s {b}Shield of Resistance{/b} is letting out a blinding light!{/i}"

                s "That glow...is the glow of perseverance! Also, you said you wouldn’t be able to detect light anymore! I knew it was a hint!"
                manny "I just said it would be harder. I didn’t say-"

                play sound "explosion.mp3"
                with flash
                with hpunch

                "{i}{b}Shield of Resistance acts by itself! It casts {b}Ray of Perseverance{/b}!{/i}"

                s "See?! I’ve been right all along!"

                manny "Ngh! I can’t...take any more!"

                play sound "slayed.mp3"
                scene gameworld14 with hpunch

                "{i}Manny the Unfriendly Maggot has been slain!{/i}"

                play sound "winner.mp3"

                "{i}Sensei has obtained the {b}Orb of Worm{/b}!{/i}"

                s "Now {i}I{/i} will be able to cast Botfly Invasion as well..."
                manny "First off...no you won’t..."
                manny "But second...shouldn’t you be more excited about the fact that you’ve obtained an Orb of Power?"
                s "I want to be...but I had to kill a friend in the process."

                "{i}Manny the Unfriendly Maggot begins to dissolve into some weird green goop.{/i}"

                scene black
                with dissolve2
                stop music fadeout 10.0

                manny "Tell...my girlfriend...I love her..."
                s "I’ll do you one better than that, Manny."
                s "I’ll love her {i}for{/i} you."
                manny "Please...don’t..."

                play sound "winner.mp3"

                "{i}Sensei has obtained {b}Manny the Unfriendly Maggot’s Girlfriend{/b}!{/i}"

                manny "You...motherfucker..."

                scene gameworld1
                with dissolve2
                play music "8pox.mp3"

                $ senseidamage = 0
                $ wormorb = True
                $ config.rollback_enabled = True

                s "I must continue my journey!"
                s "To greater heights I climb!"

                jump gameworldmainhub

            else:
                play sound "guard.mp3"
                "{i}Sensei protects himself!{/i}"
                play sound "explosion.mp3"
                with hpunch
                "{i}Manny the Unfriendly Maggot casts Bolwig Blast!{/i}"
                "{i}Sensei has taken 10 damage! He totally sucks at guarding!{/i}"

                s "Hey..."

                $ senseidamage += 10

                jump mannyfight

    #########################
label palaceofthefist:

    stop music fadeout 3.0
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene gameworld16
    with dissolve2
    play music "8faster.mp3"
    $ renpy.pause(3, hard=True)
    scene gameworld17
    with dissolve2
    $ karatekillpts = 0

    "{i}Random Karate Person appeared!{/i}"

    if karateseen == True:
        rand "So you’ve decided to give it another try, I see."
        s "You’re not the only one who’s been training, Random Karate Person."
        rand "I sure hope that’s the case. Because the pathetic display of combat skills you showed off in our last bout was nothing short of child’s play."
        s "Well, you don’t have to be a dick about it. I’m trying really hard. This puzzle is weird."
        rand "Not as weird as the hairy frog."
        s "The what?"
        rand "The one that sneaks in the night — floating by like a log on a larger log."
        s "Okay, I’m just going to fight you now."

        jump karatefight

    else:
        rand "Well, well, well...look who finally decided to return home."
        s "You know, I knew from the moment I first encountered you that you were going to be a boss I’d have to defeat for a key item in a presumably delusional RPG one day."
        rand "I highly doubt the accuracy of that statement. But I welcome you back nonetheless as I’ve been eagerly awaiting the day we cross swords."
        s "Are we even allowed to use swords in karate?"
        rand "It was merely a figure of speech — another way to say the cicada always catches its breakfast on Fish Day."
        s "What?"
        rand "Karate is no different from a blade of grass that never found its way home. Or a smile that has just learned how to frown."
        s "Oh, I get it. You’re supposed to be wise or something, but the writer of this game isn’t very good."
        rand "Or I have merely transcended human knowledge and can now speak on a level that only {b}Enlightened Ones{/b} can understand."
        s "I want to doubt you, but that bolded text is making me think twice."
        rand "You stand no chance against me, Sensei. But seeing as this is an open competition, I will not refuse your challenge. But also know that I will not hold back."

        "{i}Random Karate Person takes a step forward! But the model doesn’t move. Just pretend.{/i}"

        rand "Today will be the first day of the rest of your life...and the last day of your third week in Cancun!"
        s "???????????????"

        play sound "dodge.mp3"
        with hpunch

        "{i}Random Karate Person swings his fist!{/i}"
        "{i}Sensei narrowly dodges the attack!{/i}"

        $ karateseen = True

        jump karatefight

label karatefight:
    $ config.rollback_enabled = False

    if senseidamage > 30:
        stop music fadeout 5.0

        s "Ngh..."
        rand "Is that all you’ve got, weakling?"
        s "Your fists are just so...full of fist-energy..."
        rand "Like the hummingbird’s belt, I {i}am{/i} the Wheel of Fortune."

        play sound "tackle.mp3"
        scene black
        with hpunch

        s "One day...I will understand!"

        "{i}Sensei collapses to the ground!{/i}"
        "{i}He has failed...{/i}"
        "........."
        "......"
        "..."

        scene gameworld1
        with dissolve2
        play music "8pox.mp3"

        $ senseidamage = 0

        "{i}You somehow manage to respawn in Fucklador.{/i}"
        "{i}Your hospital bill will be sent to you later.{/i}"

        $ config.rollback_enabled = True

        jump gameworldmainhub

    else:
        jump karatefightmenu

    menu karatefightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    if karatekillpts == 3 and swordofhope == True:
                        rand "Again? Give it up, Sensei."

                        play sound "dodge.mp3"
                        with hpunch

                        "{i}Random Karate Person dodges the attack with ease!{/i}"

                        s "How are you so fast?!"
                        rand "Years of training my fists and feet — like a meadow swallowing goldfish."
                        s "Yeah, well...while you were training your fists and feet, I was studying the blade!"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei swings the Sword of Hope!{/i}"

                        rand "What?!"

                        play sound "stab.mp3"
                        with hpunch
                        $ renpy.pause(0.4, hard=True)
                        play sound "thump.mp3"
                        scene gameworld16 with hpunch

                        rand "YOU ACTUALLY USED A FUCKING SWORD?! ARE YOU INSANE?!"
                        s "YOU TOLD ME WE WERE GOING TO CROSS THEM AND YOU DIDN’T EVEN BRING ONE!"
                        rand "I TOLD YOU IT WAS A FIGURE OF SPEECH, IDIOT! THIS IS SUPPOSED TO BE A FAIR FIGHT! HOW AM I SUPPOSED TO-"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei swings the Sword of Hope again!{/i}"

                        rand "PLEASE, STOP!"

                        play sound "slayed.mp3"
                        with hpunch

                        "{i}Sensei has decapitated Random Karate Person!{/i}"

                        s "At least {i}this{/i} purchase is giving me a better return on my investment than my Boots of Ass."

                        scene black
                        with dissolve2
                        stop music fadeout 10.0

                        "{i}Sensei swings his sword once more, cleaning the blood off his blade as he reaches down and plucks the {b}Orb of Fist{/b} from Random Karate Person’s pocket!{/i}"

                        play sound "winner.mp3"

                        "{i}Sensei has obtained the Orb of Fist!{/i}"

                        $ fistorb = True
                        $ senseidamage = 0
                        $ config.rollback_enabled = True

                        s "I’m going to fist so many girls when I get home."

                        scene gameworld1
                        with dissolve2
                        play music "8pox.mp3"

                        "{i}Little did he know, it would take a lot more than an Orb of Power to get his fist inside some of the girls he hangs around.{/i}"

                        s "So...now what should I do?"

                        jump gameworldmainhub

                    else:
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Random Karate Person dodges the attack with ease!{/i}"
                        rand "Pathetic!"
                        play sound "punch.mp3"
                        with hpunch
                        "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10

                        jump karatefight

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"

                    if karatekillpts == 0:
                        s "First rule of karate — fight yellow with yellow!"

                        play sound "dodge.mp3"
                        with hpunch

                        rand "Nice try, but-"

                        "{i}Sensei’s Banana Blast is empowered by his cool dialogue!{/i}"

                        rand "What?"

                        play sound "punch.mp3"
                        with hpunch

                        "{i}It’s a hit!{/i}"

                        rand "..."
                        s "Never underestimate the effect potassium can have on one’s body."
                        rand "Your words ring true — like the bell that summons the great frog. Or a leaf, blowing carelessly through the halls of a pet store."
                        rand "Your pitiful tricks won’t work more than once, though. Like a missing platypus, you lack the technique to make the trees lose sight of the bugs that live beneath them."
                        rand "Also, you have the rules of karate wrong."
                        s "I do? What’s the actual first rule then?"
                        rand "It begins and ends with respect!"

                        play sound "punch.mp3"
                        with hpunch
                        "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10
                        $ karatekillpts += 1

                        s "That wasn’t respectful at all! In fact, you’ve been disrespecting me pretty much this whole time!"
                        rand "Rules are little more than wet socks in summer!"

                        jump karatefight

                    else:
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Random Karate Person dodges the attack with ease!{/i}"
                        rand "Pathetic!"
                        play sound "punch.mp3"
                        with hpunch
                        "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10

                        jump karatefight

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"

                    if karatekillpts == 2:
                        "{i}Random Karate Person stands there and lets it happen!{/i}"

                        s "..."
                        rand "..."
                        s "Ew. This is weird now."
                        rand "Thank you for taking the time to wash me. It is important to practice personal hygiene, especially after working up a sweat."
                        s "This is supposed to be an attack. You’re not supposed to enjoy it."
                        rand "I see that, all these years later, you still don’t know the first thing of martial arts."
                        s "Sure I do. Didn’t you see what I did with those bananas earlier?"
                        rand "I did. But if your idea of an “attack” is to gingerly rub sanitizing solution all over my muscular body, I believe there is a disconnect between you and the ideas of true strength."
                        s "Gross, is that really what I’ve been doing this whole time? Without any attack animations, I kind of figured it was just a beam or something."

                        play sound "dodge.mp3"
                        with hpunch

                        "{i}Random Karate Person dodges backwards!{/i}"

                        rand "A beam is just some sort of ray."
                        s "That...That one’s accurate, yeah. That’s what a beam is."
                        rand "And a ray is nothing more than a deer without its day."
                        s "And I’m lost again."
                        rand "No, Akira..."
                        rand "You {i}have{/i} lost again!"

                        play sound "punch.mp3"
                        with hpunch
                        "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ karatekillpts += 1
                        $ senseidamage += 10

                        jump karatefight

                    else:
                        play sound "dodge.mp3"
                        with hpunch
                        "{i}Random Karate Person dodges the attack with ease!{/i}"
                        rand "Pathetic!"
                        play sound "punch.mp3"
                        with hpunch
                        "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                        "{i}Sensei has taken 10 damage!{/i}"

                        $ senseidamage += 10

                        jump karatefight

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"
                    play sound "dodge.mp3"
                    with hpunch
                    "{i}Random Karate Person dodges the attack with ease!{/i}"
                    rand "Pathetic!"
                    play sound "punch.mp3"
                    with hpunch
                    "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                    "{i}Sensei has taken 10 damage!{/i}"

                    $ senseidamage += 10

                    jump karatefight

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"

            if karatekillpts == 1 and bootsofforgiveness == True:
                "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                play sound "dodge.mp3"
                "{i}Sensei dodges the attack thanks to his Boots of Forgiveness — which have finally decided to work!{/i}"

                s "About time."
                rand "How strange. No one has ever dodged that attack before. How did you do it?"
                s "An adventurer never reveals his secrets, Random Karate Person."
                rand "You bought the Boots of Forgiveness, didn’t you?"
                s "What? How did you-"
                rand "Because {i}I’m{/i} the one who made them."
                s "This is a plot twist I was both not expecting and don’t fully understand."
                rand "They’re made of my skin."
                s "Ew! What? I’m wearing boots made with human flesh?"
                rand "Just the extra flesh from my ass."
                s "I’m wearing ass boots?!"
                rand "Ass boots...{i}of forgiveness.{/i} And I {i}forgive{/i} you for purchasing them as they were stolen from me years ago by a former pupil of mine."
                s "So, like...how exactly do these boots allow me to dodge your-"

                play sound "punch.mp3"
                with hpunch
                "{i}Random Karate Person attacks with Fist of Polaris!{/i}"
                "{i}Sensei has taken 10 damage!{/i}"

                $ senseidamage += 10

                s "Ow! Wait your turn!"
                rand "The boots can read my mind. But I am severing my mental connection with them now. Your tricks are now as useless as a monkey wrench in a casserole."
                s "I can’t believe I’m still wearing these..."

                $ karatekillpts += 1

                jump karatefight

            else:
                play sound "punch.mp3"
                with hpunch
                "{i}Random Karate Person attacks with Fist of Polaris! It breaks through Sensei’s defense!{/i}"
                "{i}Sensei has taken 10 damage!{/i}"

                $ senseidamage += 10

                jump karatefight

    #########################
label unholycathedral:

    stop music fadeout 3.0
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene gameworld18
    with dissolve2
    play music "8faster.mp3"
    $ renpy.pause(3, hard=True)
    scene gameworld19
    with dissolve2
    $ twinskillpts = 0

    "{i}The Red Twins appeared!{/i}"

    if twinsseen == True:
        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"
        sev "Thank you for joining us once more in the Unholy Cathedral. My name is [[REDACTED] and I am joined by Moyo Makinamo and Akira Arakawa for another installment of Untitled Ass Kicking."
        s "Unfortunately, {i}yours{/i} is the ass that will be kicked this time! I’ve figured out your weakness, Red Twins."
        sev "Is such a thing even possible when you’ve yet to fully discern your own?"
        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"
        s "I guess there’s only one way to find out!"

        jump twinsfightmenu

    else:
        s "Oh god, you two are here as well?"
        sev "Perhaps we are, perhaps we aren’t. There are plenty of ways for us to blend in, Akira. Plenty of ways to fit into places we do not belong."
        sev "Could the same not be said for you, though? Wandering around with dinner on your head like you’re some sort of hero when we all know you’re anything but."
        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"
        s "They have my family!"
        sev "Who are “they?” The ones who tend the garden? Dust the cobwebs off of tombstones? Your family is no more. And at this rate, you are sure to join them."
        s "I will defeat both of you and bring honor back to the name Arakawa."
        sev "Honor never left {i}you.{/i} You’re the one who left it behind. And now that it’s sprouted legs and caught up with you...you’re afraid."
        s "The only thing {i}I’m{/i} afraid of is you making me wear that dress."
        sev "Is that you hinting at how you’d like to wear the dress? It’d be quite random otherwise."
        s "Pfft. Absolutely not. Even if it’s kind of cold in here and I still haven’t found or equipped any armor."
        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"
        s "Does that actually mean something or is she just yelling?"
        sev "She’s saying...{i}it’s time to die.{/i}"

        $ twinsseen = True

        jump twinsfightmenu

label twinsfight:
    $ config.rollback_enabled = False

    if senseidamage > 30:
        stop music fadeout 5.0

        sev "Have you had your fun yet?"

        play sound "tackle.mp3"
        with hpunch

        "{i}Sensei collapses to the ground! He’s bleeding out!{/i}"

        s "Dying has...never been my idea of fun."
        sev "Nor was it hers, but that never stopped her."
        sev "Give into the blackness that reaches out to envelop you."

        scene black
        with dissolve2
        stop music fadeout 10.0

        sev "Moyo and I will take very good care of your corpse..."
        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"

        "{i}Before the remainder of life fades from him, Sensei can make out the feeling of both oversized and undersized hands exploring his lower body...{/i}"
        "{i}He has failed...{/i}"
        "........."
        "......"
        "..."

        scene gameworld1
        with dissolve2
        play music "8pox.mp3"

        $ senseidamage = 0

        "{i}You somehow manage to respawn in Fucklador.{/i}"
        "{i}Your hospital bill will be sent to you later.{/i}"

        $ config.rollback_enabled = True

        jump gameworldmainhub

    else:
        jump twinsfightmenu

    menu twinsfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"

                    if twinskillpts == 3:
                        "{i}But no amount of sanitization will ever wash away the fact that he just drank his own cum!{/i}"

                        s "I seriously can’t believe I had to do that in order to progress."
                        sev "There are many things you shouldn’t believe — words of those who were never meant to speak, yet still managed to color outside of the lines and deliver their message to you."
                        sev "You will never escape, Akira. It doesn’t matter how many of us you slay or conquer."
                        sev "You’re a hamster on a wheel. You only {i}think{/i} you’re going somewhere. But the powers that be have you right where they want you."
                        sev "And without the assistance of The Hyphenated One, you are even more doomed than ever before."
                        s "If I knew this tone shift was coming, I would have used Guard instead."
                        sev "Thankfully for you, you shan’t deal with it any longer."
                        sev "Come, Moyo. We must feed ourselves to the Dark Entity."
                        sev "It must be done to progress Sensei-Quest."

                        play sound "moyo.mp3"
                        with hpunch

                        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"

                        "{i}Moyo’s {b}Angelic Words{/b} burn Sensei’s ears!{/i}"
                        "{i}He takes 10 damage!{/i}"

                        $ senseidamage += 10

                        scene gameworld18
                        with dissolve2
                        stop music fadeout 10.0

                        "{i}But it doesn’t matter! The Red Twins have escaped!{/i}"

                        play sound "slayed.mp3"

                        "{i}Sensei wins!{/i}"

                        s "But...my orb?"

                        "{i}There’s a twinkle on the ground — one that looks a bit like a star.{/i}"

                        play sound "winner.mp3"

                        "{i}Sensei has obtained the Orb of Red!{/i}"

                        s "..."
                        s "..."
                        s "..."

                        scene black
                        with dissolve2

                        s "Uhh..."
                        s "I guess I’m...done here then?"

                        scene gameworld1
                        with dissolve2
                        play music "8pox.mp3"

                        "{i}Sensei returns to Fucklador! His erection is still present!{/i}"

                        $ redorb = True
                        $ senseidamage = 0
                        $ config.rollback_enabled = True

                        s "Wait. I know how to fix this."

                        with hpunch

                        "{i}Sensei ejaculates into the Steel Bucket again!{/i}"

                        s "What do you know? I’m getting a lot of use out of this thing after all."

                        jump gameworldmainhub

                    else:
                        "{i}It didn’t work...{/i}"
                        sev "Open wide."
                        with hpunch
                        "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                        play sound "seek.mp3"

                        "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                        $ senseidamage += 10

                        play sound "moyo.mp3"
                        with hpunch
                        "{i}Moyo is looking at bugs.{/i}"

                        jump twinsfight

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"

                    if twinskillpts == 1:
                        with hpunch
                        sev "Aah..."

                        "{i}His penis penetrates 79 6f 75 64 69 64 69 74 with ease!{/i}"
                        "{i}He feels something crawl across it from the inside?...{/i}"

                        sev "Such a naughty boy. Did my {b}Hands of God{/b} not do the trick? Or does violence excite you the way it does me?"
                        s "This...isn’t for pleasure..."
                        s "This is...an attack!"
                        sev "Oh? But it doesn’t hurt at all. And I’m not the type who can be fucked into submission."
                        sev "Moyo on the other hand..."

                        play sound "moyo.mp3"
                        with hpunch

                        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"
                        sev "She’d do anything for a taste of your milk."
                        s "I’m not...attempting to do physical damage!"
                        s "I’m...attempting to...deal mental damage in the form of an unwanted pregnancy!"
                        s "That is...how I use Fertilize!"
                        sev "Use it {i}harder...{/i}"
                        sev "I will take everything from you. Even that which you are unwilling to give."

                        play sound "moyo.mp3"
                        with hpunch

                        moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"

                        "{i}Moyo’s {b}Angelic Words{/b} burn Sensei’s ears!{/i}"
                        "{i}He takes 10 damage!{/i}"

                        $ senseidamage += 10
                        $ twinskillpts += 1

                        jump twinsfight

                    else:
                        "{i}It didn’t work...{/i}"
                        sev "Open wide."
                        with hpunch
                        "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                        play sound "seek.mp3"

                        "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                        $ senseidamage += 10

                        play sound "moyo.mp3"
                        with hpunch
                        "{i}Moyo is looking at bugs.{/i}"

                        jump twinsfight

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}It didn’t work...{/i}"
                    sev "Open wide."
                    with hpunch
                    "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                    play sound "seek.mp3"

                    "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                    $ senseidamage += 10

                    play sound "moyo.mp3"
                    with hpunch
                    "{i}Moyo is looking at bugs.{/i}"

                    jump twinsfight

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"

                    if twinskillpts == 0:
                        sev "Oooh...what’s this? Are we playing a different game now?"
                        s "This is a special brand of massage oil that is supposed to weaken you. Probably."

                        "{i}Sensei lathers the body of 79 6f 75 64 69 64 69 74 in oil! She shivers with delight!{/i}"

                        sev "Yes...I think I could use some more."
                        s "That’s strange...you don’t seem any weaker."
                        sev "Perhaps Moyo will react differently?"

                        "{i}Sensei lathers the body of Moyo Makinamo in oil!{/i}"

                        play sound "moyo.mp3"
                        with hpunch

                        "{i}She cums!{/i}"

                        s "This oil isn’t working the way it’s supposed to. I’m going to have to ask for a refund."
                        sev "Perhaps we just need more?"
                        s "No, ew. Stop. Your body’s really disproportionate and it’s creeping me out. Just die already. And stop appearing in weird events pretending to be important."

                        with hpunch
                        "{i}79 6f 75 64 69 64 69 74 reaches forward and attacks with Handjob!{/i}"

                        s "Ngh!"
                        sev "There, there...let it all out..."
                        sev "Give us enough and we may even hand over the item you’re looking for over."
                        s "I...will obtain the orb...the way I’m supposed to!"

                        with sexfade
                        with sexfade
                        with cumflash
                        with hpunch

                        s "NGAAAAH!"

                        "{i}Sensei cums so hard that he takes 10 damage!{/i}"

                        s "Fuck!"
                        sev "If that’s what you so desire."

                        $ twinskillpts += 1
                        $ senseidamage += 10

                        jump twinsfight

                    else:
                        "{i}It didn’t work...{/i}"
                        sev "Open wide."
                        with hpunch
                        "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                        play sound "seek.mp3"

                        "{i}Sensei is poisoned by the fumes! He takes 10 damage!{/i}"

                        $ senseidamage += 10

                        play sound "moyo.mp3"
                        with hpunch
                        "{i}Moyo is looking at bugs.{/i}"

                        jump twinsfight

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"

            if twinskillpts == 2 and steelbucket == True:
                "{i}His dick is about to erupt!{/i}"

                s "My dick is WHAT?"

                "{i}About to erupt!{/i}"

                s "???!!!??!!???!!??!!??"

                sev "Your erection has been steadily growing throughout the entire battle. It’s likely due to my {b}Mantis Eyes.{/b}"
                s "You two have...too many abilities! I don’t want to erupt!"
                sev "You’ll erupt over and over...every time you come here to challenge us. Your seed only increases our power."
                s "Then all I have to do is...keep it away from you!"

                "{i}Sensei uses Steel Bucket to catch his eruption!{/i}"

                play sound "moyo.mp3"
                with hpunch

                moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"

                "{i}Moyo Makinamo is enraging!{/i}"

                sev "Uh-oh. Moyo seems a bit perturbed that you’d send her to bed without dinner."

                "{i}Moyo lunges forward! She is trying to steal the Steel Bucket!{/i}"

                s "Stop! I paid good money for this!"

                sev "She’ll catch you sooner or later. There’s no way to hide your cum from a hungry Makinamo."
                s "There is...one way!"
                sev "Oh?"

                play sound "winner.mp3"
                with hpunch

                "{i}Sensei has consumed his own cum from the Steel Bucket!{/i}"

                s "This isn’t the time to play that sound clip! That was really gross!"

                sev "I have never been more turned on than I am right now."

                play sound "moyo.mp3"
                with hpunch

                moyo "^^^$@$@#@!@#!#$!$!@#!#!$!$!!!$!^^^^!@$!#"

                "{i}Moyo has stopped enraging.{/i}"

                $ twinskillpts += 1

                jump twinsfight

            else:
                sev "Open wide."
                with hpunch
                "{i}79 6f 75 64 69 64 69 74 used Rotbreath!{/i}"

                play sound "seek.mp3"

                "{i}Sensei manages to shield himself from some of the fumes! He takes 5 damage!{/i}"

                $ senseidamage += 5

                play sound "moyo.mp3"
                with hpunch
                "{i}Moyo Makinamo uses Shriek!{/i}"

                "{i}Sensei takes 5 damage!{/i}"

                $ senseidamage += 5

                jump twinsfight

    #########################
label developerisland:
    stop music fadeout 3.0
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene gameworld22
    with dissolve2
    play music "amiawake.mp3"
    $ renpy.pause(3, hard=True)
    scene gameworld23
    with dissolve2
    $ fredkillpts = 0
    $ senseidamage = 0

    "{i}Fred appeared!{/i}"
    "{i}He tips his hat at you.{/i}"

label fredfight:
    $ config.rollback_enabled = False

    if senseidamage > 100:
        stop music fadeout 5.0

        s "He’s...too...strong!"

        play sound "tackle.mp3"
        scene black
        with hpunch

        "{i}Sensei collapses to the ground, unable to breathe.{/i}"
        "{i}As the light fades from his eyes, he curses Fred.{/i}"
        "{i}Fred merely tips his hat in response...{/i}"
        "........."
        "......"
        "..."

        scene gameworld1
        with dissolve2
        play music "8pox.mp3"

        $ senseidamage = 0

        "{i}You somehow manage to respawn in Fucklador.{/i}"
        "{i}Fred is certainly a force to be reckoned with.{/i}"

        $ config.rollback_enabled = True

        jump gameworldmainhub

    else:
        jump fredfightmenu

    menu fredfightmenu:
        "Attack":
            menu:
                "Tackle":
                    "{i}Sensei used Tackle!{/i}"

                    if fredkillpts == 0:
                        play sound "punch.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"
                        "{i}Fred picks himself up off the ground and dusts his clothes off before tipping his hat at you.{/i}"
                        "{i}It doesn’t hurt...this time.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    if fredkillpts == 10 and swordofhope == True:
                        play sound "punch.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"

                        stop music
                        play sound "slayed.mp3"
                        scene gameworld22 with hpunch

                        "{i}Fred has fallen!{/i}"
                        "{i}You have killed an innocent man!{/i}"

                        $ senseidamage = 0
                        $ fredisdead = True
                        $ config.rollback_enabled = True

                        scene black

                        "{b}{size=+20}YOU WILL PAY FOR WHAT YOU’VE DONE.{/b}{/size}"

                        jump postfreddeathscene

                    else:
                        "{i}It has no effect...{/i}"
                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

                "Venom Spit" if venomspit == True:
                    "{i}Sensei used Venom Spit!{/i}"

                    if fredkillpts == 4:
                        play sound "slap.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"
                        "{i}But why did it make a slapping noise?...{/i}"
                        "{i}Fred picks himself up off the ground, also confused by this, and dusts his clothes off before tipping his hat at you.{/i}"
                        "{i}He’s starting to feel a little upset about all of these attacks...{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    else:
                        "{i}Fred opens his mouth and swallows the venom!{/i}"

                        s "What?"

                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

                "Banana Blast" if bananablast == True:
                    "{i}Sensei used Banana Blast!{/i}"

                    if fredkillpts == 7:
                        play sound "punch.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"
                        "{i}Fred picks himself up off the ground, swipes away a few bananas, and dusts his clothes off before tipping his hat at you.{/i}"
                        "{i}It doesn’t hurt...this time.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    else:
                        "{i}Nothing happened...{/i}"
                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

                "Bubble Beam" if bubblebeam == True:
                    "{i}Sensei used Bubble Beam!{/i}"
                    "{i}It has no effect...{/i}"
                    "{i}Fred tips his hat!{/i}"

                    play sound "sword.mp3"
                    with hpunch

                    "{i}Sensei takes 50 damage!{/i}"

                    $ senseidamage += 50

                    jump fredfight

                "Sanitize" if sanitize == True:
                    "{i}Sensei used Sanitize!{/i}"

                    if fredkillpts == 5:
                        play sound "computeryay.mp3"
                        with hpunch

                        "{i}Both he and Fred are so clean now!{/i}"
                        "{i}Fred tips his hat, as if to say thanks.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    else:
                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

                "Fertilize" if fertilize == True:
                    "{i}Sensei used Fertilize!{/i}"
                    "{i}It has no effect...{/i}"
                    "{i}Fred tips his hat!{/i}"

                    play sound "sword.mp3"
                    with hpunch

                    "{i}Sensei takes 50 damage!{/i}"

                    $ senseidamage += 50

                    jump fredfight

                "Salt Spray" if saltspray == True:
                    "{i}Sensei used Salt Spray!{/i}"
                    "{i}It has no effect...{/i}"
                    "{i}Fred tips his hat!{/i}"

                    play sound "sword.mp3"
                    with hpunch

                    "{i}Sensei takes 50 damage!{/i}"

                    $ senseidamage += 50

                    jump fredfight

                "Fire Ball" if fireball == True:
                    "{i}Sensei used Fire Ball!{/i}"

                    if fredkillpts == 2:
                        play sound "explosion.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"
                        "{i}Fred picks himself up off the ground and dusts his clothes off before tipping his hat at you.{/i}"
                        "{i}It doesn’t hurt...this time.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    if fredkillpts == 8:
                        play sound "explosion.mp3"
                        with hpunch

                        "{i}A direct hit!{/i}"
                        "{i}Fred picks himself up off the ground and dusts his clothes off before tipping his hat at you.{/i}"
                        "{i}It doesn’t hurt...this time.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    else:
                        "{i}Fred reaches down to pick a coin off the ground, accidentally dodging the attack in the process!{/i}"
                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

                "Use Blowtorch" if blowtorch == True:
                    "{i}Sensei used his blowtorch!{/i}"
                    "{i}It has no effect...{/i}"
                    "{i}Fred tips his hat!{/i}"

                    play sound "sword.mp3"
                    with hpunch

                    "{i}Sensei takes 50 damage!{/i}"

                    $ senseidamage += 50

                    jump fredfight

                "Use...Massage Oil?" if massageoil == True:
                    "{i}Sensei used massage oil!{/i}"

                    if fredkillpts == 1:
                        "{i}Fred loves massages!{/i}"
                        "{i}He thanks you for the oil with a polite tip of his hat.{/i}"

                        $ fredkillpts += 1

                        jump fredfight

                    else:
                        "{i}Fred doesn’t want a massage right now...{/i}"
                        "{i}Fred tips his hat!{/i}"

                        play sound "sword.mp3"
                        with hpunch

                        "{i}Sensei takes 50 damage!{/i}"

                        $ senseidamage += 50

                        jump fredfight

        "Guard":
            play sound "guard.mp3"
            "{i}Sensei protects himself!{/i}"

            if fredkillpts == 3 and shieldofresistance == True:
                "{i}Fred tips his hat!{/i}"

                play sound "sword.mp3"
                with hpunch

                "{i}Sensei avoids taking damage!{/i}"

                $ fredkillpts += 1

                jump fredfight

            if fredkillpts == 6 and bootsofforgiveness == True:
                "{i}Fred tips his hat!{/i}"

                play sound "sword.mp3"
                with hpunch

                "{i}Sensei avoids taking damage!{/i}"

                $ fredkillpts += 1

                jump fredfight

            if fredkillpts == 9 and steelbucket == True:
                "{i}Fred tips his hat!{/i}"

                play sound "sword.mp3"
                with hpunch

                "{i}Sensei avoids taking damage!{/i}"

                $ fredkillpts += 1

                jump fredfight

            else:
                "{i}Fred politely smiles!{/i}"

                jump fredfight
