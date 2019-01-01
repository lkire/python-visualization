#!/bin/bash

#suggest jsut running through these commands instead of running script

#conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

sudo apt update
sudo apt install libgl1-mesa-glx

conda install msgpack-python sqlAlchemy tensorflow=1.11.0 keras scikit-learn numpy scipy jupyter
conda install -c pyviz/label/dev pyviz
pyviz fetch-data --path .

rm Miniconda3-latest-Linux-x86_64.sh
