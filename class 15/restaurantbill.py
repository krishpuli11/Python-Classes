totalbill=int(input("enter total bill:"))
membership=str(input("do you have a membership yes or no:"))
discount=0
finalbill=0
if totalbill>1000:  
 discount=totalbill*10/100
 finalbill=totalbill-discount
if membership=="yes":
 finalbill=finalbill-100
print(f"""
-----------------------
totalbill:{totalbill}
discount:{discount}
finalbill:{finalbill}
membership:{membership}

""")