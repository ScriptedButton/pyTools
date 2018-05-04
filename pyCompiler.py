import py_compile
import sys

file = sys.argv[1]
output = sys.argv[2]

py_compile.compile(file, output)