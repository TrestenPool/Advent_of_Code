# FILENAME='testInput.txt'
FILENAME='input.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line
lines = [line for line in lines if line != '']

result_input = list(map(int,lines[0].split(':')[1].strip().split(' ')))
result = []
for i in range(len(result_input)):
  if i % 2 == 0:
    result += list(range(result_input[i], result_input[i]+result_input[i+1]))
  else:
    continue

processing = [(num,idx) for idx,num in enumerate(result)]

print('made it')
# for idx,line in enumerate(lines):
#   print(idx)

#   # initial row
#   if idx == 0:
#     continue
  
#   # header row
#   if ':' in line:
#     # reset the processing 
#     processing = [(num,idx) for idx,num in enumerate(result)]
#     continue
  

#   # we have already mapped all of our inputs, go to the next line
#   if len(processing) == 0:
#     continue
  
#   # parse line
#   [dst, src, range_len] = list(map(int, line.strip().split(' ')))

#   # get the difference between the two
#   difference = dst-src

#   for idx,(num,result_idx) in enumerate(processing):
#     if num in range(src, src+range_len):
#       result[result_idx] += difference
#       processing[idx] = True
  
#   processing = [x for x in processing if x != True]

# print(min(result))
