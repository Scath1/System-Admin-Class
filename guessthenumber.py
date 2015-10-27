print("Welcome to guess the number")

number = 10

ans = True

while ans:

	guess = int(raw_input("Enter a Guess"));


	if guess == number:
		ans = False
		print "correct"


	elif guess > number:
		print "Too high!"

	elif guess < number:
		print "Too low!"



