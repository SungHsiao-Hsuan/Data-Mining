from dataclasses import replace
import csv
import time
from pathlib import Path
from typing import Any, List, Union

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running {func.__name__} ...", end='\r')
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} Done in {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def read_file(filename: Union[str, Path]) -> List[List[int]]:

    return [
        [int(x) for x in line.split(',')]
        for line in Path(filename).read_text().splitlines()
    ]

@timer
def ibm_read_file(filename: Union[str, Path]) -> List[List[int]]:

    return [
        [int(x) for x in line.split()]
        for line in Path(filename).read_text().splitlines()
    ]

@timer
def write_file(data: List[List[Any]], filename: Union[str, Path]) -> None:

    f = open(filename, 'w+')
    str_data = ' '.join(str(x) for x in data)
    f.write(str_data)

@timer
def ibm_write_file(data: List[List[Any]], filename: Union[str, Path]) -> None:

    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
