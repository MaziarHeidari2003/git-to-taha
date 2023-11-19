import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rack,paper or scissors: ").lower()

    if player == computer:  
        print("computer: ",computer)
        print("player: ",player)
        print("tie")
    elif player == 'rock':
        if computer == 'scissors':
            print("computer: ",computer)
            print("player: ",player)
            print("player won")
        elif computer == 'paper':
            print("computer: ",computer)
            print("player: ",player)
            print("computer won")

    elif player == 'scissors':
        if computer == 'paper':
            print("computer: ",computer)
            print("player: ",player)
            print("player won")
        elif computer == 'rock':
            print("computer: ",computer)
            print("player: ",player)
            print("computer won")
    elif player == 'paper':
        if computer == 'rock':
            print("computer: ",computer)
            print("player: ",player)
            print("player won")
        elif computer == 'scissors':
            print("computer: ",computer)
            print("player: ",player)
            print("computer won")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes' :
        break        
print("Goodbye sweetie")    
            
        
    

        
