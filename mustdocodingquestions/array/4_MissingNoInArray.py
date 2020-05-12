def solution():
    total_test = int(input())

    for test in range(0, total_test):
        array_size = int(input())
        given_array = [int(elem) for elem in input().strip().split()]

        given_sum = 0
        for elem in range(0, array_size-1):
            given_sum = given_sum + given_array[elem]

        expected_sum = 0
        for elem in range(1, array_size+1):
            expected_sum = expected_sum + elem

        print(expected_sum-given_sum)


if __name__ == "__main__":
    solution()
