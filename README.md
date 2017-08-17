# nonogram-solver
* Requirement: python 2
This is a Nonogram solver using simulated annealing

**What is a Nongram**
: https://en.wikipedia.org/wiki/Nonogram
  
**What is Simulated Annealing**
: When using local search optimization, the agent is likely to be stuck in a local maximum of reward function. Simulated Annealing can help the agent get out of local maxima by allowing the agent to make a bad move with a certain probability.
For more information about Simulated Annealing: https://en.wikipedia.org/wiki/Simulated_annealing
* To solve a Nonogram, run:
~~~
python solve.py > FILENAME
~~~
You may want to output to a file like so because the output will be quite long.
The script actually comes with a test nonogram that was hard-coded, it looks like:

| board | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| **1** | 1 | 0 | 1 | 1 | 1 |
| **2** | 0 | 0 | 0 | 1 | 1 |
| **3** | 1 | 1 | 0 | 1 | 0 |
| **4** | 1 | 1 | 0 | 0 | 0 |
| **5** | 1 | 1 | 0 | 0 | 0 |      

Where 1's represent black pixels and 0's represent white pixels.

Feel free to try more test cases yourself!
