Support for Qt Interfaces
=========================

PyQt5 does not, generally, support defining a class that inherits from more
than one Qt class.  The exception is when inheriting from classes that Qt
defines as *interfaces*, for example
:class:`~PyQt5.QtGui.QTextObjectInterface`.

A Qt interface is an abstract class contains only pure virtual methods and is
used as a mixin with (normally) a :class:`~PyQt5.QtCore.QObject` sub-class.  It
is often used to define the interface that a plugin must implement.

Note that PyQt5 does not need an equivalent of Qt's ``Q_INTERFACES`` macro in
order to use an interface class.

The ``textobject.py`` example includedd with PyQt5 demonstrates the use of an
interface.
