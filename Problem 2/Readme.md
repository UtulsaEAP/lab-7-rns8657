# Problem 2
Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should determine if the strings from the list are within that range (inclusive of the bounds) and output the results.

Ex: If the input is:

    ./Problem 2/input1.txt
    ammoniated
    millennium

and the contents of input1.txt are:
    
    aspiration
    classified
    federation
    graduation
    millennium
    philosophy
    quadratics
    transcript
    wilderness
    zoologists

the output is:

    aspiration - in range
    classified - in range
    federation - in range
    graduation - in range
    millennium - in range
    philosophy - not in range
    quadratics - not in range
    transcript - not in range
    wilderness - not in range
    zoologists - not in range

Notes:
    In the tests, the first word input always comes alphabetically before the second word input.

