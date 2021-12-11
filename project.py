# this a a text based adventure where your choices matter and don't at the same time
# play the game to understand everything
# imports the needed libaries
from tkinter.constants import S
import pygame 
import termcolor 
from termcolor import colored 
from pygame import  mixer 
import time
from time import sleep
import colorama
from colorama import init, Fore, Back
def main():
    init()
    mixer.init()
    # variable to determine which ending of the game you will get
    orbs = 0 
    # intro to the game setting the world and rules 
    print(colored("Hello there?", "magenta")) 
    print(colored("Can you hear me?", "magenta")) 
    print(colored("Are you even there?", "magenta"))
    print(colored("Oh I see you.", "magenta"))
    print(colored("Heh heh heh.", "magenta"))
    print(colored("You were not the one I was expecting to recieve.", "magenta"))
    print(colored("Let me ask you. Why are you here?", "magenta"))
    print(colored("Is it to screw over my plans?", "magenta"))
    print(colored("No not even you are that cruel", "magenta"))
    print(colored("Or are you?", "magenta"))
    print(colored("So tell me what is your name?", "magenta"))
    name = input()
    print(colored("I see now what is your gender?", "magenta"))
    gender = input()
    print(colored("Intresting answer choice.", "magenta"))
    print(colored("Now what is your age?", "magenta"))
    age = input()
    print(colored("Nice now it is time.", "magenta"))
    print(colored("To reveal what this really is", "magenta"))
    print(colored("So is this who you are?", "magenta"))
    yorn = input("Yes or No ")
    print(colored("I see well, guess what.", "magenta"))
    print(colored("In this world you don't get to choose.", "magenta"))
    print(colored("You don't get to simply choose who you are.", "magenta"))
    print(colored("In this world, MY WORLD! ", "magenta"))
    print(colored("You do as I say.", "magenta"))
    print(colored("Your choices will matter.", "magenta"))
    print(colored("Make the right ones.", "magenta"))
    print(colored("You will go on this adventure and collect them all.", "magenta"))
    print(colored("Collect all 8 elemental orbs.", "magenta"))
    print(colored("Make the right choices to collect them all.", "magenta"))
    print(colored("You can't go back if you mess up so think carefully about what the correct actions would be.", "magenta"))
    print(colored("Think about what actions will defeat his 8 elites", "magenta"))
    print(colored("They gaurd the orbs.", "magenta"))
    print(colored("They came here to invade my perfect world.", "magenta"))
    print(colored("He came here to ruin everything as he does.", "magenta"))
    print(colored("And now I'm giving you the responsablity to deal with him.", "magenta"))
    print(colored("Take back this world.", "magenta"))
    print(colored("And save us from him.", "magenta"))
    print(colored("The lord of darkness.", "magenta"))
    print()
    print()
    print()


    #start of the real adventure 
    print(colored("Toby wake up! , It's me Suise", "blue"))
    print(colored("This world, the world of Klarg is in ruins.", "blue"))
    print(colored("What will you do?", "blue"))
    Answer = input("Save the World or Let it Die ")

    # asks user if they will save the world 
    if Answer[0] == "S" or Answer[0] == "s":
        print(colored("I knew you would say that come on.", "blue"))
    elif Answer[0] == "L" or Answer [0] == "l":
        print(colored("Hahaha, you joker come on you don't really mean that.", "blue"))
    while not(Answer[0] == "S" or Answer[0] == "s" or Answer[0] == "L" or Answer[0] == "l"):
        print(colored("That doesn't answer my question.", "blue"))
        Answer = input("Save the World or Let it Die")
    print()
    print(colored("In order to save Klarg you need the 8 elemental orbs.", "blue"))
    print(colored("You do know what they are right?", "blue"))
    orbtuter = input("Yes  No ")
    # asks user if they know what orbs are 

    if orbtuter[0] == "Y" or orbtuter[0] == "y":
        print(colored("I knew you would know.", "blue"))
    elif orbtuter[0] == "N" or orbtuter[0] == "n":
        print(colored("Oh well there the 8 elemental orbs that create this world.", "blue"))
        print(colored("You need all of them in order to defeat him.", "blue"))
        print(colored("Not sure if you can beat him with 7 or less of them.", "blue"))
    while not(orbtuter[0] == "Y" or orbtuter[0] == "y" or orbtuter[0] == "N" or orbtuter[0] == "n"):
        print(colored("Ummm what that makes no sense?", "blue"))
        orbtuter = input("Yes  No ")
    print()
    print(colored("Alright lets go to Hugo.", "blue"))
    print(colored("He knows where all 8 orbs are.", "blue"))
    print(colored("Hes our best bet to find where they are.", "blue"))
    print()
    print()
    print()
    # meeting Hugo 
    print(colored("Well Toby here we are.", "blue"))
    print(colored("Hey I see Hugo.", "blue"))
    print(colored("Hey Hugo!", "blue"))
    print(colored("Ug why must you disturb me in this hour.", "green"))
    print(colored("My tea won't drink itself you know.", "green"))
    print(colored("ARE YOU SERIOUS KLARG IS IN DANGER", "blue"))
    print(colored("AND YOU WANNA DRINK TEA!!!", "blue"))
    print(colored("Now now calm down Suise and be more like Toby", "green"))
    print(colored("Whatever,", "blue"))
    print(colored("Now Toby are you willing to scrafice yourself for Klarg?", "green"))
    print()
    KLARG = input("Yes obviously  No (your lame if you choose this) ")
    # asks user if they'll die for klarg 
    if KLARG[0] == "Y" or KLARG[0] == "y":
        print(colored("Very good Toby.", "green"))
    elif KLARG[0] == "N" or KLARG[0] == "n":
        print(colored("Give up on your dreams and die for Klarg.", "green"))
    while not(KLARG[0] == "Y" or KLARG[0] == "y" or KLARG[0] == "N" or KLARG[0] == "n"):
            print(colored("Klarg no understand?", "green"))
            KLARG = input("Yes obviously  No(your lame if you choose this) ")
    print(colored("Now Toby, you and Suise must head off to STORMY STRONGHOLD.", "green"))
    print(colored("There you will find the Air orb.", "green"))
    print(colored("The first elemental orb.", "green"))
    print(colored("Now go you two!", "green"))
    print(colored("Yes sir, alright Toby lets gooooo!", "blue"))
    print()
    print()
    print()

    # chapter 1 
    piller = 0
    print(colored("Welp here we are Stormy Stronghold.", "blue"))
    print(colored("I can see why this place is called Stormy.", "blue"))
    print(colored("There's a GIANT TORNADO", "blue"))
    print(colored("Look at those pillers.", "blue"))
    print(colored("They are shooting a beam of sorts at the tornado,", "blue"))
    print(colored("I think that is what is powering that tornado.", "blue"))
    print(colored("And we know the orb is there should break the pillers?", "blue"))
    print()

    tornado = input("Yes lets break them  No they don't belong to us. ")
    # asks user if they wanna break some pillers 
    if tornado[0] == "Y" or tornado[0] == "y":
        print(colored("Yeah that should reveal the Air Orb.", "blue"))
    elif tornado[0] == "N" or tornado[0] == "n":
        print(colored("Come on lets try and break at least 1 to see what happens.", "blue"))
    while not(tornado[0] == "Y" or tornado[0] == "y" or tornado[0] == "N" or tornado[0] == "n"):
            print(colored("What does that have to do with anything?", "blue"))
            tornado = input("Yes lets break them  No they don't belong to us. " )
    print()

    print(colored("Alrighty lets break these bad boys.", "blue"))
    print("Hey look its heros trying to stop Private Payprus ")
    print(colored("Huh that must be one of the Dark Lords elites.", "blue"))
    print(colored("Lets break em down Toby", "blue"))
    print(colored("I'll distract the gaurds.", "blue"))
    print(colored("You break the pillars", "blue"))
    print(colored("These guys are nothing compared to me!", "blue"))
    print()

    BorS = input("Help Suise or Break a piller ")
    # asks user to help suise or break pillers 
    if BorS[0] == "H" or BorS[0] == "h":
        print(colored("Focus on the pillers not me!", "blue"))
    elif BorS[0] == "B" or BorS[0] == "b":
        piller = piller + 1
        print(colored("Nice now get the others!", "blue"))
    while not(BorS[0] == "H" or BorS[0] == "h" or BorS[0] == "B" or BorS[0] == "b"):
        print(colored("TOBY YOU IDIOT MOVE.", "blue"))
        BorS = input("Help Suise or Break a piller ")
    print(colored("Alright Toby these guys are tougher than they look but it nothing.", "blue"))
    print()

    BorS2 = input("Help Suise or Break a piller ")
    if BorS2[0] == "H" or BorS2[0] == "h":
        print(colored("DON'T focus on me!", "blue"))
    elif BorS2[0] == "B" or BorS2[0] == "b":
        piller = piller + 1
        print(colored("Nice job Toby!", "blue"))
    while not(BorS2[0] == "H" or BorS2[0] == "h" or BorS2[0] == "B" or BorS2[0] == "b"):
         print(colored("TOBY YOU IDIOT MOVE.", "blue"))
         BorS2 = input("Help Suise or Break a piller ")
    print(colored("These guys they...", "blue"))
    print(colored("There no pushovers.", "blue"))
    print()

    BorS3 = input("Help Suise or Break a piller ")
    if BorS3[0] == "H" or BorS3[0] == "h":
        print(colored("Please dont focus on me. Please.", "blue"))
    elif BorS3[0] == "B" or BorS3[0] == "b":
        piller = piller + 1
        print(colored("Keep em coming Toby!", "blue"))
    while not(BorS3[0] == "H" or BorS3[0] == "h" or BorS3[0] == "B" or BorS3[0] == "b"):
         print(colored("TOBY YOU IDIOT MOVE.", "blue"))
         BorS3 = input("Help Suise or Break a piller ")
    print(colored("Toby......", "blue"))
    print()

    BorS4 = input("Help Suise or Break a piller ")
    if BorS4[0] == "H" or BorS4[0] == "h":
        print(colored("Thank you.", "blue"))
        print(colored("But you should have focused on the pillers.", "blue"))
    elif BorS4[0] == "B" or BorS4[0] == "b":
        piller = piller + 1
        print(colored("Great Job!", "blue"))
    while not(BorS4[0] == "H" or BorS4[0] == "h" or BorS4[0] == "B" or BorS4[0] == "b"):
         print(colored("TOBY YOU IDIOT MOVE.", "blue"))
         BorS4 = input("Help Suise or Break a piller ")
    print()

    print(colored("I did it the gaurds are dead it nearly killed me but I'm good.", "blue"))
    if piller != 4:
        print(colored("Toby the tornado and castle are gone.", "blue"))
        print(colored("The air orb is gone.", "blue"))
        print(colored("We failed.", "blue"))
        print(colored("Lets go back to Hugo.", "blue"))
    elif piller == 4:
        print()
        print()
        papereys()
        orbs = orbs + 1

    print()
    print(colored("Hey were back.", "blue"))
    hugo()
    print(colored("So uh where do we go next?", "blue"))
    print(colored("Before I answer that Suise are you ok you look a little.", "green"))
    print(colored("Beaten up.", "green"))
    print(colored("WHAT no I'm fine right chris.", "blue"))
    fine = input("Is she really ok? ")
    print(colored("It does not matter what you answer.", "green"))
    print(colored("Suise is strong and will live.", "green"))
    print(colored("Now lets talk about the next orb.", "green"))
    print(colored("The Water Orb.", "green"))
    print(colored("Where would that be found?", "blue"))
    print(colored("At Leviathan Laggon.", "green"))
    print(colored("Huh that sounds like a lovely place.", "blue"))
    print(colored("It is except for one thing.", "green"))
    print(colored("The Leviathan.", "green"))
    print(colored("A gaint sea monster that will eat anything that it sees.", "green"))
    print(colored("So we gotta stay out of its site.", "blue"))
    print(colored("Correct now go and be carfull Suise please.", "green"))
    print(colored("Whateves.", "blue"))
    print(colored("Toby Please bring Susie back home safe please.", "green"))
    print()

    print()
    print(colored("Whoa look at this place its so...", "blue"))
    print(colored("Holy Crap look at that thing it was so huge!", "blue"))
    print(colored("It ate that entire battle ship...", "blue"))
    print(colored("Wait battle ship?", "blue"))
    print(colored("Oh no one of Kaos's elites must be here!", "blue"))
    print(colored("Look the pirates are trying to gather thoses werid statues.", "blue"))
    statues = 0
    print(colored("Toby theres seems to be 4 of them.", "blue"))
    print(colored("And the is 4 pepastals where they look like they would fit.", "blue"))
    print(colored("Toby lets get them and take the watre orb.", "blue"))
    print(colored("You get the statues and place them down.", "blue"))
    print(colored("I'll distract the pirates!", "blue"))
    print()
    water = input("Yeah lets get them No you look hurt let me do it ")
    # start of quest 2 
    if water[0] == "Y" or water[0] == "y":
        print(colored("That's the spirt!.", "blue"))
    elif water[0] == "N" or water[0] == "n":
        print(colored("What don't let Hugo get in your head.", "blue"))
    while not(water[0] == "Y" or water[0] == "y" or water[0] == "N" or water[0] == "n"):
         print(colored("Are you mute?", "blue"))
         water = input("Yeah lets get them No you look hurt let me do it")
    print()
    print(colored("I'm going to fight them get the staues now.", "blue"))
    print("Hey who are you girly.")
    print(colored("I'm the girl that gonna kill you guys.", "blue"))
    print("Get her.")
    print()
    GorS1 = input("Get a statue or help Suise fight? ")
    if GorS1[0] == "G" or GorS1[0] == "g":
        print(colored("That's right die you cowards!.", "blue"))
        statues = statues + 1
    elif GorS1[0] == "H" or GorS1[0] == "h":
        print(colored("Stay away and let me fight!", "blue"))
    while not(GorS1[0] == "G" or GorS1[0] == "g" or GorS1[0] == "H" or GorS1[0] == "h"):
         print(colored("What are you doing?", "blue"))
         GorS1 = input("Get a statue or help Suise fight? ")
    print()

    GorS2 = input("Get a statue or help Suise fight? ")
    if GorS2[0] == "G" or GorS2[0] == "g":
        print(colored("Huh whats going on over there?!.", "blue"))
        statues = statues + 1
    elif GorS2[0] == "H" or GorS2[0] == "h":
        print(colored("Stay away and let me fight already TOBY!", "blue"))
    while not(GorS2[0] == "G" or GorS2[0] == "g" or GorS2[0] == "H" or GorS2[0] == "h"):
         print(colored("What are you doing stop standing around?", "blue"))
         GorS2 = input("Get a statue or help Suise fight? ")
    print()

    GorS3 = input("Get a statue or help Suise fight? ")
    if GorS3[0] == "G" or GorS3[0] == "g":
        print(colored("Oh no you don't.", "blue"))
        statues = statues + 1
    elif GorS3[0] == "H" or GorS3[0] == "h":
        print(colored("Toby get away!", "blue"))
    while not(GorS3[0] == "G" or GorS3[0] == "g" or GorS3[0] == "H" or GorS3[0] == "h"):
         print(colored("Are you dumb?", "blue"))
         GorS3 = input("Get a statue or help Suise fight? ")
    print()
    print(colored("Toby the pirates have the last staue.", "blue"))
    print(colored("It's ok because I'm on their ship and I have it see.", "blue"))
    print(colored("Here catch.", "blue"))
    statues = statues + 1
    print(colored("Alright nice catch now....", "blue"))
    print("No our battle ship its been eaten!")
    print("Retreat!")
    if statues == 4:
        Krool()
        orbs = orbs + 1
    elif statues != 4:
        print()
    print()
    print()
    print()
    hugo()
    print(colored("But I see Suise is longer with us I take it.", "green"))
    death1 = input()
    print(colored("Be that as it may.", "green"))
    print(colored("It's dangerous to go alone come here Rivi.", "green"))
    print(colored("What is it master?", "yellow"))
    print(colored("Susie died and now Toby needs a new partner.", "green"))
    print(colored("So I'm just replacing Susie.", "yellow"))
    print(colored("YES", "green"))
    print(colored("Alright Toby next place you need to go to is Stonetown.", "green"))
    print(colored("The residents have recovered the Earth orb so this mission should be a breeze.", "green"))
    print(colored("Good luck you two.", "green"))
    print(colored("Its a shame what happened to Suise.", "yellow"))
    print(colored("Our master Hugo found her at a young age.", "yellow"))
    print(colored("She was an outcast for being a brute and women.", "yellow"))
    print(colored("Women in her family were meant ot be classy which Suise did not want to be.", "yellow"))
    print(colored("So they abused her and master took her in and raised as her own.", "yellow"))
    print(colored("Anyway we have some orbs to find let's go", "yellow"))
    print()
    print()
    print() # start of chapter 3
    print(colored("Here we are Stonetown", "yellow"))
    print(colored("Huh where all the local redidents?", "yellow"))
    print(colored("Toby look!", "yellow"))
    print(colored("Its the Earth Orb.", "yellow"))
    print(colored("But ungaurded?", "yellow"))
    print(colored("This is suspicious right?", "yellow"))
    sus = input("Yes  NO ")
    if sus[0] == "Y" or sus[0] == "y":
        print(colored("Yeah.", "yellow"))
    elif sus[0] == "N" or sus[0] == "n":
        print(colored("Really?", "yellow"))
    while not(sus[0] == "Y" or sus[0] == "y" or sus[0] == "N" or sus[0] == "n"):
        print(colored("Well say something.", "yellow"))
        sus = input("Yes  NO ")
    print(colored("well anyway kets get going...", "yellow"))
    print(colored("WHAT ON KLARG IS THAT!!!", "yellow"))
    print()
    print()
    hanz()
    print()
    orbs = orbs + 1
    print()
    print(colored("Come one lets go see Hugo", "yellow"))
    hugo()
    print(colored("I did it.", "yellow"))
    print(colored("I avenged Suise.", "yellow"))
    print(colored("Great now it not the time to cry.", "green"))
    print(colored("Now is time to get the next orb.", "green"))
    print(colored("The Life orb.", "yellow"))
    print(colored("Correct Rivi.", "green"))
    print(colored("It is located at Fallin Forest.", "green"))
    print(colored("Now leave and get to the halfway point of your adventure.", "green"))
    print()
    print()
    print()
    print(colored("Well here OH MY GOD", "yellow"))
    print(colored("Trolls are cutting down the forest.", "yellow"))
    print(colored("Ok I'll take care of whatever elite Kaos has here.", "yellow"))
    print(colored("You take down the 3 saws.", "yellow"))
    saw = 3 
    HorB1 = input("Help Rivi or Break a Saw? ")
    if HorB1[0] == "H" or HorB1[0] == "h":
        print(colored("Toby focus on the saws.", "yellow"))
    elif HorB1[0] == "B" or HorB1[0] == "b":
        print(colored("Alright were is it?", "yellow"))
        saw = saw - 1
    while not(HorB1[0] == "H" or HorB1[0] == "h" or HorB1[0] == "B" or HorB1[0] == "b"):
        print(colored("Well say something.", "yellow"))
        HorB1 = input("Help Rivi or Break a Saw? ")
    print()

    HorB2 = input("Help Rivi or Break a Saw? ")
    if HorB2[0] == "H" or HorB2[0] == "h":
        print(colored("Toby leave me be.", "yellow"))
    elif HorB2[0] == "B" or HorB2[0] == "b":
        print(colored("Found it.", "yellow"))
        saw = saw - 1
    while not(HorB2[0] == "H" or HorB2[0] == "h" or HorB2[0] == "B" or HorB2[0] == "b"):
        print(colored("We I quit everything.", "yellow"))
        HorB2 = input("Help Rivi or Break a Saw? ")
    print()

    HorB3 = input("Help Rivi or Break a Saw? ")
    if HorB3[0] == "H" or HorB3[0] == "h":
        print(colored("Bruh you suck.", "yellow"))
    elif HorB3[0] == "B" or HorB3[0] == "b":
        print(colored("Time to execute.", "yellow"))
        saw = saw - 1
    while not(HorB3[0] == "H" or HorB3[0] == "h" or HorB3[0] == "B" or HorB3[0] == "b"):
        print(colored("I quit everything.", "yellow"))
        HorB = input("Help Rivi or Break a Saw? ")
    print()

    print(colored("Haha time to ", "yellow"))
    print(colored("Rivi watch out the chainsaw", "magenta"))
    print(colored("Toby kill Die...", "yellow"))
    if saw == 0:
        Diementio()
    elif saw != 0:
        print(colored("Well this was a failure.", "magenta"))
    
    print()
    orbs = orbs + 1
    hugo()
    print(colored("And once again alone. ", "green"))
    print(colored("Rivi was never one to show emotion. ", "green"))
    print(colored("Come to me Noelle. ", "green"))
    print(colored("Yes master what is the task at hand? ", "cyan"))
    print(colored("It won't be hard will it?. ", "cyan"))
    print(colored("Get the remaining orbs. ", "green"))
    print(colored("The Tech Orb is at Battlefield good luck soliders.", "green"))
    print(colored("Alright o. ", "cyan"))
    print()
    print()
    print()
    print(colored("Alright now", "cyan"))
    print(colored("This is defenitly a battlefield aye Toby.", "cyan"))
    battle = input("Yes it is  No your just dumb ")
    print("HAULT")
    print("Silence fools.")
    print(colored("we didn't even say anthi...", "cyan"))
    print("Shut up")
    print("Names Corporal Girroro.")
    print("Lets just cut to the chase.")
    print("You want the tech orb ")
    print("Kaos wants you dead time for battle.")
    Girroro()
    print()
    print()
    orbs = orbs + 1
    print()
    print(colored("Were Back!", "cyan"))
    hugo()
    print(colored("There is very little time to waste you two.", "green"))
    print(colored("The next orb the undead orb.", "green"))
    print(colored("Can be found at the Creepy Citadel.", "green"))
    print(colored("What I don't wanna go there.", "cyan"))
    print(colored("To bad.", "green"))
    print(colored("mmmmmm Fine lets go Toby.", "cyan"))
    print()

#start of the 6th chapter 
    print()
    print(colored("Well here we are.", "cyan"))
    print(colored("Toby I cant do this.", "cyan"))
    print(colored("Then I'll take care of you.", "magenta"))
    print(colored("Wha What are you doing with that sword.", "cyan"))
    print(colored("Toby wait I'm sor...", "cyan"))
    print(colored("Only the strong will survive.", "magenta"))
    print(colored("And none of you belong here.", "magenta"))
    print()
    print()

    Darkrai()
    orbs = orbs + 1

    print(colored("Alright Hugo.", "magenta"))
    print(colored("I have another orb now what.", "magenta"))
    hugo()
    print(colored("I see Noelle is dead.", "green"))
    print(colored("Malketh get over here and help Toby.", "green"))
    print(colored("I am here.", "red"))
    print(colored("So your the last one I see.", "magenta"))
    print(colored("What?", "red"))
    print(colored("Now time is no more.", "green"))
    print(colored("Now go to Lava Lakes Railroad.", "green"))
    print(colored("That is where the next orb.", "green"))
    print(colored("The Fire Orb", "green"))
    print(colored("YAY FIRE.", "red"))    
    print(colored("Now go!", "green"))
    print(colored("YAY!!!! For KLARG", "red"))
    print()
    print()
    print()
    print(colored("YAY LAVA OF KLARG.", "red"))
    print(colored("Shut up Malketh and listen up stay out of my way.", "magenta"))
    print(colored("YAY KLARG KLARG KLARG", "red"))
    joke = input("Is this guy a joke or what? ")
    print(colored("I hate you.", "magenta"))
    print(colored("Hey Klarg is drowning in the Lava.", "magenta"))
    print(colored("NOOOOOOO DON'T WORRY KLARG I WILL SAVE YOU.", "red"))
    print(colored("And that ladies and gentelman is how you burn someone alive.", "magenta"))
    print()

    Ridley()
    orbs = orbs + 1
    print()
    print()

    print(colored("Stop I now know what your doing you let your comrads die.", "green"))
    print(colored("Wait whats going on.", "green"))
    think = input("What do you think? ")
    print(colored("glyacb laycvayluvcljsbcjywagd adiyg lqayusfc ", "green"))
    print(colored("Dark Darker yet Darker [[Hyperlinked Blocked]]", "green"))
    print(colored("Now there's only 2 beings left the General.", "magenta"))
    print(colored("And Kaos himself.", "magenta"))
    print(colored("Now I only need one more orb.", "magenta"))
    print(colored("Considering you followed my instructions.", "magenta"))
    print(colored("Did you follow my instruction?", "magenta"))
    did = input("Did you? ")
    print(colored("HAHAHA who am I kiddding?", "magenta"))
    print(colored("You know I don't care.", "magenta"))
    print(colored("Time to go to the Arkeyan Armory.", "magenta"))
    print(colored("To kill the General and get that last orb.", "magenta"))
    print(colored("The Magic Orb.", "magenta"))
    print()
    print()
    print()
    # Chapter 8 

    print(colored("Look at this place.", "magenta"))
    General()
    orbs = orbs + 1
    print()
    print()
    print(colored("I hopefully have them all I'm blind to this info.", "magenta"))
    print(colored("But now time to see Kaos.", "magenta"))
    print()
    print()
    print()
    ready = input("Ready? ")
    print(colored("good time to go.", "magenta"))
    print()
    print()
    print(colored("Hello there Kaos long time no see.", "magenta"))
    print("Toby.")
    print("What you have done is unforgivable.")
    print("Your outmatched Tobey.")
    print(colored("What do you mean.", "magenta"))
    print(name, "is on my side in this fight.")
    print(colored("Go ahead take that idiot.", "magenta"))
    die = input("Say we will stop you!")
    if orbs == 8:
        print(colored("Then you shouldn't have collected all 8 orbs.", "magenta"))
    else:
        print(colored("To bad I have all the...", "magenta"))
        print(colored("No this can't happen no I won't let you.", "magenta"))
        killP = input("Kill (Press any button hes to weak) ")
        print("You did it you stopped Toby.")
        print("Now we have peace.")

    print("Input a letter and then press enter to watch the credits.")
    credits = input("Press a key to see credits! ")
    filename21 = "Rick_Roll.mp3"
    mixer.music.load(filename21)
    mixer.music.play(loops=-1)
    while True: # end credits
        if credits[0] != " ":
            print("Directed by: Danny Romano")
            print("Produced by: Danny Romnao")
            print("Written by: Danny Romano")
            break 

    x = input("Press a button and then enter to exit. ")
    
    
    
    





    


#YOU ARE HERE DANNY LOOK HERE FOR WHEN YOU NEED TO ADD NEW CODE OUTSIDE OF FUNCTIONS 


def hugo():#greeting to the player for every time they get back
     print(colored("Ah I see you have retuned Toby.", "green"))


# the papyrus boss 
def papereys(): #the first boss battle if player meets conditions 
    print()
    print(colored("Tobey the tornado is gone and there's the castle come on!", "blue"))
    print(colored("Here we are in the middle the air orb should be here but", "blue"))
    print("Nyheheh")
    print("At last the hero arrives on scene to stop me.")
    print(colored("What who said that!", "blue"))
    print("Me.")
    print("Private Payprus one of the 8 elites of Lord K...")
    print(colored("HAHAHAHAHA", "blue"))
    print(colored("Your one of the elites.", "blue"))
    print(colored("And hear I though that this would be a hard quest.", "blue"))
    print(colored("Guess I was wrong.", "blue"))
    print("How dare you insult me like that!")
    print("I'm an elite what does an elite half to do to get some resepct.")
    print("Is it to much to ask for?")
    print(colored("Toby he has the air orb lets get it from him and end this!", "blue"))
    print("So your challenging me HA.")
    print("You'll loose so eaily it won't even be funny.")
    print()
    fight1 = input("Are you ready? Yes No ")
    filename1 = "Bonetrousle.mp3"
    mixer.music.load(filename1)
    mixer.music.play(loops=-1)
    while True: #battle 1 and music plays
        if fight1[0] != " ":
            print("It doesn't matter prepare to brawl!")
            break
    print()
    health1 = 3 # bosses health AND BOSS FIGHT start 
    battle1A = input("Fight or Admire ")
    if battle1A[0] == "A" or battle1A[0] == "a":
        print("Ummm thanks? I guess?")
        print(colored("Toby what are you doing?", "blue"))
    elif battle1A[0] == "F" or battle1A[0] == "f":
        health1 = health1 - 1
        print("Owww how rude.")
        print(colored("Great Job!", "blue"))
    while not(battle1A[0] == "A" or battle1A[0] == "a" or battle1A[0] == "F" or battle1A[0] == "f"):
        print(colored("TOBY YOU IDIOT MOVE.", "blue"))
        battle1A = input("Fight or Admire ")
    print()
    battle1B = input("Fight or Admire ")
    if battle1B[0] == "A" or battle1B[0] == "a":
        print("Wha What are you doing stop?")
        print(colored("Ok I'm weried out whats wrong man?", "blue"))
    elif battle1A[0] == "F" or battle1A[0] == "f":
        health1 = health1 - 1
        print("Owww that really hurt oww..")
        print(colored("Toby he's almost defeated!", "blue"))
    while not(battle1A[0] == "A" or battle1A[0] == "a" or battle1A[0] == "F" or battle1A[0] == "f"):
        print(colored("TOBY YOU IDIOT MOVE WERE IN THE MIDDLE OF A FIGHT.", "blue"))
        battle1B = input("Fight or Admire ")
    print()
    battle1C = input("Fight or Admire ")
    if battle1C[0] == "A" or battle1C[0] == "a":
        print("...")
        print(colored("Ummmm?", "blue"))
    elif battle1C[0] == "F" or battle1C[0] == "f":
        health1 = health1 - 1
        print("UGGG")
        print(colored("Yes eat it dirtbag!", "blue"))
    while not(battle1A[0] == "A" or battle1A[0] == "a" or battle1A[0] == "F" or battle1A[0] == "f"):
        print(colored("TOBY YOU IDIOT MOVE WERE IN A FIGHT!.", "blue"))
        battle1C = input("Fight or Admire ")
    mixer.music.stop()
    if health1 >= 1:
        print()
        print("You spared me and admired me!")
        print("Thank you.")
        print("You actualy respect me.")
        print("Truth is I only ever wanted respect.")
        print("That's the only reason I joined lor..")
        print("I mean Kaos.")
        print(colored("I guessing that's the name of the boss around here.", "blue"))
        print("It is.")
        print("he wants you guys dead.")
        print("Not only do the orbs create the world but.")
        print("They destroy Kaos as well.")
        print("They are perfectly balanced as all things should be.")
        print("Here take this the Air Orb.")
        print("It's the first step to killing him.")
        print("Some of us like me you can spare but others...")
        print("You will have to kill them good luck.")
        print(colored("Thanks dude see ya again.", "blue"))
        print()
    else:
        print("Oof I only wanted ...")
        print(colored("Nice job now we have the orb.", "blue"))
# the krool boss 
def Krool():
    print("Hahaha")
    print("Well is someone upset about the death of ye friend?")
    print("Well I lost me battleship so I guess were even heh heh.")
    print("The names Kaptain Krool.")
    print("Loyal Captain to thee Drak Lord himself.")
    print("And I know why you two landlubbers came out here.")
    print("To steal me tresure Argh.")
    print("Lord Kaos himself gave me these treasures and I ain't going down without a fight.")
    print()
    fight2 = input("Ready to face off against me? ")
    filename2 = "GangPlankGalleon.mp3"
    mixer.music.load(filename2)
    mixer.music.play(loops=-1)
    while True: #battle 2 starts and more music
        if fight2[0] != " ":
            print("Arg prepare to walk thee plank. ")
            print("And join yee friend.")
            break
    print()
    health2 = 3 # bosses health and start of boss
    battle2A = input("Fight or Talk")
    if battle2A[0] == "T" or battle2A[0] == "t":
        print("I just want the real Trusure thats all.")
    elif battle2A[0] == "F" or battle2A[0] == "f":
        health2 = health2 - 1
        print("Shiver me timbers yee tougher than I expected.")
    while not(battle2A[0] == "T" or battle2A[0] == "t" or battle2A[0] == "F" or battle2A[0] == "f"):
        print("Just because Susie is gone doesn't mean do nothing")
        battle2A = input("Fight or Talk ")
    print()

    battle2B = input("Fight or Talk ")
    if battle2B[0] == "T" or battle2B[0] == "t":
        print("No one in this god for sakken universe has the Treasure.")
        print("And why are you not fighting you coward.")
    elif battle2B[0] == "F" or battle2B[0] == "f":
        health2 = health2 - 1
        print("Arrrg")
    while not(battle2B[0] == "T" or battle2B[0] == "t" or battle2B[0] == "F" or battle2B[0] == "f"):
        print("Just because Susie is gone doesn't mean do nothing")
        battle2B = input("Fight or Talk ")
    print()

    battle2C = input("Fight or Talk ")
    if battle2C[0] == "T" or battle2C[0] == "t":
        print("No one in this god for sakken universe has the Treasure.")
        print("And why are you not fighting you coward.")
    elif battle2C[0] == "F" or battle2C[0] == "f":
        health2 = health2 - 1
        print("Arrrg noooo!")
    while not(battle2C[0] == "T" or battle2C[0] == "t" or battle2C[0] == "F" or battle2C[0] == "f"):
        print("Just because Susie is gone doesn't mean do nothing")
        battle2C = input("Fight or Talk ")
    print()
    # stops the music
    mixer.music.stop()
    if health2 >= 1:
        print("Omg you do have it.")
        print("You have the BANNANA!!!!")
        print(colored("Why do you want that so bad", "magenta"))
        print("Potassium")
        print("Anyway sorry about yer dead friend.")
        print("Hope giving you the water orb helps.")
    else:
        print("Yarrg")
        print("Looks like I walked the plank this time.")

# the hanz fight
def hanz():
    print("Well well well.")  
    print("If it isn't some of Hugos lackys.")
    print("Word on the street is one of yall died to the captain.")
    print(colored("We are not lackys and how dare you speak of Susie that way.", "yellow"))
    print("Quite down shorty.")
    print(colored("SHORTY!!!", "yellow"))
    print(colored("Toby lets kill this slime.", "yellow"))
    print("Slime heh funny you call me that for that is what I am.")
    print("Not only that I'm the Colonel under Kaos")
    print("You ready to be swallowed whole?")
    print("Just like the residents o fthis humble town?")
    fight3 = input("Ready or Not? ")
    filename3 = "Konosuba.mp3"
    mixer.music.load(filename3)
    mixer.music.play(loops=-1)
    while True: #Battle 3 music 
        if fight3[0] != " ":
            print("Prepare to die slowly!")
            break
    print()
    health3 = 3
    battle3A = input("Fight or Run ")
    if battle3A[0] == "R" or battle3A[0] == "r":
        print("You coward!")
        print(colored("I'll take care of this.", "yellow"))
        health3 = health3 - 1
    elif battle3A[0] == "F" or battle3A[0] == "f":
        health3 = health3 - 1
        print("Gloop Gloop")
    while not(battle3A[0] == "R" or battle3A[0] == "r" or battle3A[0] == "F" or battle3A[0] == "f"):
        print(colored("If you stay still the slime will kill you.", "yellow"))
        battle3A = input("Fight or Run ")    
    print()

    battle3B = input("Fight or Run ")
    if battle3B[0] == "R" or battle3B[0] == "r":
        print("What a little weaking.")
        print(colored("Says you.", "yellow"))
        health3 = health3 - 1
    elif battle3B[0] == "F" or battle3B[0] == "f":
        health3 = health3 - 1
        print("Gloop do de Scoop")
    while not(battle3B[0] == "R" or battle3B[0] == "r" or battle3B[0] == "F" or battle3B[0] == "f"):
        print(colored("If you stay still the slime will kill you.", "yellow"))
        battle3A = input("Fight or Run ")    
    print()

    battle3C = input("Fight or Run ")
    if battle3C[0] == "R" or battle3C[0] == "r":
        print("AHHHHHHH")
        print(colored("For Susie!!!", "yellow"))
        health3 = health3 - 1
    elif battle3C[0] == "F" or battle3C[0] == "f":
        health3 = health3 - 1
        print("AHHHHHHH")
        print(colored("For Susie!!!", "yellow"))
    while not(battle3C[0] == "R" or battle3C[0] == "r" or battle3C[0] == "F" or battle3C[0] == "f"):
        print(colored("If you stay still the slime will kill you.", "yellow"))
        battle3C = input("Fight or Run ")    
    print()
    mixer.music.stop()
    print(colored("He's dead.", "yellow"))
    print(colored("I avenged you Suise.", "yellow"))
    print()
    





# Boss number 4 
def Diementio():
    print("HAHAHAHA")
    print("At last we finally meet.")
    print("I am the pleasure of crowds.")
    print("The master of diemensions.")
    print("I am Lieutenant Diemento.")
    print("Charming Magician")
    print("I know what you want.")
    print("But do you know what I want?")
    what = input("What does he want? ")
    print("I just want to die.")
    print("The same way Rivi did.")
    print(colored("What are you talkig about clown.", "magenta"))
    print("Suise was the love of his life and to see her die.")
    print("Made him want to die.")
    print("And I also love my love too long ago.")
    print("That's why I joined Kaos.")
    print("Now fight me.")
    fight4 = input("Will you fight? ")
    filename4 = "It's_Showtime.mp3"
    mixer.music.load(filename4)
    mixer.music.play(loops=-1)
    while True: # battle 4 and music
        if fight4[0] != " ":
            print("Please kill me.")
            break 
    battle4A = input("Kill or nothing? ")
    if battle4A[0] == "K" or battle4A[0] == "k":
        print("Thank you now take the Life orb.")
    elif battle4A[0] == "N" or battle4A[0] == "n":
        print("Fine take the orb I'll do it myself")
    while not(battle4A[0] == "K" or battle4A[0] == "k" or battle4A[0] == "N" or battle4A[0] == "n"):
        print("Make your choice now. ")
        battle4A = input("Kill or nothing? ")
    mixer.music.stop()
    print()

        
def Girroro():

    fight5 = input("Are you ready? ") #boss 5 and more music
    filename5 = "Cuphead.mp3"
    mixer.music.load(filename5)
    mixer.music.play(loops=-1)
    while True:
        if fight5[0] != " ":
            print("WAR!!!!!!")
            break 

    print()
    health5 = 3
    battle5A = input("Fight or Steal ")
    if battle5A[0] == "F" or battle5A[0] == "f":
        health5 = health5 - 1 
        print(colored("Toby this guy is insane I think we can just take the orb.", "cyan"))
        print(colored("As long as we admit defeat.", "cyan"))
    elif battle5A[0] == "S" or battle5A[0] == "s":
        print("AHHHHHHHHHH CHARGE!!!")
    while not(battle5A[0] == "F" or battle5A[0] == "f" or battle5A[0] == "S" or battle5A[0] == "s"):
        print(colored("TOBY RUN!", "cyan"))
        battle5A = input("Fight or Steal ")
    print()

    battle5B = input("Fight or Steal ")
    if battle5B[0] == "F" or battle5B[0] == "f":
        health5 = health5 - 1 
        print(colored("Toby I don't like killing please stop.", "cyan"))
    elif battle5B[0] == "S" or battle5B[0] == "s":
        print("Requesting backup!")
    while not(battle5B[0] == "F" or battle5B[0] == "f" or battle5B[0] == "S" or battle5B[0] == "s"):
        print(colored("TOBY MOVE!", "cyan"))
        battle5B = input("Fight or Steal ")
    print()

    battle5C = input("Fight or Steal ")
    if battle5C[0] == "F" or battle5C[0] == "f":
        health5 = health5 - 1 
        print(colored("TOBY!", "cyan"))
    elif battle5C[0] == "S" or battle5C[0] == "s":
        print("Total Domination")
    while not(battle5C[0] == "F" or battle5C[0] == "f" or battle5C[0] == "S" or battle5C[0] == "s"):
        print(colored("TOBY HURRY!", "cyan"))
        battle5C = input("Fight or Steal ")
    print()
    mixer.music.stop()
#endings for girroro
    if health5 >= 1:
        print("AHHHH You admit defeat good bye losers.")
        print(colored("Oh no we lost.", "cyan"))
        print("Now leave and never return.")
    else:
        print("White flag.")
        print(colored("Toby I don't like killing.", "cyan"))
        print(colored("Please lets not dp that.", "cyan"))

def Darkrai():
    print(colored("Alright Sgt Darkrai I'm here.", "magenta"))
    print("Yes you are.")
    print(colored("It's now time to fill your role in my world Sgt.", "magenta"))
    print("I will not.")
    dare = input("Ask why not? ")
    print(colored("Shut up I don't care what you have to say.", "magenta"))
    print("Dont talk to...")
    print(colored("Enough now I get to say prepare for battle.", "magenta"))
    fight6 = input("Do you accept what is happening here? ")
    filename6 = "Berdly.mp3"
    mixer.music.load(filename6)
    mixer.music.play(loops=-1)
    while True: #battle 6 and more music
        if fight6[0] != " ":
            print(colored("You don't matter here.", "magenta"))
            break
    print("Tobey stop this madness.")
    print("Kaos can't win.")
    print(colored("Shut up!", "magenta"))
    print(colored("This is my world you hear me.", "magenta"))    
    print(colored("A world for me and me alone.", "magenta"))
    print("Then I must kill you if you want everyone else dead.")
    battle6 = input("Kill or Kill")
    mixer.music.stop()
    print(colored("When will you learn you don't have a choice.", "magenta"))
    print(colored("Even if you agree.", "magenta"))
    print("Nooo")
    print("Heheh I guess the only one who can save us now is....")
    laugh = input("Your choices don't matter anymore. How do you feel? ")
    print(colored("Now time to collect the undead orb.", "magenta"))
    

# Battle 7 starts here
def Ridley():
    print("You dare enter my lair.")
    print("You Plebian.")
    print(colored("You will die at my hands Admiral Ridley.", "magenta"))
    print("You think that but look at you compared to me your nothing.")
    fight7 = input("How do you feel about this? ")
    filename7 = "One_Winged_Angel.mp3"
    mixer.music.load(filename7)
    mixer.music.play(loops=-1)
    while True: # Plays battle theme and starts the real boss battle
        if fight7[0] != " ":
            print("I will put you back together.")
            print("And take you apart all over again.")
            break
    print()
    health7 = 3 # boss hp
    battle7A = input("Kill or Help ")
    health7 = health7 - 1
    print("Ahhhhh you think that is enough to kill me?")
    print(colored("That weak of an attack did that much damage, weak.", "magenta"))
    battle7B = input("Kill or Help ")
    health7 = health7 - 1
    print("Ok that may have done some damage.")
    print(colored("This isn't even my final form.", "magenta"))
    print("What?")
    battle7C = input("Watch Ridley die slowly. ")
    health7 = health7 - 1
    mixer.music.stop()
    print(colored("Die Die Die Die Die Die.", "magenta"))
    print(colored("What's the matter you wanna save ridley don't you.", "magenta"))
    print(colored("Too Bad.", "magenta"))
    print(colored("You get to watch me kill and kill him again and again.", "magenta"))
    print(colored("How does that make you feeeeel.", "magenta"))
    feel = input("Just put something man. ")
    print(colored("Just read what goes on.", "magenta"))
    print(colored("You failed.", "magenta"))
    print()


def General():
    print("You finally arrive.")
    print(colored("Let me kill you.", "magenta"))
    print("Violent much are we. ")
    fight8 = input("Lets get the last orb ")
    filename8 = "Darkness.mp3"
    mixer.music.load(filename8)
    mixer.music.play(loops=-1)
    while True: # 8th boss 
        if fight8[0] != " ":
            print("It's showtime")
            break
    print() # Final battle
    slash = input("Wanna see something funny? ")
    print(colored("Shut up you have no more power here this is my world.", "magenta"))
    print("Who are you talking to?")
    print("Wait no.")
    watch = input("Watch helplessly or watch helplessly? ")
    mixer.music.stop()
    print()

if __name__ == "__main__":
    main()