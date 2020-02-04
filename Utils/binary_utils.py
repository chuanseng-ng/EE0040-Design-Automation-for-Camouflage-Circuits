from copy import deepcopy

def up_counter(bool_list: list) -> list:
    ''' Increments bool in bool list by 1
    '''
    tmp_bool_list = deepcopy(bool_list)
    tmp_bool_list[1][len(tmp_bool_list[0]) - 1] += 1

    temp_count = len(tmp_bool_list[0]) - 1
    while temp_count > -1:
        # Boolean has no 2
        if tmp_bool_list[1][temp_count] == 2:
            tmp_bool_list[1][temp_count] = 0
            tmp_bool_list[1][temp_count - 1] += 1
        temp_count -= 1
    return tmp_bool_list
    
