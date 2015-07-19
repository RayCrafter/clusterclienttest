========
Usage
========

Register an application on your master server here ``https://<urltoserver>/admin/oauth2_provider/application/``.
On the hornet create a json file at ``~/.clusterclienttest/config.json``::

  {
    "host": "<url to the server>",
    "logport": <port for graylog input>
    "redirecturi": "<redirecturi>",
    "username": "<username>",
    "password": "<password>",
    "clientid": "<clientid>",
    "clientsecret": "<clientsecret>"
  }

Have a look at the jobscript ``qsubscript``. It is an example for how one would write
the job script. It asserts that you have a virtualenv ``clusterclienttest`` in ``~/.virtualenv/``:

.. literalinclude:: /../../qsubscript
   :linenos:
   :lineno-match:
