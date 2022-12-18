from abc import ABC, abstractmethod

class FileVisitor(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    # Returns _dictionary_ as a result of visiting which is
    # added to the file tree dictionary
    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        return dict()

    def report(self):
        pass