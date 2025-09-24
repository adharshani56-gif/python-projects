print("welcome to calculator world")
Ip=""
while(Ip!="q"):
    value1=int(input("Enter the number 1= "))
    value2=int(input("Enter the number 2= "))
    choice=(input("Enter the choice="))
    
    def add(value1,value2):
        return value1 +value2
    def sub(value1,value2):
        return value1 -value2
    def mul(value1,value2):
        return value1*value2
    def div(value1,value2):
        return value1/value2
    def mod(value1,value2):
        return value1%value2
    def floordiv(value1,value2):
        return value1//value2
    
    if choice=="+":
        print("addition= ",add(value1,value2))
    elif choice=="-":
        print("subtraction= ",sub(value1,value2))
    elif choice=="*":
        print("multiplication= ",mul(value1,value2))
    elif choice=="/":
        print("division= ",div(value1,value2))
    elif choice=="%":
        print("modulo=",mod(value1,value2))
    elif choice=="//":
        print("floordivision= ",floordiv(value1,value2))    
    else:
        print("undefined operator")
    Ip=input("again or quit[q] ")

else:
    print("thank you")


  
