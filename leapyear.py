# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year4 = year / 4
year100 = year / 100
year400 = year / 400
if (year4).is_integer() == False:
    print("Not leap year.")
elif (year100).is_integer() == False:
    print("Leap year.")
elif (year400).is_integer() == False:
    print("Not leap year.")
else:
    print("Leap year.")
