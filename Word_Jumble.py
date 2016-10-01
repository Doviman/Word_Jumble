import random

cars = ['FERRARI', 'CORVETTE', 'PORCHE', 'EXCAPE', 'EXPLORER', 'SILVERADO', 'VIPER', 'AUDI',
        'MERCEDES', 'BENTLY', 'TESLA', 'FOCUS', 'FIESTA', 'TAHOE', 'SUBURBAN']
print 'Guess the car word jumble'

selection = random.choice(cars)
answer = selection

jumble = list(selection)

# scramble the letters in jumble

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,         # the comma is omitting the new line

guess = raw_input("\nWhat kind of car is jumbled? ")
guess = guess.upper()

def correct_answer(guess):
    while guess != answer:
        print 'guess again'
        guess = raw_input("\nWhat kind of car is jumbled? ")
        guess = guess.upper()
        if guess == answer:
            print '\nGot It'

correct_answer(guess)




