.. _ref-build-system:

The PyQt5 Extension API
=======================

An important feature of PyQt5 (and SIP generated modules in general) is the
ability for other extension modules to build on top of it.
`QScintilla <http://www.riverbankcomputing.com/software/qscintilla/>`__ is
such an example.

PyQt5 provides an extension API that can be used by other modules.  This has
the advantage of sharing code and also enforcing consistent behaviour.  Part of
the API is accessable from Python and part from C++.


Python API
----------

The Python part of the API is accessible via the :mod:`~PyQt5.QtCore` module
and is typically used by an extension module's equivalent of PyQt5's
:program:`configure.py`.

The API consists of :attr:`PyQt5.QtCore.PYQT_CONFIGURATION` which is a dict
that describes how PyQt5 was configured.  At the moment it contains a single
value called ``sip_flags`` which is a string containing the ``-t`` and ``-x``
flags that were passed to the :program:`sip` executable by
:program:`configure.py`.  Other extension modules must use the same flags in
their configuration.

This information is also provided by SIP v4's :mod:`~sip.sipconfig` module.
However this module will not be implemented by SIP v5.


C++ API
-------

The C++ API is a set of functions.  The addresses of each function is obtained
by calling SIP's :c:func:`sipImportSymbol` function with the name of the
function required.

Several of the functions are provided as a replacement for SIP v4 features
(i.e. ``SIP_ANYSLOT``, ``SIP_QOBJECT``, ``SIP_RXOBJ_CON``, ``SIP_RXOBJ_DIS``,
``SIP_SIGNAL``, ``SIP_SLOT``, ``SIP_SLOT_CON`` and ``SIP_SLOT_DIS``) that are
not supported by SIP v5.

The functions exported by PyQt5 are as follows:

.. cpp:function:: void pyqt_err_print()

    .. versionadded:: 5.4

    A replacement for :c:func:`PyErr_Print`.  In PyQt v5.4 it raises a
    deprecation warning and calls :c:func:`PyErr_Print`.  In PyQt v5.5 and
    later it passes the text of the exception and traceback to
    :c:func:`qFatal`.

.. cpp:function:: char **pyqt5_from_argv_list(PyObject *argv_list, int &argc)

    Convert a Python list to a standard C array of command line arguments and
    an argument count.

    :param argv_list:
        is the Python list of arguments.
    :param argc:
        is updated with the number of arguments in the list.
    :return:
        an array of pointers to the arguments on the heap.


.. cpp:function:: PyObject *pyqt5_from_qvariant_by_type(QVariant &value, PyObject *type)

    Convert a :class:`~PyQt5.QtCore.QVariant` to a Python object according to
    an optional Python type.

    :param value:
        is the value to convert.
    :param type:
        is the Python type.
    :return:
        the converted value.  If it is ``0`` then a Python exception will have
        been raised.

.. cpp:function:: sipErrorState pyqt5_get_connection_parts(PyObject *slot, QObject *transmitter, const char *signal_signature, bool single_shot, QObject **receiver, QByteArray &slot_signature)

    Get the receiver object and slot signature to allow a signal to be
    connected to an optional transmitter.

    :param slot:
        is the slot and should be a callable or a bound signal.
    :param transmitter:
        is the optional :class:`~PyQt5.QtCore.QObject` transmitter.
    :param signal_signature:
        is the signature of the signal to be connected.
    :param single_shot:
        is ``true`` if the signal will only ever be emitted once.
    :param receiver:
        is updated with the :class:`~PyQt5.QtCore.QObject` receiver.  This may
        be a proxy if the slot requires it.
    :param slot_signature:
        is updated with the signature of the slot.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.

.. cpp:function:: const QMetaObject *pyqt5_get_qmetaobject(PyTypeObject *type)

    Get the QMetaObject instance for a Python type.  The Python type must be a
    sub-type of :class:`~PyQt5.QtCore.QObject`'s Python type.

    :param type:
        is the Python type object.
    :return:
        the :class:`~PyQt5.QtCore.QMetaObject`.

.. cpp:function:: sipErrorState pyqt5_get_pyqtsignal_parts(PyObject *signal, QObject **transmitter, QByteArray &signal_signature)

    Get the transmitter object and signal signature from a bound signal.

    :param signal:
        is the bound signal.
    :param transmitter:
        is updated with the :class:`~PyQt5.QtCore.QObject` transmitter.
    :param signal_signature:
        is updated with the signature of the signal.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: sipErrorState pyqt5_get_pyqtslot_parts(PyObject *slot, QObject **receiver, QByteArray &slot_signature)

    Get the receiver object and slot signature from a callable decorated with
    :func:`~PyQt5.QtCore.pyqtSlot`.

    :param slot:
        is the callable slot.
    :param receiver:
        is updated with the :class:`~PyQt5.QtCore.QObject` receiver.
    :param slot_signature:
        is updated with the signature of the slot.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: sipErrorState pyqt5_get_signal_signature(PyObject *signal, const QObject *transmitter, QByteArray &signal_signature)

    Get the signature string for a bound or unbound signal.  If the signal is
    bound, and the given transmitter is specified, then it must be bound to the
    transmitter.

    :param signal:
        is the signal.
    :param transmitter:
        is the optional :class:`~PyQt5.QtCore.QObject` transmitter.
    :param signal_signature:
        is updated with the signature of the signal.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: void pyqt5_register_from_qvariant_convertor(bool (*convertor)(const QVariant &, PyObject **))

    Register a convertor function that converts a
    :class:`~PyQt5.QtCore.QVariant` value to a Python object.

    :param convertor:
        is the convertor function.  This takes two arguments.  The first
        argument is the :class:`~PyQt5.QtCore.QVariant` value to be converted.
        The second argument is updated with a reference to the result of the
        conversion and it will be ``0``, and a Python exception raised, if
        there was an error.  The convertor will return ``true`` if the value
        was handled so that no other convertor will be tried.


.. cpp:function:: void pyqt5_register_to_qvariant_convertor(bool (*convertor)(PyObject *, QVariant &, bool *))

    Register a convertor function that converts a Python object to a
    :class:`~PyQt5.QtCore.QVariant` value.

    :param convertor:
        is the convertor function.  This takes three arguments.  The first
        argument is the Python object to be converted. The second argument is a
        pointer to :class:`~PyQt5.QtCore.QVariant` value that is updated with
        the result of the conversion.  The third argument is updated with an
        error flag which will be ``false``, and a Python exception raised, if
        there was an error.  The convertor will return ``true`` if the value
        was handled so that no other convertor will be tried.


.. cpp:function:: void pyqt5_register_to_qvariant_data_convertor(bool (*convertor)(PyObject *, void *, int, bool *))

    Register a convertor function that converts a Python object to the
    pre-allocated data of a :class:`~PyQt5.QtCore.QVariant` value.

    :param convertor:
        is the convertor function.  This takes four arguments.  The first
        argument is the Python object to be converted. The second argument is a
        pointer to the pre-allocated data of a :class:`~PyQt5.QtCore.QVariant`
        value that is updated with the result of the conversion.  The third
        argument is the meta-type of the value.  The fourth argument is updated
        with an error flag which will be ``false``, and a Python exception
        raised, if there was an error.  The convertor will return ``true`` if
        the value was handled so that no other convertor will be tried.


.. cpp:function:: void pyqt5_update_argv_list(PyObject *argv_list, int argc, char **argv)

    Update a Python list from a standard C array of command line arguments and
    an argument count.  This is used in conjunction with
    :cpp:func:`pyqt5_from_argv_list` to handle the updating of argument lists
    after calling constructors of classes such as
    :class:`~PyQt5.QtCore.QCoreApplication`.

    :param argv_list:
        is the Python list of arguments that will be updated.
    :param argc:
        is the number of command line arguments.
    :param argv:
        is the array of pointers to the arguments on the heap.
