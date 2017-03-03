#!/usr/bin/python
from random import random
from board import Board
import sys
from math import exp
import copy
#   hints are in the form of ((columns: (1), (1,2), ...), (rows: (1), ...))
class Problem:
    def __init__(self, nonogram):
        self.dimension = nonogram.n
        self.variables = [[1 if random() > 0.5 else 0 for i in range(self.dimension)] for j in range(self.dimension)]
        self.domain = (0, 1)
        self.constraints = nonogram.hints

        
def costFunc(currBoard, constraints):
    cost = 0
    dimension = len(currBoard)
    row_inBlack = [False for i in range(dimension)]
    col_inBlack = [False for i in range(dimension)]
    #row_sum = 0
    #col_sum = 0
    #local_constraints = constraints[:]
    row_constraint = []
    for i in constraints[1]:
        row_constraint.append(list(i))
    col_constraint = []
    for i in constraints[0]:
        col_constraint.append(list(i))
    #print constraints
    #print "row", row_constraint
    #print "col", col_constraint

    for i in range(dimension):
        for j in range(dimension):
            

            if currBoard[i][j] == 1:
                if len(col_constraint[j]) == 0 or len(row_constraint[i]) == 0:
                    if len(col_constraint[j]) == 0:
                        cost += 1
                    if len(row_constraint[i]) == 0:
                        cost += 1
                    continue
                row_constraint[i][0] -= 1
                col_constraint[j][0] -= 1
                if row_constraint[i][0] < 0:
                    cost += 1
                if col_constraint[j][0] < 0:
                    cost += 1
                    
                if not row_inBlack[i]:
                    row_inBlack[i] = True
                if not col_inBlack[j]:
                    col_inBlack[j] = True

            else:
                if row_inBlack[i]:
                    if len(row_constraint[i]) > 0:
                        if row_constraint[i][0] > 0:
                            cost += 1
                            row_constraint[i][0] -= 1
                        else:
                            del row_constraint[i][0]

                    row_inBlack[i] = False
                
                if col_inBlack[j]:
                    if len(col_constraint[j]) > 0:
                        if col_constraint[j][0] > 0:
                            cost += 1
                            col_constraint[j][0] -= 1
                        else:
                            del col_constraint[j][0]
                    col_inBlack[j] = False

            '''print "row:", row_constraint
            print "col:", col_constraint
            print cost
            print "\n"'''
        if len(row_constraint[i]) > 0:
            for item in row_constraint[i]:
                if item > 0:
                    cost += item
    for i in range(dimension):
        if len(col_constraint[i]) > 0:
            for item in col_constraint[i]:
                if item > 0:
                    cost += item 
            #check if the constraints has been violateed
    #print "row", row_constraint
    #print "col", col_constraint

    return cost

def prob(cost_curr, cost_successor, temperature):
    '''print "temperature", temperature
    print "cost of next:", cost_successor
    print "cost of curr:", cost_curr
    print "difference:", cost_successor - cost_curr
    print "prob of moving", exp(-(cost_successor - cost_curr)/temperature)'''
    return exp(-(cost_successor - cost_curr)/temperature)\
    if cost_curr < cost_successor else 1


def anneal(problem):
    currState = problem.variables
    constraints = problem.constraints
    dimension = problem.dimension

    k_max = 10000

    for k in range(k_max):
        '''new_board = Board(4, constraints)
        for i in range(len(currState)):
            for j in range(len(currState)):
                if currState[i][j] == 1:
                    new_board.modify(i, j)
        print new_board
        print costFunc(currState, constraints)'''

        t = temperature(float(k)/k_max)

        rand_row = int(dimension * random())
        rand_col = int(dimension * random())
        nextState = copy.deepcopy(currState)
        nextState[rand_row][rand_col] = 1 if currState[rand_row][rand_col] == 0 else 0
        if costFunc(nextState, constraints) == 0:
            return nextState

        probability = random()
        #print "random prob:", probability
        cost_curr = costFunc(currState, constraints)
        #print "cost_curr:", cost_curr
        cost_next = costFunc(nextState, constraints)
        #print "cost_next:", cost_next
        if prob(cost_curr, cost_next, t) >= probability:
            currState = nextState
    #print costFunc(currState, constraints)
    #print currState
    return currState

def temperature(alpha):
    #print "alpha", alpha
    return 1.0 - alpha

if __name__ == "__main__":
    test_hints = (([1, 3],[3],[1],[3],[2]), ([1, 3],[2],[2, 1],[2],[2]))
    test_board = Board(5, test_hints)
    test_problem = Problem(test_board)
    test_solution = anneal(test_problem)
    if test_solution == None:
        print "No satisfiable solution"
    else:
        for i in range(test_problem.dimension):
            for j in range(test_problem.dimension):
                if test_solution[i][j] == 1:
                    test_board.modify(i, j)

        print test_board

