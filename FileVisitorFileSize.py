import os

from FileVisitor import *

class FileVisitorFileSize(FileVisitor):

    def visit(self,isDir,filePath) -> dict:
        if not isDir:
            fileStats = os.stat(filePath)
            return {"size":fileStats.st_size}
        return dict()