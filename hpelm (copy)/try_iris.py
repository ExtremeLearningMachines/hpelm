# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:19:18 2014

@author: akusok
"""

from sklearn import datasets
import numpy as np
from d_elm import DELM as ELM
#from elm import ELM
from mpi4py import MPI



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    iris = datasets.load_iris()
    X = iris.data
    Y = np.zeros((150,3))
    Y[:50,0] = 1
    Y[50:100,1] = 1
    Y[100:,2] = 1
    
    X = (X - np.mean(X,0)) / np.std(X,0)

else:
    X = None
    Y = None

elm = ELM(4,3)
elm.add_neurons(10, np.tanh)
print elm.bias
elm.train(X, Y)
Yh = elm.run(X)

if rank == 0:
    print np.argmax(Yh,1) - iris.target
