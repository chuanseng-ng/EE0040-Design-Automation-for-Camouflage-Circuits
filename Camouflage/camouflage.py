from copy import*
import simulator
import output_corrupt_research


def next_camouflage(modified_logic_gate, camouflage_count_list):
    corrupt_list = []

    for w in range(simulator.logic_gate_number):
        del modified_result[:]
        simulate_number = 0

        # Reset input values to 0
        for a in range(simulator.input_number):
            simulator.input_list[1][a] = 0

        modified_logic_gate[w][0] = output_corrupt_research.gate_change(modified_logic_gate[w][0])

        while simulate_number != simulator.total_number:
            for x in range(simulator.wire_number):
                simulator.wire_list[1][x] = 0

            updated_wire1, updated_output1 = simulator.initial_simulate(
                simulator.input_list, simulator.output_list, simulator.wire_list, modified_logic_gate,
                simulator.flip_flop)
            updated_wire, updated_output = simulator.initial_simulate(
                simulator.input_list, updated_output1, updated_wire1, modified_logic_gate, simulator.flip_flop)
            modified_result.append(simulator.final_simulate(
                simulator.input_list, updated_output, updated_wire, modified_logic_gate, simulator.flip_flop))

            simulator.input_list[1][simulator.input_number - 1] += 1

            temp_count = simulator.input_number - 1
            while temp_count > -1:
                if simulator.input_list[1][temp_count] == 2:
                    simulator.input_list[1][temp_count] = 0
                    simulator.input_list[1][temp_count - 1] += 1
                temp_count -= 1

            simulate_number += 1

        modified_logic_gate[w][0] = output_corrupt_research.gate_change(modified_logic_gate[w][0])

        corrupt_list.append(output_corrupt_research.output_corrupt(original_result, modified_result))
        print('\n', corrupt_list)

    camouflage_corrupt = corrupt_list[0]
    corrupt_list_count = 0

    for w in range(len(corrupt_list)):
        if camouflage_corrupt < corrupt_list[w]:
            camouflage_corrupt = corrupt_list[w]
            corrupt_list_count = w
        else:
            pass

    camouflage_count_list.append(corrupt_list_count)
    modified_logic_gate[corrupt_list_count][0] = \
        output_corrupt_research.gate_change(modified_logic_gate[corrupt_list_count][0])

    return modified_logic_gate, camouflage_count_list


# Variable declaration
#   List
initial_corrupt = deepcopy(output_corrupt_research.corrupt_list)
initial_logic_gate = deepcopy(simulator.logic_gate)
modified_logic_gate = deepcopy(initial_logic_gate)
original_result = deepcopy(simulator.result_list)
modified_result = []
camouflage_count_list = []
corrupt_list = []

first_camouflage_count = 0
first_camouflage = copy(initial_corrupt[0])

print('\n State number of gates to be camouflaged.')
print('\n Default choice is 10% of total logic gates. \n')
user_input = input("Input: ")

if user_input == '0':
    print('\n No gates have been camouflaged.')
elif user_input == '':
    user_input = str(int(simulator.logic_gate_number*0.1))
    print(user_input)
else:
    pass

for w in range(len(initial_corrupt)):
    if first_camouflage < initial_corrupt[w]:
        first_camouflage = initial_corrupt[w]
        first_camouflage_count = w
    else:
        pass

camouflage_count_list.append(first_camouflage_count)
modified_logic_gate[first_camouflage_count][0] = \
    output_corrupt_research.gate_change(modified_logic_gate[first_camouflage_count][0])

while user_input != str(len(camouflage_count_list)):
    modified_logic_gate, camouflage_count_list = next_camouflage(modified_logic_gate, camouflage_count_list)

if user_input == str(len(camouflage_count_list)):
    print('\n', user_input, 'gates have been camouflaged.')
    for x in range(len(camouflage_count_list)):
        print('\n', initial_logic_gate[camouflage_count_list[x]], '->', modified_logic_gate[camouflage_count_list[x]])
else:
    pass
