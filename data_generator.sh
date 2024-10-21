#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=10GB
#SBATCH --time=30:00:00
#SBATCH --output=dataGen.out

module load miniconda-nobashrc
eval "$(conda shell.bash hook)"
conda activate pyCLGL

python lhs_sampling.py
python call_class.py