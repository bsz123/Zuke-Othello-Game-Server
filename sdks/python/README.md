# Ben Zuke's Solution
## Validation Process
1. I approached with random and ensured that the validation was working
2. I implemented a simple checker that would take the valid move that occured most often.

## Best move approach
1. I then tried to implement a more complex algo that would weigh both the number of occurences and the tiles that would be flipped by each move
   - In testing for this I found that in 17 games my bot won 11-6
2. After this I tried to apply foresight looking at the possible value for opponent.
   - Reusing the value applied to the previous moves, and then subtracting the average value of the opponent's possible simulated moves allowed me to get a 75% win rate
   - 15 wins, 1 tie, 4 losses in 20 games tested shows a clear improvement

## References and possible future improvements
1. here is a report on othello strategy, I did not implement the exact pruning algorithm but I was inspried by it. https://zzutk.github.io/docs/reports/2014.04%20-%20Searching%20Algorithms%20in%20Playing%20Othello.pdf
2. Adding more and more foresight would continue to improve the bot, but given that the bot moves are random it is not necessary. In a game against another bot it would be necessary. (Assuming that my bot won't be competing against others XD)


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
