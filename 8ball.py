import sys

import random



ans = True






while ans:

	question = raw_input("Ask the magic 8 ball a question: (press q to quit) ")


	answers = random.randint(1,9)

	if question == "":

		print "Ask a question!"

	if question == "":

		ignore answers

	if question == "q":

		sys.exit()

	elif answers == 1:

		print "It is certain"

	elif answers == 2:

		print "Outlook good"

	elif answers == 3:

		print "You may rely on it"

	elif answers == 4:

		print "Ask again Later"

	elif answers == 5:

		print "Concentrate and ask again"

	elif answers == 6:

		print "Reply hazy, try again"

	elif answers == 7:

		print "My reply is no"

	elif answers == 8:

		print "My sources say no!"

	elif answers == 9:

		print "9TH ANSWER"




