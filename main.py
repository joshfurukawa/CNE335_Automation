# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Josh Furukawa")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    import os

    server = "35.87.239.198"

    os.system('ping -n 4 {}'.format(server))
    # TODO - Call Ping method and print the results
    print(server.ping())
