#!/usr/bin/python3

import sys


N = sys.argv[1]

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def nqueens(N, rows, negD, posD, col_no, row_no, ret_list):
    """returns a list of list of strings"""
    while col_no < N:
        placed = False
        while row_no < N:
            if row_no in rows or (row_no - col_no) in negD\
                    or (row_no + col_no) in posD:
                row_no += 1
            else:
                rows.add(row_no)
                negD.add(row_no - col_no)
                posD.add(row_no + col_no)
                ret_list.append([col_no, row_no])
                col_no += 1
                row_no = 0
                placed = True
                break
        if len(ret_list) == N:
            return ret_list
        if col_no == 0 and len(ret_list) == 0:
            return []
        if not placed and len(ret_list) < N and len(ret_list) > 0:
            prev_row = (ret_list[-1])[1]
            rows.remove(prev_row)
            negD.remove(prev_row - col_no + 1)
            posD.remove(prev_row + col_no - 1)
            ret_list.pop(-1)
            col_no = col_no - 1
            nqueens(N, rows, negD, posD, col_no, prev_row + 1, ret_list)
            return ret_list


if __name__ == "__main__":
    i = 0
    while i < N:
        ret = nqueens(N=N, rows=set(), negD=set(), posD=set(), col_no=0,
                      row_no=i, ret_list=[])
        if ret:
            print(ret)
            if ret[0][1] == i + 1:
                i += 1
        i += 1
