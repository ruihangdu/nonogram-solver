from solve import costFunc

constraints = (([1],[1],[1]), ([1],[1],[1]))

curr_board = [[0,1,0],[1,0,0],[0,0,1]]

print costFunc(curr_board, constraints)

