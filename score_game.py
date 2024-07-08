import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

while True:
    players=input("Enter no.of player(2-4): ")
    if players.isdigit():
        players=int(players)
        if 1<=players<=4:
            break
        else:
            print("Must be (2-4)players!")

    else:
        print("Invalid,Try again!")
max_score=50
player_scores=[0 for _ in range(players)]
while max(player_scores)<max_score    :
    for player_idx in range(players):
        print("\n player number",player_idx+1,"turn has just started!")
        print("your total score is :",player_scores[player_idx],"\n")
        current_score=0
        while True:
            should_roll=input("would you like to roll(y)?" )
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                current_score=0
                print("you rolled a 1!,Turn done")
                break
            else:
                current_score += value
                print("you rolled a: ",value)
            print("your score is : ",current_score)
        player_scores[player_idx]    += current_score
        print("your total score is :", player_scores[player_idx])   
        
max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print("player number",winning_idx+1,"has won")
