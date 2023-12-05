import pathlib
import sys
from collections import * 

def solve_part1(input_data):

    answer = 0

    for line in input_data.split('\n'):
        _, _, s = line.partition(": ")
        wins, _, card = s.partition(" | ")

        winning_nums = [n for n in wins.split()]
        card_nums = [n for n in card.split()]

        match_count = 0
        for num in card_nums:
            if (num in winning_nums):
                match_count += 1

        if match_count > 0:
            total_win = 1 << (match_count - 1)
            answer += total_win
    
    print(f"p1 answer={answer}")
        
def solve_part2(input_data):

    answer = 0
    copies = defaultdict(int)

    for line in input_data.split('\n'):
        front, _, s = line.partition(": ")
        wins, _, card = s.partition(" | ")

        card_id = front.split()[1]

        winning_nums = [n for n in wins.split()]
        card_nums = [n for n in card.split()]

        match_count = 0
        for num in card_nums:
            if (num in winning_nums):
                match_count += 1
        
        current_game = int(card_id)

        if copies.get(card_id, 0) == 0:
            copies[card_id] = 1

        #print(f"game ({current_game}) match_count=", match_count)
        #print(f"copies before game ({current_game}) =", copies)
        for i in range(current_game+1, current_game+1+match_count):
            k = str(i)
            if copies[k] == 0:
                copies[k] = 1
            copies[k] += 1 * copies[card_id]

        #print(f"copies after game ({current_game}) =", copies)

    answer = sum(copies.values())
    print(f"p2 answer={answer}")
        

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_data = pathlib.Path(path).read_text()
        solve_part1(input_data)
        solve_part2(input_data)
