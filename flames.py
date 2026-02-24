

print("=======================================")
print("         FLAMES!!")
print("=======================================")

print("      F        L     A          M         E        S")
print("      |        |     |          |         |        |")
print("      Friends  Love  Affection  Marriage  Enemies  Siblings")
print("=======================================")

name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")

# Remove common letters
for letter in name1[:]:
    if letter in name2:
        name1 = name1.replace(letter, "", 1)
        name2 = name2.replace(letter, "", 1)

count = len(name1) + len(name2)

print("\nRemaining letters count:", count)
print("Calculating destiny... ")

flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

while len(flames) > 1:
    index = (count % len(flames)) - 1
    
    if index >= 0:
        right = flames[index + 1:]
        left = flames[:index]
        flames = right + left
    else:
        flames = flames[:len(flames) - 1]

result = flames[0]

print("\n=======================================")
print("             RESULT IS...")
print("=======================================")

if result == "Friends":
    print("You're just besties ")
    print("A friend in need is a friend indeed.")
elif result == "Love":
    print("IT'S LOVE BABY ")
    print("Match made in heaven ")
elif result == "Affection":
    print("Soft feelings detected ")
    print("It's giving wholesome vibes.")
elif result == "Marriage":
    print(" Wedding bells ringing!")
    print("Don't count your chickens before they hatch ")
elif result == "Enemies":
    print("Yikes ")
    print("This ship ain't sailing ")
elif result == "Siblings":
    print("Sibling energy ")
    print("Sweet home Alabama? NO.")
    
print("=======================================")
print("Remember: Love is blind ")
print("But FLAMES never lies ")
print("=======================================")