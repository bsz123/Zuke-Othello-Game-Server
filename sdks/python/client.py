#!/usr/bin/python

import sys
import json
import socket

def is_valid_move(player, board, row, col):
  # find only the squares that are the opposite color surrounding the current square
  # if there are no opposite color squares, return false
  opponent_squares = []
  opponent = 1 if player == 2 else 2

  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if row + i < 0 or row + i > 7 or col + j < 0 or col + j > 7:
        continue
      if board[row + i][col + j] == opponent:
        dir = [i, j]
        opponent_squares.append([row + i, col + j, dir])

  if len(opponent_squares) == 0:
    return False

  # for each of the squares, check if there is a player square in the same direction
  for square in opponent_squares:
    dir = square[2]
    i = square[0]
    j = square[1]
    while True:
      i += dir[0]
      j += dir[1]
      if i < 0 or i > 7 or j < 0 or j > 7:
        break
      if board[i][j] == player:
        print(opponent_squares)
        return True
      if board[i][j] == 0:
        break
      else:
        pass # Was originally breaking, but if an opponent square is found algo can keep going!

  return False

def find_valid_move(player, board):
  valid_moves = {}
  opponent_squares = 0
  player_squares = 0
  last_move = [-1, -1] #Holds last empty square
  for row in range(8):
    for col in range(8):
      if board[row][col] == 0:
        if is_valid_move(player, board, row, col):
          #return [row, col]
          #valid_moves.append([row, col])
          move_key = (row, col)
          if move_key in valid_moves:
            valid_moves[move_key] += 1
          else:
            valid_moves[move_key] = 1
        elif player_squares + opponent_squares == 63: #Edge case last move
          return [row, col]
        else:
          last_move = [row, col]
      elif board[row][col] == player:
        player_squares += 1
      else:
        opponent_squares += 1

  if valid_moves:
    best_move = max(valid_moves, key=valid_moves.get)
    return list(best_move)
  else:
    return last_move

def get_move(player, board):
  # TODO determine valid moves
  return find_valid_move(player, board)
  # TODO determine best move


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
