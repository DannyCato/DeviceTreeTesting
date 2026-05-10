from dataclasses import dataclass
from pathlib import Path
import re

@dataclass
class ProcessDT:
    name: str

def process_dt(path: Path):
    with open(path, 'r') as file:
        dt_file = file.readlines()
    
    raw_version_number = dt_file[0]
    mat = re.match("dts-v\\d", raw_version_number)
    print(mat)

if __name__ == "__main__":
    pass