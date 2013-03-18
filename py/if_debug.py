#!/usr/bin/python

import  argparse

parser  = argparse.ArgumentParser()

#print dir(parser)

DEBUG=False
parser.add_argument('-d','--debug', dest='debugflag', action='store_true', default=False)


prog_args = parser.parse_args()

#print type(prog_args)

if prog_args.debugflag:
	print "Debug: On"

