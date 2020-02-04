import os
import sys

def get_verilog_files(folder_path='Netlist'):
    folder_path = os.path.join(os.getcwd(), folder_path)
    files = [f for f in os.listdir(folder_path) if f[-2:] == '.v']
    print('file:',files) 
    return files
