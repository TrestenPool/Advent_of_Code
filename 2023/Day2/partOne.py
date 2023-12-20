# test input
FILENAME='input.txt'

# real input
# FILENAME='testinput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line

# rules
rules = {
  'red': 12,
  'green': 13,
  'blue': 14
}

possible_games_id_sums = 0

for line in lines:
  print(line)
  game_id = int(line.split(':')[0].split(' ')[1])
  game_line = line.split(':')[1:][0]
  subsets = game_line.split(';')

  possible_game = True
  
  for subset in subsets:
    entries = [x.strip() for x in subset.split(',')]

    for entry in entries:
      [quanity,color] = entry.split(' ')

      # invalid game
      if int(quanity) > rules[color]:
        possible_game = False
        break
    
    if possible_game == False:
      break
  
  if possible_game == True:
    possible_games_id_sums += game_id


print(possible_games_id_sums)
    

      


      

