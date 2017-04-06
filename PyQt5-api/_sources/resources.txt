The PyQt5 Resource System
=========================

PyQt5 supports Qt's resource system.  This is a facility for embedding
resources such as icons and translation files in an application.  This makes
the packaging and distribution of those resources much easier.

A ``.qrc`` resource collection file is an XML file used to specify which
resource files are to be embedded.  The application then refers to the resource
files by their original names but preceded by a colon.

For a full description, including the format of the ``.qrc`` files, see the Qt
Resource System in the Qt documentation.


:program:`pyrcc5`
-----------------

:program:`pyrcc5` is PyQt5's equivalent to Qt's :program:`rcc` utility and is
used in exactly the same way.  :program:`pyrcc5` reads the ``.qrc`` file, and
the resource files, and generates a Python module that only needs to be
``import``\ ed by the application in order for those resources to be made
available just as if they were the original files.
