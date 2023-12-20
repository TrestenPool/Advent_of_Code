# test input
FILENAME='partOneTestInput.txt'

# real input
# FILENAME='partOneInput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = lines_w_newline
# lines = [line.strip() for line in lines_w_newline] # remove the new line

'''
1 2 3
4 * 5
6 7 8

returns true if a symbol was found, false if one was not found
'''
def findSymbol(r, c):
  symbol_found = False
  
  # check 1
  if r > 0 and c > 0:
    char_to_check = G[r-1][c-1]
    # we found a character
    if char_to_check not in characters:
      symbol_found = True
  
  # check 2
  if r > 0:
    char_to_check = G[r-1][c]
    if char_to_check not in characters:
      symbol_found = True

  # check 3
  if r > 0 and c < len(G[r])-1:
    char_to_check = G[r-1][c+1]
    if char_to_check not in characters:
      symbol_found = True
  
  # check 4
  if c > 0:
    char_to_check = G[r][c-1]
    if char_to_check not in characters:
      symbol_found = True

  # check 5
  if c < len(G[r])-1:
    char_to_check = G[r][c+1]
    if char_to_check not in characters:
      symbol_found = True
  
  #  check 6
  if r < len(G)-1 and c > 0:
    char_to_check = G[r+1][c-1]
    if char_to_check not in characters:
      symbol_found = True
  
  # check 7
  if r < len(G)-1:
    char_to_check = G[r+1][c]
    if char_to_check not in characters:
      symbol_found = True
  
  # check 8
  if r < len(G)-1 and c < len(G[r])-1:
    char_to_check = G[r+1][c+1]
    if char_to_check not in characters:
      symbol_found = True

  return symbol_found

# grid
G = [[c for c in line] for line in lines]

print(G)
exit

# visted array
# visited = [[False]*len(lines[x]) for x in range(len(lines))]

characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\n']

curr_number = None
symbol_found = False

final_sum = 0

for r in range(len(G)):
  for c in range(len(G[r])):

    if G[r][c].isnumeric():
      if curr_number == None:
        curr_number = G[r][c]
        symbol_found = False
      else:
        curr_number += G[r][c]
      
      if symbol_found == False:
        symbol_found = findSymbol(r, c)

    else:
      if curr_number != None:
        # add to the sum if the symbol was found
        if symbol_found == True:
          curr_number = int(curr_number)
          final_sum += curr_number
        curr_number = None
        symbol_found = False

print(final_sum)
      
