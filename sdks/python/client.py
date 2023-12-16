#!/usr/bin/python

import sys
import json
import socket


# Boolean that determines if move is valid
def is_valid_move(player, board, x, y):
  if player == 1:
    opponent = 2
  else:
    opponent = 1

  # Write this algorithm but in python
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0:
        continue
      if x + dx < 0 or x + dx > 7 or y + dy < 0 or y + dy > 7:
        continue
      if board[y + dy][x + dx] != opponent:
        continue
      i = 2
      while i <= 7:
        if x + i * dx < 0 or x + i * dx > 7 or y + i * dy < 0 or y + i * dy > 7:
          break
        if board[y + i * dy][x + i * dx] == 0:
          break
        if board[y + i * dy][x + i * dx] == player:
          return True
        i += 1
  return False


def find_valid_move(player, board):
  # Find valid othello moves for player X
  valid_moves = []
  for i in range(8):
    for j in range(8):
      if board[i][j] == 0:
        # Check if move is valid
        if is_valid_move(player, board, i, j):
          valid_moves.append([i, j])
  return valid_moves[0]

def get_move(player, board):
  # TODO determine valid moves
  # TODO determine best move
  #return [5, 3]
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
