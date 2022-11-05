import os
import re

from FileFilter import *

class FileFilterFile(FileFilter):

    def filter(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        if isDir:
            return False
        else:
            for regEx in self._filterList:
                try:
                    if re.match(regEx,fileName):
                        return True
                except:
                    return False
            return False