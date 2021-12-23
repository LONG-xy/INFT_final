import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from scipy.stats import mannwhitneyu
from scipy.stats import levene


# read csv file
data1 = pd.read_csv('part2/test_m2_k8_avg_balance.csv',header = None)
data2 = pd.read_csv('part2/test_m3_k8_avg_balance.csv',header = None)
data3 = pd.read_csv('part2/test_m4_0.05_k8_avg_balance.csv',header = None)
data4 = pd.read_csv('part2/test_m4_0.08_k8_avg_balance.csv',header = None)
data5 = pd.read_csv('part2/test_m4_0.1_k8_avg_balance.csv',header = None)
data6 = pd.read_csv('part2/test_m4_0.12_k8_avg_balance.csv',header = None)
data7 = pd.read_csv('part2/test_m4_0.14_k8_avg_balance.csv',header = None)
data8 = pd.read_csv('part2/test_m4_0.16_k8_avg_balance.csv',header = None)
data9 = pd.read_csv('part2/test_m5_k8_avg_balance.csv',header = None)


data_PRSH_1 = data1.iloc[:,7]
data_PRSH_2 = data2.iloc[:,7]
data_PRSH_3 = data3.iloc[:,7]
data_PRSH_4 = data4.iloc[:,7]
data_PRSH_5 = data5.iloc[:,7]
data_PRSH_6 = data6.iloc[:,7]
data_PRSH_7 = data7.iloc[:,7]
data_PRSH_8 = data8.iloc[:,7]
data_PRSH_9 = data9.iloc[:,7]



# plot boxplot to show when k equals 8, different mutation function works
plt.figure(figsize=(8,5))
plt.title('box plot')
labels=['M2','M3','M4_0.05','M4_0.08','M4_0.1','M4_0.12','M4_0.14','M4_0.16','M5']
y_label = [np.mean(data_PRSH_1),np.mean(data_PRSH_2),
np.mean(data_PRSH_3),np.mean(data_PRSH_4),
np.mean(data_PRSH_5),np.mean(data_PRSH_6),
np.mean(data_PRSH_7),np.mean(data_PRSH_8),np.mean(data_PRSH_9)]

a = pd.DataFrame(y_label,labels)
print(a)

plt.boxplot([data_PRSH_1,data_PRSH_2,data_PRSH_3,data_PRSH_4,data_PRSH_5, data_PRSH_6,data_PRSH_7,data_PRSH_8,data_PRSH_9
            ],
            labels = labels, showmeans= True)



plt.show()

# levene(a, b, c)
# stats.normaltest(x)

# print(np.mean(data4))

# print(np.mean(data_PRSH_31),np.mean(data_PRSH_32))
# print(mannwhitneyu(data_PRSH_31, data_PRSH_32, alternative="less"))

# print(np.mean(data_PRSH_21),np.mean(data_PRSH_22))
# print(mannwhitneyu(data_PRSH_21, data_PRSH_22, alternative="less"))



