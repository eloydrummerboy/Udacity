# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:05:05 2017

@author: Scott
"""

def classify(features_train, labels_train):   
    ### import the sklearn module for Support Vector Machines
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    from sklearn.svm import SVC
    clf = SVC(kernel='linear')
    return clf.fit(features_train, labels_train)
    
