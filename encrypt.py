    # create file name for zip file
    # create command line string
    # execute command line
# get input file path from user



import os

input_file = input("Enter path of file to zip and encrypt: ")
password = input("Enter password for encryption: ")

# Use os.system to run the 7z command
os.system(f"7z a -p{password} -mhe=on archive.7z {input_file}")
