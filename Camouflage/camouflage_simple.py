from copy import*
import simulator
import output_corrupt


# Variable declaration
#   List
initial_corrupt = deepcopy(output_corrupt.corrupt_list)
initial_logic_gate = deepcopy(simulator.logic_gate)
modified_logic_gate = deepcopy(initial_logic_gate)
original_result = deepcopy(simulator.result_list)
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
initial_corrupt[first_camouflage_count] = 0

while user_input != str(len(camouflage_count_list)):
    first_camouflage = 0
    first_camouflage_count = 0
    for w in range(len(initial_corrupt)):
        if first_camouflage < initial_corrupt[w]:
            first_camouflage = initial_corrupt[w]
            first_camouflage_count = w
        else:
            pass
    camouflage_count_list.append(first_camouflage_count)
    initial_corrupt[first_camouflage_count] = 0


if user_input == str(len(camouflage_count_list)):
    print('\n', user_input, 'gates have been camouflaged.')
    for x in range(len(camouflage_count_list)):
        print('\n', initial_logic_gate[camouflage_count_list[x]], '->', modified_logic_gate[camouflage_count_list[x]])
else:
    pass
