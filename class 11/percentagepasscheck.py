math=int(input("enter math marks:"))
science=int(input("enter science marks"))
english=int(input("enter english marks"))
percentage=(math+science+english)/3
if percentage>=40:
    print("pass:")
else:
    print("fail:")
print(f"percentage is {percentage}")