# Ben Zuke's Solution
## Validation Process
1. I approached with random and ensured that the validation was working
2. I implemented a simple checker that would take the valid move that occured most often.

## Best move approach
1. I then tried to implement a more complex algo that would weigh both the number of occurences and the tiles that would be flipped by each move
2. After this I tried to apply foresight looking at the possible value for opponent.

# Python 3 Starter
Disclaimer: developed with Python 3.7.0, tested with Python 2.7.10 - not guaranteed to work with other versions

## Instructions
To run the client, run: `python client.py [optional port] [optional hostname]`

To run all tests, run `python -m unittest`
To run all tests in "test.py" tests, run `python -m unittest test`
To run the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove`
To run the test_get_move_returns_a_valid_move test case in the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove.test_get_move_returns_a_valid_move`

## Recommended Software
* Python 3.7.0
* [Pyenv](https://github.com/pyenv/pyenv)
