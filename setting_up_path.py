"""
If you've installed Python in Windows using the default installation options, the path to the Python executable wasn't added to the Windows Path variable. The Path variable lists the directories that will be searched for executables when you type a command in the command prompt. By adding the path to the Python executable, you will be able to access python.exe by typing the python keyword (you won't need to specify the full path to the program).
"""

"""
Consider what happens if we enter the python command in the command prompt and the path to that executable is not added to the Path variable:

Shell Script:

C:\>python
'python' is not recognized as an internal or external command, operable program or batch file.

As you can see from the output above, the command was not found. To run python.exe, you need to specify the full path to the executable:

Shell Script
C:\>C:\Python34\python --version
Python 3.10.0
"""