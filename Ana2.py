
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from scipy.stats import mannwhitneyu


# read csv file
data1 = pd.read_csv('part2_m2_1_avg_balance.csv',header = None)
data2 = pd.read_csv('best_o_m4_avg_balance.csv',header = None)
data3 = pd.read_csv('test_avg_balance.csv',header = None)


data4 = pd.read_csv('m5_C_144_avg_balance.csv',header = None)


data_PRSH_1 = data1.iloc[:,7]

data_PRSH_21 = data2.iloc[:,7]
data_PRSH_22 = data2.iloc[:,11]

data_PRSH_31 = data3.iloc[:,7]
data_PRSH_32 = data3.iloc[:,11]
data4 = data4.iloc[:,7]

print(np.mean(data4))

print(np.mean(data_PRSH_31),np.mean(data_PRSH_32))
print(mannwhitneyu(data_PRSH_31, data_PRSH_32, alternative="less"))

print(np.mean(data_PRSH_21),np.mean(data_PRSH_22))
print(mannwhitneyu(data_PRSH_21, data_PRSH_22, alternative="less"))

# plt.figure(figsize=(10,5))
# plt.title('box plot')
# labels=['1','2','3','4','5','6','7']
# plt.boxplot([data_PRSH_1,data_PRSH_2,data_PRSH_4,data_PRSH_3,data_PRSH_6, data_PRSH_7,data_PRSH_9
#             ],
#             labels = labels, showmeans= True)
# plt.show()

