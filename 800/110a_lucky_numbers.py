def print_is_nearly_lucky_number(num_list):
    lucky_num_count = num_list.count(4) + num_list.count(7)

    if lucky_num_count == 4 or lucky_num_count == 7:
        print("YES")
    else:
        print("NO")

input_number = list(map(int, input()))
print_is_nearly_lucky_number(input_number)


