marks=int(input("enter number of marks:"))

if marks >= 90:
    print("excellent")
elif marks >= 75 and marks <= 89 :
    print("very good")
elif marks >= 60 and marks <= 74 :
    print("good")
else:
    print("needs improvment")