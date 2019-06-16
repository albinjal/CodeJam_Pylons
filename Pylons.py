import numpy as np


# Defines an allowed move
def allowed(grid, curr, dest):
    if grid[dest[0]][dest[1]] == 1.0:
        return False
    if curr[0] == dest[0] or curr[1] == dest[1]:
        return False
    if curr[0] - curr[1] == dest[0] - dest[1]:
        return False
    if curr[0] + curr[1] == dest[0] + dest[1]:
        return False
    return True


def resetforward(path, current, last):
    for x in range(current + 1, last):
        path[x] = [0, 0]
    return path


# Calculates the next path to test
def nextpath(total_rows, total_cols, failedpath, failindex):
    lastrow = total_rows - 1
    lastcol = total_cols - 1
    total = total_cols * total_rows

    # step 1, try next row
    if failedpath[failindex][0] != lastrow:
        failedpath[failindex][0] += 1
        return resetforward(failedpath, failindex, total)

    # step 2, try next col
    if failedpath[failindex][1] != lastcol:
        failedpath[failindex][0] = 0
        failedpath[failindex][1] += 1
        return resetforward(failedpath, failindex, total)

    # step 3, take a step back, repeat
    if failindex != 0:
        return nextpath(total_rows, total_cols, failedpath, failindex - 1)
    return False


# Tests a given path
def test_path(total_rows, total_cols, pathtotest):
    path_progress = []
    current_grid = np.zeros((total_rows, total_cols))
    for i, move in enumerate(pathtotest):
        if not path_progress or allowed(current_grid, path_progress[-1], move):
            path_progress.append(move)
            current_grid[move[0]][move[1]] = 1.0
        else:
            if pathtotest:
                return [1, pathtotest, i]
            else:
                return False
    return path_progress


if __name__ == 'main':
    num_test_cases = int(input())
    test_cases = []
    for I in range(num_test_cases):
        test_cases.append(input().split())

    for index, data in enumerate(test_cases):
        r = int(data[0])
        c = int(data[1])
        first = []
        for I in range(r * c):
            first.append([0, 0])
    # -----------------------------------------------------------------
        # This Part was throw in the last second to swap from recursion to loops and therefore might be confusing
        while True:
            result = test_path(r, c, first)
            if result:
                if result[0] == 1:
                    first = nextpath(r, c, result[1], result[2])
                    if not first:
                        result = False
                        break
                else:
                    break
            else:
                break
    # -----------------------------------------------------------------
        if result:
            print('Case #%d: POSSIBLE' % (index + 1))
            for move in result:
                print('%d %d' % (move[0] + 1, move[1] + 1))
        else:
            print('Case #%d: IMPOSSIBLE' % (index + 1))

