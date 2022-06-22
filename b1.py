# -*- coding: utf-8 -*-
"""b1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12UINVtdj87gMnsPntGSuU_8PQAKIhZzn
"""

import functools as ft
import matplotlib.pyplot as plt
from random import randint, random,seed
from operator import add

def individual(length):
   return [ randint(0,1) for x in range(length) ]

def population(count, length):
 return [ individual(length) for x in range(count) ] # returns "count" individuals

def fitness(individual, target):
  decimal_individual=0
  for i in range(len(individual)):
    decimal_individual+=individual[i]*(2**i)
  return abs(target-decimal_individual)

def grade(pop, target):
  summed=0
  for x in pop:
    summed += fitness(x, target)
  return summed/len(pop)

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length =  int(len(graded)*retain)
    parents = graded[:retain_length]
    for individual in graded[retain_length:]:
      if random_select > random():
        parents.append(individual)
    for individual in parents:
      if mutate > random():
        pos_to_mutate = randint(0, len(individual)-1)
        individual[pos_to_mutate] = randint(min(individual),max(individual))
    parents_length = len(parents)
    desired_length = len(pop)- parents_length
    children = []
    while len(children) < desired_length :
      male = randint(0, parents_length-1)
      female = randint(0, parents_length-1)
      if male != female :
        male=parents[male]
        female=parents[female]
        half = (len(male)/2)
        child = male[:int(half)] + female[int(half):]
        children.append(child)
    parents.extend(children)
    return(parents)

target = 786
p_count = 1000 #population size
i_len = 12
generations = 3000
p = population(p_count, i_len)
fitness_history = [grade( p, target) , ]
for i in range(generations) :
  p = evolve( p , target )
  fitness_history.append(grade( p , target ) )
  if fitness_history[i+1]==0:
    break

for datum in fitness_history:
    print(datum)

plt.plot(fitness_history)
plt.xlabel("generations")
plt.ylabel("average fitness")
plt.grid()
plt.show()

seed(42)
 retain=0.2 
 random_select=0.05
 mutate=[0,0.005,0.008,0.01,0.013,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06]
 target = 661
 p_count = 1000 #population size
 i_len = 12
 generations = 5000
 p = population(p_count, i_len)
 mutation_generation=[0]
 for m in mutate :
   fitness_history = [grade( p, target) , ]
   for i in range(generations):
     p = evolve( p , target,retain,random_select,m)
     fitness_history.append(grade( p , target ) )
     if fitness_history[i+1]==0:
       break
   mutation_generation.append(len(fitness_history))
 plt.scatter(mutate,mutation_generation[1:])
 plt.xlabel("mutation rate")
 plt.ylabel("number of generations")
 plt.grid()
 plt.show()

seed(13)
retain=0.2 
random_select=[0,0.005,0.01,0.015,0.02,0.023,0.025,0.03,0.035,0.045,0.05,0.06]
mutate=0.01
target = 661
p_count = 1000 #population size
i_len = 12
generations = 300
p = population(p_count, i_len)
random_select_generation=[0]
fitness_history = [grade( p, target) , ]
for r in random_select :
  fitness_history = [grade( p, target) , ]
  for i in range(generations):
    p = evolve( p , target,retain,r,mutate)
    fitness_history.append(grade( p , target ) )
    if fitness_history[i+1]==0:
      break
  random_select_generation.append(len(fitness_history))
plt.scatter(random_select,random_select_generation[1:])
plt.xlabel("random_selection rate")
plt.ylabel("number of generations")
plt.grid()
plt.show()

retain=[0.09,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.6,0.7]
random_select=0.01
mutate=0.01
target = 661
p_count = 1000 #population size
i_len = 12
generations = 3000
p = population(p_count, i_len)
retain_generation=[0]
for r in retain :
  fitness_history = [grade( p, target) , ]
  for i in range(generations):
    p = evolve( p , target,r,random_select,mutate)
    fitness_history.append(grade( p , target ) )
    if fitness_history[i+1]==0:
      break
  retain_generation.append(len(fitness_history))
plt.scatter(retain,retain_generation[1:])
plt.xlabel("retain rate")
plt.ylabel("number of generations")
plt.grid()
plt.show()