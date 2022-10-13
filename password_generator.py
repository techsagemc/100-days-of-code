import random
import string

#import all letters, symbols, and numbers to use for password
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

#Ask for how many characters from each category the user wants to use in the password
rletters = input()
rnumbers = input()
rsymbols = input()

#create variable to hold characters for password(string for ordered and use list if you want random)
password = []

#use for loops to randomize the character from each category and add to password variable
for letter in range(1, int(rletters) + 1):
    password += random.choice(letters)

for number in range(1, int(rnumbers) + 1):
    password += str(random.choice(numbers))

for symbol in range(1, int(rsymbols) + 1):
    password += random.choice(symbols)

###if you dont want to mix the characters together, you can stop here and print the variable###
    
    
#you can use the shuffle function to randomly shuffle the characters around so its not separated by
#numbers, symbols, and letters
random.shuffle(password)

#join isnt working for me so i used a for loop to add the characters from the list to a new variable as a string
shuffled_password = ""
for char in password:
    shuffled_password += char
     
print(shuffled_password) 
     
 #Voila!#
     



