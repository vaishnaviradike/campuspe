

tea = input("Is there drama today? (yes/no): ")

if tea.lower() == "yes":
    print("Spill the tea sis What's the latest gossip? ")
    print("But remember — curiosity killed the cat so don't get too deep into the drama rabbit hole! ")
    spilled_tea = input("So, what's the tea? ")
    print(f"shittt {spilled_tea}! then we need to get the popcorn ready and continue")
    if "betrayal" in spilled_tea.lower():
        print("Omg, betrayal?")
    else:
        print("That's some drama, but not too wild.")
else:
    print("No drama? Impossible. This is suspicious.")