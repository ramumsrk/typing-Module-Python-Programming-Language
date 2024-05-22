#! /usr/bin/python3.12

import logging

from pathlib import Path

from typing import Literal , TypeAlias

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  filemode='+a',
  filename=f'{Path(__file__).parent}/02_TypeAlias_demo.log',
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s"
)

ZipCode: TypeAlias = int

# User-defined function
def print_zipcode(zipcode: ZipCode , / ) -> Literal[None]:
  logging.debug( f'ZipCode is {zipcode}' )
  return None

# User-defined function
def main() -> Literal[None]:
  zipcode: ZipCode = ZipCode( input( "Enter your zipcode: ") )
  # Function call
  print_zipcode(zipcode)
  return None

if __name__ == '__main__':

  # Function call
  main()