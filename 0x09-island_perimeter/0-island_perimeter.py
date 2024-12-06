#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    Args:
        grid (list of list of int): 2D grid representing the map.
    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 edges
                perimeter += 4
                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove shared edge
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove shared edge

    return perimeter

