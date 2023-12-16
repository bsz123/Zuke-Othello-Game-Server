import unittest
import client

class TestGetMove(unittest.TestCase):
  def test_get_move_returns_a_valid_move(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(client.get_move(1, board), [5, 3])

  def test_get_move_returns_a_valid_move_2(self):
    board = [[1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 2, 1, 1, 1, 1, 1],
             [1, 1, 2, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 2, 1, 1, 2],
             [1, 1, 1, 1, 1, 1, 1, 2],
             [1, 1, 1, 2, 2, 1, 1, 2],
             [1, 1, 1, 1, 1, 2, 1, 1],
             [0, 0, 2, 0, 2, 2, 2, 0]]

    move = client.get_move(1, board)
    print("Calculated move:", move) # Should be [2, 7]

    # Ensure that the move is valid
    self.assertTrue(client.is_valid_move(1, board, move[0], move[1]))

class TestPrepareResponse(unittest.TestCase):
  def test_prepare_response_returns_a_valid_response(self):
    self.assertEqual(client.prepare_response([5, 3]), b'[5, 3]\n')

if __name__ == '__main__':
  unittest.main()