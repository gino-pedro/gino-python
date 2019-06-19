
name = input("What is your name? ")
print("Welcome",name,"\n")


sex = input("Are you M or F?")

if sex == ("M") or ("F"):
    print("Thank you",name,"You are",sex,"\n")

elif sex != ("M") or ("F"):
        sex = input ("I said, are you M or F?")



age = int(input("What is your age?"))
if age < 18:
    print("You are under age",name,"and will not be allowed to gain entry")
else:
    print("You are admitted",name,". Welcome!")

