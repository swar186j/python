fname=open("datasets/fruits.txt")

for i in fname:
		lis=i.split()
		print(lis)
#function to check whether entered word is a single character or not

def is_single_char(user_in):
	if len(user_in)==1:
		print("You have entered a single character")
	else:
		return False

#function to check if the input word is in the file

def is_present(user_in):
	count=0
	for j in lis:
		if user_in ==j:
			print("yes")
			count=count+1
		else:
			continue

		
	print("Count:",count)


#function to limit number of guesses
def guess():
	import random
	random_word=random.choice(lis)
	print("now guess the characters")
	chances=7
	guesses=''
	

	while chances>0:
		fails=0
		for char in random_word:
			if char in guesses:
				print(char)
			else:
				print("-")
				#for every failure fails will be incremented
				fails+=1

		if fails==0:
			print("you win")
			#now print the correct word
			print('The word is',random_word)
			break

		new_guess=input("guess a character:")
		guesses+=new_guess

		if new_guess not in random_word:
			chances-=1
			print("wrong word!!!")
			print(chances," more chances left")

			if chances==0:
				print("you lost the game")


#function to generate a random word if user passes its chance

#def generate_random():
#	import random
#	print(random.choice(fname.readline().split()))



user_in=input("enter word:")
is_single_char(user_in)
is_present(user_in)
print("let/'s guess the word now" )
guess()
