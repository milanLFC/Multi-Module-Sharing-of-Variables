#!/usr/bin/python3

import sys
import os
sys.path.insert(0, '../subFolder/')
import subFile 


'''
########################################################################
# 
#  MAIN
#
########################################################################

'''
if __name__ == '__main__':
  print(subFile.scriptName)
  # get the script name
  subFile.scriptName = os.path.basename(__file__)
  print(subFile.scriptName)

  workingDir = os.path.abspath(os.path.dirname(__file__)) 

  subFile.subFunction()
