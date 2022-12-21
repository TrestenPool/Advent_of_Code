# FILENAME = 'Day9/testInput.txt'
FILENAME = 'Day9/input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()
lines = [x.strip().split() for x in lines]

# For Question 1 
clock_cycles_to_check = [20, 60] + list(range(100, 1000, 40))
signal_strength_array = []

# For Question 2
crt_length = 6
crt_width = 40
crt_monitor = [['?' for x in range(crt_width)] for i in range(crt_length)]

clock_cycles = 1
register_X = 1
i = 0
while True:
  if clock_cycles in clock_cycles_to_check:
    signal_strength_array.append(register_X * clock_cycles)
  
  row_idx = ( (clock_cycles-1) // 40)
  col_idx = ( (clock_cycles-1) % 40)

  left_pix = register_X-1
  mid_pix = register_X
  right_pix = register_X+1
  # if clock_cycles-1 == left_pix or clock_cycles-1 == mid_pix or clock_cycles-1 == right_pix:
  if col_idx == left_pix or col_idx == mid_pix or col_idx == right_pix:
    crt_monitor[row_idx][col_idx] = '#'
  else:
    crt_monitor[row_idx][col_idx] = '.'

  line = lines[i]
  if line[0] == 'noop':
    clock_cycles += 1
  elif line[0] == 'addx':
    if len(line) != 3:
      clock_cycles += 1
      line.append('1')
      continue
    else:
      clock_cycles += 1
      register_X += int(line[1])
  i += 1

  if i == len(lines):
    break

print(f"Question 1: {sum(signal_strength_array)}", end="\n\n")

print(f"Question 1: ")
for i in crt_monitor:
  print(''.join(i))

# close the file
inputFile.close()
