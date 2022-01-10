# PRÀCTICA KAGGLE APC UAB 2021-22 
# Predicting profitable customer segments
#### Author: Alex Casamitjana Serra
#### DATASET (Kaggle): [Predicting profitable customer segments](https://www.kaggle.com/tsiaras/predicting-profitable-customer-segments)

## **Brief summary of the data**
Description of the dataset as in Kaggle:

Each row is a comparison between two groups of potential customers:
1) Column names starting with "g1" represent characteristics of the first customer group (these were known before the campaign was run) 2) Column names starting with "g2" represent characteristics of the second customer group (these were known before the campaign was run)
3) Column names starting with "c_" are features representing some comparison of the two groups (also known before the campaign was run)

The last column, named "target", is categorical, with 3 categories:
0 - none of the two groups were profitable
1 - group1 turned out to be more profitable
2 - group2 turned out to be more profitable

## **Objective**
As implied above the objective of the dataset is predicting the variable "target", that determinates witch one of the two groups stated above would be the most profitable, if any. 



## **Analysis** 
Once the dataset is imported, I do some basic checks by going over the data and using .describe() to get some basic information about the state of the dataset.

Given that this is a ficticious dataset, there is a benefit in the lack of _Nan_ and _None_ values that could have apeared if it was produced with real data. 

Starting the preprocessing by plotting the distribution between the difrent categories that target can fall in. It is clear that group 1 is more likely to be more profitable off the bat.

Next, by doing a correlation histogram we can get a mild idea of what are the atributes most correlationated with "target". And by running some code below we can see them more easily.

## **Preprocessing**
For preprocesing, given that there is 69 atributes, two methods to diminish the load of variables are employed. One of them is selecting the variables with highest correlation to the "target" atribute, and the other is an standard PCA aiming towards aproximately 95% of explained variance. Normalization of the data is also applied but will only be used on SVCLinear model, given that is the only where it gives an improvement of results.

## **Models Used**

Non-PCA models:
| **Model**        | **Hyperparametres**  | **Accuracy**  |
| Logistic Regression | C= | :-----: | :-----: |
| SVCLinear | C= | :-----:|
| Random Forest Classifier | n_estimators =  | :-----: |
| Histogram Gradient Boosting | :-------------: | :-----: |
| Bagging Classifier (LogReg) | C= | :-----: |
| Ada Boost Classifier | n_estimators =  | :-----: |

PCA models:
| **Model**        | **Hyperparametres**  | **Accuracy**  |
| Logistic Regression | C= | :-----: |
| SVCLinear | C= | :-----:|
| Random Forest Classifier | n_estimators =  | :-----: |
| Histogram Gradient Boosting | :-------------: | :-----: |
| Bagging Classifier (LogReg) | C= | :-----: |
| Ada Boost Classifier | n_estimators =  | :-----: |

## **Demo**


## **Conclusions**

## **Concepts to be worked on in the future**
·Implementing hyperparameter search for all models.
·Tryind diferent models, maybe also deep learning.
·
