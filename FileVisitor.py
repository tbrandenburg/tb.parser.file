from abc import ABC, abstractmethod

class FileVisitor(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def visit(self,isDir,filePath) -> dict:
        return dict()

    def report(self):
        pass