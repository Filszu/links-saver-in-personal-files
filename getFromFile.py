import argparse

def readData():
    try:
        # Create an argument parser
        parser = argparse.ArgumentParser(description="Read links from a .links file")

        # Add a positional argument for the file path
        parser.add_argument("file", metavar="FILE", help="the path to the .links file")

        # Parse the command line arguments
        args = parser.parse_args()

        print(args.file)
        return args.file
    except:
        print("reading file Error - reading from example file")
        return None

readData()
        

