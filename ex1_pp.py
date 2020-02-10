def happy_birthday(age, name):      #function will save us a lot of work
    year = 2020
    birthday_date = (100 - age)+year
    return birthday_date

age  = int(input("What is your age? "))  #getting age in ints
name = input("Ok, and now Your name is...? ")
print("Congratz {} You will hit 100 at {}".format(name,happy_birthday(age,name)))

