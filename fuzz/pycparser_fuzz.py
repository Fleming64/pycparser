#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    from pycparser import c_parser
    from pycparser.plyparser import ParseError

parser = c_parser.CParser()

@atheris.instrument_func
def TestOneInput(data):
    try:
        parser.parse(data.decode('utf8'))
    except UnicodeDecodeError:
        pass
    except ParseError:
        pass


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()