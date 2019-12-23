import time

start = time.time()


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


# Variables declaration
#   Lists
logic_gate = []
flip_flop = []
input_list = []
output_list = []
wire_list = []
result_list = []


#   Variables
#file = input('State the netlist file name, with the file type: ')
file = 'camouflage.v'
find_gate = '.A'
find_flip = '.D'
find_input = 'input'
find_output = 'output'
find_wire = 'wire'

input_number = 0
output_number = 0
logic_gate_number = 0
flip_flop_number = 0
wire_number = 0
simulate_number = 0
total_number = 0


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


# Reset wire values to 0
for w in range(wire_number):
    wire_list[1][w] = 0

total_number = 2**input_number
print(input_list, '\n', output_list,'\n', wire_list,'\n', logic_gate,'\n', flip_flop,'\n')
while simulate_number != total_number:
    for w in range(wire_number):
        wire_list[1][w] = 0

    updated_wire, updated_output = initial_simulate(input_list, output_list, wire_list, logic_gate, flip_flop)
    result_list.append(final_simulate(input_list, updated_output, updated_wire, logic_gate, flip_flop))

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
