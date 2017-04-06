Introduction
============

This is the reference guide for PyQt5 5.6.  PyQt5 is a set of
`Python <http://www.python.org>`__ bindings for v5 of the Qt application
framework from `The Qt Company <http://www.qt.io>`__.

Qt is a set of C++ libraries and development tools that includes platform
independent abstractions for graphical user interfaces, networking, threads,
regular expressions, SQL databases, SVG, OpenGL, XML, user and application
settings, positioning and location services, short range communications (NFC
and Bluetooth) and access to the cloud.  PyQt5 implements over 1000 of these
classes as a set of Python modules.

PyQt5 supports the Windows, Linux, UNIX, Android, OS X and iOS platforms.

PyQt5 does not include Qt itself - you must obtain it separately.

The homepage for PyQt5 is http://www.riverbankcomputing.com/software/pyqt/.
Here you will always find the latest stable version, current development
previews, and the latest version of this documentation.

PyQt5 is built using the `SIP bindings generator
<http://www.riverbankcomputing.com/software/sip/>`__.  SIP must be installed in
order to build and use PyQt5.

Earlier versions of Qt are supported by PyQt4.


License
-------

PyQt5 is dual licensed on all platforms under the Riverbank Commercial License
and the GPL v3.  Your PyQt5 license must be compatible with your Qt license.
If you use the GPL version then your own code must also use a compatible
license.

PyQt5, unlike Qt, is not available under the LGPL.

You can purchase a commercial PyQt5 license `here
<http://www.riverbankcomputing.com/commercial/buy>`__.


PyQt5 Components
----------------

.. module:: PyQt5

PyQt5 comprises a number of different components.  First of all there are a
number of Python extension modules.  These are all installed in the
:mod:`PyQt5` Python package.

.. module:: PyQt5.QAxContainer
    :platform:  Windows

- :mod:`~PyQt5.QAxContainer` contains classes that allow access to ActiveX
  controls and COM objects.  It does not support the ability to write ActiveX
  servers in Python.  It is only available under Windows.

.. module:: PyQt5.QtBluetooth

- :mod:`~PyQt5.QtBluetooth` contains classes that enables an application to
  scan for devices and connect and interact with them.

.. module:: PyQt5.QtCore

- :mod:`~PyQt5.QtCore` contains the core classes, including the event loop and
  Qt's signal and slot mechanism.  It also includes platform independent
  abstractions for animations, state machines, threads, mapped files, shared
  memory, regular expressions, and user and application settings.

.. module:: PyQt5.QtDBus
    :platform:  UNIX

- :mod:`~PyQt5.QtDBus` contains classes that support Inter-Process
  Communication using the D-Bus protocol.  It is not available under Windows.

.. module:: PyQt5.QtDesigner

- :mod:`~PyQt5.QtDesigner` contains classes that allow Qt Designer to be
  extended using PyQt5.  See :ref:`ref-designer-plugins` for a full description
  of how to do this.

.. module:: PyQt5.QtGui

- :mod:`~PyQt5.QtGui` contains classes for windowing system integration, event
  handling, 2D graphics, basic imaging, fonts and text.  It also containes a
  complete set of OpenGL and OpenGL ES bindings (see :ref:`ref-opengl`).
  Application developers would normally use this with higher level APIs such as
  those contained in the :mod:`~PyQt5.QtWidgets` module.

.. module:: PyQt5.QtHelp

- :mod:`~PyQt5.QtHelp` contains classes for creating and viewing searchable
  documentation.

.. module:: PyQt5.QtLocation

- :mod:`~PyQt5.QtLocation` contains classes for accessing geocoding and
  navigation information, and also place search.  It allows the creation of
  mapping solutions using data from some of the popular location services.

.. module:: PyQt5.QtMacExtras
    :platform:  OS X, iOS

- :mod:`~PyQt5.QtMacExtras` contains additional classes that are specific to
  OS X and iOS.

.. module:: PyQt5.QtMultimedia

- :mod:`~PyQt5.QtMultimedia` contains classes to handle multimedia content and
  APIs to access camera and radio functionality.

.. module:: PyQt5.QtMultimediaWidgets

- :mod:`~PyQt5.QtMultimediaWidgets` contains classes to handle multimedia
  content in :mod:`~PyQt5.QtWidgets` based applications.

.. module:: PyQt5.QtNetwork

- :mod:`~PyQt5.QtNetwork` contains classes for writing UDP and TCP clients and
  servers.  It includes classes that implement HTTP clients and support DNS
  lookups.

.. module:: PyQt5.QtNfc

- :mod:`~PyQt5.QtNfc` contains classes to provide connectivity between NFC
  enabled devices.  The NFC API provides APIs for interacting with NFC Forum
  Tags and NFC Forum Devices, including target detection and loss, registering
  NDEF message handlers, reading and writing NDEF messages on NFC Forum Tags
  and sending tag specific commands.

.. module:: PyQt5.QtOpenGL

- :mod:`~PyQt5.QtOpenGL` contains classes that allow the use of OpenGL in
  rendering 3D graphics in :mod:`~PyQt5.QtWidgets` based applications.

.. module:: PyQt5.QtPositioning

- :mod:`~PyQt5.QtPositioning` contains classes to determine a position by using
  a variety of possible sources, including satellite, or Wi-Fi, or a text file,
  and so on.  That information can then be used to, for example, determine a
  position on a map.  In addition satellite information can be retrieved and
  area based monitoring can be performed.

.. module:: PyQt5.QtPrintSupport

- :mod:`~PyQt5.QtPrintSupport` contains classes to allow applications to print
  to locally attached and remote printers.  It also enables the generation of
  PostScript and PDF files.

.. module:: PyQt5.QtQml

- :mod:`~PyQt5.QtQml` contains classes to allow applications to integrate
  support for QML and JavaScript.  Python objects can be exported to QML or be
  created from QML in the same way that Qt allows the same with C++ instances.
  See :ref:`ref-integrating-qml` for a fuller description of how to do this.

.. module:: PyQt5.QtQuick

- :mod:`~PyQt5.QtQuick` contains classes that provide the basic elements
  necessary for creating user interfaces with QML.

.. module:: PyQt5.QtQuickWidgets

- :mod:`~PyQt5.QtQuickWidgets` contains classes that support the display of a
  QML scene in a traditional widget.

.. module:: PyQt5.QtSensors

- :mod:`~PyQt5.QtSensors` contains classes that provide access to a system's
  hardware sensors including accelerometers, altimeters, ambient light and
  temperature sensors, gyroscopes and magnetometers.  Note that sensor gestures
  are not currently supported.

.. module:: PyQt5.QtSerialPort

- :mod:`~PyQt5.QtSerialPort` contains classes that provide access to a system's
  serial ports.

.. module:: PyQt5.QtSql

- :mod:`~PyQt5.QtSql` contains classes that integrate with SQL databases.  It
  includes editable data models for database tables that can be used with GUI
  classes.  It also includes an implementation of
  `SQLite <http://www.sqlite.org>`__.

.. module:: PyQt5.QtSvg

- :mod:`~PyQt5.QtSvg` contains classes for displaying the contents of SVG
  files.

.. module:: PyQt5.QtTest

- :mod:`~PyQt5.QtTest` contains functions that enable unit testing of PyQt5
  applications.  (PyQt5 does not implement the complete Qt unit test framework.
  Instead it assumes that the standard Python unit test framework will be used
  and implements those functions that simulate a user interacting with a GUI.)
  In addition the :class:`~PyQt5.QtTest.QSignalSpy` class provides easy
  introspection of Qt's signals and slots.

.. module:: PyQt5.QtWebChannel

- :mod:`~PyQt5.QtWebChannel` contains classes for transparently accessing
  :class:`~PyQt5.QtCore.QObject` or QML objects from HTML clients.

.. module:: PyQt5.QtWebEngineCore

- :mod:`~PyQt5.QtWebEngineCore` contains core classes used by the
  :mod:`~PyQt5.QtWebEngineWidgets` module.

.. module:: PyQt5.QtWebEngineWidgets

- :mod:`~PyQt5.QtWebEngineWidgets` contains classes for a Chromium based
  implementation of a web browser.  This supercedes the :mod:`~PyQt5.QtWebKit`
  module and provides better and up-to-date support for HTML, CSS and
  JavaScript features.  However it also consumes more resources and doesn't
  give direct access to the network stack and the HTML document via C++ APIs.

  .. note::

    :mod:`~PyQt5.QtWebEngineWidgets` is not normally available under Windows
    using versions of Python earlier than v3.5 because of compiler
    incompatibilities.

.. module:: PyQt5.QtWebKit

- :mod:`~PyQt5.QtWebKit` contains classes for a WebKit2 based implementation of
  a web browser.

.. module:: PyQt5.QtWebKitWidgets

- :mod:`~PyQt5.QtWebKitWidgets` contains classes for a WebKit1 based
  implementation of a web browser for use in :mod:`~PyQt5.QtWidgets` based
  applications.

.. module:: PyQt5.QtWebSockets

- :mod:`~PyQt5.QtWebSockets` contains classes that implement the WebSocket
  protocol described in RFC 6455.

.. module:: PyQt5.QtWidgets

- :mod:`~PyQt5.QtWidgets` contains classes that provide a set of UI elements to
  create classic desktop-style user interfaces.

.. module:: PyQt5.QtWinExtras
    :platform:  Windows

- :mod:`~PyQt5.QtWinExtras` contains additional classes that are specific to
  Windows, for example providing access to Jump Lists, a progress indicator on
  a taskbar button, and a thumbnail toolbar.

.. module:: PyQt5.QtX11Extras
    :platform:  X11

- :mod:`~PyQt5.QtX11Extras` contains additional classes that are specific to
  X11.

.. module:: PyQt5.QtXml

- :mod:`~PyQt5.QtXml` module.  This module contains classes that implement SAX
  and DOM interfaces to Qt's XML parser.

.. module:: PyQt5.QtXmlPatterns

- :mod:`~PyQt5.QtXmlPatterns` contains classes that provide support for XPath,
  XQuery, XSLT and XML Schema validation.

.. module:: PyQt5.Enginio

- :mod:`~PyQt5.Enginio` implements the client-side library for accessing the Qt
  Cloud Services Managed Application Runtime.

.. module:: PyQt5.Qt

- :mod:`~PyQt5.Qt` consolidates the classes contained in all of the modules
  described above into a single module.  This has the advantage that you don't
  have to worry about which underlying module contains a particular class.  It
  has the disadvantage that it loads the whole of the Qt framework, thereby
  increasing the memory footprint of an application.  Whether you use this
  consolidated module, or the individual component modules is down to personal
  taste.

.. module:: PyQt5.uic

- :mod:`~PyQt5.uic` contains classes for handling the ``.ui`` files created by
  Qt Designer that describe the whole or part of a graphical user interface.
  It includes classes that load a ``.ui`` file and render it directly, and
  classes that generate Python code from a ``.ui`` file for later execution.

PyQt5 contains plugins that enable Qt Designer and :program:`qmlscene` to be
extended using Python code.  See :ref:`ref-designer-plugins` and
:ref:`ref-integrating-qml` respectively for the details.

PyQt5 also contains a number of utility programs.

- :program:`pyuic5` corresponds to the Qt :program:`uic` utility.  It converts
  :mod:`~PyQt5.QtWidgets` based GUIs created using Qt Designer to Python code.

- :program:`pyrcc5` corresponds to the Qt :program:`rcc` utility.  It embeds
  arbitrary resources (eg. icons, images, translation files) described by a
  resource collection file in a Python module.

- :program:`pylupdate5` corresponds to the Qt :program:`lupdate` utility.  It
  extracts all of the translatable strings from Python code and creates or
  updates ``.ts`` translation files.  These are then used by Qt Linguist to
  manage the translation of those strings.

The `DBus <http://www.freedesktop.org/wiki/Software/DBusBindings>`__ support
module is installed as :mod:`dbus.mainloop.pyqt5`.  This module provides
support for the Qt event loop in the same way that the
:mod:`dbus.mainloop.glib` included with the standard ``dbus-python`` bindings
package provides support for the GLib event loop.  The API is described in
:ref:`ref-dbus`.  It is only available if the ``dbus-python`` v0.80 (or later)
bindings package is installed.  The :mod:`~PyQt5.QtDBus` module provides a more
Qt-like interface to DBus.

When PyQt5 is configured a file called :file:`PyQt5.api` is generated.  This
can be used by the
`QScintilla <http://www.riverbankcomputing.com/software/qscintilla/>`_
editor component to enable the use of auto-completion and call tips when
editing PyQt5 code.  The API file is installed automatically if
`QScintilla <http://www.riverbankcomputing.com/software/qscintilla/>`_
is already installed.

PyQt5 includes a large number of examples.  These are ports to Python of many
of the C++ examples provided with Qt.  They can be found in the
:file:`examples` directory.

Finally, PyQt5 contains the ``.sip`` files used by SIP to generate PyQt5
itself.  These can be used by developers of bindings of other Qt based class
libraries.


An Explanation of Version Numbers
---------------------------------

Historically the version number of PyQt bears no relation to the version of Qt
supported.  It's no longer even true that PyQt4 requires Qt v4 as it will also
build against Qt v5.  People sometimes mistakenly believe that, for example,
PyQt4 v4.8 is needed when building against Qt v4.8.

When refering to a version number we assume it consists of three numbers
separated by a dot.  These are the major number, the minor number and the
maintenance number.  The major number will always be ``5``.  The maintenance
number may be omitted if it is ``0``.

Starting with PyQt5 the version number of PyQt5 is tied, to a certain extent,
to the version of Qt v5.  This is based on the following assumptions.

- All parts of the Qt API will be supported throughout the life of Qt v5 even
  though some may be marked as deprecated or obsolete at some point.

- When new parts of the Qt API are introduced the minor number of the version
  will be increased and the maintenance number will be reset to ``0``.

Therefore, for PyQt5 v5.n.* the following are true.

- It will build against any version of Qt v5, but will not support any new
  features introduced in Qt v5.n+1 or later.

- It will support all the features of supported modules of Qt v5.n or earlier.

- Support for new modules may be added to PyQt5 at any time.  This would result
  in a change of maintenance number only.

The maintenance numbers of PyQt5 and Qt v5 are entirely unrelated to each
other.

So, for example, PyQt5 v5.1 will build against Qt v5.2 but will not support any
new features introduced in Qt v5.2.  PyQt5 v5.1 will support all the features
of supported modules of Qt v5.0 and those new features introduced in Qt v5.1.

In summary, just as with PyQt4, you should always try and use the latest
version of PyQt5 no matter what version of Qt v5 you are using.
