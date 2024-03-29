# -*- coding: utf-8 -*-
"""LogisticReggression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sbMILbJ7ekiQJsBCn_kcjPbaaMEoAu5F
"""

import pandas as pd
dataset=pd.read_csv("dataset.csv")
dataset.head()

print(dataset.shape)  #Sending info of the table

dataset['target'].value_counts()  # this will count the freq. of distinct values in the "target" column

import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='target',data=dataset,palette='hls')
plt.show()

#splitting the datasets into features(X) and targets(Y) label sets
X=pd.DataFrame(dataset.iloc[:,:-1])
y=pd.DataFrame(dataset.iloc[:,-1])
X.head()

y.head()

#Split the data into test and training sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=1)

#import module for fitting
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)

#Predicting the test set results
y_pred=logmodel.predict(X_test)

#Calculating the accuracy
print("Accuracy %d",logmodel.score(X_test,y_test))

#Evaluate model using confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
print(confusion_matrix)

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_aoc=roc_auc_score(y_test,logmodel.predict(X_test))
fpr,tpr,threshold=roc_curve(y_test,logmodel.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr,tpr,label='Logistic Regression (area=%0.2f)' % logit_roc_aoc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.5])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiever operating Charecteristic')
plt.legend(loc='lower right')
plt.savefig('log_ROC')
plt.show()