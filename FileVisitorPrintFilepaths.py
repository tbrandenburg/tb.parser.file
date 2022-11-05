from FileVisitor import *

class FileVisitorPrintFilepaths(FileVisitor):

    __fileList = list()

    def visit(self,isDir,filePath) -> dict:
        if not isDir:
            self.__fileList.append(filePath)
        return dict()

    def report(self):
        for file in self.__fileList:
            print(file)