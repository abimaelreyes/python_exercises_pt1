# Abimael
# Exercise 1


'''
Exercise 1
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

from datetime import date

c_year=int(date.today().year)

info_per={}

info_per["name"]=input("What is your name? ")
info_per["age"]=int(input("How old are you? "))

if info_per["age"]>=100:
	print("%s,You already have 100 year old or more ;)"%info_per["name"])
else:
	less=(100-info_per["age"])+c_year
	print("Hey, %s, in %i you will be 100 years old"%(info_per["name"],less))





