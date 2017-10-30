""" this program is telling story and you have to answer if the question is asked
Jan Snobl
"""



#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."



# inform user about game is in progress
print("Mad Libs started")
# user must name his main character
name = str(input("What is your name ?"))
# user must write adjective
adjective1 = str(input("Write some adjective: "))
adjective1 = str(adjective1)
# user must write adjective
adjective2 = str(input("Write second adjective: "))
# user must write adjective
adjective3 = str(input("Write third adjective: "))
# user must write verb
verb1 = str(input("Write some verb: "))
# user must write verb
verb2 = str(input("Write second verb: "))
# user must write verb
verb3 = str(input("Write last verb: "))
# user must write noun
noun1 = str(input("Write first noun: "))
# user must write noun
noun2 = str(input("Write second noun: "))
# user must write noun
noun3 = str(input("Write last noun: "))

print("It is gonna get funny")
# user writes list of things
animal = str(input("write some animal: "))
food = str(input("write some food: "))
fruit = str(input("write some fruit: "))
number = str(input("write some number: "))
superhero = str(input("write superhero name: "))
country = str(input("write some country: "))
dessert = str(input("write some dessert: "))
year = str(input("write some year: "))

# printing story and inserting inputs
print(STORY) % (adjective1, name, adjective2, adjective3, verb1, verb2, verb3, noun1, noun2, noun3, animal, food, fruit, number, superhero, country, dessert, year)
# There is some mistake in last line of code FIX THAT