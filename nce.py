#! /usr/bin/python
from os import system
from subprocess import run 
from sys import argv



def command_list(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file: return file.read().splitlines()

try:
    system("clear")
    [print(f"{i+1}. {c}") for i, c in enumerate(command_list(argv[1]))]
    while True:
        num = int(input("Enter option number: "))
        if num == 0: break
        else:
            print(run(command_list(argv[1])[num - 1], shell=True))
            input()
            system("clear")
            [print(f"{i+1}. {c}") for i, c in enumerate(command_list(argv[1]))]


except (IndexError, ValueError): pass
except KeyboardInterrupt: exit()

