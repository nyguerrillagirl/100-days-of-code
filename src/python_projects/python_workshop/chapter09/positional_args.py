# Exercise 125: Using Positional Arguments to Accept Source and Destination Inputs from a User

import argparse

parser = argparse.ArgumentParser(description="Interpret positional arguments.")
parser.add_argument('source', action='store', help='The source of an operation.')
parser.add_argument('dest', action='store', help = 'The destination of the operation.')

arguments = parser.parse_args()

print(f"Picasso will cycle from {arguments.source} to {arguments.dest}")

