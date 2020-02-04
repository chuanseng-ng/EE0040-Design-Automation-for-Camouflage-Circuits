import os
import sys
import pandas as pd
import Simulator
import Camouflage
import Attack
import Utils

# folder_path = os.path.join(os.getcwd(), 'Simulator\\Original Netlist\\Sample')

camo_attack_choice = int(input('\n Choose 1 to camouflage, 2 to attack the logic circuit: '))
try:
    files = Utils.get_verilog_files()
    file_str = '\n Files detected: \n'
    if len(files) == 0:
        print('No files found in Netlist!')
        sys.exit()
    for i in range(len(files)):
        file_str += '{}. {}\n'.format(i+1, files[i])

    choice = int(input('{} Select clean file: '.format(file_str))) - 1
    if choice < 0 or choice >= len(files):
        print('Invalid choice')
    file_path = os.path.join(os.getcwd(), 'Netlist\\{}'.format(files[choice]))

    if camo_attack_choice == 1:
        # file_name = 'camouflage.v'
        # file_path = os.path.join(folder_path, file_name)
        print(file_path)
        reader = Simulator.Reader()

        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        user_input = input('\n State percentage of gates to be camouflaged.\n Default choice is 10% of total logic gates. (%): ')

        try:
            camo_num = int(int(user_input) * len(simulator.logic_gate) * 0.01)
            if camo_num <= 0:
                print('\n No gates selected to be camouflaged. Camouflaging 10% of total logic gates.')
                camo_num = int(len(simulator.logic_gate)*0.1)
            elif camo_num > 0 and camo_num <= len(simulator.logic_gate):
                print('\n Camouflaging {}% of total logic gates.'.format(int(user_input)))
            else:
                print('\n Invalid input. Camouflaging 10% of total logic gates.')
                camo_num = int(len(simulator.logic_gate)*0.1)
        except ValueError:
            print('\n Invalid input. Camouflaging 10% of total logic gates.')
            camo_num = int(len(simulator.logic_gate)*0.1)

        Camouflage.camouflage(simulator, camo_num)
    elif camo_attack_choice == 2:
        camo_choice = int(input('{} Select Camo file: '.format(file_str))) - 1
        if camo_choice < 0 or camo_choice >= len(files):
            print('Invalid choice')
            sys.exit()
        if camo_choice == choice:
            print('Same file selected for camo and clean!')
            sys.exit()
        camo_file_path = os.path.join(os.getcwd(), 'Netlist\\{}'.format(files[camo_choice]))

        # file_name = 's27_clean.v'
        # file_path = os.path.join(folder_path, file_name)
        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        correct_result_list = simulator.simulate()
        # print(correct_result_list, '???')

        # file_name = 's27_edited.v'
        # file_path = os.path.join(folder_path, file_name)
        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(camo_file_path)
        simulator = Simulator.Simulator(camo_file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        attack_output, camo_gate_names = Attack.attack(simulator, correct_result_list)

        print('\n')
        attack_output_keys = list(attack_output.keys())
        # print(camo_gate_names)
        columns = camo_gate_names + ['Result']
        # print(columns)
        table_columns = []
        for i in range(len(attack_output_keys)):
            tmp_column = []
            for j in range(len(attack_output_keys[0])):
                tmp_column.append(attack_output_keys[i][j])
            tmp_column.append(attack_output[attack_output_keys[i]])
            table_columns.append(tmp_column)
        df = pd.DataFrame(table_columns, columns=columns)
        print(df)
    else:
        print('Invalid choice')

except ValueError:
    print('Invalid menu choice')

except Exception as e:
    print(e)
