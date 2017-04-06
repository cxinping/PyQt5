.. _ref-integrating-qml:

Integrating Python and QML
==========================

Qt includes QML as a means of declaratively describing a user interface and
using JavaScript as a scripting language within it.  It is possible to write
complete standalone QML applications, or to combine them with C++.  PyQt5
allows QML to be integrated with Python in exactly the same way.  In
particular:

- Python types that are sub-classed from :class:`~PyQt5.QtCore.QObject` can be
  registered with QML.

- Instances of registered Python types can be created and made available to QML
  scripts.

- Instances of registered Python types can be created by QML scripts.

- Singleton instances of registered Python types can be created automatically
  by a QML engine and made available to QML scripts.

- QML scripts interact with Python objects through their properties, signals
  and slots.

- Python properties, signals and slots can be given revision numbers that only
  those implemented by a specific version are made available to QML.


Registering Python Types
------------------------

Registering Python types with QML is done in the same way is it is done with
C++ classes, i.e. using the :func:`~PyQt5.QtQml.qmlRegisterType`,
:func:`~PyQt5.QtQml.qmlRegisterSingletonType`,
:func:`~PyQt5.QtQml.qmlRegisterUncreatableType` and
:func:`~PyQt5.QtQml.qmlRegisterRevision` functions.

In C++ these are template based functions that take the C++ class, and
sometimes a revision, as template arguments.  In the Python implementation
these are simply passed as the first arguments to the respective functions.


A Simple Example
----------------

The following simple example demonstates the implementation of a Python class
that is registered with QML.  The class defines two properties.  A QML script
is executed which creates an instance of the class and sets the values of the
properties.  That instance is then returned to Python which then prints the
values of those properties.

Hopefully the comments are self explanatory::

    import sys

    from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
    from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine


    # This is the type that will be registered with QML.  It must be a
    # sub-class of QObject.
    class Person(QObject):
        def __init__(self, parent=None):
            super().__init__(parent)

            # Initialise the value of the properties.
            self._name = ''
            self._shoeSize = 0

        # Define the getter of the 'name' property.  The C++ type of the
        # property is QString which Python will convert to and from a string.
        @pyqtProperty('QString')
        def name(self):
            return self._name

        # Define the setter of the 'name' property.
        @name.setter
        def name(self, name):
            self._name = name

        # Define the getter of the 'shoeSize' property.  The C++ type and
        # Python type of the property is int.
        @pyqtProperty(int)
        def shoeSize(self):
            return self._shoeSize

        # Define the setter of the 'shoeSize' property.
        @shoeSize.setter
        def shoeSize(self, shoeSize):
            self._shoeSize = shoeSize


    # Create the application instance.
    app = QCoreApplication(sys.argv)

    # Register the Python type.  Its URI is 'People', it's v1.0 and the type
    # will be called 'Person' in QML.
    qmlRegisterType(Person, 'People', 1, 0, 'Person')

    # Create a QML engine.
    engine = QQmlEngine()

    # Create a component factory and load the QML script.
    component = QQmlComponent(engine)
    component.loadUrl(QUrl('example.qml'))

    # Create an instance of the component.
    person = component.create()

    if person is not None:
        # Print the value of the properties.
        print("The person's name is %s." % person.name)
        print("They wear a size %d shoe." % person.shoeSize)
    else:
        # Print all errors that occurred.
        for error in component.errors():
            print(error.toString())

The following is the ``example.qml`` QML script that is executed::

    import People 1.0

    Person {
        name: "Bob Jones"
        shoeSize: 12
    }


Using :class:`~PyQt5.QtQml.QQmlListProperty`
--------------------------------------------

Defining list-based properties in Python that can be updated from QML is done
using the :class:`~PyQt5.QtQml.QQmlListProperty` class.  However the way it is
used in Python is slightly different to the way it is used in C++.

In the simple case :class:`~PyQt5.QtQml.QQmlListProperty` wraps a Python list
that is usually an instance sttribute, for example::

    class BirthdayParty(QObject):

        def __init__(self, parent=None):
            super().__init__(parent)

            # The list which will be accessible from QML.
            self._guests = []

        @pyqtProperty(QQmlListProperty)
        def guests(self):
            return QQmlListProperty(Person, self, self._guests)

QML can now manipulate the Python list of ``Person`` instances.
:class:`~PyQt5.QtQml.QQmlListProperty` also acts as a proxy for the Python list
so that the following can be written::

    for guest in party.guests:
        print("Guest:", guest.name)

:class:`~PyQt5.QtQml.QQmlListProperty` can also be used to wrap a *virtual*
list.  The following code fragment is taken from the
``chapter5-listproperties.py`` example included with PyQt5::

    class PieChart(QQuickItem):

        @pyqtProperty(QQmlListProperty)
        def slices(self):
            return QQmlListProperty(PieSlice, self,
                    append=lambda pie_ch, pie_sl: pie_sl.setParentItem(pie_ch))

``PieChart`` and ``PieSlice`` are Quick items that are registered using
:func:`~PyQt5.QtQml.qmlRegisterType`.  Instances of both can be created from
QML.  ``slices`` is a property of ``PieChart`` that, as far as QML is
concerned, is a list of ``PieSlice`` instances.

The :func:`~PyQt5.QtCore.pyqtProperty` decorator specifies that the property is
a :class:`~PyQt5.QtQml.QQmlListProperty`, that its name is ``slices`` and that
the ``slices()`` function is its getter.

The getter returns an instance of :class:`~PyQt5.QtQml.QQmlListProperty`.  This
specifies that elements of the list should be of type ``PieSlice``, that the
``PieChart`` instance (i.e. ``self``) has the property, and defines the
callable that will be invoked in order to append a new element to the list.

The ``append`` callable is passed two arguments: the object whose property is
to be updated (i.e. the ``PyChart`` instance), and the element to be appended
(i.e. a ``PieSlice`` instance).  Here we simply set the chart as the slice's
parent item.  Note that there isn't actually a list anywhere - this is because,
in this particular example, one isn't needed.

The signature of the ``append`` callable is slightly different to that of the
corresponding C++ function.  In C++ the first argument is the
:class:`~PyQt5.QtQml.QQmlListProperty` instance rather than the ``PyChart``
instance.  The signatures of the ``at``, ``clear`` and ``count`` callables are
different in the same way.


Using Attached Properties
-------------------------

In order to use attached properties in C++, three steps need to be taken.

- A type that has attached properties must implement a static function called
  ``qmlAttachedProperties``.  This is a factory that creates an instance of the
  properties object to attach.

- A type that has attached properties needs to be defined as such using the
  ``QML_DECLARE_TYPEINFO`` macro with the ``QML_HAS_ATTACHED_PROPERTIES``
  argument.

- The instance of an attached properties object is retrieved using the
  ``qmlAttachedPropertiesObject()`` template function.  The template type is
  the type that has the attached properties.

PyQt5 uses similar, but slightly simpler steps to achieve the same thing.

- When calling :func:`~PyQt5.QtQml.qmlRegisterType` to register a type that
  has attached properties the type of the properties object is passed as the
  ``attachedProperties`` argument.  This type will be used as the factory for
  creating an instance of the properties object.

- The instance of an attached properties object is retrieved using the
  :func:`~PyQt5.QtQml.qmlAttachedPropertiesObject` function in the same way
  that you would from C++.  Just like :func:`~PyQt5.QtQml.qmlRegisterType`,
  :func:`~PyQt5.QtQml.qmlAttachedPropertiesObject` takes an additional first
  argument that is the type that, in C++, would be the template argument.

See the ``attach.py`` example included with PyQt5 for a complete example
showing the use of attached properties.


Using Property Value Sources
----------------------------

Property values sources are implemented in PyQt5 in the same way as they are
implemented in C++.  Simply sub-class from both :class:`~PyQt5.QtCore.QObject`
and :class:`~PyQt5.QtQml.QQmlPropertyValueSource` and provide an implementation
of the :meth:`~PyQt5.QtQml.QQmlPropertyValueSource.setTarget` method.


Using :class:`~PyQt5.QtQml.QQmlParserStatus`
--------------------------------------------

Monitoring the QML parser status is implemented in PyQt5 in the same way as it
is implemented in C++.  Simply sub-class from both
:class:`~PyQt5.QtCore.QObject` and :class:`~PyQt5.QtQml.QQmlParserStatus` and
provide implementations of the :meth:`~PyQt5.QtQml.QQmlParserStatus.classBegin`
and :meth:`~PyQt5.QtQml.QQmlParserStatus.componentComplete` methods.


Writing Python Plugins for :program:`qmlscene`
----------------------------------------------

Qt allows plugins that implement QML modules to be written that can be
dynamically loaded by a C++ application (e.g. :program:`qmlscene`).  These
plugins are sub-classes of :class:`~PyQt5.QtQml.QQmlExtensionPlugin`.  PyQt5
supports exactly the same thing and allows those plugin to be written in
Python.  In other words it is possible to provide QML extensions written in
Python to a C++ application, and to provide QML extensions written in C++ to a
Python application.

PyQt5 provides a QML plugin called ``pyqt5qmlplugin``.  This acts as a wrapper
around the Python code that implements the plugin.  It handles the loading of
the Python interpreter, locating and importing the Python module that contains
the implementation of :class:`~PyQt5.QtQml.QQmlExtensionPlugin`, creating an
instance of that class, and calling the instance's
:meth:`~PyQt5.QtQml.QQmlExtensionPlugin.registerTypes` method.  By default the
``pyqt5qmlplugin`` is installed in the ``PyQt5`` sub-directory of your Qt
installation's ``plugin`` directory.

.. note::

    ``pyqt5qmlplugin`` is the name of the plugin as seen by QML.  Its actual
    filename will be different and operating system dependent.

A QML extension module is a directory containing a file called ``qmldir``.  The
file contains the name of the module and the name of the plugin that implements
the module.  It may also specify the directory containing the plugin.  Usually
this isn't needed because the plugin is installed in the same directory.

Therefore, for a QML extension module called ``Charts``, the contents of the
``qmldir`` file might be::

    module Charts
    plugin pyqt5qmlplugin /path/to/qt/plugins/PyQt5

The ``pyqt5qmlplugin`` expects to find a Python module in the same directory
with a filename ending with ``plugin.py`` or ``plugin.pyw``.  In this case the
name ``chartsplugin.py`` would be a sensible choice.  Before importing this
module ``pyqt5qmlplugin`` first places the name of the directory at the start
of :attr:`sys.path`.

.. note::

    ``pyqt5qmlplugin`` has to locate the directory containing the ``qmldir``
    file itself.  It does this using the same algorithm used by QML, i.e. it
    searches some standard locations and locations specified by the
    :envvar:`QML2_IMPORT_PATH` environment variable.  When using
    :program:`qmlscene`, ``pyqt5qmlplugin`` will not know about any additional
    locations specified by its ``-I`` option.  Therefore,
    :envvar:`QML2_IMPORT_PATH` should always be used to specify additional
    locations to search.

Due to a limitation in QML it is not possible for multiple QML modules to use
the same C++ plugin.  In C++ this is not a problem as there is a one-to-one
relationship between a module and the plugin.  However, when using Python,
``pyqt5qmlplugin`` is used by every module.  There are two solutions to this:

- on operating systems that support it, place a symbolic link in the directory
  containing the ``qmldir`` file that points to the actual ``pyqt5qmlplugin``

- make a copy of ``pyqt5qmlplugin`` in the directory containing the ``qmldir``
  file.

In both cases the contents of the ``qmldir`` file can be simplifed to::

    module Charts
    plugin pyqt5qmlplugin

PyQt5 provides an example that can be run as follows::

    cd /path/to/examples/quick/tutorials/extending/chapter6-plugins
    QML2_IMPORT_PATH=. /path/to/qmlscene app.qml
