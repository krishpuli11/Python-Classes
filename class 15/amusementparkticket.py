age=int(input("enter your age:"))
weekend=str(input("is it a weekend today:"))
discount=0
ticketprice=600
finalticketprice=0
if age<10:
 discount=ticketprice*50/100
 finalticketprice=ticketprice-discount
if weekend=="yes":
 finalticketprice=ticketprice-100
 print(f"""
 age={age}
 weekend={weekend}
 ticketprice={ticketprice}
 finalticketprice{finalticketprice}
 discount:{discount}
 """)
