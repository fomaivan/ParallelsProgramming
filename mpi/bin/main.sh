#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --partition=RT
#SBATCH --output=out.txt
#SBATCH --error=error.txt

mpiexec ./main 1000
