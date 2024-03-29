#!/usr/bin/python

import sys
import json
import socket

def is_valid_position(i, j):
  return 0 <= i < 8 and 0 <= j < 8

'''
Goes over moves that we know are valid and returns the one that will flip the most pieces
'''
def move_value(player, board, row, col):
  opponent = 1 if player == 2 else 2
  value = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if is_valid_position(row + i, col + j) == False:
        continue
      if board[row + i][col + j] == opponent:
        dir = [i, j]
        i = row + i
        j = col + j
        while True:
          i += dir[0]
          j += dir[1]
          if is_valid_position(i, j) == False:
            break
          if board[i][j] == player:
            value += 1
            break
          if board[i][j] == 0:
            break
          else:
            pass
  return value

def is_valid_move(player, board, row, col):
  # find only the squares that are the opposite color surrounding the current square
  # if there are no opposite color squares, return false
  opponent_squares = []
  opponent = 1 if player == 2 else 2

  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if is_valid_position(row + i, col + j) == False:
        continue
      if board[row + i][col + j] == opponent:
        dir = [i, j]
        opponent_squares.append([row + i, col + j, dir])

  if len(opponent_squares) == 0:
    return False

  for square in opponent_squares:
    dir = square[2]
    i = square[0]
    j = square[1]
    while True:
      i += dir[0]
      j += dir[1]
      if is_valid_position(i, j) == False:
        break
      if board[i][j] == player:
        return True
      if board[i][j] == 0:
        break
      else:
        pass # if an opponent square is found algo can keep going!

  return False

def simulate_move(player, board, row, col):
  # Simulate opponent's move and return the resulting board
  opponent = 1 if player == 2 else 2
  temp_board = [row[:] for row in board]
  temp_board[row][col] = opponent
  return temp_board

def evaluate_move(player, board, row, col):
  # Evaluate the desirability of a move based on foresight

  opponent = 1 if player == 2 else 2

  opponent_moves = []
  for i in range(8):
    for j in range(8):
      if board[i][j] == 0 and is_valid_move(opponent, board, i, j):
        opponent_moves.append(move_value(opponent, simulate_move(opponent, board, i, j), i, j))

  if opponent_moves:
    # Average opponent move value
    average_opponent_move_value = sum(opponent_moves) / len(opponent_moves)
    return move_value(player, board, row, col) - average_opponent_move_value
  else:
    return move_value(player, board, row, col)

def find_valid_move(player, board):
  valid_moves = {}
  opponent_squares = 0
  player_squares = 0
  for row in range(8):
    for col in range(8):
      if board[row][col] == 0:
        if is_valid_move(player, board, row, col):
          val = evaluate_move(player, board, row, col)
          move_key = (row, col)
          if move_key in valid_moves:
            valid_moves[move_key] = [valid_moves[0] + 1, valid_moves[move_key][1] + val]
          else:
            valid_moves[move_key] = [0, val]
        elif player_squares + opponent_squares == 63: #Edge case last move
          return [row, col]
      elif board[row][col] == player:
        player_squares += 1
      else:
        opponent_squares += 1

  if valid_moves:
    # Sort by number of opponent pieces flipped and by number of times move appeared in valid_moves
    sorted_moves = sorted(valid_moves.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
    best_move = sorted_moves[0][0]

    return list(best_move)
  else:
    return [-1, -1]

def get_move(player, board):
  return find_valid_move(player, board)


def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print(player, maxTurnTime, board)

      move = get_move(player, board)
      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
