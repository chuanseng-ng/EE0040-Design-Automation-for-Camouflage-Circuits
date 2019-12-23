import os

class Reader:
    def __init__(self):
        self.logic_gate = []
        self.flip_flop = []
        self.input_list = []
        self.output_list = []
        self.wire_list = []
        self.result_list = []

        self.find_gate = '.A'
        self.find_flip = '.D'
        self.find_input = 'input'
        self.find_output = 'output'
        self.find_wire = 'wire'

        self.input_number = 0
        self.output_number = 0
        self.wire_number = 0

    def whatever(self, file_name):
        # Variables declaration
        #   Lists
        # Read file and store them into list of strings
        self._extract_lists(file_name)
        self._process_lists('input')
        self._process_lists('output')
        self._process_lists('wire')
        self._process_logic_lists('logic_gate')
        self._process_logic_lists('flip_flop')

        return self.input_list, self.output_list, self.wire_list, self.logic_gate, self.flip_flop

    def _extract_lists(self, file_name):
        print(os.getcwd())
        with open(file_name) as f:
            line_list = [line.rstrip('\n') for line in f]
        # Finding keywords from list of string
        #   List[1] is to store values
        for line in line_list:
            if self.find_input in line:
                self.input_list.append(line)
                self.input_list.append(line)
            if self.find_output in line:
                self.output_list.append(line)
                self.output_list.append(line)
            if self.find_gate in line:
                self.logic_gate.append(line)
            if self.find_flip in line:
                self.flip_flop.append(line)
            if self.find_wire in line:
                self.wire_list.append(line)
                self.wire_list.append(line)

    def _process_lists(self, list_type):
        replace_input_list = ['input ', 'CLK', 'NRST', ';']
        replace_output_list = ['output ', ';']
        replace_wire_list = ['wire ', ';']

        replace_list = []
        if list_type == 'input':
            replace_list = replace_input_list
            tmp_list = self.input_list
        elif list_type == 'output':
            replace_list = replace_output_list
            tmp_list = self.output_list
        elif list_type == 'wire':
            replace_list = replace_wire_list
            tmp_list = self.wire_list
        else:
            raise Exception('Invalid list type.')

        for i, line in enumerate(tmp_list):
            line = line.split(',')
            for j in range(len(line)):
                for item in replace_list:
                    line[j] = line[j].replace(item, '')
            tmp_list[i] = list(filter(None, line))
            tmp_number = len(tmp_list[i])
        # Reset input values to 0
        for i in range(tmp_number):
            tmp_list[1][i] = 0
        print(tmp_list)

    def _process_logic_lists(self, list_type):
        replace_logic_gate = ['(', ')', ',','.A','.B','.C','.D','.Z',';']
        replace_flip_flop_list = ['(', ')', ',','.D','.Q','.CP','.RN',';']

        replace_list = []
        if list_type == 'logic_gate':
            replace_list = replace_logic_gate
            tmp_list = self.logic_gate
        elif list_type == 'flip_flop':
            replace_list = replace_flip_flop_list
            tmp_list = self.flip_flop
        else:
            raise Exception('Invalid list type.')

        for i, line in enumerate(tmp_list):
            line = line.split(',')
            for j in range(len(line)):
                for item in replace_list:
                    line[j] = line[j].replace(item, '')
            tmp_list[i] = list(filter(None, line))

        print(tmp_list)
