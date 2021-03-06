import numpy as np
from ML_algorithms.Utility.DecisionTreeFunctions import entropyGain, predictionClassification, varianceReduction, predictionRegression
from ML_algorithms.Supervised_Learning.Base_Classes.DecisionTree import BaseDecisionTree

import unittest


class tests(unittest.TestCase):
    """
    This class contains unit tests for each of the methods
    defined for the kNN class.
    """
    def testSplit(self):
        np.random.seed(21)
        obj1 = BaseDecisionTree(entropyGain, predictionClassification)
        xtr = np.random.randint(8, size = (5,10))
        ytr = np.random.randint(4, size = (1,10))
        feature_row = 4
        split_pt = 4
        print(xtr)
        xtrL, ytrL, xtrR, ytrR = obj1._splitData(xtr, ytr, feature_row, split_pt)
        self.assertEqual((xtrL[4] < 4).all(), True)
        self.assertEqual((xtrR[4] >= 4).all(), True)

    def testFindingFeature_SplitPtPairOneFeature(self):
        np.random.seed(21)
        obj1 = BaseDecisionTree(entropyGain, predictionRegression)
        # Single feature test if we find the best split pt 
        # made it so that split pt 3 is clearly the best 
        xtr = np.array([2,3,3.5,3,1,2,1,5,8,3,2,4,5,3,1,3.2, 2.8, 2.5]).reshape(1,-1)
        ytr = np.array([0,1,1,1,0,0,0,1,1,1,0,1,1,1,0, 1, 0, 0]).reshape(1,-1)
        f_r, f_val, gain = obj1._findBestFeature(xtr, ytr)
        self.assertEqual(f_r, 0)
        self.assertEqual(f_val, 3)
        self.assertAlmostEqual(gain, 0.6869615765)

    def testFindingFeature_SplitPtPairTwoFeatures(self):
        np.random.seed(21)
        obj1 = BaseDecisionTree(entropyGain, predictionRegression)
        # Double feature test 
        # With a string feature and a numeric feature
        # the second featuree split with cloudy and the first feature split with == 3 produce best vals
        # take cloudy tho 
        f1 = np.array([2,3,3.5,3,1,2,1,5,8,3,2,4,5,3,1,3.2, 2.8, 2.5], dtype = object).reshape(1,-1) 
        f2 = np.array(["rainy", "cloudy", "cloudy", "cloudy","rainy", "sunny","sunny", "cloudy","cloudy", "cloudy","rainy", "cloudy","cloudy", "cloudy","rainy", "cloudy","rainy", "rainy"], dtype=object).reshape(1,-1)
        xtr = np.vstack((f1,f2))
        ytr = np.array([0,1,1,1,0,0,0,1,1,1,0,1,1,1,0, 1, 0, 0]).reshape(1,-1)
        f_r, f_val, gain = obj1._findBestFeature(xtr, ytr)
        self.assertEqual(f_r, 1)
        self.assertEqual(f_val, "cloudy")
        self.assertAlmostEqual(gain, 0.6869615765)

    def testFitAndPredict(self):
        np.random.seed(21)
        obj1 = BaseDecisionTree(entropyGain, predictionRegression)
        f1 = np.array([2,3,3.5,3,1,2,1,5,8,3,2,4,5,3,1,3.2, 2.8, 2.5], dtype = object).reshape(1,-1) 
        f2 = np.array(["rainy", "cloudy", "cloudy", "cloudy","rainy", "sunny","sunny", "cloudy","cloudy", "cloudy","rainy", "cloudy","cloudy", "cloudy","rainy", "cloudy","rainy", "rainy"], dtype=object).reshape(1,-1)
        xtr = np.vstack((f1,f2))
        ytr = np.array([0,1,1,1,0,0,0,1,1,1,0,1,1,1,0, 1, 0, 0]).reshape(1,-1) 
        obj1.fit(xtr, ytr)
        obj1.printTree()



if __name__ == "__main__":
    unittest.main()