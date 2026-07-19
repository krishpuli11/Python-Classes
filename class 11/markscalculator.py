math=int(input("enter math marks:"))
english=int(input("enter english marks:"))
science=int(input("enter science marks:"))
percentage=(math+english+science)/3
if percentage>=90:
    print("excellent")
else:
    print("keep practicing")

print(f"math is {math}")
print(f"english is {english}")
print(f"science is {science}")
print(f"percentage is {percentage}")