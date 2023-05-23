import os
import subprocess

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
        # List the contents of the current directory
    contents = os.listdir(src_dir)

    # Print the contents
    for item in contents:
        print(item)
    # Create the path to the "src" directory
    compile_command = "javac DessertShop.java Order.java"
    compile_result = run_job(compile_command)
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        run_command = "java -cp . DessertShop"
        run_result = run_job(run_command)
        print(f"{run_result}")

    # Remove .class files
    remove_class_files()
