# nonogram-solver
* Requirement: python 2
This is a Nonogram solver using simulated annealing
1. What is a Nongram: https://en.wikipedia.org/wiki/Nonogram
2. What is Simulated Annealing:
  When using local search optimization, the agent is likely to be stuck in a local maximum of reward function. Simulated Annealing can help the agent get out of local maxima by allowing the agent to make a bad move with a certain probability.
  For more information about Simulated Annealing: https://en.wikipedia.org/wiki/Simulated_annealing
* To solve a Nonogram, run:
~~~
python solve.py
~~~
The script actually comes with a test nonogram that was hard-coded, it looks like:
|     |1    |2    |3    |4    |5    |
|:___:|:___:|:___:|:___:|:___:|:___:|
|1    |#    |     |#    |#    |#    |
|2    |     |     |     |#    |#    |
|3    |#    |#    |     |#    |     |
|4    |#    |#    |     |     |     |
|5    |#    |#    |     |     |     |      
