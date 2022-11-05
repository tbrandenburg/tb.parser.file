import os
import sys
import argparse
import pprint

import sys
sys.path.insert(0,'.')
sys.path.insert(0,'..')

from FileTree import *
from FileFilterDir import *
from FileFilterFile import *
from FileVisitorPrintFilepaths import *
from FileVisitorPrintFileCount import *
from FileVisitorFileSize import *

def main():
    parser = argparse.ArgumentParser(description='Parse file structure')
    parser.add_argument("--path", "-p", help="Root path (relative)", type=str, default=".")
  
    args = parser.parse_args()

    files = FileTree(args.path,[FileFilterDir(["test"]),
                                FileFilterDir(["example"]),
                                FileFilterFile([".*\.py"]),
                                FileFilterFile([".*\.c"]),
                                FileFilterFile([".*\.txt"])],
                               [FileVisitorPrintFilepaths(),
                                FileVisitorPrintFileCount(),
                                FileVisitorFileSize()])

    print("")
    print("File tree as string:")
    print(files)

    print("")
    print("File tree as dict:")
    pprint.pprint(files.get_dict())

    print("")
    print("Writing json to build/file_tree.json")
    files.to_json("build/file_tree.json")

    return 0

if __name__ == '__main__':
    sys.exit(main())

