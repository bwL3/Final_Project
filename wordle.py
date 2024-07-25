# Welcome to wordle.py
# By Ben Weinstein
# Created for ICS3U

#import file/dependencies
import random
from rich import print as rprint
txt_path = 'words.txt'
words = []

with open(txt_path, 'r') as file: #opens file in read mode ('r')
    for rows in file: #iterates over file by row
        word = rows.strip() #removes whitespace
        words.append(word) #appends each word to a list

#Welcome/Rules
def initialize():
    print("""Welcome to wordle.py!
\nThe word must be a valid 5-letter word
Green means correct place
Yellow means the letter is in the word, but in the wrong place
Grey means the letter is not word
Good Luck!!\n""")

    #Select random word
    word = random.choice(words)
    return word

#Loop until word is correct or 6 guesses
#User guess
def user_guess():
    while True: 
        guess = input("Guess: ")
        if len(guess) == 5 and guess in words: #Verify 5 letter word
            break
        else:
            print("Invalid guess")
    return guess

def create_character_list():
    #Create list of all characters
    chars = 'qwertyuiopasdfghjklzxcvbnm'
    char_list = []
    for char in chars:
        char_list.append(char)
    #For keyboard overlay, 3 separate lists
    #of the rows on a qwerty keyboard are used
    kbtop = char_list[:10]
    kbmid = char_list[10:19]
    kbbot = char_list[19:]
    return kbtop, kbmid, kbbot

def remove_char(kblist, guess):
    #Remove character from keyboard list
    for char in guess:
        if char in kblist:
            char_index = kblist.index(char)
            kblist.pop(char_index)
    return kblist

#Check user guess --> format string coloured
def check_guess(guess, word):
    colour_list = [] #List of coloured str
    notfound = '' #str of characters from word that are not found
    for i in range(len(guess)):
        #Check green letters/correct position
        if guess[i] == word[i]:
            colour_list.append(f'[green]{guess[i]}[/green]')
            notfound += '_'
        else:
            colour_list.append(f'{guess[i]}') #Gray
            notfound += word[i] #word[i] was not in correct position
    #Check yellow letters
    for i in range(len(notfound)):
        char = notfound[i]
        if char != '_': # '_' means green character in colour_list, char in wrong pos
            #Check double letter in guess
            if guess.count(char) > word.count(char): # Guess has more of char than word
                for j in range(len(notfound)): #This itertaions makes it so the first letter is yellow
                    if guess[j] == char:
                        colour_list[j] = f'[yellow]{char}[/yellow]' #Adds yellow letter to colour_list
                        break
            elif char in guess and char in notfound: #Only 1 letter
                colour_list[guess.index(char)] = f'[yellow]{char}[/yellow]'
    colour_str = ''.join(colour_list)
    return colour_str

def main():
    word = initialize()
    kbtop, kbmid, kbbot = create_character_list()
    guess_list = []
    win = False
    for _ in range(6):
        print(''.join(kbtop))
        print(''.join(kbmid))
        print(''.join(kbbot))
        guess = user_guess()
        remove_char(kbtop, guess)
        remove_char(kbmid, guess)
        remove_char(kbbot, guess)
        colour_word = check_guess(guess,word)
        guess_list.append(colour_word)
        if guess == word:
            print(f"You win! The mystery word was {word}")
            win = True
            break
        else: #Guess is incorrect
            for i in guess_list:
                rprint(f'{i}')
            print()
    if not win:
        print(f"You lose, the word was {word}")
            
if __name__ == '__main__':
    main()