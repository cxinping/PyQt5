Platform Specific Issues
========================

OS X
----

With v5.5.0 the OS X version of Qt is built so that the Qt frameworks are built
using the *rpath* mechanism.  Unfortunately this causes problems for plugin
based applications.  The Python interpreter (with it's use of dynamically
loaded C/C++ extension modules) is one such application.  The problem arises
when a Qt framework tries to dynamically load it's own plugins and those
plugins are also linked against a Qt framework.

PyQt v5.5 (and later) implements a workaround for the most common situation
which is the loading of the QPA platform plugin (``libqcocoa.dylib``) by the
:mod:`QtGui` module.  However the problem can arise with other plugins.  The
solution is the set the :envvar:`DYLD_FRAMEWORK_PATH` environment variable to
the name of the ``lib`` directory in your Qt installation, i.e. the directory
containing the Qt frameworks.

.. note::

    The problem appears to have been fixed in Qt v5.6.
