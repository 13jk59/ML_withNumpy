import numpy as np
from ML_algorithms.Neural_Net_Util.NeuralNetwork_Base import NeuralNetwork_Base
from ML_algorithms.Neural_Net_Util.ActivationFunctions import Sigmoid
from ML_algorithms.Neural_Net_Util.LossFunctions import negative_log_loss, cross_entropy, mean_squared_error
import copy 

class MultiLayerPerceptron(NeuralNetwork_Base):
    """
    This class represents a multi-layer perceptron used for supervised learning. The user will have
    to add the number of layers desired to this layer accordingly. 

    Parameters:
    -> typeSupervised(str): binary, multiclass, or regression
    -> numberInputFeatures (int): Integer representing the number of input features on the data the user will train
    the network on
    -> regularization (str): Either L1, L2, or None depending on if the weight updates for every layer should be regularized
    or not
    -> regParameter (int): Integer representing the strength of the regularization
    """
    def __init__(self, typeSupervised, numberInputFeatures, regularization=None, regParameter= None):
        if typeSupervised == "binary":
            loss_obj = negative_log_loss(regularization=regularization, regParameter=regParameter)
        elif typeSupervised == "multiclass":
            loss_obj = cross_entropy(regularization=regularization, regParameter=regParameter)
        else:
            loss_obj = mean_squared_error(regularization=regularization, regParameter=regParameter)
        super(MultiLayerPerceptron,self).__init__(loss_obj, input_features = numberInputFeatures)



    def predictMLP(self, X, classificationThreshold = None):
        # For binary classification, we need a classification threshold to seperate out the 
        # pos class from the neg class 
        if classificationThreshold:
            predictions = self._forward_propagate(X)
            return (predictions >= classificationThreshold).astype(int)
        else:
            return self.predict(X)
