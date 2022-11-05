import os
import json

class FileTree:
    __fileTree     = dict()
    __fileFilter   = list()
    __fileVisitors = list()

    __PREFIX       ="  +-"

    def __parse_file_tree(self, path):
        fileDict = dict()

        for dirEntry in os.scandir(path):
            isDir = not dirEntry.is_file()
            fileAbsPath = os.path.join(os.path.abspath(path),dirEntry.name)
            fileName = dirEntry.name

            filtered = False
            for filter in self.__fileFilter:
                if filter.filter(isDir, fileAbsPath, fileName):
                    filtered = True
                    break

            if filtered:
                if isDir:
                    fileDict[fileName] = {"is_dir":isDir, "children":self.__parse_file_tree(fileAbsPath)}
                else:
                    fileDict[fileName] = {"is_dir":isDir}
                # Call file visitors visit method
                for visitor in self.__fileVisitors:
                    fileDict[fileName].update(visitor.visit(isDir,fileAbsPath))

        return fileDict

    def __init__(self, *args):
        if len(args)>2:
            if isinstance(args[1], list):
                self.__fileFilter = args[1]
            if isinstance(args[2], list):
                self.__fileVisitors = args[2]
            self.__fileTree = self.__parse_file_tree(args[0])

            # Call file visitors report method
            for visitor in self.__fileVisitors:
                visitor.report()
        elif len(args)>1:
            if isinstance(args[1], list):
                self.__fileFilter = args[1]
            self.__fileTree = self.__parse_file_tree(args[0])
        elif len(args)>0:
            self.__fileTree = self.__parse_file_tree(args[0])

    def get_dict(self):
        return self.__fileTree

    def to_json(self, jsonPath):
        jsonObj = json.dumps(self.__fileTree, indent = 4)
        os.makedirs(os.path.dirname(os.path.abspath(jsonPath)), exist_ok=True)
        with open(os.path.abspath(jsonPath), "w") as jsonFile:
            jsonFile.write(jsonObj)

    def __file_tree_str(self, fileTree, prefix):
        fileTreeStr = ""
        for (file, values) in fileTree.items():
            if values["is_dir"]:
                fileTreeStr = fileTreeStr + prefix + "[" + file + "]" + os.linesep
                fileTreeStr = fileTreeStr + self.__file_tree_str(values["children"], prefix + "    ")
            else:
                fileTreeStr = fileTreeStr + prefix + file + os.linesep
        return fileTreeStr

    def __str__(self):
        return self.__file_tree_str(self.__fileTree,"").strip()