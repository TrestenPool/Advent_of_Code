FILENAME='testInput.txt'
# FILENAME='input.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line
lines = [line for line in lines if line != '']

for line in lines:
  print(line)