

with open("D:\\ACADS\\AOC\\2024\\day1\\aoc1_input.txt") as input_file:
    content = input_file.read()
    sepContent = content.split("\n")

list1 = []
list2 = []
for pair in sepContent:
    sepPair = pair.split("   ")
    list1.append(int(sepPair[0]))
    list2.append(int(sepPair[1]))

list1_sorted = sorted(list1)
list2_sorted = sorted(list2)
sum_of_differences = 0
print(len(list1))
for i in range(len(list1)):
    sum_of_differences += abs(list2_sorted[i]-list1_sorted[i])

print(sum_of_differences)    
