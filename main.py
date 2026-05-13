import argparse
from pathlib import Path
from process_dt import process_dt
from helpers import *

PROJECT_NAME = "DevTreeTesting" 
ABSOLUTE_ARG_PATH = "Path"

def main():
    parser = argparse.ArgumentParser(prog="Device Tree Parser", description="Parses through Device Tree files to see if it could create a matching C or C++ include", epilog="made by Danny Catorcini for EVT-core")

    print("Reading Passed in Arguments")
    parser.add_argument(ABSOLUTE_ARG_PATH)
    ns = parser.parse_args()
    dt_file_name = getattr(ns, ABSOLUTE_ARG_PATH)
    print(f"\tfound {surround_quotes(dt_file_name)}")
    new_line_stdout()
    
    here = Path.cwd()
    dt_file_location = here.joinpath(dt_file_name)
    print(f"Look for file {surround_quotes(dt_file_name)} in directory {surround_quotes(str(here))}")
    if Path.exists(dt_file_location):
        print(f"\tdevicetree file {surround_quotes(str(dt_file_location))} found")
    else:
        print(f"\tdevicetree file {surround_quotes(str(dt_file_location))} not found")
        print(f"\tGlobbing from {surround_quotes(str(here))} for {surround_quotes(dt_file_name)}")
        potential_files = list()
        for i in here.rglob(f"{dt_file_name}"):
            potential_files.append(i)
            print(f"\tdevicetree file {surround_quotes(str(i))} found")

        if not potential_files:
            raise FileNotFoundError(f"File could not be found within {PROJECT_NAME}")
        if len(potential_files) == 1:
            dt_file_location = potential_files.pop()
        if len(potential_files) > 1:
            raise NotImplementedError(f"Too many files found in the glob with name {dt_file_name}")
        
    new_line_stdout()
    print(f"Processing devicetree file {surround_quotes(dt_file_name)}")
    process_dt(dt_file_location)




    # print(dt_file_location)

if __name__ == "__main__":
    main()