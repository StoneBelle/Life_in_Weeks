# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Calculate difference between user age and age 90
diff = (90 - int(age))
days = (diff * 365)
weeks = (diff * 52)
months = (diff * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left")