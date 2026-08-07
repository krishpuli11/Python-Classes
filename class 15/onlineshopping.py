purchaseamount=int(input("enter purchase amount:"))
premiummember=str(input("are you a premium member yes or no:"))
discount=0
finalpurchaseamount=0
if purchaseamount>2000:
 discount=purchaseamount*15/100
 finalpurchaseamount=purchaseamount-discount
if premiummember=="yes":
 finalpurchaseamount=purchaseamount-200
print(f"""
-------------------------
purchaseamount:{purchaseamount}
premiummember:{premiummember}
discount:{discount}
finalpurchaseamount:{finalpurchaseamount}
""")