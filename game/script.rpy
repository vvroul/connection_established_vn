define bot = Character("Networker", ctc="ctc_blink", ctc_position="fixed")
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
    return
