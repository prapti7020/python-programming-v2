# day =3

# match(day):
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tus")
#     case 3:
#         print("wes")



# day = 5
# match(day):
#     case 1:
#         print("mon")
#     case 2:
#         print("tue")
#     case 3:
#         print("thus")
#     case 4:
#         print("wed")
#     case 5:
#         print("fri")


a = int(input("enter a first operators"))
b = int(input("enter a second operators"))
op = input("enter operators(+,-,*,%):")
match(op):
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)



day = int(input("enter day number (1-7):"))
match(day):
    case 1:
        print("monday")
    case 2:
        print("tues")
    case 3:
        print("wed")
    case 4:
        print("thu")
    case 5:
        print("fri")
    case 6:
        print("sat")
    case 7:
        print("sun")



month = int(input("enter a month number(1,12):"))
match(month):
    case 1:
        print("jan")
    case 2:
        print("feb")
    case 3:
        print("mar")
    case 4:
        print("apr")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("jul")
    case 8:
        print("aug")
    case 9:
        print("sep")
    case 10:
        print("oct")
    case 11:
        print("nov")
    case 12:
        print("dec")



choice = int(input("enter your choice:"))
match choice:
    case 1:
        print("check balance")
    case 2:
        print("deposite money")
    case 3:
        print("withdraw money")
    case 4:
        print("invalid choice")




units = int(input("enter electricity units:"))
match units:
    case 100:
        print("bill is 500")
    case 200:
        print("bill is 1200")
    case _:
        print("invalid units") 







                    



     
          



