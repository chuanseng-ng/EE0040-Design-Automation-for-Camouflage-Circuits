from copy import*
import simulator


def gate_change(logic_gate):
    # NAND <-> OR
    # NOR <-> AND
    # XOR <-> XNOR

    find_and = '_AND'
    find_nand = '_NAND'
    find_or = '_OR'
    find_nor = '_NOR'
    find_xor = '_XOR'
    find_xnor = '_XNOR'

    if find_and in logic_gate:
        logic_gate = 'HS65_LH_NOR2X2'
    elif find_nand in logic_gate:
        logic_gate = 'HS65_LH_OR2X4'
    elif find_or in logic_gate:
        logic_gate = 'HS65_LH_NAND2X2'
    elif find_nor in logic_gate:
        logic_gate = 'HS65_LH_AND2X4'
    elif find_xor in logic_gate:
        logic_gate = 'HS65_LHS_XNOR2X3'
    elif find_xnor in logic_gate:
        logic_gate = 'HS65_LHS_XOR2X3'
    else:
        pass

    return logic_gate


def output_corrupt(original_result, modified_result):
    corrupt_count = 0

    for w in range(len(original_result)):
        for x in range(len(original_result[w])):
            if original_result[w][x] != modified_result[w][x]:
                corrupt_count += 1
            else:
                pass

    return corrupt_count


# Variables declaration
#   Lists
corrupt_list = []
original_logic = deepcopy(simulator.logic_gate)
modified_logic = deepcopy(original_logic)
original_result = deepcopy(simulator.result_list)
modified_result = []

for w in range(simulator.logic_gate_number):
    del modified_result[:]
    simulate_number = 0

    # Reset input values to 0
    for a in range(simulator.input_number):
        simulator.input_list[1][a] = 0

    modified_logic[w][0] = gate_change(modified_logic[w][0])

    while simulate_number != simulator.total_number:
        for x in range(simulator.wire_number):
            simulator.wire_list[1][x] = 0

        updated_wire1, updated_output1 = simulator.initial_simulate(
            simulator.input_list, simulator.output_list, simulator.wire_list, modified_logic, simulator.flip_flop)
        updated_wire, updated_output = simulator.initial_simulate(
            simulator.input_list, updated_output1, updated_wire1, modified_logic, simulator.flip_flop)
        modified_result.append(simulator.final_simulate(
            simulator.input_list, updated_output, updated_wire, modified_logic, simulator.flip_flop))

        simulator.input_list[1][simulator.input_number-1] += 1

        temp_count = simulator.input_number - 1
        while temp_count > -1:
            if simulator.input_list[1][temp_count] == 2:
                simulator.input_list[1][temp_count] = 0
                simulator.input_list[1][temp_count - 1] += 1
            temp_count -= 1

        simulate_number += 1

    modified_logic[w][0] = gate_change(modified_logic[w][0])

    corrupt_list.append(output_corrupt(original_result, modified_result))

    '''for w in range(len(modified_result)):
        print('\n', modified_result[w])'''

print('\n', corrupt_list)
