# test input
# FILENAME='partOneTestInput.txt'

# real input
FILENAME='partOneInput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = lines_w_newline

'''
1 2 3
4 * 5
6 7 8

returns true if a symbol was found, false if one was not found
'''
def findSymbol(r, c):
  # check 1
  if r > 0 and c > 0:
    char_to_check = G[r-1][c-1]
    # we found a character
    if char_to_check == '*':
      return (r-1, c-1)
  
  # check 2
  if r > 0:
    char_to_check = G[r-1][c]
    if char_to_check == '*':
      return (r-1, c)

  # check 3
  if r > 0 and c < len(G[r])-1:
    char_to_check = G[r-1][c+1]
    if char_to_check == '*':
      return (r-1, c+1)
  
  # check 4
  if c > 0:
    char_to_check = G[r][c-1]
    if char_to_check == '*':
      return (r, c-1)

  # check 5
  if c < len(G[r])-1:
    char_to_check = G[r][c+1]
    if char_to_check == '*':
      return (r, c+1)
  
  #  check 6
  if r < len(G)-1 and c > 0:
    char_to_check = G[r+1][c-1]
    if char_to_check == '*':
      return (r+1, c-1)
  
  # check 7
  if r < len(G)-1:
    char_to_check = G[r+1][c]
    if char_to_check == '*':
      return (r+1, c)
  
  # check 8
  if r < len(G)-1 and c < len(G[r])-1:
    char_to_check = G[r+1][c+1]
    if char_to_check == '*':
      return (r+1, c+1)

  return None

# grid
G = [[c for c in line] for line in lines]

characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\n']

gears = {
  # (r,c): [num1, num2]
  # (0,1): [123, 456]
}

curr_number = None
symbol_coord = None

for r in range(len(G)):
  for c in range(len(G[r])):

    if G[r][c].isnumeric():
      if curr_number == None:
        curr_number = G[r][c]
        symbol_coord = None
      else:
        curr_number += G[r][c]
      
      if symbol_coord == None:
        symbol_coord = findSymbol(r, c)

    else:
      if curr_number != None:
        if symbol_coord != None:
          curr_number = int(curr_number)
          if symbol_coord in gears.keys():
            gears[symbol_coord].append(curr_number)
          else:
            gears[symbol_coord] = [curr_number]
        curr_number = None
        symbol_coord = False



final_sum = 0

for key in gears:
  if len(gears[key]) == 2:
    final_sum += gears[key][0] * gears[key][1]

print(final_sum)

      
