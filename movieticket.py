age = int(input("enter your age: "))
ticket = input("do you have a ticket? (0/1): ")

if ticket == "0":
    ticket = True 
else:
    ticket = False

if age < 15:
    print("you are allowed to watch the movie with parental guidance")
elif age < 18:
    print("you are not allowed to watch the movie")
    if ticket == True:
        print("you can go inside ")
    else:
        print("you cannot go inside")
else:
    print("you can watch the movie")
      
        