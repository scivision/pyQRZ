.. image:: https://travis-ci.org/zebpalmer/pyQRZ.svg?branch=master
    :target: https://travis-ci.org/zebpalmer/pyQRZ

=====
pyQRZ
=====

:Python: 2.7, 3.4, 3.5, 3.6

A python module to query QRZ.com's ham radio license database.
**QRZ XML paid subscription is required**.




Breaking Changes
----------------
When using pyQRZ in a project, please pin pyQRZ to a version that is working with your code.
There may be breaking changes in a soon to be released version.


Install
-------------

::

    python -m pip install pyQRZ

Or for developers::

    python -m pip install -e .


Also, create a settings file (see below) and provide the file path when using QRZ.
Alternately, set environment variables ``QRZ_USER`` and ``QRZ_PASSWORD`` with appropriate contents.

.. code:: toml

    # pyQRZ settings
    [qrz]
    username=blah
    password=blahblah



Example
-------

.. code:: python

    qrz = QRZ(cfg='./settings.cfg')
    result = qrz.callsign("w1aw")
    print(result['fname'], result['name'])
    print(result['addr2'], result['state'])
    print(result['country'])


Notes
-----
I am thinking about providing a free (and opensourced) callsign lookup service, probably start off as USA only.
If this is of interest to you, feel free to contact me.
Knowing it would be useful would make it a higher priority.




