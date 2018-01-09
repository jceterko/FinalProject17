class Character():
    def __init__(self, name, species, famous_quote):
        self.name = name
        self.species = species
        self.famous_quote = famous_quote

castiel = Character("Castiel", "Angel", "I'll interrogate the cat.")
dean = Character("Dean", "Human", "I mean, come on. We hunt monsters. Normal people, they see a monster and they run, but not us. We seach out things that want to kill us. You know who does that? CRAZY PEOPLE.")
sam = Character("Sam", "Human", "I lost my shoe!")
crowley = Character("Crowley", "Demon aka King of Hell", "I was an attractive child. I could juggle. I was worth five pigs at least.")
lilith = Character("Lilith", "Demon", "The first demon Lucifer has created.")
lucifer = Character("Lucifer", "Angel", "Narcissistic personality disorder...Ok, this one I could have.")
# Creating character class

print("Welcome to Supernatural Trivia! You are going to answer questions in order to defeat your enemy. There will be 3 enemies, 3 stages and each one will get harder as you go. Now lets introduce our characters.")
# printing introduction to game

print(f"Here is {sam.name}. He is a {sam.species}. You have anything you would like to say {sam.name}? {sam.famous_quote}")
print(f"Next up is {dean.name}. He is also a {dean.species}. And here he is! {dean.famous_quote}")
print(f"Lastly, the beloved {castiel.name}. He is a {castiel.species}. OoOoOoOoO Ahhhhhhh. Anything you wanna say {castiel.name}? {castiel.famous_quote}")
# printing character introductions


