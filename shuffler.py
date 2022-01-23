#List-Shuffler 
import random

#x = ["str"]
def shuffle():
	src = 'list.txt'
	# import any .txt or .py (list) --- 'list.txt'
	with open(src, mode='r', encoding='utf-8') as f:
		lines = f.readlines()
	
	# use 'import random' to shuffle list that is under a variable of 'lines'
	random.shuffle(lines)
	
	# "*lines, sep=''" to get rid of '\n'
	print(*lines, sep='')
	
	

input("Press 'Enter' to start")
print('\n'+ '-----------------')
# call function 'shuffle'
shuffle()
print('-----------------' + '\n')

x = 1
while x == 1:
	
	q = str(input("Shuffle again? y/n:"))
	if q == "n" or q == "N":
		print ("exit")
		quit()
		
	elif q == "y" or q == "Y":
		print('\n'+ '-----------------')
		shuffle()
		print('-----------------' + '\n')
        
	else:
		
		code = "Unexpected KeyError"
		
		e = 'ValueError'
		print(e,"'",q,"'")
		raise ValueError(code, q)
		quit()
#eg = [1,2,3,4,5]
#print (random.choice(eg))


#From Greg: I made this so i can study for my chemistry quiz
