totalpurchaseamount=int(input("enter the total amount:"))
couponcode=str(input("enter coupon code:"))
validcouponcode="save8465"
discounton500=0
coupondiscount=0
if totalpurchaseamount>500:
   discounton500 = totalpurchaseamount*5/100
if couponcode==validcouponcode:
    coupondiscount=50
else:
    print("invalid coupon discount")
finalprice=totalpurchaseamount-discounton500-coupondiscount
print(f"""
    -------------------------------
    totalpurchaseamount:{totalpurchaseamount}
    discounton500:{discounton500}
    coupondiscount:{coupondiscount}
    finalprice:{finalprice}
""")

