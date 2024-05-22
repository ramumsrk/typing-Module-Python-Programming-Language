#! /usr/bin/python3.12

from typing import Any , Literal

import logging

from pathlib import Path

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  filemode='+a',
  filename=f'{Path(__file__).parent}/01_Any_demo.log',
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s"
)

# User-defined function
def main() -> Literal[None]:
  a : Any = None
  logging.debug( f'{type(a)=}' )
  a = 'Hello, World!'
  logging.debug( F'{type(a)=}' )
  a = True
  logging.debug( f'{type(a)=}' )
  return None

if __name__ == '__main__':

  # Function call
  main()