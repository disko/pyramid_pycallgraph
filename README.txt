===================
pyramid_pycallgraph
===================

This package provides a Pyramid tween to generate a callgraph image for every request.

It uses the `Python Call Graph`_ package for tracing and graph generation.
See its documentation for example images.

.. _Python Call Graph: http://pycallgraph.slowchop.com/

Usage
=====

Add ``pyramid_pycallgraph`` to the ``pyramid.includes`` in your application's ``.ini`` file::

    pyramid.includes =
        pyramid_pycallgraph

Configuration
=============

The default options of the `pycallgraph.config.Config`_ object can be overridden in your application's ``.ini`` file.

Example::

    pycallgraph.include_stdlib = True
    pycallgraph.max_depth = 10000

    pycallgraph.trace_filter.exclude =
    pycallgraph.trace_filter.include =
        sqlalchemy.*
        pyramid.*
        myapp.*

.. _pycallgraph.config.Config: https://github.com/gak/pycallgraph/blob/master/pycallgraph/config.py#L8

Development
===========

Status
------

Currently ``pyramid_pycallgraph`` is in alpha / development state and should be considered no more than a proof of concept.
There are no tests at all and it might or might not work for you.

Contributions
-------------

Contributions are highly welcome.
Just clone the `Github repository`_ and start hacking.
If you think your work might be generally useful, feel free to open a pull request.

.. _Github repository: https://github.com/disko/pyramid_pycallgraph
