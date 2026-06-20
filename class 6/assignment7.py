priceofonetoy=int(input("enter price of one toy:"))
quanity=int(input("enter quanity:"))
totalamount=priceofonetoy*quanity
discount=totalamount*0.1
finalamount=totalamount-discount
print(f"price of on toy is {priceofonetoy}")
print(f"quanity is {quanity}")
print(f"total amount is {totalamount}")
print(f"discount is {discount}")
print(f"final amount is {finalamount}")