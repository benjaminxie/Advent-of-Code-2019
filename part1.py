def run_program(code_arr):
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

if __name__ == '__main__':
    code_arr = [int(t) for t in input().split(',')]
    print(code_arr)
    code_arr[1] = 12
    code_arr[2] = 2
    print(code_arr)
    ans = run_program(code_arr)
    print(ans)
    print(code_arr)