Other Support for Dynamic Meta-objects
======================================

PyQt5 creates a :class:`~PyQt5.QtCore.QMetaObject` instance for any Python
sub-class of :class:`~PyQt5.QtCore.QObject` without the need for the equivalent
of Qt's ``Q_OBJECT`` macro.  Most of a :class:`~PyQt5.QtCore.QMetaObject` is
populated automatically by defining signals, slots and properties as described
in previous sections.  In this section we cover the ways in which the remaining
parts of a :class:`~PyQt5.QtCore.QMetaObject` are populated.


:func:`~PyQt5.QtCore.Q_ENUMS` and :func:`~PyQt5.QtCore.Q_FLAGS`
---------------------------------------------------------------

.. versionadded:: 5.2

The :func:`~PyQt5.QtCore.Q_ENUMS` and :func:`~PyQt5.QtCore.Q_FLAGS` functions
declare enumerated types and flag types respectively that are published in the
:class:`~PyQt5.QtCore.QMetaObject`.  The typical use in PyQt5 is to declare
symbolic constants that can be used by QML, and as type of properties that can
be set in Qt Designer.

Each function takes a number of Python type objects that implement the
enumerated or flag type.  For example::

    from PyQt5.QtCore import Q_ENUMS, Q_FLAGS, QObject


    class Instruction(QObject):

        class Direction:
            Up, Down, Left, Right = range(4)

        Q_ENUMS(Direction)

        class Status:
            Null = 0x00
            Urgent = 0x01
            Acknowledged = 0x02
            Completed = 0x04

        Q_FLAGS(Status)


:func:`~PyQt5.QtCore.Q_CLASSINFO`
---------------------------------

The :func:`~PyQt5.QtCore.Q_CLASSINFO` function is used in the same way as Qt's
macro of the same name, i.e. it is called from a class's definition in order to
specify a name/value pair that is placed in the class's
:class:`~PyQt5.QtCore.QMetaObject`.

For example it is used by QML to define the default property of a class::

    from PyQt5.QtCore import Q_CLASSINFO, QObject


    class BirthdayParty(QObject):

        Q_CLASSINFO('DefaultProperty', 'guests')
