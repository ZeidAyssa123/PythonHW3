#!/usr/bin/python2
# Name: Zeid Ayssa , Intro to Unix HW3 , Part1
import sys
import argparse
import fileinput
parser = argparse.ArgumentParser(description= "Process some numbers")
args = parser.parse_args()

answer = 1
Boolean = True
while(Boolean):
	try:
		InputVal = raw_input()
		value = InputVal
		InputVal = float(InputVal)
	except ValueError:
		if InputVal=='':
			print answer
			answer = 1
			continue
		else:
			print "could not convert string to float:", value
			break
	except EOFError:
		print "^D"
		if answer!=1:
			print answer
		else:
			answer = 1
		break
	else:
		answer*= InputVal
		continue		
