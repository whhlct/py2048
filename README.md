# py2048: Automating 2048 with Expectimax Algorithm

Welcome to the `py2048` repository! This project uses the Expectimax algorithm to implement an Artificial Intelligence player for the popular game [2048](https://play2048.co/). The purpose of this project is to demonstrate how we can apply the principles of AI and decision-making algorithms to automate gameplay in grid-based combinatorial games such as 2048.

## About Expectimax Algorithm
The Expectimax Algorithm is a decision-making algorithm used in situations involving uncertainty. It is based on the Minimax algorithm, but instead of an opponent minimizing the utility, the opponent is represented by the weighted average utility of possible random outcomes. It's very much suitable for AI in gaming because in games like 2048, the next tile's location and value are uncertain and based on certain pre-defined probabilities.

## Implementation?
The AI works by simulating all possible game states for a certain depth, calculating the board's score, and choosing the move that gives the highest expected score as calculated by the expectimax algorithm.

## Installation

To get the code running on your system, follow the below instructions:

Pre-requisites:
- [Python 3](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/install/)
- [Numba](https://numba.pydata.org/)
- [Pynput](https://pypi.org/project/pynput/)

To launch the game, execute the following command:

```
python main.py
```

This will start the game in automatic mode with Expectimax AI. After each game is completed, the final state will be saved as a .csv file in games/

If you want to play manually using WASD keys, run the program using the `-p` flag:

```
python main.py -p
```

## License
This project is licensed under the GPL-3.0 License - see the [LICENSE.md](https://github.com/whhlct/py2048/blob/master/LICENSE.md) file for more details.