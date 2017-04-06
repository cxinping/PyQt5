Deploying Commercial PyQt5 Applications
=======================================

Deploying commercial PyQt5 applications can be a complicated process for a
number of reasons:

- It is usually better not to rely on pre-requisite packages being already
  installed on the user's system.  This means that as well as your application
  code, you also need to include the Python interpreter, the standard library,
  third-pary packages and extension modules, and Qt itself.

- Some target platforms (iOS for example) have restrictions on how an 
  application is built in order for it to be included in app stores.

- It is necessary to discourage users from accessing the underlying PyQt5
  modules for themselves.  A user that used the modules shipped with your
  application to develop new applications would themselves be considered a
  developer and would need their own commercial PyQt5 license.

The recommended solution to all of these issues is to use `pyqtdeploy 
<http://www.riverbankcomputing.com/software/pyqtdeploy/>`__.
