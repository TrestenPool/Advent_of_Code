FILENAME='input.txt'
inputFile = open(FILENAME, "r", encoding="utf-8")

lines = inputFile.readlines()

elf_calories_array = []
curr_calorie_sum = 0

for line in lines:
  # the line is empty
  if line in ['\n', '\r', '\r\n']:
    elf_calories_array.append(curr_calorie_sum)
    curr_calorie_sum = 0
    continue
  else:
    curr_calorie_sum += int(line)
  
# Question 1
print(f"elf carrying the most calories = {max(elf_calories_array)}" )

# Question 2
elf_calories_array.sort(reverse=True)
top_3_elves_sum = sum(elf_calories_array[:3])
print(f"The top 3 elves carrying {top_3_elves_sum}")

# close the file
inputFile.close()