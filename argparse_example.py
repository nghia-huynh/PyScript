#!/usr/bin/python

import argparse
 
parser = argparse.ArgumentParser(description='ArgParse Example')

parser.add_argument('-i', '--input', 
                    help='Input file name',required=False)
parser.add_argument('', '--prefix', 
                    action='store', dest='prefix', default=None,
                    help='prefix to file')
parser.add_argument('--optimized',
                    action='store_const', dest='NTIMES', const=10, default=100,
                    help='use optimized NTIMES=10, leave out for default NTIMES=100')
parser.add_argument('--verbose',
                    action='store_true', dest='verbose', default=False,
                    help='print all log')

args = parser.parse_args()
 
## show values ##
print ("Input file: %s" % args.input )
print ("Optimized: %d" % args.NTIMES )
print ("Verbose: %s" % args.verbose )
