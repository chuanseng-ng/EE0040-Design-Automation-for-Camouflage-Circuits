import time
import simulator

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
camo_gates = []
camo_gate_output = []
camo_gate_combi = []
wrong_output = []
temp_list = []
chosen_camo = []


#   Variables
file = simulator.file
#file2 = input("Input camouflaged netlist filename, with file type: ")
file2 = 'camouflage_edited.v'
find_gate = '.A'
find_flip = '.D'
find_input = 'input'
find_output = 'output'
find_wire = 'wire'
camouflage_gate = 'CAMO'

input_number = 0
output_number = 0
logic_gate_number = 0
flip_flop_number = 0
wire_number = 0
simulate_number = 0
attack_pass = 0
identical_check = 0
camo_gate_number = 0
camo_number = 0
user_input = 0
camo_combi = 0


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
        input_list[w][x] = input_list[w][x].replace('NRST', '')
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
        logic_gate2[w][x] = logic_gate2[w][x].replace('.Z', '')
    logic_gate2[w] = list(filter(None, logic_gate2[w]))


# Reset wire values to 0
for w in range(wire_number):
    wire_list[1][w] = 0

print("Please input the camouflaged gate combinations, one at a time. \n")
print("1 - AND \n")
print("2 - NAND \n")
print("3 - OR \n")
print("4 - NOR \n")
print("5 - XOR \n")
print("6 - XNOR \n")
print("7 - End \n")

user_input = input("Selection: ")

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


# Header
camo_gate_output.append([])
for a in range(input_number):
    camo_gate_output[0].append('I' + str(a))

camo_gates.append([])
camo_gates.append([])

for a in range(logic_gate_number):
    if camouflage_gate in logic_gate2[a][0]:
        camo_gates[0].append(a)
        camo_gates[1].append(logic_gate2[a][0])
        camo_gate_number += 1
    else:
        pass

temp_list.append([])
for a in range(camo_gate_number):
    camo_gate_combi.append([])
    temp_list[0].append(0)

for a in range(int(str(camo_combi))**camo_gate_number):
    for b in range(camo_gate_number):
        camo_gate_combi[b].append(temp_list[0][b])
    camo_gate_output[0].append(a)

    temp_list[0][camo_gate_number - 1] += 1

    temp_counter = camo_gate_number - 1
    while temp_counter > -1:
        if temp_list[0][temp_counter] == camo_combi:
            temp_list[0][temp_counter] = 0
            temp_list[0][temp_counter - 1] += 1
        temp_counter -= 1

for a in range(int(str(camo_combi))**camo_gate_number):
    for b in range(camo_gate_number):
        for c in range(camo_combi):
            if camo_gate_combi[b][a] == c:
                    camo_gate_combi[b][a] = chosen_camo[c]
            else:
                pass

print(camo_gate_output[0], '\n')

for a in range(input_number):
    input_list[1][a] = 0

wrong_output.append([])

while attack_pass != 1:
    new_result_list.clear()
    camo_gate_output.append([])
    for b in range(input_number):
        camo_gate_output[simulate_number + 1].append(input_list[1][b])

    for b in range(wire_number):
        wire_list[1][b] = 0

    for b in range(int(str(camo_combi))**camo_gate_number):
        if b in wrong_output[0]:
            camo_gate_output[simulate_number + 1].append('-')
        else:
            new_result_list.clear()
            for c in range(camo_gate_number):
                logic_gate2[camo_gates[0][c]][0] = camo_gate_combi[c][b]

            updated_wire, updated_output = \
                simulator.initial_simulate(input_list, output_list, wire_list, logic_gate2, flip_flop)
            updated_wire1, updated_output1 = \
                simulator.initial_simulate(input_list, updated_output, updated_wire, logic_gate2, flip_flop)
            new_result_list.append(
                simulator.final_simulate(input_list, updated_output1, updated_wire1, logic_gate2, flip_flop))

            for c in range(len(new_result_list[0])):
                if new_result_list[0][c] == simulator.result_list[simulate_number][c]:
                    identical_check += 1
                else:
                    pass

            if identical_check == output_number:
                camo_gate_output[simulate_number + 1].append('Y')
                identical_check = 0
            else:
                camo_gate_output[simulate_number + 1].append('N')
                identical_check = 0

            if camo_gate_output[simulate_number + 1][-1] == 'N':
                wrong_output[0].append(b)
            else:
                pass

    print(camo_gate_output[simulate_number + 1], '\n')
    simulate_number += 1

    input_list[1][input_number - 1] += 1

    temp_count = input_number - 1
    while temp_count > -1:
        if input_list[1][temp_count] == 2:
            input_list[1][temp_count] = 0
            input_list[1][temp_count - 1] += 1
        temp_count -= 1

    if len(wrong_output[0]) == (int(str(camo_combi))**camo_gate_number) - 1:
        attack_pass = 1

    #print('\n', new_result_list)

end = time.time()
runtime = end - start + simulator.runtime

print('\nLegend:')
for a in range(int(str(camo_combi))**camo_gate_number):
    print('\n', camo_gate_output[0][input_number + a], ':')
    for b in range(camo_gate_number):
        print(camo_gates[1][b], '->', camo_gate_combi[b][a])

print('\n')
print('\nCorrect combination of logic gates:',)
for a in range(camo_gate_number):
    print('\n', logic_gate2[camo_gates[0][a]][1], camo_gates[1][a], '->',
          camo_gate_combi[a][camo_gate_output[-1].index('Y') - input_number])

print('\nNumber of tries to break:', simulate_number)
print('\nRuntime is', runtime, 'sec')
