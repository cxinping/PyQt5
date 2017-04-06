Support for :class:`~PyQt5.QtCore.QSettings`
============================================

Qt provies the :class:`~PyQt5.QtCore.QSettings` class as a platform independent
API for the persistent storage and retrieval of application settings.  Settings
are retrieved using the :meth:`~PyQt5.QtCore.QSettings.value` method.  However
the type of the value returned may not be what is expected.  Some platforms
only ever store string values which means that the type of the original value
is lost.  Therefore a setting with an integer value of ``42`` may be retrieved
(on some platforms) as a string value of ``'42'``.

As a solution to this problem PyQt5's implementation of
:meth:`~PyQt4.QtCore.QSettings.value` takes an optional third argument called
``type``.  This is either a Python type object, e.g. ``int``, or a string that
is the name of a C++ type, e.g. ``'QStringList'``.  The value returned will be
an object of the requested type.

For example::

    from PyQt5.QtCore import QSettings, QPoint

    settings = QSettings('foo', 'foo')

    settings.setValue('int_value', 42)
    settings.setValue('point_value', QPoint(10, 12))

    # This will write the setting to the platform specific storage.
    del settings

    settings = QSettings('foo', 'foo')

    int_value = settings.value('int_value', type=int)
    print("int_value: %s" % repr(int_value))

    point_value = settings.value('point_value', type=QPoint)
    print("point_value: %s" % repr(point_value))

When this is executed then the following will be displayed for all platforms::

    int_value: 42
    point_value: PyQt5.QtCore.QPoint(10, 20)

If the value of the setting is a container (corresponding to either
``QVariantList``, ``QVariantMap`` or ``QVariantHash``) then the type is applied
to the contents of the container.

For example::

    from PyQt5.QtCore import QSettings

    settings = QSettings('foo', 'foo')

    settings.setValue('list_value', [1, 2, 3])
    settings.setValue('dict_value', {'one': 1, 'two': 2})

    # This will write the setting to the platform specific storage.
    del settings

    settings = QSettings('foo', 'foo')

    list_value = settings.value('list_value', type=int)
    print("list_value: %s" % repr(list_value))

    dict_value = settings.value('dict_value', type=int)
    print("dict_value: %s" % repr(dict_value))

When this is executed then the following will be displayed for all platforms::

    list_value: [1, 2, 3]
    dict_value: {'one': 1, 'two': 2}
