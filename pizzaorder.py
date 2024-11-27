print("welcome to the python pizza deliveries" )
size=input("what size of pizza do you want?S,M,L:")
pepperoni=input("do you want pepperoni on your pizza? yes or no:" )
extra_cheese=input("do you want extra cheese on your pizza ? yes or no:")
bill= 0
if size == "S":
    bill=15
elif size == "M":
    bill=20
else: 
    size == "L"
    bill=25
if pepperoni == "yes":
    if size == "S":
      bill+=2
    else:
       bill+=3
if extra_cheese == "yes":
     bill+=1

print(f"your total bill is:${bill}")
