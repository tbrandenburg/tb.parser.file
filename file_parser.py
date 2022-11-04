import os
import sys
import argparse
import pprint

class File:
    isDirectory: bool
    
    def __init__(self, name, isDirectory):
      self.name  = name
      self.isDirectory = isDirectory
      self.children = list()

    def add_child(self,child):
        self.children.append(child)

    def add_children(self, children):
        self.children.extend(children)

class FileTree:
    fileTree: list

    def __parse_file_tree(self, path):
        fileList = list()
      
        for dirEntry in os.scandir(path):
            if not dirEntry.is_file():
                directory = File(dirEntry.name,True)
                directory.add_children(self.__parse_file_tree(os.path.join(path, dirEntry.name)))
                fileList.append(directory)
            else:
                fileList.append(File(dirEntry.name,False))
        return fileList
    
    def __init__(self, root):
      self.fileTree = self.__parse_file_tree(root)

    def get_file_tree(self):
        return self.fileTree

    def __todict(self, fileTree):
        fileTreeDict = dict()
        for file in fileTree:
            if file.isDirectory:
                fileTreeDict[file.name] = self.__todict(file.children)
            else:
                fileTreeDict[file.name] = ""
        return fileTreeDict

    def todict(self):
        return self.__todict(self.fileTree)

    def __file_tree_str(self, fileTree, prefix):
        fileTreeStr = ""
        for file in fileTree:
            if file.isDirectory:
                fileTreeStr = fileTreeStr + prefix + "[" + file.name + "]" + os.linesep
                fileTreeStr = fileTreeStr + self.__file_tree_str(file.children, prefix + "  ")
            else:
                fileTreeStr = fileTreeStr + prefix + file.name + os.linesep
        return fileTreeStr
    
    def __str__(self):
        return self.__file_tree_str(self.fileTree,"").strip()


def main():
    parser = argparse.ArgumentParser(description='Parse file structure')
    parser.add_argument("--path", "-p", help="Parent path", type=str, default=".")
  
    args = parser.parse_args()

    files = FileTree(os.path.abspath(args.path))

    print("File tree as string:")
    print(files)

    print("")
    print("File tree as dict:")
    pprint.pprint(files.todict())

    return 0

if __name__ == '__main__':
    sys.exit(main())

