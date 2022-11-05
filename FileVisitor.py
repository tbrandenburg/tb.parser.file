from abc import ABC, abstractmethod

class FileVisitor(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def visit(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        return dict()

    def report(self):
        pass