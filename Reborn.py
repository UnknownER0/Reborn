######################
# Reborn | By UnknownER0
######################
from colorama import Fore, Back, Style
import subprocess
import os

############
# Variables
############
Logo = fr'''{Fore.LIGHTCYAN_EX}
 ____           _
|  _ \    ___  | |__     ___    _ __   _ __
| |_) |  / _ \ | '_ \   / _ \  | '__| | '_ \
|  _ <  |  __/ | |_) | | (_) | | |    | | | |
|_| \_\  \___| |_.__/   \___/  |_|    |_| |_|
{Style.RESET_ALL}'''
settings_name = "./reborn.settings"
error_templ = f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL}"

############
# Functions
############
def parse_settings():
    parsed = dict()
    with open(settings_name, "r") as f:
        settings_file = f.read().splitlines()
        f.close()
    for line in settings_file:
        splitted = line.split("=")
        parsed[splitted[0]] = splitted[1]
    return parsed

def welcome_user():
    if os.path.exists(settings_name):
        settings = parse_settings()
        if "NAME" in settings:
            print(f"Welcome back {Fore.LIGHTGREEN_EX}{settings['NAME']}{Style.RESET_ALL}\n")
            return
    print("Looks like this is your first time using reborn!")
    name = input("What's your name? > ")
    with open(settings_name, "a") as f:
        f.write(f"NAME={name}\n")
        f.close()
    print(f"Welcome {Fore.LIGHTGREEN_EX}{name}{Style.RESET_ALL}\n")


def main():
    print(Logo)
    welcome_user()

    print("1.Show system info\n2.Open nano editor\n3.Show me all tasks\n4.Run Cava\n5.Run Atom\n6.Start VScode\n7.Open Firefox\n8.Start Google Chrome\n9.Run Neovim")
    action = input("\nWhat can I do for you? > ")

    if action == "1":
        subprocess.run("neofetch")
    elif action == "2":
        subprocess.run("nano")
    elif action == "4":
        subprocess.run("cava")
    elif action == "5":
        subprocess.run("atom")
    elif action == "6":
        subprocess.run("code")
    elif action == "7":
        subprocess.run("firefox")
    elif action == "8":
        subprocess.run("google-chrome-stable")
    elif action == "9":
        subprocess.run("nvim")

    else:
        print(f"{error_templ} Not an available option!")





if __name__ == "__main__":
    main()
