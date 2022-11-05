# tb.parser.file

Parse file structure with python supporting:

- File tree output
- Filters
- Visitors
- JSON output

## Sample output

As string:

~~~bash
[example]
    file_parser.py
FileFilter.py
FileFilterDir.py
FileFilterFile.py
FileTree.py
FileVisitor.py
FileVisitorFileSize.py
FileVisitorPrintFileCount.py
FileVisitorPrintFilepaths.py
[test]
    CMakeLists.txt
    myfile.c
    [subdir]
        myfile2.c
~~~

As dict (with file size visitor):

~~~bash
{'FileFilter.py': {'is_dir': False, 'size': 281},
 'FileFilterDir.py': {'is_dir': False, 'size': 575},
 'FileFilterFile.py': {'is_dir': False, 'size': 440},
 'FileTree.py': {'is_dir': False, 'size': 2656},
 'FileVisitor.py': {'is_dir': False, 'size': 237},
 'FileVisitorFileSize.py': {'is_dir': False, 'size': 264},
 'FileVisitorPrintFilepaths.py': {'is_dir': False, 'size': 328},
 'example': {'children': {'file_parser.py': {'is_dir': False, 'size': 1369}},
             'is_dir': True},
 'test': {'children': {'CMakeLists.txt': {'is_dir': False, 'size': 0},
                       'myfile.c': {'is_dir': False, 'size': 25},
                       'subdir': {'children': {'myfile2.c': {'is_dir': False,
                                                             'size': 32}},
                                  'is_dir': True}},
          'is_dir': True}}
~~~

As JSON (with file size visitor):

~~~bash
{
    "example": {
        "is_dir": true,
        "children": {
            "file_parser.py": {
                "is_dir": false,
                "size": 1369
            }
        }
    },
    "FileFilter.py": {
        "is_dir": false,
        "size": 281
    },
    "FileFilterDir.py": {
        "is_dir": false,
        "size": 575
    },
    "FileFilterFile.py": {
        "is_dir": false,
        "size": 440
    },
    "FileTree.py": {
        "is_dir": false,
        "size": 2656
    },
    "FileVisitor.py": {
        "is_dir": false,
        "size": 237
    },
    "FileVisitorFileSize.py": {
        "is_dir": false,
        "size": 264
    },
    "FileVisitorPrintFilepaths.py": {
        "is_dir": false,
        "size": 328
    },
    "test": {
        "is_dir": true,
        "children": {
            "CMakeLists.txt": {
                "is_dir": false,
                "size": 0
            },
            "myfile.c": {
                "is_dir": false,
                "size": 25
            },
            "subdir": {
                "is_dir": true,
                "children": {
                    "myfile2.c": {
                        "is_dir": false,
                        "size": 32
                    }
                }
            }
        }
    }
}
~~~

## Example

~~~bash
python example/file_parser.py
~~~
