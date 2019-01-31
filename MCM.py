# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:03:51 2019

@author: pengu
"""
import test
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy import stats
import random

d_list = []

class Dragon():
    def __init__(self,name,size,age):
        self.name = name
        self.size = size
        self.age = age
        self.history = []
        self.calories_fed = 0
        self.calories_history = []
        self.temp=[]
        d_list.append(self)
        
    def grow(self,growth):
        self.size = self.size + growth
        self.age += 1
        
class State():
    def __init__(self,day):
        self.day = 0
        self.season = 1
        self.timer = 1
        self.last_sum_length = 0
        self.tot_cal = 50000

def step():
    update()

def update():
    #day increase
    state.timer -= 1
    if state.timer <= 0:
        state.season = (state.season+1)%4
        if state.season == 2:
            length = int(chi2.rvs(16)*91.25)
            state.timer = length
            state.last_sum_length = length
        if state.season == 0:
            length = random.normalvariate(state.last_sum_length,0.1*state.last_sum_length)
            if length == 0:
                length == 1
            state.timer = length
        else:
            length = random.normalvariate(0.25*state.last_sum_length,0.055*state.last_sum_length)
            if length == 0:
                length ==1
            state.timer = length
    state.day += 1
            
    #dragons grow
    for dragon in d_list:
        dragon.history.append(dragon.size)
        dist = random.normalvariate(400,40)
        fight = (random.random() < 0.05)
        req_energy = test.E_out(dragon.size, 0.708, dist, fight)
        given_energy = test.E_in(dragon.size, req_energy, 1, True)
        if state.season == 3:
            temp = 1
        else:
            temp = state.season
        multiplier = (0.7+0.3*temp)
        given_energy = random.normalvariate(multiplier*given_energy,0.05*multiplier*given_energy)
        day_calories_fed = 0
        
        if state.season == 0:
            given_energy += dragon.size*1.27
            day_calories_fed += dragon.size*1.27
        if fight:
            given_energy += dragon.size
            day_calories_fed += dragon.size
        
        dragon.calories_history.append(day_calories_fed)
        dragon.grow((given_energy - req_energy)/4250)

results = []
for j in range(100):
    print(j)
    state = State(0)
    d_list=[]
    Dragon("Drogon", 10,0)
    for i in range(73000):
        step()
    if (d_list[0].size <150000):
        results.append(d_list[0].size)
print(results)
print(stats.describe(results))
    
for dragon in d_list:
    #plt.xkcd()
    plt.xlabel("time in days")
    plt.ylabel("size of dragon in kg")
    plt.plot(dragon.history)
    plt.show()
    plt.xlabel("time in days")
    plt.ylabel("percent of body weight of additional ration")
    plt.plot(dragon.calories_history)
    plt.show()
    plt.xlabel("time in days")
    plt.ylabel("weight of meat required in kg")
    plt.plot(dragon.temp)
    plt.show()
    total = 0
    for i in range(len(dragon.calories_history)):
        total += dragon.calories_history[i]
    print("Total amount of calories fed: " + str(int(total)))