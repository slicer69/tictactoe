import sys
import random

NONE = 0
x_player = 1
o_player = 2
player_symbols = [ ' ', 'X', 'O' ]
board = []
width = 3
height = 3
squares = width * height;

# Draw the game on the screen
# Include any marks from players so far.
def draw_board(my_board):
   my_square = 0
   
   print("")
   for row in range(height):
      print(" ", end='')
      for column in range(width):
         print(my_board[my_square], end='')
         my_square += 1
         if column < width - 1:
            print("|", end='')
      print("")
      if row < height - 1:
         print(" - - -")
   print("")



# Get the human player's move. Make sure it does not
# overlap with another mark on the board.
# Return the position of the move in the range of 0-8.
def get_player_move(my_board):

   finished = False
   while not finished:
      answer = input("Enter your move [1-9]> ")
      if answer.isnumeric():
          target_square = int(answer)
          if target_square < 1 or target_square > 9:
             print("Please pick a square in the range of 1 to 9.\n")
          elif my_board[target_square - 1] != player_symbols[NONE]:
             print("This square is already taken.\n")
          else:
             finished = True
      else:
         print("Please try a single-digit number.")

      if not finished:
         draw_board(my_board)
 
   target_square -= 1
   return target_square


# This function picks the first empty square on a board from
# the provided list. The returned value is the value of the square
# in the range of 0 to 8.
# It should not be possible for a match not to be found, but
# if that is the case then -1 is returned.
def pick_grid_value(my_board, all_options):
    index = 0
    while index < len(all_options):
        target = all_options[index]
        if my_board[target] == player_symbols[NONE]:
           return target
        else:
           index += 1
    return -1

# Try to figure out where the computer controlled player should
# move. The target square needs to be empty.
# We return a square value in the range of 0 to 8.
def get_ai_move(my_board):
   all_possible_moves = []

   # First look to see if we can win the game with this move.
   # We know our player's value is "O" on the board, so
   # we will assign it a value of 7 and the other player's "X"
   # will be assigned a value of 1. Any of the eight lines
   # on the board adding up to exactly 4 means we should take
   # the empty square.
  
   # First check horizontal rows
   start = 0
   while start < squares:
      total = 0
      if my_board[start] == player_symbols[o_player]:
          total += 7
      elif my_board[start] == player_symbols[x_player]:
          total += 1
      if my_board[start + 1] == player_symbols[o_player]:
          total += 7
      elif my_board[start + 1] == player_symbols[x_player]:
          total += 1
      if my_board[start + 2] == player_symbols[o_player]:
          total += 7
      elif my_board[start + 2] == player_symbols[x_player]:
          total += 1
      if total == 14:
         all_possible_moves.append(start) 
         all_possible_moves.append(start + 1) 
         all_possible_moves.append(start + 2) 
         target_square = pick_grid_value(my_board, all_possible_moves)
         return target_square
      else:
         start += 3

   # Next check vertical options for a win
   start = 0
   while start < width:
      total = 0
      if my_board[start] == player_symbols[o_player]:
         total += 7
      elif my_board[start] == player_symbols[x_player]:
         total += 1
      if my_board[start + 3] == player_symbols[o_player]:
         total += 7
      elif my_board[start + 3] == player_symbols[x_player]:
         total += 1
      if my_board[start + 6] == player_symbols[o_player]:
         total += 7
      elif my_board[start + 6] == player_symbols[x_player]:
         total += 1
      if total == 14:
          all_possible_moves.append(start)
          all_possible_moves.append(start + 3)
          all_possible_moves.append(start + 6)
          target_square = pick_grid_value(my_board, all_possible_moves)
          return target_square
      else:
          start += 1

   # Third option, look for win on the diagionals.
   total = 0
   if my_board[0] == player_symbols[o_player]:
      total += 7
   elif my_board[0] == player_symbols[x_player]: 
      total += 1
   if my_board[4] == player_symbols[o_player]:
      total += 7
   elif my_board[4] == player_symbols[x_player]: 
      total += 1
   if my_board[8] == player_symbols[o_player]:
      total += 7
   elif my_board[8] == player_symbols[x_player]: 
      total += 1
   if total == 14:
       all_possible_moves.append(0)
       all_possible_moves.append(4)
       all_possible_moves.append(8)
       target_square = pick_grid_value(my_board, all_possible_moves)
       return target_square

   total = 0
   if my_board[2] == player_symbols[o_player]:
      total += 7
   elif my_board[2] == player_symbols[x_player]:
      total += 1
   if my_board[4] == player_symbols[o_player]:
      total += 7
   elif my_board[4] == player_symbols[x_player]:
      total += 1
   if my_board[6] == player_symbols[o_player]:
      total += 7
   elif my_board[6] == player_symbols[x_player]:
      total += 1
   if total == 14:
       all_possible_moves.append(2)
       all_possible_moves.append(4) 
       all_possible_moves.append(6)
       target_square = pick_grid_value(my_board, all_possible_moves)
       return target_square

   # At this point we cannot win. Maybe we should block?
   # Now we reverse our logic. Squares with an "X" will
   # be worth 7 and any O will be worth 1. When we find
   # any line with a total value of 14 that means the opponent
   # has two of three marks in the line. We should try to
   # block in the final square.

   # Check for block horizontally.
   start = 0
   while start < squares:
      total = 0
      if my_board[start] == player_symbols[x_player]:
          total += 7
      elif my_board[start] == player_symbols[o_player]:
          total += 1
      if my_board[start + 1] == player_symbols[x_player]:
          total += 7
      elif my_board[start + 1] == player_symbols[o_player]:
          total += 1
      if my_board[start + 2] == player_symbols[x_player]:
          total += 7
      elif my_board[start + 2] == player_symbols[o_player]:
          total += 1
      if total == 14:
         all_possible_moves.append(start)
         all_possible_moves.append(start + 1)
         all_possible_moves.append(start + 2)
         target_square = pick_grid_value(my_board, all_possible_moves)
         return target_square
      else:
         start += 3


   # Next check vertical options for a block
   start = 0
   while start < width:
      total = 0
      if my_board[start] == player_symbols[x_player]:
         total += 7
      elif my_board[start] == player_symbols[o_player]:
         total += 1
      if my_board[start + 3] == player_symbols[x_player]:
         total += 7
      elif my_board[start + 3] == player_symbols[o_player]:
         total += 1
      if my_board[start + 6] == player_symbols[x_player]:
         total += 7
      elif my_board[start + 6] == player_symbols[o_player]:
         total += 1
      if total == 14:
          all_possible_moves.append(start)
          all_possible_moves.append(start + 3)
          all_possible_moves.append(start + 6)
          target_square = pick_grid_value(my_board, all_possible_moves)
          return target_square
      else:
          start += 1

   # Third option, look for a block on the diagionals.
   total = 0
   if my_board[0] == player_symbols[x_player]:
      total += 7
   elif my_board[0] == player_symbols[o_player]:
      total += 1
   if my_board[4] == player_symbols[x_player]:
      total += 7
   elif my_board[4] == player_symbols[o_player]:
      total += 1
   if my_board[8] == player_symbols[x_player]:
      total += 7
   elif my_board[8] == player_symbols[o_player]:
      total += 1
   if total == 14:
       all_possible_moves.append(0)
       all_possible_moves.append(4)
       all_possible_moves.append(8)
       target_square = pick_grid_value(my_board, all_possible_moves)
       return target_square

   total = 0
   if my_board[2] == player_symbols[x_player]:
      total += 7
   elif my_board[2] == player_symbols[o_player]:
      total += 1
   if my_board[4] == player_symbols[x_player]:
      total += 7
   elif my_board[4] == player_symbols[o_player]:
      total += 1
   if my_board[6] == player_symbols[x_player]:
      total += 7
   elif my_board[6] == player_symbols[o_player]:
      total += 1
   if total == 14:
       all_possible_moves.append(2)
       all_possible_moves.append(4)
       all_possible_moves.append(6)
       target_square = pick_grid_value(my_board, all_possible_moves)
       return target_square


   # No impending losses to block, try taking the middle?
   if my_board[4] == player_symbols[NONE]:
      return 4

   # Middle is taken, try the corners?
   if my_board[0] == player_symbols[NONE] or my_board[2] == player_symbols[NONE] or my_board[6] == player_symbols[NONE] or my_board[8] == player_symbols[NONE]:
       all_possible_moves = [0, 2, 6, 8]
       random.shuffle(all_possible_moves)
       target_square = pick_grid_value(my_board, all_possible_moves)
       return target_square


   # Cannot find anything better to do, try selecting a random position.
   all_possible_moves.clear()
   for count in range(squares):
       all_possible_moves.append(count)
   random.shuffle(all_possible_moves)
   target_square = pick_grid_value(my_board, all_possible_moves)

   return target_square 


# Show the board and declare who won
def declare_winner(my_board, my_winner):
   print("")
   draw_board(my_board)
   print(my_winner)



# See if we have the player's symbol in any of
# the eight possible winning arrangements.
# Return True if found or False otherwise.
def check_for_win(my_board, player_number):
   found_winner = False
   my_symbol = player_symbols[player_number]
   
   # Check horizontally for wins
   start = 0
   while start < squares and found_winner == False:
        if my_board[start] == my_symbol and my_board[start + 1] == my_symbol and my_board[start + 2] == my_symbol:
               found_winner = True
        else:
           start += 3
        
   # Check vertically
   start = 0
   while start < width and found_winner == False:
        if my_board[start] == my_symbol and my_board[start + 3] == my_symbol and my_board[start + 6] == my_symbol:
              found_winner = True
        else:
           start += 1

   # Check diagonally
   if my_board[0] == my_symbol and my_board[4] == my_symbol and my_board[8] == my_symbol:
         found_winner = True

   if my_board[2] == my_symbol and my_board[4] == my_symbol and my_board[6] == my_symbol:
         found_winner = True

   return found_winner



def main():
   game_finished = False
   moves = 0
   target_square = 0
   found_win = False
   winner = "Tie"

   # Initialize board
   for square in range(squares):
       board.append(player_symbols[NONE])

   while game_finished == False:
      draw_board(board)
      target_square = get_player_move(board)
      board[target_square] = player_symbols[x_player]
      moves += 1
      found_win = check_for_win(board, x_player)

      if found_win:
         game_finished = True
         winner = "You win!"

      elif moves >= squares:
         game_finished = True

      else:
         # target_square = get_ai_move(board)
         draw_board(board)
         target_square = get_ai_move(board)
         board[target_square] = player_symbols[o_player]
         moves += 1
         found_win = check_for_win(board, o_player)
         if found_win:
            game_finished = True
            winner = "Computer player won!"

   # end of while game is not finished
   declare_winner(board, winner)
   sys.exit()

if __name__ == "__main__":
   main()

