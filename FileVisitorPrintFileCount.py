from FileVisitor import *

class FileVisitorPrintFileCount(FileVisitor):

    __fileList = list()

    def visit(self,isDir,filePath) -> dict:
        if not isDir:
            self.__fileList.append(filePath)
        return dict()

    def report(self):
        print("Found " + str(len(self.__fileList)) + " files!")