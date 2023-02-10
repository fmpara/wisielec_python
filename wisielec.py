import sys
import random

from names import NAMES


number_of_tries = 5

word_random = NAMES[random.randint(0,len(NAMES)-1)]

word = word_random
used_letters =[]
user_word = []

for _ in word:
    user_word.append("_")

        

def find_indexes(word,letter):
    indexes = []
    for index,letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
        
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:",number_of_tries)
    print()
                

while True:
    letter = input("Podaj literę:")
    
    if len(letter) > 1:
        print("Musisz podać tylko jedną literę!")
    if str.isnumeric(letter):
        print("Nie można podawać cyfry!!")
    
    else:
        used_letters.append(letter)   
        found_indexes = find_indexes(word,letter)
    
    
    
        if len(found_indexes) == 0:
            print("Nie ma takiej litery")
            number_of_tries -=1
            if number_of_tries == 0:
                print("Koniec gry")
                sys.exit(0)
            
                
        else: 
            
            for index in found_indexes:
                user_word[index] = letter
            
            
            if "".join(user_word) == word:
                print("Udało się odgadnąć słowo!")
                print(user_word)
                sys.exit(0)
        
        show_state_of_game()    
        