import re
import pyrival as pr


def scan_nums(line):
    # Use a regular expression to find numbers
    numbers = re.findall(r'-?\d+\.?\d*', line)
    # Convert to appropriate numerical types
    numbers = [float(num) if '.' in num else int(num) for num in numbers]
    return numbers

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data

def write_output(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def print_board(board):
    for row in board:
        print(''.join(row))
        
def get_blocks(input):
    """
    Splits a list of strings into blocks separated by empty lines.
    """
    blocks = []
    cur_block = []
    for line in input:
        if line == '\n':
            blocks.append(cur_block)
            cur_block = []
        else:
            cur_block.append(line)
    blocks.append(cur_block)
    return blocks

def get_lines(input):
    """
    Splits a list of strings into lines.
    """
    return [line.strip() for line in input]

def get_nums(input):
    """
    Splits a list of strings into numbers.
    """
    return [int(num) for num in input]


if __name__ == '__main__':
    pass

