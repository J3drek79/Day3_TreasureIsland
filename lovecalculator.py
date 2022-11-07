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

print(namecombined)
