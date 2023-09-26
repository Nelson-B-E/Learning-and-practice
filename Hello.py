'''
the three commers is a commenting for multipule lines. start it with 3 commas and then finish it with another 3
'''
import os # importing moduals open up different fuctions . os stands for operating system 
os.system('clear') # this line tells the system to clear the page first.

# to make a veriable name it them say what it equials. 
full_name = "Bryce Nelson" # string need to have "" or '' to make it a string(words, letters)
age = 45 # numbers dont have commas to make them numbers and able to do math and number things
older = age + 5 # example of numbers
fruit = ["banana","Apple","orange"] # for a list use square brackets and seperate the items on the list with a comma remembering that the first item in the list has position 0. example banana is in position 0
fav_feature = {  # a Dictionary is a list. it is made up of two parts. a KEY and a VALUE PAIR. 
	"Bob": "tits", # the key is is "" so is the value pair. they are seperated by a : and the line finished with a ,
	"Steve": "ass",
	"Mary": "legs" # Mary is the key. Legs is the value pair.
}
print ("Hello World!") # printing a string
print (full_name) # printing a string veriable
print (age) #printing a number veriable
print (older)
print (fruit[2]) # prining a item on a list
print (fruit) # printing the list
print (fav_feature["Mary"]) # when you want to print this you call its Key. in this case its bob but when its printed you will see the Value pair