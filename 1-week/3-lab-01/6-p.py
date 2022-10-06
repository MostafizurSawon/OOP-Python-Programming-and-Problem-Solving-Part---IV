# Print the sum of the current number and the previous number
count = 0
print("Printing current and previous number sum in a range(10)")
for i in range(0, 10):
    sum = count + i
    print(f"{i+1}. Current Number {i} Previous Number  {count} Sum:  {sum}")
    count = i