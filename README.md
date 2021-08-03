# Multi-Module-Sharing-of-Variables

I created this simple example as i failed to google something similar.

Problem:

I had a variable in my main script that i wanted to be accessed via my sub module.
I didnt want to pass the variable as a parameter, and i wanted both the main script and the sub module to be able to access and change the variable's contents.

Why did i not want to pass the variable as a parameter to the function?
This is because i had many variables that i needed to have as a true "global" nature, and i didnt want to pass all of these as parameters.

Solution:

i declared the variable in the subFolder/subFile.py, and accessed it from the mainFolder/mainScript.py using subFile.<variable name>
i achieved this without the need of an __init__.py file in the subfolder
