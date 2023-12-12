#!/bin/bash
#
#SBATCH --partition=RT
#SBATCH --output=out.txt
#SBATCH --error=error.txt

if [ $# -eq 0 ]; 
then
	mpiexec ./main 1000
fi
	mpiexec ./main $1
