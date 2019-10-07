def read_wire_list(file):
    # Variables declaration
    #   Lists
    logic_gate = []
    flip_flop = []
    input_list = []
    output_list = []
    wire_list = []
    
    find_gate = '.A'
    find_flip = '.D'
    find_input = 'input'
    find_output = 'output'
    find_wire = 'wire'

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
    return logic_gate, flip_flop, input_list, output_list, wire_list

def get_input_output_list(input_list):
    for w in range(len(input_list)):
        input_list[w] = input_list[w].split(',')
        for x in range(len(input_list[w])):
            input_list[w][x] = input_list[w][x].replace('input ', '')
            input_list[w][x] = input_list[w][x].replace('CLK', '')
            input_list[w][x] = input_list[w][x].replace('NRST', '')
            input_list[w][x] = input_list[w][x].replace(';', '')
        input_list[w] = list(filter(None, input_list[w]))
    return input_list

def remove_nonsense(gate):
    for w in range(len(gate)):
        gate[w] = gate[w].split()
        for x in range(len(gate[w])):
            gate[w][x] = gate[w][x].replace(';', '')
            gate[w][x] = gate[w][x].replace('(', '')
            gate[w][x] = gate[w][x].replace(')', '')
            gate[w][x] = gate[w][x].replace(',', '')
            gate[w][x] = gate[w][x].replace('.A', '')
            gate[w][x] = gate[w][x].replace('.B', '')
            gate[w][x] = gate[w][x].replace('.C', '')
            gate[w][x] = gate[w][x].replace('.D', '')
            gate[w][x] = gate[w][x].replace('.Z', '')
            gate[w][x] = gate[w][x].replace('.D', '')
            gate[w][x] = gate[w][x].replace('.Q', '')
            gate[w][x] = gate[w][x].replace('.CP', '')
            gate[w][x] = gate[w][x].replace('.RN', '')
            gate[w][x] = gate[w][x].replace('wire ', '')
        gate[w] = list(filter(None, gate[w]))
    return gate

def get_xinv_number(logic_gate_number):
    inv_count = 0
    for w in range(logic_gate_number):
        if '_IV' in logic_gate[w][0]:
            inv_count = inv_count + 1
        else:
            pass
    logic_gate_xinv_number = logic_gate_number - inv_count
    return logic_gate_xinv_number