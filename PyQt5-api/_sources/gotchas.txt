Things to be Aware Of
=====================

Crashes On Exit
---------------

When the Python interpreter leaves a  *scope* (for example when it returns from
a function) it will potentially garbage collect all objects local to that
scope.  The order in which it is done is, in effect, random.  Theoretically
this can cause problems because it may mean that the C++ destructors of any
wrapped Qt instances are called in an order that Qt isn't expecting and may
result in a crash.

However, in practice, this is only likely to be a problem when the application
is terminating.  For example, it is preferable that any
:class:`~PyQt5.QtWidgets.QApplication` instance is destroyed only after all
widgets are destroyed.

As a way of mitigating this possiblity PyQt5 ensures that the destructors of
any module level objects are not invoked when the application terminates.  This
means that code that follows the pattern below is unlikely to crash on exit::

    if __name__ == '__main__':
        app = QApplication(sys.argv)

        w = QWidget()
        w.show()

        app.exec()

Another common pattern (and one that is required when using setuptool entry
points) is that the above code in placed in a separate function, typically
called ``main()``.  This then causes a problem when the function returns as the
destructors of the :class:`~PyQt5.QtWidgets.QApplication` and
:class:`~PyQt5.QtWidgets.QWidget` instances may be invoked in the wrong order.
To minimise the chances of this happening, the following pattern is
recommended::

    app = None

    def main():
        global app
        app = QApplication(sys.argv)

        w = QWidget()
        w.show()

        app.exec()

    if __name__ == '__main__':
        main()

The :class:`~PyQt5.QtWidgets.QWidget` destructor may be invoked when ``main()``
returns but the module level reference to the
:class:`~PyQt5.QtWidgets.QApplication` instance will prevent its destructor
being invoked at all.


Keyword Arguments
-----------------

PyQt5 supports the use of keyword arguments for optional arguments.  Although
the PyQt5 and Qt documentation may indicate that an argument has a particular
name, you may find that PyQt5 actually uses a different name.  This is because
the name of an argument is not part of the Qt API and there is some
inconsistency in the way that similar arguments are named.  Different versions
of Qt may use a different name for an argument which wouldn't affect the C++
API but would break the Python API.

The docstrings that PyQt5 generates for all classes, functions and methods will
contain the correct argument names.  In a future version of PyQt5 the
documentation will also be guaranteed to contain the correct argument names.


Python Strings, Qt Strings and Unicode
--------------------------------------

Qt uses the ``QString`` class to represent Unicode strings, and the
``QByteArray`` to represent byte arrays or strings.  In Python v3 the
corresponding native object types are ``str`` and ``bytes``.  In Python v2 the
corresponding native object types are ``unicode`` and ``str``.

PyQt5 does its best to automatically convert between objects of the various
types.  Explicit conversions can be easily made where necessary.

In some cases PyQt5 will not perform automatic conversions where it is
necessary to distinguish between different overloaded methods.

For Python v3 the following conversions are done by default.

- If Qt expects a ``char *`` (or a ``const`` version) then PyQt5 will accept a
  ``str`` that contains only ASCII characters, a ``bytes``, a ``QByteArray``,
  or a Python object that implements the buffer protocol.

- If Qt expects a ``char`` (or a ``const`` version) then PyQt5 will accept the
  same types as for ``char *`` and also require that a single character is
  provided.

- If Qt expects a ``signed char *`` or an ``unsigned char *`` (or a ``const``
  version) then PyQt5 will accept a ``bytes``.

- If Qt expects a ``signed char`` or an ``unsigned char`` (or a ``const``
  version) then PyQt5 will accept a ``bytes`` of length 1.

- If Qt expects a ``QString`` then PyQt5 will accept a ``str``, a ``bytes``
  that contains only ASCII characters, a ``QByteArray`` or ``None``.

- If Qt expects a ``QByteArray`` then PyQt5 will also accept a ``bytes``.

- If Qt expects a ``QByteArray`` then PyQt5 will also accept a ``str`` that
  contains only Latin-1 characters.

For Python v2 the following conversions are done by default.

- If Qt expects a ``char *``, ``signed char *`` or an ``unsigned char *`` (or a
  ``const`` version) then PyQt5 will accept a ``unicode`` that contains only
  ASCII characters, a ``str``, a ``QByteArray``, or a Python object that
  implements the buffer protocol.

- If Qt expects a ``char``, ``signed char`` or an ``unsigned char`` (or a
  ``const`` version) then PyQt5 will accept the same types as for ``char *``,
  ``signed char *`` and ``unsigned char *`` and also require that a single
  character is provided.

- If Qt expects a ``QString`` then PyQt5 will accept a ``unicode``, a ``str``
  that contains only ASCII characters, a ``QByteArray`` or ``None``.

- If Qt expects a ``QByteArray`` then PyQt5 will accept a ``str``.

- If Qt expects a ``QByteArray`` then PyQt5 will accept a ``unicode`` that
  contains only Latin-1 characters.

Note that the different behaviour between Python v2 and v3 is due to v3's
reduced support for the buffer protocol.

Historically ``QString`` distinguishes between empty strings and null strings.
Current versions of Qt treat null strings as empty strings but there may be
other C++ code that PyQt5 applications call that maintains the distinction.
Consequently PyQt5 will convert ``None`` to a null ``QString``.  The reverse
conversion is not done and both a null and an empty ``QString`` will be
converted to an empty (i.e. zero length) Python string.


Garbage Collection
------------------

C++ does not garbage collect unreferenced class instances, whereas Python does.
In the following C++ fragment both colours exist even though the first can no
longer be referenced from within the program::

    col = new QColor();
    col = new QColor();

In the corresponding Python fragment, the first colour is destroyed when the
second is assigned to ``col``::

    col = QColor()
    col = QColor()

In Python, each colour must be assigned to different names.  Typically this is
done within class definitions, so the code fragment would be something like::

    self.col1 = QColor()
    self.col2 = QColor()

Sometimes a Qt class instance will maintain a pointer to another instance and
will eventually call the destructor of that second instance.  The most common
example is that a :class:`~PyQt5.QtCore.QObject` (and any of its sub-classes)
keeps pointers to its children and will automatically call their destructors.
In these cases, the corresponding Python object will also keep a reference to
the corresponding child objects.

So, in the following Python fragment, the first
:class:`~PyQt5.QtWidgets.QLabel` is not destroyed when the second is assigned
to ``lab`` because the parent :class:`~PyQt5.QtWidgets.QWidget` still has a
reference to it::

    parent = QWidget()
    lab = QLabel("First label", parent)
    lab = QLabel("Second label", parent)


Multiple Inheritance
--------------------

It is not possible to define a new Python class that sub-classes from more than
one Qt class.  The exception is classes specifically intended to act as mixin
classes such as those (like :class:`~PyQt5.QtQml.QQmlParserStatus`) that
implement Qt interfaces.


Access to Protected Member Functions
------------------------------------

When an instance of a C++ class is not created from Python it is not possible
to access the protected member functions of that instance.  Attempts to do so
will raise a Python exception.  Also, any Python methods corresponding to the
instance's virtual member functions will never be called.


``None`` and ``NULL``
---------------------

Throughout PyQt5, the ``None`` value can be specified wherever ``NULL`` is
acceptable to the underlying C++ code.

Equally, ``NULL`` is converted to ``None`` whenever it is returned by the
underlying C++ code.


Support for ``void *``
----------------------

PyQt5 (actually SIP) represents ``void *`` values as objects of type
:class:`sip.voidptr`.  Such values are often used to pass the addresses of
external objects between different Python modules.  To make this easier, a
Python integer (or anything that Python can convert to an integer) can be used
whenever a :class:`sip.voidptr` is expected.

A :class:`sip.voidptr` may be converted to a Python integer by using the
``int()`` builtin function.

A :class:`sip.voidptr` may be converted to a Python string by using its
:meth:`~sip.voidptr.asstring` method.  The :meth:`~sip.voidptr.asstring` method
takes an optional integer argument which is the length of the data in bytes.

A :class:`sip.voidptr` may also be given a size (ie. the size of the block of
memory that is pointed to) by calling its :meth:`~sip.voidptr.setsize` method.
If it has a size then it is also able to support Python's buffer protocol and
behaves like a Python ``memoryview`` object so that the block of memory can be
treated as a mutable list of bytes.  It also means that the Python
:mod:`struct` module can be used to unpack and pack binary data structures in
memory, memory mapped files or shared memory.
