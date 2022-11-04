import os
import sys
import argparse
import pprint

class File:
    isDirectory: bool
    
    def __init__(self,name,isDirectory):
      self.name  = name
      self.isDirectory = isDirectory
      self.children = list()

    def add_child(self,child):
        self.children.append(child)

    def add_children(self,children):
        self.children.extend(children)

class FileTree:
    fileTree: list

    def __parse_file_tree(self,path):
        fileList = list()
      
        for dirEntry in os.scandir(path):
            if not dirEntry.is_file():
                directory = File(dirEntry.name,True)
                directory.add_children(self.__parse_file_tree(os.path.join(path, dirEntry.name)))
                fileList.append(directory)
            else:
                fileList.append(File(dirEntry.name,False))
        return fileList
    
    def __init__(self,root):
      self.fileTree = self.__parse_file_tree(root)

    def get_file_tree(self):
        return self.fileTree

    def __print_file_tree(self,fileTree,prefix):
        for file in fileTree:
            if file.isDirectory:
                print(prefix + "[" + file.name + "]")
                self.__print_file_tree(file.children, prefix + "  ")
            else:
                print(prefix + file.name)
        return
    
    def print_file_tree(self):
        self.__print_file_tree(self.fileTree,"")
        return


def main():
  parser = argparse.ArgumentParser(description='Parse file structure')
  parser.add_argument("--path", "-p", help="Parent path", type=str, default=".")
  
  args = parser.parse_args()

  files = FileTree(args.path)

  files.print_file_tree()

  return 0

if __name__ == '__main__':
    sys.exit(main())

