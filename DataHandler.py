import os
import numpy as numpy
import pandas as pd
from StringIO import StringIO

class DataHandler:
    def __init__(self):
        print "starting to load data"
        data = pd.read_csv(os.path.realpath('Data/train.csv'), delimiter=",").values
        self.trainLabels=data[:,0]
        self.trainFeatures=data[:,1:]
        data = pd.read_csv(os.path.realpath('Data/test.csv'), delimiter=",").values
        self.test = data[:,:]
        print "finished loading data"

