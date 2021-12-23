import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats


mean = []
df = []
K = range(2,20,2)

for k in K:
    data = pd.read_csv('best/best_m4_0.14_k'+str(k)+'_avg_balance.csv',header = None)
    data_PRSH = data.iloc[:,7]
    df.append(data_PRSH)
    mean.append(stats.trim_mean(data_PRSH,0.05))

print(mean)

plt.boxplot(df)
plt.show()

plt.xticks(K)
plt.plot(K,mean)
plt.scatter(K,mean)
plt.title("Best Mutation Function 5")
plt.xlabel("X")
plt.ylabel('Profit per trader')
plt.show()




