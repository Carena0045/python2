#logical operators
age=int(input("Enter age:"))
citizenship=(input("Enter citizenship:"))
if(age>=18 and citizenship=="Kenyan"):
    print("Eligible voter")
else:
    print("Not eligible")