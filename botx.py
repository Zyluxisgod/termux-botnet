import os
import sys
from termcolor import colored
from colored import fg, bg, attr
from pexpect import pxssh
from colors import *

'''
Dont you dare edit my masterpiece!
Nah, Im just kidding, do what you
want to it just make sure you give
me credit.
Created by:Zyluxisgod
'''

#Create File
def createFile():
	open("hosts.txt", "a+")

#Add 1 Bot
def addBot(host, user, password):
	file = open("hosts.txt", "a+")
	Bot = "%s %s %s" % (host, user, password)
	file.write(Bot)
	file.write("\n")

#Scan from File
def scanBots(filename):
	with open("%s" % (filename)) as f:
		file = open("hosts.txt","a")
		for line in f:
			str(line)
			file.write(line)

def listBots():
	with open("hosts.txt") as f:
		for line in f:
			list = []
			words = line.split()
			for word in words:
				list.append(word)
			count = 0
			print("%s [+]" % (fg("red")))+(list[count])
			count += 1

#Send Command
def sendCommand(cmd):
	with open("hosts.txt") as botnet:
		for bot in botnet:
			str(bot)
			loginInfo = []
			hup = bot.split()
			for word in hup:
				loginInfo.append(word)
			s = pxssh.pxssh()
			s.login(loginInfo[0], loginInfo[1], loginInfo[2])
			s.sendline(cmd)
			s.prompt()
			print(s.before)


#Menu stuff
while True:
	os.system("clear")
	file = open("Banner/banner")
	sys.stdout.write(BLUE)
	print(file.read())
	print("\n")
	print("%s 1: " % (fg("red")))+("%s Add Bots" % (fg("yellow")))
	print("%s 2: " % (fg("red")))+("%s Command Bots" % (fg("yellow")))
	print("%s 3: " % (fg("red")))+("%s List Bots" % (fg("yellow")))
	print("\n \n")
	menu_choice1 = input("%s <Botx>" % (fg("blue")))
	
#Sub Menus
	if menu_choice1==1:
		while True:
			os.system("clear")
			file = open("Banner/scanbots")
			sys.stdout.write(YELLOW)
			print(file.read())
			print("\n")
			print("%s 1: " % (fg("red")))+("%s Create txt File" % (fg("yellow")))
			print("%s 2: " % (fg("red")))+("%s Manual Input" % (fg("yellow")))
			print("%s 3: " % (fg("red")))+("%s Scan txt File" % (fg("yellow")))
			print("%s 00: " % (fg("red")))+("%s Main Menu" % (fg("yellow")))
			print("\n \n")
			menu_choice = input("%s <Botx>" % (fg("blue")))

#Create txt File
			if menu_choice==1:		
				os.system("clear")
				createFile()
#Add 1 Bot
			elif menu_choice==2:
				while True:
					os.system("clear")
					addBot(host=raw_input("%s Host: " % (fg("yellow"))), user=raw_input("%s User: " % (fg("yellow"))), password=raw_input("%s Password: " % (fg("yellow"))))
					break

#scan txt file
			elif menu_choice==3:
				while True:
					os.system("clear")
					scanBots(raw_input("%s Filename: " % (fg("yellow"))))
					print("%s [!] " % fg("red"))+("%s Scanning Bots" % (fg("yellow")))
					break

#Back Button
			elif menu_choice==00:
				break
				
#Just in Case
			else:
				print("%s One of the options please!" % (fg("white")))
				
#Command Bots
	elif menu_choice1==2:
		os.system("clear")
		file = open("Banner/commandbots")
		sys.stdout.write(YELLOW)
		print(file.read())
		sendCommand(raw_input("%s Command: " % (fg("yellow"))))
		
#List Bots
	elif menu_choice1==3:
		while True:
			os.system("clear")
			file = open("Banner/listbots")
			sys.stdout.write(YELLOW)
			print(file.read())
			print("\n")
			listBots()
			print("\n")
			print("%s 00 for back, ^C for Exit" % (fg("white")))                                            
			print("\n")
			choice = input("%s <Botx>" % (fg("blue")))
			if choice==00:
				break
			else:
				print("One of the Options Please")
