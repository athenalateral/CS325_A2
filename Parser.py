# Parser example

import argparse

def demo() -> None:

parser = argparse.ArgumentParser()

parser.add_argument(help="please enter the full path to the file", dest='input_path', type=str)
parser.add_argument(help="Enter an int value", dest='number', type=int)

args = parser.parse_args()

path = args.input_path
number = args.number

print("path: ", path, "number: ", number)

# This creates command line arguments much like how linux did it

if __name__=="__main__":
    demo()
