#!/bin/bash
#PBS -l nodes=5:ppn=2
#PBS -l walltime=0:10:00
#PBS -q pace-ice
#PBS -N dft_test_1
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR

source /storage/home/hpaceice1/smishra327/data/env.sh
python midterm.py
