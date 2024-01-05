import subprocess
import os

input_prefix = "testCases/input00"
output_prefix = "testCases/output00"
code_output_prefix = "outputCases/output00"
node_script = 'javascript.js'
# basically find the length of number of files in testCases and divide by two - input v output
number_of_files = int(len(os.listdir("./testCases"))/2)


def compare_files(file1_path, file2_path):
    """
    Compare two files line by line and print any differences.
    """
    error_found = False
    # Read the contents of the first file
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()

    # Read the contents of the second file
    with open(file2_path, 'r') as file2:
        file2_lines = file2.readlines()

    # Compare the values of each line
    for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
        value1 = line1.strip()
        value2 = line2.strip()

        if value1 != value2:
            print(f"❌ Difference at line: {i}:" )
            print(f"  {file1_path}: {value1}")
            print(f"  {file2_path}: {value2}")
            error_found = True
            break

    # Check if the files have the same number of lines
    if len(file1_lines) != len(file2_lines):
        print("❌ Files have different number of lines.")
        error_found = True

    # If there are no differences, print a success message
    elif not error_found:
        print("✅ Files are identical.")
    print("-----------------------------------------------")

def compare_outputs(intNum):
    file1=f'{code_output_prefix}{intNum}.txt'
    file2=f'{output_prefix}{intNum}.txt'
    compare_files(file1, file2)


def generate_output(intNum):
    # Define the Node.js script and input file names
    input_file = f'{input_prefix}{intNum}.txt'

    # Run the Node.js script with the input file and capture the output
    command = f'node {node_script} < "{input_file}"'
    output = subprocess.check_output(command, shell=True, text=True)

    # Define the output file name
    output_file_name = f'{code_output_prefix}{intNum}.txt'

    # Check if the output file exists, create if not
    if not os.path.exists(output_file_name):
        with open(output_file_name, 'w+'):
            pass  # Create the file

    # Write the output to the file
    with open(output_file_name, 'w') as output_file:
        output_file.write(output)

for i in range(number_of_files):
    generate_output(i)
    compare_outputs(i)