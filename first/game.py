print("welcom to computer quez")
playnig = input("do you want to play the game ")
print(playnig)

if playnig.lower() != "yes":
    quit()
print("lets play man ")

score = 0
answare = input("whay the CBS means? ")
if answare == "Core banking system":
    print("correct")
    score +=1
else:
    print("you loase")
answare = input("what mean python")
if answare == "oopl":
    print("corect")
    score +=1

print("you got " + str(score) + " marks in pyrhtom")
