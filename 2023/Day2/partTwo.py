# real input
FILENAME='partTwoInput.txt'

# test input
# FILENAME='partTwoTestInput.txt'

inputFile = open(FILENAME, "r", encoding="utf-8")
lines_w_newline = inputFile.readlines()
lines = [line.strip() for line in lines_w_newline] # remove the new line

# rules
rules = {
  'red': 12,
  'green': 13,
  'blue': 14
}

sum_of_power_sets = 0

for line in lines:
  game_id = int(line.split(':')[0].split(' ')[1])
  subsets_single_game = line.split(':')[1:][0].split(';')

  maxes = {
    'red': 1,
    'green': 1,
    'blue': 1
  }


  # go through all of the subsets for a single game
  for subset in subsets_single_game:
    entries = [x.strip() for x in subset.split(',')]

    for entry in entries:
      [quanity, color] = entry.split(' ')
      quanity = int(quanity)

      if quanity > maxes[color]:
        maxes[color] = quanity
  
  
  game_power_set = maxes['red'] * maxes['green'] * maxes['blue']
  sum_of_power_sets += game_power_set
  # print(game_id, game_power_set)


print(sum_of_power_sets)
    