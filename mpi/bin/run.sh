#!/bin/sh

for N in 1000 1000000 100000000
do
  for ((n=1; n<=8; n++))
  do
    sbatch --output=out.txt --error=error.txt --partition=RT_study --ntasks=$n my_run.sh $N
    echo "N=$N, n=$n"
    sleep 7
  done
done
GREEN='\033[0;32m'
echo -e "${GREEN}DONE"
