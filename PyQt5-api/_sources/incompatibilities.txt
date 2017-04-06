Incompatibilities with Earlier Versions
=======================================

PyQt v5.5
---------

Conversion of Latin-1 Strings to :class:`~PyQt5.QtCore.QByteArray`
******************************************************************

This version removes the automatic conversion of a Latin-1 encoded string when
a :class:`~PyQt5.QtCore.QByteArray` is expected.  It was deprecated in PyQt
v5.4.


Unhandled Python Exceptions
***************************

There are a number of situations where Python code is executed from C++.
Python reimplementations of C++ virtual methods is probably the most common
example.  In previous versions, if the Python code raised an exception then
PyQt would call Python's :c:func:`PyErr_Print` function which would then call
:func:`sys.excepthook`.  The default exception hook would then display the
exception and any traceback to ``stderr``.  There are number of disadvantages
to this behaviour:

- the application does not terminate, meaning the behaviour is different to
  when exceptions are raised in other situations

- the output written to ``stderr`` may not be seen by the developer or user
  (particularly if it is a GUI application) thereby hiding the fact that the
  application is trying to report a potential bug.

This behaviour was deprecated in PyQt v5.4.  In PyQt v5.5 an unhandled Python
exception will result in a call to Qt's :cpp:func:`qFatal` function.  By
default this will call :c:func:`abort` and the application will terminate.
Note that an application installed exception hook will still take precedence.


PyQt v5.3
---------

Execution of Python Slots
*************************

In previous versions, when a signal was emitted to a Python slot
that was not decorated with :func:`~PyQt5.QtCore.pyqtSlot`, it would not check
that the underlying C++ receiver instance still existed.  This matched the
PyQt4 behaviour at the time that PyQt5 v5.0 was released, but doesn't reflect
the standard C++ behaviour.

The lack of a check meant that an object could connect its
:func:`~PyQt5.QtCore.QObject.destroyed` signal to itself so that it could
monitor when its underlying C++ instance was destroyed.  Unfortunately this
turned out to be a potential source of obscure bugs for more common code.

In this version the check has been introduced - hence creating an
incompatibility for any code that relies on the earlier behaviour.  As a
workaround for this the ``no_receiver_check`` argument has been added to
:func:`~PyQt5.QtCore.QObject.connect` which allows the check to be suppressed
on a per connection basis.


Qt Signals with Default Arguments
*********************************

In previous versions Qt signals with default arguments were exposed as multiple
signals each with one additional default argument.  For example
``QAbstractButton::clicked(bool checked = false)`` was exposed as
``QAbstractButton::clicked(bool checked)`` and ``QAbstractButton::clicked()``
where the former was the default signal.  It was therefore possible to index
the latter by using an empty tuple as the key - although there was no benefit
in doing so.

In this version only the signal with all arguments supplied is exposed.
However the signal's ``emit()`` method still supports the default argument,
i.e. when used normally the change should not be noticed.
