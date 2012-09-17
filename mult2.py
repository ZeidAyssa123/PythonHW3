#!/usr/bin/python2
# Name: Zeid Ayssa , Intro to Unix HW3 , Part2
import sys
from sys import exit
from sys import argv
import argparse
import fileinput
global Total
global check
Total=1
check = 0
argIgnoreBlank = '--ignore-blank'
argIgnoreNonNumeric = '--ignore-non-numeric'
def file_ignore_bad(argv):
	if argv[2].lower()==argIgnoreBlank.lower() or argv[2].lower==argIgnoreNonNumeric.lower():
		global check
		check+=1
		if argv[1].lower()==argIgnoreNonNumeric.lower():
			filelocation=3
		else:
			filelocation=4
	else:
		filelocation=2
	count = int(len(argv))
	inputfile = open(argv[filelocation], 'r')
	answer = 1
	for line in inputfile:
		try:
			InputVal = line
			value = InputVal
			InputVal = float(InputVal)
		except ValueError:
				continue
		else:
			answer*= InputVal
			continue
	global Total
	Total *=answer
	if check==2:
		print Total
	elif check==0:
		print Total
	return
	
def file_ignore_blanks(argv):
	if argv[2].lower()==argIgnoreBlank.lower() or argv[2].lower==argIgnoreNonNumeric.lower():
		global check
		check+=1
		if argv[1].lower()==argIgnoreBlank.lower():
			filelocation=3
		else:
			filelocation=4
	
	else:
		filelocation=2
	count = int(len(argv))
	inputfile = open(argv[filelocation], 'r')
	answer = 1
	for line in inputfile:
		try:
			InputVal = line
			value = InputVal
			InputVal = float(InputVal)
		except ValueError:
			if InputVal=='\n':
				continue
		else:
			answer*= InputVal
			continue
	global Total
	Total *=answer
	if check==2:
		print Total
	elif check==0:
		print Total
	return

def error_menu(argv):
	#print "error , wrong number of arguments"
	return

answer = 1
Boolean = True
if len(argv)==1:
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
	
elif len(argv)>1 and argv[1].lower()!=argIgnoreBlank.lower() and argv[1].lower()!=argIgnoreNonNumeric.lower():
# it means that the inputs are file names
	
	Total = 1
	count = int(len(argv))
	for x in range(1,count):
		inputfile = open(argv[x], 'r')
		answer = 1
		for line in inputfile:
			try:
				InputVal = line
				value = InputVal
				InputVal = float(InputVal)
			except ValueError:
				if InputVal=='\n':
					print answer
					answer = 1
					continue
				else:
					print "could not convert string to float:", value
					exit()
			else:
				answer*= InputVal
				continue
		#print answer
		Total *=answer
	print Total	
			
else:
	parser = argparse.ArgumentParser(description = "Process multiple files")
	parser.add_argument('files',metavar='?' , nargs='+',help='need a file input')
	parser.add_argument('--ignore-blank',dest = 'ignoreblankfunc',action='store_const',const = file_ignore_blanks, default = error_menu,help='multiplication of two files')
	parser.add_argument('--ignore-non-numeric',dest = 'ignoreNonNumericfunc',action='store_const',const = file_ignore_bad, default = error_menu,help='multiplication of two files')
	args = parser.parse_args()
	args.ignoreblankfunc(argv)
	args.ignoreNonNumericfunc(argv)
	
	


