import time
import simulator

# AND or NOR -> AND/NOR
# OR or NAND -> OR/NAND
# XOR or XNOR -> XOR/XNOR

start = time.time()

# Variable declaration
#   Lists
new_result_list = []
logic_gate = []
logic_gate2 = []
flip_flop = []
input_list = []
output_list = []
wire_list = []
attacked_gates = []
toggle_logic_gates = []


#   Variables
file = simulator.file
#file2 = input("Input camouflaged netlist filename, with file type: ")
file2 = 'camouflage_edited.v'
find_gate = '.A'
find_flip = '.D'
find_input = 'input'
find_output = 'output'
find_wire = 'wire'
camouflage_and_nor = '_AND/NOR'
camouflage_or_nand = '_OR/NAND'
camouflage_xor_xnor = '_XOR/XNOR'

input_number = 0
output_number = 0
logic_gate_number = 0
flip_flop_number = 0
wire_number = 0
simulate_number = 0
total_number = 0
attack_pass = 0
identical_check = 0
toggle_gate_number = 0


# Read file and store them into list of strings
with open(file) as f:
    line_list = [line.rstrip('\n') for line in f]

# Finding keywords from list of string
#   List[1] is to store values
for x in range(len(line_list)):
    if find_input in line_list[x]:
        input_list.append(line_list[x])
        input_list.append(line_list[x])
    if find_output in line_list[x]:
        output_list.append(line_list[x])
        output_list.append(line_list[x])
    if find_gate in line_list[x]:
        logic_gate.append(line_list[x])
    if find_flip in line_list[x]:
        flip_flop.append(line_list[x])
    if find_wire in line_list[x]:
        wire_list.append(line_list[x])
        wire_list.append(line_list[x])

with open(file2) as g:
    line_list2 = [line.rstrip('\n') for line in g]

for x in range(len(line_list2)):
    if find_gate in line_list2[x]:
        logic_gate2.append(line_list2[x])

for w in range(len(input_list)):
    input_list[w] = input_list[w].split(',')
    for x in range(len(input_list[w])):
        input_list[w][x] = input_list[w][x].replace('input ', '')
        input_list[w][x] = input_list[w][x].replace('CLK', '')
        input_list[w][x] = input_list[w][x].replace('CK', '')
        input_list[w][x] = input_list[w][x].replace('NRST', '')
        input_list[w][x] = input_list[w][x].replace('VDD', '')
        input_list[w][x] = input_list[w][x].replace('GND', '')
        input_list[w][x] = input_list[w][x].replace(';', '')
    input_list[w] = list(filter(None, input_list[w]))
    input_number = len(input_list[w])

# Reset input values to 0
for w in range(input_number):
    input_list[1][w] = 0


for w in range(len(output_list)):
    output_list[w] = output_list[w].split(',')
    for x in range(len(output_list[w])):
        output_list[w][x] = output_list[w][x].replace('output ', '')
        output_list[w][x] = output_list[w][x].replace(';', '')
    output_list[w] = list(filter(None, output_list[w]))
    output_number = len(output_list[w])

# Reset output values to 0
for w in range(output_number):
    output_list[1][w] = 0


for w in range(len(logic_gate)):
    logic_gate[w] = logic_gate[w].split()
    for x in range(len(logic_gate[w])):
        logic_gate[w][x] = logic_gate[w][x].replace(';', '')
        logic_gate[w][x] = logic_gate[w][x].replace('(', '')
        logic_gate[w][x] = logic_gate[w][x].replace(')', '')
        logic_gate[w][x] = logic_gate[w][x].replace(',', '')
        logic_gate[w][x] = logic_gate[w][x].replace('.A', '')
        logic_gate[w][x] = logic_gate[w][x].replace('.B', '')
        logic_gate[w][x] = logic_gate[w][x].replace('.C', '')
        logic_gate[w][x] = logic_gate[w][x].replace('.D', '')
        logic_gate[w][x] = logic_gate[w][x].replace('.Z', '')
    logic_gate[w] = list(filter(None, logic_gate[w]))
logic_gate_number = len(logic_gate)


for w in range(len(flip_flop)):
    flip_flop[w] = flip_flop[w].split()
    for x in range(len(flip_flop[w])):
        flip_flop[w][x] = flip_flop[w][x].replace(';', '')
        flip_flop[w][x] = flip_flop[w][x].replace('(', '')
        flip_flop[w][x] = flip_flop[w][x].replace(')', '')
        flip_flop[w][x] = flip_flop[w][x].replace(',', '')
        flip_flop[w][x] = flip_flop[w][x].replace('.D', '')
        flip_flop[w][x] = flip_flop[w][x].replace('.Q', '')
        flip_flop[w][x] = flip_flop[w][x].replace('.CP', '')
        flip_flop[w][x] = flip_flop[w][x].replace('.RN', '')
    flip_flop[w] = list(filter(None, flip_flop[w]))
flip_flop_number = len(flip_flop)


for w in range(len(wire_list)):
    wire_list[w] = wire_list[w].split(',')
    for x in range(len(wire_list[w])):
        wire_list[w][x] = wire_list[w][x].replace('wire ', '')
        wire_list[w][x] = wire_list[w][x].replace(';', '')
    wire_number = len(wire_list[w])


for w in range(len(logic_gate2)):
    logic_gate2[w] = logic_gate2[w].split()
    for x in range(len(logic_gate2[w])):
        logic_gate2[w][x] = logic_gate2[w][x].replace(';', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('(', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace(')', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace(',', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('.A', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('.B', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('.C', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('.D', '')
        logic_gate2[w][x] = logic_gate2[w][x].replace('.Z', '')
    logic_gate2[w] = list(filter(None, logic_gate2[w]))


# Reset wire values to 0
for w in range(wire_number):
    wire_list[1][w] = 0

toggle_logic_gates.append([])
toggle_logic_gates.append([])
toggle_logic_gates.append([])

for a in range(logic_gate_number):
    if camouflage_and_nor in logic_gate2[a][0]:
        toggle_logic_gates[0].append(logic_gate2[a][0])
        toggle_logic_gates[1].append(a)
        toggle_logic_gates[2].append(0)

        toggle_gate_number += 1

    elif camouflage_or_nand in logic_gate2[a][0]:
        toggle_logic_gates[0].append(logic_gate2[a][0])
        toggle_logic_gates[1].append(a)
        toggle_logic_gates[2].append(0)

        toggle_gate_number += 1

    elif camouflage_xor_xnor in logic_gate2[a][0]:
        toggle_logic_gates[0].append(logic_gate2[a][0])
        toggle_logic_gates[1].append(a)
        toggle_logic_gates[2].append(0)

        toggle_gate_number += 1

    else:
        pass

total_number = 2**input_number

while attack_pass != 1:
    new_result_list.clear()
    for v in range(input_number):
        input_list[1][v] = 0

    for w in range(toggle_gate_number):
        if toggle_logic_gates[2][w] == 0:
            if camouflage_and_nor in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LH_AND2X4'
            elif camouflage_or_nand in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LH_OR2X4'
            elif camouflage_xor_xnor in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LHS_XOR2X3'
            else:
                pass
        elif toggle_logic_gates[2][w] == 1:
            if camouflage_and_nor in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LH_NOR2X2'
            elif camouflage_or_nand in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LH_NAND2X2'
            elif camouflage_xor_xnor in toggle_logic_gates[0][w]:
                logic_gate2[toggle_logic_gates[1][w]][0] = 'HS65_LHS_XNOR2X3'
            else:
                pass
        else:
            pass

    while simulate_number != total_number:
        for w in range(wire_number):
            wire_list[1][w] = 0

        '''print('\n')
        for w in range(len(toggle_logic_gates[1])):
            print(logic_gate2[toggle_logic_gates[1][w]])'''

        updated_wire, updated_output = \
            simulator.initial_simulate(input_list, output_list, wire_list, logic_gate2, flip_flop)
        updated_wire1, updated_output1 = \
            simulator.initial_simulate(input_list, updated_output, updated_wire, logic_gate2, flip_flop)
        new_result_list.append(
            simulator.final_simulate(input_list, updated_output1, updated_wire1, logic_gate2, flip_flop))

        input_list[1][input_number-1] += 1

        temp_count = input_number - 1
        while temp_count > -1:
            if input_list[1][temp_count] == 2:
                input_list[1][temp_count] = 0
                input_list[1][temp_count - 1] += 1
            temp_count -= 1

        simulate_number += 1

    #print('\n', new_result_list)

    for w in range(len(new_result_list)):
        for x in range(len(new_result_list[w])):
            if new_result_list[w][x] == simulator.result_list[w][x]:
                identical_check += 1
            else:
                pass

    #print(identical_check)
    if identical_check == total_number*output_number:
        attack_pass = 1
    else:
        simulate_number = 0
        identical_check = 0
        toggle_logic_gates[2][toggle_gate_number-1] += 1
        temp_counter = toggle_gate_number - 1
        while temp_counter > -1:
            if toggle_logic_gates[2][temp_counter] == 2:
                toggle_logic_gates[2][temp_counter] = 0
                toggle_logic_gates[2][temp_counter - 1] += 1
            temp_counter -= 1


for w in range(len(toggle_logic_gates[1])):
    print('\n', logic_gate2[toggle_logic_gates[1][w]])


end = time.time()
runtime = end - start + simulator.runtime

print('\n', simulate_number)
print('\nRuntime is', runtime, 'sec')
