import os
import subprocess
import requests
class Colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def run_java_junit_test(java_file, test_file, classpath):
    # Compile Java source files
    compile_command = f"javac -cp {classpath} {java_file} {test_file}"
    compile_process = subprocess.run(compile_command, shell=True, capture_output=True)

    if compile_process.returncode != 0:
        print("Compilation failed:")
        print(compile_process.stderr.decode("utf-8"))
        if "assertEquals" in compile_process.stderr.decode("utf-8"):
            print(f"{Colors.RED}Your test cases are not compiling. Try changing {Colors.BG_WHITE}assertEquals to Assert.assertEquals or import correct Test Case library{Colors.RESET}")
        return

    # Run JUnit test
    class_name = test_file.split(".")[0]
    run_command = f"java -cp {classpath}:. org.junit.runner.JUnitCore {class_name}"
    run_process = subprocess.run(run_command, shell=True, capture_output=True)

    stderr_output = run_process.stderr.decode("utf-8")

    if run_process.returncode == 0 and "FAILURES" not in stderr_output:
        print("All tests passed successfully")
    else:
        print("Test execution failed:")

    print(run_process.stdout.decode("utf-8"))
    print(stderr_output)


def remove_class_files(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file: {e.filename} - {e.strerror}")


def check_junit_installed(classpath):
    check_command = f"java -cp {classpath} org.junit.runner.JUnitCore"
    check_process = subprocess.run(check_command, shell=True, capture_output=True)
    return b"JUnit version" in check_process.stderr


def download_file(url, target_dir, file_name):
    response = requests.get(url)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, file_name), "wb") as file:
        file.write(response.content)


def install_junit(junit_jar, hamcrest_jar):
    junit_url = "https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar"
    hamcrest_url = "https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar"

    download_file(junit_url, ".", junit_jar)
    download_file(hamcrest_url, ".", hamcrest_jar)


junit_jar = "junit-4.13.2.jar"
hamcrest_jar = "hamcrest-core-1.3.jar"
classpath = f".:{junit_jar}:{hamcrest_jar}"
print("classpath: ", classpath)
os.chdir("src/")
if not check_junit_installed(classpath):
    print("Installing JUnit...")
    install_junit(junit_jar, hamcrest_jar)

java_file = "Sundae.java"
test_file = "SundaeTest.java"
run_java_junit_test(java_file, test_file, classpath)
remove_class_files("SundaeTest.class")
remove_class_files("Sundae.class")