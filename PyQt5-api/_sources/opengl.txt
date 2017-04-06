.. _ref-opengl:

Support for OpenGL
==================

When compiled against Qt v5.1 or later, PyQt5 implements a set of either
desktop QOpenGL bindings or OpenGL ES v2 bindings depending on how Qt was
configured.  This removes the dependency on any third-party OpenGL bindings
such as :mod:`PyOpenGL`.

At the moment the desktop bindings are for OpenGL v2.0 and are mostly complete.
Other versions will be added in later releases.  If there are calls which you
need, but are currently unsupported, then please ask for the support to be
added.

Obtaining an object that implements the bindings for a particular OpenGL
version and profile is done in the same way as it is done from C++, i.e. by
calling :meth:`~PyQt5.QtGui.QOpenGLContext.versionFunctions`.  In addition, the
bindings object also contains attributes corresponding to all of the OpenGL
constants.
