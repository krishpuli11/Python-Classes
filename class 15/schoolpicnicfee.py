studentage=int(input("enter student age:"))
studentgrade=int(input("enter student grade:"))
basestudentfee=500
discount=0
finalfee=500
if studentage<12:
  discount=basestudentfee*20/100
  finalfee=basestudentfee-discount
if studentgrade==10:
 finalfee=basestudentfee-50
print(f"""
  -------------------------------
  studentage:{studentage}
  studentgrade:{studentgrade}
  discount:{discount}
  finalfee:{finalfee}
  baseticket:{basestudentfee}
 """)



