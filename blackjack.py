import random

# Sum function
def sum(x):

	x_sum = 0
	x_ace = False

    # Check all the cards in the list
	for card in x:
		if card == "K(10)" or card == "Q(10)" or card == "J(10)":
			x_sum += 10
		elif card != "A(1-11)":
			x_sum += card
		# If the card is Ace:
		else:
			x_ace = True
			continue
		
    # If the card is Ace:		
	if x_ace == True:
		if x_sum <= 10:
			x_sum += 11
		else:
			x_sum += 1
	return x_sum

# Blackjack function
def blackjack():

	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)",
			   2, 3, 4, 5, 6, 7, 8, 9, 10, "J(10)", "Q(10)", "K(10)", "A(1-11)"]
	
    # Player and opponent's cards
	player = [cards[random.randrange(0, 52)], cards[random.randrange(0, 52)]]
	ai = [cards[random.randrange(0, 52)], cards[random.randrange(0, 52)]]

	end = False

    # Print the cards
	print("\nPlayer's cards:     ", player, "=", sum(player),
	      "\nOpponent's cards:   ", str(ai[0]) + ", Closed card")

    # Game loop
	while not end:

        # Check player's input
		play = input("\nWhat do you want to do? (Draw card/stay): (1/2)\n")

		player_sum = 0
		opponent_sum = 0
		# If player wants to draw a card
		if play == "1":
			player.append(cards[random.randrange(0, 52)])

            # Sum of the cards
			player_sum = sum(player)

			opponent_sum = sum(ai)

            # If opponent's sum is less than 17 and game is not over
			if opponent_sum < 17 and player_sum <= 21:
				ai.append(cards[random.randrange(0, 52)])
				opponent_sum = sum(ai)

			print("\nPlayer's cards:     ", player, "=", sum(player),
			      "\nOpponent's cards:   ", ai, "=", sum(ai))
			
		# If player wants to stay
		elif play == "2":
            
            # Sum of the cards
			player_sum = sum(player)

			opponent_sum = sum(ai)
			
            # If the sum of the cards are equal and player did not draw a card
			if player_sum == opponent_sum:
				end = True

            # If opponent's sum is less than 17 and game is not over
			if opponent_sum < 17:
				ai.append(cards[random.randrange(0, 52)])
				opponent_sum = sum(ai)
				
			print("\nPlayer's cards:     ", player, "=", sum(player),
			      "\nOpponent's cards:   ", ai, "=", sum(ai))
		# Conditions that will make the game end
		if player_sum >= 21 or opponent_sum >= 21 or (player_sum > opponent_sum and opponent_sum >= 17):
			end = True

	# Comparison of the sums		
	if 21 >= player_sum == opponent_sum or (player_sum > 21 and opponent_sum > 21):
		print("\nDraw. Try again.")
		
	elif player_sum == 21:
		print("\nBlackjack! You won! Congratulations.")
		
	elif 21 > player_sum > opponent_sum or player_sum < 21 and opponent_sum > 21:
		print("\nYou won! Congratulations.")
		
	elif 21 > opponent_sum > player_sum or player_sum > 21 and opponent_sum < 21:
		print("\nYou lost. Try again.")
		
	else:
		print("\nBlackjack! You lost. Try again.")

	ask = input("Would you like to play again? (Yes/No): (1/2)\n")

    # If player wants to play again
	if ask == "1":
		blackjack()
blackjack()
