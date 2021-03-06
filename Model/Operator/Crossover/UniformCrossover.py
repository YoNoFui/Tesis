#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

def execute_crossover_technique(chromosome_a,chromosome_b,crossover_options):
    crossover_probability = crossover_options["probability_crossover_general"]
    pmask = crossover_options["pmask_uniform_crossover"]
    chromosome_child_1 = []
    chromosome_child_2 = []
    number = aleatorio.random()
  
    if number <= crossover_probability:
       for x in range(0,len(chromosome_a)):
           number = aleatorio.random()
           if number <= pmask:
              chromosome_child_1 += [chromosome_b[x]]
              chromosome_child_2 += [chromosome_a[x]]
                    
           else:
              chromosome_child_1 += [chromosome_a[x]]
              chromosome_child_2 += [chromosome_b[x]]
                  
    else:
        chromosome_child_1 = chromosome_a
        chromosome_child_2 = chromosome_b

    return [chromosome_son_1,chromosome_son_2]    
