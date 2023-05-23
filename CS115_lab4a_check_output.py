import os
import re
import subprocess

def check_same_words_ignore_numbers(input2):
    input1 = """
        Candy Corn               $0.50    [Tax: $0.04]
        Gummy Bears              $0.10    [Tax: $0.01]
        Chocolate Chip           $2.20    [Tax: $0.16]
        Pistachio                $1.70    [Tax: $0.12]
        Vanilla                  $3.50    [Tax: $0.25]
        Oatmeal Raisin           $0.60    [Tax: $0.04]
        ----------------------------------------------
        Order Subtotals:         $8.60    [Tax: $0.62]
        Order Total:             $9.22
        Candy Corn               $0.38    [Tax: $0.03]

        Total number of items in order: 6
    """
    input1_words = set(re.findall(r'\b\w+\b', re.sub(r'\d', '', input1)))
    input2_words = set(re.findall(r'\b\w+\b', re.sub(r'\d', '', input2)))
    
    # Check whether all words from input2 are in input1
    return input2_words.issubset(input1_words)

def run_job(cmd, input_data=None):
    current_directory = os.getcwd()
    ret = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=current_directory,
        input=input_data,
        text=True,
    )
    return ret.stdout

def remove_class_files():
    for file in os.listdir('.'):
        if file.endswith('.class'):
            os.remove(file)

if __name__ == "__main__":
    # Compile
        # Get the current working directory
    current_dir = os.getcwd()


    src_dir = os.path.join(current_dir, "src")
    os.chdir(src_dir)
    # Create the path to the "src" directory
    compile_command = "javac DessertShop.java Order.java"
    compile_result = run_job(compile_command)
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        run_command = "java -cp . DessertShop"
        run_result = run_job(run_command)
        if check_same_words_ignore_numbers(run_result):
            print("OK")
        else:
            print("Make sure to match example output in the README")

    # Remove .class files
    remove_class_files()