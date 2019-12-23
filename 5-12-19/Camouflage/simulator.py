

# Function definition
def initial_simulate(input_list, output_list, wire_list, logic_gate, flip_flop):
    find_and = '_AND'
    find_nand = '_NAND'
    find_or = '_OR'
    find_nor = '_NOR'
    find_xor = '_XOR'
    find_xnor = '_XNOR'
    find_inv = '_IV'

    find_3 = '3_'
    find_4 = '4_'

    input1_value = 0
    input2_value = 0
    input3_value = 0
    input4_value = 0
    output1_value = 0
    output1_location = 0
    output1_position = 0

    for l in range(len(input_list)):
        input_number = len(input_list[l])
    for l in range(len(output_list)):
        output_number = len(output_list[l])
    for l in range(len(wire_list)):
        wire_number = len(wire_list[l])
    logic_gate_number = len(logic_gate)
    flip_flop_number = len(flip_flop)

    for a in range(logic_gate_number):

        if find_and in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_nand in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_or in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_nor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_xor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 1:
                    output1_value = 1
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == input2_value:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_xnor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 1:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 1
                elif input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == input2_value:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                output_list[1][output1_position] = output1_value

        elif find_inv in logic_gate[a][0]:
            output1_location = 0

            for b in range(input_number):
                if logic_gate[a][3] == input_list[0][b]:
                    input1_value = input_list[1][b]
                else:
                    pass

            for c in range(wire_number):
                if logic_gate[a][3] == wire_list[0][c]:
                    input1_value = wire_list[1][c]
                elif logic_gate[a][2] == wire_list[0][c]:
                    output1_location = 1
                    output1_position = c

            for d in range(output_number):
                if logic_gate[a][3] == output_list[0][d]:
                    input1_value = output_list[1][d]
                else:
                    pass

            if output1_location == 0:
                for f in range(output_number):
                    if logic_gate[a][2] == output_list[0][f]:
                        output1_location = 2
                        output1_position = f
                    else:
                        pass
            else:
                pass

            if input1_value == 0:
                output1_value = 1
            elif input1_value == 1:
                output1_value = 0
            else:
                pass

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            elif output1_location == 2:
                output_list[1][output1_position] = output1_value
            else:
                pass

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

    find_3 = '3_'
    find_4 = '4_'

    input1_value = 0
    input2_value = 0
    input3_value = 0
    input4_value = 0
    output1_value = 0
    output1_location = 0
    output1_position = 0

    result_list = []

    for l in range(len(input_list)):
        input_number = len(input_list[l])
    for l in range(len(output_list)):
        output_number = len(output_list[l])
    for l in range(len(wire_list)):
        wire_number = len(wire_list[l])
    logic_gate_number = len(logic_gate)
    flip_flop_number = len(flip_flop)

    result_list = [0 for x in range(output_number)]

    for a in range(logic_gate_number):
        if find_and in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_nand in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 1 and input2_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_or in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_nor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_xor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 1:
                    output1_value = 1
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == input2_value:
                    output1_value = 0
                else:
                    output1_value = 1

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_xnor in logic_gate[a][0]:
            output1_location = 0

            if find_3 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 1:
                    output1_value = 0
                elif input1_value == 1 and input2_value == 1 and input3_value == 1:
                    output1_value = 0
                else:
                    output1_value = 1

            elif find_4 in logic_gate[a][1]:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    elif logic_gate[a][5] == input_list[0][b]:
                        input3_value = input_list[1][b]
                    elif logic_gate[a][6] == input_list[0][b]:
                        input4_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][5] == wire_list[0][c]:
                        input3_value = wire_list[1][c]
                    elif logic_gate[a][6] == wire_list[0][c]:
                        input4_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    elif logic_gate[a][5] == output_list[0][d]:
                        input3_value = output_list[1][d]
                    elif logic_gate[a][6] == output_list[0][d]:
                        input4_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == 0 and input2_value == 0 and input3_value == 0 and input4_value == 0:
                    output1_value = 1
                elif input1_value == 1 and input2_value == 1 and input3_value == 1 and input4_value == 1:
                    output1_value = 1
                else:
                    output1_value = 0

            else:
                for b in range(input_number):
                    if logic_gate[a][3] == input_list[0][b]:
                        input1_value = input_list[1][b]
                    elif logic_gate[a][4] == input_list[0][b]:
                        input2_value = input_list[1][b]
                    else:
                        pass

                for c in range(wire_number):
                    if logic_gate[a][3] == wire_list[0][c]:
                        input1_value = wire_list[1][c]
                    elif logic_gate[a][4] == wire_list[0][c]:
                        input2_value = wire_list[1][c]
                    elif logic_gate[a][2] == wire_list[0][c]:
                        output1_location = 1
                        output1_position = c

                for d in range(output_number):
                    if logic_gate[a][3] == output_list[0][d]:
                        input1_value = output_list[1][d]
                    elif logic_gate[a][4] == output_list[0][d]:
                        input2_value = output_list[1][d]
                    else:
                        pass

                if output1_location == 0:
                    for f in range(output_number):
                        if logic_gate[a][2] == output_list[0][f]:
                            output1_location = 2
                            output1_position = f
                        else:
                            pass
                else:
                    pass

                if input1_value == input2_value:
                    output1_value = 1
                else:
                    output1_value = 0

            if output1_location == 1:
                wire_list[1][output1_position] = output1_value
            else:
                result_list[output1_position] = output1_value

        elif find_inv in logic_gate[a][0]:
            output1_location = 0

            for b in range(input_number):
                if logic_gate[a][3] == input_list[0][b]:
                    input1_value = input_list[1][b]
                else:
                    pass

            for c in range(wire_number):
                if logic_gate[a][3] == wire_list[0][c]:
                    input1_value = wire_list[1][c]
                elif logic_gate[a][2] == wire_list[0][c]:
                    output1_location = 1
                    output1_position = c

            for d in range(output_number):
                if logic_gate[a][3] == output_list[0][d]:
                    input1_value = output_list[1][d]
                else:
                    pass

            if output1_location == 0:
                for f in range(output_number):
                    if logic_gate[a][2] == output_list[0][f]:
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

    return result_list

