import random

r = random.randrange(2,10) 
# to inclued 10
r = random.randint(2,10) 
print(r)

top_number = input("Eneter the top number")
if top_number.isdigit():
    top_number = int(top_number)
print(top_number)


while True:
    guss = input("guss the rundom number ")
    if guss.isdigit():
        guss = int(guss)
    else:
        print("guss again")
        continue
    if guss == top_number:
        print("you win")
        break
    else:
        print("you loss")