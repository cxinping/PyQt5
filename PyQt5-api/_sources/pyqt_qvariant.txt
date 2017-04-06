.. _ref-qvariant:

Support for :class:`~PyQt5.QtCore.QVariant`
===========================================

PyQt4 implements two APIs for :class:`~PyQt5.QtCore.QVariant`.  v1 (the default
for Python v2) exposes the :class:`~PyQt5.QtCore.QVariant` class to Python and
requires applications to explicitly convert a :class:`~PyQt5.QtCore.QVariant`
to the actual value.  v2 (the default for Python v3) does not expose the
:class:`~PyQt5.QtCore.QVariant` class to Python and automatically converts a
:class:`~PyQt5.QtCore.QVariant` to the actual value.  While this is usually the
best thing to do, it does raise problems of its own:

- Information is lost when converting between a C++
  :class:`~PyQt5.QtCore.QVariant` and the corresponding Python object.  For
  example a :class:`~PyQt5.QtCore.QVariant` distinguishes between signed and
  unsigned integers but Python doesn't.  Normally this doesn't matter but some
  applications may need to make the distinction.

- There is no obvious way to represent a null :class:`~PyQt5.QtCore.QVariant`
  as a standard Python object.  PyQt4 introduced the ``QPyNullVariant`` class
  to address this problem.

Multiple APIs are intended to help manage an application's use of an old API to
a newer, incompatible API.  They cannot be used to temporarily change the
behaviour - modules that rely on different API versions cannot be used in the
same application.

In PyQt5 the implementation of :class:`~PyQt5.QtCore.QVariant` is different to
those of PyQt4.  By default the behaviour is the same as PyQt4's v2 API.
However it is possible to temporarily suppress the automatic conversion of a
C++ :class:`~PyQt5.QtCore.QVariant` to a Python object and to return a wrapped
Python :class:`~PyQt5.QtCore.QVariant` instead - behaviour similar to PyQt4's
v1 API - by calling the :func:`sip.enableautoconversion` function.

The actual value of a wrapped Python :class:`~PyQt5.QtCore.QVariant` is
obtained by calling its :meth:`~PyQt5.QtCore.QVariant.value` method.  (Note
that in PyQt4's v1 API this method is called ``toPyObject()``.)

PyQt5 does not support the ``QPyNullVariant`` class as it is no longer needed.
