import os
import sys

def solution_1(data):
    count = 0
    cur_num = 50
    instructions = data.strip().split('\n')

    for instruction in instructions:
        if not instruction:
            continue

        if instruction.startswith('L'):
            turn_num = int(instruction[1:])
            cur_num = cur_num - turn_num
        elif instruction.startswith('R'):
            turn_num = int(instruction[1:])
            cur_num = cur_num + turn_num
        else:
            print(f"Warning: Unexpected instruction format: {instruction}")
            continue

        if cur_num % 100 == 0:
            count += 1
    return count

def solution_2(data):
    count = 0
    cur_num = 50
    instructions = data.strip().split('\n')

    for instruction in instructions:
        if not instruction:
            continue
        start = cur_num
        if instruction.startswith('L'):
          turn_num = int(instruction[1:])
          cur_num = cur_num - turn_num
        elif instruction.startswith('R'):
          turn_num = int(instruction[1:])
          cur_num = cur_num + turn_num
        else:
            print(f"Warning: Unexpected instruction format: {instruction}")
            continue

        # if cur_num % 100 == 0:
        #   count += 1
        # if cross_detection(start, cur_num):
        #   count += 1
        count += cross_detection(start, cur_num)

    return count

def cross_detection(start, end):
    if start == end:
        return 0

    min_val = min(start, end)
    max_val = max(start, end)

    # This counts how many multiples of 100 are between min_val and max_val
    # including if we land exactly on one
    return (max_val // 100) - (min_val // 100)

    return lower != upper
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
        # result = solution_1(data)
        result = solution_2(data)
        print(f"Result: {result}")
