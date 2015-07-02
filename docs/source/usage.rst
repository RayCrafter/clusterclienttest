========
Usage
========

Register an application on your master server here ``https://<urltoserver>/admin/oauth2_provider/application/``.
On the hornet create a json file at ``~/.clusterclienttest/config.json``::

  {
    "baseurl": "https://<url to the server>",
    "redirecturi": "<redirecturi>",
    "username": "<username>",
    "password": "<password>",
    "clientid": "<clientid>",
    "clientsecret": "<clientsecret>"
  }

Submit the jobscript::

  $ qsub qsub.sh
