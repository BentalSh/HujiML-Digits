"""Maybe bootstrap GUI or something, we will see later on"""
from DataHandler import *
from Model import *

dataHandler=DataHandler()
model = Model(dataHandler)
model.train()
print model.confMatrix()




