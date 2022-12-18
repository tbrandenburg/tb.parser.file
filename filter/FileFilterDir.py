import os
import re

from FileFilter import *

class FileFilterDir(FileFilter):

    def filter(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        if isDir:
            dirList = os.path.normpath(relFilePath).split(os.sep)
            for regEx in self._filterList:
                try:
                    regExC = re.compile(regEx)
                    if any((match := regExC.match(dir)) for dir in dirList):
                        return True
                except:
                    return False
            return False
        else:
            return False