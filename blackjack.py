import random


def toplam(x):

	x_toplam = 0
	x_as = False

	for i in x:
		if i == "K(10)" or i == "Q(10)" or i == "J(10)":
			x_toplam += 10
		elif i != "A(1-11)":
			x_toplam += i
		# Kart AS ise:
		else:
			x_as = True
			continue

	if x_as == True:
		if x_toplam <= 10:
			x_toplam += 11
		else:
			x_toplam += 1
	return x_toplam

def blackjack():

	kartlar = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)"]
	oyuncu = [kartlar[random.randrange(0, 52)], kartlar[random.randrange(0, 52)]]
	ai = [kartlar[random.randrange(0, 52)], kartlar[random.randrange(0, 52)]]

	bitti = False

	print("\nOyuncunun kartları: ", oyuncu, "=", toplam(oyuncu),
	      "\nRakibin kartları:   ", str(ai[0]) + ", Kapalı kart")

	while not bitti:

		hamle = input("\nNe hamle yapmak istersiniz? (Kart çek/Çekme): (1/2)\n")

		oyuncu_toplam = 0
		rakip_toplam = 0
		# oyuncu kart çekerse
		if hamle == "1":
			oyuncu.append(kartlar[random.randrange(0, 52)])

			oyuncu_toplam = toplam(oyuncu)

			rakip_toplam = toplam(ai)

			if rakip_toplam < 17 and oyuncu_toplam <= 21:
				ai.append(kartlar[random.randrange(0, 52)])
				rakip_toplam = toplam(ai)

			print("\nİkiniz de kart çektiniz."
		          "\nOyuncunun kartları: ", oyuncu, "=", toplam(oyuncu),
			      "\nRakibin kartları:   ", ai, "=", toplam(ai))
		# oyuncu kart çekmezse
		elif hamle == "2":

			oyuncu_toplam = toplam(oyuncu)

			rakip_toplam = toplam(ai)

			if rakip_toplam < 17:
				ai.append(kartlar[random.randrange(0, 52)])
				rakip_toplam = toplam(ai)
				# oyuncu kart çekmiyorsa ve toplam eşit ise oyun dursun
				if oyuncu_toplam == rakip_toplam:
					bitti = True

			print("\nRakibin kart çekti."
				  "\nOyuncunun kartları: ", oyuncu, "=", toplam(oyuncu),
			      "\nRakibin kartları:   ", ai, "=", toplam(ai))
		# kart çekmenin duracağı koşullar
		if oyuncu_toplam >= 21 or rakip_toplam >= 21 or (oyuncu_toplam > rakip_toplam and rakip_toplam >= 17):
			bitti = True
	

	# karşılaştırma
	if oyuncu_toplam == 21:
		print("\nBlackjack! Kazandın! Tebrikler.")
	elif 21 > oyuncu_toplam > rakip_toplam or oyuncu_toplam < 21 and rakip_toplam > 21:
		print("\nKazandın! Tebrikler.")
		bitti = True
	elif 21 >= oyuncu_toplam == rakip_toplam or (oyuncu_toplam > 21 and rakip_toplam > 21):
		print("\nBerabere. Tekrar dene.")
		bitti = True
	elif 21 > rakip_toplam > oyuncu_toplam or oyuncu_toplam > 21 and rakip_toplam < 21:
		print("\nKaybettin. Tekrar dene.")
		bitti = True
	else:
		print("\nBlackjack! Kaybettin. Tekrar dene.")

	soru = input("Tekrar oynamak ister misin ? (1-2)")

	if soru == "1":
		blackjack()
blackjack()