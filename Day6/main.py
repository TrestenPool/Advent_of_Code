FILENAME='input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()
line = lines[0]
line = line.strip()

buffer = list(line[:3])
num_times = 0
main_buffer = []
for idx,character in enumerate(line, start=1):
  buffer.append(character)
  if len(set(buffer)) == 4:
    num_times = idx
    break
  else:
    buffer.pop(0)

  
print("Question 1...")
print(num_times)
print(buffer)

buffer = list(line[:13])
num_times = 0
main_buffer = []
for idx,character in enumerate(line, start=1):
  buffer.append(character)
  if len(set(buffer)) == 14:
    num_times = idx
    break
  else:
    buffer.pop(0)
  
print("Question 2...")
print(num_times)
print(buffer)


# close the file
inputFile.close()