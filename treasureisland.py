print("welcome to the treasure island")
print("your mission is to find treasure")
DIRECTION= input("you're at a cross road.where do you want to go?\n LEFT OR RIGHT: ")
swim_wait= input("do you want to?\n swim or wait?:")
door= input("which clour of door you want?\n red,yellow or blue:")

if DIRECTION== "RIGHT":
    print("Game over")
if swim_wait== "swim":
    print( "game over")
if door=="red":
    print("game over")
elif door=="blue":
    print( "game over")
else:
    print("you won!")
