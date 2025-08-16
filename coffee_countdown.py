def while_loop():
    days = int(input("How many days until the workshop ⸜(｡˃ ᵕ ˂ )⸝♡? "))
    total_coffee = 0
    if days <=0:
        print("Today is the day! Let's go PyLadies! ꉂ(˵˃ ᗜ ˂˵)")
    else:
        while days != 0:
            kohi = int(input(f"Day {days}: How many cups of coffee did you drink (˶˃ ᵕ ˂˶)? "))
            days -= 1
            total_coffee += kohi
        print(f"Total coffee before the workshop: {total_coffee} cups\nSteady fuel for the big day! ٩(ˊᗜˋ*)و☕")

def for_loop():
    days = int(input("How many days until the workshop ⸜(｡˃ ᵕ ˂ )⸝♡? "))
    total_coffee = 0 

    if days <=0:
        print("Today is the day! Let's go PyLadies! ꉂ(˵˃ ᗜ ˂˵)")
    
    else:
        for day in range(days, 0, -1):
            kohi = int(input(f"Day {day}: How many cups of coffee did you drink (˶˃ ᵕ ˂˶)? "))
            total_coffee += kohi
        print(f"Total coffee before the workshop: {total_coffee} cups 𖹭.ᐟ\nSteady fuel for the big day! ٩(ˊᗜˋ*)و☕")

for_loop()