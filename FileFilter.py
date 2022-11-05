from abc import ABC, abstractmethod

class FileFilter(ABC):
    _filterList = list()
    
    def __init__(self,filterList):
        self._filterList = filterList
        pass

    @abstractmethod
    def filter(self,isDir,filePath,fileName) -> bool:
        return True