import os

def finish_actions():
    print("Cleaning...")
    try:
        os.system("apt autoclean -y")
        os.system("apt autoremove -y")
        os.system("rm -rf temp/")
        print("Execution finished!")
    except OSError as err:
        print(err)
