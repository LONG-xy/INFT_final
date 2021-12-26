import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from scipy.stats import mannwhitneyu
from scipy.stats import levene

# read csv files

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



# plot Boxplot to show when k equals 8, different mutation function works
plt.figure(figsize=(8,5))
plt.title('Boxplot')
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


# compare the original PRSH trader with modified PRSH trader (using mutation funciton 4)
# read csv files
data = pd.read_csv('best/best_compare_origin_m4_0.14_k8_avg_balance.csv',header = None)


# describe the statistics of sample
data_PRSH_O = data.iloc[:,7]
data_PRSH_M = data.iloc[:,11]
list_to_tuple=list((zip(data_PRSH_O,data_PRSH_M)))
sample_df=pd.DataFrame(list_to_tuple,columns=['PRSH_O','PRSH_M'])
sample_df.describe()

PRSH_O_mean=np.mean(data_PRSH_O)
PRSH_M_mean=np.mean(data_PRSH_M)
print(PRSH_O_mean,PRSH_M_mean)

print('Average profit increase rate',(PRSH_M_mean-PRSH_O_mean)/PRSH_O_mean)
#0.13844425781668745

# check normality and homoscedasticity
print('PRSH_O: normal test',stats.normaltest(data_PRSH_O))
print('PRSH_M: normal test',stats.normaltest(data_PRSH_M))
print('levene test',levene(data_PRSH_O,data_PRSH_M))

# calculate confidence interval
CI_O = stats.t.interval(0.95, len(data_PRSH_O)-1, loc=np.mean(data_PRSH_O), scale=stats.sem(data_PRSH_O))
print(CI_O)
CI_M = stats.t.interval(0.95, len(data_PRSH_M)-1, loc=np.mean(data_PRSH_M), scale=stats.sem(data_PRSH_M))
print(CI_M)

# plot confidence interval around mean
def plot_CI(CI1,CI2,label1,label2,mean1,mean2):
    plt.figure(figsize=(5,5))
    plt.title('confidence interval around mean')
    plt.xlim(1, 3)

    plt.vlines(x=1.5,ymin = CI1[0], ymax = CI1[1],label=label1,colors = 'blue')
    plt.vlines(x=2,ymin = CI2[0], ymax = CI2[1],label=label2,colors = 'red')

    plt.plot(1.5, CI1[0], marker = '_', markerfacecolor='blue')
    plt.plot(1.5, CI1[1], marker = '_', markerfacecolor='blue')
    plt.plot(1.5,mean1, marker = 'o', markerfacecolor='blue')

    plt.plot(2, mean2, marker = 'o', markerfacecolor='red')
    plt.plot(2, CI2[0], marker = '_', markerfacecolor='red')
    plt.plot(2, CI2[1], marker = '_', markerfacecolor='red')

    plt.xticks([])
    plt.legend()
    # plt.text(1.4,1820,label1)
    # plt.text(1.8,1820,label2)
    plt.text(1.4,2005,label1)
    plt.text(2,2005,label2)
    plt.show()
    
plot_CI(CI_O,CI_M,'PRSH_O','PRSH_M',PRSH_O_mean,PRSH_M_mean)


# hypothesis test
print('t test',stats.ttest_ind(data_PRSH_O, data_PRSH_M, alternative="less"))


## Extending PRSH
# compare the modified PRSH trader(using mutation function 4) with improved PRSH trader with multi-armed bandit algorithm 
data = pd.read_csv('Improve_2_avg_balance.csv',header = None)
data1 = pd.read_csv('Improve_avg_balance.csv',header = None)

# describe the statistics of sample
data_PRSH_I = data1.iloc[:,11]
data_PRSH_O = data1.iloc[:,7]
list_to_tuple=list((zip(data_PRSH_O,data_PRSH_I)))
sample_df=pd.DataFrame(list_to_tuple,columns=['PRSH_O','PRSH_I'])
sample_df.describe()

PRSH_I_mean=np.mean(data_PRSH_I)
PRSH_O_mean=np.mean(data_PRSH_O)
print(PRSH_O_mean,PRSH_I_mean)
print('OM_Average profit increase rate',(PRSH_I_mean-PRSH_O_mean)/PRSH_O_mean)
#OM_Average profit increase rate 0.19128915309088154


# describe the statistics of sample
data_PRSH_I = data.iloc[:,7]
data_PRSH_M = data.iloc[:,11]
list_to_tuple=list((zip(data_PRSH_M,data_PRSH_I)))
sample_df=pd.DataFrame(list_to_tuple,columns=['PRSH_M','PRSH_I'])
sample_df.describe()

PRSH_I_mean=np.mean(data_PRSH_I)
PRSH_M_mean=np.mean(data_PRSH_M)
print(PRSH_M_mean,PRSH_I_mean)
print('IM_Average profit increase rate',(PRSH_I_mean-PRSH_M_mean)/PRSH_M_mean)
#IM_Average profit increase rate 0.06922415065677395

# calculte confidence interval
CI_M = stats.t.interval(0.95, len(data_PRSH_M)-1, loc=np.mean(data_PRSH_M), scale=stats.sem(data_PRSH_M))
print(CI_O)
CI_I = stats.t.interval(0.95, len(data_PRSH_I)-1, loc=np.mean(data_PRSH_I), scale=stats.sem(data_PRSH_I))
print(CI_M)

# plot confidence interval around mean
plot_CI(CI_M,CI_I,'PRSH_M','PRSH_I',PRSH_M_mean,PRSH_I_mean)

# check normality and homoscedasticity
print('PRSH_O: normal test',stats.normaltest(data_PRSH_O))
print('PRSH_M: normal test',stats.normaltest(data_PRSH_M))
print('levene test',levene(data_PRSH_O,data_PRSH_M))


