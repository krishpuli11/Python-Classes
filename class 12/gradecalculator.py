math=int(input("enter math marks:"))
english=int(input("enter english marks:"))
bio=int(input("enter bio marks:"))
totalmarks=math+english+bio
percentage=totalmarks/3
print(f"totalmarks is {totalmarks}")
print(f"percentage is {percentage}")
if percentage >= 90 and percentage <= 100:
    print("grade A")
elif percentage >= 80 and percentage < 90:
    print("grade B")
elif percentage >= 70 and percentage < 80:
    print("grade C")
elif percentage >= 60 and percentage < 70:
    print("grade D")
elif percentage >= 50 and percentage < 60:
    print("grade E")
else:
    print("failed")