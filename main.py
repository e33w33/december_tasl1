def count_digit(num_list):
    set1 = set(num_list)
    list1 = list(set1)
    dict_ = {}
    for i in list1:
        result = num_list.count(i)
        dict_[i] = result
    return dict_


num_list = [1, 1, 3, 2, 1, 3, 4]
print(count_digit(num_list))
