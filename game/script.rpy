#scene removes all images and places a bg
#show layers an image over the scene

#plain string creates un-attached dialogue

#define charName = Character("DisplayName", color="#000000")
# ^ creates character
# charName "string"
# ^ character dialogue

define hm = Character("Headmaster", color="#000000")
define s_r = Character("Stranger")
define r = Character("Riot")
define yp = Character("You")

label start:
    scene marble courtyard crowd
    pause
    "You're anxious about finally being in this new school."
    "After all, the entrance exams alone were enough to give gray hairs."
    show headmaster speaking
    hm "Welcome one, welcome all, to Pegasus Academy!"
    hm "This is a place of Harmony and Purity, and I hope that each of you will enjoy your time here, as it is certainly plentiful."
    hm "There will be perils, but there will be joys."
    hm "I'm excited to see how they will change you..."
    hm "And how each of you will make your mark and find your place here."
    pause
    "You really just wished he would get to the important stuff."
    pause
    scene marble courtyard crowd close
    "A stranger leans in to your side."
    show stranger riot
    s_r "That guy's really annoying. I hear he once talked for 6 hours and forced the entire school to listen to him."
    menu:
        "\"I'm sure, but I'm actually kind of interested.\"":
            yp "That sounds like it sucked, but I'm actually kind of interested in what he's saying right now."
            yp "You should probably pay attention to what he's saying as well."
        "\"Let's talk after the speech in case we miss something important.\"":
            yp "Yeah I'd hate to be there. Though, we should talk after the speech; I don't want to miss something important."
            yp "You should probably focus on what he's saying. I mean it is a welcoming speech..."
        "\"Did he really? That's insane.\"":
            yp "Did he really?"
            yp "That's insane!"
            yp "I'm bored of this speech already."
    pause