# Initial Setup
# Import all the libraries we need
#import matplotlib.pyplot as plt
#import numpy as np
#import csv
#import math
#import seaborn as sns
#import random
#import scipy.stats as st
from BSE import market_session
from BSE import HC_set
from multiprocessing import Process

# do n runs experiment   
def n_runs(n, trial_id, start_time, end_time, traders_spec, order_sched):
    trialId = trial_id
    open(trialId + '_avg_balance.csv','a')
    for i in range(n):
        trialId = trial_id 
        tdump = open(trialId + '_avg_balance.csv','a')
        market_session(trialId, start_time, end_time, traders_spec, order_sched, tdump, False, False) 
        tdump.close()
    

sellers_spec = [('PRSH', 5),('PRSH_I', 5)]
buyers_spec = sellers_spec
traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

sup_range = (100, 200)
dem_range = sup_range

start_time = 0
end_time = 5000
supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [sup_range], 'stepmode': 'fixed'}]
demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [dem_range], 'stepmode': 'fixed'}]

order_interval = 20
order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'periodic'}

trial_id = 'Improve'
n_runs(300, trial_id, start_time, end_time, traders_spec, order_sched)
    





                   
