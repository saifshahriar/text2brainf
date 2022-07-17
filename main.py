#!/usr/bin/env python3

import os

if os.path.exists("out.bf"):
    os.remove("out.bf")

output = open("out.bf", "a")

if not os.path.exists("usr_input.txt"):
    input_file = open("usr_input.txt", "w")
    input_file.write("Hello World!")

input_file = open("usr_input.txt")
usr_input = input_file.read()
input_file.close()

usr_input = list(usr_input)

for char in usr_input:
    for i in range(ord(char)):
        output.write("+")
    output.write(".>")
output.close()
