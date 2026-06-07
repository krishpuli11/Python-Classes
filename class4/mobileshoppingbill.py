mobileprice=int(input("enter mobileprice"))
numberofmobiles=int(input("enter numberofmobiles"))
totalprice=mobileprice*numberofmobiles
tax=totalprice*18/100
finalprice=totalprice+tax
print(f"mobile price is {mobileprice}")
print(f"number of mobiles is {numberofmobiles}")
print(f"total price is {totalprice}")
print(f"tax is {tax}")
print(f"finalprice is {finalprice}")

