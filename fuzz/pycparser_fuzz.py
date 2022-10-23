#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    from pycparser import c_parser

@atheris.instrument_func
def TestOneInput(data):
    c_parser.CParser().parse(data.decode("utf8"))


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()