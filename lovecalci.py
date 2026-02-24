print("===================================================")
print("            Love in air??!")
print("===================================================")


name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

crush_reply_time = int(input("How many hours do they take to reply? "))
green_flags = int(input("How many green flags? "))
red_flags = int(input("How many red flags? "))
overthinking_level = int(input("Overthinking level (1-10)? "))

print("\nAnalyzing compatibility...")
print("Loading delusion percentage...")

for i in range(1, 3):
    print("Processing" + "." * i)

# Love Score Formula (dramatic but simple)
score = (len(name1) + len(name2)) + green_flags * 5 - red_flags * 3 - crush_reply_time + overthinking_level

print("\n===================================================")
print("                RESULTS ARE IN")
print("===================================================")

if score >= 30:
    print(" LOVE SCORE:", score, "%")
    print("Match made in heaven ")
    print("You both are two peas in a pod ")
    print("Don't let this slip through your fingers ")
    
elif score >= 20:
    print(" LOVE SCORE:", score, "%")
    print("It's giving soft launch vibes ")
    print("But don't count your chickens before they hatch ")
    print("Proceed with caution duhh .")
    
elif score >= 10:
    print(" LOVE SCORE:", score, "%")
    print("Situationship detected.")
    print("You're building castles in the air ")
    print("Don't put all your eggs in one basket ")
    
else:
    print(" LOVE SCORE:", score, "%")
    print("Bruhh… run.")
    print("This ship is sinking ")
    print("Better safe than sorry ")

print("\n===================================================")
print("           BONUS DRAMA ANALYSIS")
print("===================================================")

if red_flags > green_flags:
    print(" Red flag parade happening.")
    print("When someone shows you who they are — believe them.")
else:
    print("Green flag energy ")
    print("Maybe love is in the air... or maybe it's just delusion.")

if crush_reply_time > 5:
    print("\nSlow replies detected.")
    print("If they wanted to, they would ")
else:
    print("\nFast replies??")
    print("Okayyy effort king/queen ")

print("\n===================================================")
print("FINAL ADVICE:")
print("Love is blind ")
print("But you don't have to be ")
print("===================================================")