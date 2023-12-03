import pathlib
import re
import sys

def solve(input_data):
    powers = []

    for line in input_data.split('\n'):
        before, _, after = line.partition(':')
        
        # Grab the game ID
        # Don't need this for part 2 
        _, _, game_id_str = before.partition(' ')
        game_id = int(game_id_str)

        min_blue = 0
        min_red = 0
        min_green = 0

        for set in after.split(';'):
            for cube in set.strip().split(','):
                m = re.match(r'(\d+) (red|green|blue)', cube.strip())
                cube_color = m.group(2)
                cube_count = int(m.group(1))

                # Keep track of max cube needed per game set
                match cube_color.lower():
                    case "green":
                        if cube_count > min_green:
                            min_green = cube_count
                    case "red":
                        if cube_count > min_red:
                            min_red = cube_count
                    case "blue":
                        if cube_count > min_blue:
                            min_blue = cube_count
                    case _:
                        print(f"unknown color detected with cube count ({cube_count}) for {cube_color}")
                        
            print(f"green: [{min_green}] red: [{min_red}] blue: [{min_blue}]")

        power = min_blue * min_green * min_red
        powers.append(power)
    
    print(f"powers: {powers}")
    print(f"answer: {sum(powers)}")

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_data = pathlib.Path(path).read_text()
        solve(input_data)