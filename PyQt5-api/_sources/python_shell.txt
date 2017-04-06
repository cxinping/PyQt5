Using PyQt5 from the Python Shell
=================================

PyQt5 installs an input hook (using ``PyOS_InputHook``) that processes events
when an interactive interpreter is waiting for user input.  This means that
you can, for example, create widgets from the Python shell prompt, interact
with them, and still being able to enter other Python commands.

For example, if you enter the following in the Python shell::

    >>> from PyQt5.QtWidgets import QApplication, QWidget
    >>> a = QApplication([])
    >>> w = QWidget()
    >>> w.show()
    >>> w.hide()
    >>>

The widget would be displayed when ``w.show()`` was entered and hidden as soon
as ``w.hide()`` was entered.

The installation of an input hook can cause problems for certain applications
(particularly those that implement a similar feature using different means).
The :mod:`~PyQt5.QtCore` module contains the
:func:`~PyQt5.QtCore.pyqtRemoveInputHook` and
:func:`~PyQt5.QtCore.pyqtRestoreInputHook` functions that remove and restore
the input hook respectively.
