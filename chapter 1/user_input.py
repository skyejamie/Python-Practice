# user input
hobby = input('What is your favorite hobby?') # have the user type
print(hobby) # prints out whatever the user typed

# Numbers only input
favNum = int(input("Type your favorite number here and this program will print it out for you: ")) # allows the user to type an integer when prompted (typing anything that isn't a number will result in an error)
print(favNum) # prints out the number

#type conversion
num = int(input("Type a number here and it'll add by 10: ")) # create a number only input and have it be converted into an integer
print(type(num)) # storing the integer in the num variable
print(num) # prints the number the user inputted
print(num + 10) # have it also print the number added by 10