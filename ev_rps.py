from random import choice

print "Hi, I am your computer. My name is Bob. We are going to play Rock-Paper-Scissors. Make your move (r, p, s)."


def rock_paper_scissors(s, computer, user):

	x = choice("rps")
	

	if s == "r" and x == "r":
		print "I play rock!"
		print "We tied!"
		return computer, user
	elif s == "r" and x == "s":
		print "I play scissors!"
		print "Rock beats scissors! I lose...You win!"
		return computer, user + 1
	elif s == "r" and "p":
		print "I play paper!"
		print "Paper beats rock! I win!"
		return computer + 1, user
	elif s == "s" and x == "r":
		print " I play rock!"
		print "Rock beats scissors! I win!"
		return computer + 1, user
	elif s == "s" and x == "s":
		print "I play scissors"
		print "We tied!!"
		return computer, user
	elif s == "s" and x == "p":
		print "I play paper!"
		print "Scissors beats paper! I lose...You win!"
		return computer, user + 1
	elif s == "p" and x == "r":
		print "I play rock!"
		print "Paper beats rock! I lose... You win!"
		return computer, user + 1
	elif s == "p" and x == "s":
		print " I play scissors!"
		print "Scissors beats paper! I win!"
		return computer + 1, user
	elif s == "p" and x == "p":
		print "I played paper!"
		print "We tied!"
		return computer, user
	else:
		print "I don't understand what you are saying! Please try again!!"

x = 0
s = 0	

move = raw_input("Make your move (r, p, s) or q to quit: ")
while move != "q":
	s, x =  rock_paper_scissors(move, s, x)
	print s, x
	
	move = raw_input("Make your move (r, p, s) or q to quit: : ")

print "Final Score is Bob: %d, You: %d" % (s, x)





