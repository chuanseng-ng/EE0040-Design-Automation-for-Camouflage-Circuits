import os
import Simulator
import Camouflage
import Attack
folder_path = os.path.join(os.getcwd(), 'Simulator\\Original Netlist\\Sample')
file_name = 'camouflage.v'
file_path = os.path.join(folder_path, file_name)

# corrupt_list = Camouflage.corrupt(simulator)
# print('\n', corrupt_list)

choice = 0
choice = 2
# while(choice != 3):
try:
    # choice = int(input('\nSelect an option.\n 1. Camouflage\n 2. Attack\n 3. Exit\n Your choice: '))
    if choice == 1:
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
                print('\n Camouflaging {}% of total logic gates.'.format(camo_num))
            else:
                print('\n Invalid input. Camouflaging 10% of total logic gates.')
                camo_num = int(len(simulator.logic_gate)*0.1)
        except ValueError:
            print('\n Invalid input. Camouflaging 10% of total logic gates.')
            camo_num = int(len(simulator.logic_gate)*0.1)

        Camouflage.camouflage_research.camouflage(simulator, camo_num)
    elif choice == 2:
        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        correct_result_list = simulator.simulate()

        file_name = 'camouflage_edited.v'
        file_path = os.path.join(folder_path, file_name)
        reader = Simulator.Reader()
        input_list, output_list, wire_list, logic_gate, flip_flop = reader.extract(file_path)
        simulator = Simulator.Simulator(file_path, input_list, output_list, wire_list, logic_gate, flip_flop)
        Attack.attack(simulator, correct_result_list)

except ValueError:
    print('Invalid menu choice')
    choice = 0


# %%
