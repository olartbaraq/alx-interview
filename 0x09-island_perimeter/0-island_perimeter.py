#!/usr/bin/python3
"""
main file containing code
"""


def island_perimeter(grid):
    """returns the perimeter of the island described
    in argument"""
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                if r == 0:
                    count += 1
                elif grid[r-1][c] == 0:
                    count += 1
                if r == len(grid) - 1:
                    count += 1
                elif grid[r+1][c] == 0:
                    count += 1
                if c == 0:
                    count += 1
                elif grid[r][c-1] == 0:
                    count += 1
                if c == len(grid[r]) - 1:
                    count += 1
                elif grid[r][c+1] == 0:
                    count += 1
    return count
