'''
import random
def mutate_strat(s,pre,i):
    pre_upper_bound = pre
    newstrat = s
    while newstrat == s:
        #range = random.uniform(pre_upper_bound, pre_upper_bound + 0.05*i)
        if i % 2 != 0:            
            range1 = random.uniform(pre_upper_bound, pre_upper_bound + 0.1)
            newstrat = s + range1
            print ("range1: ",pre_upper_bound, pre_upper_bound + 0.1, "newstart: ",newstrat)
        else:
            range2 = random.uniform(pre_upper_bound, pre_upper_bound + 0.1)
            newstrat = s - range2
            print ("range2: ", pre_upper_bound, pre_upper_bound + 0., "newstart: ",newstrat)
        newstrat = max(-1.0, min(1.0, newstrat))
        #print("bound",pre_upper_bound,pre_upper_bound + 0.05*i)
        #print ("range: ",range1, range2, "newstart: ",newstrat)
        if (abs(newstrat) == 1):
                break
    return newstrat

def mutate_strat_2(s, i):
    interval = 0.08
    newstrat = s
    while newstrat == s:
        if i % 2 == 1:
            newstrat = s + random.uniform(int((i+1)/2-1)*interval, int((i+1)/2)*interval)
            print(int((i+1)/2-1)*interval, int((i+1)/2)*interval)
        else:
            newstrat = s - random.uniform(int((i+1)/2-1)*interval, int((i+1)/2)*interval)
            print(int((i+1)/2-1)*interval, int((i+1)/2)*interval)

        newstrat = max(-1.0, min(1.0, newstrat))
        if (abs(newstrat) == 1):
            break
    return newstrat
        
def mutate_strat_3(s,i):
        newstrat = s
        while newstrat == s:
            if i%4 == 1:
                newstrat = s + random.uniform(0, 0.05)
                print(i,newstrat)
            elif i%4 == 2:
                newstrat = s - random.uniform(0, 0.05)
                print(i,newstrat)
            elif i%4 == 3:
                newstrat = s + random.uniform(0.05, 0.15)
                print(i,newstrat)
            elif i%4 == 0:
                newstrat = s - random.uniform(0.05, 0.15)
                print(i,newstrat)
            newstrat = max(-1.0, min(1.0, newstrat))
        return newstrat
    




k = 12
pre = 0

for s in range(0, k):
    # initialise each of the strategies in sequence
            profit = 0.0
            profit_per_second = 0
            lut_bid = None
            lut_ask = None
            if s == 0:
                strategy = random.uniform(0, 1)
                print(strategy)
            else:
                i = s
                #strategy = self.mutate_strat(self.strats[0]['stratval'])     # mutant of strats[0]
                #strategy = mutate_strat(strategy,order)
                strategy = mutate_strat_2(strategy,i)     # mutant of strats[0]
'''
 
    