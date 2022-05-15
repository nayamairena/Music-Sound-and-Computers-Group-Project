#start of something wonderful

from debugpy import trace_this_thread
import numpy as np
import tkinter as tk
# import matlab.plotlib as mb -for extra cuteness at the end for graphs showing quantization of Python fundamental syntax.
import ast
import inspect as ins
import sys

from sympy import monic


#some kind of GUI for the user to use

#call in the code file and parse the file, by reading the function types , variable types, save into
# an array maybe

# Part A: The Parsing Code
class AssignmentVisitor(ast.NodeVisitor):
  """
  def visit_FunctionDef(self, node):
    for defi in ast.walk(node):
      if isinstance(defi, ast.FunctionDef):
        print(defi.name, end=' ')
  """
  def visit_Assign(self, node):
      for target in node.targets:
        if isinstance(target, ast.Name):
          print(target.id, end=' ')

  def visit_Import(self, node):      
    for alias in ast.walk(node):
      if isinstance(alias, ast.Import):
        for name in alias.names:
          print(name.name, end=' ')

  def visit_ImportFrom(self, node):
    for module in ast.walk(node):
      if isinstance(module, ast.ImportFrom):
        print(module.module, end=' ')
   
  
  

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

