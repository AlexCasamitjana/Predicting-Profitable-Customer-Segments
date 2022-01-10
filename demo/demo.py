# -*- coding: utf-8 -*-
"""
@author: Alex casamitjana
"""

from libraries import *

pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option('precision', 12);


def load_dataset(name):
    dataset = pd.read_csv(name, header=0, delimiter=',')
    return dataset


dataset = load_dataset('customerTargeting.csv')
data = dataset.values
labels = dataset.columns.values

pcaX = X

pca = PCA()
pca.fit(pcaX)
pca_data = pca.transform(pcaX)
per_var = pca.explained_variance_ratio_*100 
cumulative_sum = np.cumsum(per_var)

labels = ['PC'+str(i) for i in range(1, 8)]
pca_variables = pd.DataFrame(pca_data[:,:7], columns=labels)

x_t, x_v, y_t, y_v = train_test_split(pca_variables, y, train_size=0.7)

logireg = LogisticRegression(C=2.0, fit_intercept=True, penalty='l2', tol=0.001)
logireg.fit(x_t, y_t)

clf = RandomForestClassifier(n_estimators=5,max_depth=10, random_state=0)
clf.fit(x_t, y_t)