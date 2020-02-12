import os
import sys
import pandas as pd
import Simulator
import Camouflage
import Attack
import Utils
import time

# folder_path = os.path.join(os.getcwd(), 'Simulator\\Original Netlist\\Sample')

camo_attack_choice = int(input('\n Choose 1 to camouflage, 2 to attack the logic circuit: '))
start = time.time()
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
        user_input = input('\n State percentage of gates to be camouflaged.\n Default choice is 10% of total logic gates. (%): ')
        start = time.time()

        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)

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
        #print('\nRuntime: {0:.5f} seconds'.format(time.time() - start))

    elif camo_attack_choice == 2:
        camo_choice = int(input('{} Select Camo file: '.format(file_str))) - 1
        if camo_choice < 0 or camo_choice >= len(files):
            print('Invalid choice')
            sys.exit()
        if camo_choice == choice:
            print('Same file selected for camo and clean!')
            sys.exit()
        camo_file_path = os.path.join(os.getcwd(), 'Netlist\\{}'.format(files[camo_choice]))

        print("\nPlease input the camouflaged gate combinations, one at a time. \n")
        print("1 - AND \n")
        print("2 - NAND \n")
        print("3 - OR \n")
        print("4 - NOR \n")
        print("5 - XOR \n")
        print("6 - XNOR \n")
        print("7 - End \n")

        user_input = input("Selection: ")
        chosen_camo = []
        while user_input != "7":
            if user_input == "1":
                chosen_camo.append('HS65_LH_AND2X4')
                user_input = input("Selection: ")
            elif user_input == "2":
                chosen_camo.append('HS65_LH_NAND2X2')
                user_input = input("Selection: ")
            elif user_input == "3":
                chosen_camo.append('HS65_LH_OR2X4')
                user_input = input("Selection: ")
            elif user_input == "4":
                chosen_camo.append('HS65_LH_NOR2X2')
                user_input = input("Selection: ")
            elif user_input == "5":
                chosen_camo.append('HS65_LH_XOR2X3')
                user_input = input("Selection: ")
            elif user_input == "6":
                chosen_camo.append('HS65_LH_XNOR2X3')
                user_input = input("Selection: ")
            else:
                break
        print('\n')

        start = time.time()

        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        correct_result_list = simulator.simulate()

        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(camo_file_path)
        simulator = Simulator.Simulator(camo_file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        attack_output, camo_gate_names = Attack.attack(chosen_camo, simulator, correct_result_list)

        print('\n')
        attack_output_keys = list(attack_output.keys())
        columns = camo_gate_names + ['Result']
        table_columns = []
        for i in range(len(attack_output_keys)):
            tmp_column = []
            for j in range(len(attack_output_keys[0])):
                tmp_column.append(attack_output_keys[i][j])
            tmp_column.append(attack_output[attack_output_keys[i]])
            table_columns.append(tmp_column)
        df = pd.DataFrame(table_columns, columns=columns)
        print(df.to_string())

        count = 0
        result = [item.tolist() for item in df.values if item[-1][-1] == 'Y']
        print('\nPossible Correct Combination: ')
        for item in result:
            print('{}'.format(item[:-1]))
            count += 1
        print('\nNumber of tries: {}' .format(len(df.values[-1][-1])))
        print('\nNumber of possible combinations: {}' .format(count))

    else:
        print('Invalid choice')

    runtime = time.time() - start
    #print('\nRuntime: {} seconds'.format(runtime))
    if(int(runtime/60) == 0):
        print('\nRuntime: {0:.5f} seconds'.format(runtime))
    elif(int(runtime/3600) == 0):
        print('\nRuntime: {0:} minutes {1:.5f} seconds'.format(int(runtime/60), runtime % 60))
    elif(int(runtime/3600) != 0):
        print('\nRuntime: {0:} hours {1:} minutes {2:.5f} seconds'.format(int(runtime/3600), int((runtime/60) % 60), runtime % 3600))

except ValueError:
    print('Invalid menu choice')

except Exception as e:
    print(e)
