# Losing Battle
# Demonstrate (and fixing) the infinite loop

print("Lady GlitterSparkle is surrounded by a massive horde of orcs.")
print("Their decaying bodies spew from the earth as far as the eye can see.")
print("Fate settles over Lady GlitterSparkle omniously as she grips her wand ")
print("and prepares herself for her last battle. \n")

health = 10
horde = 0
damage = 3

while health > 0:
    horde += 1
    health -= damage
    
    print("Lady GlitterSparkle flicks the tip of her wand the horde, " \
          "but takes", damage, "damage points.\n")

print("She fought all magical creatures--defeating", horde, "of the horde.")
print("But alas, Lady GlitterSparkle is no more.")

input("\n\nPress the enter key to exit.")