from random import randint

## I imported a module on the internet called random. Random has a function called "randint" which takes in
## a range(an interval) and outputs a random number in between that interval  

#print(randint(0, 50)) -- This will print a random number inbetween 0 to 50 

#1. Create a list of play combination:


fing1 = ['rock', 'paper', 'scissor']

#indexing: Is extracting an element from a list: 0 indexing, if we need to extract scissor: we need to index[2]
# emotion = ['angry', 'happy', 'sad', 'fustrated']
# print(emotion[0]) -> output 'angrey'
#Task for Caleb: To print a random element from fling1: 

# Assign a random play to a computer: 
computer = (fing1[randint(0,2)])

# Creating games: C++, Python

# 10 years: Python and javascript: AI = Machine learning = Python

player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
    print(player)

