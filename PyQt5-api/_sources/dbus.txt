.. _ref-dbus:

DBus Support
============

PyQt5 provides two different modules that implement support for DBus.  The
:mod:`~PyQt5.QtDBus` module provides wrappers for the standard Qt DBus classes.
The :mod:`dbus.mainloop.pyqt5` module add support for the Qt event loop to the
standard ``dbus-python`` Python module.


:mod:`~PyQt5.QtDBus`
--------------------

The :mod:`~PyQt5.QtDBus` module is used in a similar way to the C++ library it
wraps.  The main difference is in the way it supports the demarshalling of
DBus structures.  C++ relies on the template-based registration of types using
``qDBusRegisterMetaType()`` which isn't possible from Python.  Instead a slot
that accepts a DBus structure in an argument should specify a slot with a
single :class:`~PyQt5.QtDBus.QDBusMessage` argument.  The implementation of the
slot should then extract the arguments from the message using its
:meth:`~PyQt5.QtDBus.QDBusMessage.arguments` method.

For example, say we have a DBus method called ``setColors()`` that has a single
argument that is an array of structures of three integers (red, green and
blue).  The DBus signature of the argument would then be ``a(iii)``.  In C++
you would typically define a class to hold the red, green and blue values and
so your code would include the following (incomplete) fragments::

    struct Color
    {
        int red;
        int green;
        int blue;
    };
    Q_DECLARE_METATYPE(Color)

    qDBusRegisterMetaType<Color>();

    class ServerAdaptor : public QDBusAbstractAdaptor
    {
        Q_OBJECT

    public slots:
        void setColors(QList<const Color &> colors);
    };

The Python version is, of course, much simpler::

    class ServerAdaptor(QDBusAbstractAdaptor):

        @pyqtSlot(QDBusMessage)
        def setColors(self, message):
            # Get the single argument.
            colors = message.arguments()[0]

            # The argument will be a list of 3-tuples of ints.
            for red, green, blue in colors:
                print("RGB:", red, green, blue)

Note that this technique can be used for arguments of any type, it is only
require if DBus structures are involved.


:mod:`dbus.mainloop.pyqt5`
--------------------------

The :mod:`dbus.mainloop.pyqt5` module provides support for the Qt event loop to
``dbus-python``.  The module's API is almost identical to that of the
:mod:`dbus.mainloop.glib` modules that provides support for the GLib event
loop.

The :mod:`dbus.mainloop.pyqt5` module contains the following function.

.. function:: DBusQtMainLoop(set_as_default=False)

    Create a ``dbus.mainloop.NativeMainLoop`` object that uses the the Qt event
    loop.

    :param set_as_default:
        is optionally set to make the main loop instance the default for all
        new Connection and Bus instances.  It may only be specified as a
        keyword argument, and not as a positional argument.

The following code fragment is all that is normally needed to set up the
standard ``dbus-python`` language bindings package to be used with PyQt5::

    from dbus.mainloop.pyqt5 import DBusQtMainLoop

    DBusQtMainLoop(set_as_default=True)
