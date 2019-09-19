﻿#define characters
define networker = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define ai = Character("AI", ctc="ctc_blink", ctc_position="fixed")
define mum = Character("Mom", ctc="ctc_blink", ctc_position="fixed")
define mio = Character("Mio", color="#FA5858", ctc="ctc_blink", ctc_position="fixed", image="mio")  #cherry blossom, beautiful
define aki = Character("Aki", ctc="ctc_blink", ctc_position="fixed")  #clear, bright
define kana = Character("Kana", ctc="ctc_blink", ctc_position="fixed") #summer, flower
define gou = Character("Gou", ctc="ctc_blink", ctc_position="fixed")  #powerful like a mountain
define kage = Character("Kage", ctc="ctc_blink", ctc_position="fixed") #shadow
define WGOD = Character("WIRED GOD", ctc="ctc_blink", ctc_position="fixed")
define unknown = Character("???", ctc="ctc_blink", ctc_position="fixed")

#define effects
image ctc_blink:
    xalign 0.96 yalign 0.95
    "images/ctc_normal.png"
    linear 0.5 alpha 1.0
    "images/ctc_transparent.png"
    linear 0.5 alpha 1.0
    repeat

define flash = Fade(0.1, 0.0, 0.3, color="#fff")

#define bgs
image bg black_bg = "black_bg.png"
image bg dino_bg = "dino.png"
image bg home_bg = "home.png"
image bg internet_bg = "background_internet.png"

#define side images
image side mio = "mio.png"

label start:
    scene bg internet_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    unknown "Today is the day."
    unknown "I..."
    "You know what to do right?"
    "Unless you want us to repeat the mission again."
    unknown "No, sir. Everything's clear."
    "Good. Now...go. Do not dissapoint us."
    unknown "Yes, sir."
    scene black with Pause(1)
    $ renpy.pause(1, hard=True)
    scene bg dino_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    unknown "I haven't been in this planet since the Initial Incident."
    unknown "Their systems seem to work well. Maybe better than ours."
    unknown "They're going to need three of them."
    unknown "Let's hope this will work."
    $ renpy.pause(1, hard=True)
    scene bg home_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    mio "Good morning, I'm Mio, Kana's friend. Is she home?"
    ai "Hello Mio. Unfortunately, she left an hour ago. Would you like to leave a message for her?"
    mio "Oh, I see."
    mio "Yes please, tell her we have an extra ticket for the {color=#FE2E64} Epic Dinosaur Battle {/color} tonight, so she can join us."
    mio "Also, Gou's coming too and he's taking his camera with him."
    ai "Call recorded. Anything else you'd like?"
    menu : 
        "No, that's all. Thank you." :
            $no_thats_all = True
            $miss_times_together = False
        "Yes..I... I really miss the days we were having fun together." :
            $miss_times_together = True
            $no_thats_all = False
    ai "Alright, ending the call in 3...2..."
    mio "Hope she'll come tonight..."
    jump tv_news

    label tv_news :
        scene black with Pause(1)
        $ renpy.pause(1, hard=True)
        "A dead body was found yesterday in a car accident."
        "The camera which captured the event reported that the man crashed all by himself..."
        "Dear God Danny..."
        "*blink*"
        kage "Hey wait, why did you turn that off?"
        mum  "..."
        kage "Mum. Not this again. I'm old enough for this."
        kage "Everything's going to be fine."
        mum "Thank you honey. I'm proud of you."
        mum "I heard that your friends are going to the big battle show today."
        mum "Why don't you join them?"
        kage "I don't know. I have a feeling this will be really boring."
        mum "You're really interested in this technology, are you?"
        kage "Yeah, how do you..."
        mum "I'm your mother. I can easily tell."
        menu : 
            "Build a new machine." :
                jump buildMachine
            "Afraid of moving on." :
                jump afraidMoving

    label buildMachine : 
        kage "I want to build a new machine based on this feature. The ability to counter such a vast scale of attacks."
        kage "It's so intriguing..."
        kage "I'm going!"
        mum "Better hurry up, honey."
        kage "You're right! See ya, mum. Thank you!"
        mum "Kage..."
        kage "What now?"
        mum "I love you."
        kage "Me too mum. Me too..."
        jump timeForShow

    label afraidMoving : 
        kage "I really want to invest time on this feature."
        kage "But, I'm afraid I'll fail miserably."
        kage "There's no way I'm going to succeed all by myself. I..."
        mum  "What about asking for Aki's help?"
        kage "Aki...she's not into machines."
        mum  "Oh really? Then, how do you explain this?"
        kage "Wow...Had no idea...This changes evetything."
        kage "Have to find her, do you know if she's also going to the show?"
        mum  "Only one way to know."
        kage "I'm going!"
        mum "Better hurry up, honey."
        kage "See ya, mum. Thank you!"
        mum "Kage..."
        kage "What now?"
        mum "I love you."
        kage "Me too mum. Me too..."
        jump timeForShow


    label timeForShow : 
        gou "Bet he's not coming after all."
        aki "Wait."
        aki "He called me and said he'll be here in a minute."
        gou "I'm going in either way, catch you later."
        kana "He's always getting on my nerves with his lack of persistence."
        mio  "I'm really happy she's beside us, wonder if the AI managed to deliver my call."
        kana "Hey, Mio, you know..."
        aki  "Is that Kage over there?" 
        kage "Hey, guys, thanks a lot for waiting."
        kana "You're late."
        kage "I know. I'll explain later, let's not waste our time."
        mio "Seems like we're the first getting here."
        aki "That's weird."
        aki  "30000 tickets were listed as closed."
        unknown "..."
        unknown "Hi and welcome to the Big Dinosaur Battle."
        kana "Here it goes."
        unknown "The first Technolized battle event between two advanced mecha beasts developed by the biggest tech company in our universe..."
        unknown "Don't be afraid as they're trained not to attack anyone else than their opponent." 
        kana "Gou, I'm scared."
        gou "Don't be afraid Kana, it's gonna be alright." 
        #show beasts
        unknown "And now, get prepared for some fight." 
        #lights off. 
        unknown "3...2..."
        unknown "Or..."
        unknown "Not."
        kana "What happened?"
        kage "Something's not right."
        aki "Well, those dinosaurs aren't that amazing as we expected."
        unknown "That's because I'm controlling them now."
        unknown "If I order an attack they will immediatelly execute it."
        gou "And why should we care about that?"
        networker "I'm not one of your race."
        networker "I've heard you guys are amongst the most intelligent technolized."
        networker "I need...I mean...they need..."
        networker "Your brains." 
        kana "You're just trying to scare us, aren't you? I'm not falling for this."
        kana "I'm getting out of this place."
        mio "Kana..."
        kana "Uh..."
        networker "Hm."
        kana "The...there's no exit."
        gou "Is this one of your tricks? Networker?"
        networker "I've closed all the exits with a magic barrier."
        networker "The only way to break it, is to solve a puzzle."
        networker "One of your friends is already captured. In order to identify who it is..."
        networker "You must kill him."
        mio "Whaaaaaat?!!"
        kage "No way..."
        kana "This is nonsense!! I'm not killing anyone!"
        kage "Kana's right, we have to find another method to break the barrier."
        gou "You should relax guys. If this weirdo wants us to play this game, we'll play it."
        kana "Weirdo, you should call yourself for telling us to kill each other."
        kana "What if he's lying and none of us is fake."
        mio "Kana...I always agree with what you think but now...you're wrong."
        kana "How am I wrong?"
        mio "There's clearly a fake..."
        kage "Aki...what do you have to say?"
        aki "We need to discuss about it..."
        aki "From my point of view, there are at least three cases that may be true."
        menu : 
            "Kage was late." :
                jump kageLate
            "Gou went inside before Kage arrived." :
                jump gouInside
            "I searched the area." : 
                jump akiSearched

        #blamed kage first cause late but aki image, then aki for being fake but was her robot #then gou because he went inside and might was captured
        label kageLate :
            aki "Kage..." #
            aki "We all know you were late to come to our meeting place, about 45 minutes."
            kana "Indeed, Kage was really late! He is the fake one!"
            mio "The rest of us were here and waiting for him...it can't be..."
            gou "Wait..."
            gou "I also have a proposal, so let's not rush to quick conclusions."
            kage "If you really think I'm the fake one, then we're all done."
            mio "Mind explaining?"
            kage "Aki. I understand your reasons, but after the conversation we had before, I didn't imagine you'd get suspicious."
            kage "Initially, I wasn't sure whether I was going to watch the battle or not. But a specific photo changed my mind."
            kage "This photo depicts Aki with a robot machine, most probably created by her."
            kana "So what?"
            kage "While I was getting out of my house and running to catch you guys up, I met Aki on the road..."
            kage "And we talked about the robot she is developing and various other techniques on how one can simulate this battle."
            mio "But... wait. Aki was here with us all the time."
            kage "Yes...the fake one! That's why she blamed me first because she wants to get rid of us one by one..."
            kana "Here's where you are wrong Kage. It couldn't have been the fake, and I can prove to you why."
            networker "Seems like I have underestimated them. Already came up with more arguments than I expected."
            kana "I also know about Aki's occupation you mentioned with her robot. In fact, I was with her when she was starting to develop it."
            kana "That day, she put the robot in offline mode while she wanted to upgrade a major part of it."
            kana "The upgrading was complete until yesterday and today the robot could move into the streets and interact with anyone."
            kana "Oh, and forgot to mention...the robot is more or less an Aki's clone."
            gou "So you're saying that it's so technologically advanced that could talk to Kage without realizing himself?"
            kana "Ask Aki. She's really done a great job."
            kana "So your argument for the fake Aki is not valid."
            networker "..." #
            aki "Gou..."
            aki "I believe you are the fake one. You entered the stage without waiting for Kage."
            aki "There is a great chance you got captured by Networker."
            aki "Moreover you're trying to cover Kage all the time, because he was the only one that saw you."
            gou "I don't understand."
            kage "..."
            aki "He told me before the show started, he saw you while he was coming here."
            aki "So...anything to say about this?"
            gou "You guys...dare to call me a fake one...I was the first one to call him Networker."
            gou "You know why?"
            gou "Because while you all were waiting outside for your Kage, I was actuall doing my own research around this place."
            gou "As you already noticed, no one other than us, was here, which was strange by itself."
            gou "So I scanned this whole place and guess what I found...this guy..."
            gou "This guy mind-controlled all the people that were invited in this event. Stole all the records..."
            gou "That's how he knows about us. And our minds."
            kana "I can't believe this...this is unreal..."
            kana "But I believe you Gou..."
            kage "Yeah, me too."
            aki "Mio?"
            mio "...this guy must pay for his actions..." #
            aki "There's something else I haven't yet mentioned."
            aki "Indeed today is the day I activated my robot upgrade and was really proud of that accomplishment of mine."
            aki "But I was kind of worried when I saw it moving..."
            aki "It followed a weird pathing which led to our country's most expensive equipment."
            mio "I don't understand. What's the meaning of this?"
            kage "Did you give it a specific command for that?"
            aki "Yes..."
            aki "To detect the nearest possible threat."
            kana "Wait...this place is..."
            gou "That's right."
            aki "Right here..."
            kage "Aki. (She's amazing!!!)"
            aki "So I guess this location has to do with the reason we're trapped here."
            jump blamingMio

        label gouInside :
            aki "Gou..." #
            aki "I believe you are the fake one. You entered the stage without waiting for Kage."
            aki "There is a great chance you got captured by Networker."
            aki "Moreover you're trying to cover Kage all the time, because he was the only one that saw you."
            gou "I don't understand."
            kage "..."
            aki "He told me before the show started, he saw you while he was coming here."
            gou "You guys...dare to call me a fake one...I was the first one to call him Networker."
            gou "You know why?"
            gou "Because while you all were waiting outside for your Kage, I was actuall doing my own research around this place."
            gou "As you already noticed, no one other than us, was here, which was strange by itself."
            gou "So I scanned this whole place and guess what I found...this guy..."
            gou "This guy mind-controlled all the people that were invited in this event. Stole all the records..."
            gou "That's how he knows about us. And our minds."
            kana "I can't believe this...this is unreal..."
            kana "But I believe you Gou..."
            kage "Yeah, me too."
            aki "Mio?"
            mio "...this guy must pay for his actions..."
            aki "Kage..." #
            aki "We all know you were late to come to our meeting place, about 45 minutes."
            kana "Indeed, Kage was really late! He is the fake one!"
            mio "The rest of us were here and waiting for him...it can't be..."
            gou "Wait..."
            gou "I also have a proposal, so let's not rush to quick conclusions."
            kage "If you really think I'm the fake one, then we're all done."
            mio "Mind explaining?"
            kage "Aki. I understand your reasons, but after the conversation we had before, I didn't imagine you'd get suspicious."
            kage "Initially, I wasn't sure whether I was going to watch the battle or not. But a specific photo changed my mind."
            kage "This photo depicts Aki with a robot machine, most probably created by her."
            kana "So what?"
            kage "While I was getting out of my house and running to catch you guys up, I met Aki on the road..."
            kage "And we talked about the robot she is developing and various other techniques on how one can simulate this battle."
            mio "But... wait. Aki was here with us all the time."
            kage "Yes...the fake one! That's why she blamed me first because she wants to get rid of us one by one..."
            kana "Here's where you are wrong Kage. It couldn't have been the fake, and I can prove to you why."
            networker "Seems like I have underestimated them. Already came up with more arguments than I expected."
            kana "I also know about Aki's occupation you mentioned with her robot. In fact, I was with her when she was starting to develop it."
            kana "That day, she put the robot in offline mode while she wanted to upgrade a major part of it."
            kana "The upgrading was complete until yesterday and today the robot could move into the streets and interact with anyone."
            kana "Oh, and forgot to mention...the robot is more or less an Aki's clone."
            gou "So you're saying that it's so technologically advanced that could talk to Kage without realizing himself?"
            kana "Ask Aki. She's really done a great job."
            kana "So your argument for the fake Aki is not valid."
            networker "..." #
            aki "There's something else I haven't yet mentioned."
            aki "Indeed today is the day I activated my robot upgrade and was really proud of that accomplishment of mine."
            aki "But I was kind of worried when I saw it moving..."
            aki "It followed a weird pathing which led to our country's most expensive equipment."
            mio "I don't understand. What's the meaning of this?"
            kage "Did you give it a specific command for that?"
            aki "Yes..."
            aki "To detect the nearest possible threat."
            kana "Wait...this place is..."
            gou "That's right."
            aki "Right here..."
            kage "Aki. (She's amazing!!!)"
            aki "So I guess this location has to do with the reason we're trapped here."
            jump blamingMio

        label akiSearched :
            aki "There's something else I haven't yet mentioned." #
            aki "Indeed today is the day I activated my robot upgrade and was really proud of that accomplishment of mine."
            aki "But I was kind of worried when I saw it moving..."
            aki "It followed a weird pathing which led to our country's most expensive equipment."
            mio "I don't understand. What's the meaning of this?"
            kage "Did you give it a specific command for that?"
            aki "Yes..."
            aki "To detect the nearest possible threat."
            kana "Wait...this place is..."
            gou "That's right."
            aki "Right here..."
            kage "Aki. (She's amazing!!!)"
            aki "So I guess this location has to do with the reason we're trapped here." #
            aki "Kage..."
            aki "We all know you were late to come to our meeting place, about 45 minutes."
            kana "Indeed, Kage was really late! He is the fake one!"
            mio "The rest of us were here and waiting for him...it can't be..."
            gou "Wait..."
            gou "I also have a proposal, so let's not rush to quick conclusions."
            kage "If you really think I'm the fake one, then we're all done."
            mio "Mind explaining?"
            kage "Aki. I understand your reasons, but after the conversation we had before, I didn't imagine you'd get suspicious."
            kage "Initially, I wasn't sure whether I was going to watch the battle or not. But a specific photo changed my mind."
            kage "This photo depicts Aki with a robot machine, most probably created by her."
            kana "So what?"
            kage "While I was getting out of my house and running to catch you guys up, I met Aki on the road..."
            kage "And we talked about the robot she is developing and various other techniques on how one can simulate this battle."
            mio "But... wait. Aki was here with us all the time."
            kage "Yes...the fake one! That's why she blamed me first because she wants to get rid of us one by one..."
            kana "Here's where you are wrong Kage. It couldn't have been the fake, and I can prove to you why."
            networker "Seems like I have underestimated them. Already came up with more arguments than I expected."
            kana "I also know about Aki's occupation you mentioned with her robot. In fact, I was with her when she was starting to develop it."
            kana "That day, she put the robot in offline mode while she wanted to upgrade a major part of it."
            kana "The upgrading was complete until yesterday and today the robot could move into the streets and interact with anyone."
            kana "Oh, and forgot to mention...the robot is more or less an Aki's clone."
            gou "So you're saying that it's so technologically advanced that could talk to Kage without realizing himself?"
            kana "Ask Aki. She's really done a great job."
            kana "So your argument for the fake Aki is not valid."
            networker "..." #
            aki "Gou..."
            aki "I believe you are the fake one. You entered the stage without waiting for Kage."
            aki "There is a great chance you got captured by Networker."
            aki "Moreover you're trying to cover Kage all the time, because he was the only one that saw you."
            gou "I don't understand."
            kage "..."
            aki "He told me before the show started, he saw you while he was coming here."
            aki "So...anything to say about this?"
            gou "You guys...dare to call me a fake one...I was the first one to call him Networker."
            gou "You know why?"
            gou "Because while you all were waiting outside for your Kage, I was actuall doing my own research around this place."
            gou "As you already noticed, no one other than us, was here, which was strange by itself."
            gou "So I scanned this whole place and guess what I found...this guy..."
            gou "This guy mind-controlled all the people that were invited in this event. Stole all the records..."
            gou "That's how he knows about us. And our minds."
            kana "I can't believe this...this is unreal..."
            kana "But I believe you Gou..."
            kage "Yeah, me too."
            aki "Mio?"
            mio "...this guy must pay for his actions..."
            jump blamingMio


        label blamingMio : 
            networker "Do you understand now? What they really want?"
            networker "They want to attack your country from the inside"
            networker "That's why I came here to take over your minds. Because you are the only ones that can operate these weapons correctly."
            gou "And why you're telling us that? You are the bad guy in this situation."
            networker "Well...not really? Am I? MIO."
            mio "..."
            kana "Mio??!!"
            mio "Why? You were supposed to let them kill one another."
            menu : 
                 "I'm not like them." :
                    jump changeOfHeart
                 "I'm not the real Networker." :
                    jump robot

            label changeOfHeart : 
                networker "Besides the fact I'm generally opposite to the methods used by the Wired, I'm not the type that kills people."
                networker "From the beginning I got assigned this mission, I didn't know what to do and I got desperate."
                networker "Yes, I investigated these super weapons of yours. But never intended to use them against yourselves."
                networker "But against my masters."
                aki "Your masters?"
                networker "Yes. The Wired have this weird system where they obey to a bunch of Digital Gods."
                networker "In my case, I was born to follow the commands of three Gods."
                kana "Do you really want us to believe that you communicate with deities now?"
                networker "I don't need to try that much. You have one right in front of you."
                mio "...Ok that's not fun anymore."
                mio "You've said enough. YOU ARE NOTHING TO OUR SOCIETY ANYMORE."
                mio "YOU'VE BETRAYED US."
                mio "AND...AND YOU WILL PAY FOR THIS ACTION OF YOURS."
                kage "How exactly he's going to pay? You can't do anything."
                networker "Don't worry I've taken account all the possible scenarios. The worst thing he can do is banish me from the society."
                gou "We're going to support you."
                kana "I also believe in you, Networker."
                mio "HM...HAHAHAHAHA"
                mio "AS YOU'VE SAID..."
                WGOD "I'M A GOD. I CAN DO EVERYTHING THAT I WANT."
                WGOD "AND WHAT I WANT IS TO REDEEM YOU FROM YOUR SINS."
                WGOD "NOW...DO YOU KNOW WHY MIO ISN'T HERE?"
                WGOD "BECAUSE WE'VE ALREADY CAPTURED HER AND WE'RE ABOUT TO EXTRACT ALL THE INFORMATION IN HER MIND." #
                networker "I know you don't completely trust me yet, and I'm sorry I trapped you but that was the only option I had."
                networker "Now we have to fight him together."
                aki "What's the plan?"
                networker "We cannot kill a god but we can defy him."
                kage "Mio's mind."
                networker "Exactly. We have to scan for Mio with the help of one of these systems you've got here."
                networker "She must be somewhere here."
                gou "We have her so close? That'd be a mistake and a possible risk for their own temporaty existence."
                networker "I think you answered it yourself. The range we can control a mind isn't very long."
                aki "But there must be something else right? I can't be such a limited skill."
                networker "Well yes. The problem is that her body becomes invinsible when is taken over."
                networker "And that's why we have to use your technology."
                kana "Yes but what we do after we find the body? Do we...kill her...?"
                kage "Networker...is there any chance to do a reverse mind control?"
                kage "I want to try to take over his mind..."
                aki "Kage...what are you actually thinking?"
                networker "Yes...this is possible but it comes with a sacrifice. The user loses its own mind completely when he tries to overtake a fake mind."
                networker "More so...if that's a GOD's mind...you'll take double the damage."
                kage "I... I don't care. I want us to try it. I know that the scanning weapon has a long charge time once you use it the first time."
                kage "But then again, if we find her and realise her no one guaranties us that we can save her."
                kage "So please Networker...enchance me with that skill of yours."
                gou "Fool..."
                networker "If I agree...how do I know that you're not going to overtake me?"
                unknown "He's not going to..."
                scene black with Pause(1)
                $ renpy.pause(1, hard=True)
                window show dissolve
                kana "Who's there? Are you an evil GOD that wants to overtake us as well?"
				mum "What? A GOD? That's nonsense. If a GOD existed then my husband would be alive right now."
				mum "And kage would follow his dream instead of...helping his friends I guess, which is awesome."
				mum "But I want him to be happy and all. And I know he's past that THE DEATH OF MY FATHER thing."
				mum "And..."
				kage "MUUUUUUUM!!! WHAT ARE YOU DOING HERE?"
				mum "What do you mean what I'm doing here, I came to pick you up from the show as we had agreed."
				aki "..."
				mum "I've heard it all."
				mum "He's not going to overtake your mind."
				mum "And I'm saying that with absolute awareness of what that GOD thing is."
				networker "What do you mean with absolute awareness?"
				kage "Mum?"
				aki "You've seen again one of these GODs haven't you?"
				mum "Yes Aki, love."
				mum "My...husband...Your father...Kage...wasn't killed in a car accident."
				kana "Oh my..."
				kage "What do you mean Mum? Were you lying to all these years?"
				kage "I mean, were you ever going to tell me the truth if this GOD wasn't about to appear?"
				mum "I'm sorry honey. Really, I'm sorry."
				mum "But I couldn't explain that how your father fought a GOD and..."
				mum "You wouldn't believe me."
				gou "Well, she has a point."
				gou "Hell we don't even know what that guy is capable of...even if he's all words 'till now."
                aki "I can understand what's happening here but I think we have a more important problem."
                aki "We have to find out what are his weaknesses."
                kana "If he has any..."
                networker "He's not a real GOD. As I've mentioned before he has simply overtaken Mio."
                kana "The weapon. We have to find her as soon as possible."
                WGOD "I'VE BEEN LISTENING TO YOU WHINING ALL THIS TIME AND TRY TO FIND A WAY TO DEFEAT ME."
                WGOD "JUST LOOK AT WHAT'S HAPPENING OUTSIDE. THE TIME YOU MORONS WERE SOLVING YOUR PERSONAL ISSUES, I WAS PREPARING FOR A FIGHT."
                #scenery with fights and overtaken minds
                mum "Kids...go away, you don't want to fight him."
                kage "I'm still going with my decision, I strongly believe we can do it. NETWORKEEEER!!"
                networker "If you insist..."
                networker "I will overtake you without completely controlling your mind."
                networker "You'll still have some senses so use them to trigger my overtake skill on him."
                kage "Ok we've got this!!"
                mum "Honey...your father wanted to protect me and...died trying the same thing."
                jump finale

            label robot : 
                
                jump finale

            label finale :

    return