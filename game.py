class Character(object):
    def __init__(self, name, species, famous_quote, advance, fail):
        self.name = name
        self.species = species
        self.famous_quote = famous_quote
        self.advance = advance
        self.fail = fail

cas = Character("Castiel", "Angel", "I'll interrogate the cat.","yay! XD", "gosh darnit.")
d = Character("Dean", "Human", "I mean, come on. We hunt monsters. Normal people, they see a monster and they run, but not us. We seach out things that want to kill us. You know who does that? CRAZY PEOPLE.", "HECK YEA HAHAHAHAHA!", "WHAT DO YOU MEAN! F**K, LIKE CMON!")
s = Character("Sam", "Human", "I lost my shoe!" , "Niceee." , "whelp, rip me.")
crow = Character("Crowley", "King of Hell", "I was an attractive child. I could juggle. I was worth five pigs at least.", "NOOOOOOOOOOO!!!!!!", "BAHAHAHAHAHAHA SUCKS FOR YOU!" )
lil = Character("Lilith", "Demon", "The first demon Lucifer has created.", "How is that even possible!!!!", "Have fun in hell suckerssss!")
luc = Character("Lucifer", "Angel", "Narcissistic personality disorder...Ok, this one I could have.", 'I hate you all.' , "Such a fool, you will never learn.")
# Creating character class

print("Welcome to Supernatural Trivia! You are going to answer questions in order to defeat your enemy. There will be 3 enemies, 3 stages and each one will get harder as you go. Now lets introduce our characters.")
# printing introduction to game

print(f"Here is {s.name}. He is a {s.species}. You have anything you would like to say {s.name}? {s.name}: {s.famous_quote}")
print(f"Next up is {d.name}. He is also a {d.species}. And here he is! {d.name}: {d.famous_quote}")
print(f"Lastly, the beloved {cas.name}. He is a {cas.species}. OoOoOoOoO Ahhhhhhh. Anything you wanna say {cas.name}? {cas.name}: {cas.famous_quote}")
# printing character introductions

character = input(f'Now what character will you control? {s.name}, {d.name} or {cas.name}')
c = character
print(f'Great! You chose {c}. On we go to the first hunt.')
# using input to determine player's character

print("You are now in an abandoned barn in the middle of Kansas and you notice it is getting extremely cold inside depsite the fact that is summer. Then, suddenly, a figure appears in the darkness...")
print(f'{crow.name}: Well well well, look who we have here. You know {c}, I thought you were smarter than that and would stay away. You do know how I am right? For god\'s sake I am {crow.name}, the {crow.species}! You see {crow.famous_quote}')
# introducing Stage 1

print(f'{c}: Seems like times have changed for the worst there {crow.name}.')
print(f'{crow.name}: You take that back! NO actually, I\'ll just kill ya instead!')
print(f'{c}: oh sh*t')
print(f'Ok if you somehow forgot the purpose of this game, you will be asked a series of 3 questions and you must get 1 of them right in order to escape and defeat {crow.name}. Here we go!')
# setting up battle questions

ques0 = 'What is the last name of Sam and Dean?'
ans0 = 'winchester'
com0 = {'ques' : ques0, 'ans' : ans0}

ques1 = 'Who is the older brother, Sam or Dean?'
ans1 = 'dean'
com1 = {'ques' : ques1, 'ans' : ans1}

ques2 = 'Who killed Sam and Dean\'s mom?'
ans2 = 'Azazel'
com2 = {'ques' : ques2, 'ans' : ans2}

ques3 = 'How many seasons of Supernatural are there?'
ans3 = '13'
com3 = {'ques' : ques3, 'ans' : ans3}

ques4 = 'What is the name of Sam and Dean\'s angel friend?'
ans4 = 'castiel'
com4 = {'ques' : ques4, 'ans' : ans4}

ques5 = 'What creature can become the appearance of another person by shedding its skin?'
ans5 = 'shapeshifter'
com5 = {'ques' : ques5, 'ans' : ans5}

ques6 = 'What is Sam and Dean\'s dad\'s name?'
ans6 = 'john'
com6 = {'ques' : ques6, 'ans' : ans6}

ques7 = 'What color car does Dean drive?'
ans7 = 'black'
com7 = {'ques' : ques7, 'ans' : ans7}

ques8 = 'In the pilot episode, who or what did Sam and Dean search for?'
ans8 = 'the woman in white'
com8 = {'ques' : ques8, 'ans' : ans8}

qa = [com0 , com1, com2, com3, com4, com5, com6, com8, com8]
# creating lists and dictionaries for the questions and answers

counter1 = 0
# setting variable for stage 1

def questions1():
    global counter1
    ans = input(qa[counter1]['ques']).lower()
    if ans == qa[counter1]['ans']:
        print(f'{crow.name}: {crow.advance}! That was correct!')
        counter1 += 1
    else:
        print(f'{crow.name}: {crow.fail}')
        print('Whelp, you died')
        print('GAME OVER')
# defining a function to ask the questions for stage 1 and what to do when the question is answered

counter2 = 3
# setting variable for stage 2

def questions2():
    global counter2
    ans = input(qa[counter2]['ques']).lower()
    if ans == qa[counter2]['ans']:
        print(f'{lil.name}: {lil.advance}! That was correct!')
        counter2 += 1
    else:
        print(f'{lil.name}: {lil.fail}')
        print('Whelp, you died')
        print('GAME OVER')
# defining a function to ask the questions for stage 2 and what to do when the question is answered

counter3 = 6
# setting the variable for stage 3

def questions3():
    global counter3
    ans = input(qa[counter3]['ques']).lower()
    if ans == qa[counter3]['ans']:
        print(f'{luc.name}: {luc.advance}! That was correct!')
        counter3 += 1
    else:
        print(f'{crow.name}: {crow.fail}')
        print('Whelp, you died')
        print('GAME OVER')
# defining a function to ask the questions for stage 3 and what to do when the question is answered

for x in range(3):
    questions1()
# asking the first round of questions

print(f'{crow.name}: This will not be the end of me! I will be back! Just watch your pretty little ....')
print(f'OKKKKKKKKK great work {c}! You have defeated {crow.name}, {crow.species}! Now onto the next hunt.')
# moving to stage 2

response = input('You are now looking around the barn and see a old red door that is covered in weird goo. Do you want to go in?')
if response == 'yes':
    print('Well aren\'t you daring. You open the door and AHHHHHHHHHHHHHHHH!!!!! You are sent soaring across the room and hit a wall')
elif response == 'no':
    print('Before you can turn around and run home crying to your mommy, the door bursts open! AHHHHHHHHHHHHHHHH!!!!! You are dragged into the room and was sent soaring across the room and hit a wall')
else:
    print('Whelp, no matter what you wanna do you open the door and AHHHHHHHHHHHHHHHH!!!!! You are sent soaring across the room and hit a wall')
# entering stage 2 by using if else statement to enter the door

print(f'{lil.name}: Well look what the cat dragged in. The beloved {c}. Seems like you were able to get past {crow.name} but you are no match against me. As you know, I am {lil.species} and not just your average {lil.species} but {lil.famous_quote}.')
print(f'{c}: I\'m sorry, I could\'t hear that over the size of your ego. So you can take your tush and move it back to hell. XD')
print(f'{lil.name}: HOW DARE YOU SAY THAT TO ME! OH NOW YOU ARE GOING TO HAVE IT!')
print(f'{c}: wow, what a surprise')
print(f'Well it looks like you got onto {lil.name}\'s bad side, now here comes another set of questions!')
# introducing lilith and stage 2

for x in range(3):
    questions2()
# asking next 3 questions for stage 2

print(f'I am not gonna lie, I am quite flabbergasted. I was not expecting you to defeat {lil.name} so HEY YOUR STILL ALIVE! Buttttt you are not done yet, now you only have to get through one more door, specifically the blue door that looks like it is begging someone to smash into it.')
# leaving stage 3

respone = input(f'Now {c}, do you want to go through the door?')
if response == 'yes':
    print(f'You touch the door and it turns into a pile of dust at your feet (shocker). You strut through the door like you are on the next episode of America\'s Top Model because {cas.name} got hold of the Netflix again and you just cannot help youself. When BAMM! Some random dude smashes through the wall.')
elif response == 'no':
    print(f'CMON REALLY. WHY ARE YOU EVEN HERE IF YOU DON\'T WANNA DO ANYTHING! ANYWAYSSSS you go touch the door and it turns into a pile of dust at your feet (shocker). You strut through the door like you are on the next episode of America\'s Top Model because {cas.name} got hold of the Netflix again and you just cannot help youself. When BAMM! Some random dude smashes through the wall.')
else:
    print(f'Really? It\'s a yes or no question what could you have possibly said? ANYWAYSSSS you go and touch the door and it turns into a pile of dust at your feet (shocker). You strut through the door like you are on the next episode of America\'s Top Model because {cas.name} got hold of the Netflix again and you just cannot help youself. When BAMM! Some random dude smashes through the wall.')
# entering stage 3 by using if else statement to enter the door

print(f'{c}: Well well well, isn\'t it lovely seeing your face again {luc.name}.')
print(f'{luc.name}: Why right back atcha {c}. Now all I am wondering is how you can be so dumb to wander into a place like this but it seems like you have gotten past {crow.name} and {lil.name}. They were worthless anyways, but how has your day been {c}? I must say, those struts really are fantastic! Have you been watching Project Runway by any chance?')
print(f'{c}: Alright alright I am not here to chat {luc.name} and don\'t you remember? I hate your guts so back off! And no, it\'s actually America\'s Next Top Model!')
print(f'{luc.name}: Ok if you just wanna get the suffering over with now then here we go! Let the fun begin!')
# introducing stage 3

for x in range(3):
    questions3()















