import os
import pandas as pd
import Simulator
import Camouflage
import Attack

folder_path = os.path.join(os.getcwd(), 'Simulator\\Original Netlist\\Sample')

# corrupt_list = Camouflage.corrupt(simulator)
# print('\n', corrupt_list)

# choice = input('\n Choose 1 to camouflage, 2 to attack the logic circuit and 3 to exit.\n :')
choice = 2
while(choice != 3):
    try:
        # choice = int(input('\nSelect an option.\n 1. Camouflage\n 2. Attack\n 3. Exit\n Your choice: '))
        if choice == 1:
            file_name = 'camouflage.v'
            file_path = os.path.join(folder_path, file_name)
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
        elif choice == 2:
            file_name = 's27_clean.v'
            file_path = os.path.join(folder_path, file_name)
            reader = Simulator.Reader()
            input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
            simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
            correct_result_list = simulator.simulate()
            # print(correct_result_list, '???')

            file_name = 's27_edited.v'
            file_path = os.path.join(folder_path, file_name)
            reader = Simulator.Reader()
            input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
            simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
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
                tmp_column.append(attack_output[attack_output_keys[i]][0])
                table_columns.append(tmp_column)
            df = pd.DataFrame(table_columns, columns=columns)
            print(df)
            # choice = 3
        elif choice == 3:
            break

    except ValueError:
        print('Invalid menu choice')
        choice = 0
