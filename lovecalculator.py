# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
namecombined = name1 + name2
count_t = namecombined.count("t")
count_r = namecombined.count("r")
count_u = namecombined.count("u")
count_e = namecombined.count("e")
count_l = namecombined.count("l")
count_o = namecombined.count("o")
count_v = namecombined.count("v")
count_e1 = namecombined.count("e")
count1 = count_t + count_r + count_u + count_e
count2 = count_l + count_o + count_v + count_e1
countcombined = int((f"{count1}{count2}"))
if countcombined < 10 or countcombined > 90:
    print(f"Your score is {countcombined}, you go together like coke and mentos.")
elif countcombined >= 40 and countcombined <= 50:
    print(f"Your score is {countcombined}, you are alright together.")
else:
    print(f"Your score is {countcombined}.")
