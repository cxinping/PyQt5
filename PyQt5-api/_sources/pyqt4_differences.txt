Differences Between PyQt4 and PyQt5
===================================

PyQt5 is not compatibile with PyQt4 (although experience shows that the effort
in porting applications from PyQt4 to PyQt5 is not great).  This section
describes the main differences between the two.


Supported Python Versions
-------------------------

Versions of Python earlier than v2.6 are not supported.


Deprecated Features
-------------------

PyQt5 does not support any parts of the Qt API that are marked as deprecated or
obsolete in Qt v5.0.  However it is possible that some of these have been
included accidentaly.  These are considered bugs and will be removed if found.


Multiple APIs
-------------

PyQt4 supports a number of different API versions (``QString``,
:class:`~PyQt5.QtCore.QVariant` etc.).  With the exception of
:class:`~PyQt5.QtCore.QVariant`, PyQt5 only implements v2 of those APIs for all
versions of Python.  The changed support for :class:`~PyQt5.QtCore.QVariant`,
including the removal of ``QPyNullVariant``, is described in
:ref:`ref-qvariant`.


Old-style Signals and Slots
---------------------------

PyQt4's old-style signals and slots are not supported.  Therefore the following
are not implemented in PyQt5:

- ``QObject.connect()``

- ``QObject.emit()``

- ``SIGNAL()``

- ``SLOT()``

All methods that had arguments that are usually the results of calls to
``SIGNAL()`` or ``SLOT()`` are no longer supported.  There will always be an
equivalent that takes a bound signal or callable respectively.

In addition the following methods have differences:

- :meth:`~PyQt5.QtCore.QObject.disconnect` takes no arguments and disconnects
  all connections to the :class:`~PyQt5.QtCore.QObject` instance.


New-style Signals and Slots
---------------------------

Qt implements signals with an optional argument as two separate signals, one
with the argument and one without it.  PyQt4 exposed both of these allowing you
to connect to each of them.  However, when emitting the signal, you had to use
the signal appropriate to the number of arguments being emitted.

PyQt5 exposes only the signal where all arguments are specified.  However it
allows any optional arguments to be omitted when emitting the signal.

Unlike PyQt4, PyQt5 supports the definition of properties, signals and slots in
classes not sub-classed from :class:`~PyQt5.QtCore.QObject` (i.e. in mixins).


``QtDeclarative``, ``QtScript`` and ``QtScriptTools`` Modules
-------------------------------------------------------------

PyQt4's ``QtDeclarative``, ``QtScript`` and ``QtScriptTools`` modules are not
supported.  These have been replaced by PyQt5's :mod:`~PyQt5.QtQml` and
:mod:`~PyQt5.QtQuick` modules.  Unlike PyQt4, PyQt5 supports the creation of
Python objects from QML.


``QtGui`` Module
----------------

PyQt4's ``QtGui`` module has been split into PyQt5's :mod:`~PyQt5.QtGui`,
:mod:`~PyQt5.QtPrintSupport` and :mod:`~PyQt5.QtWidgets` modules.


``QtOpenGL`` Module
-------------------

Only the :class:`~PyQt5.QtOpenGL.QGLContext`,
:class:`~PyQt5.QtOpenGL.QGLFormat` and :class:`~PyQt5.QtOpenGL.QGLWidget`
classes are supported by PyQt5.


``QtWebKit`` Module
-------------------

PyQt4's ``QtWebKit`` module has been split into PyQt5's :mod:`~PyQt5.QtWebKit`
and :mod:`~PyQt5.QtWebKitWidgets` modules.


``pyqtconfig`` Module
---------------------

PyQt4's ``pyqtconfig`` module is not supported.  The section
:ref:`ref-build-system` describes the support that PyQt5 provides to
third-party packages (e.g.
`QScintilla <http://www.riverbankcomputing.com/software/qscintilla/>`__) that
want to build on top of PyQt5.


``dbus.mainloop.qt`` Module
---------------------------

PyQt4's ``dbus.mainloop.qt`` module is called :mod:`dbus.mainloop.pyqt5` in
PyQt5.  This allows them to be installed side by side.  Their functionality is
identical.


``QDataStream``
---------------

The :meth:`~PyQt5.QtCore.QDataStream.readUInt8`,
:meth:`~PyQt5.QtCore.QDataStream.readInt8`,
:meth:`~PyQt5.QtCore.QDataStream.writeUInt8` and
:meth:`~PyQt5.QtCore.QDataStream.writeInt8` methods all interpret the values
being read and written as numeric values.  In PyQt4 they are interpreted as
single character strings.


``QFileDialog``
---------------

The ``getOpenFileNameAndFilter()``, ``getOpenFileNamesAndFilter()`` and
``getSaveFileNameAndFilter()`` methods of PyQt4's ``QFileDialog`` have now been
renamed :meth:`~PyQt5.QtWidgets.QFileDialog.getOpenFileName`,
:meth:`~PyQt5.QtWidgets.QFileDialog.getOpenFileNames` and
:meth:`~PyQt5.QtWidgets.QFileDialog.getSaveFileName` respectively in PyQt5.
PyQt4's implementations of ``getOpenFileName()``, ``getOpenFileNames()`` and
``getSaveFileName()`` are not supported in PyQt5.


``QGraphicsItemAnimation``
--------------------------

Support for the deprecated ``QGraphicsItemAnimation`` class has been removed.
If porting an existing PyQt4 application then consider first updating it to use
:class:`~PyQt5.QtCore.QPropertyAnimation` instead.


``QMatrix``
-----------

Support for the deprecated ``QMatrix`` class has been removed.  If porting an
existing PyQt4 application then consider first updating it to use
:class:`~PyQt5.QtGui.QTransform` instead.


``QPyTextObject``
-----------------

PyQt4 implements the ``QPyTextObject`` as a workaround for the inability to
define a Python class that is sub-classed from more than one Qt class.  PyQt5
does support the ability to define a Python class that is sub-classed from more
than one Qt class so long as all but one of the Qt classes are interfaces, i.e.
they have been declared in C++ as such using ``Q_DECLARE_INTERFACE``.
Therefore ``QPyTextObject`` is not implemented in PyQt5.


``QSet``
--------

In PyQt4, ``QSet`` was implemented as a list in Python v2 and a set in Python
v3.  In PyQt5 ``QSet`` is always implemented as a set.


``pyuic5``
----------

:program:`pyuic5` does not support the ``--pyqt3-wrapper`` flag of ``pyuic4``.


``pyrcc5``
----------

:program:`pyrcc5` does not support the ``-py2`` and ``-py3`` flags of
``pyrcc4``.  The output of :program:`pyrcc5` is compatible with all versions of
Python starting with Python v2.6.


Cooperative Multi-inheritance
-----------------------------

Unlike PyQt4, PyQt5 classes implement cooperative multi-inheritance.  In other
words PyQt5 classes always do the equivalent of the following Python v3 code
in their ``__init__`` methods (where ``kwds`` is a dictionary of unused keyword
arguments)::

    super().__init__(**kwds)

This means that those unused keyword arguments are passed to the ``__init__``
methods of any mixin classes.  Those mixin classes must cooperate, i.e. they
must make a similar call if they have their own ``__init__`` implementations.

When using multiple inheritance in PyQt4 it is common to call the ``__init__``
methods of the super-classes explicitly, for example::

    class MyQObject(QObject, MyMixin):
        def __init__(self, parent, mixin_arg):
            QObject.__init__(self, parent)
            MyMixin.__init__(self, mixin_arg)

            # Other initialisation...

In PyQt5 the above would cause ``MyMixin.__init__`` to be called twice.
Instead it should be implemented as follows::

    class MyQObject(QObject, MyMixin):
        def __init__(self, **kwds):
            super().__init__(**kwds)

            # Other initialisation...

Note that if there is no other initialisation to do then the ``__init__``
method isn't actually needed.

The mixin class should be implemented as follows::

    class MyMixin:
        def __init__(self, mixin_arg, **kwds):
            super().__init__(**kwds)

            # Other initialisation...

If a class only inherits from a single class then it can still call the
super-class's ``__init__`` method explicitly (although it is recommended to use
``super()``).

See :ref:`ref-cooperative-multiinheritance`.


Releasing the GIL
-----------------

The GIL is only released when it is known to be needed.  PyQt4 always released
the GIL when calling Qt.


Object Destruction on Exit
--------------------------

When the Python interpreter exits PyQt4 (by default) calls the C++ destructor
of all wrapped instances that it owns.  This happens in a random order and can
therefore cause the interpreter to crash.  This behavior can be disabled by
calling the :func:`sip.setdestroyonexit` function.  PyQt5 always calls
:func:`sip.setdestroyonexit` automatically.
