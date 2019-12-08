# Introduction
- History
- Features
- Setting up path
- Working with Python & Basic Syntax 
- Variable and Data Types 
- Operator

### History
Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL), capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until July 12, 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. He now shares his leadership as a member of a five-person steering council. In January, 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project.

Python 2.0 was released on 16 October 2000 with many major new features, including a cycle-detecting garbage collector and support for Unicode.

Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible. Many of its major features were backported to Python 2.6.x and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates (at least partially) the translation of Python 2 code to Python 3.

Python 2.7's end-of-life date was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.

[https://en.wikipedia.org/wiki/Python_(programming_language)](https://en.wikipedia.org/wiki/Python_(programming_language)

### Features
- Easy to Learn and Use: Python is easy to learn and use. It is developer-friendly and high level programming language.
- Expressive Language: Python language is more expressive means that it is more understandable and readable.
- Interpreted Language: Python is an interpreted language i.e. interpreter executes the code line by line at a time. This makes debugging easy and thus suitable for beginners.
- Cross-platform Language: Python can run equally on different platforms such as Windows, Linux, Unix and Macintosh etc. So, we can say that Python is a portable language.
- Free and Open Source: Python language is freely available at offical web address.The source-code is also available. Therefore it is open source.
- Object-Oriented Language: Python supports object oriented language and concepts of classes and objects come into existence.
- Extensible: It implies that other languages such as C/C++ can be used to compile the code and thus it can be used further in our python code.
- Large Standard Library: Python has a large and broad library and prvides rich set of module and functions for rapid application development.
- GUI Programming Support: Graphical user interfaces can be developed using Python.
- Integrated: It can be easily integrated with languages like C, C++, JAVA etc.

### Setting up path
If you’ve installed Python in Windows using the default installation options, the path to the Python executable wasn’t added to the Windows Path variable. The Path variable lists the directories that will be searched for executables when you type a command in the command prompt. By adding the path to the Python executable, you will be able to access python.exe by typing the python keyword (you won’t need to specify the full path to the program).

Consider what happens if we enter the python command in the command prompt and the path to that executable is not added to the Path variable:

```shell script
C:\>python
'python' is not recognized as an internal or external command,
operable program or batch file.
```

As you can see from the output above, the command was not found. To run python.exe, you need to specify the full path to the executable:

```shell script
C:\>C:\Python34\python --version
Python 3.4.3
```
