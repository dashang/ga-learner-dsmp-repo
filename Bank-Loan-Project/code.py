# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path) 


categorical_var = bank.select_dtypes(include='object')

print(categorical_var)

numerical_var = bank.select_dtypes(include='number')

print(numerical_var)
# code ends here



# --------------
# code starts here

banks = bank.drop(['Loan_ID'],axis=1)

print(banks.isnull().sum())

bank_mode = banks.mode()

banks = banks.fillna(bank_mode)

banks['Gender'] =  banks['Gender'].fillna(banks['Gender'].mode()[0])
banks['Married'] =  banks['Married'].fillna(banks['Married'].mode()[0])
banks['Dependents'] =  banks['Dependents'].fillna(banks['Dependents'].mode()[0])
banks['Education'] =  banks['Education'].fillna(banks['Education'].mode()[0])
banks['Self_Employed'] =  banks['Self_Employed'].fillna(banks['Self_Employed'].mode()[0])
banks['ApplicantIncome'] =  banks['ApplicantIncome'].fillna(banks['ApplicantIncome'].mode()[0])
banks['CoapplicantIncome'] =  banks['CoapplicantIncome'].fillna(banks['CoapplicantIncome'].mode()[0])

banks['LoanAmount'] =  banks['LoanAmount'].fillna(banks['LoanAmount'].mode()[0])
banks['Loan_Amount_Term'] =  banks['Loan_Amount_Term'].fillna(banks['Loan_Amount_Term'].mode()[0])
banks['Credit_History'] =  banks['Credit_History'].fillna(banks['Credit_History'].mode()[0])
banks['Property_Area'] =  banks['Property_Area'].fillna(banks['Property_Area'].mode()[0])
banks['Loan_Status'] =  banks['Loan_Status'].fillna(banks['Loan_Status'].mode()[0])



#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks, values ='LoanAmount', index =['Gender', 'Married','Self_Employed'], aggfunc = np.mean) 



# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]

loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]

Loan_Status = 614


percentage_se = (len(loan_approved_se) / 614) *100
percentage_nse = (len(loan_approved_nse) / 614) *100

# code ends here


# --------------
# code starts here




loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 if isinstance(x, float) else None)
loan_term_without_na = loan_term.dropna() >= 25

big_loan_term = loan_term_without_na.value_counts()[True]
print(big_loan_term)



# code ends here


# --------------
# code starts here


loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


