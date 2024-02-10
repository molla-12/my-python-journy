name = input("enter you name bor ")
print("wellcome ", name ," choose your best turn ")

answare = input("yoy ar on bad way bro inter left to turn to left and right if you want to the right").lower()
if answare == "left":
    user_input= input("do you want ot swim or walk")
    if user_input == "swim":
        print("ok letswim on the watter  ")
    else:
        print("ok walk on yor preference")

elif answare == "right":
    print("what dos it mean niga")
else:
    print("wrong turn bro s")