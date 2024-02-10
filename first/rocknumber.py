import random

option = ["rock","sheet","paper"]

user_score = 0
computer_score = 0

while True:
    user_guss = input("input rock/sheet /papare  and q to quit").lower()

    if user_guss == "q":
        break

    if user_guss not in option:
        continue

    computer_rand = random.randint(0,2)

    computer_guss = option[computer_rand]

    if user_guss == "rock" and computer_guss == "scissors":
        user_score += 1
    elif user_guss == "paper" and computer_guss == "rock":
        user_score += 1
    elif user_guss == "scissors" and computer_guss == "paper":
        user_score += 1
    else:
        computer_score +=1

print("user win " + str(user_score))
print("computer win win " + str(computer_score))
print("the last")



