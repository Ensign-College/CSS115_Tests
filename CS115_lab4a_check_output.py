import subprocess
import os


def remove_main(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file: {e.filename} - {e.strerror}")


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


def check_output(output, numbers):
    for number in numbers:
        if (
            "The sum of the list of numbers is" or "The largest number in the list is"
        ) not in output:
            return False
    return True


if __name__ == "__main__":
    # Compile
    compile_command = "javac Lab4a/DessertShop.java"
    compile_result = run_job(compile_command)
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        run_command = "java -cp . Lab4a.DessertShop"
        run_result = run_job(run_command)
        print(f"{run_result}")

        # Remove .class file
        remove_main("Lab4a/DessertShop.class")
