# define the varaible in the subFile (and not in the mainFile)
scriptName ="subFile"

def subFunction():
  # if called from main, the value set from main will be displayed
  print(scriptName)

'''
########################################################################
# 
#  MAIN
#
########################################################################

'''
if __name__ == '__main__':

  # if called directly, the local definition will be displayed
  subFunction()

