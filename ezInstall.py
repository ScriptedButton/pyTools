# Auto Installer

import os

os.system("cls")
os.system("color A")
print("Automatic install engaging.\n")

requirements = list()

for i in open("install_settings.txt", 'r').readlines():
    cmd, name = i.split(":")
    requirements.append((cmd.strip(),name.strip()))

for i in requirements:
    opt = input("Would you like to install {}? ".format(i[1]))
    if "y" in opt.lower():
        os.system(i[0])
    elif "n" in opt.lower():
        print("Install skipped.")
    else:
        print("Invalid option, skipped.")

delete = input("Delete installer? ")
if "y" in delete.lower():
    os.remove("install_settings.txt")
    os.remove("installer.py")
elif "n" in delete.lower():
    print("Uninstall skipped.")
else:
    print("Invalid option, skipped.")