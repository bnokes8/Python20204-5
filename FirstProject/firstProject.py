#Johnathan sall
#sean fullmer
#aiden searle
#Brady Nokes
#Revenge of the Rainbow Dragon
#choose your own adventure
#10/21

### Brady Nokes code start
print("Welocme to the game. \nWe hope you have fun. \nThe name of this book is 'The Revenge of the Rainbow Dragons by Rose Estes'. \nGood luck.")#1
# The choice and end pages will be marked in the name of the function with either an e or a c after the number. Make sure to capitalize the e or c
# The "End" is an ending and doesnt siginfy the end of the game
# The functions without an E or C are regular pages and they will just move on ot hte next page. The others we will need to make and if/elif/else statement
# depending on the users choice
# The page numbers are sometimes skipped, those are pictures and I dont want any confusion with the code.
# We are using def to make functions of the pages. Later on in the code we can call the functions when needed.
def page1C() :
    print('''\nOnce upon a time a young wizard's apprentice named Jaimie
joined the master wizard, Pentegarn, in a war
of wizards at Rainbow Castle. YOU are Jaimie and you control your own fate. Tricked
into leaving Pentegarn's side, you must battle
strange monsters and magical creatures in
order to save you and your friends from al- most certain death in the tunnels and towers
of the magical castle.
What will you do?
Forced into a tower high in the castle, you
must choose from several dangerous paths to
win your way to freedom.
1) If you want to try to climb down the
outside of the tower, turn to page 12.
2) If you want to go down the hidden
staircase into the unknown, turn to
page 105.
3) If you decide to fight the three-headed
dog blocking the door, turn to page 8. Whichever path you pick, you are sure to find
adventure, as you turn the pages of
REVENGE OF THE RAINBOW DRAGONS''')
    choice1 = input("Page 12 or 8?: ")
    if "12" in choice1:
        page12C()
    elif "8" in choice1:
        page8()
    else:
        print("That is not recognized")
def page5() :
    print('''\nFoxes aren't supposed to fly, Jaimie,"
Fox says nervously, as he hovers in
midair. "How about putting me down?
Leave the flying to Featherface. I feel better on old terra extra-firma."
"Hush, Friend Fox," scolds Pentegarn.
"Consider yourself part of an important les- son. This is the first time Jaimie has levitated
an object. And you know he needs silence to
concentrate."
"Now I'm an object," mutters Fox in disgust, as he dangles above the ground.
You ache with the effort ofholding the spell.
Just as you feel you are mastering the skill, a thunderous noise rolls through the room. Your
concentration breaks and Fox falls to the floor
with a thump.
"Oh, Fox, I'm sorry," you cry, rushing to his
side. "I'll be more careful next time."
"Next time?" growls Fox. "Forget it! I have
to go dig a den—a very long one." He turns
and trots quickly from the room.
"Unfortunate attitude," says Owl. "But what
can one expect from the family Canidae?"
"Well done, child," says Pentegarn. "You're
moving ahead nicely with your studies. I hadn't planned on your being able to lift objects for another six months or so. But now
that we've been interrupted, I suppose we'd
better see who's at the door." And he makes a
small gesture with his hand.''')
    input("Press enter to go to the next page")
    page6()
def page6() :
    print('''\nPoof! A cloud of dust appears, then clears.
Before you stands a travel-stained man, one
hand raised as if knocking on a door.
Lowering his hand, the traveler snaps, "Do
you always answer doors like that? But then,
what else should I expect from a wizard?"
Giving a short bow, he says, "Sir, I come from
Rainbow Castle. Your presence is required, no
later than four days hence."
"Is it a party?" you ask hopefully.
The messenger fixes you with an icy glance.
"Hardly. You will answer to charges of occu- pying the Castle of the Pillars and calling
yourselves 'Wizard and Apprentice.' This castle is part of the domain assigned to the wizards Malus, Pothos, and Rubus. Unless you
can support your claim to the castle and win
their permission to practice wizardry in the
area, you will be banished from this land,"
says the messenger coldly. "And now, if you
will show me the door, I will return to Rainbow Castle."
Poof! A cloud of smoke forms in front of the
messenger, and when it clears, a large wooden
door stands before him.
"A mere first-level spell," sneers the messenger. "You'll have to do better than that at
Rainbow Castle." Still sneering, he turns and
strides out of the room. "Rainbow Castle? Wizards? What's this all
about, sir?" you ask worriedly.
"Centuries ago, when I lost my kingdom to
the Evil One, Rainbow Castle was in the
hands ofthe forces of good," sighs Pentegarn,''')
    input("Press enter to go to the next page")
    page7C()
def page7C() :
    print('''\nObviously, while I was in the Evil One's
power, the balance changed. I think we had
better meet with them. It is always best to be
polite to one's neighbors."
"I think Fll sit this one out," says Fox, poking his head through the doorway. "That fel- low didn't look too pleasant, and he's only the
messenger."
"Pshaw!" says Owl. "Don't be such a co- ward. Remember: Cowards die a thousand
deaths. The valiant die but once."
"Go feather a nest, Beak Brain," growls
Fox.
"We will let Jaimie decide. As my apprentice and the heir to this kingdom, Jaimie must
learn to make good, sound decisions," says
Pentegarn. And suddenly there are three pairs
of eyes staring at you.
"Well," you stammer, thinking quickly, "the
way I see it, we have only two choices:
1) "Go to Rainbow Castle and see if we
can work out our problems with our
neighbors." Turn to page 110.
2) "Ignore them and don't go." Turn to
page 83.''')
    print("This part of he game is not accessible yet. Please start from the beggining")
    page1C()
def page8() :
    print('''\n"I don't like the idea of climbing down from
this tower," you say. "High places make me
dizzy. And that fireplace stairway must be a
trap. Otherwise we wouldn't have found it so
easily. I have an idea! Let's fight that
creature—or rather, let's trick it." Still concentrating on keeping the spiders
up on the ceiling, you back up behind the door
and motion Fox and Owl to join you. "Be
ready to move—fast!—when I give you the
word." And you open the door quickly.
Snapping, snarling jaws snatch at you as
the three-headed dog bursts into the room. At
the instant you open the door, you drop your
concentration, ending the levitation spell. Before the dog can even reach you, it is covered
by the rug full of spiders. Shrieking in fear
and pain, the dog falls to the floor and rolls over and over, trying to shake off the spiders.
It does no good. Gradually, its agonized
thrashing grows slower and slower and then
ceases. Instantly, the spiders begin to spin,
and within seconds, the awful three-headed
dog is completely encased in spider silk.
"Kid, I hate to interrupt the show, but don't
you think we should leave before they decide
we'd make a nice dessert?" asks Fox.
Even as he speaks, a few spiders leave the
dog and move toward you. Jolted into action,
you yell loudly and the three of you race through the door and slam it. You pound down a narrow, winding stairway, wild with relief at escaping the spiders,''')
    input("Press enter to go to the next page.")
    page10C()
def page10C() :
    print('''\nthe dog, and the room—until Owl perches on
your shoulder and says, "Perhaps a more
moderate pace would be indicated by the multitude of dangers we have encountered in such
a short span of time."
"I think he means slow down, Jaimie," says
Fox. "It's not a bad idea." Turning to Owl, he
says, "If we ever get out of here, I'm going to
press you between the pages of the biggest
dictionary I can find. You can learn some
simple words there!"
Your heart is pounding and your knees are wobbly, but you can't help laughing at Fox's
words. Weakly you sink to the step and lean
against the cold stone wall.
Just as you are about to speak, you hear an
eerie howl coming from somewhere ahead of
you—a howl that sends chills up and down
your spine. You huddle up against the wall
and, to your amazement, it moves beneath
your touch. An opening appears.
"OOOOOOOO!" wails the creepy howl.
"It would appear that something this way
comes," says Owl.
1) If you want to find out what is making
the awful noise, turn to page 49.
2) If you want to slip into the open space in
the wall, turn to page 76.''')
    if "49" in input("Page 49 or page 76?: "):
        page49()
    else:
        print("That is not recognized or it is not yet open")
def page11E() :
    print('''\n"I don't think they should go," you say. "I
mean, there's so many of them. Why don't
they stay here and we'll come back for them
later?"
"NO!" cries Quentin, and before you can
say another word, he grabs you by the neck
and flings you into a small stone room. Fox
and Owl follow you with a thump and a crash,
and the door closes firmly behind them.
"I thought you understood," yells Quentin
as he stomps away. "But you're just like all
the others! Mushrooms have rights too!"
"Good going, kid," growls Fox. "Have you
ever thought of being a diplomat?"
The three of you sit and stare at each other.
You are all covered with smears of the glowing fungus. Lighting your own way, you ex- plore the tiny room. "We must hope that our captors are mushrooms of honor and that they mean well and
will return for us," says Owl. "I suggest that
we entwine our metacarpals and pray."
And so you sit, glowing in the dark, with
claws, paws, and fingers crossed, hoping that
this is not
THE END	''')
    input("You have reached the end of the game, press enter to start at the beginning...")
    page1C()
def page12C() :
    print('''\nFighting the cold, blowing wind and rain,
you squeeze through the narrow window. Behind you, you hear the rug drop and the plop,
plop, plop of falling spiders.
"Do me a favor, kid—don't fall, huh," quavers Fox from inside your shirt. "I'm too gorgeous to become a grease spot."
"Don't worry, Fox. I don't want to fall
either."
As you clutch the tough stems of the ivy, you
shout to Owl, who flaps near your shoulder.
"At least we don't have to worry about those
wizards. They can't get us up here."
"Hold fast, youngster," calls Owl. "We are about to be engulfed by a large cloud."
You turn in time to see a large mass of pinkish stuff close in on you, and then you see nothing. You bury your face against the
crispness of the vine, its bark rough beneath
your fingers, hoping that the cloud will pass
quickly. Fox scrambles out of your shirt and
disappears into the mist.
And then a strange thing happens—you no
longer feel the shrubbery, and the comforting
solidity of the vine fades from your grasp. It feels as if you were drifting away on a misty
cloud.
Please turn to page 69.''')
    input("Press enter to go to the next page")
    #page69() but it is not coded in so it will tell them that the page is not in the game yet
    print("The next page is not in the game yet, taking you back to the start")
    page1C()
def page13() :
    print('''\nYou continue urging Pentegarn to wake up,
while concentrating on the spell. Just as you
are beginning to despair, Pentegarn moves.
"Hooray! He's waking up!" yips Foxjoyfully.
All at once, a brilliant light floods the dark
room. You hear screams of anguish and terror. Opening your eyes, you see confusion. Owl
flies about the room, dipping and wheeling,
looking for an enemy who has vanished.
Imogene screams and hollers and stamps
her feet in rage, crying, "They're gone! They're
gone! And now I'll never know!"
Turning in wonder to Pentegarn, now upright and alert, you notice that he holds on his
outstretched palm the Cube of Mystic Forces.
It sits serene, crystal clear, and glowing with a strange warmth. Inside the cube, hands and
faces pressed desperately against its clear
surfaces, are the three evil wizards.
Eyes open wide, you stare at the tiny fig- ures. "Wow! How did you do that?"
"You'll learn some day, Jaimie, when you
have the wisdom to handle such power," says
Pentegarn, placing his arm around you.
"Where are they? What have you done with
them?" screeches a shrill voice, and suddenly
Pentegarn gasps and clutches his ankle.
"Imogene, don't! This is Pentegarn, my
great-grandfather! He's a powerful wizard
and a good guy!"
"What's he done with my rotten uncles?"
screeches Imogene. "I've got to find out where
my father is!"''')
    input("Press enter to go to the next page")
    page15()
def page15() :
    print('''\n"Here they are," says Pentegarn, holding
out the cube, "and I'll find out the answer to
that question if you promise not to kick me
again."
Imogene's face turns a deep, dark red and
her foot trembles, but at last she mutters, "All
right, but find out fast!"
Pentegarn places the cube against his forehead and closes his eyes. Instantly a bright
yellow glow surrounds the cube and the tiny
figures inside sag limply.
Seconds later, Pentegarn lowers the cube
and smiles. "There, that wasn't hard. Your
father is in the dungeons, my dear, and we'll rescue him in a minute. But first, what shall
we do with these fellows?"
"Stamp on them!" shrills Imogene. "No,
wait!" An evil grin crosses her face. "Can we
send them anywhere I want and make sure they can't get back?"
"Certainly," says Pentegarn. "As long as they can do no harm to anyone else."
"Don't worry, they'll be the ones in
danger—from each other," smiles Imogene
slyly. "Let's send them back up to Limbo and
put them where they put me. It'll serve them
right!"
"Done!" says Pentegarn, and placing the
cube to his forehead once more, he closes his
eyes. The cube turns pink and then slowly
pales, becoming clear. And then it is totally
empty.
"Wow!" you breathe in awe.''')
    input("Press enter to go to the next page")
    page16E()
def page16E() :
    print('''\n"How come they got you, Pentegarn? I figured you could take those guys with one hand
tied behind your back," says Fox.
"They cheated, my furry friend. They
brought a powerful magical amulet into the
contest. Against it, I was helpless. And without your timely help, I would have been lost. You have my everlasting thanks."
"It was nothing," says Owl.
"Sure it was! It was quick, brilliant thinking
and brave action on my part," growls Fox.
"Speak for yourself, Bird Brain."
"And now that we have solved the question
of who has the right to practice magic, I suggest we bid farewell to Rainbow Castle and
return home," says Pentegarn.
"AFTER we find my father," demands Imogene, lifting her foot in a threatening manner.
"And maybe, after we get home, I can learn
to do something besides levitate," you say. "If
things keep going like this, Fm going to need
it." THE END''')
    input("You have reached the end of the game, press enter to start at the beginning...")
    page1C()
def page17() :
    print('''\n"If these guys scare US—and we're kind of
used to them—imagine how those wizards upstairs will feel," snickers Fox.
"The element of surprise would indeed be
useful/' adds Owl.
"All right, we'll all go," you say.
"Let's get ready then. The messenger should
be here soon," says Quentin.
The mushroom men hide themselves in
another corridor, and you, Fox, Owl, and
Quentin crouch beside the cave entrance,
waiting quietly.
Soon you hear footsteps hurrying toward
you, and a figure passes through the doorway.
Instantly, all of you fling yourselves upon the
figure and bring him crashing to the ground.
A muffled snarl erupts from beneath you.
"You dare lay hands upon a wizard's official
messenger?"
"We'll lay more than hands on you if you
don't cooperate," snarls Fox, showing his
long white fangs.
"I won't do it, whatever it is you want. And
no matter how you threaten or bribe me, I won't show you the way out of here."
"Well, if you won't show us, I guess you'll
just have to stay here," says Quentin with a
nasty smile. Pulling the necklace out of his
pocket with a quick motion, he places it around the messenger's neck and forces the
broken ends together.
"There! I can't think of anyone who de- serves it more, except perhaps my beloved uncles.''')
    input("Press enter to go to the next page")
    page18C()
def page18C() :
    print('''\nEnjoy your stay here. I hope you like
mushrooms.
"
The messenger stands dazed for a moment
and then, before your eyes, begins to change
shape. Soon, thickened and mushroomlike, he
wanders aimlessly off into the dark.
"Wonderful. Now what do we do?" asks
Fox.
1) "I know," you say. "Quentin, do you
have aiiy more of those homing bats?
We could tie a string on its leg and fol- low it." Turn to page 106.
2) "Or maybe I could find a way out by
sniffing," says Fox. "If Mouse Breath
would help, I think we could do it." Turn to page 144.''')
    #normally would take to either 106 or 144 but not in game yet so start at beginning
    input("You have reached a part of the game that is not accessible yet, press enter to go to the beginning...")
    page1C()
def page19() :
    print('''\n"Look, are we going to let a little noise scare us away?" you ask angrily.
"Sounds good to me. I want to get out of
here," says Fox, starting down the stairs.
"I agree with Jaimie," says Owl. "I should
like to check out this curiosity. Let's find out
what produces such a great and steady volume of noise."
"Two against one, Fox," you say, and Owl
flies up, plucks the key from its hook, and
places it in your hand.
With trembling hands, you place the heavy
key in the lock, and the screaming stops.
"You'll excuse me if I stay down here," says
Fox, crouching on the second step with only
his nose, eyes, and ears visible.
You turn the key in the lock, ready for the
worst—a whirlwind of magic, a horrible
monster, a frightening vision.
The door opens and you see a pink blur of
motion and feel a sharp pain in your ankle.
You clutch the wounded ankle with both
hands and hop up and down with pain.
"What took you so long?" screams a harsh,
ugly voice. "Why didn't you come up here
right away and let me out? You, you, slug!"
"Ow! Ow! Stop kicking me! Who are you?
What are you doing here?"
"I'm a princess, dummy! Princess Imogene!"
screams the little girl. "It certainly took you
long enough to rescue me!" And she kicks you
again, this time in the other leg.''')
    input("Press enter to go to the next page")
    page21()
def page21() :
    print('''\n"Ow! Stop that! How could I rescue you sooner? I didn't even know you were here and
needed rescuing. How did you get here?"
"I don't know," wails the little girl. "My
uncle brought me here. He said there was
something he wanted me to see, a surprise. He
sent me up the stairs and I came in the room,
and the door slammed shut behind me. And . .
.
and I've been here ever since," Imogene says,
bursting into tears.
As she cries, you peer into the room. You see a small bed, a nightstand, and the broken
bodies of hundreds of dolls and toys.
"Don't cry," you say, patting Imogene on
the head. "We're here now. We'll get you out."
"Don't touch me!" screams Imogene. "How
dare you, a commoner, touch a princess without permission!"
"Look, Imogene," you say, "I'm sorry if I don't come up to your royal standards. But
just remember—I AM rescuing you. If that's
not good enough, go back in your room and
wait for a royal prince to come."
"I vote for that," growls Fox. "Put her back
in her room, the graveyard of the dolls. If we
let her out, she'll probably break us into little bits too."
"What is that mangy dog doing in my castle?" screams Imogene. "Get rid of it immediately. It clashes with my dress."
You notice for the first time that Imogene is dressed entirely in pink. Long curls flow over her shoulders and freckles are sprinkled over her frowning face.''')
    input("Press enter to go to the next page")
    page22C()
def page22C() :
    print('''\n"Mangy dog?" snarls Fox with menace.
"Now, now, Fox. Control yourself," says
Owl from his place on your shoulder. "Just
consider this child as ill-tempered and simple,
not worldly and well-mannered like yourself."
"Well, since you put it that way," says Fox,
sinking back on his haunches. "But we should
vote and decide what to do with her."
"You? A commoner and two dirty animals
decide what to do with me?" screams Imogene, with her hands on her hips.
"We three are a democracy, Imogene. We
make all important decisions by voting, and
the majority rules. Fox and Owl may only be
animals to you, but they are my best friends
and I value their opinions."
"Hmmph!" sniffs Imogene.
"Well, let's put it to a vote," you say. As you
speak, Fox leaves the safety of the steps and
sits at your feet.
1) "Should we take her along with us?"
Turn to page 53.
2) "Or should we leave her here and go on
by ourselves?" "If you do that you'll be
very sorry," screeches Imogene. If this
is your choice, turn to page 89.	''')
    # would normally take them to either 53 or 89 but isnt coded in the game yet, start at beginning
    input("You have reached a part of the game that is not accessible at this time, press enter to go to the beginning")
    page1C()
def page23E() :
    print('''\nYou go on but fear that you have made the
wrong decision. Just as you are about to suggest turning around and going back, you see a glimmer of light ahead of you.
"Look up ahead. It's a light! Hurry!" you
cry, urging your friends forward.
The light dances and floats in front of you.
You run toward the glow, pulling Nesbitt behind you. He shouts vague words, but you do
not stop to listen.
The light moves into another tunnel, and
you follow without a second thought. "Hurry!
We'll be out soon!" you yell. The light turns
again and still you follow.
Somehow, no matter how fast you run, you
never catch up to the moving light. It turns
many corners and changes its direction often.
But it is always just out of reach.
At last you can follow no longer. You sink to
the floor in despair. The light stops and bobs
up and down gently . . . waiting.
"It's no use. It's a Will-o'-the-Wisp," gasps
Nesbitt. "It has no intelligence. It leads no- where. We are lost forever."
"No! We're not lost! Use your stones!"
"I cannot. I dropped them. I tried to tell you,
but you did not listen."
A silence sinks over your party as each of
you realizes that you are truly lost. And in the
distance, the Will-o'-the-Wisp bobs up and
down . . . and waits.
THE END	''')
    input("You have reached the end of the game, press enter to go back to the beginning and choose a different path...")
    page1C()
def page24() :
    print('''\n"No, it couldn't be. It's got to be just a plain
old ring," you say, looking at it. Suddenly your eyes open wide. What you
saw before as bright metal is now dull and
gray—nothing more than a circle of poorly
forged iron. It turns to grainy powder and
crumbles to dust even as you watch.
"Besides, if it had been a wish ring, the
fourth wish would have canceled out everything I wished before. And I sure don't want
these guys oh us again," you say with a
shudder.
Settling on your shoulder, Owl says, "I see an exit at the end of this room."
Kicking away the last ofyour tiny pursuers,
the three of you slip through the door and
close it behind you.
"Wow! We're safe," you say breathlessly.
"Oh, yeah? What makes you say that, kid?
We're still lost. We're still in the dark. Why
can't we ever get lost in daylight?"
"Some of us are more in the dark than others," murmurs Owl.
"I know just what you mean, Fox," you say
quickly. "But here, I guess I can fix it for a
while." Holding out your hand, you utter magical words that have never been more than
boring homework before. A glowing ball appears in front of you, casting light ten feet in
all directions.
"When did you learn that? And why didn't
you use it before this?" sputters Fox.
"I was saving this until we really needed it.''')
    input("Press enter to go to the next page")
    page25()
def page25() :
    print('''\nAnd we need to get back to Pentegarn. The
light will help."
Avoiding further quarrel, you walk down
the corridor revealed by the light.
Faded tapestries and formal portraits line
the stone walls. Underfoot, a fine carpet lies
buried by thick dust.
You open every door you pass, but each re- veals only an empty, lifeless room. The glowing ball sputters and fizzes, glows
its last, and disappears. In its dying light you
reach the last door in the corridor. With shaking hand, you grasp the doorknob and push.
The door creaks open and bright sunlight
streams into the dark corridor. With your
hand over your dazzled eyes, you enter the
most splendid room you have ever seen. Bright, warm light streams in through three
rounded tower windows. On the floor is a thick
carpet patterned in flowers of vivid red, blue,
gold, and green that wriggle aside as you
pass. On the walls hang richly colored and
intricate tapestries.
More books than you have ever seen before
spill out of bookcases, cascade off chairs and
tables, and overflow onto the floor.
The door closes quietly behind you. Out
from behind a chair come two large
comfortable-looking slippers. Flip, flop, flip,
flop go the slippers as they pad up to you and
arrange themselves on either side ofyour feet. When you do not move, they jump up and
down with a demanding thump.'''
)
    input("Press enter to go to the next page")
    page26()
def page26() :
    print('''\nWith a sidelong look at Fox and Owl, you
step out of your own boots and into the big
slippers, which promptly stride across the
room, taking you with them.
"Be careful!" barks Fox. "Those things
could be a trap."
But the slippers walk to a large overstuffed
chair, turn themselves around, and back you
into the seat, settling you deep in its soft, sagging depths.
As you sit there, your legs dangling over the
edge, a large curved wooden pipe on the table
next to you stands up. A round wooden canister opens itselfup, releasing a sweet smell into
the air. A chunk of tobacco floats through the
air and packs itself into the bowl of the pipe.
Instantly, a roaring fire bursts into life across the room. A spark leaps from it, flies to the
pipe, and settles into the tobacco. Great puffs
of smoke soon billow out of the bowl as the
pipe lights itself. The smoking pipe floats through the air and
places itself firmly between your lips. You inhale in surprise, and thick, harsh smoke pours
down your throat. "Get me something to
drink," you gasp, coughing.
Even before you have finished speaking, a
long-stemmed glass thrusts itself into your
hand. Not questioning where the glass came
from or what it contains, you raise it to your
lips and swallow deeply.
Hot, raging, burning fire courses down your
throat and settles like a pool of lava in your stomach.''')
    input("Press enter to go to the next page")
    page27()
def page27() :
    print('''\nTears pour down your cheeks and
you are sure you'll never breathe again. Then
a soothing pressure pats you firmly on the
back and rubs gently between your shoulder
blades.
At last your harsh coughing dies, and you
are not even startled when a soft, knitted
afghan lifts itself from a nearby hook and
wraps itself comfortingly around you.
"What is this stuff?" says Fox, lapping at
the amber liquid in the glass.
"I will determine its chemical elements,"
says Owl, dipping his beak into the glass.
"Hmmmmmm, unusual flavor," adds Fox.
"I think I'd better try that again. It might be
poison." Dipping his muzzle into the glass
again, he slurps up more of the fluid.
"I am better at distinguishing among the
many complex chemical compounds than you
are. Make way for the expert," says Owl,
drinking deeply.
As you snuggle in the depths of the large
chair, trying to sort out confused thoughts,
Fox turns to Owl and says, "Old Buddy, did I ever tell you that even though you can be a
real pain, you're not so bad for a bird?"
"And I have frequently thought that, hie,
for a member ofthe genus Canis, you are rather exceptional yourself. Hie."
"Say, do you know that old song that the
Wood Elves, hie, Wood Elves sing?"
"Hummmm a few bars, friend Fox," says
Owl, blearily.''')
    input("\nPress enter to go to the next page")
    page29()
def page29() :
    print('''\nBy the tree and by the root
We really love to drink this fruit. Sharing's nice, it's really fine!
But give me more, or I'll take thine.
"Fine tenor voice, Fox. I myself sing baritone," says Owl, sagging comfortably against
a pile of books. And the two ofthem raise their
voices in silly song.
As the pain in your throat and chest eases,
you sit up straighter in the chair just in time to
grab a very large book that settles itself in
your lap and opens to a well-used page. Gold
letters heaped in one corner march themselves quickly across the page and arrange
themselves into lines of words.
As you try to understand the words, your
friends' voices turn quarrelsome.
"That was my chorus, you Buzzard, you! You should stick to hooting."
"Howling at the moon is more your tune,"
snipes Owl.
"That does it! That's the final straw. I'll show you who's going to howl," shrieks Fox
as he leaps upon Owl.
Fur and feathers fly in a frantic flurry of
beak and tooth, claw and talon. Then Fox
snaps at Owl, catches him by the back of the
neck, and drags him across the room. Stopping in front of an enormous open
book, Fox drags a struggling, flapping Owl up
into the book, wedges him into it, and slams
the cover shut.''')
    input("\nPress enter to go to the next page")
    page30C()
def page30C() :
    print('''\n"There! I told you I'd do this. Now! While
you're in there, learn some simple words or I'll never, ever let you out!"
"Mfle! Pring!" squeaks Owl from between
the pages of the dictionary.
Fox sits on top of the heavy book with a
satisfied smirk on his face, wraps his tail
around his legs, and settles down for a long,
satisfying wait.
You start to rise, but the strange words that
have formed on your page demand your attention. And you realize that Fox and Owl must
settle their own differences if there is ever to
be peace.
Before you on the large page are three
blocks of words. One reads: "How to Rescue a
Friend." The second reads: "How to Be Wise."
The third reads: "How to Be Powerful."
Each has a magical formula written beneath it that you know you could figure out
with a little effort.
1) If you want to read the spell that says
"Rescue a Friend," turn to page 100.
2) If you want to read the spell that says
"Be Wise," turn to page 135.
3) If you want to read the spell that says
"Be Powerful," turn to page 121.''')
    #normally take them to one of the three choices but not in code yet, back to start
    input("You have reached a part of the game that s not accessible, press enter to start from the beginning and make different choices")
    page1C()
    
def page32E() :
    print('''\n"He'll never wake up in time. If we're to be
saved, I'd better try to use the cube myself,"
you say nervously.
"No! Jaimie! You haven't enough experience to use it yet," squawks Owl.
"Pentegarn won't wake up. I have to try,"
you say, raising the cube to your forehead the
way you have seen Pentegarn do.
A mighty surge of power zaps into your
head and flows down through your body. You
are rigid with shock. Your thoughts whirl
through your mind like birds in a storm, but
they are the only things that move. You are unable to move even your little finger. Through frozen eyes you see the wizards
untangle themselves from their robes and
move toward you.
Malus plucks the cube from your nerveless
fingers. "A fine addition to our collection of
magical goodies, wouldn't you say, Pothos?
Good thing the brat decided to use it or it would have been all over for us. "Now I suppose we had best herd the zoo and Pentegarn—and Imogene, mustn't forget
Imogene—and lock them up in the dungeon.
This one," he adds, tapping your rigid arm,
"will do for a statue in the fountain.
"Yes, I'd say everything worked out for the
best ... for us."
THE END	'''
)
    input("You have reached the end of the game, press enter to go back to the beginning and make different choices...")
    page1C()
def page33() :
    print('''\n"What happened? Where are we?" wails
Fox, opening his eyes.
"We are in a narrow corridor dripping with
slime and foul fluids. It appears to be the home
of numerous tasty rats," answers Owl. "Wait!
Here's a sign tacked on the wall. It says, Welcome to the Game Room.'"
You peer into the blackness surrounding
you and groan. "Some game room! This is a
dungeon! Those wizards tricked us. So they
must be planning to trick Pentegarn. We've
got to get out of here fast and get back to help
him!"
"Easier said than done," says Owl.
"Ahwooo!" wails Fox, and the noise echoes
through the darkness.
"Be quiet, Fox!" you yell, grabbing him and
holding his muzzle shut. "None ofus wants to
be here, but until we figure out exactly where
we are, we can't figure how to get out. And
don't forget, there are usually all sorts of dangerous monsters and other creepy things
wandering around in these old dungeons. So
be quiet unless you want to be dinner for one of
them," you add sternly.
"Right now the most important thing to do
is to figure out how we're going to get out of
here. Do you pick up any clues with your special senses?" you ask the animals.
"As a matter of fact, I have spied a most
peculiar rainbow-colored cord that appears to
be attached to the wall and gives off a faint
glow," says Owl. "It stretches off to our left."'''
)
    input("\nPress enter to go to the next page")
    page34C()
def page34C() :
    print('''\nCautiously you let go of Fox's muzzle, hoping that he will not start howling again. But
he only lifts his nose into the air and sniffs.
"To our right I smell a strange, fungusy,
foresty, earthy smell," says Fox. "And I hear
something moving."
"Very good," you say. "Two clues. Well,
which way should we go?"
1) If you want to follow the glowing rainbow cord, turn to page 43.
2) If you want to find out what is moving
about and smelling earthy, turn to
page 68.''')
    input("You have reached a part of the game where some of the story is in accessible, press enter to go to page 43 and continue your journey...")
    page43C()
def page35C() :
    print('''\n"They scare me, Owl. Let's get out of here
while we still have a chance."
With one last look at Fox, you start running,
darting and weaving between the slow-moving
figures. Arrows whiz by you. Amace narrowly
misses your head, and once, Owl is creased by
a spear. But at last you are clear of the grasping reach of the iron men.
On you run until you fear your lungs will
burst. Gasping for breath, you hold your aching chest and collapse on the dusty floor.
"Owl, where do we go from here?"
"I don't know, young Jaimie. I fear that no
matter where we go, it will no longer matter.
We have lost our friend Fox. We have failed in our mission, and even worse, we have left the
battlefield without our honor."
Somehow—you are never able to remember
how—you find your way out of Rainbow Castle. Looking up at its great towers shrouded
with mist, you realize that two of those you
love best, Pentegarn and Fox, remain within
its walls.
"I wish I had it to do over again, Owl. I sure would do it differently."
If you would like to make a
different choice and try again,
go back to page 82.	'''
)
    input("You have reached a part of the game that is not accessible, press enter to start at the beginning...")
    page1C()
def page36C() :
    print('''\nRaising your hand, you pound on the heavy
door as hard as you can. The sound echoes in
the distance, but no one comes. The shrill
whining continues. Once again you pound on
the door, but still no one answers. However,
the noise changes tone.
"Well, now what do we do?" you ask.
Turn back to page 48
and make another choice.''')
    input("Press enter to return to page 48 and make a different choice...")
    page48C()
def page37() :
    print('''\n"Nothing good lives in dungeons on purpose," you say. "Let's try to fight our way
through them and head for that tunnel."
"Yeah! We'll show them," says Fox.
"I hope you are correct," says Owl, looking
doubtful.
Drawing your dagger, you move swiftly to- ward the swaying shadows. As you near
them, the smell grows stronger. It is strangely
familiar, sort of like mushrooms.
Without pausing, you give a loud war cry
and plunge your weapon into the first creature
you meet—or try to. Your wrist is gripped and
twisted, and your dagger falls to the floor.
You strike out with your other fist, and it, too, is grasped and held firmly. Then you are
lifted off the ground and shaken hard. You
hear barks of panic from Fox and one squawk
from Owl—then all is silent.
"Have you caught them all?" asks an
almost-human voice.
"Yes," answers a mealy, muffled voice.
"Good," says the human voice. "They cer- tainly are an odd bunch, but it doesn't matter.
As soon as they grow their gills and alter their
shapes, they'll be just like the rest of you and
won't cause any problems.
"Take them and give them their first dose of
mushrooms."
Soft, spongy hands pull you forward. The
smell of mushrooms is overpowering. You
struggle but are held firm. Soon you find yourself being pushed into the mouth of the tunnel you saw earlier.'''
)
    input("\nPress enter to go to the next page")
    page39()
def page39() :
    print('''\nFox and Owl and more lumpy
creatures crowd in behind you.
Rich warm smells of cooking hang heavy on
the air, and you realize how hungry you are. "What are these things?" hisses Fox.
"I don't know," you answer. "Just be careful
not to eat any of those mushrooms."
"I never drink or eat anything given to me
by strangers," says Owl.
As you watch, one of the stumpy figures
takes a stick and stirs the embers in a stone
hearth. Bending, it scoops up an armload of
coal and adds it to the glowing embers. Soon
the room is lit by a bright fire. Hanging over
the fire is a large iron pot that simmers and
bubbles, sending good smells into the air. But you can't take your eyes off the stumpy
creatures revealed in the firelight. Although
they are human in shape, their skin is rough
and brown and lumpy. On what should be
their necks are narrow openings that look like
fish gills. Their heads are crude, shapeless
lumps. Looking closely, you make out the
suggestion of eyes, nose, and mouth on some
of the creatures. But others have none at all. To your terrified eyes, the creatures look like
nothing more than enormous walking
mushrooms!
As you stare in terror, one of the creatures
dips a bowl into the cooking pot, fills it, and
walks toward you.
"Eat!" it commands, placing two more
steaming bowls in front of Fox and Owl.''')
    input("\nPress enter to go to the next page")
    page40E()
def page40E() :
    print('''\n"You can't make us!" Fox barks bravely.
Chuckling, the creature says, "That is not
necessary. You will be hungry soon and will
eat. Then you will be just like us."
Turning, the mushroom people shuffle
through the door. The last one through touches
a lever and a grate of metal bars drops to the
ground.
You rush to the grate and shake it, but it does not move. Slowly you return to Fox and
Owl and look down at the stew. Good smells
drift upward and your stomach rumbles its
message of hunger.
"What do you think?" asks Fox. "Should we
eat? Food can't really hurt us, can it?"
"I don't know, Fox. I just don't know."
Shaking your head, you wonder if your
hunger will force you to eat, or if you will be
able to hold out long enough to talk to the
mushroom people and convince them to let you go.
THE END	''')
    input("You have reached the end of the game, press enter to return to the beginning and make different choices...")
    page1C()
def page41C() :
    print('''\n"There's nothing wrong with being obvious,"
says Fox. "Let's try the door."
Hurriedly, you seize the doorknob and pull.
Instantly a loud, crazed barking bursts forth,
and a large brown dog with three horrible
heads hurls itself at the opening.
Quickly, you slam the door shut and shiver
with fear as it shakes beneath the frenzied
attack of the dog.
"The rug! It's dropping!" shrieks Fox.
Snapping your attention back to the drooping, spider-filled carpet, you pin it to the ceil- ing once more. "Fox," you whisper, "look out the window
and see if we can climb down from here. Owl,
check out the fireplace. See if there's any way
to get out through there."
"We're up real high, Jaimie. I don't know if
we could get down or not. But there's some
kind of ivy growing all over the walls."
"There appears to be a hidden staircase on
one side of this fireplace, which I can see with
my superior eyesight," says Owl.
1) If you want to try to climb down the
tower, turn to page 12.
2) If you want to try the hidden staircase,
turn to page 105.
3) If you want to try to fight the dog, turn
to page 8.''')
    page41C = input("Which page would you like to go to?: ")
    if "12" in page41C:
        page12C
    elif "8" in page41C:
        page8()
    elif "105" in page41C:
        input("You have reached a part of the game that is not accessible, press enter to return to the start")
        page1C()
    else:
        input("That is not recognized, press enter to return to page 41 and try again")
        page41C()
def page42E() :
    print('''\n"Looks fine to me. Im hungry. Let's eat. What could possibly happen?" growls Fox as he leaps to the top of the table. He sticks his
muzzle into a large chocolate cake and begins
to eat hungrily.
"Well, young one, one for all and all for
one," says Owl, picking up a piece of candy
and swallowing it whole.
"All right. I guess so, and anyhow it's too
late now," you say as you pick up a glass of
some pale pink liquid and take a long drink.
"See? That wasn't sooo " says Fox as he
fades and disappears from sight.
"Fox! Fox! Where aaaaare . . ." cries Owl in
alarm as he, too, disappears.
"Fox! Owl! Come back!" you cry. And then
you feel soft, smooth, soothing warmth, and
then nothing at all. In the empty room, in the partially empty
castle, a half-eaten chocolate cake becomes
whole, a piece of candy arranges itself on a
plate, and a half-empty glass refills itself. Then all is still, except for the thin, shrill noise
that continues unheard.
THE END	''')
    input("You have reached the end of the game, press enter to return to the start and make different choices...")
    page1C()
def page43C() :
    print('''\nThe cord is velvety smooth to the touch.
Although it glows with a soft, warm shimmery
rainbow of colors, it sheds little real light. The
darkness presses in on all sides.
"Where do you think it goes?" asks Fox.
"Let's go find out," you answer. Holding the shining cord in one hand and
your dagger in the other, you advance slowly.
"Do you see anything yet?" whispers Fox.
"I'm not sure. I think there's some sort of
pinkish light up ahead," you answer.
"Correct," says Owl.
Cautiously you approach the light. Soon
you make out a doorway filled with a dull pink
glowing fog that seems almost solid. You
cannot see through it. Oddly, the cord does not
go through the door but continues down the
dark corridor.
"What do we do now?" you ask.
1) "I hate this darkness. Let's go through
the door," says Fox, dashing in. If you
choose to follow, drop the cord and turn
to page 69.
2) "I think we should follow the cord,"
says Owl. If this is your choice, turn to
page 72.''')
    input("You have reached a part of the game that is not accessible, press enter to return to the beginning of the game")
    page1C()
def page44() :
    print('''\nSettling down in the dense cloud cover, you
stare at the caves. All you can tell is that they
are very large. A peculiar multicolored glow
shimmers through the opening, but you do not
know where it comes from or what could be
making it. "Why are we sitting here?" growls Fox.
"Let's go down there and check it out!"
"No, let's wait. I'd like to see what lives in
there before we have to face it." Fox grumbles but does not argue.
You do not have long to wait. Around a
thundercloud mountain come three of the
most unusual dragons you have ever seen. Each is covered with scales that shimmer and
glow and change colors before your astonished eyes.
The largest dragon is in the lead, holding a
chunk of bright-blue substance in its jaws.
Behind it, a slightly smaller dragon carries a
mouthful of crimson red. Last of all is a small,
delicate dragon who carries a little bundle of
golden yellow.
With grace unusual for animals so large, the
immense creatures flow smoothly through the
air. The sun bathes them in light, sparkling
on the multicolored scales and filtering
through gauzy, transparent wings. With a
gentle swirl, they bank and turn, enter the
cave, and disappear into its depths.
"Wow! Will you look at that!" whistles Fox.
"Truly astonishing," murmurs Owl.
"I wouldn't have believed it if I hadn't seen it," you say.'''
)
    input("\nPress enter to go to the next page")
    page46C()
def page46C() :
    print('''\n"Well, what should we do? They
look pretty nice to me. Not at all like dragons
I've read about. They're so beautiful, maybe
they're friendly. We could try to talk to them."
"Have you lost your grip? Are you nuts?"
says Fox. "A dragon's a dragon! The only
thing dragons understand is violence. Kill
them, yes! Talk to them, no!"
"I myself attempt to avoid danger whenever
possible. I suggest that we avoid this confrontation completely," says Owl.
1) If you want to try to talk to the dragons,
turn to page 150.
2) If you want to fight the dragons, turn to
page 65.
3) If you want to go to the cloud castle, go
on to the next page.''')
    page46C = input("Would you like to go to page 150, 65, or the next page, which is 47?: ")
    if "105" in page46C:
        input("You have reached a part aof the game that is not accessible yet, press enter to return to the beginning of the game and start over...")
        page1C
    elif "65" in page46C:
        input("You have reached a part aof the game that is not accessible yet, press enter to return to the beginning of the game and start over...")
        page1C()
    elif "47" or "next" in page46C:
        page47
    else:
        input("That is not recognized, press enter to retry this page")
        page46C()
def page47() :
    print('''\n"If there's a castle, there must be people who
live in it and can help us. That's why I vote for
the castle."
"I'm with you," says Fox, leaping to his feet
and sinking to his belly in cloud.
"I second your decision," says Owl.
Although you can see little or nothing
through the foggy mist, you move in the direction that Owl points out. With each step, you
sink kneedeep in the clouds. The soft stuff
wraps around your legs and tugs at your ankles. Soon your muscles ache and burn with
the effort of moving.
Fox pants heavily as he struggles alongside
you. "Have to stop for a minute," gasps Fox as he collapses.
"My keen sight tells me that the castle lies
just beyond the next cloud field and up a slight
hill. It's really not far. I think we should push
on," urges Owl.
"That's easy for you to say, Beady Eyes.
You're flying. Try walking. It's like trying to
swim through glue. I don't think I can make
it." Fox groans.
"Faint heart ne'er won . . . AAWWK!" Owl
shrieks suddenly as Fox leaps up in the air
and snaps at his tail. Owl flaps swiftly upward, narrowly avoiding the sharp, shiny
teeth. With Fox in pursuit on the cloud below,
he flies off toward the castle.
"I'll get you if it's the last thing I ever do,"
yelps Fox. "Then we'll see who's got a faint
heart!"''')
    input("\nPress enter to go to the next page")
    page48C()
def page48C() :
    print('''\nSmiling, you heave yourselfto your feet and
struggle after the barking Fox.
At last you break out ofthe clinging cloud. A
clean breeze blows softly about you. In front of
you is a low hill. Perched on top is a small
castle built of pink cloud puffs. Tiny slits of
windows spiral up the sides of its towers.
Heavy wooden doors are set into the castle
wall.
Calling on your last reserve of strength, you
climb to the top of the hill and collapse at the
castle door.
"What took you so long?" asks Fox smugly.
"We've been waiting for you for ages."
"Oh, I just thought I'd take my time and
look at the scenery," you say, fighting down
the impulse to strangle him.
As you stand before the massive doors, you
hear a distant whining noise that sends chills
down your back. "Well," you say, "somebody
must be in there. But how do we get in?"
"I'd say we have three choices," says Owl.
1) "Knock on the door." Turn to page 36.
2) "Try to open it ourselves." Turn to page 132.
3) "Or find another way in." Turn to page 140.''')
    page48C = input("Would you like to go to page 36, 132, or 140")
    if "36" in page48C:
        page36C()
    elif "132" in page48C:
        input("You have reached a part of the game that is not accessible yet, press enter to go to the beginning and start over")
        page1C()
    elif "140" in page48C:
        input("You have reached a part of the game that is not accessible yet, press enter to go to the beginning and start over")
        page1C()
    else:
        input("That is not recognized, press enter to retry")
        page48C()
def page49() :
    print('''\n"Listen, we're not going to let a little noise
scare us, are we?" you ask.
"I don't know about you, kid, but I'm con- vinced we shouldn't go in there. That noise is
REAL convincing! I want nothing to do with
something that sounds that scary."
"Jaimie is right, Fox. Don't exhibit your
cowardice," chirps Owl. "These sounds are merely ululations of vocal phonics, acting on
your auditory sense in such a manner as to
produce fear."
"OK, Owl, I admit it," screams Fox. "I AM
scared. But that doesn't mean I'm dumb. And
just because you can talk big words doesn't
make you smarter or braver than me."
Still full of rage, Fox turns and stomps
down the stairs. "You want action? You got it. Look out, noise, here I come!"
"Owl, I think you went too far," you say as you hurry to catch up with Fox. "You shouldn't
tease him so much. Underneath all that wisecracking, Fox is very sensitive, and he IS your
friend."
"I was only pointing out his shortcomings
so that he might endeavor to improve himself.
However, I will try to be kinder in the future,"
agrees Owl.
"If there is a future," you mutter.
"OOOOOOOOOO!" wails the noise from
around the very next turn in the stairs.
"Come on, you chickens," says Fox as he
takes a deep breath and turns the corner. There is a sudden yelp and then silence.''')
    
    input("\nPress enter to go to the next page")
    page51E()
def page51E() :
    print('''\nBefore your startled eyes, a misty white foxshaped figure floats through the air and up
the stairs toward you.
"Fox, a ghostly appearance is not appropriate at this time," Owl says sternly. "Whatever is making that noise could seize the opportunity to get us."
"Won't happen, Fuzzface. I've already been
gotten. Thanks to you. But why don't we let
bygones be bygones?" And so saying, Fox
drapes a paw around Owl's neck.
PLINK! Owl seems to melt away beneath
Fox's touch until his feathers fade to fog.
"Fox! Owl! Is this a joke? Don't do this to me. Come back!" you cry.
"OOOOOOOOO!" wail Owl and Fox to- gether, as they drift close to you.
"Not bad, huh, kid? Maybe we could form a
group. We could call it the Spiritones."
"What do you mean? Fox? Owl? What's
happened to you? You're not ghosts, are you?"
Fearfully you touch your friends.
PLINK! Your hand goes soft and strange.
You hold it up and realize that you can see through it. The strange coolness spreads up
your arm and soon engulfs your entire body.
"0000000!" you cry in fear.
"Don't worry, kid. We'll only haunt the best
places," says Fox, and the three ofyou drift off
down the stairs.
THE END	''')

page1C()
veryEnd = input("You have reached the very end of the game, there is definitely nothing else beyond this point")
if "dragon" in veryEnd:
    print('''WWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
WWWWWWWWWNWWNNWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
WWWWWWWWNNWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNN
WWWWWWWWWWWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNNNNNNNNN
WWWWWWWWWWWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMWWMMMMMWXNNNNXNNNNNNN
WWWWWWWWWWWWNWMMMMMMWNXKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNXXXNWMMMWXNNNNXNNNNNNN
WWWWWWWWWWWWNWMMMMMMMWNX0OKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKXXWWMMMMMWXNNNNXNNNNNNN
WWWWWWWWWWWWNWMMMMMMMMMMWKkk0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOO0XNWMMMMMMMMWXNNNNNNNNNNNN
WWWWWWWNWWNWNWMMMMMMMMMMWWXOdx0NWWWMMMMMMMMMMMMMMMMMMMMMMWWMMMWWMNK0OkxxOXWMMMMMMMMMMMWXNNNNNNNNNNNN
WWWWWWWNWWNWNWMMMMMMMMMMWWWNkodxOKNMMMMMMMMMMMMMMMMMMMMMMWWMWMWXOdlodxxOXWMMMMMMMMMMMMWXNNNNNNNNNNNN
WWWWWWWNWWNWNWMMMMMMMMMMWWWW0ollllo0WWWMMMMMMMMMMMMMMMMMMWWMNOxolodxdokXWWWMMMMMMMMMMMWXNNNNNNNNNNNN
WWWWWWWNWWNWNWMMMMMMMMMMMMWWKoccloc:oKNNWMMMMWWWMWWNNWWMN0Kkllllolcllok0KXXNWMMMMMMMMMWXNNNNNNNNNNNN
NNNNNNNNWWNWNWMMMMMMMWWWNNXKx:,;;,,'.;lONNWWN0O0OkxxOKNWNk:;::clooxkOOxddxkO0KXWMMMMMMNXXNNNNNNNNNNN
NNNNNNNNWWNWNWMMMMMWWNXK0Oxol:;,'..,c,.xX0XXkl:;;;;;;cdKNo.';:ldO0KXK0O0KXXNWNNWMMMMMMNXXNNNNNNNNXXX
NNNNNNNNWWNWNWMMMMMMMMMMMWNKOkoc;;lkOc,k0k0Okl.'llc;',l0Nk;loclk00000KNNWWWWMMMMMMMMMMNXXNNNNNNNXXXX
NNNNNNNWWWNWNWMMMMMMMMMMMWWN0dlodxk0O:lXOlcloc:kXxc,.,:kN0co0Odok00KKNWWWMMMMMMMMMMMMMWXXNNNNNNNXXXX
WWWWWWWWWWNWNWMMMMMMMMMMMMWWKxxxk0O0xckXdcccldKWNd:'';:oKXl:kOOxoxKXXWMMMMMMMMMMMMMMMMWXXNNNNNXXXXXX
NNNNNNNNWWNWNWMMMMMMMMMMMMMWKkkKX0Ox:dWNXXXNWWXOl'..,:ONWNxcllxO0OxxKNWMMMMMMMMMMMMMMMNXXNNNNNXXXXXX
NNNNNNNNWWNWNWMMMMMMMMMMMMWKxOXXKOkx:oWWWWWWNKl'...,oxOWMWo,cloxO000O0XWMMMMMMMMMMMMMMNXXNNNNXXXXXXX
NNNNNNNNNWNWNWMMMMMMMMMMMNOk0NNX0kdd::0WWWW0dc'.';:lOXXWWX:.:cldxkKNXK0KXWWWMMMMMMMMMMNXXNNXXXXXXXXX
NNNNNNNNNNNNNWMMMMMMMMMWXKKNWWNX0xll;'coddOd'..';llo0NWWKd'.::clx0XWWWWNNNNWWWMMMMMMMMNXXNNXXXXXXXXX
NNNNNNNNNNNNNWMMMMMMMMMWWWMMWWWWNKoc:,'..;oc..,;cllodkOxl;.,::lkXWWMWMWWWMMMMMMWMMMMMMNXXNNXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWN0occc;,lo'..,,,::;;;;,,,.,:o0NMMMMMMMMMMMMMMMWMMMMWMNXXNXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMWWWMWKklcdOxl:.'lx:.'',;:xNWWMWWMMMMMMMMMMMMMMWWWMWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMWXK00NWXKKOxol;....'ckXNWWWMMMMMMMMMMMMWWWWWWMWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWW0xo:....,cccxOKNWWWMWWMWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0:.':,...,:,..,;oKWMWWMMWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKx;. ':'...;,....';dXWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWKOd,.;;...:o,..';l::OWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMWWWWWWWWNXKKOkkkO0kc:ccc:,;ckXxcOWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWWWKOkkOOOxdxOkOK0Okxdol:,...:xxlxNWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWKxdxkO00OkO00OOxolododc'...',:cxXWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMNd:oxdddolloolox0kooodO0kxxxxk0XWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMNOooxOko'.',,'ckK0kdloxdoxOKNWWWWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWWWWNOdc,;dd:;xNKl;;;cc;,:,,lkXNXK0XWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMWWWWWNx:lO0kl:lO0;..,d0Ol.....;0KOO0XXNWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMWWWWNl.;xOOkOKWk'.,;dXNo. ...cOKXNNNNWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMMMMWWO,.dNWWWWWNk:,;ldo' ...,l0NWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMMMMMWWO:;dXWWWWWNK0kd:...';cdKNWWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMWWMWWWWWXd:cdO0Okollcclodk0KKNWNNWWWWWWNNWWWWNNNNNNWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMWWWWWWWWWWWWWWWWWWWWWWXOxddxxkO0KNWWWWWWWWWNNWWNNNNNNNNNNNNNNNNWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWNXXXXXXXXXXXXX
NNNNNNNNNNNNXNMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWWNWNXXXXXXXXXXXXX
NNNNNNNXNNNNXNWMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXXXXXXXXXXXXXX
NNNNNNNNNNNNXNNWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXX
NNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
NNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
else:
    retryOrNot = input("Do you want to retry?: ")
    if "y" in retryOrNot or "Y" in retryOrNot:
        page1C()
    else:
        print("Please close the game out.")
### Brady Nokes code end
















































































# End ascii art for credit
##print('''WWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
##WWWWWWWWWNWWNNWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
##WWWWWWWWNNWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNN
##WWWWWWWWWWWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNNNNNNNNN
##WWWWWWWWWWWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMWWMMMMMWXNNNNXNNNNNNN
##WWWWWWWWWWWWNWMMMMMMWNXKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNXXXNWMMMWXNNNNXNNNNNNN
##WWWWWWWWWWWWNWMMMMMMMWNX0OKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKXXWWMMMMMWXNNNNXNNNNNNN
##WWWWWWWWWWWWNWMMMMMMMMMMWKkk0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOO0XNWMMMMMMMMWXNNNNNNNNNNNN
##WWWWWWWNWWNWNWMMMMMMMMMMWWXOdx0NWWWMMMMMMMMMMMMMMMMMMMMMMWWMMMWWMNK0OkxxOXWMMMMMMMMMMMWXNNNNNNNNNNNN
##WWWWWWWNWWNWNWMMMMMMMMMMWWWNkodxOKNMMMMMMMMMMMMMMMMMMMMMMWWMWMWXOdlodxxOXWMMMMMMMMMMMMWXNNNNNNNNNNNN
##WWWWWWWNWWNWNWMMMMMMMMMMWWWW0ollllo0WWWMMMMMMMMMMMMMMMMMMWWMNOxolodxdokXWWWMMMMMMMMMMMWXNNNNNNNNNNNN
##WWWWWWWNWWNWNWMMMMMMMMMMMMWWKoccloc:oKNNWMMMMWWWMWWNNWWMN0Kkllllolcllok0KXXNWMMMMMMMMMWXNNNNNNNNNNNN
##NNNNNNNNWWNWNWMMMMMMMWWWNNXKx:,;;,,'.;lONNWWN0O0OkxxOKNWNk:;::clooxkOOxddxkO0KXWMMMMMMNXXNNNNNNNNNNN
##NNNNNNNNWWNWNWMMMMMWWNXK0Oxol:;,'..,c,.xX0XXkl:;;;;;;cdKNo.';:ldO0KXK0O0KXXNWNNWMMMMMMNXXNNNNNNNNXXX
##NNNNNNNNWWNWNWMMMMMMMMMMMWNKOkoc;;lkOc,k0k0Okl.'llc;',l0Nk;loclk00000KNNWWWWMMMMMMMMMMNXXNNNNNNNXXXX
##NNNNNNNWWWNWNWMMMMMMMMMMMWWN0dlodxk0O:lXOlcloc:kXxc,.,:kN0co0Odok00KKNWWWMMMMMMMMMMMMMWXXNNNNNNNXXXX
##WWWWWWWWWWNWNWMMMMMMMMMMMMWWKxxxk0O0xckXdcccldKWNd:'';:oKXl:kOOxoxKXXWMMMMMMMMMMMMMMMMWXXNNNNNXXXXXX
##NNNNNNNNWWNWNWMMMMMMMMMMMMMWKkkKX0Ox:dWNXXXNWWXOl'..,:ONWNxcllxO0OxxKNWMMMMMMMMMMMMMMMNXXNNNNNXXXXXX
##NNNNNNNNWWNWNWMMMMMMMMMMMMWKxOXXKOkx:oWWWWWWNKl'...,oxOWMWo,cloxO000O0XWMMMMMMMMMMMMMMNXXNNNNXXXXXXX
##NNNNNNNNNWNWNWMMMMMMMMMMMNOk0NNX0kdd::0WWWW0dc'.';:lOXXWWX:.:cldxkKNXK0KXWWWMMMMMMMMMMNXXNNXXXXXXXXX
##NNNNNNNNNNNNNWMMMMMMMMMWXKKNWWNX0xll;'coddOd'..';llo0NWWKd'.::clx0XWWWWNNNNWWWMMMMMMMMNXXNNXXXXXXXXX
##NNNNNNNNNNNNNWMMMMMMMMMWWWMMWWWWNKoc:,'..;oc..,;cllodkOxl;.,::lkXWWMWMWWWMMMMMMWMMMMMMNXXNNXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWN0occc;,lo'..,,,::;;;;,,,.,:o0NMMMMMMMMMMMMMMMWMMMMWMNXXNXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMWWWMWKklcdOxl:.'lx:.'',;:xNWWMWWMMMMMMMMMMMMMMWWWMWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMWXK00NWXKKOxol;....'ckXNWWWMMMMMMMMMMMMWWWWWWMWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWW0xo:....,cccxOKNWWWMWWMWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0:.':,...,:,..,;oKWMWWMMWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKx;. ':'...;,....';dXWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWKOd,.;;...:o,..';l::OWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMWWWWWWWWNXKKOkkkO0kc:ccc:,;ckXxcOWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWWWKOkkOOOxdxOkOK0Okxdol:,...:xxlxNWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWKxdxkO00OkO00OOxolododc'...',:cxXWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMNd:oxdddolloolox0kooodO0kxxxxk0XWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMNOooxOko'.',,'ckK0kdloxdoxOKNWWWWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMWWWWNOdc,;dd:;xNKl;;;cc;,:,,lkXNXK0XWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMWWWWWNx:lO0kl:lO0;..,d0Ol.....;0KOO0XXNWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMWWWWNl.;xOOkOKWk'.,;dXNo. ...cOKXNNNNWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMMMMWWO,.dNWWWWWNk:,;ldo' ...,l0NWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMMMMMMWWO:;dXWWWWWNK0kd:...';cdKNWWWWWWWWWWWWWWWWWWWWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMMMMMMMMMMMMMWWMWWWWWXd:cdO0Okollcclodk0KKNWNNWWWWWWNNWWWWNNNNNNWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMWWWWWWWWWWWWWWWWWWWWWWXOxddxxkO0KNWWWWWWWWWNNWWNNNNNNNNNNNNNNNNWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWNXXXXXXXXXXXXX
##NNNNNNNNNNNNXNMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWWNWNXXXXXXXXXXXXX
##NNNNNNNXNNNNXNWMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXXXXXXXXXXXXXX
##NNNNNNNNNNNNXNNWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXX
##NNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
##NNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
