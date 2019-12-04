def run_program(code_arr, noun, verb):
    code_arr[1] = noun
    code_arr[2] = verb
    ip = 0
    while code_arr[ip] != 99:
        arg1_addr = code_arr[ip + 1]
        arg2_addr = code_arr[ip + 2]
        overwrite_addr = code_arr[ip + 3]

        arg1 = code_arr[arg1_addr]
        arg2 = code_arr[arg2_addr]

        if code_arr[ip] == 1:
            code_arr[overwrite_addr] = arg1 + arg2
        else: #code_arr[ip] == 2
            code_arr[overwrite_addr] = arg1 * arg2
        ip += 4
    return code_arr[0]

def brute_force(code_arr, output):
    for i in range(len(code_arr)):
        for j in range(len(code_arr)):
            code_arr_copy = [num for num in code_arr]
            if run_program(code_arr_copy, i, j) == output:
                return i, j
    return -1, -1

if __name__ == '__main__':
    code_arr = [int(t) for t in input().split(',')]
    noun, verb = brute_force(code_arr, 19690720)
    print(100 * noun + verb)