FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /pycparser
WORKDIR /pycparser
RUN python3 -m pip install . && chmod +x fuzz/pycparser_fuzz.py

ENTRYPOINT [ ]
CMD ["/pycparser/fuzz/pycparserfuzz.py"]