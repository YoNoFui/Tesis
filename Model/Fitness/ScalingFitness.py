#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

falta ver como se modifica el get_evaluated
def assign_scaling_fitness(population,fitness_options):
    alpha = fitness_options[0]
    beta = fitness_options[1]
    total_fitness = 0
    for individual in population.get_individuals():
        current_fitness = alpha*individual.get_evaluated_function(x) + beta
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness 
     
    
    population.set_total_fitness(total_fitness)
    population.calculate_population_properties() 
