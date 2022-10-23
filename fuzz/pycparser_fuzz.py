#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    from pycparser import c_parser

parser = c_parser.CParser()

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    parser.parse(fdp.ConsumeUnicodeNoSurrogates(len(data)))


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()