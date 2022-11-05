from FileVisitor import *

class FileVisitorPrintFilepaths(FileVisitor):

    __fileList = list()

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        if not isDir:
            self.__fileList.append(absFilePath)
        return dict()

    def report(self):
        for file in self.__fileList:
            print(file)