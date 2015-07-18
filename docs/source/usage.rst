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
the job script. It asserts that you have a virtualenv ``clusterclienttest`` in ``~/.virtualenv/``::

  #!/bin/bash
  #PBS -N clusterclienttest
  #PBS -l nodes=1:ppn=1
  #PBS -l walltime=00:02:00
  module load tools/python/3.4.3
  source $HOME/.virtualenv/clusterclienttest/bin/activate
  
  WORKSPACE=`ws_allocate Pythontest_WS`
  cd $WORKSPACE
  aprun -n 1 -N 1 python -m clusterclienttest $HOME/.clusterclienttest/config.json
