Support for Qt Properties
=========================

PyQt5 does not support the setting and getting of Qt properties as if they were
normal instance attributes.  This is because the name of a property often
conflicts with the name of the property's getter method.

However, PyQt5 does support the initial setting of properties using keyword
arguments passed when an instance is created.  For example::

    act = QAction("&Save", self, shortcut=QKeySequence.Save,
            statusTip="Save the document to disk", triggered=self.save)

The example also demonstrates the use of a keyword argument to connect a
signal to a slot.

PyQt5 also supports setting the values of properties (and connecting a signal
to a slot) using the :meth:`~PyQt5.QtCore.QObject.pyqtConfigure()` method.  For
example, the following gives the same results as above::

    act = QAction("&Save", self)
    act.pyqtConfigure(shortcut=QKeySequence.Save,
            statusTip="Save the document to disk", triggered=self.save)


Defining New Qt Properties
--------------------------

A new Qt property may be defined using the :func:`~PyQt5.QtCore.pyqtProperty`
function.  It is used in the same way as the standard Python ``property()``
function.  In fact, Qt properties defined in this way also behave as Python
properties.

.. function:: PyQt5.QtCore.pyqtProperty(type[, fget=None[, fset=None[, freset=None[, fdel=None[, doc=None[, designable=True[, scriptable=True[, stored=True[, user=False[, constant=False[, final=False[, notify=None[, revision=0]]]]]]]]]]]]])

    Create a property that behaves as both a Python property and a Qt property.

    :param type:
        the type of the property.  It is either a Python type object or a
        string that is the name of a C++ type.
    :param fget:
        the optional callable used to get the value of the property.
    :param fset:
        the optional callable used to set the value of the property.
    :param freset:
        the optional callable used to reset the value of the property to its
        default value.  It is ignored by Python
    :param fdel:
        the optional callable used to delete the property.  It is ignored by
        Qt.
    :param doc:
        the optional docstring of the property.  It is ignored by Qt.
    :param designable:
        optionally sets the Qt ``DESIGNABLE`` flag.  It is ignored by Python
    :param scriptable:
        optionally sets the Qt ``SCRIPTABLE`` flag.  It is ignored by Python
    :param stored:
        optionally sets the Qt ``STORED`` flag.  It is ignored by Python
    :param user:
        optionally sets the Qt ``USER`` flag.  It is ignored by Python
    :param constant:
        optionally sets the Qt ``CONSTANT`` flag.  It is ignored by Python
    :param final:
        optionally sets the Qt ``FINAL`` flag.  It is ignored by Python
    :param notify:
        the optional unbound notify signal.  It is ignored by Python
    :param revision:
        the revision exported to QML.  It is ignored by Python
    :rtype:
        the property object.
      
It is also possible to use :func:`~PyQt5.QtCore.pyqtProperty` as a decorator in
the same way as the standard Python ``property()`` function.  The following
example shows how to define an ``int`` property with a getter and setter::

    from PyQt5.QtCore import QObject, pyqtProperty

    class Foo(QObject):

        def __init__(self):
            QObject.__init__(self)

            self._total = 0

        @pyqtProperty(int)
        def total(self):
            return self._total

        @total.setter
        def total(self, value):
            self._total = value

If you prefer the Qt terminology you may also use ``write`` instead of
``setter`` (and ``read`` instead of ``getter``).
