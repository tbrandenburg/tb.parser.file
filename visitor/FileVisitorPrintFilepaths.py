from FileVisitor import *

class FileVisitorPrintFilepaths(FileVisitor):

    __fileList = list()

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            self.__fileList.append(absFilePath)
        return dict()

    def report(self):
        print("[FileVisitorPrintFileCount] File paths:")
        for file in self.__fileList:
            print(file)