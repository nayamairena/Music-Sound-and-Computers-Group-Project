#start of something wonderful

import numpy as np
import tkinter as tk
# import matlab.plotlib as mb -for extra cuteness at the end for graphs showing quantization of Python fundamental syntax.
import ast
import inspect as ins
import sys


#some kind of GUI for the user to use

#call in the code file and parse the file, by reading the function types , variable types, save into
# an array maybe

# Part A: The Parsing Code
class AssignmentVisitor(ast.NodeVisitor):
  def visit_Assign(self, node):
      for target in node.targets:
        if isinstance(target, ast.Name):
          print(target.id, end=' ')
        elif isinstance(target, ast.FunctionType):
          #print(target., end=' ')
          pass


def parseMe():
  with open(sys.argv[1], "rb") as source:
    tree = ast.parse(source.read())
  #print(ast.For(tree))
  AssignmentVisitor().visit(tree)


#create an array of notes?
#apply effects to sections of array?
def makeMusic():
  pass

def main():
  parseMe()
  makeMusic()
  

if __name__ == "__main__":
  main()
  
# Part B: The Musical Machina

