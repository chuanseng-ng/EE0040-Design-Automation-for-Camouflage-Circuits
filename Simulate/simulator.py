from gates import Gates


# Function definition
def initial_simulate(input_list, output_list, wire_list, logic_gate, flip_flop):
    find_and = '_AND'
    find_nand = '_NAND'
    find_or = '_OR'
    find_nor = '_NOR'
    find_xor = '_XOR'
    find_xnor = '_XNOR'
    find_inv = '_IV'

    output_number = len(output_list[0])
    wire_number = len(wire_list[0])
    logic_gate_number = len(logic_gate)
    flip_flop_number = len(flip_flop)
    
    for a in range(logic_gate_number):
        gates = Gates(a, logic_gate, input_list, wire_list, output_list)

        if find_and in logic_gate[a][0]:
            wire_list, output_list = gates.and_gate()

        elif find_nand in logic_gate[a][0]:
            wire_list, output_list = gates.nand_gate()

        elif find_or in logic_gate[a][0]:
            wire_list, output_list = gates.or_gate()

        elif find_nor in logic_gate[a][0]:
            wire_list, output_list = gates.nor_gate()

        elif find_xor in logic_gate[a][0]:
            wire_list, output_list = gates.xor_gate()

        elif find_xnor in logic_gate[a][0]:
            wire_list, output_list = gates.xnor_gate()

        elif find_inv in logic_gate[a][0]:
            wire_list, output_list = gates.inv_gate()

        else:
            pass

        if flip_flop_number != 0:
            for g in range(flip_flop_number):
                for h in range(wire_number):
                    if flip_flop[g][2] == wire_list[0][h]:
                        for i in range(wire_number):
                            if flip_flop[g][5] == wire_list[0][i]:
                                wire_list[1][i] = wire_list[1][h]
                            else:
                                pass
                        for j in range(output_number):
                            if flip_flop[g][5] == output_list[0][j]:
                                output_list[1][j] = wire_list[1][h]
                    else:
                        pass
        else:
            pass

    return wire_list, output_list


def final_simulate(input_list, output_list, wire_list, logic_gate, flip_flop):
    find_and = '_AND'
    find_nand = '_NAND'
    find_or = '_OR'
    find_nor = '_NOR'
    find_xor = '_XOR'
    find_xnor = '_XNOR'
    find_inv = '_IV'

    result_list = []

    input_number = len(input_list[0])
    output_number = len(output_list[0])
    wire_number = len(wire_list[0])
    logic_gate_number = len(logic_gate)
    flip_flop_number = len(flip_flop)

    result_list = [0 for x in range(output_number)]

    for a in range(flip_flop_number):
        if flip_flop[a][5] not in output_list[0]:
            for c in range(wire_number):
                if flip_flop[a][2] == wire_list[0][c]:
                    wire_list[1][c] = 0
                else:
                    pass
        else:
            pass

    for a in range(logic_gate_number):
        gates = Gates(a, logic_gate, input_list, wire_list, output_list)

        if find_and in logic_gate[a][0]:
            wire_list, output_list = gates.and_gate()

        elif find_nand in logic_gate[a][0]:
            wire_list, output_list = gates.nand_gate()

        elif find_or in logic_gate[a][0]:
            wire_list, output_list = gates.or_gate()

        elif find_nor in logic_gate[a][0]:
            wire_list, output_list = gates.nor_gate()

        elif find_xor in logic_gate[a][0]:
            wire_list, output_list = gates.xor_gate()

        elif find_xnor in logic_gate[a][0]:
            wire_list, output_list = gates.xnor_gate()

        elif find_inv in logic_gate[a][0]:
            wire_list, output_list = gates.inv_gate()

        else:
            pass

        # Transfer Flip-Flop input value to output
        if flip_flop_number != 0:
            for g in range(flip_flop_number):
                for h in range(wire_number):
                    if flip_flop[g][2] == wire_list[0][h]:
                        for i in range(wire_number):
                            if flip_flop[g][5] == wire_list[0][i]:
                                wire_list[1][i] = wire_list[1][h]
                            else:
                                pass
                        for j in range(output_number):
                            if flip_flop[g][5] == output_list[0][j]:
                                result_list[j] = wire_list[1][h]
                            else:
                                pass
                    else:
                        pass

    for a in range(output_number):
        for b in range(logic_gate_number):
            if output_list[0][a] == logic_gate[b][2]:
                if find_inv in logic_gate[b][0]:
                    for c in range(logic_gate_number):
                        if logic_gate[b][3] == logic_gate[c][2]:
                            gates = Gates(c, logic_gate, input_list, wire_list, output_list)

                            if find_and in logic_gate[c][0]:
                                wire_list, output_list = gates.and_gate()

                            elif find_nand in logic_gate[c][0]:
                                wire_list, output_list = gates.nand_gate()

                            elif find_or in logic_gate[c][0]:
                                wire_list, output_list = gates.or_gate()

                            elif find_nor in logic_gate[c][0]:
                                wire_list, output_list = gates.nor_gate()

                            elif find_xor in logic_gate[c][0]:
                                wire_list, output_list = gates.xor_gate()

                            elif find_xnor in logic_gate[c][0]:
                                wire_list, output_list = gates.xnor_gate()

                            elif find_inv in logic_gate[c][0]:
                                wire_list, output_list = gates.inv_gate()

                            else:
                                pass
                    output1_location = 0

                    for c in range(input_number):
                        if logic_gate[b][3] == input_list[0][c]:
                            input1_value = input_list[1][c]
                        else:
                            pass

                    for c in range(wire_number):
                        if logic_gate[b][3] == wire_list[0][c]:
                            input1_value = wire_list[1][c]
                        elif logic_gate[b][2] == wire_list[0][c]:
                            output1_location = 1
                            output1_position = c

                    for d in range(output_number):
                        if logic_gate[b][3] == output_list[0][d]:
                            input1_value = output_list[1][d]
                        else:
                            pass

                    if output1_location == 0:
                        for f in range(output_number):
                            if logic_gate[b][2] == output_list[0][f]:
                                output1_location = 2
                                output1_position = f
                            else:
                                pass
                    else:
                        pass

                    if input1_value == 0:
                        output1_value = 1
                    else:
                        output1_value = 0

                    if output1_location == 1:
                        wire_list[1][output1_position] = output1_value
                    else:
                        result_list[output1_position] = output1_value

                else:
                    gates = Gates(b, logic_gate, input_list, wire_list, output_list)

                    if find_and in logic_gate[b][0]:
                        wire_list, output_list = gates.and_gate()

                    elif find_nand in logic_gate[b][0]:
                        wire_list, output_list = gates.nand_gate()

                    elif find_or in logic_gate[b][0]:
                        wire_list, output_list = gates.or_gate()

                    elif find_nor in logic_gate[b][0]:
                        wire_list, output_list = gates.nor_gate()

                    elif find_xor in logic_gate[b][0]:
                        wire_list, output_list = gates.xor_gate()

                    elif find_xnor in logic_gate[b][0]:
                        wire_list, output_list = gates.xnor_gate()

                    else:
                        pass
            else:
                for c in range(flip_flop_number):
                    if output_list[0][a] == flip_flop[c][5]:
                        for d in range(wire_number):
                            if flip_flop[c][2] == wire_list[0][d]:
                                output_list[1][a] = wire_list[1][d]
                            else:
                                pass
                    else:
                        pass

    return result_list

