#! /usr/bin/python3.12

from typing import TypeVar

T : TypeVar = TypeVar('T')

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  filemode='+a',
  filename=f'{Path(__file__).parent}/04_TypeVar_demo.log',
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s"
)

from collections.abc import Sequence

# User-defined function
def first(collection: Sequence[T]) -> T:
  return collection[0]

from typing import Literal

# User-defined function
def main() -> Literal[None]:
  list_of_numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
  ]
  logging.debug( f'First element in {list_of_numbers=} is {first(list_of_numbers)=}' )
  return None

if __name__ == '__main__':

  # Function call
  main()