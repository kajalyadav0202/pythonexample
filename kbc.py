amount=0
print("KBC game")
print("your first question is:")
print("who is prime minister of india?")
print("1. modi 2. rajkumar 3. manmohan 4.yogi" )
ans=int(input("enter your choice"))
if ans==1:
    print("your answer is correct ")
    amount+=1000
    print("your second questionn is:")
    print(" which is national animal of india?")
    print("1.lion 2.tiger 3.cow 4.zebra")
    ans=int(input("enter your choise sir!"))
    if ans==2:
        print("your answer is correct ")
        amount+=30000
        print("your third question is:")
        print("what is capital of india? ")
        print("1.bhopal 2.goa 3.rajasthan 4.delhi")
        ans=int(input("enter your choice sir"))
        if ans==4:
            print("your answer is correct")
            amount+=50000
        else:
            print("your answer is incorrect")
    else:
        print("your answer is incorrect")
else:
    print("your answer is incorrect")
print(" you win the total amount is:",amount)

        