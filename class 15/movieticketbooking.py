age=int(input("enter the age:"))
student=str(input("are you a student yes or no:"))
baseticket=200
agediscount=0
studentdiscount=0
if age<12:
   agediscount=baseticket*50/100
if student=="yes":
   studentdiscount=baseticket*20/100
finalprice=baseticket-studentdiscount-agediscount
print(f"""
---------------------------------
baseticket:{baseticket}
agediscount:{agediscount}
studentdiscount:{studentdiscount}
finalprice:{finalprice}
""")

   
   
