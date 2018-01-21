#exception handling
try:
    
    s=input("enter the name:")
except EOFError :
    print("why did you do an EOF on me")
except KeyboardInterrupt:
    print("you cancelled the operation")

else :
    print("You enteered {}".format(s))
