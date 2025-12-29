import os

def solution(data):
    max_nums = []
    instructions = data.strip().split('\n')
    for line in instructions:
        line_str = str(line)
        cur_max = 0
        for i in range(0,len(line_str)):
            for j in range(i + 1, len(line_str)):
                cur_num = int(line_str[i]+line_str[j])
                cur_max = max(cur_max, cur_num)
        max_nums.append(cur_max)
    print(max_nums)
    return sum(max_nums)

def solution_2(data):
    max_nums = []
    instructions = data.strip().split('\n')
    for line in instructions:
        line_list = [num for num in str(line)]


        max_nums.append(cur_max)
    print(max_nums)
    return sum(max_nums)

if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read()

    if not data:
        print("Warning: File is empty or no data was read!")
        print(f"File path: {file_path}")
        print(f"File exists: {os.path.exists(file_path)}")
    else:
        result = solution(data)

        print(f"Result: {result}")
