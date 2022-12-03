def segregate_odd_even(int_array_param, left_count, right_count):
    if((right_count-left_count == 1) or (right_count-left_count == 0) or (left_count>right_count)) :
        print(int_array_param)
    else:
        while(int_array_param[left_count]%2 == 1):
            left_count += 1
        while(int_array_param[right_count]%2 == 0):
            right_count -= 1
        if left_count<right_count:
            aux_element = int_array_param[left_count]
            int_array_param[left_count] = int_array_param[right_count]
            int_array_param[right_count] = aux_element
        segregate_odd_even(int_array_param, left_count, right_count)

print("the first list")
input_array = [5, 2, 34, 9, -1]
segregate_odd_even(input_array, 0, len(input_array)-1)

print("")
print("the second list")
input_array2 = [5, 2, 34, 9, -1, 4, 7, 5, 5, 3, 6, 9, 7, 5, 2, 8, -93]
segregate_odd_even(input_array2, 0, len(input_array2)-1)

print("")
print("the thrid list")
input_array3 = [4, 2, 34, 64, -93]
segregate_odd_even(input_array3, 0, len(input_array3)-1)
