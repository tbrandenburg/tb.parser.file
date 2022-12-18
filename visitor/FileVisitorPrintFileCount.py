from FileVisitor import *

class FileVisitorPrintFileCount(FileVisitor):

    __fileCount = 0

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            self.__fileCount = self.__fileCount + 1
        return dict()

    def report(self):
        print("[FileVisitorPrintFileCount] Found " + str(self.__fileCount) + " files!")