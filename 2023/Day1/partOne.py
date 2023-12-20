FILENAME='input.txt'
inputFile = open(FILENAME, "r", encoding="utf-8")
lines = inputFile.readlines()
sum_of_all_lines = 0

for line in lines:
  sum_of_curr_line = 0
  first_num = None
  second_num = None

  for char in line:
    if char.isnumeric():
      if first_num is None:
        first_num = char
        second_num = char
      else:
        second_num = char
  
  sum_of_all_lines += int(first_num + second_num)

print(sum_of_all_lines)


      


