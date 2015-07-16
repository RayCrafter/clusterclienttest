#!/bin/bash
#PBS -N clusterclienttest
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:02:00
module load tools/python/3.4.3
source $HOME/.virtualenv/clusterclienttest/bin/activate

WORKSPACE=`ws_allocate Pythontest_WS`
cd $WORKSPACE
aprun -n 1 -N 1 python -m clusterclienttest $HOME/.clusterclienttest/config.json
