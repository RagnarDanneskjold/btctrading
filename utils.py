# -*- coding: utf-8 -*-
import math
import pandas as pd
from sklearn.metrics import log_loss, cohen_kappa_score, accuracy_score, confusion_matrix, hinge_loss, classification_report
from pandas_ml import ConfusionMatrix
from datetime import datetime

import settings

# split dataset (train and test) in 2 pieces.
# start piece to train, end piece to test.
def split_df(dframe):
    test = dframe.tail(settings.NTESTS)
    train = dframe[:-settings.NTESTS]
    return train, test

# Split dataset (train and test)
# splitea 1 de cada 4 de forma salpicada
def split_df2(dframe):
    trainfilter = [False if i%4 == 0 else True for i in range(dframe.shape[0])]
    testfilter = [True if i%4 == 0 else False for i in range(dframe.shape[0])]
    return dframe[trainfilter], dframe[testfilter]

# drop rows with "Nans" values
def dropna(df):
    df = df[df < math.exp(709)] # big number
    df = df[df != 0.0]
    df = df.dropna()
    return df

# show metrics
def metrics(y_true, y_pred, y_pred_proba=False):
    target_names = ['KEEP', 'UP', 'DOWN']

    if y_pred_proba is not False:
        print('Cross Entropy: {}'.format(log_loss(y_true, y_pred_proba)))
    print('Accuracy: {}'.format(accuracy_score(y_true, y_pred)))
    print('Coefficient Kappa: {}'.format(cohen_kappa_score(y_true, y_pred)))
    print('Report: {}'.format(classification_report(y_true, y_pred, target_names=target_names)))
    cm = ConfusionMatrix(y_true.tolist(), y_pred.tolist())
    cm.print_stats()

# show metrics
def metrics2(y_true, y_pred):
	print('Accuracy: {}'.format(accuracy_score(y_true, y_pred)))
	print('Coefficient Kappa: {}'.format(cohen_kappa_score(y_true, y_pred)))
	print "Confussion Matrix:"
	print confusion_matrix(y_true, y_pred)

def timestamptodate(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
