from dataclasses import dataclass
from pathlib import Path
import re
from helpers import surround_quotes
from generate_tree import lexer

SUPPORTED_VERSIONS = [1]

def process_dt(path: Path):
    with open(path, 'r') as file:
        dt_file = file.readlines()
    
    raw_version_number = dt_file.pop(0)
    mat = re.search("dts\\-v\\d*", raw_version_number)
    if not mat:
        raise Exception(f"Does not contain proper devicetree header at first line: Must fit the pattern {surround_quotes('/dts-v[0-9]*/;')}")
    else:
        matched_string = mat.group()
    print(f"Found device tree specification header, {matched_string}")

    version = re.search("\\d+", matched_string)
    if not version:
        raise Exception(f"No version number found in devicetree header")
    else:
        version = version.group(0)

    if version in SUPPORTED_VERSIONS:
        raise Exception(f"Not a supported version of the devicetree format: Expected {surround_quotes(str(SUPPORTED_VERSIONS))} have {surround_quotes(version)}")
    else:
        print(f"Found version: {version}")
    
    print("Beginning Lexer")    
    lexer(dt_file)


if __name__ == "__main__":
    pass