class Gates():
    def __init__(self, a, logic_gate, input_list, wire_list, output_list):
        self.a = a
        self.logic_gate = logic_gate
        self.input_list = input_list
        self.wire_list = wire_list
        self.output_list = output_list
        self.input_number = len(input_list)
        self.output_number = len(output_list)
        self.wire_number = len(wire_list)
        self.find_3 = '3_'
        self.find_4 = '4_'

    def and_gate(self):
        logic_gate = self.logic_gate
        input_list = self.input_list
        wire_list = self.wire_list
        output_list = self.output_list
        a = self.a
        input_number = self.input_number
        wire_number = self.wire_number
        output_number = self.output_number
        input1_value = None
        input2_value = None
        input3_value = None
        input4_value = None
        output1_position = None
        output1_location = 0

        if self.find_3 in logic_gate[a][1]:
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

        elif self.find_4 in logic_gate[a][1]:
            for b in range(input_number):
                if logic_gate[a][3] == input_list[0][b]:
                    input1_value = input_list[1][b]
                elif logic_gate[a][4] == input_list[0][b]:
                    input2_value = input_list[1][b]
                elif logic_gate[a][5] == output_list[0][b]:
                    input3_value = input_list[1][b]
                elif logic_gate[a][6] == output_list[0][b]:
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
        return wire_list, output_list

    def nand_gate(self):
        logic_gate = self.logic_gate
        input_list = self.input_list
        wire_list = self.wire_list
        output_list = self.output_list
        a = self.a
        input_number = self.input_number
        wire_number = self.wire_number
        output_number = self.output_number
        input1_value = None
        input2_value = None
        input3_value = None
        input4_value = None
        output1_position = None
        output1_location = 0

        if self.find_3 in logic_gate[a][1]:
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

        elif self.find_4 in logic_gate[a][1]:
            for b in range(input_number):
                if logic_gate[a][3] == input_list[0][b]:
                    input1_value = input_list[1][b]
                elif logic_gate[a][4] == input_list[0][b]:
                    input2_value = input_list[1][b]
                elif logic_gate[a][5] == output_list[0][b]:
                    input3_value = input_list[1][b]
                elif logic_gate[a][6] == output_list[0][b]:
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
        return wire_list, output_list
    
