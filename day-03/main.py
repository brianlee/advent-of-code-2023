import pathlib
import sys
from collections import *

def part1(input_data):
    grid = build_grid(input_data)
    #print_grid(grid)

    height = len(grid)
    width = len(grid[0])
    answer = 0

    #print(f"height={height} width={width}")

    for y in range(height):
        x = 0
        while x < width:
            #print()
            #print(f"at y={y} x={x} grid={grid[y][x]}")

            # we don't care if the current cell could not be a part of the part number
            if not grid[y][x].isdigit():
                #print(f"not number={grid[y][x]}")
                x += 1
                continue

            part_num = grid[y][x]
            checks = get_adjacent_cells(x, y, width, height)
            #print("checks=", checks)

            # check if a number exist in next cell
            nx = x + 1
            while nx < width and grid[y][nx].isdigit():
                #print(f"at y={y} x={x} nx={nx} val={grid[y][nx]} part_num={part_num}")
                
                extra_checks = get_adjacent_cells(nx, y, width, height)
                #print("adding checks=", extra_checks)
                
                checks.extend(extra_checks)
                part_num += grid[y][nx]
                nx += 1 

                #print("ext checks=", checks)
            
            # add to answer
            valid_part = False
            for m, n in checks:
                if grid[n][m] != "." and not grid[n][m].isdigit():
                    #print(f"found a gear at y={n} x={m} val={grid[n][m]}")
                    valid_part = True
                    break;
            
            if valid_part:
                #print("adding part_num=", part_num)
                answer += int(part_num)
            
            x = nx
            #print(f"part_num={part_num}")
    print("p1 answer=", answer)

def part2(input_data):
    grid = build_grid(input_data)
    #print_grid(grid)

    height = len(grid)
    width = len(grid[0])
    answer = 0

    gear_dict = defaultdict(list)

    for y in range(height):
        x = 0
        while x < width:

            # we don't care if the current cell could not be a part of the part number
            if not grid[y][x].isdigit():
                x += 1
                continue

            part_num = grid[y][x]
            checks = get_adjacent_cells(x, y, width, height)

            # check if a number exist in next cell
            nx = x + 1
            while nx < width and grid[y][nx].isdigit():
                extra_checks = get_adjacent_cells(nx, y, width, height)
                checks.extend(extra_checks)
                part_num += grid[y][nx]
                nx += 1 
            
            # Keep a dict to track locations of gears and their neighboring numbers
            for m, n in checks:
                if grid[n][m] == "*":
                    gear_dict[(n, m)].append(part_num)

            x = nx
    
    # Check gear ratio for each gear found
    for k in gear_dict.keys():
        # Remove duplicate number
        # this could potentially cause a bug. it's better to clean up dupe num locations
        clean_list = list(set(gear_dict[k]))
        if len(clean_list) == 2:
            answer += int(clean_list[0]) * int(clean_list[1])


    print("p2 answer=", answer)


def get_adjacent_cells(x, y, max_width, max_height):
    adj_cells = []
    for j in range(-1, 2):
        for i in range (-1, 2):
            # skip the current cell
            if i == 0 and j == 0:
                continue

            cellx = x + i
            celly = y + j

            # if the adj cell is within bounds, include into the adj cells to check
            if cellx >= 0 and celly >= 0 and celly < max_height and cellx < max_width:
                adj_cells.append((cellx, celly))
    return adj_cells

def build_grid(data):
    outer = []
    for line in input_data.split():
        inner = []
        for c in line:
            inner.append(c)
        outer.append(inner)
    return outer

def print_grid(grid):
    print("[")
    for i in grid:
        print(i)
    print("]")

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_data = pathlib.Path(path).read_text()
        part1(input_data)
        part2(input_data)