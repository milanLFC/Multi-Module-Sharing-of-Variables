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
  # the above will print out the value from subFile
  subFile.scriptName = os.path.basename(__file__)
  # the above will update the variable
  print(subFile.scriptName)


  subFile.subFunction()
