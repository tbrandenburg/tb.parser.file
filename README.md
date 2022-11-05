# tb.parser.file

Parse file structure with python supporting:

- Filters
- Visitors
- JSON output

## Sample output

~~~bash
[example]
  file_parser.py
FileFilter.py
FileFilterDir.py
FileFilterFile.py
FileTree.py
FileVisitor.py
FileVisitorFileSize.py
FileVisitorPrintFilepaths.py
[test]
  CMakeLists.txt
  myfile.c
  [subdir]
    myfile2.c
~~~

## Example

~~~bash
python example/file_parser.py
~~~
