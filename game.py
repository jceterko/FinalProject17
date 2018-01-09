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

print(f"Here is {sam.name}. He is a {sam.species}. You have anything you would like to say {sam.name}? {sam.famous_quote}")
print(f"Next up is {dean.name}. He is also a {dean.species}. And here he is! {dean.famous_quote}")
print(f"Lastly, the beloved {castiel.name}. He is a {castiel.species}. OoOoOoOoO Ahhhhhhh. Anything you wanna say {castiel.name}? {castiel.famous_quote}")
# printing character introductions

character = input(f'Now what character will you control? {sam.name}, {dean.name} or {castiel.name}')
print(f'Great! You chose {character}. On we go to the first hunt.')
# using input to determine player's character

print("You are now in an abandoned barn in the middle of Kansas and you notice it is getting extremely cold inside depsite the fact that is summer. Then, suddenly, a figure appears in the darkness...")
print(f'Well well well, look who we have here. You know {character}, I thought you were smarter than that and would stay away. You do know how I am right? For god\'s sake I am {crowley.name}, the {crowley.species}! {crowley.famous_quote}')


