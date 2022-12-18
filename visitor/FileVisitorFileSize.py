import os

from FileVisitor import *

class FileVisitorFileSize(FileVisitor):

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if not isDir:
            fileStats = os.stat(absFilePath)
            return {"size":fileStats.st_size}
        return dict()