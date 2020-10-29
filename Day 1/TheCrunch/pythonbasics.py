##########################################################
# Day 1
#Python Basics
# Manish Beesetti
##########################################################

#Strings
#Declaring a string

string1 = "i am batman\t"
#printing a variable
print(string1)

string2 = ", Where is the Joker."

print(string2)

#string concatination

string_3 = string1 + string2;

print(string_3)

############## I nbuilt String Functions and Methods ####################

#Length of a string or tbh almost anything

print(len(string_3))

#captralize coverts the 1st char to capital

print(string_3.capitalize())

#center returns a centered string based on given spaces
#for suppose you input 50 spaces ,  the following returns a string centered in those 50 spaces.

#Note until and unless the parameter passed to the center is > the Length of the input string there will be no change.
print(string_3.center(32)) # so here nothing happens
print(string_3.center(100)) #here the the givenf string is palced or centered in b/w those 100 spaces

#casefold converts the given string into lower case

print(string_3.casefold())

#count returns the number of occourances of a substring in a given string
# synntax string.count(value, start, end)
print(string_3.count("e"))
print(string_3.count("e",25,-1)) # in python reverse indexing starts with -1
#where - 1 represents the last  and -2 represents the last before position in anything and so on


#endswith returns a boolen value
# boolen is True/False
print(string_3.endswith("."))

#expandable tabs as its obvious it increases the alcual tab size which is generally 4 spaces to a specified value

print(string_3.expandtabs(50))

#find methos is very useful to search for a specific substring which returns the start position of the substring
#syntax string.find(value, start, end)
print(string_3.find("batman"))

#Formatting strings
#the braces within the strings are called place holders
str_1 = "I am {name}, Intentional Kills {kills}".format(name="Batman",kills=0)
print(str_1)

#index
#gives the index of a given substring

print("position {pos}".format(pos=string_3.index("batman")))

#isalnum
#returns boolena value if all the characters are alphanumeric (a-z,A-Z,0-9)

print(str_1.isalnum())
