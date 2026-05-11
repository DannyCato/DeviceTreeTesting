import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(prog="Device Tree Parser", description="Parses through Device Tree files to see if it could create a matching C or C++ include", epilog="made by Danny Catorcini for EVT-core")
    path_arg = "Path"
    parser.add_argument(path_arg)
    ns = parser.parse_args()
    dt_file_name = getattr(ns, path_arg)
    
    here = Path.cwd()
    dt_file_location = here.joinpath(dt_file_name)
    if Path.exists(dt_file_location):
        print(f"devicetree file \"{dt_file_name}\" found")
    else:
        for i in here.glob(f"*/{dt_file_name}"):
            print(i)

    # print(dt_file_location)

if __name__ == "__main__":
    main()