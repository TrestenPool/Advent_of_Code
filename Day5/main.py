from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
FILENAME = 'input.txt'
inputFile = open(FILENAME, 'r')
lines = inputFile.readlines()

letter_index = [x for x in range(1, 34, 4)]
crates_array = [ [] for i in range(9)]

def populate_crates(line_array):
  for crate_number, letter_idx in enumerate(letter_index):
    if line_array[letter_idx] != ' ':
      crates_array[crate_number].append(line_array[letter_idx])

def move_crates(num_crates, src, dst):
  dst -= 1
  src -= 1
  crates_to_be_moved = crates_array[src][:num_crates]
  crates_array[src] = crates_array[src][num_crates:]
  crates_array[dst] = crates_to_be_moved + crates_array[dst]
  print_crates_array(num_crates, dst+1, src+1)

def print_crates_array(num_crates=None, dst=None, src=None):
  if num_crates == None:
    for idx, arr in enumerate(crates_array, start=1):
      print(f"{idx}: {arr}")
    print(end="\n\n")
  else:
    dst -= 1
    src -= 1
    for idx, arr in enumerate(crates_array, start=1):
      if idx-1 == dst:
        print(f"{Fore.YELLOW}{idx}: {Fore.RED}{arr[:num_crates]},{Fore.RESET}{arr[num_crates:]}")
      elif idx-1 == src:
        print(f"{Fore.YELLOW}{idx}{Fore.RESET}: {arr}")
      else:
        print(f"{idx}: {arr}")
    print(end="\n\n")

populate = True
flag = True
for idx,line in enumerate(lines):
  if line in ['\n', '\r', '\r\n']:
    populate = False
    print_crates_array()
    continue
  if flag and '1' in line:
    flag = False
    continue

  if populate:
    line_array = [*line]
    populate_crates(line_array)
  else:
    line = line.strip()
    line_array = line.split(' ')
    print(line)
    move_crates(int(line_array[1]), int(line_array[3]), int(line_array[5]))
  
top_array = [x[0] for x in crates_array]
top_array = ''.join(top_array)
print(top_array)

# Close the file
inputFile.close()