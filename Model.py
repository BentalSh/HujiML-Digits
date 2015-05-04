"""Rewrite this file with different models"""
from sklearn import svm, metrics
from sklearn.metrics import confusion_matrix
class Model:
    def __init__(self,dataHandler):
        print "initing model..."
        self.data = dataHandler
        self.model = svm.LinearSVC()
    def train(self):
        print "train started"
        self.model.fit(self.data.trainFeatures, self.data.trainLabels)
        print "train done"

    def confMatrix(self):
        print "predict started"
        y_pred = self.model.predict(self.data.trainFeatures)
        print "predict done"
        return metrics.confusion_matrix(self.data.trainLabels,y_pred)


