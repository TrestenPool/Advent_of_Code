FILENAME = 'input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()

count = 0
for idx, line in enumerate(lines):
  flag = False
  line = line.strip()
  pair1,pair2 = line.split(',')
  pair1 = pair1.split('-')
  pair2 = pair2.split('-')
  pair1[0],pair1[1] = int(pair1[0]), int(pair1[1])
  pair2[0],pair2[1] = int(pair2[0]), int(pair2[1])

  if pair1[0] < pair2[0]:
    smallest_pair, other_pair = pair1, pair2
  elif pair1[0] > pair2[0]:
    smallest_pair, other_pair = pair2, pair1
  else: 
    if pair1[1] >= pair2[1]:
      smallest_pair, other_pair = pair1, pair2
    else:
      smallest_pair, other_pair = pair2, pair1
      flag = True
    
  # if other_pair[0] <= smallest_pair[1] or other_pair[1] <= smallest_pair[1]:
  #   count += 1
  if other_pair[0] <= smallest_pair[1]:
    count += 1
  
print(count)

# close the file
inputFile.close()