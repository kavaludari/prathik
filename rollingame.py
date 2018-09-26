import random
while True:
	#true is used to run loop indefenately till condition is satisfied
	a=input("enter r to roll the dice and any othe char to quit")
	if (a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		break
