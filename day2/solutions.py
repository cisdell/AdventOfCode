from input import IDs
def parse_ids(IDs):
    invalid_sum = 0
    for id in IDs.split(","):
        start, end = id.split("-")
        for number in range(int(start), int(end) + 1):
            if helper(number):
                invalid_sum += number
    print(invalid_sum)
    return invalid_sum

#used this function for only part 1
def find_invalid(number):
    if len(str(number)) %2 != 0:
        return False
    # print(number)
    first_half = str(number)[:len(str(number))//2]
    second_half = str(number)[len(str(number))//2:]
    if first_half == second_half:
        return True
    return False

#used this shit for part 2
def helper(number, char_start=1):
    number_str = str(number)
    if char_start > len(number_str)//2:
        return False
    cur_char = number_str[:char_start]
    if len(number_str) % len(cur_char) == 0 and number_str == cur_char * (len(number_str)//len(cur_char)):
        return True
    return helper(number_str, char_start + 1)

if __name__ == "__main__":
    parse_ids(IDs)
    # res = helper(112)
    # print(res)
    # print(invalid_count)

