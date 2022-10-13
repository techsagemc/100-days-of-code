from random import choice

wins = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_end = False

player_hand = [choice(cards),choice(cards)]
print(f"player_hand: {player_hand}")
print(f"Player total: {player_hand[0] + player_hand[1]}")
"\n"
    
dealer_hand = [choice(cards),choice(cards)]
print(f"dealer_hand: {dealer_hand[0]}")

turn_end = False

def player_turn():
    losses = 0
       
    player_total = sum(player_hand)
    
    if player_total > 21:
        print("Bust!! You went over 21.")
        losses += 1
    
    elif input("Do you want to hit or stand?\n").lower() == "hit":
        player_hand.append(choice(cards))
        player_total += player_hand[-1]
        print(f"player_hand: {player_hand}")
        print(f"player_total: {player_total}")
    
    player_turn()
    

        

def dealer_turn():
    dealer_total = sum(dealer_hand)
    print(f"dealer_hand: {dealer_hand}")
    print(f"dealer total: {dealer_total}")
    
    dealer_total = sum(dealer_hand)
    
    
    if dealer_total < 17:
        dealer_hand.append(choice(cards))
        dealer_total += dealer_hand[-1]
        print(f"dealer_hand: {dealer_hand}")
        print(f"dealer total: {dealer_total}")
    
    elif (dealer_total > player_total) and (dealer_total <= 21)and dealer_total:
        print("Dealer Wins!")
        losses += 1
        game_end = True
        
        dealer_turn() 
    
    elif dealer_total > 21:
        print("Dealer Busts! You win!")
        wins += 1
        game_end = True
    
    elif dealer_total == player_total:
        print("It's a tie!")
        
    else:
        print("You win!")

player_turn()
        
        
        
                
    
            
        
    
    