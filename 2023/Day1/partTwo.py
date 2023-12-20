# file input
FILENAME='input.txt'
inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line

digital_values = [
  ('zero', 0),
  ('one', 1),
  ('two', 2),
  ('three', 3),
  ('four', 4),
  ('five', 5),
  ('six', 6),
  ('seven', 7),
  ('eight', 8),
  ('nine', 9),
]

# our final answer
sum_of_all_lines = 0

# go through every line in the file
for line in lines:
  first_num = None
  second_num = None

  # go through every character in the string
  for idx,char in enumerate(line):
    
    # character is a number
    if char.isnumeric():
      if first_num is None:
        first_num = char
        second_num = char
      else:
        second_num = char
    
    # character is a character
    else:
      for (char_digit, value) in digital_values:
        if char_digit == line[idx:idx+len(char_digit)]:
          if first_num is None:
            first_num = str(value)
            second_num = str(value)
          else:
            second_num = str(value)
  
  sum_of_all_lines += int(first_num + second_num)

print(sum_of_all_lines)



    


        








    

