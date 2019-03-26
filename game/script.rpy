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
    unknown "So, they need three of them. Let's hope this will work."
    $ renpy.pause(1, hard=True)
    scene bg home_bg with fade
    $ renpy.pause(1.0)
    window show dissolve
    mio "Hello I'm Mio, Kana's friend, is she at home?"
    ai "Hello. Unfortunately, she left an hour ago. Would you like to deliver a message for her?" #ai
    mio "Oh I see."
    mio "Yes, please tell her that we have an extra ticket for the {color=#FE2E64} Epic Dinosaur Battle {/color} tonight, so she can join us."
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
    mio "Hope she'll come tonight."
    jump tv_news

    label tv_news :
        scene black with Pause(1)
        $ renpy.pause(1, hard=True)
        "A dead body was found yesterday in a car accident."
        "The camera which captured the event reported that the man crashed all by himself..."
        "Dear God Danny..."
        kage "Hey, why did you turn that off?"
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
        mum "Better run, honey."
        kage "Oh, you're right! See ya, mum. Thank you!"
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
        kage "Aki...why Aki's she's not into machines."
        mum  "Oh really? Then, how do you explain this?"
        kage "Had no idea...This changes evetything."
        kage "Have to find her, do you know if she's also going to the show?"
        mum  "Only one way to know."
        kage "I'm going!"
        mum "Better run, honey."
        kage "See ya, mum. Thank you!"
        mum "Kage..."
        kage "What now?"
        mum "I love you."
        kage "Me too mum. Me too..."
        jump timeForShow


    label timeForShow : 
        gou "Bet he's not coming after all."
        aki "Wait!"
        aki "He called me and said he'll be here in a minute."
        gou "Well 10 minutes have passed and he's nowhere to be seen." 
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
        networker "I'm not from your race."
        networker "I've heard you guys are among the most intelligent technolized troops."
        networker "I need..."
        networker "Your brains." 
        kana "You're just trying to scare us, aren't you? I'm not fallin for this."
        kana "I'm getting out of this place."
        mio "Kana..."
        kana "Uh..."
        networker "Hm."
        kana "The...there's no exit."
        gou "Is this one of your tricks? Networker?"
        networker "I've closed all the exits with a magic barrier."
        networker "The only way to break it, is to solve a puzzle."
        networker "One of your friends is already captured. In order to identify who it is..."
        networker "You should kill him."
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
        aki "Πρέπει να το συζητήσουμε..."
        aki "Από την οπτική μου γωνία, υπάρχουν τουλάχιστον τρεις περιπτώσεις που μπορεί ισχύει κάτι τέτοιο."
        menu : 
            "Kage was late." :
                jump buildMachine
            "Afraid of moving on." :
                jump afraidMoving

    return