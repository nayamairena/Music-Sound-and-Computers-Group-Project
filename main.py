#start of something wonderful

import numpy, tkinter, matlab, ast, inspect, sys


#some kind of GUI for the user to use

#call in the code file and parse the file, by reading the function types , variable types, save into
# an array maybe

def parseMe():
  with open(sys.argv[1], "rb") as source:
    tree = ast.parse(source.read())
    print(ast.dump(tree))
    


#create an array of notes?
#apply effects to sections of array?
def makeMusic():
  pass

def main():
  parseMe()
  makeMusic()
  

if __name__ == "__main__":
  main()