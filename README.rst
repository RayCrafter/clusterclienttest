=========================================================
Cluster Client Test
=========================================================

.. image::  https://img.shields.io/travis/RayCrafter/clusterclienttest/master.png?style=flat
    :target: https://travis-ci.org/RayCrafter/clusterclienttest
    :alt: Build Status

.. image:: https://img.shields.io/coveralls/RayCrafter/clusterclienttest/master.png?style=flat
    :target: https://coveralls.io/r/RayCrafter/clusterclienttest
    :alt: Coverage

.. image:: https://readthedocs.org/projects/clusterclienttest/badge/?version=latest&style=flat
    :target: http://clusterclienttest.readthedocs.org/en/latest/
    :alt: Documentation


Client for compute nodes to communicate via REST API with master server.
This is for test purposes. The master server should be setup with `ansible django stack <https://github.com/RayCrafter/ansible-django-stack>`_.
The django project to test against is `djangotest <https://github.com/RayCrafter/djangotest>`_.

Features
--------

* Authentication via OAuth2.
* Sends a request to the REST API

