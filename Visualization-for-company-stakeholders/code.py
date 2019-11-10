# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data= pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
print(loan_status)

y_pos = np.arange(len(loan_status))


plt.bar(y_pos, loan_status, align='center', alpha=0.5)




# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status'])

property_and_loan = property_and_loan.size().unstack()

y_pos = np.arange(len(property_and_loan))

#plt.bar(y_pos,property_and_loan)
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()





# --------------

#Task 1 - Loan Status
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


education_and_loan = data.groupby(['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()

y_pos = np.arange(len(education_and_loan))

#plt.bar(y_pos,property_and_loan)
education_and_loan.plot(kind='bar', stacked=False)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()







# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot.kde()
#Series.plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot.kde()










#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows= 3,ncols= 1,figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set(title="Applicant Income")

ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set(title="Coapplicant Income")

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set(title='Total Income')




