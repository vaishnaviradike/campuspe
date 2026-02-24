
print("======================================================")
print("             LIE DETECTOR 9000 ")
print("======================================================")

print("""
           [========]
              0   0   
                |    
             \\____/  

""")


print("Answer honestly (yes/no)\n")

score = 0

eye_contact = input("Did they avoid eye contact? ")
if eye_contact.lower() == "yes":
    score += 2

voice = input("Was their voice shaky? ")
if voice.lower() == "yes":
    score += 2

story_change = input("Did their story change midway? ")
if story_change.lower() == "yes":
    score += 3

late_reply = input("Did they reply late but were online? ")
if late_reply.lower() == "yes":
    score += 2

over_explain = input("Did they over-explain simple things? ")
if over_explain.lower() == "yes":
    score += 3

print("\nScanning behavior patterns...")

for i in range(5):
    print("Analyzing" + "." * i)

print("\n======================================================")
print("                 RESULTS")
print("======================================================")

percentage = score * 10

print("Suspicion Level:", percentage, "%")

if percentage >= 70:
    print(" RED ALERT!!!")
    print("This story has more holes than Swiss cheese ")
    print("When someone shows you who they are — believe them.")
    
elif percentage >= 40:
    print("⚠ Something feels off...")
    print("Trust your gut. It rarely lies.")
    
else:
    print("Seems clean… for now ")
    print("But keep your eyes open ")

print("\n======================================================")
print("FINAL VERDICT:")
print("Truth always comes out ")
print("You can run from the truth...")
print("But you can't hide forever ")
print("======================================================")