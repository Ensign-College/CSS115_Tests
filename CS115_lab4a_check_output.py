import os
import subprocess

def check_output(output, expected_output):
    # Remove all styling (whitespaces, newlines, and punctuation)
    output = ''.join(e for e in output if e.isalnum())
    expected_output = ''.join(e for e in expected_output if e.isalnum())

    # Convert both strings to lowercase
    output = output.lower()
    expected_output = expected_output.lower()

    # Check if the modified output matches the modified expected output
    return output == expected_output    
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
        print(f"{run_result}")
        if check_ouput(run_result) == True: 
            print("OK")

    # Remove .class files
    remove_class_files()
