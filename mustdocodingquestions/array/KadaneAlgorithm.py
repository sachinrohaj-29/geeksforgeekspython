def long_solution():
    total_test = int(input())

    for test in range(0, total_test):
        array_size = int(input())
        input_array = [int(elem) for elem in input().strip().split()]

        sum_, store_sum = 0, []
        for elem in range(0, array_size):
            sum_ = 0
            for inner_elem in range(elem, array_size):
                store_sum.append(input_array[inner_elem])
                sum_ = sum_ + input_array[inner_elem]
                store_sum.append(sum_)

        store_sum.sort()
        print(store_sum[-1])


def optimized_solution():
    total_test = int(input())

    for test in range(0, total_test):
        array_size = int(input())
        input_array = [int(elem) for elem in input().strip().split()]

        local_sum, global_sum = input_array[0], input_array[0]
        for index in range(1, array_size):
            local_sum = max(input_array[index], local_sum+input_array[index])
            global_sum = max(local_sum, global_sum)

        print(global_sum)

if __name__ == "__main__":
    #long_solution()
    optimized_solution()
