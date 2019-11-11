import math, random

gameLoop = False
startLoop = True

start = input("välkommen till ett gissa talet spel.\nÄr du redo att spela? [JA] eller [NEJ]: ")

while startLoop == True:
	
	if start == "ja" or "JA":
		gameLoop = True
		startLoop = False
	elif start == "nej" or "NEJ":
		gameLoop = False
		startLoop = False
	else:
		start = input("Ditt svar var inte accepterat av systemet\nÄr du redo att spela? [JA] eller [NEJ]: ")
		pass

answer = random.randint(1,10)
while gameLoop == True:
	try:	
				
		guess = int(input("Bra.\nVälj ett heltal mellan 1 och tio: "))
		print(answer, guess)
		if guess > answer:
			print("Ditt tal var för stort, prova igen.")
		elif guess < answer:
			print("Ditt tal var för litet, prova igen.")
		elif guess == answer:
			print("Rätt svar var " + str(answer) + ", bra jobbat.")
			gameLoop = False
	except:
		print("Något gick fel.")