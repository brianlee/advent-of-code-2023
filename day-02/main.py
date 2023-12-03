import pathlib
import re
import sys

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def solve(input_data):
    possible_games = []

    for line in input_data.split('\n'):
        before, _, after = line.partition(':')
        
        # Grab the game ID
        _, _, game_id_str = before.partition(' ')
        game_id = int(game_id_str)

        limit_reached = False
        for set in after.split(';'):
            #print(f"set: [{set}]")
            
            for cube in set.strip().split(','):
                #print(f"cube: [{cube.strip()}]")
                
                m = re.match(r'(\d+) (red|green|blue)', cube.strip())
                #print(f"match: [{m}]")

                cube_color = m.group(2)
                cube_count = int(m.group(1))
                #print(f"match group 0: [{m.group(0)}]")
                #print(f"cube_color: [{cube_color}]")
                #print(f"cube_count: [{cube_count}]")

                # For specific color, check if count is less than the possible limit
                # This is ugly but it works
                match cube_color.lower():
                    case "green":
                        if cube_count > GREEN_LIMIT:
                            limit_reached = True
                    case "red":
                        if cube_count > RED_LIMIT:
                            limit_reached = True
                    case "blue":
                        if cube_count > BLUE_LIMIT:
                            limit_reached = True
                    case _:
                        print(f"unknown color detected with cube count ({cube_count}) for {cube_color}")
                
        if limit_reached == False:
            possible_games.append(game_id)
    
    print(f"possible games: {possible_games}")
    print(f"answer: {sum(possible_games)}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_data = pathlib.Path(path).read_text()
        solve(input_data)