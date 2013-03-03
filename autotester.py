#!/usr/bin/env python2

import sys
import filepath_normalize

def main():
    """Tests the filepath_normalize.py format_filepath() function.
    This reads in the input file given as the first argument, with the
    filepaths separated by the optional second argument. The separator
    defaults to the newline character. Note that this does mean that
    certain valid filenames will not work, depending on the separator.
    
    The expected output needs to be in a file with the the name of the
    called <input_file>.out, where <input_file> is the first argument.
    The output will be written to a file called <input_file>.tmp.
    
    For example, an input file test.dat will need expected output file
    test.dat.out, with actual output file test.dat.tmp.
    """
    # processing dots
    max_num_dots = 3
    
    # default to no filepath and error
    filepath = None
    if len(sys.argv) >= 2:
        filepath = sys.argv[1]

    # default to newline character as a separator
    sep = '\n'
    if len(sys.argv) >= 3:
        sep = sys.argv[2]
    if filepath == None:
        exit('Error: No input file specified. Give a file as argument.')

    # read the input file
    print 'Reading input from '+str(filepath)
    body = ''
    try:
        body = open(str(filepath), 'r').read()
    except IOError:
        exit('Error: Could not open '+str(filepath))

    # process the filepaths in the input file and write to a temporary file
    input_arr = str.split(body,sep)
    sys.stdout.write('Processing')
    tmpout = open(str(filepath)+'.tmp', 'w')
    for i in range(len(input_arr)):
        formatted = filepath_normalize.format_filepath(input_arr[i])
        tmpout.write(str(formatted))
        if i != len(input_arr) - 1:
            tmpout.write(sep)
        if i % (1+len(input_arr)/(max_num_dots+1)) == 0:
            sys.stdout.write('.')

    print ''
    tmpout.close()
    print 'Wrote output to file '+str(filepath)+'.tmp'
    
    # read in the expected outputs and compares them to actual outputs
    tmpin = str.strip(open(str(filepath)+'.tmp', 'r').read(), sep)
    outin = ''
    try:
        outin = str.strip(open(str(filepath) + '.out', 'r').read(), sep)
    except IOError:
        exit('Error: Could not open expected output file ' + str(filepath) + 
            '.out')

    print 'Comparing to expected output file ' + str(filepath) + '.out'
    if tmpin == outin:
        print 'Test passed! Time to celebrate!'
    else:
        print 'Test failed. Difference between expected and actual output.'


if __name__ == "__main__":
    main()
