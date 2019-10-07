import util
import simulator
import time
start = time.time()

#   Variables
#file = input('State the netlist file name, with the file type: ')
result_list = []

input_number = 0
output_number = 0
logic_gate_number = 0
flip_flop_number = 0
wire_number = 0
logic_gate_xinv_number = 0
inv_count = 0
simulate_number = 0
total_number = 0

file = 's27_edited.v'
logic_gate, flip_flop, input_list, output_list, wire_list = util.read_wire_list(file)

input_list = util.get_input_output_list(input_list)
input_number = len(input_list[0])

# Reset input values to 0
for w in range(input_number):
    input_list[1][w] = 0

output_list = util.get_input_output_list(output_list)
output_number = len(output_list[0])

# Reset output values to 0
for w in range(output_number):
    output_list[1][w] = 0


logic_gate = util.remove_nonsense(logic_gate)
flip_flop = util.remove_nonsense(flip_flop)
wire_list = util.remove_nonsense(wire_list)

logic_gate_xinv_number = util.get_xinv_number(len(logic_gate))
wire_number = len(wire_list[0])

# Reset wire values to 0
for w in range(wire_number):
    wire_list[1][w] = 0

total_number = 2**input_number

while simulate_number != total_number:
    for w in range(wire_number):
        wire_list[1][w] = 0

    updated_wire, updated_output = simulator.initial_simulate(input_list, output_list, wire_list, logic_gate, flip_flop)
    result_list.append(simulator.final_simulate(input_list, updated_output, updated_wire, logic_gate, flip_flop))

    input_list[1][input_number-1] += 1

    temp_count = input_number - 1
    while temp_count > -1:
        if input_list[1][temp_count] == 2:
            input_list[1][temp_count] = 0
            input_list[1][temp_count - 1] += 1
        temp_count -= 1

    simulate_number += 1

for w in range(len(result_list)):
    print('\n', result_list[w])

end = time.time()

runtime = end - start
