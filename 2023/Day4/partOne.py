# input file
# FILENAME='partOneTestInput.txt'
FILENAME='partOneInput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line

result = 0

for line in lines:
  winning_numbers = line.split(':')[1].split('|')[0].strip().split(' ')
  winning_numbers = [x for x in winning_numbers if x != '']
  sample_numbers = line.split(':')[1].split('|')[1].strip().split(' ')
  sample_numbers = [x for x in sample_numbers if x != '']

  card_score = 0

  for win_num in winning_numbers:
    if win_num in sample_numbers:
      if card_score == 0:
        card_score = 1
      else:
        card_score *= 2
  
  result += card_score


print(result)

  
  
  