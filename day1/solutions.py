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


# def cross_detection(start_number, turn_num):
#     count = 0
#     temp = -1 if turn_num < 0 else 1
#     for num in range(start_number, start_number + turn_num + temp, temp):
#       if num % 100 == 0:
#         count += 1
#     return count

def solution_2(data):
    instructions = data.strip().split('\n')
    pos = 50
    count = 0
    for line in instructions:
        d = line[0]
        amt = int(line[1:])
        for _ in range(amt):
            if d=='L':
                pos = (pos-1+100)%100 #made it consistent with positive counts
            else:
                pos = (pos+1)%100
            if pos==0:
                p2 += 1
        if pos==0:
            p1 += 1
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
        # result = solution_1(data)
        # result = solution_2(data)
        # print(f"Result: {result}")
