#Import Random Module
import random

#User's input if they want to roll a dice or not
user_input = input("Do you want to roll a dice? (y) or (n): ")


#Generate Random number if user wants to roll the dice
while (user_input=="y"):
    generate = random.randint(1,6)
    
    if(generate==1):
        print("[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]")
    
    elif(generate==2):
        print("[-----]\n[0    ]\n[     ]\n[    0]\n[-----]")

    elif(generate==3):
        print("[-----]\n[     ]\n[0 0 0]\n[     ]\n[-----]")
    
    elif(generate==4):
        print("[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]")

    elif(generate==5):
        print("[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]")

    else:
        print("[-----]\n[0   0]\n[0   0]\n[0   0]\n[-----]")

    user_input = input("Do you want to roll a dice again? (y) or (n): ")

