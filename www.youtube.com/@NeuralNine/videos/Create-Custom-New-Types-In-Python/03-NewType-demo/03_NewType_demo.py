#! /usr/bin/python3.12

from typing import NewType

ZipCode: NewType = NewType('ZipCode', int)

import logging

from pathlib import Path

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/03_NewType_demo.log'
)

from typing import Literal

# User defined function
def print_zipcode(zipcode: ZipCode , /) -> Literal[None]:
  logging.debug( F'ZipCode is {zipcode}' )
  return None

# User defined function
def main() -> Literal[None]:
  zipcode: ZipCode = ZipCode( input( "Enter a zipcode: " ) )
  # Function call
  print_zipcode(zipcode)
  return None

if __name__ == '__main__':

  # Function call
  main()