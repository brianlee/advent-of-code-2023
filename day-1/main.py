import pathlib
import sys

def solve(input_data):
    data_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    cal_vals = []
    for line in input_data.split():
        intermediate_vals = []
        
        # Keep only digits from the input string
        pos = 0
        for c in line:
            if c.isdigit():
                intermediate_vals.append(c)
            else:
               # Added for part 2
               # If the character is not a digit, check if the string 
               # at this particular position is one of the pre-defined string
               # If yes, add the numeric value of the string
               for key in data_map.keys():
                   if line[pos:].startswith(key):
                       intermediate_vals.append(data_map[key])
            pos += 1
        
        print(f"interim: {intermediate_vals}")

        # Keep only first and last digits
        # If there is only one digit, repeat it twice
        if len(intermediate_vals) > 1:
            first, *_, last = intermediate_vals
            intermediate_vals = [first, last]
        else:
            intermediate_vals = [intermediate_vals[0] * 2]

        # Convert the digit string as int and add to the calibrated values
        cal_vals.append(int(''.join(intermediate_vals)))
    
    print(f"calibrated: {cal_vals}")

    # Sum all the calibrated values
    print(f"sum: {sum(cal_vals)}")

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_data = pathlib.Path(path).read_text()
        solve(input_data)
