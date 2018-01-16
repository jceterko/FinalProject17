class Character(object):
    def __init__(self, name, species, famous_quote):
        self.name = name
        self.species = species
        self.famous_quote = famous_quote
        self.n = 0
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
    print('CORRECT!')
    self.n += 1

def fail(self):
    print('NOOOOOOOOOOO you ded')

def get_questions(self):
    global q
    q = self.questions[self.n]
    if input(q['ques']) == q['a']:
      self.advance()
    else:
        self.fail()

c = Character("Castiel", "Angel", "I'll interrogate the cat.")
d = Character("Dean", "Human", "I mean, come on. We hunt monsters. Normal people, they see a monster and they run, but not us. We seach out things that want to kill us. You know who does that? CRAZY PEOPLE.")
s = Character("Sam", "Human", "I lost my shoe!")
crow = Character("Crowley", "King of Hell", "I was an attractive child. I could juggle. I was worth five pigs at least.")
lil = Character("Lilith", "Demon", "The first demon Lucifer has created.")
luc = Character("Lucifer", "Angel", "Narcissistic personality disorder...Ok, this one I could have.")
# Creating character class

print("Welcome to Supernatural Trivia! You are going to answer questions in order to defeat your enemy. There will be 3 enemies, 3 stages and each one will get harder as you go. Now lets introduce our characters.")
# printing introduction to game

print(f"Here is {s.name}. He is a {s.species}. You have anything you would like to say {s.name}? {s.name}: {s.famous_quote}")
print(f"Next up is {d.name}. He is also a {d.species}. And here he is! {d.name}: {d.famous_quote}")
print(f"Lastly, the beloved {c.name}. He is a {c.species}. OoOoOoOoO Ahhhhhhh. Anything you wanna say {c.name}? {c.name}: {c.famous_quote}")
# printing character introductions

character = input(f'Now what character will you control? {s.name}, {d.name} or {c.name}')
print(f'Great! You chose {character}. On we go to the first hunt.')
# using input to determine player's character

print("You are now in an abandoned barn in the middle of Kansas and you notice it is getting extremely cold inside depsite the fact that is summer. Then, suddenly, a figure appears in the darkness...")
print(f'{crow.name}: Well well well, look who we have here. You know {character}, I thought you were smarter than that and would stay away. You do know how I am right? For god\'s sake I am {crow.name}, the {crow.species}! You see {crow.famous_quote}')
# introducint Stage 1

print(f'{character}: Seems like times have changed for the worst there {crow.name}.')
print(f'{crow.name}: You take that back! NO actually, I\'ll just kill ya instead!')
print(f'{character}: oh sh*t')
print(f'Ok if you somehow forgot the purpose of this game, you will be asked a series of 3 questions and you must get 1 of them right in order to escape and defeat {crow.name}. Here we go!')
# setting up battle questions

print(f'{crow.name}: HAHAHA if you are so smart then')

get_questions(c)
input(q['ques'])




