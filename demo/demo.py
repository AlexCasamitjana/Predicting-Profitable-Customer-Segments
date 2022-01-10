# -*- coding: utf-8 -*-
"""
@author: Alex casamitjana
"""

from libraries import *


warnings.filterwarnings("ignore")

pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option('precision', 12);


def load_dataset(name):
    dataset = pd.read_csv(name, header=0, delimiter=',')
    return dataset


dataset = load_dataset('customerTargeting.csv')
data = dataset.values
labels = dataset.columns.values

X = data[:, [i for i in range(69)]]
y = data[:, 70]


#fem servir els atributs que hem vist abans amb major correlació amb target
orX = data[:,[0,32,43,49,51,52,53,58,59,60,61,62,66,67]]

ox_t, ox_v, oy_t, oy_v = train_test_split(orX, y, train_size=0.7)

scaler = preprocessing.StandardScaler().fit(ox_t)
X_scaled = scaler.transform(ox_t)

svcLin = svm.LinearSVC(C=10, max_iter=10000)
svcLin.fit(X_scaled,oy_t)
#pickle.dump(svcLin, open("LinearSVC.sav", "wb"))
print ("\n\nCorrect classification SVM Linear ", 0.7*100, "% of the data: ", svcLin.score(ox_v, oy_v))
print(metrics.classification_report(oy_v, svcLin.predict(ox_v)))