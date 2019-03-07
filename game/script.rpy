#define bgs

#define characters
define bot = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define ai = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
define mio = Character("Mio", color="#FA5858", ctc="ctc_blink", ctc_position="fixed")  #cherry blossom, beautiful
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


image bg black_bg = "black_bg.png"


label start:

    scene bg black_bg with fade
    $ renpy.pause(1.0)
    window show dissolve

    unknown "Today is the day."
    unknown "I..."
    "You know what to do right?"
    "Unless you want us to repeat the mission again."
    "No, sir. Everything's clear."
    "Good. Now...go. Do not dissapoint us."
    "Yes, sir."
    scene black with Pause(1)
    $ renpy.pause(1, hard=True)
    unknown "I haven't been in this planet since the Initial Incident."
    #show mecha dinosaur image
    unknown "Their systems seem to work just fine. Maybe better than ours."
    unknown "So, they need three of them. Let's hope this works."
    scene black with Pause(1)
    $ renpy.pause(1, hard=True)
    #show the technolyzed backdround
    mio "Hello I'm Mio, Kana's friend, is she there?"
    "Unfortunately, she left an hour ago. Would you like to deliver a message for her?" #ai
    mio "Oh I see."
    mio "Yes, please tell her that we have an extra ticket for the Epic Dinosaur Battle tonight, so she can join us." #with color
    mio "Gou is coming also and he's taking his camera with him."
    ai "Message saved. Anything else you want?"
    menu : 
        "No, that's all." :
            $no_thats_all = True
            $miss_times_together = False
        "I really miss the times we were having fun together." :
            $miss_times_together = True
            $no_thats_all = False
    ai "Alright, closing the call in 3...2..."
    #call closed sound
    jump tv_news


    label tv_news :
        "A dead body was foudn yesterday by a car accident."
        "The camera thar captured the event reported that the man crashed all by himself..."
        "Dear God..."
        #closing tv
        "Why did you turn that off?"
    return
