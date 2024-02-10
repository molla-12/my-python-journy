import random

def roll():
    min_val = 1
    max_val = 6
    roll =random.randint(min_val,max_val)
    return roll

value = roll()
print(value)

 
while True:
    players= input("enter the number of players b/n (1-4) ")

    if players .isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("player number must be b/n 2 - 4")
    else:
        print("invalid number of players")

max_score = 3
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nplayer ", player_index ," trun started\n" )
        current_score = 0
        while True:
            should_roll = input("would you like to roll(y) ").lower()
            if should_roll != 'y':
                break
            value = roll()
            if value == 1:
                current_score = 0
                print("you rolled at one your turn done ")
                break
            else:
                current_score += value
                print("you rolled a: ",value )
        player_scores[player_index] += current_score
        print(player_scores[player_index])


print(player_scores)

   