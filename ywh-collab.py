# -*- coding: utf-8 -*-
# Author: Aethlios <tom.chambaretaud@protonmail.com>.

import pathlib
import argparse

from src.constants import ACTION_EXPORT, ACTION_COMPARE, ASCII_ART, DESCRIPTION, WARNING
from src.collaborator import YWHCollaborator, AuthenticationFail

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("-j", "--jwt", help="The JWT token of the YWH session")
parser.add_argument(
    "-f", "--filename", help="The input or output filename", required=True
)
parser.add_argument(
    "action", choices=[ACTION_EXPORT, ACTION_COMPARE], help="Export your list of program IDs or compare a list with your programs to find common programs that accept collab."
)

args = parser.parse_args()

print(ASCII_ART)
print(DESCRIPTION)
print(f"{WARNING}\n")

logged = False
if args.jwt:
    try:
        collaborator = YWHCollaborator(args.jwt)
        logged = True
    except AuthenticationFail as e:
        print("Your JWT is invalid.\n[+] Please login again :")

while not logged:
    collaborator = YWHCollaborator()
    email = input("Email : ")
    password = input("Password : ")
    try:
        totp_token = collaborator.login(email, password)
        if totp_token:
            totp_code = input("TOTP : ")
            collaborator.login_totp(totp_token, totp_code)
            logged = True
    except AuthenticationFail as e:
        print(e)
        print("[+] Please login again :")


if args.action == ACTION_EXPORT:
    if pathlib.Path(args.filename).is_file():
        confirm = input(
            "The output file already exists, are you sure you want to overwrite it? [O/n] : "
        )
        if confirm != "O" and confirm != "o" and confirm != "":
            exit(-1)
    n = collaborator.export(args.filename)
    print(f"Exportation of {n} programs completed in '{args.filename}' file.")
elif args.action == ACTION_COMPARE:
    if not pathlib.Path(args.filename).is_file():
        print(f"The '{args.filename}' file doesn't exist.")
        exit(-1)
    print(f"Comparison with '{args.filename}' file:")
    for program in collaborator.compare(args.filename):
        print(program)
