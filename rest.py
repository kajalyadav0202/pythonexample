print("xyz resturent")
print("\n 1.Rs.10 samosa")
print("\n 2.Rs.20 kachori")
print("\n 3.Rs.35 cheeze petiez")
print("\n 4.Rs.45 paneer patiez")
print("\n 5.Rs.60 dosa")
print("\n 6.Rs.50 dark cold coffee")
ch=int(input("enter the choice:"))
amount=0
if ch==1:
    print("\n you selected samosa" )
    qua=int(input("enter the quantity you want sir! "))
    amount=qua*10
elif ch==2:
     print("\n you selected kachori ")
     qua=int(input("enter the quantity you want sir! "))
     amount=qua*20
elif ch==3:
      print("\n you selected cheez patiez")
      qua=int(input("enter the quantity you want sir! "))
      amount=qua*35
elif ch==4:
     print("\n you selected paneer patiez")
     qua=int(input("enter the quantity you want sir! "))
     amount=qua*45
elif ch==5:
     print("\n you selected dosa")
     a=int(input("enter the quantity you want sir! "))
     amount=qua*60
elif ch==6:
     print ("\n you selescted dark cold coffee")
     qua=int(input("enter the quantity you want sir! "))
     amount=qua*50
else:
     print("invalid choice")

gst=(amount*18)/100
total_amount=amount+gst
print("amount",amount)
print("gst",gst)
print("total bill is:",total_amount)