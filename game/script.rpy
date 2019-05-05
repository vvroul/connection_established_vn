#define characters
define networker = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define ai = Character("AI", ctc="ctc_blink", ctc_position="fixed")
define mum = Character("Mom", ctc="ctc_blink", ctc_position="fixed")
define mio = Character("Mio", color="#FA5858", ctc="ctc_blink", ctc_position="fixed", image="mio")  #cherry blossom, beautiful
define aki = Character("Aki", ctc="ctc_blink", ctc_position="fixed")  #clear, bright
define kana = Character("Kana", ctc="ctc_blink", ctc_position="fixed") #summer, flower
define gou = Character("Gou", ctc="ctc_blink", ctc_position="fixed")  #powerful like a mountain
define kage = Character("Kage", ctc="ctc_blink", ctc_position="fixed") #shadow
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
    unknown "Their systems seem to work just fine. Maybe better than ours."
    unknown "So, they'll need three of them. Let's hope this will work."
    $ renpy.pause(1, hard=True)
    scene bg home_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    mio "Good morning, I'm Mio, Kana's friend. Is she at home?"
    ai "Hello. Unfortunately, she left an hour ago. Would you like to deliver a message for her?"
    mio "Oh, I see."
    mio "Yes, please tell her that we have an extra ticket for the {color=#FE2E64} Epic Dinosaur Battle {/color} tonight, so she can join us."
    mio "Gou is coming also and he's taking his camera with him."
    ai "Message saved. Anything else you'd like?"
    menu : 
        "No, that's all." :
            $no_thats_all = True
            $miss_times_together = False
        "I really miss the days we were having fun together." :
            $miss_times_together = True
            $no_thats_all = False
    ai "Alright, closing the call in 3...2..."
    mio "Hope she'll come tonight."
    jump tv_news

    label tv_news :
        scene black with Pause(1)
        $ renpy.pause(1, hard=True)
        "A dead body was found yesterday in a car accident."
        "The camera which captured the event reported that the man crashed all by himself..."
        "Dear God Danny..."
        kage "Hey wait, why did you turn that off?"
        mum  "..."
        kage "Mum, I am old enough to compromise with dad's death."
        kage "Everything's going to be fine."
        mum "Thank you, honey, you've really grown up. I'm proud of you."
        mum "So, I heard that your friends are going to the big battle show in a few minutes. Why don't you go with them?"
        kage "I don't know..."
        mum "You're really interested in this technology, right?"
        kage "How do you..."
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
        gou "Well, 10 minutes have passed and he's nowhere to be seen." 
        gou "I'm going in either way, catch you later."
        kana "That Gou, always getting on my nerves with his lack of persistence."
        mio  "I'm really happy she's beside us, wonder if the AI managed to deliver my call."
        kana "Hey, Mio, you know..."
        aki  "Is that Kage over there?" 
        kage "Hey, guys, thanks a lot for waiting."
        kana "You're late."
        kage "I know. I'll explain later, let's not waste our time."
        mio "Huh, seems like we're the first getting here."
        aki "That's weird."
        aki  "3000 tickets were listed as closed."
        unknown "..."
        unknown "Hi and welcome to the Big Dinosaur Battle"
        kana "Here it goes."
        unknown "The first Technolized battle event between two advanced mecha beasts developed by the biggest tech company in our universe..."
        unknown "Don't be afraid as they're trained not to attack anyone else than their opponent." 
        kana "Gou, I'm scared."
        gou "Don't mind Kana, it's gonna be alright." 
        #show beasts
        unknown "And now, get prepared for some fight." 
        #lights off. 
        unknown "3...2..."
        unknown "Or."
        unknown "Not."
        kana "What happened?"
        kage "Something's not right."
        aki "Well, those dinosaurs aren't that amazing as we expected."
        unknown "That's because I'm controlling them now."
        unknown "If I order an attack they will immediatelly come for you."
        gou "And why should we care about that?"
        networker "I'm not one of your race."
        networker "I've heard you guys are among the most intelligent technolized."
        networker "I need..."
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
        kage "Kana is right, we have to find another method to break the barrier."
        gou "You should relax guys. If this weirdo wants us to play this game, we'll play it."
        kana "Weirdo, you should call yourself for telling us to kill each other."
        kana "What if he's lying and none of us is fake."
        mio "Kana...I always agree with what you think but now...you're wrong."
        kana "How am I wrong?"
        mio "There's clearly a fake..."
        aki "Hm"
        kage "Aki...what do you say?"
        aki "We need to discuss about it..."
        aki "From my point of view, there are at least three cases that may be true."
        menu : 
            "Kage was late." :
                jump kageLate
            "Gou went inside before Kage arrived." :
                jump gouInside
            "I searched."
                jump akiSearched

        label kageLate : 
            aki "Kage..."
            aki "We all know you were late to come to our meeting place, about 45 minutes."
            aki "What do you have to say about this?"
            kana "Indeed, Kage was really late! He is the fake one!"
            mio "The rest of us were here and waiting for him...it can't be..."
            gou "Wait..."
            gou "I also have a proposal, so let's not rush to quick conclusions."
            kage "If you really think I'm the fake obe, then we're surely all done."
            mio "Mind explaining?"
            kage "Aki. I understand your reasons, but after the conversation we did before, I did not think you would be suspicious."
            kage "Initially, I was not sure whether I was going to watch the battle. What changed my mind was a specific photo."
            kage "The picture depicts Aki with a robot machine, which most probably created by her."
            kana "And so what?"
            kage "While getting out of the house and running to catch you guys up, I met Aki on the road..."
            kage "And we talked about the robot she is developing and various other techniques on how one can simulate this battle."
            mio "But ... wait. Aki was here with us all the time."
            kage "Yes...the fake one! That's why she blamed me first because she wants to get rid of us one by one without realising it ..."
            kana "Here's where you are wrong Kage. It could not have been the fake, and I can prove to you why."
            networker "Seems like I have underestimated them. Already came up with more arguments than I expected."
            kana "I also know about Aki's occupation you mentioned with this particular robot. In fact, I was in her house when she was starting to develop it."
            kana "That day she put the robot in ofline mode while she wanted to upgrade a major part of it."
            kana "The upgrading was complete until yesterday and today the robot could move into the streets and interact with anyone."
            gou "So you're saying that it's so technologically advanced that could talk to Kage without realizing himself?"
            kana "Ask Aki herself. She has really done a great job."
            kana "So your argument for the fake Aki is not valid."
            networker "..."
            mio "Gou..."
            mio "I believe you are the fake one. You entered the stage without waiting for Kage."
            mio "There is a great chance you got captured by Networker."
            mio "Επιπλέον προσπαθήσεις όλη αυτήν την ώρα να προστατέψεις τον Kage γιατί ήταν ο μόνος που σε είδε."
            gou "I don't understand."
            kage "..."
            mio "He told me before the show started, he saw you while he was coming here."

    return