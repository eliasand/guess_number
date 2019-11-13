import math, random, time

gameLoop = False
startLoop = True
restartLoop = True

while startLoop == True:
	start = input("välkommen till ett gissa talet spel.\nÄr du redo att spela? [JA] eller [NEJ]: ").lower()
	if start == "ja":
		gameLoop = True
		startLoop = False
	elif start == "nej":
		gameLoop = False
		startLoop = False
		print("avslutar programmet...")
		time.sleep(2)
	else:
		print("Ditt svar var inte accepterat av systemet.")

answer = random.randint(1,10)
while gameLoop == True:
	try:	
				
		guess = int(input("Bra.\nVälj ett heltal mellan 1 och tio: "))
		if guess > answer:
			print("Ditt tal var för stort, prova igen.")
		elif guess < answer:
			print("Ditt tal var för litet, prova igen.")
		elif guess == answer:
			print("Rätt svar var " + str(answer) + ", bra jobbat.")
			while restartLoop == True:
				restart = input("Vill du spela igen? [JA] eller [NEJ]: ").lower()
				if restart == "ja":
					restartLoop = False
				elif restart == "nej":
					gameLoop = False
					restartLoop = False
					print("avslutar programmet...")
					time.sleep(2)
				else:
					print("Ditt svar var inte accepterat av systemet.")
					restartLoop = True

	except:
		print("Något gick fel.")