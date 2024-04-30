import os
import time

# List of files in the given order
file_list = ['Cryptography.py', 'Fernet.py', 'PyCryptodome.py', 'PyNaCl.py']

# Path to the folder containing the .py files
folder_path = '/Users/andreidanila/Desktop/ICTE Project'

# Iterate through each file and run them
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    os.system('/opt/homebrew/bin/python3 "{}"'.format(file_path))
    
    # Add a 1-minute break
    time.sleep(60)


