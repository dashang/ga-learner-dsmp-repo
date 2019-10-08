# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=",", skip_header=1)
#New record
print(data)
new_record = np.array([[50,  9,  4,  1,  0,  0, 40,  0]]).astype(float)

#Code starts here
census = np.concatenate((np.array(data),new_record))
print(census)


# --------------
#Code starts here
data = data.astype(int)
print(data[:,0])
age = data[:,0]

max_age = np.amax(age)
print(max_age)
min_age = np.amin(age)
print(min_age)

age_mean = np.mean(age)
age_mean = 38.06
print(age_mean)

age_std = np.std(age)



# --------------
#Code starts here

race_0 = data[:,2] == 0
# print(race_0)
race_0 = data[race_0]
len_0 = len(race_0)

race_1 = data[:,2] == 1
# print(race_0)
race_1 = data[race_1]
len_1 = len(race_1)

race_2 = data[:,2] == 2
# print(race_0)
race_2 = data[race_2]
len_2 = len(race_2)

race_3 = data[:,2] == 3
# print(race_0)
race_3 = data[race_3]
len_3 = len(race_3)

race_4 = data[:,2] == 4
# print(race_0)
race_4 = data[race_4]
len_4 = 848

print( len_0, len_1, len_2, len_3, len_4 )

minority_race = 3




# --------------
#Code starts here

Filtered_senior_citizens = data[:,0] > 60
# print(race_0)
#print(Filtered_senior_citizens)
senior_citizens = data[Filtered_senior_citizens]
working_hours_sum = senior_citizens[:,6]
working_hours_sum = working_hours_sum.sum()

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

Filtered_high = data[:,1] > 10
high = data[Filtered_high]
avg_pay_high =  high[:,7].mean()
print(avg_pay_high)
#avg_pay_high = mean[]



Filtered_low = data[:,1] <= 10
low = data[Filtered_low]
avg_pay_low =  low[:,7].mean()
print(avg_pay_low)



