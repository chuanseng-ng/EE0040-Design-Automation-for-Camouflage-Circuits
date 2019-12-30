import time
import reader
import simulator

start = time.time()

#   Variables
# file = input('State the netlist file name, with the file type: ')
file_name = 'camouflage.v'
read = reader.Reader()
input_list, output_list, wire_list, logic_gate, flip_flop = read.extract(file_name)
simulate_number = 0
total_number = 2 ** len(input_list[1])


result_list = []

while simulate_number != total_number:
    for i in range(len(wire_list[1])):
        wire_list[1][i] = 0

    simulation_result = simulator.simulate_stable(input_list, output_list, wire_list, logic_gate, flip_flop)
    result_list.append(simulation_result)

    input_list[1][len(input_list[1]) - 1] += 1

    temp_count = len(input_list[1]) - 1
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

print("Runtime: ", runtime, "s")
