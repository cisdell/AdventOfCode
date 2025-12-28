import os
import sys

def solutions(data):
    count = 0
    cur_num = 50
    instructions = data.strip().split('\n')

    for instruction in instructions:
        if not instruction:  # Skip empty lines
            continue

        if instruction.startswith('L'):
            turn_num = int(instruction[1:])  # More efficient than split
            cur_num = cur_num - turn_num
        elif instruction.startswith('R'):
            turn_num = int(instruction[1:])  # More efficient than split
            cur_num = cur_num + turn_num
        else:
            print(f"Warning: Unexpected instruction format: {instruction}")
            continue

        if cur_num % 100 == 0:
            count += 1

    return count



if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'tests.txt')

    with open(file_path, 'r') as file:
        data = file.read()

    if not data:
        print("Warning: File is empty or no data was read!")
        print(f"File path: {file_path}")
        print(f"File exists: {os.path.exists(file_path)}")
    else:
        result = solutions(data)
        print(f"Result: {result}")
