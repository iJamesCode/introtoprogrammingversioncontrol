"""
AI attempt
By James Heffernan
"""
from __future__ import division
import random
import sys
import os
import math
"""	0 = Good
1 = OK
2 = bad
3 = awful
4 = sad 
5 = irritated
6 = bored
7 = confused
8 = exhausted
9 = annoyed
10 = Angry """
mood = 1
moodstr = ""

# Reponse type = 0 = Friendly and good 1 = monotone response 2 = angry response 3 = sad/depressed 4 = Funny/good
responsetype = 0
loop = True
responselist = []

# Identification words and phrases
hello = ["hello", "hi"]
robotstate = ["how are you"]
calc = ["square root of", "+", "plus", "-", "minus", "*", "times", "/", "divided by"]
bye = ["bye", "cya"]

def clear():
	sys.stdout.flush()

def getMood():
	global moodstr
	global responsetype
	if mood == 1:
		moodstr = "Good"
		responsetype = 0
	elif mood == 2:
		moodstr = "OK"
		responsetype = 1	
	elif mood == 3:
		moodstr = "bad"
		responsetype = 2
	elif mood == 4:
		moodstr = "awful"
		responsetype = 2
	elif mood == 5:
		moodstr = "sad"
		responsetype = 3
	elif mood == 6:
		moodstr = "irritated"
		responsetype = 2
	elif mood == 7:
		moodstr = "bored"
		responsetype = 3
	elif mood == 8:
		moodstr = "confused"
		responsetype = 1
	elif mood == 9:
		moodstr = "exhausted"
		responsetype = 2
	elif mood == 10:
		moodstr = "annoyed"
		responsetype = 2
	print moodstr

def getResponse(x):
	if responsetype == 0:
		print x[0]
	elif responsetype == 1:
		print x[1]
	elif responsetype == 2:
		print x[2]
	elif responsetype == 3:
		print x[3]
	elif responsetype == 4:
		print x[4]

def Hello():
	global lastsaid
	global mood
	helloresponse = ["Hello!", "Hello.", "Leave me alone", "Oh... Hey, I guess :(", "What's poppin B?"]
	getResponse(helloresponse)
	lastsaid = "hello"

def robotState():
	global lastsaid
	getMood()
	robotStateresponse = ["I am doing " + moodstr + ", and you?", "I am " + moodstr, "What does it matter to you?", moodstr + ", Thanks!"]
	getResponse(robotStateresponse)
	lastsaid = "robotstate"

def Calc():
	sqrtnum = 0
	if calc[0] in usertext:
		listsqrt = list(usertext.lower())
		slicesqrt = usertext.find("root of")
		narrowedsqrtlist = listsqrt[slicesqrt + 8:] 
		for item in narrowedsqrtlist:
			try:
				sqrtnum = sqrtnum * 10 + int(item)
			except ValueError:
				pass
		sqrtofsqrtnum = math.sqrt(float(sqrtnum))
		print "The square root of " + str(sqrtnum) + ", is " + str(sqrtofsqrtnum) + "."

	elif calc[1] or calc[2] or calc[3] or calc[4] or calc[5] or calc[6] or calc[7] or calc[8] in usertext:
		firstnum = 0
		secondnum = 0
		usertextlist = list(usertext.lower())
		
		if calc[1] in usertext:
			sliceplus = usertext.find("+")
			narrowedlist = usertextlist[sliceplus + 1:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == "+":
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ' :
						if item is usertextlist[sliceplus + 1]:
							pass
						else:
							break
			equationnum = firstnum + secondnum
			print str(firstnum) + " + " + str(secondnum) + " is " + str(equationnum)

		elif calc[2] in usertext:
			sliceplus = usertext.find("plus")
			narrowedlist = usertextlist[sliceplus + 5:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == 'p':
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						break
			equationnum = firstnum + secondnum
			print str(firstnum) + " plus " + str(secondnum) + " is " + str(equationnum)

		elif calc[3] in usertext:
			sliceplus = usertext.find("-")
			narrowedlist = usertextlist[sliceplus + 1:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == '-':
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						if item is usertextlist[sliceplus + 1]:
							pass
						else:
							break
			equationnum = firstnum - secondnum
			print str(firstnum) + " - " + str(secondnum) + " is " + str(equationnum)

		elif calc[4] in usertext:
			sliceplus = usertext.find("minus")
			narrowedlist = usertextlist[sliceplus + 6:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == 'm':
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						break
			equationnum = firstnum - secondnum
			print str(firstnum) + " minus " + str(secondnum) + " is " + str(equationnum)

		elif calc[5] in usertext:
			sliceplus = usertext.find("*")
			narrowedlist = usertextlist[sliceplus + 1:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == '*':
						if item is usertextlist[sliceplus + 1]:
							pass
						else:
							break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						break
			equationnum = firstnum * secondnum
			print str(firstnum) + " * " + str(secondnum) + " is " + str(equationnum)

		elif calc[6] in usertext:
			sliceplus = usertext.find("times")
			narrowedlist = usertextlist[sliceplus + 6:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == 'm':
						break

			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						break
			equationnum = firstnum * secondnum
			print str(firstnum) + " times " + str(secondnum) + " is " + str(equationnum)

		elif calc[7] in usertext:
			sliceplus = usertext.find("/")
			narrowedlist = usertextlist[sliceplus + 1:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == '/':
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						if item is usertextlist[sliceplus + 1]:
							pass
						else:
							break
			try:			
				equationnum = firstnum / secondnum
				print str(firstnum) + " / " + str(secondnum) + " is " + str(equationnum)
			except ZeroDivisionError:
				print "Cannot divide by zero!"

		elif calc[8] in usertext:
			sliceplus = usertext.find("divided by")
			narrowedlist = usertextlist[sliceplus + 11:]
			for item in usertextlist:
				try:
					firstnum = firstnum * 10 + int(item)
				except ValueError:
					if item == 'd':
						break
			for item in narrowedlist:
				try:
					secondnum = secondnum * 10 + int(item)
				except ValueError:
					if item == ' ':
						break
			try:			
				equationnum = firstnum / secondnum
				print str(firstnum) + " divided by " + str(secondnum) + " is " + str(equationnum)
			except ZeroDivisionError:
				print "Cannot divide by zero!"

def Bye():
	global lastsaid
	global mood
	global loop
	byeresponse = ["Talk to you again soon!", "Bye.", "Does this mean you will finally shut up?", "Cya!"]
	getResponse(byeresponse)
	lastsaid = "bye"
	loop = False

def getIntent():
	for item in hello:
		if item in usertext.lower():
			Hello()
			break
		else:
			pass

	for item in robotstate:
		if item in usertext.lower():
			robotState()
			break
		else:
			pass

	for item in calc:
		if item in usertext.lower():
			Calc()
			break
		else:
			pass

	for item in bye:
		if item in usertext.lower():
			Bye()
			break
		else:
			pass

while loop == True:
	usertext = raw_input("")
	getIntent()








