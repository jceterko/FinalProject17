class Character(object):
    def __init__(self, name, species, famous_quote, advance, fail):
        self.name = name
        self.species = species
        self.famous_quote = famous_quote
        self.advance = advance
        self.fail = fail
        self.questions = [
            {'ques':'What is the last name of Sam and Dean?', 'a': 'Winchester'},
            {'ques':'Who is the older brother, Sam or Dean?', 'a':'Dean'},
            {'ques':'What creature killed Sam and Dean\'s mom?', 'a':'Demon'},
            {'ques':'How many seasons of Supernatural are there?', 'a':'13'},
            {'ques':'What is the name of Sam and Dean\'s angel friend?', 'a': 'Castiel'},
            {'ques':'What creature can become the appearance of another person by shedding its skin?', 'a':'shapeshifter'},
            {'ques':'In the pilot episode, who or what did Sam and Dean search for?', 'a':'The Woman in White'},
            {'ques':'What color car does Dean drive?', 'a':'black'},
            {'ques':'What is Sam and Dean\'s dad\'s name?', 'a':'John'}
        ]

def advance(self):
    n = 0
    print('CORRECT!')
    n += 1
def fail(self):
    print('NOOOOOOOOOOO you ded')

def get_questions(self):
    global q
    n = 0
    q = self.questions[n]
    n += 1



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
print(f'Great! You chose {character}. On we go to the first hunt.')
# using input to determine player's character
c = character

print("You are now in an abandoned barn in the middle of Kansas and you notice it is getting extremely cold inside depsite the fact that is summer. Then, suddenly, a figure appears in the darkness...")
print(f'{crow.name}: Well well well, look who we have here. You know {c}, I thought you were smarter than that and would stay away. You do know how I am right? For god\'s sake I am {crow.name}, the {crow.species}! You see {crow.famous_quote}')
# introducing Stage 1

print(f'{c}: Seems like times have changed for the worst there {crow.name}.')
print(f'{crow.name}: You take that back! NO actually, I\'ll just kill ya instead!')
print(f'{c}: oh sh*t')
print(f'Ok if you somehow forgot the purpose of this game, you will be asked a series of 3 questions and you must get 1 of them right in order to escape and defeat {crow.name}. Here we go!')
# setting up battle questions

print(f'{crow.name}: HAHAHA if you are so smart then')

get_questions(crow)
if input(q['ques']) == q['a']:
    advance(c)
else:
    fail(c)

get_questions(crow)
if input(q['ques']) == q['a']:
    advance(c)
else:
    fail(c)



