from copy import deepcopy

def attack(simulator, correct_result_list: list):
    user_input = 0
    camo_combi = 0

    print("Please input the camouflaged gate combinations, one at a time. \n")
    print("1 - AND \n")
    print("2 - NAND \n")
    print("3 - OR \n")
    print("4 - NOR \n")
    print("5 - XOR \n")
    print("6 - XNOR \n")
    print("7 - End \n")

    # user_input = input("Selection: ")
    chosen_camo = []
    while user_input != "7":
        camo_combi = camo_combi + 1
        if user_input == "1":
            chosen_camo.append('HS65_LH_AND2X4')
            user_input = input("Selection: ")
        elif user_input == "2":
            chosen_camo.append('HS65_LH_NAND2X2')
            user_input = input("Selection: ")
        elif user_input == "3":
            chosen_camo.append('HS65_LH_OR2X4')
            user_input = input("Selection: ")
        elif user_input == "4":
            chosen_camo.append('HS65_LH_NOR2X2')
            user_input = input("Selection: ")
        elif user_input == "5":
            chosen_camo.append('HS65_LH_XOR2X3')
            user_input = input("Selection: ")
        elif user_input == "6":
            chosen_camo.append('HS65_LH_XNOR2X3')
            user_input = input("Selection: ")
        else:
            break
    chosen_camo.append('HS65_LH_NAND2X2')
    chosen_camo.append('HS65_LH_NOR2X2')
    # Create table
    logic_gate_list = deepcopy(simulator.logic_gate)
    camo_gates_indexes = _get_camo_gate_indexes(logic_gate_list)
    output_compare_result = _match_gate_output(correct_result_list, chosen_camo, camo_gates_indexes, simulator)
    print(output_compare_result)
   
   
#     wrong_output = []
#     camo_gate_combi = []
#     temp_list = []
#     temp_list.append([])
#     for i in range(camo_gate_number):
#         camo_gate_combi.append([])
#         temp_list[0].append(0)

#     for i in range(int(str(camo_combi))**camo_gate_number):
#         for b in range(camo_gate_number):
#             camo_gate_combi[b].append(temp_list[0][b])
#         camo_gate_output[0].append(i)

#         temp_list[0][camo_gate_number - 1] += 1

#         temp_counter = camo_gate_number - 1
#         while temp_counter > -1:
#             if temp_list[0][temp_counter] == camo_combi:
#                 temp_list[0][temp_counter] = 0
#                 temp_list[0][temp_counter - 1] += 1
#             temp_counter -= 1

#     for i in range(int(str(camo_combi))**camo_gate_number):
#         for b in range(camo_gate_number):
#             for c in range(camo_combi):
#                 if camo_gate_combi[b][i] == c:
#                         camo_gate_combi[b][i] = chosen_camo[c]
#                 else:
#                     pass

#     print(camo_gate_output[0], '\n')

#     for i in range(input_number):
#         input_list[1][i] = 0

#     wrong_output.append([])

#     while(True):
#         new_result_list = []
#         camo_gate_output.append([])
#         for b in range(input_number):
#             camo_gate_output[simulate_number + 1].append(input_list[1][b])

#         for b in range(wire_number):
#             wire_list[1][b] = 0

#         for b in range(int(str(camo_combi))**camo_gate_number):
#             if b in wrong_output[0]:
#                 camo_gate_output[simulate_number + 1].append('-')
#             else:
#                 for c in range(camo_gate_number):
#                     logic_gate2[camo_gates[0][c]][0] = camo_gate_combi[c][b]

#                 simulator1.logic_gate = deepcopy(logic_gate2)
#                 new_result_list = simulator1.simulate()

#                 for c in range(len(new_result_list[0])):
#                     if new_result_list[0][c] == simulator.result_list[simulate_number][c]:
#                         identical_check += 1
#                     else:
#                         pass

#                 if identical_check == output_number:
#                     camo_gate_output[simulate_number + 1].append('Y')
#                     identical_check = 0
#                 else:
#                     camo_gate_output[simulate_number + 1].append('N')
#                     identical_check = 0

#                 if camo_gate_output[simulate_number + 1][-1] == 'N':
#                     wrong_output[0].append(b)

#         print(camo_gate_output[simulate_number + 1], '\n')
#         simulate_number += 1

#         input_list[1][input_number - 1] += 1

#         temp_count = input_number - 1
#         while temp_count > -1:
#             if input_list[1][temp_count] == 2:
#                 input_list[1][temp_count] = 0
#                 input_list[1][temp_count - 1] += 1
#             temp_count -= 1

#         if len(wrong_output[0]) == (int(str(camo_combi))**camo_gate_number) - 1:
#             break

#         #print('\n', new_result_list)

#     end = time.time()
#     runtime = end - start + simulator.runtime

#     print('\nLegend:')
#     for i in range(int(str(camo_combi))**camo_gate_number):
#         print('\n', camo_gate_output[0][input_number + i], ':')
#         for b in range(camo_gate_number):
#             print(camo_gates[1][b], '->', camo_gate_combi[b][i])

#     print('\n')
#     print('\nCorrect combination of logic gates:',)
#     for i in range(camo_gate_number):
#         print('\n', logic_gate2[camo_gates[0][i]][1], camo_gates[1][i], '->',
#             camo_gate_combi[i][camo_gate_output[-1].index('Y') - input_number])

#     print('\nNumber of tries to break:', simulate_number)
#     print('\nRuntime is', runtime, 'sec')

# def create_table(input_number, logic_gate_number, logic_gate2):
#     table = []
#     _create_table_with_header(table, input_number)
#     camo_gates, camo_gate_number = _get_camo_gate_indexes(logic_gate_number, logic_gate2)

# def _create_table_with_header(table, input_number):
#     header_list = []
#     for i in range(input_number):
#         header_list.append('I' + str(i))
#     return table.insert(0, header_list)

def _get_camo_gate_indexes(logic_gate_list: list):
    camouflage_gate = 'CAMO'
    camo_gates = []
    for i in range(len(logic_gate_list)):
        if camouflage_gate in logic_gate_list[i][0]:
            camo_gates.append(i)
    return camo_gates

def _match_gate_output(correct_result_list: list, user_input_combi: list, camo_gates_indexes: list, simulator):
    combi_list = _grid_produce(user_input_combi, camo_gates_indexes)
    output_compare_result = {}
    for combi in combi_list:
        output_compare_result[combi] = []
    for combi in combi_list:
        if len(output_compare_result[combi]) == 0 or output_compare_result[combi][-1] != 'N' or output_compare_result[combi][-1] != '-':
            for i in range(len(camo_gates_indexes)):
                simulator.logic_gate[camo_gates_indexes[i]][0] = combi[i]
            combi_result = simulator.simulate()

            if combi_result == correct_result_list:
                output_compare_result[combi].append('Y')
            else:
                output_compare_result[combi].append('N')
        else:
            output_compare_result[combi].append('-')
    return output_compare_result

def _grid_produce(user_input_combi, camo_gates_indexes):
    camo_gate_num = len(camo_gates_indexes)
    idx=[0] * camo_gate_num

    result = []

    count = 0
    total = len(user_input_combi) ** camo_gate_num
    while(count<total):
        for i in range(camo_gate_num):
            result.append(user_input_combi[idx[i]])
        
        count+=1
        idx[-1]+=1

        tmp = len(idx) - 1
        while tmp > -1:
            if idx[tmp] == len(user_input_combi):
                idx[tmp] = 0
                idx[tmp-1] +=1
            tmp -=1

    result_combi = []
    for i in range(len(result)):
        if i % camo_gate_num == 0:
            result_combi.append([])
        result_combi[-1].append(result[i])

    for i, combi in enumerate(result_combi):
        result_combi[i] = tuple(combi)

    return result_combi