#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_sp_ranking_fitness(population,fitness_options):
    total_fitness = 0
    sp = fitness_options[0] 

    #Falta hacer la evaluación por el frente de pareto.
    population.get_population().sort(key=lambda individual: individual.evaluated_functions[x])
    y = 0
         
    for individual in population.get_individuals():
        current_fitness = 2.0 - sp + 2.0 * (sp - 1.0) * (y/(population.get_size() - 1.0))
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness        
        y += 1
  
    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
    
