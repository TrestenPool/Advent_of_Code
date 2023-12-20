# input file
# FILENAME='partOneTestInput.txt'
FILENAME='partOneInput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line

result = 0

card_copies = [1 for x in range(len(lines))]

finished = {}

for idx,line in enumerate(lines):
  winning_numbers = line.split(':')[1].split('|')[0].strip().split(' ')
  winning_numbers = [x for x in winning_numbers if x != '']
  sample_numbers = line.split(':')[1].split('|')[1].strip().split(' ')
  sample_numbers = [x for x in sample_numbers if x != '']
  
  while card_copies[idx] > 0:
    result += 1
    print(idx)

    card_score = 0
    if idx in finished:
      card_score = finished[idx]

    else:
      for win_num in winning_numbers:
        if win_num in sample_numbers:
          card_score += 1
      finished[idx] = card_score

    
    for x in range(idx+1, idx+1+card_score):
      card_copies[x] += 1
    
    card_copies[idx] -= 1

print(result)