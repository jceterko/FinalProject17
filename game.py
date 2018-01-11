class Character():
    def __init__(self, name, species, famous_quote):
        self.name = name
        self.species = species
        self.famous_quote = famous_quote

castiel = Character("Castiel", "Angel", "I'll interrogate the cat.")
dean = Character("Dean", "Human", "I mean, come on. We hunt monsters. Normal people, they see a monster and they run, but not us. We seach out things that want to kill us. You know who does that? CRAZY PEOPLE.")
sam = Character("Sam", "Human", "I lost my shoe!")
crowley = Character("Crowley", "King of Hell", "I was an attractive child. I could juggle. I was worth five pigs at least.")
lilith = Character("Lilith", "Demon", "The first demon Lucifer has created.")
lucifer = Character("Lucifer", "Angel", "Narcissistic personality disorder...Ok, this one I could have.")
# Creating character class

print("Welcome to Supernatural Trivia! You are going to answer questions in order to defeat your enemy. There will be 3 enemies, 3 stages and each one will get harder as you go. Now lets introduce our characters.")
# printing introduction to game

print(f"Here is {sam.name}. He is a {sam.species}. You have anything you would like to say {sam.name}? {sam.name}: {sam.famous_quote}")
print(f"Next up is {dean.name}. He is also a {dean.species}. And here he is! {dean.name}: {dean.famous_quote}")
print(f"Lastly, the beloved {castiel.name}. He is a {castiel.species}. OoOoOoOoO Ahhhhhhh. Anything you wanna say {castiel.name}? {castiel.name}: {castiel.famous_quote}")
# printing character introductions

character = input(f'Now what character will you control? {sam.name}, {dean.name} or {castiel.name}')
print(f'Great! You chose {character}. On we go to the first hunt.')
# using input to determine player's character

print("You are now in an abandoned barn in the middle of Kansas and you notice it is getting extremely cold inside depsite the fact that is summer. Then, suddenly, a figure appears in the darkness...")
print(f'{crowley.name}: Well well well, look who we have here. You know {character}, I thought you were smarter than that and would stay away. You do know how I am right? For god\'s sake I am {crowley.name}, the {crowley.species}! You see {crowley.famous_quote}')
# introducint Stage 1

print(f'{character}: Seems like times have changed for the worst there {crowley.name}.')
print(f'{crowley.name}: You take that back! NO actually, I\'ll just kill ya instead!')
print(f'{character}: oh sh*t')
print(f'Ok if you somehow forgot the purpose of this game, you will be asked a series of 3 questions and you must get 1 of them right in order to escape and defeat {crowley.name}. Here we go!')
# setting up battle questions

questions1 = ['What is the last name of Sam and Dean?', 'Who is the older brother, Sam or Dean?', 'What creature killed Sam and Dean\'s mom?']
questions2 = ['How many seasons of Supernatural are there?', 'What is the name of Sam and Dean\'s angel friend?', 'What creature can become the appearance of another person by shedding its skin?']
questions3= ['In the pilot episode, who or what did Sam and Dean search for?', 'What color car does Dean drive?', 'What is Sam and Dean\'s dad\'s name?']
answers1 = ['Winchester', 'Dean', 'Demon']
answers2 = ['13', 'Castiel', 'shapeshifter']
answers3 = ['The Woman in White', 'black', 'John']
# creating question and answers list




