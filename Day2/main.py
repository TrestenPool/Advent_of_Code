####### Describing the input.txt ###########

### Legend for 1st column ###
# A = Rock
# B = Paper
# C = Scissors

# the first column is what your opponent is going to play
# the second column is what I should play to win

### Legend for 2nd column ###
# X = Rock
# Y = Paper
# Z = Scissors

# Score for a single round is the ( shape selected + outcome )

### shape selected legend ###
# Rock = 1
# Paper = 2
# Scissors = 3

### outcome legend
# loss = 0
# draw = 3
# win = 6

FILENAME='input.txt'
inputFile = open(FILENAME, "r", encoding="utf-8")
lines = inputFile.readlines()

opponent = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}
ourPlayer = {
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}

shape_selection = {
  'rock':   1,
  'paper':  2,
  'scissors': 3
}

# opponent, ourPlayer
# ex. win = (scissors, rock)
# ex. loss= (rock, scissors)
# 0 = won
# 1 = loss
# 2 = draw
outcomes = [
  # Won
  [ ('scissors', 'rock'), ('rock', 'paper'), ('paper', 'scissors') ],
  # Loss
  [ ('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper') ],
  # Draw
  [('rock', 'rock'), ('paper', 'paper'), ('scissors', 'scissors') ]
]

def simulate_game(opp, ourP):
  curr_game = (opp, ourP)
  index = 0
  for outcome_array in outcomes:
    if curr_game in outcome_array:
      if index == 0:
        return 6
      elif index == 1:
        return 0
      elif index == 2:
        return 3
    index += 1
  return -1

######## Question 1 ######## 
# total_score = 0
# for idx, line in enumerate(lines):
#   line_array = [*line.strip().replace(" ", "")]
#   game_result = simulate_game(opponent.get(line_array[0]), ourPlayer.get(line_array[1]))
#   shape_number = shape_selection.get(ourPlayer.get(line_array[1]))
#   total_score += (game_result + shape_number)
#   # print(f"{opponent.get(line_array[0])} {ourPlayer.get(line_array[1])}, result = {game_result}")

# print(total_score)

######## Question 2 ######## 
# X = I need to lose
# Y = I need to end in Draw
# Z = I need to win

def get_our_play(other_elf, our_elf):
  if our_elf == 'X':  # We need to lose
    index = 1
  elif our_elf == 'Y':# we need to draw
    index = 2
  elif our_elf == 'Z':# We need to win
    index = 0
  
  array_to_check = outcomes[index]
  for x,y in array_to_check:
    if x == other_elf:
      return y

total_score = 0
for line in lines:
  line_array = [*line.strip().replace(" ", "")]
  our_play = get_our_play(opponent.get(line_array[0]), line_array[1])

  if line_array[1] == 'X':
    result_score = 0
  elif line_array[1] == 'Y':
    result_score = 3
  elif line_array[1] == 'Z':
    result_score = 6

  total_score += shape_selection.get(our_play) + result_score
  
print(total_score)
  
