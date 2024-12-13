file = "/Users/samiyakan/Documents/proj/advent-of-code-2024/inputs/day1_input.txt"
f = open(file,"r")

left, right, sum = [], [], 0 

for line in f:
    a = line.split("   ")
    left.append(int(a[0]))
    right.append(int(a[1]))

left = sorted(left)
right = sorted(right)

for index in range(len(left)):
    sum += abs(left[index] - right[index])

print(sum)



# ----------------------- Same solution but using map -----------------------
# file = "/Users/samiyakan/Documents/proj/advent-of-code-2024/inputs/day1_input.txt"
# f = open(file,"r")

# left, right, sum = [], [], 0

# for line in f:
#     num1, num2 = map(int, line.split("   "))
#     left.append(num1)
#     right.append(num2)

# left = sorted(left)
# right = sorted(right)


# for index in range(len(left)):
#     sum += abs(left[index] - right[index])

# print("The sum is",sum)
