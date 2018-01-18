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
lil = Character("Lilith", "Demon", "The first demon Lucifer has created.", "Have fun in hell suckerssss!" , "How is that even possible!!!!")
luc = Character("Lucifer", "Angel", "Narcissistic personality disorder...Ok, this one I could have.", "Such a fool, you will never learn.", "*poof*")
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

ques2 = 'What creature killed Sam and Dean\'s mom?'
ans2 = 'demon'
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

counter = 0

def questions():
    global counter
    ans = input(qa[counter]['ques']).lower()
    if ans == qa[counter]['ans']:
        print(f'{crow.name}: {crow.advance}! That was correct!')
        counter += 1
    else:
        print(f'{crow.name}: {crow.fail}')
        counter = 0

for x in range(3):
    questions()

print(f'{crow.name}: This will not be the end of me! I will be back just watch your pretty little ....')
print(f'OKKKKKKKKK great work {c}! You have defeated {crow.name}, {crow.species}! Now onto the next hunt.')

for x in range(3):
    questions()














