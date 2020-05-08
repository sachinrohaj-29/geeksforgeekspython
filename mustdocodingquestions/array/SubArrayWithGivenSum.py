class SubArrayWithGivenSum:

    def work(self):
        total_test = int(input())

        while total_test > 0 :
            size_sum = [int(entry) for entry in input().strip().split()]
            array_size = size_sum[0]
            expected_sum = size_sum[1]

            given_array = [int(entry) for entry in input().strip().split()]
            flag, start, current_index, sum_ = True, 0, 0, 0

            while flag:
                sum_ = sum_ + given_array[current_index]

                # This is important, rather than an if condition use a loop
                while sum_ > expected_sum and current_index < array_size:
                    sum_ = sum_ - given_array[start]
                    start += 1
                if sum_ == expected_sum:
                    print(start+1, current_index+1)
                    flag = False
                current_index += 1
                if current_index == array_size:
                    flag = False
            if sum_ != expected_sum:
                print(-1)
            total_test -= 1


if __name__ == "__main__":
    SubArrayWithGivenSum.work(SubArrayWithGivenSum())
