# Finicky Counter
# Demonstrates the break and continue statements

count = 0
while True:
    count += 1
    
#end loop if count is greater than 10 <--this is the exit condition
    if count > 10:
        break
#Skip 5
    if count == 5:
        continue
    print(count)
    
input("\n\nPress the enter key to exit.")