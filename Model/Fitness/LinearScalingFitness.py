#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_fitness(population,fitness_options):
    alpha_linear_scaling_fitness = fitness_options["alpha_linear_scaling_fitness"]
    beta = fitness_options["beta_linear_scaling_fitness"]
    total_fitness = 0.0
    for individual in population.get_individuals():
        current_fitness = alpha_linear_scaling_fitness*individual.get_pareto_dominates() + beta
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness 
     
    
    population.set_total_fitness(total_fitness)
    population.calculate_population_properties() 
