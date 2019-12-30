from copy import deepcopy

# Function definition
def simulate(input_list, output_list, wire_list, logic_gate, flip_flop):
    ''' Simulates one cycle
    '''
    find_list = ['_AND','_NAND','_OR','_NOR','_XOR','_XNOR','_IV']
    # name of input: number of inputs
    input_param_names = {'2X':2, '3X':3, '4X':4}

    output_number = len(output_list[0])
    wire_number = len(wire_list[0])
    flip_flop_number = len(flip_flop)

    input_values = []
    output1_position = 0

    for gate in logic_gate:
        # Logic gate name always at position 0
        output1_location = 0

        for key in input_param_names:
            if key in gate[0]:
                param_num = input_param_names[key]
                input_values = [0]*param_num
                input_values = _input_match(input_list, gate, param_num)
                input_values, output1_location, output1_position = _wire_match(input_values, wire_list, gate, output1_location, output1_position, param_num)
                input_values = _output_match(input_values, output_list, gate, param_num)
                output1_location, output1_position = _logic_output_match(gate, output1_location, output1_position, output_list)
                for find in find_list:
                    if find in gate[0]:
                        output1_value = _logic_output_calc(find, input_values)
        wire_list, output_list = _update_node(wire_list, output_list, output1_location, output1_position, output1_value)

        # Flip flop logic
        if flip_flop_number != 0:
            for g in range(flip_flop_number):
                for h in range(wire_number):
                    if flip_flop[g][2] == wire_list[0][h]:
                        for i in range(wire_number):
                            if flip_flop[g][5] == wire_list[0][i]:
                                wire_list[1][i] = wire_list[1][h]
                        for j in range(output_number):
                            if flip_flop[g][5] == output_list[0][j]:
                                output_list[1][j] = wire_list[1][h]
    return output_list, wire_list

def simulate_stable(input_list, output_list, wire_list, logic_gate, flip_flop, upper_limit=10):
    ''' Simulate until stable by comparing results in each cycle of simulation
    '''
    result_output_list = []
    tmp_result_output = deepcopy(output_list)
    tmp_result_wire = deepcopy(wire_list)
    for _ in range(upper_limit):
        tmp_result_output, tmp_result_wire = simulate(input_list, tmp_result_output, tmp_result_wire, logic_gate, flip_flop)
        result_output_list.append(tmp_result_output)
        if len(result_output_list) > 1:
            if result_output_list[-1] == result_output_list[-2]:
                break
    return result_output_list[-1][1]

def _input_match(input_list, gate, param_num):
    values_list = [0]*param_num
    for i in range(len(input_list[0])):
        for j in range(param_num):
            if gate[3+j] == input_list[0][i]:
                values_list[j] = input_list[1][i]
    return values_list

def _wire_match(input_values, wire_list, gate, output1_location, output1_position, param_num):
    values_list = deepcopy(input_values)
    for i in range(len(wire_list[0])):
        for j in range(param_num):
            if gate[3+j] == wire_list[0][i]:
                values_list[j] = wire_list[1][i]
        if gate[2] == wire_list[0][i]:
            output1_location = 1
            output1_position = i
    return values_list, output1_location, output1_position

def _output_match(input_values, output_list, gate, param_num):
    values_list = deepcopy(input_values)
    for i in range(len(output_list[0])):
        for j in range(param_num):
            if gate[3+j] == output_list[0][i]:
                values_list[j] = output_list[1][i]
    return values_list

def _logic_output_match(gate, output1_location, output1_position, output_list):
    if output1_location == 0:
        for i in range(len(output_list[0])):
            if gate[2] == output_list[0][i]:
                output1_location = 2
                output1_position = i
    return output1_location, output1_position

def _logic_output_calc(gate_type: str, input_values: list):
    if gate_type == '_AND':
        for value in input_values:
            if value == 0:
                return 0
        return 1
    elif gate_type == '_NAND':
        for value in input_values:
            if value == 0:
                return 1
        return 0
    elif gate_type == '_OR':
        for value in input_values:
            if value == 1:
                return 1
        return 0
    elif gate_type == '_NOR':
        for value in input_values:
            if value == 1:
                return 0
        return 1
    elif gate_type == '_XOR':
        count = [0,0]
        for value in input_values:
            if value == 0:
                count[0] += 1
            else:
                count[1] += 1
        if count[0] == 0 or count[1] == 0:
            return 0
        return 1
    elif gate_type == '_XNOR':
        count = [0,0]
        for value in input_values:
            if value == 0:
                count[0] += 1
            else:
                count[1] += 1
        if count[0] == 0 or count[1] == 0:
            return 1
        return 0
    elif gate_type == '_IV':
        if len(input_values) > 1:
            raise Exception('Inverter only takes 1 input!')
        for value in input_values:
            if value == 1:
                return 0
        return 1
    else:
        raise Exception('Logic gate unknown.')

def _update_node(wire_list, output_list, output1_location, output1_position, output1_value):
    ''' Returns updated wire_list, output_list
    '''
    if output1_location == 1:
        tmp_list = deepcopy(wire_list)
        tmp_list[1][output1_position] = output1_value
        return tmp_list, output_list
    else:
        tmp_list = deepcopy(output_list)
        tmp_list[1][output1_position] = output1_value
        return wire_list, tmp_list
