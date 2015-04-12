import sys


def main():
    """
    The main function called when the program is run. Will either start the interpreter or run a file if a filename is provided
    """
    if len(sys.argv) == 1:
        from interpreter import Interpreter

        # Main loop which prompts user for input and print the response of the input handed to the rep function
        interpreter = Interpreter()
        interpreter.cmdloop()
    else:
        from fileParser import FileParser
        from virtualmachine import VirtualMachine
        from env import Env

        env = Env()
        env.setToStandardEnv()

        parser = FileParser(sys.argv[1], VirtualMachine(env))
        parser.run()

if __name__ == '__main__':
    main()
