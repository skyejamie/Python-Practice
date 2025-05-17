# user input
hobby = input('What is your favorite hobby?') # have the user type their hobby
print(hobby) # prints out whatever the user put

# Numbers only input
favNum = int(input("Type your favorite number here and this program will print it out for you: ")) # allows the user to type their favorite number when prompted (ONLY NUMBERS WORK)
print(favNum) #prints out the number

#type conversion
num = int(input("Type a number here and it'll add by 10: ")) # create a number only input and have it be converted into an integer
print(type(num)) # storing the integer in the num variable
print(num) # prints the number the user inputed
print(num + 10) # have it also print the number added by 10