#!/usr/bin/python3
import random
import argparse
import sys

# Argparse Setup

parser = argparse.ArgumentParser(description="This program exists to roll dice.")
parser.add_argument('-d', metavar='dice', type=int, nargs='+', help="The number of sides to be rolled")
args = parser.parse_args()
try:
  usrinput = args.d[0]
except:
  print("Use the argument -h to show the help prompts.")
  sys.exit()

#def dice(type):
result = random.randint(1,usrinput)

#result = dice(usrinput)
print("")
print("The Result of your d"+str(usrinput)+" roll is: ")
print("")
print(result)