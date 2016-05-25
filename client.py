import random
from socket import *
serverName = 'allv25.all.cs.stonybrook.edu' 
serverName = 'localhost' 
serverPort = 5166 
G = 0
W = 0
O = 0
tieBreaker = True


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

command = raw_input("Connection Started. Enter Command to Begin (Login or Help): ")
if command == 'login' or command == 'Login':
		userID = raw_input("Enter User ID: ")
		clientSocket.send(userID)
		user = clientSocket.recv(1024)

elif command == 'help' or command == 'Help':
		print "Help List: "
		print "-Help: Displays list of acceptable commands"
		print "-Login: Accepts a user ID"
		print "-Rock: Throws rock shape as move"
		print "-Paper: Throws paper shape as move"
		print "-Scissors: Throws scissor shape as move"
		print "-Logout: End game session"
		break		

while True:
	servMove = random.randint(0,2)
	print servMove
	command = raw_input("Enter Rock, paper or scissors: ")	
	clientSocket.send(command)
	move = clientSocket.recv(1024)
	if move1 == 'rock' or move1 == 'Rock':
		if servMove == 0:
			while tieBreaker != False:
				print servMove
				move2 = raw_input("Tie. Pick Another move: ")
				servMove = random.randint(0,2)
				if move2 == 'rock' and servMove == 1:
					print "You Lose"
					G += 1
					tieBreaker = False
				elif move2 == 'rock' and servMove == 2:
					print "You Win!"
					G += 1
					W += 1
					tieBreaker = False
				elif move2 == 'paper' and servMove == 0:
					print "You Win!"
					G += 1
					W += 1
					tieBreaker = False
				elif move2 == 'paper' and servMove == 2:
					print "You Lose"
					G += 1
					tieBreaker = False
				elif move2 == 'scissors' and servMove ==0:
					print "You Lose"
					G += 1
					tieBreaker = False
				elif move2 == 'scissors' and servMove == 1:
					print "You Win!"
					G += 1
					W += 1
					tieBreaker = False
				else:
					move2 = raw_input("Tie. Pick Another move: ")
					servMove = random.randint(0,2)

			elif servMove == 1:
				print "You Lose"
				G += 1
			else:
				print "You Win!"
				G += 1
				W += 1	
		elif move1 == 'paper' or move1 == 'Paper':
			if servMove == 0:
				print "You Win!"
				G += 1
				W += 1
			elif servMove == 1:
				while tieBreaker != False:
					print servMove
					move2 = raw_input("Tie. Pick Another move: ")
					servMove = random.randint(0,2)
					if move2 == 'rock' and servMove == 1:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'rock' and servMove == 2:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					elif move2 == 'paper' and servMove == 0:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					elif move2 == 'paper' and servMove == 2:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'scissors' and servMove == 0:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'scissors' and servMove == 1:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					else:
						move2 = raw_input("Tie. Pick Another move: ")
						servMove = random.randint(0,2)
			else:
				print "You Lose"
				G += 1
		elif move1 == 'scissors' or move1 == 'Scissors':
			if servMove == 0:
				print "You Lose"
				G += 1
			elif servMove == 1: 
				print "You Win!"
				G += 1
				W += 1
			else:
				while tieBreaker != False:
					print servMove
					move2 = raw_input("Tie. Pick Another move: ")
					servMove = random.randint(0,2)
					if move2 == 'rock' and servMove == 1:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'rock' and servMove == 2:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					elif move2 == 'paper' and servMove == 0:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					elif move2 == 'paper' and servMove == 2:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'scissors' and servMove == 0:
						print "You Lose"
						G += 1
						tieBreaker = False
					elif move2 == 'scissors' and servMove == 1:
						print "You Win!"
						G += 1
						W += 1
						tieBreaker = False
					else:
						move2 = raw_input("Tie. Pick Another move: ")
						servMove = random.randint(0,2)
	elif command == 'Logout' or 'logout':
		connectionSocket.close()
		print "Thanks for playing " + userID
		print "Games Played: " + G
		print "Games Won: " + W
		print "Games Timed-Out: " + O

	else:
		print "Enter Login or Help to begin"

print "in it"