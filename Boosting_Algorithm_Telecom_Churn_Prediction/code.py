# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here
df = pd.read_csv(path)

X= df.drop(['customerID','Churn'],axis=1)

y = df.Churn
#Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3 , random_state = 0)


# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
X_train['TotalCharges'] = X_train['TotalCharges'].replace(' ', np.NaN)
X_test['TotalCharges'] = X_test['TotalCharges'].replace(' ', np.NaN)

X_train['TotalCharges'] = X_train['TotalCharges'].astype(float)
X_test['TotalCharges'] = X_test['TotalCharges'].astype(float)

X_train['TotalCharges'] = X_train['TotalCharges'].fillna((X_train['TotalCharges'].mean()))
X_test['TotalCharges'] =  X_test['TotalCharges'].fillna((X_test['TotalCharges'].mean()))

#print(X_train.isnull().sum())

#print(X_train.dtypes)

# Categorical boolean mask
categorical_feature_mask = X_train.dtypes==object

# filter categorical columns using mask and turn it into a list
categorical_cols = X_train.columns[categorical_feature_mask].tolist()


le = LabelEncoder()

# apply le on categorical feature columns
X_train[categorical_cols] = X_train[categorical_cols].apply(lambda col: le.fit_transform(col))
#X_train[categorical_cols].head(10)

X_test[categorical_cols] = X_test[categorical_cols].apply(lambda col: le.fit_transform(col))
#X_test[categorical_cols].head(10)

#replace yes and no
y_train = y_train.replace('No', 0)
y_train = y_train.replace('Yes', 1)

y_test = y_test.replace('No', 0)
y_test = y_test.replace('Yes', 1)




# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(X_train.head(5), X_test.head(5), y_train.head(5), y_test.head(5) )

ada_model = AdaBoostClassifier(random_state=0)
ada_model.fit(X_train,y_train)

y_pred = ada_model.predict(X_test)

ada_score = accuracy_score(y_test,y_pred)
print(ada_score)



# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model = XGBClassifier(random_state=0)

#fit
xgb_model.fit(X_train,y_train)

#predict
y_pred = xgb_model.predict(X_test)

# accuracy_score
xgb_score = accuracy_score(y_test,y_pred)
print(xgb_score)

print(" XGBOOST confusion matrix")
# confusion_matrix
xgb_cm = confusion_matrix(y_test,y_pred)
print(xgb_cm)

print("xgboost classification_report")
 #classification_report
xgb_cr = classification_report(y_test,y_pred)
print(xgb_cr)

clf_model = GridSearchCV(estimator=xgb_model,param_grid=parameters)
clf_model.fit(X_train,y_train)

y_pred = clf_model.predict(X_test)
clf_score = accuracy_score(y_test,y_pred)



clf_cm = confusion_matrix(y_test,y_pred)
print(clf_cm)


 #classification_report
clf_cr = classification_report(y_test,y_pred)
print(clf_cr)




