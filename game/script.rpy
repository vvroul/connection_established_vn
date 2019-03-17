#define characters
define bot = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define ai = Character("AI", ctc="ctc_blink", ctc_position="fixed")
define mum = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define mio = Character("Mio", color="#FA5858", ctc="ctc_blink", ctc_position="fixed", image="mio")  #cherry blossom, beautiful
define aki = Character("Aki", ctc="ctc_blink", ctc_position="fixed")  #clear, bright
define kana = Character("Kana", ctc="ctc_blink", ctc_position="fixed") #summer, flower
define gou = Character("Gou", ctc="ctc_blink", ctc_position="fixed")  #powerful like a mountain
define kage = Character("Kage", ctc="ctc_blink", ctc_position="fixed") #shadow
define unknown = Character("???", ctc="ctc_blink", ctc_position="fixed")


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
    unknown "So, they need three of them. Let's hope this will work."
    $ renpy.pause(1, hard=True)
    scene bg home_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    #dring dring
    mio "Hello I'm Mio, Kana's friend, is she at home?"
    ai "Hello. Unfortunately, she left an hour ago. Would you like to deliver a message for her?" #ai
    mio "Oh I see."
    mio "Yes, please tell her that we have an extra ticket for the {color=#FE2E64} Epic Dinosaur Battle {/color} tonight, so she can join us." #with color
    mio "Gou is coming also and he's taking his camera with him."
    ai "Message saved. Anything else you want?"
    menu : 
        "No, that's all." :
            $no_thats_all = True
            $miss_times_together = False
        "I really miss the days we were having fun together." :
            $miss_times_together = True
            $no_thats_all = False
    ai "Alright, closing the call in 3...2..."
    #call closed sound
    mio "Hope she'll come tonight."
    jump tv_news


    label tv_news :
        scene black with Pause(1)
        $ renpy.pause(1, hard=True)
        "A dead body was found yesterday in a car accident."
        "The camera which captured the event reported that the man crashed all by himself..."
        "Dear God Danny..."
        #closing tv
        kage "Hey, why did you turn that off?"
        mum  "..."
        kage "Mum, I am old enough to compromise with dad's death."
        kage "Everything's going to be fine."
        mum "Thank you, honey, you've really grown up. I'm proud of you."
        mum "So, I heard that your friends are going to the big battle show in a few minutes. Why don't you go with them?"
        kage "I don't know, Let me think about it."
        mum "You're really interested in this technology, right?"
        kage "Seems like you knew this all along."
        mum "Of course, I'm your mother. I can easily interpret your feelings."
        menu : 
            "Build a new machine." :
                jump buildMachine
            "Afraid of moving on." :
                jump afraidMoving

    label buildMachine : 
        kage "I want to build a new machine based on this feature. The ability to counter such a vast scale of attacks."
        kage "It's so intriguing..."
        kage "I'm going!"
        mum "Better run, honey."
        kage "Oh, crap! See ya, mum. Thank you!"
        mum "Kage..."
        kage "What now?"
        mum "I love you."
        kage "Me too mum. Me too."
        jump timeForShow


    label afraidMoving : 
        kage "Mum. You're right I really want to invest on this feature."
        kage "But, I'm afraid I'll fail miserably. I mean there are so many people behind this ongoing project."
        kage "There's no way I'm going to succeed by myself. I..."
        mum  "What about asking for Aki's help?"
        kage "Aki...why Aki's she's not into machines."
        mum  "Oh really? Then, how do you explain this?"
        #show a phot of Aki with a flyer
        kage "Had no idea...This changes evetything."
        kage "Have to find her, do you know if she's also going to the show?"
        mum  "Only one way to know."
        kage "I'm going!"
        mum "Better run, honey."
        kage "Oh, crap! See ya, mum. Thank you!"
        mum "Kage..."
        kage "What now?"
        mum "I love you."
        kage "Me too mum. Me too."
        jump timeForShow


    label timeForShow : 
        gou "Bet he's not coming after all."
        aki "Wait!!"
        aki ""

    return
